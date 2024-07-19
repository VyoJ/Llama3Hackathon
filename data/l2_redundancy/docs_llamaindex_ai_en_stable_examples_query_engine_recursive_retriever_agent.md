Title: Recursive Retriever + Document Agents

URL Source: https://docs.llamaindex.ai/en/stable/examples/query_engine/recursive_retriever_agents/

Markdown Content:
Recursive Retriever + Document Agents - LlamaIndex


This guide shows how to combine recursive retrieval and "document agents" for advanced decision making over heterogeneous documents.

There are two motivating factors that lead to solutions for better retrieval:

*   Decoupling retrieval embeddings from chunk-based synthesis. Oftentimes fetching documents by their summaries will return more relevant context to queries rather than raw chunks. This is something that recursive retrieval directly allows.
*   Within a document, users may need to dynamically perform tasks beyond fact-based question-answering. We introduce the concept of "document agents" - agents that have access to both vector search and summary tools for a given document.

### Setup and Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/recursive_retriever_agents/#setup-and-download-data)

In this section, we'll define imports and then download Wikipedia articles about different cities. Each article is stored separately.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai
%pip install llama\-index\-agent\-openai

%pip install llama-index-llms-openai %pip install llama-index-agent-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.core import SummaryIndex
from llama\_index.core.schema import IndexNode
from llama\_index.core.tools import QueryEngineTool, ToolMetadata
from llama\_index.llms.openai import OpenAI

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.core import SummaryIndex from llama\_index.core.schema import IndexNode from llama\_index.core.tools import QueryEngineTool, ToolMetadata from llama\_index.llms.openai import OpenAI

In \[ \]:

Copied!

wiki\_titles \= \["Toronto", "Seattle", "Chicago", "Boston", "Houston"\]

wiki\_titles = \["Toronto", "Seattle", "Chicago", "Boston", "Houston"\]

In \[ \]:

Copied!

from pathlib import Path

import requests

for title in wiki\_titles:
    response \= requests.get(
        "https://en.wikipedia.org/w/api.php",
        params\={
            "action": "query",
            "format": "json",
            "titles": title,
            "prop": "extracts",
            \# 'exintro': True,
            "explaintext": True,
        },
    ).json()
    page \= next(iter(response\["query"\]\["pages"\].values()))
    wiki\_text \= page\["extract"\]

    data\_path \= Path("data")
    if not data\_path.exists():
        Path.mkdir(data\_path)

    with open(data\_path / f"{title}.txt", "w") as fp:
        fp.write(wiki\_text)

