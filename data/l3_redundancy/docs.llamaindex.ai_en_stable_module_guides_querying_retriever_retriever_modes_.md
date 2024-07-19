Title: Retriever Modes - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retriever_modes/

Markdown Content:
Retriever Modes - LlamaIndex


Here we show the mapping from `retriever_mode` configuration to the selected retriever class.

> Note that `retriever_mode` can mean different thing for different index classes.

Vector Index[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retriever_modes/#vector-index "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------

Specifying `retriever_mode` has no effect (silently ignored). `vector_index.as_retriever(...)` always returns a VectorIndexRetriever.

Summary Index[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retriever_modes/#summary-index "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------

*   `default`: SummaryIndexRetriever
*   `embedding`: SummaryIndexEmbeddingRetriever
*   `llm`: SummaryIndexLLMRetriever

Tree Index[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retriever_modes/#tree-index "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------

*   `select_leaf`: TreeSelectLeafRetriever
*   `select_leaf_embedding`: TreeSelectLeafEmbeddingRetriever
*   `all_leaf`: TreeAllLeafRetriever
*   `root`: TreeRootRetriever

Keyword Table Index[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retriever_modes/#keyword-table-index "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------

*   `default`: KeywordTableGPTRetriever
*   `simple`: KeywordTableSimpleRetriever
*   `rake`: KeywordTableRAKERetriever

Knowledge Graph Index[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retriever_modes/#knowledge-graph-index "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------

*   `keyword`: KGTableRetriever
*   `embedding`: KGTableRetriever
*   `hybrid`: KGTableRetriever

Document Summary Index[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retriever_modes/#document-summary-index "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------

*   `llm`: DocumentSummaryIndexLLMRetriever
*   `embedding`: DocumentSummaryIndexEmbeddingRetrievers

Back to top

[Previous Retriever Modules](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retrievers/)[Next Node Postprocessor](https://docs.llamaindex.ai/en/stable/module_guides/querying/node_postprocessors/)
