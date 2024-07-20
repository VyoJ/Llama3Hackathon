Title: pgvecto.rs - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/PGVectoRsDemo/

Markdown Content:
pgvecto.rs - LlamaIndex


[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/docs/examples/vector_stores/PGVectoRsDemo.ipynb)

Firstly, you will probably need to install dependencies :

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-pgvecto\-rs

%pip install llama-index-vector-stores-pgvecto-rs

In \[ \]:

Copied!

%pip install llama\-index "pgvecto\_rs\[sdk\]"

%pip install llama-index "pgvecto\_rs\[sdk\]"

Then start the pgvecto.rs server as the [official document suggests](https://github.com/tensorchord/pgvecto.rs#installation):

In \[ \]:

Copied!

!docker run \--name pgvecto\-rs\-demo \-e POSTGRES\_PASSWORD\=mysecretpassword \-p 5432:5432 \-d tensorchord/pgvecto\-rs:latest

!docker run --name pgvecto-rs-demo -e POSTGRES\_PASSWORD=mysecretpassword -p 5432:5432 -d tensorchord/pgvecto-rs:latest

Setup the logger.

In \[ \]:

Copied!

import logging
import os
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import os import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

#### Creating a pgvecto\_rs client[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PGVectoRsDemo/#creating-a-pgvecto_rs-client)

In \[ \]:

Copied!

from pgvecto\_rs.sdk import PGVectoRs

URL \= "postgresql+psycopg://{username}:{password}@{host}:{port}/{db\_name}".format(
    port\=os.getenv("DB\_PORT", "5432"),
    host\=os.getenv("DB\_HOST", "localhost"),
    username\=os.getenv("DB\_USER", "postgres"),
    password\=os.getenv("DB\_PASS", "mysecretpassword"),
    db\_name\=os.getenv("DB\_NAME", "postgres"),
)

client \= PGVectoRs(
    db\_url\=URL,
    collection\_name\="example",
    dimension\=1536,  \# Using OpenAI’s text-embedding-ada-002
)

from pgvecto\_rs.sdk import PGVectoRs URL = "postgresql+psycopg://{username}:{password}@{host}:{port}/{db\_name}".format( port=os.getenv("DB\_PORT", "5432"), host=os.getenv("DB\_HOST", "localhost"), username=os.getenv("DB\_USER", "postgres"), password=os.getenv("DB\_PASS", "mysecretpassword"), db\_name=os.getenv("DB\_NAME", "postgres"), ) client = PGVectoRs( db\_url=URL, collection\_name="example", dimension=1536, # Using OpenAI’s text-embedding-ada-002 )

#### Setup OpenAI[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PGVectoRsDemo/#setup-openai)

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..."

#### Load documents, build the PGVectoRsStore and VectorStoreIndex[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PGVectoRsDemo/#load-documents-build-the-pgvectorsstore-and-vectorstoreindex)

In \[ \]:

Copied!

from IPython.display import Markdown, display

from llama\_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama\_index.vector\_stores.pgvecto\_rs import PGVectoRsStore

from IPython.display import Markdown, display from llama\_index.core import SimpleDirectoryReader, VectorStoreIndex from llama\_index.vector\_stores.pgvecto\_rs import PGVectoRsStore

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham").load\_data()

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham").load\_data()

In \[ \]:

Copied!

\# initialize without metadata filter
from llama\_index.core import StorageContext

vector\_store \= PGVectoRsStore(client\=client)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

\# initialize without metadata filter from llama\_index.core import StorageContext vector\_store = PGVectoRsStore(client=client) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

#### Query Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PGVectoRsDemo/#query-index)

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did the author do growing up?")

\# set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine() response = query\_engine.query("What did the author do growing up?")

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"

In \[ \]:

Copied!

display(Markdown(f"<b>{response}</b>"))

display(Markdown(f"**{response}**"))

**The author, growing up, worked on writing and programming. They wrote short stories and also tried writing programs on an IBM 1401 computer. They later got a microcomputer and started programming more extensively, writing simple games and a word processor.**

Back to top

[Previous Opensearch Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/OpensearchDemo/)[Next Pinecone Vector Store - Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PineconeIndexDemo-Hybrid/)
