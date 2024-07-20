Title: Lantern Vector Store - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanternIndexDemo/

Markdown Content:
Lantern Vector Store - LlamaIndex


In this notebook we are going to show how to use [Postgresql](https://www.postgresql.org/) and [Lantern](https://github.com/lanterndata/lantern) to perform vector searches in LlamaIndex

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-lantern
%pip install llama\-index\-embeddings\-openai

%pip install llama-index-vector-stores-lantern %pip install llama-index-embeddings-openai

In \[ \]:

Copied!

!pip install psycopg2\-binary llama\-index asyncpg

!pip install psycopg2-binary llama-index asyncpg

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader, StorageContext
from llama\_index.core import VectorStoreIndex
from llama\_index.vector\_stores.lantern import LanternVectorStore
import textwrap
import openai

from llama\_index.core import SimpleDirectoryReader, StorageContext from llama\_index.core import VectorStoreIndex from llama\_index.vector\_stores.lantern import LanternVectorStore import textwrap import openai

### Setup OpenAI[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanternIndexDemo/#setup-openai)

The first step is to configure the openai key. It will be used to created embeddings for the documents loaded into the index

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "<your\_key>"
openai.api\_key \= "<your\_key>"

import os os.environ\["OPENAI\_API\_KEY"\] = "" openai.api\_key = ""

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

### Loading documents[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanternIndexDemo/#loading-documents)

Load the documents stored in the `data/paul_graham/` using the SimpleDirectoryReader

In \[ \]:

Copied!

documents \= SimpleDirectoryReader("./data/paul\_graham").load\_data()
print("Document ID:", documents\[0\].doc\_id)

documents = SimpleDirectoryReader("./data/paul\_graham").load\_data() print("Document ID:", documents\[0\].doc\_id)

### Create the Database[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanternIndexDemo/#create-the-database)

Using an existing postgres running at localhost, create the database we'll be using.

In \[ \]:

Copied!

import psycopg2

connection\_string \= "postgresql://postgres:postgres@localhost:5432"
db\_name \= "postgres"
conn \= psycopg2.connect(connection\_string)
conn.autocommit \= True

with conn.cursor() as c:
    c.execute(f"DROP DATABASE IF EXISTS {db\_name}")
    c.execute(f"CREATE DATABASE {db\_name}")

import psycopg2 connection\_string = "postgresql://postgres:postgres@localhost:5432" db\_name = "postgres" conn = psycopg2.connect(connection\_string) conn.autocommit = True with conn.cursor() as c: c.execute(f"DROP DATABASE IF EXISTS {db\_name}") c.execute(f"CREATE DATABASE {db\_name}")

In \[ \]:

Copied!

from llama\_index.embeddings.openai import OpenAIEmbedding
from llama\_index.core import Settings

\# Setup global settings with embedding model
\# So query strings will be transformed to embeddings and HNSW index will be used
Settings.embed\_model \= OpenAIEmbedding(model\="text-embedding-3-small")

from llama\_index.embeddings.openai import OpenAIEmbedding from llama\_index.core import Settings # Setup global settings with embedding model # So query strings will be transformed to embeddings and HNSW index will be used Settings.embed\_model = OpenAIEmbedding(model="text-embedding-3-small")

### Create the index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanternIndexDemo/#create-the-index)

Here we create an index backed by Postgres using the documents loaded previously. LanternVectorStore takes a few arguments.

In \[ \]:

Copied!

from sqlalchemy import make\_url

url \= make\_url(connection\_string)
vector\_store \= LanternVectorStore.from\_params(
    database\=db\_name,
    host\=url.host,
    password\=url.password,
    port\=url.port,
    user\=url.username,
    table\_name\="paul\_graham\_essay",
    embed\_dim\=1536,  \# openai embedding dimension
)

storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context, show\_progress\=True
)
query\_engine \= index.as\_query\_engine()

