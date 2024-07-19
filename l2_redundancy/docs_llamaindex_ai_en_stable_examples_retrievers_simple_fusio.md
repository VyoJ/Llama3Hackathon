Title: Simple Fusion Retriever - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/retrievers/simple_fusion/

Markdown Content:
Simple Fusion Retriever - LlamaIndex


In this example, we walk through how you can combine retrieval results from multiple queries and multiple indexes.

The retrieved nodes will be returned as the top-k across all queries and indexes, as well as handling de-duplication of any nodes.

In \[ \]:

Copied!

import os
import openai

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."
openai.api\_key \= os.environ\["OPENAI\_API\_KEY"\]

import os import openai os.environ\["OPENAI\_API\_KEY"\] = "sk-..." openai.api\_key = os.environ\["OPENAI\_API\_KEY"\]

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/simple_fusion/#setup)
---------------------------------------------------------------------------------------

For this notebook, we will use two very similar pages of our documentation, each stored in a separaete index.

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

documents\_1 \= SimpleDirectoryReader(
    input\_files\=\["../../community/integrations/vector\_stores.md"\]
).load\_data()
documents\_2 \= SimpleDirectoryReader(
    input\_files\=\["../../module\_guides/storing/vector\_stores.md"\]
).load\_data()

from llama\_index.core import SimpleDirectoryReader documents\_1 = SimpleDirectoryReader( input\_files=\["../../community/integrations/vector\_stores.md"\] ).load\_data() documents\_2 = SimpleDirectoryReader( input\_files=\["../../module\_guides/storing/vector\_stores.md"\] ).load\_data()

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex

index\_1 \= VectorStoreIndex.from\_documents(documents\_1)
index\_2 \= VectorStoreIndex.from\_documents(documents\_2)

from llama\_index.core import VectorStoreIndex index\_1 = VectorStoreIndex.from\_documents(documents\_1) index\_2 = VectorStoreIndex.from\_documents(documents\_2)

Fuse the Indexes![¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/simple_fusion/#fuse-the-indexes)
--------------------------------------------------------------------------------------------------------------

In this step, we fuse our indexes into a single retriever. This retriever will also generate augment our query by generating extra queries related to the original question, and aggregate the results.

This setup will query 4 times, once with your original query, and generate 3 more queries.

By default, it uses the following prompt to generate extra queries:

QUERY\_GEN\_PROMPT \= (
    "You are a helpful assistant that generates multiple search queries based on a "
    "single input query. Generate {num\_queries} search queries, one on each line, "
    "related to the following input query:\\n"
    "Query: {query}\\n"
    "Queries:\\n"
)

In \[ \]:

Copied!

from llama\_index.core.retrievers import QueryFusionRetriever

retriever \= QueryFusionRetriever(
    \[index\_1.as\_retriever(), index\_2.as\_retriever()\],
    similarity\_top\_k\=2,
    num\_queries\=4,  \# set this to 1 to disable query generation
    use\_async\=True,
    verbose\=True,
    \# query\_gen\_prompt="...",  # we could override the query generation prompt here
)

from llama\_index.core.retrievers import QueryFusionRetriever retriever = QueryFusionRetriever( \[index\_1.as\_retriever(), index\_2.as\_retriever()\], similarity\_top\_k=2, num\_queries=4, # set this to 1 to disable query generation use\_async=True, verbose=True, # query\_gen\_prompt="...", # we could override the query generation prompt here )

In \[ \]:

Copied!

\# apply nested async to run in a notebook
import nest\_asyncio

nest\_asyncio.apply()

\# apply nested async to run in a notebook import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

nodes\_with\_scores \= retriever.retrieve("How do I setup a chroma vector store?")

nodes\_with\_scores = retriever.retrieve("How do I setup a chroma vector store?")

Generated queries:
1. What are the steps to set up a chroma vector store?
2. Best practices for configuring a chroma vector store
3. Troubleshooting common issues when setting up a chroma vector store

In \[ \]:

Copied!

for node in nodes\_with\_scores:
    print(f"Score: {node.score:.2f} - {node.text\[:100\]}...")

for node in nodes\_with\_scores: print(f"Score: {node.score:.2f} - {node.text\[:100\]}...")

Score: 0.78 - # Vector Stores

Vector stores contain embedding vectors of ingested document chunks
(and sometimes ...
Score: 0.78 - # Using Vector Stores

LlamaIndex offers multiple integration points with vector stores / vector dat...

Use in a Query Engine![¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/simple_fusion/#use-in-a-query-engine)
------------------------------------------------------------------------------------------------------------------------

Now, we can plug our retriever into a query engine to synthesize natural language responses.

In \[ \]:

Copied!

from llama\_index.core.query\_engine import RetrieverQueryEngine

query\_engine \= RetrieverQueryEngine.from\_args(retriever)

from llama\_index.core.query\_engine import RetrieverQueryEngine query\_engine = RetrieverQueryEngine.from\_args(retriever)

In \[ \]:

Copied!

response \= query\_engine.query(
    "How do I setup a chroma vector store? Can you give an example?"
)

response = query\_engine.query( "How do I setup a chroma vector store? Can you give an example?" )

Generated queries:
1. How to set up a chroma vector store?
2. Step-by-step guide for creating a chroma vector store.
3. Examples of chroma vector store setups and configurations.

In \[ \]:

Copied!

from llama\_index.core.response.notebook\_utils import display\_response

display\_response(response)

from llama\_index.core.response.notebook\_utils import display\_response display\_response(response)

**`Final Response:`** To set up a Chroma vector store, you need to follow these steps:

1.  Import the necessary libraries:

import chromadb
from llama\_index.vector\_stores.chroma import ChromaVectorStore

2.  Create a Chroma client:

chroma\_client \= chromadb.EphemeralClient()
chroma\_collection \= chroma\_client.create\_collection("quickstart")

3.  Construct the vector store:

vector\_store \= ChromaVectorStore(chroma\_collection\=chroma\_collection)

Here's an example of how to set up a Chroma vector store using the above steps:

import chromadb
from llama\_index.vector\_stores.chroma import ChromaVectorStore

\# Creating a Chroma client
\# EphemeralClient operates purely in-memory, PersistentClient will also save to disk
chroma\_client \= chromadb.EphemeralClient()
chroma\_collection \= chroma\_client.create\_collection("quickstart")

\# construct vector store
vector\_store \= ChromaVectorStore(chroma\_collection\=chroma\_collection)

This example demonstrates how to create a Chroma client, create a collection named "quickstart", and then construct a Chroma vector store using that collection.

Back to top

[Previous Router Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/router_retriever/)[Next Auto-Retrieval from a Vectara Index](https://docs.llamaindex.ai/en/stable/examples/retrievers/vectara_auto_retriever/)
