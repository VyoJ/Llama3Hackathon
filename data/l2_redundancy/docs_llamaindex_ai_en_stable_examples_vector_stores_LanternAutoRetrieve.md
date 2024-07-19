Title: Lantern Vector Store (auto-retriever) - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanternAutoRetriever/

Markdown Content:
Lantern Vector Store (auto-retriever) - LlamaIndex


This guide shows how to perform **auto-retrieval** in LlamaIndex.

Many popular vector DBs support a set of metadata filters in addition to a query string for semantic search. Given a natural language query, we first use the LLM to infer a set of metadata filters as well as the right query string to pass to the vector DB (either can also be blank). This overall query bundle is then executed against the vector DB.

This allows for more dynamic, expressive forms of retrieval beyond top-k semantic search. The relevant context for a given query may only require filtering on a metadata tag, or require a joint combination of filtering + semantic search within the filtered set, or just raw semantic search.

We demonstrate an example with Lantern, but auto-retrieval is also implemented with many other vector DBs (e.g. Pinecone, Chroma, Weaviate, and more).

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-lantern

%pip install llama-index-vector-stores-lantern

In \[ \]:

Copied!

!pip install llama\-index psycopg2\-binary asyncpg

!pip install llama-index psycopg2-binary asyncpg

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

os.environ\["OPENAI\_API\_KEY"\] \= "<your-api-key>"

import openai

openai.api\_key \= os.environ\["OPENAI\_API\_KEY"\]

\# set up OpenAI import os os.environ\["OPENAI\_API\_KEY"\] = "" import openai openai.api\_key = os.environ\["OPENAI\_API\_KEY"\]

In \[ \]:

Copied!

import psycopg2
from sqlalchemy import make\_url

connection\_string \= "postgresql://postgres:postgres@localhost:5432"

url \= make\_url(connection\_string)

db\_name \= "postgres"
conn \= psycopg2.connect(connection\_string)
conn.autocommit \= True

import psycopg2 from sqlalchemy import make\_url connection\_string = "postgresql://postgres:postgres@localhost:5432" url = make\_url(connection\_string) db\_name = "postgres" conn = psycopg2.connect(connection\_string) conn.autocommit = True

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, StorageContext
from llama\_index.vector\_stores.lantern import LanternVectorStore

from llama\_index.core import VectorStoreIndex, StorageContext from llama\_index.vector\_stores.lantern import LanternVectorStore

In \[ \]:

Copied!

from llama\_index.core.schema import TextNode

nodes \= \[
    TextNode(
        text\=(
            "Michael Jordan is a retired professional basketball player,"
            " widely regarded as one of the greatest basketball players of all"
            " time."
        ),
        metadata\={
            "category": "Sports",
            "country": "United States",
        },
    ),
    TextNode(
        text\=(
            "Angelina Jolie is an American actress, filmmaker, and"
            " humanitarian. She has received numerous awards for her acting"
            " and is known for her philanthropic work."
        ),
        metadata\={
            "category": "Entertainment",
            "country": "United States",
        },
    ),
    TextNode(
        text\=(
            "Elon Musk is a business magnate, industrial designer, and"
            " engineer. He is the founder, CEO, and lead designer of SpaceX,"
            " Tesla, Inc., Neuralink, and The Boring Company."
        ),
        metadata\={
            "category": "Business",
            "country": "United States",
        },
    ),
    TextNode(
        text\=(
            "Rihanna is a Barbadian singer, actress, and businesswoman. She"
            " has achieved significant success in the music industry and is"
            " known for her versatile musical style."
        ),
        metadata\={
            "category": "Music",
            "country": "Barbados",
        },
    ),
    TextNode(
        text\=(
            "Cristiano Ronaldo is a Portuguese professional footballer who is"
            " considered one of the greatest football players of all time. He"
            " has won numerous awards and set multiple records during his"
            " career."
        ),
        metadata\={
            "category": "Sports",
            "country": "Portugal",
        },
    ),
\]

