Title: Auto-Retrieval from a Vector Database

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/elasticsearch_auto_retriever/

Markdown Content:
Auto-Retrieval from a Vector Database - LlamaIndex


This guide shows how to perform **auto-retrieval** in LlamaIndex.

Many popular vector dbs support a set of metadata filters in addition to a query string for semantic search. Given a natural language query, we first use the LLM to infer a set of metadata filters as well as the right query string to pass to the vector db (either can also be blank). This overall query bundle is then executed against the vector db.

This allows for more dynamic, expressive forms of retrieval beyond top-k semantic search. The relevant context for a given query may only require filtering on a metadata tag, or require a joint combination of filtering + semantic search within the filtered set, or just raw semantic search.

We demonstrate an example with Elasticsearch, but auto-retrieval is also implemented with many other vector dbs (e.g. Pinecone, Weaviate, and more).

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/elasticsearch_auto_retriever/#setup)
---------------------------------------------------------------------------------------------------------

We first define imports.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-elasticsearch

%pip install llama-index-vector-stores-elasticsearch

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

In \[ \]:

Copied!

\# set up OpenAI
import os
import getpass

os.environ\["OPENAI\_API\_KEY"\] \= getpass.getpass("OpenAI API Key:")
import openai

openai.api\_key \= os.environ\["OPENAI\_API\_KEY"\]

\# set up OpenAI import os import getpass os.environ\["OPENAI\_API\_KEY"\] = getpass.getpass("OpenAI API Key:") import openai openai.api\_key = os.environ\["OPENAI\_API\_KEY"\]

Defining Some Sample Data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/elasticsearch_auto_retriever/#defining-some-sample-data)
-------------------------------------------------------------------------------------------------------------------------------------------------

We insert some sample nodes containing text chunks into the vector database. Note that each `TextNode` not only contains the text, but also metadata e.g. `category` and `country`. These metadata fields will get converted/stored as such in the underlying vector db.

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, StorageContext
from llama\_index.vector\_stores.elasticsearch import ElasticsearchStore

from llama\_index.core import VectorStoreIndex, StorageContext from llama\_index.vector\_stores.elasticsearch import ElasticsearchStore

In \[ \]:

Copied!

from llama\_index.core.schema import TextNode

nodes \= \[
    TextNode(
        text\=(
            "A bunch of scientists bring back dinosaurs and mayhem breaks"
            " loose"
        ),
        metadata\={"year": 1993, "rating": 7.7, "genre": "science fiction"},
    ),
    TextNode(
        text\=(
            "Leo DiCaprio gets lost in a dream within a dream within a dream"
            " within a ..."
        ),
        metadata\={
            "year": 2010,
            "director": "Christopher Nolan",
            "rating": 8.2,
        },
    ),
    TextNode(
        text\=(
            "A psychologist / detective gets lost in a series of dreams within"
            " dreams within dreams and Inception reused the idea"
        ),
        metadata\={"year": 2006, "director": "Satoshi Kon", "rating": 8.6},
    ),
    TextNode(
        text\=(
            "A bunch of normal-sized women are supremely wholesome and some"
            " men pine after them"
        ),
        metadata\={"year": 2019, "director": "Greta Gerwig", "rating": 8.3},
    ),
    TextNode(
        text\="Toys come alive and have a blast doing so",
        metadata\={"year": 1995, "genre": "animated"},
    ),
\]

from llama\_index.core.schema import TextNode nodes = \[ TextNode( text=( "A bunch of scientists bring back dinosaurs and mayhem breaks" " loose" ), metadata={"year": 1993, "rating": 7.7, "genre": "science fiction"}, ), TextNode( text=( "Leo DiCaprio gets lost in a dream within a dream within a dream" " within a ..." ), metadata={ "year": 2010, "director": "Christopher Nolan", "rating": 8.2, }, ), TextNode( text=( "A psychologist / detective gets lost in a series of dreams within" " dreams within dreams and Inception reused the idea" ), metadata={"year": 2006, "director": "Satoshi Kon", "rating": 8.6}, ), TextNode( text=( "A bunch of normal-sized women are supremely wholesome and some" " men pine after them" ), metadata={"year": 2019, "director": "Greta Gerwig", "rating": 8.3}, ), TextNode( text="Toys come alive and have a blast doing so", metadata={"year": 1995, "genre": "animated"}, ), \]

