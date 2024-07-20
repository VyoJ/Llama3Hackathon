Title: DocArray Hnsw Vector Store - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/DocArrayHnswIndexDemo/

Markdown Content:
DocArray Hnsw Vector Store - LlamaIndex


[DocArrayHnswVectorStore](https://docs.docarray.org/user_guide/storing/index_hnswlib/) is a lightweight Document Index implementation provided by [DocArray](https://github.com/docarray/docarray) that runs fully locally and is best suited for small- to medium-sized datasets. It stores vectors on disk in hnswlib, and stores all other data in SQLite.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-docarray

%pip install llama-index-vector-stores-docarray

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import os
import sys
import logging
import textwrap

import warnings

warnings.filterwarnings("ignore")

\# stop h|uggingface warnings
os.environ\["TOKENIZERS\_PARALLELISM"\] \= "false"

\# Uncomment to see debug logs
\# logging.basicConfig(stream=sys.stdout, level=logging.INFO)
\# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from llama\_index.core import (
    GPTVectorStoreIndex,
    SimpleDirectoryReader,
    Document,
)
from llama\_index.vector\_stores.docarray import DocArrayHnswVectorStore
from IPython.display import Markdown, display

import os import sys import logging import textwrap import warnings warnings.filterwarnings("ignore") # stop h|uggingface warnings os.environ\["TOKENIZERS\_PARALLELISM"\] = "false" # Uncomment to see debug logs # logging.basicConfig(stream=sys.stdout, level=logging.INFO) # logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout)) from llama\_index.core import ( GPTVectorStoreIndex, SimpleDirectoryReader, Document, ) from llama\_index.vector\_stores.docarray import DocArrayHnswVectorStore from IPython.display import Markdown, display

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "<your openai key>"

import os os.environ\["OPENAI\_API\_KEY"\] = ""

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()
print(
    "Document ID:",
    documents\[0\].doc\_id,
    "Document Hash:",
    documents\[0\].doc\_hash,
)

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data() print( "Document ID:", documents\[0\].doc\_id, "Document Hash:", documents\[0\].doc\_hash, )

Document ID: 07d9ca27-ded0-46fa-9165-7e621216fd47 Document Hash: 77ae91ab542f3abb308c4d7c77c9bc4c9ad0ccd63144802b7cbe7e1bb3a4094e

Initialization and indexing[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DocArrayHnswIndexDemo/#initialization-and-indexing)
----------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core import StorageContext

vector\_store \= DocArrayHnswVectorStore(work\_dir\="hnsw\_index")
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= GPTVectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

from llama\_index.core import StorageContext vector\_store = DocArrayHnswVectorStore(work\_dir="hnsw\_index") storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = GPTVectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

Querying[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DocArrayHnswIndexDemo/#querying)
--------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did the author do growing up?")
print(textwrap.fill(str(response), 100))

\# set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine() response = query\_engine.query("What did the author do growing up?") print(textwrap.fill(str(response), 100))

Token indices sequence length is longer than the specified maximum sequence length for this model (1830 > 1024). Running this sequence through the model will result in indexing errors

 Growing up, the author wrote short stories, programmed on an IBM 1401, and nagged his father to buy
him a TRS-80 microcomputer. He wrote simple games, a program to predict how high his model rockets
would fly, and a word processor. He also studied philosophy in college, but switched to AI after
becoming bored with it. He then took art classes at Harvard and applied to art schools, eventually
attending RISD.

In \[ \]:

Copied!

response \= query\_engine.query("What was a hard moment for the author?")
print(textwrap.fill(str(response), 100))

response = query\_engine.query("What was a hard moment for the author?") print(textwrap.fill(str(response), 100))

 A hard moment for the author was when he realized that the AI programs of the time were a hoax and
that there was an unbridgeable gap between what they could do and actually understanding natural
language.

Querying with filters[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DocArrayHnswIndexDemo/#querying-with-filters)
----------------------------------------------------------------------------------------------------------------------------------

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

from llama\_index.core import StorageContext

vector\_store \= DocArrayHnswVectorStore(work\_dir\="hnsw\_filters")
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

index \= GPTVectorStoreIndex(nodes, storage\_context\=storage\_context)

from llama\_index.core import StorageContext vector\_store = DocArrayHnswVectorStore(work\_dir="hnsw\_filters") storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = GPTVectorStoreIndex(nodes, storage\_context=storage\_context)

In \[ \]:

Copied!

from llama\_index.core.vector\_stores import ExactMatchFilter, MetadataFilters

filters \= MetadataFilters(
    filters\=\[ExactMatchFilter(key\="theme", value\="Mafia")\]
)

retriever \= index.as\_retriever(filters\=filters)
retriever.retrieve("What is inception about?")

from llama\_index.core.vector\_stores import ExactMatchFilter, MetadataFilters filters = MetadataFilters( filters=\[ExactMatchFilter(key="theme", value="Mafia")\] ) retriever = index.as\_retriever(filters=filters) retriever.retrieve("What is inception about?")

Out\[ \]:

\[NodeWithScore(node=Node(text='director: Francis Ford Coppola\\ntheme: Mafia\\n\\nThe Godfather', doc\_id='d96456bf-ef6e-4c1b-bdb8-e90a37d881f3', embedding=None, doc\_hash='b770e43e6a94854a22dc01421d3d9ef6a94931c2b8dbbadf4fdb6eb6fbe41010', extra\_info=None, node\_info=None, relationships={<DocumentRelationship.SOURCE: '1'>: 'None'}), score=0.4634347)\]

In \[ \]:

Copied!

\# remove created indices
import os, shutil

hnsw\_dirs \= \["hnsw\_filters", "hnsw\_index"\]
for dir in hnsw\_dirs:
    if os.path.exists(dir):
        shutil.rmtree(dir)

\# remove created indices import os, shutil hnsw\_dirs = \["hnsw\_filters", "hnsw\_index"\] for dir in hnsw\_dirs: if os.path.exists(dir): shutil.rmtree(dir)

Back to top

[Previous Deep Lake Vector Store Quickstart](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DeepLakeIndexDemo/)[Next DocArray InMemory Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DocArrayInMemoryIndexDemo/)
