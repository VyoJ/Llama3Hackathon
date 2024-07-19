Title: Web Page Reader - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/

Markdown Content:
Web Page Reader - LlamaIndex
===============
             

[Skip to content](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/#web-page-reader)

[![Image 1: logo](https://docs.llamaindex.ai/en/stable/_static/assets/LlamaSquareBlack.svg)](https://docs.llamaindex.ai/en/stable/ "LlamaIndex")

LlamaIndex

Web Page Reader

  

Initializing search

*   [Home](https://docs.llamaindex.ai/en/stable/)
*   [Learn](https://docs.llamaindex.ai/en/stable/understanding/)
*   [Use Cases](https://docs.llamaindex.ai/en/stable/use_cases/)
*   [Examples](https://docs.llamaindex.ai/en/stable/examples/)
*   [Component Guides](https://docs.llamaindex.ai/en/stable/module_guides/)
*   [Advanced Topics](https://docs.llamaindex.ai/en/stable/optimizing/production_rag/)
*   [API Reference](https://docs.llamaindex.ai/en/stable/api_reference/)
*   [Open-Source Community](https://docs.llamaindex.ai/en/stable/community/integrations/)
*   [LlamaCloud](https://docs.llamaindex.ai/en/stable/llama_cloud/)

 [![Image 2: logo](https://docs.llamaindex.ai/en/stable/_static/assets/LlamaSquareBlack.svg)](https://docs.llamaindex.ai/en/stable/ "LlamaIndex")LlamaIndex

*   [Home](https://docs.llamaindex.ai/en/stable/)
    
    Home
    
    *   [High-Level Concepts](https://docs.llamaindex.ai/en/stable/getting_started/concepts/)
    *   [Installation and Setup](https://docs.llamaindex.ai/en/stable/getting_started/installation/)
    *   [How to read these docs](https://docs.llamaindex.ai/en/stable/getting_started/reading/)
    *    Starter Examples
        
        Starter Examples
        
        *   [Starter Tutorial (OpenAI)](https://docs.llamaindex.ai/en/stable/getting_started/starter_example/)
        *   [Starter Tutorial (Local Models)](https://docs.llamaindex.ai/en/stable/getting_started/starter_example_local/)
        
    *   [Discover LlamaIndex Video Series](https://docs.llamaindex.ai/en/stable/getting_started/discover_llamaindex/)
    *   [Frequently Asked Questions (FAQ)](https://docs.llamaindex.ai/en/stable/getting_started/customization/)
    *   [Starter Tools](https://docs.llamaindex.ai/en/stable/getting_started/starter_tools/)
        
        Starter Tools
        
        *   [RAG CLI](https://docs.llamaindex.ai/en/stable/getting_started/starter_tools/rag_cli/)
        
    
*   [Learn](https://docs.llamaindex.ai/en/stable/understanding/)
    
    Learn
    
    *   [Using LLMs](https://docs.llamaindex.ai/en/stable/understanding/using_llms/using_llms/)
    *    Building a RAG pipeline
        
        Building a RAG pipeline
        
        *    Loading & Ingestion
            
            Loading & Ingestion
            
            *   [Loading Data (Ingestion)](https://docs.llamaindex.ai/en/stable/understanding/loading/loading/)
            *   [LlamaHub](https://docs.llamaindex.ai/en/stable/understanding/loading/llamahub/)
            
        *   [Indexing & Embedding](https://docs.llamaindex.ai/en/stable/understanding/indexing/indexing/)
        *   [Storing](https://docs.llamaindex.ai/en/stable/understanding/storing/storing/)
        *   [Querying](https://docs.llamaindex.ai/en/stable/understanding/querying/querying/)
        
    *    Building an agent
        
        Building an agent
        
        *   [Building a basic agent](https://docs.llamaindex.ai/en/stable/understanding/agent/basic_agent/)
        *   [Agents with local models](https://docs.llamaindex.ai/en/stable/understanding/agent/local_models/)
        *   [Adding RAG to an agent](https://docs.llamaindex.ai/en/stable/understanding/agent/rag_agent/)
        *   [Enhancing with LlamaParse](https://docs.llamaindex.ai/en/stable/understanding/agent/llamaparse/)
        *   [Memory](https://docs.llamaindex.ai/en/stable/understanding/agent/memory/)
        *   [Adding other tools](https://docs.llamaindex.ai/en/stable/understanding/agent/tools/)
        
    *   [Tracing and Debugging](https://docs.llamaindex.ai/en/stable/understanding/tracing_and_debugging/tracing_and_debugging/)
    *    Evaluating
        
        Evaluating
        
        *   [Evaluating](https://docs.llamaindex.ai/en/stable/understanding/evaluating/evaluating/)
        *   [Cost Analysis](https://docs.llamaindex.ai/en/stable/understanding/evaluating/cost_analysis/)
            
            Cost Analysis
            
            *   [Usage Pattern](https://docs.llamaindex.ai/en/stable/understanding/evaluating/cost_analysis/usage_pattern/)
            
        
    *   [Putting it all Together](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/)
        
        Putting it all Together
        
        *   [Full-stack web application](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/apps/)
            
            Full-stack web application
            
            *   [A Guide to Building a Full-Stack Web App with LLamaIndex](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/apps/fullstack_app_guide/)
            *   [A Guide to Building a Full-Stack LlamaIndex Web App with Delphic](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/apps/fullstack_with_delphic/)
            
        *   [Q&A Patterns](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/q_and_a/)
            
            Q&A Patterns
            
            *   [A Guide to Extracting Terms and Definitions](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/q_and_a/terms_definitions_tutorial/)
            
        *    Chatbots
            
            Chatbots
            
            *   [How to Build a Chatbot](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/chatbots/building_a_chatbot/)
            
        *   [Structured data](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/structured_data/)
            
            Structured data
            
        *   [Agents](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/agents/)
        
    
*   [Use Cases](https://docs.llamaindex.ai/en/stable/use_cases/)
    
    Use Cases
    
    *   [Prompting](https://docs.llamaindex.ai/en/stable/use_cases/prompting/)
    *   [Question-Answering (RAG)](https://docs.llamaindex.ai/en/stable/use_cases/q_and_a/)
    *   [Chatbots](https://docs.llamaindex.ai/en/stable/use_cases/chatbots/)
    *   [Structured Data Extraction](https://docs.llamaindex.ai/en/stable/use_cases/extraction/)
    *   [Agents](https://docs.llamaindex.ai/en/stable/use_cases/agents/)
    *   [Multi-Modal Applications](https://docs.llamaindex.ai/en/stable/use_cases/multimodal/)
    *   [Fine-Tuning](https://docs.llamaindex.ai/en/stable/use_cases/fine_tuning/)
    
*   [Examples](https://docs.llamaindex.ai/en/stable/examples/)
    
    Examples
    
    *    Agents
        
        Agents
        
        *   [💬🤖 How to Build a Chatbot](https://docs.llamaindex.ai/en/stable/examples/agent/Chatbot_SEC/)
        *   [GPT Builder Demo](https://docs.llamaindex.ai/en/stable/examples/agent/agent_builder/)
        *   [Building a Multi-PDF Agent using Query Pipelines and HyDE](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_around_query_pipeline_with_HyDE_for_PDFs/)
        *   [Step-wise, Controllable Agents](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_runner/)
        *   [Controllable Agents for RAG](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_runner_rag_controllable/)
        *   [Building an Agent around a Query Pipeline](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/query_pipeline_agent/)
        *   [Agentic rag using vertex ai](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/)
        *   [Agentic rag with llamaindex and vertexai managed index](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_with_llamaindex_and_vertexai_managed_index/)
        *   [Function Calling Anthropic Agent](https://docs.llamaindex.ai/en/stable/examples/agent/anthropic_agent/)
        *   [Function Calling AWS Bedrock Converse Agent](https://docs.llamaindex.ai/en/stable/examples/agent/bedrock_converse_agent/)
        *   [Chain-of-Abstraction LlamaPack](https://docs.llamaindex.ai/en/stable/examples/agent/coa_agent/)
        *   [Building a Custom Agent](https://docs.llamaindex.ai/en/stable/examples/agent/custom_agent/)
        *   [DashScope Agent Tutorial](https://docs.llamaindex.ai/en/stable/examples/agent/dashscope_agent/)
        *   [Introspective Agents: Performing Tasks With Reflection](https://docs.llamaindex.ai/en/stable/examples/agent/introspective_agent_toxicity_reduction/)
        *   [Language Agent Tree Search](https://docs.llamaindex.ai/en/stable/examples/agent/lats_agent/)
        *   [LLM Compiler Agent Cookbook](https://docs.llamaindex.ai/en/stable/examples/agent/llm_compiler/)
        *   [Simple Composable Memory](https://docs.llamaindex.ai/en/stable/examples/agent/memory/composable_memory/)
        *   [Vector Memory](https://docs.llamaindex.ai/en/stable/examples/agent/memory/vector_memory/)
        *   [Function Calling Mistral Agent](https://docs.llamaindex.ai/en/stable/examples/agent/mistral_agent/)
        *   [Multi-Document Agents (V1)](https://docs.llamaindex.ai/en/stable/examples/agent/multi_document_agents-v1/)
        *   [Multi-Document Agents](https://docs.llamaindex.ai/en/stable/examples/agent/multi_document_agents/)
        *   [Build your own OpenAI Agent](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent/)
        *   [Context-Augmented OpenAI Agent](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_context_retrieval/)
        *   [OpenAI Agent Workarounds for Lengthy Tool Descriptions](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_lengthy_tools/)
        *   [Single-Turn Multi-Function Calling OpenAI Agents](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_parallel_function_calling/)
        *   [OpenAI Agent + Query Engine Experimental Cookbook](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_query_cookbook/)
        *   [OpenAI Agent Query Planning](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_query_plan/)
        *   [Retrieval-Augmented OpenAI Agent](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_retrieval/)
        *   [OpenAI Agent with Tool Call Parser](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_tool_call_parser/)
        *   [OpenAI Agent with Query Engine Tools](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_with_query_engine/)
        *   [OpenAI Assistant Agent](https://docs.llamaindex.ai/en/stable/examples/agent/openai_assistant_agent/)
        *   [OpenAI Assistant Advanced Retrieval Cookbook](https://docs.llamaindex.ai/en/stable/examples/agent/openai_assistant_query_cookbook/)
        *   [OpenAI agent: specifying a forced function call](https://docs.llamaindex.ai/en/stable/examples/agent/openai_forced_function_call/)
        *   [Benchmarking OpenAI Retrieval API (through Assistant Agent)](https://docs.llamaindex.ai/en/stable/examples/agent/openai_retrieval_benchmark/)
        *   [ReAct Agent - A Simple Intro with Calculator Tools](https://docs.llamaindex.ai/en/stable/examples/agent/react_agent/)
        *   [ReAct Agent with Query Engine (RAG) Tools](https://docs.llamaindex.ai/en/stable/examples/agent/react_agent_with_query_engine/)
        *   [Controlling Agent Reasoning Loop with Return Direct Tools](https://docs.llamaindex.ai/en/stable/examples/agent/return_direct_agent/)
        *   [Structured Planning Agent](https://docs.llamaindex.ai/en/stable/examples/agent/structured_planner/)
        
    *    Callbacks
        
        Callbacks
        
        *   [Aim Callback](https://docs.llamaindex.ai/en/stable/examples/callbacks/AimCallback/)
        *   [HoneyHive LlamaIndex Tracer](https://docs.llamaindex.ai/en/stable/examples/callbacks/HoneyHiveLlamaIndexTracer/)
        *   [Langfuse Callback Handler](https://docs.llamaindex.ai/en/stable/examples/callbacks/LangfuseCallbackHandler/)
        *   [Llama Debug Handler](https://docs.llamaindex.ai/en/stable/examples/callbacks/LlamaDebugHandler/)
        *   [OpenInference Callback Handler + Arize Phoenix](https://docs.llamaindex.ai/en/stable/examples/callbacks/OpenInferenceCallback/)
        *   [Observability with OpenLLMetry](https://docs.llamaindex.ai/en/stable/examples/callbacks/OpenLLMetry/)
        *   [PromptLayer Handler](https://docs.llamaindex.ai/en/stable/examples/callbacks/PromptLayerHandler/)
        *   [Token Counting Handler](https://docs.llamaindex.ai/en/stable/examples/callbacks/TokenCountingHandler/)
        *   [UpTrain Callback Handler](https://docs.llamaindex.ai/en/stable/examples/callbacks/UpTrainCallback/)
        *   [Wandb Callback Handler](https://docs.llamaindex.ai/en/stable/examples/callbacks/WandbCallbackHandler/)
        
    *    Chat Engines
        
        Chat Engines
        
        *   [Chat Engine - Best Mode](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_best/)
        *   [Chat Engine - Condense Plus Context Mode](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_condense_plus_context/)
        *   [Chat Engine - Condense Question Mode](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_condense_question/)
        *   [Chat Engine - Context Mode](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_context/)
        *   [Chat Engine - OpenAI Agent Mode](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_openai/)
        *   [Chat Engine with a Personality ✨](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_personality/)
        *   [Chat Engine - ReAct Agent Mode](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_react/)
        *   [Chat Engine - Simple Mode REPL](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_repl/)
        
    *    Cookbooks
        
        Cookbooks
        
        *   [Anthropic Haiku Cookbook](https://docs.llamaindex.ai/en/stable/examples/cookbooks/anthropic_haiku/)
        *   [Codestral from MistralAI Cookbook](https://docs.llamaindex.ai/en/stable/examples/cookbooks/codestral/)
        *   [Cohere init8 and binary Embeddings Retrieval Evaluation](https://docs.llamaindex.ai/en/stable/examples/cookbooks/cohere_retriever_eval/)
        *   [CrewAI + LlamaIndex Cookbook](https://docs.llamaindex.ai/en/stable/examples/cookbooks/crewai_llamaindex/)
        *   [Llama3 Cookbook](https://docs.llamaindex.ai/en/stable/examples/cookbooks/llama3_cookbook/)
        *   [Llama3 Cookbook with Groq](https://docs.llamaindex.ai/en/stable/examples/cookbooks/llama3_cookbook_groq/)
        *   [Llama3 Cookbook with Ollama and Replicate](https://docs.llamaindex.ai/en/stable/examples/cookbooks/llama3_cookbook_ollama_replicate/)
        *   [MistralAI Cookbook](https://docs.llamaindex.ai/en/stable/examples/cookbooks/mistralai/)
        *   [mixedbread Rerank Cookbook](https://docs.llamaindex.ai/en/stable/examples/cookbooks/mixedbread_reranker/)
        *   [Prometheus-2 Cookbook](https://docs.llamaindex.ai/en/stable/examples/cookbooks/prometheus2_cookbook/)
        
    *    Customization
        
        Customization
        
        *   [Azure OpenAI](https://docs.llamaindex.ai/en/stable/examples/customization/llms/AzureOpenAI/)
        *   [ChatGPT](https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-ChatGPT/)
        *   [HuggingFace LLM - Camel-5b](https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-Huggingface_camel/)
        *   [HuggingFace LLM - StableLM](https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-Huggingface_stablelm/)
        *   [Chat Prompts Customization](https://docs.llamaindex.ai/en/stable/examples/customization/prompts/chat_prompts/)
        *   [Completion Prompts Customization](https://docs.llamaindex.ai/en/stable/examples/customization/prompts/completion_prompts/)
        *   [Streaming](https://docs.llamaindex.ai/en/stable/examples/customization/streaming/SimpleIndexDemo-streaming/)
        *   [Streaming for Chat Engine - Condense Question Mode](https://docs.llamaindex.ai/en/stable/examples/customization/streaming/chat_engine_condense_question_stream_response/)
        
    *    Data Connectors
        
        Data Connectors
        
        *   [Chroma Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/ChromaDemo/)
        *   [DashVector Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/DashvectorReaderDemo/)
        *   [Database Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/DatabaseReaderDemo/)
        *   [DeepLake Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/DeepLakeReader/)
        *   [Discord Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/DiscordDemo/)
        *   [Faiss Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/FaissDemo/)
        *   [Github Repo Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/GithubRepositoryReaderDemo/)
        *   [Google Chat Reader Test](https://docs.llamaindex.ai/en/stable/examples/data_connectors/GoogleChatDemo/)
        *   [Google Docs Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/GoogleDocsDemo/)
        *   [Google Drive Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/GoogleDriveDemo/)
        *   [Google Maps Text Search Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/GoogleMapsTextSearchReaderDemo/)
        *   [Google Sheets Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/GoogleSheetsDemo/)
        *   [Make Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/MakeDemo/)
        *   [Mbox Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/MboxReaderDemo/)
        *   [MilvusReader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/MilvusReaderDemo/)
        *   [MongoDB Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/MongoDemo/)
        *   [MyScale Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/MyScaleReaderDemo/)
        *   [Notion Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/NotionDemo/)
        *   [Obsidian Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/ObsidianReaderDemo/)
        *   [Pathway Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/PathwayReaderDemo/)
        *   [Pinecone Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/PineconeDemo/)
        *   [Psychic Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/PsychicDemo/)
        *   [Qdrant Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/QdrantDemo/)
        *   [Slack Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/SlackDemo/)
        *   [Twitter Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/TwitterDemo/)
        *   [Weaviate Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WeaviateDemo/)
        *    Web Page Reader [Web Page Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/)
            
            Table of contents
            
            *   [Using SimpleWebPageReader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/#using-simplewebpagereader)
            
        *   [Deplot Reader Demo](https://docs.llamaindex.ai/en/stable/examples/data_connectors/deplot/DeplotReader/)
        *   [HTML Tag Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/html_tag_reader/)
        *   [Simple Directory Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/simple_directory_reader/)
        *   [Parallel Processing SimpleDirectoryReader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/simple_directory_reader_parallel/)
        *   [Simple Directory Reader over a Remote FileSystem](https://docs.llamaindex.ai/en/stable/examples/data_connectors/simple_directory_reader_remote_fs/)
        
    *    Discover LlamaIndex
        
        Discover LlamaIndex
        
        *   [Discord Thread Management](https://docs.llamaindex.ai/en/stable/examples/discover_llamaindex/document_management/Discord_Thread_Management/)
        
    *    Docstores
        
        Docstores
        
        *   [Demo: Azure Table Storage as a Docstore](https://docs.llamaindex.ai/en/stable/examples/docstore/AzureDocstoreDemo/)
        *   [Docstore Demo](https://docs.llamaindex.ai/en/stable/examples/docstore/DocstoreDemo/)
        *   [Dynamo DB Docstore Demo](https://docs.llamaindex.ai/en/stable/examples/docstore/DynamoDBDocstoreDemo/)
        *   [Firestore Demo](https://docs.llamaindex.ai/en/stable/examples/docstore/FirestoreDemo/)
        *   [MongoDB Demo](https://docs.llamaindex.ai/en/stable/examples/docstore/MongoDocstoreDemo/)
        *   [Redis Docstore+Index Store Demo](https://docs.llamaindex.ai/en/stable/examples/docstore/RedisDocstoreIndexStoreDemo/)
        
    *    Embeddings
        
        Embeddings
        
        *   [Anyscale Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/Anyscale/)
        *   [LangChain Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/Langchain/)
        *   [OpenAI Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/OpenAI/)
        *   [Aleph Alpha Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/alephalpha/)
        *   [Bedrock Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/bedrock/)
        *   [Embeddings with Clarifai](https://docs.llamaindex.ai/en/stable/examples/embeddings/clarifai/)
        *   [Cloudflare Workers AI Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/cloudflare_workersai/)
        *   [CohereAI Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/cohereai/)
        *   [Custom Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/custom_embeddings/)
        *   [Dashscope embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/dashscope_embeddings/)
        *   [Databricks Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/databricks/)
        *   [Deepinfra](https://docs.llamaindex.ai/en/stable/examples/embeddings/deepinfra/)
        *   [Elasticsearch Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/elasticsearch/)
        *   [Qdrant FastEmbed Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/fastembed/)
        *   [Fireworks Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/fireworks/)
        *   [Google Gemini Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/gemini/)
        *   [Google PaLM Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/google_palm/)
        *   [Gradient Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/gradient/)
        *   [Local Embeddings with HuggingFace](https://docs.llamaindex.ai/en/stable/examples/embeddings/huggingface/)
        *   [IBM watsonx.ai](https://docs.llamaindex.ai/en/stable/examples/embeddings/ibm_watsonx/)
        *   [Local Embeddings with IPEX-LLM on Intel CPU](https://docs.llamaindex.ai/en/stable/examples/embeddings/ipex_llm/)
        *   [Local Embeddings with IPEX-LLM on Intel GPU](https://docs.llamaindex.ai/en/stable/examples/embeddings/ipex_llm_gpu/)
        *   [Optimized BGE Embedding Model using Intel® Extension for Transformers](https://docs.llamaindex.ai/en/stable/examples/embeddings/itrex/)
        *   [Jina 8K Context Window Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/jina_embeddings/)
        *   [Jina Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/jinaai_embeddings/)
        *   [Llamafile Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/llamafile/)
        *   [LLMRails Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/llm_rails/)
        *   [MistralAI Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/mistralai/)
        *   [Mixedbread AI Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/mixedbreadai/)
        *   [Nomic Embedding](https://docs.llamaindex.ai/en/stable/examples/embeddings/nomic/)
        *   [NVIDIA NIMs](https://docs.llamaindex.ai/en/stable/examples/embeddings/nvidia/)
        *   [Oracle Cloud Infrastructure Generative AI](https://docs.llamaindex.ai/en/stable/examples/embeddings/oci_genai/)
        *   [OctoAI Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/octoai/)
        *   [Ollama Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/ollama_embedding/)
        *   [Local Embeddings with OpenVINO](https://docs.llamaindex.ai/en/stable/examples/embeddings/openvino/)
        *   [Optimized Embedding Model using Optimum-Intel](https://docs.llamaindex.ai/en/stable/examples/embeddings/optimum_intel/)
        *   [PremAI Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/premai/)
        *   [Interacting with Embeddings deployed in Amazon SageMaker Endpoint with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/embeddings/sagemaker_embedding_endpoint/)
        *   [Text Embedding Inference](https://docs.llamaindex.ai/en/stable/examples/embeddings/text_embedding_inference/)
        *   [Together AI Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/together/)
        *   [Upstage Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/upstage/)
        *   [Voyage Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/voyageai/)
        
    *    Evaluation
        
        Evaluation
        
        *   [BEIR Out of Domain Benchmark](https://docs.llamaindex.ai/en/stable/examples/evaluation/BeirEvaluation/)
        *   [🚀 RAG/LLM Evaluators - DeepEval](https://docs.llamaindex.ai/en/stable/examples/evaluation/Deepeval/)
        *   [HotpotQADistractor Demo](https://docs.llamaindex.ai/en/stable/examples/evaluation/HotpotQADistractor/)
        *   [QuestionGeneration](https://docs.llamaindex.ai/en/stable/examples/evaluation/QuestionGeneration/)
        *   [Self Correcting Query Engines - Evaluation & Retry](https://docs.llamaindex.ai/en/stable/examples/evaluation/RetryQuery/)
        *   [Tonic Validate Evaluators](https://docs.llamaindex.ai/en/stable/examples/evaluation/TonicValidateEvaluators/)
        *   [How to use UpTrain with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/evaluation/UpTrain/)
        *   [Answer Relevancy and Context Relevancy Evaluations](https://docs.llamaindex.ai/en/stable/examples/evaluation/answer_and_context_relevancy/)
        *   [BatchEvalRunner - Running Multiple Evaluations](https://docs.llamaindex.ai/en/stable/examples/evaluation/batch_eval/)
        *   [Correctness Evaluator](https://docs.llamaindex.ai/en/stable/examples/evaluation/correctness_eval/)
        *   [Faithfulness Evaluator](https://docs.llamaindex.ai/en/stable/examples/evaluation/faithfulness_eval/)
        *   [Guideline Evaluator](https://docs.llamaindex.ai/en/stable/examples/evaluation/guideline_eval/)
        *   [Benchmarking LLM Evaluators On The MT-Bench Human Judgement LabelledPairwiseEvaluatorDataset](https://docs.llamaindex.ai/en/stable/examples/evaluation/mt_bench_human_judgement/)
        *   [Benchmarking LLM Evaluators On A Mini MT-Bench (Single Grading) LabelledEvaluatorDataset](https://docs.llamaindex.ai/en/stable/examples/evaluation/mt_bench_single_grading/)
        *   [Evaluating Multi-Modal RAG](https://docs.llamaindex.ai/en/stable/examples/evaluation/multi_modal/multi_modal_rag_evaluation/)
        *   [Pairwise Evaluator](https://docs.llamaindex.ai/en/stable/examples/evaluation/pairwise_eval/)
        *   [Evaluation using Prometheus model](https://docs.llamaindex.ai/en/stable/examples/evaluation/prometheus_evaluation/)
        *   [Relevancy Evaluator](https://docs.llamaindex.ai/en/stable/examples/evaluation/relevancy_eval/)
        *   [Retrieval Evaluation](https://docs.llamaindex.ai/en/stable/examples/evaluation/retrieval/retriever_eval/)
        *   [Embedding Similarity Evaluator](https://docs.llamaindex.ai/en/stable/examples/evaluation/semantic_similarity_eval/)
        
    *    Finetuning
        
        Finetuning
        
        *   [How to Finetune a cross-encoder using LLamaIndex](https://docs.llamaindex.ai/en/stable/examples/finetuning/cross_encoder_finetuning/cross_encoder_finetuning/)
        *   [Finetune Embeddings](https://docs.llamaindex.ai/en/stable/examples/finetuning/embeddings/finetune_embedding/)
        *   [Finetuning an Adapter on Top of any Black-Box Embedding Model](https://docs.llamaindex.ai/en/stable/examples/finetuning/embeddings/finetune_embedding_adapter/)
        *   [Fine Tuning Nous-Hermes-2 With Gradient and LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/finetuning/gradient/gradient_fine_tuning/)
        *   [Fine Tuning Llama2 for Better Structured Outputs With Gradient and LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/finetuning/gradient/gradient_structured/)
        *   [Fine Tuning for Text-to-SQL With Gradient and LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/finetuning/gradient/gradient_text2sql/)
        *   [Knowledge Distillation For Fine-Tuning A GPT-3.5 Judge (Correctness)](https://docs.llamaindex.ai/en/stable/examples/finetuning/llm_judge/correctness/finetune_llm_judge_single_grading_correctness/)
        *   [Knowledge Distillation For Fine-Tuning A GPT-3.5 Judge (Pairwise)](https://docs.llamaindex.ai/en/stable/examples/finetuning/llm_judge/pairwise/finetune_llm_judge/)
        *   [Fine Tuning MistralAI models using Finetuning API](https://docs.llamaindex.ai/en/stable/examples/finetuning/mistralai_fine_tuning/)
        *   [Fine Tuning GPT-3.5-Turbo](https://docs.llamaindex.ai/en/stable/examples/finetuning/openai_fine_tuning/)
        *   [Fine Tuning with Function Calling](https://docs.llamaindex.ai/en/stable/examples/finetuning/openai_fine_tuning_functions/)
        *   [Fine-tuning a gpt-3.5 ReAct Agent on Better Chain of Thought](https://docs.llamaindex.ai/en/stable/examples/finetuning/react_agent/react_agent_finetune/)
        *   [Custom Cohere Reranker](https://docs.llamaindex.ai/en/stable/examples/finetuning/rerankers/cohere_custom_reranker/)
        *   [Router Fine-tuning](https://docs.llamaindex.ai/en/stable/examples/finetuning/router/router_finetune/)
        
    *    Ingestion
        
        Ingestion
        
        *   [Advanced Ingestion Pipeline](https://docs.llamaindex.ai/en/stable/examples/ingestion/advanced_ingestion_pipeline/)
        *   [Async Ingestion Pipeline + Metadata Extraction](https://docs.llamaindex.ai/en/stable/examples/ingestion/async_ingestion_pipeline/)
        *   [Ingestion Pipeline + Document Management](https://docs.llamaindex.ai/en/stable/examples/ingestion/document_management_pipeline/)
        *   [Building a Live RAG Pipeline over Google Drive Files](https://docs.llamaindex.ai/en/stable/examples/ingestion/ingestion_gdrive/)
        *   [Parallelizing Ingestion Pipeline](https://docs.llamaindex.ai/en/stable/examples/ingestion/parallel_execution_ingestion_pipeline/)
        *   [Redis Ingestion Pipeline](https://docs.llamaindex.ai/en/stable/examples/ingestion/redis_ingestion_pipeline/)
        
    *    LLMs
        
        LLMs
        
        *   [AI21](https://docs.llamaindex.ai/en/stable/examples/llm/ai21/)
        *   [Aleph Alpha](https://docs.llamaindex.ai/en/stable/examples/llm/alephalpha/)
        *   [Anthropic](https://docs.llamaindex.ai/en/stable/examples/llm/anthropic/)
        *   [Anyscale](https://docs.llamaindex.ai/en/stable/examples/llm/anyscale/)
        *   [Azure OpenAI](https://docs.llamaindex.ai/en/stable/examples/llm/azure_openai/)
        *   [Bedrock](https://docs.llamaindex.ai/en/stable/examples/llm/bedrock/)
        *   [Bedrock Converse](https://docs.llamaindex.ai/en/stable/examples/llm/bedrock_converse/)
        *   [Clarifai LLM](https://docs.llamaindex.ai/en/stable/examples/llm/clarifai/)
        *   [Cleanlab Trustworthy Language Model](https://docs.llamaindex.ai/en/stable/examples/llm/cleanlab/)
        *   [Cohere](https://docs.llamaindex.ai/en/stable/examples/llm/cohere/)
        *   [DashScope LLMS](https://docs.llamaindex.ai/en/stable/examples/llm/dashscope/)
        *   [DataBricks](https://docs.llamaindex.ai/en/stable/examples/llm/databricks/)
        *   [DeepInfra](https://docs.llamaindex.ai/en/stable/examples/llm/deepinfra/)
        *   [EverlyAI](https://docs.llamaindex.ai/en/stable/examples/llm/everlyai/)
        *   [Fireworks](https://docs.llamaindex.ai/en/stable/examples/llm/fireworks/)
        *   [Fireworks Function Calling Cookbook](https://docs.llamaindex.ai/en/stable/examples/llm/fireworks_cookbook/)
        *   [Friendli](https://docs.llamaindex.ai/en/stable/examples/llm/friendli/)
        *   [Gemini](https://docs.llamaindex.ai/en/stable/examples/llm/gemini/)
        *   [Gradient Base Model](https://docs.llamaindex.ai/en/stable/examples/llm/gradient_base_model/)
        *   [Gradient Model Adapter](https://docs.llamaindex.ai/en/stable/examples/llm/gradient_model_adapter/)
        *   [Groq](https://docs.llamaindex.ai/en/stable/examples/llm/groq/)
        *   [Hugging Face LLMs](https://docs.llamaindex.ai/en/stable/examples/llm/huggingface/)
        *   [IBM watsonx.ai](https://docs.llamaindex.ai/en/stable/examples/llm/ibm_watsonx/)
        *   [IPEX-LLM on Intel CPU](https://docs.llamaindex.ai/en/stable/examples/llm/ipex_llm/)
        *   [IPEX-LLM on Intel GPU](https://docs.llamaindex.ai/en/stable/examples/llm/ipex_llm_gpu/)
        *   [Konko](https://docs.llamaindex.ai/en/stable/examples/llm/konko/)
        *   [Langchain](https://docs.llamaindex.ai/en/stable/examples/llm/langchain/)
        *   [LiteLLM](https://docs.llamaindex.ai/en/stable/examples/llm/litellm/)
        *   [Replicate - Llama 2 13B](https://docs.llamaindex.ai/en/stable/examples/llm/llama_2/)
        *   [LlamaCPP](https://docs.llamaindex.ai/en/stable/examples/llm/llama_2_llama_cpp/)
        *   [🦙 x 🦙 Rap Battle](https://docs.llamaindex.ai/en/stable/examples/llm/llama_2_rap_battle/)
        *   [Llama API](https://docs.llamaindex.ai/en/stable/examples/llm/llama_api/)
        *   [llamafile](https://docs.llamaindex.ai/en/stable/examples/llm/llamafile/)
        *   [LLM Predictor](https://docs.llamaindex.ai/en/stable/examples/llm/llm_predictor/)
        *   [LM Studio](https://docs.llamaindex.ai/en/stable/examples/llm/lmstudio/)
        *   [LocalAI](https://docs.llamaindex.ai/en/stable/examples/llm/localai/)
        *   [Maritalk](https://docs.llamaindex.ai/en/stable/examples/llm/maritalk/)
        *   [MistralRS LLM](https://docs.llamaindex.ai/en/stable/examples/llm/mistral_rs/)
        *   [MistralAI](https://docs.llamaindex.ai/en/stable/examples/llm/mistralai/)
        *   [None](https://docs.llamaindex.ai/en/stable/examples/llm/mlx.ipynb)
        *   [ModelScope LLMS](https://docs.llamaindex.ai/en/stable/examples/llm/modelscope/)
        *   [Monster API <> LLamaIndex](https://docs.llamaindex.ai/en/stable/examples/llm/monsterapi/)
        *   [MyMagic AI LLM](https://docs.llamaindex.ai/en/stable/examples/llm/mymagic/)
        *   [Neutrino AI](https://docs.llamaindex.ai/en/stable/examples/llm/neutrino/)
        *   [NVIDIA NIMs](https://docs.llamaindex.ai/en/stable/examples/llm/nvidia/)
        *   [NVIDIA NIMs](https://docs.llamaindex.ai/en/stable/examples/llm/nvidia_nim/)
        *   [Nvidia TensorRT-LLM](https://docs.llamaindex.ai/en/stable/examples/llm/nvidia_tensorrt/)
        *   [Nvidia Triton](https://docs.llamaindex.ai/en/stable/examples/llm/nvidia_triton/)
        *   [Oracle Cloud Infrastructure Generative AI](https://docs.llamaindex.ai/en/stable/examples/llm/oci_genai/)
        *   [OctoAI](https://docs.llamaindex.ai/en/stable/examples/llm/octoai/)
        *   [Ollama - Llama 3](https://docs.llamaindex.ai/en/stable/examples/llm/ollama/)
        *   [Ollama - Gemma](https://docs.llamaindex.ai/en/stable/examples/llm/ollama_gemma/)
        *   [OpenAI](https://docs.llamaindex.ai/en/stable/examples/llm/openai/)
        *   [OpenAI JSON Mode vs. Function Calling for Data Extraction](https://docs.llamaindex.ai/en/stable/examples/llm/openai_json_vs_function_calling/)
        *   [OpenLLM](https://docs.llamaindex.ai/en/stable/examples/llm/openllm/)
        *   [OpenRouter](https://docs.llamaindex.ai/en/stable/examples/llm/openrouter/)
        *   [OpenVINO LLMs](https://docs.llamaindex.ai/en/stable/examples/llm/openvino/)
        *   [Optimum Intel LLMs optimized with IPEX backend](https://docs.llamaindex.ai/en/stable/examples/llm/optimum_intel/)
        *   [PaLM](https://docs.llamaindex.ai/en/stable/examples/llm/palm/)
        *   [Perplexity](https://docs.llamaindex.ai/en/stable/examples/llm/perplexity/)
        *   [Portkey](https://docs.llamaindex.ai/en/stable/examples/llm/portkey/)
        *   [Predibase](https://docs.llamaindex.ai/en/stable/examples/llm/predibase/)
        *   [PremAI LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/llm/premai/)
        *   [Client of Baidu Intelligent Cloud's Qianfan LLM Platform](https://docs.llamaindex.ai/en/stable/examples/llm/qianfan/)
        *   [RunGPT](https://docs.llamaindex.ai/en/stable/examples/llm/rungpt/)
        *   [Interacting with LLM deployed in Amazon SageMaker Endpoint with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/llm/sagemaker_endpoint_llm/)
        *   [Solar LLM](https://docs.llamaindex.ai/en/stable/examples/llm/solar/)
        *   [Together AI LLM](https://docs.llamaindex.ai/en/stable/examples/llm/together/)
        *   [Unify](https://docs.llamaindex.ai/en/stable/examples/llm/unify/)
        *   [Upstage](https://docs.llamaindex.ai/en/stable/examples/llm/upstage/)
        *   [Vertex AI](https://docs.llamaindex.ai/en/stable/examples/llm/vertex/)
        *   [Replicate - Vicuna 13B](https://docs.llamaindex.ai/en/stable/examples/llm/vicuna/)
        *   [vLLM](https://docs.llamaindex.ai/en/stable/examples/llm/vllm/)
        *   [Xorbits Inference](https://docs.llamaindex.ai/en/stable/examples/llm/xinference_local_deployment/)
        *   [Yi](https://docs.llamaindex.ai/en/stable/examples/llm/yi/)
        
    *    Llama Datasets
        
        Llama Datasets
        
        *   [Downloading a LlamaDataset from LlamaHub](https://docs.llamaindex.ai/en/stable/examples/llama_dataset/downloading_llama_datasets/)
        *   [Benchmarking RAG Pipelines With A LabelledRagDatatset](https://docs.llamaindex.ai/en/stable/examples/llama_dataset/labelled-rag-datasets/)
        *   [LlamaDataset Submission Template Notebook](https://docs.llamaindex.ai/en/stable/examples/llama_dataset/ragdataset_submission_template/)
        *   [Contributing a LlamaDataset To LlamaHub](https://docs.llamaindex.ai/en/stable/examples/llama_dataset/uploading_llama_dataset/)
        
    *    Llama Hub
        
        Llama Hub
        
        *   [LlamaHub Demostration](https://docs.llamaindex.ai/en/stable/examples/llama_hub/llama_hub/)
        *   [Ollama Llama Pack Example](https://docs.llamaindex.ai/en/stable/examples/llama_hub/llama_pack_ollama/)
        *   [Llama Pack - Resume Screener 📄](https://docs.llamaindex.ai/en/stable/examples/llama_hub/llama_pack_resume/)
        *   [Llama Packs Example](https://docs.llamaindex.ai/en/stable/examples/llama_hub/llama_packs_example/)
        
    *    Low Level
        
        Low Level
        
        *   [Building Evaluation from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/evaluation/)
        *   [Building an Advanced Fusion Retriever from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/fusion_retriever/)
        *   [Building Data Ingestion from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/ingestion/)
        *   [Building RAG from Scratch (Open-source only!)](https://docs.llamaindex.ai/en/stable/examples/low_level/oss_ingestion_retrieval/)
        *   [Building Response Synthesis from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/response_synthesis/)
        *   [Building Retrieval from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/retrieval/)
        *   [Building a Router from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/router/)
        *   [Building a (Very Simple) Vector Store from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/vector_store/)
        
    *    Managed Indexes
        
        Managed Indexes
        
        *   [Google Generative Language Semantic Retriever](https://docs.llamaindex.ai/en/stable/examples/managed/GoogleDemo/)
        *   [PostgresML Managed Index](https://docs.llamaindex.ai/en/stable/examples/managed/PostgresMLDemo/)
        *   [Google Cloud LlamaIndex on Vertex AI for RAG](https://docs.llamaindex.ai/en/stable/examples/managed/VertexAIDemo/)
        *   [Semantic Retriever Benchmark](https://docs.llamaindex.ai/en/stable/examples/managed/manage_retrieval_benchmark/)
        *   [Vectara Managed Index](https://docs.llamaindex.ai/en/stable/examples/managed/vectaraDemo/)
        *   [Managed Index with Zilliz Cloud Pipelines](https://docs.llamaindex.ai/en/stable/examples/managed/zcpDemo/)
        
    *    Metadata Extractors
        
        Metadata Extractors
        
        *   [Entity Metadata Extraction](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/EntityExtractionClimate/)
        *   [Metadata Extraction and Augmentation w/ Marvin](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MarvinMetadataExtractorDemo/)
        *   [Extracting Metadata for Better Document Indexing and Understanding](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MetadataExtractionSEC/)
        *   [Automated Metadata Extraction for Better Retrieval + Synthesis](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MetadataExtraction_LLMSurvey/)
        *   [Pydantic Extractor](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/PydanticExtractor/)
        
    *    Multi-Modal
        
        Multi-Modal
        
        *   [Chroma Multi-Modal Demo with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/multi_modal/ChromaMultiModalDemo/)
        *   [Multi-Modal LLM using Anthropic model for image reasoning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/anthropic_multi_modal/)
        *   [Multi-Modal LLM using Azure OpenAI GPT-4V model for image reasoning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/azure_openai_multi_modal/)
        *   [Multi-Modal LLM using DashScope qwen-vl model for image reasoning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/dashscope_multi_modal/)
        *   [Multi-Modal LLM using Google's Gemini model for image understanding and build Retrieval Augmented Generation with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gemini/)
        *   [Multimodal Structured Outputs: GPT-4o vs. Other GPT-4 Variants](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gpt4o_mm_structured_outputs/)
        *   [GPT4-V Experiments with General, Specific questions and Chain Of Thought (COT) Prompting Technique.](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gpt4v_experiments_cot/)
        *   [Advanced Multi-Modal Retrieval using GPT4V and Multi-Modal Index/Retriever](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gpt4v_multi_modal_retrieval/)
        *   [Image to Image Retrieval using CLIP embedding and image correlation reasoning using GPT4V](https://docs.llamaindex.ai/en/stable/examples/multi_modal/image_to_image_retrieval/)
        *   [LlaVa Demo with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/multi_modal/llava_demo/)
        *   [Retrieval-Augmented Image Captioning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/llava_multi_modal_tesla_10q/)
        *   [\[Beta\] Multi-modal ReAct Agent](https://docs.llamaindex.ai/en/stable/examples/multi_modal/mm_agent/)
        *   [Multi-Modal GPT4V Pydantic Program](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_pydantic/)
        *   [Multi-Modal RAG using Nomic Embed and Anthropic.](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_rag_nomic/)
        *   [Multi-Modal Retrieval using GPT text embedding and CLIP image embedding for Wikipedia Articles](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_retrieval/)
        *   [Multimodal RAG for processing videos using OpenAI GPT4V and LanceDB vectorstore](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_video_RAG/)
        *   [Multimodal Ollama Cookbook](https://docs.llamaindex.ai/en/stable/examples/multi_modal/ollama_cookbook/)
        *   [Multi-Modal LLM using OpenAI GPT-4V model for image reasoning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/openai_multi_modal/)
        *   [Multi-Modal LLM using Replicate LlaVa, Fuyu 8B, MiniGPT4 models for image reasoning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/replicate_multi_modal/)
        *   [Semi-structured Image Retrieval](https://docs.llamaindex.ai/en/stable/examples/multi_modal/structured_image_retrieval/)
        
    *    Multi-Tenancy
        
        Multi-Tenancy
        
        *   [Multi-Tenancy RAG with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/multi_tenancy/multi_tenancy_rag/)
        
    *    Node Parsers & Text Splitters
        
        Node Parsers & Text Splitters
        
        *   [Semantic Chunker](https://docs.llamaindex.ai/en/stable/examples/node_parsers/semantic_chunking/)
        *   [Semantic double merging chunking](https://docs.llamaindex.ai/en/stable/examples/node_parsers/semantic_double_merging_chunking/)
        
    *    Node Postprocessors
        
        Node Postprocessors
        
        *   [Cohere Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/CohereRerank/)
        *   [Colbert Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/ColbertRerank/)
        *   [File Based Node Parsers](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/FileNodeProcessors/)
        *   [FlagEmbeddingReranker](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/FlagEmbeddingReranker/)
        *   [Jina Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/JinaRerank/)
        *   [LLM Reranker Demonstration (Great Gatsby)](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/LLMReranker-Gatsby/)
        *   [LLM Reranker Demonstration (2021 Lyft 10-k)](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/LLMReranker-Lyft-10k/)
        *   [LongContextReorder](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/LongContextReorder/)
        *   [Metadata Replacement + Node Sentence Window](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/MetadataReplacementDemo/)
        *   [Mixedbread AI Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/MixedbreadAIRerank/)
        *   [NVIDIA NIMs](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/NVIDIARerank/)
        *   [Sentence Embedding OptimizerThis postprocessor optimizes token usage by removing sentences that are not relevant to the query (this is done using embeddings).The percentile cutoff is a measure for using the top percentage of relevant sentences. The threshold cutoff can be specified instead, which uses a raw similarity cutoff for picking which sentences to keep.](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/OptimizerDemo/)
        *   [PII Masking](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/PII/)
        *   [Forward/Backward Augmentation](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/PrevNextPostprocessorDemo/)
        *   [Recency Filtering](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/RecencyPostprocessorDemo/)
        *   [SentenceTransformerRerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/SentenceTransformerRerank/)
        *   [Time-Weighted Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/TimeWeightedPostprocessorDemo/)
        *   [VoyageAI Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/VoyageAIRerank/)
        *   [OpenVINO Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/openvino_rerank/)
        *   [RankGPT Reranker Demonstration (Van Gogh Wiki)](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/rankGPT/)
        *   [RankLLM Reranker Demonstration (Van Gogh Wiki)](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/rankLLM/)
        
    *    Object Stores
        
        Object Stores
        
        *   [The ObjectIndex Class](https://docs.llamaindex.ai/en/stable/examples/objects/object_index/)
        
    *    Output Parsers
        
        Output Parsers
        
        *   [Guardrails Output Parsing](https://docs.llamaindex.ai/en/stable/examples/output_parsing/GuardrailsDemo/)
        *   [Langchain Output Parsing](https://docs.llamaindex.ai/en/stable/examples/output_parsing/LangchainOutputParserDemo/)
        *   [DataFrame Structured Data Extraction](https://docs.llamaindex.ai/en/stable/examples/output_parsing/df_program/)
        *   [Evaporate Demo](https://docs.llamaindex.ai/en/stable/examples/output_parsing/evaporate_program/)
        *   [Function Calling Program for Structured Extraction](https://docs.llamaindex.ai/en/stable/examples/output_parsing/function_program/)
        *   [Guidance Pydantic Program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/guidance_pydantic_program/)
        *   [Guidance for Sub-Question Query Engine](https://docs.llamaindex.ai/en/stable/examples/output_parsing/guidance_sub_question/)
        *   [LLM Pydantic Program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/llm_program/)
        *   [LM Format Enforcer Pydantic Program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/lmformatenforcer_pydantic_program/)
        *   [LM Format Enforcer Regular Expression Generation](https://docs.llamaindex.ai/en/stable/examples/output_parsing/lmformatenforcer_regular_expressions/)
        *   [OpenAI Pydantic Program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/openai_pydantic_program/)
        *   [OpenAI function calling for Sub-Question Query Engine](https://docs.llamaindex.ai/en/stable/examples/output_parsing/openai_sub_question/)
        
    *    Param Optimizer
        
        Param Optimizer
        
        *   [\[WIP\] Hyperparameter Optimization for RAG](https://docs.llamaindex.ai/en/stable/examples/param_optimizer/param_optimizer/)
        
    *    Prompts
        
        Prompts
        
        *   [Advanced Prompt Techniques (Variable Mappings, Functions)](https://docs.llamaindex.ai/en/stable/examples/prompts/advanced_prompts/)
        *   [EmotionPrompt in RAG](https://docs.llamaindex.ai/en/stable/examples/prompts/emotion_prompt/)
        *   [Accessing/Customizing Prompts within Higher-Level Modules](https://docs.llamaindex.ai/en/stable/examples/prompts/prompt_mixin/)
        *   ["Optimization by Prompting" for RAG](https://docs.llamaindex.ai/en/stable/examples/prompts/prompt_optimization/)
        *   [Prompt Engineering for RAG](https://docs.llamaindex.ai/en/stable/examples/prompts/prompts_rag/)
        
    *    Property Graph
        
        Property Graph
        
        *   [Using a Property Graph Store](https://docs.llamaindex.ai/en/stable/examples/property_graph/graph_store/)
        *   [Property Graph Construction with Predefined Schemas](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_advanced/)
        *   [Property Graph Index](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_basic/)
        *   [Defining a Custom Property Graph Retriever](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_custom_retriever/)
        *   [Neo4j Property Graph Index](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_neo4j/)
        
    *    Query Engines
        
        Query Engines
        
        *   [Retriever Query Engine with Custom Retrievers - Simple Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/query_engine/CustomRetrievers/)
        *   [JSONalyze Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/JSONalyze_query_engine/)
        *   [Joint QA Summary Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/JointQASummary/)
        *   [Retriever Router Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/RetrieverRouterQueryEngine/)
        *   [Router Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/RouterQueryEngine/)
        *   [SQL Auto Vector Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLAutoVectorQueryEngine/)
        *   [SQL Join Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLJoinQueryEngine/)
        *   [SQL Router Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLRouterQueryEngine/)
        *   [CitationQueryEngine](https://docs.llamaindex.ai/en/stable/examples/query_engine/citation_query_engine/)
        *   [Cogniswitch query engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/cogniswitch_query_engine/)
        *   [Defining a Custom Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/custom_query_engine/)
        *   [Ensemble Query Engine Guide](https://docs.llamaindex.ai/en/stable/examples/query_engine/ensemble_query_engine/)
        *   [FLARE Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/flare_query_engine/)
        *   [JSON Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/json_query_engine/)
        *   [Knowledge Graph Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/knowledge_graph_query_engine/)
        *   [Knowledge Graph RAG Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/knowledge_graph_rag_query_engine/)
        *   [Structured Hierarchical Retrieval](https://docs.llamaindex.ai/en/stable/examples/query_engine/multi_doc_auto_retrieval/multi_doc_auto_retrieval/)
        *   [Pandas Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/pandas_query_engine/)
        *   [Recursive Retriever + Query Engine Demo](https://docs.llamaindex.ai/en/stable/examples/query_engine/pdf_tables/recursive_retriever/)
        *   [\[Beta\] Text-to-SQL with PGVector](https://docs.llamaindex.ai/en/stable/examples/query_engine/pgvector_sql_query_engine/)
        *   [Query Engine with Pydantic Outputs](https://docs.llamaindex.ai/en/stable/examples/query_engine/pydantic_query_engine/)
        *   [Recursive Retriever + Document Agents](https://docs.llamaindex.ai/en/stable/examples/query_engine/recursive_retriever_agents/)
        *   [Joint Tabular/Semantic QA over Tesla 10K](https://docs.llamaindex.ai/en/stable/examples/query_engine/sec_tables/tesla_10q_table/)
        *   [Sub Question Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/sub_question_query_engine/)
        
    *    Query Pipeline
        
        Query Pipeline
        
        *   [An Introduction to LlamaIndex Query Pipelines](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/)
        *   [Query Pipeline with Async/Parallel Execution](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_async/)
        *   [Query Pipeline Chat Engine](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_memory/)
        *   [Query Pipeline over Pandas DataFrames](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_pandas/)
        *   [Query Pipeline with Routing](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_routing/)
        *   [Query Pipeline for Advanced Text-to-SQL](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_sql/)
        
    *    Query Transformations
        
        Query Transformations
        
        *   [HyDE Query Transform](https://docs.llamaindex.ai/en/stable/examples/query_transformations/HyDEQueryTransformDemo/)
        *   [Multi-Step Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_transformations/SimpleIndexDemo-multistep/)
        *   [Query Transform Cookbook](https://docs.llamaindex.ai/en/stable/examples/query_transformations/query_transform_cookbook/)
        
    *    Response Synthesizers
        
        Response Synthesizers
        
        *   [Pydantic Tree Summarize](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/custom_prompt_synthesizer/)
        *   [Stress-Testing Long Context LLMs with a Recall Task](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/long_context_test/)
        *   [Pydantic Tree Summarize](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/pydantic_tree_summarize/)
        *   [Refine](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/refine/)
        *   [Refine with Structured Answer Filtering](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/structured_refine/)
        *   [Tree Summarize](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/tree_summarize/)
        
    *    Retrievers
        
        Retrievers
        
        *   [Auto Merging Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/auto_merging_retriever/)
        *   [Comparing Methods for Structured Retrieval (Auto-Retrieval vs. Recursive Retrieval)](https://docs.llamaindex.ai/en/stable/examples/retrievers/auto_vs_recursive_retriever/)
        *   [Bedrock (Knowledge Bases)](https://docs.llamaindex.ai/en/stable/examples/retrievers/bedrock_retriever/)
        *   [BM25 Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/bm25_retriever/)
        *   [Composable Objects](https://docs.llamaindex.ai/en/stable/examples/retrievers/composable_retrievers/)
        *   [Activeloop Deep Memory](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/)
        *   [Ensemble Retrieval Guide](https://docs.llamaindex.ai/en/stable/examples/retrievers/ensemble_retrieval/)
        *   [Chunk + Document Hybrid Retrieval with Long-Context Embeddings (Together.ai)](https://docs.llamaindex.ai/en/stable/examples/retrievers/multi_doc_together_hybrid/)
        *   [Pathway Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/pathway_retriever/)
        *   [Reciprocal Rerank Fusion Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/reciprocal_rerank_fusion/)
        *   [Recursive Retriever + Node References + Braintrust](https://docs.llamaindex.ai/en/stable/examples/retrievers/recurisve_retriever_nodes_braintrust/)
        *   [Recursive Retriever + Node References](https://docs.llamaindex.ai/en/stable/examples/retrievers/recursive_retriever_nodes/)
        *   [Relative Score Fusion and Distribution-Based Score Fusion](https://docs.llamaindex.ai/en/stable/examples/retrievers/relative_score_dist_fusion/)
        *   [Router Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/router_retriever/)
        *   [Simple Fusion Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/simple_fusion/)
        *   [Auto-Retrieval from a Vectara Index](https://docs.llamaindex.ai/en/stable/examples/retrievers/vectara_auto_retriever/)
        *   [VideoDB Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/videodb_retriever/)
        *   [You.com Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/you_retriever/)
        
    *    Tools
        
        Tools
        
        *   [OnDemandLoaderTool Tutorial](https://docs.llamaindex.ai/en/stable/examples/tools/OnDemandLoaderTool/)
        *   [Azure Code Interpreter Tool Spec](https://docs.llamaindex.ai/en/stable/examples/tools/azure_code_interpreter/)
        *   [Cassandra Database Tools](https://docs.llamaindex.ai/en/stable/examples/tools/cassandra/)
        *   [Evaluation Query Engine Tool](https://docs.llamaindex.ai/en/stable/examples/tools/eval_query_engine_tool/)
        
    *    Transforms
        
        Transforms
        
        *   [Transforms Evaluation](https://docs.llamaindex.ai/en/stable/examples/transforms/TransformsEval/)
        
    *    Use Cases
        
        Use Cases
        
        *   [10K Analysis](https://docs.llamaindex.ai/en/stable/examples/usecases/10k_sub_question/)
        *   [10Q Analysis](https://docs.llamaindex.ai/en/stable/examples/usecases/10q_sub_question/)
        *   [Email Data Extraction](https://docs.llamaindex.ai/en/stable/examples/usecases/email_data_extraction/)
        *   [Github Issue Analysis](https://docs.llamaindex.ai/en/stable/examples/usecases/github_issue_analysis/)
        
    *    Vector Stores
        
        Vector Stores
        
        *   [AWSDocDBDemo](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AWSDocDBDemo/)
        *   [Alibaba Cloud OpenSearch Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AlibabaCloudOpenSearchIndexDemo/)
        *   [Amazon Neptune - Neptune Analytics vector store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AmazonNeptuneVectorDemo/)
        *   [AnalyticDB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AnalyticDBDemo/)
        *   [Astra DB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AstraDBIndexDemo/)
        *   [Simple Vector Store - Async Index Creation](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AsyncIndexCreationDemo/)
        *   [Awadb Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AwadbDemo/)
        *   [Azure AI Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureAISearchIndexDemo/)
        *   [Azure CosmosDB MongoDB Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureCosmosDBMongoDBvCoreDemo/)
        *   [Bagel Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BagelAutoRetriever/)
        *   [Bagel Network](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BagelIndexDemo/)
        *   [Baidu VectorDB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BaiduVectorDBIndexDemo/)
        *   [Cassandra Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/CassandraIndexDemo/)
        *   [Chroma + Fireworks + Nomic with Matryoshka embedding](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ChromaFireworksNomic/)
        *   [Chroma](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ChromaIndexDemo/)
        *   [ClickHouse Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ClickHouseIndexDemo/)
        *   [CouchbaseVectorStoreDemo](https://docs.llamaindex.ai/en/stable/examples/vector_stores/CouchbaseVectorStoreDemo/)
        *   [DashVector Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DashvectorIndexDemo/)
        *   [Databricks Vector Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DatabricksVectorSearchDemo/)
        *   [Deep Lake Vector Store Quickstart](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DeepLakeIndexDemo/)
        *   [DocArray Hnsw Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DocArrayHnswIndexDemo/)
        *   [DocArray InMemory Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DocArrayInMemoryIndexDemo/)
        *   [DuckDB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DuckDBDemo/)
        *   [Elasticsearch Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ElasticsearchIndexDemo/)
        *   [Elasticsearch](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Elasticsearch_demo/)
        *   [Epsilla Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/EpsillaIndexDemo/)
        *   [Faiss Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/FaissIndexDemo/)
        *   [Firestore Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/FirestoreVectorStore/)
        *   [Hologres](https://docs.llamaindex.ai/en/stable/examples/vector_stores/HologresDemo/)
        *   [Jaguar Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/JaguarIndexDemo/)
        *   [Advanced RAG with temporal filters using LlamaIndex and KDB.AI vector store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/KDBAI_Advanced_RAG_Demo/)
        *   [LanceDB Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanceDBIndexDemo/)
        *   [Lantern Vector Store (auto-retriever)](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanternAutoRetriever/)
        *   [Lantern Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanternIndexDemo/)
        *   [Metal Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MetalIndexDemo/)
        *   [Milvus Vector Store With Hybrid Retrieval](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusHybridIndexDemo/)
        *   [Milvus Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusIndexDemo/)
        *   [MilvusOperatorFunctionDemo](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusOperatorFunctionDemo/)
        *   [MongoDBAtlasVectorSearch](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MongoDBAtlasVectorSearch/)
        *   [now make sure you create the search index with the right name here](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MongoDBAtlasVectorSearchRAGFireworks/)
        *   [MongoDBAtlasVectorSearchRAGOpenAI](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MongoDBAtlasVectorSearchRAGOpenAI/)
        *   [MyScale Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MyScaleIndexDemo/)
        *   [Neo4j vector store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Neo4jVectorDemo/)
        *   [Opensearch Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/OpensearchDemo/)
        *   [pgvecto.rs](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PGVectoRsDemo/)
        *   [Pinecone Vector Store - Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PineconeIndexDemo-Hybrid/)
        *   [Pinecone Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PineconeIndexDemo/)
        *   [Qdrant Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/QdrantIndexDemo/)
        *   [Qdrant Vector Store - Metadata Filter](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Qdrant_metadata_filter/)
        *   [Qdrant Vector Store - Default Qdrant Filters](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Qdrant_using_qdrant_filters/)
        *   [Redis Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RedisIndexDemo/)
        *   [Relyt](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RelytDemo/)
        *   [Rockset Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RocksetIndexDemo/)
        *   [Simple Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemo/)
        *   [Local Llama2 + VectorStoreIndex](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemoLlama-Local/)
        *   [Llama2 + VectorStoreIndex](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemoLlama2/)
        *   [Simple Vector Stores - Maximum Marginal Relevance Retrieval](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemoMMR/)
        *   [S3/R2 Storage](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexOnS3/)
        *   [Supabase Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SupabaseVectorIndexDemo/)
        *   [Tair Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TairIndexDemo/)
        *   [Tencent Cloud VectorDB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TencentVectorDBIndexDemo/)
        *   [TiDB Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TiDBVector/)
        *   [Timescale Vector Store (PostgreSQL)](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Timescalevector/)
        *   [txtai Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TxtaiIndexDemo/)
        *   [Typesense Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TypesenseDemo/)
        *   [Upstash Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/UpstashVectorDemo/)
        *   [VearchDemo](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VearchDemo/)
        *   [Google Vertex AI Vector Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VertexAIVectorSearchDemo/)
        *   [Vespa Vector Store demo](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VespaIndexDemo/)
        *   [Weaviate Vector Store - Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo-Hybrid/)
        *   [Weaviate Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo/)
        *   [Auto-Retrieval from a Weaviate Vector Database](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndex_auto_retriever/)
        *   [Weaviate Vector Store Metadata Filter](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndex_metadata_filter/)
        *   [Zep Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ZepIndexDemo/)
        *   [Auto-Retrieval from a Vector Database](https://docs.llamaindex.ai/en/stable/examples/vector_stores/chroma_auto_retriever/)
        *   [Chroma Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/chroma_metadata_filter/)
        *   [Auto-Retrieval from a Vector Database](https://docs.llamaindex.ai/en/stable/examples/vector_stores/elasticsearch_auto_retriever/)
        *   [Guide: Using Vector Store Index with Existing Pinecone Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/existing_data/pinecone_existing_data/)
        *   [Guide: Using Vector Store Index with Existing Weaviate Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/existing_data/weaviate_existing_data/)
        *   [Neo4j Vector Store - Metadata Filter](https://docs.llamaindex.ai/en/stable/examples/vector_stores/neo4j_metadata_filter/)
        *   [A Simple to Advanced Guide with Auto-Retrieval (with Pinecone + Arize Phoenix)](https://docs.llamaindex.ai/en/stable/examples/vector_stores/pinecone_auto_retriever/)
        *   [Pinecone Vector Store - Metadata Filter](https://docs.llamaindex.ai/en/stable/examples/vector_stores/pinecone_metadata_filter/)
        *   [Postgres Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/postgres/)
        *   [Hybrid Search with Qdrant BM42](https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_bm42/)
        *   [Qdrant Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_hybrid/)
        
    
*   [Component Guides](https://docs.llamaindex.ai/en/stable/module_guides/)
    
    Component Guides
    
    *   [Models](https://docs.llamaindex.ai/en/stable/module_guides/models/)
        
        Models
        
        *    LLMs
            
            LLMs
            
            *   [Using LLMs](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/)
            *   [Standalone Usage](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/usage_standalone/)
            *   [Customizing LLMs](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/usage_custom/)
            *   [Available LLM Integrations](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/modules/)
            
        *   [Embeddings](https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings/)
        *   [Multi Modal](https://docs.llamaindex.ai/en/stable/module_guides/models/multi_modal/)
        
    *   [Prompts](https://docs.llamaindex.ai/en/stable/module_guides/models/prompts/)
        
        Prompts
        
        *   [Usage pattern](https://docs.llamaindex.ai/en/stable/module_guides/models/prompts/usage_pattern/)
        
    *   [Loading](https://docs.llamaindex.ai/en/stable/module_guides/loading/)
        
        Loading
        
        *   [Documents and Nodes](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/)
            
            Documents and Nodes
            
            *   [Using Documents](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_documents/)
            *   [Using Nodes](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_nodes/)
            *   [Metadata Extraction](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_metadata_extractor/)
            
        *   [SimpleDirectoryReader](https://docs.llamaindex.ai/en/stable/module_guides/loading/simpledirectoryreader/)
        *   [Data Connectors](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/)
            
            Data Connectors
            
            *   [Usage Pattern](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/usage_pattern/)
            *   [LlamaParse](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/llama_parse/)
            *   [Module Guides](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/modules/)
            
        *   [Node Parsers / Text Splitters](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/)
            
            Node Parsers / Text Splitters
            
            *   [Node Parser Modules](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/)
            
        *   [Ingestion Pipeline](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/)
            
            Ingestion Pipeline
            
            *   [Transformations](https://docs.llamaindex.ai/en/stable/module_guides/loading/ingestion_pipeline/transformations/)
            
        
    *   [Indexing](https://docs.llamaindex.ai/en/stable/module_guides/indexing/)
        
        Indexing
        
        *   [Index Guide](https://docs.llamaindex.ai/en/stable/module_guides/indexing/index_guide/)
        *   [Vector Store Index](https://docs.llamaindex.ai/en/stable/module_guides/indexing/vector_store_index/)
        *   [Property Graph Index](https://docs.llamaindex.ai/en/stable/module_guides/indexing/lpg_index_guide/)
        *   [Document Management](https://docs.llamaindex.ai/en/stable/module_guides/indexing/document_management/)
        *   [LlamaCloud](https://docs.llamaindex.ai/en/stable/module_guides/indexing/llama_cloud_index/)
        *   [Metadata Extraction](https://docs.llamaindex.ai/en/stable/module_guides/indexing/metadata_extraction/)
        *   [Modules](https://docs.llamaindex.ai/en/stable/module_guides/indexing/modules/)
        
    *   [Storing](https://docs.llamaindex.ai/en/stable/module_guides/storing/)
        
        Storing
        
        *   [Vector Stores](https://docs.llamaindex.ai/en/stable/module_guides/storing/vector_stores/)
        *   [Document Stores](https://docs.llamaindex.ai/en/stable/module_guides/storing/docstores/)
        *   [Index Stores](https://docs.llamaindex.ai/en/stable/module_guides/storing/index_stores/)
        *   [Chat Stores](https://docs.llamaindex.ai/en/stable/module_guides/storing/chat_stores/)
        *   [Key-Value Stores](https://docs.llamaindex.ai/en/stable/module_guides/storing/kv_stores/)
        *   [Persisting & Loading Data](https://docs.llamaindex.ai/en/stable/module_guides/storing/save_load/)
        *   [Customizing Storage](https://docs.llamaindex.ai/en/stable/module_guides/storing/customization/)
        
    *   [Querying](https://docs.llamaindex.ai/en/stable/module_guides/querying/)
        
        Querying
        
        *   [Query Engines](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/)
            
            Query Engines
            
            *   [Usage Pattern](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/usage_pattern/)
            *   [Response Modes](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/response_modes/)
            *   [Streaming](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/streaming/)
            *   [Module Guides](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/modules/)
            *   [Supporting Modules](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/supporting_modules/)
            
        *   [Chat Engines](https://docs.llamaindex.ai/en/stable/module_guides/deploying/chat_engines/)
            
            Chat Engines
            
            *   [Usage Pattern](https://docs.llamaindex.ai/en/stable/module_guides/deploying/chat_engines/usage_pattern/)
            *   [Module Guides](https://docs.llamaindex.ai/en/stable/module_guides/deploying/chat_engines/modules/)
            
        *   [Retrieval](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/)
            
            Retrieval
            
            *   [Retriever Modules](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retrievers/)
            *   [Retriever Modes](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retriever_modes/)
            
        *   [Node Postprocessors](https://docs.llamaindex.ai/en/stable/module_guides/querying/node_postprocessors/)
            
            Node Postprocessors
            
            *   [Node Postprocessor Modules](https://docs.llamaindex.ai/en/stable/module_guides/querying/node_postprocessors/node_postprocessors/)
            
        *   [Response Synthesis](https://docs.llamaindex.ai/en/stable/module_guides/querying/response_synthesizers/)
            
            Response Synthesis
            
            *   [Response Synthesis Modules](https://docs.llamaindex.ai/en/stable/module_guides/querying/response_synthesizers/response_synthesizers/)
            
        *   [Routing](https://docs.llamaindex.ai/en/stable/module_guides/querying/router/)
        *   [Query Pipelines](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/)
            
            Query Pipelines
            
            *   [Usage Pattern](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/usage_pattern/)
            *   [Module Guides](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/modules/)
            *   [Module Usage](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/module_usage/)
            
        *   [Structured Outputs](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/)
            
            Structured Outputs
            
            *   [Output Parsing Modules](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/output_parser/)
            *   [Query Engines + Pydantic Outputs](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/query_engine/)
            *   [Pydantic Program](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/pydantic_program/)
            
        
    *   [Agents](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/)
        
        Agents
        
        *   [Usage Pattern](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/usage_pattern/)
        *   [Lower-Level Agent API](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/agent_runner/)
        *   [Module Guides](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/modules/)
        *   [Tools](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/)
        
    *   [Evaluation](https://docs.llamaindex.ai/en/stable/module_guides/evaluating/)
        
        Evaluation
        
        *   [Usage Pattern (Response Evaluation)](https://docs.llamaindex.ai/en/stable/module_guides/evaluating/usage_pattern/)
        *   [Usage Pattern (Retrieval)](https://docs.llamaindex.ai/en/stable/module_guides/evaluating/usage_pattern_retrieval/)
        *   [Modules](https://docs.llamaindex.ai/en/stable/module_guides/evaluating/modules/)
        *    LlamaDatasets
            
            LlamaDatasets
            
            *   [Contributing A LabelledRagDataset](https://docs.llamaindex.ai/en/stable/module_guides/evaluating/contributing_llamadatasets/)
            *   [Evaluating With LabelledRagDataset's](https://docs.llamaindex.ai/en/stable/module_guides/evaluating/evaluating_with_llamadatasets/)
            *   [Evaluating Evaluators with LabelledEvaluatorDataset's](https://docs.llamaindex.ai/en/stable/module_guides/evaluating/evaluating_evaluators_with_llamadatasets/)
            
        
    *   [Observability](https://docs.llamaindex.ai/en/stable/module_guides/observability/)
        
        Observability
        
        *   [Instrumentation](https://docs.llamaindex.ai/en/stable/module_guides/observability/instrumentation/)
        
    *   [Settings](https://docs.llamaindex.ai/en/stable/module_guides/supporting_modules/settings/)
    
*    Advanced Topics
    
    Advanced Topics
    
    *   [Building Performant RAG Applications for Production](https://docs.llamaindex.ai/en/stable/optimizing/production_rag/)
    *   [Basic Strategies](https://docs.llamaindex.ai/en/stable/optimizing/basic_strategies/basic_strategies/)
    *   [Agentic strategies](https://docs.llamaindex.ai/en/stable/optimizing/agentic_strategies/agentic_strategies/)
    *    Retrieval
        
        Retrieval
        
        *   [Advanced Retrieval Strategies](https://docs.llamaindex.ai/en/stable/optimizing/advanced_retrieval/advanced_retrieval/)
        *   [Query Transformations](https://docs.llamaindex.ai/en/stable/optimizing/advanced_retrieval/query_transformations/)
        
    *    Evaluation
        
        Evaluation
        
        *   [Component Wise Evaluation](https://docs.llamaindex.ai/en/stable/optimizing/evaluation/component_wise_evaluation/)
        *   [End-to-End Evaluation](https://docs.llamaindex.ai/en/stable/optimizing/evaluation/e2e_evaluation/)
        *   [Evaluation](https://docs.llamaindex.ai/en/stable/optimizing/evaluation/evaluation/)
        
    *   [Fine-Tuning](https://docs.llamaindex.ai/en/stable/optimizing/fine-tuning/fine-tuning/)
    *   [Writing Custom Modules](https://docs.llamaindex.ai/en/stable/optimizing/custom_modules/)
    *   [Building RAG from Scratch (Lower-Level)](https://docs.llamaindex.ai/en/stable/optimizing/building_rag_from_scratch/)
    
*   [API Reference](https://docs.llamaindex.ai/en/stable/api_reference/)
    
    API Reference
    
    *   [Agents](https://docs.llamaindex.ai/en/stable/api_reference/agent/)
        
        Agents
        
        *   [Coa](https://docs.llamaindex.ai/en/stable/api_reference/agent/coa/)
        *   [Dashscope](https://docs.llamaindex.ai/en/stable/api_reference/agent/dashscope/)
        *   [Introspective](https://docs.llamaindex.ai/en/stable/api_reference/agent/introspective/)
        *   [Lats](https://docs.llamaindex.ai/en/stable/api_reference/agent/lats/)
        *   [Llm compiler](https://docs.llamaindex.ai/en/stable/api_reference/agent/llm_compiler/)
        *   [Openai](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai/)
        *   [Openai legacy](https://docs.llamaindex.ai/en/stable/api_reference/agent/openai_legacy/)
        *   [React](https://docs.llamaindex.ai/en/stable/api_reference/agent/react/)
        
    *   [Callbacks](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/)
        
        Callbacks
        
        *   [Agentops](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/agentops/)
        *   [Aim](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/aim/)
        *   [Argilla](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/argilla/)
        *   [Arize phoenix](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/arize_phoenix/)
        *   [Deepeval](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/deepeval/)
        *   [Honeyhive](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/honeyhive/)
        *   [Langfuse](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/langfuse/)
        *   [Llama debug](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/llama_debug/)
        *   [Openinference](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/openinference/)
        *   [Promptlayer](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/promptlayer/)
        *   [Token counter](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/token_counter/)
        *   [Uptrain](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/uptrain/)
        *   [Wandb](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/wandb/)
        
    *   [Chat Engines](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/)
        
        Chat Engines
        
        *   [Condense plus context](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/condense_plus_context/)
        *   [Condense question](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/condense_question/)
        *   [Context](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/context/)
        *   [Simple](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/simple/)
        
    *   [Embeddings](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/)
        
        Embeddings
        
        *   [Adapter](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/adapter/)
        *   [Alephalpha](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/alephalpha/)
        *   [Anyscale](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/anyscale/)
        *   [Azure openai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/azure_openai/)
        *   [Bedrock](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/bedrock/)
        *   [Clarifai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/clarifai/)
        *   [Clip](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/clip/)
        *   [Cloudflare workersai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/cloudflare_workersai/)
        *   [Cohere](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/cohere/)
        *   [Dashscope](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/dashscope/)
        *   [Databricks](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/databricks/)
        *   [Deepinfra](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/deepinfra/)
        *   [Elasticsearch](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/elasticsearch/)
        *   [Fastembed](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/fastembed/)
        *   [Fireworks](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/fireworks/)
        *   [Gemini](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/gemini/)
        *   [Google](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/google/)
        *   [Gradient](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/gradient/)
        *   [Huggingface](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/huggingface/)
        *   [Huggingface api](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/huggingface_api/)
        *   [Huggingface itrex](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/huggingface_itrex/)
        *   [Huggingface openvino](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/huggingface_openvino/)
        *   [Huggingface optimum](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/huggingface_optimum/)
        *   [Huggingface optimum intel](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/huggingface_optimum_intel/)
        *   [Ibm](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/ibm/)
        *   [Instructor](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/instructor/)
        *   [Ipex llm](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/ipex_llm/)
        *   [Jinaai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/jinaai/)
        *   [Langchain](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/langchain/)
        *   [Litellm](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/litellm/)
        *   [Llamafile](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/llamafile/)
        *   [Llm rails](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/llm_rails/)
        *   [Mistralai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/mistralai/)
        *   [Mixedbreadai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/mixedbreadai/)
        *   [Nomic](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/nomic/)
        *   [Nvidia](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/nvidia/)
        *   [Oci genai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/oci_genai/)
        *   [Octoai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/octoai/)
        *   [Ollama](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/ollama/)
        *   [Openai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/openai/)
        *   [Premai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/premai/)
        *   [Sagemaker endpoint](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/sagemaker_endpoint/)
        *   [Text embeddings inference](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/text_embeddings_inference/)
        *   [Together](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/together/)
        *   [Upstage](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/upstage/)
        *   [Vertex](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/vertex/)
        *   [Voyageai](https://docs.llamaindex.ai/en/stable/api_reference/embeddings/voyageai/)
        
    *   [Evaluation](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/)
        
        Evaluation
        
        *   [Answer relevancy](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/answer_relevancy/)
        *   [Context relevancy](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/context_relevancy/)
        *   [Correctness](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/correctness/)
        *   [Dataset generation](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/dataset_generation/)
        *   [Faithfullness](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/faithfullness/)
        *   [Guideline](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/guideline/)
        *   [Metrics](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/metrics/)
        *   [Multi modal](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/multi_modal/)
        *   [Pairwise comparison](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/pairwise_comparison/)
        *   [Query response](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/query_response/)
        *   [Response](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/response/)
        *   [Retrieval](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/retrieval/)
        *   [Semantic similarity](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/semantic_similarity/)
        *   [Tonic validate](https://docs.llamaindex.ai/en/stable/api_reference/evaluation/tonic_validate/)
        
    *   [Indexes](https://docs.llamaindex.ai/en/stable/api_reference/indices/)
        
        Indexes
        
        *   [Colbert](https://docs.llamaindex.ai/en/stable/api_reference/indices/colbert/)
        *   [Dashscope](https://docs.llamaindex.ai/en/stable/api_reference/indices/dashscope/)
        *   [Document summary](https://docs.llamaindex.ai/en/stable/api_reference/indices/document_summary/)
        *   [Google](https://docs.llamaindex.ai/en/stable/api_reference/indices/google/)
        *   [Keyword](https://docs.llamaindex.ai/en/stable/api_reference/indices/keyword/)
        *   [Knowledge graph](https://docs.llamaindex.ai/en/stable/api_reference/indices/knowledge_graph/)
        *   [Llama cloud](https://docs.llamaindex.ai/en/stable/api_reference/indices/llama_cloud/)
        *   [Postgresml](https://docs.llamaindex.ai/en/stable/api_reference/indices/postgresml/)
        *   [Property graph](https://docs.llamaindex.ai/en/stable/api_reference/indices/property_graph/)
        *   [Summary](https://docs.llamaindex.ai/en/stable/api_reference/indices/summary/)
        *   [Tree](https://docs.llamaindex.ai/en/stable/api_reference/indices/tree/)
        *   [Vectara](https://docs.llamaindex.ai/en/stable/api_reference/indices/vectara/)
        *   [Vector](https://docs.llamaindex.ai/en/stable/api_reference/indices/vector/)
        *   [Vertexai](https://docs.llamaindex.ai/en/stable/api_reference/indices/vertexai/)
        *   [Zilliz](https://docs.llamaindex.ai/en/stable/api_reference/indices/zilliz/)
        
    *   [Ingestion](https://docs.llamaindex.ai/en/stable/api_reference/ingestion/)
        
        Ingestion
        
    *   [Instrumentation](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/)
        
        Instrumentation
        
        *   [Event handlers](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_handlers/)
        *   [Event types](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/event_types/)
        *   [Span handlers](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/span_handlers/)
        *   [Span types](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/span_types/)
        
    *   [LLMs](https://docs.llamaindex.ai/en/stable/api_reference/llms/)
        
        LLMs
        
        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/llms/OptimumIntelLLM.md)
        *   [Ai21](https://docs.llamaindex.ai/en/stable/api_reference/llms/ai21/)
        *   [Alephalpha](https://docs.llamaindex.ai/en/stable/api_reference/llms/alephalpha/)
        *   [Anthropic](https://docs.llamaindex.ai/en/stable/api_reference/llms/anthropic/)
        *   [Anyscale](https://docs.llamaindex.ai/en/stable/api_reference/llms/anyscale/)
        *   [Azure openai](https://docs.llamaindex.ai/en/stable/api_reference/llms/azure_openai/)
        *   [Bedrock](https://docs.llamaindex.ai/en/stable/api_reference/llms/bedrock/)
        *   [Bedrock converse](https://docs.llamaindex.ai/en/stable/api_reference/llms/bedrock_converse/)
        *   [Clarifai](https://docs.llamaindex.ai/en/stable/api_reference/llms/clarifai/)
        *   [Cleanlab](https://docs.llamaindex.ai/en/stable/api_reference/llms/cleanlab/)
        *   [Cohere](https://docs.llamaindex.ai/en/stable/api_reference/llms/cohere/)
        *   [Custom llm](https://docs.llamaindex.ai/en/stable/api_reference/llms/custom_llm/)
        *   [Dashscope](https://docs.llamaindex.ai/en/stable/api_reference/llms/dashscope/)
        *   [Databricks](https://docs.llamaindex.ai/en/stable/api_reference/llms/databricks/)
        *   [Deepinfra](https://docs.llamaindex.ai/en/stable/api_reference/llms/deepinfra/)
        *   [Everlyai](https://docs.llamaindex.ai/en/stable/api_reference/llms/everlyai/)
        *   [Fireworks](https://docs.llamaindex.ai/en/stable/api_reference/llms/fireworks/)
        *   [Friendli](https://docs.llamaindex.ai/en/stable/api_reference/llms/friendli/)
        *   [Gemini](https://docs.llamaindex.ai/en/stable/api_reference/llms/gemini/)
        *   [Gradient](https://docs.llamaindex.ai/en/stable/api_reference/llms/gradient/)
        *   [Groq](https://docs.llamaindex.ai/en/stable/api_reference/llms/groq/)
        *   [Huggingface](https://docs.llamaindex.ai/en/stable/api_reference/llms/huggingface/)
        *   [Huggingface api](https://docs.llamaindex.ai/en/stable/api_reference/llms/huggingface_api/)
        *   [Ibm](https://docs.llamaindex.ai/en/stable/api_reference/llms/ibm/)
        *   [Ipex llm](https://docs.llamaindex.ai/en/stable/api_reference/llms/ipex_llm/)
        *   [Konko](https://docs.llamaindex.ai/en/stable/api_reference/llms/konko/)
        *   [Langchain](https://docs.llamaindex.ai/en/stable/api_reference/llms/langchain/)
        *   [Litellm](https://docs.llamaindex.ai/en/stable/api_reference/llms/litellm/)
        *   [Llama api](https://docs.llamaindex.ai/en/stable/api_reference/llms/llama_api/)
        *   [Llama cpp](https://docs.llamaindex.ai/en/stable/api_reference/llms/llama_cpp/)
        *   [Llamafile](https://docs.llamaindex.ai/en/stable/api_reference/llms/llamafile/)
        *   [Lmstudio](https://docs.llamaindex.ai/en/stable/api_reference/llms/lmstudio/)
        *   [Localai](https://docs.llamaindex.ai/en/stable/api_reference/llms/localai/)
        *   [Maritalk](https://docs.llamaindex.ai/en/stable/api_reference/llms/maritalk/)
        *   [Mistral rs](https://docs.llamaindex.ai/en/stable/api_reference/llms/mistral_rs/)
        *   [Mistralai](https://docs.llamaindex.ai/en/stable/api_reference/llms/mistralai/)
        *   [Mlx](https://docs.llamaindex.ai/en/stable/api_reference/llms/mlx/)
        *   [Modelscope](https://docs.llamaindex.ai/en/stable/api_reference/llms/modelscope/)
        *   [Monsterapi](https://docs.llamaindex.ai/en/stable/api_reference/llms/monsterapi/)
        *   [Mymagic](https://docs.llamaindex.ai/en/stable/api_reference/llms/mymagic/)
        *   [Neutrino](https://docs.llamaindex.ai/en/stable/api_reference/llms/neutrino/)
        *   [Nvidia](https://docs.llamaindex.ai/en/stable/api_reference/llms/nvidia/)
        *   [Nvidia tensorrt](https://docs.llamaindex.ai/en/stable/api_reference/llms/nvidia_tensorrt/)
        *   [Nvidia triton](https://docs.llamaindex.ai/en/stable/api_reference/llms/nvidia_triton/)
        *   [Oci genai](https://docs.llamaindex.ai/en/stable/api_reference/llms/oci_genai/)
        *   [Octoai](https://docs.llamaindex.ai/en/stable/api_reference/llms/octoai/)
        *   [Ollama](https://docs.llamaindex.ai/en/stable/api_reference/llms/ollama/)
        *   [Openai](https://docs.llamaindex.ai/en/stable/api_reference/llms/openai/)
        *   [Openai like](https://docs.llamaindex.ai/en/stable/api_reference/llms/openai_like/)
        *   [Openllm](https://docs.llamaindex.ai/en/stable/api_reference/llms/openllm/)
        *   [Openrouter](https://docs.llamaindex.ai/en/stable/api_reference/llms/openrouter/)
        *   [Openvino](https://docs.llamaindex.ai/en/stable/api_reference/llms/openvino/)
        *   [Optimum intel](https://docs.llamaindex.ai/en/stable/api_reference/llms/optimum_intel/)
        *   [Palm](https://docs.llamaindex.ai/en/stable/api_reference/llms/palm/)
        *   [Perplexity](https://docs.llamaindex.ai/en/stable/api_reference/llms/perplexity/)
        *   [Portkey](https://docs.llamaindex.ai/en/stable/api_reference/llms/portkey/)
        *   [Predibase](https://docs.llamaindex.ai/en/stable/api_reference/llms/predibase/)
        *   [Premai](https://docs.llamaindex.ai/en/stable/api_reference/llms/premai/)
        *   [Qianfan](https://docs.llamaindex.ai/en/stable/api_reference/llms/qianfan/)
        *   [Replicate](https://docs.llamaindex.ai/en/stable/api_reference/llms/replicate/)
        *   [Rungpt](https://docs.llamaindex.ai/en/stable/api_reference/llms/rungpt/)
        *   [Sagemaker endpoint](https://docs.llamaindex.ai/en/stable/api_reference/llms/sagemaker_endpoint/)
        *   [Solar](https://docs.llamaindex.ai/en/stable/api_reference/llms/solar/)
        *   [Text generation inference](https://docs.llamaindex.ai/en/stable/api_reference/llms/text_generation_inference/)
        *   [Together](https://docs.llamaindex.ai/en/stable/api_reference/llms/together/)
        *   [Unify](https://docs.llamaindex.ai/en/stable/api_reference/llms/unify/)
        *   [Upstage](https://docs.llamaindex.ai/en/stable/api_reference/llms/upstage/)
        *   [Vertex](https://docs.llamaindex.ai/en/stable/api_reference/llms/vertex/)
        *   [Vllm](https://docs.llamaindex.ai/en/stable/api_reference/llms/vllm/)
        *   [Xinference](https://docs.llamaindex.ai/en/stable/api_reference/llms/xinference/)
        *   [Yi](https://docs.llamaindex.ai/en/stable/api_reference/llms/yi/)
        *   [You](https://docs.llamaindex.ai/en/stable/api_reference/llms/you/)
        
    *   [Llama Datasets](https://docs.llamaindex.ai/en/stable/api_reference/llama_dataset/)
        
        Llama Datasets
        
    *   [Llama Packs](https://docs.llamaindex.ai/en/stable/api_reference/packs/)
        
        Llama Packs
        
        *   [Agent search retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/agent_search_retriever/)
        *   [Agents coa](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_coa/)
        *   [Agents lats](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_lats/)
        *   [Agents llm compiler](https://docs.llamaindex.ai/en/stable/api_reference/packs/agents_llm_compiler/)
        *   [Amazon product extraction](https://docs.llamaindex.ai/en/stable/api_reference/packs/amazon_product_extraction/)
        *   [Arize phoenix query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/arize_phoenix_query_engine/)
        *   [Auto merging retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/auto_merging_retriever/)
        *   [Chroma autoretrieval](https://docs.llamaindex.ai/en/stable/api_reference/packs/chroma_autoretrieval/)
        *   [Code hierarchy](https://docs.llamaindex.ai/en/stable/api_reference/packs/code_hierarchy/)
        *   [Cogniswitch agent](https://docs.llamaindex.ai/en/stable/api_reference/packs/cogniswitch_agent/)
        *   [Cohere citation chat](https://docs.llamaindex.ai/en/stable/api_reference/packs/cohere_citation_chat/)
        *   [Corrective rag](https://docs.llamaindex.ai/en/stable/api_reference/packs/corrective_rag/)
        *   [Deeplake deepmemory retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/deeplake_deepmemory_retriever/)
        *   [Deeplake multimodal retrieval](https://docs.llamaindex.ai/en/stable/api_reference/packs/deeplake_multimodal_retrieval/)
        *   [Dense x retrieval](https://docs.llamaindex.ai/en/stable/api_reference/packs/dense_x_retrieval/)
        *   [Diff private simple dataset](https://docs.llamaindex.ai/en/stable/api_reference/packs/diff_private_simple_dataset/)
        *   [Docugami kg rag](https://docs.llamaindex.ai/en/stable/api_reference/packs/docugami_kg_rag/)
        *   [Evaluator benchmarker](https://docs.llamaindex.ai/en/stable/api_reference/packs/evaluator_benchmarker/)
        *   [Finchat](https://docs.llamaindex.ai/en/stable/api_reference/packs/finchat/)
        *   [Fusion retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/fusion_retriever/)
        *   [Fuzzy citation](https://docs.llamaindex.ai/en/stable/api_reference/packs/fuzzy_citation/)
        *   [Gmail openai agent](https://docs.llamaindex.ai/en/stable/api_reference/packs/gmail_openai_agent/)
        *   [Gradio agent chat](https://docs.llamaindex.ai/en/stable/api_reference/packs/gradio_agent_chat/)
        *   [Gradio react agent chatbot](https://docs.llamaindex.ai/en/stable/api_reference/packs/gradio_react_agent_chatbot/)
        *   [Infer retrieve rerank](https://docs.llamaindex.ai/en/stable/api_reference/packs/infer_retrieve_rerank/)
        *   [Koda retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/koda_retriever/)
        *   [Llama dataset metadata](https://docs.llamaindex.ai/en/stable/api_reference/packs/llama_dataset_metadata/)
        *   [Llama guard moderator](https://docs.llamaindex.ai/en/stable/api_reference/packs/llama_guard_moderator/)
        *   [Llava completion](https://docs.llamaindex.ai/en/stable/api_reference/packs/llava_completion/)
        *   [Mixture of agents](https://docs.llamaindex.ai/en/stable/api_reference/packs/mixture_of_agents/)
        *   [Multi document agents](https://docs.llamaindex.ai/en/stable/api_reference/packs/multi_document_agents/)
        *   [Multi tenancy rag](https://docs.llamaindex.ai/en/stable/api_reference/packs/multi_tenancy_rag/)
        *   [Multidoc autoretrieval](https://docs.llamaindex.ai/en/stable/api_reference/packs/multidoc_autoretrieval/)
        *   [Nebulagraph query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/nebulagraph_query_engine/)
        *   [Neo4j query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/neo4j_query_engine/)
        *   [Node parser semantic chunking](https://docs.llamaindex.ai/en/stable/api_reference/packs/node_parser_semantic_chunking/)
        *   [Ollama query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/ollama_query_engine/)
        *   [Panel chatbot](https://docs.llamaindex.ai/en/stable/api_reference/packs/panel_chatbot/)
        *   [Query understanding agent](https://docs.llamaindex.ai/en/stable/api_reference/packs/query_understanding_agent/)
        *   [Raft dataset](https://docs.llamaindex.ai/en/stable/api_reference/packs/raft_dataset/)
        *   [Rag cli local](https://docs.llamaindex.ai/en/stable/api_reference/packs/rag_cli_local/)
        *   [Rag evaluator](https://docs.llamaindex.ai/en/stable/api_reference/packs/rag_evaluator/)
        *   [Rag fusion query pipeline](https://docs.llamaindex.ai/en/stable/api_reference/packs/rag_fusion_query_pipeline/)
        *   [Ragatouille retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/ragatouille_retriever/)
        *   [Raptor](https://docs.llamaindex.ai/en/stable/api_reference/packs/raptor/)
        *   [Recursive retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/recursive_retriever/)
        *   [Redis ingestion pipeline](https://docs.llamaindex.ai/en/stable/api_reference/packs/redis_ingestion_pipeline/)
        *   [Resume screener](https://docs.llamaindex.ai/en/stable/api_reference/packs/resume_screener/)
        *   [Retry engine weaviate](https://docs.llamaindex.ai/en/stable/api_reference/packs/retry_engine_weaviate/)
        *   [Searchain](https://docs.llamaindex.ai/en/stable/api_reference/packs/searchain/)
        *   [Secgpt](https://docs.llamaindex.ai/en/stable/api_reference/packs/secgpt/)
        *   [Self discover](https://docs.llamaindex.ai/en/stable/api_reference/packs/self_discover/)
        *   [Self rag](https://docs.llamaindex.ai/en/stable/api_reference/packs/self_rag/)
        *   [Sentence window retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/sentence_window_retriever/)
        *   [Snowflake query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/snowflake_query_engine/)
        *   [Stock market data query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/stock_market_data_query_engine/)
        *   [Streamlit chatbot](https://docs.llamaindex.ai/en/stable/api_reference/packs/streamlit_chatbot/)
        *   [Sub question weaviate](https://docs.llamaindex.ai/en/stable/api_reference/packs/sub_question_weaviate/)
        *   [Subdoc summary](https://docs.llamaindex.ai/en/stable/api_reference/packs/subdoc_summary/)
        *   [Tables](https://docs.llamaindex.ai/en/stable/api_reference/packs/tables/)
        *   [Timescale vector autoretrieval](https://docs.llamaindex.ai/en/stable/api_reference/packs/timescale_vector_autoretrieval/)
        *   [Trulens eval packs](https://docs.llamaindex.ai/en/stable/api_reference/packs/trulens_eval_packs/)
        *   [Vanna](https://docs.llamaindex.ai/en/stable/api_reference/packs/vanna/)
        *   [Vectara rag](https://docs.llamaindex.ai/en/stable/api_reference/packs/vectara_rag/)
        *   [Voyage query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/voyage_query_engine/)
        *   [Zenguard](https://docs.llamaindex.ai/en/stable/api_reference/packs/zenguard/)
        *   [Zephyr query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/zephyr_query_engine/)
        
    *   [Memory](https://docs.llamaindex.ai/en/stable/api_reference/memory/)
        
        Memory
        
        *   [Chat memory buffer](https://docs.llamaindex.ai/en/stable/api_reference/memory/chat_memory_buffer/)
        *   [Simple composable memory](https://docs.llamaindex.ai/en/stable/api_reference/memory/simple_composable_memory/)
        *   [Vector memory](https://docs.llamaindex.ai/en/stable/api_reference/memory/vector_memory/)
        
    *   [Metadata Extractors](https://docs.llamaindex.ai/en/stable/api_reference/extractors/)
        
        Metadata Extractors
        
        *   [Entity](https://docs.llamaindex.ai/en/stable/api_reference/extractors/entity/)
        *   [Keyword](https://docs.llamaindex.ai/en/stable/api_reference/extractors/keyword/)
        *   [Marvin](https://docs.llamaindex.ai/en/stable/api_reference/extractors/marvin/)
        *   [Pydantic](https://docs.llamaindex.ai/en/stable/api_reference/extractors/pydantic/)
        *   [Question](https://docs.llamaindex.ai/en/stable/api_reference/extractors/question/)
        *   [Summary](https://docs.llamaindex.ai/en/stable/api_reference/extractors/summary/)
        *   [Title](https://docs.llamaindex.ai/en/stable/api_reference/extractors/title/)
        
    *   [Multi-Modal LLMs](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/)
        
        Multi-Modal LLMs
        
        *   [Anthropic](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/anthropic/)
        *   [Azure openai](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/azure_openai/)
        *   [Dashscope](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/dashscope/)
        *   [Gemini](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/gemini/)
        *   [Ollama](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/ollama/)
        *   [Openai](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/openai/)
        *   [Replicate](https://docs.llamaindex.ai/en/stable/api_reference/multi_modal_llms/replicate/)
        
    *   [Node Parsers & Text Splitters](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/)
        
        Node Parsers & Text Splitters
        
        *   [Dashscope](https://docs.llamaindex.ai/en/stable/api_reference/node_parser/dashscope/)
        *   [Code](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/code/)
        *   [Hierarchical](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/hierarchical/)
        *   [Html](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/html/)
        *   [Json](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/json/)
        *   [Langchain](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/langchain/)
        *   [Markdown](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/markdown/)
        *   [Markdown element](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/markdown_element/)
        *   [Semantic splitter](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/semantic_splitter/)
        *   [Sentence splitter](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/sentence_splitter/)
        *   [Sentence window](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/sentence_window/)
        *   [Token text splitter](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/token_text_splitter/)
        *   [Unstructured element](https://docs.llamaindex.ai/en/stable/api_reference/node_parsers/unstructured_element/)
        
    *   [Node Postprocessors](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/)
        
        Node Postprocessors
        
        *   [NER PII](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/NER_PII/)
        *   [PII](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/PII/)
        *   [Auto prev next](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/auto_prev_next/)
        *   [Cohere rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/cohere_rerank/)
        *   [Colbert rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/colbert_rerank/)
        *   [Dashscope rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/dashscope_rerank/)
        *   [Embedding recency](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/embedding_recency/)
        *   [Fixed recency](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/fixed_recency/)
        *   [Flag embedding reranker](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/flag_embedding_reranker/)
        *   [Jinaai rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/jinaai_rerank/)
        *   [Keyword](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/keyword/)
        *   [Llm rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/llm_rerank/)
        *   [Long context reorder](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/long_context_reorder/)
        *   [Longllmlingua](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/longllmlingua/)
        *   [Metadata replacement](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/metadata_replacement/)
        *   [Mixedbreadai rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/mixedbreadai_rerank/)
        *   [Nvidia rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/nvidia_rerank/)
        *   [Openvino rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/openvino_rerank/)
        *   [Presidio](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/presidio/)
        *   [Prev next](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/prev_next/)
        *   [Rankgpt rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/rankgpt_rerank/)
        *   [Rankllm rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/rankllm_rerank/)
        *   [Sbert rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/sbert_rerank/)
        *   [Sentence optimizer](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/sentence_optimizer/)
        *   [Similarity](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/similarity/)
        *   [Time weighted](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/time_weighted/)
        *   [Voyageai rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/voyageai_rerank/)
        
    *   [Object Stores](https://docs.llamaindex.ai/en/stable/api_reference/objects/)
        
        Object Stores
        
    *   [Output Parsers](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/)
        
        Output Parsers
        
        *   [Guardrails](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/guardrails/)
        *   [Langchain](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/langchain/)
        *   [Pydantic](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/pydantic/)
        *   [Selection](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/selection/)
        
    *   [Programs](https://docs.llamaindex.ai/en/stable/api_reference/program/)
        
        Programs
        
        *   [Evaporate](https://docs.llamaindex.ai/en/stable/api_reference/program/evaporate/)
        *   [Guidance](https://docs.llamaindex.ai/en/stable/api_reference/program/guidance/)
        *   [Llm text completion](https://docs.llamaindex.ai/en/stable/api_reference/program/llm_text_completion/)
        *   [Lmformatenforcer](https://docs.llamaindex.ai/en/stable/api_reference/program/lmformatenforcer/)
        *   [Multi modal](https://docs.llamaindex.ai/en/stable/api_reference/program/multi_modal/)
        *   [Openai](https://docs.llamaindex.ai/en/stable/api_reference/program/openai/)
        
    *   [Prompts](https://docs.llamaindex.ai/en/stable/api_reference/prompts/)
        
        Prompts
        
    *   [Query Engines](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/)
        
        Query Engines
        
        *   [FLARE](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/FLARE/)
        *   [JSONalayze](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/JSONalayze/)
        *   [NL SQL table](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/NL_SQL_table/)
        *   [PGVector SQL](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/PGVector_SQL/)
        *   [SQL join](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/SQL_join/)
        *   [SQL table retriever](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/SQL_table_retriever/)
        *   [Citation](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/citation/)
        *   [Cogniswitch](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/cogniswitch/)
        *   [Custom](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/custom/)
        *   [Knowledge graph](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/knowledge_graph/)
        *   [Multi step](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/multi_step/)
        *   [Pandas](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/pandas/)
        *   [Retriever](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/retriever/)
        *   [Retriever router](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/retriever_router/)
        *   [Retry](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/retry/)
        *   [Router](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/router/)
        *   [Simple multi modal](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/simple_multi_modal/)
        *   [Sub question](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/sub_question/)
        *   [Tool retriever router](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/tool_retriever_router/)
        *   [Transform](https://docs.llamaindex.ai/en/stable/api_reference/query_engine/transform/)
        
    *   [Query Pipeline](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/)
        
        Query Pipeline
        
        *   [Agent](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/agent/)
        *   [Arg pack](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/arg_pack/)
        *   [Custom](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/custom/)
        *   [Function](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/function/)
        *   [Input](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/input/)
        *   [Llm](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/llm/)
        *   [Multi modal](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/multi_modal/)
        *   [Object](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/object/)
        *   [Output parser](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/output_parser/)
        *   [Postprocessor](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/postprocessor/)
        *   [Prompt](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/prompt/)
        *   [Query engine](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/query_engine/)
        *   [Query transform](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/query_transform/)
        *   [Retriever](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/retriever/)
        *   [Router](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/router/)
        *   [Synthesizer](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/synthesizer/)
        *   [Tool runner](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/tool_runner/)
        
    *   [Question Generators](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/)
        
        Question Generators
        
        *   [Guidance](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/guidance/)
        *   [Llm question gen](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/llm_question_gen/)
        *   [Openai](https://docs.llamaindex.ai/en/stable/api_reference/question_gen/openai/)
        
    *   [Readers](https://docs.llamaindex.ai/en/stable/api_reference/readers/)
        
        Readers
        
        *   [Agent search](https://docs.llamaindex.ai/en/stable/api_reference/readers/agent_search/)
        *   [Airbyte cdk](https://docs.llamaindex.ai/en/stable/api_reference/readers/airbyte_cdk/)
        *   [Airbyte gong](https://docs.llamaindex.ai/en/stable/api_reference/readers/airbyte_gong/)
        *   [Airbyte hubspot](https://docs.llamaindex.ai/en/stable/api_reference/readers/airbyte_hubspot/)
        *   [Airbyte salesforce](https://docs.llamaindex.ai/en/stable/api_reference/readers/airbyte_salesforce/)
        *   [Airbyte shopify](https://docs.llamaindex.ai/en/stable/api_reference/readers/airbyte_shopify/)
        *   [Airbyte stripe](https://docs.llamaindex.ai/en/stable/api_reference/readers/airbyte_stripe/)
        *   [Airbyte typeform](https://docs.llamaindex.ai/en/stable/api_reference/readers/airbyte_typeform/)
        *   [Airbyte zendesk support](https://docs.llamaindex.ai/en/stable/api_reference/readers/airbyte_zendesk_support/)
        *   [Airtable](https://docs.llamaindex.ai/en/stable/api_reference/readers/airtable/)
        *   [Apify](https://docs.llamaindex.ai/en/stable/api_reference/readers/apify/)
        *   [Arango db](https://docs.llamaindex.ai/en/stable/api_reference/readers/arango_db/)
        *   [Arxiv](https://docs.llamaindex.ai/en/stable/api_reference/readers/arxiv/)
        *   [Asana](https://docs.llamaindex.ai/en/stable/api_reference/readers/asana/)
        *   [Assemblyai](https://docs.llamaindex.ai/en/stable/api_reference/readers/assemblyai/)
        *   [Astra db](https://docs.llamaindex.ai/en/stable/api_reference/readers/astra_db/)
        *   [Athena](https://docs.llamaindex.ai/en/stable/api_reference/readers/athena/)
        *   [Awadb](https://docs.llamaindex.ai/en/stable/api_reference/readers/awadb/)
        *   [Azcognitive search](https://docs.llamaindex.ai/en/stable/api_reference/readers/azcognitive_search/)
        *   [Azstorage blob](https://docs.llamaindex.ai/en/stable/api_reference/readers/azstorage_blob/)
        *   [Azure devops](https://docs.llamaindex.ai/en/stable/api_reference/readers/azure_devops/)
        *   [Bagel](https://docs.llamaindex.ai/en/stable/api_reference/readers/bagel/)
        *   [Bilibili](https://docs.llamaindex.ai/en/stable/api_reference/readers/bilibili/)
        *   [Bitbucket](https://docs.llamaindex.ai/en/stable/api_reference/readers/bitbucket/)
        *   [Boarddocs](https://docs.llamaindex.ai/en/stable/api_reference/readers/boarddocs/)
        *   [Chatgpt plugin](https://docs.llamaindex.ai/en/stable/api_reference/readers/chatgpt_plugin/)
        *   [Chroma](https://docs.llamaindex.ai/en/stable/api_reference/readers/chroma/)
        *   [Clickhouse](https://docs.llamaindex.ai/en/stable/api_reference/readers/clickhouse/)
        *   [Confluence](https://docs.llamaindex.ai/en/stable/api_reference/readers/confluence/)
        *   [Couchbase](https://docs.llamaindex.ai/en/stable/api_reference/readers/couchbase/)
        *   [Couchdb](https://docs.llamaindex.ai/en/stable/api_reference/readers/couchdb/)
        *   [Dad jokes](https://docs.llamaindex.ai/en/stable/api_reference/readers/dad_jokes/)
        *   [Dashscope](https://docs.llamaindex.ai/en/stable/api_reference/readers/dashscope/)
        *   [Dashvector](https://docs.llamaindex.ai/en/stable/api_reference/readers/dashvector/)
        *   [Database](https://docs.llamaindex.ai/en/stable/api_reference/readers/database/)
        *   [Deeplake](https://docs.llamaindex.ai/en/stable/api_reference/readers/deeplake/)
        *   [Discord](https://docs.llamaindex.ai/en/stable/api_reference/readers/discord/)
        *   [Docstring walker](https://docs.llamaindex.ai/en/stable/api_reference/readers/docstring_walker/)
        *   [Docugami](https://docs.llamaindex.ai/en/stable/api_reference/readers/docugami/)
        *   [Earnings call transcript](https://docs.llamaindex.ai/en/stable/api_reference/readers/earnings_call_transcript/)
        *   [Elasticsearch](https://docs.llamaindex.ai/en/stable/api_reference/readers/elasticsearch/)
        *   [Faiss](https://docs.llamaindex.ai/en/stable/api_reference/readers/faiss/)
        *   [Feedly rss](https://docs.llamaindex.ai/en/stable/api_reference/readers/feedly_rss/)
        *   [Feishu docs](https://docs.llamaindex.ai/en/stable/api_reference/readers/feishu_docs/)
        *   [Feishu wiki](https://docs.llamaindex.ai/en/stable/api_reference/readers/feishu_wiki/)
        *   [File](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/)
        *   [Firebase realtimedb](https://docs.llamaindex.ai/en/stable/api_reference/readers/firebase_realtimedb/)
        *   [Firestore](https://docs.llamaindex.ai/en/stable/api_reference/readers/firestore/)
        *   [Gcs](https://docs.llamaindex.ai/en/stable/api_reference/readers/gcs/)
        *   [Genius](https://docs.llamaindex.ai/en/stable/api_reference/readers/genius/)
        *   [Github](https://docs.llamaindex.ai/en/stable/api_reference/readers/github/)
        *   [Google](https://docs.llamaindex.ai/en/stable/api_reference/readers/google/)
        *   [Gpt repo](https://docs.llamaindex.ai/en/stable/api_reference/readers/gpt_repo/)
        *   [Graphdb cypher](https://docs.llamaindex.ai/en/stable/api_reference/readers/graphdb_cypher/)
        *   [Graphql](https://docs.llamaindex.ai/en/stable/api_reference/readers/graphql/)
        *   [Guru](https://docs.llamaindex.ai/en/stable/api_reference/readers/guru/)
        *   [Hatena blog](https://docs.llamaindex.ai/en/stable/api_reference/readers/hatena_blog/)
        *   [Hive](https://docs.llamaindex.ai/en/stable/api_reference/readers/hive/)
        *   [Hubspot](https://docs.llamaindex.ai/en/stable/api_reference/readers/hubspot/)
        *   [Huggingface fs](https://docs.llamaindex.ai/en/stable/api_reference/readers/huggingface_fs/)
        *   [Hwp](https://docs.llamaindex.ai/en/stable/api_reference/readers/hwp/)
        *   [Iceberg](https://docs.llamaindex.ai/en/stable/api_reference/readers/iceberg/)
        *   [Imdb review](https://docs.llamaindex.ai/en/stable/api_reference/readers/imdb_review/)
        *   [Intercom](https://docs.llamaindex.ai/en/stable/api_reference/readers/intercom/)
        *   [Jaguar](https://docs.llamaindex.ai/en/stable/api_reference/readers/jaguar/)
        *   [Jira](https://docs.llamaindex.ai/en/stable/api_reference/readers/jira/)
        *   [Joplin](https://docs.llamaindex.ai/en/stable/api_reference/readers/joplin/)
        *   [Json](https://docs.llamaindex.ai/en/stable/api_reference/readers/json/)
        *   [Kaltura esearch](https://docs.llamaindex.ai/en/stable/api_reference/readers/kaltura_esearch/)
        *   [Kibela](https://docs.llamaindex.ai/en/stable/api_reference/readers/kibela/)
        *   [Lilac](https://docs.llamaindex.ai/en/stable/api_reference/readers/lilac/)
        *   [Linear](https://docs.llamaindex.ai/en/stable/api_reference/readers/linear/)
        *   [Llama parse](https://docs.llamaindex.ai/en/stable/api_reference/readers/llama_parse/)
        *   [Macrometa gdn](https://docs.llamaindex.ai/en/stable/api_reference/readers/macrometa_gdn/)
        *   [Make com](https://docs.llamaindex.ai/en/stable/api_reference/readers/make_com/)
        *   [Mangadex](https://docs.llamaindex.ai/en/stable/api_reference/readers/mangadex/)
        *   [Mangoapps guides](https://docs.llamaindex.ai/en/stable/api_reference/readers/mangoapps_guides/)
        *   [Maps](https://docs.llamaindex.ai/en/stable/api_reference/readers/maps/)
        *   [Mbox](https://docs.llamaindex.ai/en/stable/api_reference/readers/mbox/)
        *   [Memos](https://docs.llamaindex.ai/en/stable/api_reference/readers/memos/)
        *   [Metal](https://docs.llamaindex.ai/en/stable/api_reference/readers/metal/)
        *   [Microsoft onedrive](https://docs.llamaindex.ai/en/stable/api_reference/readers/microsoft_onedrive/)
        *   [Microsoft outlook](https://docs.llamaindex.ai/en/stable/api_reference/readers/microsoft_outlook/)
        *   [Microsoft sharepoint](https://docs.llamaindex.ai/en/stable/api_reference/readers/microsoft_sharepoint/)
        *   [Milvus](https://docs.llamaindex.ai/en/stable/api_reference/readers/milvus/)
        *   [Minio](https://docs.llamaindex.ai/en/stable/api_reference/readers/minio/)
        *   [Mondaydotcom](https://docs.llamaindex.ai/en/stable/api_reference/readers/mondaydotcom/)
        *   [Mongodb](https://docs.llamaindex.ai/en/stable/api_reference/readers/mongodb/)
        *   [Myscale](https://docs.llamaindex.ai/en/stable/api_reference/readers/myscale/)
        *   [Notion](https://docs.llamaindex.ai/en/stable/api_reference/readers/notion/)
        *   [Nougat ocr](https://docs.llamaindex.ai/en/stable/api_reference/readers/nougat_ocr/)
        *   [Obsidian](https://docs.llamaindex.ai/en/stable/api_reference/readers/obsidian/)
        *   [Openalex](https://docs.llamaindex.ai/en/stable/api_reference/readers/openalex/)
        *   [Openapi](https://docs.llamaindex.ai/en/stable/api_reference/readers/openapi/)
        *   [Opendal](https://docs.llamaindex.ai/en/stable/api_reference/readers/opendal/)
        *   [Opensearch](https://docs.llamaindex.ai/en/stable/api_reference/readers/opensearch/)
        *   [Pandas ai](https://docs.llamaindex.ai/en/stable/api_reference/readers/pandas_ai/)
        *   [Papers](https://docs.llamaindex.ai/en/stable/api_reference/readers/papers/)
        *   [Patentsview](https://docs.llamaindex.ai/en/stable/api_reference/readers/patentsview/)
        *   [Pathway](https://docs.llamaindex.ai/en/stable/api_reference/readers/pathway/)
        *   [Pdb](https://docs.llamaindex.ai/en/stable/api_reference/readers/pdb/)
        *   [Pdf marker](https://docs.llamaindex.ai/en/stable/api_reference/readers/pdf_marker/)
        *   [Pdf table](https://docs.llamaindex.ai/en/stable/api_reference/readers/pdf_table/)
        *   [Pebblo](https://docs.llamaindex.ai/en/stable/api_reference/readers/pebblo/)
        *   [None](https://docs.llamaindex.ai/en/stable/api_reference/readers/pinecone.md)
        *   [Preprocess](https://docs.llamaindex.ai/en/stable/api_reference/readers/preprocess/)
        *   [Psychic](https://docs.llamaindex.ai/en/stable/api_reference/readers/psychic/)
        *   [Qdrant](https://docs.llamaindex.ai/en/stable/api_reference/readers/qdrant/)
        *   [Rayyan](https://docs.llamaindex.ai/en/stable/api_reference/readers/rayyan/)
        *   [Readme](https://docs.llamaindex.ai/en/stable/api_reference/readers/readme/)
        *   [Readwise](https://docs.llamaindex.ai/en/stable/api_reference/readers/readwise/)
        *   [Reddit](https://docs.llamaindex.ai/en/stable/api_reference/readers/reddit/)
        *   [Remote](https://docs.llamaindex.ai/en/stable/api_reference/readers/remote/)
        *   [Remote depth](https://docs.llamaindex.ai/en/stable/api_reference/readers/remote_depth/)
        *   [S3](https://docs.llamaindex.ai/en/stable/api_reference/readers/s3/)
        *   [Sec filings](https://docs.llamaindex.ai/en/stable/api_reference/readers/sec_filings/)
        *   [Semanticscholar](https://docs.llamaindex.ai/en/stable/api_reference/readers/semanticscholar/)
        *   [Simple directory reader](https://docs.llamaindex.ai/en/stable/api_reference/readers/simple_directory_reader/)
        *   [Singlestore](https://docs.llamaindex.ai/en/stable/api_reference/readers/singlestore/)
        *   [Slack](https://docs.llamaindex.ai/en/stable/api_reference/readers/slack/)
        *   [Smart pdf loader](https://docs.llamaindex.ai/en/stable/api_reference/readers/smart_pdf_loader/)
        *   [Snowflake](https://docs.llamaindex.ai/en/stable/api_reference/readers/snowflake/)
        *   [Snscrape twitter](https://docs.llamaindex.ai/en/stable/api_reference/readers/snscrape_twitter/)
        *   [Spotify](https://docs.llamaindex.ai/en/stable/api_reference/readers/spotify/)
        *   [Stackoverflow](https://docs.llamaindex.ai/en/stable/api_reference/readers/stackoverflow/)
        *   [Steamship](https://docs.llamaindex.ai/en/stable/api_reference/readers/steamship/)
        *   [String iterable](https://docs.llamaindex.ai/en/stable/api_reference/readers/string_iterable/)
        *   [Stripe docs](https://docs.llamaindex.ai/en/stable/api_reference/readers/stripe_docs/)
        *   [Structured data](https://docs.llamaindex.ai/en/stable/api_reference/readers/structured_data/)
        *   [Telegram](https://docs.llamaindex.ai/en/stable/api_reference/readers/telegram/)
        *   [Toggl](https://docs.llamaindex.ai/en/stable/api_reference/readers/toggl/)
        *   [Trello](https://docs.llamaindex.ai/en/stable/api_reference/readers/trello/)
        *   [Twitter](https://docs.llamaindex.ai/en/stable/api_reference/readers/twitter/)
        *   [Txtai](https://docs.llamaindex.ai/en/stable/api_reference/readers/txtai/)
        *   [Upstage](https://docs.llamaindex.ai/en/stable/api_reference/readers/upstage/)
        *   [Weather](https://docs.llamaindex.ai/en/stable/api_reference/readers/weather/)
        *   [Weaviate](https://docs.llamaindex.ai/en/stable/api_reference/readers/weaviate/)
        *   [Web](https://docs.llamaindex.ai/en/stable/api_reference/readers/web/)
        *   [Whatsapp](https://docs.llamaindex.ai/en/stable/api_reference/readers/whatsapp/)
        *   [Wikipedia](https://docs.llamaindex.ai/en/stable/api_reference/readers/wikipedia/)
        *   [Wordlift](https://docs.llamaindex.ai/en/stable/api_reference/readers/wordlift/)
        *   [Wordpress](https://docs.llamaindex.ai/en/stable/api_reference/readers/wordpress/)
        *   [Youtube metadata](https://docs.llamaindex.ai/en/stable/api_reference/readers/youtube_metadata/)
        *   [Youtube transcript](https://docs.llamaindex.ai/en/stable/api_reference/readers/youtube_transcript/)
        *   [Zendesk](https://docs.llamaindex.ai/en/stable/api_reference/readers/zendesk/)
        *   [Zep](https://docs.llamaindex.ai/en/stable/api_reference/readers/zep/)
        *   [Zulip](https://docs.llamaindex.ai/en/stable/api_reference/readers/zulip/)
        
    *   [Response Synthesizers](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/)
        
        Response Synthesizers
        
        *   [Accumulate](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/accumulate/)
        *   [Compact accumulate](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/compact_accumulate/)
        *   [Compact and refine](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/compact_and_refine/)
        *   [Generation](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/generation/)
        *   [Google](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/google/)
        *   [Refine](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/refine/)
        *   [Simple summarize](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/simple_summarize/)
        *   [Tree summarize](https://docs.llamaindex.ai/en/stable/api_reference/response_synthesizers/tree_summarize/)
        
    *   [Retrievers](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/)
        
        Retrievers
        
        *   [Auto merging](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/auto_merging/)
        *   [Bedrock](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/bedrock/)
        *   [Bm25](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/bm25/)
        *   [Duckdb retriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/duckdb_retriever/)
        *   [Keyword](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/keyword/)
        *   [Knowledge graph](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/knowledge_graph/)
        *   [Mongodb atlas bm25 retriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/mongodb_atlas_bm25_retriever/)
        *   [Pathway](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/pathway/)
        *   [Query fusion](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/query_fusion/)
        *   [Recursive](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/recursive/)
        *   [Router](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/router/)
        *   [Sql](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/sql/)
        *   [Summary](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/summary/)
        *   [Transform](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/transform/)
        *   [Tree](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/tree/)
        *   [Vector](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/vector/)
        *   [Videodb](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/videodb/)
        *   [You](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/you/)
        
    *   [Schema](https://docs.llamaindex.ai/en/stable/api_reference/schema/)
        
        Schema
        
    *    Storage
        
        Storage
        
        *   [Chat Store](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/)
            
            Chat Store
            
            *   [Azure](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/azure/)
            *   [Redis](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/redis/)
            *   [Simple](https://docs.llamaindex.ai/en/stable/api_reference/storage/chat_store/simple/)
            
        *   [Docstore](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/)
            
            Docstore
            
            *   [Azure](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/azure/)
            *   [Dynamodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/dynamodb/)
            *   [Elasticsearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/elasticsearch/)
            *   [Firestore](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/firestore/)
            *   [Mongodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/mongodb/)
            *   [Postgres](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/postgres/)
            *   [Redis](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/redis/)
            *   [Simple](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/simple/)
            
        *   [Graph Stores](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/)
            
            Graph Stores
            
            *   [Falkordb](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/falkordb/)
            *   [Kuzu](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/kuzu/)
            *   [Nebula](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/nebula/)
            *   [Neo4j](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/)
            *   [Neptune](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neptune/)
            *   [Simple](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/simple/)
            *   [Tidb](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/tidb/)
            
        *   [Index Store](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/)
            
            Index Store
            
            *   [Azure](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/azure/)
            *   [Dynamodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/dynamodb/)
            *   [Elasticsearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/elasticsearch/)
            *   [Firestore](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/firestore/)
            *   [Mongodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/mongodb/)
            *   [Postgres](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/postgres/)
            *   [Redis](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/redis/)
            *   [Simple](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/simple/)
            
        *   [Kvstore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/)
            
            Kvstore
            
            *   [Azure](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/azure/)
            *   [Dynamodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/dynamodb/)
            *   [Elasticsearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/elasticsearch/)
            *   [Firestore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/firestore/)
            *   [Mongodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/mongodb/)
            *   [Postgres](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/postgres/)
            *   [Redis](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/redis/)
            *   [S3](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/s3/)
            *   [Simple](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/simple/)
            
        *    Storage
            
            Storage
            
            *   [Storage context](https://docs.llamaindex.ai/en/stable/api_reference/storage/storage_context/)
            
        *   [Vector Store](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/)
            
            Vector Store
            
            *   [Alibabacloud opensearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/alibabacloud_opensearch/)
            *   [Analyticdb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/analyticdb/)
            *   [Astra db](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/astra_db/)
            *   [Awadb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/awadb/)
            *   [Awsdocdb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/awsdocdb/)
            *   [Azureaisearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/azureaisearch/)
            *   [Azurecosmosmongo](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/azurecosmosmongo/)
            *   [Bagel](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/bagel/)
            *   [Baiduvectordb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/baiduvectordb/)
            *   [Cassandra](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/cassandra/)
            *   [Chatgpt plugin](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/chatgpt_plugin/)
            *   [Chroma](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/chroma/)
            *   [Clickhouse](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/clickhouse/)
            *   [Couchbase](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/couchbase/)
            *   [Dashvector](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/dashvector/)
            *   [Databricks](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/databricks/)
            *   [Deeplake](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/deeplake/)
            *   [Docarray](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/docarray/)
            *   [Duckdb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/duckdb/)
            *   [Dynamodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/dynamodb/)
            *   [Elasticsearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/elasticsearch/)
            *   [Epsilla](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/epsilla/)
            *   [Faiss](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/faiss/)
            *   [Firestore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/firestore/)
            *   [Google](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/google/)
            *   [Hologres](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/hologres/)
            *   [Jaguar](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/jaguar/)
            *   [Kdbai](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/kdbai/)
            *   [Lancedb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/lancedb/)
            *   [Lantern](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/lantern/)
            *   [Metal](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/metal/)
            *   [Milvus](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/milvus/)
            *   [Mongodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/mongodb/)
            *   [Myscale](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/myscale/)
            *   [Neo4jvector](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/neo4jvector/)
            *   [Neptune](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/neptune/)
            *   [Opensearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/opensearch/)
            *   [Pgvecto rs](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/pgvecto_rs/)
            *   [Pinecone](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/pinecone/)
            *   [Postgres](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/postgres/)
            *   [Qdrant](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/qdrant/)
            *   [Redis](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/redis/)
            *   [Relyt](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/relyt/)
            *   [Rocksetdb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/rocksetdb/)
            *   [Simple](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/simple/)
            *   [Singlestoredb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/singlestoredb/)
            *   [Supabase](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/supabase/)
            *   [Tair](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/tair/)
            *   [Tencentvectordb](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/tencentvectordb/)
            *   [Tidbvector](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/tidbvector/)
            *   [Timescalevector](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/timescalevector/)
            *   [Txtai](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/txtai/)
            *   [Typesense](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/typesense/)
            *   [Upstash](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/upstash/)
            *   [Vearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/vearch/)
            *   [Vertexaivectorsearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/vertexaivectorsearch/)
            *   [Vespa](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/vespa/)
            *   [Weaviate](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/weaviate/)
            *   [Wordlift](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/wordlift/)
            *   [Zep](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/zep/)
            
        
    *   [Tools](https://docs.llamaindex.ai/en/stable/api_reference/tools/)
        
        Tools
        
        *   [Arxiv](https://docs.llamaindex.ai/en/stable/api_reference/tools/arxiv/)
        *   [Azure code interpreter](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_code_interpreter/)
        *   [Azure cv](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_cv/)
        *   [Azure speech](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_speech/)
        *   [Azure translate](https://docs.llamaindex.ai/en/stable/api_reference/tools/azure_translate/)
        *   [Bing search](https://docs.llamaindex.ai/en/stable/api_reference/tools/bing_search/)
        *   [Brave search](https://docs.llamaindex.ai/en/stable/api_reference/tools/brave_search/)
        *   [Cassandra](https://docs.llamaindex.ai/en/stable/api_reference/tools/cassandra/)
        *   [Chatgpt plugin](https://docs.llamaindex.ai/en/stable/api_reference/tools/chatgpt_plugin/)
        *   [Code interpreter](https://docs.llamaindex.ai/en/stable/api_reference/tools/code_interpreter/)
        *   [Cogniswitch](https://docs.llamaindex.ai/en/stable/api_reference/tools/cogniswitch/)
        *   [Database](https://docs.llamaindex.ai/en/stable/api_reference/tools/database/)
        *   [Duckduckgo](https://docs.llamaindex.ai/en/stable/api_reference/tools/duckduckgo/)
        *   [Exa](https://docs.llamaindex.ai/en/stable/api_reference/tools/exa/)
        *   [Finance](https://docs.llamaindex.ai/en/stable/api_reference/tools/finance/)
        *   [Function](https://docs.llamaindex.ai/en/stable/api_reference/tools/function/)
        *   [Google](https://docs.llamaindex.ai/en/stable/api_reference/tools/google/)
        *   [Graphql](https://docs.llamaindex.ai/en/stable/api_reference/tools/graphql/)
        *   [Ionic shopping](https://docs.llamaindex.ai/en/stable/api_reference/tools/ionic_shopping/)
        *   [Jina](https://docs.llamaindex.ai/en/stable/api_reference/tools/jina/)
        *   [Load and search](https://docs.llamaindex.ai/en/stable/api_reference/tools/load_and_search/)
        *   [Metaphor](https://docs.llamaindex.ai/en/stable/api_reference/tools/metaphor/)
        *   [Multion](https://docs.llamaindex.ai/en/stable/api_reference/tools/multion/)
        *   [Neo4j](https://docs.llamaindex.ai/en/stable/api_reference/tools/neo4j/)
        *   [Notion](https://docs.llamaindex.ai/en/stable/api_reference/tools/notion/)
        *   [Ondemand loader](https://docs.llamaindex.ai/en/stable/api_reference/tools/ondemand_loader/)
        *   [Openai](https://docs.llamaindex.ai/en/stable/api_reference/tools/openai/)
        *   [Openapi](https://docs.llamaindex.ai/en/stable/api_reference/tools/openapi/)
        *   [Passio nutrition ai](https://docs.llamaindex.ai/en/stable/api_reference/tools/passio_nutrition_ai/)
        *   [Playgrounds](https://docs.llamaindex.ai/en/stable/api_reference/tools/playgrounds/)
        *   [Python file](https://docs.llamaindex.ai/en/stable/api_reference/tools/python_file/)
        *   [Query engine](https://docs.llamaindex.ai/en/stable/api_reference/tools/query_engine/)
        *   [Query plan](https://docs.llamaindex.ai/en/stable/api_reference/tools/query_plan/)
        *   [Requests](https://docs.llamaindex.ai/en/stable/api_reference/tools/requests/)
        *   [Retriever](https://docs.llamaindex.ai/en/stable/api_reference/tools/retriever/)
        *   [Salesforce](https://docs.llamaindex.ai/en/stable/api_reference/tools/salesforce/)
        *   [Shopify](https://docs.llamaindex.ai/en/stable/api_reference/tools/shopify/)
        *   [Slack](https://docs.llamaindex.ai/en/stable/api_reference/tools/slack/)
        *   [Tavily research](https://docs.llamaindex.ai/en/stable/api_reference/tools/tavily_research/)
        *   [Text to image](https://docs.llamaindex.ai/en/stable/api_reference/tools/text_to_image/)
        *   [Tool spec](https://docs.llamaindex.ai/en/stable/api_reference/tools/tool_spec/)
        *   [Vector db](https://docs.llamaindex.ai/en/stable/api_reference/tools/vector_db/)
        *   [Waii](https://docs.llamaindex.ai/en/stable/api_reference/tools/waii/)
        *   [Weather](https://docs.llamaindex.ai/en/stable/api_reference/tools/weather/)
        *   [Wikipedia](https://docs.llamaindex.ai/en/stable/api_reference/tools/wikipedia/)
        *   [Wolfram alpha](https://docs.llamaindex.ai/en/stable/api_reference/tools/wolfram_alpha/)
        *   [Yahoo finance](https://docs.llamaindex.ai/en/stable/api_reference/tools/yahoo_finance/)
        *   [Yelp](https://docs.llamaindex.ai/en/stable/api_reference/tools/yelp/)
        *   [Zapier](https://docs.llamaindex.ai/en/stable/api_reference/tools/zapier/)
        
    
*   [Open-Source Community](https://docs.llamaindex.ai/en/stable/community/llama_packs/)
    
    Open-Source Community
    
    *   [Integrations](https://docs.llamaindex.ai/en/stable/community/integrations/)
    *   [Full Stack Projects](https://docs.llamaindex.ai/en/stable/community/full_stack_projects/)
    *    Community FAQ
        
        Community FAQ
        
        *   [Chat Engines](https://docs.llamaindex.ai/en/stable/community/faq/chat_engines/)
        *   [Documents and Nodes](https://docs.llamaindex.ai/en/stable/community/faq/documents_and_nodes/)
        *   [Embeddings](https://docs.llamaindex.ai/en/stable/community/faq/embeddings/)
        *   [Large Language Models](https://docs.llamaindex.ai/en/stable/community/faq/llms/)
        *   [Query Engines](https://docs.llamaindex.ai/en/stable/community/faq/query_engines/)
        *   [Vector Database](https://docs.llamaindex.ai/en/stable/community/faq/vector_database/)
        
    *    Contributing
        
        Contributing
        
        *   [Code](https://docs.llamaindex.ai/en/stable/CONTRIBUTING/)
        *   [Docs](https://docs.llamaindex.ai/en/stable/DOCS_README/)
        
    *   [Changelog](https://docs.llamaindex.ai/en/stable/CHANGELOG/)
    *   [Presentations](https://docs.llamaindex.ai/en/stable/presentations/past_presentations/)
    *   [Upgrading to v0.10.x](https://docs.llamaindex.ai/en/stable/getting_started/v0_10_0_migration/)
    *   [Deprecated Terms](https://docs.llamaindex.ai/en/stable/changes/deprecated_terms/)
    
*   [LlamaCloud](https://docs.llamaindex.ai/en/stable/llama_cloud/)
    
    LlamaCloud
    
    *   [LlamaParse](https://docs.llamaindex.ai/en/stable/llama_cloud/llama_parse/)
    

Table of contents

*   [Using SimpleWebPageReader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/#using-simplewebpagereader)

       

[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/docs/examples/data_connectors/WebPageDemo.ipynb)

Web Page Reader[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/#web-page-reader)
==============================================================================================================

Demonstrates our web page reader.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index llama\-index\-readers\-web

%pip install llama-index llama-index-readers-web

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

#### Using SimpleWebPageReader[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/#using-simplewebpagereader)

In \[ \]:

Copied!

from llama\_index.core import SummaryIndex
from llama\_index.readers.web import SimpleWebPageReader
from IPython.display import Markdown, display
import os

from llama\_index.core import SummaryIndex from llama\_index.readers.web import SimpleWebPageReader from IPython.display import Markdown, display import os

In \[ \]:

Copied!

\# NOTE: the html\_to\_text=True option requires html2text to be installed

\# NOTE: the html\_to\_text=True option requires html2text to be installed

In \[ \]:

Copied!

documents \= SimpleWebPageReader(html\_to\_text\=True).load\_data(
    \["http://paulgraham.com/worked.html"\]
)

documents = SimpleWebPageReader(html\_to\_text=True).load\_data( \["http://paulgraham.com/worked.html"\] )

In \[ \]:

Copied!

documents\[0\]

documents\[0\]

In \[ \]:

Copied!

index \= SummaryIndex.from\_documents(documents)

index = SummaryIndex.from\_documents(documents)

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did the author do growing up?")

\# set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine() response = query\_engine.query("What did the author do growing up?")

In \[ \]:

Copied!

display(Markdown(f"<b>{response}</b>"))

display(Markdown(f"**{response}**"))

Using Spider Reader 🕷[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/#using-spider-reader)
=========================================================================================================================

[Spider](https://spider.cloud/?ref=llama_index) is the [fastest](https://github.com/spider-rs/spider/blob/main/benches/BENCHMARKS.md#benchmark-results) crawler. It converts any website into pure HTML, markdown, metadata or text while enabling you to crawl with custom actions using AI.

Spider allows you to use high performance proxies to prevent detection, caches AI actions, webhooks for crawling status, scheduled crawls etc...

**Prerequisites:** you need to have a Spider api key to use this loader. You can get one on [spider.cloud](https://spider.cloud/).

In \[ \]:

Copied!

\# Scrape single URL
from llama\_index.readers.web import SpiderWebReader

spider\_reader \= SpiderWebReader(
    api\_key\="YOUR\_API\_KEY",  \# Get one at https://spider.cloud
    mode\="scrape",
    \# params={} # Optional parameters see more on https://spider.cloud/docs/api
)

documents \= spider\_reader.load\_data(url\="https://spider.cloud")
print(documents)

\# Scrape single URL from llama\_index.readers.web import SpiderWebReader spider\_reader = SpiderWebReader( api\_key="YOUR\_API\_KEY", # Get one at https://spider.cloud mode="scrape", # params={} # Optional parameters see more on https://spider.cloud/docs/api ) documents = spider\_reader.load\_data(url="https://spider.cloud") print(documents)

\[Document(id\_='54a6ecf3-b33e-41e9-8cec-48657aa2ed9b', embedding=None, metadata={'description': 'Collect data rapidly from any website. Seamlessly scrape websites and get data tailored for LLM workloads.', 'domain': 'spider.cloud', 'extracted\_data': None, 'file\_size': 101750, 'keywords': None, 'pathname': '/', 'resource\_type': 'html', 'title': 'Spider - Fastest Web Crawler', 'url': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48/spider.cloud/index.html', 'user\_id': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='Spider - Fastest Web Crawler\[Spider v1 Logo Spider \](/)\[Pricing\](/credits/new)\[GitHubGithub637\](https://github.com/spider-rs/spider)The World\\'s Fastest and Cheapest Crawler API==========View Demo\* Basic\* StreamingExample requestPythonCopy\`\`\`import requests, osheaders = {    \\'Authorization\\': os.environ\["SPIDER\_API\_KEY"\],    \\'Content-Type\\': \\'application/json\\',}json\_data = {"limit":50,"url":"http://www.example.com"}response = requests.post(\\'https://api.spider.cloud/crawl\\',  headers=headers,  json=json\_data)print(response.json())\`\`\`Example ResponseUnmatched Speed----------### 5secs  ###To crawl 200 pages### 21x  ###Faster than FireCrawl### 150x  ###Faster than Apify Benchmarks displaying performance between Spider Cloud, Firecrawl, and Apify.\[See framework benchmarks \](https://github.com/spider-rs/spider/blob/main/benches/BENCHMARKS.md)Foundations for Crawling Effectively----------### Leading in performance ###Spider is written in Rust and runs in full concurrency to achieve crawling dozens of pages in secs.### Optimal response format ###Get clean and formatted markdown, HTML, or text content for fine-tuning or training AI models.### Caching ###Further boost speed by caching repeated web page crawls.### Smart Mode ###Spider dynamically switches to Headless Chrome when it needs to.Beta### Scrape with AI ###Do custom browser scripting and data extraction using the latest AI models.### Best crawler for LLMs ###Don\\'t let crawling and scraping be the highest latency in your LLM & AI agent stack.### Scrape with no headaches ###\* Proxy rotations\* Agent headers\* Avoid anti-bot detections\* Headless chrome\* Markdown LLM Responses### The Fastest Web Crawler ###\* Powered by \[spider-rs\](https://github.com/spider-rs/spider)\* Do 20,000 pages in seconds\* Full concurrency\* Powerful and simple API\* 5,000 requests per minute### Do more with AI ###\* Custom browser scripting\* Advanced data extraction\* Data pipelines\* Perfect for LLM and AI Agents\* Accurate website labeling\[API\](/docs/api) \[Pricing\](/credits/new) \[Guides\](/guides) \[About\](/about) \[Docs\](https://docs.rs/spider/latest/spider/) \[Privacy\](/privacy) \[Terms\](/eula)© 2024 Spider from A11yWatchTheme Light Dark Toggle Theme \[GitHubGithub\](https://github.com/spider-rs/spider)', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n')\]

Crawl domain following all deeper subpages

In \[ \]:

Copied!

\# Crawl domain with deeper crawling following subpages
from llama\_index.readers.web import SpiderWebReader

spider\_reader \= SpiderWebReader(
    api\_key\="YOUR\_API\_KEY",
    mode\="crawl",
    \# params={} # Optional parameters see more on https://spider.cloud/docs/api
)

documents \= spider\_reader.load\_data(url\="https://spider.cloud")
print(documents)

\# Crawl domain with deeper crawling following subpages from llama\_index.readers.web import SpiderWebReader spider\_reader = SpiderWebReader( api\_key="YOUR\_API\_KEY", mode="crawl", # params={} # Optional parameters see more on https://spider.cloud/docs/api ) documents = spider\_reader.load\_data(url="https://spider.cloud") print(documents)

\[Document(id\_='63f7ccbf-c6c8-4f69-80f7-f6763f761a39', embedding=None, metadata={'description': 'Our privacy policy and how it plays a part in the data collected.', 'domain': 'spider.cloud', 'extracted\_data': None, 'file\_size': 26647, 'keywords': None, 'pathname': '/privacy', 'resource\_type': 'html', 'title': 'Privacy', 'url': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48/spider.cloud/privacy.html', 'user\_id': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text="Privacy\[Spider v1 Logo Spider \](/) \[Credits\](/credits/new)\[GitHubGithub637\](https://github.com/spider-rs/spider)Privacy Policy==========Learn about how we take privacy with the Spider project.\[Spider\](https://spider.cloud) offers a cutting-edge data scraping service with powerful AI capabilities. Our data collecting platform is designed to help users maximize the benefits of data collection while embracing the advancements in AI technology. With our innovative tools, we provide a seamless and fast interactive experience. This privacy policy details Spider's approach to product development, deployment, and usage, encompassing the Crawler, AI products, and features.\[AI Development at Spider----------\](#ai-development-at-spider)Spider leverages a robust combination of proprietary code, open-source frameworks, and synthetic datasets to train its cutting-edge products. To continuously improve our offerings, Spider may utilize inputs from user-generated prompts and content, obtained from trusted third-party providers. By harnessing this diverse data, Spider can deliver highly precise and pertinent recommendations to our valued users. While the foundational data crawling aspect of Spider is openly available on Github, the dashboard and AI components remain closed source. Spider respects all robots.txt files declared on websites allowing data to be extracted without harming the website.\[Security, Privacy, and Trust----------\](#security-privacy-and-trust)At Spider, our utmost priority is the development and implementation of Crawlers, AI technologies, and products that adhere to ethical, moral, and legal standards. We are dedicated to creating a secure and respectful environment for all users. Safeguarding user data and ensuring transparency in its usage are core principles we uphold. In line with this commitment, we provide the following important disclosures when utilizing our AI-related products:\* Spider ensures comprehensive disclosure of features that utilize third-party AI platforms. To provide clarity, these integrations will be clearly indicated through distinct markers, designations, explanatory notes that appear when hovering, references to the underlying codebase, or any other suitable form of notification as determined by the system. Our commitment to transparency aims to keep users informed about the involvement of third-party AI platforms in our products.\* We collect and use personal data as set forth in our \[Privacy Policy\](https://spider.cloud/privacy) which governs the collection and usage of personal data. If you choose to input personal data into our AI products, please be aware that such information may be processed through third-party AI providers. For any inquiries or concerns regarding data privacy, feel free to reach out to us at \[Spider Help Github\](https://github.com/orgs/spider-rs/discussions). We are here to assist you.\* Except for user-generated prompts and/or content as inputs, Spider does not use customer data, including the code related to the use of Spider's deployment services, to train or finetune any models used.\* We periodically review and update our policies and procedures in an effort to comply with applicable data protection regulations and industry standards.\* We use reasonable measures designed to maintain the safety of users and avoid harm to people and the environment. Spider's design and development process includes considerations for ethical, security, and regulatory requirements with certain safeguards to prevent and report misuse or abuse.\[Third-Party Service Providers----------\](#third-party-service-providers)In providing AI products and services, we leverage various third-party providers in the AI space to enhance our services and capabilities, and will continue to do so for certain product features.This page will be updated from time to time with information about Spider's use of AI. The current list of third-party AI providers integrated into Spider is as follows:\* \[Anthropic\](https://console.anthropic.com/legal/terms)\* \[Azure Cognitive Services\](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/data-privacy)\* \[Cohere\](https://cohere.com/terms-of-use)\* \[ElevenLabs\](https://elevenlabs.io/terms)\* \[Hugging Face\](https://huggingface.co/terms-of-service)\* \[Meta AI\](https://www.facebook.com/policies\_center/)\* \[OpenAI\](https://openai.com/policies)\* \[Pinecone\](https://www.pinecone.io/terms)\* \[Replicate\](https://replicate.com/terms)We prioritize the safety of our users and take appropriate measures to avoid harm both to individuals and the environment. Our design and development processes incorporate considerations for ethical practices, security protocols, and regulatory requirements, along with established safeguards to prevent and report any instances of misuse or abuse. We are committed to maintaining a secure and respectful environment and upholding responsible practices throughout our services.\[Acceptable Use----------\](#acceptable-use)Spider's products are intended to provide helpful and respectful responses to user prompts and queries while collecting data along the web. We don't allow the use of our Scraper or AI tools, products and services for the following usages:\* Denial of Service Attacks\* Illegal activity\* Inauthentic, deceptive, or impersonation behavior\* Any other use that would violate Spider's standard published policies, codes of conduct, or terms of service.Any violation of this Spider AI Policy or any Spider policies or terms of service may result in termination of use of services at Spider's sole discretion. We will review and update this Spider AI Policy so that it remains relevant and effective. If you have feedback or would like to report any concerns or issues related to the use of AI systems, please reach out to \[support@spider.cloud\](mailto:support@spider.cloud).\[More Information----------\](#more-information)To learn more about Spider's integration of AI capabilities into products and features, check out the following resources:\* \[Spider-Rust\](https://github.com/spider-rs)\* \[Spider\](/)\* \[About\](/)\[API\](/docs/api) \[Pricing\](/credits/new) \[Guides\](/guides) \[About\](/about) \[Docs\](https://docs.rs/spider/latest/spider/) \[Privacy\](/privacy) \[Terms\](/eula)© 2024 Spider from A11yWatchTheme Light Dark Toggle Theme \[GitHubGithub\](https://github.com/spider-rs/spider)", start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), Document(id\_='18e4d35d-ff48-4d00-b924-abab7a06fbec', embedding=None, metadata={'description': 'Learn how to crawl and scrape websites with the fastest web crawler built for the job.', 'domain': 'spider.cloud', 'extracted\_data': None, 'file\_size': 27058, 'keywords': None, 'pathname': '/guides', 'resource\_type': 'html', 'title': 'Spider Guides', 'url': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48/spider.cloud/guides.html', 'user\_id': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='Spider Guides\[Spider v1 Logo Spider \](/) \[Credits\](/credits/new)\[GitHubGithub637\](https://github.com/spider-rs/spider)Spider Guides==========Learn how to crawl and scrape websites easily.(4) Total Guides\* \[  Spider v1 Logo  Spider Platform  ----------  How to use the platform to collect data from the internet fast, affordable, and unblockable.  \](/guides/spider)\* \[  Spider v1 Logo  Spider API  ----------  How to use the Spider API to curate data from any source blazing fast. The most advanced crawler that handles all workloads of all sizes.  \](/guides/spider-api)\* \[  Spider v1 Logo  Extract Contacts  ----------  Get contact information from any website in real time with AI. The only way to accurately get dynamic information from websites.  \](/guides/pipelines-extract-contacts)\* \[  Spider v1 Logo  Website Archiving  ----------  The programmable time machine that can store pages and all assets for easy website archiving.  \](/guides/website-archiving)\[API\](/docs/api) \[Pricing\](/credits/new) \[Guides\](/guides) \[About\](/about) \[Docs\](https://docs.rs/spider/latest/spider/) \[Privacy\](/privacy) \[Terms\](/eula)© 2024 Spider from A11yWatchTheme Light Dark Toggle Theme \[GitHubGithub\](https://github.com/spider-rs/spider)', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), Document(id\_='b10c6402-bc35-4fec-b97c-fa30bde54ce8', embedding=None, metadata={'description': 'Complete reference documentation for the Spider API. Includes code snippets and examples for quickly getting started with the system.', 'domain': 'spider.cloud', 'extracted\_data': None, 'file\_size': 195426, 'keywords': None, 'pathname': '/docs/api', 'resource\_type': 'html', 'title': 'Spider API Reference', 'url': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48/spider.cloud/docs\*\_\*api.html', 'user\_id': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='Spider API Reference\[Spider v1 Logo Spider \](/) \[Credits\](/credits/new)\[GitHubGithub637\](https://github.com/spider-rs/spider)API Reference==========The Spider API is based on REST. Our API is predictable, returns \[JSON-encoded\](http://www.json.org/) responses, uses standard HTTP response codes, authentication, and verbs. Set your API secret key in the \`authorization\` header to commence. You can use the \`content-type\` header with \`application/json\`, \`application/xml\`, \`text/csv\`, and \`application/jsonl\` for shaping the response.The Spider API supports multi domain actions. You can work with multiple domains per request by adding the urls comma separated.The Spider API differs for every account as we release new versions and tailor functionality. You can add \`v1\` before any path to pin to the version.Just getting started?----------Check out our \[development quickstart\](/guides/spider-api) guide.Not a developer?----------Use Spiders \[no-code options or apps\](/guides/spider) to get started with Spider and to do more with your Spider account no code required.Base UrlJSONCopy\`\`\`https://api.spider.cloud\`\`\`Crawl websites==========Start crawling a website(s) to collect resources.POST https://api.spider.cloud/crawlRequest body\* url\\xa0required\\xa0string  ----------  The URI resource to crawl. This can be a comma split list for multiple urls.  Test Url\* request\\xa0string  ----------  The request type to perform. Possible values are \`http\`, \`chrome\`, and \`smart\`. Use \`smart\` to perform HTTP request by default until JavaScript rendering is needed for the HTML.  HTTP\* limit\\xa0number  ----------  The maximum amount of pages allowed to crawl per website. Remove the value or set it to 0 to crawl all pages.  Crawl Limit\* depth\\xa0number  ----------  The crawl limit for maximum depth. If zero, no limit will be applied.  Crawl DepthSet Example\* cache\\xa0boolean  ----------  Use HTTP caching for the crawl to speed up repeated runs.  Set Example\* budget\\xa0object  ----------  Object that has paths with a counter for limiting the amount of pages example \`{"\*":1}\` for only crawling the root page. The wildcard matches all routes and you can set child paths preventing a depth level, example of limiting \`{ "/docs/colors": 10, "/docs/": 100 }\` which only allows a max of 100 pages if the route matches \`/docs/:pathname\` and only 10 pages if it matches \`/docs/colors/:pathname\`.  Crawl Budget  Set Example\* locale\\xa0string  ----------  The locale to use for request, example \`en-US\`.  Set Example\* cookies\\xa0string  ----------  Add HTTP cookies to use for request.  Set Example\* stealth\\xa0boolean  ----------  Use stealth mode for headless chrome request to help prevent being blocked. The default is enabled on chrome.  Set Example\* headers\\xa0string  ----------  Forward HTTP headers to use for all request. The object is expected to be a map of key value pairs.  Set Example\* metadata\\xa0boolean  ----------  Boolean to store metadata about the pages and content found. This could help improve AI interopt. Defaults to false unless you have the website already stored with the configuration enabled.  Set Example\* viewport\\xa0object  ----------  Configure the viewport for chrome. Defaults to 800x600.  Set Example\* encoding\\xa0string  ----------  The type of encoding to use like \`UTF-8\`, \`SHIFT\_JIS\`, or etc.  Set Example\* subdomains\\xa0boolean  ----------  Allow subdomains to be included.  Set Example\* user\\\\\_agent\\xa0string  ----------  Add a custom HTTP user agent to the request.  Set Example\* store\\\\\_data\\xa0boolean  ----------  Boolean to determine if storage should be used. If set this takes precedence over \`storageless\`. Defaults to false.  Set Example\* gpt\\\\\_config\\xa0object  ----------  Use AI to generate actions to perform during the crawl. You can pass an array for the\`"prompt"\` to chain steps.  Set Example\* fingerprint\\xa0boolean  ----------  Use advanced fingerprint for chrome.  Set Example\* storageless\\xa0boolean  ----------  Boolean to prevent storing any type of data for the request including storage and AI vectors embedding. Defaults to false unless you have the website already stored.  Set Example\* readability\\xa0boolean  ----------  Use \[readability\](https://github.com/mozilla/readability) to pre-process the content for reading. This may drastically improve the content for LLM usage.  Set Example\* return\\\\\_format\\xa0string  ----------  The format to return the data in. Possible values are \`markdown\`, \`raw\`, \`text\`, and \`html2text\`. Use \`raw\` to return the default format of the page like \`HTML\` etc.  Raw\* proxy\\\\\_enabled\\xa0boolean  ----------  Enable high performance premium proxies for the request to prevent being blocked at the network level.  Set Example\* query\\\\\_selector\\xa0string  ----------  The CSS query selector to use when extracting content from the markup.  Test Query Selector\* full\\\\\_resources\\xa0boolean  ----------  Crawl and download all the resources for a website.  Set Example\* request\\\\\_timeout\\xa0number  ----------  The timeout to use for request. Timeouts can be from 5-60. The default is 30 seconds.  Set Example\* run\\\\\_in\\\\\_background\\xa0boolean  ----------  Run the request in the background. Useful if storing data and wanting to trigger crawls to the dashboard. This has no effect if storageless is set.  Set ExampleShow More Properties\* Basic\* StreamingExample requestPythonCopy\`\`\`import requests, osheaders = {    \\'Authorization\\': os.environ\["SPIDER\_API\_KEY"\],    \\'Content-Type\\': \\'application/json\\',}json\_data = {"limit":50,"url":"http://www.example.com"}response = requests.post(\\'https://api.spider.cloud/crawl\\',  headers=headers,  json=json\_data)print(response.json())\`\`\`ResponseCopy\`\`\`\[  {    "content": "<html>...",    "error": null,    "status": 200,    "url": "http://www.example.com"  },  // more content...\]\`\`\`Crawl websites get links==========Start crawling a website(s) to collect links found.POST https://api.spider.cloud/linksRequest body\* url\\xa0required\\xa0string  ----------  The URI resource to crawl. This can be a comma split list for multiple urls.  Test Url\* request\\xa0string  ----------  The request type to perform. Possible values are \`http\`, \`chrome\`, and \`smart\`. Use \`smart\` to perform HTTP request by default until JavaScript rendering is needed for the HTML.  HTTP\* limit\\xa0number  ----------  The maximum amount of pages allowed to crawl per website. Remove the value or set it to 0 to crawl all pages.  Crawl Limit\* depth\\xa0number  ----------  The crawl limit for maximum depth. If zero, no limit will be applied.  Crawl DepthSet Example\* cache\\xa0boolean  ----------  Use HTTP caching for the crawl to speed up repeated runs.  Set Example\* budget\\xa0object  ----------  Object that has paths with a counter for limiting the amount of pages example \`{"\*":1}\` for only crawling the root page. The wildcard matches all routes and you can set child paths preventing a depth level, example of limiting \`{ "/docs/colors": 10, "/docs/": 100 }\` which only allows a max of 100 pages if the route matches \`/docs/:pathname\` and only 10 pages if it matches \`/docs/colors/:pathname\`.  Crawl Budget  Set Example\* locale\\xa0string  ----------  The locale to use for request, example \`en-US\`.  Set Example\* cookies\\xa0string  ----------  Add HTTP cookies to use for request.  Set Example\* stealth\\xa0boolean  ----------  Use stealth mode for headless chrome request to help prevent being blocked. The default is enabled on chrome.  Set Example\* headers\\xa0string  ----------  Forward HTTP headers to use for all request. The object is expected to be a map of key value pairs.  Set Example\* metadata\\xa0boolean  ----------  Boolean to store metadata about the pages and content found. This could help improve AI interopt. Defaults to false unless you have the website already stored with the configuration enabled.  Set Example\* viewport\\xa0object  ----------  Configure the viewport for chrome. Defaults to 800x600.  Set Example\* encoding\\xa0string  ----------  The type of encoding to use like \`UTF-8\`, \`SHIFT\_JIS\`, or etc.  Set Example\* subdomains\\xa0boolean  ----------  Allow subdomains to be included.  Set Example\* user\\\\\_agent\\xa0string  ----------  Add a custom HTTP user agent to the request.  Set Example\* store\\\\\_data\\xa0boolean  ----------  Boolean to determine if storage should be used. If set this takes precedence over \`storageless\`. Defaults to false.  Set Example\* gpt\\\\\_config\\xa0object  ----------  Use AI to generate actions to perform during the crawl. You can pass an array for the\`"prompt"\` to chain steps.  Set Example\* fingerprint\\xa0boolean  ----------  Use advanced fingerprint for chrome.  Set Example\* storageless\\xa0boolean  ----------  Boolean to prevent storing any type of data for the request including storage and AI vectors embedding. Defaults to false unless you have the website already stored.  Set Example\* readability\\xa0boolean  ----------  Use \[readability\](https://github.com/mozilla/readability) to pre-process the content for reading. This may drastically improve the content for LLM usage.  Set Example\* return\\\\\_format\\xa0string  ----------  The format to return the data in. Possible values are \`markdown\`, \`raw\`, \`text\`, and \`html2text\`. Use \`raw\` to return the default format of the page like \`HTML\` etc.  Raw\* proxy\\\\\_enabled\\xa0boolean  ----------  Enable high performance premium proxies for the request to prevent being blocked at the network level.  Set Example\* query\\\\\_selector\\xa0string  ----------  The CSS query selector to use when extracting content from the markup.  Test Query Selector\* full\\\\\_resources\\xa0boolean  ----------  Crawl and download all the resources for a website.  Set Example\* request\\\\\_timeout\\xa0number  ----------  The timeout to use for request. Timeouts can be from 5-60. The default is 30 seconds.  Set Example\* run\\\\\_in\\\\\_background\\xa0boolean  ----------  Run the request in the background. Useful if storing data and wanting to trigger crawls to the dashboard. This has no effect if storageless is set.  Set ExampleShow More Properties\* Basic\* StreamingExample requestPythonCopy\`\`\`import requests, osheaders = {    \\'Authorization\\': os.environ\["SPIDER\_API\_KEY"\],    \\'Content-Type\\': \\'application/json\\',}json\_data = {"limit":50,"url":"http://www.example.com"}response = requests.post(\\'https://api.spider.cloud/links\\',  headers=headers,  json=json\_data)print(response.json())\`\`\`ResponseCopy\`\`\`\[  {    "content": "",    "error": null,    "status": 200,    "url": "http://www.example.com"  },  // more content...\]\`\`\`Screenshot websites==========Start taking screenshots of website(s) to collect images to base64 or binary.POST https://api.spider.cloud/screenshotRequest bodyGeneralSpecific\* url\\xa0required\\xa0string  ----------  The URI resource to crawl. This can be a comma split list for multiple urls.  Test Url\* request\\xa0string  ----------  The request type to perform. Possible values are \`http\`, \`chrome\`, and \`smart\`. Use \`smart\` to perform HTTP request by default until JavaScript rendering is needed for the HTML.  HTTP\* limit\\xa0number  ----------  The maximum amount of pages allowed to crawl per website. Remove the value or set it to 0 to crawl all pages.  Crawl Limit\* depth\\xa0number  ----------  The crawl limit for maximum depth. If zero, no limit will be applied.  Crawl DepthSet Example\* cache\\xa0boolean  ----------  Use HTTP caching for the crawl to speed up repeated runs.  Set Example\* budget\\xa0object  ----------  Object that has paths with a counter for limiting the amount of pages example \`{"\*":1}\` for only crawling the root page. The wildcard matches all routes and you can set child paths preventing a depth level, example of limiting \`{ "/docs/colors": 10, "/docs/": 100 }\` which only allows a max of 100 pages if the route matches \`/docs/:pathname\` and only 10 pages if it matches \`/docs/colors/:pathname\`.  Crawl Budget  Set Example\* locale\\xa0string  ----------  The locale to use for request, example \`en-US\`.  Set Example\* cookies\\xa0string  ----------  Add HTTP cookies to use for request.  Set Example\* stealth\\xa0boolean  ----------  Use stealth mode for headless chrome request to help prevent being blocked. The default is enabled on chrome.  Set Example\* headers\\xa0string  ----------  Forward HTTP headers to use for all request. The object is expected to be a map of key value pairs.  Set Example\* metadata\\xa0boolean  ----------  Boolean to store metadata about the pages and content found. This could help improve AI interopt. Defaults to false unless you have the website already stored with the configuration enabled.  Set Example\* viewport\\xa0object  ----------  Configure the viewport for chrome. Defaults to 800x600.  Set Example\* encoding\\xa0string  ----------  The type of encoding to use like \`UTF-8\`, \`SHIFT\_JIS\`, or etc.  Set Example\* subdomains\\xa0boolean  ----------  Allow subdomains to be included.  Set Example\* user\\\\\_agent\\xa0string  ----------  Add a custom HTTP user agent to the request.  Set Example\* store\\\\\_data\\xa0boolean  ----------  Boolean to determine if storage should be used. If set this takes precedence over \`storageless\`. Defaults to false.  Set Example\* gpt\\\\\_config\\xa0object  ----------  Use AI to generate actions to perform during the crawl. You can pass an array for the\`"prompt"\` to chain steps.  Set Example\* fingerprint\\xa0boolean  ----------  Use advanced fingerprint for chrome.  Set Example\* storageless\\xa0boolean  ----------  Boolean to prevent storing any type of data for the request including storage and AI vectors embedding. Defaults to false unless you have the website already stored.  Set Example\* readability\\xa0boolean  ----------  Use \[readability\](https://github.com/mozilla/readability) to pre-process the content for reading. This may drastically improve the content for LLM usage.  Set Example\* return\\\\\_format\\xa0string  ----------  The format to return the data in. Possible values are \`markdown\`, \`raw\`, \`text\`, and \`html2text\`. Use \`raw\` to return the default format of the page like \`HTML\` etc.  Raw\* proxy\\\\\_enabled\\xa0boolean  ----------  Enable high performance premium proxies for the request to prevent being blocked at the network level.  Set Example\* query\\\\\_selector\\xa0string  ----------  The CSS query selector to use when extracting content from the markup.  Test Query Selector\* full\\\\\_resources\\xa0boolean  ----------  Crawl and download all the resources for a website.  Set Example\* request\\\\\_timeout\\xa0number  ----------  The timeout to use for request. Timeouts can be from 5-60. The default is 30 seconds.  Set Example\* run\\\\\_in\\\\\_background\\xa0boolean  ----------  Run the request in the background. Useful if storing data and wanting to trigger crawls to the dashboard. This has no effect if storageless is set.  Set ExampleShow More Properties\* Basic\* StreamingExample requestPythonCopy\`\`\`import requests, osheaders = {    \\'Authorization\\': os.environ\["SPIDER\_API\_KEY"\],    \\'Content-Type\\': \\'application/json\\',}json\_data = {"limit":50,"url":"http://www.example.com"}response = requests.post(\\'https://api.spider.cloud/screenshot\\',  headers=headers,  json=json\_data)print(response.json())\`\`\`ResponseCopy\`\`\`\[  {    "content": "base64...",    "error": null,    "status": 200,    "url": "http://www.example.com"  },  // more content...\]\`\`\`Pipelines----------Create powerful workflows with our pipeline API endpoints. Use AI to extract contacts from any website or filter links with prompts with ease.Crawl websites and extract contacts==========Start crawling a website(s) to collect all contacts found leveraging AI.POST https://api.spider.cloud/pipeline/extract-contactsRequest bodyGeneralSpecific\* url\\xa0required\\xa0string  ----------  The URI resource to crawl. This can be a comma split list for multiple urls.  Test Url\* request\\xa0string  ----------  The request type to perform. Possible values are \`http\`, \`chrome\`, and \`smart\`. Use \`smart\` to perform HTTP request by default until JavaScript rendering is needed for the HTML.  HTTP\* limit\\xa0number  ----------  The maximum amount of pages allowed to crawl per website. Remove the value or set it to 0 to crawl all pages.  Crawl Limit\* depth\\xa0number  ----------  The crawl limit for maximum depth. If zero, no limit will be applied.  Crawl DepthSet Example\* cache\\xa0boolean  ----------  Use HTTP caching for the crawl to speed up repeated runs.  Set Example\* budget\\xa0object  ----------  Object that has paths with a counter for limiting the amount of pages example \`{"\*":1}\` for only crawling the root page. The wildcard matches all routes and you can set child paths preventing a depth level, example of limiting \`{ "/docs/colors": 10, "/docs/": 100 }\` which only allows a max of 100 pages if the route matches \`/docs/:pathname\` and only 10 pages if it matches \`/docs/colors/:pathname\`.  Crawl Budget  Set Example\* locale\\xa0string  ----------  The locale to use for request, example \`en-US\`.  Set Example\* cookies\\xa0string  ----------  Add HTTP cookies to use for request.  Set Example\* stealth\\xa0boolean  ----------  Use stealth mode for headless chrome request to help prevent being blocked. The default is enabled on chrome.  Set Example\* headers\\xa0string  ----------  Forward HTTP headers to use for all request. The object is expected to be a map of key value pairs.  Set Example\* metadata\\xa0boolean  ----------  Boolean to store metadata about the pages and content found. This could help improve AI interopt. Defaults to false unless you have the website already stored with the configuration enabled.  Set Example\* viewport\\xa0object  ----------  Configure the viewport for chrome. Defaults to 800x600.  Set Example\* encoding\\xa0string  ----------  The type of encoding to use like \`UTF-8\`, \`SHIFT\_JIS\`, or etc.  Set Example\* subdomains\\xa0boolean  ----------  Allow subdomains to be included.  Set Example\* user\\\\\_agent\\xa0string  ----------  Add a custom HTTP user agent to the request.  Set Example\* store\\\\\_data\\xa0boolean  ----------  Boolean to determine if storage should be used. If set this takes precedence over \`storageless\`. Defaults to false.  Set Example\* gpt\\\\\_config\\xa0object  ----------  Use AI to generate actions to perform during the crawl. You can pass an array for the\`"prompt"\` to chain steps.  Set Example\* fingerprint\\xa0boolean  ----------  Use advanced fingerprint for chrome.  Set Example\* storageless\\xa0boolean  ----------  Boolean to prevent storing any type of data for the request including storage and AI vectors embedding. Defaults to false unless you have the website already stored.  Set Example\* readability\\xa0boolean  ----------  Use \[readability\](https://github.com/mozilla/readability) to pre-process the content for reading. This may drastically improve the content for LLM usage.  Set Example\* return\\\\\_format\\xa0string  ----------  The format to return the data in. Possible values are \`markdown\`, \`raw\`, \`text\`, and \`html2text\`. Use \`raw\` to return the default format of the page like \`HTML\` etc.  Raw\* proxy\\\\\_enabled\\xa0boolean  ----------  Enable high performance premium proxies for the request to prevent being blocked at the network level.  Set Example\* query\\\\\_selector\\xa0string  ----------  The CSS query selector to use when extracting content from the markup.  Test Query Selector\* full\\\\\_resources\\xa0boolean  ----------  Crawl and download all the resources for a website.  Set Example\* request\\\\\_timeout\\xa0number  ----------  The timeout to use for request. Timeouts can be from 5-60. The default is 30 seconds.  Set Example\* run\\\\\_in\\\\\_background\\xa0boolean  ----------  Run the request in the background. Useful if storing data and wanting to trigger crawls to the dashboard. This has no effect if storageless is set.  Set ExampleShow More Properties\* Basic\* StreamingExample requestPythonCopy\`\`\`import requests, osheaders = {    \\'Authorization\\': os.environ\["SPIDER\_API\_KEY"\],    \\'Content-Type\\': \\'application/json\\',}json\_data = {"limit":50,"url":"http://www.example.com"}response = requests.post(\\'https://api.spider.cloud/pipeline/extract-contacts\\',  headers=headers,  json=json\_data)print(response.json())\`\`\`ResponseCopy\`\`\`\[  {    "content": \[{ "full\_name": "John Doe", "email": "johndoe@gmail.com", "phone": "555-555-555", "title": "Baker"}, ...\],    "error": null,    "status": 200,    "url": "http://www.example.com"  },  // more content...\]\`\`\`Label website==========Crawl a website and accurately categorize it using AI.POST https://api.spider.cloud/pipeline/labelRequest bodyGeneralSpecific\* url\\xa0required\\xa0string  ----------  The URI resource to crawl. This can be a comma split list for multiple urls.  Test Url\* request\\xa0string  ----------  The request type to perform. Possible values are \`http\`, \`chrome\`, and \`smart\`. Use \`smart\` to perform HTTP request by default until JavaScript rendering is needed for the HTML.  HTTP\* limit\\xa0number  ----------  The maximum amount of pages allowed to crawl per website. Remove the value or set it to 0 to crawl all pages.  Crawl Limit\* depth\\xa0number  ----------  The crawl limit for maximum depth. If zero, no limit will be applied.  Crawl DepthSet Example\* cache\\xa0boolean  ----------  Use HTTP caching for the crawl to speed up repeated runs.  Set Example\* budget\\xa0object  ----------  Object that has paths with a counter for limiting the amount of pages example \`{"\*":1}\` for only crawling the root page. The wildcard matches all routes and you can set child paths preventing a depth level, example of limiting \`{ "/docs/colors": 10, "/docs/": 100 }\` which only allows a max of 100 pages if the route matches \`/docs/:pathname\` and only 10 pages if it matches \`/docs/colors/:pathname\`.  Crawl Budget  Set Example\* locale\\xa0string  ----------  The locale to use for request, example \`en-US\`.  Set Example\* cookies\\xa0string  ----------  Add HTTP cookies to use for request.  Set Example\* stealth\\xa0boolean  ----------  Use stealth mode for headless chrome request to help prevent being blocked. The default is enabled on chrome.  Set Example\* headers\\xa0string  ----------  Forward HTTP headers to use for all request. The object is expected to be a map of key value pairs.  Set Example\* metadata\\xa0boolean  ----------  Boolean to store metadata about the pages and content found. This could help improve AI interopt. Defaults to false unless you have the website already stored with the configuration enabled.  Set Example\* viewport\\xa0object  ----------  Configure the viewport for chrome. Defaults to 800x600.  Set Example\* encoding\\xa0string  ----------  The type of encoding to use like \`UTF-8\`, \`SHIFT\_JIS\`, or etc.  Set Example\* subdomains\\xa0boolean  ----------  Allow subdomains to be included.  Set Example\* user\\\\\_agent\\xa0string  ----------  Add a custom HTTP user agent to the request.  Set Example\* store\\\\\_data\\xa0boolean  ----------  Boolean to determine if storage should be used. If set this takes precedence over \`storageless\`. Defaults to false.  Set Example\* gpt\\\\\_config\\xa0object  ----------  Use AI to generate actions to perform during the crawl. You can pass an array for the\`"prompt"\` to chain steps.  Set Example\* fingerprint\\xa0boolean  ----------  Use advanced fingerprint for chrome.  Set Example\* storageless\\xa0boolean  ----------  Boolean to prevent storing any type of data for the request including storage and AI vectors embedding. Defaults to false unless you have the website already stored.  Set Example\* readability\\xa0boolean  ----------  Use \[readability\](https://github.com/mozilla/readability) to pre-process the content for reading. This may drastically improve the content for LLM usage.  Set Example\* return\\\\\_format\\xa0string  ----------  The format to return the data in. Possible values are \`markdown\`, \`raw\`, \`text\`, and \`html2text\`. Use \`raw\` to return the default format of the page like \`HTML\` etc.  Raw\* proxy\\\\\_enabled\\xa0boolean  ----------  Enable high performance premium proxies for the request to prevent being blocked at the network level.  Set Example\* query\\\\\_selector\\xa0string  ----------  The CSS query selector to use when extracting content from the markup.  Test Query Selector\* full\\\\\_resources\\xa0boolean  ----------  Crawl and download all the resources for a website.  Set Example\* request\\\\\_timeout\\xa0number  ----------  The timeout to use for request. Timeouts can be from 5-60. The default is 30 seconds.  Set Example\* run\\\\\_in\\\\\_background\\xa0boolean  ----------  Run the request in the background. Useful if storing data and wanting to trigger crawls to the dashboard. This has no effect if storageless is set.  Set ExampleShow More Properties\* Basic\* StreamingExample requestPythonCopy\`\`\`import requests, osheaders = {    \\'Authorization\\': os.environ\["SPIDER\_API\_KEY"\],    \\'Content-Type\\': \\'application/json\\',}json\_data = {"limit":50,"url":"http://www.example.com"}response = requests.post(\\'https://api.spider.cloud/pipeline/label\\',  headers=headers,  json=json\_data)print(response.json())\`\`\`ResponseCopy\`\`\`\[  {    "content": \["Government"\],    "error": null,    "status": 200,    "url": "http://www.example.com"  },  // more content...\]\`\`\`Crawl State==========Get the state of the crawl for the domain.POST https://api.spider.cloud/crawl/statusRequest body\* url\\xa0required\\xa0string  ----------  The URI resource to crawl. This can be a comma split list for multiple urls.  Test UrlShow More Properties\* Basic\* StreamingExample requestPythonCopy\`\`\`import requests, osheaders = {    \\'Authorization\\': os.environ\["SPIDER\_API\_KEY"\],    \\'Content-Type\\': \\'application/json\\',}response = requests.post(\\'https://api.spider.cloud/crawl/status\\',  headers=headers)print(response.json())\`\`\`ResponseCopy\`\`\`  {    "content": {        "data": {          "id": "195bf2f2-2821-421d-b89c-f27e57ca71fh",          "user\_id": "6bd06efa-bb0a-4f1f-a29f-05db0c4b1bfg",          "domain": "example.com",          "url": "https://example.com/",          "links":1,          "credits\_used": 3,          "mode":2,          "crawl\_duration": 340,          "message": null,          "request\_user\_agent": "Spider",          "level": "info",          "status\_code": 0,          "created\_at": "2024-04-21T01:21:32.886863+00:00",          "updated\_at": "2024-04-21T01:21:32.886863+00:00"        },        "error": ""      },    "error": null,    "status": 200,    "url": "http://www.example.com"  }\`\`\`Credits Available==========Get the remaining credits available.GET https://api.spider.cloud/credits\* Basic\* StreamingExample requestPythonCopy\`\`\`import requests, osheaders = {    \\'Authorization\\': os.environ\["SPIDER\_API\_KEY"\],    \\'Content-Type\\': \\'application/json\\',}response = requests.post(\\'https://api.spider.cloud/credits\\',  headers=headers)print(response.json())\`\`\`ResponseCopy\`\`\`{ "credits": 52566 }\`\`\`\[API\](/docs/api) \[Pricing\](/credits/new) \[Guides\](/guides) \[About\](/about) \[Docs\](https://docs.rs/spider/latest/spider/) \[Privacy\](/privacy) \[Terms\](/eula)© 2024 Spider from A11yWatchTheme Light Dark Toggle Theme \[GitHubGithub\](https://github.com/spider-rs/spider)', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), Document(id\_='44b350c3-f907-4767-84ec-a73fe59c190c', embedding=None, metadata={'description': 'End User License Agreement for the Spiderwebai and the spider project.', 'domain': 'spider.cloud', 'extracted\_data': None, 'file\_size': 20123, 'keywords': None, 'pathname': '/eula', 'resource\_type': 'html', 'title': 'EULA', 'url': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48/spider.cloud/eula.html', 'user\_id': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='EULA\[Spider v1 Logo Spider \](/) \[Credits\](/credits/new)\[GitHubGithub637\](https://github.com/spider-rs/spider)End User License Agreement==========Our end user license agreement may change from time to time as we build out the software.Right to Ban----------Part of making sure the Spider is being used for the right purpose we will not allow malicious acts to be done with the system. If we find that you are using the tool to hack, crawl illegal pages, porn, or anything that falls into this line will be banned from the system. You can reach out to us to weigh out your reasons on why you should not be banned.License----------You can use the API and service to build ontop of. Replicating the features and re-selling the service is not allowed. We do not provide any custom license for the platform and encourage users to use our system to handle any crawling, scraping, or data curation needs for speed and cost effectiveness.### Adjustments to Plans ###The software is very new and while we figure out what we can charge to maintain the systems the plans may change. We will send out a notification of the changes in our \[Discord\](https://discord.gg/5bDPDxwTn3) or Github. For the most part plans will increase drastically with things set to scale costs that allow more usage for everyone. Spider is a product of\[A11yWatch LLC\](https://a11ywatch.com) the web accessibility tool. The crawler engine of Spider powers the curation for A11yWatch allowing auditing websites accessibility compliance extremely fast.#### Contact ####For information about how to contact Spider, please reach out to email below.\[support@spider.cloud\](mailto:support@spider.cloud)\[API\](/docs/api) \[Pricing\](/credits/new) \[Guides\](/guides) \[About\](/about) \[Docs\](https://docs.rs/spider/latest/spider/) \[Privacy\](/privacy) \[Terms\](/eula)© 2024 Spider from A11yWatchTheme Light Dark Toggle Theme \[GitHubGithub\](https://github.com/spider-rs/spider)', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), Document(id\_='445c0c76-bfd5-4f89-a439-fbdeb8077a4c', embedding=None, metadata={'description': 'Spider is the fastest web crawler written in Rust. The Cloud version is a hosted version of open-source project.', 'domain': 'spider.cloud', 'extracted\_data': None, 'file\_size': 139080, 'keywords': None, 'pathname': '/about', 'resource\_type': 'html', 'title': 'About', 'url': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48/spider.cloud/about.html', 'user\_id': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='About\[Spider v1 Logo Spider \](/) \[Credits\](/credits/new)\[GitHubGithub637\](https://github.com/spider-rs/spider) About==========Spider is the fastest web crawler written in Rust. The Cloud version is a hosted version of open-source project. Spider Features----------Our features that facilitate website scraping and provide swift insights in one platform. Deliver astonishing results using our powerful API.### Fast Unblockable Scraping ###When it comes to speed, the Spider project is the fastest web crawler available to the public. Utilize the foundation of open-source tools and make the most of your budget to scrape content effectively.Collecting Data Logo### Gain Website Insights with AI ###Enhance your crawls with AI to obtain relevant information fast from any website.AI Search### Extract Data Using Webhooks ###Set up webhooks across your websites to deliver the desired information anywhere you need.News Logo\[A11yWatch\](https://a11ywatch.com)maintains the project and the hosting for the service.\[API\](/docs/api) \[Pricing\](/credits/new) \[Guides\](/guides) \[About\](/about) \[Docs\](https://docs.rs/spider/latest/spider/) \[Privacy\](/privacy) \[Terms\](/eula)© 2024 Spider from A11yWatchTheme Light Dark Toggle Theme \[GitHubGithub\](https://github.com/spider-rs/spider)', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), Document(id\_='1a2d63a5-0315-4c5b-8fed-8ac460b82cc7', embedding=None, metadata={'description': 'Add the amount of credits you want to purchase for scraping the internet with AI and LLM data curation abilities fast.', 'domain': 'spider.cloud', 'extracted\_data': None, 'file\_size': 23083, 'keywords': None, 'pathname': '/credits/new', 'resource\_type': 'html', 'title': 'Purchase Spider Credits', 'url': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48/spider.cloud/credits\*\_\*new.html', 'user\_id': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='Purchase Spider Credits\[Spider v1 Logo Spider \](/) \[Credits\](/credits/new)\[GitHubGithub637\](https://github.com/spider-rs/spider)Add credits==========Add credits to start crawling any website today.|Default|      Features      |       Amount       ||-------|--------------------|--------------------||Default| Scraping Websites  |$0.03 / gb bandwidth|| Extra |  Premium Proxies   |$0.01 / gb bandwidth|| Extra |Javascript Rendering|$0.01 / gb bandwidth|| Extra |    Data Storage    |  $0.30 / gb month  || Extra |      AI Chat       | $0.01 input/output |\[API\](/docs/api) \[Pricing\](/credits/new) \[Guides\](/guides) \[About\](/about) \[Docs\](https://docs.rs/spider/latest/spider/) \[Privacy\](/privacy) \[Terms\](/eula)© 2024 Spider from A11yWatchTheme Light Dark Toggle Theme \[GitHubGithub\](https://github.com/spider-rs/spider)', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), Document(id\_='6701b47a-0000-4111-8b5b-c77b01937a7d', embedding=None, metadata={'description': 'Collect data rapidly from any website. Seamlessly scrape websites and get data tailored for LLM workloads.', 'domain': 'spider.cloud', 'extracted\_data': None, 'file\_size': 101750, 'keywords': None, 'pathname': '/', 'resource\_type': 'html', 'title': 'Spider - Fastest Web Crawler', 'url': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48/spider.cloud/index.html', 'user\_id': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='Spider - Fastest Web Crawler\[Spider v1 Logo Spider \](/)\[Pricing\](/credits/new)\[GitHubGithub637\](https://github.com/spider-rs/spider)The World\\'s Fastest and Cheapest Crawler API==========View Demo\* Basic\* StreamingExample requestPythonCopy\`\`\`import requests, osheaders = {    \\'Authorization\\': os.environ\["SPIDER\_API\_KEY"\],    \\'Content-Type\\': \\'application/json\\',}json\_data = {"limit":50,"url":"http://www.example.com"}response = requests.post(\\'https://api.spider.cloud/crawl\\',  headers=headers,  json=json\_data)print(response.json())\`\`\`Example ResponseUnmatched Speed----------### 5secs  ###To crawl 200 pages### 21x  ###Faster than FireCrawl### 150x  ###Faster than Apify Benchmarks displaying performance between Spider Cloud, Firecrawl, and Apify.\[See framework benchmarks \](https://github.com/spider-rs/spider/blob/main/benches/BENCHMARKS.md)Foundations for Crawling Effectively----------### Leading in performance ###Spider is written in Rust and runs in full concurrency to achieve crawling dozens of pages in secs.### Optimal response format ###Get clean and formatted markdown, HTML, or text content for fine-tuning or training AI models.### Caching ###Further boost speed by caching repeated web page crawls.### Smart Mode ###Spider dynamically switches to Headless Chrome when it needs to.Beta### Scrape with AI ###Do custom browser scripting and data extraction using the latest AI models.### Best crawler for LLMs ###Don\\'t let crawling and scraping be the highest latency in your LLM & AI agent stack.### Scrape with no headaches ###\* Proxy rotations\* Agent headers\* Avoid anti-bot detections\* Headless chrome\* Markdown LLM Responses### The Fastest Web Crawler ###\* Powered by \[spider-rs\](https://github.com/spider-rs/spider)\* Do 20,000 pages in seconds\* Full concurrency\* Powerful and simple API\* 5,000 requests per minute### Do more with AI ###\* Custom browser scripting\* Advanced data extraction\* Data pipelines\* Perfect for LLM and AI Agents\* Accurate website labeling\[API\](/docs/api) \[Pricing\](/credits/new) \[Guides\](/guides) \[About\](/about) \[Docs\](https://docs.rs/spider/latest/spider/) \[Privacy\](/privacy) \[Terms\](/eula)© 2024 Spider from A11yWatchTheme Light Dark Toggle Theme \[GitHubGithub\](https://github.com/spider-rs/spider)', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), Document(id\_='91b98a80-7112-4837-8389-cb78221b254c', embedding=None, metadata={'description': 'Get contact information from any website in real time with AI. The only way to accurately get dynamic information from websites.', 'domain': 'spider.cloud', 'extracted\_data': None, 'file\_size': 25891, 'keywords': None, 'pathname': '/guides/pipelines-extract-contacts', 'resource\_type': 'html', 'title': 'Guides - Extract Contacts', 'url': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48/spider.cloud/guides\*\_\*pipelines-extract-contacts.html', 'user\_id': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='Guides - Extract Contacts\[Spider v1 Logo Spider \](/) \[Credits\](/credits/new)\[GitHubGithub637\](https://github.com/spider-rs/spider)Extract Contacts==========Contents----------\* \[Seamless extracting any contact any website\](#seamless-extracting-any-contact-any-website)\* \[UI (Extracting Contacts)\](#ui-extracting-contacts)\* \[API Extracting Usage\](#api-extracting-usage)  \* \[API Extracting Example\](#api-extracting-example)  \* \[Pipelines Combo\](#pipelines-combo)Seamless extracting any contact any website----------Extracting contacts from a website used to be a very difficult challenge involving many steps that would change often. The challenges typically faced involve being able to get the data from a website without being blocked and setting up query selectors for the information you need using javascript. This would often break in two folds - the data extracting with a correct stealth technique or the css selector breaking as they update the website HTML code. Now we toss those two hard challenges away - one of them spider takes care of and the other the advancement in AI to process and extract information.UI (Extracting Contacts)----------You can use the UI on the dashboard to extract contacts after you crawled a page. Go to the page youwant to extract and click on the horizontal dropdown menu to display an option to extract the contact.The crawl will get the data first to see if anything new has changed. Afterwards if a contact was found usually within 10-60 seconds you will get a notification that the extraction is complete with the data.!\[Extracting contacts with the spider app\](/img/app/extract-contacts.png)After extraction if the page has contact related data you can view it with a grid in the app.!\[The menu displaying the found contacts after extracting with the spider app\](/img/app/extract-contacts-found.png)The grid will display the name, email, phone, title, and host(website found) of the contact(s).!\[Grid display of all the contact information found for the web page\](/img/app/extract-contacts-grid.png)API Extracting Usage----------The endpoint \`/pipeline/extract-contacts\` provides the ability to extract all contacts from a website concurrently.### API Extracting Example ###To extract contacts from a website you can follow the example below. All params are optional except \`url\`. Use the \`prompt\` param to adjust the way the AI handles the extracting. If you use the param \`store\_data\` or if the website already exist in the dashboard the contact data will be saved with the page.\`\`\`import requests, os, jsonheaders = {    \\'Authorization\\': os.environ\["SPIDER\_API\_KEY"\],    \\'Content-Type\\': \\'application/json\\',}json\_data = {"limit":1,"url":"http://www.example.com/contacts", "model": "gpt-4-1106-preview", "prompt": "A custom prompt to tailor the extracting."}response = requests.post(\\'https://api.spider.cloud/crawl/pipeline/extract-contacts\\',  headers=headers,  json=json\_data,  stream=True)for line in response.iter\_lines():  if line:      print(json.loads(line))\`\`\`### Pipelines Combo ###Piplines bring a whole new entry to workflows for data curation, if you combine the API endpoints to only use the extraction on pages you know may have contacts can save credits on the system. One way would be to perform gathering all the links first with the \`/links\` endpoint. After getting the links for the pages use \`/pipeline/filter-links\` with a custom prompt that can use AI to reduce the noise of the links to process before \`/pipline/extract-contacts\`.Loading graph...Written on:  2/1/2024\[API\](/docs/api) \[Pricing\](/credits/new) \[Guides\](/guides) \[About\](/about) \[Docs\](https://docs.rs/spider/latest/spider/) \[Privacy\](/privacy) \[Terms\](/eula)© 2024 Spider from A11yWatchTheme Light Dark Toggle Theme \[GitHubGithub\](https://github.com/spider-rs/spider)', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), Document(id\_='5e7ade0d-0a50-46de-8116-72ee5dca0b20', embedding=None, metadata={'description': 'How to use the Spider API to curate data from any source blazing fast. The most advanced crawler that handles all workloads of all sizes.', 'domain': 'spider.cloud', 'extracted\_data': None, 'file\_size': 24752, 'keywords': None, 'pathname': '/guides/spider-api', 'resource\_type': 'html', 'title': 'Guides - Spider API', 'url': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48/spider.cloud/guides\*\_\*spider-api.html', 'user\_id': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='Guides - Spider API\[Spider v1 Logo Spider \](/) \[Credits\](/credits/new)\[GitHubGithub637\](https://github.com/spider-rs/spider)Getting started Spider API==========Contents----------\* \[API built to scale\](#api-built-to-scale)\* \[API Usage\](#api-usage)\* \[Crawling One Page\](#crawling-one-page)\* \[Crawling Multiple Pages\](#crawling-multiple-pages)  \* \[Planet Scale Crawling\](#planet-scale-crawling)    \* \[Automatic Configuration\](#automatic-configuration)API built to scale----------Welcome to our cutting-edge web crawler SaaS, renowned for its unparalleled speed.Our platform is designed to effortlessly manage thousands of requests per second, thanks to our elastically scalable system architecture and the Open-Source \[spider\](https://github.com/spider-rs/spider) project. We deliver consistent latency times ensuring swift processing for all responses.For an in-depth understanding of the request parameters supported, we invite you to explore our comprehensive API documentation. At present, we do not provide client-side libraries, as our API has been crafted with simplicity in mind for straightforward usage. However, we are open to expanding our offerings in the future to enhance user convenience.Dive into our \[documentation\]((/docs/api)) to get started and unleash the full potential of our web crawler today.API Usage----------Getting started with the API is simple and straight forward. After you get your \[secret key\](/api-keys)you can access our instance directly. We have one main endpoint \`/crawl\` that handles all things relatedto data curation. The crawler is highly configurable through the params to fit all needs.Crawling One Page----------Most cases you probally just want to crawl one page. Even if you only need one page, our system performs fast enough to lead the race.The most straight forward way to make sure you only crawl a single page is to set the \[budget limit\](./account/settings) with a wild card value or \`\*\` to 1.You can also pass in the param \`limit\` in the JSON body with the limit of pages.Crawling Multiple Pages----------When you crawl multiple pages, the concurrency horsepower of the spider kicks in. You might wonder why and how one request may take (x)ms to come back, and 100 requests take about the same time! That’s because the built-in isolated concurrency allows for crawling thousands to millions of pages in no time. It’s the only current solution that can handle large websites with over 100k pages within a minute or two (sometimes even in a blink or two). By default, we do not add any limits to crawls unless specified.### Planet Scale Crawling ###If you plan on processing crawls that have over 200 pages, we recommend streaming the request from the client instead of parsing the entire payload once finished. We have an example of this with Python on the API docs page, also shown below.\`\`\`import requests, os, jsonheaders = {    \\'Authorization\\': os.environ\["SPIDER\_API\_KEY"\],    \\'Content-Type\\': \\'application/json\\',}json\_data = {"limit":250,"url":"http://www.example.com"}response = requests.post(\\'https://api.spider.cloud/crawl/crawl\\',  headers=headers,  json=json\_data,  stream=True)for line in response.iter\_lines():  if line:      print(json.loads(line))\`\`\`#### Automatic Configuration ####Spider handles automatic concurrency handling and ip rotation to make it simple to curate data.The more credits you have or usage available allows for a higher concurrency limit.Written on:  1/3/2024\[API\](/docs/api) \[Pricing\](/credits/new) \[Guides\](/guides) \[About\](/about) \[Docs\](https://docs.rs/spider/latest/spider/) \[Privacy\](/privacy) \[Terms\](/eula)© 2024 Spider from A11yWatchTheme Light Dark Toggle Theme \[GitHubGithub\](https://github.com/spider-rs/spider)', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), Document(id\_='08e5f1d6-4ae7-4b68-ab96-4b6a3768e88c', embedding=None, metadata={'description': 'The programmable time machine that can store pages and all assets for easy website archiving.', 'domain': 'spider.cloud', 'extracted\_data': None, 'file\_size': 18970, 'keywords': None, 'pathname': '/guides/website-archiving', 'resource\_type': 'html', 'title': 'Guides - Website Archiving', 'url': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48/spider.cloud/guides\*\_\*website-archiving.html', 'user\_id': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='Guides - Website Archiving\[Spider v1 Logo Spider \](/) \[Credits\](/credits/new)\[GitHubGithub637\](https://github.com/spider-rs/spider)Website Archiving==========With Spider you can easily backup or capture a website at any point in time.Enable Full Resource storing in the settings or website configuration to get a 1:1 copy of any websitelocally.Time Machine----------Time machine is storing data at a certain point of a time. Spider brings this to you with one simple configuration.After running the crawls you can simply download the data. This can help store assets incase the code is lost orversion control is removed.Written on:  2/7/2024\[API\](/docs/api) \[Pricing\](/credits/new) \[Guides\](/guides) \[About\](/about) \[Docs\](https://docs.rs/spider/latest/spider/) \[Privacy\](/privacy) \[Terms\](/eula)© 2024 Spider from A11yWatchTheme Light Dark Toggle Theme \[GitHubGithub\](https://github.com/spider-rs/spider)', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), Document(id\_='024cb27e-21d2-49a5-8a1a-963e72038421', embedding=None, metadata={'description': 'How to use the platform to collect data from the internet fast, affordable, and unblockable.', 'domain': 'spider.cloud', 'extracted\_data': None, 'file\_size': 24666, 'keywords': None, 'pathname': '/guides/spider', 'resource\_type': 'html', 'title': 'Guides - Spider Platform', 'url': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48/spider.cloud/guides\*\_\*spider.html', 'user\_id': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='Guides - Spider Platform\[Spider v1 Logo Spider \](/) \[Credits\](/credits/new)\[GitHubGithub637\](https://github.com/spider-rs/spider)Getting started collecting data with Spider==========Contents----------\* \[Data Curation\](#data-curation)  \* \[Crawling (Website)\](#crawling-website)  \* \[Crawling (API)\](#crawling-api)\* \[Crawl Configuration\](#crawl-configuration)  \* \[Proxies\](#proxies)  \* \[Headless Browser\](#headless-browser)  \* \[Crawl Budget Limits\](#crawl-budget-limits)\* \[Crawling and Scraping Websites\](#crawling-and-scraping-websites)  \* \[Transforming Data\](#transforming-data)    \* \[Leveraging Open Source\](#leveraging-open-source)\* \[Subscription and Spider Credits\](#subscription-and-spider-credits)Data Curation----------Collecting data with Spider can be fast and rewarding if done with some simple preliminary steps.Use the dashboard to collect data seamlessly across the internet with scheduled updates.You have two main ways of collecting data using Spider. The first and simplest is to use the UI available for scraping.The alternative is to use the API to programmatically access the system and perform actions.### Crawling (Website) ###1. Register or login to your account using email or Github.2. Purchase \[credits\](/credits/new) to kickstart crawls with \`pay-as-you-go\` go after credits deplete.3. Configure crawl \[settings\](/account/settings) to fit workflows that you need.4. Navigate to the \[dashboard\](/) and enter a website url or ask a question to get a url that should be crawled.5. Crawl the website and export/download the data as needed.### Crawling (API) ###1. Register or login to your account using email or Github.2. Purchase \[credits\](/credits/new) to kickstart crawls with \`pay-as-you-go\` after credits deplete.3. Configure crawl \[settings\](/account/settings) to fit workflows that you need.4. Navigate to \[API keys\](/api-keys) and create a new secret key.5. Go to the \[API docs\](/docs/api) page to see how the API works and perform crawls with code examples.Crawl Configuration----------Configuration your account for how you would like to crawl can help save costs or effectiveness of the content. Some of the configurations include setting Premium Proxies, Headless Browser Rendering, Webhooks, and Budgeting.### Proxies ###Using proxies with our system is straight forward. Simple check the toggle on if you want all request to use a proxy to increase the success of not being blocked.!\[Proxies example app screenshot.\](/img/app/proxy-setting.png)### Headless Browser ###If you want pages that require JavaScript to be executed the headless browser config is for you. Enabling will run all request through a real Chrome Browser for JavaScript required rendering pages.!\[Headless browser example app screenshot.\](/img/app/headless-browser.png)### Crawl Budget Limits ###One of the key things you may need to do before getting into the crawl is setting up crawl-budgets.Crawl budgets allows you to determine how many pages you are going to crawl for a website.Determining the budget will save you costs when dealing with large websites that you only want certain data points from. The example below shows adding a asterisk (\\\\\*) to determine all routes with a limit of 50 pages maximum. The settings can be overwritten by the website configuration or parameters if using the API.!\[Crawl budget example screenshot\](/img/app/edit-budget.png)Crawling and Scraping Websites----------Collecting data can be done in many ways and for many reasons. Leveraging our state-of-the-art technology allows you to create fast workloads that can process content from multiple locations. At the time of writing, we have started to focus on our data processing API instead of the dashboard. The API has much more flexibility than the UI for performing advanced workloads like batching, formatting, and so on.!\[Dashboard UI for Spider displaying data collecting from www.napster.com, jeffmendez.com, rsseau.rs, and www.drake.com\](/img/app/ui-crawl.png)### Transforming Data ###The API has more features for gathering the content in different formats and transforming the HTML as needed. You can transform the content from HTML to Markdown and feed it to a LLM for better handling the learning aspect. The API is the first class citizen for the application. The UI will have the features provided by the API eventually as the need arises.#### Leveraging Open Source ####One of the reasons Spider is the ultimate data-curation service for scraping is from the power of Open-Source. The core of the engine is completly available on \[Github\](https://github.com/spider-rs/spider) under \[MIT\](https://opensource.org/license/mit/) to show what is in store. We are constantly working on the crawler features including performance with plans to maintain the project for the long run.Subscription and Spider Credits----------The platform allows purchasing credits that gives you the ability to crawl at any time.When you purchase credits a crawl subscription is created that allows you to continue to usethe platform when your credits deplete. The limits provided coralate with the amount of creditspurchased, an example would be if you bought $5 in credits you would have about $40 in spending limit - $10 in credit gives $80 and so on.The highest purchase of credits directly determines how much is allowed on the platform. You can view your usage and credits on the \[usage limits page\](/account/usage).Written on:  1/2/2024\[API\](/docs/api) \[Pricing\](/credits/new) \[Guides\](/guides) \[About\](/about) \[Docs\](https://docs.rs/spider/latest/spider/) \[Privacy\](/privacy) \[Terms\](/eula)© 2024 Spider from A11yWatchTheme Light Dark Toggle Theme \[GitHubGithub\](https://github.com/spider-rs/spider)', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), Document(id\_='44bff527-c7f3-4346-a2f8-1454c52e1b01', embedding=None, metadata={'description': 'Generate API keys that allow access to the system programmatically anywhere. Full management access for your Spider API journey.', 'domain': 'spider.cloud', 'extracted\_data': None, 'file\_size': 28770, 'keywords': None, 'pathname': '/api-keys', 'resource\_type': 'html', 'title': 'API Keys Spider', 'url': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48/spider.cloud/api-keys.html', 'user\_id': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text="API Keys Spider\[Spider v1 Logo Spider \](/) \[Credits\](/credits/new)\[GitHubGithub637\](https://github.com/spider-rs/spider) API Keys==========Generate API keys that allow access to the system programmatically anywhere. Full management access for your Spider API journey. Key Management----------Your secret API keys are listed below. Please note that we do not display your secret API keys again after you generate them.Do not share your API key with others, or expose it in the browser or other client-side code. In order to protect the security of your account, Spider may also automatically disable any API key that we've found has leaked publicly.Filter Name...Columns|   Name    |Key|Created|Last Used|   ||-----------|---|-------|---------|---||No results.|   |       |         |   |0 of 0 row(s) selected.PreviousNext\[API\](/docs/api) \[Pricing\](/credits/new) \[Guides\](/guides) \[About\](/about) \[Docs\](https://docs.rs/spider/latest/spider/) \[Privacy\](/privacy) \[Terms\](/eula)© 2024 Spider from A11yWatchTheme Light Dark Toggle Theme \[GitHubGithub\](https://github.com/spider-rs/spider)", start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), Document(id\_='e577c57a-2376-452f-8c39-04d1e284595c', embedding=None, metadata={'description': 'Explore your usage and set limits that work with your budget.', 'domain': 'spider.cloud', 'extracted\_data': None, 'file\_size': 21195, 'keywords': None, 'pathname': '/account/usage', 'resource\_type': 'html', 'title': 'Usage - Spider', 'url': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48/spider.cloud/account\*\_\*usage.html', 'user\_id': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text="Usage - Spider\[Spider v1 Logo Spider \](/) \[Credits\](/credits/new)\[GitHubGithub637\](https://github.com/spider-rs/spider) Usage limit==========Below you'll find a summary of usage for your account. The data may be delayed up to 5 minutes.Credits----------###  Pay as you go  ######  Approved usage limit  ### The maximum usage Spider allows for your organization each month. Ask for increase.###  Set a monthly budget  ###When your organization reaches this usage threshold each month, subsequent requests will be rejected. Data may be deleted if payments are rejected.\[API\](/docs/api) \[Pricing\](/credits/new) \[Guides\](/guides) \[About\](/about) \[Docs\](https://docs.rs/spider/latest/spider/) \[Privacy\](/privacy) \[Terms\](/eula)© 2024 Spider from A11yWatchTheme Light Dark Toggle Theme \[GitHubGithub\](https://github.com/spider-rs/spider)", start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), Document(id\_='e3eb1e3c-5080-4590-94e8-fd2ef4f6d3c6', embedding=None, metadata={'description': 'Adjust your spider settings to adjust your crawl settings.', 'domain': 'spider.cloud', 'extracted\_data': None, 'file\_size': 18322, 'keywords': None, 'pathname': '/account/settings', 'resource\_type': 'html', 'title': 'Settings - Spider', 'url': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48/spider.cloud/account\*\_\*settings.html', 'user\_id': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='Settings - Spider\[Spider v1 Logo Spider \](/) \[Credits\](/credits/new)\[GitHubGithub637\](https://github.com/spider-rs/spider)\[API\](/docs/api) \[Pricing\](/credits/new) \[Guides\](/guides) \[About\](/about) \[Docs\](https://docs.rs/spider/latest/spider/) \[Privacy\](/privacy) \[Terms\](/eula)© 2024 Spider from A11yWatchTheme Light Dark Toggle Theme \[GitHubGithub\](https://github.com/spider-rs/spider)', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n')\]

For guides and documentation, visit [Spider](https://spider.cloud/docs/api)

Using Browserbase Reader 🅱️[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/#using-browserbase-reader)
====================================================================================================================================

[Browserbase](https://browserbase.com/) is a serverless platform for running headless browsers, it offers advanced debugging, session recordings, stealth mode, integrated proxies and captcha solving.

Installation and Setup[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/#installation-and-setup)
----------------------------------------------------------------------------------------------------------------------------

*   Get an API key and Project ID from [browserbase.com](https://browserbase.com/) and set it in environment variables (`BROWSERBASE_API_KEY`, `BROWSERBASE_PROJECT_ID`).
*   Install the [Browserbase SDK](http://github.com/browserbase/python-sdk):

In \[ \]:

Copied!

% pip install browserbase

% pip install browserbase

In \[ \]:

Copied!

from llama\_index.readers.web import BrowserbaseWebReader

from llama\_index.readers.web import BrowserbaseWebReader

In \[ \]:

Copied!

reader \= BrowserbaseWebReader()
docs \= reader.load\_data(
    urls\=\[
        "https://example.com",
    \],
    \# Text mode
    text\_content\=False,
)

reader = BrowserbaseWebReader() docs = reader.load\_data( urls=\[ "https://example.com", \], # Text mode text\_content=False, )

### Using FireCrawl Reader 🔥[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/#using-firecrawl-reader)

Firecrawl is an api that turns entire websites into clean, LLM accessible markdown.

Using Firecrawl to gather an entire website

In \[ \]:

Copied!

from llama\_index.readers.web import FireCrawlWebReader

from llama\_index.readers.web import FireCrawlWebReader

In \[ \]:

Copied!

\# using firecrawl to crawl a website
firecrawl\_reader \= FireCrawlWebReader(
    api\_key\="<your\_api\_key>",  \# Replace with your actual API key from https://www.firecrawl.dev/
    mode\="scrape",  \# Choose between "crawl" and "scrape" for single page scraping
    params\={"additional": "parameters"},  \# Optional additional parameters
)

\# Load documents from a single page URL
documents \= firecrawl\_reader.load\_data(url\="http://paulgraham.com/")

\# using firecrawl to crawl a website firecrawl\_reader = FireCrawlWebReader( api\_key="", # Replace with your actual API key from https://www.firecrawl.dev/ mode="scrape", # Choose between "crawl" and "scrape" for single page scraping params={"additional": "parameters"}, # Optional additional parameters ) # Load documents from a single page URL documents = firecrawl\_reader.load\_data(url="http://paulgraham.com/")

In \[ \]:

Copied!

index \= SummaryIndex.from\_documents(documents)

index = SummaryIndex.from\_documents(documents)

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did the author do growing up?")

\# set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine() response = query\_engine.query("What did the author do growing up?")

In \[ \]:

Copied!

display(Markdown(f"<b>{response}</b>"))

display(Markdown(f"**{response}**"))

Using firecrawl for a single page

In \[ \]:

Copied!

\# Initialize the FireCrawlWebReader with your API key and desired mode
from llama\_index.readers.web.firecrawl\_web.base import FireCrawlWebReader

firecrawl\_reader \= FireCrawlWebReader(
    api\_key\="<your\_api\_key>",  \# Replace with your actual API key from https://www.firecrawl.dev/
    mode\="scrape",  \# Choose between "crawl" and "scrape" for single page scraping
    params\={"additional": "parameters"},  \# Optional additional parameters
)

\# Load documents from a single page URL
documents \= firecrawl\_reader.load\_data(url\="http://paulgraham.com/worked.html")

\# Initialize the FireCrawlWebReader with your API key and desired mode from llama\_index.readers.web.firecrawl\_web.base import FireCrawlWebReader firecrawl\_reader = FireCrawlWebReader( api\_key="", # Replace with your actual API key from https://www.firecrawl.dev/ mode="scrape", # Choose between "crawl" and "scrape" for single page scraping params={"additional": "parameters"}, # Optional additional parameters ) # Load documents from a single page URL documents = firecrawl\_reader.load\_data(url="http://paulgraham.com/worked.html")

Running cells with '/opt/homebrew/bin/python3' requires the ipykernel package.
Run the following command to install 'ipykernel' into the Python environment. 
Command: '/opt/homebrew/bin/python3 -m pip install ipykernel -U --user --force-reinstall'

In \[ \]:

Copied!

index \= SummaryIndex.from\_documents(documents)

index = SummaryIndex.from\_documents(documents)

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did the author do growing up?")

\# set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine() response = query\_engine.query("What did the author do growing up?")

In \[ \]:

Copied!

display(Markdown(f"<b>{response}</b>"))

display(Markdown(f"**{response}**"))

#### Using TrafilaturaWebReader[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/#using-trafilaturawebreader)

In \[ \]:

Copied!

from llama\_index.readers.web import TrafilaturaWebReader

from llama\_index.readers.web import TrafilaturaWebReader

\---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In\[7\], line 1
\----> 1 from llama\_index.readers.web import TrafilaturaWebReader

ModuleNotFoundError: No module named 'llama\_index.readers.web'

In \[ \]:

Copied!

documents \= TrafilaturaWebReader().load\_data(
    \["http://paulgraham.com/worked.html"\]
)

documents = TrafilaturaWebReader().load\_data( \["http://paulgraham.com/worked.html"\] )

In \[ \]:

Copied!

index \= SummaryIndex.from\_documents(documents)

index = SummaryIndex.from\_documents(documents)

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did the author do growing up?")

\# set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine() response = query\_engine.query("What did the author do growing up?")

In \[ \]:

Copied!

display(Markdown(f"<b>{response}</b>"))

display(Markdown(f"**{response}**"))

### Using RssReader[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/#using-rssreader)

In \[ \]:

Copied!

from llama\_index.core import SummaryIndex
from llama\_index.readers.web import RssReader

documents \= RssReader().load\_data(
    \["https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"\]
)

index \= SummaryIndex.from\_documents(documents)

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What happened in the news today?")

from llama\_index.core import SummaryIndex from llama\_index.readers.web import RssReader documents = RssReader().load\_data( \["https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"\] ) index = SummaryIndex.from\_documents(documents) # set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine() response = query\_engine.query("What happened in the news today?")

Using ScrapFly[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/#using-scrapfly)
------------------------------------------------------------------------------------------------------------

ScrapFly is a web scraping API with headless browser capabilities, proxies, and anti-bot bypass. It allows for extracting web page data into accessible LLM markdown or text. Install ScrapFly Python SDK using pip:

pip install scrapfly-sdk

Here is a basic usage of ScrapflyReader

In \[ \]:

Copied!

from llama\_index.readers.web import ScrapflyReader

\# Initiate ScrapflyReader with your ScrapFly API key
scrapfly\_reader \= ScrapflyReader(
    api\_key\="Your ScrapFly API key",  \# Get your API key from https://www.scrapfly.io/
    ignore\_scrape\_failures\=True,  \# Ignore unprocessable web pages and log their exceptions
)

\# Load documents from URLs as markdown
documents \= scrapfly\_reader.load\_data(
    urls\=\["https://web-scraping.dev/products"\]
)

from llama\_index.readers.web import ScrapflyReader # Initiate ScrapflyReader with your ScrapFly API key scrapfly\_reader = ScrapflyReader( api\_key="Your ScrapFly API key", # Get your API key from https://www.scrapfly.io/ ignore\_scrape\_failures=True, # Ignore unprocessable web pages and log their exceptions ) # Load documents from URLs as markdown documents = scrapfly\_reader.load\_data( urls=\["https://web-scraping.dev/products"\] )

The ScrapflyReader also allows passigng ScrapeConfig object for customizing the scrape request. See the documentation for the full feature details and their API params: [https://scrapfly.io/docs/scrape-api/getting-started](https://scrapfly.io/docs/scrape-api/getting-started)

In \[ \]:

Copied!

from llama\_index.readers.web import ScrapflyReader

\# Initiate ScrapflyReader with your ScrapFly API key
scrapfly\_reader \= ScrapflyReader(
    api\_key\="Your ScrapFly API key",  \# Get your API key from https://www.scrapfly.io/
    ignore\_scrape\_failures\=True,  \# Ignore unprocessable web pages and log their exceptions
)

scrapfly\_scrape\_config \= {
    "asp": True,  \# Bypass scraping blocking and antibot solutions, like Cloudflare
    "render\_js": True,  \# Enable JavaScript rendering with a cloud headless browser
    "proxy\_pool": "public\_residential\_pool",  \# Select a proxy pool (datacenter or residnetial)
    "country": "us",  \# Select a proxy location
    "auto\_scroll": True,  \# Auto scroll the page
    "js": "",  \# Execute custom JavaScript code by the headless browser
}

\# Load documents from URLs as markdown
documents \= scrapfly\_reader.load\_data(
    urls\=\["https://web-scraping.dev/products"\],
    scrape\_config\=scrapfly\_scrape\_config,  \# Pass the scrape config
    scrape\_format\="markdown",  \# The scrape result format, either \`markdown\`(default) or \`text\`
)

from llama\_index.readers.web import ScrapflyReader # Initiate ScrapflyReader with your ScrapFly API key scrapfly\_reader = ScrapflyReader( api\_key="Your ScrapFly API key", # Get your API key from https://www.scrapfly.io/ ignore\_scrape\_failures=True, # Ignore unprocessable web pages and log their exceptions ) scrapfly\_scrape\_config = { "asp": True, # Bypass scraping blocking and antibot solutions, like Cloudflare "render\_js": True, # Enable JavaScript rendering with a cloud headless browser "proxy\_pool": "public\_residential\_pool", # Select a proxy pool (datacenter or residnetial) "country": "us", # Select a proxy location "auto\_scroll": True, # Auto scroll the page "js": "", # Execute custom JavaScript code by the headless browser } # Load documents from URLs as markdown documents = scrapfly\_reader.load\_data( urls=\["https://web-scraping.dev/products"\], scrape\_config=scrapfly\_scrape\_config, # Pass the scrape config scrape\_format="markdown", # The scrape result format, either \`markdown\`(default) or \`text\` )

Back to top

[Previous Weaviate Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WeaviateDemo/)[Next Deplot Reader Demo](https://docs.llamaindex.ai/en/stable/examples/data_connectors/deplot/DeplotReader/)
