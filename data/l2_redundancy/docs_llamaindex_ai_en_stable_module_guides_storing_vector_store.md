Title: Vector Stores - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/module_guides/storing/vector_stores/

Markdown Content:
Vector Stores - LlamaIndex


Vector stores contain embedding vectors of ingested document chunks (and sometimes the document chunks as well).

Simple Vector Store[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/vector_stores/#simple-vector-store "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------

By default, LlamaIndex uses a simple in-memory vector store that's great for quick experimentation. They can be persisted to (and loaded from) disk by calling `vector_store.persist()` (and `SimpleVectorStore.from_persist_path(...)` respectively).

Vector Store Options & Feature Support[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/vector_stores/#vector-store-options-feature-support "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

LlamaIndex supports over 20 different vector store options. We are actively adding more integrations and improving feature coverage for each.

| Vector Store | Type | Metadata Filtering | Hybrid Search | Delete | Store Documents | Async |
| --- | --- | --- | --- | --- | --- | --- |
| Alibaba Cloud OpenSearch | cloud | ✓ |  | ✓ | ✓ | ✓ |
| Apache Cassandra® | self-hosted / cloud | ✓ |  | ✓ | ✓ |  |
| Astra DB | cloud | ✓ |  | ✓ | ✓ |  |
| Azure AI Search | cloud | ✓ | ✓ | ✓ | ✓ |  |
| Azure CosmosDB MongoDB | cloud |  |  | ✓ | ✓ |  |
| BaiduVectorDB | cloud | ✓ | ✓ |  | ✓ |  |
| ChatGPT Retrieval Plugin | aggregator |  |  | ✓ | ✓ |  |
| Chroma | self-hosted | ✓ |  | ✓ | ✓ |  |
| Couchbase | self-hosted / cloud | ✓ | ✓ | ✓ | ✓ |  |
| DashVector | cloud | ✓ | ✓ | ✓ | ✓ |  |
| Databricks | cloud | ✓ |  | ✓ | ✓ |  |
| Deeplake | self-hosted / cloud | ✓ |  | ✓ | ✓ |  |
| DocArray | aggregator | ✓ |  | ✓ | ✓ |  |
| DuckDB | in-memory / self-hosted | ✓ |  | ✓ | ✓ |  |
| DynamoDB | cloud |  |  | ✓ |  |  |
| Elasticsearch | self-hosted / cloud | ✓ | ✓ | ✓ | ✓ | ✓ |
| FAISS | in-memory |  |  |  |  |  |
| txtai | in-memory |  |  |  |  |  |
| Jaguar | self-hosted / cloud | ✓ | ✓ | ✓ | ✓ |  |
| LanceDB | cloud | ✓ |  | ✓ | ✓ |  |
| Lantern | self-hosted / cloud | ✓ | ✓ | ✓ | ✓ | ✓ |
| Metal | cloud | ✓ |  | ✓ | ✓ |  |
| MongoDB Atlas | self-hosted / cloud | ✓ |  | ✓ | ✓ |  |
| MyScale | cloud | ✓ | ✓ | ✓ | ✓ |  |
| Milvus / Zilliz | self-hosted / cloud | ✓ | ✓ | ✓ | ✓ |  |
| Neo4jVector | self-hosted / cloud | ✓ |  | ✓ | ✓ |  |
| OpenSearch | self-hosted / cloud | ✓ | ✓ | ✓ | ✓ | ✓ |
| Pinecone | cloud | ✓ | ✓ | ✓ | ✓ |  |
| Postgres | self-hosted / cloud | ✓ | ✓ | ✓ | ✓ | ✓ |
| pgvecto.rs | self-hosted / cloud | ✓ | ✓ | ✓ | ✓ |  |
| Qdrant | self-hosted / cloud | ✓ | ✓ | ✓ | ✓ | ✓ |
| Redis | self-hosted / cloud | ✓ |  | ✓ | ✓ |  |
| Simple | in-memory | ✓ |  | ✓ |  |  |
| SingleStore | self-hosted / cloud | ✓ |  | ✓ | ✓ |  |
| Supabase | self-hosted / cloud | ✓ |  | ✓ | ✓ |  |
| Tair | cloud | ✓ |  | ✓ | ✓ |  |
| TiDB | cloud | ✓ |  | ✓ | ✓ |  |
| TencentVectorDB | cloud | ✓ | ✓ | ✓ | ✓ |  |
| Timescale |  | ✓ |  | ✓ | ✓ | ✓ |
| Typesense | self-hosted / cloud | ✓ |  | ✓ | ✓ |  |
| Upstash | cloud |  |  |  | ✓ |  |
| Vearch | self-hosted | ✓ |  | ✓ | ✓ |  |
| Vespa | self-hosted / cloud | ✓ | ✓ | ✓ | ✓ |  |
| Vertex AI Vector Search | cloud | ✓ |  | ✓ | ✓ |  |
| Weaviate | self-hosted / cloud | ✓ | ✓ | ✓ | ✓ |  |

For more details, see [Vector Store Integrations](https://docs.llamaindex.ai/en/stable/community/integrations/vector_stores/).

Example Notebooks[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/vector_stores/#example-notebooks "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------

*   [Alibaba Cloud OpenSearch](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AlibabaCloudOpenSearchIndexDemo/)
*   [Astra DB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AstraDBIndexDemo/)
*   [Async Index Creation](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AsyncIndexCreationDemo/)
*   [Azure AI Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureAISearchIndexDemo/)
*   [Azure Cosmos DB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureCosmosDBMongoDBvCoreDemo/)
*   [Baidu](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BaiduVectorDBIndexDemo/)
*   [Caasandra](https://docs.llamaindex.ai/en/stable/examples/vector_stores/CassandraIndexDemo/)
*   [Chromadb](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ChromaIndexDemo/)
*   [Couchbase](https://docs.llamaindex.ai/en/stable/examples/vector_stores/CouchbaseVectorStoreDemo/)
*   [Dash](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DashvectorIndexDemo/)
*   [Databricks](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DatabricksVectorSearchDemo/)
*   [Deeplake](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DeepLakeIndexDemo/)
*   [DocArray HNSW](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DocArrayHnswIndexDemo/)
*   [DocArray in-Memory](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DocArrayInMemoryIndexDemo/)
*   [DuckDB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DuckDBDemo/)
*   [Espilla](https://docs.llamaindex.ai/en/stable/examples/vector_stores/EpsillaIndexDemo/)
*   [Jaguar](https://docs.llamaindex.ai/en/stable/examples/vector_stores/JaguarIndexDemo/)
*   [LanceDB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanceDBIndexDemo/)
*   [Lantern](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanternIndexDemo/)
*   [Metal](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MetalIndexDemo/)
*   [Milvus](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusIndexDemo/)
*   [Milvus Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusHybridIndexDemo/)
*   [MyScale](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MyScaleIndexDemo/)
*   [ElsaticSearch](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ElasticsearchIndexDemo/)
*   [FAISS](https://docs.llamaindex.ai/en/stable/examples/vector_stores/FaissIndexDemo/)
*   [MongoDB Atlas](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MongoDBAtlasVectorSearch/)
*   [Neo4j](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Neo4jVectorDemo/)
*   [OpenSearch](https://docs.llamaindex.ai/en/stable/examples/vector_stores/OpensearchDemo/)
*   [Pinecone](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PineconeIndexDemo/)
*   [Pinecone Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PineconeIndexDemo-Hybrid/)
*   [PGvectoRS](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PGVectoRsDemo/)
*   [Postgres](https://docs.llamaindex.ai/en/stable/examples/vector_stores/postgres/)
*   [Redis](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RedisIndexDemo/)
*   [Qdrant](https://docs.llamaindex.ai/en/stable/examples/vector_stores/QdrantIndexDemo/)
*   [Qdrant Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_hybrid/)
*   [Rockset](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RocksetIndexDemo/)
*   [Simple](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemo/)
*   [Supabase](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SupabaseVectorIndexDemo/)
*   [Tair](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TairIndexDemo/)
*   [TiDB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TiDBVector/)
*   [Tencent](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TencentVectorDBIndexDemo/)
*   [Timesacle](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Timescalevector/)
*   [Upstash](https://docs.llamaindex.ai/en/stable/examples/vector_stores/UpstashVectorDemo/)
*   [Vearch](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VearchDemo/)
*   [Vespa](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VespaIndexDemo/)
*   [Vertex AI Vector Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VertexAIVectorSearchDemo/)
*   [Weaviate](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo/)
*   [Weaviate Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo-Hybrid/)
*   [Zep](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ZepIndexDemo/)

Back to top

[Previous Storing](https://docs.llamaindex.ai/en/stable/module_guides/storing/)[Next Document Stores](https://docs.llamaindex.ai/en/stable/module_guides/storing/docstores/)
