Title: Qdrant Vector Store - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/QdrantIndexDemo/

Markdown Content:
Qdrant Vector Store - LlamaIndex


#### Creating a Qdrant client[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/QdrantIndexDemo/#creating-a-qdrant-client)

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-qdrant llama\-index\-readers\-file llama\-index\-embeddings\-fastembed llama\-index\-llms\-openai

%pip install llama-index-vector-stores-qdrant llama-index-readers-file llama-index-embeddings-fastembed llama-index-llms-openai

In \[ \]:

Copied!

import logging
import sys
import os

import qdrant\_client
from IPython.display import Markdown, display
from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.core import StorageContext
from llama\_index.vector\_stores.qdrant import QdrantVectorStore
from llama\_index.embeddings.fastembed import FastEmbedEmbedding
from llama\_index.core import Settings

Settings.embed\_model \= FastEmbedEmbedding(model\_name\="BAAI/bge-base-en-v1.5")

import logging import sys import os import qdrant\_client from IPython.display import Markdown, display from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.core import StorageContext from llama\_index.vector\_stores.qdrant import QdrantVectorStore from llama\_index.embeddings.fastembed import FastEmbedEmbedding from llama\_index.core import Settings Settings.embed\_model = FastEmbedEmbedding(model\_name="BAAI/bge-base-en-v1.5")

If running for the first, time, install the dependencies using:

```
!pip install -U qdrant_client fastembed
```

Set your OpenAI key for authenticating the LLM

Follow these set the OpenAI API key to the OPENAI\_API\_KEY environment variable -

1.  Using Terminal

In \[ \]:

Copied!

export OPENAI\_API\_KEY\=your\_api\_key\_here

export OPENAI\_API\_KEY=your\_api\_key\_here

2.  Using IPython Magic Command in Jupyter Notebook

In \[ \]:

Copied!

%env OPENAI\_API\_KEY\=<YOUR\_OPENAI\_API\_KEY\>

%env OPENAI\_API\_KEY=

3.  Using Python Script

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "your\_api\_key\_here"

import os os.environ\["OPENAI\_API\_KEY"\] = "your\_api\_key\_here"

Note: It's generally recommended to set sensitive information like API keys as environment variables rather than hardcoding them into scripts.

In \[ \]:

Copied!

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

#### Load the documents[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/QdrantIndexDemo/#load-the-documents)

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data()

#### Build the VectorStoreIndex[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/QdrantIndexDemo/#build-the-vectorstoreindex)

In \[ \]:

Copied!

client \= qdrant\_client.QdrantClient(
    \# you can use :memory: mode for fast and light-weight experiments,
    \# it does not require to have Qdrant deployed anywhere
    \# but requires qdrant-client >= 1.1.1
    \# location=":memory:"
    \# otherwise set Qdrant instance address with:
    \# url="http://<host>:<port>"
    \# otherwise set Qdrant instance with host and port:
    host\="localhost",
    port\=6333
    \# set API KEY for Qdrant Cloud
    \# api\_key="<qdrant-api-key>",
)

client = qdrant\_client.QdrantClient( # you can use :memory: mode for fast and light-weight experiments, # it does not require to have Qdrant deployed anywhere # but requires qdrant-client >= 1.1.1 # location=":memory:" # otherwise set Qdrant instance address with: # url="http://:" # otherwise set Qdrant instance with host and port: host="localhost", port=6333 # set API KEY for Qdrant Cloud # api\_key="", )

In \[ \]:

Copied!

vector\_store \= QdrantVectorStore(client\=client, collection\_name\="paul\_graham")
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents,
    storage\_context\=storage\_context,
)

vector\_store = QdrantVectorStore(client=client, collection\_name="paul\_graham") storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context, )

#### Query Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/QdrantIndexDemo/#query-index)

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did the author do growing up?")

\# set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine() response = query\_engine.query("What did the author do growing up?")

In \[ \]:

Copied!

display(Markdown(f"<b>{response}</b>"))

display(Markdown(f"**{response}**"))

**The author worked on writing and programming before college.**

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query(
    "What did the author do after his time at Viaweb?"
)

\# set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine() response = query\_engine.query( "What did the author do after his time at Viaweb?" )

In \[ \]:

Copied!

display(Markdown(f"<b>{response}</b>"))

display(Markdown(f"**{response}**"))

**The author arranged to do freelance work for a group that did projects for customers after his time at Viaweb.**

#### Build the VectorStoreIndex asynchronously[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/QdrantIndexDemo/#build-the-vectorstoreindex-asynchronously)

In \[ \]:

Copied!

\# To connect to the same event-loop,
\# allows async events to run on notebook

import nest\_asyncio

nest\_asyncio.apply()

\# To connect to the same event-loop, # allows async events to run on notebook import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

aclient \= qdrant\_client.AsyncQdrantClient(
    \# you can use :memory: mode for fast and light-weight experiments,
    \# it does not require to have Qdrant deployed anywhere
    \# but requires qdrant-client >= 1.1.1
    location\=":memory:"
    \# otherwise set Qdrant instance address with:
    \# uri="http://<host>:<port>"
    \# set API KEY for Qdrant Cloud
    \# api\_key="<qdrant-api-key>",
)

aclient = qdrant\_client.AsyncQdrantClient( # you can use :memory: mode for fast and light-weight experiments, # it does not require to have Qdrant deployed anywhere # but requires qdrant-client >= 1.1.1 location=":memory:" # otherwise set Qdrant instance address with: # uri="http://:" # set API KEY for Qdrant Cloud # api\_key="", )

In \[ \]:

Copied!

vector\_store \= QdrantVectorStore(
    collection\_name\="paul\_graham",
    client\=client,
    aclient\=aclient,
    prefer\_grpc\=True,
)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents,
    storage\_context\=storage\_context,
    use\_async\=True,
)

vector\_store = QdrantVectorStore( collection\_name="paul\_graham", client=client, aclient=aclient, prefer\_grpc=True, ) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context, use\_async=True, )

#### Async Query Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/QdrantIndexDemo/#async-query-index)

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(use\_async\=True)
response \= await query\_engine.aquery("What did the author do growing up?")

query\_engine = index.as\_query\_engine(use\_async=True) response = await query\_engine.aquery("What did the author do growing up?")

In \[ \]:

Copied!

display(Markdown(f"<b>{response}</b>"))

display(Markdown(f"**{response}**"))

**The author worked on writing short stories and programming, particularly on an IBM 1401 computer in 9th grade using an early version of Fortran. Later, the author transitioned to working on microcomputers, starting with a TRS-80 in about 1980, where they wrote simple games, programs, and a word processor.**

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine(use\_async\=True)
response \= await query\_engine.aquery(
    "What did the author do after his time at Viaweb?"
)

\# set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine(use\_async=True) response = await query\_engine.aquery( "What did the author do after his time at Viaweb?" )

In \[ \]:

Copied!

display(Markdown(f"<b>{response}</b>"))

display(Markdown(f"**{response}**"))

**The author went on to co-found Y Combinator after his time at Viaweb.**

Back to top

[Previous Pinecone Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PineconeIndexDemo/)[Next Qdrant Vector Store - Metadata Filter](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Qdrant_metadata_filter/)
