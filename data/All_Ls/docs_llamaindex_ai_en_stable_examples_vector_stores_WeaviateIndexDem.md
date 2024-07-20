Title: Weaviate Vector Store - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo/

Markdown Content:
Weaviate Vector Store - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-weaviate

%pip install llama-index-vector-stores-weaviate

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

#### Creating a Weaviate Client[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo/#creating-a-weaviate-client)

In \[ \]:

Copied!

import os
import openai

os.environ\["OPENAI\_API\_KEY"\] \= ""
openai.api\_key \= os.environ\["OPENAI\_API\_KEY"\]

import os import openai os.environ\["OPENAI\_API\_KEY"\] = "" openai.api\_key = os.environ\["OPENAI\_API\_KEY"\]

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

In \[ \]:

Copied!

import weaviate

import weaviate

In \[ \]:

Copied!

\# cloud
cluster\_url \= ""
api\_key \= ""

client \= weaviate.connect\_to\_wcs(
    cluster\_url\=cluster\_url,
    auth\_credentials\=weaviate.auth.AuthApiKey(api\_key),
)

\# local
\# client = connect\_to\_local()

\# cloud cluster\_url = "" api\_key = "" client = weaviate.connect\_to\_wcs( cluster\_url=cluster\_url, auth\_credentials=weaviate.auth.AuthApiKey(api\_key), ) # local # client = connect\_to\_local()

#### Load documents, build the VectorStoreIndex[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo/#load-documents-build-the-vectorstoreindex)

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.vector\_stores.weaviate import WeaviateVectorStore
from IPython.display import Markdown, display

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.vector\_stores.weaviate import WeaviateVectorStore from IPython.display import Markdown, display

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham").load\_data()

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham").load\_data()

In \[ \]:

Copied!

from llama\_index.core import StorageContext

\# If you want to load the index later, be sure to give it a name!
vector\_store \= WeaviateVectorStore(
    weaviate\_client\=client, index\_name\="LlamaIndex"
)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

\# NOTE: you may also choose to define a index\_name manually.
\# index\_name = "test\_prefix"
\# vector\_store = WeaviateVectorStore(weaviate\_client=client, index\_name=index\_name)

from llama\_index.core import StorageContext # If you want to load the index later, be sure to give it a name! vector\_store = WeaviateVectorStore( weaviate\_client=client, index\_name="LlamaIndex" ) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context ) # NOTE: you may also choose to define a index\_name manually. # index\_name = "test\_prefix" # vector\_store = WeaviateVectorStore(weaviate\_client=client, index\_name=index\_name)

#### Query Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo/#query-index)

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

Loading the index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo/#loading-the-index)
----------------------------------------------------------------------------------------------------------------------

Here, we use the same index name as when we created the initial index. This stops it from being auto-generated and allows us to easily connect back to it.

In \[ \]:

Copied!

cluster\_url \= ""
api\_key \= ""

client \= weaviate.connect\_to\_wcs(
    cluster\_url\=cluster\_url,
    auth\_credentials\=weaviate.auth.AuthApiKey(api\_key),
)

\# local
\# client = weaviate.connect\_to\_local()

cluster\_url = "" api\_key = "" client = weaviate.connect\_to\_wcs( cluster\_url=cluster\_url, auth\_credentials=weaviate.auth.AuthApiKey(api\_key), ) # local # client = weaviate.connect\_to\_local()

In \[ \]:

Copied!

vector\_store \= WeaviateVectorStore(
    weaviate\_client\=client, index\_name\="LlamaIndex"
)

loaded\_index \= VectorStoreIndex.from\_vector\_store(vector\_store)

vector\_store = WeaviateVectorStore( weaviate\_client=client, index\_name="LlamaIndex" ) loaded\_index = VectorStoreIndex.from\_vector\_store(vector\_store)

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
query\_engine \= loaded\_index.as\_query\_engine()
response \= query\_engine.query("What happened at interleaf?")
display(Markdown(f"<b>{response}</b>"))

\# set Logging to DEBUG for more detailed outputs query\_engine = loaded\_index.as\_query\_engine() response = query\_engine.query("What happened at interleaf?") display(Markdown(f"**{response}**"))

Metadata Filtering[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo/#metadata-filtering)
------------------------------------------------------------------------------------------------------------------------

Let's insert a dummy document, and try to filter so that only that document is returned.

In \[ \]:

Copied!

from llama\_index.core import Document

doc \= Document.example()
print(doc.metadata)
print("-----")
print(doc.text\[:100\])

from llama\_index.core import Document doc = Document.example() print(doc.metadata) print("-----") print(doc.text\[:100\])

In \[ \]:

Copied!

loaded\_index.insert(doc)

loaded\_index.insert(doc)

In \[ \]:

Copied!

from llama\_index.core.vector\_stores import ExactMatchFilter, MetadataFilters

filters \= MetadataFilters(
    filters\=\[ExactMatchFilter(key\="filename", value\="README.md")\]
)
query\_engine \= loaded\_index.as\_query\_engine(filters\=filters)
response \= query\_engine.query("What is the name of the file?")
display(Markdown(f"<b>{response}</b>"))

from llama\_index.core.vector\_stores import ExactMatchFilter, MetadataFilters filters = MetadataFilters( filters=\[ExactMatchFilter(key="filename", value="README.md")\] ) query\_engine = loaded\_index.as\_query\_engine(filters=filters) response = query\_engine.query("What is the name of the file?") display(Markdown(f"**{response}**"))

Deleting the index completely[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo/#deleting-the-index-completely)


You must ensure your client connections are closed:

In \[ \]:

Copied!

client.close()

client.close()

Back to top

[Previous Weaviate Vector Store - Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo-Hybrid/)[Next Auto-Retrieval from a Weaviate Vector Database](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndex_auto_retriever/)
