Title: Agentic strategies - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/optimizing/agentic_strategies/agentic_strategies/

Markdown Content:
Agentic strategies - LlamaIndex


You can build agents on top of your existing LlamaIndex RAG pipeline to empower it with automated decision capabilities. A lot of modules (routing, query transformations, and more) are already agentic in nature in that they use LLMs for decision making.

Simpler Agentic Strategies[#](https://docs.llamaindex.ai/en/stable/optimizing/agentic_strategies/agentic_strategies/#simpler-agentic-strategies "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

These include routing and query transformations.

*   [Routing](https://docs.llamaindex.ai/en/stable/module_guides/querying/router/)
*   [Query Transformations](https://docs.llamaindex.ai/en/stable/optimizing/advanced_retrieval/query_transformations/)
*   [Sub Question Query Engine (Intro)](https://docs.llamaindex.ai/en/stable/examples/query_engine/sub_question_query_engine/)

Data Agents[#](https://docs.llamaindex.ai/en/stable/optimizing/agentic_strategies/agentic_strategies/#data-agents "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------

This guides below show you how to deploy a full agent loop, capable of chain-of-thought and query planning, on top of existing RAG query engines as tools for more advanced decision making.

Make sure to check out our [full module guide on Data Agents](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/), which highlight these use cases and much more.

Our [lower-level agent API](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/agent_runner/) shows you the internals of how an agent works (with step-wise execution).

Example guides below (using OpenAI function calling):

*   [OpenAIAgent](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent/)
*   [OpenAIAgent with Query Engine Tools](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_with_query_engine/)
*   [OpenAIAgent Retrieval](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_retrieval/)
*   [OpenAIAgent Query Cookbook](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_query_cookbook/)
*   [OpenAIAgent Query Planning](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_query_plan/)
*   [OpenAIAgent Context Retrieval](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_context_retrieval/)

Back to top

[Previous Basic Strategies](https://docs.llamaindex.ai/en/stable/optimizing/basic_strategies/basic_strategies/)[Next Advanced Retrieval Strategies](https://docs.llamaindex.ai/en/stable/optimizing/advanced_retrieval/advanced_retrieval/)
