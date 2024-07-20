Title: Chroma Vector Store - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/chroma_metadata_filter/

Markdown Content:
Chroma Vector Store - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-chroma

%pip install llama-index-vector-stores-chroma

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

#### Creating a Chroma Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/chroma_metadata_filter/#creating-a-chroma-index)

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

In \[ \]:

Copied!

import os
import getpass

\# os.environ\["OPENAI\_API\_KEY"\] = getpass.getpass("OpenAI API Key:")
import openai

openai.api\_key \= "sk-"

import os import getpass # os.environ\["OPENAI\_API\_KEY"\] = getpass.getpass("OpenAI API Key:") import openai openai.api\_key = "sk-"

In \[ \]:

Copied!

import chromadb

import chromadb

In \[ \]:

Copied!

chroma\_client \= chromadb.EphemeralClient()
chroma\_collection \= chroma\_client.create\_collection("quickstart")

chroma\_client = chromadb.EphemeralClient() chroma\_collection = chroma\_client.create\_collection("quickstart")

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex
from llama\_index.vector\_stores.chroma import ChromaVectorStore
from IPython.display import Markdown, display

from llama\_index.core import VectorStoreIndex from llama\_index.vector\_stores.chroma import ChromaVectorStore from IPython.display import Markdown, display

In \[ \]:

Copied!

from llama\_index.core.schema import TextNode

nodes \= \[
    TextNode(
        text\="The Shawshank Redemption",
        metadata\={
            "author": "Stephen King",
            "theme": "Friendship",
            "year": 1994,
        },
    ),
    TextNode(
        text\="The Godfather",
        metadata\={
            "director": "Francis Ford Coppola",
            "theme": "Mafia",
            "year": 1972,
        },
    ),
    TextNode(
        text\="Inception",
        metadata\={
            "director": "Christopher Nolan",
            "theme": "Fiction",
            "year": 2010,
        },
    ),
    TextNode(
        text\="To Kill a Mockingbird",
        metadata\={
            "author": "Harper Lee",
            "theme": "Mafia",
            "year": 1960,
        },
    ),
    TextNode(
        text\="1984",
        metadata\={
            "author": "George Orwell",
            "theme": "Totalitarianism",
            "year": 1949,
        },
    ),
    TextNode(
        text\="The Great Gatsby",
        metadata\={
            "author": "F. Scott Fitzgerald",
            "theme": "The American Dream",
            "year": 1925,
        },
    ),
    TextNode(
        text\="Harry Potter and the Sorcerer's Stone",
        metadata\={
            "author": "J.K. Rowling",
            "theme": "Fiction",
            "year": 1997,
        },
    ),
\]

from llama\_index.core.schema import TextNode nodes = \[ TextNode( text="The Shawshank Redemption", metadata={ "author": "Stephen King", "theme": "Friendship", "year": 1994, }, ), TextNode( text="The Godfather", metadata={ "director": "Francis Ford Coppola", "theme": "Mafia", "year": 1972, }, ), TextNode( text="Inception", metadata={ "director": "Christopher Nolan", "theme": "Fiction", "year": 2010, }, ), TextNode( text="To Kill a Mockingbird", metadata={ "author": "Harper Lee", "theme": "Mafia", "year": 1960, }, ), TextNode( text="1984", metadata={ "author": "George Orwell", "theme": "Totalitarianism", "year": 1949, }, ), TextNode( text="The Great Gatsby", metadata={ "author": "F. Scott Fitzgerald", "theme": "The American Dream", "year": 1925, }, ), TextNode( text="Harry Potter and the Sorcerer's Stone", metadata={ "author": "J.K. Rowling", "theme": "Fiction", "year": 1997, }, ), \]

In \[ \]:

Copied!

from llama\_index.core import StorageContext

vector\_store \= ChromaVectorStore(chroma\_collection\=chroma\_collection)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

from llama\_index.core import StorageContext vector\_store = ChromaVectorStore(chroma\_collection=chroma\_collection) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store)

In \[ \]:

Copied!

index \= VectorStoreIndex(nodes, storage\_context\=storage\_context)

index = VectorStoreIndex(nodes, storage\_context=storage\_context)

