Title: Prompting - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/use_cases/prompting/

Markdown Content:
Prompting - LlamaIndex


Prompting LLMs is a fundamental unit of any LLM application. You can build an entire application entirely around prompting, or orchestrate with other modules (e.g. retrieval) to build RAG, agents, and more.

LlamaIndex supports LLM abstractions and simple-to-advanced prompt abstractions to make complex prompt workflows possible.

LLM Integrations[#](https://docs.llamaindex.ai/en/stable/use_cases/prompting/#llm-integrations "Permanent link")
----------------------------------------------------------------------------------------------------------------

LlamaIndex supports 40+ LLM integrations, from proprietary model providers like OpenAI, Anthropic to open-source models/model providers like Mistral, Ollama, Replicate. It provides all the tools to standardize interface around common LLM usage patterns, including but not limited to async, streaming, function calling.

Here's the [full module guide for LLMs](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/).

Prompts[#](https://docs.llamaindex.ai/en/stable/use_cases/prompting/#prompts "Permanent link")
----------------------------------------------------------------------------------------------

LlamaIndex has robust prompt abstractions that capture all the common interaction patterns with LLMs.

Here's the [full module guide for prompts](https://docs.llamaindex.ai/en/stable/module_guides/models/prompts/).

### Table Stakes[#](https://docs.llamaindex.ai/en/stable/use_cases/prompting/#table-stakes "Permanent link")

*   [Text Completion Prompts](https://docs.llamaindex.ai/en/stable/examples/customization/prompts/completion_prompts/)
*   [Chat Prompts](https://docs.llamaindex.ai/en/stable/examples/customization/prompts/chat_prompts/)

### Advanced[#](https://docs.llamaindex.ai/en/stable/use_cases/prompting/#advanced "Permanent link")

*   [Variable Mappings, Functions, Partials](https://docs.llamaindex.ai/en/stable/examples/prompts/advanced_prompts/)
*   [Few-shot Examples, RAG](https://docs.llamaindex.ai/en/stable/examples/prompts/prompts_rag/)

Prompt Chains and Pipelines[#](https://docs.llamaindex.ai/en/stable/use_cases/prompting/#prompt-chains-and-pipelines "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------

LlamaIndex has robust abstractions for creating sequential prompt chains, as well as general DAGs to orchestrate prompts with any other component. This allows you to build complex workflows, including RAG with multi-hop query understanding layers, as well as agents.

These pipelines are integrated with [observability partners](https://docs.llamaindex.ai/en/stable/module_guides/observability/) out of the box.

The central guide for prompt chains and pipelines is through our [Query Pipelines](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/).

Back to top

[Previous Use Cases](https://docs.llamaindex.ai/en/stable/use_cases/)[Next Question-Answering (RAG)](https://docs.llamaindex.ai/en/stable/use_cases/q_and_a/)

Hi, how can I help you?

🦙
