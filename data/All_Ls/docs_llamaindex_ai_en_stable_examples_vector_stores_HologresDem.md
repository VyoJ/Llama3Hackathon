Title: Hologres - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/HologresDemo/

Markdown Content:
Hologres - LlamaIndex


> [Hologres](https://www.alibabacloud.com/help/en/hologres/) is a one-stop real-time data warehouse, which can support high performance OLAP analysis and high QPS online services.

To run this notebook you need a Hologres instance running in the cloud. You can get one following [this link](https://www.alibabacloud.com/help/en/hologres/getting-started/purchase-a-hologres-instance#task-1918224).

After creating the instance, you should be able to figure out following configurations with [Hologres console](https://www.alibabacloud.com/help/en/hologres/user-guide/instance-list?spm=a2c63.p38356.0.0.79b34766nhwskN)

In \[ \]:

Copied!

test\_hologres\_config \= {
    "host": "<host>",
    "port": 80,
    "user": "<user>",
    "password": "<password>",
    "database": "<database>",
    "table\_name": "<table\_name>",
}

test\_hologres\_config = { "host": "", "port": 80, "user": "", "password": "", "database": "", "table\_name": "", }

By the way, you need to ensure you have `llama-index` installed:

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-hologres

%pip install llama-index-vector-stores-hologres

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

### Import needed package dependencies:[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/HologresDemo/#import-needed-package-dependencies)

In \[ \]:

Copied!

from llama\_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
)
from llama\_index.vector\_stores.hologres import HologresVectorStore

from llama\_index.core import ( VectorStoreIndex, SimpleDirectoryReader, StorageContext, ) from llama\_index.vector\_stores.hologres import HologresVectorStore

### Load some example data:[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/HologresDemo/#load-some-example-data)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!curl 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-o 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !curl 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -o 'data/paul\_graham/paul\_graham\_essay.txt'

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 75042  100 75042    0     0  31985      0  0:00:02  0:00:02 --:--:-- 31987

### Read the data:[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/HologresDemo/#read-the-data)

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

Total documents: 1
First document, id: 824dafc0-0aa1-4c80-b99c-33895cfc606a
First document, hash: 8430b3bdb65ee0a7853463b71e7e1e20beee3a3ce15ef3ec714919f8653b2eb9
First document, text (75014 characters):



What I Worked On

February 2021

Before college the two main things I worked on, outside of school, were writing and programming. I didn't write essays. I wrote what beginning writers were supposed to write then, and probably still are: short stories. My stories were awful. They had hardly any plot, just characters with strong feelings, which I imagined ma ...

### Create the AnalyticDB Vector Store object:[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/HologresDemo/#create-the-analyticdb-vector-store-object)

In \[ \]:

Copied!

hologres\_store \= HologresVectorStore.from\_param(
    host\=test\_hologres\_config\["host"\],
    port\=test\_hologres\_config\["port"\],
    user\=test\_hologres\_config\["user"\],
    password\=test\_hologres\_config\["password"\],
    database\=test\_hologres\_config\["database"\],
    table\_name\=test\_hologres\_config\["table\_name"\],
    embedding\_dimension\=1536,
    pre\_delete\_table\=True,
)

hologres\_store = HologresVectorStore.from\_param( host=test\_hologres\_config\["host"\], port=test\_hologres\_config\["port"\], user=test\_hologres\_config\["user"\], password=test\_hologres\_config\["password"\], database=test\_hologres\_config\["database"\], table\_name=test\_hologres\_config\["table\_name"\], embedding\_dimension=1536, pre\_delete\_table=True, )

### Build the Index from the Documents:[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/HologresDemo/#build-the-index-from-the-documents)

In \[ \]:

Copied!

storage\_context \= StorageContext.from\_defaults(vector\_store\=hologres\_store)

index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

storage\_context = StorageContext.from\_defaults(vector\_store=hologres\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

### Query using the index:[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/HologresDemo/#query-using-the-index)

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("Why did the author choose to work on AI?")

print(response.response)

query\_engine = index.as\_query\_engine() response = query\_engine.query("Why did the author choose to work on AI?") print(response.response)

The author was inspired to work on AI due to the influence of a science fiction novel, "The Moon is a Harsh Mistress," which featured an intelligent computer named Mike, and a PBS documentary showcasing Terry Winograd's use of the SHRDLU program. These experiences led the author to believe that creating intelligent machines was an imminent reality and sparked their interest in the field of AI.

Back to top

[Previous Firestore Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/FirestoreVectorStore/)[Next Jaguar Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/JaguarIndexDemo/)
