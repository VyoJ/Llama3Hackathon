Title: DocArray InMemory Vector Store - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/DocArrayInMemoryIndexDemo/

Markdown Content:
DocArray InMemory Vector Store - LlamaIndex


[DocArrayInMemoryVectorStore](https://docs.docarray.org/user_guide/storing/index_in_memory/) is a document index provided by [Docarray](https://github.com/docarray/docarray) that stores documents in memory. It is a great starting point for small datasets, where you may not want to launch a database server.

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

\# stop huggingface warnings
os.environ\["TOKENIZERS\_PARALLELISM"\] \= "false"

\# Uncomment to see debug logs
\# logging.basicConfig(stream=sys.stdout, level=logging.INFO)
\# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from llama\_index.core import (
    GPTVectorStoreIndex,
    SimpleDirectoryReader,
    Document,
)
from llama\_index.vector\_stores.docarray import DocArrayInMemoryVectorStore
from IPython.display import Markdown, display

import os import sys import logging import textwrap import warnings warnings.filterwarnings("ignore") # stop huggingface warnings os.environ\["TOKENIZERS\_PARALLELISM"\] = "false" # Uncomment to see debug logs # logging.basicConfig(stream=sys.stdout, level=logging.INFO) # logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout)) from llama\_index.core import ( GPTVectorStoreIndex, SimpleDirectoryReader, Document, ) from llama\_index.vector\_stores.docarray import DocArrayInMemoryVectorStore from IPython.display import Markdown, display

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

Document ID: 1c21062a-50a3-4133-a0b1-75f837a953e5 Document Hash: 77ae91ab542f3abb308c4d7c77c9bc4c9ad0ccd63144802b7cbe7e1bb3a4094e

Initialization and indexing[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DocArrayInMemoryIndexDemo/#initialization-and-indexing)
--------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core import StorageContext

vector\_store \= DocArrayInMemoryVectorStore()
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= GPTVectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

from llama\_index.core import StorageContext vector\_store = DocArrayInMemoryVectorStore() storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = GPTVectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

Querying[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DocArrayInMemoryIndexDemo/#querying)
------------------------------------------------------------------------------------------------------------

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
language. He had invested a lot of time and energy into learning about AI and was disappointed to
find out that it was not going to get him the results he had hoped for.

Querying with filters[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DocArrayInMemoryIndexDemo/#querying-with-filters)
--------------------------------------------------------------------------------------------------------------------------------------

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

vector\_store \= DocArrayInMemoryVectorStore()
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

index \= GPTVectorStoreIndex(nodes, storage\_context\=storage\_context)

from llama\_index.core import StorageContext vector\_store = DocArrayInMemoryVectorStore() storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = GPTVectorStoreIndex(nodes, storage\_context=storage\_context)

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

\[NodeWithScore(node=Node(text='director: Francis Ford Coppola\\ntheme: Mafia\\n\\nThe Godfather', doc\_id='41c99963-b200-4ce6-a9c4-d06ffeabdbc5', embedding=None, doc\_hash='b770e43e6a94854a22dc01421d3d9ef6a94931c2b8dbbadf4fdb6eb6fbe41010', extra\_info=None, node\_info=None, relationships={<DocumentRelationship.SOURCE: '1'>: 'None'}), score=0.7681788983417586)\]

Back to top

[Previous DocArray Hnsw Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DocArrayHnswIndexDemo/)[Next DuckDB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DuckDBDemo/)
