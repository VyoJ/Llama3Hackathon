Title: Guide: Using Vector Store Index with Existing Weaviate Vector Store

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/existing_data/weaviate_existing_data/

Markdown Content:
Guide: Using Vector Store Index with Existing Weaviate Vector Store - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-weaviate
%pip install llama\-index\-embeddings\-openai

%pip install llama-index-vector-stores-weaviate %pip install llama-index-embeddings-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import weaviate

import weaviate

In \[ \]:

Copied!

client \= weaviate.Client("https://test-cluster-bbn8vqsn.weaviate.network")

client = weaviate.Client("https://test-cluster-bbn8vqsn.weaviate.network")

Prepare Sample "Existing" Weaviate Vector Store[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/existing_data/weaviate_existing_data/#prepare-sample-existing-weaviate-vector-store)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Define schema[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/existing_data/weaviate_existing_data/#define-schema)

We create a schema for "Book" class, with 4 properties: title (str), author (str), content (str), and year (int)

In \[ \]:

Copied!

try:
    client.schema.delete\_class("Book")
except:
    pass

try: client.schema.delete\_class("Book") except: pass

In \[ \]:

Copied!

schema \= {
    "classes": \[
        {
            "class": "Book",
            "properties": \[
                {"name": "title", "dataType": \["text"\]},
                {"name": "author", "dataType": \["text"\]},
                {"name": "content", "dataType": \["text"\]},
                {"name": "year", "dataType": \["int"\]},
            \],
        },
    \]
}

if not client.schema.contains(schema):
    client.schema.create(schema)

schema = { "classes": \[ { "class": "Book", "properties": \[ {"name": "title", "dataType": \["text"\]}, {"name": "author", "dataType": \["text"\]}, {"name": "content", "dataType": \["text"\]}, {"name": "year", "dataType": \["int"\]}, \], }, \] } if not client.schema.contains(schema): client.schema.create(schema)

### Define sample data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/existing_data/weaviate_existing_data/#define-sample-data)

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

### Add data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/existing_data/weaviate_existing_data/#add-data)

We add the sample books to our Weaviate "Book" class (with embedding of content field

In \[ \]:

Copied!

from llama\_index.embeddings.openai import OpenAIEmbedding

embed\_model \= OpenAIEmbedding()

from llama\_index.embeddings.openai import OpenAIEmbedding embed\_model = OpenAIEmbedding()

In \[ \]:

Copied!

with client.batch as batch:
    for book in books:
        vector \= embed\_model.get\_text\_embedding(book\["content"\])
        batch.add\_data\_object(
            data\_object\=book, class\_name\="Book", vector\=vector
        )

with client.batch as batch: for book in books: vector = embed\_model.get\_text\_embedding(book\["content"\]) batch.add\_data\_object( data\_object=book, class\_name="Book", vector=vector )

Query Against "Existing" Weaviate Vector Store[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/existing_data/weaviate_existing_data/#query-against-existing-weaviate-vector-store)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.vector\_stores.weaviate import WeaviateVectorStore
from llama\_index.core import VectorStoreIndex
from llama\_index.core.response.pprint\_utils import pprint\_source\_node

from llama\_index.vector\_stores.weaviate import WeaviateVectorStore from llama\_index.core import VectorStoreIndex from llama\_index.core.response.pprint\_utils import pprint\_source\_node

You must properly specify a "index\_name" that matches the desired Weaviate class and select a class property as the "text" field.

In \[ \]:

Copied!

vector\_store \= WeaviateVectorStore(
    weaviate\_client\=client, index\_name\="Book", text\_key\="content"
)

vector\_store = WeaviateVectorStore( weaviate\_client=client, index\_name="Book", text\_key="content" )

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

Document ID: cf927ce7-0672-4696-8aae-7e77b33b9659
Similarity: None
Text: author: Harper Lee title: To Kill a Mockingbird year: 1960  To
Kill a Mockingbird is a novel by Harper Lee published in 1960......

The remaining fields should be loaded as metadata (in `metadata`)

In \[ \]:

Copied!

nodes\[0\].node.metadata

nodes\[0\].node.metadata

Out\[ \]:

{'author': 'Harper Lee', 'title': 'To Kill a Mockingbird', 'year': 1960}

Back to top

[Previous Guide: Using Vector Store Index with Existing Pinecone Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/existing_data/pinecone_existing_data/)[Next Neo4j Vector Store - Metadata Filter](https://docs.llamaindex.ai/en/stable/examples/vector_stores/neo4j_metadata_filter/)
