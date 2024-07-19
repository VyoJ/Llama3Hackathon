Title: DuckDB - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/DuckDBDemo/

Markdown Content:
DuckDB - LlamaIndex
===============
             

[Skip to content](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DuckDBDemo/#duckdb)

[![Image 1: logo](https://docs.llamaindex.ai/en/stable/_static/assets/LlamaSquareBlack.svg)](https://docs.llamaindex.ai/en/stable/ "LlamaIndex")

LlamaIndex

DuckDB

  

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
        *    DuckDB [DuckDB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DuckDBDemo/)
            
            Table of contents
            
            *   [Basic example](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DuckDBDemo/#basic-example)
                
                *   [Creating a DuckDB Index](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DuckDBDemo/#creating-a-duckdb-index)
                
            *   [Persisting to disk example](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DuckDBDemo/#persisting-to-disk-example)
            *   [Metadata filter example](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DuckDBDemo/#metadata-filter-example)
            
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

*   [Basic example](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DuckDBDemo/#basic-example)
    
    *   [Creating a DuckDB Index](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DuckDBDemo/#creating-a-duckdb-index)
    
*   [Persisting to disk example](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DuckDBDemo/#persisting-to-disk-example)
*   [Metadata filter example](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DuckDBDemo/#metadata-filter-example)

       

DuckDB[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DuckDBDemo/#duckdb)
=========================================================================================

> [DuckDB](https://duckdb.org/docs/api/python/overview) is a fast in-process analytical database. DuckDB is under an MIT license.

In this notebook we are going to show how to use DuckDB as a Vector store to be used in LlamaIndex.

Install DuckDB with:

pip install duckdb

Make sure to use the latest DuckDB version (>= 0.10.0).

You can run DuckDB in different modes depending on persistence:

*   `in-memory` is the default mode, where the database is created in memory, you can force this to be use by setting `database_name = ":memory:"` when initializing the vector store.
*   `persistence` is set by using a name for a database and setting a persistence directory `database_name = "my_vector_store.duckdb"` where the database is persisted in the default `persist_dir` or to the one you set it to.

With the vector store created, you can:

*   `.add`
*   `.get`
*   `.update`
*   `.upsert`
*   `.delete`
*   `.peek`
*   `.query` to run a search.

Basic example[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DuckDBDemo/#basic-example)
-------------------------------------------------------------------------------------------------------

In this basic example, we take the Paul Graham essay, split it into chunks, embed it using an open-source embedding model, load it into `DuckDBVectorStore`, and then query it.

For the embedding model we will use OpenAI.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

### Creating a DuckDB Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DuckDBDemo/#creating-a-duckdb-index)

In \[ \]:

Copied!

!pip install duckdb
!pip install llama\-index\-vector\-stores\-duckdb

!pip install duckdb !pip install llama-index-vector-stores-duckdb

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.vector\_stores.duckdb import DuckDBVectorStore
from llama\_index.core import StorageContext

from IPython.display import Markdown, display

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.vector\_stores.duckdb import DuckDBVectorStore from llama\_index.core import StorageContext from IPython.display import Markdown, display

In \[ \]:

Copied!

\# Setup OpenAI API
import os
import openai

openai.api\_key \= os.environ\["OPENAI\_API\_KEY"\]

\# Setup OpenAI API import os import openai openai.api\_key = os.environ\["OPENAI\_API\_KEY"\]

Download and prepare the sample dataset

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

\--2024-02-16 19:38:34--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.110.133, 185.199.111.133, 185.199.108.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.110.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 75042 (73K) \[text/plain\]
Saving to: ‘data/paul\_graham/paul\_graham\_essay.txt’

data/paul\_graham/pa 100%\[===================>\]  73.28K  --.-KB/s    in 0.06s   

2024-02-16 19:38:34 (1.24 MB/s) - ‘data/paul\_graham/paul\_graham\_essay.txt’ saved \[75042/75042\]

In \[ \]:

Copied!

documents \= SimpleDirectoryReader("data/paul\_graham/").load\_data()

vector\_store \= DuckDBVectorStore()
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

documents = SimpleDirectoryReader("data/paul\_graham/").load\_data() vector\_store = DuckDBVectorStore() storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did the author do growing up?")
display(Markdown(f"<b>{response}</b>"))

query\_engine = index.as\_query\_engine() response = query\_engine.query("What did the author do growing up?") display(Markdown(f"**{response}**"))

**The author mentions that before college, they worked on two main things outside of school: writing and programming. They wrote short stories and also tried writing programs on an IBM 1401 computer. They later got a microcomputer and started programming more extensively.**

Persisting to disk example[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DuckDBDemo/#persisting-to-disk-example)
---------------------------------------------------------------------------------------------------------------------------------

Extending the previous example, if you want to save to disk, simply initialize the DuckDBVectorStore by specifying a database name and persist directory.

In \[ \]:

Copied!

\# Save to disk
documents \= SimpleDirectoryReader("data/paul\_graham/").load\_data()

vector\_store \= DuckDBVectorStore("pg.duckdb", persist\_dir\="./persist/")
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

\# Save to disk documents = SimpleDirectoryReader("data/paul\_graham/").load\_data() vector\_store = DuckDBVectorStore("pg.duckdb", persist\_dir="./persist/") storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

In \[ \]:

Copied!

\# Load from disk
vector\_store \= DuckDBVectorStore.from\_local("./persist/pg.duckdb")
index \= VectorStoreIndex.from\_vector\_store(vector\_store)

\# Load from disk vector\_store = DuckDBVectorStore.from\_local("./persist/pg.duckdb") index = VectorStoreIndex.from\_vector\_store(vector\_store)

In \[ \]:

Copied!

\# Query Data
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did the author do growing up?")
display(Markdown(f"<b>{response}</b>"))

\# Query Data query\_engine = index.as\_query\_engine() response = query\_engine.query("What did the author do growing up?") display(Markdown(f"**{response}**"))

**The author mentions that before college, they worked on two main things outside of school: writing and programming. They wrote short stories and also tried writing programs on an IBM 1401 computer. They later got a microcomputer and started programming more extensively.**

Metadata filter example[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DuckDBDemo/#metadata-filter-example)
---------------------------------------------------------------------------------------------------------------------------

It is possible to narrow down the search space by filter with metadata. Below is an example to show that in practice.

In \[ \]:

Copied!

from llama\_index.core.schema import TextNode

nodes \= \[
    TextNode(
        \*\*{
            "text": "The Shawshank Redemption",
            "metadata": {
                "author": "Stephen King",
                "theme": "Friendship",
                "year": 1994,
                "ref\_doc\_id": "doc\_1",
            },
        }
    ),
    TextNode(
        \*\*{
            "text": "The Godfather",
            "metadata": {
                "director": "Francis Ford Coppola",
                "theme": "Mafia",
                "year": 1972,
                "ref\_doc\_id": "doc\_1",
            },
        }
    ),
    TextNode(
        \*\*{
            "text": "Inception",
            "metadata": {
                "director": "Christopher Nolan",
                "theme": "Sci-fi",
                "year": 2010,
                "ref\_doc\_id": "doc\_2",
            },
        }
    ),
\]

vector\_store \= DuckDBVectorStore()
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex(nodes, storage\_context\=storage\_context)

from llama\_index.core.schema import TextNode nodes = \[ TextNode( \*\*{ "text": "The Shawshank Redemption", "metadata": { "author": "Stephen King", "theme": "Friendship", "year": 1994, "ref\_doc\_id": "doc\_1", }, } ), TextNode( \*\*{ "text": "The Godfather", "metadata": { "director": "Francis Ford Coppola", "theme": "Mafia", "year": 1972, "ref\_doc\_id": "doc\_1", }, } ), TextNode( \*\*{ "text": "Inception", "metadata": { "director": "Christopher Nolan", "theme": "Sci-fi", "year": 2010, "ref\_doc\_id": "doc\_2", }, } ), \] vector\_store = DuckDBVectorStore() storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex(nodes, storage\_context=storage\_context)

Define the metadata filters.

In \[ \]:

Copied!

from llama\_index.core.vector\_stores import ExactMatchFilter, MetadataFilters

filters \= MetadataFilters(
    filters\=\[ExactMatchFilter(key\="theme", value\="Mafia")\]
)

from llama\_index.core.vector\_stores import ExactMatchFilter, MetadataFilters filters = MetadataFilters( filters=\[ExactMatchFilter(key="theme", value="Mafia")\] )

Use the index as a retriever to use the metadatafilter option.

In \[ \]:

Copied!

retriever \= index.as\_retriever(filters\=filters)
retriever.retrieve("What is inception about?")

retriever = index.as\_retriever(filters=filters) retriever.retrieve("What is inception about?")

Out\[ \]:

\[NodeWithScore(node=TextNode(id\_='736a1279-4ebd-496e-87b5-925197646477', embedding=\[-0.006784645840525627, -0.021635770797729492, -0.015731574967503548, -0.03265434503555298, -0.005616107489913702, 0.025351788848638535, -0.0057811918668448925, 0.0027044713497161865, -0.01623653806746006, -0.023759208619594574, 0.027164479717612267, 0.017932699993252754, 0.029028963297605515, 0.003991158679127693, -0.0009047273779287934, 0.010973258875310421, 0.027164479717612267, -0.012844215147197247, 0.006972389295697212, -0.011148054152727127, 0.003528274828568101, 0.007736308965831995, -0.031022923067212105, -0.013996569439768791, 0.0012567456578835845, 0.004988139029592276, 0.010571876540780067, -0.024290068075060844, 0.019123896956443787, -0.02119554579257965, 0.014022464863955975, -0.023098871111869812, -0.009050510823726654, 0.001241370104253292, 0.006881754379719496, -0.007186027709394693, -0.0036577528808265924, -0.012734158895909786, 0.0034473512787371874, 0.003987921867519617, 0.01084378082305193, 0.003936130553483963, -0.01015754695981741, -0.011970238760113716, 0.004363407846540213, 0.0013425247743725777, 0.03288740664720535, -0.009186462499201298, -0.009549001231789589, 0.01988781802356243, 0.00900519359856844, 0.03363838046789169, -0.012539941817522049, -0.031955163925886154, 0.02144155278801918, 0.013096697628498077, -0.0035088532604277134, -0.009050510823726654, 0.002782158087939024, -0.014760489575564861, 0.0010722394799813628, 0.003816363401710987, -0.028821798041462898, 0.011102736927568913, -0.011335796676576138, -0.012798897922039032, -0.001216283766552806, 0.018787255510687828, 3.707318683154881e-05, 0.00591390673071146, 0.03358658775687218, 0.027371644973754883, -0.017414787784218788, 0.012973693199455738, 0.007419087924063206, -0.010791989043354988, -0.024303017184138298, 0.001213856041431427, 0.004201560281217098, -0.0054024686105549335, 0.023085923865437508, -0.02022445946931839, -0.0027643549256026745, 0.022334951907396317, 0.007198975421488285, 0.02203715220093727, -0.013841195963323116, 0.02256801165640354, 0.0038454958703368902, 0.0022626277059316635, -0.018424715846776962, 0.006308814510703087, 0.017220571637153625, 0.00503345625475049, -0.0069464934058487415, 0.029313813894987106, -0.007665096316486597, 0.004486411809921265, 0.029158441349864006, -0.013193805702030659, 0.0007109150174073875, 0.0006736901123076677, 0.00758093548938632, -0.011445852927863598, -0.021739352494478226, -0.008085899986326694, 0.028614632785320282, -0.009128197096288204, 0.008506703190505505, -0.006392975337803364, -0.020366886630654335, 0.021091962233185768, 0.030582698062062263, -0.046482592821121216, 0.016819190233945847, -0.016806241124868393, 0.014799333177506924, -0.011957291513681412, 0.01698751002550125, -0.026102760806679726, -0.010623668320477009, 0.04780326783657074, 0.019020315259695053, -0.0176090057939291, 0.02243853360414505, -0.0009945527417585254, 0.007542092353105545, 0.0009281952516175807, -0.011776021681725979, -0.008830398321151733, 0.05432895943522453, 0.01621064357459545, 0.00039571707020513713, 0.00791757833212614, -0.013044905848801136, 0.03190337494015694, -0.01125163584947586, 0.028847694396972656, -0.0282003041356802, -0.02044457197189331, 0.02770828641951084, 0.0271126888692379, -0.018994418904185295, 0.011983186937868595, -0.009613740257918835, 0.00953605305403471, 0.013491605408489704, -0.00014161653234623373, 0.026154551655054092, -0.021700508892536163, 0.022697489708662033, -0.027967242524027824, -0.001959972782060504, 0.02586969919502735, 0.03231770172715187, 0.019085053354501724, 0.001658936613239348, -0.006674589589238167, -0.014436794444918633, 0.005684083327651024, 0.023163611069321632, 0.0244583897292614, 0.0008909703465178609, -0.007250766735523939, 0.0011402154341340065, 0.022891705855727196, 0.029650457203388214, 0.006758750416338444, 0.00384873291477561, 0.004492885898798704, -0.0012939705047756433, 0.02680194191634655, -0.00532154506072402, 0.023396670818328857, -0.015653887763619423, 0.02957276999950409, 0.023293089121580124, 0.01736299693584442, -0.038196004927158356, -0.007444983813911676, -0.005366862285882235, 0.02031509391963482, 0.03356069326400757, 0.051221489906311035, -0.007716887630522251, -0.0014954706421121955, -0.006380027160048485, 0.005790902767330408, 0.01244930736720562, -0.0006445575854741037, 0.0018499166471883655, 0.021959464997053146, 0.01829523779451847, -0.013815300539135933, -0.6500830054283142, -0.008221851661801338, -0.01732415333390236, -0.012915428727865219, 0.0010447254171594977, 0.030997028574347496, 0.014216681942343712, 0.022697489708662033, -0.0171428844332695, -0.004389303270727396, -0.011387588456273079, 0.0074126143008470535, 0.0467415489256382, -0.003353479551151395, -0.05448433384299278, -0.03526980057358742, -0.013491605408489704, -0.021234387531876564, -0.023241296410560608, 0.0033761383965611458, -0.020392781123518944, 0.008267168886959553, -0.026465298607945442, -0.012022030539810658, 0.002188177779316902, -0.004007343202829361, 0.02667246386408806, -0.017311206087470055, 0.007192501798272133, 0.0038325481582432985, -0.005917143542319536, 0.013161436654627323, 0.013802352361381054, 0.006166388746351004, 0.04088914394378662, -0.007561514154076576, -0.021855883300304413, 0.028821798041462898, 0.0032385678496211767, 0.025170518085360527, -0.005162934307008982, -0.008636181242763996, 0.014915863052010536, -0.018994418904185295, -0.01266941986978054, -0.013400970958173275, 0.04000869393348694, -0.022270211949944496, 0.017816169187426567, 0.00038539929664693773, 0.00421450799331069, 0.016120009124279022, -0.0027659733314067125, 0.01747952774167061, 0.0074838269501924515, 0.004819817841053009, 0.032990988343954086, -0.003131748642772436, -0.0012308500008657575, 0.00835132971405983, 0.003641568124294281, -0.0026170737110078335, 0.0176090057939291, -0.0012494624825194478, 0.02072942443192005, -0.005936565343290567, -0.00503993034362793, 0.004994613118469715, 0.0225939080119133, -0.008435490541160107, -0.0035897770430892706, 0.016663815826177597, -0.019706549122929573, -0.02923612669110298, 0.025442423298954964, -0.0031560256611555815, 0.01698751002550125, 0.015822209417819977, 0.005907432641834021, 0.008655603043735027, -0.010565402917563915, 0.0022885233629494905, -0.029365604743361473, -0.01378940511494875, 0.009464840404689312, -0.00693354569375515, -0.05427716672420502, 0.016158850863575935, 0.00040603484376333654, 0.0036577528808265924, 0.03371606394648552, -0.009775587357580662, -0.004162717144936323, 0.026141604408621788, 0.010397081263363361, 0.010902046225965023, -0.007477353326976299, -0.007833417505025864, 0.017583109438419342, -0.023616783320903778, -0.011659491807222366, 0.0013117737835273147, -0.012041452340781689, 0.0014760489575564861, 0.02421238273382187, 0.002783776493743062, -0.0025571901351213455, 0.027319854125380516, 0.050030291080474854, -0.01894262805581093, 0.030453220009803772, 0.005295649170875549, -0.0030265478417277336, -0.013621083460748196, 0.00869444664567709, -0.02533883973956108, 0.02817440778017044, -0.004347223322838545, 0.0054024686105549335, -0.000619875849224627, -0.013116119429469109, -0.009322414174675941, -0.008759185671806335, -0.010306446813046932, 0.016430756077170372, 0.00438606645911932, -0.023474358022212982, -0.02312476746737957, -0.010332342237234116, 0.017893856391310692, 0.01829523779451847, -0.0025312944781035185, 0.01422963012009859, -0.0009710848098620772, 0.0136340307071805, -0.0002207194920629263, -0.002903543645516038, -0.0052438583225011826, 0.026348767802119255, -0.03016836941242218, 0.014074256643652916, -0.008778606541454792, 0.00034372357185930014, -0.0017592820804566145, 0.01346570998430252, -0.031307775527238846, -0.010125177912414074, -0.026063917204737663, -0.01676739752292633, -0.00585887860506773, -0.005726163741201162, 0.007762204855680466, -0.0018774307100102305, 0.013582239858806133, 0.011413483880460262, -0.02387573942542076, -0.01614590361714363, -0.005700267851352692, -0.02489861473441124, -0.017596056684851646, 0.016689712181687355, 0.0020263304468244314, -0.01804923079907894, -0.0006117834709584713, 0.006214942783117294, -0.0022011257242411375, 0.007710413541644812, 0.020548155531287193, 0.01118689775466919, -0.02682783640921116, 0.022088943049311638, 0.01149764470756054, 0.01259173359721899, 0.012429885566234589, -0.005528709851205349, 0.022231368348002434, 0.009432470425963402, -0.004965480417013168, -0.012132086791098118, -0.008286590687930584, 0.011737179011106491, -0.011653018184006214, 0.01716878078877926, -0.00195188052020967, 0.039413098245859146, -0.015213662758469582, 0.036978911608457565, 0.015071236528456211, -0.022075995802879333, 0.020638789981603622, -0.013070802204310894, 0.0008796410402283072, -0.005153223406523466, -0.019214531406760216, 0.0141001520678401, 0.027993138879537582, -0.00811826903373003, 0.01869661919772625, 0.0059883566573262215, 0.0386362299323082, 0.0336642749607563, -0.014656906947493553, 0.02662067301571369, -0.012235668487846851, -0.004415199160575867, -0.020496364682912827, 0.015874000266194344, -0.010973258875310421, 0.013659927062690258, 0.0005409751902334392, 0.004628837574273348, -0.02328014001250267, -0.008344856090843678, -0.007762204855680466, 0.02651708945631981, 0.02629697695374489, -0.020366886630654335, -0.0016095731407403946, -0.01922748051583767, -0.024290068075060844, 0.006758750416338444, 0.022956445813179016, -0.0028274753130972385, -0.006998284719884396, -0.0035703552421182394, -0.006745802704244852, 0.0014995168894529343, 0.020574050024151802, 0.010332342237234116, -0.027760079130530357, -0.013193805702030659, 0.03902466222643852, -0.0058685895055532455, 0.010779041796922684, -0.008849820122122765, -0.007166605908423662, -0.009380679577589035, -0.017816169187426567, 0.01794564723968506, -0.009348309598863125, 0.015563253313302994, 0.03205874562263489, 0.029831726104021072, -0.01820460334420204, 0.013180858455598354, -0.01966770552098751, 0.0123910428956151, -0.00822832528501749, -0.020340990275144577, 0.020431624725461006, -0.00789815653115511, 0.006218180060386658, -0.011426431126892567, -0.00622465368360281, 0.034389350563287735, -0.017181728035211563, 0.0029682826716452837, 0.007218397222459316, 0.013375075533986092, 0.03306867554783821, 0.011788969859480858, 0.006156677845865488, 0.0050561148673295975, 0.02449723333120346, 0.009031089022755623, 0.0038875762838870287, 4.352179530542344e-05, -0.0010155929485335946, -0.01439795084297657, -0.024600815027952194, -0.009853274561464787, -0.0021541898604482412, 0.014643959701061249, -0.015576200559735298, 0.015407879836857319, 0.009069932624697685, 0.004318090621381998, 0.007665096316486597, 0.010371185839176178, -0.0017317679012194276, -0.030997028574347496, -0.0030653912108391523, 0.03594308719038963, -0.009173514321446419, 0.00014424655819311738, -0.008603811264038086, 0.013970674015581608, -0.006804067641496658, 0.007438509725034237, -0.005014034919440746, -0.014825228601694107, 0.010455346666276455, 0.00681701535359025, 0.005476918537169695, -0.0021104910410940647, -0.012222721241414547, 0.01916274055838585, -0.021493343636393547, -0.002458463190123439, -0.027682391926646233, -0.0064447661861777306, -0.001683213748037815, -0.006836437154561281, -0.02053520642220974, 0.029987100511789322, 0.006606613751500845, 0.00537657318636775, -0.010164021514356136, 0.0072378190234303474, 0.01517481915652752, 0.01248167734593153, 0.009639635682106018, -0.020625842735171318, -0.022399690002202988, 0.0026850495487451553, -0.016845084726810455, -0.015757469460368156, -0.005415416322648525, 0.0188519936054945, -0.004806870128959417, 0.003722491906955838, -0.026374664157629013, -0.0345965139567852, -0.0015901514561846852, 0.0869574099779129, 0.010526559315621853, 0.030815759673714638, 0.026154551655054092, 0.01125163584947586, -0.010338816791772842, -0.03205874562263489, -0.022930549457669258, 0.003819600446149707, -0.024769136682152748, -0.016573181375861168, -0.03172210603952408, 0.011277532204985619, 0.01508418470621109, 0.03842906281352043, -0.012876585125923157, -0.010688407346606255, -0.00038357850280590355, -7.556253694929183e-05, -0.013892986811697483, -0.009322414174675941, 0.008085899986326694, 0.017116988077759743, 0.00822832528501749, -0.016430756077170372, -0.04959006607532501, 0.017065197229385376, -0.0019356957636773586, 0.003796941600739956, -0.02256801165640354, -0.0033372947946190834, -0.0015772036276757717, -0.008409595116972923, 0.005661424715071917, -0.0016476073069497943, -0.0026737202424556017, 0.03918003663420677, 0.013944778591394424, 0.017596056684851646, -0.006609850563108921, 0.009782060980796814, -0.022775176912546158, -0.015110080130398273, -0.014022464863955975, 0.028977170586586, -0.014190786518156528, -0.028718216344714165, 0.011050945147871971, 0.018877889961004257, -0.02022445946931839, 0.029650457203388214, 0.015187766402959824, -0.0006619561463594437, 0.0015861052088439465, 0.019486436620354652, 0.011232214979827404, 0.0028938327450305223, 0.015420827083289623, -0.0027934873942285776, 0.019395800307393074, -0.02028919942677021, -0.037626300007104874, 0.007509722840040922, -0.010170495137572289, 0.009128197096288204, -0.01586105301976204, -0.01935695856809616, -0.008603811264038086, -0.007406140211969614, -0.01595168747007847, 0.002808053744956851, -0.008105321787297726, -0.013362127356231213, 0.0021460975985974073, 0.018217552453279495, -0.0031819213181734085, 0.006745802704244852, 0.0015755851054564118, 0.030893445014953613, 0.009594318456947803, -0.02219252474606037, -0.030271951109170914, -0.002346788300201297, -0.0392577238380909, -0.0025976519100368023, 0.007988790981471539, -0.019085053354501724, -0.014359108172357082, -0.02000434696674347, -0.0018580090254545212, 0.006231127772480249, -0.007211923599243164, 0.022671593353152275, -0.015809260308742523, -0.00040987873217090964, -0.0020554629154503345, 0.005285938270390034, 0.0022561538498848677, -0.0026138366665691137, -0.00391023512929678, 0.02091069333255291, -0.02471734583377838, -0.017932699993252754, 0.008344856090843678, -0.004473464097827673, -0.0037645723205059767, -0.0007355967536568642, 0.00716013228520751, -0.0007975033950060606, -0.005629055202007294, 0.01747952774167061, -0.031307775527238846, 0.002071647671982646, -0.02359088696539402, 0.0002816146006807685, 0.01960296556353569, 0.005635528825223446, 0.0005057733505964279, 0.0063703167252242565, -0.022231368348002434, -0.0036253833677619696, -0.011814865283668041, 0.012235668487846851, 0.03938720002770424, -0.01235867291688919, -0.011542961932718754, 0.021493343636393547, -0.011860182508826256, 0.02175229974091053, -0.0019955793395638466, -0.039931006729602814, 0.009717321954667568, 0.011834287084639072, -0.008545546792447567, -0.004878082778304815, -0.019344009459018707, 0.007444983813911676, -0.000181370327482, -0.02299528941512108, -0.0012025267351418734, -0.025546004995703697, -0.008454912342131138, -0.0036448051687330008, -0.0171428844332695, 0.00028485155780799687, -0.02296939305961132, -0.004657970275729895, -0.009930960834026337, -0.012416938319802284, 0.015744522213935852, -0.021234387531876564, -0.021791143342852592, -0.0044799381867051125, 0.0029731381218880415, 0.003018455347046256, -0.03249897435307503, -0.038506750017404556, -0.013239122927188873, 0.004169190768152475, 0.01567978225648403, 0.03418218716979027, -0.0008974442607723176, 0.011012102477252483, 0.00018056108092423528, -0.005820035003125668, 0.026089811697602272, 0.000589934061281383, 0.01794564723968506, -0.0021428605541586876, 0.04360818490386009, 0.037445031106472015, 0.0029731381218880415, 0.018722515553236008, 0.0025005433708429337, 0.022166630253195763, 0.01645665057003498, 0.009458365850150585, 0.019408749416470528, 0.014967653900384903, -0.018101021647453308, -0.008940454572439194, 0.03154083713889122, -0.025066936388611794, -0.01645665057003498, -0.011737179011106491, -0.017842065542936325, 0.0005810324219055474, -0.029987100511789322, -0.02724216692149639, 0.012837741523981094, 0.02693141996860504, -0.01745363138616085, -0.00455762492492795, -0.014967653900384903, 0.007315505761653185, -0.03542517498135567, -0.001539978664368391, 0.0010107374982908368, 0.01835997775197029, 0.013148488476872444, 0.013569291681051254, 0.030556803569197655, -0.00402029138058424, -0.029495082795619965, 0.0038454958703368902, 0.0520501472055912, -0.008888662792742252, 0.009840326383709908, 0.01463101152330637, -0.013737613335251808, 0.00866207666695118, -0.02923612669110298, -0.012352199293673038, -0.04513602331280708, 0.014954706653952599, 0.003521800972521305, 0.0026219291612505913, 0.0035897770430892706, 0.004907215479761362, -0.023047080263495445, 0.03962026163935661, -0.012125612236559391, 0.03586539998650551, 0.006305577699095011, 0.0193181149661541, 0.015498514287173748, 0.00633470993489027, -0.009943909011781216, 0.030220160260796547, 0.005703505128622055, -0.0017689928645268083, 0.022542115300893784, 0.01257231179624796, 0.011847235262393951, -0.0072442926466465, -0.0020020531956106424, -0.01617179997265339, -0.022826967760920525, -0.01957707107067108, 0.019046209752559662, 0.033172257244586945, 0.016754450276494026, -0.012183877639472485, -0.0023435514885932207, 0.012643524445593357, 0.002867937320843339, -0.0037775200325995684, -0.004780974239110947, -0.003266081912443042, -0.0467415489256382, -0.012598207220435143, -0.019615912809967995, -0.01117394957691431, -0.01683213748037815, -0.006661641877144575, -0.03889518603682518, 0.012403990142047405, -0.011665965430438519, 0.006078991107642651, -0.01736299693584442, -0.026167498901486397, 0.04521371051669121, 0.011659491807222366, -0.009056984446942806, 0.026193395256996155, -0.0013781312154605985, -0.019486436620354652, -0.011471749283373356, -0.003118800697848201, 0.02786366082727909, 0.005379809997975826, -0.0032709373626857996, 0.003230475587770343, 0.009827378205955029, -0.008577915839850903, 0.0021153464913368225, -0.013621083460748196, -0.015420827083289623, -0.010306446813046932, -0.031178297474980354, -0.011957291513681412, 0.011523540131747723, -0.00889513734728098, 0.01355634443461895, -0.008435490541160107, -0.016741503030061722, 0.012242143042385578, -0.0033631904516369104, 0.019551174715161324, -0.026542985811829567, -0.029210232198238373, -0.023176558315753937, 0.011057419702410698, 0.0012502716854214668, -0.017557213082909584, -0.00044184361468069255, 0.0015027538174763322, 0.03754861280322075, -0.015886947512626648, 0.01801038719713688, -0.02168756164610386, 0.005826509092003107, -0.008862767368555069, 0.019085053354501724, -0.001272930414415896, -0.009529579430818558, 0.010558929294347763, -0.018282290548086166, 0.0035444595851004124, 0.013491605408489704, 0.010202865116298199, 0.024354808032512665, 0.013983621262013912, -0.017906803637742996, 0.002309563336893916, 0.02299528941512108, -0.008027634583413601, -0.005648477002978325, 0.0002723083598539233, 0.035917192697525024, -0.01621064357459545, 0.006425344850867987, 0.01779027469456196, -0.008927506394684315, 0.0011426431592553854, 0.004457279574126005, -0.0035120900720357895, 0.01126458402723074, -0.03703070059418678, -0.003347005695104599, -0.01916274055838585, 0.039931006729602814, -0.004376355558633804, 0.011640070006251335, -0.014074256643652916, -0.009652582928538322, -0.007198975421488285, 0.024393651634454727, -0.009743218310177326, -0.02290465496480465, 0.02318950556218624, 0.023383723571896553, -0.0031754474621266127, 0.010008648037910461, -0.0030653912108391523, -0.02496335469186306, 0.0024681738577783108, -0.038662124425172806, -0.035140324383974075, -0.03218822553753853, -0.026905523613095284, 0.04536908492445946, 0.007645674515515566, -0.0019486435921862721, -0.004836002364754677, 0.009665531106293201, -0.03125598281621933, -0.02877000719308853, -9.533827324048616e-06, 0.019279271364212036, 0.02549421414732933, 0.005114380270242691, -0.006399448961019516, 0.00869444664567709, 0.005457496736198664, 0.0132455974817276, -0.019654756411910057, 0.0216616652905941, -0.009031089022755623, -0.01157533098012209, 0.016845084726810455, 0.005237384233623743, -0.0005272181588225067, -0.004233929794281721, -0.007943473756313324, 0.01736299693584442, -0.011089788749814034, 0.02356499247252941, -0.02414764277637005, -0.011394062079489231, -0.027785973623394966, -0.016094112768769264, -0.014721645973622799, 0.002252916805446148, -0.0026219291612505913, -0.02069058082997799, 0.0057811918668448925, -0.008448437787592411, 0.0053992317989468575, -0.023137714713811874, -0.01007986068725586, 0.01876135915517807, -0.008921032771468163, -0.01007986068725586, -0.008921032771468163, -0.012365146540105343, 0.024536076933145523, -0.011743652634322643, 0.010112229734659195, 0.019214531406760216, -0.00967847928404808, 0.0019939609337598085, 0.014592167921364307, -0.0014622919261455536, -0.004460516385734081, 0.008027634583413601, -0.03293919935822487, -0.03604666888713837, -0.025817908346652985, -0.0032822666689753532, 0.012637050822377205, -0.003010363085195422, 0.03964615613222122, -0.015666835010051727, -0.007567987777292728, -0.005496340338140726, -0.0076197790913283825, -0.004959006793797016, -0.007024180144071579, 0.02449723333120346, -0.027164479717612267, -0.001715583261102438, -0.020276252180337906, 0.0036027247551828623, -0.02135091833770275, -0.0026154550723731518, -0.0107531463727355, -0.0038066525012254715, -0.017583109438419342, -0.00842901598662138, -0.012423411943018436, -0.013478657230734825, -0.017647847533226013, -0.03309457004070282, -0.011924921534955502, 0.03902466222643852, 0.20778626203536987, 0.006422107573598623, -0.012080295011401176, 0.016650868579745293, -0.017660796642303467, 0.018088074401021004, 0.022645698860287666, -0.0006623608060181141, -0.012863636948168278, 0.012009082362055779, -0.013193805702030659, 0.00944541860371828, 0.033301737159490585, 0.008396646939218044, 0.009438944980502129, -0.017997438088059425, -0.021700508892536163, -0.02113080583512783, -0.026284029707312584, -0.019188636913895607, -0.004114162642508745, 0.005713215563446283, -0.005680846516042948, -0.002369446912780404, 0.029779935255646706, 0.008545546792447567, -0.0165213905274868, 0.004288957919925451, 0.017751431092619896, 0.025002198293805122, -0.004230692982673645, -0.028070826083421707, 0.0031803029123693705, -0.005535183474421501, -0.031929269433021545, 0.016404859721660614, -0.0244583897292614, -0.00933536235243082, -0.010791989043354988, 0.006043384782969952, -0.004068845417350531, 0.014385003596544266, -0.005175882019102573, -0.00130287220235914, 0.008195956237614155, 0.014255525544285774, -0.021894726902246475, 0.011646544560790062, -0.014605116099119186, 0.010837307199835777, -0.04153653606772423, -0.013944778591394424, 0.029210232198238373, 0.02851105108857155, -0.015524409711360931, -0.021609874442219734, 0.01190549973398447, 0.02421238273382187, -0.004797159228473902, -0.027345748618245125, 0.022516220808029175, 0.02611570805311203, -0.020250355824828148, -0.017647847533226013, -0.003842259058728814, 0.0244583897292614, -0.026452351361513138, -0.02788955718278885, 0.04182138666510582, -0.035632338374853134, 0.021791143342852592, -0.003974974155426025, -0.00591390673071146, 0.013219701126217842, 0.02396637387573719, -0.02359088696539402, -0.02682783640921116, 0.01953822746872902, 0.0043116165325045586, 0.03534748777747154, -0.024937458336353302, 0.010902046225965023, -0.016404859721660614, -0.00794994831085205, -0.00455762492492795, -0.01785501278936863, 0.0032968330197036266, 0.011206318624317646, 0.0022027441300451756, -0.00800821278244257, -0.013905934989452362, -0.028744110837578773, -0.016754450276494026, 0.005917143542319536, 0.010545981116592884, 0.011076840572059155, 0.009141145274043083, 0.012831267900764942, -0.010053965263068676, -0.0020360411144793034, -0.03019426390528679, 0.028381573036313057, 0.028277991339564323, -0.019279271364212036, -0.03029784746468067, -0.01835997775197029, 0.011801918037235737, 0.044980648905038834, 0.002332222182303667, -0.029313813894987106, 0.003440877189859748, -0.012119138613343239, -0.013116119429469109, -0.012675894424319267, 0.021363865584135056, 0.006739328615367413, -0.013621083460748196, -0.037004806101322174, 0.002421238226816058, -0.004285721108317375, -0.008293064311146736, -0.00384873291477561, 0.0015067999484017491, 0.013362127356231213, -0.006483609788119793, 0.0032498971559107304, -0.007969369180500507, -0.0028663186822086573, 0.03262845054268837, -0.02739753946661949, 0.01547261793166399, -0.02480798028409481, 0.004334275145083666, -0.0052632796578109264, -0.0036027247551828623, 0.008480807766318321, 0.017958596348762512, 0.015278401784598827, -0.002523201983422041, -0.018748411908745766, 0.0011329322587698698, -0.01583515666425228, 0.010384134016931057, 0.007937000133097172, -0.009710848331451416, -0.008163586258888245, 0.010584824718534946, -0.005726163741201162, -0.020017296075820923, -0.018813150003552437, -0.013724666088819504, -0.02640056051313877, -0.0022836679127067327, -0.008966349996626377, 0.027268061414361, -0.022451480850577354, -0.010358238592743874, 0.010856728069484234, -0.012488150969147682, -0.012565838173031807, -0.03949078172445297, 0.012436360120773315, 0.013931830413639545, 0.00546073354780674, -0.015148923732340336, -0.010681932792067528, -0.1639709174633026, 0.023293089121580124, 0.015964634716510773, -0.006894702557474375, 0.026879629120230675, -0.02465260773897171, 0.03288740664720535, 0.002220547292381525, -0.022399690002202988, 0.0008723578648641706, -0.012598207220435143, -0.00705007603392005, -0.017414787784218788, -0.014902914874255657, -0.004399014171212912, 0.015019445680081844, -0.042805418372154236, 0.02006908692419529, 0.022399690002202988, -0.0007533999742008746, 0.006153441034257412, -0.016819190233945847, -0.022477377206087112, -0.019188636913895607, 0.002359736245125532, 0.02215368114411831, -0.0029456240590661764, 0.006862333044409752, -0.009561948478221893, -0.002031185897067189, -0.01191844791173935, 0.00922530610114336, -0.002044133609160781, 0.011996135115623474, 0.01623653806746006, 0.0047777374275028706, -0.009918013587594032, 0.0023273667320609093, -0.007283136248588562, -0.004780974239110947, 0.02662067301571369, 0.017777325585484505, 0.018994418904185295, 0.005470444448292255, -0.007147184573113918, 0.02372036501765251, 0.03278382495045662, -0.007406140211969614, 0.023539096117019653, -0.03063448891043663, -0.006409159861505032, -0.024639658629894257, -0.0026397323235869408, -0.006101649720221758, 0.02044457197189331, 0.018593037500977516, -0.001836968818679452, 0.011814865283668041, -0.004415199160575867, 0.0019227479351684451, -0.03659047558903694, -0.007477353326976299, 0.020871849730610847, 0.00444109458476305, -0.015537356957793236, -0.01791975274682045, -0.001009118976071477, 0.0006902794702909887, -0.023383723571896553, 0.006247312296181917, -0.015874000266194344, 0.009199410676956177, 0.0015237939078360796, -0.027811869978904724, 0.000155980495037511, 0.013724666088819504, -0.02306002750992775, -0.004350460134446621, 0.002518346766009927, -0.0019713023211807013, -0.021428605541586876, 0.025377683341503143, 0.014825228601694107, -0.02443249523639679, 0.03835137560963631, 0.027216270565986633, -0.024691451340913773, -0.02137681469321251, -0.010850254446268082, -0.03723786771297455, 0.0017835590988397598, -0.025079883635044098, -0.02028919942677021, -0.0032223830930888653, 0.02436775527894497, 0.0033033068757504225, 0.025753170251846313, -0.007749257143586874, 0.010209338739514351, -0.028407467529177666, -0.013880039565265179, -0.009820904582738876, -0.01264999806880951, 0.001183914253488183, 0.03288740664720535, 0.0349072627723217, 0.01061072014272213, 0.01701340638101101, 0.006331473123282194, 0.007315505761653185, -0.02015972137451172, 0.03599487617611885, 0.025610744953155518, 0.0059883566573262215, -0.005285938270390034, 0.02115670219063759, 0.01966770552098751, -0.04365997388958931, 0.009963330812752247, 0.014708698727190495, 0.0467415489256382, -0.0010212576016783714, 0.014035413041710854, 0.006862333044409752, -0.009037562645971775, 0.0030281662475317717, -0.08436784893274307, 0.001717201666906476, 0.0035088532604277134, 0.011769548058509827, 0.0007809140370227396, 0.027449332177639008, -0.020366886630654335, 0.03690122440457344, -0.01663791947066784, 0.006648694165050983, -0.003926419652998447, -0.04640490561723709, -0.032240018248558044, -0.020056139677762985, 0.02206304669380188, 0.005065825767815113, -0.008377225138247013, -0.009626687504351139, -0.03413039445877075, 0.005175882019102573, -0.0216616652905941, -0.008344856090843678, -0.0001375703577650711, -0.01191844791173935, 0.0022367320489138365, 0.003696596249938011, -0.02015972137451172, 0.006205231882631779, 0.0016508442349731922, 0.014126047492027283, -0.006486846599727869, -0.020677633583545685, 0.023098871111869812, -0.018618933856487274, -0.0019065631786361337, -0.00967847928404808, 0.006438292562961578, -0.005250331945717335, 0.024549024179577827, -0.03260255604982376, -0.003118800697848201, -0.0031527888495475054, 0.0032968330197036266, -0.04946058616042137, 0.0014040268724784255, -0.007011232431977987, -0.014436794444918633, 0.00016700636479072273, 0.03371606394648552, -0.01244930736720562, -0.014164891093969345, -0.008098847232758999, -0.009464840404689312, -0.009503684006631374, 0.013400970958173275, -0.015524409711360931, 0.025442423298954964, -0.030090682208538055, -0.022412637248635292, 0.024924511089920998, 0.021247336640954018, -0.015938738361001015, -0.012585259042680264, 0.021713456138968468, 0.0062699709087610245, -0.01299311500042677, 0.004165953956544399, -0.027268061414361, 0.019654756411910057, -0.0031592627055943012, -0.008901610970497131, 0.0072378190234303474, -0.03374196216464043, -0.005175882019102573, -0.03016836941242218, 0.0022399690933525562, -0.034233976155519485, -0.00769746582955122, 0.02502809278666973, -0.02303413301706314, -0.015692731365561485, -0.008933980949223042, 0.005201777908951044, -0.02788955718278885, 0.021635770797729492, 0.04254646226763725, 0.022024204954504967, 0.014022464863955975, -0.009205884300172329, -0.0282003041356802, -0.0005603968747891486, 0.012293933890759945, -0.0023856316693127155, -0.01149764470756054, 0.0048133437521755695, 0.00857144221663475, 0.0009629924898035824, 0.007341401185840368, 0.005124091170728207, 0.006952967494726181, -0.03001299500465393, 0.004399014171212912, -0.07949947565793991, 0.007334927562624216, -0.023862792178988457, -0.01041002944111824, 0.02119554579257965, 0.007341401185840368, 0.008383698761463165, -0.021648718044161797, 0.006072517018765211, 0.007509722840040922, -0.01148469652980566, 0.02131207473576069, 0.010274077765643597, -1.5641040590708144e-05, -0.011840760707855225, -0.0025895596481859684, 0.02059994637966156, -0.008487281389534473, 0.011950816959142685, 0.025571901351213455, -0.012086769565939903, 0.003906997852027416, -0.006137256044894457, -0.014372055418789387, -0.007982317358255386, -0.020988380536437035, 0.0025102542713284492, 0.018968524411320686, -0.011976713314652443, -0.0035023794043809175, 0.0033696643076837063, -0.02203715220093727, 0.02529999613761902, 0.017971543595194817, 0.004227456171065569, -0.025442423298954964, -0.008577915839850903, -0.01233925111591816, 0.03003889136016369, 0.010028069838881493, -0.02474324218928814, -0.01463101152330637, 0.01561504416167736, -0.022801071405410767, -0.022075995802879333, 0.009244727902114391, -0.021700508892536163, 0.004246877506375313, 0.01636601611971855, 0.008946928195655346, 0.021829986944794655, 0.014915863052010536, -0.021804092451930046, -0.016262434422969818, 0.003347005695104599, -0.02022445946931839, 0.01798449084162712, -0.0009095827699638903, -0.0011062275152653456, -0.006642220076173544, 0.0182304996997118, -0.0008051911718212068, -0.01683213748037815, -0.009134671650826931, -0.005752059165388346, 0.01061072014272213, -0.014566272497177124, 0.022114839404821396, -0.0032223830930888653, -0.01539493165910244, -0.021739352494478226, -0.005347440484911203, 0.0029342947527766228, 0.02084595523774624, 0.0006077372818253934, -0.00716013228520751, 0.022710436955094337, 0.013142014853656292, 0.00942599680274725, 0.005234147422015667, 0.033457107841968536, 0.004172428045421839, -0.02529999613761902, 0.026698358356952667, 0.03508853167295456, 0.03765219449996948, -0.014889967627823353, 0.025908542796969414, -2.9916493076598272e-05, -0.007723361253738403, -0.006590429227799177, 0.01960296556353569, 0.008629707619547844, 0.014877019450068474, -0.011860182508826256, -0.005651713814586401, -0.01621064357459545, -0.019188636913895607, 0.0077427830547094345, 0.02954687550663948, -0.010118704289197922, 0.006965915206819773, -0.002694760449230671, -0.01807512529194355, -0.02509283274412155, 0.028821798041462898, -0.024976301938295364, -0.022632749751210213, -0.015187766402959824, 0.008823923766613007, 0.02724216692149639, 0.010584824718534946, -0.022736333310604095, 0.006842911243438721, -0.03493315726518631, -0.013491605408489704, -0.013388022780418396, -0.03446703776717186, -0.0019486435921862721, -0.0015772036276757717, 0.008901610970497131, 0.023979321122169495, 0.038196004927158356, -0.01248167734593153, 0.007736308965831995, 0.00325313420034945, 0.023396670818328857, -0.018178708851337433, -0.0001203740612254478, -0.015511461533606052, 0.023111818358302116, -0.012222721241414547, -0.01115452777594328, -0.009167040698230267, -0.01385414320975542, -0.0031738290563225746, -0.0038357852026820183, 0.02159692719578743, -0.01966770552098751, 0.03905055671930313, -0.004787448327988386, -0.0009314321796409786, 0.0033599536400288343, -0.026776045560836792, -0.01017696876078844, -0.013841195963323116, 0.0006340374820865691, -0.030686281621456146, -0.021247336640954018, 0.02724216692149639, 0.015744522213935852, 0.027811869978904724, -0.012837741523981094, -0.021713456138968468, 0.0017398602794855833, 0.0021202019415795803, -0.0071536581963300705, 0.010902046225965023, -0.012099716812372208, 0.011219266802072525, 0.015187766402959824, 0.014605116099119186, -0.0069076502695679665, 0.014190786518156528, -0.0002251702971989289, 0.025261154398322105, -0.002346788300201297, -0.01991371251642704, -0.05026335269212723, 0.004470227286219597, -0.019680652767419815, -0.023539096117019653, -0.009807956404983997, 0.020483415573835373, -0.009069932624697685, 0.013737613335251808, 0.0006384882726706564, 0.011465274728834629, 0.0271126888692379, -0.03508853167295456, 0.02817440778017044, -0.028096720576286316, -0.009943909011781216, 0.03091934137046337, 0.005344203673303127, -0.005862115416675806, -0.013362127356231213, -0.02596033550798893\], metadata={'director': 'Francis Ford Coppola', 'theme': 'Mafia', 'year': 1972, 'ref\_doc\_id': 'None', '\_node\_content': '{"id\_": "736a1279-4ebd-496e-87b5-925197646477", "embedding": null, "metadata": {"director": "Francis Ford Coppola", "theme": "Mafia", "year": 1972, "ref\_doc\_id": "doc\_1"}, "excluded\_embed\_metadata\_keys": \[\], "excluded\_llm\_metadata\_keys": \[\], "relationships": {}, "text": "", "start\_char\_idx": null, "end\_char\_idx": null, "text\_template": "{metadata\_str}\\\\n\\\\n{content}", "metadata\_template": "{key}: {value}", "metadata\_seperator": "\\\\n", "class\_name": "TextNode"}', '\_node\_type': 'TextNode', 'document\_id': 'None', 'doc\_id': 'None'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='The Godfather', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.7543986421543848)\]

Back to top

[Previous DocArray InMemory Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DocArrayInMemoryIndexDemo/)[Next Elasticsearch Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ElasticsearchIndexDemo/)
