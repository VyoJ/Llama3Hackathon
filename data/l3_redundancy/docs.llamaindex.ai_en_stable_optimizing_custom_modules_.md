Title: Writing Custom Modules - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/optimizing/custom_modules/

Markdown Content:
Writing Custom Modules - LlamaIndex


A core design principle of LlamaIndex is that **almost every core module can be subclassed and customized**.

This allows you to use LlamaIndex for any advanced LLM use case, beyond the capabilities offered by our prepackaged modules. You're free to write as much custom code for any given module, but still take advantage of our lower-level abstractions and also plug this module along with other components.

We offer convenient/guided ways to subclass our modules, letting you write your custom logic without having to worry about having to define all boilerplate (for instance, [callbacks](https://docs.llamaindex.ai/en/stable/module_guides/observability/callbacks/)).

This guide centralizes all the resources around writing custom modules in LlamaIndex. Check them out below 👇

Custom LLMs[#](https://docs.llamaindex.ai/en/stable/optimizing/custom_modules/#custom-llms "Permanent link")
------------------------------------------------------------------------------------------------------------

*   [Custom LLMs](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/usage_custom/#example-using-a-custom-llm-model---advanced)

Custom Embeddings[#](https://docs.llamaindex.ai/en/stable/optimizing/custom_modules/#custom-embeddings "Permanent link")
------------------------------------------------------------------------------------------------------------------------

*   [Custom Embedding Model](https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings/#custom-embedding-model)

Custom Output Parsers[#](https://docs.llamaindex.ai/en/stable/optimizing/custom_modules/#custom-output-parsers "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------

*   [Custom Output Parsers](https://docs.llamaindex.ai/en/stable/examples/output_parsing/llm_program/)

Custom Transformations[#](https://docs.llamaindex.ai/en/stable/optimizing/custom_modules/#custom-transformations "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------

*   [Custom Transformations](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/transformations/#custom-transformations)
*   [Custom Property Graph Extractors](https://docs.llamaindex.ai/en/stable/module_guides/indexing/lpg_index_guide/#sub-classing-extractors)

Custom Retrievers[#](https://docs.llamaindex.ai/en/stable/optimizing/custom_modules/#custom-retrievers "Permanent link")
------------------------------------------------------------------------------------------------------------------------

*   [Custom Retrievers](https://docs.llamaindex.ai/en/stable/examples/query_engine/CustomRetrievers/)
*   [Custom Property Graph Retrievers](https://docs.llamaindex.ai/en/stable/module_guides/indexing/lpg_index_guide/#sub-classing-retrievers)

Custom Postprocessors/Rerankers[#](https://docs.llamaindex.ai/en/stable/optimizing/custom_modules/#custom-postprocessorsrerankers "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------

*   [Custom Node Postprocessor](https://docs.llamaindex.ai/en/stable/optimizing/custom_modules/#custom-postprocessorsrerankers)

Custom Query Engines[#](https://docs.llamaindex.ai/en/stable/optimizing/custom_modules/#custom-query-engines "Permanent link")
------------------------------------------------------------------------------------------------------------------------------

*   [Custom Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/custom_query_engine/)

Custom Agents[#](https://docs.llamaindex.ai/en/stable/optimizing/custom_modules/#custom-agents "Permanent link")
----------------------------------------------------------------------------------------------------------------

*   [Custom Agents](https://docs.llamaindex.ai/en/stable/examples/agent/custom_agent/)

Custom Query Components (for use in Query Pipeline)[#](https://docs.llamaindex.ai/en/stable/optimizing/custom_modules/#custom-query-components-for-use-in-query-pipeline "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   [Custom Query Component](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/usage_pattern/#defining-a-custom-query-component)

Other Ways of Customization[#](https://docs.llamaindex.ai/en/stable/optimizing/custom_modules/#other-ways-of-customization "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------

Some modules can be customized heavily within your workflows but not through subclassing (and instead through parameters or functions we expose). We list these in guides below:

*   [Customizing Documents](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_documents/)
*   [Customizing Nodes](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_nodes/)
*   [Customizing Prompts within Higher-Level Modules](https://docs.llamaindex.ai/en/stable/examples/prompts/prompt_mixin/)

Back to top

[Previous Fine-Tuning](https://docs.llamaindex.ai/en/stable/optimizing/fine-tuning/fine-tuning/)[Next Building RAG from Scratch (Lower-Level)](https://docs.llamaindex.ai/en/stable/optimizing/building_rag_from_scratch/)
