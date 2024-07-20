Title: Managed Index with Zilliz Cloud Pipelines

URL Source: https://docs.llamaindex.ai/en/stable/examples/managed/zcpDemo/

Markdown Content:
Managed Index with Zilliz Cloud Pipelines - LlamaIndex


[Zilliz Cloud Pipelines](https://docs.zilliz.com/docs/pipelines) is a scalable API service for retrieval. You can use Zilliz Cloud Pipelines as managed index in `llama-index`. This service can transform documents into vector embeddings and store them in Zilliz Cloud for effective semantic search.

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/managed/zcpDemo/#setup)
------------------------------------------------------------------------------

1.  Install llama-index dependencies

In \[ \]:

Copied!

%pip install llama\-index\-indices\-managed\-zilliz

%pip install llama-index-indices-managed-zilliz

In \[ \]:

Copied!

%pip install llama\-index

%pip install llama-index

2.  Configure credentials of your [Zilliz Cloud](https://cloud.zilliz.com/signup?utm_source=twitter&utm_medium=social%20&utm_campaign=2023-12-22_social_pipeline-llamaindex_twitter) accounts.

In \[ \]:

Copied!

from getpass import getpass

ZILLIZ\_PROJECT\_ID \= getpass("Enter your Zilliz Project ID:")
ZILLIZ\_CLUSTER\_ID \= getpass("Enter your Zilliz Cluster ID:")
ZILLIZ\_TOKEN \= getpass("Enter your Zilliz API Key:")

from getpass import getpass ZILLIZ\_PROJECT\_ID = getpass("Enter your Zilliz Project ID:") ZILLIZ\_CLUSTER\_ID = getpass("Enter your Zilliz Cluster ID:") ZILLIZ\_TOKEN = getpass("Enter your Zilliz API Key:")

> [Find your OpenAI API key](https://beta.openai.com/account/api-keys)
> 
> [Find your Zilliz Cloud credentials](https://docs.zilliz.com/docs/on-zilliz-cloud-console)

Indexing documents[¶](https://docs.llamaindex.ai/en/stable/examples/managed/zcpDemo/#indexing-documents)
--------------------------------------------------------------------------------------------------------

> It is optional to add metadata for each document. The metadata can be used to filter doc data during retrieval.

### From Signed URL[¶](https://docs.llamaindex.ai/en/stable/examples/managed/zcpDemo/#from-signed-url)

Zilliz Cloud Pipelines accepts files from AWS S3 and Google Cloud Storage. You can generate a presigned url from the Object Storage and use `from_document_url()` to ingest the file. It can automatically index the document and store the doc chunks as vectors on Zilliz Cloud.

In \[ \]:

Copied!

from llama\_index.indices.managed.zilliz import ZillizCloudPipelineIndex

\# Create pipelines: skip this step if you have prepared valid pipelines
pipeline\_ids \= ZillizCloudPipelineIndex.create\_pipelines(
    project\_id\=ZILLIZ\_PROJECT\_ID,
    cluster\_id\=ZILLIZ\_CLUSTER\_ID,
    api\_key\=ZILLIZ\_TOKEN,
    data\_type\="doc",
    collection\_name\="zcp\_llamalection\_doc",  \# change this value will customize collection name
    metadata\_schema\={"user\_id": "VarChar"},
)
print(pipeline\_ids)

from llama\_index.indices.managed.zilliz import ZillizCloudPipelineIndex # Create pipelines: skip this step if you have prepared valid pipelines pipeline\_ids = ZillizCloudPipelineIndex.create\_pipelines( project\_id=ZILLIZ\_PROJECT\_ID, cluster\_id=ZILLIZ\_CLUSTER\_ID, api\_key=ZILLIZ\_TOKEN, data\_type="doc", collection\_name="zcp\_llamalection\_doc", # change this value will customize collection name metadata\_schema={"user\_id": "VarChar"}, ) print(pipeline\_ids)

{'INGESTION': 'pipe-d639f220f27320e2e381de', 'SEARCH': 'pipe-47bd43fe8fd54502874a08', 'DELETION': 'pipe-bd434c99e064282f1a28e8'}

In \[ \]:

Copied!

zcp\_doc\_index \= ZillizCloudPipelineIndex.from\_document\_url(
    \# a public or pre-signed url of a file stored on AWS S3 or Google Cloud Storage
    url\="https://publicdataset.zillizcloud.com/milvus\_doc.md",
    pipeline\_ids\=pipeline\_ids,
    api\_key\=ZILLIZ\_TOKEN,
    metadata\={
        "user\_id": "user-001"
    },  \# optional, which can be used for filtering
)

\# # Delete docs by doc name
\# zcp\_doc\_index.delete\_by\_expression(expression="doc\_name  'milvus\_doc\_22.md'")

### From Document Nodes[¶](https://docs.llamaindex.ai/en/stable/examples/managed/zcpDemo/#from-document-nodes)

Zilliz Cloud Pipelines support text as data input as well. The following example prepares data with a sample document node.

In \[ \]:

Copied!

from llama\_index.core import Document
from llama\_index.indices.managed.zilliz import ZillizCloudPipelineIndex

\# prepare documents
documents \= \[Document(text\="The number that is being searched for is ten.")\]

\# create pipelines: skip this step if you have prepared valid pipelines
pipeline\_ids \= ZillizCloudPipelineIndex.create\_pipelines(
    project\_id\=ZILLIZ\_PROJECT\_ID,
    cluster\_id\=ZILLIZ\_CLUSTER\_ID,
    api\_key\=ZILLIZ\_TOKEN,
    data\_type\="text",
    collection\_name\="zcp\_llamalection\_text",  \# change this value will customize collection name
)
print(pipeline\_ids)

from llama\_index.core import Document from llama\_index.indices.managed.zilliz import ZillizCloudPipelineIndex # prepare documents documents = \[Document(text="The number that is being searched for is ten.")\] # create pipelines: skip this step if you have prepared valid pipelines pipeline\_ids = ZillizCloudPipelineIndex.create\_pipelines( project\_id=ZILLIZ\_PROJECT\_ID, cluster\_id=ZILLIZ\_CLUSTER\_ID, api\_key=ZILLIZ\_TOKEN, data\_type="text", collection\_name="zcp\_llamalection\_text", # change this value will customize collection name ) print(pipeline\_ids)

{'INGESTION': 'pipe-2bbab10f273a57eb987024', 'SEARCH': 'pipe-e1914a072ec5e6f83e446a', 'DELETION': 'pipe-72bbabf273a51af0b0c447'}

In \[ \]:

Copied!

zcp\_text\_index \= ZillizCloudPipelineIndex.from\_documents(
    \# a public or pre-signed url of a file stored on AWS S3 or Google Cloud Storage
    documents\=documents,
    pipeline\_ids\=pipeline\_ids,
    api\_key\=ZILLIZ\_TOKEN,
)

zcp\_text\_index = ZillizCloudPipelineIndex.from\_documents( # a public or pre-signed url of a file stored on AWS S3 or Google Cloud Storage documents=documents, pipeline\_ids=pipeline\_ids, api\_key=ZILLIZ\_TOKEN, )

Working as Query Engine[¶](https://docs.llamaindex.ai/en/stable/examples/managed/zcpDemo/#working-as-query-engine)
------------------------------------------------------------------------------------------------------------------

To conduct semantic search with `ZillizCloudPipelineIndex`, you can use it `as_query_engine()` by specifying a few parameters:

*   **search\_top\_k**: How many text nodes/chunks to retrieve. Optional, defaults to `DEFAULT_SIMILARITY_TOP_K` (2).
*   **filters**: Metadata filters. Optional, defaults to None.
*   **output\_metadata**: What metadata fields to return with the retrieved text node. Optional, defaults to \[\].

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= getpass("Enter your OpenAI API Key:")

import os os.environ\["OPENAI\_API\_KEY"\] = getpass("Enter your OpenAI API Key:")

In \[ \]:

Copied!

query\_engine \= zcp\_doc\_index.as\_query\_engine(search\_top\_k\=3)

query\_engine = zcp\_doc\_index.as\_query\_engine(search\_top\_k=3)

Then the query engine is ready for Semantic Search or Retrieval Augmented Generation with Milvus 2.3 documents:

*   **Retrieve** (Semantic search powered by Zilliz Cloud Pipelines):

In \[ \]:

Copied!

question \= "Can users delete entities by filtering non-primary fields?"
retrieved\_nodes \= query\_engine.retrieve(question)
print(retrieved\_nodes)

question = "Can users delete entities by filtering non-primary fields?" retrieved\_nodes = query\_engine.retrieve(question) print(retrieved\_nodes)

\[NodeWithScore(node=TextNode(id\_='449755997496672548', embedding=None, metadata={}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='# Delete Entities\\nThis topic describes how to delete entities in Milvus.  \\nMilvus supports deleting entities by primary key or complex boolean expressions. Deleting entities by primary key is much faster and lighter than deleting them by complex boolean expressions. This is because Milvus executes queries first when deleting data by complex boolean expressions.  \\nDeleted entities can still be retrieved immediately after the deletion if the consistency level is set lower than Strong.\\nEntities deleted beyond the pre-specified span of time for Time Travel cannot be retrieved again.\\nFrequent deletion operations will impact the system performance.  \\nBefore deleting entities by comlpex boolean expressions, make sure the collection has been loaded.\\nDeleting entities by complex boolean expressions is not an atomic operation. Therefore, if it fails halfway through, some data may still be deleted.\\nDeleting entities by complex boolean expressions is supported only when the consistency is set to Bounded. For details, see Consistency.\\\\\\n\\\\\\n# Delete Entities\\n## Prepare boolean expression\\nPrepare the boolean expression that filters the entities to delete.  \\nMilvus supports deleting entities by primary key or complex boolean expressions. For more information on expression rules and supported operators, see Boolean Expression Rules.\\\\\\n\\\\\\n# Delete Entities\\n## Prepare boolean expression\\n### Simple boolean expression\\nUse a simple expression to filter data with primary key values of 0 and 1:  \\n\`\`\`python\\nexpr = "book\_id in \[0,1\]"\\n\`\`\`\\\\\\n\\\\\\n# Delete Entities\\n## Prepare boolean expression\\n### Complex boolean expression\\nTo filter entities that meet specific conditions, define complex boolean expressions.  \\nFilter entities whose word\_count is greater than or equal to 11000:  \\n\`\`\`python\\nexpr = "word\_count >= 11000"\\n\`\`\`  \\nFilter entities whose book\_name is not Unknown:  \\n\`\`\`python\\nexpr = "book\_name != Unknown"\\n\`\`\`  \\nFilter entities whose primary key values are greater than 5 and word\_count is smaller than or equal to 9999:  \\n\`\`\`python\\nexpr = "book\_id > 5 && word\_count <= 9999"\\n\`\`\`', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.742070198059082), NodeWithScore(node=TextNode(id\_='449755997496672549', embedding=None, metadata={}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='# Delete Entities\\n## Delete entities\\nDelete the entities with the boolean expression you created. Milvus returns the ID list of the deleted entities.\\n\`\`\`python\\nfrom pymilvus import Collection\\ncollection = Collection("book")      # Get an existing collection.\\ncollection.delete(expr)\\n\`\`\`  \\nParameter\\tDescription\\nexpr\\tBoolean expression that specifies the entities to delete.\\npartition\_name (optional)\\tName of the partition to delete entities from.\\\\\\n\\\\\\n# Upsert Entities\\nThis topic describes how to upsert entities in Milvus.  \\nUpserting is a combination of insert and delete operations. In the context of a Milvus vector database, an upsert is a data-level operation that will overwrite an existing entity if a specified field already exists in a collection, and insert a new entity if the specified value doesn’t already exist.  \\nThe following example upserts 3,000 rows of randomly generated data as the example data. When performing upsert operations, it\\'s important to note that the operation may compromise performance. This is because the operation involves deleting data during execution.\\\\\\n\\\\\\n# Upsert Entities\\n## Prepare data\\nFirst, prepare the data to upsert. The type of data to upsert must match the schema of the collection, otherwise Milvus will raise an exception.  \\nMilvus supports default values for scalar fields, excluding a primary key field. This indicates that some fields can be left empty during data inserts or upserts. For more information, refer to Create a Collection.  \\n\`\`\`python\\n# Generate data to upsert\\n\\nimport random\\nnb = 3000\\ndim = 8\\nvectors = \[\[random.random() for \_ in range(dim)\] for \_ in range(nb)\]\\ndata = \[\\n\[i for i in range(nb)\],\\n\[str(i) for i in range(nb)\],\\n\[i for i in range(10000, 10000+nb)\],\\nvectors,\\n\[str("dy"\*i) for i in range(nb)\]\\n\]\\n\`\`\`', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.6409814953804016), NodeWithScore(node=TextNode(id\_='449755997496672550', embedding=None, metadata={}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='# Upsert Entities\\n## Upsert data\\nUpsert the data to the collection.  \\n\`\`\`python\\nfrom pymilvus import Collection\\ncollection = Collection("book") # Get an existing collection.\\nmr = collection.upsert(data)\\n\`\`\`  \\nParameter\\tDescription\\ndata\\tData to upsert into Milvus.\\npartition\_name (optional)\\tName of the partition to upsert data into.\\ntimeout (optional)\\tAn optional duration of time in seconds to allow for the RPC. If it is set to None, the client keeps waiting until the server responds or error occurs.\\nAfter upserting entities into a collection that has previously been indexed, you do not need to re-index the collection, as Milvus will automatically create an index for the newly upserted data. For more information, refer to Can indexes be created after inserting vectors?\\\\\\n\\\\\\n# Upsert Entities\\n## Flush data\\nWhen data is upserted into Milvus it is updated and inserted into segments. Segments have to reach a certain size to be sealed and indexed. Unsealed segments will be searched brute force. In order to avoid this with any remainder data, it is best to call flush(). The flush() call will seal any remaining segments and send them for indexing. It is important to only call this method at the end of an upsert session. Calling it too often will cause fragmented data that will need to be cleaned later on.\\\\\\n\\\\\\n# Upsert Entities\\n## Limits\\nUpdating primary key fields is not supported by upsert().\\nupsert() is not applicable and an error can occur if autoID is set to True for primary key fields.', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.5456743240356445)\]

*   **Query** (RAG powered by Zilliz Cloud Pipelines as retriever and OpenAI's LLM):

In \[ \]:

Copied!

response \= query\_engine.query(question)
print(response.response)

response = query\_engine.query(question) print(response.response)

Users can delete entities by filtering non-primary fields using complex boolean expressions in Milvus.

Multi-Tenancy[¶](https://docs.llamaindex.ai/en/stable/examples/managed/zcpDemo/#multi-tenancy)
----------------------------------------------------------------------------------------------

With the tenant-specific value (eg. user id) as metadata, the managed index is able to achieve multi-tenancy by applying metadata filters.

By specifying metadata value, each document is tagged with the tenant-specific field at ingestion.

In \[ \]:

Copied!

zcp\_doc\_index.\_insert\_doc\_url(
    url\="https://publicdataset.zillizcloud.com/milvus\_doc\_22.md",
    metadata\={"user\_id": "user\_002"},
)

zcp\_doc\_index.\_insert\_doc\_url( url="https://publicdataset.zillizcloud.com/milvus\_doc\_22.md", metadata={"user\_id": "user\_002"}, )

Out\[ \]:

{'token\_usage': 984, 'doc\_name': 'milvus\_doc\_22.md', 'num\_chunks': 3}

Then the managed index is able to build a query engine for each tenant by filtering the tenant-specific field.

In \[ \]:

Copied!

from llama\_index.core.vector\_stores import ExactMatchFilter, MetadataFilters

query\_engine\_for\_user\_002 \= zcp\_doc\_index.as\_query\_engine(
    search\_top\_k\=3,
    filters\=MetadataFilters(
        filters\=\[ExactMatchFilter(key\="user\_id", value\="user\_002")\]
    ),
    output\_metadata\=\["user\_id"\],  \# optional, display user\_id in outputs
)

from llama\_index.core.vector\_stores import ExactMatchFilter, MetadataFilters query\_engine\_for\_user\_002 = zcp\_doc\_index.as\_query\_engine( search\_top\_k=3, filters=MetadataFilters( filters=\[ExactMatchFilter(key="user\_id", value="user\_002")\] ), output\_metadata=\["user\_id"\], # optional, display user\_id in outputs )

> Change `filters` to build query engines with different conditions.

In \[ \]:

Copied!

question \= "Can I delete entities by filtering non-primary fields?"

\# search\_results = query\_engine\_for\_user\_002.retrieve(question)
response \= query\_engine\_for\_user\_002.query(question)
print(response.response)

question = "Can I delete entities by filtering non-primary fields?" # search\_results = query\_engine\_for\_user\_002.retrieve(question) response = query\_engine\_for\_user\_002.query(question) print(response.response)

Milvus only supports deleting entities by primary key filtered with boolean expressions. Other operators can be used only in query or scalar filtering in vector search.

Back to top

[Previous Vectara Managed Index](https://docs.llamaindex.ai/en/stable/examples/managed/vectaraDemo/)[Next Entity Metadata Extraction](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/EntityExtractionClimate/)

Hi, how can I help you?

🦙
