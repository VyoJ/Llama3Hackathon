Title: Databricks Vector Search - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/DatabricksVectorSearchDemo/

Markdown Content:
Databricks Vector Search - LlamaIndex


Databricks Vector Search is a vector database that is built into the Databricks Intelligence Platform and integrated with its governance and productivity tools. Full docs here: [https://docs.databricks.com/en/generative-ai/vector-search.html](https://docs.databricks.com/en/generative-ai/vector-search.html)

Install llama-index and databricks-vectorsearch. You must be inside a Databricks runtime to use the Vector Search python client.

In \[ \]:

Copied!

%pip install llama\-index llama\-index\-vector\-stores\-databricks
%pip install databricks\-vectorsearch

%pip install llama-index llama-index-vector-stores-databricks %pip install databricks-vectorsearch

Import databricks dependencies

In \[ \]:

Copied!

from databricks.vector\_search.client import (
    VectorSearchIndex,
    VectorSearchClient,
)

from databricks.vector\_search.client import ( VectorSearchIndex, VectorSearchClient, )

Import LlamaIndex dependencies

In \[ \]:

Copied!

from llama\_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    ServiceContext,
    StorageContext,
)
from llama\_index.vector\_stores.databricks import DatabricksVectorSearch

from llama\_index.core import ( VectorStoreIndex, SimpleDirectoryReader, ServiceContext, StorageContext, ) from llama\_index.vector\_stores.databricks import DatabricksVectorSearch

Load example data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

Read the data

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

Create a Databricks Vector Search endpoint which will serve the index

In \[ \]:

Copied!

\# Create a vector search endpoint
client \= VectorSearchClient()
client.create\_endpoint(
    name\="llamaindex\_dbx\_vector\_store\_test\_endpoint", endpoint\_type\="STANDARD"
)

\# Create a vector search endpoint client = VectorSearchClient() client.create\_endpoint( name="llamaindex\_dbx\_vector\_store\_test\_endpoint", endpoint\_type="STANDARD" )

Create the Databricks Vector Search index, and build it from the documents

In \[ \]:

Copied!

\# Create a vector search index
\# it must be placed inside a Unity Catalog-enabled schema

\# We'll use self-managed embeddings (i.e. managed by LlamaIndex) rather than a Databricks-managed index
databricks\_index \= client.create\_direct\_access\_index(
    endpoint\_name\="llamaindex\_dbx\_vector\_store\_test\_endpoint",
    index\_name\="my\_catalog.my\_schema.my\_test\_table",
    primary\_key\="my\_primary\_key\_name",
    embedding\_dimension\=1536,  \# match the embeddings model dimension you're going to use
    embedding\_vector\_column\="my\_embedding\_vector\_column\_name",  \# you name this anything you want - it'll be picked up by the LlamaIndex class
    schema\={
        "my\_primary\_key\_name": "string",
        "my\_embedding\_vector\_column\_name": "array<double>",
        "text": "string",  \# one column must match the text\_column in the DatabricksVectorSearch instance created below; this will hold the raw node text,
        "doc\_id": "string",  \# one column must contain the reference document ID (this will be populated by LlamaIndex automatically)
        \# add any other metadata you may have in your nodes (Databricks Vector Search supports metadata filtering)
        \# NOTE THAT THESE FIELDS MUST BE ADDED EXPLICITLY TO BE USED FOR METADATA FILTERING
    },
)

databricks\_vector\_store \= DatabricksVectorSearch(
    index\=databricks\_index,
    text\_column\="text",
    columns\=None,  \# YOU MUST ALSO RECORD YOUR METADATA FIELD NAMES HERE
)  \# text\_column is required for self-managed embeddings
storage\_context \= StorageContext.from\_defaults(
    vector\_store\=databricks\_vector\_store
)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

\# Create a vector search index # it must be placed inside a Unity Catalog-enabled schema # We'll use self-managed embeddings (i.e. managed by LlamaIndex) rather than a Databricks-managed index databricks\_index = client.create\_direct\_access\_index( endpoint\_name="llamaindex\_dbx\_vector\_store\_test\_endpoint", index\_name="my\_catalog.my\_schema.my\_test\_table", primary\_key="my\_primary\_key\_name", embedding\_dimension=1536, # match the embeddings model dimension you're going to use embedding\_vector\_column="my\_embedding\_vector\_column\_name", # you name this anything you want - it'll be picked up by the LlamaIndex class schema={ "my\_primary\_key\_name": "string", "my\_embedding\_vector\_column\_name": "array", "text": "string", # one column must match the text\_column in the DatabricksVectorSearch instance created below; this will hold the raw node text, "doc\_id": "string", # one column must contain the reference document ID (this will be populated by LlamaIndex automatically) # add any other metadata you may have in your nodes (Databricks Vector Search supports metadata filtering) # NOTE THAT THESE FIELDS MUST BE ADDED EXPLICITLY TO BE USED FOR METADATA FILTERING }, ) databricks\_vector\_store = DatabricksVectorSearch( index=databricks\_index, text\_column="text", columns=None, # YOU MUST ALSO RECORD YOUR METADATA FIELD NAMES HERE ) # text\_column is required for self-managed embeddings storage\_context = StorageContext.from\_defaults( vector\_store=databricks\_vector\_store ) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

Query the index

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("Why did the author choose to work on AI?")

print(response.response)

query\_engine = index.as\_query\_engine() response = query\_engine.query("Why did the author choose to work on AI?") print(response.response)

Back to top

[Previous DashVector Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DashvectorIndexDemo/)[Next Deep Lake Vector Store Quickstart](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DeepLakeIndexDemo/)
