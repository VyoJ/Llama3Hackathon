Title: Structured Data Extraction - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/use_cases/extraction/

Markdown Content:
Structured Data Extraction - LlamaIndex


LLMs are capable of ingesting large amounts of unstructured data and returning it in structured formats, and LlamaIndex is set up to make this easy.

Using LlamaIndex, you can get an LLM to read natural language and identify semantically important details such as names, dates, addresses, and figures, and return them in a consistent structured format regardless of the source format.

This can be especially useful when you have unstructured source material like chat logs and conversation transcripts.

Once you have structured data you can send them to a database, or you can parse structured outputs in code to automate workflows.

Core Guides[#](https://docs.llamaindex.ai/en/stable/use_cases/extraction/#core-guides "Permanent link")
-------------------------------------------------------------------------------------------------------

Check out our Structured Output guide for a comprehensive overview of structured data extraction with LlamaIndex. Do it in a standalone fashion (Pydantic program) or as part of a RAG pipeline. We also have standalone output parsing modules that you can use yourself with an LLM / prompt.

*   [Structured Outputs](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/)
*   [Pydantic Program](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/pydantic_program/)
*   [Output Parsing](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/output_parser/)

We also have multi-modal structured data extraction. [Check it out](https://docs.llamaindex.ai/en/stable/use_cases/multimodal/#simple-evaluation-of-multi-modal-rag).

Misc Examples[#](https://docs.llamaindex.ai/en/stable/use_cases/extraction/#misc-examples "Permanent link")
-----------------------------------------------------------------------------------------------------------

Some additional miscellaneous examples highlighting use cases:

*   [Extracting names and locations from descriptions of people](https://docs.llamaindex.ai/en/stable/examples/output_parsing/df_program/)
*   [Extracting album data from music reviews](https://docs.llamaindex.ai/en/stable/examples/llm/llama_api/)
*   [Extracting information from emails](https://docs.llamaindex.ai/en/stable/examples/usecases/email_data_extraction/)

Back to top

[Previous Chatbots](https://docs.llamaindex.ai/en/stable/use_cases/chatbots/)[Next Agents](https://docs.llamaindex.ai/en/stable/use_cases/agents/)

Hi, how can I help you?

🦙