One Exact Match Filter[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/chroma_metadata_filter/#one-exact-match-filter)
-------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core.vector\_stores import (
    MetadataFilter,
    MetadataFilters,
    FilterOperator,
)

filters \= MetadataFilters(
    filters\=\[
        MetadataFilter(key\="theme", operator\=FilterOperator.EQ, value\="Mafia"),
    \]
)

retriever \= index.as\_retriever(filters\=filters)
retriever.retrieve("What is inception about?")

from llama\_index.core.vector\_stores import ( MetadataFilter, MetadataFilters, FilterOperator, ) filters = MetadataFilters( filters=\[ MetadataFilter(key="theme", operator=FilterOperator.EQ, value="Mafia"), \] ) retriever = index.as\_retriever(filters=filters) retriever.retrieve("What is inception about?")

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"

Out\[ \]:

\[NodeWithScore(node=TextNode(id\_='f343294f-4cd5-4f1c-acbf-19490aa95efb', embedding=None, metadata={'director': 'Francis Ford Coppola', 'theme': 'Mafia', 'year': 1972}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, hash='79563896e320da86be371351f55d903acdcfb3229368a6622f6be6e929e8b7cc', text='The Godfather', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.6215522669166147),
 NodeWithScore(node=TextNode(id\_='7910d5cd-7871-46e5-b71a-0dae1797aee1', embedding=None, metadata={'author': 'Harper Lee', 'theme': 'Mafia', 'year': 1960}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, hash='0a1875c24455356c77eedd8eddd39035ec622959b59d2296eff56d42019a0c00', text='To Kill a Mockingbird', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.5873631114046581)\]

Multiple Exact Match Metadata Filters[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/chroma_metadata_filter/#multiple-exact-match-metadata-filters)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core.vector\_stores import ExactMatchFilter, MetadataFilters

filters \= MetadataFilters(
    filters\=\[
        MetadataFilter(key\="theme", value\="Mafia"),
        MetadataFilter(key\="year", value\=1972),
    \]
)

retriever \= index.as\_retriever(filters\=filters)
retriever.retrieve("What is inception about?")

from llama\_index.core.vector\_stores import ExactMatchFilter, MetadataFilters filters = MetadataFilters( filters=\[ MetadataFilter(key="theme", value="Mafia"), MetadataFilter(key="year", value=1972), \] ) retriever = index.as\_retriever(filters=filters) retriever.retrieve("What is inception about?")

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"

Out\[ \]:

\[NodeWithScore(node=TextNode(id\_='f343294f-4cd5-4f1c-acbf-19490aa95efb', embedding=None, metadata={'director': 'Francis Ford Coppola', 'theme': 'Mafia', 'year': 1972}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, hash='79563896e320da86be371351f55d903acdcfb3229368a6622f6be6e929e8b7cc', text='The Godfather', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.6215522669166147)\]

Multiple Metadata Filters with `AND` condition[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/chroma_metadata_filter/#multiple-metadata-filters-with-and-condition)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core.vector\_stores import FilterOperator, FilterCondition

filters \= MetadataFilters(
    filters\=\[
        MetadataFilter(key\="theme", value\="Fiction"),
        MetadataFilter(key\="year", value\=1997, operator\=FilterOperator.GT),
    \],
    condition\=FilterCondition.AND,
)

retriever \= index.as\_retriever(filters\=filters)
retriever.retrieve("Harry Potter?")

from llama\_index.core.vector\_stores import FilterOperator, FilterCondition filters = MetadataFilters( filters=\[ MetadataFilter(key="theme", value="Fiction"), MetadataFilter(key="year", value=1997, operator=FilterOperator.GT), \], condition=FilterCondition.AND, ) retriever = index.as\_retriever(filters=filters) retriever.retrieve("Harry Potter?")

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"

Out\[ \]:

\[NodeWithScore(node=TextNode(id\_='b71ce5e8-353e-42c6-94b3-d0a11370aaba', embedding=None, metadata={'director': 'Christopher Nolan', 'theme': 'Fiction', 'year': 2010}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, hash='110b4ab08da17685bdc3d53aecf6085a535dd00a43612eed991bce8074aa36a9', text='Inception', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.6250006485226994)\]

Multiple Metadata Filters with `OR` condition[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/chroma_metadata_filter/#multiple-metadata-filters-with-or-condition)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core.vector\_stores import FilterOperator, FilterCondition

filters \= MetadataFilters(
    filters\=\[
        MetadataFilter(key\="theme", value\="Fiction"),
        MetadataFilter(key\="year", value\=1997, operator\=FilterOperator.GT),
    \],
    condition\=FilterCondition.OR,
)

retriever \= index.as\_retriever(filters\=filters)
retriever.retrieve("Harry Potter?")

from llama\_index.core.vector\_stores import FilterOperator, FilterCondition filters = MetadataFilters( filters=\[ MetadataFilter(key="theme", value="Fiction"), MetadataFilter(key="year", value=1997, operator=FilterOperator.GT), \], condition=FilterCondition.OR, ) retriever = index.as\_retriever(filters=filters) retriever.retrieve("Harry Potter?")

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"

Out\[ \]:

\[NodeWithScore(node=TextNode(id\_='6b0e9499-9f4d-4637-ab2a-460e5c870948', embedding=None, metadata={'author': 'J.K. Rowling', 'theme': 'Fiction', 'year': 1997}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, hash='a2656c2bc96ed472bb0ed3ea81075042e9860987f3156428789d07079e019ed0', text="Harry Potter and the Sorcerer's Stone", start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.7405548668973673),
 NodeWithScore(node=TextNode(id\_='b71ce5e8-353e-42c6-94b3-d0a11370aaba', embedding=None, metadata={'director': 'Christopher Nolan', 'theme': 'Fiction', 'year': 2010}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, hash='110b4ab08da17685bdc3d53aecf6085a535dd00a43612eed991bce8074aa36a9', text='Inception', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.6250006485226994)\]

Back to top

[Previous Auto-Retrieval from a Vector Database](https://docs.llamaindex.ai/en/stable/examples/vector_stores/chroma_auto_retriever/)[Next Auto-Retrieval from a Vector Database](https://docs.llamaindex.ai/en/stable/examples/vector_stores/elasticsearch_auto_retriever/)

Hi, how can I help you?

🦙
