Title: Pinecone Vector Store - Hybrid Search

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/PineconeIndexDemo-Hybrid/

Markdown Content:
Pinecone Vector Store - Hybrid Search - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-pinecone

%pip install llama-index-vector-stores-pinecone

In \[ \]:

Copied!

!pip install llama\-index\>=0.9.31 pinecone\-client\>=3.0.0 "transformers\[torch\]"

!pip install llama-index>=0.9.31 pinecone-client>=3.0.0 "transformers\[torch\]"

#### Creating a Pinecone Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PineconeIndexDemo-Hybrid/#creating-a-pinecone-index)

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

In \[ \]:

Copied!

from pinecone import Pinecone, ServerlessSpec

from pinecone import Pinecone, ServerlessSpec

In \[ \]:

Copied!

import os

os.environ\[
    "PINECONE\_API\_KEY"
\] \= #"<Your Pinecone API key, from app.pinecone.io>"
os.environ\[
    "OPENAI\_API\_KEY"
\] \= "sk-..."

api\_key \= os.environ\["PINECONE\_API\_KEY"\]

pc \= Pinecone(api\_key\=api\_key)

import os os.environ\[ "PINECONE\_API\_KEY" \] = #"" os.environ\[ "OPENAI\_API\_KEY" \] = "sk-..." api\_key = os.environ\["PINECONE\_API\_KEY"\] pc = Pinecone(api\_key=api\_key)

In \[ \]:

Copied!

\# delete if needed
\# pc.delete\_index("quickstart")

\# delete if needed # pc.delete\_index("quickstart")

In \[ \]:

Copied!

\# dimensions are for text-embedding-ada-002
\# NOTE: needs dotproduct for hybrid search

pc.create\_index(
    name\="quickstart",
    dimension\=1536,
    metric\="dotproduct",
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

\# dimensions are for text-embedding-ada-002 # NOTE: needs dotproduct for hybrid search pc.create\_index( name="quickstart", dimension=1536, metric="dotproduct", spec=ServerlessSpec(cloud="aws", region="us-west-2"), ) # If you need to create a PodBased Pinecone index, you could alternatively do this: # # from pinecone import Pinecone, PodSpec # # pc = Pinecone(api\_key='xxx') # # pc.create\_index( # name='my-index', # dimension=1536, # metric='cosine', # spec=PodSpec( # environment='us-east1-gcp', # pod\_type='p1.x1', # pods=1 # ) # ) #

In \[ \]:

Copied!

pinecone\_index \= pc.Index("quickstart")

pinecone\_index = pc.Index("quickstart")

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

#### Load documents, build the PineconeVectorStore[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PineconeIndexDemo-Hybrid/#load-documents-build-the-pineconevectorstore)

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.vector\_stores.pinecone import PineconeVectorStore
from IPython.display import Markdown, display

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.vector\_stores.pinecone import PineconeVectorStore from IPython.display import Markdown, display

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data()

In \[ \]:

Copied!

\# set add\_sparse\_vector=True to compute sparse vectors during upsert
from llama\_index.core import StorageContext

if "OPENAI\_API\_KEY" not in os.environ:
    raise EnvironmentError(f"Environment variable OPENAI\_API\_KEY is not set")

vector\_store \= PineconeVectorStore(
    pinecone\_index\=pinecone\_index,
    add\_sparse\_vector\=True,
)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

\# set add\_sparse\_vector=True to compute sparse vectors during upsert from llama\_index.core import StorageContext if "OPENAI\_API\_KEY" not in os.environ: raise EnvironmentError(f"Environment variable OPENAI\_API\_KEY is not set") vector\_store = PineconeVectorStore( pinecone\_index=pinecone\_index, add\_sparse\_vector=True, ) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"

Upserted vectors:   0%|          | 0/22 \[00:00<?, ?it/s\]

#### Query Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PineconeIndexDemo-Hybrid/#query-index)

May need to wait a minute or two for the index to be ready

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine(vector\_store\_query\_mode\="hybrid")
response \= query\_engine.query("What happened at Viaweb?")

\# set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine(vector\_store\_query\_mode="hybrid") response = query\_engine.query("What happened at Viaweb?")

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"

In \[ \]:

Copied!

display(Markdown(f"<b>{response}</b>"))

display(Markdown(f"**{response}**"))

**At Viaweb, Lisp was used as a programming language. The speaker gave a talk at a Lisp conference about how Lisp was used at Viaweb, and afterward, the talk gained a lot of attention when it was posted online. This led to a realization that publishing essays online could reach a wider audience than traditional print media. The speaker also wrote a collection of essays, which was later published as a book called "Hackers & Painters."**

Back to top

[Previous pgvecto.rs](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PGVectoRsDemo/)[Next Pinecone Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PineconeIndexDemo/)
