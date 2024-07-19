Title: Neo4j Vector Store - Metadata Filter

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/neo4j_metadata_filter/

Markdown Content:
Neo4j Vector Store - Metadata Filter - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-neo4jvector

%pip install llama-index-vector-stores-neo4jvector

In \[ \]:

Copied!

\# !pip install llama-index>=0.9.31 neo4j

\# !pip install llama-index>=0.9.31 neo4j

In \[ \]:

Copied!

import logging
import sys
import os

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys import os logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

Build a Neo4j vector Index and connect to it

In \[ \]:

Copied!

import os
from llama\_index.vector\_stores.neo4jvector import Neo4jVectorStore

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

username \= "neo4j"
password \= "password"
url \= "bolt://localhost:7687"
embed\_dim \= 1536  \# Dimensions are for text-embedding-ada-002

vector\_store \= Neo4jVectorStore(username, password, url, embed\_dim)

import os from llama\_index.vector\_stores.neo4jvector import Neo4jVectorStore os.environ\["OPENAI\_API\_KEY"\] = "sk-..." username = "neo4j" password = "password" url = "bolt://localhost:7687" embed\_dim = 1536 # Dimensions are for text-embedding-ada-002 vector\_store = Neo4jVectorStore(username, password, url, embed\_dim)

INFO:numexpr.utils:Note: NumExpr detected 16 cores but "NUMEXPR\_MAX\_THREADS" not set, so enforcing safe limit of 8.
Note: NumExpr detected 16 cores but "NUMEXPR\_MAX\_THREADS" not set, so enforcing safe limit of 8.
INFO:numexpr.utils:NumExpr defaulting to 8 threads.
NumExpr defaulting to 8 threads.

Build the VectorStoreIndex

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, StorageContext
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

from llama\_index.core import VectorStoreIndex, StorageContext from llama\_index.core.schema import TextNode nodes = \[ TextNode( text="The Shawshank Redemption", metadata={ "author": "Stephen King", "theme": "Friendship", "year": 1994, }, ), TextNode( text="The Godfather", metadata={ "director": "Francis Ford Coppola", "theme": "Mafia", "year": 1972, }, ), TextNode( text="Inception", metadata={ "director": "Christopher Nolan", "theme": "Fiction", "year": 2010, }, ), TextNode( text="To Kill a Mockingbird", metadata={ "author": "Harper Lee", "theme": "Mafia", "year": 1960, }, ), TextNode( text="1984", metadata={ "author": "George Orwell", "theme": "Totalitarianism", "year": 1949, }, ), TextNode( text="The Great Gatsby", metadata={ "author": "F. Scott Fitzgerald", "theme": "The American Dream", "year": 1925, }, ), TextNode( text="Harry Potter and the Sorcerer's Stone", metadata={ "author": "J.K. Rowling", "theme": "Fiction", "year": 1997, }, ), \]

In \[ \]:

Copied!

storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex(nodes, storage\_context\=storage\_context)

storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex(nodes, storage\_context=storage\_context)

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"

Define metadata filters

In \[ \]:

Copied!

from llama\_index.core.vector\_stores import (
    MetadataFilter,
    MetadataFilters,
    FilterOperator,
)

filters \= MetadataFilters(
    filters\=\[
        MetadataFilter(
            key\="theme", operator\=FilterOperator.EQ, value\="Fiction"
        ),
    \]
)

from llama\_index.core.vector\_stores import ( MetadataFilter, MetadataFilters, FilterOperator, ) filters = MetadataFilters( filters=\[ MetadataFilter( key="theme", operator=FilterOperator.EQ, value="Fiction" ), \] )

Retrieve from vector store with filters

In \[ \]:

Copied!

retriever \= index.as\_retriever(filters\=filters)
retriever.retrieve("What is inception about?")

retriever = index.as\_retriever(filters=filters) retriever.retrieve("What is inception about?")

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"

Out\[ \]:

\[NodeWithScore(node=TextNode(id\_='814e5f2a-2150-4bae-8a59-fa728379e978', embedding=None, metadata={'director': 'Christopher Nolan', 'theme': 'Fiction', 'year': 2010}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='Inception', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.9202238321304321),
 NodeWithScore(node=TextNode(id\_='fc1df8cc-f1d3-4a7b-8c21-f83b18463758', embedding=None, metadata={'author': 'J.K. Rowling', 'theme': 'Fiction', 'year': 1997}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text="Harry Potter and the Sorcerer's Stone", start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.8823964595794678)\]

Multiple Metadata Filters with `AND` condition

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

\[NodeWithScore(node=TextNode(id\_='814e5f2a-2150-4bae-8a59-fa728379e978', embedding=None, metadata={'director': 'Christopher Nolan', 'theme': 'Fiction', 'year': 2010}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='Inception', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.8818434476852417)\]

Multiple Metadata Filters with `OR` condition

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

\[NodeWithScore(node=TextNode(id\_='fc1df8cc-f1d3-4a7b-8c21-f83b18463758', embedding=None, metadata={'author': 'J.K. Rowling', 'theme': 'Fiction', 'year': 1997}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text="Harry Potter and the Sorcerer's Stone", start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.9242331385612488),
 NodeWithScore(node=TextNode(id\_='814e5f2a-2150-4bae-8a59-fa728379e978', embedding=None, metadata={'director': 'Christopher Nolan', 'theme': 'Fiction', 'year': 2010}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='Inception', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.8818434476852417)\]

Back to top

[Previous Guide: Using Vector Store Index with Existing Weaviate Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/existing_data/weaviate_existing_data/)[Next A Simple to Advanced Guide with Auto-Retrieval (with Pinecone + Arize Phoenix)](https://docs.llamaindex.ai/en/stable/examples/vector_stores/pinecone_auto_retriever/)
