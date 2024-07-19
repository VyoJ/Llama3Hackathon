Title: Alibaba Cloud OpenSearch Vector Store

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/AlibabaCloudOpenSearchIndexDemo/

Markdown Content:
Alibaba Cloud OpenSearch Vector Store - LlamaIndex


> [Alibaba Cloud OpenSearch Vector Search Edition](https://help.aliyun.com/zh/open-search/vector-search-edition/product-overview) is a large-scale distributed search engine that is developed by Alibaba Group. Alibaba Cloud OpenSearch Vector Search Edition provides search services for the entire Alibaba Group, including Taobao, Tmall, Cainiao, Youku, and other e-commerce platforms that are provided for customers in regions outside the Chinese mainland. Alibaba Cloud OpenSearch Vector Search Edition is also a base engine of Alibaba Cloud OpenSearch. After years of development, Alibaba Cloud OpenSearch Vector Search Edition has met the business requirements for high availability, high timeliness, and cost-effectiveness. Alibaba Cloud OpenSearch Vector Search Edition also provides an automated O&M system on which you can build a custom search service based on your business features.

To run, you should have a instance.

### Setup[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AlibabaCloudOpenSearchIndexDemo/#setup)

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-alibabacloud\-opensearch

%pip install llama-index-vector-stores-alibabacloud-opensearch

In \[ \]:

Copied!

%pip install llama\-index

%pip install llama-index

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

### Please provide OpenAI access key[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AlibabaCloudOpenSearchIndexDemo/#please-provide-openai-access-key)

In order use embeddings by OpenAI you need to supply an OpenAI API Key:

In \[ \]:

Copied!

import openai

OPENAI\_API\_KEY \= getpass.getpass("OpenAI API Key:")
openai.api\_key \= OPENAI\_API\_KEY

import openai OPENAI\_API\_KEY = getpass.getpass("OpenAI API Key:") openai.api\_key = OPENAI\_API\_KEY

#### Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AlibabaCloudOpenSearchIndexDemo/#download-data)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

#### Load documents[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AlibabaCloudOpenSearchIndexDemo/#load-documents)

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader
from IPython.display import Markdown, display

from llama\_index.core import SimpleDirectoryReader from IPython.display import Markdown, display

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham").load\_data()
print(f"Total documents: {len(documents)}")

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham").load\_data() print(f"Total documents: {len(documents)}")

Total documents: 1

### Create the Alibaba Cloud OpenSearch Vector Store object:[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AlibabaCloudOpenSearchIndexDemo/#create-the-alibaba-cloud-opensearch-vector-store-object)

To run the next step, you should have a Alibaba Cloud OpenSearch Vector Service instance, and configure a table.

In \[ \]:

Copied!

\# if run fllowing cells raise async io exception, run this
import nest\_asyncio

nest\_asyncio.apply()

\# if run fllowing cells raise async io exception, run this import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

\# initialize without metadata filter
from llama\_index.core import StorageContext, VectorStoreIndex
from llama\_index.vector\_stores.alibabacloud\_opensearch import (
    AlibabaCloudOpenSearchStore,
    AlibabaCloudOpenSearchConfig,
)

config \= AlibabaCloudOpenSearchConfig(
    endpoint\="\*\*\*\*\*",
    instance\_id\="\*\*\*\*\*",
    username\="your\_username",
    password\="your\_password",
    table\_name\="llama",
)

vector\_store \= AlibabaCloudOpenSearchStore(config)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

\# initialize without metadata filter from llama\_index.core import StorageContext, VectorStoreIndex from llama\_index.vector\_stores.alibabacloud\_opensearch import ( AlibabaCloudOpenSearchStore, AlibabaCloudOpenSearchConfig, ) config = AlibabaCloudOpenSearchConfig( endpoint="\*\*\*\*\*", instance\_id="\*\*\*\*\*", username="your\_username", password="your\_password", table\_name="llama", ) vector\_store = AlibabaCloudOpenSearchStore(config) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

#### Query Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AlibabaCloudOpenSearchIndexDemo/#query-index)

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

**Before college, the author worked on writing and programming. They wrote short stories and tried writing programs on the IBM 1401 in 9th grade using an early version of Fortran.**

### Connecting to an existing store[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AlibabaCloudOpenSearchIndexDemo/#connecting-to-an-existing-store)

Since this store is backed by Alibaba Cloud OpenSearch, it is persistent by definition. So, if you want to connect to a store that was created and populated previously, here is how:

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex
from llama\_index.vector\_stores.alibabacloud\_opensearch import (
    AlibabaCloudOpenSearchStore,
    AlibabaCloudOpenSearchConfig,
)

config \= AlibabaCloudOpenSearchConfig(
    endpoint\="\*\*\*",
    instance\_id\="\*\*\*",
    username\="your\_username",
    password\="your\_password",
    table\_name\="llama",
)

vector\_store \= AlibabaCloudOpenSearchStore(config)

\# Create index from existing stored vectors
index \= VectorStoreIndex.from\_vector\_store(vector\_store)
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query(
    "What did the author study prior to working on AI?"
)

display(Markdown(f"<b>{response}</b>"))

from llama\_index.core import VectorStoreIndex from llama\_index.vector\_stores.alibabacloud\_opensearch import ( AlibabaCloudOpenSearchStore, AlibabaCloudOpenSearchConfig, ) config = AlibabaCloudOpenSearchConfig( endpoint="\*\*\*", instance\_id="\*\*\*", username="your\_username", password="your\_password", table\_name="llama", ) vector\_store = AlibabaCloudOpenSearchStore(config) # Create index from existing stored vectors index = VectorStoreIndex.from\_vector\_store(vector\_store) query\_engine = index.as\_query\_engine() response = query\_engine.query( "What did the author study prior to working on AI?" ) display(Markdown(f"**{response}**"))

### Metadata filtering[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AlibabaCloudOpenSearchIndexDemo/#metadata-filtering)

The Alibaba Cloud OpenSearch vector store support metadata filtering at query time. The following cells, which work on a brand new table, demonstrate this feature.

In this demo, for the sake of brevity, a single source document is loaded (the `../data/paul_graham/paul_graham_essay.txt` text file). Nevertheless, you will attach some custom metadata to the document to illustrate how you can can restrict queries with conditions on the metadata attached to the documents.

In \[ \]:

Copied!

from llama\_index.core import StorageContext, VectorStoreIndex
from llama\_index.vector\_stores.alibabacloud\_opensearch import (
    AlibabaCloudOpenSearchStore,
    AlibabaCloudOpenSearchConfig,
)

config \= AlibabaCloudOpenSearchConfig(
    endpoint\="\*\*\*\*",
    instance\_id\="\*\*\*\*",
    username\="your\_username",
    password\="your\_password",
    table\_name\="llama",
)

md\_storage\_context \= StorageContext.from\_defaults(
    vector\_store\=AlibabaCloudOpenSearchStore(config)
)

def my\_file\_metadata(file\_name: str):
    """Depending on the input file name, associate a different metadata."""
    if "essay" in file\_name:
        source\_type \= "essay"
    elif "dinosaur" in file\_name:
        \# this (unfortunately) will not happen in this demo
        source\_type \= "dinos"
    else:
        source\_type \= "other"
    return {"source\_type": source\_type}

\# Load documents and build index
md\_documents \= SimpleDirectoryReader(
    "../data/paul\_graham", file\_metadata\=my\_file\_metadata
).load\_data()
md\_index \= VectorStoreIndex.from\_documents(
    md\_documents, storage\_context\=md\_storage\_context
)

from llama\_index.core import StorageContext, VectorStoreIndex from llama\_index.vector\_stores.alibabacloud\_opensearch import ( AlibabaCloudOpenSearchStore, AlibabaCloudOpenSearchConfig, ) config = AlibabaCloudOpenSearchConfig( endpoint="\*\*\*\*", instance\_id="\*\*\*\*", username="your\_username", password="your\_password", table\_name="llama", ) md\_storage\_context = StorageContext.from\_defaults( vector\_store=AlibabaCloudOpenSearchStore(config) ) def my\_file\_metadata(file\_name: str): """Depending on the input file name, associate a different metadata.""" if "essay" in file\_name: source\_type = "essay" elif "dinosaur" in file\_name: # this (unfortunately) will not happen in this demo source\_type = "dinos" else: source\_type = "other" return {"source\_type": source\_type} # Load documents and build index md\_documents = SimpleDirectoryReader( "../data/paul\_graham", file\_metadata=my\_file\_metadata ).load\_data() md\_index = VectorStoreIndex.from\_documents( md\_documents, storage\_context=md\_storage\_context )

Add filter to query engine:

In \[ \]:

Copied!

from llama\_index.core.vector\_stores import MetadataFilter, MetadataFilters

md\_query\_engine \= md\_index.as\_query\_engine(
    filters\=MetadataFilters(
        filters\=\[MetadataFilter(key\="source\_type", value\="essay")\]
    )
)
md\_response \= md\_query\_engine.query(
    "How long it took the author to write his thesis?"
)

display(Markdown(f"<b>{md\_response}</b>"))

from llama\_index.core.vector\_stores import MetadataFilter, MetadataFilters md\_query\_engine = md\_index.as\_query\_engine( filters=MetadataFilters( filters=\[MetadataFilter(key="source\_type", value="essay")\] ) ) md\_response = md\_query\_engine.query( "How long it took the author to write his thesis?" ) display(Markdown(f"**{md\_response}**"))

To test that the filtering is at play, try to change it to use only `"dinos"` documents... there will be no answer this time :)

Back to top

[Previous AWSDocDBDemo](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AWSDocDBDemo/)[Next Amazon Neptune - Neptune Analytics vector store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AmazonNeptuneVectorDemo/)
