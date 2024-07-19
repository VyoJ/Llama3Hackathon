Title: Retriever Query Engine with Custom Retrievers - Simple Hybrid Search

URL Source: https://docs.llamaindex.ai/en/stable/examples/query_engine/CustomRetrievers/

Markdown Content:
Retriever Query Engine with Custom Retrievers - Simple Hybrid Search - LlamaIndex


In this tutorial, we show you how to define a very simple version of hybrid search!

Combine keyword lookup retrieval with vector retrieval using "AND" and "OR" conditions.

### Setup[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/CustomRetrievers/#setup)

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..."

### Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/CustomRetrievers/#download-data)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

Will not apply HSTS. The HSTS database must be a regular and non-world-writable file.
ERROR: could not open HSTS store at '/home/loganm/.wget-hsts'. HSTS will be disabled.
--2023-11-23 12:54:37--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.109.133, 185.199.111.133, 185.199.108.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.109.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 75042 (73K) \[text/plain\]
Saving to: ‘data/paul\_graham/paul\_graham\_essay.txt’

data/paul\_graham/pa 100%\[ "AND":
            retrieve\_ids \= vector\_ids.intersection(keyword\_ids)
        else:
            retrieve\_ids \= vector\_ids.union(keyword\_ids)

        retrieve\_nodes \= \[combined\_dict\[rid\] for rid in retrieve\_ids\]
        return retrieve\_nodes

class CustomRetriever(BaseRetriever): """Custom retriever that performs both semantic search and hybrid search.""" def \_\_init\_\_( self, vector\_retriever: VectorIndexRetriever, keyword\_retriever: KeywordTableSimpleRetriever, mode: str = "AND", ) -> None: """Init params.""" self.\_vector\_retriever = vector\_retriever self.\_keyword\_retriever = keyword\_retriever if mode not in ("AND", "OR"): raise ValueError("Invalid mode.") self.\_mode = mode super().\_\_init\_\_() def \_retrieve(self, query\_bundle: QueryBundle) -> List\[NodeWithScore\]: """Retrieve nodes given query.""" vector\_nodes = self.\_vector\_retriever.retrieve(query\_bundle) keyword\_nodes = self.\_keyword\_retriever.retrieve(query\_bundle) vector\_ids = {n.node.node\_id for n in vector\_nodes} keyword\_ids = {n.node.node\_id for n in keyword\_nodes} combined\_dict = {n.node.node\_id: n for n in vector\_nodes} combined\_dict.update({n.node.node\_id: n for n in keyword\_nodes}) if self.\_mode == "AND": retrieve\_ids = vector\_ids.intersection(keyword\_ids) else: retrieve\_ids = vector\_ids.union(keyword\_ids) retrieve\_nodes = \[combined\_dict\[rid\] for rid in retrieve\_ids\] return retrieve\_nodes

### Plugin Retriever into Query Engine[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/CustomRetrievers/#plugin-retriever-into-query-engine)

Plugin retriever into a query engine, and run some queries

In \[ \]:

Copied!

from llama\_index.core import get\_response\_synthesizer
from llama\_index.core.query\_engine import RetrieverQueryEngine

\# define custom retriever
vector\_retriever \= VectorIndexRetriever(index\=vector\_index, similarity\_top\_k\=2)
keyword\_retriever \= KeywordTableSimpleRetriever(index\=keyword\_index)
custom\_retriever \= CustomRetriever(vector\_retriever, keyword\_retriever)

\# define response synthesizer
response\_synthesizer \= get\_response\_synthesizer()

\# assemble query engine
custom\_query\_engine \= RetrieverQueryEngine(
    retriever\=custom\_retriever,
    response\_synthesizer\=response\_synthesizer,
)

\# vector query engine
vector\_query\_engine \= RetrieverQueryEngine(
    retriever\=vector\_retriever,
    response\_synthesizer\=response\_synthesizer,
)
\# keyword query engine
keyword\_query\_engine \= RetrieverQueryEngine(
    retriever\=keyword\_retriever,
    response\_synthesizer\=response\_synthesizer,
)

from llama\_index.core import get\_response\_synthesizer from llama\_index.core.query\_engine import RetrieverQueryEngine # define custom retriever vector\_retriever = VectorIndexRetriever(index=vector\_index, similarity\_top\_k=2) keyword\_retriever = KeywordTableSimpleRetriever(index=keyword\_index) custom\_retriever = CustomRetriever(vector\_retriever, keyword\_retriever) # define response synthesizer response\_synthesizer = get\_response\_synthesizer() # assemble query engine custom\_query\_engine = RetrieverQueryEngine( retriever=custom\_retriever, response\_synthesizer=response\_synthesizer, ) # vector query engine vector\_query\_engine = RetrieverQueryEngine( retriever=vector\_retriever, response\_synthesizer=response\_synthesizer, ) # keyword query engine keyword\_query\_engine = RetrieverQueryEngine( retriever=keyword\_retriever, response\_synthesizer=response\_synthesizer, )

In \[ \]:

Copied!

response \= custom\_query\_engine.query(
    "What did the author do during his time at YC?"
)

response = custom\_query\_engine.query( "What did the author do during his time at YC?" )

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:llama\_index.indices.keyword\_table.retrievers:> Starting query: What did the author do during his time at YC?

\> Starting query: What did the author do during his time at YC?
INFO:llama\_index.indices.keyword\_table.retrievers:query keywords: \['author', 'yc', 'time'\]
query keywords: \['author', 'yc', 'time'\]
INFO:llama\_index.indices.keyword\_table.retrievers:> Extracted keywords: \['yc', 'time'\]
> Extracted keywords: \['yc', 'time'\]
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"

In \[ \]:

Copied!

print(response)

print(response)

During his time at YC, the author worked on various projects, including writing essays and working on YC itself. He also wrote all of YC's internal software in Arc. Additionally, he mentioned that he dealt with urgent problems, with about a 60% chance of them being related to Hacker News (HN), and a 40% chance of them being related to everything else combined. The author also mentioned that YC was different from other kinds of work he had done, as the problems of the startups in each batch became their problems, and he worked hard even at the parts of the job he didn't like.

In \[ \]:

Copied!

\# hybrid search can allow us to not retrieve nodes that are irrelevant
\# Yale is never mentioned in the essay
response \= custom\_query\_engine.query(
    "What did the author do during his time at Yale?"
)

\# hybrid search can allow us to not retrieve nodes that are irrelevant # Yale is never mentioned in the essay response = custom\_query\_engine.query( "What did the author do during his time at Yale?" )

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:llama\_index.indices.keyword\_table.retrievers:> Starting query: What did the author do during his time at Yale?
> Starting query: What did the author do during his time at Yale?
INFO:llama\_index.indices.keyword\_table.retrievers:query keywords: \['author', 'yale', 'time'\]
query keywords: \['author', 'yale', 'time'\]
INFO:llama\_index.indices.keyword\_table.retrievers:> Extracted keywords: \['time'\]
> Extracted keywords: \['time'\]

In \[ \]:

Copied!

print(str(response))
len(response.source\_nodes)

print(str(response)) len(response.source\_nodes)

Empty Response

Out\[ \]:

0

In \[ \]:

Copied!

\# in contrast, vector search will return an answer
response \= vector\_query\_engine.query(
    "What did the author do during his time at Yale?"
)

\# in contrast, vector search will return an answer response = vector\_query\_engine.query( "What did the author do during his time at Yale?" )

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"

In \[ \]:

Copied!

print(str(response))
len(response.source\_nodes)

print(str(response)) len(response.source\_nodes)

The context information does not provide any information about the author's time at Yale.

Out\[ \]:

2

Back to top

[Previous Neo4j Property Graph Index](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_neo4j/)[Next JSONalyze Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/JSONalyze_query_engine/)

Hi, how can I help you?

🦙
