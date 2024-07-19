Title: PostgresML Managed Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/managed/PostgresMLDemo/

Markdown Content:
PostgresML Managed Index - LlamaIndex


In this notebook we are going to show how to use [PostgresML](https://postgresml.org/) with LlamaIndex.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

!pip install llama\-index\-indices\-managed\-postgresml

!pip install llama-index-indices-managed-postgresml

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

from llama\_index.indices.managed.postgresml import PostgresMLIndex

from llama\_index.core import SimpleDirectoryReader

\# Need this as asyncio can get pretty wild with notebooks and this prevents event loop errors
import nest\_asyncio

nest\_asyncio.apply()

from llama\_index.indices.managed.postgresml import PostgresMLIndex from llama\_index.core import SimpleDirectoryReader # Need this as asyncio can get pretty wild with notebooks and this prevents event loop errors import nest\_asyncio nest\_asyncio.apply()

### Loading documents[¶](https://docs.llamaindex.ai/en/stable/examples/managed/PostgresMLDemo/#loading-documents)

Load the `paul_graham_essay.txt` document.

In \[ \]:

Copied!

!mkdir data
!curl \-o data/paul\_graham\_essay.txt https://raw.githubusercontent.com/run\-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt

!mkdir data !curl -o data/paul\_graham\_essay.txt https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt

In \[ \]:

Copied!

documents \= SimpleDirectoryReader("data").load\_data()
print(f"documents loaded into {len(documents)} document objects")
print(f"Document ID of first doc is {documents\[0\].doc\_id}")

documents = SimpleDirectoryReader("data").load\_data() print(f"documents loaded into {len(documents)} document objects") print(f"Document ID of first doc is {documents\[0\].doc\_id}")

### Upsert the documents into your PostgresML database[¶](https://docs.llamaindex.ai/en/stable/examples/managed/PostgresMLDemo/#upsert-the-documents-into-your-postgresml-database)

First let's set the url to our PostgresML database. If you don't have a url yet, you can make one for free here: [https://postgresml.org/signup](https://postgresml.org/signup)

In \[ \]:

Copied!

\# Let's set some secrets we need
from google.colab import userdata

PGML\_DATABASE\_URL \= userdata.get("PGML\_DATABASE\_URL")

\# If you don't have those secrets set, uncomment the lines below and run them instead
\# Make sure to replace {REPLACE\_ME} with your keys
\# PGML\_DATABASE\_URL = "{REPLACE\_ME}"

\# Let's set some secrets we need from google.colab import userdata PGML\_DATABASE\_URL = userdata.get("PGML\_DATABASE\_URL") # If you don't have those secrets set, uncomment the lines below and run them instead # Make sure to replace {REPLACE\_ME} with your keys # PGML\_DATABASE\_URL = "{REPLACE\_ME}"

In \[ \]:

Copied!

index \= PostgresMLIndex.from\_documents(
    documents,
    collection\_name\="llama-index-example-demo",
    pgml\_database\_url\=PGML\_DATABASE\_URL,
)

index = PostgresMLIndex.from\_documents( documents, collection\_name="llama-index-example-demo", pgml\_database\_url=PGML\_DATABASE\_URL, )

### Query the Postgresml Index[¶](https://docs.llamaindex.ai/en/stable/examples/managed/PostgresMLDemo/#query-the-postgresml-index)

We can now ask questions using the PostgresMLIndex retriever.

In \[ \]:

Copied!

query \= "What did the author write about?"

query = "What did the author write about?"

We can use a retriever to list search our documents:

In \[ \]:

Copied!

retriever \= index.as\_retriever()
response \= retriever.retrieve(query)
texts \= \[t.node.text for t in response\]

print("The Nodes:")
print(response)
print("\\nThe Texts")
print(texts)

retriever = index.as\_retriever() response = retriever.retrieve(query) texts = \[t.node.text for t in response\] print("The Nodes:") print(response) print("\\nThe Texts") print(texts)

PostgresML allows for easy re-reranking in the same query as doing retrieval:

In \[ \]:

Copied!

retriever \= index.as\_retriever(
    limit\=2,  \# Limit to returning the 2 most related Nodes
    rerank\={
        "model": "mixedbread-ai/mxbai-rerank-base-v1",  \# Use the mxbai-rerank-base model for reranking
        "num\_documents\_to\_rerank": 100,  \# Rerank up to 100 results returned from the vector search
    },
)
response \= retriever.retrieve(query)
texts \= \[t.node.text for t in response\]

print("The Nodes:")
print(response)
print("\\nThe Texts")
print(texts)

retriever = index.as\_retriever( limit=2, # Limit to returning the 2 most related Nodes rerank={ "model": "mixedbread-ai/mxbai-rerank-base-v1", # Use the mxbai-rerank-base model for reranking "num\_documents\_to\_rerank": 100, # Rerank up to 100 results returned from the vector search }, ) response = retriever.retrieve(query) texts = \[t.node.text for t in response\] print("The Nodes:") print(response) print("\\nThe Texts") print(texts)

with the as\_query\_engine(), we can ask questions and get the response in one query:

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()
response \= query\_engine.query(query)

print("The Response:")
print(response)
print("\\nThe Source Nodes:")
print(response.get\_formatted\_sources())

query\_engine = index.as\_query\_engine() response = query\_engine.query(query) print("The Response:") print(response) print("\\nThe Source Nodes:") print(response.get\_formatted\_sources())

Note that the "response" object above includes both the summary text but also the source documents used to provide this response (citations). Notice the source nodes are all from the same document. That is because we only uploaded one document which PostgresML automatically split before embedding for us. All parameters can be controlled. See the documentation for more information.

We can enable streaming by passing `streaming=True` when we create our query\_engine.

**NOTE: Streaming is painfully slow on google collab due to their internet connectivity.**

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(streaming\=True)
results \= query\_engine.query(query)
for text in results.response\_gen:
    print(text, end\="", flush\=True)

query\_engine = index.as\_query\_engine(streaming=True) results = query\_engine.query(query) for text in results.response\_gen: print(text, end="", flush=True)

Back to top

[Previous Google Generative Language Semantic Retriever](https://docs.llamaindex.ai/en/stable/examples/managed/GoogleDemo/)[Next Google Cloud LlamaIndex on Vertex AI for RAG](https://docs.llamaindex.ai/en/stable/examples/managed/VertexAIDemo/)

Hi, how can I help you?

🦙
