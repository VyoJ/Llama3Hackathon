Title: Relyt - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/RelytDemo/

Markdown Content:
Relyt - LlamaIndex


[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/docs/examples/vector_stores/PGVectoRsDemo.ipynb)

Firstly, you will probably need to install dependencies :

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-relyt

%pip install llama-index-vector-stores-relyt

In \[ \]:

Copied!

%pip install llama\-index "pgvecto\_rs\[sdk\]"

%pip install llama-index "pgvecto\_rs\[sdk\]"

Then start the relyt as the [official document](https://docs.relyt.cn/docs/vector-engine/use/):

Setup the logger.

In \[ \]:

Copied!

import logging
import os
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import os import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

#### Creating a pgvecto\_rs client[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RelytDemo/#creating-a-pgvecto_rs-client)

In \[ \]:

Copied!

from pgvecto\_rs.sdk import PGVectoRs

URL \= "postgresql+psycopg://{username}:{password}@{host}:{port}/{db\_name}".format(
    port\=os.getenv("RELYT\_PORT", "5432"),
    host\=os.getenv("RELYT\_HOST", "localhost"),
    username\=os.getenv("RELYT\_USER", "postgres"),
    password\=os.getenv("RELYT\_PASS", "mysecretpassword"),
    db\_name\=os.getenv("RELYT\_NAME", "postgres"),
)

client \= PGVectoRs(
    db\_url\=URL,
    collection\_name\="example",
    dimension\=1536,  \# Using OpenAI’s text-embedding-ada-002
)

from pgvecto\_rs.sdk import PGVectoRs URL = "postgresql+psycopg://{username}:{password}@{host}:{port}/{db\_name}".format( port=os.getenv("RELYT\_PORT", "5432"), host=os.getenv("RELYT\_HOST", "localhost"), username=os.getenv("RELYT\_USER", "postgres"), password=os.getenv("RELYT\_PASS", "mysecretpassword"), db\_name=os.getenv("RELYT\_NAME", "postgres"), ) client = PGVectoRs( db\_url=URL, collection\_name="example", dimension=1536, # Using OpenAI’s text-embedding-ada-002 )

#### Setup OpenAI[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RelytDemo/#setup-openai)

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..."

#### Load documents, build the PGVectoRsStore and VectorStoreIndex[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RelytDemo/#load-documents-build-the-pgvectorsstore-and-vectorstoreindex)

In \[ \]:

Copied!

from IPython.display import Markdown, display

from llama\_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama\_index.vector\_stores.relyt import RelytVectorStore

from IPython.display import Markdown, display from llama\_index.core import SimpleDirectoryReader, VectorStoreIndex from llama\_index.vector\_stores.relyt import RelytVectorStore

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

vector\_store \= RelytVectorStore(client\=client)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

\# initialize without metadata filter from llama\_index.core import StorageContext vector\_store = RelytVectorStore(client=client) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

#### Query Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RelytDemo/#query-index)

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

[Previous Redis Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RedisIndexDemo/)[Next Rockset Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RocksetIndexDemo/)
