Title: Redis Vector Store - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/RedisIndexDemo/

Markdown Content:
Redis Vector Store - LlamaIndex


In this notebook we are going to show a quick demo of using the RedisVectorStore.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install \-U llama\-index llama\-index\-vector\-stores\-redis llama\-index\-embeddings\-cohere llama\-index\-embeddings\-openai

%pip install -U llama-index llama-index-vector-stores-redis llama-index-embeddings-cohere llama-index-embeddings-openai

In \[ \]:

Copied!

import os
import getpass
import sys
import logging
import textwrap
import warnings

warnings.filterwarnings("ignore")

\# Uncomment to see debug logs
logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.vector\_stores.redis import RedisVectorStore

import os import getpass import sys import logging import textwrap import warnings warnings.filterwarnings("ignore") # Uncomment to see debug logs logging.basicConfig(stream=sys.stdout, level=logging.INFO) from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.vector\_stores.redis import RedisVectorStore

### Start Redis[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RedisIndexDemo/#start-redis)

The easiest way to start Redis is using the [Redis Stack](https://hub.docker.com/r/redis/redis-stack) docker image or quickly signing up for a [FREE Redis Cloud](https://redis.com/try-free) instance.

To follow every step of this tutorial, launch the image as follows:

docker run \--name redis-vecdb \-d \-p 6379:6379 \-p 8001:8001 redis/redis-stack:latest

This will also launch the RedisInsight UI on port 8001 which you can view at [http://localhost:8001](http://localhost:8001/).

### Setup OpenAI[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RedisIndexDemo/#setup-openai)

Lets first begin by adding the openai api key. This will allow us to access openai for embeddings and to use chatgpt.

In \[ \]:

Copied!

oai\_api\_key \= getpass.getpass("OpenAI API Key:")
os.environ\["OPENAI\_API\_KEY"\] \= oai\_api\_key

oai\_api\_key = getpass.getpass("OpenAI API Key:") os.environ\["OPENAI\_API\_KEY"\] = oai\_api\_key

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

\--2024-04-10 19:35:33--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 2606:50c0:8003::154, 2606:50c0:8000::154, 2606:50c0:8002::154, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|2606:50c0:8003::154|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 75042 (73K) \[text/plain\]
Saving to: ‘data/paul\_graham/paul\_graham\_essay.txt’

data/paul\_graham/pa 100%\[>\]  73.28K  --.-KB/s    in 0.03s   

2024-04-10 19:35:33 (2.15 MB/s) - ‘data/paul\_graham/paul\_graham\_essay.txt’ saved \[75042/75042\]

### Read in a dataset[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RedisIndexDemo/#read-in-a-dataset)

Here we will use a set of Paul Graham essays to provide the text to turn into embeddings, store in a `RedisVectorStore` and query to find context for our LLM QnA loop.

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham").load\_data()
print(
    "Document ID:",
    documents\[0\].id\_,
    "Document Filename:",
    documents\[0\].metadata\["file\_name"\],
)

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham").load\_data() print( "Document ID:", documents\[0\].id\_, "Document Filename:", documents\[0\].metadata\["file\_name"\], )

Document ID: 7056f7ba-3513-4ef4-9792-2bd28040aaed Document Filename: paul\_graham\_essay.txt

### Initialize the default Redis Vector Store[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RedisIndexDemo/#initialize-the-default-redis-vector-store)

Now we have our documents prepared, we can initialize the Redis Vector Store with **default** settings. This will allow us to store our vectors in Redis and create an index for real-time search.

In \[ \]:

Copied!

from llama\_index.core import StorageContext
from redis import Redis

\# create a Redis client connection
redis\_client \= Redis.from\_url("redis://localhost:6379")

\# create the vector store wrapper
vector\_store \= RedisVectorStore(redis\_client\=redis\_client, overwrite\=True)

\# load storage context
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

\# build and load index from documents and storage context
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)
\# index = VectorStoreIndex.from\_vector\_store(vector\_store=vector\_store)

from llama\_index.core import StorageContext from redis import Redis # create a Redis client connection redis\_client = Redis.from\_url("redis://localhost:6379") # create the vector store wrapper vector\_store = RedisVectorStore(redis\_client=redis\_client, overwrite=True) # load storage context storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) # build and load index from documents and storage context index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context ) # index = VectorStoreIndex.from\_vector\_store(vector\_store=vector\_store)

19:39:17 llama\_index.vector\_stores.redis.base INFO   Using default RedisVectorStore schema.
19:39:19 httpx INFO   HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
19:39:19 llama\_index.vector\_stores.redis.base INFO   Added 22 documents to index llama\_index

### Query the default vector store[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RedisIndexDemo/#query-the-default-vector-store)

Now that we have our data stored in the index, we can ask questions against the index.

The index will use the data as the knowledge base for an LLM. The default setting for as\_query\_engine() utilizes OpenAI embeddings and GPT as the language model. Therefore, an OpenAI key is required unless you opt for a customized or local language model.

Below we will test searches against out index and then full RAG with an LLM.

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()
retriever \= index.as\_retriever()

query\_engine = index.as\_query\_engine() retriever = index.as\_retriever()

In \[ \]:

Copied!

result\_nodes \= retriever.retrieve("What did the author learn?")
for node in result\_nodes:
    print(node)

result\_nodes = retriever.retrieve("What did the author learn?") for node in result\_nodes: print(node)

19:39:22 httpx INFO   HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
19:39:22 llama\_index.vector\_stores.redis.base INFO   Querying index llama\_index with filters \*
19:39:22 llama\_index.vector\_stores.redis.base INFO   Found 2 results for query with id \['llama\_index/vector\_adb6b7ce-49bb-4961-8506-37082c02a389', 'llama\_index/vector\_e39be1fe-32d0-456e-b211-4efabd191108'\]
Node ID: adb6b7ce-49bb-4961-8506-37082c02a389
Text: What I Worked On  February 2021  Before college the two main
things I worked on, outside of school, were writing and programming. I
didn't write essays. I wrote what beginning writers were supposed to
write then, and probably still are: short stories. My stories were
awful. They had hardly any plot, just characters with strong feelings,
which I ...
Score:  0.820

Node ID: e39be1fe-32d0-456e-b211-4efabd191108
Text: Except for a few officially anointed thinkers who went to the
right parties in New York, the only people allowed to publish essays
were specialists writing about their specialties. There were so many
essays that had never been written, because there had been no way to
publish them. Now they could be, and I was going to write them. \[12\]
I've wor...
Score:  0.819

In \[ \]:

Copied!

response \= query\_engine.query("What did the author learn?")
print(textwrap.fill(str(response), 100))

response = query\_engine.query("What did the author learn?") print(textwrap.fill(str(response), 100))

19:39:25 httpx INFO   HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
19:39:25 llama\_index.vector\_stores.redis.base INFO   Querying index llama\_index with filters \*
19:39:25 llama\_index.vector\_stores.redis.base INFO   Found 2 results for query with id \['llama\_index/vector\_adb6b7ce-49bb-4961-8506-37082c02a389', 'llama\_index/vector\_e39be1fe-32d0-456e-b211-4efabd191108'\]
19:39:27 httpx INFO   HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
The author learned that working on things that weren't prestigious often led to valuable discoveries
and indicated the right kind of motives. Despite the lack of initial prestige, pursuing such work
could be a sign of genuine potential and appropriate motivations, steering clear of the common
pitfall of being driven solely by the desire to impress others.

In \[ \]:

Copied!

result\_nodes \= retriever.retrieve("What was a hard moment for the author?")
for node in result\_nodes:
    print(node)

result\_nodes = retriever.retrieve("What was a hard moment for the author?") for node in result\_nodes: print(node)

19:39:27 httpx INFO   HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
19:39:27 llama\_index.vector\_stores.redis.base INFO   Querying index llama\_index with filters \*
19:39:27 llama\_index.vector\_stores.redis.base INFO   Found 2 results for query with id \['llama\_index/vector\_adb6b7ce-49bb-4961-8506-37082c02a389', 'llama\_index/vector\_e39be1fe-32d0-456e-b211-4efabd191108'\]
Node ID: adb6b7ce-49bb-4961-8506-37082c02a389
Text: What I Worked On  February 2021  Before college the two main
things I worked on, outside of school, were writing and programming. I
didn't write essays. I wrote what beginning writers were supposed to
write then, and probably still are: short stories. My stories were
awful. They had hardly any plot, just characters with strong feelings,
which I ...
Score:  0.802

Node ID: e39be1fe-32d0-456e-b211-4efabd191108
Text: Except for a few officially anointed thinkers who went to the
right parties in New York, the only people allowed to publish essays
were specialists writing about their specialties. There were so many
essays that had never been written, because there had been no way to
publish them. Now they could be, and I was going to write them. \[12\]
I've wor...
Score:  0.799

In \[ \]:

Copied!

response \= query\_engine.query("What was a hard moment for the author?")
print(textwrap.fill(str(response), 100))

response = query\_engine.query("What was a hard moment for the author?") print(textwrap.fill(str(response), 100))

19:39:29 httpx INFO   HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
19:39:29 llama\_index.vector\_stores.redis.base INFO   Querying index llama\_index with filters \*
19:39:29 llama\_index.vector\_stores.redis.base INFO   Found 2 results for query with id \['llama\_index/vector\_adb6b7ce-49bb-4961-8506-37082c02a389', 'llama\_index/vector\_e39be1fe-32d0-456e-b211-4efabd191108'\]
19:39:31 httpx INFO   HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
A hard moment for the author was when one of his programs on the IBM 1401 mainframe didn't
terminate, leading to a technical error and an uncomfortable situation with the data center manager.

In \[ \]:

Copied!

index.vector\_store.delete\_index()

index.vector\_store.delete\_index()

19:39:34 llama\_index.vector\_stores.redis.base INFO   Deleting index llama\_index

### Use a custom index schema[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RedisIndexDemo/#use-a-custom-index-schema)

In most use cases, you need the ability to customize the underling index configuration and specification. For example, this is handy in order to define specific metadata filters you wish to enable.

With Redis, this is as simple as defining an index schema object (from file or dict) and passing it through to the vector store client wrapper.

For this example, we will:

1.  switch the embedding model to [Cohere](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RedisIndexDemo/cohereai.com)
2.  add an additional metadata field for the document `updated_at` timestamp
3.  index the existing `file_name` metadata field

In \[ \]:

Copied!

from llama\_index.core.settings import Settings
from llama\_index.embeddings.cohere import CohereEmbedding

\# set up Cohere Key
co\_api\_key \= getpass.getpass("Cohere API Key:")
os.environ\["CO\_API\_KEY"\] \= co\_api\_key

\# set llamaindex to use Cohere embeddings
Settings.embed\_model \= CohereEmbedding()

from llama\_index.core.settings import Settings from llama\_index.embeddings.cohere import CohereEmbedding # set up Cohere Key co\_api\_key = getpass.getpass("Cohere API Key:") os.environ\["CO\_API\_KEY"\] = co\_api\_key # set llamaindex to use Cohere embeddings Settings.embed\_model = CohereEmbedding()

In \[ \]:

Copied!

from redisvl.schema import IndexSchema

custom\_schema \= IndexSchema.from\_dict(
    {
        \# customize basic index specs
        "index": {
            "name": "paul\_graham",
            "prefix": "essay",
            "key\_separator": ":",
        },
        \# customize fields that are indexed
        "fields": \[
            \# required fields for llamaindex
            {"type": "tag", "name": "id"},
            {"type": "tag", "name": "doc\_id"},
            {"type": "text", "name": "text"},
            \# custom metadata fields
            {"type": "numeric", "name": "updated\_at"},
            {"type": "tag", "name": "file\_name"},
            \# custom vector field definition for cohere embeddings
            {
                "type": "vector",
                "name": "vector",
                "attrs": {
                    "dims": 1024,
                    "algorithm": "hnsw",
                    "distance\_metric": "cosine",
                },
            },
        \],
    }
)

from redisvl.schema import IndexSchema custom\_schema = IndexSchema.from\_dict( { # customize basic index specs "index": { "name": "paul\_graham", "prefix": "essay", "key\_separator": ":", }, # customize fields that are indexed "fields": \[ # required fields for llamaindex {"type": "tag", "name": "id"}, {"type": "tag", "name": "doc\_id"}, {"type": "text", "name": "text"}, # custom metadata fields {"type": "numeric", "name": "updated\_at"}, {"type": "tag", "name": "file\_name"}, # custom vector field definition for cohere embeddings { "type": "vector", "name": "vector", "attrs": { "dims": 1024, "algorithm": "hnsw", "distance\_metric": "cosine", }, }, \], } )

In \[ \]:

Copied!

custom\_schema.index

custom\_schema.index

Out\[ \]:

IndexInfo(name='paul\_graham', prefix='essay', key\_separator=':', storage\_type=<StorageType.HASH: 'hash'>)

In \[ \]:

Copied!

custom\_schema.fields

custom\_schema.fields

Out\[ \]:

{'id': TagField(name='id', type='tag', path=None, attrs=TagFieldAttributes(sortable=False, separator=',', case\_sensitive=False, withsuffixtrie=False)),
 'doc\_id': TagField(name='doc\_id', type='tag', path=None, attrs=TagFieldAttributes(sortable=False, separator=',', case\_sensitive=False, withsuffixtrie=False)),
 'text': TextField(name='text', type='text', path=None, attrs=TextFieldAttributes(sortable=False, weight=1, no\_stem=False, withsuffixtrie=False, phonetic\_matcher=None)),
 'updated\_at': NumericField(name='updated\_at', type='numeric', path=None, attrs=NumericFieldAttributes(sortable=False)),
 'file\_name': TagField(name='file\_name', type='tag', path=None, attrs=TagFieldAttributes(sortable=False, separator=',', case\_sensitive=False, withsuffixtrie=False)),
 'vector': HNSWVectorField(name='vector', type='vector', path=None, attrs=HNSWVectorFieldAttributes(dims=1024, algorithm=<VectorIndexAlgorithm.HNSW: 'HNSW'>, datatype=<VectorDataType.FLOAT32: 'FLOAT32'>, distance\_metric=<VectorDistanceMetric.COSINE: 'COSINE'>, initial\_cap=None, m=16, ef\_construction=200, ef\_runtime=10, epsilon=0.01))}

Learn more about [schema and index design](https://redisvl.com/) with redis.

In \[ \]:

Copied!

from datetime import datetime

def date\_to\_timestamp(date\_string: str) \-> int:
    date\_format: str \= "%Y-%m-%d"
    return int(datetime.strptime(date\_string, date\_format).timestamp())

\# iterate through documents and add new field
for document in documents:
    document.metadata\["updated\_at"\] \= date\_to\_timestamp(
        document.metadata\["last\_modified\_date"\]
    )

from datetime import datetime def date\_to\_timestamp(date\_string: str) -> int: date\_format: str = "%Y-%m-%d" return int(datetime.strptime(date\_string, date\_format).timestamp()) # iterate through documents and add new field for document in documents: document.metadata\["updated\_at"\] = date\_to\_timestamp( document.metadata\["last\_modified\_date"\] )

In \[ \]:

Copied!

vector\_store \= RedisVectorStore(
    schema\=custom\_schema,  \# provide customized schema
    redis\_client\=redis\_client,
    overwrite\=True,
)

storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

\# build and load index from documents and storage context
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

vector\_store = RedisVectorStore( schema=custom\_schema, # provide customized schema redis\_client=redis\_client, overwrite=True, ) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) # build and load index from documents and storage context index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

19:40:05 httpx INFO   HTTP Request: POST https://api.cohere.ai/v1/embed "HTTP/1.1 200 OK"
19:40:06 httpx INFO   HTTP Request: POST https://api.cohere.ai/v1/embed "HTTP/1.1 200 OK"
19:40:06 httpx INFO   HTTP Request: POST https://api.cohere.ai/v1/embed "HTTP/1.1 200 OK"
19:40:06 llama\_index.vector\_stores.redis.base INFO   Added 22 documents to index paul\_graham

### Query the vector store and filter on metadata[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RedisIndexDemo/#query-the-vector-store-and-filter-on-metadata)

Now that we have additional metadata indexed in Redis, let's try some queries with filters.

In \[ \]:

Copied!

from llama\_index.core.vector\_stores import (
    MetadataFilters,
    MetadataFilter,
    ExactMatchFilter,
)

retriever \= index.as\_retriever(
    similarity\_top\_k\=3,
    filters\=MetadataFilters(
        filters\=\[
            ExactMatchFilter(key\="file\_name", value\="paul\_graham\_essay.txt"),
            MetadataFilter(
                key\="updated\_at",
                value\=date\_to\_timestamp("2023-01-01"),
                operator\=">=",
            ),
            MetadataFilter(
                key\="text",
                value\="learn",
                operator\="text\_match",
            ),
        \],
        condition\="and",
    ),
)

from llama\_index.core.vector\_stores import ( MetadataFilters, MetadataFilter, ExactMatchFilter, ) retriever = index.as\_retriever( similarity\_top\_k=3, filters=MetadataFilters( filters=\[ ExactMatchFilter(key="file\_name", value="paul\_graham\_essay.txt"), MetadataFilter( key="updated\_at", value=date\_to\_timestamp("2023-01-01"), operator=">=", ), MetadataFilter( key="text", value="learn", operator="text\_match", ), \], condition="and", ), )

In \[ \]:

Copied!

result\_nodes \= retriever.retrieve("What did the author learn?")

for node in result\_nodes:
    print(node)

result\_nodes = retriever.retrieve("What did the author learn?") for node in result\_nodes: print(node)

19:40:22 httpx INFO   HTTP Request: POST https://api.cohere.ai/v1/embed "HTTP/1.1 200 OK"

19:40:22 llama\_index.vector\_stores.redis.base INFO   Querying index paul\_graham with filters ((@file\_name:{paul\_graham\_essay\\.txt} @updated\_at:\[1672549200 +inf\]) @text:(learn))
19:40:22 llama\_index.vector\_stores.redis.base INFO   Found 3 results for query with id \['essay:0df3b734-ecdb-438e-8c90-f21a8c80f552', 'essay:01108c0d-140b-4dcc-b581-c38b7df9251e', 'essay:ced36463-ac36-46b0-b2d7-935c1b38b781'\]
Node ID: 0df3b734-ecdb-438e-8c90-f21a8c80f552
Text: All that seemed left for philosophy were edge cases that people
in other fields felt could safely be ignored.  I couldn't have put
this into words when I was 18. All I knew at the time was that I kept
taking philosophy courses and they kept being boring. So I decided to
switch to AI.  AI was in the air in the mid 1980s, but there were two
things...
Score:  0.410

Node ID: 01108c0d-140b-4dcc-b581-c38b7df9251e
Text: It was not, in fact, simply a matter of teaching SHRDLU more
words. That whole way of doing AI, with explicit data structures
representing concepts, was not going to work. Its brokenness did, as
so often happens, generate a lot of opportunities to write papers
about various band-aids that could be applied to it, but it was never
going to get us ...
Score:  0.390

Node ID: ced36463-ac36-46b0-b2d7-935c1b38b781
Text: Grad students could take classes in any department, and my
advisor, Tom Cheatham, was very easy going. If he even knew about the
strange classes I was taking, he never said anything.  So now I was in
a PhD program in computer science, yet planning to be an artist, yet
also genuinely in love with Lisp hacking and working away at On Lisp.
In other...
Score:  0.389

### Restoring from an existing index in Redis[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RedisIndexDemo/#restoring-from-an-existing-index-in-redis)

Restoring from an index requires a Redis connection client (or URL), `overwrite=False`, and passing in the same schema object used before. (This can be offloaded to a YAML file for convenience using `.to_yaml()`)

In \[ \]:

Copied!

custom\_schema.to\_yaml("paul\_graham.yaml")

custom\_schema.to\_yaml("paul\_graham.yaml")

In \[ \]:

Copied!

vector\_store \= RedisVectorStore(
    schema\=IndexSchema.from\_yaml("paul\_graham.yaml"),
    redis\_client\=redis\_client,
)
index \= VectorStoreIndex.from\_vector\_store(vector\_store\=vector\_store)

vector\_store = RedisVectorStore( schema=IndexSchema.from\_yaml("paul\_graham.yaml"), redis\_client=redis\_client, ) index = VectorStoreIndex.from\_vector\_store(vector\_store=vector\_store)

19:40:28 redisvl.index.index INFO   Index already exists, not overwriting.

**In the near future** -- we will implement a convenience method to load just using an index name:

RedisVectorStore.from\_existing\_index(index\_name\="paul\_graham", redis\_client\=redis\_client)

### Deleting documents or index completely[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RedisIndexDemo/#deleting-documents-or-index-completely)

Sometimes it may be useful to delete documents or the entire index. This can be done using the `delete` and `delete_index` methods.

In \[ \]:

Copied!

document\_id \= documents\[0\].doc\_id
document\_id

document\_id = documents\[0\].doc\_id document\_id

Out\[ \]:

'7056f7ba-3513-4ef4-9792-2bd28040aaed'

In \[ \]:

Copied!

print("Number of documents before deleting", redis\_client.dbsize())
vector\_store.delete(document\_id)
print("Number of documents after deleting", redis\_client.dbsize())

print("Number of documents before deleting", redis\_client.dbsize()) vector\_store.delete(document\_id) print("Number of documents after deleting", redis\_client.dbsize())

Number of documents before deleting 22
19:40:32 llama\_index.vector\_stores.redis.base INFO   Deleted 22 documents from index paul\_graham
Number of documents after deleting 0

However, the Redis index still exists (with no associated documents) for continuous upsert.

In \[ \]:

Copied!

vector\_store.index\_exists()

vector\_store.index\_exists()

Out\[ \]:

True

In \[ \]:

Copied!

\# now lets delete the index entirely
\# this will delete all the documents and the index
vector\_store.delete\_index()

\# now lets delete the index entirely # this will delete all the documents and the index vector\_store.delete\_index()

19:40:37 llama\_index.vector\_stores.redis.base INFO   Deleting index paul\_graham

In \[ \]:

Copied!

print("Number of documents after deleting", redis\_client.dbsize())

print("Number of documents after deleting", redis\_client.dbsize())

Number of documents after deleting 0

### Troubleshooting[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RedisIndexDemo/#troubleshooting)

If you get an empty query result, there a couple of issues to check:

#### Schema[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RedisIndexDemo/#schema)

Unlike other vector stores, Redis expects users to explicitly define the schema for the index. This is for a few reasons:

1.  Redis is used for many use cases, including real-time vector search, but also for standard document storage/retrieval, caching, messaging, pub/sub, session mangement, and more. Not all attributes on records need to be indexed for search. This is partially an efficiency thing, and partially an attempt to minimize user foot guns.
2.  All index schemas, when using Redis & LlamaIndex, must include the following fields `id`, `doc_id`, `text`, and `vector`, at a minimum.

Instantiate your `RedisVectorStore` with the default schema (assumes OpenAI embeddings), or with a custom schema (see above).

#### Prefix issues[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RedisIndexDemo/#prefix-issues)

Redis expects all records to have a key prefix that segments the keyspace into "partitions" for potentially different applications, use cases, and clients.

Make sure that the chosen `prefix`, as part of the index schema, is consistent across your code (tied to a specific index).

To see what prefix your index was created with, you can run `FT.INFO <name of your index>` in the Redis CLI and look under `index_definition` => `prefixes`.

#### Data vs Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RedisIndexDemo/#data-vs-index)

Redis treats the records in the dataset and the index as different entities. This allows you more flexibility in performing updates, upserts, and index schema migrations.

If you have an existing index and want to make sure it's dropped, you can run `FT.DROPINDEX <name of your index>` in the Redis CLI. Note that this will _not_ drop your actual data unless you pass `DD`

#### Empty queries when using metadata[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RedisIndexDemo/#empty-queries-when-using-metadata)

If you add metadata to the index _after_ it has already been created and then try to query over that metadata, your queries will come back empty.

Redis indexes fields upon index creation only (similar to how it indexes the prefixes, above).

Back to top

[Previous Qdrant Vector Store - Default Qdrant Filters](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Qdrant_using_qdrant_filters/)[Next Relyt](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RelytDemo/)
