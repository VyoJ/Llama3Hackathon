Title: Query Pipeline Chat Engine - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_memory/

Markdown Content:
Query Pipeline Chat Engine - LlamaIndex


By combining a query pipeline with a memory buffer, we can design our own custom chat engine loop.

In \[ \]:

Copied!

%pip install llama\-index\-core
%pip install llama\-index\-llms\-openai
%pip install llama\-index\-embeddings\-openai
%pip install llama\-index\-postprocessor\-colbert\-rerank
%pip install llama\-index\-readers\-web

%pip install llama-index-core %pip install llama-index-llms-openai %pip install llama-index-embeddings-openai %pip install llama-index-postprocessor-colbert-rerank %pip install llama-index-readers-web

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..."

Index Construction[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_memory/#index-construction)
-----------------------------------------------------------------------------------------------------------------------

As a test, we will index Anthropic's latest documentation about tool/function calling.

In \[ \]:

Copied!

from llama\_index.readers.web import BeautifulSoupWebReader

reader \= BeautifulSoupWebReader()

documents \= reader.load\_data(
    \["https://docs.anthropic.com/claude/docs/tool-use"\]
)

from llama\_index.readers.web import BeautifulSoupWebReader reader = BeautifulSoupWebReader() documents = reader.load\_data( \["https://docs.anthropic.com/claude/docs/tool-use"\] )

If you inspected the document text, you'd notice that there are way too many blank lines, lets clean that up a bit.

In \[ \]:

Copied!

lines \= documents\[0\].text.split("\\n")

\# remove sections with more than two empty lines in a row
fixed\_lines \= \[lines\[0\]\]
for idx in range(1, len(lines)):
    if lines\[idx\].strip() \ "":
        continue
    fixed\_lines.append(lines\[idx\])

documents\[0\].text \= "\\n".join(fixed\_lines)

lines = documents\[0\].text.split("\\n") # remove sections with more than two empty lines in a row fixed\_lines = \[lines\[0\]\] for idx in range(1, len(lines)): if lines\[idx\].strip()  "": continue fixed\_lines.append(lines\[idx\]) documents\[0\].text = "\\n".join(fixed\_lines)

Now, we can create our index using OpenAI embeddings.

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex
from llama\_index.embeddings.openai import OpenAIEmbedding

index \= VectorStoreIndex.from\_documents(
    documents,
    embed\_model\=OpenAIEmbedding(
        model\="text-embedding-3-large", embed\_batch\_size\=256
    ),
)

from llama\_index.core import VectorStoreIndex from llama\_index.embeddings.openai import OpenAIEmbedding index = VectorStoreIndex.from\_documents( documents, embed\_model=OpenAIEmbedding( model="text-embedding-3-large", embed\_batch\_size=256 ), )

Query Pipeline Contruction[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_memory/#query-pipeline-contruction)
---------------------------------------------------------------------------------------------------------------------------------------

As a demonstration, lets make a robust query pipeline with HyDE for retrieval and Colbert for reranking.

In \[ \]:

Copied!

from llama\_index.core.query\_pipeline import (
    QueryPipeline,
    InputComponent,
    ArgPackComponent,
)
from llama\_index.core.prompts import PromptTemplate
from llama\_index.llms.openai import OpenAI
from llama\_index.postprocessor.colbert\_rerank import ColbertRerank

\# First, we create an input component to capture the user query
input\_component \= InputComponent()

\# Next, we use the LLM to rewrite a user query
rewrite \= (
    "Please write a query to a semantic search engine using the current conversation.\\n"
    "\\n"
    "\\n"
    "{chat\_history\_str}"
    "\\n"
    "\\n"
    "Latest message: {query\_str}\\n"
    'Query:"""\\n'
)
rewrite\_template \= PromptTemplate(rewrite)
llm \= OpenAI(
    model\="gpt-4-turbo-preview",
    temperature\=0.2,
)

\# we will retrieve two times, so we need to pack the retrieved nodes into a single list
argpack\_component \= ArgPackComponent()

\# using that, we will retrieve...
retriever \= index.as\_retriever(similarity\_top\_k\=6)

\# then postprocess/rerank with Colbert
reranker \= ColbertRerank(top\_n\=3)

from llama\_index.core.query\_pipeline import ( QueryPipeline, InputComponent, ArgPackComponent, ) from llama\_index.core.prompts import PromptTemplate from llama\_index.llms.openai import OpenAI from llama\_index.postprocessor.colbert\_rerank import ColbertRerank # First, we create an input component to capture the user query input\_component = InputComponent() # Next, we use the LLM to rewrite a user query rewrite = ( "Please write a query to a semantic search engine using the current conversation.\\n" "\\n" "\\n" "{chat\_history\_str}" "\\n" "\\n" "Latest message: {query\_str}\\n" 'Query:"""\\n' ) rewrite\_template = PromptTemplate(rewrite) llm = OpenAI( model="gpt-4-turbo-preview", temperature=0.2, ) # we will retrieve two times, so we need to pack the retrieved nodes into a single list argpack\_component = ArgPackComponent() # using that, we will retrieve... retriever = index.as\_retriever(similarity\_top\_k=6) # then postprocess/rerank with Colbert reranker = ColbertRerank(top\_n=3)

For generating a response using chat history + retrieved nodes, lets create a custom component.

In \[ \]:

Copied!

\# then lastly, we need to create a response using the nodes AND chat history
from typing import Any, Dict, List, Optional
from llama\_index.core.bridge.pydantic import Field
from llama\_index.core.llms import ChatMessage
from llama\_index.core.query\_pipeline import CustomQueryComponent
from llama\_index.core.schema import NodeWithScore

DEFAULT\_CONTEXT\_PROMPT \= (
    "Here is some context that may be relevant:\\n"
    "-----\\n"
    "{node\_context}\\n"
    "-----\\n"
    "Please write a response to the following question, using the above context:\\n"
    "{query\_str}\\n"
)

class ResponseWithChatHistory(CustomQueryComponent):
    llm: OpenAI \= Field(..., description\="OpenAI LLM")
    system\_prompt: Optional\[str\] \= Field(
        default\=None, description\="System prompt to use for the LLM"
    )
    context\_prompt: str \= Field(
        default\=DEFAULT\_CONTEXT\_PROMPT,
        description\="Context prompt to use for the LLM",
    )

    def \_validate\_component\_inputs(
        self, input: Dict\[str, Any\]
    ) \-> Dict\[str, Any\]:
        """Validate component inputs during run\_component."""
        \# NOTE: this is OPTIONAL but we show you where to do validation as an example
        return input

    @property
    def \_input\_keys(self) \-> set:
        """Input keys dict."""
        \# NOTE: These are required inputs. If you have optional inputs please override
        \# \`optional\_input\_keys\_dict\`
        return {"chat\_history", "nodes", "query\_str"}

    @property
    def \_output\_keys(self) \-> set:
        return {"response"}

    def \_prepare\_context(
        self,
        chat\_history: List\[ChatMessage\],
        nodes: List\[NodeWithScore\],
        query\_str: str,
    ) \-> List\[ChatMessage\]:
        node\_context \= ""
        for idx, node in enumerate(nodes):
            node\_text \= node.get\_content(metadata\_mode\="llm")
            node\_context += f"Context Chunk {idx}:\\n{node\_text}\\n\\n"

        formatted\_context \= self.context\_prompt.format(
            node\_context\=node\_context, query\_str\=query\_str
        )
        user\_message \= ChatMessage(role\="user", content\=formatted\_context)

        chat\_history.append(user\_message)

        if self.system\_prompt is not None:
            chat\_history \= \[
                ChatMessage(role\="system", content\=self.system\_prompt)
            \] + chat\_history

        return chat\_history

    def \_run\_component(self, \*\*kwargs) \-> Dict\[str, Any\]:
        """Run the component."""
        chat\_history \= kwargs\["chat\_history"\]
        nodes \= kwargs\["nodes"\]
        query\_str \= kwargs\["query\_str"\]

        prepared\_context \= self.\_prepare\_context(
            chat\_history, nodes, query\_str
        )

        response \= llm.chat(prepared\_context)

        return {"response": response}

    async def \_arun\_component(self, \*\*kwargs: Any) \-> Dict\[str, Any\]:
        """Run the component asynchronously."""
        \# NOTE: Optional, but async LLM calls are easy to implement
        chat\_history \= kwargs\["chat\_history"\]
        nodes \= kwargs\["nodes"\]
        query\_str \= kwargs\["query\_str"\]

        prepared\_context \= self.\_prepare\_context(
            chat\_history, nodes, query\_str
        )

        response \= await llm.achat(prepared\_context)

        return {"response": response}

response\_component \= ResponseWithChatHistory(
    llm\=llm,
    system\_prompt\=(
        "You are a Q&A system. You will be provided with the previous chat history, "
        "as well as possibly relevant context, to assist in answering a user message."
    ),
)

\# then lastly, we need to create a response using the nodes AND chat history from typing import Any, Dict, List, Optional from llama\_index.core.bridge.pydantic import Field from llama\_index.core.llms import ChatMessage from llama\_index.core.query\_pipeline import CustomQueryComponent from llama\_index.core.schema import NodeWithScore DEFAULT\_CONTEXT\_PROMPT = ( "Here is some context that may be relevant:\\n" "-----\\n" "{node\_context}\\n" "-----\\n" "Please write a response to the following question, using the above context:\\n" "{query\_str}\\n" ) class ResponseWithChatHistory(CustomQueryComponent): llm: OpenAI = Field(..., description="OpenAI LLM") system\_prompt: Optional\[str\] = Field( default=None, description="System prompt to use for the LLM" ) context\_prompt: str = Field( default=DEFAULT\_CONTEXT\_PROMPT, description="Context prompt to use for the LLM", ) def \_validate\_component\_inputs( self, input: Dict\[str, Any\] ) -> Dict\[str, Any\]: """Validate component inputs during run\_component.""" # NOTE: this is OPTIONAL but we show you where to do validation as an example return input @property def \_input\_keys(self) -> set: """Input keys dict.""" # NOTE: These are required inputs. If you have optional inputs please override # \`optional\_input\_keys\_dict\` return {"chat\_history", "nodes", "query\_str"} @property def \_output\_keys(self) -> set: return {"response"} def \_prepare\_context( self, chat\_history: List\[ChatMessage\], nodes: List\[NodeWithScore\], query\_str: str, ) -> List\[ChatMessage\]: node\_context = "" for idx, node in enumerate(nodes): node\_text = node.get\_content(metadata\_mode="llm") node\_context += f"Context Chunk {idx}:\\n{node\_text}\\n\\n" formatted\_context = self.context\_prompt.format( node\_context=node\_context, query\_str=query\_str ) user\_message = ChatMessage(role="user", content=formatted\_context) chat\_history.append(user\_message) if self.system\_prompt is not None: chat\_history = \[ ChatMessage(role="system", content=self.system\_prompt) \] + chat\_history return chat\_history def \_run\_component(self, \*\*kwargs) -> Dict\[str, Any\]: """Run the component.""" chat\_history = kwargs\["chat\_history"\] nodes = kwargs\["nodes"\] query\_str = kwargs\["query\_str"\] prepared\_context = self.\_prepare\_context( chat\_history, nodes, query\_str ) response = llm.chat(prepared\_context) return {"response": response} async def \_arun\_component(self, \*\*kwargs: Any) -> Dict\[str, Any\]: """Run the component asynchronously.""" # NOTE: Optional, but async LLM calls are easy to implement chat\_history = kwargs\["chat\_history"\] nodes = kwargs\["nodes"\] query\_str = kwargs\["query\_str"\] prepared\_context = self.\_prepare\_context( chat\_history, nodes, query\_str ) response = await llm.achat(prepared\_context) return {"response": response} response\_component = ResponseWithChatHistory( llm=llm, system\_prompt=( "You are a Q&A system. You will be provided with the previous chat history, " "as well as possibly relevant context, to assist in answering a user message." ), )

With our modules created, we can link them together in a query pipeline.

In \[ \]:

Copied!

pipeline \= QueryPipeline(
    modules\={
        "input": input\_component,
        "rewrite\_template": rewrite\_template,
        "llm": llm,
        "rewrite\_retriever": retriever,
        "query\_retriever": retriever,
        "join": argpack\_component,
        "reranker": reranker,
        "response\_component": response\_component,
    },
    verbose\=False,
)

\# run both retrievers -- once with the hallucinated query, once with the real query
pipeline.add\_link(
    "input", "rewrite\_template", src\_key\="query\_str", dest\_key\="query\_str"
)
pipeline.add\_link(
    "input",
    "rewrite\_template",
    src\_key\="chat\_history\_str",
    dest\_key\="chat\_history\_str",
)
pipeline.add\_link("rewrite\_template", "llm")
pipeline.add\_link("llm", "rewrite\_retriever")
pipeline.add\_link("input", "query\_retriever", src\_key\="query\_str")

\# each input to the argpack component needs a dest key -- it can be anything
\# then, the argpack component will pack all the inputs into a single list
pipeline.add\_link("rewrite\_retriever", "join", dest\_key\="rewrite\_nodes")
pipeline.add\_link("query\_retriever", "join", dest\_key\="query\_nodes")

\# reranker needs the packed nodes and the query string
pipeline.add\_link("join", "reranker", dest\_key\="nodes")
pipeline.add\_link(
    "input", "reranker", src\_key\="query\_str", dest\_key\="query\_str"
)

\# synthesizer needs the reranked nodes and query str
pipeline.add\_link("reranker", "response\_component", dest\_key\="nodes")
pipeline.add\_link(
    "input", "response\_component", src\_key\="query\_str", dest\_key\="query\_str"
)
pipeline.add\_link(
    "input",
    "response\_component",
    src\_key\="chat\_history",
    dest\_key\="chat\_history",
)

pipeline = QueryPipeline( modules={ "input": input\_component, "rewrite\_template": rewrite\_template, "llm": llm, "rewrite\_retriever": retriever, "query\_retriever": retriever, "join": argpack\_component, "reranker": reranker, "response\_component": response\_component, }, verbose=False, ) # run both retrievers -- once with the hallucinated query, once with the real query pipeline.add\_link( "input", "rewrite\_template", src\_key="query\_str", dest\_key="query\_str" ) pipeline.add\_link( "input", "rewrite\_template", src\_key="chat\_history\_str", dest\_key="chat\_history\_str", ) pipeline.add\_link("rewrite\_template", "llm") pipeline.add\_link("llm", "rewrite\_retriever") pipeline.add\_link("input", "query\_retriever", src\_key="query\_str") # each input to the argpack component needs a dest key -- it can be anything # then, the argpack component will pack all the inputs into a single list pipeline.add\_link("rewrite\_retriever", "join", dest\_key="rewrite\_nodes") pipeline.add\_link("query\_retriever", "join", dest\_key="query\_nodes") # reranker needs the packed nodes and the query string pipeline.add\_link("join", "reranker", dest\_key="nodes") pipeline.add\_link( "input", "reranker", src\_key="query\_str", dest\_key="query\_str" ) # synthesizer needs the reranked nodes and query str pipeline.add\_link("reranker", "response\_component", dest\_key="nodes") pipeline.add\_link( "input", "response\_component", src\_key="query\_str", dest\_key="query\_str" ) pipeline.add\_link( "input", "response\_component", src\_key="chat\_history", dest\_key="chat\_history", )

Lets test the pipeline to confirm it works!

Running the Pipeline with Memory[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_memory/#running-the-pipeline-with-memory)
---------------------------------------------------------------------------------------------------------------------------------------------------

The above pipeline uses two inputs -- a query string and a chat\_history list.

The query string is simply the string input/query.

The chat history list is a list of ChatMessage objects. We can use a memory module from llama-index to directly manage and create the memory!

In \[ \]:

Copied!

from llama\_index.core.memory import ChatMemoryBuffer

pipeline\_memory \= ChatMemoryBuffer.from\_defaults(token\_limit\=8000)

from llama\_index.core.memory import ChatMemoryBuffer pipeline\_memory = ChatMemoryBuffer.from\_defaults(token\_limit=8000)

Lets pre-create a "chat session" and watch it play out.

In \[ \]:

Copied!

user\_inputs \= \[
    "Hello!",
    "How does tool-use work with Claude-3 work?",
    "What models support it?",
    "Thanks, that what I needed to know!",
\]

for msg in user\_inputs:
    \# get memory
    chat\_history \= pipeline\_memory.get()

    \# prepare inputs
    chat\_history\_str \= "\\n".join(\[str(x) for x in chat\_history\])

    \# run pipeline
    response \= pipeline.run(
        query\_str\=msg,
        chat\_history\=chat\_history,
        chat\_history\_str\=chat\_history\_str,
    )

    \# update memory
    user\_msg \= ChatMessage(role\="user", content\=msg)
    pipeline\_memory.put(user\_msg)
    print(str(user\_msg))

    pipeline\_memory.put(response.message)
    print(str(response.message))
    print()

user\_inputs = \[ "Hello!", "How does tool-use work with Claude-3 work?", "What models support it?", "Thanks, that what I needed to know!", \] for msg in user\_inputs: # get memory chat\_history = pipeline\_memory.get() # prepare inputs chat\_history\_str = "\\n".join(\[str(x) for x in chat\_history\]) # run pipeline response = pipeline.run( query\_str=msg, chat\_history=chat\_history, chat\_history\_str=chat\_history\_str, ) # update memory user\_msg = ChatMessage(role="user", content=msg) pipeline\_memory.put(user\_msg) print(str(user\_msg)) pipeline\_memory.put(response.message) print(str(response.message)) print()

user: Hello!
assistant: Hello! How can I assist you today?

user: How does tool-use work with Claude-3 work?
assistant: Tool use with Claude-3 operates under a framework designed to extend the model's capabilities by integrating it with external data sources and functionalities through user-provided tools. This process involves several key steps and considerations to ensure effective tool integration and utilization. Here's a breakdown of how tool use works with Claude-3:

1. \*\*Tool Specification\*\*: Users define tools in the API request, specifying the tool's name, a detailed description of its purpose and behavior, and an input schema that outlines the expected parameters. This schema is crucial for Claude to understand when and how to use the tool correctly.

2. \*\*Decision to Use a Tool\*\*: When Claude-3 receives a user prompt that may benefit from tool use, it assesses whether any available tools can assist with the query or task. This decision is based on the context provided by the user and the detailed descriptions of the tools.

3. \*\*Tool Use Request Formation\*\*: If Claude decides to use a tool, it constructs a properly formatted tool use request. This includes selecting the appropriate tool(s) and determining the necessary inputs based on the user's prompt and the tool's input schema.

4. \*\*Execution of Tool Code\*\*: The actual execution of the tool code occurs on the client side. The system extracts the tool name and input from Claude's tool use request, runs the tool code, and then returns the results to Claude.

5. \*\*Formulating a Response\*\*: After receiving the tool results, Claude uses this information to formulate its final response to the user's original prompt. This step may involve interpreting the tool's output and integrating it into a coherent and informative answer.

6. \*\*Sequential Tool Use\*\*: Claude generally prefers using one tool at a time, using the output of one tool to inform its next action. This sequential approach helps manage dependencies between tools and simplifies the tool use process.

7. \*\*Error Handling and Retries\*\*: If a tool use request is invalid or missing required parameters, Claude can retry the request with the missing information filled in, based on error responses from the client side. However, after a few failed attempts, Claude may stop trying and apologize to the user.

8. \*\*Debugging and Improvement\*\*: Developers are encouraged to debug unexpected tool use behavior by examining Claude's chain of thought output and refining tool descriptions and schemas for clarity and comprehensiveness.

By adhering to these steps and best practices, developers can effectively integrate and utilize tools with Claude-3, significantly expanding its capabilities beyond its base knowledge. This framework allows for the creation of complex, agentic orchestrations where Claude can perform a wide variety of tasks, from simple data retrieval to more complex problem-solving scenarios.

user: What models support it?
assistant: The tool use feature, as described in the provided context, is supported by Claude-3 models, including specific versions like Claude-3 Opus and Haiku. These models are designed to interact with external client-side tools and functions, allowing for a wide variety of tasks to be performed by equipping Claude with custom tools. The context specifically mentions Claude-3 Opus as being capable of handling more complex tool use scenarios, including managing multiple tools simultaneously and better catching missing arguments. Haiku is mentioned for dealing with more straightforward tools, inferring missing parameters when they are not explicitly given.

user: Thanks, that what I needed to know!
assistant: You're welcome! If you have any more questions or need further assistance, feel free to ask. Happy to help!

Back to top

[Previous Query Pipeline with Async/Parallel Execution](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_async/)[Next Query Pipeline over Pandas DataFrames](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_pandas/)
