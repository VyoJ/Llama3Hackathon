Title: Multi-Document Agents (V1) - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/multi_document_agents-v1/

Markdown Content:
Multi-Document Agents (V1) - LlamaIndex


In this guide, you learn towards setting up a multi-document agent over the LlamaIndex documentation.

This is an extension of V0 multi-document agents with the additional features:

*   Reranking during document (tool) retrieval
*   Query planning tool that the agent can use to plan

We do this with the following architecture:

*   setup a "document agent" over each Document: each doc agent can do QA/summarization within its doc
*   setup a top-level agent over this set of document agents. Do tool retrieval and then do CoT over the set of tools to answer a question.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-core
%pip install llama\-index\-agent\-openai
%pip install llama\-index\-readers\-file
%pip install llama\-index\-postprocessor\-cohere\-rerank
%pip install llama\-index\-llms\-openai
%pip install llama\-index\-embeddings\-openai
%pip install unstructured\[html\]

%pip install llama-index-core %pip install llama-index-agent-openai %pip install llama-index-readers-file %pip install llama-index-postprocessor-cohere-rerank %pip install llama-index-llms-openai %pip install llama-index-embeddings-openai %pip install unstructured\[html\]

In \[ \]:

Copied!

%load\_ext autoreload
%autoreload 2

%load\_ext autoreload %autoreload 2

Setup and Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/agent/multi_document_agents-v1/#setup-and-download-data)
---------------------------------------------------------------------------------------------------------------------------------

In this section, we'll load in the LlamaIndex documentation.

In \[ \]:

Copied!

domain \= "docs.llamaindex.ai"
docs\_url \= "https://docs.llamaindex.ai/en/latest/"
!wget \-e robots\=off \--recursive \--no\-clobber \--page\-requisites \--html\-extension \--convert\-links \--restrict\-file\-names\=windows \--domains {domain} \--no\-parent {docs\_url}

domain = "docs.llamaindex.ai" docs\_url = "https://docs.llamaindex.ai/en/latest/" !wget -e robots=off --recursive --no-clobber --page-requisites --html-extension --convert-links --restrict-file-names=windows --domains {domain} --no-parent {docs\_url}

In \[ \]:

Copied!

from llama\_index.readers.file import UnstructuredReader

reader \= UnstructuredReader()

from llama\_index.readers.file import UnstructuredReader reader = UnstructuredReader()

In \[ \]:

Copied!

from pathlib import Path

all\_files\_gen \= Path("./docs.llamaindex.ai/").rglob("\*")
all\_files \= \[f.resolve() for f in all\_files\_gen\]

from pathlib import Path all\_files\_gen = Path("./docs.llamaindex.ai/").rglob("\*") all\_files = \[f.resolve() for f in all\_files\_gen\]

In \[ \]:

Copied!

all\_html\_files \= \[f for f in all\_files if f.suffix.lower() \ ".html"\]

In \[ \]:

Copied!

len(all\_html\_files)

len(all\_html\_files)

Out\[ \]:

1219

In \[ \]:

Copied!

from llama\_index.core import Document

\# TODO: set to higher value if you want more docs
doc\_limit \= 100

docs \= \[\]
for idx, f in enumerate(all\_html\_files):
    if idx \> doc\_limit:
        break
    print(f"Idx {idx}/{len(all\_html\_files)}")
    loaded\_docs \= reader.load\_data(file\=f, split\_documents\=True)
    \# Hardcoded Index. Everything before this is ToC for all pages
    start\_idx \= 72
    loaded\_doc \= Document(
        text\="\\n\\n".join(\[d.get\_content() for d in loaded\_docs\[72:\]\]),
        metadata\={"path": str(f)},
    )
    print(loaded\_doc.metadata\["path"\])
    docs.append(loaded\_doc)

from llama\_index.core import Document # TODO: set to higher value if you want more docs doc\_limit = 100 docs = \[\] for idx, f in enumerate(all\_html\_files): if idx > doc\_limit: break print(f"Idx {idx}/{len(all\_html\_files)}") loaded\_docs = reader.load\_data(file=f, split\_documents=True) # Hardcoded Index. Everything before this is ToC for all pages start\_idx = 72 loaded\_doc = Document( text="\\n\\n".join(\[d.get\_content() for d in loaded\_docs\[72:\]\]), metadata={"path": str(f)}, ) print(loaded\_doc.metadata\["path"\]) docs.append(loaded\_doc)

