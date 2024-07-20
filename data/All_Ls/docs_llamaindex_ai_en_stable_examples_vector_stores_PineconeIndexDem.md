Title: Pinecone Vector Store - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/PineconeIndexDemo/

Markdown Content:
Pinecone Vector Store - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-pinecone

%pip install llama-index-vector-stores-pinecone

In \[ \]:

Copied!

!pip install llama\-index\>=0.9.31 pinecone\-client\>=3.0.0

!pip install llama-index>=0.9.31 pinecone-client>=3.0.0

In \[ \]:

Copied!

import logging
import sys
import os

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys import os logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

#### Creating a Pinecone Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PineconeIndexDemo/#creating-a-pinecone-index)

In \[ \]:

Copied!

from pinecone import Pinecone, ServerlessSpec

from pinecone import Pinecone, ServerlessSpec

In \[ \]:

Copied!

os.environ\[
    "PINECONE\_API\_KEY"
\] \= "<Your Pinecone API key, from app.pinecone.io>"
os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

api\_key \= os.environ\["PINECONE\_API\_KEY"\]

pc \= Pinecone(api\_key\=api\_key)

os.environ\[ "PINECONE\_API\_KEY" \] = "" os.environ\["OPENAI\_API\_KEY"\] = "sk-..." api\_key = os.environ\["PINECONE\_API\_KEY"\] pc = Pinecone(api\_key=api\_key)

In \[ \]:

Copied!

\# delete if needed
\# pc.delete\_index("quickstart")

\# delete if needed # pc.delete\_index("quickstart")

In \[ \]:

Copied!

\# dimensions are for text-embedding-ada-002

pc.create\_index(
    name\="quickstart",
    dimension\=1536,
    metric\="euclidean",
    spec\=ServerlessSpec(cloud\="aws", region\="us-west-2"),
)

\# If you need to create a PodBased Pinecone index, you could alternatively do this:
#
\# from pinecone import Pinecone, PodSpec
#
\# pc = Pinecone(api\_key='xxx')
#
\# pc.create\_index(
\# 	 name='my-index',
\# 	 dimension=1536,
\# 	 metric='cosine',
\# 	 spec=PodSpec(
\# 		 environment='us-east1-gcp',
\# 		 pod\_type='p1.x1',
\# 		 pods=1
\# 	 )
\# )
#

\# dimensions are for text-embedding-ada-002 pc.create\_index( name="quickstart", dimension=1536, metric="euclidean", spec=ServerlessSpec(cloud="aws", region="us-west-2"), ) # If you need to create a PodBased Pinecone index, you could alternatively do this: # # from pinecone import Pinecone, PodSpec # # pc = Pinecone(api\_key='xxx') # # pc.create\_index( # name='my-index', # dimension=1536, # metric='cosine', # spec=PodSpec( # environment='us-east1-gcp', # pod\_type='p1.x1', # pods=1 # ) # ) #

In \[ \]:

Copied!

pinecone\_index \= pc.Index("quickstart")

pinecone\_index = pc.Index("quickstart")

#### Load documents, build the PineconeVectorStore and VectorStoreIndex[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PineconeIndexDemo/#load-documents-build-the-pineconevectorstore-and-vectorstoreindex)

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.vector\_stores.pinecone import PineconeVectorStore
from IPython.display import Markdown, display

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.vector\_stores.pinecone import PineconeVectorStore from IPython.display import Markdown, display

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

Will not apply HSTS. The HSTS database must be a regular and non-world-writable file.
ERROR: could not open HSTS store at '/home/loganm/.wget-hsts'. HSTS will be disabled.
--2024-01-16 11:56:25--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.111.133, 185.199.110.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 75042 (73K) \[text/plain\]
Saving to: ‘data/paul\_graham/paul\_graham\_essay.txt’

data/paul\_graham/pa 100%\[>\]  73.28K  --.-KB/s    in 0.04s   

2024-01-16 11:56:25 (1.79 MB/s) - ‘data/paul\_graham/paul\_graham\_essay.txt’ saved \[75042/75042\]

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham").load\_data()

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham").load\_data()

In \[ \]:

Copied!

\# initialize without metadata filter
from llama\_index.core import StorageContext

if "OPENAI\_API\_KEY" not in os.environ:
    raise EnvironmentError(f"Environment variable OPENAI\_API\_KEY is not set")

vector\_store \= PineconeVectorStore(pinecone\_index\=pinecone\_index)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

\# initialize without metadata filter from llama\_index.core import StorageContext if "OPENAI\_API\_KEY" not in os.environ: raise EnvironmentError(f"Environment variable OPENAI\_API\_KEY is not set") vector\_store = PineconeVectorStore(pinecone\_index=pinecone\_index) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"

Upserted vectors:   0%|          | 0/22 \[00:00<?, ?it/s\]

#### Query Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PineconeIndexDemo/#query-index)

May take a minute or so for the index to be ready!

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did the author do growing up?")

\# set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine() response = query\_engine.query("What did the author do growing up?")

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"

In \[ \]:

Copied!

display(Markdown(f"<b>{response}</b>"))

display(Markdown(f"**{response}**"))

**The author, growing up, worked on writing and programming. They wrote short stories and tried writing programs on an IBM 1401 computer. They later got a microcomputer and started programming more extensively, writing simple games and a word processor.**

Back to top

[Previous Pinecone Vector Store - Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PineconeIndexDemo-Hybrid/)[Next Qdrant Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/QdrantIndexDemo/)
