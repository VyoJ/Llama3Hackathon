Title: AWSDocDBDemo - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/AWSDocDBDemo/

Markdown Content:
AWSDocDBDemo - LlamaIndex


       

In \[ \]:

Copied!

%pip install llama\-index
%pip install llama\-index\-vector\-stores\-awsdocdb

%pip install llama-index %pip install llama-index-vector-stores-awsdocdb

In \[ \]:

Copied!

import pymongo
from llama\_index.vector\_stores.awsdocdb import AWSDocDbVectorStore
from llama\_index.core import VectorStoreIndex
from llama\_index.core import StorageContext
from llama\_index.core import SimpleDirectoryReader
import os

import pymongo from llama\_index.vector\_stores.awsdocdb import AWSDocDbVectorStore from llama\_index.core import VectorStoreIndex from llama\_index.core import StorageContext from llama\_index.core import SimpleDirectoryReader import os

In \[ \]:

Copied!

!mkdir \-p 'data/10k/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' \-O 'data/10k/uber\_2021.pdf'

!mkdir -p 'data/10k/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' -O 'data/10k/uber\_2021.pdf'

In \[ \]:

Copied!

mongo\_uri \= os.environ\["MONGO\_URI"\]
mongodb\_client \= pymongo.MongoClient(mongo\_uri)
store \= AWSDocDbVectorStore(mongodb\_client)
storage\_context \= StorageContext.from\_defaults(vector\_store\=store)
uber\_docs \= SimpleDirectoryReader(
    input\_files\=\["./data/10k/uber\_2021.pdf"\]
).load\_data()
index \= VectorStoreIndex.from\_documents(
    uber\_docs, storage\_context\=storage\_context
)

mongo\_uri = os.environ\["MONGO\_URI"\] mongodb\_client = pymongo.MongoClient(mongo\_uri) store = AWSDocDbVectorStore(mongodb\_client) storage\_context = StorageContext.from\_defaults(vector\_store=store) uber\_docs = SimpleDirectoryReader( input\_files=\["./data/10k/uber\_2021.pdf"\] ).load\_data() index = VectorStoreIndex.from\_documents( uber\_docs, storage\_context=storage\_context )

In \[ \]:

Copied!

response \= index.as\_query\_engine().query("What was Uber's revenue?")
display(f"{response}")

response = index.as\_query\_engine().query("What was Uber's revenue?") display(f"{response}")

In \[ \]:

Copied!

from llama\_index.core import Response

print(store.\_collection.count\_documents({}))
typed\_response \= (
    response if isinstance(response, Response) else response.get\_response()
)
ref\_doc\_id \= typed\_response.source\_nodes\[0\].node.ref\_doc\_id
print(store.\_collection.count\_documents({"metadata.ref\_doc\_id": ref\_doc\_id}))

from llama\_index.core import Response print(store.\_collection.count\_documents({})) typed\_response = ( response if isinstance(response, Response) else response.get\_response() ) ref\_doc\_id = typed\_response.source\_nodes\[0\].node.ref\_doc\_id print(store.\_collection.count\_documents({"metadata.ref\_doc\_id": ref\_doc\_id}))

In \[ \]:

Copied!

\# Test delete
if ref\_doc\_id:
    store.delete(ref\_doc\_id)
    print(store.\_collection.count\_documents({}))

\# Test delete if ref\_doc\_id: store.delete(ref\_doc\_id) print(store.\_collection.count\_documents({}))

Back to top

[Previous Github Issue Analysis](https://docs.llamaindex.ai/en/stable/examples/usecases/github_issue_analysis/)[Next Alibaba Cloud OpenSearch Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AlibabaCloudOpenSearchIndexDemo/)
