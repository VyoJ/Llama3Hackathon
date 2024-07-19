Title: Supabase Vector Store - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/SupabaseVectorIndexDemo/

Markdown Content:
Supabase Vector Store - LlamaIndex


In this notebook we are going to show how to use [Vecs](https://supabase.github.io/vecs/) to perform vector searches in LlamaIndex.  
See [this guide](https://supabase.github.io/vecs/hosting/) for instructions on hosting a database on Supabase

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-supabase

%pip install llama-index-vector-stores-supabase

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import logging
import sys

\# Uncomment to see debug logs
\# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
\# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from llama\_index.core import SimpleDirectoryReader, Document, StorageContext
from llama\_index.core import VectorStoreIndex
from llama\_index.vector\_stores.supabase import SupabaseVectorStore
import textwrap

import logging import sys # Uncomment to see debug logs # logging.basicConfig(stream=sys.stdout, level=logging.DEBUG) # logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout)) from llama\_index.core import SimpleDirectoryReader, Document, StorageContext from llama\_index.core import VectorStoreIndex from llama\_index.vector\_stores.supabase import SupabaseVectorStore import textwrap

### Setup OpenAI[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SupabaseVectorIndexDemo/#setup-openai)

The first step is to configure the OpenAI key. It will be used to created embeddings for the documents loaded into the index

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "\[your\_openai\_api\_key\]"

import os os.environ\["OPENAI\_API\_KEY"\] = "\[your\_openai\_api\_key\]"

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

### Loading documents[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SupabaseVectorIndexDemo/#loading-documents)

Load the documents stored in the `./data/paul_graham/` using the SimpleDirectoryReader

In \[ \]:

Copied!

documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()
print(
    "Document ID:",
    documents\[0\].doc\_id,
    "Document Hash:",
    documents\[0\].doc\_hash,
)

documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data() print( "Document ID:", documents\[0\].doc\_id, "Document Hash:", documents\[0\].doc\_hash, )

Document ID: fb056993-ee9e-4463-80b4-32cf9509d1d8 Document Hash: 77ae91ab542f3abb308c4d7c77c9bc4c9ad0ccd63144802b7cbe7e1bb3a4094e

### Create an index backed by Supabase's vector store.[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SupabaseVectorIndexDemo/#create-an-index-backed-by-supabases-vector-store)

This will work with all Postgres providers that support pgvector. If the collection does not exist, we will attempt to create a new collection

> Note: you need to pass in the embedding dimension if not using OpenAI's text-embedding-ada-002, e.g. `vector_store = SupabaseVectorStore(..., dimension=...)`

In \[ \]:

Copied!

vector\_store \= SupabaseVectorStore(
    postgres\_connection\_string\=(
        "postgresql://<user>:<password>@<host>:<port>/<db\_name>"
    ),
    collection\_name\="base\_demo",
)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

vector\_store = SupabaseVectorStore( postgres\_connection\_string=( "postgresql://:@:/" ), collection\_name="base\_demo", ) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

### Query the index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SupabaseVectorIndexDemo/#query-the-index)

We can now ask questions using our index.

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("Who is the author?")

query\_engine = index.as\_query\_engine() response = query\_engine.query("Who is the author?")

/Users/suo/miniconda3/envs/llama/lib/python3.9/site-packages/vecs/collection.py:182: UserWarning: Query does not have a covering index for cosine\_distance. See Collection.create\_index
  warnings.warn(

In \[ \]:

Copied!

print(textwrap.fill(str(response), 100))

print(textwrap.fill(str(response), 100))

 The author of this text is Paul Graham.

In \[ \]:

Copied!

response \= query\_engine.query("What did the author do growing up?")

response = query\_engine.query("What did the author do growing up?")

In \[ \]:

Copied!

print(textwrap.fill(str(response), 100))

print(textwrap.fill(str(response), 100))

 The author grew up writing essays, learning Italian, exploring Florence, painting people, working
with computers, attending RISD, living in a rent-stabilized apartment, building an online store
builder, editing Lisp expressions, publishing essays online, writing essays, painting still life,
working on spam filters, cooking for groups, and buying a building in Cambridge.

Using metadata filters[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SupabaseVectorIndexDemo/#using-metadata-filters)
--------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core.schema import TextNode

nodes \= \[
    TextNode(
        \*\*{
            "text": "The Shawshank Redemption",
            "metadata": {
                "author": "Stephen King",
                "theme": "Friendship",
            },
        }
    ),
    TextNode(
        \*\*{
            "text": "The Godfather",
            "metadata": {
                "director": "Francis Ford Coppola",
                "theme": "Mafia",
            },
        }
    ),
    TextNode(
        \*\*{
            "text": "Inception",
            "metadata": {
                "director": "Christopher Nolan",
            },
        }
    ),
\]

from llama\_index.core.schema import TextNode nodes = \[ TextNode( \*\*{ "text": "The Shawshank Redemption", "metadata": { "author": "Stephen King", "theme": "Friendship", }, } ), TextNode( \*\*{ "text": "The Godfather", "metadata": { "director": "Francis Ford Coppola", "theme": "Mafia", }, } ), TextNode( \*\*{ "text": "Inception", "metadata": { "director": "Christopher Nolan", }, } ), \]

In \[ \]:

Copied!

vector\_store \= SupabaseVectorStore(
    postgres\_connection\_string\=(
        "postgresql://<user>:<password>@<host>:<port>/<db\_name>"
    ),
    collection\_name\="metadata\_filters\_demo",
)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex(nodes, storage\_context\=storage\_context)

vector\_store = SupabaseVectorStore( postgres\_connection\_string=( "postgresql://:@:/" ), collection\_name="metadata\_filters\_demo", ) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex(nodes, storage\_context=storage\_context)

Define metadata filters

In \[ \]:

Copied!

from llama\_index.core.vector\_stores import ExactMatchFilter, MetadataFilters

filters \= MetadataFilters(
    filters\=\[ExactMatchFilter(key\="theme", value\="Mafia")\]
)

from llama\_index.core.vector\_stores import ExactMatchFilter, MetadataFilters filters = MetadataFilters( filters=\[ExactMatchFilter(key="theme", value="Mafia")\] )

Retrieve from vector store with filters

In \[ \]:

Copied!

retriever \= index.as\_retriever(filters\=filters)
retriever.retrieve("What is inception about?")

retriever = index.as\_retriever(filters=filters) retriever.retrieve("What is inception about?")

Out\[ \]:

\[NodeWithScore(node=Node(text='The Godfather', doc\_id='f837ed85-aacb-4552-b88a-7c114a5be15d', embedding=None, doc\_hash='f8ee912e238a39fe2e620fb232fa27ade1e7f7c819b6d5b9cb26f3dddc75b6c0', extra\_info={'theme': 'Mafia', 'director': 'Francis Ford Coppola'}, node\_info={'\_node\_type': '1'}, relationships={}), score=0.20671339734643313)\]

Back to top

[Previous S3/R2 Storage](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexOnS3/)[Next Tair Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TairIndexDemo/)
