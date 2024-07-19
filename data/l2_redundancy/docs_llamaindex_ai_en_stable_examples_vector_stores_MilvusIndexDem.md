Title: Milvus Vector Store - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusIndexDemo/

Markdown Content:
Milvus Vector Store - LlamaIndex


This guide demonstrates how to build a Retrieval-Augmented Generation (RAG) system using LlamaIndex and Milvus.

The RAG system combines a retrieval system with a generative model to generate new text based on a given prompt. The system first retrieves relevant documents from a corpus using a vector similarity search engine like Milvus, and then uses a generative model to generate new text based on the retrieved documents.

[Milvus](https://milvus.io/) is the world's most advanced open-source vector database, built to power embedding similarity search and AI applications.

In this notebook we are going to show a quick demo of using the MilvusVectorStore.

Before you begin[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusIndexDemo/#before-you-begin)
------------------------------------------------------------------------------------------------------------------

### Install dependencies[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusIndexDemo/#install-dependencies)

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-milvus

%pip install llama-index-vector-stores-milvus

In \[ \]:

Copied!

%pip install llama\-index

%pip install llama-index

This notebook will use [Milvus Lite](https://milvus.io/docs/milvus_lite.md) requiring a higher version of pymilvus:

In \[ \]:

Copied!

%pip install pymilvus\>=2.4.2

%pip install pymilvus>=2.4.2

> If you are using Google Colab, to enable dependencies just installed, you may need to **restart the runtime** (click on the "Runtime" menu at the top of the screen, and select "Restart session" from the dropdown menu).

### Setup OpenAI[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusIndexDemo/#setup-openai)

Lets first begin by adding the openai api key. This will allow us to access chatgpt.

In \[ \]:

Copied!

import openai

openai.api\_key \= "sk-\*\*\*\*\*\*\*\*\*\*\*"

import openai openai.api\_key = "sk-\*\*\*\*\*\*\*\*\*\*\*"

### Prepare data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusIndexDemo/#prepare-data)

You can download sample data with the following commands:

In \[ \]:

Copied!

! mkdir \-p 'data/'
! wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham\_essay.txt'
! wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' \-O 'data/uber\_2021.pdf'

! mkdir -p 'data/' ! wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham\_essay.txt' ! wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' -O 'data/uber\_2021.pdf'

Getting Started[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusIndexDemo/#getting-started)
----------------------------------------------------------------------------------------------------------------

### Generate our data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusIndexDemo/#generate-our-data)

As a first example, lets generate a document from the file `paul_graham_essay.txt`. It is a single essay from Paul Graham titled `What I Worked On`. To generate the documents we will use the SimpleDirectoryReader.

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

\# load documents
documents \= SimpleDirectoryReader(
    input\_files\=\["./data/paul\_graham\_essay.txt"\]
).load\_data()

print("Document ID:", documents\[0\].doc\_id)

from llama\_index.core import SimpleDirectoryReader # load documents documents = SimpleDirectoryReader( input\_files=\["./data/paul\_graham\_essay.txt"\] ).load\_data() print("Document ID:", documents\[0\].doc\_id)

Document ID: 95f25e4d-f270-4650-87ce-006d69d82033

### Create an index across the data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusIndexDemo/#create-an-index-across-the-data)

Now that we have a document, we can can create an index and insert the document.

> Please note that **Milvus Lite** requires `pymilvus>=2.4.2`.

In \[ \]:

Copied!

\# Create an index over the documents
from llama\_index.core import VectorStoreIndex, StorageContext
from llama\_index.vector\_stores.milvus import MilvusVectorStore

vector\_store \= MilvusVectorStore(
    uri\="./milvus\_demo.db", dim\=1536, overwrite\=True
)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

\# Create an index over the documents from llama\_index.core import VectorStoreIndex, StorageContext from llama\_index.vector\_stores.milvus import MilvusVectorStore vector\_store = MilvusVectorStore( uri="./milvus\_demo.db", dim=1536, overwrite=True ) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

> For the parameters of `MilvusVectorStore`:
> 
> *   Setting the `uri` as a local file, e.g.`./milvus.db`, is the most convenient method, as it automatically utilizes [Milvus Lite](https://milvus.io/docs/milvus_lite.md) to store all data in this file.
> *   If you have large scale of data, you can set up a more performant Milvus server on [docker or kubernetes](https://milvus.io/docs/quickstart.md). In this setup, please use the server uri, e.g.`http://localhost:19530`, as your `uri`.
> *   If you want to use [Zilliz Cloud](https://zilliz.com/cloud), the fully managed cloud service for Milvus, adjust the `uri` and `token`, which correspond to the [Public Endpoint and Api key](https://docs.zilliz.com/docs/on-zilliz-cloud-console#free-cluster-details) in Zilliz Cloud.

### Query the data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusIndexDemo/#query-the-data)

Now that we have our document stored in the index, we can ask questions against the index. The index will use the data stored in itself as the knowledge base for chatgpt.

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()
res \= query\_engine.query("What did the author learn?")
print(res)

query\_engine = index.as\_query\_engine() res = query\_engine.query("What did the author learn?") print(res)

The author learned that philosophy courses in college were boring to him, leading him to switch his focus to studying AI.

In \[ \]:

Copied!

res \= query\_engine.query(
    "What challenges did the disease pose for the author?"
)
print(res)

res = query\_engine.query( "What challenges did the disease pose for the author?" ) print(res)

The disease posed challenges for the author as it affected his mother's health, leading to a stroke caused by colon cancer. This resulted in her losing her balance and needing to be placed in a nursing home. The author and his sister were determined to help their mother get out of the nursing home and back to her house.

This next test shows that overwriting removes the previous data.

In \[ \]:

Copied!

from llama\_index.core import Document

vector\_store \= MilvusVectorStore(
    uri\="./milvus\_demo.db", dim\=1536, overwrite\=True
)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    \[Document(text\="The number that is being searched for is ten.")\],
    storage\_context,
)
query\_engine \= index.as\_query\_engine()
res \= query\_engine.query("Who is the author?")
print(res)

from llama\_index.core import Document vector\_store = MilvusVectorStore( uri="./milvus\_demo.db", dim=1536, overwrite=True ) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( \[Document(text="The number that is being searched for is ten.")\], storage\_context, ) query\_engine = index.as\_query\_engine() res = query\_engine.query("Who is the author?") print(res)

The author is the individual who created the context information.

The next test shows adding additional data to an already existing index.

In \[ \]:

Copied!

del index, vector\_store, storage\_context, query\_engine

vector\_store \= MilvusVectorStore(uri\="./milvus\_demo.db", overwrite\=False)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)
query\_engine \= index.as\_query\_engine()
res \= query\_engine.query("What is the number?")
print(res)

del index, vector\_store, storage\_context, query\_engine vector\_store = MilvusVectorStore(uri="./milvus\_demo.db", overwrite=False) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context ) query\_engine = index.as\_query\_engine() res = query\_engine.query("What is the number?") print(res)

The number is ten.

In \[ \]:

Copied!

res \= query\_engine.query("Who is the author?")
print(res)

res = query\_engine.query("Who is the author?") print(res)

Paul Graham

Metadata filtering[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusIndexDemo/#metadata-filtering)
----------------------------------------------------------------------------------------------------------------------

We can generate results by filtering specific sources. The following example illustrates loading all documents from the directory and subsequently filtering them based on metadata.

In \[ \]:

Copied!

from llama\_index.core.vector\_stores import ExactMatchFilter, MetadataFilters

\# Load all the two documents loaded before
documents\_all \= SimpleDirectoryReader("./data/").load\_data()

vector\_store \= MilvusVectorStore(
    uri\="./milvus\_demo.db", dim\=1536, overwrite\=True
)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(documents\_all, storage\_context)

from llama\_index.core.vector\_stores import ExactMatchFilter, MetadataFilters # Load all the two documents loaded before documents\_all = SimpleDirectoryReader("./data/").load\_data() vector\_store = MilvusVectorStore( uri="./milvus\_demo.db", dim=1536, overwrite=True ) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents(documents\_all, storage\_context)

We want to only retrieve documents from the file `uber_2021.pdf`.

In \[ \]:

Copied!

filters \= MetadataFilters(
    filters\=\[ExactMatchFilter(key\="file\_name", value\="uber\_2021.pdf")\]
)
query\_engine \= index.as\_query\_engine(filters\=filters)
res \= query\_engine.query(
    "What challenges did the disease pose for the author?"
)

print(res)

filters = MetadataFilters( filters=\[ExactMatchFilter(key="file\_name", value="uber\_2021.pdf")\] ) query\_engine = index.as\_query\_engine(filters=filters) res = query\_engine.query( "What challenges did the disease pose for the author?" ) print(res)

The disease posed challenges related to the adverse impact on the business and operations, including reduced demand for Mobility offerings globally, affecting travel behavior and demand. Additionally, the pandemic led to driver supply constraints, impacted by concerns regarding COVID-19, with uncertainties about when supply levels would return to normal. The rise of the Omicron variant further affected travel, resulting in advisories and restrictions that could adversely impact both driver supply and consumer demand for Mobility offerings.

We get a different result this time when retrieve from the file `paul_graham_essay.txt`.

In \[ \]:

Copied!

filters \= MetadataFilters(
    filters\=\[ExactMatchFilter(key\="file\_name", value\="paul\_graham\_essay.txt")\]
)
query\_engine \= index.as\_query\_engine(filters\=filters)
res \= query\_engine.query(
    "What challenges did the disease pose for the author?"
)

print(res)

filters = MetadataFilters( filters=\[ExactMatchFilter(key="file\_name", value="paul\_graham\_essay.txt")\] ) query\_engine = index.as\_query\_engine(filters=filters) res = query\_engine.query( "What challenges did the disease pose for the author?" ) print(res)

The disease posed challenges for the author as it affected his mother's health, leading to a stroke caused by colon cancer. This resulted in his mother losing her balance and needing to be placed in a nursing home. The author and his sister were determined to help their mother get out of the nursing home and back to her house.

Back to top

[Previous Milvus Vector Store With Hybrid Retrieval](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusHybridIndexDemo/)[Next MilvusOperatorFunctionDemo](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusOperatorFunctionDemo/)
