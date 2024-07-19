Title: Router Query Engine - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/query_engine/RouterQueryEngine/

Markdown Content:
Router Query Engine - LlamaIndex


In this tutorial, we define a custom router query engine that selects one out of several candidate query engines to execute a query.

### Setup[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/RouterQueryEngine/#setup)

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-embeddings\-openai
%pip install llama\-index\-llms\-openai

%pip install llama-index-embeddings-openai %pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

\# NOTE: This is ONLY necessary in jupyter notebook.
\# Details: Jupyter runs an event-loop behind the scenes.
\#          This results in nested event-loops when we start an event-loop to make async queries.
\#          This is normally not allowed, we use nest\_asyncio to allow it for convenience.
import nest\_asyncio

nest\_asyncio.apply()

\# NOTE: This is ONLY necessary in jupyter notebook. # Details: Jupyter runs an event-loop behind the scenes. # This results in nested event-loops when we start an event-loop to make async queries. # This is normally not allowed, we use nest\_asyncio to allow it for convenience. import nest\_asyncio nest\_asyncio.apply()

Global Models[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/RouterQueryEngine/#global-models)
-------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..."

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI
from llama\_index.embeddings.openai import OpenAIEmbedding
from llama\_index.core import Settings

Settings.llm \= OpenAI(model\="gpt-3.5-turbo-1106", temperature\=0.2)
Settings.embed\_model \= OpenAIEmbedding(model\="text-embedding-3-small")

from llama\_index.llms.openai import OpenAI from llama\_index.embeddings.openai import OpenAIEmbedding from llama\_index.core import Settings Settings.llm = OpenAI(model="gpt-3.5-turbo-1106", temperature=0.2) Settings.embed\_model = OpenAIEmbedding(model="text-embedding-3-small")

### Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/RouterQueryEngine/#load-data)

We first show how to convert a Document into a set of Nodes, and insert into a DocumentStore.

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

\# load documents
documents \= SimpleDirectoryReader("../data/paul\_graham").load\_data()

from llama\_index.core import SimpleDirectoryReader # load documents documents = SimpleDirectoryReader("../data/paul\_graham").load\_data()

In \[ \]:

Copied!

from llama\_index.core import Settings

\# initialize settings (set chunk size)
Settings.chunk\_size \= 1024
nodes \= Settings.node\_parser.get\_nodes\_from\_documents(documents)

from llama\_index.core import Settings # initialize settings (set chunk size) Settings.chunk\_size = 1024 nodes = Settings.node\_parser.get\_nodes\_from\_documents(documents)

In \[ \]:

Copied!

from llama\_index.core import StorageContext

\# initialize storage context (by default it's in-memory)
storage\_context \= StorageContext.from\_defaults()
storage\_context.docstore.add\_documents(nodes)

from llama\_index.core import StorageContext # initialize storage context (by default it's in-memory) storage\_context = StorageContext.from\_defaults() storage\_context.docstore.add\_documents(nodes)

### Define Summary Index and Vector Index over Same Data[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/RouterQueryEngine/#define-summary-index-and-vector-index-over-same-data)

In \[ \]:

Copied!

from llama\_index.core import SummaryIndex
from llama\_index.core import VectorStoreIndex

summary\_index \= SummaryIndex(nodes, storage\_context\=storage\_context)
vector\_index \= VectorStoreIndex(nodes, storage\_context\=storage\_context)

from llama\_index.core import SummaryIndex from llama\_index.core import VectorStoreIndex summary\_index = SummaryIndex(nodes, storage\_context=storage\_context) vector\_index = VectorStoreIndex(nodes, storage\_context=storage\_context)

### Define Query Engines and Set Metadata[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/RouterQueryEngine/#define-query-engines-and-set-metadata)

In \[ \]:

Copied!

list\_query\_engine \= summary\_index.as\_query\_engine(
    response\_mode\="tree\_summarize",
    use\_async\=True,
)
vector\_query\_engine \= vector\_index.as\_query\_engine()

list\_query\_engine = summary\_index.as\_query\_engine( response\_mode="tree\_summarize", use\_async=True, ) vector\_query\_engine = vector\_index.as\_query\_engine()

In \[ \]:

Copied!

from llama\_index.core.tools import QueryEngineTool

list\_tool \= QueryEngineTool.from\_defaults(
    query\_engine\=list\_query\_engine,
    description\=(
        "Useful for summarization questions related to Paul Graham eassy on"
        " What I Worked On."
    ),
)

vector\_tool \= QueryEngineTool.from\_defaults(
    query\_engine\=vector\_query\_engine,
    description\=(
        "Useful for retrieving specific context from Paul Graham essay on What"
        " I Worked On."
    ),
)

from llama\_index.core.tools import QueryEngineTool list\_tool = QueryEngineTool.from\_defaults( query\_engine=list\_query\_engine, description=( "Useful for summarization questions related to Paul Graham eassy on" " What I Worked On." ), ) vector\_tool = QueryEngineTool.from\_defaults( query\_engine=vector\_query\_engine, description=( "Useful for retrieving specific context from Paul Graham essay on What" " I Worked On." ), )

### Define Router Query Engine[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/RouterQueryEngine/#define-router-query-engine)

There are several selectors available, each with some distinct attributes.

The LLM selectors use the LLM to output a JSON that is parsed, and the corresponding indexes are queried.

The Pydantic selectors (currently only supported by `gpt-4-0613` and `gpt-3.5-turbo-0613` (the default)) use the OpenAI Function Call API to produce pydantic selection objects, rather than parsing raw JSON.

For each type of selector, there is also the option to select 1 index to route to, or multiple.

#### PydanticSingleSelector[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/RouterQueryEngine/#pydanticsingleselector)

Use the OpenAI Function API to generate/parse pydantic objects under the hood for the router selector.

In \[ \]:

Copied!

from llama\_index.core.query\_engine import RouterQueryEngine
from llama\_index.core.selectors import LLMSingleSelector, LLMMultiSelector
from llama\_index.core.selectors import (
    PydanticMultiSelector,
    PydanticSingleSelector,
)

query\_engine \= RouterQueryEngine(
    selector\=PydanticSingleSelector.from\_defaults(),
    query\_engine\_tools\=\[
        list\_tool,
        vector\_tool,
    \],
)

from llama\_index.core.query\_engine import RouterQueryEngine from llama\_index.core.selectors import LLMSingleSelector, LLMMultiSelector from llama\_index.core.selectors import ( PydanticMultiSelector, PydanticSingleSelector, ) query\_engine = RouterQueryEngine( selector=PydanticSingleSelector.from\_defaults(), query\_engine\_tools=\[ list\_tool, vector\_tool, \], )

In \[ \]:

Copied!

response \= query\_engine.query("What is the summary of the document?")
print(str(response))

response = query\_engine.query("What is the summary of the document?") print(str(response))

The document provides a comprehensive account of the author's diverse experiences, including writing, programming, founding and running startups, and investing in early-stage companies. It covers the challenges, successes, and lessons learned in these ventures, as well as the author's personal and professional growth, interactions with colleagues, and evolving interests and priorities over time.

In \[ \]:

Copied!

response \= query\_engine.query("What did Paul Graham do after RICS?")
print(str(response))

response = query\_engine.query("What did Paul Graham do after RICS?") print(str(response))

Paul Graham started painting after leaving Y Combinator. He wanted to see how good he could get if he really focused on it. After spending most of 2014 painting, he eventually ran out of steam and stopped working on it. He then started writing essays again and wrote a bunch of new ones over the next few months. Later, in March 2015, he started working on Lisp again.

#### LLMSingleSelector[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/RouterQueryEngine/#llmsingleselector)

Use OpenAI (or any other LLM) to parse generated JSON under the hood to select a sub-index for routing.

In \[ \]:

Copied!

query\_engine \= RouterQueryEngine(
    selector\=LLMSingleSelector.from\_defaults(),
    query\_engine\_tools\=\[
        list\_tool,
        vector\_tool,
    \],
)

query\_engine = RouterQueryEngine( selector=LLMSingleSelector.from\_defaults(), query\_engine\_tools=\[ list\_tool, vector\_tool, \], )

In \[ \]:

Copied!

response \= query\_engine.query("What is the summary of the document?")
print(str(response))

response = query\_engine.query("What is the summary of the document?") print(str(response))

The document provides a comprehensive account of the author's professional journey, covering his involvement in various projects such as Viaweb, Y Combinator, and Hacker News, as well as his transition to focusing on writing essays and working on Y Combinator. It also delves into his experiences with the Summer Founders Program, the growth and challenges of Y Combinator, personal struggles, and his return to working on Lisp. The author reflects on the challenges and successes encountered throughout his career, including funding startups, developing a new version of Arc, and the impact of Hacker News. Additionally, the document touches on the author's interactions with colleagues, his time in Italy, experiences with painting, and the completion of a new Lisp called Bel. Throughout, the author shares insights and lessons learned from his diverse experiences.

In \[ \]:

Copied!

response \= query\_engine.query("What did Paul Graham do after RICS?")
print(str(response))

response = query\_engine.query("What did Paul Graham do after RICS?") print(str(response))

Paul Graham started painting after leaving Y Combinator. He wanted to see how good he could get if he really focused on it. After spending most of 2014 painting, he eventually ran out of steam and stopped working on it. He then started writing essays again and wrote a bunch of new ones over the next few months. In March 2015, he started working on Lisp again.

In \[ \]:

Copied!

\# \[optional\] look at selected results
print(str(response.metadata\["selector\_result"\]))

\# \[optional\] look at selected results print(str(response.metadata\["selector\_result"\]))

selections=\[SingleSelection(index=1, reason='The question is asking for specific context about what Paul Graham did after RICS, which would require retrieving specific information from his essay.')\]

#### PydanticMultiSelector[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/RouterQueryEngine/#pydanticmultiselector)

In case you are expecting queries to be routed to multiple indexes, you should use a multi selector. The multi selector sends to query to multiple sub-indexes, and then aggregates all responses using a summary index to form a complete answer.

In \[ \]:

Copied!

from llama\_index.core import SimpleKeywordTableIndex

keyword\_index \= SimpleKeywordTableIndex(nodes, storage\_context\=storage\_context)

keyword\_tool \= QueryEngineTool.from\_defaults(
    query\_engine\=vector\_query\_engine,
    description\=(
        "Useful for retrieving specific context using keywords from Paul"
        " Graham essay on What I Worked On."
    ),
)

from llama\_index.core import SimpleKeywordTableIndex keyword\_index = SimpleKeywordTableIndex(nodes, storage\_context=storage\_context) keyword\_tool = QueryEngineTool.from\_defaults( query\_engine=vector\_query\_engine, description=( "Useful for retrieving specific context using keywords from Paul" " Graham essay on What I Worked On." ), )

In \[ \]:

Copied!

query\_engine \= RouterQueryEngine(
    selector\=PydanticMultiSelector.from\_defaults(),
    query\_engine\_tools\=\[
        list\_tool,
        vector\_tool,
        keyword\_tool,
    \],
)

query\_engine = RouterQueryEngine( selector=PydanticMultiSelector.from\_defaults(), query\_engine\_tools=\[ list\_tool, vector\_tool, keyword\_tool, \], )

In \[ \]:

Copied!

\# This query could use either a keyword or vector query engine, so it will combine responses from both
response \= query\_engine.query(
    "What were noteable events and people from the authors time at Interleaf"
    " and YC?"
)
print(str(response))

\# This query could use either a keyword or vector query engine, so it will combine responses from both response = query\_engine.query( "What were noteable events and people from the authors time at Interleaf" " and YC?" ) print(str(response))

The author's time at Interleaf involved working on software for creating documents and learning valuable lessons about what not to do. Notable individuals associated with Y Combinator during the author's time there include Jessica Livingston, Robert Morris, and Sam Altman, who eventually became the second president of YC. The author's time at Y Combinator included notable events such as the creation of the Summer Founders Program, which attracted impressive individuals like Reddit, Justin Kan, Emmett Shear, Aaron Swartz, and Sam Altman.

In \[ \]:

Copied!

\# \[optional\] look at selected results
print(str(response.metadata\["selector\_result"\]))

\# \[optional\] look at selected results print(str(response.metadata\["selector\_result"\]))

selections=\[SingleSelection(index=0, reason='Summarization questions related to Paul Graham essay on What I Worked On.'), SingleSelection(index=2, reason='Retrieving specific context using keywords from Paul Graham essay on What I Worked On.')\]

Back to top

[Previous Retriever Router Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/RetrieverRouterQueryEngine/)[Next SQL Auto Vector Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLAutoVectorQueryEngine/)

Hi, how can I help you?

🦙
