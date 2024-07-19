Title: DashVector Vector Store - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/DashvectorIndexDemo/

Markdown Content:
DashVector Vector Store - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-dashvector

%pip install llama-index-vector-stores-dashvector

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import logging
import sys
import os

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys import os logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

#### Creating a DashVector Collection[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DashvectorIndexDemo/#creating-a-dashvector-collection)

In \[ \]:

Copied!

import dashvector

import dashvector

In \[ \]:

Copied!

api\_key \= os.environ\["DASHVECTOR\_API\_KEY"\]
client \= dashvector.Client(api\_key\=api\_key)

api\_key = os.environ\["DASHVECTOR\_API\_KEY"\] client = dashvector.Client(api\_key=api\_key)

In \[ \]:

Copied!

\# dimensions are for text-embedding-ada-002
client.create("llama-demo", dimension\=1536)

\# dimensions are for text-embedding-ada-002 client.create("llama-demo", dimension=1536)

Out\[ \]:

{"code": 0, "message": "", "requests\_id": "82b969d2-2568-4e18-b0dc-aa159b503c84"}

In \[ \]:

Copied!

dashvector\_collection \= client.get("quickstart")

dashvector\_collection = client.get("quickstart")

#### Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DashvectorIndexDemo/#download-data)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

#### Load documents, build the DashVectorStore and VectorStoreIndex[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DashvectorIndexDemo/#load-documents-build-the-dashvectorstore-and-vectorstoreindex)

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.vector\_stores.dashvector import DashVectorStore
from IPython.display import Markdown, display

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.vector\_stores.dashvector import DashVectorStore from IPython.display import Markdown, display

INFO:numexpr.utils:Note: NumExpr detected 12 cores but "NUMEXPR\_MAX\_THREADS" not set, so enforcing safe limit of 8.
Note: NumExpr detected 12 cores but "NUMEXPR\_MAX\_THREADS" not set, so enforcing safe limit of 8.
INFO:numexpr.utils:NumExpr defaulting to 8 threads.
NumExpr defaulting to 8 threads.

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham").load\_data()

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham").load\_data()

In \[ \]:

Copied!

\# initialize without metadata filter
from llama\_index.core import StorageContext

vector\_store \= DashVectorStore(dashvector\_collection)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

\# initialize without metadata filter from llama\_index.core import StorageContext vector\_store = DashVectorStore(dashvector\_collection) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

#### Query Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DashvectorIndexDemo/#query-index)

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

**The author worked on writing and programming outside of school. They wrote short stories and tried writing programs on the IBM 1401 computer. They also built a microcomputer and started programming on it, writing simple games and a word processor.**

Back to top

[Previous CouchbaseVectorStoreDemo](https://docs.llamaindex.ai/en/stable/examples/vector_stores/CouchbaseVectorStoreDemo/)[Next Databricks Vector Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DatabricksVectorSearchDemo/)
