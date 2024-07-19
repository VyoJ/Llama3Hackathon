Title: Google Vertex AI Vector Search

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/VertexAIVectorSearchDemo/

Markdown Content:
Google Vertex AI Vector Search - LlamaIndex


This notebook shows how to use functionality related to the `Google Cloud Vertex AI Vector Search` vector database.

> [Google Vertex AI Vector Search](https://cloud.google.com/vertex-ai/docs/vector-search/overview), formerly known as Vertex AI Matching Engine, provides the industry's leading high-scale low latency vector database. These vector databases are commonly referred to as vector similarity-matching or an approximate nearest neighbor (ANN) service.

**Note**: LlamaIndex expects Vertex AI Vector Search endpoint and deployed index is already created. An empty index creation time take upto a minute and deploying an index to the endpoint can take upto 30 min.

> To see how to create an index refer to the section [Create Index and deploy it to an Endpoint](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VertexAIVectorSearchDemo/#create-index-and-deploy-it-to-an-endpoint)  
> If you already have an index deployed , skip to [Create VectorStore from texts](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VertexAIVectorSearchDemo/#create-vector-store-from-texts)

Installation[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VertexAIVectorSearchDemo/#installation)
-------------------------------------------------------------------------------------------------------------------

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

! pip install llama\-index llama\-index\-vector\-stores\-vertexaivectorsearch llama\-index\-llms\-vertex

! pip install llama-index llama-index-vector-stores-vertexaivectorsearch llama-index-llms-vertex

Create Index and deploy it to an Endpoint[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VertexAIVectorSearchDemo/#create-index-and-deploy-it-to-an-endpoint)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   This section demonstrates creating a new index and deploying it to an endpoint.

In \[ \]:

Copied!

\# TODO : Set values as per your requirements

\# Project and Storage Constants
PROJECT\_ID \= "\[your\_project\_id\]"
REGION \= "\[your\_region\]"
GCS\_BUCKET\_NAME \= "\[your\_gcs\_bucket\]"
GCS\_BUCKET\_URI \= f"gs://{GCS\_BUCKET\_NAME}"

\# The number of dimensions for the textembedding-gecko@003 is 768
\# If other embedder is used, the dimensions would probably need to change.
VS\_DIMENSIONS \= 768

\# Vertex AI Vector Search Index configuration
\# parameter description here
\# https://cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.MatchingEngineIndex#google\_cloud\_aiplatform\_MatchingEngineIndex\_create\_tree\_ah\_index
VS\_INDEX\_NAME \= "llamaindex-doc-index"  \# @param {type:"string"}
VS\_INDEX\_ENDPOINT\_NAME \= "llamaindex-doc-endpoint"  \# @param {type:"string"}

\# TODO : Set values as per your requirements # Project and Storage Constants PROJECT\_ID = "\[your\_project\_id\]" REGION = "\[your\_region\]" GCS\_BUCKET\_NAME = "\[your\_gcs\_bucket\]" GCS\_BUCKET\_URI = f"gs://{GCS\_BUCKET\_NAME}" # The number of dimensions for the textembedding-gecko@003 is 768 # If other embedder is used, the dimensions would probably need to change. VS\_DIMENSIONS = 768 # Vertex AI Vector Search Index configuration # parameter description here # https://cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.MatchingEngineIndex#google\_cloud\_aiplatform\_MatchingEngineIndex\_create\_tree\_ah\_index VS\_INDEX\_NAME = "llamaindex-doc-index" # @param {type:"string"} VS\_INDEX\_ENDPOINT\_NAME = "llamaindex-doc-endpoint" # @param {type:"string"}

In \[ \]:

Copied!

from google.cloud import aiplatform

aiplatform.init(project\=PROJECT\_ID, location\=REGION)

from google.cloud import aiplatform aiplatform.init(project=PROJECT\_ID, location=REGION)

### Create Cloud Storage bucket[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VertexAIVectorSearchDemo/#create-cloud-storage-bucket)

In \[ \]:

Copied!

\# Create a bucket.
! gsutil mb \-l $REGION \-p $PROJECT\_ID $GCS\_BUCKET\_URI

\# Create a bucket. ! gsutil mb -l $REGION -p $PROJECT\_ID $GCS\_BUCKET\_URI

### Create an empty Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VertexAIVectorSearchDemo/#create-an-empty-index)

**Note :** While creating an index you should specify an "index\_update\_method" - `BATCH_UPDATE` or `STREAM_UPDATE`

> A batch index is for when you want to update your index in a batch, with data which has been stored over a set amount of time, like systems which are processed weekly or monthly.
> 
> A streaming index is when you want index data to be updated as new data is added to your datastore, for instance, if you have a bookstore and want to show new inventory online as soon as possible.
> 
> Which type you choose is important, since setup and requirements are different.

Refer [Official Documentation](https://cloud.google.com/vertex-ai/docs/vector-search/create-manage-index) and [API reference](https://cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.MatchingEngineIndex#google_cloud_aiplatform_MatchingEngineIndex_create_tree_ah_index) for more details on configuring indexes

In \[ \]:

Copied!

\# NOTE : This operation can take upto 30 seconds

\# check if index exists
index\_names \= \[
    index.resource\_name
    for index in aiplatform.MatchingEngineIndex.list(
        filter\=f"display\_name={VS\_INDEX\_NAME}"
    )
\]

if len(index\_names) \ 0: print(f"Creating Vector Search index {VS\_INDEX\_NAME} ...") vs\_index = aiplatform.MatchingEngineIndex.create\_tree\_ah\_index( display\_name=VS\_INDEX\_NAME, dimensions=VS\_DIMENSIONS, distance\_measure\_type="DOT\_PRODUCT\_DISTANCE", shard\_size="SHARD\_SIZE\_SMALL", index\_update\_method="STREAM\_UPDATE", # allowed values BATCH\_UPDATE , STREAM\_UPDATE ) print( f"Vector Search index {vs\_index.display\_name} created with resource name {vs\_index.resource\_name}" ) else: vs\_index = aiplatform.MatchingEngineIndex(index\_name=index\_names\[0\]) print( f"Vector Search index {vs\_index.display\_name} exists with resource name {vs\_index.resource\_name}" )

### Create an Endpoint[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VertexAIVectorSearchDemo/#create-an-endpoint)

To use the index, you need to create an index endpoint. It works as a server instance accepting query requests for your index. An endpoint can be a [public endpoint](https://cloud.google.com/vertex-ai/docs/vector-search/deploy-index-public) or a [private endpoint](https://cloud.google.com/vertex-ai/docs/vector-search/deploy-index-vpc).

Let's create a public endpoint.

In \[ \]:

Copied!

endpoint\_names \= \[
    endpoint.resource\_name
    for endpoint in aiplatform.MatchingEngineIndexEndpoint.list(
        filter\=f"display\_name={VS\_INDEX\_ENDPOINT\_NAME}"
    )
\]

if len(endpoint\_names) \ 0: print( f"Creating Vector Search index endpoint {VS\_INDEX\_ENDPOINT\_NAME} ..." ) vs\_endpoint = aiplatform.MatchingEngineIndexEndpoint.create( display\_name=VS\_INDEX\_ENDPOINT\_NAME, public\_endpoint\_enabled=True ) print( f"Vector Search index endpoint {vs\_endpoint.display\_name} created with resource name {vs\_endpoint.resource\_name}" ) else: vs\_endpoint = aiplatform.MatchingEngineIndexEndpoint( index\_endpoint\_name=endpoint\_names\[0\] ) print( f"Vector Search index endpoint {vs\_endpoint.display\_name} exists with resource name {vs\_endpoint.resource\_name}" )

### Deploy Index to the Endpoint[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VertexAIVectorSearchDemo/#deploy-index-to-the-endpoint)

With the index endpoint, deploy the index by specifying a unique deployed index ID.

**NOTE : This operation can take upto 30 minutes.**

In \[ \]:

Copied!

\# check if endpoint exists
index\_endpoints \= \[
    (deployed\_index.index\_endpoint, deployed\_index.deployed\_index\_id)
    for deployed\_index in vs\_index.deployed\_indexes
\]

if len(index\_endpoints) \ 0: print( f"Deploying Vector Search index {vs\_index.display\_name} at endpoint {vs\_endpoint.display\_name} ..." ) vs\_deployed\_index = vs\_endpoint.deploy\_index( index=vs\_index, deployed\_index\_id=VS\_INDEX\_NAME, display\_name=VS\_INDEX\_NAME, machine\_type="e2-standard-16", min\_replica\_count=1, max\_replica\_count=1, ) print( f"Vector Search index {vs\_index.display\_name} is deployed at endpoint {vs\_deployed\_index.display\_name}" ) else: vs\_deployed\_index = aiplatform.MatchingEngineIndexEndpoint( index\_endpoint\_name=index\_endpoints\[0\]\[0\] ) print( f"Vector Search index {vs\_index.display\_name} is already deployed at endpoint {vs\_deployed\_index.display\_name}" )

Create Vector Store from texts[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VertexAIVectorSearchDemo/#create-vector-store-from-texts)
-------------------------------------------------------------------------------------------------------------------------------------------------------

NOTE : If you have existing Vertex AI Vector Search Index and Endpoints, you can assign them using following code:

In \[ \]:

Copied!

\# TODO : replace 1234567890123456789 with your actual index ID
vs\_index \= aiplatform.MatchingEngineIndex(index\_name\="1234567890123456789")

\# TODO : replace 1234567890123456789 with your actual endpoint ID
vs\_endpoint \= aiplatform.MatchingEngineIndexEndpoint(
    index\_endpoint\_name\="1234567890123456789"
)

\# TODO : replace 1234567890123456789 with your actual index ID vs\_index = aiplatform.MatchingEngineIndex(index\_name="1234567890123456789") # TODO : replace 1234567890123456789 with your actual endpoint ID vs\_endpoint = aiplatform.MatchingEngineIndexEndpoint( index\_endpoint\_name="1234567890123456789" )

In \[ \]:

Copied!

\# import modules needed
from llama\_index.core import (
    StorageContext,
    Settings,
    VectorStoreIndex,
    SimpleDirectoryReader,
)
from llama\_index.core.schema import TextNode
from llama\_index.core.vector\_stores.types import (
    MetadataFilters,
    MetadataFilter,
    FilterOperator,
)
from llama\_index.llms.vertex import Vertex
from llama\_index.embeddings.vertex import VertexTextEmbedding
from llama\_index.vector\_stores.vertexaivectorsearch import VertexAIVectorStore

\# import modules needed from llama\_index.core import ( StorageContext, Settings, VectorStoreIndex, SimpleDirectoryReader, ) from llama\_index.core.schema import TextNode from llama\_index.core.vector\_stores.types import ( MetadataFilters, MetadataFilter, FilterOperator, ) from llama\_index.llms.vertex import Vertex from llama\_index.embeddings.vertex import VertexTextEmbedding from llama\_index.vector\_stores.vertexaivectorsearch import VertexAIVectorStore

### Create a simple vector store from plain text without metadata filters[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VertexAIVectorSearchDemo/#create-a-simple-vector-store-from-plain-text-without-metadata-filters)

In \[ \]:

Copied!

\# setup storage
vector\_store \= VertexAIVectorStore(
    project\_id\=PROJECT\_ID,
    region\=REGION,
    index\_id\=vs\_index.resource\_name,
    endpoint\_id\=vs\_endpoint.resource\_name,
    gcs\_bucket\_name\=GCS\_BUCKET\_NAME,
)

\# set storage context
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

\# setup storage vector\_store = VertexAIVectorStore( project\_id=PROJECT\_ID, region=REGION, index\_id=vs\_index.resource\_name, endpoint\_id=vs\_endpoint.resource\_name, gcs\_bucket\_name=GCS\_BUCKET\_NAME, ) # set storage context storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store)

### Use [Vertex AI Embeddings](https://github.com/run-llama/llama_index/tree/main/llama-index-integrations/embeddings/llama-index-embeddings-vertex) as the embeddings model[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VertexAIVectorSearchDemo/#use-vertex-ai-embeddings-as-the-embeddings-model)

In \[ \]:

Copied!

\# configure embedding model
embed\_model \= VertexTextEmbedding(
    model\_name\="textembedding-gecko@003",
    project\=PROJECT\_ID,
    location\=REGION,
)

\# setup the index/query process, ie the embedding model (and completion if used)
Settings.embed\_model \= embed\_model

\# configure embedding model embed\_model = VertexTextEmbedding( model\_name="textembedding-gecko@003", project=PROJECT\_ID, location=REGION, ) # setup the index/query process, ie the embedding model (and completion if used) Settings.embed\_model = embed\_model

### Add vectors and mapped text chunks to your vectore store[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VertexAIVectorSearchDemo/#add-vectors-and-mapped-text-chunks-to-your-vectore-store)

In \[ \]:

Copied!

\# Input texts
texts \= \[
    "The cat sat on",
    "the mat.",
    "I like to",
    "eat pizza for",
    "dinner.",
    "The sun sets",
    "in the west.",
\]
nodes \= \[
    TextNode(text\=text, embedding\=embed\_model.get\_text\_embedding(text))
    for text in texts
\]

vector\_store.add(nodes)

\# Input texts texts = \[ "The cat sat on", "the mat.", "I like to", "eat pizza for", "dinner.", "The sun sets", "in the west.", \] nodes = \[ TextNode(text=text, embedding=embed\_model.get\_text\_embedding(text)) for text in texts \] vector\_store.add(nodes)

### Running a similarity search[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VertexAIVectorSearchDemo/#running-a-similarity-search)

In \[ \]:

Copied!

\# define index from vector store
index \= VectorStoreIndex.from\_vector\_store(
    vector\_store\=vector\_store, embed\_model\=embed\_model
)
retriever \= index.as\_retriever()

\# define index from vector store index = VectorStoreIndex.from\_vector\_store( vector\_store=vector\_store, embed\_model=embed\_model ) retriever = index.as\_retriever()

In \[ \]:

Copied!

response \= retriever.retrieve("pizza")
for row in response:
    print(f"Score: {row.get\_score():.3f} Text: {row.get\_text()}")

response = retriever.retrieve("pizza") for row in response: print(f"Score: {row.get\_score():.3f} Text: {row.get\_text()}")

Score: 0.703 Text: eat pizza for
Score: 0.626 Text: dinner.

Add documents with metadata attributes and use filters[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VertexAIVectorSearchDemo/#add-documents-with-metadata-attributes-and-use-filters)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

\# Input text with metadata
records \= \[
    {
        "description": "A versatile pair of dark-wash denim jeans."
        "Made from durable cotton with a classic straight-leg cut, these jeans"
        " transition easily from casual days to dressier occasions.",
        "price": 65.00,
        "color": "blue",
        "season": \["fall", "winter", "spring"\],
    },
    {
        "description": "A lightweight linen button-down shirt in a crisp white."
        " Perfect for keeping cool with breathable fabric and a relaxed fit.",
        "price": 34.99,
        "color": "white",
        "season": \["summer", "spring"\],
    },
    {
        "description": "A soft, chunky knit sweater in a vibrant forest green. "
        "The oversized fit and cozy wool blend make this ideal for staying warm "
        "when the temperature drops.",
        "price": 89.99,
        "color": "green",
        "season": \["fall", "winter"\],
    },
    {
        "description": "A classic crewneck t-shirt in a soft, heathered blue. "
        "Made from comfortable cotton jersey, this t-shirt is a wardrobe essential "
        "that works for every season.",
        "price": 19.99,
        "color": "blue",
        "season": \["fall", "winter", "summer", "spring"\],
    },
    {
        "description": "A flowing midi-skirt in a delicate floral print. "
        "Lightweight and airy, this skirt adds a touch of feminine style "
        "to warmer days.",
        "price": 45.00,
        "color": "white",
        "season": \["spring", "summer"\],
    },
\]

nodes \= \[\]
for record in records:
    text \= record.pop("description")
    embedding \= embed\_model.get\_text\_embedding(text)
    metadata \= {\*\*record}
    nodes.append(TextNode(text\=text, embedding\=embedding, metadata\=metadata))

vector\_store.add(nodes)

\# Input text with metadata records = \[ { "description": "A versatile pair of dark-wash denim jeans." "Made from durable cotton with a classic straight-leg cut, these jeans" " transition easily from casual days to dressier occasions.", "price": 65.00, "color": "blue", "season": \["fall", "winter", "spring"\], }, { "description": "A lightweight linen button-down shirt in a crisp white." " Perfect for keeping cool with breathable fabric and a relaxed fit.", "price": 34.99, "color": "white", "season": \["summer", "spring"\], }, { "description": "A soft, chunky knit sweater in a vibrant forest green. " "The oversized fit and cozy wool blend make this ideal for staying warm " "when the temperature drops.", "price": 89.99, "color": "green", "season": \["fall", "winter"\], }, { "description": "A classic crewneck t-shirt in a soft, heathered blue. " "Made from comfortable cotton jersey, this t-shirt is a wardrobe essential " "that works for every season.", "price": 19.99, "color": "blue", "season": \["fall", "winter", "summer", "spring"\], }, { "description": "A flowing midi-skirt in a delicate floral print. " "Lightweight and airy, this skirt adds a touch of feminine style " "to warmer days.", "price": 45.00, "color": "white", "season": \["spring", "summer"\], }, \] nodes = \[\] for record in records: text = record.pop("description") embedding = embed\_model.get\_text\_embedding(text) metadata = {\*\*record} nodes.append(TextNode(text=text, embedding=embedding, metadata=metadata)) vector\_store.add(nodes)

### Running a similarity search with filters[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VertexAIVectorSearchDemo/#running-a-similarity-search-with-filters)

In \[ \]:

Copied!

\# define index from vector store
index \= VectorStoreIndex.from\_vector\_store(
    vector\_store\=vector\_store, embed\_model\=embed\_model
)

\# define index from vector store index = VectorStoreIndex.from\_vector\_store( vector\_store=vector\_store, embed\_model=embed\_model )

In \[ \]:

Copied!

\# simple similarity search without filter
retriever \= index.as\_retriever()
response \= retriever.retrieve("pants")

for row in response:
    print(f"Text: {row.get\_text()}")
    print(f"   Score: {row.get\_score():.3f}")
    print(f"   Metadata: {row.metadata}")

\# simple similarity search without filter retriever = index.as\_retriever() response = retriever.retrieve("pants") for row in response: print(f"Text: {row.get\_text()}") print(f" Score: {row.get\_score():.3f}") print(f" Metadata: {row.metadata}")

Text: A pair of well-tailored dress pants in a neutral grey. Made from a wrinkle-resistant blend, these pants look sharp and professional for workwear or formal occasions.
   Score: 0.669
   Metadata: {'price': 69.99, 'color': 'grey', 'season': \['fall', 'winter', 'summer', 'spring'\]}
Text: A pair of tailored black trousers in a comfortable stretch fabric. Perfect for work or dressier events, these trousers provide a sleek, polished look.
   Score: 0.642
   Metadata: {'price': 59.99, 'color': 'black', 'season': \['fall', 'winter', 'spring'\]}

In \[ \]:

Copied!

\# similarity search with text filter
filters \= MetadataFilters(filters\=\[MetadataFilter(key\="color", value\="blue")\])
retriever \= index.as\_retriever(filters\=filters, similarity\_top\_k\=3)
response \= retriever.retrieve("denims")

for row in response:
    print(f"Text: {row.get\_text()}")
    print(f"   Score: {row.get\_score():.3f}")
    print(f"   Metadata: {row.metadata}")

\# similarity search with text filter filters = MetadataFilters(filters=\[MetadataFilter(key="color", value="blue")\]) retriever = index.as\_retriever(filters=filters, similarity\_top\_k=3) response = retriever.retrieve("denims") for row in response: print(f"Text: {row.get\_text()}") print(f" Score: {row.get\_score():.3f}") print(f" Metadata: {row.metadata}")

Text: A versatile pair of dark-wash denim jeans.Made from durable cotton with a classic straight-leg cut, these jeans transition easily from casual days to dressier occasions.
   Score: 0.704
   Metadata: {'price': 65.0, 'color': 'blue', 'season': \['fall', 'winter', 'spring'\]}
Text: A denim jacket with a faded wash and distressed details. This wardrobe staple adds a touch of effortless cool to any outfit.
   Score: 0.667
   Metadata: {'price': 79.99, 'color': 'blue', 'season': \['fall', 'spring', 'summer'\]}

In \[ \]:

Copied!

\# similarity search with text and numeric filter
filters \= MetadataFilters(
    filters\=\[
        MetadataFilter(key\="color", value\="blue"),
        MetadataFilter(key\="price", operator\=FilterOperator.GT, value\=70.0),
    \]
)
retriever \= index.as\_retriever(filters\=filters, similarity\_top\_k\=3)
response \= retriever.retrieve("denims")

for row in response:
    print(f"Text: {row.get\_text()}")
    print(f"   Score: {row.get\_score():.3f}")
    print(f"   Metadata: {row.metadata}")

\# similarity search with text and numeric filter filters = MetadataFilters( filters=\[ MetadataFilter(key="color", value="blue"), MetadataFilter(key="price", operator=FilterOperator.GT, value=70.0), \] ) retriever = index.as\_retriever(filters=filters, similarity\_top\_k=3) response = retriever.retrieve("denims") for row in response: print(f"Text: {row.get\_text()}") print(f" Score: {row.get\_score():.3f}") print(f" Metadata: {row.metadata}")

Text: A denim jacket with a faded wash and distressed details. This wardrobe staple adds a touch of effortless cool to any outfit.
   Score: 0.667
   Metadata: {'price': 79.99, 'color': 'blue', 'season': \['fall', 'spring', 'summer'\]}

Parse, Index and Query PDFs using Vertex AI Vector Search and Gemini Pro[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VertexAIVectorSearchDemo/#parse-index-and-query-pdfs-using-vertex-ai-vector-search-and-gemini-pro)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

! mkdir \-p ./data/arxiv/
! wget 'https://arxiv.org/pdf/1706.03762.pdf' \-O ./data/arxiv/test.pdf

! mkdir -p ./data/arxiv/ ! wget 'https://arxiv.org/pdf/1706.03762.pdf' -O ./data/arxiv/test.pdf

E0501 00:56:50.842446801  266241 backup\_poller.cc:127\]                 Run client channel backup poller: UNKNOWN:pollset\_work {created\_time:"2024-05-01T00:56:50.841935606+00:00", children:\[UNKNOWN:Bad file descriptor {created\_time:"2024-05-01T00:56:50.841810434+00:00", errno:9, os\_error:"Bad file descriptor", syscall:"epoll\_wait"}\]}
--2024-05-01 00:56:52--  https://arxiv.org/pdf/1706.03762.pdf
Resolving arxiv.org (arxiv.org)... 151.101.67.42, 151.101.195.42, 151.101.131.42, ...
Connecting to arxiv.org (arxiv.org)|151.101.67.42|:443... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: http://arxiv.org/pdf/1706.03762 \[following\]
--2024-05-01 00:56:52--  http://arxiv.org/pdf/1706.03762
Connecting to arxiv.org (arxiv.org)|151.101.67.42|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2215244 (2.1M) \[application/pdf\]
Saving to: ‘./data/arxiv/test.pdf’

./data/arxiv/test.p 100%\[>\]   2.11M  --.-KB/s    in 0.07s   

2024-05-01 00:56:52 (31.5 MB/s) - ‘./data/arxiv/test.pdf’ saved \[2215244/2215244\]

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/arxiv/").load\_data()
print(f"# of documents = {len(documents)}")

\# load documents documents = SimpleDirectoryReader("./data/arxiv/").load\_data() print(f"# of documents = {len(documents)}")

\# of documents = 15

In \[ \]:

Copied!

\# setup storage
vector\_store \= VertexAIVectorStore(
    project\_id\=PROJECT\_ID,
    region\=REGION,
    index\_id\=vs\_index.resource\_name,
    endpoint\_id\=vs\_endpoint.resource\_name,
    gcs\_bucket\_name\=GCS\_BUCKET\_NAME,
)

\# set storage context
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

\# configure embedding model
embed\_model \= VertexTextEmbedding(
    model\_name\="textembedding-gecko@003",
    project\=PROJECT\_ID,
    location\=REGION,
)

vertex\_gemini \= Vertex(model\="gemini-pro", temperature\=0, additional\_kwargs\={})

\# setup the index/query process, ie the embedding model (and completion if used)
Settings.llm \= vertex\_gemini
Settings.embed\_model \= embed\_model

\# setup storage vector\_store = VertexAIVectorStore( project\_id=PROJECT\_ID, region=REGION, index\_id=vs\_index.resource\_name, endpoint\_id=vs\_endpoint.resource\_name, gcs\_bucket\_name=GCS\_BUCKET\_NAME, ) # set storage context storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) # configure embedding model embed\_model = VertexTextEmbedding( model\_name="textembedding-gecko@003", project=PROJECT\_ID, location=REGION, ) vertex\_gemini = Vertex(model="gemini-pro", temperature=0, additional\_kwargs={}) # setup the index/query process, ie the embedding model (and completion if used) Settings.llm = vertex\_gemini Settings.embed\_model = embed\_model

In \[ \]:

Copied!

\# define index from vector store
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

\# define index from vector store index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()

query\_engine = index.as\_query\_engine()

In \[ \]:

Copied!

response \= query\_engine.query(
    "who are the authors of paper Attention is All you need?"
)

print(f"Response:")
print("-" \* 80)
print(response.response)
print("-" \* 80)
print(f"Source Documents:")
print("-" \* 80)
for source in response.source\_nodes:
    print(f"Sample Text: {source.text\[:50\]}")
    print(f"Relevance score: {source.get\_score():.3f}")
    print(f"File Name: {source.metadata.get('file\_name')}")
    print(f"Page #: {source.metadata.get('page\_label')}")
    print(f"File Path: {source.metadata.get('file\_path')}")
    print("-" \* 80)

response = query\_engine.query( "who are the authors of paper Attention is All you need?" ) print(f"Response:") print("-" \* 80) print(response.response) print("-" \* 80) print(f"Source Documents:") print("-" \* 80) for source in response.source\_nodes: print(f"Sample Text: {source.text\[:50\]}") print(f"Relevance score: {source.get\_score():.3f}") print(f"File Name: {source.metadata.get('file\_name')}") print(f"Page #: {source.metadata.get('page\_label')}") print(f"File Path: {source.metadata.get('file\_path')}") print("-" \* 80)

Response:
--------------------------------------------------------------------------------
The authors of the paper "Attention Is All You Need" are:

\* Ashish Vaswani
\* Noam Shazeer
\* Niki Parmar
\* Jakob Uszkoreit
\* Llion Jones
\* Aidan N. Gomez
\* Łukasz Kaiser
\* Illia Polosukhin
--------------------------------------------------------------------------------
Source Documents:
--------------------------------------------------------------------------------
Sample Text: Provided proper attribution is provided, Google he
Relevance score: 0.720
File Name: test.pdf
Page #: 1
File Path: /home/jupyter/llama\_index/docs/docs/examples/vector\_stores/data/arxiv/test.pdf
--------------------------------------------------------------------------------
Sample Text: length nis smaller than the representation dimensi
Relevance score: 0.678
File Name: test.pdf
Page #: 7
File Path: /home/jupyter/llama\_index/docs/docs/examples/vector\_stores/data/arxiv/test.pdf
--------------------------------------------------------------------------------

* * *

Clean Up[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VertexAIVectorSearchDemo/#clean-up)
-----------------------------------------------------------------------------------------------------------

Please delete Vertex AI Vector Search Index and Index Endpoint after running your experiments to avoid incurring additional charges. Please note that you will be charged as long as the endpoint is running.

**⚠️ NOTE: Enabling \`CLEANUP\_RESOURCES\` flag deletes Vector Search Index, Index Endpoint and Cloud Storage bucket. Please run it with caution.**

In \[ \]:

Copied!

CLEANUP\_RESOURCES \= False

CLEANUP\_RESOURCES = False

*   Undeploy indexes and Delete index endpoint

In \[ \]:

Copied!

if CLEANUP\_RESOURCES:
    print(
        f"Undeploying all indexes and deleting the index endpoint {vs\_endpoint.display\_name}"
    )
    vs\_endpoint.undeploy\_all()
    vs\_endpoint.delete()

if CLEANUP\_RESOURCES: print( f"Undeploying all indexes and deleting the index endpoint {vs\_endpoint.display\_name}" ) vs\_endpoint.undeploy\_all() vs\_endpoint.delete()

*   Delete index

In \[ \]:

Copied!

if CLEANUP\_RESOURCES:
    print(f"Deleting the index {vs\_index.display\_name}")
    vs\_index.delete()

if CLEANUP\_RESOURCES: print(f"Deleting the index {vs\_index.display\_name}") vs\_index.delete()

*   Delete contents from the Cloud Storage bucket

In \[ \]:

Copied!

if CLEANUP\_RESOURCES and "GCS\_BUCKET\_NAME" in globals():
    print(f"Deleting contents from the Cloud Storage bucket {GCS\_BUCKET\_NAME}")

    shell\_output \= ! gsutil du \-ash gs://$GCS\_BUCKET\_NAME
    print(shell\_output)
    print(
        f"Size of the bucket {GCS\_BUCKET\_NAME} before deleting = {' '.join(shell\_output\[0\].split()\[:2\])}"
    )

    \# uncomment below line to delete contents of the bucket
    \# ! gsutil -m rm -r gs://$GCS\_BUCKET\_NAME

if CLEANUP\_RESOURCES and "GCS\_BUCKET\_NAME" in globals(): print(f"Deleting contents from the Cloud Storage bucket {GCS\_BUCKET\_NAME}") shell\_output = ! gsutil du -ash gs://$GCS\_BUCKET\_NAME print(shell\_output) print( f"Size of the bucket {GCS\_BUCKET\_NAME} before deleting = {' '.join(shell\_output\[0\].split()\[:2\])}" ) # uncomment below line to delete contents of the bucket # ! gsutil -m rm -r gs://$GCS\_BUCKET\_NAME

Back to top

[Previous VearchDemo](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VearchDemo/)[Next Vespa Vector Store demo](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VespaIndexDemo/)
