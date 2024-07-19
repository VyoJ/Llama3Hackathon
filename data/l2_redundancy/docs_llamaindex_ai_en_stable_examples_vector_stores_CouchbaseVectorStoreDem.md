Title: CouchbaseVectorStoreDemo - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/CouchbaseVectorStoreDemo/

Markdown Content:
CouchbaseVectorStoreDemo - LlamaIndex


       

Couchbase Vector Store[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/CouchbaseVectorStoreDemo/#couchbase-vector-store)
---------------------------------------------------------------------------------------------------------------------------------------

[Couchbase](https://couchbase.com/) is an award-winning distributed NoSQL cloud database that delivers unmatched versatility, performance, scalability, and financial value for all of your cloud, mobile, AI, and edge computing applications. Couchbase embraces AI with coding assistance for developers and vector search for their applications.

Vector Search is a part of the [Full Text Search Service](https://docs.couchbase.com/server/current/learn/services-and-indexes/services/search-service.html) (Search Service) in Couchbase.

This tutorial explains how to use Vector Search in Couchbase. You can work with both [Couchbase Capella](https://www.couchbase.com/products/capella/) and your self-managed Couchbase Server.

### Installation[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/CouchbaseVectorStoreDemo/#installation)

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-couchbase

%pip install llama-index-vector-stores-couchbase

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

### Creating Couchbase Connection[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/CouchbaseVectorStoreDemo/#creating-couchbase-connection)

We create a connection to the Couchbase cluster initially and then pass the cluster object to the Vector Store.

Here, we are connecting using the username and password. You can also connect using any other supported way to your cluster.

For more information on connecting to the Couchbase cluster, please check the [Python SDK documentation](https://docs.couchbase.com/python-sdk/current/hello-world/start-using-sdk.html#connect).

In \[ \]:

Copied!

COUCHBASE\_CONNECTION\_STRING \= (
    "couchbase://localhost"  \# or "couchbases://localhost" if using TLS
)
DB\_USERNAME \= "Administrator"
DB\_PASSWORD \= "P@ssword1!"

COUCHBASE\_CONNECTION\_STRING = ( "couchbase://localhost" # or "couchbases://localhost" if using TLS ) DB\_USERNAME = "Administrator" DB\_PASSWORD = "P@ssword1!"

In \[ \]:

Copied!

from datetime import timedelta

from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster
from couchbase.options import ClusterOptions

auth \= PasswordAuthenticator(DB\_USERNAME, DB\_PASSWORD)
options \= ClusterOptions(auth)
cluster \= Cluster(COUCHBASE\_CONNECTION\_STRING, options)

\# Wait until the cluster is ready for use.
cluster.wait\_until\_ready(timedelta(seconds\=5))

from datetime import timedelta from couchbase.auth import PasswordAuthenticator from couchbase.cluster import Cluster from couchbase.options import ClusterOptions auth = PasswordAuthenticator(DB\_USERNAME, DB\_PASSWORD) options = ClusterOptions(auth) cluster = Cluster(COUCHBASE\_CONNECTION\_STRING, options) # Wait until the cluster is ready for use. cluster.wait\_until\_ready(timedelta(seconds=5))

### Creating the Search Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/CouchbaseVectorStoreDemo/#creating-the-search-index)

Currently, the Search index needs to be created from the Couchbase Capella or Server UI or using the REST interface.

Let us define a Search index with the name `vector-index` on the `testing` bucket

For this example, let us use the Import Index feature on the Search Service on the UI.

We are defining an index on the testing bucket’s `_default` scope on the `_default` collection with the vector field set to `embedding` with 1536 dimensions and the text field set to text. We are also indexing and storing all the fields under metadata in the document as a dynamic mapping to account for varying document structures. The similarity metric is set to `dot_product`.

#### How to Import an Index to the Full Text Search service?[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/CouchbaseVectorStoreDemo/#how-to-import-an-index-to-the-full-text-search-service)

*   [Couchbase Server](https://docs.couchbase.com/server/current/search/import-search-index.html)
    
    *   Click on Search -> Add Index -> Import
    *   Copy the following Index definition in the Import screen
    *   Click on Create Index to create the index.
*   [Couchbase Capella](https://docs.couchbase.com/cloud/search/import-search-index.html)
    
    *   Copy the index definition to a new file `index.json`
    *   Import the file in Capella using the instructions in the documentation.
    *   Click on Create Index to create the index.

#### Index Definition[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/CouchbaseVectorStoreDemo/#index-definition)

```
{
 "name": "vector-index",
 "type": "fulltext-index",
 "params": {
  "doc_config": {
   "docid_prefix_delim": "",
   "docid_regexp": "",
   "mode": "type_field",
   "type_field": "type"
  },
  "mapping": {
   "default_analyzer": "standard",
   "default_datetime_parser": "dateTimeOptional",
   "default_field": "_all",
   "default_mapping": {
    "dynamic": true,
    "enabled": true,
    "properties": {
     "metadata": {
      "dynamic": true,
      "enabled": true
     },
     "embedding": {
      "enabled": true,
      "dynamic": false,
      "fields": [
       {
        "dims": 1536,
        "index": true,
        "name": "embedding",
        "similarity": "dot_product",
        "type": "vector",
        "vector_index_optimized_for": "recall"
       }
      ]
     },
     "text": {
      "enabled": true,
      "dynamic": false,
      "fields": [
       {
        "index": true,
        "name": "text",
        "store": true,
        "type": "text"
       }
      ]
     }
    }
   },
   "default_type": "_default",
   "docvalues_dynamic": false,
   "index_dynamic": true,
   "store_dynamic": true,
   "type_field": "_type"
  },
  "store": {
   "indexType": "scorch",
   "segmentVersion": 16
  }
 },
 "sourceType": "gocbcore",
 "sourceName": "testing",
 "sourceParams": {},
 "planParams": {
  "maxPartitionsPerPIndex": 103,
  "indexPartitions": 10,
  "numReplicas": 0
 }
}
```

We will now set the bucket, scope, and collection names in the Couchbase cluster that we want to use for Vector Search.

For this example, we are using the default scope & collections.

In \[ \]:

Copied!

BUCKET\_NAME \= "testing"
SCOPE\_NAME \= "\_default"
COLLECTION\_NAME \= "\_default"
SEARCH\_INDEX\_NAME \= "vector-index"

BUCKET\_NAME = "testing" SCOPE\_NAME = "\_default" COLLECTION\_NAME = "\_default" SEARCH\_INDEX\_NAME = "vector-index"

In \[ \]:

Copied!

\# Import required packages
from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.core import StorageContext
from llama\_index.core import Settings
from llama\_index.vector\_stores.couchbase import CouchbaseVectorStore

\# Import required packages from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.core import StorageContext from llama\_index.core import Settings from llama\_index.vector\_stores.couchbase import CouchbaseVectorStore

For this tutorial, we will use OpenAI embeddings

In \[ \]:

Copied!

import os
import getpass

os.environ\["OPENAI\_API\_KEY"\] \= getpass.getpass("OpenAI API Key:")

import os import getpass os.environ\["OPENAI\_API\_KEY"\] = getpass.getpass("OpenAI API Key:")

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

#### Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/CouchbaseVectorStoreDemo/#download-data)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

\--2024-04-09 23:31:46--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 2606:50c0:8000::154, 2606:50c0:8001::154, 2606:50c0:8003::154, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|2606:50c0:8000::154|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 75042 (73K) \[text/plain\]
Saving to: ‘data/paul\_graham/paul\_graham\_essay.txt’

data/paul\_graham/pa 100%\[>\]  73.28K  --.-KB/s    in 0.008s  

2024-04-09 23:31:46 (8.97 MB/s) - ‘data/paul\_graham/paul\_graham\_essay.txt’ saved \[75042/75042\]

#### Load the documents[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/CouchbaseVectorStoreDemo/#load-the-documents)

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data()

In \[ \]:

Copied!

vector\_store \= CouchbaseVectorStore(
    cluster\=cluster,
    bucket\_name\=BUCKET\_NAME,
    scope\_name\=SCOPE\_NAME,
    collection\_name\=COLLECTION\_NAME,
    index\_name\=SEARCH\_INDEX\_NAME,
)

vector\_store = CouchbaseVectorStore( cluster=cluster, bucket\_name=BUCKET\_NAME, scope\_name=SCOPE\_NAME, collection\_name=COLLECTION\_NAME, index\_name=SEARCH\_INDEX\_NAME, )

In \[ \]:

Copied!

storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"

### Basic Example[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/CouchbaseVectorStoreDemo/#basic-example)

We will ask the query engine a question about the essay we just indexed.

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What were his investments in Y Combinator?")
print(response)

query\_engine = index.as\_query\_engine() response = query\_engine.query("What were his investments in Y Combinator?") print(response)

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
His investments in Y Combinator were $6k per founder, totaling $12k in the typical two-founder case, in return for 6% equity.

### Metadata Filters[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/CouchbaseVectorStoreDemo/#metadata-filters)

We will create some example documents with metadata so that we can see how to filter documents based on metadata.

In \[ \]:

Copied!

from llama\_index.core.schema import TextNode

nodes \= \[
    TextNode(
        text\="The Shawshank Redemption",
        metadata\={
            "author": "Stephen King",
            "theme": "Friendship",
        },
    ),
    TextNode(
        text\="The Godfather",
        metadata\={
            "director": "Francis Ford Coppola",
            "theme": "Mafia",
        },
    ),
    TextNode(
        text\="Inception",
        metadata\={
            "director": "Christopher Nolan",
        },
    ),
\]
vector\_store.add(nodes)

from llama\_index.core.schema import TextNode nodes = \[ TextNode( text="The Shawshank Redemption", metadata={ "author": "Stephen King", "theme": "Friendship", }, ), TextNode( text="The Godfather", metadata={ "director": "Francis Ford Coppola", "theme": "Mafia", }, ), TextNode( text="Inception", metadata={ "director": "Christopher Nolan", }, ), \] vector\_store.add(nodes)

Out\[ \]:

\['5abb42cf-7312-46eb-859e-60df4f92842a',
 'b90525f4-38bf-453c-a51a-5f0718bccc98',
 '22f732d0-da17-4bad-b3cd-b54e2102367a'\]

In \[ \]:

Copied!

\# Metadata filter
from llama\_index.core.vector\_stores import ExactMatchFilter, MetadataFilters

filters \= MetadataFilters(
    filters\=\[ExactMatchFilter(key\="theme", value\="Mafia")\]
)

retriever \= index.as\_retriever(filters\=filters)

retriever.retrieve("What is inception about?")

\# Metadata filter from llama\_index.core.vector\_stores import ExactMatchFilter, MetadataFilters filters = MetadataFilters( filters=\[ExactMatchFilter(key="theme", value="Mafia")\] ) retriever = index.as\_retriever(filters=filters) retriever.retrieve("What is inception about?")

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"

Out\[ \]:

\[NodeWithScore(node=TextNode(id\_='b90525f4-38bf-453c-a51a-5f0718bccc98', embedding=None, metadata={'director': 'Francis Ford Coppola', 'theme': 'Mafia'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='The Godfather', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.3068528194400547)\]

### Custom Filters and overriding Query[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/CouchbaseVectorStoreDemo/#custom-filters-and-overriding-query)

Couchbase supports `ExactMatchFilters` only at the moment via LlamaIndex. Couchbase supports a wide range of filters, including range filters, geospatial filters, and more. To use these filters, you can pass them in as a list of dictionaries to the `cb_search_options` parameter. The different search/query possibilities for the search\_options can be found [here](https://docs.couchbase.com/server/current/search/search-request-params.html#query-object).

In \[ \]:

Copied!

def custom\_query(query, query\_str):
    print("custom query", query)
    return query

query\_engine \= index.as\_query\_engine(
    vector\_store\_kwargs\={
        "cb\_search\_options": {
            "query": {"match": "growing up", "field": "text"}
        },
        "custom\_query": custom\_query,
    }
)
response \= query\_engine.query("what were his investments in Y Combinator?")
print(response)

def custom\_query(query, query\_str): print("custom query", query) return query query\_engine = index.as\_query\_engine( vector\_store\_kwargs={ "cb\_search\_options": { "query": {"match": "growing up", "field": "text"} }, "custom\_query": custom\_query, } ) response = query\_engine.query("what were his investments in Y Combinator?") print(response)

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
His investments in Y Combinator were based on a combination of the deal he did with Julian ($10k for 10%) and what Robert said MIT grad students got for the summer ($6k). He invested $6k per founder, which in the typical two-founder case was $12k, in return for 6%.

Back to top

[Previous ClickHouse Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ClickHouseIndexDemo/)[Next DashVector Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DashvectorIndexDemo/)
