Title: MongoDBAtlasVectorSearch - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/MongoDBAtlasVectorSearch/

Markdown Content:
MongoDBAtlasVectorSearch - LlamaIndex


       

[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/docs/examples/vector_stores/MongoDBAtlasVectorSearch.ipynb)

MongoDB Atlas[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MongoDBAtlasVectorSearch/#mongodb-atlas)
---------------------------------------------------------------------------------------------------------------------

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-mongodb

%pip install llama-index-vector-stores-mongodb

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

\# Provide URI to constructor, or use environment variable
import pymongo
from llama\_index.vector\_stores.mongodb import MongoDBAtlasVectorSearch
from llama\_index.core import VectorStoreIndex
from llama\_index.core import StorageContext
from llama\_index.core import SimpleDirectoryReader

\# Provide URI to constructor, or use environment variable import pymongo from llama\_index.vector\_stores.mongodb import MongoDBAtlasVectorSearch from llama\_index.core import VectorStoreIndex from llama\_index.core import StorageContext from llama\_index.core import SimpleDirectoryReader

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/10k/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' \-O 'data/10k/uber\_2021.pdf'

!mkdir -p 'data/10k/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' -O 'data/10k/uber\_2021.pdf'

In \[ \]:

Copied!

\# mongo\_uri = os.environ\["MONGO\_URI"\]
mongo\_uri \= (
    "mongodb+srv://<username>:<password>@<host>?retryWrites=true&w=majority"
)
mongodb\_client \= pymongo.MongoClient(mongo\_uri)
store \= MongoDBAtlasVectorSearch(mongodb\_client)
storage\_context \= StorageContext.from\_defaults(vector\_store\=store)
uber\_docs \= SimpleDirectoryReader(
    input\_files\=\["./data/10k/uber\_2021.pdf"\]
).load\_data()
index \= VectorStoreIndex.from\_documents(
    uber\_docs, storage\_context\=storage\_context
)

\# mongo\_uri = os.environ\["MONGO\_URI"\] mongo\_uri = ( "mongodb+srv://:@?retryWrites=true&w=majority" ) mongodb\_client = pymongo.MongoClient(mongo\_uri) store = MongoDBAtlasVectorSearch(mongodb\_client) storage\_context = StorageContext.from\_defaults(vector\_store=store) uber\_docs = SimpleDirectoryReader( input\_files=\["./data/10k/uber\_2021.pdf"\] ).load\_data() index = VectorStoreIndex.from\_documents( uber\_docs, storage\_context=storage\_context )

In \[ \]:

Copied!

response \= index.as\_query\_engine().query("What was Uber's revenue?")
display(Markdown(f"<b>{response}</b>"))

response = index.as\_query\_engine().query("What was Uber's revenue?") display(Markdown(f"**{response}**"))

**Uber's revenue for 2021 was $17,455 million.**

In \[ \]:

Copied!

from llama\_index.core import Response

\# Initial size

print(store.\_collection.count\_documents({}))
\# Get a ref\_doc\_id
typed\_response \= (
    response if isinstance(response, Response) else response.get\_response()
)
ref\_doc\_id \= typed\_response.source\_nodes\[0\].node.ref\_doc\_id
print(store.\_collection.count\_documents({"metadata.ref\_doc\_id": ref\_doc\_id}))
\# Test store delete
if ref\_doc\_id:
    store.delete(ref\_doc\_id)
    print(store.\_collection.count\_documents({}))

from llama\_index.core import Response # Initial size print(store.\_collection.count\_documents({})) # Get a ref\_doc\_id typed\_response = ( response if isinstance(response, Response) else response.get\_response() ) ref\_doc\_id = typed\_response.source\_nodes\[0\].node.ref\_doc\_id print(store.\_collection.count\_documents({"metadata.ref\_doc\_id": ref\_doc\_id})) # Test store delete if ref\_doc\_id: store.delete(ref\_doc\_id) print(store.\_collection.count\_documents({}))

4454
1
4453

Note: For MongoDB Atlas, you have to additionally create an Atlas Search Index.

[MongoDB Docs | Create an Atlas Vector Search Index](https://www.mongodb.com/docs/atlas/atlas-vector-search/create-index/)

Back to top

[Previous MilvusOperatorFunctionDemo](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusOperatorFunctionDemo/)[Next now make sure you create the search index with the right name here](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MongoDBAtlasVectorSearchRAGFireworks/)