from sqlalchemy import make\_url url = make\_url(connection\_string) vector\_store = LanternVectorStore.from\_params( database=db\_name, host=url.host, password=url.password, port=url.port, user=url.username, table\_name="paul\_graham\_essay", embed\_dim=1536, # openai embedding dimension ) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context, show\_progress=True ) query\_engine = index.as\_query\_engine()

### Query the index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanternIndexDemo/#query-the-index)

We can now ask questions using our index.

In \[ \]:

Copied!

response \= query\_engine.query("What did the author do?")

response = query\_engine.query("What did the author do?")

In \[ \]:

Copied!

print(textwrap.fill(str(response), 100))

print(textwrap.fill(str(response), 100))

In \[ \]:

Copied!

response \= query\_engine.query("What happened in the mid 1980s?")

response = query\_engine.query("What happened in the mid 1980s?")

In \[ \]:

Copied!

print(textwrap.fill(str(response), 100))

print(textwrap.fill(str(response), 100))

### Querying existing index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanternIndexDemo/#querying-existing-index)

In \[ \]:

Copied!

vector\_store \= LanternVectorStore.from\_params(
    database\=db\_name,
    host\=url.host,
    password\=url.password,
    port\=url.port,
    user\=url.username,
    table\_name\="paul\_graham\_essay",
    embed\_dim\=1536,  \# openai embedding dimension
    m\=16,  \# HNSW M parameter
    ef\_construction\=128,  \# HNSW ef construction parameter
    ef\=64,  \# HNSW ef search parameter
)

\# Read more about HNSW parameters here: https://github.com/nmslib/hnswlib/blob/master/ALGO\_PARAMS.md

index \= VectorStoreIndex.from\_vector\_store(vector\_store\=vector\_store)
query\_engine \= index.as\_query\_engine()

vector\_store = LanternVectorStore.from\_params( database=db\_name, host=url.host, password=url.password, port=url.port, user=url.username, table\_name="paul\_graham\_essay", embed\_dim=1536, # openai embedding dimension m=16, # HNSW M parameter ef\_construction=128, # HNSW ef construction parameter ef=64, # HNSW ef search parameter ) # Read more about HNSW parameters here: https://github.com/nmslib/hnswlib/blob/master/ALGO\_PARAMS.md index = VectorStoreIndex.from\_vector\_store(vector\_store=vector\_store) query\_engine = index.as\_query\_engine()

In \[ \]:

Copied!

response \= query\_engine.query("What did the author do?")

response = query\_engine.query("What did the author do?")

In \[ \]:

Copied!

print(textwrap.fill(str(response), 100))

print(textwrap.fill(str(response), 100))

### Hybrid Search[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanternIndexDemo/#hybrid-search)

To enable hybrid search, you need to:

1.  pass in `hybrid_search=True` when constructing the `LanternVectorStore` (and optionally configure `text_search_config` with the desired language)
2.  pass in `vector_store_query_mode="hybrid"` when constructing the query engine (this config is passed to the retriever under the hood). You can also optionally set the `sparse_top_k` to configure how many results we should obtain from sparse text search (default is using the same value as `similarity_top_k`).

In \[ \]:

Copied!

from sqlalchemy import make\_url

url \= make\_url(connection\_string)
hybrid\_vector\_store \= LanternVectorStore.from\_params(
    database\=db\_name,
    host\=url.host,
    password\=url.password,
    port\=url.port,
    user\=url.username,
    table\_name\="paul\_graham\_essay\_hybrid\_search",
    embed\_dim\=1536,  \# openai embedding dimension
    hybrid\_search\=True,
    text\_search\_config\="english",
)

storage\_context \= StorageContext.from\_defaults(
    vector\_store\=hybrid\_vector\_store
)
hybrid\_index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

from sqlalchemy import make\_url url = make\_url(connection\_string) hybrid\_vector\_store = LanternVectorStore.from\_params( database=db\_name, host=url.host, password=url.password, port=url.port, user=url.username, table\_name="paul\_graham\_essay\_hybrid\_search", embed\_dim=1536, # openai embedding dimension hybrid\_search=True, text\_search\_config="english", ) storage\_context = StorageContext.from\_defaults( vector\_store=hybrid\_vector\_store ) hybrid\_index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

In \[ \]:

Copied!

hybrid\_query\_engine \= hybrid\_index.as\_query\_engine(
    vector\_store\_query\_mode\="hybrid", sparse\_top\_k\=2
)
hybrid\_response \= hybrid\_query\_engine.query(
    "Who does Paul Graham think of with the word schtick"
)

hybrid\_query\_engine = hybrid\_index.as\_query\_engine( vector\_store\_query\_mode="hybrid", sparse\_top\_k=2 ) hybrid\_response = hybrid\_query\_engine.query( "Who does Paul Graham think of with the word schtick" )

In \[ \]:

Copied!

print(hybrid\_response)

print(hybrid\_response)

Back to top

[Previous Lantern Vector Store (auto-retriever)](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanternAutoRetriever/)[Next Metal Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MetalIndexDemo/)