from pathlib import Path import requests for title in wiki\_titles: response = requests.get( "https://en.wikipedia.org/w/api.php", params={ "action": "query", "format": "json", "titles": title, "prop": "extracts", # 'exintro': True, "explaintext": True, }, ).json() page = next(iter(response\["query"\]\["pages"\].values())) wiki\_text = page\["extract"\] data\_path = Path("data") if not data\_path.exists(): Path.mkdir(data\_path) with open(data\_path / f"{title}.txt", "w") as fp: fp.write(wiki\_text)

In \[ \]:

Copied!

\# Load all wiki documents
city\_docs \= {}
for wiki\_title in wiki\_titles:
    city\_docs\[wiki\_title\] \= SimpleDirectoryReader(
        input\_files\=\[f"data/{wiki\_title}.txt"\]
    ).load\_data()

\# Load all wiki documents city\_docs = {} for wiki\_title in wiki\_titles: city\_docs\[wiki\_title\] = SimpleDirectoryReader( input\_files=\[f"data/{wiki\_title}.txt"\] ).load\_data()

Define LLM + Service Context + Callback Manager

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..."

In \[ \]:

Copied!

from llama\_index.core import Settings

Settings.llm \= OpenAI(temperature\=0, model\="gpt-3.5-turbo")

from llama\_index.core import Settings Settings.llm = OpenAI(temperature=0, model="gpt-3.5-turbo")

Build Document Agent for each Document[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/recursive_retriever_agents/#build-document-agent-for-each-document)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this section we define "document agents" for each document.

First we define both a vector index (for semantic search) and summary index (for summarization) for each document. The two query engines are then converted into tools that are passed to an OpenAI function calling agent.

This document agent can dynamically choose to perform semantic search or summarization within a given document.

We create a separate document agent for each city.

In \[ \]:

Copied!

from llama\_index.agent.openai import OpenAIAgent

\# Build agents dictionary
agents \= {}

for wiki\_title in wiki\_titles:
    \# build vector index
    vector\_index \= VectorStoreIndex.from\_documents(
        city\_docs\[wiki\_title\],
    )
    \# build summary index
    summary\_index \= SummaryIndex.from\_documents(
        city\_docs\[wiki\_title\],
    )
    \# define query engines
    vector\_query\_engine \= vector\_index.as\_query\_engine()
    list\_query\_engine \= summary\_index.as\_query\_engine()

    \# define tools
    query\_engine\_tools \= \[
        QueryEngineTool(
            query\_engine\=vector\_query\_engine,
            metadata\=ToolMetadata(
                name\="vector\_tool",
                description\=(
                    f"Useful for retrieving specific context from {wiki\_title}"
                ),
            ),
        ),
        QueryEngineTool(
            query\_engine\=list\_query\_engine,
            metadata\=ToolMetadata(
                name\="summary\_tool",
                description\=(
                    "Useful for summarization questions related to"
                    f" {wiki\_title}"
                ),
            ),
        ),
    \]

    \# build agent
    function\_llm \= OpenAI(model\="gpt-3.5-turbo-0613")
    agent \= OpenAIAgent.from\_tools(
        query\_engine\_tools,
        llm\=function\_llm,
        verbose\=True,
    )

    agents\[wiki\_title\] \= agent

from llama\_index.agent.openai import OpenAIAgent # Build agents dictionary agents = {} for wiki\_title in wiki\_titles: # build vector index vector\_index = VectorStoreIndex.from\_documents( city\_docs\[wiki\_title\], ) # build summary index summary\_index = SummaryIndex.from\_documents( city\_docs\[wiki\_title\], ) # define query engines vector\_query\_engine = vector\_index.as\_query\_engine() list\_query\_engine = summary\_index.as\_query\_engine() # define tools query\_engine\_tools = \[ QueryEngineTool( query\_engine=vector\_query\_engine, metadata=ToolMetadata( name="vector\_tool", description=( f"Useful for retrieving specific context from {wiki\_title}" ), ), ), QueryEngineTool( query\_engine=list\_query\_engine, metadata=ToolMetadata( name="summary\_tool", description=( "Useful for summarization questions related to" f" {wiki\_title}" ), ), ), \] # build agent function\_llm = OpenAI(model="gpt-3.5-turbo-0613") agent = OpenAIAgent.from\_tools( query\_engine\_tools, llm=function\_llm, verbose=True, ) agents\[wiki\_title\] = agent

Build Composable Retriever over these Agents[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/recursive_retriever_agents/#build-composable-retriever-over-these-agents)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now we define a set of summary nodes, where each node links to the corresponding Wikipedia city article. We then define a composable retriever + query engine on top of these Nodes to route queries down to a given node, which will in turn route it to the relevant document agent.

In \[ \]:

Copied!

\# define top-level nodes
objects \= \[\]
for wiki\_title in wiki\_titles:
    \# define index node that links to these agents
    wiki\_summary \= (
        f"This content contains Wikipedia articles about {wiki\_title}. Use"
        " this index if you need to lookup specific facts about"
        f" {wiki\_title}.\\nDo not use this index if you want to analyze"
        " multiple cities."
    )
    node \= IndexNode(
        text\=wiki\_summary, index\_id\=wiki\_title, obj\=agents\[wiki\_title\]
    )
    objects.append(node)

\# define top-level nodes objects = \[\] for wiki\_title in wiki\_titles: # define index node that links to these agents wiki\_summary = ( f"This content contains Wikipedia articles about {wiki\_title}. Use" " this index if you need to lookup specific facts about" f" {wiki\_title}.\\nDo not use this index if you want to analyze" " multiple cities." ) node = IndexNode( text=wiki\_summary, index\_id=wiki\_title, obj=agents\[wiki\_title\] ) objects.append(node)

In \[ \]:

Copied!

\# define top-level retriever
vector\_index \= VectorStoreIndex(
    objects\=objects,
)
query\_engine \= vector\_index.as\_query\_engine(similarity\_top\_k\=1, verbose\=True)

\# define top-level retriever vector\_index = VectorStoreIndex( objects=objects, ) query\_engine = vector\_index.as\_query\_engine(similarity\_top\_k=1, verbose=True)

Running Example Queries[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/recursive_retriever_agents/#running-example-queries)
------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

\# should use Boston agent -> vector tool
response \= query\_engine.query("Tell me about the sports teams in Boston")

\# should use Boston agent -> vector tool response = query\_engine.query("Tell me about the sports teams in Boston")

Retrieval entering Boston: OpenAIAgent
Retrieving from object OpenAIAgent with query Tell me about the sports teams in Boston
Added user message to memory: Tell me about the sports teams in Boston

In \[ \]:

Copied!

print(response)

print(response)

Boston is home to several professional sports teams across different leagues, including a successful baseball team in Major League Baseball, a highly successful American football team in the National Football League, one of the most successful basketball teams in the NBA, a professional ice hockey team in the National Hockey League, and a professional soccer team in Major League Soccer. These teams have a rich history, passionate fan bases, and have achieved great success both locally and nationally.

In \[ \]:

Copied!

\# should use Houston agent -> vector tool
response \= query\_engine.query("Tell me about the sports teams in Houston")

\# should use Houston agent -> vector tool response = query\_engine.query("Tell me about the sports teams in Houston")

Retrieval entering Houston: OpenAIAgent
Retrieving from object OpenAIAgent with query Tell me about the sports teams in Houston
Added user message to memory: Tell me about the sports teams in Houston

In \[ \]:

Copied!

print(response)

print(response)

Houston is home to several professional sports teams across different leagues, including the Houston Texans in the NFL, the Houston Rockets in the NBA, the Houston Astros in MLB, the Houston Dynamo in MLS, and the Houston Dash in NWSL. These teams compete in football, basketball, baseball, soccer, and women's soccer respectively, and have achieved various levels of success in their respective leagues. Additionally, the city also has minor league baseball, hockey, and other sports teams that cater to sports enthusiasts.

In \[ \]:

Copied!

\# should use Seattle agent -> summary tool
response \= query\_engine.query(
    "Give me a summary on all the positive aspects of Chicago"
)

\# should use Seattle agent -> summary tool response = query\_engine.query( "Give me a summary on all the positive aspects of Chicago" )

Retrieval entering Chicago: OpenAIAgent
Retrieving from object OpenAIAgent with query Give me a summary on all the positive aspects of Chicago
Added user message to memory: Give me a summary on all the positive aspects of Chicago

Calling function: summary\_tool with args: {
  "input": "positive aspects of Chicago"
}
Got output: Chicago is recognized for its robust economy, acting as a key hub for finance, culture, commerce, industry, education, technology, telecommunications, and transportation. It stands out in the derivatives market and is a top-ranking city in terms of gross domestic product. Chicago is a favored destination for tourists, known for its rich art scene covering visual arts, literature, film, theater, comedy, food, dance, and music. The city hosts prestigious educational institutions and professional sports teams across different leagues.


In \[ \]:

Copied!

print(response)

print(response)

Chicago is known for its strong economy with a focus on finance, culture, commerce, industry, education, technology, telecommunications, and transportation. It is a major player in the derivatives market and boasts a high gross domestic product. The city is a popular tourist destination with a vibrant art scene that includes visual arts, literature, film, theater, comedy, food, dance, and music. Additionally, Chicago is home to prestigious educational institutions and professional sports teams across various leagues.

Back to top

[Previous Query Engine with Pydantic Outputs](https://docs.llamaindex.ai/en/stable/examples/query_engine/pydantic_query_engine/)[Next Joint Tabular/Semantic QA over Tesla 10K](https://docs.llamaindex.ai/en/stable/examples/query_engine/sec_tables/tesla_10q_table/)
