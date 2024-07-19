Title: Building an LLM Application - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/understanding/

Markdown Content:
Building an LLM Application - LlamaIndex


Welcome to the beginning of Understanding LlamaIndex. This is a series of short, bite-sized tutorials on every stage of building an LLM application to get you acquainted with how to use LlamaIndex before diving into more advanced and subtle strategies. If you're an experienced programmer new to LlamaIndex, this is the place to start.

Key steps in building an LLM application[#](https://docs.llamaindex.ai/en/stable/understanding/#key-steps-in-building-an-llm-application "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------

Tip

If you've already read our [high-level concepts](https://docs.llamaindex.ai/en/stable/getting_started/concepts/) page you'll recognize several of these steps.

This tutorial has two main parts: **Building a RAG pipeline** and **Building an agent**, with some smaller sections before and after. Here's what to expect:

*   **[Using LLMs](https://docs.llamaindex.ai/en/stable/understanding/using_llms/using_llms/)**: hit the ground running by getting started working with LLMs. We'll show you how to use any of our [dozens of supported LLMs](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/modules/), whether via remote API calls or running locally on your machine.
    
*   **Building a RAG pipeline**: Retrieval-Augmented Generation (RAG) is a key technique for getting your data into an LLM, and a component of more sophisticated agentic systems. We'll show you how to build a full-featured RAG pipeline that can answer questions about your data. This includes:
    
    *   **[Loading & Ingestion](https://docs.llamaindex.ai/en/stable/understanding/loading/loading/)**: Getting your data from wherever it lives, whether that's unstructured text, PDFs, databases, or APIs to other applications. LlamaIndex has hundreds of connectors to every data source over at [LlamaHub](https://llamahub.ai/).
        
    *   **[Indexing and Embedding](https://docs.llamaindex.ai/en/stable/understanding/indexing/indexing/)**: Once you've got your data there are an infinite number of ways to structure access to that data to ensure your applications is always working with the most relevant data. LlamaIndex has a huge number of these strategies built-in and can help you select the best ones.
        
    *   **[Storing](https://docs.llamaindex.ai/en/stable/understanding/storing/storing/)**: You will probably find it more efficient to store your data in indexed form, or pre-processed summaries provided by an LLM, often in a specialized database known as a `Vector Store` (see below). You can also store your indexes, metadata and more.
        
    *   **[Querying](https://docs.llamaindex.ai/en/stable/understanding/querying/querying/)**: Every indexing strategy has a corresponding querying strategy and there are lots of ways to improve the relevance, speed and accuracy of what you retrieve and what the LLM does with it before returning it to you, including turning it into structured responses such as an API.
        
*   **Building an agent**: agents are LLM-powered knowledge workers that can interact with the world via a set of tools. Those tools can be RAG engines such as you learned how to build in the previous section, or any arbitrary code. This tutorial includes:
    
    *   **[Building a basic agent](https://docs.llamaindex.ai/en/stable/understanding/agent/basic_agent/)**: We show you how to build a simple agent that can interact with the world via a set of tools.
        
    *   **[Using local models with agents](https://docs.llamaindex.ai/en/stable/understanding/agent/local_models/)**: Agents can be built to use local models, which can be important for performance or privacy reasons.
        
    *   **[Adding RAG to an agent](https://docs.llamaindex.ai/en/stable/understanding/agent/rag_agent/)**: The RAG pipelines you built in the previous tutorial can be used as a tool by an agent, giving your agent powerful information-retrieval capabilities.
        
    *   **[Adding other tools](https://docs.llamaindex.ai/en/stable/understanding/agent/tools/)**: Let's add more sophisticated tools to your agent, such as API integrations.
        
*   **[Putting it all together](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/)**: whether you are building question & answering, chatbots, an API, or an autonomous agent, we show you how to get your application into production.
    
*   **[Tracing and debugging](https://docs.llamaindex.ai/en/stable/understanding/tracing_and_debugging/tracing_and_debugging/)**: also called **observability**, it's especially important with LLM applications to be able to look into the inner workings of what's going on to help you debug problems and spot places to improve.
    
*   **[Evaluating](https://docs.llamaindex.ai/en/stable/understanding/evaluating/evaluating/)**: every strategy has pros and cons and a key part of building, shipping and evolving your application is evaluating whether your change has improved your application in terms of accuracy, performance, clarity, cost and more. Reliably evaluating your changes is a crucial part of LLM application development.
    

Let's get started![#](https://docs.llamaindex.ai/en/stable/understanding/#lets-get-started "Permanent link")
------------------------------------------------------------------------------------------------------------

Ready to dive in? Head to [using LLMs](https://docs.llamaindex.ai/en/stable/understanding/using_llms/using_llms/).

Back to top

[Previous RAG CLI](https://docs.llamaindex.ai/en/stable/getting_started/starter_tools/rag_cli/)[Next Using LLMs](https://docs.llamaindex.ai/en/stable/understanding/using_llms/using_llms/)

Hi, how can I help you?

🦙