from llama\_index.core.schema import TextNode nodes = \[ TextNode( text=( "Michael Jordan is a retired professional basketball player," " widely regarded as one of the greatest basketball players of all" " time." ), metadata={ "category": "Sports", "country": "United States", }, ), TextNode( text=( "Angelina Jolie is an American actress, filmmaker, and" " humanitarian. She has received numerous awards for her acting" " and is known for her philanthropic work." ), metadata={ "category": "Entertainment", "country": "United States", }, ), TextNode( text=( "Elon Musk is a business magnate, industrial designer, and" " engineer. He is the founder, CEO, and lead designer of SpaceX," " Tesla, Inc., Neuralink, and The Boring Company." ), metadata={ "category": "Business", "country": "United States", }, ), TextNode( text=( "Rihanna is a Barbadian singer, actress, and businesswoman. She" " has achieved significant success in the music industry and is" " known for her versatile musical style." ), metadata={ "category": "Music", "country": "Barbados", }, ), TextNode( text=( "Cristiano Ronaldo is a Portuguese professional footballer who is" " considered one of the greatest football players of all time. He" " has won numerous awards and set multiple records during his" " career." ), metadata={ "category": "Sports", "country": "Portugal", }, ), \]

Build Vector Index with Lantern Vector Store[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanternAutoRetriever/#build-vector-index-with-lantern-vector-store)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Here we load the data into the vector store. As mentioned above, both the text and metadata for each node will get converted into corresponding representations in Lantern. We can now run semantic queries and also metadata filtering on this data from Lantern.

In \[ \]:

Copied!

vector\_store \= LanternVectorStore.from\_params(
    database\=db\_name,
    host\=url.host,
    password\=url.password,
    port\=url.port,
    user\=url.username,
    table\_name\="famous\_people",
    embed\_dim\=1536,  \# openai embedding dimension
    m\=16,  \# HNSW M parameter
    ef\_construction\=128,  \# HNSW ef construction parameter
    ef\=64,  \# HNSW ef search parameter
)

storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

vector\_store = LanternVectorStore.from\_params( database=db\_name, host=url.host, password=url.password, port=url.port, user=url.username, table\_name="famous\_people", embed\_dim=1536, # openai embedding dimension m=16, # HNSW M parameter ef\_construction=128, # HNSW ef construction parameter ef=64, # HNSW ef search parameter ) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store)

In \[ \]:

Copied!

index \= VectorStoreIndex(nodes, storage\_context\=storage\_context)

index = VectorStoreIndex(nodes, storage\_context=storage\_context)

Define `VectorIndexAutoRetriever`[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanternAutoRetriever/#define-vectorindexautoretriever)
-------------------------------------------------------------------------------------------------------------------------------------------------------

We define our core `VectorIndexAutoRetriever` module. The module takes in `VectorStoreInfo`, which contains a structured description of the vector store collection and the metadata filters it supports. This information will then be used in the auto-retrieval prompt where the LLM infers metadata filters.

In \[ \]:

Copied!

from llama\_index.core.retrievers import VectorIndexAutoRetriever
from llama\_index.core.vector\_stores import MetadataInfo, VectorStoreInfo

vector\_store\_info \= VectorStoreInfo(
    content\_info\="brief biography of celebrities",
    metadata\_info\=\[
        MetadataInfo(
            name\="category",
            type\="str",
            description\=(
                "Category of the celebrity, one of \[Sports, Entertainment,"
                " Business, Music\]"
            ),
        ),
        MetadataInfo(
            name\="country",
            type\="str",
            description\=(
                "Country of the celebrity, one of \[United States, Barbados,"
                " Portugal\]"
            ),
        ),
    \],
)
retriever \= VectorIndexAutoRetriever(
    index, vector\_store\_info\=vector\_store\_info
)

from llama\_index.core.retrievers import VectorIndexAutoRetriever from llama\_index.core.vector\_stores import MetadataInfo, VectorStoreInfo vector\_store\_info = VectorStoreInfo( content\_info="brief biography of celebrities", metadata\_info=\[ MetadataInfo( name="category", type="str", description=( "Category of the celebrity, one of \[Sports, Entertainment," " Business, Music\]" ), ), MetadataInfo( name="country", type="str", description=( "Country of the celebrity, one of \[United States, Barbados," " Portugal\]" ), ), \], ) retriever = VectorIndexAutoRetriever( index, vector\_store\_info=vector\_store\_info )

Running over some sample data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanternAutoRetriever/#running-over-some-sample-data)
-------------------------------------------------------------------------------------------------------------------------------------------------

We try running over some sample data. Note how metadata filters are inferred - this helps with more precise retrieval!

In \[ \]:

Copied!

retriever.retrieve("Tell me about two celebrities from United States")

retriever.retrieve("Tell me about two celebrities from United States")

Back to top

[Previous LanceDB Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanceDBIndexDemo/)[Next Lantern Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanternIndexDemo/)
