Title: AnalyticDB - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/AnalyticDBDemo/

Markdown Content:
AnalyticDB - LlamaIndex


> [AnalyticDB for PostgreSQL](https://www.alibabacloud.com/help/en/analyticdb-for-postgresql/product-overview/overview-product-overview) is a massively parallel processing (MPP) data warehousing service that is designed to analyze large volumes of data online.

To run this notebook you need a AnalyticDB for PostgreSQL instance running in the cloud (you can get one at [common-buy.aliyun.com](https://common-buy.aliyun.com/?commodityCode=GreenplumPost&regionId=cn-hangzhou&request=%7B%22instance_rs_type%22%3A%22ecs%22%2C%22engine_version%22%3A%226.0%22%2C%22seg_node_num%22%3A%224%22%2C%22SampleData%22%3A%22false%22%2C%22vector_optimizor%22%3A%22Y%22%7D)).

After creating the instance, you should create a manager account by [API](https://www.alibabacloud.com/help/en/analyticdb-for-postgresql/developer-reference/api-gpdb-2016-05-03-createaccount) or 'Account Management' at the instance detail web page.

You should ensure you have `llama-index` installed:

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-analyticdb

%pip install llama-index-vector-stores-analyticdb

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

### Please provide parameters:[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AnalyticDBDemo/#please-provide-parameters)

In \[ \]:

Copied!

import os
import getpass

\# alibaba cloud ram ak and sk:
alibaba\_cloud\_ak \= ""
alibaba\_cloud\_sk \= ""

\# instance information:
region\_id \= "cn-hangzhou"  \# region id of the specific instance
instance\_id \= "gp-xxxx"  \# adb instance id
account \= "test\_account"  \# instance account name created by API or 'Account Management' at the instance detail web page
account\_password \= ""  \# instance account password

import os import getpass # alibaba cloud ram ak and sk: alibaba\_cloud\_ak = "" alibaba\_cloud\_sk = "" # instance information: region\_id = "cn-hangzhou" # region id of the specific instance instance\_id = "gp-xxxx" # adb instance id account = "test\_account" # instance account name created by API or 'Account Management' at the instance detail web page account\_password = "" # instance account password

### Import needed package dependencies:[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AnalyticDBDemo/#import-needed-package-dependencies)

In \[ \]:

Copied!

from llama\_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
)
from llama\_index.vector\_stores.analyticdb import AnalyticDBVectorStore

from llama\_index.core import ( VectorStoreIndex, SimpleDirectoryReader, StorageContext, ) from llama\_index.vector\_stores.analyticdb import AnalyticDBVectorStore

### Load some example data:[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AnalyticDBDemo/#load-some-example-data)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

### Read the data:[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AnalyticDBDemo/#read-the-data)

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()
print(f"Total documents: {len(documents)}")
print(f"First document, id: {documents\[0\].doc\_id}")
print(f"First document, hash: {documents\[0\].hash}")
print(
    "First document, text"
    f" ({len(documents\[0\].text)} characters):\\n{'='\*20}\\n{documents\[0\].text\[:360\]} ..."
)

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data() print(f"Total documents: {len(documents)}") print(f"First document, id: {documents\[0\].doc\_id}") print(f"First document, hash: {documents\[0\].hash}") print( "First document, text" f" ({len(documents\[0\].text)} characters):\\n{'='\*20}\\n{documents\[0\].text\[:360\]} ..." )

### Create the AnalyticDB Vector Store object:[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AnalyticDBDemo/#create-the-analyticdb-vector-store-object)

In \[ \]:

Copied!

analytic\_db\_store \= AnalyticDBVectorStore.from\_params(
    access\_key\_id\=alibaba\_cloud\_ak,
    access\_key\_secret\=alibaba\_cloud\_sk,
    region\_id\=region\_id,
    instance\_id\=instance\_id,
    account\=account,
    account\_password\=account\_password,
    namespace\="llama",
    collection\="llama",
    metrics\="cosine",
    embedding\_dimension\=1536,
)

analytic\_db\_store = AnalyticDBVectorStore.from\_params( access\_key\_id=alibaba\_cloud\_ak, access\_key\_secret=alibaba\_cloud\_sk, region\_id=region\_id, instance\_id=instance\_id, account=account, account\_password=account\_password, namespace="llama", collection="llama", metrics="cosine", embedding\_dimension=1536, )

### Build the Index from the Documents:[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AnalyticDBDemo/#build-the-index-from-the-documents)

In \[ \]:

Copied!

storage\_context \= StorageContext.from\_defaults(vector\_store\=analytic\_db\_store)

index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

storage\_context = StorageContext.from\_defaults(vector\_store=analytic\_db\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

### Query using the index:[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AnalyticDBDemo/#query-using-the-index)

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("Why did the author choose to work on AI?")

print(response.response)

query\_engine = index.as\_query\_engine() response = query\_engine.query("Why did the author choose to work on AI?") print(response.response)

### Delete the collection:[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AnalyticDBDemo/#delete-the-collection)

In \[ \]:

Copied!

analytic\_db\_store.delete\_collection()

analytic\_db\_store.delete\_collection()

Back to top

[Previous Amazon Neptune - Neptune Analytics vector store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AmazonNeptuneVectorDemo/)[Next Astra DB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AstraDBIndexDemo/)
