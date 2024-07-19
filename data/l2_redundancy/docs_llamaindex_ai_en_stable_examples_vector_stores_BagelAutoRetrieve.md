Title: Bagel Vector Store - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/BagelAutoRetriever/

Markdown Content:
Bagel Vector Store - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-bagel
%pip install llama\-index
%pip install bagelML

%pip install llama-index-vector-stores-bagel %pip install llama-index %pip install bagelML

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

In \[ \]:

Copied!

import os

\# Set environment variable
os.environ\["BAGEL\_API\_KEY"\] \= getpass.getpass("Bagel API Key:")

import os # Set environment variable os.environ\["BAGEL\_API\_KEY"\] = getpass.getpass("Bagel API Key:")

In \[ \]:

Copied!

import bagel
from bagel import Settings

import bagel from bagel import Settings

In \[ \]:

Copied!

server\_settings \= Settings(
    bagel\_api\_impl\="rest", bagel\_server\_host\="api.bageldb.ai"
)

client \= bagel.Client(server\_settings)

collection \= client.get\_or\_create\_cluster(
    "testing\_embeddings\_3", embedding\_model\="custom", dimension\=1536
)

server\_settings = Settings( bagel\_api\_impl="rest", bagel\_server\_host="api.bageldb.ai" ) client = bagel.Client(server\_settings) collection = client.get\_or\_create\_cluster( "testing\_embeddings\_3", embedding\_model="custom", dimension=1536 )

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, StorageContext
from llama\_index.vector\_stores.bagel import BagelVectorStore

from llama\_index.core import VectorStoreIndex, StorageContext from llama\_index.vector\_stores.bagel import BagelVectorStore

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

In \[ \]:

Copied!

vector\_store \= BagelVectorStore(collection\=collection)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

vector\_store = BagelVectorStore(collection=collection) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store)

In \[ \]:

Copied!

index \= VectorStoreIndex(nodes, storage\_context\=storage\_context)

index = VectorStoreIndex(nodes, storage\_context=storage\_context)

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

In \[ \]:

Copied!

retriever.retrieve("celebrity")

retriever.retrieve("celebrity")

Back to top

[Previous Azure CosmosDB MongoDB Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureCosmosDBMongoDBvCoreDemo/)[Next Bagel Network](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BagelIndexDemo/)
