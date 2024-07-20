Title: Advanced Retrieval Strategies - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/optimizing/advanced_retrieval/advanced_retrieval/

Markdown Content:
Advanced Retrieval Strategies - LlamaIndex


Main Advanced Retrieval Strategies[#](https://docs.llamaindex.ai/en/stable/optimizing/advanced_retrieval/advanced_retrieval/#main-advanced-retrieval-strategies "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

There are a variety of more advanced retrieval strategies you may wish to try, each with different benefits:

*   [Reranking](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/CohereRerank/)
*   [Recursive retrieval](https://docs.llamaindex.ai/en/stable/examples/query_engine/pdf_tables/recursive_retriever/)
*   [Embedded tables](https://docs.llamaindex.ai/en/stable/examples/query_engine/sec_tables/tesla_10q_table/)
*   [Small-to-big retrieval](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/MetadataReplacementDemo/)

See our full [retrievers module guide](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retrievers/) for a comprehensive list of all retrieval strategies, broken down into different categories.

*   Basic retrieval from each index
*   Advanced retrieval and search
*   Auto-Retrieval
*   Knowledge Graph Retrievers
*   Composed/Hierarchical Retrievers
*   and more!

More resources are below.

Query Transformations[#](https://docs.llamaindex.ai/en/stable/optimizing/advanced_retrieval/advanced_retrieval/#query-transformations "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------

A user query can be transformed before it enters a pipeline (query engine, agent, and more). See resources below on query transformations:

*   [Query Transform Cookbook](https://docs.llamaindex.ai/en/stable/examples/query_transformations/query_transform_cookbook/)
*   [Query Transformations Docs](https://docs.llamaindex.ai/en/stable/optimizing/advanced_retrieval/query_transformations/)

Composable Retrievers[#](https://docs.llamaindex.ai/en/stable/optimizing/advanced_retrieval/advanced_retrieval/#composable-retrievers "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------

Every retriever is capable of retrieving and running other objects, including

*   other retrievers
*   query engines
*   query pipelines
*   other nodes

For more details, check out the guide below.

*   [Composable Retrievers](https://docs.llamaindex.ai/en/stable/examples/retrievers/composable_retrievers/)

Third-Party Resources[#](https://docs.llamaindex.ai/en/stable/optimizing/advanced_retrieval/advanced_retrieval/#third-party-resources "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------

Here are some third-party resources on advanced retrieval strategies.

*   [DeepMemory (Activeloop)](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/)
*   [Weaviate Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo-Hybrid/)
*   [Pinecone Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PineconeIndexDemo-Hybrid/)
*   [Milvus Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusHybridIndexDemo/)

Back to top

[Previous Agentic strategies](https://docs.llamaindex.ai/en/stable/optimizing/agentic_strategies/agentic_strategies/)[Next Query Transformations](https://docs.llamaindex.ai/en/stable/optimizing/advanced_retrieval/query_transformations/)
