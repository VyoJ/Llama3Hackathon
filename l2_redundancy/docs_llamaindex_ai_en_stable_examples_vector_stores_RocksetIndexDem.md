Title: Rockset Vector Store - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/RocksetIndexDemo/

Markdown Content:
Rockset Vector Store - LlamaIndex


As a real-time search and analytics database, Rockset uses indexing to deliver scalable and performant personalization, product search, semantic search, chatbot applications, and more. Since Rockset is purpose-built for real-time, you can build these responsive applications on constantly updating, streaming data. By integrating Rockset with LlamaIndex, you can easily use LLMs on your own real-time data for production-ready vector search applications.

We'll walk through a demonstration of how to use Rockset as a vector store in LlamaIndex.

Tutorial[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RocksetIndexDemo/#tutorial)
---------------------------------------------------------------------------------------------------

In this example, we'll use OpenAI's `text-embedding-ada-002` model to generate embeddings and Rockset as vector store to store embeddings. We'll ingest text from a file and ask questions about the content.

### Setting Up Your Environment[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RocksetIndexDemo/#setting-up-your-environment)

1.  Create a [collection](https://rockset.com/docs/collections) from the Rockset console with the [Write API](https://rockset.com/docs/write-api/) as your source. Name your collection `llamaindex_demo`. Configure the following [ingest transformation](https://rockset.com/docs/ingest-transformation) with [`VECTOR_ENFORCE`](https://rockset.com/docs/vector-functions) to define your embeddings field and take advantage of performance and storage optimizations:

SELECT 
    \_input.\* EXCEPT(\_meta), 
    VECTOR\_ENFORCE(
        \_input.embedding,
        1536,
        'float'
    ) as embedding
FROM \_input

2.  Create an [API key](https://rockset.com/docs/iam) from the Rockset console and set the `ROCKSET_API_KEY` environment variable. Find your API server [here](http://rockset.com/docs/rest-api#introduction) and set the `ROCKSET_API_SERVER` environment variable. Set the `OPENAI_API_KEY` environment variable.
    
3.  Install the dependencies.
    

pip3 install llama\_index rockset

4.  LlamaIndex allows you to ingest data from a variety of sources. For this example, we'll read from a text file named `constitution.txt`, which is a transcript of the American Constitution, found [here](https://www.archives.gov/founding-docs/constitution-transcript).

### Data ingestion[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RocksetIndexDemo/#data-ingestion)

Use LlamaIndex's `SimpleDirectoryReader` class to convert the text file to a list of `Document` objects.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai
%pip install llama\-index\-vector\-stores\-rocksetdb

%pip install llama-index-llms-openai %pip install llama-index-vector-stores-rocksetdb

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

docs \= SimpleDirectoryReader(
    input\_files\=\["{path to}/consitution.txt"\]
).load\_data()

from llama\_index.core import SimpleDirectoryReader docs = SimpleDirectoryReader( input\_files=\["{path to}/consitution.txt"\] ).load\_data()

Instantiate the LLM and service context.

In \[ \]:

Copied!

from llama\_index.core import Settings
from llama\_index.llms.openai import OpenAI

Settings.llm \= OpenAI(temperature\=0.8, model\="gpt-3.5-turbo")

from llama\_index.core import Settings from llama\_index.llms.openai import OpenAI Settings.llm = OpenAI(temperature=0.8, model="gpt-3.5-turbo")

Instantiate the vector store and storage context.

In \[ \]:

Copied!

from llama\_index.core import StorageContext
from llama\_index.vector\_stores.rocksetdb import RocksetVectorStore

vector\_store \= RocksetVectorStore(collection\="llamaindex\_demo")
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

from llama\_index.core import StorageContext from llama\_index.vector\_stores.rocksetdb import RocksetVectorStore vector\_store = RocksetVectorStore(collection="llamaindex\_demo") storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store)

Add documents to the `llamaindex_demo` collection and create an index.

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex

index \= VectorStoreIndex.from\_documents(
    docs,
    storage\_context\=storage\_context,
)

from llama\_index.core import VectorStoreIndex index = VectorStoreIndex.from\_documents( docs, storage\_context=storage\_context, )

### Querying[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RocksetIndexDemo/#querying)

Ask a question about your document and generate a response.

In \[ \]:

Copied!

response \= index.as\_query\_engine().query("What is the duty of the president?")

print(str(response))

response = index.as\_query\_engine().query("What is the duty of the president?") print(str(response))

Run the program.

$ python3 main.py
The duty of the president is to faithfully execute the Office of President of the United States, preserve, protect and defend the Constitution of the United States, serve as the Commander in Chief of the Army and Navy, grant reprieves and pardons for offenses against the United States (except in cases of impeachment), make treaties and appoint ambassadors and other public ministers, take care that the laws be faithfully executed, and commission all the officers of the United States.

Metadata Filtering[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RocksetIndexDemo/#metadata-filtering)
-----------------------------------------------------------------------------------------------------------------------

Metadata filtering allows you to retrieve relevant documents that match specific filters.

1.  Add nodes to your vector store and create an index.

In \[ \]:

Copied!

from llama\_index.vector\_stores.rocksetdb import RocksetVectorStore
from llama\_index.core import VectorStoreIndex, StorageContext
from llama\_index.core.vector\_stores.types import NodeWithEmbedding
from llama\_index.core.schema import TextNode

nodes \= \[
    NodeWithEmbedding(
        node\=TextNode(
            text\="Apples are blue",
            metadata\={"type": "fruit"},
        ),
        embedding\=\[\],
    )
\]
index \= VectorStoreIndex(
    nodes,
    storage\_context\=StorageContext.from\_defaults(
        vector\_store\=RocksetVectorStore(collection\="llamaindex\_demo")
    ),
)

from llama\_index.vector\_stores.rocksetdb import RocksetVectorStore from llama\_index.core import VectorStoreIndex, StorageContext from llama\_index.core.vector\_stores.types import NodeWithEmbedding from llama\_index.core.schema import TextNode nodes = \[ NodeWithEmbedding( node=TextNode( text="Apples are blue", metadata={"type": "fruit"}, ), embedding=\[\], ) \] index = VectorStoreIndex( nodes, storage\_context=StorageContext.from\_defaults( vector\_store=RocksetVectorStore(collection="llamaindex\_demo") ), )

2.  Define metadata filters.

In \[ \]:

Copied!

from llama\_index.core.vector\_stores import ExactMatchFilter, MetadataFilters

filters \= MetadataFilters(
    filters\=\[ExactMatchFilter(key\="type", value\="fruit")\]
)

from llama\_index.core.vector\_stores import ExactMatchFilter, MetadataFilters filters = MetadataFilters( filters=\[ExactMatchFilter(key="type", value="fruit")\] )

3.  Retrieve relevant documents that satisfy the filters.

In \[ \]:

Copied!

retriever \= index.as\_retriever(filters\=filters)
retriever.retrieve("What colors are apples?")

retriever = index.as\_retriever(filters=filters) retriever.retrieve("What colors are apples?")

Creating an Index from an Existing Collection[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RocksetIndexDemo/#creating-an-index-from-an-existing-collection)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can create indices with data from existing collections.

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex
from llama\_index.vector\_stores.rocksetdb import RocksetVectorStore

vector\_store \= RocksetVectorStore(collection\="llamaindex\_demo")

index \= VectorStoreIndex.from\_vector\_store(vector\_store)

from llama\_index.core import VectorStoreIndex from llama\_index.vector\_stores.rocksetdb import RocksetVectorStore vector\_store = RocksetVectorStore(collection="llamaindex\_demo") index = VectorStoreIndex.from\_vector\_store(vector\_store)

Creating an Index from a New Collection[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RocksetIndexDemo/#creating-an-index-from-a-new-collection)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

You can also create a new Rockset collection to use as a vector store.

In \[ \]:

Copied!

from llama\_index.vector\_stores.rocksetdb import RocksetVectorStore

vector\_store \= RocksetVectorStore.with\_new\_collection(
    collection\="llamaindex\_demo",  \# name of new collection
    dimensions\=1536,  \# specifies length of vectors in ingest tranformation (optional)
    \# other RocksetVectorStore args
)

index \= VectorStoreIndex(
    nodes,
    storage\_context\=StorageContext.from\_defaults(vector\_store\=vector\_store),
)

from llama\_index.vector\_stores.rocksetdb import RocksetVectorStore vector\_store = RocksetVectorStore.with\_new\_collection( collection="llamaindex\_demo", # name of new collection dimensions=1536, # specifies length of vectors in ingest tranformation (optional) # other RocksetVectorStore args ) index = VectorStoreIndex( nodes, storage\_context=StorageContext.from\_defaults(vector\_store=vector\_store), )

Configuration[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RocksetIndexDemo/#configuration)
-------------------------------------------------------------------------------------------------------------

*   **collection**: Name of the collection to query (required).

RocksetVectorStore(collection\="my\_collection")

*   **workspace**: Name of the workspace containing the collection. Defaults to `"commons"`.

RocksetVectorStore(worksapce\="my\_workspace")

*   **api\_key**: The API key to use to authenticate Rockset requests. Ignored if `client` is passed in. Defaults to the `ROCKSET_API_KEY` environment variable.

RocksetVectorStore(api\_key\="<my key>")

*   **api\_server**: The API server to use for Rockset requests. Ignored if `client` is passed in. Defaults to the `ROCKSET_API_KEY` environment variable or `"https://api.use1a1.rockset.com"` if the `ROCKSET_API_SERVER` is not set.

from rockset import Regions
RocksetVectorStore(api\_server\=Regions.euc1a1)

*   **client**: Rockset client object to use to execute Rockset requests. If not specified, a client object is internally constructed with the `api_key` parameter (or `ROCKSET_API_SERVER` environment variable) and the `api_server` parameter (or `ROCKSET_API_SERVER` environment variable).

from rockset import RocksetClient
RocksetVectorStore(client\=RocksetClient(api\_key\="<my key>"))

*   **embedding\_col**: The name of the database field containing embeddings. Defaults to `"embedding"`.

RocksetVectorStore(embedding\_col\="my\_embedding")

*   **metadata\_col**: The name of the database field containing node data. Defaults to `"metadata"`.

RocksetVectorStore(metadata\_col\="node")

*   **distance\_func**: The metric to measure vector relationship. Defaults to cosine similarity.

RocksetVectorStore(distance\_func\=RocksetVectorStore.DistanceFunc.DOT\_PRODUCT)

Back to top

[Previous Relyt](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RelytDemo/)[Next Simple Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemo/)
