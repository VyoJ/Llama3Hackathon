Title: Agents - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/use_cases/agents/

Markdown Content:
Agents - LlamaIndex


An "agent" is an automated reasoning and decision engine. It takes in a user input/query and can make internal decisions for executing that query in order to return the correct result. The key agent components can include, but are not limited to:

*   Breaking down a complex question into smaller ones
*   Choosing an external Tool to use + coming up with parameters for calling the Tool
*   Planning out a set of tasks
*   Storing previously completed tasks in a memory module

LlamaIndex provides a comprehensive framework for building agents. This includes the following components:

*   Using agents with tools at a high-level to build agentic RAG and workflow automation use cases
*   Low-level components for building and debugging agents
*   Core agent ingredients that can be used as standalone modules: query planning, tool use, and more.

Use Cases[#](https://docs.llamaindex.ai/en/stable/use_cases/agents/#use-cases "Permanent link")
-----------------------------------------------------------------------------------------------

The scope of possible use cases for agents is vast and ever-expanding. That said, here are some practical use cases that can deliver immediate value.

*   **Agentic RAG**: Build a context-augmented research assistant over your data that not only answers simple questions, but complex research tasks. Here are two resources ([resource 1](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/agents/), [resource 2](https://docs.llamaindex.ai/en/stable/optimizing/agentic_strategies/agentic_strategies/)) to help you get started.
    
*   **SQL Agent**: A subset of the above is a "text-to-SQL assistant" that can interact with a structured database. Check out [this guide](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/query_pipeline_agent/?h=sql+agent#setup-simple-retry-agent-pipeline-for-text-to-sql) to see how to build an agent from scratch.
    
*   **Workflow Assistant**: Build an agent that can operate over common workflow tools like email, calendar. Check out our [GSuite agent tutorial](https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/tools/llama-index-tools-google/examples/advanced_tools_usage.ipynb).
    
*   **Coding Assistant**: Build an agent that can operate over code. Check out our [code interpreter tutorial](https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/tools/llama-index-tools-code-interpreter/examples/code_interpreter.ipynb).
    

Resources[#](https://docs.llamaindex.ai/en/stable/use_cases/agents/#resources "Permanent link")
-----------------------------------------------------------------------------------------------

**Using Agents with Tools**

The following component guides are the central hubs for getting started in building with agents:

*   [Agents](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/)
*   [Tools](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/)

**Building Custom Agents**

If you're interested in building custom agents, check out the following resources.

*   [Custom Agent](https://docs.llamaindex.ai/en/stable/examples/agent/custom_agent/)
*   [Custom Agent with Query Pipelines](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/query_pipeline_agent/)

**Building with Agentic Ingredients**

LlamaIndex has robust abstractions for every agent sub-ingredient.

*   **Query Planning**: [Routing](https://docs.llamaindex.ai/en/stable/module_guides/querying/router/), [Sub-Questions](https://docs.llamaindex.ai/en/stable/examples/query_engine/sub_question_query_engine/), [Query Transformations](https://docs.llamaindex.ai/en/stable/optimizing/advanced_retrieval/query_transformations/).
*   **Function Calling and Tool Use**: Check out our [OpenAI](https://docs.llamaindex.ai/en/stable/examples/llm/openai/), [Mistral](https://docs.llamaindex.ai/en/stable/examples/llm/mistralai/) guides as examples.
*   **Memory**: [Example guide for adding memory to RAG](https://docs.llamaindex.ai/en/stable/use_cases/examples/pipeline/query_pipeline_memory/).

LlamaHub[#](https://docs.llamaindex.ai/en/stable/use_cases/agents/#llamahub "Permanent link")
---------------------------------------------------------------------------------------------

We offer a collection of 40+ agent tools for use with your agent in [LlamaHub](https://llamahub.ai/) 🦙.

Back to top

[Previous Structured Data Extraction](https://docs.llamaindex.ai/en/stable/use_cases/extraction/)[Next Multi-Modal Applications](https://docs.llamaindex.ai/en/stable/use_cases/multimodal/)

Hi, how can I help you?

🦙