Define Global LLM + Embeddings

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import nest\_asyncio

nest\_asyncio.apply()

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..." import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI
from llama\_index.embeddings.openai import OpenAIEmbedding
from llama\_index.core import Settings

llm \= OpenAI(model\="gpt-3.5-turbo")
Settings.llm \= llm
Settings.embed\_model \= OpenAIEmbedding(
    model\="text-embedding-3-small", embed\_batch\_size\=256
)

from llama\_index.llms.openai import OpenAI from llama\_index.embeddings.openai import OpenAIEmbedding from llama\_index.core import Settings llm = OpenAI(model="gpt-3.5-turbo") Settings.llm = llm Settings.embed\_model = OpenAIEmbedding( model="text-embedding-3-small", embed\_batch\_size=256 )

Building Multi-Document Agents[¶](https://docs.llamaindex.ai/en/stable/examples/agent/multi_document_agents-v1/#building-multi-document-agents)
-----------------------------------------------------------------------------------------------------------------------------------------------

In this section we show you how to construct the multi-document agent. We first build a document agent for each document, and then define the top-level parent agent with an object index.

### Build Document Agent for each Document[¶](https://docs.llamaindex.ai/en/stable/examples/agent/multi_document_agents-v1/#build-document-agent-for-each-document)

In this section we define "document agents" for each document.

We define both a vector index (for semantic search) and summary index (for summarization) for each document. The two query engines are then converted into tools that are passed to an OpenAI function calling agent.

This document agent can dynamically choose to perform semantic search or summarization within a given document.

We create a separate document agent for each city.

In \[ \]:

Copied!

from llama\_index.agent.openai import OpenAIAgent
from llama\_index.core import (
    load\_index\_from\_storage,
    StorageContext,
    VectorStoreIndex,
)
from llama\_index.core import SummaryIndex
from llama\_index.core.tools import QueryEngineTool, ToolMetadata
from llama\_index.core.node\_parser import SentenceSplitter
import os
from tqdm.notebook import tqdm
import pickle

async def build\_agent\_per\_doc(nodes, file\_base):
    print(file\_base)

    vi\_out\_path \= f"./data/llamaindex\_docs/{file\_base}"
    summary\_out\_path \= f"./data/llamaindex\_docs/{file\_base}\_summary.pkl"
    if not os.path.exists(vi\_out\_path):
        Path("./data/llamaindex\_docs/").mkdir(parents\=True, exist\_ok\=True)
        \# build vector index
        vector\_index \= VectorStoreIndex(nodes)
        vector\_index.storage\_context.persist(persist\_dir\=vi\_out\_path)
    else:
        vector\_index \= load\_index\_from\_storage(
            StorageContext.from\_defaults(persist\_dir\=vi\_out\_path),
        )

    \# build summary index
    summary\_index \= SummaryIndex(nodes)

    \# define query engines
    vector\_query\_engine \= vector\_index.as\_query\_engine(llm\=llm)
    summary\_query\_engine \= summary\_index.as\_query\_engine(
        response\_mode\="tree\_summarize", llm\=llm
    )

    \# extract a summary
    if not os.path.exists(summary\_out\_path):
        Path(summary\_out\_path).parent.mkdir(parents\=True, exist\_ok\=True)
        summary \= str(
            await summary\_query\_engine.aquery(
                "Extract a concise 1-2 line summary of this document"
            )
        )
        pickle.dump(summary, open(summary\_out\_path, "wb"))
    else:
        summary \= pickle.load(open(summary\_out\_path, "rb"))

    \# define tools
    query\_engine\_tools \= \[
        QueryEngineTool(
            query\_engine\=vector\_query\_engine,
            metadata\=ToolMetadata(
                name\=f"vector\_tool\_{file\_base}",
                description\=f"Useful for questions related to specific facts",
            ),
        ),
        QueryEngineTool(
            query\_engine\=summary\_query\_engine,
            metadata\=ToolMetadata(
                name\=f"summary\_tool\_{file\_base}",
                description\=f"Useful for summarization questions",
            ),
        ),
    \]

    \# build agent
    function\_llm \= OpenAI(model\="gpt-4")
    agent \= OpenAIAgent.from\_tools(
        query\_engine\_tools,
        llm\=function\_llm,
        verbose\=True,
        system\_prompt\=f"""\\
You are a specialized agent designed to answer queries about the \`{file\_base}.html\` part of the LlamaIndex docs.
You must ALWAYS use at least one of the tools provided when answering a question; do NOT rely on prior knowledge.\\
""",
    )

    return agent, summary

async def build\_agents(docs):
    node\_parser \= SentenceSplitter()

    \# Build agents dictionary
    agents\_dict \= {}
    extra\_info\_dict \= {}

    \# # this is for the baseline
    \# all\_nodes = \[\]

    for idx, doc in enumerate(tqdm(docs)):
        nodes \= node\_parser.get\_nodes\_from\_documents(\[doc\])
        \# all\_nodes.extend(nodes)

        \# ID will be base + parent
        file\_path \= Path(doc.metadata\["path"\])
        file\_base \= str(file\_path.parent.stem) + "\_" + str(file\_path.stem)
        agent, summary \= await build\_agent\_per\_doc(nodes, file\_base)

        agents\_dict\[file\_base\] \= agent
        extra\_info\_dict\[file\_base\] \= {"summary": summary, "nodes": nodes}

    return agents\_dict, extra\_info\_dict

from llama\_index.agent.openai import OpenAIAgent from llama\_index.core import ( load\_index\_from\_storage, StorageContext, VectorStoreIndex, ) from llama\_index.core import SummaryIndex from llama\_index.core.tools import QueryEngineTool, ToolMetadata from llama\_index.core.node\_parser import SentenceSplitter import os from tqdm.notebook import tqdm import pickle async def build\_agent\_per\_doc(nodes, file\_base): print(file\_base) vi\_out\_path = f"./data/llamaindex\_docs/{file\_base}" summary\_out\_path = f"./data/llamaindex\_docs/{file\_base}\_summary.pkl" if not os.path.exists(vi\_out\_path): Path("./data/llamaindex\_docs/").mkdir(parents=True, exist\_ok=True) # build vector index vector\_index = VectorStoreIndex(nodes) vector\_index.storage\_context.persist(persist\_dir=vi\_out\_path) else: vector\_index = load\_index\_from\_storage( StorageContext.from\_defaults(persist\_dir=vi\_out\_path), ) # build summary index summary\_index = SummaryIndex(nodes) # define query engines vector\_query\_engine = vector\_index.as\_query\_engine(llm=llm) summary\_query\_engine = summary\_index.as\_query\_engine( response\_mode="tree\_summarize", llm=llm ) # extract a summary if not os.path.exists(summary\_out\_path): Path(summary\_out\_path).parent.mkdir(parents=True, exist\_ok=True) summary = str( await summary\_query\_engine.aquery( "Extract a concise 1-2 line summary of this document" ) ) pickle.dump(summary, open(summary\_out\_path, "wb")) else: summary = pickle.load(open(summary\_out\_path, "rb")) # define tools query\_engine\_tools = \[ QueryEngineTool( query\_engine=vector\_query\_engine, metadata=ToolMetadata( name=f"vector\_tool\_{file\_base}", description=f"Useful for questions related to specific facts", ), ), QueryEngineTool( query\_engine=summary\_query\_engine, metadata=ToolMetadata( name=f"summary\_tool\_{file\_base}", description=f"Useful for summarization questions", ), ), \] # build agent function\_llm = OpenAI(model="gpt-4") agent = OpenAIAgent.from\_tools( query\_engine\_tools, llm=function\_llm, verbose=True, system\_prompt=f"""\\ You are a specialized agent designed to answer queries about the \`{file\_base}.html\` part of the LlamaIndex docs. You must ALWAYS use at least one of the tools provided when answering a question; do NOT rely on prior knowledge.\\ """, ) return agent, summary async def build\_agents(docs): node\_parser = SentenceSplitter() # Build agents dictionary agents\_dict = {} extra\_info\_dict = {} # # this is for the baseline # all\_nodes = \[\] for idx, doc in enumerate(tqdm(docs)): nodes = node\_parser.get\_nodes\_from\_documents(\[doc\]) # all\_nodes.extend(nodes) # ID will be base + parent file\_path = Path(doc.metadata\["path"\]) file\_base = str(file\_path.parent.stem) + "\_" + str(file\_path.stem) agent, summary = await build\_agent\_per\_doc(nodes, file\_base) agents\_dict\[file\_base\] = agent extra\_info\_dict\[file\_base\] = {"summary": summary, "nodes": nodes} return agents\_dict, extra\_info\_dict

In \[ \]:

Copied!

agents\_dict, extra\_info\_dict \= await build\_agents(docs)

agents\_dict, extra\_info\_dict = await build\_agents(docs)

### Build Retriever-Enabled OpenAI Agent[¶](https://docs.llamaindex.ai/en/stable/examples/agent/multi_document_agents-v1/#build-retriever-enabled-openai-agent)

We build a top-level agent that can orchestrate across the different document agents to answer any user query.

This `RetrieverOpenAIAgent` performs tool retrieval before tool use (unlike a default agent that tries to put all tools in the prompt).

**Improvements from V0**: We make the following improvements compared to the "base" version in V0.

*   Adding in reranking: we use Cohere reranker to better filter the candidate set of documents.
*   Adding in a query planning tool: we add an explicit query planning tool that's dynamically created based on the set of retrieved tools.

In \[ \]:

Copied!

\# define tool for each document agent
all\_tools \= \[\]
for file\_base, agent in agents\_dict.items():
    summary \= extra\_info\_dict\[file\_base\]\["summary"\]
    doc\_tool \= QueryEngineTool(
        query\_engine\=agent,
        metadata\=ToolMetadata(
            name\=f"tool\_{file\_base}",
            description\=summary,
        ),
    )
    all\_tools.append(doc\_tool)

\# define tool for each document agent all\_tools = \[\] for file\_base, agent in agents\_dict.items(): summary = extra\_info\_dict\[file\_base\]\["summary"\] doc\_tool = QueryEngineTool( query\_engine=agent, metadata=ToolMetadata( name=f"tool\_{file\_base}", description=summary, ), ) all\_tools.append(doc\_tool)

In \[ \]:

Copied!

print(all\_tools\[0\].metadata)

print(all\_tools\[0\].metadata)

ToolMetadata(description='This document provides examples and documentation for an agent on the llama index platform.', name='tool\_latest\_index', fn\_schema=<class 'llama\_index.core.tools.types.DefaultToolFnSchema'>)

In \[ \]:

Copied!

\# define an "object" index and retriever over these tools
from llama\_index.core import VectorStoreIndex
from llama\_index.core.objects import (
    ObjectIndex,
    ObjectRetriever,
)
from llama\_index.postprocessor.cohere\_rerank import CohereRerank
from llama\_index.core.query\_engine import SubQuestionQueryEngine
from llama\_index.core.schema import QueryBundle
from llama\_index.llms.openai import OpenAI

llm \= OpenAI(model\_name\="gpt-4-0613")

obj\_index \= ObjectIndex.from\_objects(
    all\_tools,
    index\_cls\=VectorStoreIndex,
)
vector\_node\_retriever \= obj\_index.as\_node\_retriever(
    similarity\_top\_k\=10,
)

\# define a custom object retriever that adds in a query planning tool
class CustomObjectRetriever(ObjectRetriever):
    def \_\_init\_\_(
        self,
        retriever,
        object\_node\_mapping,
        node\_postprocessors\=None,
        llm\=None,
    ):
        self.\_retriever \= retriever
        self.\_object\_node\_mapping \= object\_node\_mapping
        self.\_llm \= llm or OpenAI("gpt-4-0613")
        self.\_node\_postprocessors \= node\_postprocessors or \[\]

    def retrieve(self, query\_bundle):
        if isinstance(query\_bundle, str):
            query\_bundle \= QueryBundle(query\_str\=query\_bundle)

        nodes \= self.\_retriever.retrieve(query\_bundle)
        for processor in self.\_node\_postprocessors:
            nodes \= processor.postprocess\_nodes(
                nodes, query\_bundle\=query\_bundle
            )
        tools \= \[self.\_object\_node\_mapping.from\_node(n.node) for n in nodes\]

        sub\_question\_engine \= SubQuestionQueryEngine.from\_defaults(
            query\_engine\_tools\=tools, llm\=self.\_llm
        )
        sub\_question\_description \= f"""\\
Useful for any queries that involve comparing multiple documents. ALWAYS use this tool for comparison queries - make sure to call this \\
tool with the original query. Do NOT use the other tools for any queries involving multiple documents.
"""
        sub\_question\_tool \= QueryEngineTool(
            query\_engine\=sub\_question\_engine,
            metadata\=ToolMetadata(
                name\="compare\_tool", description\=sub\_question\_description
            ),
        )

        return tools + \[sub\_question\_tool\]

\# define an "object" index and retriever over these tools from llama\_index.core import VectorStoreIndex from llama\_index.core.objects import ( ObjectIndex, ObjectRetriever, ) from llama\_index.postprocessor.cohere\_rerank import CohereRerank from llama\_index.core.query\_engine import SubQuestionQueryEngine from llama\_index.core.schema import QueryBundle from llama\_index.llms.openai import OpenAI llm = OpenAI(model\_name="gpt-4-0613") obj\_index = ObjectIndex.from\_objects( all\_tools, index\_cls=VectorStoreIndex, ) vector\_node\_retriever = obj\_index.as\_node\_retriever( similarity\_top\_k=10, ) # define a custom object retriever that adds in a query planning tool class CustomObjectRetriever(ObjectRetriever): def \_\_init\_\_( self, retriever, object\_node\_mapping, node\_postprocessors=None, llm=None, ): self.\_retriever = retriever self.\_object\_node\_mapping = object\_node\_mapping self.\_llm = llm or OpenAI("gpt-4-0613") self.\_node\_postprocessors = node\_postprocessors or \[\] def retrieve(self, query\_bundle): if isinstance(query\_bundle, str): query\_bundle = QueryBundle(query\_str=query\_bundle) nodes = self.\_retriever.retrieve(query\_bundle) for processor in self.\_node\_postprocessors: nodes = processor.postprocess\_nodes( nodes, query\_bundle=query\_bundle ) tools = \[self.\_object\_node\_mapping.from\_node(n.node) for n in nodes\] sub\_question\_engine = SubQuestionQueryEngine.from\_defaults( query\_engine\_tools=tools, llm=self.\_llm ) sub\_question\_description = f"""\\ Useful for any queries that involve comparing multiple documents. ALWAYS use this tool for comparison queries - make sure to call this \\ tool with the original query. Do NOT use the other tools for any queries involving multiple documents. """ sub\_question\_tool = QueryEngineTool( query\_engine=sub\_question\_engine, metadata=ToolMetadata( name="compare\_tool", description=sub\_question\_description ), ) return tools + \[sub\_question\_tool\]

In \[ \]:

Copied!

\# wrap it with ObjectRetriever to return objects
custom\_obj\_retriever \= CustomObjectRetriever(
    vector\_node\_retriever,
    obj\_index.object\_node\_mapping,
    node\_postprocessors\=\[CohereRerank(top\_n\=5)\],
    llm\=llm,
)

\# wrap it with ObjectRetriever to return objects custom\_obj\_retriever = CustomObjectRetriever( vector\_node\_retriever, obj\_index.object\_node\_mapping, node\_postprocessors=\[CohereRerank(top\_n=5)\], llm=llm, )

In \[ \]:

Copied!

tmps \= custom\_obj\_retriever.retrieve("hello")

\# should be 5 + 1 -- 5 from reranker, 1 from subquestion
print(len(tmps))

tmps = custom\_obj\_retriever.retrieve("hello") # should be 5 + 1 -- 5 from reranker, 1 from subquestion print(len(tmps))

6

In \[ \]:

Copied!

from llama\_index.agent.openai import OpenAIAgent
from llama\_index.core.agent import ReActAgent

top\_agent \= OpenAIAgent.from\_tools(
    tool\_retriever\=custom\_obj\_retriever,
    system\_prompt\=""" \\
You are an agent designed to answer queries about the documentation.
Please always use the tools provided to answer a question. Do not rely on prior knowledge.\\

""",
    llm\=llm,
    verbose\=True,
)

\# top\_agent = ReActAgent.from\_tools(
\#     tool\_retriever=custom\_obj\_retriever,
\#     system\_prompt=""" \\
\# You are an agent designed to answer queries about the documentation.
\# Please always use the tools provided to answer a question. Do not rely on prior knowledge.\\

\# """,
\#     llm=llm,
\#     verbose=True,
\# )

from llama\_index.agent.openai import OpenAIAgent from llama\_index.core.agent import ReActAgent top\_agent = OpenAIAgent.from\_tools( tool\_retriever=custom\_obj\_retriever, system\_prompt=""" \\ You are an agent designed to answer queries about the documentation. Please always use the tools provided to answer a question. Do not rely on prior knowledge.\\ """, llm=llm, verbose=True, ) # top\_agent = ReActAgent.from\_tools( # tool\_retriever=custom\_obj\_retriever, # system\_prompt=""" \\ # You are an agent designed to answer queries about the documentation. # Please always use the tools provided to answer a question. Do not rely on prior knowledge.\\ # """, # llm=llm, # verbose=True, # )

### Define Baseline Vector Store Index[¶](https://docs.llamaindex.ai/en/stable/examples/agent/multi_document_agents-v1/#define-baseline-vector-store-index)

As a point of comparison, we define a "naive" RAG pipeline which dumps all docs into a single vector index collection.

We set the top\_k = 4

In \[ \]:

Copied!

all\_nodes \= \[
    n for extra\_info in extra\_info\_dict.values() for n in extra\_info\["nodes"\]
\]

all\_nodes = \[ n for extra\_info in extra\_info\_dict.values() for n in extra\_info\["nodes"\] \]

In \[ \]:

Copied!

base\_index \= VectorStoreIndex(all\_nodes)
base\_query\_engine \= base\_index.as\_query\_engine(similarity\_top\_k\=4)

base\_index = VectorStoreIndex(all\_nodes) base\_query\_engine = base\_index.as\_query\_engine(similarity\_top\_k=4)

Running Example Queries[¶](https://docs.llamaindex.ai/en/stable/examples/agent/multi_document_agents-v1/#running-example-queries)
---------------------------------------------------------------------------------------------------------------------------------

Let's run some example queries, ranging from QA / summaries over a single document to QA / summarization over multiple documents.

In \[ \]:

Copied!

response \= top\_agent.query(
    "What types of agents are available in LlamaIndex?",
)

response = top\_agent.query( "What types of agents are available in LlamaIndex?", )

Added user message to memory: What types of agents are available in LlamaIndex?

Calling function: tool\_agents\_index with args: {"input":"types of agents"}
Added user message to memory: types of agents

Calling function: vector\_tool\_agents\_index with args: {
  "input": "types of agents"
}
Got output: The types of agents mentioned in the provided context are ReActAgent, Native OpenAIAgent, OpenAIAgent with Query Engine Tools, OpenAIAgent Query Planning, OpenAI Assistant, OpenAI Assistant Cookbook, Forced Function Calling, Parallel Function Calling, and Context Retrieval.


In \[ \]:

Copied!

print(response)

print(response)

The types of agents available in LlamaIndex include ReActAgent, Native OpenAIAgent, OpenAIAgent with Query Engine Tools, OpenAIAgent Query Planning, OpenAI Assistant, OpenAI Assistant Cookbook, Forced Function Calling, Parallel Function Calling, and Context Retrieval.

In \[ \]:

Copied!

\# baseline
response \= base\_query\_engine.query(
    "What types of agents are available in LlamaIndex?",
)
print(str(response))

\# baseline response = base\_query\_engine.query( "What types of agents are available in LlamaIndex?", ) print(str(response))

The types of agents available in LlamaIndex are ReActAgent, Native OpenAIAgent, and OpenAIAgent.

In \[ \]:

Copied!

response \= top\_agent.query(
    "Compare the content in the agents page vs. tools page."
)

response = top\_agent.query( "Compare the content in the agents page vs. tools page." )

Added user message to memory: Compare the content in the agents page vs. tools page.

Calling function: compare\_tool with args: {"input":"agents vs tools"}
Generated 2 sub questions.
\[tool\_understanding\_index\] Q: What are the functionalities of agents in the Llama Index platform?
Added user message to memory: What are the functionalities of agents in the Llama Index platform?
\[tool\_understanding\_index\] Q: How do agents differ from tools in the Llama Index platform?
Added user message to memory: How do agents differ from tools in the Llama Index platform?

Calling function: vector\_tool\_understanding\_index with args: {
  "input": "difference between agents and tools"
}

Calling function: vector\_tool\_understanding\_index with args: {
  "input": "functionalities of agents"
}
Got output: Agents are typically individuals or entities that act on behalf of others, making decisions and taking actions based on predefined rules or instructions. On the other hand, tools are instruments or devices used to carry out specific functions or tasks, often under the control or direction of an agent.


\[tool\_understanding\_index\] A: In the context of the Llama Index platform, agents are entities that make decisions and take actions based on predefined rules or instructions. They are designed to interact with users, understand their queries, and provide appropriate responses. 

On the other hand, tools are instruments or devices that are used to perform specific functions or tasks. They are typically controlled or directed by an agent and do not make decisions on their own. They are used to assist the agents in providing accurate and relevant responses to user queries.
\[tool\_understanding\_index\] A: In the Llama Index platform, agents have a variety of functionalities. They can perform tasks autonomously or semi-autonomously. These tasks include data collection and analysis, making decisions, communicating with other systems or users, and executing specific actions. These actions are based on predefined rules or algorithms.
Got output: Agents in the Llama Index platform are responsible for making decisions and taking actions based on predefined rules or instructions. They interact with users, understand queries, and provide appropriate responses. On the other hand, tools in the platform are instruments or devices used to perform specific functions or tasks. Unlike agents, tools are typically controlled or directed by an agent and do not make decisions independently. Their role is to assist agents in delivering accurate and relevant responses to user queries.
 Calling Function  Calling Function  Calling Function  Calling Function  Calling Function 

Got output: The response mode "tree\_summarize" in the response synthesizer configures the system to recursively construct a tree from a set of Node objects and the query, returning the root node as the final response. This mode is particularly useful for summarization purposes.



Calling function: summary\_tool\_querying\_index with args: {
  "input": "compact vs tree\_summarize response synthesizer response modes"
}
Got output: Response synthesizer response modes can be evaluated by comparing what was retrieved for a query to a set of nodes that were expected to be retrieved. This evaluation process typically involves analyzing metrics such as Mean Reciprocal Rank (MRR) and Hit Rate. It is important to evaluate a batch of retrievals to get a comprehensive understanding of the performance. If you are making calls to a hosted, remote LLM, you may also want to consider analyzing the cost implications of your application.


\[tool\_querying\_index\] A: The compact response synthesizer response mode optimizes query logic and response quality by compacting the prompt during each LLM call. It does this by stuffing as many Node text chunks that can fit within the maximum prompt size. If there are too many chunks to fit in one prompt, it will "create and refine" an answer by going through multiple prompts. This approach allows for a more efficient use of the prompt space and can lead to more refined and accurate responses.
\[tool\_querying\_index\] A: The "tree\_summarize" response synthesizer response mode optimizes query logic and response quality by recursively constructing a tree from a set of Node objects and the query. This approach allows the system to handle complex queries and generate comprehensive responses. The root node, which is returned as the final response, contains a summarized version of the information, making it easier for users to understand the response. This mode is particularly useful for summarization purposes, where the goal is to provide a concise yet comprehensive answer to a query.
\[tool\_evaluating\_index\] A: When evaluating retrievals in the context of response synthesizer response modes, you should compare what was retrieved for a query to a set of nodes that were expected to be retrieved. This evaluation process typically involves analyzing metrics such as Mean Reciprocal Rank (MRR) and Hit Rate. It's crucial to evaluate a batch of retrievals to get a comprehensive understanding of the performance. If you are making calls to a hosted, remote LLM, you may also want to consider analyzing the cost implications of your application.
\[tool\_querying\_index\] A: The "compact" and "tree\_summarize" are two different response modes for the response synthesizer in LlamaIndex. 

The "compact" mode provides a more concise response, focusing on delivering the most relevant information in a compact format. This mode is useful when you want a brief and direct answer to your query.

On the other hand, the "tree\_summarize" mode provides a more detailed and structured response. It breaks down the information into a tree-like structure, making it easier to understand the relationships and hierarchy of the information. This mode is useful when you want a comprehensive understanding of the query topic.
Got output: The "compact" response synthesizer mode focuses on providing a concise and direct response, while the "tree\_summarize" mode offers a more detailed and structured response by breaking down information into a tree-like structure. The compact mode aims to deliver the most relevant information in a compact format, suitable for brief answers, whereas the tree\_summarize mode is designed to provide a comprehensive understanding of the query topic by presenting information in a hierarchical manner.


In \[ \]:

Copied!

print(str(response))

print(str(response))

The "compact" response synthesizer mode provides concise and direct responses, while the "tree\_summarize" mode offers detailed and structured responses in a tree-like format. The compact mode is suitable for brief answers, while the tree\_summarize mode presents information hierarchically for a comprehensive understanding of the query topic.

Back to top

[Previous Function Calling Mistral Agent](https://docs.llamaindex.ai/en/stable/examples/agent/mistral_agent/)[Next Multi-Document Agents](https://docs.llamaindex.ai/en/stable/examples/agent/multi_document_agents/)

Hi, how can I help you?

🦙
