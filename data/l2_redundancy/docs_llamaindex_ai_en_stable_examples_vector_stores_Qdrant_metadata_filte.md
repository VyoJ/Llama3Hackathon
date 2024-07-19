Title: Qdrant Vector Store - Metadata Filter

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/Qdrant_metadata_filter/

Markdown Content:
Qdrant Vector Store - Metadata Filter - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-qdrant

%pip install llama-index-vector-stores-qdrant

In \[ \]:

Copied!

!pip install llama\-index qdrant\_client

!pip install llama-index qdrant\_client

Build a Pinecone Index and connect to it

In \[ \]:

Copied!

import qdrant\_client
from llama\_index.core import VectorStoreIndex
from llama\_index.vector\_stores.qdrant import QdrantVectorStore

client \= qdrant\_client.QdrantClient(
    \# you can use :memory: mode for fast and light-weight experiments,
    \# it does not require to have Qdrant deployed anywhere
    \# but requires qdrant-client >= 1.1.1
    location\=":memory:"
    \# otherwise set Qdrant instance address with:
    \# uri="http://<host>:<port>"
    \# set API KEY for Qdrant Cloud
    \# api\_key="<qdrant-api-key>",
)

import qdrant\_client from llama\_index.core import VectorStoreIndex from llama\_index.vector\_stores.qdrant import QdrantVectorStore client = qdrant\_client.QdrantClient( # you can use :memory: mode for fast and light-weight experiments, # it does not require to have Qdrant deployed anywhere # but requires qdrant-client >= 1.1.1 location=":memory:" # otherwise set Qdrant instance address with: # uri="http://:" # set API KEY for Qdrant Cloud # api\_key="", )

Build the PineconeVectorStore and VectorStoreIndex

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

import os

from llama\_index.core import StorageContext

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

vector\_store \= QdrantVectorStore(
    client\=client, collection\_name\="test\_collection\_1"
)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex(nodes, storage\_context\=storage\_context)

import os from llama\_index.core import StorageContext os.environ\["OPENAI\_API\_KEY"\] = "sk-..." vector\_store = QdrantVectorStore( client=client, collection\_name="test\_collection\_1" ) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex(nodes, storage\_context=storage\_context)

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
        MetadataFilter(key\="theme", operator\=FilterOperator.EQ, value\="Mafia"),
    \]
)

from llama\_index.core.vector\_stores import ( MetadataFilter, MetadataFilters, FilterOperator, ) filters = MetadataFilters( filters=\[ MetadataFilter(key="theme", operator=FilterOperator.EQ, value="Mafia"), \] )

Retrieve from vector store with filters

In \[ \]:

Copied!

retriever \= index.as\_retriever(filters\=filters)
retriever.retrieve("What is inception about?")

retriever = index.as\_retriever(filters=filters) retriever.retrieve("What is inception about?")

\[FieldCondition(key='theme', match=MatchValue(value='Mafia'), range=None, geo\_bounding\_box=None, geo\_radius=None, geo\_polygon=None, values\_count=None)\]

Out\[ \]:

\[NodeWithScore(node=TextNode(id\_='050c085d-6d91-4080-9fd6-3f874a528970', embedding=None, metadata={'director': 'Francis Ford Coppola', 'theme': 'Mafia', 'year': 1972}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, hash='bfa890174187ddaed4876803691ed605463de599f5493f095a03b8d83364f1ef', text='The Godfather', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.7620959333946706),
 NodeWithScore(node=TextNode(id\_='11d0043a-aba3-4ffe-84cb-3f17988759be', embedding=None, metadata={'author': 'Harper Lee', 'theme': 'Mafia', 'year': 1960}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, hash='3475334d04bbe4606cb77728d5dc0784f16c8db3f190f3692e6310906c821927', text='To Kill a Mockingbird', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.7340329162691743)\]

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

\[FieldCondition(key='theme', match=MatchValue(value='Fiction'), range=None, geo\_bounding\_box=None, geo\_radius=None, geo\_polygon=None, values\_count=None)\]
\[FieldCondition(key='theme', match=MatchValue(value='Fiction'), range=None, geo\_bounding\_box=None, geo\_radius=None, geo\_polygon=None, values\_count=None), FieldCondition(key='year', match=None, range=Range(lt=None, gt=1997.0, gte=None, lte=None), geo\_bounding\_box=None, geo\_radius=None, geo\_polygon=None, values\_count=None)\]

Out\[ \]:

\[NodeWithScore(node=TextNode(id\_='1be42402-518f-4e88-9860-12cfec9f5ed2', embedding=None, metadata={'director': 'Christopher Nolan', 'theme': 'Fiction', 'year': 2010}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, hash='7937eb153ccc78a3329560f37d90466ba748874df6b0303b3b8dd3c732aa7688', text='Inception', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.7649987694994126)\]

Use keyword arguments specific to pinecone

In \[ \]:

Copied!

retriever \= index.as\_retriever(
    vector\_store\_kwargs\={"filter": {"theme": "Mafia"}}
)
retriever.retrieve("What is inception about?")

retriever = index.as\_retriever( vector\_store\_kwargs={"filter": {"theme": "Mafia"}} ) retriever.retrieve("What is inception about?")

Out\[ \]:

\[NodeWithScore(node=TextNode(id\_='1be42402-518f-4e88-9860-12cfec9f5ed2', embedding=None, metadata={'director': 'Christopher Nolan', 'theme': 'Fiction', 'year': 2010}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, hash='7937eb153ccc78a3329560f37d90466ba748874df6b0303b3b8dd3c732aa7688', text='Inception', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.841150534139415),
 NodeWithScore(node=TextNode(id\_='ee4d3b32-7675-49bc-bc49-04011d62cf7c', embedding=None, metadata={'author': 'J.K. Rowling', 'theme': 'Fiction', 'year': 1997}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, hash='1b24f5e9fb6f18cc893e833af8d5f28ff805a6361fc0838a3015c287510d29a3', text="Harry Potter and the Sorcerer's Stone", start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.7661930751179629)\]

Back to top

[Previous Qdrant Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/QdrantIndexDemo/)[Next Qdrant Vector Store - Default Qdrant Filters](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Qdrant_using_qdrant_filters/)
