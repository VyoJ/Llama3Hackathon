Title: Faiss Vector Store - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/FaissIndexDemo/

Markdown Content:
Faiss Vector Store - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-faiss

%pip install llama-index-vector-stores-faiss

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

#### Creating a Faiss Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/FaissIndexDemo/#creating-a-faiss-index)

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

In \[ \]:

Copied!

import faiss

\# dimensions of text-ada-embedding-002
d \= 1536
faiss\_index \= faiss.IndexFlatL2(d)

import faiss # dimensions of text-ada-embedding-002 d = 1536 faiss\_index = faiss.IndexFlatL2(d)

#### Load documents, build the VectorStoreIndex[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/FaissIndexDemo/#load-documents-build-the-vectorstoreindex)

In \[ \]:

Copied!

from llama\_index.core import (
    SimpleDirectoryReader,
    load\_index\_from\_storage,
    VectorStoreIndex,
    StorageContext,
)
from llama\_index.vector\_stores.faiss import FaissVectorStore
from IPython.display import Markdown, display

from llama\_index.core import ( SimpleDirectoryReader, load\_index\_from\_storage, VectorStoreIndex, StorageContext, ) from llama\_index.vector\_stores.faiss import FaissVectorStore from IPython.display import Markdown, display

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data()

In \[ \]:

Copied!

vector\_store \= FaissVectorStore(faiss\_index\=faiss\_index)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

vector\_store = FaissVectorStore(faiss\_index=faiss\_index) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

In \[ \]:

Copied!

\# save index to disk
index.storage\_context.persist()

\# save index to disk index.storage\_context.persist()

In \[ \]:

Copied!

\# load index from disk
vector\_store \= FaissVectorStore.from\_persist\_dir("./storage")
storage\_context \= StorageContext.from\_defaults(
    vector\_store\=vector\_store, persist\_dir\="./storage"
)
index \= load\_index\_from\_storage(storage\_context\=storage\_context)

\# load index from disk vector\_store = FaissVectorStore.from\_persist\_dir("./storage") storage\_context = StorageContext.from\_defaults( vector\_store=vector\_store, persist\_dir="./storage" ) index = load\_index\_from\_storage(storage\_context=storage\_context)

#### Query Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/FaissIndexDemo/#query-index)

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

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query(
    "What did the author do after his time at Y Combinator?"
)

\# set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine() response = query\_engine.query( "What did the author do after his time at Y Combinator?" )

In \[ \]:

Copied!

display(Markdown(f"<b>{response}</b>"))

display(Markdown(f"**{response}**"))

Back to top

[Previous Epsilla Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/EpsillaIndexDemo/)[Next Firestore Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/FirestoreVectorStore/)
