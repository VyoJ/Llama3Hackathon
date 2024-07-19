Title: Weaviate Vector Store - Hybrid Search

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo-Hybrid/

Markdown Content:
Weaviate Vector Store - Hybrid Search - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-weaviate

%pip install llama-index-vector-stores-weaviate

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

Creating a Weaviate Client[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo-Hybrid/#creating-a-weaviate-client)
-----------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

import os
import openai

os.environ\["OPENAI\_API\_KEY"\] \= ""
openai.api\_key \= os.environ\["OPENAI\_API\_KEY"\]

import os import openai os.environ\["OPENAI\_API\_KEY"\] = "" openai.api\_key = os.environ\["OPENAI\_API\_KEY"\]

In \[ \]:

Copied!

import weaviate

import weaviate

In \[ \]:

Copied!

\# Connect to cloud instance
cluster\_url \= ""
api\_key \= ""

client \= weaviate.connect\_to\_wcs(
    cluster\_url\=cluster\_url,
    auth\_credentials\=weaviate.auth.AuthApiKey(api\_key),
)

\# Connect to local instance
\# client = weaviate.connect\_to\_local()

\# Connect to cloud instance cluster\_url = "" api\_key = "" client = weaviate.connect\_to\_wcs( cluster\_url=cluster\_url, auth\_credentials=weaviate.auth.AuthApiKey(api\_key), ) # Connect to local instance # client = weaviate.connect\_to\_local()

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.vector\_stores.weaviate import WeaviateVectorStore
from llama\_index.core.response.notebook\_utils import display\_response

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.vector\_stores.weaviate import WeaviateVectorStore from llama\_index.core.response.notebook\_utils import display\_response

Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo-Hybrid/#download-data)
---------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

Load documents[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo-Hybrid/#load-documents)
-----------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data()

Build the VectorStoreIndex with WeaviateVectorStore[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo-Hybrid/#build-the-vectorstoreindex-with-weaviatevectorstore)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core import StorageContext

vector\_store \= WeaviateVectorStore(weaviate\_client\=client)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

\# NOTE: you may also choose to define a index\_name manually.
\# index\_name = "test\_prefix"
\# vector\_store = WeaviateVectorStore(weaviate\_client=client, index\_name=index\_name)

from llama\_index.core import StorageContext vector\_store = WeaviateVectorStore(weaviate\_client=client) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context ) # NOTE: you may also choose to define a index\_name manually. # index\_name = "test\_prefix" # vector\_store = WeaviateVectorStore(weaviate\_client=client, index\_name=index\_name)

Query Index with Default Vector Search[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo-Hybrid/#query-index-with-default-vector-search)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine(similarity\_top\_k\=2)
response \= query\_engine.query("What did the author do growing up?")

\# set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine(similarity\_top\_k=2) response = query\_engine.query("What did the author do growing up?")

In \[ \]:

Copied!

display\_response(response)

display\_response(response)

Query Index with Hybrid Search[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo-Hybrid/#query-index-with-hybrid-search)
-------------------------------------------------------------------------------------------------------------------------------------------------------

Use hybrid search with bm25 and vector.  
`alpha` parameter determines weighting (alpha = 0 -> bm25, alpha=1 -> vector search).

### By default, `alpha=0.75` is used (very similar to vector search)[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo-Hybrid/#by-default-alpha075-is-used-very-similar-to-vector-search)

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine(
    vector\_store\_query\_mode\="hybrid", similarity\_top\_k\=2
)
response \= query\_engine.query(
    "What did the author do growing up?",
)

\# set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine( vector\_store\_query\_mode="hybrid", similarity\_top\_k=2 ) response = query\_engine.query( "What did the author do growing up?", )

In \[ \]:

Copied!

display\_response(response)

display\_response(response)

### Set `alpha=0.` to favor bm25[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo-Hybrid/#set-alpha0-to-favor-bm25)

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine(
    vector\_store\_query\_mode\="hybrid", similarity\_top\_k\=2, alpha\=0.0
)
response \= query\_engine.query(
    "What did the author do growing up?",
)

\# set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine( vector\_store\_query\_mode="hybrid", similarity\_top\_k=2, alpha=0.0 ) response = query\_engine.query( "What did the author do growing up?", )

In \[ \]:

Copied!

display\_response(response)

display\_response(response)

Back to top

[Previous Vespa Vector Store demo](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VespaIndexDemo/)[Next Weaviate Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo/)
