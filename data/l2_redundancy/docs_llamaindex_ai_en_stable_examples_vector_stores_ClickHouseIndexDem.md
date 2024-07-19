Title: ClickHouse Vector Store - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/ClickHouseIndexDemo/

Markdown Content:
ClickHouse Vector Store - LlamaIndex


In this notebook we are going to show a quick demo of using the ClickHouseVectorStore.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

!pip install llama\-index
!pip install clickhouse\_connect

!pip install llama-index !pip install clickhouse\_connect

#### Creating a ClickHouse Client[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ClickHouseIndexDemo/#creating-a-clickhouse-client)

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
    host\="localhost",
    port\=8123,
    username\="default",
    password\="",
)

from os import environ import clickhouse\_connect environ\["OPENAI\_API\_KEY"\] = "sk-\*" # initialize client client = clickhouse\_connect.get\_client( host="localhost", port=8123, username="default", password="", )

#### Load documents, build and store the VectorStoreIndex with ClickHouseVectorStore[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ClickHouseIndexDemo/#load-documents-build-and-store-the-vectorstoreindex-with-clickhousevectorstore)

Here we will use a set of Paul Graham essays to provide the text to turn into embeddings, store in a `ClickHouseVectorStore` and query to find context for our LLM QnA loop.

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.vector\_stores.clickhouse import ClickHouseVectorStore

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.vector\_stores.clickhouse import ClickHouseVectorStore

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("../data/paul\_graham").load\_data()
print("Document ID:", documents\[0\].doc\_id)
print("Number of Documents: ", len(documents))

\# load documents documents = SimpleDirectoryReader("../data/paul\_graham").load\_data() print("Document ID:", documents\[0\].doc\_id) print("Number of Documents: ", len(documents))

Document ID: d03ac7db-8dae-4199-bc38-445dec51a534
Number of Documents:  1

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

\--2024-02-13 10:08:31--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.111.133, 185.199.109.133, 185.199.110.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.111.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 75042 (73K) \[text/plain\]
Saving to: ‘data/paul\_graham/paul\_graham\_essay.txt’

data/paul\_graham/pa 100%\[>\]  73.28K  --.-KB/s    in 0.003s  

2024-02-13 10:08:31 (23.9 MB/s) - ‘data/paul\_graham/paul\_graham\_essay.txt’ saved \[75042/75042\]

You can process your files individually using [SimpleDirectoryReader](https://docs.llamaindex.ai/examples/data_connectors/simple_directory_reader.ipynb):

In \[ \]:

Copied!

loader \= SimpleDirectoryReader("./data/paul\_graham/")
documents \= loader.load\_data()
for file in loader.input\_files:
    print(file)
    \# Here is where you would do any preprocessing

loader = SimpleDirectoryReader("./data/paul\_graham/") documents = loader.load\_data() for file in loader.input\_files: print(file) # Here is where you would do any preprocessing

data/paul\_graham/paul\_graham\_essay.txt

In \[ \]:

Copied!

\# initialize with metadata filter and store indexes
from llama\_index.core import StorageContext

for document in documents:
    document.metadata \= {"user\_id": "123", "favorite\_color": "blue"}
vector\_store \= ClickHouseVectorStore(clickhouse\_client\=client)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

\# initialize with metadata filter and store indexes from llama\_index.core import StorageContext for document in documents: document.metadata = {"user\_id": "123", "favorite\_color": "blue"} vector\_store = ClickHouseVectorStore(clickhouse\_client=client) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

#### Query Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ClickHouseIndexDemo/#query-index)

Now ClickHouse vector store supports filter search and hybrid search

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

The author learned several things during their time at Interleaf, including the importance of having
technology companies run by product people rather than sales people, the drawbacks of having too
many people edit code, the value of corridor conversations over planned meetings, the challenges of
dealing with big bureaucratic customers, and the importance of being the "entry level" option in a
market.

#### Clear All Indexes[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ClickHouseIndexDemo/#clear-all-indexes)

In \[ \]:

Copied!

for document in documents:
    index.delete\_ref\_doc(document.doc\_id)

for document in documents: index.delete\_ref\_doc(document.doc\_id)

Back to top

[Previous Chroma](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ChromaIndexDemo/)[Next CouchbaseVectorStoreDemo](https://docs.llamaindex.ai/en/stable/examples/vector_stores/CouchbaseVectorStoreDemo/)
