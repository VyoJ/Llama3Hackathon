Title: Question-Answering (RAG) - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/use_cases/q_and_a/

Markdown Content:
Question-Answering (RAG) - LlamaIndex


One of the most common use-cases for LLMs is to answer questions over a set of data. This data is oftentimes in the form of unstructured documents (e.g. PDFs, HTML), but can also be semi-structured or structured.

The predominant framework for enabling QA with LLMs is Retrieval Augmented Generation (RAG). LlamaIndex offers simple-to-advanced RAG techniques to tackle simple-to-advanced questions over different volumes and types of data.

There are different subtypes of question-answering.

RAG over Unstructured Documents[#](https://docs.llamaindex.ai/en/stable/use_cases/q_and_a/#rag-over-unstructured-documents "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------

LlamaIndex can pull in unstructured text, PDFs, Notion and Slack documents and more and index the data within them.

The simplest queries involve either semantic search or summarization.

*   **Semantic search**: A query about specific information in a document that matches the query terms and/or semantic intent. This is typically executed with simple vector retrieval (top-k). [Example of semantic search](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/q_and_a/#semantic-search)
*   **Summarization**: condensing a large amount of data into a short summary relevant to your current question. [Example of summarization](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/q_and_a/#summarization)

QA over Structured Data[#](https://docs.llamaindex.ai/en/stable/use_cases/q_and_a/#qa-over-structured-data "Permanent link")
----------------------------------------------------------------------------------------------------------------------------

If your data already exists in a SQL database, CSV file, or other structured format, LlamaIndex can query the data in these sources. This includes **text-to-SQL** (natural language to SQL operations) and also **text-to-Pandas** (natural language to Pandas operations).

*   [Text-to-SQL Guide](https://docs.llamaindex.ai/en/stable/examples/index_structs/struct_indices/SQLIndexDemo/)
*   [Text-to-Pandas Guide](https://docs.llamaindex.ai/en/stable/examples/query_engine/pandas_query_engine/)

Advanced QA Topics[#](https://docs.llamaindex.ai/en/stable/use_cases/q_and_a/#advanced-qa-topics "Permanent link")
------------------------------------------------------------------------------------------------------------------

As you scale to more complex questions / more data, there are many techniques in LlamaIndex to help you with better query understanding, retrieval, and integration of data sources.

*   **Querying Complex Documents**: Oftentimes your document representation is complex - your PDF may have text, tables, charts, images, headers/footers, and more. LlamaIndex provides advanced indexing/retrieval integrated with LlamaParse, our proprietary document parser. [Full cookbooks here](https://github.com/run-llama/llama_parse/tree/main/examples).
*   **Combine multiple sources**: is some of your data in Slack, some in PDFs, some in unstructured text? LlamaIndex can combine queries across an arbitrary number of sources and combine them.
    *   [Example of combining multiple sources](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/q_and_a.md#multi-document-queries)
*   **Route across multiple sources**: given multiple data sources, your application can first pick the best source and then "route" the question to that source.
    *   [Example of routing across multiple sources](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/q_and_a.md#routing-over-heterogeneous-data)
*   **Multi-document queries**: some questions have partial answers in multiple data sources which need to be questioned separately before they can be combined
    *   [Example of multi-document queries](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/q_and_a.md#multi-document-queries)
    *   [Building a multi-document agent over the LlamaIndex docs](https://docs.llamaindex.ai/en/stable/examples/agent/multi_document_agents-v1/) - [Text to SQL](https://docs.llamaindex.ai/en/stable/examples/index_structs/struct_indices/SQLIndexDemo/)

Resources[#](https://docs.llamaindex.ai/en/stable/use_cases/q_and_a/#resources "Permanent link")
------------------------------------------------------------------------------------------------

LlamaIndex has a lot of resources around QA / RAG. Here are some core resource guides to refer to.

**I'm a RAG beginner and want to learn the basics**: Take a look at our ["Learn" series of guides](https://docs.llamaindex.ai/en/stable/understanding/).

**I've built RAG, and now I want to optimize it**: Take a look at our ["Advanced Topics" Guides](https://docs.llamaindex.ai/en/stable/optimizing/production_rag/).

**I want to learn all about a particular module**: Here are the core module guides to help build simple-to-advanced QA/RAG systems:

*   [Query Engines](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/)
*   [Chat Engines](https://docs.llamaindex.ai/en/stable/module_guides/deploying/chat_engines/)
*   [Agents](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/)

Further examples[#](https://docs.llamaindex.ai/en/stable/use_cases/q_and_a/#further-examples "Permanent link")
--------------------------------------------------------------------------------------------------------------

For further examples of Q&A use cases, see our [Q&A section in Putting it All Together](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/q_and_a.md).

Back to top

[Previous Prompting](https://docs.llamaindex.ai/en/stable/use_cases/prompting/)[Next Chatbots](https://docs.llamaindex.ai/en/stable/use_cases/chatbots/)

Hi, how can I help you?

🦙
