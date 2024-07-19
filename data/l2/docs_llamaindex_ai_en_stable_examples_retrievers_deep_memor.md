Title: Activeloop Deep Memory - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/

Markdown Content:
Activeloop Deep Memory - LlamaIndex
===============
             

[Skip to content](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/#activeloop-deep-memory)

[![Image 1: logo](https://docs.llamaindex.ai/en/stable/_static/assets/LlamaSquareBlack.svg)](https://docs.llamaindex.ai/en/stable/ "LlamaIndex")

LlamaIndex

Activeloop Deep Memory

  

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
        *   [Web Page Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/)
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
        *    Activeloop Deep Memory [Activeloop Deep Memory](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/)
            
            Table of contents
            
            *   [1\. Dataset Creation and ingestion](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/#1-dataset-creation-and-ingestion)
            *   [2\. Training Deep Memory](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/#2-training-deep-memory)
            *   [3\. DeepMemory Evaluation](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/#3-deepmemory-evaluation)
            *   [4\. Deep Memory Inference](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/#4-deep-memory-inference)
            
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

*   [1\. Dataset Creation and ingestion](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/#1-dataset-creation-and-ingestion)
*   [2\. Training Deep Memory](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/#2-training-deep-memory)
*   [3\. DeepMemory Evaluation](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/#3-deepmemory-evaluation)
*   [4\. Deep Memory Inference](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/#4-deep-memory-inference)

       

Activeloop Deep Memory[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/#activeloop-deep-memory)
=======================================================================================================================

**How do we get +15% RAG hit\_rate improvement for question answering on documentation?**

Retrieval-Augmented Generators (RAGs) have recently gained significant attention. As advanced RAG techniques and agents emerge, they expand the potential of what RAGs can accomplish. However, several challenges may limit the integration of RAGs into production. The primary factors to consider when implementing RAGs in production settings are accuracy (recall), cost, and latency. For basic use cases, OpenAI's Ada model paired with a naive similarity search can produce satisfactory results. Yet, for higher accuracy or recall during searches, one might need to employ advanced retrieval techniques. These methods might involve varying data chunk sizes, rewriting queries multiple times, and more, potentially increasing latency and costs. [Activeloop's](https://activeloop.ai/) [Deep Memory](https://www.activeloop.ai/resources/use-deep-memory-to-boost-rag-apps-accuracy-by-up-to-22/) a feature available to Activeloop Deep Lake users, addresses these issuea by introducing a tiny neural network layer trained to match user queries with relevant data from a corpus. While this addition incurs minimal latency during search, it can boost retrieval accuracy by up to 27 % and remains cost-effective and simple to use, without requiring any additional advanced rag techniques.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-deeplake
%pip install llama\-index\-llms\-openai

%pip install llama-index-vector-stores-deeplake %pip install llama-index-llms-openai

In \[ \]:

Copied!

import nest\_asyncio
import os
import getpass

nest\_asyncio.apply()

import nest\_asyncio import os import getpass nest\_asyncio.apply()

In \[ \]:

Copied!

!pip install deeplake beautifulsoup4 html2text tiktoken openai llama\-index python\-dotenv

!pip install deeplake beautifulsoup4 html2text tiktoken openai llama-index python-dotenv

For this tutorial we will parse deeplake documentation, and create a RAG system that could answer the question from the docs.

The tutorial can be divided into several parts:

1.  [Dataset creation and uploading](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/#1-dataset-creation-and-ingestion)
2.  [Generating synthetic queries and training deep\_memory](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/#2-training-deep-memory)
3.  [Evaluating deep memory performance](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/#3-deepmemory-evaluation)
4.  [Deep Memory inference](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/#4-deep-memory-inference)

1\. Dataset Creation and ingestion[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/#1-dataset-creation-and-ingestion)
---------------------------------------------------------------------------------------------------------------------------------------------

Let me parse all of the links using BeautifulSoup and convert them into LlamaIndex documents:

In \[ \]:

Copied!

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get\_all\_links(url):
    response \= requests.get(url)
    if response.status\_code != 200:
        print(f"Failed to retrieve the page: {url}")
        return \[\]

    soup \= BeautifulSoup(response.content, "html.parser")

    \# Finding all 'a' tags which typically contain href attribute for links
    links \= \[
        urljoin(url, a\["href"\])
        for a in soup.find\_all("a", href\=True)
        if a\["href"\]
    \]

    return links

import requests from bs4 import BeautifulSoup from urllib.parse import urljoin def get\_all\_links(url): response = requests.get(url) if response.status\_code != 200: print(f"Failed to retrieve the page: {url}") return \[\] soup = BeautifulSoup(response.content, "html.parser") # Finding all 'a' tags which typically contain href attribute for links links = \[ urljoin(url, a\["href"\]) for a in soup.find\_all("a", href=True) if a\["href"\] \] return links

In \[ \]:

Copied!

from langchain.document\_loaders import AsyncHtmlLoader
from langchain.document\_transformers import Html2TextTransformer
from llama\_index.core import Document

def load\_documents(url):
    all\_links \= get\_all\_links(url)
    loader \= AsyncHtmlLoader(all\_links)
    docs \= loader.load()

    html2text \= Html2TextTransformer()
    docs\_transformed \= html2text.transform\_documents(docs)
    docs \= \[Document.from\_langchain\_format(doc) for doc in docs\_transformed\]
    return docs

docs \= load\_documents("https://docs.deeplake.ai/en/latest/")

from langchain.document\_loaders import AsyncHtmlLoader from langchain.document\_transformers import Html2TextTransformer from llama\_index.core import Document def load\_documents(url): all\_links = get\_all\_links(url) loader = AsyncHtmlLoader(all\_links) docs = loader.load() html2text = Html2TextTransformer() docs\_transformed = html2text.transform\_documents(docs) docs = \[Document.from\_langchain\_format(doc) for doc in docs\_transformed\] return docs docs = load\_documents("https://docs.deeplake.ai/en/latest/")

Fetching pages: 100%|##########| 120/120 \[00:13<00:00,  8.70it/s\]

In \[ \]:

Copied!

len(docs)

len(docs)

Out\[ \]:

120

In \[ \]:

Copied!

from llama\_index.core.evaluation import generate\_question\_context\_pairs
from llama\_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
)
from llama\_index.vector\_stores.deeplake import DeepLakeVectorStore
from llama\_index.core.node\_parser import SimpleNodeParser
from llama\_index.llms.openai import OpenAI

os.environ\["OPENAI\_API\_KEY"\] \= getpass.getpass("Enter your OpenAI API token: ")
\# # activeloop token is needed if you are not signed in using CLI: \`activeloop login -u <USERNAME> -p <PASSWORD>\`
os.environ\["ACTIVELOOP\_TOKEN"\] \= getpass.getpass(
    "Enter your ActiveLoop API token: "
)  \# Get your API token from https://app.activeloop.ai, click on your profile picture in the top right corner, and select "API Tokens"

token \= os.getenv("ACTIVELOOP\_TOKEN")

vector\_store \= DeepLakeVectorStore(
    dataset\_path\="hub://activeloop-test/deeplake\_docs\_deepmemory2",
    overwrite\=False,  \# set to True to overwrite the existing dataset
    runtime\={"tensor\_db": True},
    token\=token,
)

from llama\_index.core.evaluation import generate\_question\_context\_pairs from llama\_index.core import ( VectorStoreIndex, SimpleDirectoryReader, StorageContext, ) from llama\_index.vector\_stores.deeplake import DeepLakeVectorStore from llama\_index.core.node\_parser import SimpleNodeParser from llama\_index.llms.openai import OpenAI os.environ\["OPENAI\_API\_KEY"\] = getpass.getpass("Enter your OpenAI API token: ") # # activeloop token is needed if you are not signed in using CLI: \`activeloop login -u \-p \` os.environ\["ACTIVELOOP\_TOKEN"\] = getpass.getpass( "Enter your ActiveLoop API token: " ) # Get your API token from https://app.activeloop.ai, click on your profile picture in the top right corner, and select "API Tokens" token = os.getenv("ACTIVELOOP\_TOKEN") vector\_store = DeepLakeVectorStore( dataset\_path="hub://activeloop-test/deeplake\_docs\_deepmemory2", overwrite=False, # set to True to overwrite the existing dataset runtime={"tensor\_db": True}, token=token, )

Deep Lake Dataset in hub://activeloop-test/deeplake\_docs\_deepmemory2 already exists, loading from the storage

In \[ \]:

Copied!

def create\_modules(vector\_store, docs\=\[\], populate\_vector\_store\=True):
    if populate\_vector\_store:
        node\_parser \= SimpleNodeParser.from\_defaults(chunk\_size\=512)
        nodes \= node\_parser.get\_nodes\_from\_documents(docs)
    else:
        nodes \= \[\]

    \# by default, the node ids are set to random uuids. To ensure same id's per run, we manually set them.
    for idx, node in enumerate(nodes):
        node.id\_ \= f"node\_{idx}"

    llm \= OpenAI(model\="gpt-4")
    storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
    return storage\_context, nodes, llm

def create\_modules(vector\_store, docs=\[\], populate\_vector\_store=True): if populate\_vector\_store: node\_parser = SimpleNodeParser.from\_defaults(chunk\_size=512) nodes = node\_parser.get\_nodes\_from\_documents(docs) else: nodes = \[\] # by default, the node ids are set to random uuids. To ensure same id's per run, we manually set them. for idx, node in enumerate(nodes): node.id\_ = f"node\_{idx}" llm = OpenAI(model="gpt-4") storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) return storage\_context, nodes, llm

In \[ \]:

Copied!

(
    storage\_context,
    nodes,
    llm,
) \= create\_modules(
    docs\=docs,
    vector\_store\=vector\_store,
    \# populate\_vector\_store=False, # uncomment this line to skip populating the vector store
)

( storage\_context, nodes, llm, ) = create\_modules( docs=docs, vector\_store=vector\_store, # populate\_vector\_store=False, # uncomment this line to skip populating the vector store )

In \[ \]:

Copied!

vector\_index \= VectorStoreIndex(nodes, storage\_context\=storage\_context)
deep\_memory\_retriever \= vector\_index.as\_retriever(
    similarity\_top\_k\=4, deep\_memory\=True
)

vector\_index = VectorStoreIndex(nodes, storage\_context=storage\_context) deep\_memory\_retriever = vector\_index.as\_retriever( similarity\_top\_k=4, deep\_memory=True )

2\. Training Deep Memory[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/#2-training-deep-memory)
-------------------------------------------------------------------------------------------------------------------------

![Image 3: Image description](blob:https://docs.llamaindex.ai/384a98df00187f57b3e39c94f8fa1019)

Here above, we showed the overall schema of how deep\_memory works. So as you can see, in order to train it, you need relevance, queries together with corpus data (data that we want to query). The corpus data was already populated in the previous section; here, we will be generating questions and relevance.

1.  `questions` - is a text of strings, where each string represents a query.
2.  `relevance` - contains links to the ground truth for each question. There might be several docs that contain an answer to the given question. Because of this, relevance is List\[List\[tuple\[str, float\]\]\], where the outer list represents queries and the inner list relevant documents. The tuple contains a str, float pair where the string represents the id of the source doc (corresponds to the id tensor in the dataset), while the float corresponds to how much the current document is related to the question.

In \[ \]:

Copied!

from llama\_index.core.evaluation import (
    generate\_question\_context\_pairs,
    EmbeddingQAFinetuneDataset,
)
import random

def create\_train\_test\_datasets(
    number\_of\_samples\=600, llm\=None, nodes\=None, save\=False
):
    random\_indices \= random.sample(range(len(nodes)), number\_of\_samples)

    ratio \= int(len(random\_indices) \* 0.8)

    train\_indices \= random\_indices\[:ratio\]
    test\_indices \= random\_indices\[ratio:\]

    train\_nodes \= \[nodes\[i\] for i in train\_indices\]
    test\_nodes \= \[nodes\[i\] for i in test\_indices\]

    train\_qa\_dataset \= generate\_question\_context\_pairs(
        train\_nodes, llm\=llm, num\_questions\_per\_chunk\=1
    )

    test\_qa\_dataset \= generate\_question\_context\_pairs(
        test\_nodes, llm\=llm, num\_questions\_per\_chunk\=1
    )

    \# \[optional\] save
    if save:
        train\_qa\_dataset.save\_json(
            f"deeplake\_docs\_{number\_of\_samples}\_train.json"
        )
        test\_qa\_dataset.save\_json(
            f"deeplake\_docs\_{number\_of\_samples}\_test.json"
        )
    return train\_qa\_dataset, test\_qa\_dataset

from llama\_index.core.evaluation import ( generate\_question\_context\_pairs, EmbeddingQAFinetuneDataset, ) import random def create\_train\_test\_datasets( number\_of\_samples=600, llm=None, nodes=None, save=False ): random\_indices = random.sample(range(len(nodes)), number\_of\_samples) ratio = int(len(random\_indices) \* 0.8) train\_indices = random\_indices\[:ratio\] test\_indices = random\_indices\[ratio:\] train\_nodes = \[nodes\[i\] for i in train\_indices\] test\_nodes = \[nodes\[i\] for i in test\_indices\] train\_qa\_dataset = generate\_question\_context\_pairs( train\_nodes, llm=llm, num\_questions\_per\_chunk=1 ) test\_qa\_dataset = generate\_question\_context\_pairs( test\_nodes, llm=llm, num\_questions\_per\_chunk=1 ) # \[optional\] save if save: train\_qa\_dataset.save\_json( f"deeplake\_docs\_{number\_of\_samples}\_train.json" ) test\_qa\_dataset.save\_json( f"deeplake\_docs\_{number\_of\_samples}\_test.json" ) return train\_qa\_dataset, test\_qa\_dataset

In \[ \]:

Copied!

train\_qa\_dataset, test\_qa\_dataset \= create\_train\_test\_datasets(
    number\_of\_samples\=600, llm\=llm, nodes\=nodes, save\=True
)

train\_qa\_dataset, test\_qa\_dataset = create\_train\_test\_datasets( number\_of\_samples=600, llm=llm, nodes=nodes, save=True )

  4%|▍         | 19/480 \[02:25<1:04:00,  8.33s/it\]

In \[ \]:

Copied!

train\_qa\_dataset \= EmbeddingQAFinetuneDataset.from\_json(
    "deeplake\_docs\_600\_train.json"
)
test\_qa\_dataset \= EmbeddingQAFinetuneDataset.from\_json(
    "deeplake\_docs\_600\_test.json"
)

train\_qa\_dataset = EmbeddingQAFinetuneDataset.from\_json( "deeplake\_docs\_600\_train.json" ) test\_qa\_dataset = EmbeddingQAFinetuneDataset.from\_json( "deeplake\_docs\_600\_test.json" )

In \[ \]:

Copied!

def create\_query\_relevance(qa\_dataset):
    """Function for converting llama-index dataset to correct format for deep memory training"""
    queries \= \[text for \_, text in qa\_dataset.queries.items()\]
    relevant\_docs \= qa\_dataset.relevant\_docs
    relevance \= \[\]
    for doc in relevant\_docs:
        relevance.append(\[(relevant\_docs\[doc\]\[0\], 1)\])
    return queries, relevance

def create\_query\_relevance(qa\_dataset): """Function for converting llama-index dataset to correct format for deep memory training""" queries = \[text for \_, text in qa\_dataset.queries.items()\] relevant\_docs = qa\_dataset.relevant\_docs relevance = \[\] for doc in relevant\_docs: relevance.append(\[(relevant\_docs\[doc\]\[0\], 1)\]) return queries, relevance

In \[ \]:

Copied!

train\_queries, train\_relevance \= create\_query\_relevance(train\_qa\_dataset)
test\_queries, test\_relevance \= create\_query\_relevance(test\_qa\_dataset)

train\_queries, train\_relevance = create\_query\_relevance(train\_qa\_dataset) test\_queries, test\_relevance = create\_query\_relevance(test\_qa\_dataset)

In \[ \]:

Copied!

train\_queries\[:3\]

train\_queries\[:3\]

Out\[ \]:

\['In the context of creating a bounding box tensor in a dataset, explain the significance of the "coords" argument and its keys "type" and "mode". What does the "type" key specify about the bounding box coordinates?',
 'Explain the process of creating an intrinsics tensor and appending intrinsics matrices in the context of computer vision. What are the dimensions of the intrinsics parameters and what do they represent? Also, describe the concept of a Segmentation Mask Htype and its role in image processing.',
 'In the context of querying for images in the MNIST Train Dataset using \`ds.query\`, what does the command "select \* where labels == 0" signify and what is the expected output?'\]

In \[ \]:

Copied!

train\_relevance\[:3\]

train\_relevance\[:3\]

Out\[ \]:

\[\[('node\_788', 1)\], \[('node\_861', 1)\], \[('node\_82', 1)\]\]

In \[ \]:

Copied!

test\_queries\[:3\]

test\_queries\[:3\]

Out\[ \]:

\['What are the steps to update the information of keypoints and connections in a tensor, and what types of data can be appended to keypoints?',
 'What is the command to create a mesh tensor in DeepLake and what are the supported compressions? Also, explain how to append a ply file containing mesh data to this tensor.',
 'What is a Sequence htype in the context of tensors and how does it function as a wrapper for other htypes? Provide examples.'\]

In \[ \]:

Copied!

test\_relevance\[:3\]

test\_relevance\[:3\]

Out\[ \]:

\[\[('node\_933', 1)\], \[('node\_671', 1)\], \[('node\_471', 1)\]\]

In \[ \]:

Copied!

from langchain.embeddings.openai import OpenAIEmbeddings

embeddings \= OpenAIEmbeddings()

job\_id \= vector\_store.vectorstore.deep\_memory.train(
    queries\=train\_queries,
    relevance\=train\_relevance,
    embedding\_function\=embeddings.embed\_documents,
)

from langchain.embeddings.openai import OpenAIEmbeddings embeddings = OpenAIEmbeddings() job\_id = vector\_store.vectorstore.deep\_memory.train( queries=train\_queries, relevance=train\_relevance, embedding\_function=embeddings.embed\_documents, )

Starting DeepMemory training job
Your Deep Lake dataset has been successfully created!

Preparing training data for deepmemory:

Creating 483 embeddings in 1 batches of size 483:: 100%|██████████| 1/1 \[00:03<00:00,  3.67s/it\]

DeepMemory training job started. Job ID: 65421a5003888c9ca36c72e8

In \[ \]:

Copied!

vector\_store.vectorstore.deep\_memory.status(job\_id)

vector\_store.vectorstore.deep\_memory.status(job\_id)

This dataset can be visualized in Jupyter Notebook by ds.visualize() or at https://app.activeloop.ai/adilkhan/deeplake\_docs\_deepmemory2
--------------------------------------------------------------
|                  65421a5003888c9ca36c72e8                  |
--------------------------------------------------------------
| status                     | completed                     |
--------------------------------------------------------------
| progress                   | eta: 12.2 seconds             |
|                            | recall@10: 67.01% (+18.56%)   |
--------------------------------------------------------------
| results                    | recall@10: 67.01% (+18.56%)   |
--------------------------------------------------------------

3\. DeepMemory Evaluation[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/#3-deepmemory-evaluation)
---------------------------------------------------------------------------------------------------------------------------

Fantastic! The training has led to some remarkable improvements! Now, let's assess its performance on a test set.

In \[ \]:

Copied!

recalls \= vector\_store.vectorstore.deep\_memory.evaluate(
    queries\=test\_queries,
    relevance\=test\_relevance,
    embedding\_function\=embeddings.embed\_documents,
)

recalls = vector\_store.vectorstore.deep\_memory.evaluate( queries=test\_queries, relevance=test\_relevance, embedding\_function=embeddings.embed\_documents, )

info Wed Nov  1 09:32:44 2023 GMT         Added distance metric \`deepmemory\_distance\`.
Embedding queries took 0.95 seconds
---- Evaluating without Deep Memory ---- 
Recall@1:	  12.5%
Recall@3:	  23.3%
Recall@5:	  30.8%
Recall@10:	  50.8%
Recall@50:	  94.2%
Recall@100:	  95.8%
---- Evaluating with Deep Memory ---- 
Recall@1:	  11.7%
Recall@3:	  27.5%
Recall@5:	  40.8%
Recall@10:	  65.0%
Recall@50:	  96.7%
Recall@100:	  98.3%

Impressive! We've observed a 15% increase in recall on the test set. Next, let's employ the RetrieverEvaluator to examine the MRR (Mean Reciprocal Rank) and hit rates.

In \[ \]:

Copied!

import pandas as pd

def display\_results(eval\_results):
    """Display results from evaluate."""
    hit\_rates \= \[\]
    mrrs \= \[\]
    names \= \[\]
    for name, eval\_result in eval\_results.items():
        metric\_dicts \= \[\]
        for er in eval\_result:
            metric\_dict \= er.metric\_vals\_dict
            metric\_dicts.append(metric\_dict)

        full\_df \= pd.DataFrame(metric\_dicts)

        hit\_rate \= full\_df\["hit\_rate"\].mean()
        mrr \= full\_df\["mrr"\].mean()

        hit\_rates.append(hit\_rate)
        mrrs.append(mrr)
        names.append(name)

    metric\_df \= pd.DataFrame(
        \[
            {"retrievers": names\[i\], "hit\_rate": hit\_rates\[i\], "mrr": mrrs\[i\]}
            for i in range(2)
        \],
    )

    return metric\_df

import pandas as pd def display\_results(eval\_results): """Display results from evaluate.""" hit\_rates = \[\] mrrs = \[\] names = \[\] for name, eval\_result in eval\_results.items(): metric\_dicts = \[\] for er in eval\_result: metric\_dict = er.metric\_vals\_dict metric\_dicts.append(metric\_dict) full\_df = pd.DataFrame(metric\_dicts) hit\_rate = full\_df\["hit\_rate"\].mean() mrr = full\_df\["mrr"\].mean() hit\_rates.append(hit\_rate) mrrs.append(mrr) names.append(name) metric\_df = pd.DataFrame( \[ {"retrievers": names\[i\], "hit\_rate": hit\_rates\[i\], "mrr": mrrs\[i\]} for i in range(2) \], ) return metric\_df

Evaluating performance of retrieval with deep memory:

In \[ \]:

Copied!

from llama\_index.core.evaluation import RetrieverEvaluator

deep\_memory\_retriever \= vector\_index.as\_retriever(
    similarity\_top\_k\=10, vector\_store\_kwargs\={"deep\_memory": True}
)
dm\_retriever\_evaluator \= RetrieverEvaluator.from\_metric\_names(
    \["mrr", "hit\_rate"\], retriever\=deep\_memory\_retriever
)

dm\_eval\_results \= await dm\_retriever\_evaluator.aevaluate\_dataset(
    test\_qa\_dataset, retriever\=dm\_retriever\_evaluator
)

from llama\_index.core.evaluation import RetrieverEvaluator deep\_memory\_retriever = vector\_index.as\_retriever( similarity\_top\_k=10, vector\_store\_kwargs={"deep\_memory": True} ) dm\_retriever\_evaluator = RetrieverEvaluator.from\_metric\_names( \["mrr", "hit\_rate"\], retriever=deep\_memory\_retriever ) dm\_eval\_results = await dm\_retriever\_evaluator.aevaluate\_dataset( test\_qa\_dataset, retriever=dm\_retriever\_evaluator )

In \[ \]:

Copied!

from llama\_index.core.evaluation import RetrieverEvaluator

naive\_retriever \= vector\_index.as\_retriever(similarity\_top\_k\=10)
naive\_retriever\_evaluator \= RetrieverEvaluator.from\_metric\_names(
    \["mrr", "hit\_rate"\], retriever\=naive\_retriever
)

naive\_eval\_results \= await naive\_retriever\_evaluator.aevaluate\_dataset(
    test\_qa\_dataset, retriever\=naive\_retriever
)

from llama\_index.core.evaluation import RetrieverEvaluator naive\_retriever = vector\_index.as\_retriever(similarity\_top\_k=10) naive\_retriever\_evaluator = RetrieverEvaluator.from\_metric\_names( \["mrr", "hit\_rate"\], retriever=naive\_retriever ) naive\_eval\_results = await naive\_retriever\_evaluator.aevaluate\_dataset( test\_qa\_dataset, retriever=naive\_retriever )

In \[ \]:

Copied!

eval\_results \= {
    f"{mode} with Deep Memory top-10 eval": eval\_result
    for mode, eval\_result in zip(
        \["with", "without"\], \[dm\_eval\_results, naive\_eval\_results\]
    )
}

display\_results(eval\_results)

eval\_results = { f"{mode} with Deep Memory top-10 eval": eval\_result for mode, eval\_result in zip( \["with", "without"\], \[dm\_eval\_results, naive\_eval\_results\] ) } display\_results(eval\_results)

Out\[ \]:

|  | retrievers | hit\_rate | mrr |
| --- | --- | --- | --- |
| 0 | with with Deep Memory top-10 eval | 0.650000 | 0.244775 |
| 1 | without with Deep Memory top-10 eval | 0.508333 | 0.215129 |

Not only hit\_rate has increased but also MRR

4\. Deep Memory Inference[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/#4-deep-memory-inference)
---------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

query\_engine \= vector\_index.as\_query\_engine(
    vector\_store\_kwargs\={"deep\_memory": True}, llm\=llm
)
response \= query\_engine.query(
    "How can you connect your own storage to the deeplake?"
)
print(response)

query\_engine = vector\_index.as\_query\_engine( vector\_store\_kwargs={"deep\_memory": True}, llm=llm ) response = query\_engine.query( "How can you connect your own storage to the deeplake?" ) print(response)

info Wed Nov  1 11:37:33 2023 GMT         Can't find any metric in the dataset.
You can connect your own storage to deeplake by using the \`connect()\` function in the deeplake API.

In \[ \]:

Copied!

query\_engine \= vector\_index.as\_query\_engine(
    vector\_store\_kwargs\={"deep\_memory": False}, llm\=llm
)
response \= query\_engine.query(
    "How can you connect your own storage to the deeplake?"
)
print(response)

query\_engine = vector\_index.as\_query\_engine( vector\_store\_kwargs={"deep\_memory": False}, llm=llm ) response = query\_engine.query( "How can you connect your own storage to the deeplake?" ) print(response)

The context does not provide information on how to connect your own storage to Deep Lake.

From our observations, without "deep memory", our model tends to produce inaccuracies because it retrieves the wrong context.

Back to top

[Previous Composable Objects](https://docs.llamaindex.ai/en/stable/examples/retrievers/composable_retrievers/)[Next Ensemble Retrieval Guide](https://docs.llamaindex.ai/en/stable/examples/retrievers/ensemble_retrieval/)
