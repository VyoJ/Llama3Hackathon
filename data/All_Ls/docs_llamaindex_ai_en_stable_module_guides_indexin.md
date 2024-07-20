Title: Indexing - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/module_guides/indexing/

Markdown Content:
Indexing - LlamaIndex


Concept[#](https://docs.llamaindex.ai/en/stable/module_guides/indexing/#concept "Permanent link")
-------------------------------------------------------------------------------------------------

An `Index` is a data structure that allows us to quickly retrieve relevant context for a user query. For LlamaIndex, it's the core foundation for retrieval-augmented generation (RAG) use-cases.

At a high-level, `Indexes` are built from [Documents](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/). They are used to build [Query Engines](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/) and [Chat Engines](https://docs.llamaindex.ai/en/stable/module_guides/deploying/chat_engines/) which enables question & answer and chat over your data.

Under the hood, `Indexes` store data in `Node` objects (which represent chunks of the original documents), and expose a [Retriever](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/) interface that supports additional configuration and automation.

The most common index by far is the `VectorStoreIndex`; the best place to start is the [VectorStoreIndex usage guide](https://docs.llamaindex.ai/en/stable/module_guides/indexing/vector_store_index/).

For other indexes, check out our guide to [how each index works](https://docs.llamaindex.ai/en/stable/module_guides/indexing/index_guide/) to help you decide which one matches your use-case.

Other Index resources[#](https://docs.llamaindex.ai/en/stable/module_guides/indexing/#other-index-resources "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------

See the [modules guide](https://docs.llamaindex.ai/en/stable/module_guides/indexing/modules/).

Back to top

[Previous Transformations](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/transformations/)[Next Index Guide](https://docs.llamaindex.ai/en/stable/module_guides/indexing/index_guide/)
