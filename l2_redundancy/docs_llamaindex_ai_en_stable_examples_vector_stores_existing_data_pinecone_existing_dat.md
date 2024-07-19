Title: Guide: Using Vector Store Index with Existing Pinecone Vector Store

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/existing_data/pinecone_existing_data/

Markdown Content:
Guide: Using Vector Store Index with Existing Pinecone Vector Store - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-embeddings\-openai
%pip install llama\-index\-vector\-stores\-pinecone

%pip install llama-index-embeddings-openai %pip install llama-index-vector-stores-pinecone

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import os
import pinecone

import os import pinecone

In \[ \]:

Copied!

api\_key \= os.environ\["PINECONE\_API\_KEY"\]
pinecone.init(api\_key\=api\_key, environment\="eu-west1-gcp")

api\_key = os.environ\["PINECONE\_API\_KEY"\] pinecone.init(api\_key=api\_key, environment="eu-west1-gcp")

Prepare Sample "Existing" Pinecone Vector Store[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/existing_data/pinecone_existing_data/#prepare-sample-existing-pinecone-vector-store)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Create index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/existing_data/pinecone_existing_data/#create-index)

In \[ \]:

Copied!

indexes \= pinecone.list\_indexes()
print(indexes)

indexes = pinecone.list\_indexes() print(indexes)

\['quickstart-index'\]

In \[ \]:

Copied!

if "quickstart-index" not in indexes:
    \# dimensions are for text-embedding-ada-002
    pinecone.create\_index(
        "quickstart-index", dimension\=1536, metric\="euclidean", pod\_type\="p1"
    )

if "quickstart-index" not in indexes: # dimensions are for text-embedding-ada-002 pinecone.create\_index( "quickstart-index", dimension=1536, metric="euclidean", pod\_type="p1" )

In \[ \]:

Copied!

pinecone\_index \= pinecone.Index("quickstart-index")

pinecone\_index = pinecone.Index("quickstart-index")

In \[ \]:

Copied!

pinecone\_index.delete(deleteAll\="true")

pinecone\_index.delete(deleteAll="true")

Out\[ \]:

{}

### Define sample data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/existing_data/pinecone_existing_data/#define-sample-data)

We create 4 sample books

In \[ \]:

Copied!

books \= \[
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "content": (
            "To Kill a Mockingbird is a novel by Harper Lee published in"
            " 1960..."
        ),
        "year": 1960,
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "content": (
            "1984 is a dystopian novel by George Orwell published in 1949..."
        ),
        "year": 1949,
    },
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "content": (
            "The Great Gatsby is a novel by F. Scott Fitzgerald published in"
            " 1925..."
        ),
        "year": 1925,
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "content": (
            "Pride and Prejudice is a novel by Jane Austen published in"
            " 1813..."
        ),
        "year": 1813,
    },
\]

books = \[ { "title": "To Kill a Mockingbird", "author": "Harper Lee", "content": ( "To Kill a Mockingbird is a novel by Harper Lee published in" " 1960..." ), "year": 1960, }, { "title": "1984", "author": "George Orwell", "content": ( "1984 is a dystopian novel by George Orwell published in 1949..." ), "year": 1949, }, { "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "content": ( "The Great Gatsby is a novel by F. Scott Fitzgerald published in" " 1925..." ), "year": 1925, }, { "title": "Pride and Prejudice", "author": "Jane Austen", "content": ( "Pride and Prejudice is a novel by Jane Austen published in" " 1813..." ), "year": 1813, }, \]

### Add data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/existing_data/pinecone_existing_data/#add-data)

We add the sample books to our Weaviate "Book" class (with embedding of content field

In \[ \]:

Copied!

import uuid
from llama\_index.embeddings.openai import OpenAIEmbedding

embed\_model \= OpenAIEmbedding()

import uuid from llama\_index.embeddings.openai import OpenAIEmbedding embed\_model = OpenAIEmbedding()

In \[ \]:

Copied!

entries \= \[\]
for book in books:
    vector \= embed\_model.get\_text\_embedding(book\["content"\])
    entries.append(
        {"id": str(uuid.uuid4()), "values": vector, "metadata": book}
    )
pinecone\_index.upsert(entries)

entries = \[\] for book in books: vector = embed\_model.get\_text\_embedding(book\["content"\]) entries.append( {"id": str(uuid.uuid4()), "values": vector, "metadata": book} ) pinecone\_index.upsert(entries)

Out\[ \]:

{'upserted\_count': 4}

Query Against "Existing" Pinecone Vector Store[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/existing_data/pinecone_existing_data/#query-against-existing-pinecone-vector-store)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.vector\_stores.pinecone import PineconeVectorStore
from llama\_index.core import VectorStoreIndex
from llama\_index.core.response.pprint\_utils import pprint\_source\_node

from llama\_index.vector\_stores.pinecone import PineconeVectorStore from llama\_index.core import VectorStoreIndex from llama\_index.core.response.pprint\_utils import pprint\_source\_node

You must properly select a class property as the "text" field.

In \[ \]:

Copied!

vector\_store \= PineconeVectorStore(
    pinecone\_index\=pinecone\_index, text\_key\="content"
)

vector\_store = PineconeVectorStore( pinecone\_index=pinecone\_index, text\_key="content" )

In \[ \]:

Copied!

retriever \= VectorStoreIndex.from\_vector\_store(vector\_store).as\_retriever(
    similarity\_top\_k\=1
)

retriever = VectorStoreIndex.from\_vector\_store(vector\_store).as\_retriever( similarity\_top\_k=1 )

In \[ \]:

Copied!

nodes \= retriever.retrieve("What is that book about a bird again?")

nodes = retriever.retrieve("What is that book about a bird again?")

Let's inspect the retrieved node. We can see that the book data is loaded as LlamaIndex `Node` objects, with the "content" field as the main text.

In \[ \]:

Copied!

pprint\_source\_node(nodes\[0\])

pprint\_source\_node(nodes\[0\])

Document ID: 07e47f1d-cb90-431b-89c7-35462afcda28
Similarity: 0.797243237
Text: author: Harper Lee title: To Kill a Mockingbird year: 1960.0  To
Kill a Mockingbird is a novel by Harper Lee published in 1960......

The remaining fields should be loaded as metadata (in `metadata`)

In \[ \]:

Copied!

nodes\[0\].node.metadata

nodes\[0\].node.metadata

Out\[ \]:

{'author': 'Harper Lee', 'title': 'To Kill a Mockingbird', 'year': 1960.0}

Back to top

[Previous Auto-Retrieval from a Vector Database](https://docs.llamaindex.ai/en/stable/examples/vector_stores/elasticsearch_auto_retriever/)[Next Guide: Using Vector Store Index with Existing Weaviate Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/existing_data/weaviate_existing_data/)
