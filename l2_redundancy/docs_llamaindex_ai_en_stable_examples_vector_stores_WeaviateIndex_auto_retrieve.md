Title: Auto-Retrieval from a Weaviate Vector Database

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndex_auto_retriever/

Markdown Content:
Auto-Retrieval from a Weaviate Vector Database - LlamaIndex


This guide shows how to perform **auto-retrieval** in LlamaIndex with [Weaviate](https://weaviate.io/).

The Weaviate vector database supports a set of [metadata filters](https://weaviate.io/developers/weaviate/search/filters) in addition to a query string for semantic search. Given a natural language query, we first use a Large Language Model (LLM) to infer a set of metadata filters as well as the right query string to pass to the vector database (either can also be blank). This overall query bundle is then executed against the vector database.

This allows for more dynamic, expressive forms of retrieval beyond top-k semantic search. The relevant context for a given query may only require filtering on a metadata tag, or require a joint combination of filtering + semantic search within the filtered set, or just raw semantic search.

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndex_auto_retriever/#setup)
---------------------------------------------------------------------------------------------------------

We first define imports and define an empty Weaviate collection.

If you're opening this Notebook on Colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-weaviate

%pip install llama-index-vector-stores-weaviate

In \[ \]:

Copied!

!pip install llama\-index weaviate\-client

!pip install llama-index weaviate-client

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

We will be using GPT-4 for its reasoning capabilities to infer the metadata filters. Depending on your use case, `"gpt-3.5-turbo"` can work as well.

In \[ \]:

Copied!

\# set up OpenAI
import os
import getpass
import openai

os.environ\["OPENAI\_API\_KEY"\] \= getpass.getpass("OpenAI API Key:")
openai.api\_key \= os.environ\["OPENAI\_API\_KEY"\]

\# set up OpenAI import os import getpass import openai os.environ\["OPENAI\_API\_KEY"\] = getpass.getpass("OpenAI API Key:") openai.api\_key = os.environ\["OPENAI\_API\_KEY"\]

In \[ \]:

Copied!

from llama\_index.embeddings.openai import OpenAIEmbedding
from llama\_index.llms.openai import OpenAI
from llama\_index.core.settings import Settings

Settings.llm \= OpenAI(model\="gpt-4")
Settings.embed\_model \= OpenAIEmbedding()

from llama\_index.embeddings.openai import OpenAIEmbedding from llama\_index.llms.openai import OpenAI from llama\_index.core.settings import Settings Settings.llm = OpenAI(model="gpt-4") Settings.embed\_model = OpenAIEmbedding()

This Notebook uses Weaviate in [Embedded mode](https://weaviate.io/developers/weaviate/installation/embedded), which is supported on Linux and macOS.

If you prefer to try out Weaviate's fully managed service, [Weaviate Cloud Services (WCS)](https://weaviate.io/developers/weaviate/installation/weaviate-cloud-services), you can enable the code in the comments.

In \[ \]:

Copied!

import weaviate
from weaviate.embedded import EmbeddedOptions

\# Connect to Weaviate client in embedded mode
client \= weaviate.connect\_to\_embedded()

\# Enable this code if you want to use Weaviate Cloud Services instead of Embedded mode.
"""
import weaviate

\# cloud
cluster\_url = ""
api\_key = ""

client = weaviate.connect\_to\_wcs(cluster\_url=cluster\_url,
    auth\_credentials=weaviate.auth.AuthApiKey(api\_key), 
)

\# local
\# client = weaviate.connect\_to\_local()
"""

import weaviate from weaviate.embedded import EmbeddedOptions # Connect to Weaviate client in embedded mode client = weaviate.connect\_to\_embedded() # Enable this code if you want to use Weaviate Cloud Services instead of Embedded mode. """ import weaviate # cloud cluster\_url = "" api\_key = "" client = weaviate.connect\_to\_wcs(cluster\_url=cluster\_url, auth\_credentials=weaviate.auth.AuthApiKey(api\_key), ) # local # client = weaviate.connect\_to\_local() """

Defining Some Sample Data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndex_auto_retriever/#defining-some-sample-data)
-------------------------------------------------------------------------------------------------------------------------------------------------

We insert some sample nodes containing text chunks into the vector database. Note that each `TextNode` not only contains the text, but also metadata e.g. `category` and `country`. These metadata fields will get converted/stored as such in the underlying vector db.

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

Build Vector Index with Weaviate Vector Store[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndex_auto_retriever/#build-vector-index-with-weaviate-vector-store)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Here we load the data into the vector store. As mentioned above, both the text and metadata for each node will get converted into corresopnding representations in Weaviate. We can now run semantic queries and also metadata filtering on this data from Weaviate.

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, StorageContext
from llama\_index.vector\_stores.weaviate import WeaviateVectorStore

vector\_store \= WeaviateVectorStore(
    weaviate\_client\=client, index\_name\="LlamaIndex\_filter"
)

storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

from llama\_index.core import VectorStoreIndex, StorageContext from llama\_index.vector\_stores.weaviate import WeaviateVectorStore vector\_store = WeaviateVectorStore( weaviate\_client=client, index\_name="LlamaIndex\_filter" ) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store)

In \[ \]:

Copied!

index \= VectorStoreIndex(nodes, storage\_context\=storage\_context)

index = VectorStoreIndex(nodes, storage\_context=storage\_context)

Define `VectorIndexAutoRetriever`[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndex_auto_retriever/#define-vectorindexautoretriever)
---------------------------------------------------------------------------------------------------------------------------------------------------------------

We define our core `VectorIndexAutoRetriever` module. The module takes in `VectorStoreInfo`, which contains a structured description of the vector store collection and the metadata filters it supports. This information will then be used in the auto-retrieval prompt where the LLM infers metadata filters.

In \[ \]:

Copied!

from llama\_index.core.retrievers import VectorIndexAutoRetriever
from llama\_index.core.vector\_stores.types import MetadataInfo, VectorStoreInfo

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

from llama\_index.core.retrievers import VectorIndexAutoRetriever from llama\_index.core.vector\_stores.types import MetadataInfo, VectorStoreInfo vector\_store\_info = VectorStoreInfo( content\_info="brief biography of celebrities", metadata\_info=\[ MetadataInfo( name="category", type="str", description=( "Category of the celebrity, one of \[Sports, Entertainment," " Business, Music\]" ), ), MetadataInfo( name="country", type="str", description=( "Country of the celebrity, one of \[United States, Barbados," " Portugal\]" ), ), \], ) retriever = VectorIndexAutoRetriever( index, vector\_store\_info=vector\_store\_info )

Running over some sample data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndex_auto_retriever/#running-over-some-sample-data)
---------------------------------------------------------------------------------------------------------------------------------------------------------

We try running over some sample data. Note how metadata filters are inferred - this helps with more precise retrieval!

In \[ \]:

Copied!

response \= retriever.retrieve("Tell me about celebrities from United States")

response = retriever.retrieve("Tell me about celebrities from United States")

In \[ \]:

Copied!

print(response\[0\])

print(response\[0\])

In \[ \]:

Copied!

response \= retriever.retrieve(
    "Tell me about Sports celebrities from United States"
)

response = retriever.retrieve( "Tell me about Sports celebrities from United States" )

In \[ \]:

Copied!

print(response\[0\])

print(response\[0\])

Back to top

[Previous Weaviate Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo/)[Next Weaviate Vector Store Metadata Filter](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndex_metadata_filter/)
