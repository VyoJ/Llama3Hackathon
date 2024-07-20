Title: Epsilla Vector Store - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/EpsillaIndexDemo/

Markdown Content:
Epsilla Vector Store - LlamaIndex


In this notebook we are going to show how to use [Epsilla](https://www.epsilla.com/) to perform vector searches in LlamaIndex.

As a prerequisite, you need to have a running Epsilla vector database (for example, through our docker image), and install the `pyepsilla` package. View full docs at [docs](https://epsilla-inc.gitbook.io/epsilladb/quick-start)

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-epsilla

%pip install llama-index-vector-stores-epsilla

In \[ \]:

Copied!

!pip/pip3 install pyepsilla

!pip/pip3 install pyepsilla

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import logging
import sys

\# Uncomment to see debug logs
\# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
\# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from llama\_index.core import SimpleDirectoryReader, Document, StorageContext
from llama\_index.core import VectorStoreIndex
from llama\_index.vector\_stores.epsilla import EpsillaVectorStore
import textwrap

import logging import sys # Uncomment to see debug logs # logging.basicConfig(stream=sys.stdout, level=logging.DEBUG) # logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout)) from llama\_index.core import SimpleDirectoryReader, Document, StorageContext from llama\_index.core import VectorStoreIndex from llama\_index.vector\_stores.epsilla import EpsillaVectorStore import textwrap

### Setup OpenAI[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/EpsillaIndexDemo/#setup-openai)

Lets first begin by adding the openai api key. It will be used to created embeddings for the documents loaded into the index.

In \[ \]:

Copied!

import openai
import getpass

OPENAI\_API\_KEY \= getpass.getpass("OpenAI API Key:")
openai.api\_key \= OPENAI\_API\_KEY

import openai import getpass OPENAI\_API\_KEY = getpass.getpass("OpenAI API Key:") openai.api\_key = OPENAI\_API\_KEY

### Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/EpsillaIndexDemo/#download-data)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

### Loading documents[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/EpsillaIndexDemo/#loading-documents)

Load documents stored in the `/data/paul_graham` folder using the SimpleDirectoryReader.

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()
print(f"Total documents: {len(documents)}")
print(f"First document, id: {documents\[0\].doc\_id}")
print(f"First document, hash: {documents\[0\].hash}")

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data() print(f"Total documents: {len(documents)}") print(f"First document, id: {documents\[0\].doc\_id}") print(f"First document, hash: {documents\[0\].hash}")

Total documents: 1
First document, id: ac7f23f0-ce15-4d94-a0a2-5020fa87df61
First document, hash: 4c702b4df575421e1d1af4b1fd50511b226e0c9863dbfffeccb8b689b8448f35

### Create the index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/EpsillaIndexDemo/#create-the-index)

Here we create an index backed by Epsilla using the documents loaded previously. EpsillaVectorStore takes a few arguments.

*   client (Any): Epsilla client to connect to.
    
*   collection\_name (str, optional): Which collection to use. Defaults to "llama\_collection".
    
*   db\_path (str, optional): The path where the database will be persisted. Defaults to "/tmp/langchain-epsilla".
    
*   db\_name (str, optional): Give a name to the loaded database. Defaults to "langchain\_store".
    
*   dimension (int, optional): The dimension of the embeddings. If not provided, collection creation will be done on first insert. Defaults to None.
    
*   overwrite (bool, optional): Whether to overwrite existing collection with same name. Defaults to False.
    

Epsilla vectordb is running with default host "localhost" and port "8888".

In \[ \]:

Copied!

\# Create an index over the documnts
from pyepsilla import vectordb

client \= vectordb.Client()
vector\_store \= EpsillaVectorStore(client\=client, db\_path\="/tmp/llamastore")

storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

\# Create an index over the documnts from pyepsilla import vectordb client = vectordb.Client() vector\_store = EpsillaVectorStore(client=client, db\_path="/tmp/llamastore") storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

\[INFO\] Connected to localhost:8888 successfully.

### Query the data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/EpsillaIndexDemo/#query-the-data)

Now we have our document stored in the index, we can ask questions against the index.

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("Who is the author?")
print(textwrap.fill(str(response), 100))

query\_engine = index.as\_query\_engine() response = query\_engine.query("Who is the author?") print(textwrap.fill(str(response), 100))

The author of the given context information is Paul Graham.

In \[ \]:

Copied!

response \= query\_engine.query("How did the author learn about AI?")
print(textwrap.fill(str(response), 100))

response = query\_engine.query("How did the author learn about AI?") print(textwrap.fill(str(response), 100))

The author learned about AI through various sources. One source was a novel called "The Moon is a
Harsh Mistress" by Heinlein, which featured an intelligent computer called Mike. Another source was
a PBS documentary that showed Terry Winograd using SHRDLU, a program that could understand natural
language. These experiences sparked the author's interest in AI and motivated them to start learning
about it, including teaching themselves Lisp, which was regarded as the language of AI at the time.

Next, let's try to overwrite the previous data.

In \[ \]:

Copied!

vector\_store \= EpsillaVectorStore(client\=client, overwrite\=True)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
single\_doc \= Document(text\="Epsilla is the vector database we are using.")
index \= VectorStoreIndex.from\_documents(
    \[single\_doc\],
    storage\_context\=storage\_context,
)

query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("Who is the author?")
print(textwrap.fill(str(response), 100))

vector\_store = EpsillaVectorStore(client=client, overwrite=True) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) single\_doc = Document(text="Epsilla is the vector database we are using.") index = VectorStoreIndex.from\_documents( \[single\_doc\], storage\_context=storage\_context, ) query\_engine = index.as\_query\_engine() response = query\_engine.query("Who is the author?") print(textwrap.fill(str(response), 100))

There is no information provided about the author in the given context.

In \[ \]:

Copied!

response \= query\_engine.query("What vector database is being used?")
print(textwrap.fill(str(response), 100))

response = query\_engine.query("What vector database is being used?") print(textwrap.fill(str(response), 100))

Epsilla is the vector database being used.

Next, let's add more data to existing collection.

In \[ \]:

Copied!

vector\_store \= EpsillaVectorStore(client\=client, overwrite\=False)
index \= VectorStoreIndex.from\_vector\_store(vector\_store\=vector\_store)
for doc in documents:
    index.insert(document\=doc)

query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("Who is the author?")
print(textwrap.fill(str(response), 100))

vector\_store = EpsillaVectorStore(client=client, overwrite=False) index = VectorStoreIndex.from\_vector\_store(vector\_store=vector\_store) for doc in documents: index.insert(document=doc) query\_engine = index.as\_query\_engine() response = query\_engine.query("Who is the author?") print(textwrap.fill(str(response), 100))

The author of the given context information is Paul Graham.

In \[ \]:

Copied!

response \= query\_engine.query("What vector database is being used?")
print(textwrap.fill(str(response), 100))

response = query\_engine.query("What vector database is being used?") print(textwrap.fill(str(response), 100))

Epsilla is the vector database being used.

Back to top

[Previous Elasticsearch](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Elasticsearch_demo/)[Next Faiss Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/FaissIndexDemo/)
