Title: Zep Vector Store - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/ZepIndexDemo/

Markdown Content:
Zep Vector Store - LlamaIndex


A long-term memory store for LLM applications[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ZepIndexDemo/#a-long-term-memory-store-for-llm-applications)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This notebook demonstrates how to use the Zep Vector Store with LlamaIndex.

About Zep[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ZepIndexDemo/#about-zep)
-------------------------------------------------------------------------------------------------

Zep makes it easy for developers to add relevant documents, chat history memory & rich user data to their LLM app's prompts.

Note[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ZepIndexDemo/#note)
---------------------------------------------------------------------------------------

Zep can automatically embed your documents. The LlamaIndex implementation of the Zep Vector Store utilizes LlamaIndex's embedders to do so.

Getting Started[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ZepIndexDemo/#getting-started)
-------------------------------------------------------------------------------------------------------------

**Quick Start Guide:** [https://docs.getzep.com/deployment/quickstart/](https://docs.getzep.com/deployment/quickstart/) **GitHub:** [https://github.com/getzep/zep](https://github.com/getzep/zep)

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-zep

%pip install llama-index-vector-stores-zep

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

\# !pip install zep-python

\# !pip install zep-python

In \[ \]:

Copied!

import logging
import sys
from uuid import uuid4

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import os
import openai
from dotenv import load\_dotenv

load\_dotenv()

\# os.environ\["OPENAI\_API\_KEY"\] = "sk-..."
openai.api\_key \= os.environ\["OPENAI\_API\_KEY"\]

import logging import sys from uuid import uuid4 logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout)) import os import openai from dotenv import load\_dotenv load\_dotenv() # os.environ\["OPENAI\_API\_KEY"\] = "sk-..." openai.api\_key = os.environ\["OPENAI\_API\_KEY"\]

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.vector\_stores.zep import ZepVectorStore

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.vector\_stores.zep import ZepVectorStore

INFO:numexpr.utils:NumExpr defaulting to 8 threads.
NumExpr defaulting to 8 threads.

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("../data/paul\_graham/").load\_data()

\# load documents documents = SimpleDirectoryReader("../data/paul\_graham/").load\_data()

Create a Zep Vector Store and Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ZepIndexDemo/#create-a-zep-vector-store-and-index)
-----------------------------------------------------------------------------------------------------------------------------------------------------

You can use an existing Zep Collection, or create a new one.

In \[ \]:

Copied!

from llama\_index.core import StorageContext

zep\_api\_url \= "http://localhost:8000"
collection\_name \= f"graham{uuid4().hex}"

vector\_store \= ZepVectorStore(
    api\_url\=zep\_api\_url,
    collection\_name\=collection\_name,
    embedding\_dimensions\=1536,
)

storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

from llama\_index.core import StorageContext zep\_api\_url = "http://localhost:8000" collection\_name = f"graham{uuid4().hex}" vector\_store = ZepVectorStore( api\_url=zep\_api\_url, collection\_name=collection\_name, embedding\_dimensions=1536, ) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

INFO:httpx:HTTP Request: GET http://localhost:8000/healthz "HTTP/1.1 200 OK"
HTTP Request: GET http://localhost:8000/healthz "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://localhost:8000/api/v1/collection/grahamfbf0c456a2ad46c2887a707ccc7bb5df "HTTP/1.1 404 Not Found"
HTTP Request: GET http://localhost:8000/api/v1/collection/grahamfbf0c456a2ad46c2887a707ccc7bb5df "HTTP/1.1 404 Not Found"
INFO:llama\_index.vector\_stores.zep:Collection grahamfbf0c456a2ad46c2887a707ccc7bb5df does not exist, will try creating one with dimensions=1536
Collection grahamfbf0c456a2ad46c2887a707ccc7bb5df does not exist, will try creating one with dimensions=1536
INFO:httpx:HTTP Request: POST http://localhost:8000/api/v1/collection/grahamfbf0c456a2ad46c2887a707ccc7bb5df "HTTP/1.1 200 OK"
HTTP Request: POST http://localhost:8000/api/v1/collection/grahamfbf0c456a2ad46c2887a707ccc7bb5df "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://localhost:8000/api/v1/collection/grahamfbf0c456a2ad46c2887a707ccc7bb5df "HTTP/1.1 200 OK"
HTTP Request: GET http://localhost:8000/api/v1/collection/grahamfbf0c456a2ad46c2887a707ccc7bb5df "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://localhost:8000/api/v1/collection/grahamfbf0c456a2ad46c2887a707ccc7bb5df/document "HTTP/1.1 200 OK"
HTTP Request: POST http://localhost:8000/api/v1/collection/grahamfbf0c456a2ad46c2887a707ccc7bb5df/document "HTTP/1.1 200 OK"

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did the author do growing up?")

print(str(response))

query\_engine = index.as\_query\_engine() response = query\_engine.query("What did the author do growing up?") print(str(response))

INFO:httpx:HTTP Request: POST http://localhost:8000/api/v1/collection/grahamfbf0c456a2ad46c2887a707ccc7bb5df/search?limit=2 "HTTP/1.1 200 OK"
HTTP Request: POST http://localhost:8000/api/v1/collection/grahamfbf0c456a2ad46c2887a707ccc7bb5df/search?limit=2 "HTTP/1.1 200 OK"
The author worked on writing and programming outside of school before college. They wrote short stories and tried writing programs on an IBM 1401 computer using an early version of Fortran. They later got a microcomputer and started programming more extensively, writing simple games, a program to predict rocket heights, and a word processor. They initially planned to study philosophy in college but switched to AI. They also started publishing essays online and realized the potential of the web as a medium for publishing.

Querying with Metadata filters[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ZepIndexDemo/#querying-with-metadata-filters)
-------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core.schema import TextNode

nodes \= \[
    TextNode(
        text\="The Shawshank Redemption",
        metadata\={
            "author": "Stephen King",
            "theme": "Friendship",
        },
    ),
    TextNode(
        text\="The Godfather",
        metadata\={
            "director": "Francis Ford Coppola",
            "theme": "Mafia",
        },
    ),
    TextNode(
        text\="Inception",
        metadata\={
            "director": "Christopher Nolan",
        },
    ),
\]

from llama\_index.core.schema import TextNode nodes = \[ TextNode( text="The Shawshank Redemption", metadata={ "author": "Stephen King", "theme": "Friendship", }, ), TextNode( text="The Godfather", metadata={ "director": "Francis Ford Coppola", "theme": "Mafia", }, ), TextNode( text="Inception", metadata={ "director": "Christopher Nolan", }, ), \]

In \[ \]:

Copied!

collection\_name \= f"movies{uuid4().hex}"

vector\_store \= ZepVectorStore(
    api\_url\=zep\_api\_url,
    collection\_name\=collection\_name,
    embedding\_dimensions\=1536,
)

storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex(nodes, storage\_context\=storage\_context)

collection\_name = f"movies{uuid4().hex}" vector\_store = ZepVectorStore( api\_url=zep\_api\_url, collection\_name=collection\_name, embedding\_dimensions=1536, ) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex(nodes, storage\_context=storage\_context)

INFO:httpx:HTTP Request: GET http://localhost:8000/healthz "HTTP/1.1 200 OK"
HTTP Request: GET http://localhost:8000/healthz "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://localhost:8000/api/v1/collection/movies40ffd4f8a68c4822ae1680bb752c07e1 "HTTP/1.1 404 Not Found"
HTTP Request: GET http://localhost:8000/api/v1/collection/movies40ffd4f8a68c4822ae1680bb752c07e1 "HTTP/1.1 404 Not Found"
INFO:llama\_index.vector\_stores.zep:Collection movies40ffd4f8a68c4822ae1680bb752c07e1 does not exist, will try creating one with dimensions=1536
Collection movies40ffd4f8a68c4822ae1680bb752c07e1 does not exist, will try creating one with dimensions=1536
INFO:httpx:HTTP Request: POST http://localhost:8000/api/v1/collection/movies40ffd4f8a68c4822ae1680bb752c07e1 "HTTP/1.1 200 OK"
HTTP Request: POST http://localhost:8000/api/v1/collection/movies40ffd4f8a68c4822ae1680bb752c07e1 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET http://localhost:8000/api/v1/collection/movies40ffd4f8a68c4822ae1680bb752c07e1 "HTTP/1.1 200 OK"
HTTP Request: GET http://localhost:8000/api/v1/collection/movies40ffd4f8a68c4822ae1680bb752c07e1 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST http://localhost:8000/api/v1/collection/movies40ffd4f8a68c4822ae1680bb752c07e1/document "HTTP/1.1 200 OK"
HTTP Request: POST http://localhost:8000/api/v1/collection/movies40ffd4f8a68c4822ae1680bb752c07e1/document "HTTP/1.1 200 OK"

In \[ \]:

Copied!

from llama\_index.core.vector\_stores import ExactMatchFilter, MetadataFilters

filters \= MetadataFilters(
    filters\=\[ExactMatchFilter(key\="theme", value\="Mafia")\]
)

from llama\_index.core.vector\_stores import ExactMatchFilter, MetadataFilters filters = MetadataFilters( filters=\[ExactMatchFilter(key="theme", value="Mafia")\] )

In \[ \]:

Copied!

retriever \= index.as\_retriever(filters\=filters)
result \= retriever.retrieve("What is inception about?")

for r in result:
    print("\\n", r.node)
    print("Score:", r.score)

retriever = index.as\_retriever(filters=filters) result = retriever.retrieve("What is inception about?") for r in result: print("\\n", r.node) print("Score:", r.score)

INFO:httpx:HTTP Request: POST http://localhost:8000/api/v1/collection/movies40ffd4f8a68c4822ae1680bb752c07e1/search?limit=2 "HTTP/1.1 200 OK"
HTTP Request: POST http://localhost:8000/api/v1/collection/movies40ffd4f8a68c4822ae1680bb752c07e1/search?limit=2 "HTTP/1.1 200 OK"

 Node ID: 2b5ad50a-8ec0-40fa-b401-6e6b7ac3d304
Text: The Godfather
Score: 0.8841066656525941

Back to top

[Previous Weaviate Vector Store Metadata Filter](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndex_metadata_filter/)[Next Auto-Retrieval from a Vector Database](https://docs.llamaindex.ai/en/stable/examples/vector_stores/chroma_auto_retriever/)
