Title: MyScale Vector Store - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/MyScaleIndexDemo/

Markdown Content:
MyScale Vector Store - LlamaIndex


In this notebook we are going to show a quick demo of using the MyScaleVectorStore.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-myscale

%pip install llama-index-vector-stores-myscale

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

#### Creating a MyScale Client[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MyScaleIndexDemo/#creating-a-myscale-client)

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

In \[ \]:

Copied!

from os import environ
import clickhouse\_connect

environ\["OPENAI\_API\_KEY"\] \= "sk-\*"

\# initialize client
client \= clickhouse\_connect.get\_client(
    host\="YOUR\_CLUSTER\_HOST",
    port\=8443,
    username\="YOUR\_USERNAME",
    password\="YOUR\_CLUSTER\_PASSWORD",
)

from os import environ import clickhouse\_connect environ\["OPENAI\_API\_KEY"\] = "sk-\*" # initialize client client = clickhouse\_connect.get\_client( host="YOUR\_CLUSTER\_HOST", port=8443, username="YOUR\_USERNAME", password="YOUR\_CLUSTER\_PASSWORD", )

#### Load documents, build and store the VectorStoreIndex with MyScaleVectorStore[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MyScaleIndexDemo/#load-documents-build-and-store-the-vectorstoreindex-with-myscalevectorstore)

Here we will use a set of Paul Graham essays to provide the text to turn into embeddings, store in a `MyScaleVectorStore` and query to find context for our LLM QnA loop.

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.vector\_stores.myscale import MyScaleVectorStore
from IPython.display import Markdown, display

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.vector\_stores.myscale import MyScaleVectorStore from IPython.display import Markdown, display

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("../data/paul\_graham").load\_data()
print("Document ID:", documents\[0\].doc\_id)
print("Number of Documents: ", len(documents))

\# load documents documents = SimpleDirectoryReader("../data/paul\_graham").load\_data() print("Document ID:", documents\[0\].doc\_id) print("Number of Documents: ", len(documents))

Document ID: a5f2737c-ed18-4e5d-ab9a-75955edb816d
Number of Documents:  1

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

You can process your files individually using [SimpleDirectoryReader](https://docs.llamaindex.ai/examples/data_connectors/simple_directory_reader.ipynb):

In \[ \]:

Copied!

loader \= SimpleDirectoryReader("./data/paul\_graham/")
documents \= loader.load\_data()
for file in loader.input\_files:
    print(file)
    \# Here is where you would do any preprocessing

loader = SimpleDirectoryReader("./data/paul\_graham/") documents = loader.load\_data() for file in loader.input\_files: print(file) # Here is where you would do any preprocessing

../data/paul\_graham/paul\_graham\_essay.txt

In \[ \]:

Copied!

\# initialize with metadata filter and store indexes
from llama\_index.core import StorageContext

for document in documents:
    document.metadata \= {"user\_id": "123", "favorite\_color": "blue"}
vector\_store \= MyScaleVectorStore(myscale\_client\=client)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

\# initialize with metadata filter and store indexes from llama\_index.core import StorageContext for document in documents: document.metadata = {"user\_id": "123", "favorite\_color": "blue"} vector\_store = MyScaleVectorStore(myscale\_client=client) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

#### Query Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MyScaleIndexDemo/#query-index)

Now MyScale vector store supports filter search and hybrid search

You can learn more about [query\_engine](https://docs.llamaindex.ai/module_guides/deploying/query_engine/index.md) and [retriever](https://docs.llamaindex.ai/module_guides/querying/retriever/index.md).

In \[ \]:

Copied!

import textwrap

from llama\_index.core.vector\_stores import ExactMatchFilter, MetadataFilters

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine(
    filters\=MetadataFilters(
        filters\=\[
            ExactMatchFilter(key\="user\_id", value\="123"),
        \]
    ),
    similarity\_top\_k\=2,
    vector\_store\_query\_mode\="hybrid",
)
response \= query\_engine.query("What did the author learn?")
print(textwrap.fill(str(response), 100))

import textwrap from llama\_index.core.vector\_stores import ExactMatchFilter, MetadataFilters # set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine( filters=MetadataFilters( filters=\[ ExactMatchFilter(key="user\_id", value="123"), \] ), similarity\_top\_k=2, vector\_store\_query\_mode="hybrid", ) response = query\_engine.query("What did the author learn?") print(textwrap.fill(str(response), 100))

#### Clear All Indexes[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MyScaleIndexDemo/#clear-all-indexes)

In \[ \]:

Copied!

for document in documents:
    index.delete\_ref\_doc(document.doc\_id)

for document in documents: index.delete\_ref\_doc(document.doc\_id)

Back to top

[Previous MongoDBAtlasVectorSearchRAGOpenAI](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MongoDBAtlasVectorSearchRAGOpenAI/)[Next Neo4j vector store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Neo4jVectorDemo/)