Build Vector Index with Elasticsearch Vector Store[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/elasticsearch_auto_retriever/#build-vector-index-with-elasticsearch-vector-store)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Here we load the data into the vector store. As mentioned above, both the text and metadata for each node will get converted into corresponding representation in Elasticsearch. We can now run semantic queries and also metadata filtering on this data from Elasticsearch.

In \[ \]:

Copied!

vector\_store \= ElasticsearchStore(
    index\_name\="auto\_retriever\_movies", es\_url\="http://localhost:9200"
)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

vector\_store = ElasticsearchStore( index\_name="auto\_retriever\_movies", es\_url="http://localhost:9200" ) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store)

In \[ \]:

Copied!

index \= VectorStoreIndex(nodes, storage\_context\=storage\_context)

index = VectorStoreIndex(nodes, storage\_context=storage\_context)

Define `VectorIndexAutoRetriever`[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/elasticsearch_auto_retriever/#define-vectorindexautoretriever)
---------------------------------------------------------------------------------------------------------------------------------------------------------------

We define our core `VectorIndexAutoRetriever` module. The module takes in `VectorStoreInfo`, which contains a structured description of the vector store collection and the metadata filters it supports. This information will then be used in the auto-retrieval prompt where the LLM infers metadata filters.

In \[ \]:

Copied!

from llama\_index.core.retrievers import VectorIndexAutoRetriever
from llama\_index.core.vector\_stores import MetadataInfo, VectorStoreInfo

vector\_store\_info \= VectorStoreInfo(
    content\_info\="Brief summary of a movie",
    metadata\_info\=\[
        MetadataInfo(
            name\="genre",
            description\="The genre of the movie",
            type\="string or list\[string\]",
        ),
        MetadataInfo(
            name\="year",
            description\="The year the movie was released",
            type\="integer",
        ),
        MetadataInfo(
            name\="director",
            description\="The name of the movie director",
            type\="string",
        ),
        MetadataInfo(
            name\="rating",
            description\="A 1-10 rating for the movie",
            type\="float",
        ),
    \],
)
retriever \= VectorIndexAutoRetriever(
    index, vector\_store\_info\=vector\_store\_info
)

from llama\_index.core.retrievers import VectorIndexAutoRetriever from llama\_index.core.vector\_stores import MetadataInfo, VectorStoreInfo vector\_store\_info = VectorStoreInfo( content\_info="Brief summary of a movie", metadata\_info=\[ MetadataInfo( name="genre", description="The genre of the movie", type="string or list\[string\]", ), MetadataInfo( name="year", description="The year the movie was released", type="integer", ), MetadataInfo( name="director", description="The name of the movie director", type="string", ), MetadataInfo( name="rating", description="A 1-10 rating for the movie", type="float", ), \], ) retriever = VectorIndexAutoRetriever( index, vector\_store\_info=vector\_store\_info )

Running over some sample data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/elasticsearch_auto_retriever/#running-over-some-sample-data)
---------------------------------------------------------------------------------------------------------------------------------------------------------

We try running over some sample data. Note how metadata filters are inferred - this helps with more precise retrieval!

In \[ \]:

Copied!

retriever.retrieve(
    "What are 2 movies by Christopher Nolan were made before 2020?"
)

retriever.retrieve( "What are 2 movies by Christopher Nolan were made before 2020?" )

In \[ \]:

Copied!

retriever.retrieve("Has Andrei Tarkovsky directed any science fiction movies")

retriever.retrieve("Has Andrei Tarkovsky directed any science fiction movies")

INFO:llama\_index.indices.vector\_store.retrievers.auto\_retriever.auto\_retriever:Using query str: science fiction
Using query str: science fiction
INFO:llama\_index.indices.vector\_store.retrievers.auto\_retriever.auto\_retriever:Using filters: {'director': 'Andrei Tarkovsky'}
Using filters: {'director': 'Andrei Tarkovsky'}
INFO:llama\_index.indices.vector\_store.retrievers.auto\_retriever.auto\_retriever:Using top\_k: 2
Using top\_k: 2
INFO:elastic\_transport.transport:POST http://localhost:9200/auto\_retriever\_movies/\_search \[status:200 duration:0.042s\]
POST http://localhost:9200/auto\_retriever\_movies/\_search \[status:200 duration:0.042s\]

Out\[ \]:

\[\]

Back to top

[Previous Chroma Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/chroma_metadata_filter/)[Next Guide: Using Vector Store Index with Existing Pinecone Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/existing_data/pinecone_existing_data/)
