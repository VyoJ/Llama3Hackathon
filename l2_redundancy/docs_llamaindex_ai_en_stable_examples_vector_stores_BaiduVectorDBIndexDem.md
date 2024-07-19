Title: Baidu VectorDB - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/BaiduVectorDBIndexDemo/

Markdown Content:
Baidu VectorDB - LlamaIndex


> [Baidu VectorDB](https://cloud.baidu.com/product/vdb.html) is a robust, enterprise-level distributed database service, meticulously developed and fully managed by Baidu Intelligent Cloud. It stands out for its exceptional ability to store, retrieve, and analyze multi-dimensional vector data. At its core, VectorDB operates on Baidu's proprietary "Mochow" vector database kernel, which ensures high performance, availability, and security, alongside remarkable scalability and user-friendliness.

> This database service supports a diverse range of index types and similarity calculation methods, catering to various use cases. A standout feature of VectorDB is its capacity to manage an immense vector scale of up to 10 billion, while maintaining impressive query performance, supporting millions of queries per second (QPS) with millisecond-level query latency.

**This notebook shows the basic usage of BaiduVectorDB as a Vector Store in LlamaIndex.**

To run, you should have a [Database instance.](https://cloud.baidu.com/doc/VDB/s/hlrsoazuf)

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BaiduVectorDBIndexDemo/#setup)
---------------------------------------------------------------------------------------------------

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-baiduvectordb

%pip install llama-index-vector-stores-baiduvectordb

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

!pip install pymochow

!pip install pymochow

In \[ \]:

Copied!

from llama\_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
)
from llama\_index.vector\_stores.baiduvectordb import (
    BaiduVectorDB,
    TableParams,
    TableField,
)
import pymochow

from llama\_index.core import ( VectorStoreIndex, SimpleDirectoryReader, StorageContext, ) from llama\_index.vector\_stores.baiduvectordb import ( BaiduVectorDB, TableParams, TableField, ) import pymochow

### Please provide OpenAI access key[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BaiduVectorDBIndexDemo/#please-provide-openai-access-key)

In order use embeddings by OpenAI you need to supply an OpenAI API Key:

In \[ \]:

Copied!

import openai

OPENAI\_API\_KEY \= getpass.getpass("OpenAI API Key:")
openai.api\_key \= OPENAI\_API\_KEY

import openai OPENAI\_API\_KEY = getpass.getpass("OpenAI API Key:") openai.api\_key = OPENAI\_API\_KEY

Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BaiduVectorDBIndexDemo/#download-data)
-------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

Creating and populating the Vector Store[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BaiduVectorDBIndexDemo/#creating-and-populating-the-vector-store)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You will now load some essays by Paul Graham from a local file and store them into the Baidu VectorDB.

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham").load\_data()
print(f"Total documents: {len(documents)}")
print(f"First document, id: {documents\[0\].doc\_id}")
print(f"First document, hash: {documents\[0\].hash}")
print(
    f"First document, text ({len(documents\[0\].text)} characters):\\n{'='\*20}\\n{documents\[0\].text\[:360\]} ..."
)

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham").load\_data() print(f"Total documents: {len(documents)}") print(f"First document, id: {documents\[0\].doc\_id}") print(f"First document, hash: {documents\[0\].hash}") print( f"First document, text ({len(documents\[0\].text)} characters):\\n{'='\*20}\\n{documents\[0\].text\[:360\]} ..." )

### Initialize the Baidu VectorDB[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BaiduVectorDBIndexDemo/#initialize-the-baidu-vectordb)

Creation of the vector store entails creation of the underlying database collection if it does not exist yet:

In \[ \]:

Copied!

vector\_store \= BaiduVectorDB(
    endpoint\="http://192.168.X.X",
    api\_key\="\*\*\*\*\*\*\*",
    table\_params\=TableParams(dimension\=1536, drop\_exists\=True),
)

vector\_store = BaiduVectorDB( endpoint="http://192.168.X.X", api\_key="\*\*\*\*\*\*\*", table\_params=TableParams(dimension=1536, drop\_exists=True), )

Now wrap this store into an `index` LlamaIndex abstraction for later querying:

In \[ \]:

Copied!

storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

Note that the above `from_documents` call does several things at once: it splits the input documents into chunks of manageable size ("nodes"), computes embedding vectors for each node, and stores them all in the Baidu VectorDB.

Querying the store[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BaiduVectorDBIndexDemo/#querying-the-store)
-----------------------------------------------------------------------------------------------------------------------------

### Basic querying[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BaiduVectorDBIndexDemo/#basic-querying)

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("Why did the author choose to work on AI?")
print(response)

query\_engine = index.as\_query\_engine() response = query\_engine.query("Why did the author choose to work on AI?") print(response)

### MMR-based queries[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BaiduVectorDBIndexDemo/#mmr-based-queries)

The MMR (maximal marginal relevance) method is designed to fetch text chunks from the store that are at the same time relevant to the query but as different as possible from each other, with the goal of providing a broader context to the building of the final answer:

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(vector\_store\_query\_mode\="mmr")
response \= query\_engine.query("Why did the author choose to work on AI?")
print(response)

query\_engine = index.as\_query\_engine(vector\_store\_query\_mode="mmr") response = query\_engine.query("Why did the author choose to work on AI?") print(response)

Connecting to an existing store[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BaiduVectorDBIndexDemo/#connecting-to-an-existing-store)
-------------------------------------------------------------------------------------------------------------------------------------------------------

Since this store is backed by Baidu VectorDB, it is persistent by definition. So, if you want to connect to a store that was created and populated previously, here is how:

In \[ \]:

Copied!

vector\_store \= BaiduVectorDB(
    endpoint\="http://192.168.X.X",
    api\_key\="\*\*\*\*\*\*\*",
    table\_params\=TableParams(dimension\=1536, drop\_exists\=False),
)

\# Create index (from preexisting stored vectors)
new\_index\_instance \= VectorStoreIndex.from\_vector\_store(
    vector\_store\=new\_vector\_store
)

\# now you can do querying, etc:
query\_engine \= index.as\_query\_engine(similarity\_top\_k\=5)
response \= query\_engine.query(
    "What did the author study prior to working on AI?"
)
print(response)

vector\_store = BaiduVectorDB( endpoint="http://192.168.X.X", api\_key="\*\*\*\*\*\*\*", table\_params=TableParams(dimension=1536, drop\_exists=False), ) # Create index (from preexisting stored vectors) new\_index\_instance = VectorStoreIndex.from\_vector\_store( vector\_store=new\_vector\_store ) # now you can do querying, etc: query\_engine = index.as\_query\_engine(similarity\_top\_k=5) response = query\_engine.query( "What did the author study prior to working on AI?" ) print(response)

Metadata filtering[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BaiduVectorDBIndexDemo/#metadata-filtering)
-----------------------------------------------------------------------------------------------------------------------------

The Baidu VectorDB vector store support metadata filtering in the form of exact-match `key=value` pairs at query time. The following cells, which work on a brand new collection, demonstrate this feature.

In this demo, for the sake of brevity, a single source document is loaded (the `../data/paul_graham/paul_graham_essay.txt` text file). Nevertheless, you will attach some custom metadata to the document to illustrate how you can can restrict queries with conditions on the metadata attached to the documents.

In \[ \]:

Copied!

filter\_fields \= \[
    TableField(name\="source\_type"),
\]

md\_storage\_context \= StorageContext.from\_defaults(
    vector\_store\=BaiduVectorDB(
        endpoint\="http://192.168.X.X",
        api\_key\="="\*\*\*\*\*\*\*",",
        table\_params\=TableParams(
            dimension\=1536, drop\_exists\=True, filter\_fields\=filter\_fields
        ),
    )
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

filter\_fields = \[ TableField(name="source\_type"), \] md\_storage\_context = StorageContext.from\_defaults( vector\_store=BaiduVectorDB( endpoint="http://192.168.X.X", api\_key="="\*\*\*\*\*\*\*",", table\_params=TableParams( dimension=1536, drop\_exists=True, filter\_fields=filter\_fields ), ) ) def my\_file\_metadata(file\_name: str): """Depending on the input file name, associate a different metadata.""" if "essay" in file\_name: source\_type = "essay" elif "dinosaur" in file\_name: # this (unfortunately) will not happen in this demo source\_type = "dinos" else: source\_type = "other" return {"source\_type": source\_type} # Load documents and build index md\_documents = SimpleDirectoryReader( "../data/paul\_graham", file\_metadata=my\_file\_metadata ).load\_data() md\_index = VectorStoreIndex.from\_documents( md\_documents, storage\_context=md\_storage\_context )

In \[ \]:

Copied!

from llama\_index.core.vector\_stores import MetadataFilter, MetadataFilters

from llama\_index.core.vector\_stores import MetadataFilter, MetadataFilters

In \[ \]:

Copied!

md\_query\_engine \= md\_index.as\_query\_engine(
    filters\=MetadataFilters(
        filters\=\[MetadataFilter(key\="source\_type", value\="essay")\]
    )
)
md\_response \= md\_query\_engine.query(
    "How long it took the author to write his thesis?"
)
print(md\_response.response)

md\_query\_engine = md\_index.as\_query\_engine( filters=MetadataFilters( filters=\[MetadataFilter(key="source\_type", value="essay")\] ) ) md\_response = md\_query\_engine.query( "How long it took the author to write his thesis?" ) print(md\_response.response)

Back to top

[Previous Bagel Network](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BagelIndexDemo/)[Next Cassandra Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/CassandraIndexDemo/)
