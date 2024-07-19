Title: Pinecone Vector Store - Metadata Filter

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/pinecone_metadata_filter/

Markdown Content:
Pinecone Vector Store - Metadata Filter - LlamaIndex
===============
             

[Skip to content](https://docs.llamaindex.ai/en/stable/examples/vector_stores/pinecone_metadata_filter/#pinecone-vector-store-metadata-filter)

[![Image 1: logo](https://docs.llamaindex.ai/en/stable/_static/assets/LlamaSquareBlack.svg)](https://docs.llamaindex.ai/en/stable/ "LlamaIndex")

LlamaIndex

Pinecone Vector Store - Metadata Filter

  

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
        *    [Pinecone Vector Store - Metadata Filter](https://docs.llamaindex.ai/en/stable/examples/vector_stores/pinecone_metadata_filter/)
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
    

       

[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/docs/examples/vector_stores/pinecone_metadata_filter.ipynb)

Pinecone Vector Store - Metadata Filter[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/pinecone_metadata_filter/#pinecone-vector-store-metadata-filter)
=======================================================================================================================================================================

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-pinecone

%pip install llama-index-vector-stores-pinecone

In \[ \]:

Copied!

\# !pip install llama-index>=0.9.31 pinecone-client>=3.0.0

\# !pip install llama-index>=0.9.31 pinecone-client>=3.0.0

In \[ \]:

Copied!

import logging
import sys
import os

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys import os logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

In \[ \]:

Copied!

import os

os.environ\[
    "PINECONE\_API\_KEY"
\] \= "<Your Pinecone API key, from app.pinecone.io>"
os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import os os.environ\[ "PINECONE\_API\_KEY" \] = "" os.environ\["OPENAI\_API\_KEY"\] = "sk-..."

Build a Pinecone Index and connect to it

In \[ \]:

Copied!

from pinecone import Pinecone
from pinecone import ServerlessSpec

api\_key \= os.environ\["PINECONE\_API\_KEY"\]
pc \= Pinecone(api\_key\=api\_key)

from pinecone import Pinecone from pinecone import ServerlessSpec api\_key = os.environ\["PINECONE\_API\_KEY"\] pc = Pinecone(api\_key=api\_key)

In \[ \]:

Copied!

\# delete if needed
\# pc.delete\_index("quickstart-index")

\# delete if needed # pc.delete\_index("quickstart-index")

In \[ \]:

Copied!

\# Dimensions are for text-embedding-ada-002
pc.create\_index(
    "quickstart-index",
    dimension\=1536,
    metric\="euclidean",
    spec\=ServerlessSpec(cloud\="aws", region\="us-west-2"),
)

\# Dimensions are for text-embedding-ada-002 pc.create\_index( "quickstart-index", dimension=1536, metric="euclidean", spec=ServerlessSpec(cloud="aws", region="us-west-2"), )

In \[ \]:

Copied!

pinecone\_index \= pc.Index("quickstart-index")

pinecone\_index = pc.Index("quickstart-index")

Build the PineconeVectorStore and VectorStoreIndex

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, StorageContext
from llama\_index.vector\_stores.pinecone import PineconeVectorStore

from llama\_index.core import VectorStoreIndex, StorageContext from llama\_index.vector\_stores.pinecone import PineconeVectorStore

In \[ \]:

Copied!

from llama\_index.core.schema import TextNode

nodes \= \[
    TextNode(
        text\="The Shawshank Redemption",
        metadata\={
            "author": "Stephen King",
            "theme": "Friendship",
            "year": 1994,
        },
    ),
    TextNode(
        text\="The Godfather",
        metadata\={
            "director": "Francis Ford Coppola",
            "theme": "Mafia",
            "year": 1972,
        },
    ),
    TextNode(
        text\="Inception",
        metadata\={
            "director": "Christopher Nolan",
            "theme": "Fiction",
            "year": 2010,
        },
    ),
    TextNode(
        text\="To Kill a Mockingbird",
        metadata\={
            "author": "Harper Lee",
            "theme": "Mafia",
            "year": 1960,
        },
    ),
    TextNode(
        text\="1984",
        metadata\={
            "author": "George Orwell",
            "theme": "Totalitarianism",
            "year": 1949,
        },
    ),
    TextNode(
        text\="The Great Gatsby",
        metadata\={
            "author": "F. Scott Fitzgerald",
            "theme": "The American Dream",
            "year": 1925,
        },
    ),
    TextNode(
        text\="Harry Potter and the Sorcerer's Stone",
        metadata\={
            "author": "J.K. Rowling",
            "theme": "Fiction",
            "year": 1997,
        },
    ),
\]

from llama\_index.core.schema import TextNode nodes = \[ TextNode( text="The Shawshank Redemption", metadata={ "author": "Stephen King", "theme": "Friendship", "year": 1994, }, ), TextNode( text="The Godfather", metadata={ "director": "Francis Ford Coppola", "theme": "Mafia", "year": 1972, }, ), TextNode( text="Inception", metadata={ "director": "Christopher Nolan", "theme": "Fiction", "year": 2010, }, ), TextNode( text="To Kill a Mockingbird", metadata={ "author": "Harper Lee", "theme": "Mafia", "year": 1960, }, ), TextNode( text="1984", metadata={ "author": "George Orwell", "theme": "Totalitarianism", "year": 1949, }, ), TextNode( text="The Great Gatsby", metadata={ "author": "F. Scott Fitzgerald", "theme": "The American Dream", "year": 1925, }, ), TextNode( text="Harry Potter and the Sorcerer's Stone", metadata={ "author": "J.K. Rowling", "theme": "Fiction", "year": 1997, }, ), \]

In \[ \]:

Copied!

vector\_store \= PineconeVectorStore(
    pinecone\_index\=pinecone\_index, namespace\="test\_05\_14"
)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex(nodes, storage\_context\=storage\_context)

vector\_store = PineconeVectorStore( pinecone\_index=pinecone\_index, namespace="test\_05\_14" ) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex(nodes, storage\_context=storage\_context)

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"

Upserted vectors:   0%|          | 0/7 \[00:00<?, ?it/s\]

Define metadata filters

In \[ \]:

Copied!

from llama\_index.core.vector\_stores import (
    MetadataFilter,
    MetadataFilters,
    FilterOperator,
)

filters \= MetadataFilters(
    filters\=\[
        MetadataFilter(
            key\="theme", operator\=FilterOperator.EQ, value\="Fiction"
        ),
    \]
)

from llama\_index.core.vector\_stores import ( MetadataFilter, MetadataFilters, FilterOperator, ) filters = MetadataFilters( filters=\[ MetadataFilter( key="theme", operator=FilterOperator.EQ, value="Fiction" ), \] )

Retrieve from vector store with filters

In \[ \]:

Copied!

retriever \= index.as\_retriever(filters\=filters)
retriever.retrieve("What is inception about?")

retriever = index.as\_retriever(filters=filters) retriever.retrieve("What is inception about?")

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"

Out\[ \]:

\[NodeWithScore(node=TextNode(id\_='7fed3d0b-e2d7-432a-9231-3ac02130c00f', embedding=\[0.00310940156, -0.0246712118, -0.0222742166, -0.0364649445, -0.00715911388, 0.0117236068, -0.0400604382, -0.0275654588, -0.0157589763, 0.00740136392, 0.0278459582, 0.029962454, 0.0187679715, -0.00440511806, 0.00412780605, 0.00442743069, 0.0276674572, -0.00760536361, -0.00303608901, -0.012947605, -0.00570242899, -0.01923972, 0.00208462193, 0.0092118606, 0.00205274695, -0.0128328558, 0.0136297289, -0.0292994548, 0.0149939768, -0.0193289705, 0.0219937172, -0.00944136083, -0.0221977159, -0.00928198546, -0.00940948538, -0.00429993076, -0.0119786067, -0.0272339582, 0.0158864763, -0.0080261128, 0.0143437283, 0.00407999381, -0.00648655277, -0.0170722231, 0.00394293154, -0.0149939768, -0.00831298716, -0.0212669671, -0.0228479654, 0.0105123585, 0.0167662241, 0.0527849197, -0.0421514362, -0.0262139607, -0.00156506011, -0.00443380559, -0.00724836392, 0.00597655354, 0.0354959443, -0.00842773728, -0.00259143347, -0.00748423859, -0.0113602327, 0.00446568057, 0.00110207649, -0.00814723782, -0.0293504559, -0.00159932568, -0.002620121, -0.00987486, 0.0405959375, 0.0500819236, 0.0242504627, 0.00166227866, 0.00172921608, 0.020769719, 0.0108884834, -0.0177224725, -0.0181432217, 0.0102828592, -0.00192684087, -0.01313248, -0.0168554746, 0.0307019539, 0.0214709677, 0.0193544701, -0.00752248848, 0.0236257147, 0.0111753577, -0.00342974486, 0.00284962077, 0.00194277824, 0.039830938, 0.023485465, -0.0199919697, 0.0154529763, -0.0131962299, -0.00124949811, 0.0134894792, -0.0197624695, 0.021203218, 0.0137062287, -0.0169574749, -0.0205147192, -0.00436049327, -0.0307019539, 0.0176587235, -0.00387918158, 0.0247349627, -0.0103529841, -0.0174547229, 0.0141524784, 0.0326144509, -0.015287227, -0.0133619793, 0.00142720097, 0.0320789516, -0.0129093556, 0.011219983, -0.0230137147, 0.0161542259, 0.0332009494, 0.00287193316, -0.0117682321, 0.0194564704, 0.0134257292, 0.00268227723, -0.00101840473, -0.00237309, -0.0019013409, 0.0287129562, 0.00605305331, 0.0164729748, -0.00611361582, -0.0191632211, 0.0252832118, -0.0152362268, 0.034271948, -0.0182197224, -0.0288659558, 0.017327223, 0.0317219533, -0.0138847288, 0.0215219669, 0.00148616964, 0.0190229714, 0.000236273074, 0.0140377283, 0.0296309553, 1.55763919e-05, 0.0136679793, 0.00215315307, -0.00300102658, 0.0186659712, -0.00411505625, 0.0307274535, 0.0160777252, 0.00638455292, 0.00648655277, 0.0150959771, 0.0026759021, 0.004376431, 0.0038313691, 0.00076499884, 0.0301154535, 0.0223762151, 0.0180412233, -0.00129252928, -0.0119339814, 0.0129731055, -0.00279383943, 0.00654074, -0.0249262117, 0.0291209556, -0.00252768374, 0.00199537189, 0.014241728, 0.00161526317, -0.0360569432, -0.0294269547, 0.018002972, 0.0166514739, 0.0377909429, 0.0324359499, -0.0249134619, -0.0124949813, 0.0245819632, -0.0213179681, 0.0189974718, 0.00352855702, 0.00503305485, 0.0214582179, 0.0238169637, 0.00242090249, -0.651575, -0.0190357212, 0.0048704925, -0.00865723658, 0.0117427325, 0.0166514739, 0.00119531073, 0.0226567145, -0.014547728, -0.0105697336, -0.0111052329, -0.00859348662, 0.0186914708, -0.0139102284, -0.0432989337, -0.00793686323, -0.0220829658, -0.00709536439, -0.0278714579, 0.00343611976, -0.0167789739, 0.0162434746, -0.0455939323, -0.0106079839, -0.00494380482, 0.00252927747, 0.0331244506, -0.0257294606, 0.00623155292, -0.00325124501, -0.00392380636, 0.0150577268, 0.00994498469, 0.0225419663, 0.0425594337, 0.0087719867, -0.0111817326, 0.0307784528, 0.00728661381, 0.0435794331, -0.0125651062, -0.00641961535, 0.0209992174, 0.00480355509, -0.0133109801, 0.0251302123, 0.00989398453, -0.0291464552, 0.0231284648, -0.0155167263, 0.0188317206, 0.000304405781, -0.00463780528, 0.0156442262, -0.00439236825, 0.0223762151, 0.02613746, 0.0129539799, -0.00112917018, 0.0151342265, -0.00870823674, -0.0186277218, -0.0297329538, 0.0173782241, -0.0211777184, 0.0227332152, -0.0147772273, -0.0148919774, 0.0182962213, -0.0282539576, 0.0202342197, 0.0331754498, -0.00733123859, -0.0151597271, 0.00619967794, -0.0138974786, 0.0456704311, 0.00312693277, 0.0187552217, 0.0177989732, -0.00784123782, -0.0147899771, -0.0134257292, -0.0149684772, 0.0282029565, -0.00641961535, -0.0279734582, -0.00807711296, 0.0156952254, -0.000839108077, -0.00745236361, -0.00872098655, -0.013502229, 0.000639491191, -0.00991311, 0.00435730582, 0.00927561056, 0.00872736145, 0.0203617197, -0.0186277218, 0.0113538578, -0.00815998763, -0.0027524021, -0.00493105501, -0.000635905308, 0.017135974, 0.00815361273, 0.0165877249, 0.0389129408, -0.0162944756, 0.010722734, -0.0322319493, -0.0147389779, 0.0106079839, 0.00919911079, -0.0267239586, 0.0278204568, 0.0178754721, 0.0171487238, -0.0100214845, -0.0113156075, -0.00483861752, 0.0076563633, 0.00935848616, 0.030574454, 0.00866998639, -0.0131069804, -0.00276515214, -0.0330734514, 0.00422661845, 0.0236002132, 0.0148409773, 0.0381224416, -0.0193927195, 0.000672163034, 0.0186659712, 0.00437961845, -0.0340679474, 0.014981227, -0.0377909429, -0.0340679474, 0.00441468088, -0.00339468243, -0.0119786067, -0.0122782309, -0.0456959307, -0.0199027192, 0.00363055686, 0.00792411249, 0.0147517277, -0.0216877162, 0.00978561, 0.0132599799, 0.021572968, 0.00146146654, -0.0322829522, 0.0089887362, -0.0233834647, -0.0175567232, -0.0252322108, 0.0270809587, 0.0150194773, -0.0400604382, -0.0109076081, 0.0252832118, -0.00270777708, 0.0187169723, 0.0233452152, -0.0171742234, -0.0188189708, 0.008013363, -0.0107482336, -0.00763086323, 0.00140887289, 0.0223889668, 0.0298859552, -0.0158354752, -0.00268387096, 0.0151979765, -0.022006467, 0.0105251092, -0.00608811574, -0.0218024664, -0.0142544778, 0.0248752125, 0.0138337286, 0.0420239344, 0.0274889581, -0.00262808963, 0.00637817755, -0.0112582324, 0.00303130783, 0.00754798856, -0.0215347167, 0.00180093478, 0.0280754566, 0.0172252245, 0.0121889813, 0.00180890353, 0.0209099688, 0.0366434455, -0.0160522256, -0.00279543316, -0.00701248925, 0.0213434678, 0.00352855702, 0.0235747136, -0.0288149565, 0.00874011125, -0.0285344571, 0.0116088577, -0.0122017311, -0.0227587149, -0.00744598871, 0.0111179827, 0.0340424478, -0.0236002132, 0.0103338594, -0.0301154535, -0.0121698566, -0.0130177299, -0.000304405781, 0.0101617342, 0.00903336145, -0.0106526092, -0.0045995554, -0.0228607152, 0.00581399119, 0.0175949726, -0.0402899384, -0.00288627692, 0.0334559493, -0.000845483097, 0.017505724, -0.0204254687, 0.00477168, 0.022682216, -0.0144967278, 0.0385304429, 0.0125523554, 0.00611042837, 0.0132599799, 0.0266474597, -0.0198262203, 0.0127244806, -0.0285344571, 0.0201449692, 0.00233643386, -0.0211139675, 0.0159757249, -0.0153764766, -0.0204892196, -0.0164474752, -0.00671923952, 0.0207314678, -0.00648974, -0.00344249466, -0.0201322194, 0.0180539731, 0.0387089401, -0.00412780605, -0.0156187266, 0.00747148879, 0.0135149797, 0.00484180497, -0.0230392143, -0.00119849818, -0.00277949567, -0.0200174693, -0.00214199675, -0.00164315372, -0.00346799474, 0.00958161056, 0.0107546085, 0.00835123751, 0.0112709831, 0.00632399041, 0.0174929742, 0.0177479722, 0.00944773573, -0.0178117231, -0.0092118606, 0.0112964828, -0.000124710743, 0.00257230853, -0.0060976781, -0.00112518575, 0.00165430992, -0.0106398584, 0.0130496053, -0.0177734736, 0.00953061, 0.00119929505, -0.0203744695, 0.00425211852, -0.0340679474, 0.0217897166, -0.0165494755, 0.00660449, -0.0163454749, -0.0259972103, -0.0103529841, 0.0158099756, -0.00949236, 0.0241739638, -0.00962623488, -0.00284802681, -0.0118001066, 0.013871979, -0.0100724846, 0.0260992106, 0.00933936052, -0.0136042293, -0.0231539644, 0.024416212, -0.0131962299, -0.0149684772, -0.0280754566, -0.000733123859, -0.00204318436, -0.00430949358, -0.0199792199, -0.0221977159, 0.0222359654, 0.0914938599, 0.0360569432, -0.0109777329, 0.0186532214, 0.000553030404, -0.0112454826, -0.0356999449, 0.0175567232, 0.0111116078, -0.0142672285, 0.0156314764, -0.014177978, 0.0179647226, 0.0061454908, 0.00734398887, -0.00976011, -0.0366689451, -0.00565461628, -0.00986211, -0.0170084741, -0.0375359431, -0.0103338594, 0.0229499657, 0.0273104589, 0.00178499729, -0.0478124283, 0.0345014483, -0.000409593136, -0.014177978, -0.0155804763, 0.00433180574, -0.00195074698, -0.0114176078, -0.000521952345, 0.00619330304, 0.0195457209, 0.0266984589, 0.0202087183, 0.0204254687, -0.00956248585, -0.0110159833, -0.0121698566, 0.0150194773, -0.0044879932, 0.0074906135, -0.0359549448, -0.00416286848, 0.0268259589, 0.0286109559, -0.016026726, 0.0222614668, 0.0333029479, -0.0307019539, 0.0120997317, 0.0121252313, 0.00600842852, 0.00340743223, 0.00976011, -0.0134002296, 0.0158737265, -0.0197369698, -0.0283814576, 0.00541874161, -0.0188572221, -0.0190867204, -0.0197369698, -0.00773286307, -0.00750336377, -0.0126097305, -0.00662999, -0.00561317895, -0.0203489698, -0.0283049569, -0.0133492295, 0.0206677187, -0.0204764679, 0.0101234848, -0.00441149343, 0.00349986972, 0.0102318591, -0.0168427248, -0.0273104589, -0.0113538578, -0.0182324722, -0.00424574362, 0.00684036454, -0.0126671055, -0.00795598794, -0.00330543239, 0.0043828059, 0.00100565469, -0.0226057153, 0.020960968, -0.00958798546, 0.0207187179, 0.0172507241, 0.00456768041, 0.0151342265, 0.0291719548, -0.0057693664, 0.0182324722, -0.0191632211, -0.0246712118, 0.00285918312, 0.0150194773, -0.00364649436, 0.00127659179, 0.0320024528, -0.0169574749, 0.00141923223, 0.015784476, 0.00629211543, 0.00872736145, -0.0207824688, -0.00276515214, 0.0309059527, -0.0136934789, 0.0221212171, -0.00494699227, -0.00438599335, 0.00507130474, 0.00595105346, 0.00404174393, 0.0196349695, 0.00284802681, 0.00736311357, 0.0226694662, 0.00342018227, 0.0114813577, 0.0344759487, -0.03292045, 0.0217387173, -0.0119148567, -0.0217514671, -0.0262394603, -0.0215219669, -0.0144712282, 0.00184077839, -0.0189082213, -0.0161032248, -0.0149047272, 0.00319387019, 0.00673199, -0.0224272162, 0.00416605594, -0.0175312236, 0.0166259743, -0.00478124293, -0.0287639555, 0.0186404716, -0.000409593136, 0.00979198515, -0.0206549689, -0.0111116078, 0.00998323504, -0.0555389151, -0.0315944515, -0.012635231, 0.0199792199, 0.0217769668, 0.0261629596, 0.00421386864, 0.0213562176, 0.00668098964, 0.0114749828, 0.0194947198, 0.0109394835, 0.00820461288, -0.0196604691, 0.0161797255, 0.00161207572, -0.0153892264, 0.0204509683, 0.00580761628, 0.0201832186, 0.00758623844, -0.00909711141, 0.0155167263, -0.00188699714, 0.0172124729, -0.0266474597, -0.00180571596, -0.0118893571, -0.0219937172, -0.0216749664, -0.00678936485, -0.000194835637, 0.00770098809, 0.00994498469, -0.0224782154, 0.0363884456, -0.0192014705, 0.0147134773, -0.00682123937, 0.00904611126, -0.00330224494, -0.00842773728, -0.0199537203, 0.0172379743, 0.0123674814, 0.00414374378, 0.0135277295, 0.00713998917, -1.64977773e-05, -0.00359549443, 0.0401114374, -0.00290221442, 0.0211139675, 0.00514780451, -0.000441069627, -0.00517649204, -0.0219937172, -0.0247732121, -0.0268004593, -0.00753523828, 0.0119531071, -0.0121571068, 0.0227587149, 0.000832733116, -0.0200684685, 0.0124184815, -0.0176969729, 0.0300389547, 0.0147517277, 0.0200047195, 0.00207824679, -0.0095242355, -0.0209992174, 0.0251047108, -0.00526574207, -0.00757348863, 0.0141142281, -0.000571756915, 0.00885486137, -0.0168682244, -0.0339914486, -2.20634429e-05, -0.030574454, -0.0202724691, 0.011653482, 0.0153254764, 0.0272084586, -0.012514106, -0.0294269547, -0.00581717864, 0.0279734582, -0.00828111265, -0.0092118606, -0.0189209711, -0.0163709745, -0.00287671434, -0.0150959771, -0.0259589609, 0.0239062142, -0.00864448678, -0.0244544633, 0.0217132177, -0.0194564704, 0.0033723698, 0.0085424874, -0.0157462265, 0.027182959, -0.000542272639, -0.00660449, 0.0440639332, 0.00470474269, -0.00866361149, -0.0151979765, -0.00210374687, 0.0241357125, -0.00737586385, -0.00282890187, -0.0226439647, 0.00282890187, 0.0153892264, 0.0095242355, -0.00895686168, -0.0300899539, -0.00407999381, -0.00869548693, -0.00352536957, -0.00722286385, 0.0174419731, -0.0147134773, -0.00250218366, -0.012016857, -0.0125842309, -0.0059988657, 0.0149557274, -0.0425594337, -0.00617736578, -0.022503715, -0.0100151096, 0.0204382185, -0.0262139607, 0.0023555588, 0.0110032335, 0.0319769494, -0.0156697258, -0.0186659712, -0.0089887362, -0.00308868289, 0.00828748755, 0.00558130397, 0.00385686918, -0.00282412069, 0.0276419576, -0.00897598639, 0.00959436, 0.0196604691, -0.00394611899, 0.00308230775, -0.00324965129, -0.0224144664, -0.0106908586, 0.016026726, -0.0142034786, 0.0100661097, -0.0434009321, -0.00367836934, -0.0325379521, 0.00771373836, 0.0167534743, -0.000457007118, 0.00180730969, 0.0121124815, -0.00100246724, 0.0172634739, -0.0385049395, -0.00703161443, 0.000191847357, 0.0260099601, -0.00822373759, -0.00652799, -0.00789223798, -0.00089329551, -0.014305478, 0.00821736269, -0.0158737265, -0.0115833571, -0.00238105888, 0.0155422259, 0.00782848801, 0.0261629596, -0.0113666076, -0.0228352156, -0.0106271086, -0.021572968, -0.0246839616, -0.00742686354, -0.00859348662, 0.0562529154, 0.00569605362, 0.00518924231, -0.00856798701, -0.0158992261, 0.00338193239, -0.0187679715, -0.0200812202, 0.0280754566, 0.00408318127, 0.0168172251, -0.00800061319, 0.00844686199, -0.0122399814, 0.00731848879, -0.0042712437, 0.0178499725, 0.0225674659, -0.00189655961, 0.0169829745, 0.0148919774, -0.0180157218, -0.0140887285, 0.00970911048, 0.00552074146, 0.000212566083, 0.00837036222, -0.00814086292, -0.0107099833, 0.0033723698, -0.0295544546, -0.00906523596, 0.016523974, 0.00699973945, -0.0294014551, 0.00116423261, -0.00798786245, -0.00812173728, -0.00547292922, 0.00657899, -0.000409194676, 0.000534702325, 0.00583311589, -0.0139229791, -0.014177978, -0.00353811961, -0.0117363567, -0.00189655961, 0.00213562185, 0.035317447, 0.00177862227, 0.00412143115, -0.0011331545, -0.00519561721, -0.000510397658, -0.021330718, -0.0116789825, -0.00831298716, -0.0296564549, 0.00691048941, -0.00402580621, 0.0125204809, -0.0168809742, 0.00562592875, -0.00529761706, 0.0102446098, -0.0209354684, 0.00266155833, 0.0155804763, -0.0378164425, 0.0201832186, -0.017135974, -0.00218184036, 0.00410868134, -0.0244672131, 0.00194437208, 0.00276196445, -0.00252608978, 0.00300899544, -0.0203107186, 0.00905886106, -0.028483456, 0.00229021534, 0.0117554823, 0.0294524543, 0.204203695, -0.000746272271, -0.0162944756, 0.0224272162, 0.0131962299, 0.0272594579, 0.0107482336, -0.0055111791, -0.0119786067, 0.0113474829, -0.00185990345, 0.0160777252, 0.0146624772, -0.0064164279, -0.00578849111, -0.0165494755, -0.0183854718, -0.0131197302, -0.0108247334, -0.00798786245, -0.00350943208, -0.00676386477, -0.0247987118, -0.0216494668, 0.0152489766, -0.000493264874, 0.00163996627, -0.00225355895, 0.0300899539, 0.0210502185, -0.00371024432, -0.0187679715, 0.0101808598, -0.00419155601, -0.031007953, 0.0148664769, 0.00819823705, 0.00376443169, -0.0064738025, -0.00995136, -0.015478476, 0.0143692279, -0.00150131027, 0.00532630458, 0.0191504713, 0.0152107272, -0.0114112329, 0.00415330613, 0.00492786756, 0.0443699323, -0.027004458, -0.0327674486, 0.0117682321, 0.0343994461, -0.0169192236, 0.00193959079, 0.00189815334, 0.0139102284, 0.000863811176, -0.00611680327, 0.00620286539, 0.0261884592, 0.00301058916, -0.0192524698, -0.00057693664, 0.0486284271, -0.0151214767, 0.0140504781, 0.0178627223, -0.0166259743, 0.0195967201, -0.00282093324, -0.0260864608, -0.0151597271, -0.0116662318, -0.0188317206, 0.00863173697, 0.0340169482, 0.0190867204, 0.0404939391, -0.0141524784, -0.00663636485, 0.0173527244, -0.0216494668, -0.0210884679, -0.0218407158, -0.00909073651, -0.00331180752, 0.000288667536, -0.0168554746, 0.00363374455, -0.0040130564, -0.0124758556, 0.0136297289, 0.0182962213, -0.00794323813, 0.0329459496, 0.0170594733, -0.0165877249, 0.000735116075, -0.0199409705, 0.0068913647, 0.0121124815, -0.000981748453, -0.0170849748, -0.00934573542, -0.0193289705, 0.00604667841, 0.0154529763, -0.0351644456, 0.0180412233, 0.010913983, 0.00932661071, -0.00128456054, 0.0141269788, 0.0140759787, -0.0101362346, -0.0200684685, 0.00313968281, -0.0308039524, -0.00195871573, -0.0306764524, 0.00308708893, 0.00733761396, 0.0054059918, -0.00546974177, 0.00718461396, -0.00617099041, 0.00947961, -0.0353939459, -0.000944295432, -0.0259589609, 0.0163199753, -0.0461039282, 0.00986848492, 0.0130432304, 0.0199792199, 0.0155549766, 0.000767389429, -0.0121061066, -0.00635586539, -0.0258187111, 0.00218662177, 0.0269279592, -0.0200557187, -0.00914173573, 0.0136679793, -0.0106462333, -0.0192652214, -0.0161797255, -0.00526574207, -0.018245222, -0.0101298597, -0.0166132245, 0.0318239518, -0.0022009653, 0.00482586771, -0.0287384558, -0.0297839548, 0.0115451077, -0.0293249544, 0.0167279746, 0.0230519641, -0.0222742166, -0.0334049501, 0.0253852122, -0.160343751, 0.00382818165, 0.0153892264, -0.042227935, 0.0340679474, -0.0135404794, 0.0102701094, -0.00416286848, -0.0262904596, 0.0130942296, -0.0137062287, 0.0192652214, -0.0259717107, 0.00121363881, 0.00777111296, 0.0131197302, -0.012947605, 0.0189974718, 0.00453899289, -0.00249899621, 0.0227204654, -0.0215984676, 0.000143736106, -0.0132727297, 0.00581080373, 0.0108566089, -0.0118001066, 0.0215602163, 0.00366243185, -0.0210884679, -0.0163327251, -0.00993861, 0.0155804763, 0.000129492, 0.0187934712, 0.00406724401, -0.00610724092, -0.00804523751, -0.00417561876, 0.0294269547, 0.0399839394, 0.0275909584, 0.00768186338, 0.000111163892, -0.00717186416, 0.00973461, 0.0311099533, 0.0143692279, 0.00537730427, -0.021572968, 0.000463382108, -0.0344249457, 0.00960073527, -0.0198644698, 0.0233962145, 0.0249517113, 0.00713998917, -0.00386961899, -0.0154529763, -0.00782211311, -0.0457214303, -0.023115715, 0.00938398577, -0.000474139903, -0.014305478, -0.00407361891, 0.00297552673, 0.00729936408, 0.00019124971, 0.00245437119, -0.0197879691, -0.0211139675, 0.0112518575, -0.0182197224, -0.00243524625, 0.008013363, 0.00314924517, -0.0152999768, 0.0119849816, -0.0099577345, -0.0203107186, 0.0415394381, 0.00459636794, -0.0171232242, 0.0289424565, -0.000348433066, -0.00939036068, -0.008013363, -0.015848225, 0.00979836, -0.0116726076, -0.0338639468, -0.0185129717, -0.00258027739, -0.00327993254, 0.00968361, 0.01306873, -0.00318908878, 0.0198134705, -0.00509680482, -0.00697423937, 0.0121889813, 0.000250616809, 0.00213243417, 0.0138337286, 0.0365924425, 0.00468561798, 0.00296596414, 0.0154147269, 0.00656624, 0.000337276841, 0.0103976093, 0.0217642169, 0.0112709831, -0.00737586385, 0.00884211157, 0.000929951726, -0.00320183882, 0.0194437206, 0.0028145581, 0.036362946, -0.0226694662, -0.0188572221, 0.00222327793, -0.0173144732, -0.00980473496, -0.08037588, -0.00919911079, -0.00269821472, 0.0147899771, 0.0067511145, 0.0116279824, -0.021394467, 0.0028018083, -0.0170977246, 0.0254107118, -0.0175312236, -0.0263669603, -0.0050234925, -0.00783486292, 0.0137062287, 0.0092883613, -0.0149429776, -0.0369749442, -0.0169957243, 0.0217897166, -0.00550799165, 0.000106482257, 0.0206677187, -0.0166769754, -0.0336344503, 0.0220319666, -0.023115715, 0.00178499729, 0.016460225, -0.0186404716, 0.00256912108, -0.0239572134, 0.00766911311, -0.0288149565, -0.00137859164, -0.00806436315, -0.00991948508, 0.00450393045, 0.0312374532, -0.0304214545, 0.00432224339, 0.00282571441, 0.0210757181, 0.0173782241, 0.0134512298, -0.00480355509, -0.012883855, 0.0234599635, 0.0236384645, -0.0159884747, -0.0267749596, -0.0261629596, -0.0203489698, -0.0444464311, 0.0238169637, -0.0177352224, 0.0263669603, -0.0275399573, -0.0311609525, 0.0129221054, 0.000639491191, -0.0179774724, -0.0176842231, 0.0178627223, 0.016090475, -0.0309824534, -0.0174802225, -0.00342018227, 0.00747786369, 0.0175184738, -0.0311354529, 0.0162817258, -0.0108438581, -0.000390468165, -0.0389894396, -0.0184492227, -0.0291209556, -0.0146879777, 0.0229244642, -0.0133874798, -0.0215984676, -0.0246967115, -0.000635108387, -0.0229372159, -0.00453261798, 0.0308804531, 0.00329268258, -0.000878951803, 0.00458043069, -0.00979836, -0.00710173929, 0.00790498778, 0.0201194696, -0.00607536593, -0.00414374378, -0.0109394835, -0.00194277824, 0.0109904837, 0.00930748601, 0.0356744453, -0.0277439579, -0.0140504781, -0.0740008876, 0.0204892196, 0.0155804763, -0.00938398577, 0.00256434, 0.0166514739, 0.0285854563, -6.1807521e-05, -0.000939514197, -0.000860623666, -0.0139994789, 0.022503715, -0.0121762315, 0.00317155756, -0.0246967115, -0.0218024664, 0.00193640334, 0.014305478, -0.0228352156, 0.00987486, -0.0135787297, -0.00960073527, -0.00140568533, 0.00142002909, -0.0145094777, -0.0161797255, 0.0129093556, 0.0132854795, -0.015784476, 0.000553030404, 0.0137827294, -0.0150322272, 0.0139612285, 0.010110735, -0.00977286, -0.0146369776, -0.0262904596, 0.015044977, 0.0146752279, 0.0164219756, -0.00390468165, -0.0320279524, 0.0117363567, -0.00439236825, -0.0176077224, 0.0113666076, -0.0249389615, 0.00100007665, 0.00493743, 0.0276929568, 0.00650886493, 0.0016750287, -0.0245437119, -0.00181209098, 0.00441468088, -0.00812173728, 0.0207824688, 0.00947961, -0.00807711296, -0.0245819632, 0.0409529358, -0.00557492906, 0.00821736269, 0.000754241, 0.0193034708, 0.0097537348, -0.00249740249, 0.0114494823, 0.0175439734, -0.0288659558, -0.0223124661, 0.0127244806, 0.0251429621, 0.0231412146, -0.00468243053, -0.00121842, 0.0223252159, 0.00715273898, -0.0029133705, 0.0100406101, 0.0211649686, 0.00307433913, -0.0538559183, 0.0242122132, 0.00770098809, 0.032741949, -0.0102254841, 0.0148409773, 6.74354451e-05, 0.0140759787, 0.00786673836, 0.014305478, 0.01337473, 0.014177978, -0.00827473775, -0.00637180265, -0.0325889513, -0.00268387096, 0.020897219, -0.00179934106, -0.00464418065, -0.012144356, -0.0145987282, -0.0195712205, -0.0084596118, 0.00256593362, 0.00203521573, -0.0333029479, 0.0135532292, 0.00944136083, 0.025461711, 0.0206422191, -0.0245819632, -0.00320024509, -0.0376634412, -0.000196728215, 0.00419155601, -0.00216430915, -0.0258824602, 0.0126734804, -0.00300262053, 0.0164984744, 0.0412844382, -0.00696786446, 0.0221722163, 0.00697423937, 0.0357764438, -0.033787448, 0.0205529686, -0.00150051329, 0.00978561, 0.00789861288, 0.00180571596, 0.00746511342, -0.01337473, 0.00178340357, -0.00232209032, 0.0161924753, -0.0108056087, 0.0573749132, 0.0132599799, -0.00544742914, 0.0142034786, -0.017199723, -0.0303449538, -0.00172921608, 0.010850233, -0.046409931, -0.0137062287, 0.0321299508, 0.0142927282, 0.016702475, -0.0108247334, -0.0418454371, 0.0107801082, 0.000737108232, 0.00359549443, -0.00790498778, 0.00479080528, 0.0155039765, 0.00797511265, 0.00354130706, -0.00828748755, 0.00862536207, -0.00979198515, 0.0355214477, 0.0140887285, -0.025397962, -0.0525299199, -0.0171104744, -0.0200557187, -0.0168172251, 0.00370068196, 0.0246839616, 0.00443380559, 0.011098858, -0.0148282275, -0.0103147347, 0.0333029479, -0.0236257147, 0.0321299508, -0.0199409705, -0.0260354597, 0.00523067964, 0.0208079685, -0.00128695113, -0.00499161752, -0.0355979465\], metadata={'director': 'Christopher Nolan', 'theme': 'Fiction', 'year': 2010}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, hash='7937eb153ccc78a3329560f37d90466ba748874df6b0303b3b8dd3c732aa7688', text='Inception', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.317687511),
 NodeWithScore(node=TextNode(id\_='6b7bdb44-9dc2-48f6-b9cb-05dcaea4889b', embedding=\[0.0131883333, -0.0137667693, -0.0396421254, -0.00729471678, -0.0107653309, 0.0171731133, -0.0282276608, -0.0507480912, -0.0210422054, -0.01610622, 0.0254768785, 0.0143452045, 0.0170060098, 0.00128059229, -0.0103797065, -0.000858012936, 0.0219162852, -0.0112602143, 0.015424951, -0.0149622029, -0.0174430497, -0.00926139764, -0.00690909289, 0.0097370008, -0.0101161972, -0.00156177639, 0.0225204285, -0.0414159931, 0.0201038532, 0.00370198837, 0.00786672533, -0.00535053, -0.0264537912, -0.0238444041, -0.0343205184, 0.00850300491, -0.0269165393, -0.00934494939, 0.00577793, -0.0037951807, 0.0304385703, 0.0138181858, -0.0188184399, -0.0150521817, -0.0169160292, -0.0138567481, 0.011915775, -0.0171988215, -0.0302843209, 0.00484921923, 0.017700132, 0.0325209387, -0.0286389925, -0.023600176, -0.00468532881, 0.000876490725, -0.00141154369, 0.00646241195, 0.00751323672, -0.016556114, -0.0100455, -0.00316372188, -0.00587112224, -0.015090744, -0.00502275, -0.0114980163, -0.0207337048, -0.00732042501, -0.00301911286, -0.0234973431, 0.0178672355, 0.014525163, 0.0153735345, -0.0133297285, 0.0100390725, -0.00729471678, -0.020643726, -0.00382731599, -0.00339991646, -0.0126548875, 0.0267622899, -0.00226714648, -0.00968558434, 0.0245899428, 0.0247184839, 0.014409475, -0.0071918834, 0.0187798776, -0.00759036141, -0.00408761203, -0.0152321393, 0.0355288051, 0.00103475712, 0.0115558598, -0.0135482494, 0.0139210187, -0.00108697708, 0.0325466469, 0.0180729013, -0.0106882062, 0.0216977652, -0.0027009733, -0.0151935769, -0.0255025867, -0.0367885083, -0.00529268663, 0.0089978883, -0.00420329906, 0.0172759462, -0.00715332106, -0.0153349722, 0.0111123919, 0.0243714228, -0.0267622899, 0.00829091109, -0.0154378051, -0.0109002991, -0.0118772127, -0.0208879542, -0.0276363716, 0.0173273627, 0.0276106633, 0.0209650788, -0.0106432168, 0.0313383602, 0.00315890159, -0.0152964098, 0.00492313039, -0.00266241096, -0.0123206796, 0.0235359054, 0.00965987612, 0.0130019486, -0.00671628071, -0.0318268165, 0.0417759083, -0.0188184399, 0.00364093133, -0.0238572583, -0.0126484605, 0.0232274067, 0.0223019086, -0.0299758222, 0.0173916332, -0.0101226242, 0.0102640195, 0.0101933219, 0.00359272817, 0.0108231744, -0.0167489257, 0.0173145086, -0.00805311, 0.0105403839, 0.0277649127, 0.0185356494, 0.00911357533, 0.00782173593, 0.0113951825, -0.0289474912, -0.0185613576, 0.018034339, 0.0247827545, 0.0159776788, -0.000874080579, 0.0135482494, 0.0198082086, 0.0357858874, 0.0114915883, 0.0107589038, -0.0123463878, -0.0160162412, 0.00124444009, -0.0238186959, 0.00484279217, 0.000368953595, 0.0064109955, 0.0186898988, 0.0130019486, -0.0270964988, -0.00176904909, 0.000858816318, 0.0121600032, 0.0260167513, 0.047431726, -0.00881150365, -0.00815594289, 0.0116586927, -0.00481065689, 0.020528039, -0.0014203809, 0.0143837668, 0.038022507, 0.00139467267, 0.0146279959, -0.665535212, -0.0407475792, -0.014756537, -0.0108296014, -0.0112087978, 0.00891433656, 0.0050934474, 0.0279962867, -0.00877294131, -0.0142423715, -0.0123335337, -0.00651704194, 0.027122207, -0.00235873205, -0.025309775, -0.000651141803, -0.0226361156, -0.0042900648, -0.000323361601, 0.00583577342, 0.0126356063, 0.0197567921, -0.0282276608, -0.0268137064, 0.000913446362, 0.0175201744, 0.00810452644, -0.016903175, 0.021672057, 0.018265713, 0.0100840619, 0.02155637, 0.0101033431, 0.0297701564, 0.0298215728, 0.0252197962, -0.022237638, 0.0208236836, 0.00451822532, 0.0413131602, -0.0252455045, -0.00190562417, 0.00193454593, 0.0103797065, -0.0101740407, -0.00384338363, 0.0303614456, -0.0105082486, 0.00179636409, 0.00249852077, 0.020091, -0.0255540032, 0.00708905049, 0.0215820782, 0.0138696022, 0.0183171295, 0.0377911292, 0.00726900855, 0.00831019226, 0.00956347, -0.0102961548, 0.0117550986, -0.012474929, 0.00986554194, -0.00164693489, -0.000925497094, -0.0225075744, 0.00533124898, 0.00472067762, -0.038253881, 0.02133785, 0.0158619918, -0.0123785231, -0.00331957801, 0.00288414466, -0.0208365377, 0.0347575583, -0.00876651425, 0.007146894, 0.00998122897, 0.0040843985, -0.00134968327, -0.0162990317, -0.0207979754, 0.038356714, -0.00187348889, -0.0323923975, 0.00889505539, 0.0134839779, 0.0191012323, 0.00175458821, -0.00845801458, -0.0140367057, 0.0166075304, -0.0146537041, -0.00573294, -0.0013842287, 0.00528947311, 0.00947991759, -0.0131240627, 0.0154506592, 0.00436718948, -0.0161833446, -0.0274821222, -0.0012307826, 0.0171088427, 0.00684482232, 0.00656203134, 0.0423672, -0.0115237245, 0.0364285931, -0.0207079966, -0.0043800436, 0.00134325621, 0.00287611084, -0.0229317602, 0.0297444481, 0.00959560554, 0.00289539201, -0.0146537041, 0.0137539152, 0.010778185, -0.00148143806, -0.0042193667, 0.00257725222, -0.00229606824, -0.00807881821, -0.00213057152, -0.0117293904, 0.00113759015, 0.0294873659, 0.00742968498, 0.0266080406, -0.00710833166, -0.00652989605, -0.0066584372, 0.0319296494, -0.00525091076, 0.026209563, -0.0148722241, -0.0182142965, -0.00612499099, -0.0284333266, 0.00551763363, -0.00988482311, -0.0483058058, -0.0141266845, 0.00208076159, -0.00190401741, -0.00532160839, -0.0339348912, -0.00960846, -0.0342691019, -0.0104054147, -0.0125392005, -0.0189984, 0.00553048775, -0.000976913609, -0.0159776788, -0.00729471678, 0.0125263464, 0.0123913772, -0.00960846, -0.00882435776, 0.0147436829, -0.000602135493, -0.0110481214, 0.0172245298, -0.00804025587, -0.0282019526, -0.00996837486, 0.00152080378, -0.00294841523, 0.010662498, -0.00389480032, 0.0179829225, -0.00437683, 0.0121792844, 0.00829091109, -0.0165432598, 0.0070119258, -0.0208622459, -0.0155149307, 0.000502114301, 0.0408761203, -0.00473353174, 0.026428083, -0.00245353137, 0.0106753521, 0.007146894, -0.00747467438, 0.0243971311, 0.0238444041, -0.0077960277, -0.0108038932, 0.0173402168, -0.00198435574, -0.00586790871, -0.003573447, 0.0423929095, 0.0229446143, -0.00850300491, 0.0211707465, -0.032109607, 0.0117358174, -0.0355802216, 0.0198853333, -0.0224818662, 0.00599323632, 0.00898503419, 0.00283915503, -0.0118579315, -0.0195511263, -0.0208108295, 0.00616034, 0.024949858, -0.0231374279, 0.000281786546, -0.0352974311, -0.00435112184, 0.00398477912, 0.00443788711, 0.020528039, 0.00664558308, -0.00304803462, 0.0183042753, -0.0030400008, -0.00253386959, 0.0305928197, -0.0254640244, -0.00465640705, 0.000375179807, -0.00727543561, 0.011343766, -0.00429327833, 0.00844516, 0.0265052076, -0.0385366715, 0.0331122279, -0.00616998039, -0.00948634464, 0.00853514, 0.0133682908, -0.0208108295, 0.0103090089, -0.0229446143, 0.0143066421, -0.00856727548, -0.0135482494, 0.0192040652, -0.00551442, -0.00536338426, -0.0205151848, -0.00414866908, 0.0212350171, -0.00292110024, 0.0208879542, -0.000678055163, -0.00563974772, 0.0321353152, 0.00141797075, 0.00816879701, 0.00325852097, 0.0168131962, 0.0103411442, 0.010212603, -0.00547907129, 0.0146022877, -0.0201552697, -0.0139724351, -0.0164918434, -0.02133785, 0.00630173553, -0.0103861336, 0.00610571, 0.000804989657, 0.000960042526, 0.0129505321, 0.00260135368, 0.0144737456, -0.00465640705, -0.0208108295, 0.00167907018, -0.00432541361, -0.00755822612, -0.0226746779, -0.00331315096, 0.00516735855, 0.00805311, -0.00365378545, 0.0203223731, 0.0150264734, 0.0182914212, -0.0134711238, -0.00353488466, -0.0207079966, 0.0239086747, -0.032443814, -0.0138953105, -0.00793742295, -0.0326237716, -0.0246027969, -0.0104889665, -0.021903431, 0.0430870317, -0.0167360716, -0.0113887554, -0.0134582696, 0.0288446583, 0.00664558308, 0.0173530709, -0.000582452572, -0.0168517586, -0.00563332066, -0.00612820452, 0.0156049095, 0.00122917583, 0.00558833126, 0.0242043193, -0.0043125595, 0.0170959886, -0.0316982754, -0.0255154409, 0.0283819102, 0.0949148685, 0.00521234795, -0.00745539321, 0.0154378051, 0.0125777628, -0.0005362581, -0.0291274507, -0.00714046694, 0.0114465989, -0.0202966649, 0.0172116756, 0.000426998, 0.0164147187, 0.0190626699, -0.00791171473, -0.0119479103, 0.00747467438, -0.0158748459, -0.0111702355, -0.0142809339, -0.0233430937, 0.00143725204, 0.0161576364, 0.0080659641, -0.0123142526, -0.0400277488, 0.00185420772, 0.0181628801, 0.00147340423, -0.0115430057, -0.0051384368, -0.0215306617, -0.0140881222, -0.00259010633, 0.00621175626, 0.0182785671, 0.0356573462, 0.0198853333, 0.0101933219, -0.014409475, 0.0146279959, -0.00538266543, 0.0224433038, -0.00260456721, 0.0198981874, -0.0137539152, -0.0123849502, 0.024731338, 0.0320581906, 0.00535374368, 0.0054694307, 0.0134454155, -0.013046938, 0.0125070652, 0.0166075304, 0.0130083757, 0.007146894, 0.00455357414, -0.0123013984, -0.000179154376, -0.00136976782, -0.0278934538, -0.00565260183, 0.00860583782, -0.0303614456, -0.029615907, -0.0054919254, -0.0129955215, -0.00407154439, 0.0173530709, -0.00318943, -0.0193711687, -0.001886343, -0.00793742295, 0.0107460497, -0.00245835166, 0.0236258842, 0.00462748529, 0.0163633022, 0.0248084627, -0.0169545915, -0.0414159931, -0.00318139629, -0.0385109633, 0.00558511773, 0.0192040652, -0.0127577204, 0.0101097701, -0.0214792453, 0.00729471678, 0.0186384823, 0.00467890175, 0.0122114196, -0.0212992877, 0.010662498, -0.00014149581, 0.00500989566, 0.0118643586, 0.00979484431, -0.00675484352, -0.00159953535, -0.00930638704, 0.00682554115, -0.00965344906, 0.0268394146, 0.0153992428, 0.00505167153, 0.0457606874, -0.0207979754, -0.00937065762, 0.0228931978, -0.0123335337, 0.027353581, -0.00941564701, -0.00238444051, 0.0316211507, -0.0138567481, 0.00834232755, 0.0198082086, -0.0348089747, -0.00693480112, -0.0340634361, 0.0217748899, 0.0263509583, -0.0044925171, 0.0265052076, -0.00140350987, -0.0174559038, 0.00254351017, 0.00418401789, -0.0343719348, 0.0478687659, 0.0025692184, -0.00256761163, -0.0233302396, -0.0048010163, -0.0199881662, -0.0172759462, 0.00532803545, -0.00973057374, -0.0247184839, 0.000261300273, 0.00270258, -0.0222890545, -0.0200652909, -0.0211450383, 0.00808524527, -0.0164404269, -0.0181243178, -0.00339991646, 0.00209040218, 0.000144508493, -0.00970486552, 0.00364414486, 0.00993624, -0.0256182738, -0.0154892216, -0.0129826674, -0.00166942959, 0.0184328165, 0.0345776, 0.00946063641, 0.00746182026, 0.00354452524, -0.00267526507, 0.00441539241, 0.0268394146, 0.0124106584, -0.0143709127, 0.0221348051, 0.023715863, -0.000923086947, 0.0312355272, -0.00128219905, 0.0344490595, 0.0179700684, 0.00159792858, 0.0265823323, 0.00334528624, -0.0140109975, -0.0198467709, 0.00373733719, -0.00659416663, 0.017031718, -0.038356714, -0.0183814, 0.000772452622, -0.0198082086, 0.00227357354, -0.0146922665, 0.0303871538, -0.0219677016, -0.00233784411, -0.0121600032, 0.0186898988, -0.0319553576, 0.0182142965, -0.0265052076, -0.00760321552, 0.00499382801, 0.0301557798, 0.0123528149, 0.0164918434, 0.00487171393, 0.0305671114, 0.0192554817, 0.00616355333, 0.00967915729, 0.0276363716, -0.00832947344, -0.00424507493, -0.0242043193, 0.00643349, -0.0122628361, -0.0109195802, 0.00479780277, -0.00577793, 0.0260296054, -0.0239858, -0.000108356267, 0.0135482494, -0.021903431, 0.0288189501, 0.0109967049, 0.00739112264, 0.0108681638, -0.00118257955, -0.0160676576, 0.0342433937, 0.00742968498, -0.00989767723, 0.0144994548, 0.0204252061, 0.00739112264, -0.0190112535, -0.0133297285, -0.00711475872, -0.0397192501, -0.0153735345, 0.0099169584, 0.0208365377, -0.00510951504, -0.00628888141, -0.00825877581, -0.0180214848, 0.0134325614, -0.0250269845, -0.00501310918, -0.0253869, -0.0198210627, -0.00232820353, 0.00107974664, -0.00232338323, -0.00546621718, -0.0151164522, -0.0148336617, 0.0205537472, -0.0187670235, -0.00258367928, -0.00648812, -0.0232016984, 0.026659457, -0.00964059494, 0.00179636409, 0.0288446583, -0.00548871187, -0.00288896495, 0.00476888102, -0.0148208076, 0.0219419934, -0.0119543374, 0.00100342522, 0.00168549723, 0.0191655029, -0.00370841543, 0.015424951, -0.00563010713, -0.0279705785, 0.00483315159, -0.0154763674, 0.00212414446, 0.0103861336, -0.0182271507, 0.000870063668, -0.0136896446, -0.0211450383, 0.00460177707, -0.00920998119, 0.000132658592, -0.0455550216, -0.0206694342, -0.030181488, -0.0246027969, 0.0134968329, -0.016003387, 0.00178833026, 0.0204380602, 0.0594374798, -0.00758393435, -0.0133682908, -0.00718545634, -0.00274435594, -0.00150875305, -0.00141636399, 0.00392693561, -0.0179572143, 0.0144994548, -0.0112087978, -0.0103925606, 0.00717260223, 0.00511272857, -0.00369234779, 0.00412296085, -0.00594824692, -0.0096920114, 0.0080659641, 0.00834875461, 0.0178415272, 0.00299983169, 0.00694122817, 0.00965344906, 0.00704406109, 0.0213635582, -0.0150007652, 0.0102254571, 0.0172116756, -0.0156948883, -0.00449573062, -0.0456835628, -0.00805311, -0.0254511703, 0.0363257602, -0.0281505361, -0.0128669804, -0.0264795, -0.010321863, -5.48810931e-05, -0.00144608924, 0.00710833166, -0.0227646567, -0.00158507447, 0.0369427577, 0.0145765794, 0.0066584372, -0.0137024987, -0.0105789462, -0.0212350171, -0.0209907889, -0.0338577665, -0.0221605133, -0.00129424979, 0.0385366715, 0.00643991726, 0.0115494328, -0.019294044, -0.00957632437, -0.00845158752, -0.0204252061, -0.0228803437, 0.0121021597, 0.0353488475, 0.0108296014, 0.0206051636, 0.00549835246, -0.00993624, -0.0162476152, -0.00404262263, 0.0128091369, 0.00787957944, 0.0129955215, 0.0438839868, 0.0204380602, 0.00742968498, -0.0197182298, 0.00706976932, 0.00976270903, -0.0120507432, 0.00304321432, 0.00144689262, 0.0016421146, 0.00204541278, 0.000219524372, 0.000348668167, -0.000840338471, 0.00680626, -0.0319296494, -0.0132011874, -0.0129441051, -0.0126934499, -0.0072433, 0.0150393276, 0.00530232722, -0.00913928356, 0.0253226291, -0.010553238, 0.00166139577, -0.00747467438, 0.00610249629, 0.0280991197, -0.0182014424, 0.00104600447, -0.00189277006, -0.0062535326, -0.00428363774, -0.00218841503, 0.00487171393, -0.0265309159, -0.0213249959, -0.0189341269, -0.0182528589, 0.00250816136, -0.0186256282, -0.00217877445, -0.0131176356, -0.00461141765, -0.015772013, -0.00699907169, -0.0291274507, 0.0316468589, 0.019859625, -0.0106175086, 0.00340634352, -0.0261967089, -0.017250238, 0.0161833446, -0.0399249159, -0.00575543521, 0.00587112224, -0.025643982, -0.00116651191, -0.0177258402, 0.00329386978, -0.0100776348, 0.00404262263, 0.0016967447, 0.0138953105, 0.219856977, -0.00185420772, 0.00248084636, 0.0219677016, 0.00360236876, 0.0197953545, 0.028921783, -0.0156177636, -0.0293588247, 0.0079309959, -0.0225589909, 0.0270964988, -0.000545095303, 0.00126131112, -0.00876651425, -0.0097370008, -0.0344490595, -0.0232402608, -0.0286647, -0.0332407691, -0.0101161972, -0.0194997098, -0.0253611915, -0.033909183, 0.0116394116, 0.00529268663, -0.0155920554, -0.0141266845, 0.0467376038, 0.00424828893, 0.00491991686, -0.000484038173, -0.00226553972, 0.00251780194, -0.0187670235, -0.00676769763, 0.0170188639, -0.000114984177, 0.00711475872, 0.0130790733, -0.0223147627, 0.0131240627, -0.0244614016, -6.42204177e-05, -0.00727543561, 0.0157848671, -0.0148850782, -0.00925497059, -0.00473353174, 0.0275335386, -0.0259010643, -0.0175973, 0.0468147285, 0.0399763323, -0.0251169633, 0.0109195802, 0.0223019086, 0.00984626077, -0.011806515, -0.0214149747, -0.0019634678, 0.0280991197, -0.0196925215, -0.0119222021, 0.0113951825, 0.0302843209, -0.016453281, -0.0104118418, 0.0127255851, -0.0224947203, 0.00906215888, 0.00366663956, -0.0161704905, 0.00308981049, -0.0219162852, -0.0282790773, 0.0111316731, 0.0047496, -0.00509987446, 0.0269936658, -0.0044025383, 0.00902359653, 0.00276363711, 0.0140881222, -0.0175715908, -0.0464291051, 0.0106303627, -0.017584445, 0.00180279114, -0.00135450356, 0.00721116457, 0.000410729495, 0.00646241195, -0.00776389241, 0.0218391605, 0.0135353953, 0.00431577303, 0.0362229273, -0.00642384961, 0.0107460497, -0.0152707016, -0.000495285552, -0.000503319374, -0.00280541298, -0.0159005541, 0.00856727548, -0.00941564701, 0.0232402608, 0.0216463488, -0.00217877445, 0.0306956526, -0.00304160756, -0.00491670333, 0.00912000239, -0.00313801365, 0.0136896446, -0.0260681678, -0.0166975092, -0.0134454155, -0.0271993317, -0.0132011874, -0.00843230635, 0.00326334126, 0.0118193692, -0.00510630151, 0.00609928276, 0.00418401789, 0.00241978932, -0.00291628, -0.0330608115, 0.0126420334, -0.00825234875, 0.0192040652, -0.00950562675, 0.0179700684, 0.0173145086, 0.0189212728, 0.00743611204, -0.00867653545, -0.00908144, 0.00222215708, -0.0279191621, -0.00118579308, 0.0275849551, 0.000910232833, -0.0142295174, 0.00965344906, -0.0167232174, -0.0106432168, -0.0325466469, -0.0178029649, -0.00869581662, -0.00578435697, -0.0226232614, 0.0190112535, -0.0134068532, -0.0298986975, -0.0193968769, -0.00823949464, 0.0127255851, -0.023034595, 0.020643726, 0.00883078482, 0.00104359433, -0.0110738296, 0.0160290953, -0.163607314, 0.00861226488, 0.0225461368, -0.0177772567, 0.0288960747, -0.0223790333, 0.0280991197, -0.00896575302, -0.00254190341, 0.0132011874, 0.00111991575, 0.00746182026, -0.0264537912, 0.00306731579, -0.0103539983, 0.0188184399, -0.011800088, 0.00708905049, 0.0244485475, 0.00998765603, 0.0251812339, -0.0171474051, 0.00106126873, 0.00630173553, 0.0295130741, 0.0027009733, 0.00170156499, 0.0113887554, 0.00422900729, -0.012821991, -0.00902359653, 0.00674198894, -0.00809809938, -0.00984626077, 0.0244614016, -0.00623103743, 0.00101868948, 0.024731338, 0.0095570432, 0.031878233, 0.0413645767, 0.0153606804, 0.0413645767, -0.00484921923, -0.0175973, 0.0173016544, 0.0277906209, 0.012031462, 0.00559154479, -0.0214921, -0.00611856394, -0.00551120657, 0.0177129861, -0.0191140864, 0.0151935769, 0.0164018646, 0.00024141655, 0.0066584372, -0.00116570853, 0.0014525163, -0.0200267285, -0.020309519, 0.0173273627, 0.00955061615, -0.0114465989, 0.00531839486, 0.0127191581, 0.0112216519, -0.0278420374, 0.00919712707, -0.0356059298, -0.0352203064, 0.00992338546, -0.0110288402, -0.0103154359, -0.00122194539, -0.0109517155, -0.00924854353, -0.000695327879, 0.00301589933, -0.0232531149, 0.0224304497, 0.00542765483, -0.00708262343, 0.0296673235, 0.0070569152, -0.00769319432, -0.0102640195, -0.0298986975, -0.00517378561, 0.0197310839, -0.0266851652, -0.0361458026, -0.014756537, 0.0331636444, 0.00894647185, 0.0161833446, 0.00454714708, 0.0244742557, -0.0167360716, 0.0043800436, 0.0144994548, -0.00839374401, -0.0161576364, 0.0208493918, 0.00910072122, -0.00599323632, -0.0070119258, 0.0241529029, 0.027122207, -0.0186898988, 0.00546621718, 0.0265566241, 0.00989125, -0.00881150365, 0.00766105903, 0.0154892216, -0.0364800096, 0.0222890545, 0.01464085, 0.0474060178, 0.0040619038, -0.0195896886, 0.00900431536, 0.00252744253, 0.0047560269, -0.0730114356, -0.0278934538, -0.00616034, 0.00614105863, -0.00170638529, 0.0178929437, -0.0134711238, 0.00351239, -0.0166460928, 0.0260810219, -0.0139081646, -0.0192169193, -0.00910714827, -0.0171474051, 0.011909348, 0.00352524407, -0.0256054197, -0.0174301956, -0.030849902, 0.00655239075, 0.00266241096, 0.00946063641, 0.00465962058, -0.00617319392, -0.0206694342, 0.00159873196, -0.0267108735, 0.0166589469, 0.0216206405, 0.00266562449, 0.0113694742, -0.010893872, -0.0162347611, -0.0212992877, 0.013381145, 0.0104246959, 0.0128348451, 0.0116008492, 0.0140109975, -0.0438325703, 0.00529911369, -0.00780888181, -0.00536659779, -0.0137410611, 0.0197567921, -0.00762249669, -0.0382795893, 0.00536338426, 0.00573615357, -0.0033517133, -0.0197053757, 0.00117856264, 0.00589361694, -0.0171859674, 0.0218263064, -0.0286132842, 0.0138310399, -0.0117293904, 0.00854156725, 0.0263766665, -0.010096916, -0.025643982, -0.00425471598, 0.0200395826, 0.0126420334, 0.00373412366, 0.00547264423, -0.0137153529, 0.0257082526, -0.0254511703, -0.00323281274, 0.0121728573, -0.024499964, 0.00896575302, -0.0135996658, -0.00632423, -0.0297187399, 0.00239890139, 0.00435112184, -0.0291531589, -0.0171988215, -0.0227775108, 0.00134164945, -0.0275849551, 0.0426242836, 0.018831294, 0.0246027969, 0.0171731133, 0.02155637, -0.0165046975, 0.00596110104, 0.0154892216, 0.0230217408, -0.00867010839, -0.00432541361, 0.00898503419, -0.00545336306, 0.026659457, 0.0294102412, 0.0089528989, -0.031544026, 0.0148336617, -0.0676127, 0.0242300276, 0.0131176356, -0.0258882102, 0.0159648247, 0.00945420936, -4.66715246e-05, 0.00792456884, -0.00536981132, 0.00417116378, -0.013278312, 0.0187927317, -0.0112794954, -0.00494883861, -0.0128605533, -0.00470461, 0.00439289771, 0.0181243178, -0.0130790733, 0.00385302422, -0.0008596197, -0.00258046575, 0.0192426275, 0.0080209747, -0.0292302836, -0.0103090089, -0.0130726462, 0.0141523927, -0.0245385263, 0.00943492819, 0.00516414503, -0.0350403488, 0.0179829225, 0.0150393276, -0.0107717579, 0.00229928177, 0.00685124937, 0.00210968335, 0.00111268531, 0.0206051636, -0.0120764514, -0.0174944662, 0.024499964, -0.0177386943, 0.0055819042, 0.0285361595, -0.0295901988, 0.0149364946, 0.0162476152, 0.0201681238, 0.00211932394, 0.0308241937, -0.00043744198, 0.000492072, -0.00821378641, -0.00845158752, 0.0155020766, -0.0127320122, -0.00646241195, -0.0349118076, 0.00244871108, -0.0203223731, -0.010431123, -0.0205408931, 0.00184456713, 0.00347061409, 0.017134551, 0.00154972554, 0.0248598792, -0.00336135388, -0.0262995418, 0.0119800456, 0.00795670412, 0.0290760342, -0.0108553097, 0.000443467346, 0.0040619038, 0.0159005541, -0.0143580586, 0.00155534921, 0.0121728573, -0.00134727312, -0.0381767564, 0.0225075744, 0.0116458386, 0.0243200064, -0.0132526038, -0.0163761564, -0.00249048695, 0.0201552697, 0.00256761163, 0.00730757089, 0.0165046975, 0.0187284611, -0.00205666013, 0.00122033863, -0.0236901548, 0.0114915883, 0.00872152485, 0.00576828932, -0.000425391248, -0.012474929, -0.00389480032, -0.0259653348, -0.0357858874, -0.00248727342, -0.0236258842, -0.0301557798, 0.0115044434, -0.00328744273, 0.00471425056, 0.0259653348, -0.013162625, -0.00258207251, -0.0175201744, 0.0109517155, 0.00745539321, -0.00732685206, -0.00116169162, 0.0183042753, 0.00504524447, 0.00843230635, 0.0284847431, -0.0282019526, 0.0215435158, 0.00105644844, 0.0150650358, -0.0208879542, 0.0134839779, -0.0128991157, -0.0166203845, -0.0271479152, 0.0080209747, 0.00114401721, -0.00118257955, -0.00937708467, -0.0195382722, 0.031209819, -0.00982698, 0.0531132482, 0.00708905049, -0.00667129131, -0.0111381, -0.026428083, -0.00961488672, -0.00171120558, -0.00244710431, -0.0310812779, -0.0318011083, 0.0189469811, 0.0178929437, 0.0163247399, -0.0111959437, -0.0388965867, -0.0146279959, 0.00412296085, 0.0105918, -0.0206951424, -0.000291828823, 0.0304385703, 0.00892076362, 0.00848372281, 0.00370198837, -0.00910714827, -0.0157077424, 0.0453236476, -0.00607357454, 0.00253065606, -0.0420329943, -0.0163761564, -0.0170445722, -0.0171474051, -0.00527340546, 0.0111959437, -0.00434469478, -0.00521234795, -0.00232177647, 0.0123399608, 0.0101933219, -0.0187284611, 0.0380739234, -0.0221476592, 0.00493277097, -0.00102752668, 0.00693480112, -0.0202966649, -0.000482029718, -0.0274049975\], metadata={'author': 'J.K. Rowling', 'theme': 'Fiction', 'year': 1997}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, hash='1b24f5e9fb6f18cc893e833af8d5f28ff805a6361fc0838a3015c287510d29a3', text="Harry Potter and the Sorcerer's Stone", start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.467440248)\]

Multiple Metadata Filters with `AND` condition

In \[ \]:

Copied!

from llama\_index.core.vector\_stores import FilterOperator, FilterCondition

filters \= MetadataFilters(
    filters\=\[
        MetadataFilter(key\="theme", value\="Fiction"),
        MetadataFilter(key\="year", value\=1997, operator\=FilterOperator.GT),
    \],
    condition\=FilterCondition.AND,
)

retriever \= index.as\_retriever(filters\=filters)
retriever.retrieve("Harry Potter?")

from llama\_index.core.vector\_stores import FilterOperator, FilterCondition filters = MetadataFilters( filters=\[ MetadataFilter(key="theme", value="Fiction"), MetadataFilter(key="year", value=1997, operator=FilterOperator.GT), \], condition=FilterCondition.AND, ) retriever = index.as\_retriever(filters=filters) retriever.retrieve("Harry Potter?")

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"

Out\[ \]:

\[NodeWithScore(node=TextNode(id\_='7fed3d0b-e2d7-432a-9231-3ac02130c00f', embedding=\[0.00310940156, -0.0246712118, -0.0222742166, -0.0364649445, -0.00715911388, 0.0117236068, -0.0400604382, -0.0275654588, -0.0157589763, 0.00740136392, 0.0278459582, 0.029962454, 0.0187679715, -0.00440511806, 0.00412780605, 0.00442743069, 0.0276674572, -0.00760536361, -0.00303608901, -0.012947605, -0.00570242899, -0.01923972, 0.00208462193, 0.0092118606, 0.00205274695, -0.0128328558, 0.0136297289, -0.0292994548, 0.0149939768, -0.0193289705, 0.0219937172, -0.00944136083, -0.0221977159, -0.00928198546, -0.00940948538, -0.00429993076, -0.0119786067, -0.0272339582, 0.0158864763, -0.0080261128, 0.0143437283, 0.00407999381, -0.00648655277, -0.0170722231, 0.00394293154, -0.0149939768, -0.00831298716, -0.0212669671, -0.0228479654, 0.0105123585, 0.0167662241, 0.0527849197, -0.0421514362, -0.0262139607, -0.00156506011, -0.00443380559, -0.00724836392, 0.00597655354, 0.0354959443, -0.00842773728, -0.00259143347, -0.00748423859, -0.0113602327, 0.00446568057, 0.00110207649, -0.00814723782, -0.0293504559, -0.00159932568, -0.002620121, -0.00987486, 0.0405959375, 0.0500819236, 0.0242504627, 0.00166227866, 0.00172921608, 0.020769719, 0.0108884834, -0.0177224725, -0.0181432217, 0.0102828592, -0.00192684087, -0.01313248, -0.0168554746, 0.0307019539, 0.0214709677, 0.0193544701, -0.00752248848, 0.0236257147, 0.0111753577, -0.00342974486, 0.00284962077, 0.00194277824, 0.039830938, 0.023485465, -0.0199919697, 0.0154529763, -0.0131962299, -0.00124949811, 0.0134894792, -0.0197624695, 0.021203218, 0.0137062287, -0.0169574749, -0.0205147192, -0.00436049327, -0.0307019539, 0.0176587235, -0.00387918158, 0.0247349627, -0.0103529841, -0.0174547229, 0.0141524784, 0.0326144509, -0.015287227, -0.0133619793, 0.00142720097, 0.0320789516, -0.0129093556, 0.011219983, -0.0230137147, 0.0161542259, 0.0332009494, 0.00287193316, -0.0117682321, 0.0194564704, 0.0134257292, 0.00268227723, -0.00101840473, -0.00237309, -0.0019013409, 0.0287129562, 0.00605305331, 0.0164729748, -0.00611361582, -0.0191632211, 0.0252832118, -0.0152362268, 0.034271948, -0.0182197224, -0.0288659558, 0.017327223, 0.0317219533, -0.0138847288, 0.0215219669, 0.00148616964, 0.0190229714, 0.000236273074, 0.0140377283, 0.0296309553, 1.55763919e-05, 0.0136679793, 0.00215315307, -0.00300102658, 0.0186659712, -0.00411505625, 0.0307274535, 0.0160777252, 0.00638455292, 0.00648655277, 0.0150959771, 0.0026759021, 0.004376431, 0.0038313691, 0.00076499884, 0.0301154535, 0.0223762151, 0.0180412233, -0.00129252928, -0.0119339814, 0.0129731055, -0.00279383943, 0.00654074, -0.0249262117, 0.0291209556, -0.00252768374, 0.00199537189, 0.014241728, 0.00161526317, -0.0360569432, -0.0294269547, 0.018002972, 0.0166514739, 0.0377909429, 0.0324359499, -0.0249134619, -0.0124949813, 0.0245819632, -0.0213179681, 0.0189974718, 0.00352855702, 0.00503305485, 0.0214582179, 0.0238169637, 0.00242090249, -0.651575, -0.0190357212, 0.0048704925, -0.00865723658, 0.0117427325, 0.0166514739, 0.00119531073, 0.0226567145, -0.014547728, -0.0105697336, -0.0111052329, -0.00859348662, 0.0186914708, -0.0139102284, -0.0432989337, -0.00793686323, -0.0220829658, -0.00709536439, -0.0278714579, 0.00343611976, -0.0167789739, 0.0162434746, -0.0455939323, -0.0106079839, -0.00494380482, 0.00252927747, 0.0331244506, -0.0257294606, 0.00623155292, -0.00325124501, -0.00392380636, 0.0150577268, 0.00994498469, 0.0225419663, 0.0425594337, 0.0087719867, -0.0111817326, 0.0307784528, 0.00728661381, 0.0435794331, -0.0125651062, -0.00641961535, 0.0209992174, 0.00480355509, -0.0133109801, 0.0251302123, 0.00989398453, -0.0291464552, 0.0231284648, -0.0155167263, 0.0188317206, 0.000304405781, -0.00463780528, 0.0156442262, -0.00439236825, 0.0223762151, 0.02613746, 0.0129539799, -0.00112917018, 0.0151342265, -0.00870823674, -0.0186277218, -0.0297329538, 0.0173782241, -0.0211777184, 0.0227332152, -0.0147772273, -0.0148919774, 0.0182962213, -0.0282539576, 0.0202342197, 0.0331754498, -0.00733123859, -0.0151597271, 0.00619967794, -0.0138974786, 0.0456704311, 0.00312693277, 0.0187552217, 0.0177989732, -0.00784123782, -0.0147899771, -0.0134257292, -0.0149684772, 0.0282029565, -0.00641961535, -0.0279734582, -0.00807711296, 0.0156952254, -0.000839108077, -0.00745236361, -0.00872098655, -0.013502229, 0.000639491191, -0.00991311, 0.00435730582, 0.00927561056, 0.00872736145, 0.0203617197, -0.0186277218, 0.0113538578, -0.00815998763, -0.0027524021, -0.00493105501, -0.000635905308, 0.017135974, 0.00815361273, 0.0165877249, 0.0389129408, -0.0162944756, 0.010722734, -0.0322319493, -0.0147389779, 0.0106079839, 0.00919911079, -0.0267239586, 0.0278204568, 0.0178754721, 0.0171487238, -0.0100214845, -0.0113156075, -0.00483861752, 0.0076563633, 0.00935848616, 0.030574454, 0.00866998639, -0.0131069804, -0.00276515214, -0.0330734514, 0.00422661845, 0.0236002132, 0.0148409773, 0.0381224416, -0.0193927195, 0.000672163034, 0.0186659712, 0.00437961845, -0.0340679474, 0.014981227, -0.0377909429, -0.0340679474, 0.00441468088, -0.00339468243, -0.0119786067, -0.0122782309, -0.0456959307, -0.0199027192, 0.00363055686, 0.00792411249, 0.0147517277, -0.0216877162, 0.00978561, 0.0132599799, 0.021572968, 0.00146146654, -0.0322829522, 0.0089887362, -0.0233834647, -0.0175567232, -0.0252322108, 0.0270809587, 0.0150194773, -0.0400604382, -0.0109076081, 0.0252832118, -0.00270777708, 0.0187169723, 0.0233452152, -0.0171742234, -0.0188189708, 0.008013363, -0.0107482336, -0.00763086323, 0.00140887289, 0.0223889668, 0.0298859552, -0.0158354752, -0.00268387096, 0.0151979765, -0.022006467, 0.0105251092, -0.00608811574, -0.0218024664, -0.0142544778, 0.0248752125, 0.0138337286, 0.0420239344, 0.0274889581, -0.00262808963, 0.00637817755, -0.0112582324, 0.00303130783, 0.00754798856, -0.0215347167, 0.00180093478, 0.0280754566, 0.0172252245, 0.0121889813, 0.00180890353, 0.0209099688, 0.0366434455, -0.0160522256, -0.00279543316, -0.00701248925, 0.0213434678, 0.00352855702, 0.0235747136, -0.0288149565, 0.00874011125, -0.0285344571, 0.0116088577, -0.0122017311, -0.0227587149, -0.00744598871, 0.0111179827, 0.0340424478, -0.0236002132, 0.0103338594, -0.0301154535, -0.0121698566, -0.0130177299, -0.000304405781, 0.0101617342, 0.00903336145, -0.0106526092, -0.0045995554, -0.0228607152, 0.00581399119, 0.0175949726, -0.0402899384, -0.00288627692, 0.0334559493, -0.000845483097, 0.017505724, -0.0204254687, 0.00477168, 0.022682216, -0.0144967278, 0.0385304429, 0.0125523554, 0.00611042837, 0.0132599799, 0.0266474597, -0.0198262203, 0.0127244806, -0.0285344571, 0.0201449692, 0.00233643386, -0.0211139675, 0.0159757249, -0.0153764766, -0.0204892196, -0.0164474752, -0.00671923952, 0.0207314678, -0.00648974, -0.00344249466, -0.0201322194, 0.0180539731, 0.0387089401, -0.00412780605, -0.0156187266, 0.00747148879, 0.0135149797, 0.00484180497, -0.0230392143, -0.00119849818, -0.00277949567, -0.0200174693, -0.00214199675, -0.00164315372, -0.00346799474, 0.00958161056, 0.0107546085, 0.00835123751, 0.0112709831, 0.00632399041, 0.0174929742, 0.0177479722, 0.00944773573, -0.0178117231, -0.0092118606, 0.0112964828, -0.000124710743, 0.00257230853, -0.0060976781, -0.00112518575, 0.00165430992, -0.0106398584, 0.0130496053, -0.0177734736, 0.00953061, 0.00119929505, -0.0203744695, 0.00425211852, -0.0340679474, 0.0217897166, -0.0165494755, 0.00660449, -0.0163454749, -0.0259972103, -0.0103529841, 0.0158099756, -0.00949236, 0.0241739638, -0.00962623488, -0.00284802681, -0.0118001066, 0.013871979, -0.0100724846, 0.0260992106, 0.00933936052, -0.0136042293, -0.0231539644, 0.024416212, -0.0131962299, -0.0149684772, -0.0280754566, -0.000733123859, -0.00204318436, -0.00430949358, -0.0199792199, -0.0221977159, 0.0222359654, 0.0914938599, 0.0360569432, -0.0109777329, 0.0186532214, 0.000553030404, -0.0112454826, -0.0356999449, 0.0175567232, 0.0111116078, -0.0142672285, 0.0156314764, -0.014177978, 0.0179647226, 0.0061454908, 0.00734398887, -0.00976011, -0.0366689451, -0.00565461628, -0.00986211, -0.0170084741, -0.0375359431, -0.0103338594, 0.0229499657, 0.0273104589, 0.00178499729, -0.0478124283, 0.0345014483, -0.000409593136, -0.014177978, -0.0155804763, 0.00433180574, -0.00195074698, -0.0114176078, -0.000521952345, 0.00619330304, 0.0195457209, 0.0266984589, 0.0202087183, 0.0204254687, -0.00956248585, -0.0110159833, -0.0121698566, 0.0150194773, -0.0044879932, 0.0074906135, -0.0359549448, -0.00416286848, 0.0268259589, 0.0286109559, -0.016026726, 0.0222614668, 0.0333029479, -0.0307019539, 0.0120997317, 0.0121252313, 0.00600842852, 0.00340743223, 0.00976011, -0.0134002296, 0.0158737265, -0.0197369698, -0.0283814576, 0.00541874161, -0.0188572221, -0.0190867204, -0.0197369698, -0.00773286307, -0.00750336377, -0.0126097305, -0.00662999, -0.00561317895, -0.0203489698, -0.0283049569, -0.0133492295, 0.0206677187, -0.0204764679, 0.0101234848, -0.00441149343, 0.00349986972, 0.0102318591, -0.0168427248, -0.0273104589, -0.0113538578, -0.0182324722, -0.00424574362, 0.00684036454, -0.0126671055, -0.00795598794, -0.00330543239, 0.0043828059, 0.00100565469, -0.0226057153, 0.020960968, -0.00958798546, 0.0207187179, 0.0172507241, 0.00456768041, 0.0151342265, 0.0291719548, -0.0057693664, 0.0182324722, -0.0191632211, -0.0246712118, 0.00285918312, 0.0150194773, -0.00364649436, 0.00127659179, 0.0320024528, -0.0169574749, 0.00141923223, 0.015784476, 0.00629211543, 0.00872736145, -0.0207824688, -0.00276515214, 0.0309059527, -0.0136934789, 0.0221212171, -0.00494699227, -0.00438599335, 0.00507130474, 0.00595105346, 0.00404174393, 0.0196349695, 0.00284802681, 0.00736311357, 0.0226694662, 0.00342018227, 0.0114813577, 0.0344759487, -0.03292045, 0.0217387173, -0.0119148567, -0.0217514671, -0.0262394603, -0.0215219669, -0.0144712282, 0.00184077839, -0.0189082213, -0.0161032248, -0.0149047272, 0.00319387019, 0.00673199, -0.0224272162, 0.00416605594, -0.0175312236, 0.0166259743, -0.00478124293, -0.0287639555, 0.0186404716, -0.000409593136, 0.00979198515, -0.0206549689, -0.0111116078, 0.00998323504, -0.0555389151, -0.0315944515, -0.012635231, 0.0199792199, 0.0217769668, 0.0261629596, 0.00421386864, 0.0213562176, 0.00668098964, 0.0114749828, 0.0194947198, 0.0109394835, 0.00820461288, -0.0196604691, 0.0161797255, 0.00161207572, -0.0153892264, 0.0204509683, 0.00580761628, 0.0201832186, 0.00758623844, -0.00909711141, 0.0155167263, -0.00188699714, 0.0172124729, -0.0266474597, -0.00180571596, -0.0118893571, -0.0219937172, -0.0216749664, -0.00678936485, -0.000194835637, 0.00770098809, 0.00994498469, -0.0224782154, 0.0363884456, -0.0192014705, 0.0147134773, -0.00682123937, 0.00904611126, -0.00330224494, -0.00842773728, -0.0199537203, 0.0172379743, 0.0123674814, 0.00414374378, 0.0135277295, 0.00713998917, -1.64977773e-05, -0.00359549443, 0.0401114374, -0.00290221442, 0.0211139675, 0.00514780451, -0.000441069627, -0.00517649204, -0.0219937172, -0.0247732121, -0.0268004593, -0.00753523828, 0.0119531071, -0.0121571068, 0.0227587149, 0.000832733116, -0.0200684685, 0.0124184815, -0.0176969729, 0.0300389547, 0.0147517277, 0.0200047195, 0.00207824679, -0.0095242355, -0.0209992174, 0.0251047108, -0.00526574207, -0.00757348863, 0.0141142281, -0.000571756915, 0.00885486137, -0.0168682244, -0.0339914486, -2.20634429e-05, -0.030574454, -0.0202724691, 0.011653482, 0.0153254764, 0.0272084586, -0.012514106, -0.0294269547, -0.00581717864, 0.0279734582, -0.00828111265, -0.0092118606, -0.0189209711, -0.0163709745, -0.00287671434, -0.0150959771, -0.0259589609, 0.0239062142, -0.00864448678, -0.0244544633, 0.0217132177, -0.0194564704, 0.0033723698, 0.0085424874, -0.0157462265, 0.027182959, -0.000542272639, -0.00660449, 0.0440639332, 0.00470474269, -0.00866361149, -0.0151979765, -0.00210374687, 0.0241357125, -0.00737586385, -0.00282890187, -0.0226439647, 0.00282890187, 0.0153892264, 0.0095242355, -0.00895686168, -0.0300899539, -0.00407999381, -0.00869548693, -0.00352536957, -0.00722286385, 0.0174419731, -0.0147134773, -0.00250218366, -0.012016857, -0.0125842309, -0.0059988657, 0.0149557274, -0.0425594337, -0.00617736578, -0.022503715, -0.0100151096, 0.0204382185, -0.0262139607, 0.0023555588, 0.0110032335, 0.0319769494, -0.0156697258, -0.0186659712, -0.0089887362, -0.00308868289, 0.00828748755, 0.00558130397, 0.00385686918, -0.00282412069, 0.0276419576, -0.00897598639, 0.00959436, 0.0196604691, -0.00394611899, 0.00308230775, -0.00324965129, -0.0224144664, -0.0106908586, 0.016026726, -0.0142034786, 0.0100661097, -0.0434009321, -0.00367836934, -0.0325379521, 0.00771373836, 0.0167534743, -0.000457007118, 0.00180730969, 0.0121124815, -0.00100246724, 0.0172634739, -0.0385049395, -0.00703161443, 0.000191847357, 0.0260099601, -0.00822373759, -0.00652799, -0.00789223798, -0.00089329551, -0.014305478, 0.00821736269, -0.0158737265, -0.0115833571, -0.00238105888, 0.0155422259, 0.00782848801, 0.0261629596, -0.0113666076, -0.0228352156, -0.0106271086, -0.021572968, -0.0246839616, -0.00742686354, -0.00859348662, 0.0562529154, 0.00569605362, 0.00518924231, -0.00856798701, -0.0158992261, 0.00338193239, -0.0187679715, -0.0200812202, 0.0280754566, 0.00408318127, 0.0168172251, -0.00800061319, 0.00844686199, -0.0122399814, 0.00731848879, -0.0042712437, 0.0178499725, 0.0225674659, -0.00189655961, 0.0169829745, 0.0148919774, -0.0180157218, -0.0140887285, 0.00970911048, 0.00552074146, 0.000212566083, 0.00837036222, -0.00814086292, -0.0107099833, 0.0033723698, -0.0295544546, -0.00906523596, 0.016523974, 0.00699973945, -0.0294014551, 0.00116423261, -0.00798786245, -0.00812173728, -0.00547292922, 0.00657899, -0.000409194676, 0.000534702325, 0.00583311589, -0.0139229791, -0.014177978, -0.00353811961, -0.0117363567, -0.00189655961, 0.00213562185, 0.035317447, 0.00177862227, 0.00412143115, -0.0011331545, -0.00519561721, -0.000510397658, -0.021330718, -0.0116789825, -0.00831298716, -0.0296564549, 0.00691048941, -0.00402580621, 0.0125204809, -0.0168809742, 0.00562592875, -0.00529761706, 0.0102446098, -0.0209354684, 0.00266155833, 0.0155804763, -0.0378164425, 0.0201832186, -0.017135974, -0.00218184036, 0.00410868134, -0.0244672131, 0.00194437208, 0.00276196445, -0.00252608978, 0.00300899544, -0.0203107186, 0.00905886106, -0.028483456, 0.00229021534, 0.0117554823, 0.0294524543, 0.204203695, -0.000746272271, -0.0162944756, 0.0224272162, 0.0131962299, 0.0272594579, 0.0107482336, -0.0055111791, -0.0119786067, 0.0113474829, -0.00185990345, 0.0160777252, 0.0146624772, -0.0064164279, -0.00578849111, -0.0165494755, -0.0183854718, -0.0131197302, -0.0108247334, -0.00798786245, -0.00350943208, -0.00676386477, -0.0247987118, -0.0216494668, 0.0152489766, -0.000493264874, 0.00163996627, -0.00225355895, 0.0300899539, 0.0210502185, -0.00371024432, -0.0187679715, 0.0101808598, -0.00419155601, -0.031007953, 0.0148664769, 0.00819823705, 0.00376443169, -0.0064738025, -0.00995136, -0.015478476, 0.0143692279, -0.00150131027, 0.00532630458, 0.0191504713, 0.0152107272, -0.0114112329, 0.00415330613, 0.00492786756, 0.0443699323, -0.027004458, -0.0327674486, 0.0117682321, 0.0343994461, -0.0169192236, 0.00193959079, 0.00189815334, 0.0139102284, 0.000863811176, -0.00611680327, 0.00620286539, 0.0261884592, 0.00301058916, -0.0192524698, -0.00057693664, 0.0486284271, -0.0151214767, 0.0140504781, 0.0178627223, -0.0166259743, 0.0195967201, -0.00282093324, -0.0260864608, -0.0151597271, -0.0116662318, -0.0188317206, 0.00863173697, 0.0340169482, 0.0190867204, 0.0404939391, -0.0141524784, -0.00663636485, 0.0173527244, -0.0216494668, -0.0210884679, -0.0218407158, -0.00909073651, -0.00331180752, 0.000288667536, -0.0168554746, 0.00363374455, -0.0040130564, -0.0124758556, 0.0136297289, 0.0182962213, -0.00794323813, 0.0329459496, 0.0170594733, -0.0165877249, 0.000735116075, -0.0199409705, 0.0068913647, 0.0121124815, -0.000981748453, -0.0170849748, -0.00934573542, -0.0193289705, 0.00604667841, 0.0154529763, -0.0351644456, 0.0180412233, 0.010913983, 0.00932661071, -0.00128456054, 0.0141269788, 0.0140759787, -0.0101362346, -0.0200684685, 0.00313968281, -0.0308039524, -0.00195871573, -0.0306764524, 0.00308708893, 0.00733761396, 0.0054059918, -0.00546974177, 0.00718461396, -0.00617099041, 0.00947961, -0.0353939459, -0.000944295432, -0.0259589609, 0.0163199753, -0.0461039282, 0.00986848492, 0.0130432304, 0.0199792199, 0.0155549766, 0.000767389429, -0.0121061066, -0.00635586539, -0.0258187111, 0.00218662177, 0.0269279592, -0.0200557187, -0.00914173573, 0.0136679793, -0.0106462333, -0.0192652214, -0.0161797255, -0.00526574207, -0.018245222, -0.0101298597, -0.0166132245, 0.0318239518, -0.0022009653, 0.00482586771, -0.0287384558, -0.0297839548, 0.0115451077, -0.0293249544, 0.0167279746, 0.0230519641, -0.0222742166, -0.0334049501, 0.0253852122, -0.160343751, 0.00382818165, 0.0153892264, -0.042227935, 0.0340679474, -0.0135404794, 0.0102701094, -0.00416286848, -0.0262904596, 0.0130942296, -0.0137062287, 0.0192652214, -0.0259717107, 0.00121363881, 0.00777111296, 0.0131197302, -0.012947605, 0.0189974718, 0.00453899289, -0.00249899621, 0.0227204654, -0.0215984676, 0.000143736106, -0.0132727297, 0.00581080373, 0.0108566089, -0.0118001066, 0.0215602163, 0.00366243185, -0.0210884679, -0.0163327251, -0.00993861, 0.0155804763, 0.000129492, 0.0187934712, 0.00406724401, -0.00610724092, -0.00804523751, -0.00417561876, 0.0294269547, 0.0399839394, 0.0275909584, 0.00768186338, 0.000111163892, -0.00717186416, 0.00973461, 0.0311099533, 0.0143692279, 0.00537730427, -0.021572968, 0.000463382108, -0.0344249457, 0.00960073527, -0.0198644698, 0.0233962145, 0.0249517113, 0.00713998917, -0.00386961899, -0.0154529763, -0.00782211311, -0.0457214303, -0.023115715, 0.00938398577, -0.000474139903, -0.014305478, -0.00407361891, 0.00297552673, 0.00729936408, 0.00019124971, 0.00245437119, -0.0197879691, -0.0211139675, 0.0112518575, -0.0182197224, -0.00243524625, 0.008013363, 0.00314924517, -0.0152999768, 0.0119849816, -0.0099577345, -0.0203107186, 0.0415394381, 0.00459636794, -0.0171232242, 0.0289424565, -0.000348433066, -0.00939036068, -0.008013363, -0.015848225, 0.00979836, -0.0116726076, -0.0338639468, -0.0185129717, -0.00258027739, -0.00327993254, 0.00968361, 0.01306873, -0.00318908878, 0.0198134705, -0.00509680482, -0.00697423937, 0.0121889813, 0.000250616809, 0.00213243417, 0.0138337286, 0.0365924425, 0.00468561798, 0.00296596414, 0.0154147269, 0.00656624, 0.000337276841, 0.0103976093, 0.0217642169, 0.0112709831, -0.00737586385, 0.00884211157, 0.000929951726, -0.00320183882, 0.0194437206, 0.0028145581, 0.036362946, -0.0226694662, -0.0188572221, 0.00222327793, -0.0173144732, -0.00980473496, -0.08037588, -0.00919911079, -0.00269821472, 0.0147899771, 0.0067511145, 0.0116279824, -0.021394467, 0.0028018083, -0.0170977246, 0.0254107118, -0.0175312236, -0.0263669603, -0.0050234925, -0.00783486292, 0.0137062287, 0.0092883613, -0.0149429776, -0.0369749442, -0.0169957243, 0.0217897166, -0.00550799165, 0.000106482257, 0.0206677187, -0.0166769754, -0.0336344503, 0.0220319666, -0.023115715, 0.00178499729, 0.016460225, -0.0186404716, 0.00256912108, -0.0239572134, 0.00766911311, -0.0288149565, -0.00137859164, -0.00806436315, -0.00991948508, 0.00450393045, 0.0312374532, -0.0304214545, 0.00432224339, 0.00282571441, 0.0210757181, 0.0173782241, 0.0134512298, -0.00480355509, -0.012883855, 0.0234599635, 0.0236384645, -0.0159884747, -0.0267749596, -0.0261629596, -0.0203489698, -0.0444464311, 0.0238169637, -0.0177352224, 0.0263669603, -0.0275399573, -0.0311609525, 0.0129221054, 0.000639491191, -0.0179774724, -0.0176842231, 0.0178627223, 0.016090475, -0.0309824534, -0.0174802225, -0.00342018227, 0.00747786369, 0.0175184738, -0.0311354529, 0.0162817258, -0.0108438581, -0.000390468165, -0.0389894396, -0.0184492227, -0.0291209556, -0.0146879777, 0.0229244642, -0.0133874798, -0.0215984676, -0.0246967115, -0.000635108387, -0.0229372159, -0.00453261798, 0.0308804531, 0.00329268258, -0.000878951803, 0.00458043069, -0.00979836, -0.00710173929, 0.00790498778, 0.0201194696, -0.00607536593, -0.00414374378, -0.0109394835, -0.00194277824, 0.0109904837, 0.00930748601, 0.0356744453, -0.0277439579, -0.0140504781, -0.0740008876, 0.0204892196, 0.0155804763, -0.00938398577, 0.00256434, 0.0166514739, 0.0285854563, -6.1807521e-05, -0.000939514197, -0.000860623666, -0.0139994789, 0.022503715, -0.0121762315, 0.00317155756, -0.0246967115, -0.0218024664, 0.00193640334, 0.014305478, -0.0228352156, 0.00987486, -0.0135787297, -0.00960073527, -0.00140568533, 0.00142002909, -0.0145094777, -0.0161797255, 0.0129093556, 0.0132854795, -0.015784476, 0.000553030404, 0.0137827294, -0.0150322272, 0.0139612285, 0.010110735, -0.00977286, -0.0146369776, -0.0262904596, 0.015044977, 0.0146752279, 0.0164219756, -0.00390468165, -0.0320279524, 0.0117363567, -0.00439236825, -0.0176077224, 0.0113666076, -0.0249389615, 0.00100007665, 0.00493743, 0.0276929568, 0.00650886493, 0.0016750287, -0.0245437119, -0.00181209098, 0.00441468088, -0.00812173728, 0.0207824688, 0.00947961, -0.00807711296, -0.0245819632, 0.0409529358, -0.00557492906, 0.00821736269, 0.000754241, 0.0193034708, 0.0097537348, -0.00249740249, 0.0114494823, 0.0175439734, -0.0288659558, -0.0223124661, 0.0127244806, 0.0251429621, 0.0231412146, -0.00468243053, -0.00121842, 0.0223252159, 0.00715273898, -0.0029133705, 0.0100406101, 0.0211649686, 0.00307433913, -0.0538559183, 0.0242122132, 0.00770098809, 0.032741949, -0.0102254841, 0.0148409773, 6.74354451e-05, 0.0140759787, 0.00786673836, 0.014305478, 0.01337473, 0.014177978, -0.00827473775, -0.00637180265, -0.0325889513, -0.00268387096, 0.020897219, -0.00179934106, -0.00464418065, -0.012144356, -0.0145987282, -0.0195712205, -0.0084596118, 0.00256593362, 0.00203521573, -0.0333029479, 0.0135532292, 0.00944136083, 0.025461711, 0.0206422191, -0.0245819632, -0.00320024509, -0.0376634412, -0.000196728215, 0.00419155601, -0.00216430915, -0.0258824602, 0.0126734804, -0.00300262053, 0.0164984744, 0.0412844382, -0.00696786446, 0.0221722163, 0.00697423937, 0.0357764438, -0.033787448, 0.0205529686, -0.00150051329, 0.00978561, 0.00789861288, 0.00180571596, 0.00746511342, -0.01337473, 0.00178340357, -0.00232209032, 0.0161924753, -0.0108056087, 0.0573749132, 0.0132599799, -0.00544742914, 0.0142034786, -0.017199723, -0.0303449538, -0.00172921608, 0.010850233, -0.046409931, -0.0137062287, 0.0321299508, 0.0142927282, 0.016702475, -0.0108247334, -0.0418454371, 0.0107801082, 0.000737108232, 0.00359549443, -0.00790498778, 0.00479080528, 0.0155039765, 0.00797511265, 0.00354130706, -0.00828748755, 0.00862536207, -0.00979198515, 0.0355214477, 0.0140887285, -0.025397962, -0.0525299199, -0.0171104744, -0.0200557187, -0.0168172251, 0.00370068196, 0.0246839616, 0.00443380559, 0.011098858, -0.0148282275, -0.0103147347, 0.0333029479, -0.0236257147, 0.0321299508, -0.0199409705, -0.0260354597, 0.00523067964, 0.0208079685, -0.00128695113, -0.00499161752, -0.0355979465\], metadata={'director': 'Christopher Nolan', 'theme': 'Fiction', 'year': 2010}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, hash='7937eb153ccc78a3329560f37d90466ba748874df6b0303b3b8dd3c732aa7688', text='Inception', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.470013738)\]

Multiple Metadata Filters with `OR` condition

In \[ \]:

Copied!

from llama\_index.core.vector\_stores import FilterOperator, FilterCondition

filters \= MetadataFilters(
    filters\=\[
        MetadataFilter(key\="theme", value\="Fiction"),
        MetadataFilter(key\="year", value\=1997, operator\=FilterOperator.GT),
    \],
    condition\=FilterCondition.OR,
)

retriever \= index.as\_retriever(filters\=filters)
retriever.retrieve("Harry Potter?")

from llama\_index.core.vector\_stores import FilterOperator, FilterCondition filters = MetadataFilters( filters=\[ MetadataFilter(key="theme", value="Fiction"), MetadataFilter(key="year", value=1997, operator=FilterOperator.GT), \], condition=FilterCondition.OR, ) retriever = index.as\_retriever(filters=filters) retriever.retrieve("Harry Potter?")

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"

Out\[ \]:

\[NodeWithScore(node=TextNode(id\_='6b7bdb44-9dc2-48f6-b9cb-05dcaea4889b', embedding=\[0.0131883333, -0.0137667693, -0.0396421254, -0.00729471678, -0.0107653309, 0.0171731133, -0.0282276608, -0.0507480912, -0.0210422054, -0.01610622, 0.0254768785, 0.0143452045, 0.0170060098, 0.00128059229, -0.0103797065, -0.000858012936, 0.0219162852, -0.0112602143, 0.015424951, -0.0149622029, -0.0174430497, -0.00926139764, -0.00690909289, 0.0097370008, -0.0101161972, -0.00156177639, 0.0225204285, -0.0414159931, 0.0201038532, 0.00370198837, 0.00786672533, -0.00535053, -0.0264537912, -0.0238444041, -0.0343205184, 0.00850300491, -0.0269165393, -0.00934494939, 0.00577793, -0.0037951807, 0.0304385703, 0.0138181858, -0.0188184399, -0.0150521817, -0.0169160292, -0.0138567481, 0.011915775, -0.0171988215, -0.0302843209, 0.00484921923, 0.017700132, 0.0325209387, -0.0286389925, -0.023600176, -0.00468532881, 0.000876490725, -0.00141154369, 0.00646241195, 0.00751323672, -0.016556114, -0.0100455, -0.00316372188, -0.00587112224, -0.015090744, -0.00502275, -0.0114980163, -0.0207337048, -0.00732042501, -0.00301911286, -0.0234973431, 0.0178672355, 0.014525163, 0.0153735345, -0.0133297285, 0.0100390725, -0.00729471678, -0.020643726, -0.00382731599, -0.00339991646, -0.0126548875, 0.0267622899, -0.00226714648, -0.00968558434, 0.0245899428, 0.0247184839, 0.014409475, -0.0071918834, 0.0187798776, -0.00759036141, -0.00408761203, -0.0152321393, 0.0355288051, 0.00103475712, 0.0115558598, -0.0135482494, 0.0139210187, -0.00108697708, 0.0325466469, 0.0180729013, -0.0106882062, 0.0216977652, -0.0027009733, -0.0151935769, -0.0255025867, -0.0367885083, -0.00529268663, 0.0089978883, -0.00420329906, 0.0172759462, -0.00715332106, -0.0153349722, 0.0111123919, 0.0243714228, -0.0267622899, 0.00829091109, -0.0154378051, -0.0109002991, -0.0118772127, -0.0208879542, -0.0276363716, 0.0173273627, 0.0276106633, 0.0209650788, -0.0106432168, 0.0313383602, 0.00315890159, -0.0152964098, 0.00492313039, -0.00266241096, -0.0123206796, 0.0235359054, 0.00965987612, 0.0130019486, -0.00671628071, -0.0318268165, 0.0417759083, -0.0188184399, 0.00364093133, -0.0238572583, -0.0126484605, 0.0232274067, 0.0223019086, -0.0299758222, 0.0173916332, -0.0101226242, 0.0102640195, 0.0101933219, 0.00359272817, 0.0108231744, -0.0167489257, 0.0173145086, -0.00805311, 0.0105403839, 0.0277649127, 0.0185356494, 0.00911357533, 0.00782173593, 0.0113951825, -0.0289474912, -0.0185613576, 0.018034339, 0.0247827545, 0.0159776788, -0.000874080579, 0.0135482494, 0.0198082086, 0.0357858874, 0.0114915883, 0.0107589038, -0.0123463878, -0.0160162412, 0.00124444009, -0.0238186959, 0.00484279217, 0.000368953595, 0.0064109955, 0.0186898988, 0.0130019486, -0.0270964988, -0.00176904909, 0.000858816318, 0.0121600032, 0.0260167513, 0.047431726, -0.00881150365, -0.00815594289, 0.0116586927, -0.00481065689, 0.020528039, -0.0014203809, 0.0143837668, 0.038022507, 0.00139467267, 0.0146279959, -0.665535212, -0.0407475792, -0.014756537, -0.0108296014, -0.0112087978, 0.00891433656, 0.0050934474, 0.0279962867, -0.00877294131, -0.0142423715, -0.0123335337, -0.00651704194, 0.027122207, -0.00235873205, -0.025309775, -0.000651141803, -0.0226361156, -0.0042900648, -0.000323361601, 0.00583577342, 0.0126356063, 0.0197567921, -0.0282276608, -0.0268137064, 0.000913446362, 0.0175201744, 0.00810452644, -0.016903175, 0.021672057, 0.018265713, 0.0100840619, 0.02155637, 0.0101033431, 0.0297701564, 0.0298215728, 0.0252197962, -0.022237638, 0.0208236836, 0.00451822532, 0.0413131602, -0.0252455045, -0.00190562417, 0.00193454593, 0.0103797065, -0.0101740407, -0.00384338363, 0.0303614456, -0.0105082486, 0.00179636409, 0.00249852077, 0.020091, -0.0255540032, 0.00708905049, 0.0215820782, 0.0138696022, 0.0183171295, 0.0377911292, 0.00726900855, 0.00831019226, 0.00956347, -0.0102961548, 0.0117550986, -0.012474929, 0.00986554194, -0.00164693489, -0.000925497094, -0.0225075744, 0.00533124898, 0.00472067762, -0.038253881, 0.02133785, 0.0158619918, -0.0123785231, -0.00331957801, 0.00288414466, -0.0208365377, 0.0347575583, -0.00876651425, 0.007146894, 0.00998122897, 0.0040843985, -0.00134968327, -0.0162990317, -0.0207979754, 0.038356714, -0.00187348889, -0.0323923975, 0.00889505539, 0.0134839779, 0.0191012323, 0.00175458821, -0.00845801458, -0.0140367057, 0.0166075304, -0.0146537041, -0.00573294, -0.0013842287, 0.00528947311, 0.00947991759, -0.0131240627, 0.0154506592, 0.00436718948, -0.0161833446, -0.0274821222, -0.0012307826, 0.0171088427, 0.00684482232, 0.00656203134, 0.0423672, -0.0115237245, 0.0364285931, -0.0207079966, -0.0043800436, 0.00134325621, 0.00287611084, -0.0229317602, 0.0297444481, 0.00959560554, 0.00289539201, -0.0146537041, 0.0137539152, 0.010778185, -0.00148143806, -0.0042193667, 0.00257725222, -0.00229606824, -0.00807881821, -0.00213057152, -0.0117293904, 0.00113759015, 0.0294873659, 0.00742968498, 0.0266080406, -0.00710833166, -0.00652989605, -0.0066584372, 0.0319296494, -0.00525091076, 0.026209563, -0.0148722241, -0.0182142965, -0.00612499099, -0.0284333266, 0.00551763363, -0.00988482311, -0.0483058058, -0.0141266845, 0.00208076159, -0.00190401741, -0.00532160839, -0.0339348912, -0.00960846, -0.0342691019, -0.0104054147, -0.0125392005, -0.0189984, 0.00553048775, -0.000976913609, -0.0159776788, -0.00729471678, 0.0125263464, 0.0123913772, -0.00960846, -0.00882435776, 0.0147436829, -0.000602135493, -0.0110481214, 0.0172245298, -0.00804025587, -0.0282019526, -0.00996837486, 0.00152080378, -0.00294841523, 0.010662498, -0.00389480032, 0.0179829225, -0.00437683, 0.0121792844, 0.00829091109, -0.0165432598, 0.0070119258, -0.0208622459, -0.0155149307, 0.000502114301, 0.0408761203, -0.00473353174, 0.026428083, -0.00245353137, 0.0106753521, 0.007146894, -0.00747467438, 0.0243971311, 0.0238444041, -0.0077960277, -0.0108038932, 0.0173402168, -0.00198435574, -0.00586790871, -0.003573447, 0.0423929095, 0.0229446143, -0.00850300491, 0.0211707465, -0.032109607, 0.0117358174, -0.0355802216, 0.0198853333, -0.0224818662, 0.00599323632, 0.00898503419, 0.00283915503, -0.0118579315, -0.0195511263, -0.0208108295, 0.00616034, 0.024949858, -0.0231374279, 0.000281786546, -0.0352974311, -0.00435112184, 0.00398477912, 0.00443788711, 0.020528039, 0.00664558308, -0.00304803462, 0.0183042753, -0.0030400008, -0.00253386959, 0.0305928197, -0.0254640244, -0.00465640705, 0.000375179807, -0.00727543561, 0.011343766, -0.00429327833, 0.00844516, 0.0265052076, -0.0385366715, 0.0331122279, -0.00616998039, -0.00948634464, 0.00853514, 0.0133682908, -0.0208108295, 0.0103090089, -0.0229446143, 0.0143066421, -0.00856727548, -0.0135482494, 0.0192040652, -0.00551442, -0.00536338426, -0.0205151848, -0.00414866908, 0.0212350171, -0.00292110024, 0.0208879542, -0.000678055163, -0.00563974772, 0.0321353152, 0.00141797075, 0.00816879701, 0.00325852097, 0.0168131962, 0.0103411442, 0.010212603, -0.00547907129, 0.0146022877, -0.0201552697, -0.0139724351, -0.0164918434, -0.02133785, 0.00630173553, -0.0103861336, 0.00610571, 0.000804989657, 0.000960042526, 0.0129505321, 0.00260135368, 0.0144737456, -0.00465640705, -0.0208108295, 0.00167907018, -0.00432541361, -0.00755822612, -0.0226746779, -0.00331315096, 0.00516735855, 0.00805311, -0.00365378545, 0.0203223731, 0.0150264734, 0.0182914212, -0.0134711238, -0.00353488466, -0.0207079966, 0.0239086747, -0.032443814, -0.0138953105, -0.00793742295, -0.0326237716, -0.0246027969, -0.0104889665, -0.021903431, 0.0430870317, -0.0167360716, -0.0113887554, -0.0134582696, 0.0288446583, 0.00664558308, 0.0173530709, -0.000582452572, -0.0168517586, -0.00563332066, -0.00612820452, 0.0156049095, 0.00122917583, 0.00558833126, 0.0242043193, -0.0043125595, 0.0170959886, -0.0316982754, -0.0255154409, 0.0283819102, 0.0949148685, 0.00521234795, -0.00745539321, 0.0154378051, 0.0125777628, -0.0005362581, -0.0291274507, -0.00714046694, 0.0114465989, -0.0202966649, 0.0172116756, 0.000426998, 0.0164147187, 0.0190626699, -0.00791171473, -0.0119479103, 0.00747467438, -0.0158748459, -0.0111702355, -0.0142809339, -0.0233430937, 0.00143725204, 0.0161576364, 0.0080659641, -0.0123142526, -0.0400277488, 0.00185420772, 0.0181628801, 0.00147340423, -0.0115430057, -0.0051384368, -0.0215306617, -0.0140881222, -0.00259010633, 0.00621175626, 0.0182785671, 0.0356573462, 0.0198853333, 0.0101933219, -0.014409475, 0.0146279959, -0.00538266543, 0.0224433038, -0.00260456721, 0.0198981874, -0.0137539152, -0.0123849502, 0.024731338, 0.0320581906, 0.00535374368, 0.0054694307, 0.0134454155, -0.013046938, 0.0125070652, 0.0166075304, 0.0130083757, 0.007146894, 0.00455357414, -0.0123013984, -0.000179154376, -0.00136976782, -0.0278934538, -0.00565260183, 0.00860583782, -0.0303614456, -0.029615907, -0.0054919254, -0.0129955215, -0.00407154439, 0.0173530709, -0.00318943, -0.0193711687, -0.001886343, -0.00793742295, 0.0107460497, -0.00245835166, 0.0236258842, 0.00462748529, 0.0163633022, 0.0248084627, -0.0169545915, -0.0414159931, -0.00318139629, -0.0385109633, 0.00558511773, 0.0192040652, -0.0127577204, 0.0101097701, -0.0214792453, 0.00729471678, 0.0186384823, 0.00467890175, 0.0122114196, -0.0212992877, 0.010662498, -0.00014149581, 0.00500989566, 0.0118643586, 0.00979484431, -0.00675484352, -0.00159953535, -0.00930638704, 0.00682554115, -0.00965344906, 0.0268394146, 0.0153992428, 0.00505167153, 0.0457606874, -0.0207979754, -0.00937065762, 0.0228931978, -0.0123335337, 0.027353581, -0.00941564701, -0.00238444051, 0.0316211507, -0.0138567481, 0.00834232755, 0.0198082086, -0.0348089747, -0.00693480112, -0.0340634361, 0.0217748899, 0.0263509583, -0.0044925171, 0.0265052076, -0.00140350987, -0.0174559038, 0.00254351017, 0.00418401789, -0.0343719348, 0.0478687659, 0.0025692184, -0.00256761163, -0.0233302396, -0.0048010163, -0.0199881662, -0.0172759462, 0.00532803545, -0.00973057374, -0.0247184839, 0.000261300273, 0.00270258, -0.0222890545, -0.0200652909, -0.0211450383, 0.00808524527, -0.0164404269, -0.0181243178, -0.00339991646, 0.00209040218, 0.000144508493, -0.00970486552, 0.00364414486, 0.00993624, -0.0256182738, -0.0154892216, -0.0129826674, -0.00166942959, 0.0184328165, 0.0345776, 0.00946063641, 0.00746182026, 0.00354452524, -0.00267526507, 0.00441539241, 0.0268394146, 0.0124106584, -0.0143709127, 0.0221348051, 0.023715863, -0.000923086947, 0.0312355272, -0.00128219905, 0.0344490595, 0.0179700684, 0.00159792858, 0.0265823323, 0.00334528624, -0.0140109975, -0.0198467709, 0.00373733719, -0.00659416663, 0.017031718, -0.038356714, -0.0183814, 0.000772452622, -0.0198082086, 0.00227357354, -0.0146922665, 0.0303871538, -0.0219677016, -0.00233784411, -0.0121600032, 0.0186898988, -0.0319553576, 0.0182142965, -0.0265052076, -0.00760321552, 0.00499382801, 0.0301557798, 0.0123528149, 0.0164918434, 0.00487171393, 0.0305671114, 0.0192554817, 0.00616355333, 0.00967915729, 0.0276363716, -0.00832947344, -0.00424507493, -0.0242043193, 0.00643349, -0.0122628361, -0.0109195802, 0.00479780277, -0.00577793, 0.0260296054, -0.0239858, -0.000108356267, 0.0135482494, -0.021903431, 0.0288189501, 0.0109967049, 0.00739112264, 0.0108681638, -0.00118257955, -0.0160676576, 0.0342433937, 0.00742968498, -0.00989767723, 0.0144994548, 0.0204252061, 0.00739112264, -0.0190112535, -0.0133297285, -0.00711475872, -0.0397192501, -0.0153735345, 0.0099169584, 0.0208365377, -0.00510951504, -0.00628888141, -0.00825877581, -0.0180214848, 0.0134325614, -0.0250269845, -0.00501310918, -0.0253869, -0.0198210627, -0.00232820353, 0.00107974664, -0.00232338323, -0.00546621718, -0.0151164522, -0.0148336617, 0.0205537472, -0.0187670235, -0.00258367928, -0.00648812, -0.0232016984, 0.026659457, -0.00964059494, 0.00179636409, 0.0288446583, -0.00548871187, -0.00288896495, 0.00476888102, -0.0148208076, 0.0219419934, -0.0119543374, 0.00100342522, 0.00168549723, 0.0191655029, -0.00370841543, 0.015424951, -0.00563010713, -0.0279705785, 0.00483315159, -0.0154763674, 0.00212414446, 0.0103861336, -0.0182271507, 0.000870063668, -0.0136896446, -0.0211450383, 0.00460177707, -0.00920998119, 0.000132658592, -0.0455550216, -0.0206694342, -0.030181488, -0.0246027969, 0.0134968329, -0.016003387, 0.00178833026, 0.0204380602, 0.0594374798, -0.00758393435, -0.0133682908, -0.00718545634, -0.00274435594, -0.00150875305, -0.00141636399, 0.00392693561, -0.0179572143, 0.0144994548, -0.0112087978, -0.0103925606, 0.00717260223, 0.00511272857, -0.00369234779, 0.00412296085, -0.00594824692, -0.0096920114, 0.0080659641, 0.00834875461, 0.0178415272, 0.00299983169, 0.00694122817, 0.00965344906, 0.00704406109, 0.0213635582, -0.0150007652, 0.0102254571, 0.0172116756, -0.0156948883, -0.00449573062, -0.0456835628, -0.00805311, -0.0254511703, 0.0363257602, -0.0281505361, -0.0128669804, -0.0264795, -0.010321863, -5.48810931e-05, -0.00144608924, 0.00710833166, -0.0227646567, -0.00158507447, 0.0369427577, 0.0145765794, 0.0066584372, -0.0137024987, -0.0105789462, -0.0212350171, -0.0209907889, -0.0338577665, -0.0221605133, -0.00129424979, 0.0385366715, 0.00643991726, 0.0115494328, -0.019294044, -0.00957632437, -0.00845158752, -0.0204252061, -0.0228803437, 0.0121021597, 0.0353488475, 0.0108296014, 0.0206051636, 0.00549835246, -0.00993624, -0.0162476152, -0.00404262263, 0.0128091369, 0.00787957944, 0.0129955215, 0.0438839868, 0.0204380602, 0.00742968498, -0.0197182298, 0.00706976932, 0.00976270903, -0.0120507432, 0.00304321432, 0.00144689262, 0.0016421146, 0.00204541278, 0.000219524372, 0.000348668167, -0.000840338471, 0.00680626, -0.0319296494, -0.0132011874, -0.0129441051, -0.0126934499, -0.0072433, 0.0150393276, 0.00530232722, -0.00913928356, 0.0253226291, -0.010553238, 0.00166139577, -0.00747467438, 0.00610249629, 0.0280991197, -0.0182014424, 0.00104600447, -0.00189277006, -0.0062535326, -0.00428363774, -0.00218841503, 0.00487171393, -0.0265309159, -0.0213249959, -0.0189341269, -0.0182528589, 0.00250816136, -0.0186256282, -0.00217877445, -0.0131176356, -0.00461141765, -0.015772013, -0.00699907169, -0.0291274507, 0.0316468589, 0.019859625, -0.0106175086, 0.00340634352, -0.0261967089, -0.017250238, 0.0161833446, -0.0399249159, -0.00575543521, 0.00587112224, -0.025643982, -0.00116651191, -0.0177258402, 0.00329386978, -0.0100776348, 0.00404262263, 0.0016967447, 0.0138953105, 0.219856977, -0.00185420772, 0.00248084636, 0.0219677016, 0.00360236876, 0.0197953545, 0.028921783, -0.0156177636, -0.0293588247, 0.0079309959, -0.0225589909, 0.0270964988, -0.000545095303, 0.00126131112, -0.00876651425, -0.0097370008, -0.0344490595, -0.0232402608, -0.0286647, -0.0332407691, -0.0101161972, -0.0194997098, -0.0253611915, -0.033909183, 0.0116394116, 0.00529268663, -0.0155920554, -0.0141266845, 0.0467376038, 0.00424828893, 0.00491991686, -0.000484038173, -0.00226553972, 0.00251780194, -0.0187670235, -0.00676769763, 0.0170188639, -0.000114984177, 0.00711475872, 0.0130790733, -0.0223147627, 0.0131240627, -0.0244614016, -6.42204177e-05, -0.00727543561, 0.0157848671, -0.0148850782, -0.00925497059, -0.00473353174, 0.0275335386, -0.0259010643, -0.0175973, 0.0468147285, 0.0399763323, -0.0251169633, 0.0109195802, 0.0223019086, 0.00984626077, -0.011806515, -0.0214149747, -0.0019634678, 0.0280991197, -0.0196925215, -0.0119222021, 0.0113951825, 0.0302843209, -0.016453281, -0.0104118418, 0.0127255851, -0.0224947203, 0.00906215888, 0.00366663956, -0.0161704905, 0.00308981049, -0.0219162852, -0.0282790773, 0.0111316731, 0.0047496, -0.00509987446, 0.0269936658, -0.0044025383, 0.00902359653, 0.00276363711, 0.0140881222, -0.0175715908, -0.0464291051, 0.0106303627, -0.017584445, 0.00180279114, -0.00135450356, 0.00721116457, 0.000410729495, 0.00646241195, -0.00776389241, 0.0218391605, 0.0135353953, 0.00431577303, 0.0362229273, -0.00642384961, 0.0107460497, -0.0152707016, -0.000495285552, -0.000503319374, -0.00280541298, -0.0159005541, 0.00856727548, -0.00941564701, 0.0232402608, 0.0216463488, -0.00217877445, 0.0306956526, -0.00304160756, -0.00491670333, 0.00912000239, -0.00313801365, 0.0136896446, -0.0260681678, -0.0166975092, -0.0134454155, -0.0271993317, -0.0132011874, -0.00843230635, 0.00326334126, 0.0118193692, -0.00510630151, 0.00609928276, 0.00418401789, 0.00241978932, -0.00291628, -0.0330608115, 0.0126420334, -0.00825234875, 0.0192040652, -0.00950562675, 0.0179700684, 0.0173145086, 0.0189212728, 0.00743611204, -0.00867653545, -0.00908144, 0.00222215708, -0.0279191621, -0.00118579308, 0.0275849551, 0.000910232833, -0.0142295174, 0.00965344906, -0.0167232174, -0.0106432168, -0.0325466469, -0.0178029649, -0.00869581662, -0.00578435697, -0.0226232614, 0.0190112535, -0.0134068532, -0.0298986975, -0.0193968769, -0.00823949464, 0.0127255851, -0.023034595, 0.020643726, 0.00883078482, 0.00104359433, -0.0110738296, 0.0160290953, -0.163607314, 0.00861226488, 0.0225461368, -0.0177772567, 0.0288960747, -0.0223790333, 0.0280991197, -0.00896575302, -0.00254190341, 0.0132011874, 0.00111991575, 0.00746182026, -0.0264537912, 0.00306731579, -0.0103539983, 0.0188184399, -0.011800088, 0.00708905049, 0.0244485475, 0.00998765603, 0.0251812339, -0.0171474051, 0.00106126873, 0.00630173553, 0.0295130741, 0.0027009733, 0.00170156499, 0.0113887554, 0.00422900729, -0.012821991, -0.00902359653, 0.00674198894, -0.00809809938, -0.00984626077, 0.0244614016, -0.00623103743, 0.00101868948, 0.024731338, 0.0095570432, 0.031878233, 0.0413645767, 0.0153606804, 0.0413645767, -0.00484921923, -0.0175973, 0.0173016544, 0.0277906209, 0.012031462, 0.00559154479, -0.0214921, -0.00611856394, -0.00551120657, 0.0177129861, -0.0191140864, 0.0151935769, 0.0164018646, 0.00024141655, 0.0066584372, -0.00116570853, 0.0014525163, -0.0200267285, -0.020309519, 0.0173273627, 0.00955061615, -0.0114465989, 0.00531839486, 0.0127191581, 0.0112216519, -0.0278420374, 0.00919712707, -0.0356059298, -0.0352203064, 0.00992338546, -0.0110288402, -0.0103154359, -0.00122194539, -0.0109517155, -0.00924854353, -0.000695327879, 0.00301589933, -0.0232531149, 0.0224304497, 0.00542765483, -0.00708262343, 0.0296673235, 0.0070569152, -0.00769319432, -0.0102640195, -0.0298986975, -0.00517378561, 0.0197310839, -0.0266851652, -0.0361458026, -0.014756537, 0.0331636444, 0.00894647185, 0.0161833446, 0.00454714708, 0.0244742557, -0.0167360716, 0.0043800436, 0.0144994548, -0.00839374401, -0.0161576364, 0.0208493918, 0.00910072122, -0.00599323632, -0.0070119258, 0.0241529029, 0.027122207, -0.0186898988, 0.00546621718, 0.0265566241, 0.00989125, -0.00881150365, 0.00766105903, 0.0154892216, -0.0364800096, 0.0222890545, 0.01464085, 0.0474060178, 0.0040619038, -0.0195896886, 0.00900431536, 0.00252744253, 0.0047560269, -0.0730114356, -0.0278934538, -0.00616034, 0.00614105863, -0.00170638529, 0.0178929437, -0.0134711238, 0.00351239, -0.0166460928, 0.0260810219, -0.0139081646, -0.0192169193, -0.00910714827, -0.0171474051, 0.011909348, 0.00352524407, -0.0256054197, -0.0174301956, -0.030849902, 0.00655239075, 0.00266241096, 0.00946063641, 0.00465962058, -0.00617319392, -0.0206694342, 0.00159873196, -0.0267108735, 0.0166589469, 0.0216206405, 0.00266562449, 0.0113694742, -0.010893872, -0.0162347611, -0.0212992877, 0.013381145, 0.0104246959, 0.0128348451, 0.0116008492, 0.0140109975, -0.0438325703, 0.00529911369, -0.00780888181, -0.00536659779, -0.0137410611, 0.0197567921, -0.00762249669, -0.0382795893, 0.00536338426, 0.00573615357, -0.0033517133, -0.0197053757, 0.00117856264, 0.00589361694, -0.0171859674, 0.0218263064, -0.0286132842, 0.0138310399, -0.0117293904, 0.00854156725, 0.0263766665, -0.010096916, -0.025643982, -0.00425471598, 0.0200395826, 0.0126420334, 0.00373412366, 0.00547264423, -0.0137153529, 0.0257082526, -0.0254511703, -0.00323281274, 0.0121728573, -0.024499964, 0.00896575302, -0.0135996658, -0.00632423, -0.0297187399, 0.00239890139, 0.00435112184, -0.0291531589, -0.0171988215, -0.0227775108, 0.00134164945, -0.0275849551, 0.0426242836, 0.018831294, 0.0246027969, 0.0171731133, 0.02155637, -0.0165046975, 0.00596110104, 0.0154892216, 0.0230217408, -0.00867010839, -0.00432541361, 0.00898503419, -0.00545336306, 0.026659457, 0.0294102412, 0.0089528989, -0.031544026, 0.0148336617, -0.0676127, 0.0242300276, 0.0131176356, -0.0258882102, 0.0159648247, 0.00945420936, -4.66715246e-05, 0.00792456884, -0.00536981132, 0.00417116378, -0.013278312, 0.0187927317, -0.0112794954, -0.00494883861, -0.0128605533, -0.00470461, 0.00439289771, 0.0181243178, -0.0130790733, 0.00385302422, -0.0008596197, -0.00258046575, 0.0192426275, 0.0080209747, -0.0292302836, -0.0103090089, -0.0130726462, 0.0141523927, -0.0245385263, 0.00943492819, 0.00516414503, -0.0350403488, 0.0179829225, 0.0150393276, -0.0107717579, 0.00229928177, 0.00685124937, 0.00210968335, 0.00111268531, 0.0206051636, -0.0120764514, -0.0174944662, 0.024499964, -0.0177386943, 0.0055819042, 0.0285361595, -0.0295901988, 0.0149364946, 0.0162476152, 0.0201681238, 0.00211932394, 0.0308241937, -0.00043744198, 0.000492072, -0.00821378641, -0.00845158752, 0.0155020766, -0.0127320122, -0.00646241195, -0.0349118076, 0.00244871108, -0.0203223731, -0.010431123, -0.0205408931, 0.00184456713, 0.00347061409, 0.017134551, 0.00154972554, 0.0248598792, -0.00336135388, -0.0262995418, 0.0119800456, 0.00795670412, 0.0290760342, -0.0108553097, 0.000443467346, 0.0040619038, 0.0159005541, -0.0143580586, 0.00155534921, 0.0121728573, -0.00134727312, -0.0381767564, 0.0225075744, 0.0116458386, 0.0243200064, -0.0132526038, -0.0163761564, -0.00249048695, 0.0201552697, 0.00256761163, 0.00730757089, 0.0165046975, 0.0187284611, -0.00205666013, 0.00122033863, -0.0236901548, 0.0114915883, 0.00872152485, 0.00576828932, -0.000425391248, -0.012474929, -0.00389480032, -0.0259653348, -0.0357858874, -0.00248727342, -0.0236258842, -0.0301557798, 0.0115044434, -0.00328744273, 0.00471425056, 0.0259653348, -0.013162625, -0.00258207251, -0.0175201744, 0.0109517155, 0.00745539321, -0.00732685206, -0.00116169162, 0.0183042753, 0.00504524447, 0.00843230635, 0.0284847431, -0.0282019526, 0.0215435158, 0.00105644844, 0.0150650358, -0.0208879542, 0.0134839779, -0.0128991157, -0.0166203845, -0.0271479152, 0.0080209747, 0.00114401721, -0.00118257955, -0.00937708467, -0.0195382722, 0.031209819, -0.00982698, 0.0531132482, 0.00708905049, -0.00667129131, -0.0111381, -0.026428083, -0.00961488672, -0.00171120558, -0.00244710431, -0.0310812779, -0.0318011083, 0.0189469811, 0.0178929437, 0.0163247399, -0.0111959437, -0.0388965867, -0.0146279959, 0.00412296085, 0.0105918, -0.0206951424, -0.000291828823, 0.0304385703, 0.00892076362, 0.00848372281, 0.00370198837, -0.00910714827, -0.0157077424, 0.0453236476, -0.00607357454, 0.00253065606, -0.0420329943, -0.0163761564, -0.0170445722, -0.0171474051, -0.00527340546, 0.0111959437, -0.00434469478, -0.00521234795, -0.00232177647, 0.0123399608, 0.0101933219, -0.0187284611, 0.0380739234, -0.0221476592, 0.00493277097, -0.00102752668, 0.00693480112, -0.0202966649, -0.000482029718, -0.0274049975\], metadata={'author': 'J.K. Rowling', 'theme': 'Fiction', 'year': 1997}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, hash='1b24f5e9fb6f18cc893e833af8d5f28ff805a6361fc0838a3015c287510d29a3', text="Harry Potter and the Sorcerer's Stone", start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.300355315),
 NodeWithScore(node=TextNode(id\_='7fed3d0b-e2d7-432a-9231-3ac02130c00f', embedding=\[0.00310940156, -0.0246712118, -0.0222742166, -0.0364649445, -0.00715911388, 0.0117236068, -0.0400604382, -0.0275654588, -0.0157589763, 0.00740136392, 0.0278459582, 0.029962454, 0.0187679715, -0.00440511806, 0.00412780605, 0.00442743069, 0.0276674572, -0.00760536361, -0.00303608901, -0.012947605, -0.00570242899, -0.01923972, 0.00208462193, 0.0092118606, 0.00205274695, -0.0128328558, 0.0136297289, -0.0292994548, 0.0149939768, -0.0193289705, 0.0219937172, -0.00944136083, -0.0221977159, -0.00928198546, -0.00940948538, -0.00429993076, -0.0119786067, -0.0272339582, 0.0158864763, -0.0080261128, 0.0143437283, 0.00407999381, -0.00648655277, -0.0170722231, 0.00394293154, -0.0149939768, -0.00831298716, -0.0212669671, -0.0228479654, 0.0105123585, 0.0167662241, 0.0527849197, -0.0421514362, -0.0262139607, -0.00156506011, -0.00443380559, -0.00724836392, 0.00597655354, 0.0354959443, -0.00842773728, -0.00259143347, -0.00748423859, -0.0113602327, 0.00446568057, 0.00110207649, -0.00814723782, -0.0293504559, -0.00159932568, -0.002620121, -0.00987486, 0.0405959375, 0.0500819236, 0.0242504627, 0.00166227866, 0.00172921608, 0.020769719, 0.0108884834, -0.0177224725, -0.0181432217, 0.0102828592, -0.00192684087, -0.01313248, -0.0168554746, 0.0307019539, 0.0214709677, 0.0193544701, -0.00752248848, 0.0236257147, 0.0111753577, -0.00342974486, 0.00284962077, 0.00194277824, 0.039830938, 0.023485465, -0.0199919697, 0.0154529763, -0.0131962299, -0.00124949811, 0.0134894792, -0.0197624695, 0.021203218, 0.0137062287, -0.0169574749, -0.0205147192, -0.00436049327, -0.0307019539, 0.0176587235, -0.00387918158, 0.0247349627, -0.0103529841, -0.0174547229, 0.0141524784, 0.0326144509, -0.015287227, -0.0133619793, 0.00142720097, 0.0320789516, -0.0129093556, 0.011219983, -0.0230137147, 0.0161542259, 0.0332009494, 0.00287193316, -0.0117682321, 0.0194564704, 0.0134257292, 0.00268227723, -0.00101840473, -0.00237309, -0.0019013409, 0.0287129562, 0.00605305331, 0.0164729748, -0.00611361582, -0.0191632211, 0.0252832118, -0.0152362268, 0.034271948, -0.0182197224, -0.0288659558, 0.017327223, 0.0317219533, -0.0138847288, 0.0215219669, 0.00148616964, 0.0190229714, 0.000236273074, 0.0140377283, 0.0296309553, 1.55763919e-05, 0.0136679793, 0.00215315307, -0.00300102658, 0.0186659712, -0.00411505625, 0.0307274535, 0.0160777252, 0.00638455292, 0.00648655277, 0.0150959771, 0.0026759021, 0.004376431, 0.0038313691, 0.00076499884, 0.0301154535, 0.0223762151, 0.0180412233, -0.00129252928, -0.0119339814, 0.0129731055, -0.00279383943, 0.00654074, -0.0249262117, 0.0291209556, -0.00252768374, 0.00199537189, 0.014241728, 0.00161526317, -0.0360569432, -0.0294269547, 0.018002972, 0.0166514739, 0.0377909429, 0.0324359499, -0.0249134619, -0.0124949813, 0.0245819632, -0.0213179681, 0.0189974718, 0.00352855702, 0.00503305485, 0.0214582179, 0.0238169637, 0.00242090249, -0.651575, -0.0190357212, 0.0048704925, -0.00865723658, 0.0117427325, 0.0166514739, 0.00119531073, 0.0226567145, -0.014547728, -0.0105697336, -0.0111052329, -0.00859348662, 0.0186914708, -0.0139102284, -0.0432989337, -0.00793686323, -0.0220829658, -0.00709536439, -0.0278714579, 0.00343611976, -0.0167789739, 0.0162434746, -0.0455939323, -0.0106079839, -0.00494380482, 0.00252927747, 0.0331244506, -0.0257294606, 0.00623155292, -0.00325124501, -0.00392380636, 0.0150577268, 0.00994498469, 0.0225419663, 0.0425594337, 0.0087719867, -0.0111817326, 0.0307784528, 0.00728661381, 0.0435794331, -0.0125651062, -0.00641961535, 0.0209992174, 0.00480355509, -0.0133109801, 0.0251302123, 0.00989398453, -0.0291464552, 0.0231284648, -0.0155167263, 0.0188317206, 0.000304405781, -0.00463780528, 0.0156442262, -0.00439236825, 0.0223762151, 0.02613746, 0.0129539799, -0.00112917018, 0.0151342265, -0.00870823674, -0.0186277218, -0.0297329538, 0.0173782241, -0.0211777184, 0.0227332152, -0.0147772273, -0.0148919774, 0.0182962213, -0.0282539576, 0.0202342197, 0.0331754498, -0.00733123859, -0.0151597271, 0.00619967794, -0.0138974786, 0.0456704311, 0.00312693277, 0.0187552217, 0.0177989732, -0.00784123782, -0.0147899771, -0.0134257292, -0.0149684772, 0.0282029565, -0.00641961535, -0.0279734582, -0.00807711296, 0.0156952254, -0.000839108077, -0.00745236361, -0.00872098655, -0.013502229, 0.000639491191, -0.00991311, 0.00435730582, 0.00927561056, 0.00872736145, 0.0203617197, -0.0186277218, 0.0113538578, -0.00815998763, -0.0027524021, -0.00493105501, -0.000635905308, 0.017135974, 0.00815361273, 0.0165877249, 0.0389129408, -0.0162944756, 0.010722734, -0.0322319493, -0.0147389779, 0.0106079839, 0.00919911079, -0.0267239586, 0.0278204568, 0.0178754721, 0.0171487238, -0.0100214845, -0.0113156075, -0.00483861752, 0.0076563633, 0.00935848616, 0.030574454, 0.00866998639, -0.0131069804, -0.00276515214, -0.0330734514, 0.00422661845, 0.0236002132, 0.0148409773, 0.0381224416, -0.0193927195, 0.000672163034, 0.0186659712, 0.00437961845, -0.0340679474, 0.014981227, -0.0377909429, -0.0340679474, 0.00441468088, -0.00339468243, -0.0119786067, -0.0122782309, -0.0456959307, -0.0199027192, 0.00363055686, 0.00792411249, 0.0147517277, -0.0216877162, 0.00978561, 0.0132599799, 0.021572968, 0.00146146654, -0.0322829522, 0.0089887362, -0.0233834647, -0.0175567232, -0.0252322108, 0.0270809587, 0.0150194773, -0.0400604382, -0.0109076081, 0.0252832118, -0.00270777708, 0.0187169723, 0.0233452152, -0.0171742234, -0.0188189708, 0.008013363, -0.0107482336, -0.00763086323, 0.00140887289, 0.0223889668, 0.0298859552, -0.0158354752, -0.00268387096, 0.0151979765, -0.022006467, 0.0105251092, -0.00608811574, -0.0218024664, -0.0142544778, 0.0248752125, 0.0138337286, 0.0420239344, 0.0274889581, -0.00262808963, 0.00637817755, -0.0112582324, 0.00303130783, 0.00754798856, -0.0215347167, 0.00180093478, 0.0280754566, 0.0172252245, 0.0121889813, 0.00180890353, 0.0209099688, 0.0366434455, -0.0160522256, -0.00279543316, -0.00701248925, 0.0213434678, 0.00352855702, 0.0235747136, -0.0288149565, 0.00874011125, -0.0285344571, 0.0116088577, -0.0122017311, -0.0227587149, -0.00744598871, 0.0111179827, 0.0340424478, -0.0236002132, 0.0103338594, -0.0301154535, -0.0121698566, -0.0130177299, -0.000304405781, 0.0101617342, 0.00903336145, -0.0106526092, -0.0045995554, -0.0228607152, 0.00581399119, 0.0175949726, -0.0402899384, -0.00288627692, 0.0334559493, -0.000845483097, 0.017505724, -0.0204254687, 0.00477168, 0.022682216, -0.0144967278, 0.0385304429, 0.0125523554, 0.00611042837, 0.0132599799, 0.0266474597, -0.0198262203, 0.0127244806, -0.0285344571, 0.0201449692, 0.00233643386, -0.0211139675, 0.0159757249, -0.0153764766, -0.0204892196, -0.0164474752, -0.00671923952, 0.0207314678, -0.00648974, -0.00344249466, -0.0201322194, 0.0180539731, 0.0387089401, -0.00412780605, -0.0156187266, 0.00747148879, 0.0135149797, 0.00484180497, -0.0230392143, -0.00119849818, -0.00277949567, -0.0200174693, -0.00214199675, -0.00164315372, -0.00346799474, 0.00958161056, 0.0107546085, 0.00835123751, 0.0112709831, 0.00632399041, 0.0174929742, 0.0177479722, 0.00944773573, -0.0178117231, -0.0092118606, 0.0112964828, -0.000124710743, 0.00257230853, -0.0060976781, -0.00112518575, 0.00165430992, -0.0106398584, 0.0130496053, -0.0177734736, 0.00953061, 0.00119929505, -0.0203744695, 0.00425211852, -0.0340679474, 0.0217897166, -0.0165494755, 0.00660449, -0.0163454749, -0.0259972103, -0.0103529841, 0.0158099756, -0.00949236, 0.0241739638, -0.00962623488, -0.00284802681, -0.0118001066, 0.013871979, -0.0100724846, 0.0260992106, 0.00933936052, -0.0136042293, -0.0231539644, 0.024416212, -0.0131962299, -0.0149684772, -0.0280754566, -0.000733123859, -0.00204318436, -0.00430949358, -0.0199792199, -0.0221977159, 0.0222359654, 0.0914938599, 0.0360569432, -0.0109777329, 0.0186532214, 0.000553030404, -0.0112454826, -0.0356999449, 0.0175567232, 0.0111116078, -0.0142672285, 0.0156314764, -0.014177978, 0.0179647226, 0.0061454908, 0.00734398887, -0.00976011, -0.0366689451, -0.00565461628, -0.00986211, -0.0170084741, -0.0375359431, -0.0103338594, 0.0229499657, 0.0273104589, 0.00178499729, -0.0478124283, 0.0345014483, -0.000409593136, -0.014177978, -0.0155804763, 0.00433180574, -0.00195074698, -0.0114176078, -0.000521952345, 0.00619330304, 0.0195457209, 0.0266984589, 0.0202087183, 0.0204254687, -0.00956248585, -0.0110159833, -0.0121698566, 0.0150194773, -0.0044879932, 0.0074906135, -0.0359549448, -0.00416286848, 0.0268259589, 0.0286109559, -0.016026726, 0.0222614668, 0.0333029479, -0.0307019539, 0.0120997317, 0.0121252313, 0.00600842852, 0.00340743223, 0.00976011, -0.0134002296, 0.0158737265, -0.0197369698, -0.0283814576, 0.00541874161, -0.0188572221, -0.0190867204, -0.0197369698, -0.00773286307, -0.00750336377, -0.0126097305, -0.00662999, -0.00561317895, -0.0203489698, -0.0283049569, -0.0133492295, 0.0206677187, -0.0204764679, 0.0101234848, -0.00441149343, 0.00349986972, 0.0102318591, -0.0168427248, -0.0273104589, -0.0113538578, -0.0182324722, -0.00424574362, 0.00684036454, -0.0126671055, -0.00795598794, -0.00330543239, 0.0043828059, 0.00100565469, -0.0226057153, 0.020960968, -0.00958798546, 0.0207187179, 0.0172507241, 0.00456768041, 0.0151342265, 0.0291719548, -0.0057693664, 0.0182324722, -0.0191632211, -0.0246712118, 0.00285918312, 0.0150194773, -0.00364649436, 0.00127659179, 0.0320024528, -0.0169574749, 0.00141923223, 0.015784476, 0.00629211543, 0.00872736145, -0.0207824688, -0.00276515214, 0.0309059527, -0.0136934789, 0.0221212171, -0.00494699227, -0.00438599335, 0.00507130474, 0.00595105346, 0.00404174393, 0.0196349695, 0.00284802681, 0.00736311357, 0.0226694662, 0.00342018227, 0.0114813577, 0.0344759487, -0.03292045, 0.0217387173, -0.0119148567, -0.0217514671, -0.0262394603, -0.0215219669, -0.0144712282, 0.00184077839, -0.0189082213, -0.0161032248, -0.0149047272, 0.00319387019, 0.00673199, -0.0224272162, 0.00416605594, -0.0175312236, 0.0166259743, -0.00478124293, -0.0287639555, 0.0186404716, -0.000409593136, 0.00979198515, -0.0206549689, -0.0111116078, 0.00998323504, -0.0555389151, -0.0315944515, -0.012635231, 0.0199792199, 0.0217769668, 0.0261629596, 0.00421386864, 0.0213562176, 0.00668098964, 0.0114749828, 0.0194947198, 0.0109394835, 0.00820461288, -0.0196604691, 0.0161797255, 0.00161207572, -0.0153892264, 0.0204509683, 0.00580761628, 0.0201832186, 0.00758623844, -0.00909711141, 0.0155167263, -0.00188699714, 0.0172124729, -0.0266474597, -0.00180571596, -0.0118893571, -0.0219937172, -0.0216749664, -0.00678936485, -0.000194835637, 0.00770098809, 0.00994498469, -0.0224782154, 0.0363884456, -0.0192014705, 0.0147134773, -0.00682123937, 0.00904611126, -0.00330224494, -0.00842773728, -0.0199537203, 0.0172379743, 0.0123674814, 0.00414374378, 0.0135277295, 0.00713998917, -1.64977773e-05, -0.00359549443, 0.0401114374, -0.00290221442, 0.0211139675, 0.00514780451, -0.000441069627, -0.00517649204, -0.0219937172, -0.0247732121, -0.0268004593, -0.00753523828, 0.0119531071, -0.0121571068, 0.0227587149, 0.000832733116, -0.0200684685, 0.0124184815, -0.0176969729, 0.0300389547, 0.0147517277, 0.0200047195, 0.00207824679, -0.0095242355, -0.0209992174, 0.0251047108, -0.00526574207, -0.00757348863, 0.0141142281, -0.000571756915, 0.00885486137, -0.0168682244, -0.0339914486, -2.20634429e-05, -0.030574454, -0.0202724691, 0.011653482, 0.0153254764, 0.0272084586, -0.012514106, -0.0294269547, -0.00581717864, 0.0279734582, -0.00828111265, -0.0092118606, -0.0189209711, -0.0163709745, -0.00287671434, -0.0150959771, -0.0259589609, 0.0239062142, -0.00864448678, -0.0244544633, 0.0217132177, -0.0194564704, 0.0033723698, 0.0085424874, -0.0157462265, 0.027182959, -0.000542272639, -0.00660449, 0.0440639332, 0.00470474269, -0.00866361149, -0.0151979765, -0.00210374687, 0.0241357125, -0.00737586385, -0.00282890187, -0.0226439647, 0.00282890187, 0.0153892264, 0.0095242355, -0.00895686168, -0.0300899539, -0.00407999381, -0.00869548693, -0.00352536957, -0.00722286385, 0.0174419731, -0.0147134773, -0.00250218366, -0.012016857, -0.0125842309, -0.0059988657, 0.0149557274, -0.0425594337, -0.00617736578, -0.022503715, -0.0100151096, 0.0204382185, -0.0262139607, 0.0023555588, 0.0110032335, 0.0319769494, -0.0156697258, -0.0186659712, -0.0089887362, -0.00308868289, 0.00828748755, 0.00558130397, 0.00385686918, -0.00282412069, 0.0276419576, -0.00897598639, 0.00959436, 0.0196604691, -0.00394611899, 0.00308230775, -0.00324965129, -0.0224144664, -0.0106908586, 0.016026726, -0.0142034786, 0.0100661097, -0.0434009321, -0.00367836934, -0.0325379521, 0.00771373836, 0.0167534743, -0.000457007118, 0.00180730969, 0.0121124815, -0.00100246724, 0.0172634739, -0.0385049395, -0.00703161443, 0.000191847357, 0.0260099601, -0.00822373759, -0.00652799, -0.00789223798, -0.00089329551, -0.014305478, 0.00821736269, -0.0158737265, -0.0115833571, -0.00238105888, 0.0155422259, 0.00782848801, 0.0261629596, -0.0113666076, -0.0228352156, -0.0106271086, -0.021572968, -0.0246839616, -0.00742686354, -0.00859348662, 0.0562529154, 0.00569605362, 0.00518924231, -0.00856798701, -0.0158992261, 0.00338193239, -0.0187679715, -0.0200812202, 0.0280754566, 0.00408318127, 0.0168172251, -0.00800061319, 0.00844686199, -0.0122399814, 0.00731848879, -0.0042712437, 0.0178499725, 0.0225674659, -0.00189655961, 0.0169829745, 0.0148919774, -0.0180157218, -0.0140887285, 0.00970911048, 0.00552074146, 0.000212566083, 0.00837036222, -0.00814086292, -0.0107099833, 0.0033723698, -0.0295544546, -0.00906523596, 0.016523974, 0.00699973945, -0.0294014551, 0.00116423261, -0.00798786245, -0.00812173728, -0.00547292922, 0.00657899, -0.000409194676, 0.000534702325, 0.00583311589, -0.0139229791, -0.014177978, -0.00353811961, -0.0117363567, -0.00189655961, 0.00213562185, 0.035317447, 0.00177862227, 0.00412143115, -0.0011331545, -0.00519561721, -0.000510397658, -0.021330718, -0.0116789825, -0.00831298716, -0.0296564549, 0.00691048941, -0.00402580621, 0.0125204809, -0.0168809742, 0.00562592875, -0.00529761706, 0.0102446098, -0.0209354684, 0.00266155833, 0.0155804763, -0.0378164425, 0.0201832186, -0.017135974, -0.00218184036, 0.00410868134, -0.0244672131, 0.00194437208, 0.00276196445, -0.00252608978, 0.00300899544, -0.0203107186, 0.00905886106, -0.028483456, 0.00229021534, 0.0117554823, 0.0294524543, 0.204203695, -0.000746272271, -0.0162944756, 0.0224272162, 0.0131962299, 0.0272594579, 0.0107482336, -0.0055111791, -0.0119786067, 0.0113474829, -0.00185990345, 0.0160777252, 0.0146624772, -0.0064164279, -0.00578849111, -0.0165494755, -0.0183854718, -0.0131197302, -0.0108247334, -0.00798786245, -0.00350943208, -0.00676386477, -0.0247987118, -0.0216494668, 0.0152489766, -0.000493264874, 0.00163996627, -0.00225355895, 0.0300899539, 0.0210502185, -0.00371024432, -0.0187679715, 0.0101808598, -0.00419155601, -0.031007953, 0.0148664769, 0.00819823705, 0.00376443169, -0.0064738025, -0.00995136, -0.015478476, 0.0143692279, -0.00150131027, 0.00532630458, 0.0191504713, 0.0152107272, -0.0114112329, 0.00415330613, 0.00492786756, 0.0443699323, -0.027004458, -0.0327674486, 0.0117682321, 0.0343994461, -0.0169192236, 0.00193959079, 0.00189815334, 0.0139102284, 0.000863811176, -0.00611680327, 0.00620286539, 0.0261884592, 0.00301058916, -0.0192524698, -0.00057693664, 0.0486284271, -0.0151214767, 0.0140504781, 0.0178627223, -0.0166259743, 0.0195967201, -0.00282093324, -0.0260864608, -0.0151597271, -0.0116662318, -0.0188317206, 0.00863173697, 0.0340169482, 0.0190867204, 0.0404939391, -0.0141524784, -0.00663636485, 0.0173527244, -0.0216494668, -0.0210884679, -0.0218407158, -0.00909073651, -0.00331180752, 0.000288667536, -0.0168554746, 0.00363374455, -0.0040130564, -0.0124758556, 0.0136297289, 0.0182962213, -0.00794323813, 0.0329459496, 0.0170594733, -0.0165877249, 0.000735116075, -0.0199409705, 0.0068913647, 0.0121124815, -0.000981748453, -0.0170849748, -0.00934573542, -0.0193289705, 0.00604667841, 0.0154529763, -0.0351644456, 0.0180412233, 0.010913983, 0.00932661071, -0.00128456054, 0.0141269788, 0.0140759787, -0.0101362346, -0.0200684685, 0.00313968281, -0.0308039524, -0.00195871573, -0.0306764524, 0.00308708893, 0.00733761396, 0.0054059918, -0.00546974177, 0.00718461396, -0.00617099041, 0.00947961, -0.0353939459, -0.000944295432, -0.0259589609, 0.0163199753, -0.0461039282, 0.00986848492, 0.0130432304, 0.0199792199, 0.0155549766, 0.000767389429, -0.0121061066, -0.00635586539, -0.0258187111, 0.00218662177, 0.0269279592, -0.0200557187, -0.00914173573, 0.0136679793, -0.0106462333, -0.0192652214, -0.0161797255, -0.00526574207, -0.018245222, -0.0101298597, -0.0166132245, 0.0318239518, -0.0022009653, 0.00482586771, -0.0287384558, -0.0297839548, 0.0115451077, -0.0293249544, 0.0167279746, 0.0230519641, -0.0222742166, -0.0334049501, 0.0253852122, -0.160343751, 0.00382818165, 0.0153892264, -0.042227935, 0.0340679474, -0.0135404794, 0.0102701094, -0.00416286848, -0.0262904596, 0.0130942296, -0.0137062287, 0.0192652214, -0.0259717107, 0.00121363881, 0.00777111296, 0.0131197302, -0.012947605, 0.0189974718, 0.00453899289, -0.00249899621, 0.0227204654, -0.0215984676, 0.000143736106, -0.0132727297, 0.00581080373, 0.0108566089, -0.0118001066, 0.0215602163, 0.00366243185, -0.0210884679, -0.0163327251, -0.00993861, 0.0155804763, 0.000129492, 0.0187934712, 0.00406724401, -0.00610724092, -0.00804523751, -0.00417561876, 0.0294269547, 0.0399839394, 0.0275909584, 0.00768186338, 0.000111163892, -0.00717186416, 0.00973461, 0.0311099533, 0.0143692279, 0.00537730427, -0.021572968, 0.000463382108, -0.0344249457, 0.00960073527, -0.0198644698, 0.0233962145, 0.0249517113, 0.00713998917, -0.00386961899, -0.0154529763, -0.00782211311, -0.0457214303, -0.023115715, 0.00938398577, -0.000474139903, -0.014305478, -0.00407361891, 0.00297552673, 0.00729936408, 0.00019124971, 0.00245437119, -0.0197879691, -0.0211139675, 0.0112518575, -0.0182197224, -0.00243524625, 0.008013363, 0.00314924517, -0.0152999768, 0.0119849816, -0.0099577345, -0.0203107186, 0.0415394381, 0.00459636794, -0.0171232242, 0.0289424565, -0.000348433066, -0.00939036068, -0.008013363, -0.015848225, 0.00979836, -0.0116726076, -0.0338639468, -0.0185129717, -0.00258027739, -0.00327993254, 0.00968361, 0.01306873, -0.00318908878, 0.0198134705, -0.00509680482, -0.00697423937, 0.0121889813, 0.000250616809, 0.00213243417, 0.0138337286, 0.0365924425, 0.00468561798, 0.00296596414, 0.0154147269, 0.00656624, 0.000337276841, 0.0103976093, 0.0217642169, 0.0112709831, -0.00737586385, 0.00884211157, 0.000929951726, -0.00320183882, 0.0194437206, 0.0028145581, 0.036362946, -0.0226694662, -0.0188572221, 0.00222327793, -0.0173144732, -0.00980473496, -0.08037588, -0.00919911079, -0.00269821472, 0.0147899771, 0.0067511145, 0.0116279824, -0.021394467, 0.0028018083, -0.0170977246, 0.0254107118, -0.0175312236, -0.0263669603, -0.0050234925, -0.00783486292, 0.0137062287, 0.0092883613, -0.0149429776, -0.0369749442, -0.0169957243, 0.0217897166, -0.00550799165, 0.000106482257, 0.0206677187, -0.0166769754, -0.0336344503, 0.0220319666, -0.023115715, 0.00178499729, 0.016460225, -0.0186404716, 0.00256912108, -0.0239572134, 0.00766911311, -0.0288149565, -0.00137859164, -0.00806436315, -0.00991948508, 0.00450393045, 0.0312374532, -0.0304214545, 0.00432224339, 0.00282571441, 0.0210757181, 0.0173782241, 0.0134512298, -0.00480355509, -0.012883855, 0.0234599635, 0.0236384645, -0.0159884747, -0.0267749596, -0.0261629596, -0.0203489698, -0.0444464311, 0.0238169637, -0.0177352224, 0.0263669603, -0.0275399573, -0.0311609525, 0.0129221054, 0.000639491191, -0.0179774724, -0.0176842231, 0.0178627223, 0.016090475, -0.0309824534, -0.0174802225, -0.00342018227, 0.00747786369, 0.0175184738, -0.0311354529, 0.0162817258, -0.0108438581, -0.000390468165, -0.0389894396, -0.0184492227, -0.0291209556, -0.0146879777, 0.0229244642, -0.0133874798, -0.0215984676, -0.0246967115, -0.000635108387, -0.0229372159, -0.00453261798, 0.0308804531, 0.00329268258, -0.000878951803, 0.00458043069, -0.00979836, -0.00710173929, 0.00790498778, 0.0201194696, -0.00607536593, -0.00414374378, -0.0109394835, -0.00194277824, 0.0109904837, 0.00930748601, 0.0356744453, -0.0277439579, -0.0140504781, -0.0740008876, 0.0204892196, 0.0155804763, -0.00938398577, 0.00256434, 0.0166514739, 0.0285854563, -6.1807521e-05, -0.000939514197, -0.000860623666, -0.0139994789, 0.022503715, -0.0121762315, 0.00317155756, -0.0246967115, -0.0218024664, 0.00193640334, 0.014305478, -0.0228352156, 0.00987486, -0.0135787297, -0.00960073527, -0.00140568533, 0.00142002909, -0.0145094777, -0.0161797255, 0.0129093556, 0.0132854795, -0.015784476, 0.000553030404, 0.0137827294, -0.0150322272, 0.0139612285, 0.010110735, -0.00977286, -0.0146369776, -0.0262904596, 0.015044977, 0.0146752279, 0.0164219756, -0.00390468165, -0.0320279524, 0.0117363567, -0.00439236825, -0.0176077224, 0.0113666076, -0.0249389615, 0.00100007665, 0.00493743, 0.0276929568, 0.00650886493, 0.0016750287, -0.0245437119, -0.00181209098, 0.00441468088, -0.00812173728, 0.0207824688, 0.00947961, -0.00807711296, -0.0245819632, 0.0409529358, -0.00557492906, 0.00821736269, 0.000754241, 0.0193034708, 0.0097537348, -0.00249740249, 0.0114494823, 0.0175439734, -0.0288659558, -0.0223124661, 0.0127244806, 0.0251429621, 0.0231412146, -0.00468243053, -0.00121842, 0.0223252159, 0.00715273898, -0.0029133705, 0.0100406101, 0.0211649686, 0.00307433913, -0.0538559183, 0.0242122132, 0.00770098809, 0.032741949, -0.0102254841, 0.0148409773, 6.74354451e-05, 0.0140759787, 0.00786673836, 0.014305478, 0.01337473, 0.014177978, -0.00827473775, -0.00637180265, -0.0325889513, -0.00268387096, 0.020897219, -0.00179934106, -0.00464418065, -0.012144356, -0.0145987282, -0.0195712205, -0.0084596118, 0.00256593362, 0.00203521573, -0.0333029479, 0.0135532292, 0.00944136083, 0.025461711, 0.0206422191, -0.0245819632, -0.00320024509, -0.0376634412, -0.000196728215, 0.00419155601, -0.00216430915, -0.0258824602, 0.0126734804, -0.00300262053, 0.0164984744, 0.0412844382, -0.00696786446, 0.0221722163, 0.00697423937, 0.0357764438, -0.033787448, 0.0205529686, -0.00150051329, 0.00978561, 0.00789861288, 0.00180571596, 0.00746511342, -0.01337473, 0.00178340357, -0.00232209032, 0.0161924753, -0.0108056087, 0.0573749132, 0.0132599799, -0.00544742914, 0.0142034786, -0.017199723, -0.0303449538, -0.00172921608, 0.010850233, -0.046409931, -0.0137062287, 0.0321299508, 0.0142927282, 0.016702475, -0.0108247334, -0.0418454371, 0.0107801082, 0.000737108232, 0.00359549443, -0.00790498778, 0.00479080528, 0.0155039765, 0.00797511265, 0.00354130706, -0.00828748755, 0.00862536207, -0.00979198515, 0.0355214477, 0.0140887285, -0.025397962, -0.0525299199, -0.0171104744, -0.0200557187, -0.0168172251, 0.00370068196, 0.0246839616, 0.00443380559, 0.011098858, -0.0148282275, -0.0103147347, 0.0333029479, -0.0236257147, 0.0321299508, -0.0199409705, -0.0260354597, 0.00523067964, 0.0208079685, -0.00128695113, -0.00499161752, -0.0355979465\], metadata={'director': 'Christopher Nolan', 'theme': 'Fiction', 'year': 2010}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, hash='7937eb153ccc78a3329560f37d90466ba748874df6b0303b3b8dd3c732aa7688', text='Inception', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.470002413)\]

Use keyword arguments specific to pinecone

In \[ \]:

Copied!

retriever \= index.as\_retriever(
    vector\_store\_kwargs\={"filter": {"theme": "Mafia"}}
)
retriever.retrieve("What is inception about?")

retriever = index.as\_retriever( vector\_store\_kwargs={"filter": {"theme": "Mafia"}} ) retriever.retrieve("What is inception about?")

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"

Out\[ \]:

\[NodeWithScore(node=TextNode(id\_='54f65cf7-a12f-4366-88fe-6239c71920d2', embedding=\[-0.00178836891, -0.0238407217, -0.0128082475, -0.0354147442, -0.00969749317, 0.0257046539, -0.000490778184, 0.000809174, -0.0218256582, -0.0278834421, 0.0238407217, 0.01876528, 0.0284375846, -0.0019048648, 0.00637263851, 0.0153522659, 0.029117668, -0.00807284843, 0.0104090627, -0.000399667391, 0.0102390414, 0.00693307817, -0.0297725648, -0.000678116106, 0.00477633, -0.00108309672, 0.00440165447, -0.0270018522, 0.021548586, -0.0175058655, 0.0120022222, -0.0240674149, -0.00652376842, 0.0020103408, 0.0100942096, -0.003102883, 0.00582164479, -0.0105350045, 0.000989427674, 0.0146092111, 0.0140172858, 0.00744314119, -0.0082617607, -0.0168761574, 0.0058814669, -0.00278488081, 0.0226190891, -0.0117125567, -0.0136142736, 0.0145840226, 0.00707791094, 0.0314853676, -0.0147855291, -0.0302259531, 0.0201254468, 0.00941412523, 0.00496524246, -0.0163472034, 0.00379083841, -0.0177955311, 0.0108057782, 0.00447092252, -0.025578713, 0.0125941476, -0.0018686566, -0.0135638965, -0.000861912, 0.0103209037, -0.0058342386, -0.00435757497, 0.0348606, 0.0251631066, -0.0154530192, 0.0149492528, 0.00702123716, -0.00879071467, -0.0214856155, -0.00305250636, -0.00804766, 0.000632855925, 0.0218508448, -0.0177073721, -0.00333115202, 0.0217878744, 0.0099934563, 0.0230598841, -0.0193068273, 0.0214982089, 0.00187495374, 0.00188125076, -0.0129593778, 0.00383176934, 0.01876528, 0.0132868253, -0.0115110511, 0.0216745269, -0.000614358229, 0.00363656017, 0.0294199288, -0.0106546488, -0.00165927887, -0.000918585632, 0.0035358069, -0.0114102978, -0.0195083339, -0.00600426, 0.0211707614, -0.00399234472, 0.0156545248, -0.00552568212, -0.0258683786, 0.0186015554, 0.033500433, -0.0466739088, 0.0119833313, -0.0086521795, 0.0195839, -0.00707791094, 0.0180348195, -0.0264477096, -0.00722904038, 0.0454396829, 0.0238407217, -0.0179340653, 0.0302259531, -0.011794419, 0.0100375358, 0.000116987823, -0.0132238548, -0.00628762832, 0.057832323, 0.012921595, 0.000734002679, 0.0104090627, -0.00794061, 0.0198609699, 0.000976046431, 0.0234377086, -0.0236895904, -0.0126697123, 0.0276819356, 0.0275056176, -0.0107868873, 0.0101256948, -0.0117440429, 0.0062655881, 0.0233243611, 0.00584053574, 0.0200750716, -0.0208181255, 0.0209818501, -0.0264225211, -0.00228898623, 0.0196846519, 0.027656747, 0.0125248795, 0.00804136321, -0.00896703266, -0.0127074951, 0.0113851093, 0.00890406221, 0.0265232753, -0.00408680085, -0.00670638354, 0.00752500305, 0.0266744047, 0.0238281265, 0.00129877147, 0.00641986681, -0.00307139778, -0.000216855478, 0.0211203843, -0.00954636373, 0.0259943195, -0.00834992, 0.0313846171, 0.020755155, 0.0145210521, -0.0352636129, -0.00930077769, -0.000806025462, 0.0214730222, 0.0350872949, 0.0461701453, -0.00925669819, 0.00767613295, -0.000469525548, -0.00131215272, 0.0153144831, -0.00336893438, -0.000912288553, 0.0190171618, 0.021107791, -0.00843807869, -0.660134852, -0.010950611, -0.0181985423, -0.00915594492, 0.0031107543, 0.0299236942, 0.0122604026, 0.0252890475, -0.0172665752, -0.00546586, -0.0077831829, 0.00976046454, 0.0409813561, -0.00602944801, -0.0479333252, -0.0312082972, -0.0132364491, -0.0130727254, -0.0333493, 0.00524546253, -0.0212211385, 0.0144328931, -0.019999506, 0.0030588035, 0.0107868873, 0.00157977839, 0.0296718106, -0.0221027285, 0.00374990748, 0.00408365251, -0.0148988767, 0.00933226291, 0.0057775653, 0.00890406221, 0.0378076322, 0.00235353131, -0.0246215574, 0.0345331505, -0.00317372521, 0.0228205957, -0.0114291888, -0.00481096422, 0.0171532296, -0.00722904038, -0.0118259043, -0.013186072, 0.0350872949, -0.0310319792, 0.0144832693, 0.00967230555, 0.00419699959, 0.00853883196, 0.000763913733, 0.0138913449, 0.000799334783, 0.00382862077, 0.0299740713, 0.011441783, 0.00047975831, 0.00931966864, -0.00655525364, -0.00471965689, 0.0165864918, 0.00158056547, 0.0137528088, -0.00270459312, -0.00787763949, 0.000251882942, 0.0217626859, -0.0125248795, -0.000144340738, 0.00716607, -0.021813063, -0.0267499685, 0.0238407217, -0.00685751345, 0.0176444, 0.00935115479, 0.0109946905, 0.00558235589, -0.0135764908, -0.000287894334, -0.0245837756, -0.00839399919, 0.0123800468, -0.00789023377, -0.0499987639, 0.026548462, 0.00589406118, 0.000691497407, 0.0327447839, -0.0111143347, -0.00871515, 0.0232613906, 0.0033500432, 0.0185637735, -0.00479207328, -0.00499672815, 0.0186897144, -0.0311075449, -0.00673786877, -0.000324102526, -0.00924410392, 0.00180411164, 0.0212337319, 0.00614909269, 0.00135229656, 0.0282612666, 0.0515352525, -0.0220649466, 0.0358429439, -0.0038191753, -0.00579960505, -0.0136394612, 0.0111836027, -0.0283872075, 0.0263217688, -0.00353895547, -0.000949283887, -0.00137118786, -0.0135890851, -0.00217091618, 0.00221971842, -0.00786504522, 0.0187904686, 0.00678194826, -0.0236518085, -0.0259943195, -0.011529942, 0.0157426838, 0.0203269534, -0.00198515248, 0.0144958636, -0.00755648827, 0.0177325588, -0.00196311274, 0.00245585875, -0.0130349426, 0.0215611812, -0.032089889, 0.0103272, -0.00517934328, -0.00404901849, 0.00737387314, 0.00374990748, -0.031863194, -0.0113347331, -0.021636745, -0.0116432896, -0.0087403385, 0.00227639219, 0.00585942715, 0.00200561807, 0.00613020128, 0.0166116804, -0.024911223, -0.00811692793, -0.0111773061, -0.0176821835, -0.0252134837, 0.0188156571, 0.0073549822, -0.0249238182, 0.00447407085, 0.0153144831, 0.0071156933, 0.00741795264, 0.0120022222, 0.0142817628, -0.0189667866, 0.0218760334, 0.00679454254, 0.00913705397, 0.014646993, -0.00149712933, 0.0239918511, 0.0135387089, -0.00823657215, -0.00208590575, -0.012657118, 0.0203395486, -0.0166620575, 0.0144832693, -5.84447153e-05, 0.0383617729, -0.00668119499, 0.0351628587, 0.0186015554, -0.0223294236, 0.0249364115, -0.00982973166, 0.00349802454, 0.00355469808, -0.0285383388, 0.0107176192, 0.0317120627, -0.00420959387, 0.0162716378, 0.00280062342, 0.0312334858, 0.0403768383, -0.016284233, 0.0207173731, -0.00570514891, -0.00488967774, -0.0108561553, 0.0133246081, -0.0178207178, 0.00437646639, -0.0020008951, 0.00926929247, -0.0217878744, -0.0109883938, -0.0126382271, 0.0182237308, 0.0187526848, -0.0228961594, -0.00295805046, -0.0212085433, -0.0248356592, 0.00207016291, 0.0166998394, -0.00834362302, -0.00388844311, 0.00760686491, -0.00990529731, -0.00469761714, 0.0204151124, 0.00921261869, -0.0383365862, -0.0155033953, 0.0344072096, -0.00220869854, 0.012235214, -0.0033941227, -0.0166494623, -0.0115425363, -0.0152641069, 0.0217878744, -0.00700234575, 0.0131608844, 0.0324929021, 0.0354651175, -0.0153648602, 0.0182741079, -0.0145336464, 0.0174303, -0.013274231, -0.0254275836, 0.0148107177, -0.0199743174, -0.00101461599, -0.0164479557, -0.00161519938, 0.034079764, -0.0160827264, 0.00589720951, 0.000798154098, 0.0237021856, 0.0378328189, 0.010440548, 0.00528639322, 0.00212053955, 0.0201506354, 0.004392209, 0.000456537848, -0.000342403393, 0.00325873564, -0.00704012858, -0.0255661197, -0.0120525993, -0.0048204097, 0.0157930609, -0.016019756, 0.0161205083, 0.00498098508, -0.00228898623, 0.011108038, 0.0047353995, -0.00201978628, -0.0205158666, -0.00111694343, 0.0317624398, -0.00845067296, -0.00582164479, -0.00982973166, 0.0164353624, -0.00968489889, 0.00302731828, -0.00365545135, -0.0119959256, 0.0142691694, 0.00373731321, 0.00655525364, -0.00034771653, -0.00157584273, 0.0176318064, -0.0143447341, 0.000708420819, -0.0318380035, -0.0128397336, -0.00419385126, -0.00564847514, -0.0236014314, 0.0339790098, 0.00140975742, 0.00139480177, -0.00287618837, 0.00929448102, 0.0179718491, 0.0148107177, 0.0134631433, -0.010843561, -0.020666996, 0.00438906, -0.0123359673, -0.0150626, -0.00918743, 0.0205536485, -0.01170626, 0.00908038, -0.0322158299, -0.0364978388, 0.00128539011, 0.100551672, 0.0076950239, 0.0371023566, 0.029470304, 0.00959044322, -0.00697086053, -0.034961354, -0.022808, -0.00160575379, -0.0154278306, -0.00789023377, -0.0355154946, 0.026548462, 0.0201506354, 0.0378076322, -0.00782726239, -0.00848845579, 0.00239446224, 0.0071156933, -0.00527379941, -0.0110576618, 0.0129593778, 0.023538461, 0.0100564267, -0.00931966864, -0.0415858738, 0.0204780828, -0.0080791451, 0.00741795264, -0.0220145695, -0.002152025, 0.00175845786, -0.0100312382, 0.000643088657, -0.00697086053, -0.00627188524, 0.0354399309, 0.0170650706, 0.0244452395, -0.00539974077, 0.0152137298, -0.0252386723, -0.0125437705, -0.0136268679, 0.029697, -0.0181481671, -0.0306289662, 0.011794419, 0.0240044445, -0.0164731443, 0.0249616, 0.015931597, 0.00133025681, 0.00578071363, 0.0296214353, 0.00653636269, -0.00301000127, 0.0154908011, -0.00518249162, 0.0112528708, -0.0230850726, -0.0314601809, 0.00867107, -0.00979824644, 0.0149744414, -0.0182867013, -0.0118070133, -0.00407420658, -0.0101886652, -0.00872774422, 0.00432294095, -0.0130853187, -0.00742425, -0.00199774653, 0.0136268679, -0.00123265223, 0.00179624022, -0.00173484383, 0.0253142361, 0.00420959387, -0.0285383388, -0.0356162488, 0.000809961115, -0.0356414355, -0.00907408353, 0.00743054692, -0.00866477378, -0.00884738844, -0.0112024937, 0.0025755032, 0.00925040152, -0.00304935803, 0.0235762447, -0.0099934563, 0.00670008641, -0.00238659093, 0.00440165447, 0.00107994815, 0.00137984625, 0.00554457353, 0.0293191746, -0.0285635255, -0.0149366586, 0.000657650642, 0.00289507955, -0.00721014943, -0.00810433365, 0.000562800968, -0.0134631433, -0.00444258563, 0.011215088, -0.0265988391, -0.00285887136, -0.0175436474, -0.00551938498, 0.0146847758, 0.0017191011, 0.00440480327, 0.00938264, -0.0166620575, -0.00704642525, -0.0178207178, 0.00882849749, 0.0350369178, -0.00794690661, -0.0108246701, 0.0237147789, -0.0189038161, 0.0138031859, 0.00882849749, -0.0345835276, 0.0134253614, 0.00736757601, -0.011019879, -0.0109883938, -0.0147477463, 0.00065096, -0.00418125698, -0.016687246, -0.000255425053, -0.0204654895, -0.00285572303, -0.000674180454, -0.0182867013, 0.000505340169, -0.023009507, -0.00239603664, -0.00354210404, -0.00848215818, 0.0116873691, -0.0194327701, -0.0180348195, -0.01258785, 0.003014724, 0.00277386094, -0.0405279659, -0.0339790098, -0.0111710085, -0.00398919638, 0.0142313866, 0.0358681306, 0.00542492885, 0.0191682931, -0.00623725168, -0.00611445867, 0.0278834421, -0.00262430543, 0.017568836, -0.00118935981, 0.0448855422, 0.033500433, 0.00123658788, 0.0188660324, 0.00284627732, 0.0152515126, 0.0121218665, 0.0112780593, 0.0110513642, 0.0139669096, -0.0152515126, -0.00924410392, 0.0265988391, -0.0293443631, -0.0174303, -0.00533677, -0.0208810959, 0.00143494562, -0.0255535245, -0.0283116437, 0.0174051113, 0.0246719345, -0.015931597, -0.0135387089, -0.00717236707, -0.000975259289, -0.0285383388, -0.00617428077, 0.00763835059, 0.0145714283, 0.0113536241, 0.017480677, 0.0306037776, -0.00552568212, -0.0282360781, 0.00523916539, 0.0518878885, -0.0163220149, 0.0169769116, 0.0243696757, -0.0156293362, 0.0101886652, -0.0307045318, -0.0150248175, -0.0502002724, 0.00495894533, -0.00146406959, 0.00274080131, 0.00715977279, 0.00113898318, -0.0206292141, 0.0397471301, -0.0162590444, 0.0271277931, -0.0003219379, 0.0217626859, 0.0103775775, 0.0017978145, -0.0151255708, 0.0356918126, 0.00136016787, -0.00503451051, 0.0201128535, 0.00980454404, 0.0138535621, 0.00571144605, -0.00892295316, -0.0165864918, -0.0326440297, -0.0163849853, 0.0214226451, 0.0384625271, 0.00982973166, -0.0116621805, -0.00221656985, 0.00790282711, 0.00456537865, -0.0088222, -0.012235214, -0.0107365111, -0.0404524021, -0.0145714283, -0.0228835661, -0.0137024326, -0.0168383755, -0.00556031615, -0.0381098911, 0.0112339798, -0.0134757375, 0.0147729348, -0.0142691694, -0.0249741934, 0.0401249528, 0.00942671951, -0.00304620946, 0.0282864552, 0.00794690661, -0.0232362021, -0.00743054692, -0.00668119499, 0.024558587, 0.00186235958, -0.00972897932, 0.00603574514, 0.0149114709, -0.0120274108, 0.00771391531, -0.0160575379, -0.0263217688, 0.000515179359, -0.0286642797, -0.0122918878, 0.00736127933, -0.00854512863, 0.0189793799, -0.00596647756, -0.0123044821, 0.00984232593, -0.000263689959, 0.0147603406, -0.0383617729, -0.0258683786, -0.024382269, 0.00380343245, 0.00723533751, -0.0199239403, -0.00366174825, -0.00345079647, 0.0282360781, -0.0118384985, 0.0125122853, -0.0169769116, 0.00324299303, -0.0125122853, 0.0193697978, -0.0116118044, -0.00670008641, 0.00133655395, -0.0222790465, 0.00751240877, 0.00982343499, 0.00937004574, 0.0226946529, 0.0139165325, -0.0146092111, -0.00529583916, 0.0262210146, -0.00963452272, 0.00110592355, -0.00606723037, 0.036069639, -0.0115866158, 0.00264004804, 0.016687246, -0.00507229287, -0.00133734103, 0.00632541068, -0.00833102874, 0.0095085809, -0.0390670449, -0.00413717749, -0.0215233974, 0.0421652049, -0.00665600691, 0.0116306953, -0.0159064084, -0.00922521297, 0.000290846103, 0.0278078783, -0.00492746, -0.0195335224, 0.02584319, 0.0174932703, -0.00266523636, 0.0109002348, -0.00124209782, -0.026372144, 0.00370897632, -0.0399234481, -0.031510558, -0.0381854549, -0.020931473, 0.0465731584, 0.00254716631, 0.00213313382, -0.00150578772, 0.0123044821, -0.0189667866, -0.0243192986, -0.00471650809, 0.0124619091, 0.0173547342, 0.00119172118, -0.000488810358, 0.00799098611, 0.00566421775, 0.00470391428, -0.013450549, 0.0150500061, -0.00780207431, -0.0123737501, 0.0261202622, 0.00628447952, 0.00218351022, -0.00848215818, -0.0153396716, 0.0196720585, -0.011372515, 0.0151633536, -0.0224931464, -0.0109443143, -0.0292184222, -0.0241681691, -0.0107365111, -0.00213313382, -0.012147055, -0.023450302, 0.00256133475, -0.00222286698, 0.000237124186, -0.02274503, -0.00539029529, 0.0163849853, -0.00675046304, -0.00578071363, -0.0148233119, -0.00720385229, 0.0239666626, -0.00531473, 0.00191745895, 0.024029633, -0.011548833, 0.00294388202, 0.0129719721, -0.00381602673, -0.0023440856, -0.000401832018, -0.0262462031, -0.0386640318, -0.0358177535, -0.00359877758, 0.0051636, -0.0115425363, 0.0288909748, -0.0184756145, -0.00942671951, -0.0108939372, -0.0116495863, -0.00454019, -0.00225435244, 0.0316365, -0.032089889, 0.004779479, -0.0248860344, -0.00669378927, -0.016687246, -0.00232047169, 0.000994937611, -0.000473067659, -0.0175940245, -0.0059255464, -0.00125547906, -0.0142313866, -0.017921472, -0.0351628587, -0.0128271393, 0.0394448712, 0.205637231, -0.00084380788, -0.0141558219, 0.0125248795, -0.0168005917, 0.0170146935, 0.0197602175, -0.00168761576, -0.0142313866, 0.00977305882, -0.0100375358, 0.00989270303, 0.0299488828, 0.00680083968, 0.0152767012, -0.0257172491, -0.0226190891, -0.0135261146, -0.0257424377, -0.0113095446, -0.00749981496, 0.00072140852, -0.0133875785, -0.0075942711, 0.0255157426, -0.00113583473, -0.0137779973, 0.012764168, 0.0148359053, 0.0195839, -0.0080791451, -0.022216076, 0.00246687862, -0.00186708232, -0.0335759968, 0.0136772441, -0.0221405104, -0.0191305093, -0.0153900478, -0.00249993824, 0.00232834299, 0.0206795894, -0.00133812812, 0.00267783063, 0.00428515859, 0.0133120138, -0.0220523514, 0.00274552405, -0.0135890851, 0.0159567855, -0.0436261259, -0.0299992599, 0.0233747382, 0.0349865407, -0.0143699218, -0.0165487099, 0.0141306333, 0.0216745269, -0.00676305732, -0.0266492162, 0.0208055321, 0.0235636495, -0.028185701, -0.0241555739, 0.00138535618, 0.0305282138, -0.017833313, -0.0209944434, 0.0406539068, -0.0418377593, 0.0212589204, -0.00503451051, -0.000571853, 0.00635374757, 0.0245208051, -0.022039758, -0.0127074951, 0.0207173731, 0.00787134189, 0.0194453634, -0.0211203843, 0.0113347331, -0.00971638504, -0.00782726239, -0.00340986531, -0.0174932703, 0.00811692793, 0.00602315087, -0.00647968892, -0.0151759479, -0.00873404089, -0.0264980868, -0.0186267439, 0.0123107787, 0.00840659346, 0.0168257803, 0.0124493148, 0.0108813429, -0.0103083095, 0.00115866156, -0.0358681306, 0.0161708854, 0.0196594633, -0.0192186683, -0.0379335731, -0.0144202989, 0.00494635152, 0.046950981, 0.00894814171, -0.0315609351, -0.00229843194, -0.00971638504, -0.0172665752, -0.0117755281, 0.0166494623, 0.00209377706, -0.00646709464, -0.0253268313, -0.00117283, -0.00423478195, -0.000179466602, -0.0123044821, 0.00463779457, 0.00529269036, -0.00279117795, -0.000488810358, -0.000838297943, -0.00101855164, 0.0192438569, -0.027656747, 0.0165235214, -0.0178710949, 0.0148107177, -0.00539659197, -0.00468187407, 0.00970379077, 0.0210448205, 0.013186072, -0.00303991232, -0.0271781702, -0.000307572685, -0.0127578713, 0.0104531422, 0.0103397947, -0.00829324592, -0.000169233856, 0.0107491044, -0.0149996299, -0.0167124327, -0.0148610938, -0.00867736712, -0.0224553645, 0.00493060891, -0.0140172858, 0.025578713, -0.0282864552, -0.013186072, 0.0108120758, -0.0199743174, -0.00246215588, -0.0279338192, 0.00905519165, 0.0208055321, 0.00601685373, -0.0223420169, -0.012235214, -0.157980978, 0.0200498831, 0.0138283735, 0.000615539, 0.0190801341, -0.0269262865, 0.0281101372, -0.00185133971, -0.0297473762, 0.000567917363, -0.00578071363, -0.0132364491, -0.0107428078, -0.00725422893, -0.000154967041, 0.0142313866, -0.0356162488, 0.0271781702, 0.0223546121, -0.00653636269, 0.00685751345, -0.0111017413, -0.023941474, -0.0178710949, 0.00690159295, 0.0122604026, -0.000809174, 0.00726052606, -0.00877182372, -0.00708420807, -0.0172665752, 0.00642616348, -0.00541863171, 0.00958414655, 0.0092189163, 0.00903000403, -0.0153900478, 0.0010933294, -0.00267468207, -0.00887257699, 0.0273544881, 0.0169769116, 0.0178207178, 0.010667243, -0.00611445867, 0.027480429, 0.0177325588, -0.00422533648, 0.026195826, -0.0214730222, -0.0100942096, -0.0167502165, 5.76575803e-05, -0.00504710479, 0.0231606364, 0.0250623524, 0.00243539317, 0.00625929143, -0.00163566484, -0.000493139611, -0.035717003, -0.00788393617, 0.0207425617, 0.00678194826, -0.0135261146, -0.0166242737, 0.00732349651, 0.00408050371, -0.0244074576, -6.83330873e-05, -0.016775405, -0.000772572239, 0.00783985667, -0.036774911, 0.00261013699, 0.00668749213, -0.0205032714, -0.00531473, 0.00756908255, 0.00212211395, -0.0198483765, 0.0224553645, 0.0105287069, -0.0240674149, 0.0279086307, 0.023941474, -0.0164227691, -0.0193320159, -0.0253142361, -0.0284627732, -0.00178364618, -0.0204403, -0.0282612666, -0.00819879, 0.0339286327, 0.003683788, 0.0178836901, -0.0100312382, 0.0118259043, -0.0359185077, -0.0157678723, -0.00438906, -0.0178836901, -0.00142392574, 0.0287902206, 0.0312082972, 0.00820508692, 0.0201758239, -0.00182457711, 0.00847586151, -0.0119455485, 0.0332989246, 0.0236140266, 0.00584998168, 0.00168604148, 0.0135261146, 0.0214352384, -0.0364474617, 0.0260446966, 0.0157174952, 0.0526939109, -0.00152231753, 0.0212715156, 0.0100816153, -0.0029627732, -0.00148925791, -0.0884612948, 0.00619317219, 0.00288878265, 0.0163597967, 0.00840659346, 0.0356162488, -0.0182741079, 0.0363718979, -0.0200876649, 0.00616798364, -0.00573978247, -0.0440039523, -0.0289665386, -0.0204780828, 0.0118762814, 0.00599166565, -0.00760686491, -0.00502191624, -0.0317624398, 0.00162779354, -0.0182363261, -0.00704642525, -0.00609241892, -0.0141054448, -0.0012436721, 0.0159819722, -0.0154782068, 0.00750611164, 0.00373416464, 0.0114291888, -0.00047346123, -0.0147225587, 0.0147225587, -0.00745573547, -0.00136331643, -0.00624354836, 0.0127389804, -0.00948969, 0.0259187557, -0.0372786745, -0.000716292125, -0.0127767622, 0.00295962463, -0.041157674, 0.00393567095, -0.00509118428, -0.0277575012, 0.000203080621, 0.0390922353, -0.0106798373, -0.015931597, -0.012077787, -0.00519508589, -0.0144454874, 0.0138031859, -0.02274503, 0.026019508, -0.0329966657, -0.029293986, 0.0312082972, 0.0198735651, -0.0130601311, -0.0116810715, 0.0248482525, 0.0114165945, -0.00749981496, 0.00362396589, -0.0306289662, 0.0208685026, -0.0113788126, -0.00394826522, 0.00616798364, -0.0328959115, -0.00569570297, -0.0323921479, -0.00321780471, -0.0302259531, -0.00354525261, 0.0208810959, -0.01170626, -0.0183622669, -0.0136520555, 0.00213470799, -0.0313846171, 0.0141684161, 0.0375053696, 0.0181481671, 0.0139920982, -0.00504710479, -0.0189290028, 0.00141448015, 0.00743054692, -0.00664341263, -0.00739276456, -0.000326857495, -0.0043449807, 0.000652534247, 0.00804766, 0.00443943683, 0.00688270153, -0.0236769971, 0.00733609078, -0.0779829621, 0.0072668232, -0.0190423504, -0.0048235585, 0.0224427711, -0.00217406475, 0.0142565751, -0.0210700091, 0.0111458208, 0.013009754, -0.0109757995, 0.0201758239, 0.00600111112, 0.00524861086, -0.0183874555, -0.00733609078, 0.0253142361, -0.000207409859, 0.00653636269, 0.0211329795, -0.0109443143, 0.00330911228, -0.00858291145, -0.0221908875, -0.00908038, -0.0238281265, 0.00421903934, 0.0129593778, -0.0117881224, -0.00452129869, 0.00958414655, -0.0175310541, 0.0244956166, 0.0181229785, 0.0062089148, -0.0301252, -0.00455278438, -0.0115551306, 0.0216241516, 0.00993678253, -0.0137654031, -0.0131356958, 0.0172917638, -0.0111899, -0.0277826898, -0.00118227559, -0.0240800101, 0.00169706135, 0.0137024326, 0.0134253614, 0.0172539819, 0.00474169664, -0.0233243611, -0.0131105073, 0.0125374738, -0.0108813429, 0.021284109, -0.00578386197, -0.002152025, -0.016372392, 0.0230346955, -0.00352006429, -0.0204780828, -0.00971638504, -0.00105082418, 0.0141306333, -0.014735152, 0.0146218054, -0.000872144708, -0.0107491044, -0.019558711, -0.00532417558, 0.00207016291, 0.0188660324, -0.00317057665, -0.00659933314, 0.0234628972, 0.0107365111, 0.0052989875, 0.00190329051, 0.0293947402, 0.0120274108, -0.0225183349, 0.0330974199, 0.0350872949, 0.040049389, -0.00555087067, 0.0142691694, 0.00101776456, -0.00188597362, -0.0099871587, 0.0181733556, 0.0124870967, 0.0116243977, -0.0177073721, -0.00137748488, -0.026019508, -0.0131986663, 0.0129719721, 0.0335759968, -0.0114858625, -0.00201348937, -0.011372515, -0.0129971597, -0.0153522659, 0.0315861218, -0.0244956166, -0.024470428, -0.012165946, 0.0120148165, 0.0287650321, 0.0267499685, -0.0197224356, 0.000262115704, -0.0363215208, -0.00722904038, -0.00586572429, -0.0383869596, 0.00227954076, -0.00106656691, 0.00201821211, 0.0224427711, 0.0357925668, -0.0141432276, -0.00178836891, -0.00232834299, 0.0212589204, -0.0189541914, -0.0062529943, -0.0108309668, 0.0195713043, -0.014735152, -0.0115740215, -0.00742425, -0.00937634241, 0.0027171874, -0.00697086053, 0.0214352384, -0.0291932337, 0.034608718, -0.0071156933, 0.00630651927, -0.00251253252, -0.0174051113, -0.00970379077, -0.0190045685, 0.009647117, -0.0281353258, -0.0249364115, 0.0237903446, 0.0124808, 0.0306793433, -0.0116999634, -0.0102894185, 0.00664341263, -0.00361452019, 0.000895758742, 0.0118888747, -0.0155915543, 0.0107994815, 0.0157930609, 0.0234377086, -0.0067882454, 0.0224679597, -2.76726882e-06, 0.0270270407, 0.0114732683, -0.0129971597, -0.0561195202, -0.00363656017, -0.0181481671, -0.019911347, -0.0036774911, 0.0134127671, -0.00692678103, 0.011460674, 0.00887887366, 0.00770132104, 0.0271277931, -0.0433994308, 0.0227576252, -0.0274552405, -0.0073549822, 0.0383617729, 0.0133372024, -0.00533047272, -0.0162590444, -0.0255031493\], metadata={'director': 'Francis Ford Coppola', 'theme': 'Mafia', 'year': 1972}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, hash='bfa890174187ddaed4876803691ed605463de599f5493f095a03b8d83364f1ef', text='The Godfather', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.475807905),
 NodeWithScore(node=TextNode(id\_='640b7827-e53a-4afc-8830-40d0ad7c5824', embedding=\[-0.00646311697, -0.0191921256, -0.0201491471, -0.0353321359, -0.0191533286, 0.0294606909, -0.0100357747, -0.0118140215, -0.0417208895, -0.0135405371, 0.00920808222, 0.0163469333, -0.00118657516, -0.0230848696, 0.00523127709, 0.00842565391, 0.0374789648, -0.0339871347, -0.012441257, -0.0105983475, 0.00869077444, 0.0176660679, -0.0289692469, -0.0133077484, -0.0113743097, 0.0122537334, 0.0123959929, -0.0400137715, 0.0199292898, -0.00394124025, 0.0184032321, -0.0035338602, -0.0168254431, -0.00741043687, -0.0225546286, 0.00227777171, -0.0112320501, -0.0152605856, 0.0129003683, -0.00406410079, 0.00135550858, 0.0090334909, -0.0096413279, -0.0383325219, -0.01394145, 0.00152363372, 0.0131654888, -0.0255808812, -0.0265896302, 0.0103655588, 0.0208733771, 0.0071776486, -0.0068284655, -0.0330301151, 0.0127969068, 0.0131072914, 0.0101780351, 0.00641785236, 0.00280962908, -0.00893649552, 0.00335926889, 0.00205791579, -0.0302107874, -0.00430982234, 0.0074492353, -0.00782428309, -0.0269258805, 0.00603957102, -0.0150407301, -0.00648898212, 0.0252575632, 0.0210673679, -0.00546729891, 0.007720822, 0.0129714981, -0.0124606565, -0.024520399, 0.00909815449, -0.00347566302, -0.00153737469, 0.00856791344, -0.00577445049, -0.0210544355, 0.0167737119, 0.0169418361, -0.00308929873, -0.00559339253, 0.0211191, -0.00462020701, -0.00612686668, -0.00609453488, 0.0225287639, 0.0147691434, 0.0123959929, -0.0230460707, 0.0206535216, -0.0210932326, 0.0341423266, 0.0316592492, -0.0270810742, 0.00150665955, 0.00998404436, -0.0137215946, -0.00971245766, -0.0177824628, -0.0103978906, 0.0219985228, 0.0110121937, 0.00962839462, -0.00770788919, -0.00199486897, 0.00706772041, 0.0281415544, -0.0481613725, 0.00397357205, -0.0230331384, -0.00548669789, -0.0107341409, 0.0115230354, 5.82981847e-05, 0.00548669789, 0.0352028087, 0.0101392362, -0.0221149176, 0.014549287, -0.0142389024, 0.0057550515, -0.0094861351, 0.00568392174, 0.0016392197, 0.0605250336, 0.0192955881, 0.014795009, 0.00608483516, 0.00232465286, 0.0437125266, 0.0030133191, -0.00215491117, -0.0189464055, -0.028529536, 0.00200618501, 0.0232529938, -0.00498555601, -0.00699012447, 0.0017636969, -0.00828986056, 0.0205241945, 0.0102556311, 0.0180799142, 0.00251541, 0.0110768573, -0.0222183783, -0.00723584555, 0.0152217876, 0.0134112099, 0.0253351592, -0.00057712174, 0.00224705669, -0.00848385133, 0.000382727099, 0.0220373198, 0.0197999626, 0.0100681065, -0.00875543803, 0.0156356338, 0.0319954976, 0.0307798255, 0.0100745736, 0.0170323662, -0.0122601995, 0.0033172376, 0.0247790534, -0.00515691424, 0.0168642402, -0.0162564032, 0.0475664698, 0.0122860651, 0.0311160758, -0.00985471718, -0.00131913542, -0.0189981367, 0.03323704, 0.0338319428, 0.0392378122, 0.00192050589, 0.00820579845, 0.00316366181, -0.00014205763, 0.0105595496, 0.00750096608, 0.0216105413, 0.0230072737, 0.0131008253, 0.0120015452, -0.653049588, -0.0331594422, -0.0157390963, -0.0109151984, -0.0055319625, 0.00437448593, 0.00901409145, 0.0248695817, -0.0012302231, 0.00696425885, -0.00224544, 0.0103526264, 0.0394705981, -0.017265154, -0.0365995392, -0.0239772256, -0.000944087107, -0.0151700573, -0.0184420291, 0.00901409145, 0.00233920198, 0.0216234736, -0.0057712174, -0.0234340522, -0.000793744461, 0.00452321162, 0.0339354053, -0.0372720398, 0.011102723, 0.0211449638, -0.00914341863, 0.0217269361, 0.0291244406, 0.0255032834, 0.0335991532, 0.00519247912, -0.00788894668, 0.0253222268, -0.000455473521, 0.0409190618, -0.00597490743, -0.00120597426, -0.00416756235, 0.00757856201, -0.0027029342, -0.00731344195, 0.0557140708, -0.0210027043, 0.000950553454, 0.0213518869, -0.00192212255, 0.0112191169, -0.00719704758, 0.00755916303, -0.00180087844, 0.0160624124, 0.0132689504, 0.0173686165, -0.0115683, 0.012402459, -0.0116911605, -0.000691495312, 0.0206405893, -0.0100681065, -0.00293733948, 0.00502112089, 0.00611716695, 0.0276242476, 0.00893649552, -0.036185693, 0.0035888243, 0.012441257, -0.0283484776, -0.0307280943, 0.0330042504, 0.0113678435, 0.0327714607, -0.00260917214, 0.003566192, 0.00759149482, -0.0129650319, -0.00603633747, -0.0146268839, -0.0130167622, 0.0261499193, -0.0134112099, -0.0363150202, 0.00148806872, 0.0183644332, 0.0187006835, 0.0243910719, -0.00481419731, -0.00054438581, 0.00912402, -0.0100745736, 0.00558692636, -0.00431305543, 0.0023586012, 0.0170194339, -0.0414363705, -0.0093374094, -0.00441651698, -0.00843858626, -0.0165926535, 0.0188946743, -0.00519247912, 0.0129262339, 0.0150148645, 0.0418502167, -0.0192309245, 0.0345303081, -0.00106290623, -0.00253642583, 0.0158554893, 0.00527007505, -0.0233176574, 0.026667228, 6.12787699e-05, 0.036703, -0.0102685634, 0.00198840257, 0.00318629388, 0.0130749596, -0.00350476173, 0.0307798255, 0.00719058095, -0.008917097, -0.0138379885, 0.00017802669, 0.0111932522, 0.00594580872, 0.00350152841, 0.02917617, -0.00460080802, 0.0234211199, -0.000881040178, 0.0154933743, -0.0192179922, 0.037168581, -0.0255550146, -0.00525067607, -0.00984825101, -0.00345626404, 0.0190110691, -0.00502758706, -0.0377117544, -0.020343136, -0.0196189061, -0.0194249153, 0.0065568788, 0.00783075, 0.00647604931, -0.0214036182, -0.0095314, -0.0135922674, -0.013656931, -0.0157132298, -0.0057550515, -0.0273397267, -0.00128599536, 0.00671853777, 0.0105142854, -0.0263051111, -0.000367773639, 0.0123507287, 0.00315557886, 0.0194637123, 0.00722937938, 0.0155839035, -0.0290985741, 0.0170840956, -0.0142518356, -0.00114454399, -0.00872310624, -2.15839682e-05, 0.00648251595, 0.00617536437, 0.00472043548, -0.00026107888, -0.0181316454, 0.00793421175, -0.00111221219, 0.000980460318, -0.00419019489, 0.0190240014, -0.00869077444, 0.0239772256, 0.0210285708, 0.00846445188, 0.0111867851, -0.00924041402, 0.0155063067, -0.0144975567, -0.0111673865, 0.00407380052, 0.0303142481, -0.00192535564, 0.018558424, 0.00296805473, 0.0252575632, 0.00537677, -0.00699012447, 0.0170194339, -0.0115295015, -0.00565805612, -0.00646958314, 0.00120435772, -0.036185693, -0.0183644332, -0.00622062851, 0.00586174615, -0.00832219236, -0.0177307315, -0.0150019322, 0.000859216263, 0.0197223667, -0.0256196782, 0.0112643819, -0.0349182896, -0.037168581, 0.0083674565, 0.012033877, 0.000223493218, -0.0127775073, 0.0193731841, -0.01523472, 0.00406410079, 0.00159395521, 0.00586174615, -0.0264732372, -0.00622709515, 0.01422597, -0.00527977478, 0.00873603858, 0.00894942787, -0.00693839369, -0.00823166315, -0.0333922319, 0.02845194, -0.0226451568, 0.0129068345, 0.00376018253, 0.0320989601, -0.0394705981, 0.0117364256, -0.00589084486, 0.00141370576, -0.0124735888, -0.01523472, 0.0101327701, -0.027313862, 0.00909168832, -0.00872310624, 0.0165150575, 0.0322282873, -0.0107212085, 0.0141095752, 0.0108958, 0.0162952021, 0.0314005949, 0.010294429, 0.00067209627, 0.0109669296, 0.00332047069, 0.0044132839, 0.00418372825, 0.00208701449, 0.0256196782, -0.0057259528, -0.012033877, -0.0091886837, -0.00733284093, 0.00725524453, -0.0206793863, 0.0103914244, 0.000466789643, -0.014872605, 0.0105272178, 0.0125576518, -0.00725524453, -0.0335474238, -0.00336573506, 0.0225416962, 0.00460404111, -0.0125835165, -0.0130555602, 0.00471396931, -0.0170065, 0.0182997696, 0.0151829896, 0.00968012586, -0.00160769629, 0.0132689504, -0.00853558164, 0.00512781553, -0.0193214528, 0.024520399, -0.0245850626, 0.0073263743, -0.0236021765, -0.00469133677, -0.0083674565, 0.0114066415, -0.00694486, 0.0226839557, 0.00284842704, -0.00228100503, -0.0279863626, 0.0282191504, 0.00256229122, 0.00936974119, -0.0128421709, -0.0126158483, -0.0162822697, -0.00339806685, 0.0035726584, 0.00135065883, -0.00744276866, 0.0103073614, -0.00781781692, 0.0071000522, -0.0236021765, -0.0295641515, 0.0234728511, 0.106358521, 0.00874250475, 0.0117622903, 0.0222701095, 0.00983531866, -0.000851941586, -0.0310384799, -0.0223347731, 0.0110186599, -0.0105789481, -0.000451836211, -0.00180087844, 0.00715824915, -0.0013708662, 0.0207569841, -0.000368986104, -0.00907875504, -0.0284260735, -0.000753733912, -0.00953786634, -0.0147562101, 0.00686079729, 0.0168125089, -0.00742336968, -0.0205629934, -0.0346855, 0.00340130017, -0.0117234923, 0.0167995766, -0.0300038643, -0.00331400428, 0.00205144961, -0.00372138433, -0.00242649787, -0.00397680514, 0.0132430848, 0.0311419405, 0.00429365644, 0.0281415544, -0.00937620737, 0.0218433309, -0.0174462125, 0.0093050776, -0.0107600065, 0.0352545381, -0.0175755396, -0.0305211712, 0.013010296, 0.0118010882, 0.00134015107, 0.0206793863, 0.0159460194, -0.000313820055, 0.00641461927, 0.0194378477, 0.020912176, -0.00771435536, 0.0181187131, 0.00952493306, 0.019088665, -0.00694486, -0.0406345427, -0.00142987166, -0.011995079, -0.000345949724, -0.029383095, -0.00511164963, -0.0140190469, -0.0183385685, -0.012564118, 0.00045102791, -0.00928567816, 0.0044423826, -0.0108505348, 0.00805707183, -0.00311678066, 0.0283743441, -0.0255420823, 0.0216752049, 0.00307959924, -0.0277794395, -0.0282967482, 0.0032784394, -0.0377893485, 4.56433372e-05, 0.0252187643, -0.00642108545, -0.0224641, -0.0166055858, 0.0162952021, -0.0057712174, 0.00980945304, 0.0129003683, -0.0326162688, -0.0017798628, -0.011671762, -0.0159460194, 0.0192309245, -0.00150504289, 0.0203560703, 0.0229555424, -0.0109863281, -0.016127076, 0.00981591921, 0.0112708481, -0.00380221382, -0.00367612, 0.032952521, -0.0492218547, -0.00641138572, 0.0214682817, -0.00279023, 0.0204207338, 0.00246044621, -0.00632732362, -0.0148079414, -0.00714531681, -0.0023036371, 0.0137733249, -0.0336508863, -0.0175626073, -0.0179764535, -0.00136924954, 0.045755893, -0.0203690026, -0.00290500768, 0.00572918588, -0.0177048668, 0.0117946221, -0.00904642325, -0.0377893485, 0.028167421, -0.0111803189, -0.00243296404, -0.012079142, -0.00209671399, -0.0123507287, -0.00356295891, -0.0213518869, -0.0170582309, 0.00591671, 0.0217916, -0.00360175688, -0.0293054972, 0.00352092762, -0.0236409754, -0.00099015981, 0.00536707044, -0.022735687, 0.0232400615, -0.0273397267, -0.0264861695, 0.00857438, 0.0223606378, -0.0149114029, -0.0250894371, -0.0423933901, 0.00838039, 0.0110057276, 0.0158166923, 0.0147820758, -0.0174850095, 0.0127322432, -0.00601047231, 0.000381514634, 0.0289175175, 0.00898176, 0.00666680699, -0.00360175688, 0.0173298176, 0.0333405, 0.011225583, 0.0127128437, 0.0132948151, 0.0277794395, 0.0253092945, 0.01422597, 0.0131978206, 0.0198646262, -0.0094538033, -0.00766909122, 0.02155881, -0.0250247736, 0.00757856201, -0.0298745371, -0.0123377955, 0.0280639585, -0.0129973637, -0.0096413279, -0.00181057793, 0.032952521, -0.0168383755, -0.00244266377, -0.000541960937, -0.00368905254, -0.0237832349, -0.00390244229, 0.00192212255, 0.00376988202, 0.010456088, 0.0412294455, 0.0151700573, 0.0122472672, -0.0240548216, 0.0113355117, 0.0314005949, 0.00407380052, 0.000345545588, 0.00248307828, -0.00527330814, -0.00118980836, -0.0243134759, -0.0187524147, -0.0370651186, 0.00380868, 0.013695729, 0.000246125448, 0.0180152506, -0.00518277939, -0.0189852025, 0.0157778934, -0.0271845348, 0.0241453499, 0.00615919847, 0.015195922, 0.0302107874, 0.00448118057, 0.00398327177, 0.0372461751, 0.00647604931, 0.00688666245, 0.012441257, -0.00186069217, -0.00347243, 0.010333227, 0.00536383735, -0.00633702287, -0.0193214528, -0.0123507287, 0.0141613064, 0.0125253201, -0.00634995569, -0.0200715493, -0.00951200072, -0.023990158, 0.00512458244, -0.00493705831, -0.0120597426, -0.014795009, -0.0155192399, -0.0202914067, 0.00839978829, 0.00142178871, -0.00831572618, -0.00473983446, -0.0244298708, -0.00164002797, -0.00538970251, 0.00179441215, -0.0187394824, -0.014549287, 0.0359011739, 0.00622062851, 0.0113419779, 0.0103590926, -0.0112643819, 0.00142663845, -0.0104625542, -0.00407380052, 0.0271845348, 0.00672500394, -0.0153252492, 0.00124558061, 0.017679, -0.0192955881, 0.0153252492, 0.00169903343, -0.0338578075, -0.00072544365, -0.015842557, -0.00936974119, 0.0252575632, -0.00124153914, 0.00993231311, -0.0155580379, -0.0249083806, -0.00980298687, -0.00310869771, 0.0129391663, -0.0158942882, -0.034452714, -0.0181187131, -0.0165021252, 0.0119239492, -0.0167478472, -0.0148855373, 0.00108392187, 0.0532309934, -0.0406604074, 0.00307151629, -0.0241712164, 0.00895589497, -0.00360175688, 0.0202526078, -0.00677673472, -0.0256714094, 0.0134112099, -0.010171568, -0.0151441917, -0.0247014575, 0.00397033896, 0.0133206807, -0.0119304154, -0.0109151984, 0.00530564, 0.022658091, 0.00351769431, 0.00537030352, -0.0282450169, 0.0353062712, -0.00825106259, 0.00430982234, 0.0331077129, -0.0324869417, -0.00902055856, -0.00937620737, -0.0226839557, -0.00817993283, -0.0285812672, -0.00274496549, -0.0209251083, 0.051420413, -0.0241194852, -0.00599430641, -0.0101133715, -0.0118786851, -0.00532180583, -0.00345949712, -0.00571948662, 0.00153414148, 0.0107988045, 0.0198904928, -0.00778548513, 0.00253480906, 0.00451351237, -0.00110170431, 0.0012431558, -0.0140061136, -0.0343751162, -0.0287364591, -0.016372798, 0.0233952533, 0.011995079, -0.00555459457, -0.0251929, -0.00148887711, -0.0388756953, -0.029667614, -0.013210753, 0.0129714981, 0.0126481801, 0.00615919847, 0.0158942882, 0.0210544355, 0.00577445049, 1.80097941e-05, -0.0124671226, 0.00504698604, -0.018196309, 0.00349829532, 0.0286071319, 0.0279604979, -0.0070224558, -0.00591347693, -0.00277891383, 0.00524744298, -0.0318144411, 0.0147174122, -0.016372798, -0.00384747819, -0.0116394302, -0.00253965892, -0.00741690351, -0.00355649251, -0.00540263532, -0.0220631864, -0.0167219806, 0.00305373385, -0.00785661489, 0.00041910031, 0.00480126496, 0.0296934787, 0.00512458244, -0.00280639576, 0.0122020021, -0.00457170932, 0.0046687047, -0.00231495337, 0.0266413614, 0.0076432256, -0.00853558164, 0.00333017018, 0.00603310438, -0.00143067993, 0.00422899285, -0.00118900009, -0.0316075198, -0.0398327149, -0.0194766466, -0.0154157784, 0.0043033557, -0.0043809521, -0.00437448593, -0.0143164983, 0.00684786448, -0.020058617, -0.0323834792, -0.00611716695, 0.0248695817, 0.0436607935, -0.02917617, -0.00374078332, -0.0188300107, -0.0112579148, 0.0107664727, -0.00884596631, 0.0108246701, 0.00431628851, -0.00661507575, -0.00985471718, 0.00378604792, 0.000181057796, -0.02845194, -0.0156356338, -0.0217269361, 0.0162176061, 0.208061278, -0.00662154239, 0.00787601434, 0.014872605, -0.0181833766, 0.0075656292, 0.0301590562, 0.00282902806, -0.0162176061, 0.00163113675, -0.00283226138, -0.00673793675, 0.0158554893, 0.0123571949, 0.00633379, -0.0192697234, -0.0299004018, -0.0256972741, -0.0122601995, -0.0262533799, 0.00307636592, 0.0178471263, -0.0163081344, -0.00284196087, 0.00929214526, 0.0037828146, 0.000947320252, 0.00969305821, 0.00226807222, 0.0284260735, -0.0135276038, -0.00268515176, -0.000569038792, -0.00133691786, -0.0170452986, 0.0126675796, -0.0117040938, -0.00263665407, 0.000984501792, -0.00660537649, -0.0259300638, 0.00102410815, 0.00210156362, 0.00818639901, -0.0155968359, 0.0246367939, -0.0271328036, 0.0240289569, -0.0126740457, 0.0272621308, -0.0397292525, -0.0119756805, 0.0337026156, 0.0301590562, 0.0142777, 0.00505021913, 0.0340647325, 0.00659567676, -0.0136310654, -0.0282191504, 0.0227227528, 0.0304953065, -0.00870370679, -0.0115683, -0.00605897, 0.0243005436, -0.0279087666, -0.0221795794, 0.0393671393, -0.0368581936, 0.00632732362, -0.00279507972, -0.00845151953, -0.00416432926, 0.00232465286, -0.0229038112, 0.0163598657, 0.0114907036, -0.00588437822, 0.0284260735, -0.0164115969, 0.00478833215, 0.0067508691, -0.00115343521, -0.00938267354, -0.0314523242, 0.0080700051, 0.0105078183, 0.00181704434, 0.00618829671, -0.00551902968, 0.00562895741, -0.0091822166, -0.00142017205, 0.00720998039, 0.0214165505, 0.0127387093, 0.0344009809, 5.44587892e-05, 0.00455877651, -0.0359270386, 0.00536060426, 0.00793421175, -0.0194895789, -0.019411983, -0.0144716911, 0.00761736, 0.019334387, 0.0114454394, -0.015157124, -0.0021823931, -0.0365478098, -0.00976418797, 0.00557399355, 0.0127451755, 0.0120597426, -0.0102814967, -0.0273914579, 0.0017798628, -0.00134015107, 0.000303110166, -0.00462020701, -0.00995171256, 0.0101780351, 0.00534443837, 0.00467193779, -0.0114131076, -0.0020385168, 0.0238996297, -0.0274949204, -0.00376341562, -0.0241453499, 0.0170582309, -0.00408673333, -0.00779195176, 0.0065407129, 0.0183385685, -0.00781781692, -0.00475923344, -0.0113355117, 0.00511811581, -0.0468163751, 0.00257845712, 0.00106533116, -0.0180411171, -0.0139155854, 0.0369099267, -0.0156873651, -0.0177178, -0.0216881372, -0.0284260735, -0.0256714094, -0.00753329787, -0.0247402545, 0.0172392894, -0.0227615517, 0.00159233867, -0.0146527486, -0.00570655381, 0.00358235789, -0.043324545, 0.0104690203, 0.0110445255, 0.00619153026, -0.0251670331, -0.00138864864, -0.163986638, 0.0176531356, 0.0333663672, -0.00425162492, 0.0290985741, -0.000689474575, 0.0433762744, -0.00532503938, -0.0278311707, -0.00329622184, 0.00641785236, 0.00132075197, -0.0140707772, -0.00396063924, -0.0185972229, 0.0162952021, -0.0180152506, 0.0175626073, 0.0185325593, 0.0071776486, 0.0122731319, -0.0117493579, 0.0056774551, 0.012156738, 0.0065568788, 0.0132430848, 0.00722937938, -0.00982885156, -0.0253868904, 0.0012205235, -0.0137086622, 0.0129327, -0.0135146715, 0.00516338041, 0.0276242476, 0.008167, -0.019696502, -0.00375048304, 0.00742336968, -0.000839008891, 0.0271069389, 0.00452644518, 0.0219467916, 0.0126805119, -0.00922101457, 0.037685886, 0.0191015974, 0.0161788072, 0.0187653471, -0.0500754155, -0.0210285708, -0.0192826558, 0.0277277082, 0.001367633, 0.0314781927, 0.0121308723, -0.00343686505, 0.00475276727, 0.00512134936, 0.000252389727, -0.0204078, -0.014588085, 0.0119627472, -0.00827046111, -0.0248954464, -0.0120080123, -0.0102620972, 0.0227486193, -0.0045749424, -0.00137248274, -0.0310902111, -0.0182221737, 0.0210027043, -0.0313488655, -0.00624326104, 0.000182775417, -0.0127516417, 0.00193828833, 0.00588114513, -0.0100487079, -0.0157261621, 0.0325645395, 0.0112385163, -0.00587144587, 0.0401431, 0.00534767145, -0.02212785, -0.0186230876, -0.015195922, -0.0366512723, 0.0073263743, -0.0312971324, -0.0203302037, -0.036392618, 0.0087619042, 0.0206147227, 0.0105789481, -0.0115618333, 0.0107212085, -0.0334439613, -0.00933094323, -0.0217269361, -0.00147432776, -0.00324772415, 0.0290209781, 0.0171487592, 0.0090658227, 0.000831734273, -0.00411259849, 0.0122601995, -0.0479027219, 0.000384747807, 0.0201620795, -0.00790188, 0.000728676794, 0.0216105413, 0.014872605, -0.052920606, 0.0264344383, -0.00124800554, 0.0586627275, 0.0151183261, -0.00407056743, 0.0314264596, 0.0226063598, -0.00761089381, -0.0711815804, 0.0177178, -0.0105272178, 0.00424839184, 0.0137086622, 0.0316333845, -0.013333614, 0.0300814603, -0.01872655, 0.01661852, 0.00186392537, -0.0219467916, -0.0320730954, -0.0188558772, 0.0195542425, 0.0228262153, 0.00489179371, -0.0143940952, -0.0013102442, 0.0288657863, -0.00354679301, -0.00405440154, -0.0280122273, -0.0244686678, 0.000990968081, 0.00401237, -0.0294348244, 0.0228003506, 0.0205500592, 0.00613009976, -0.00514721451, -0.0165667888, 0.00161658751, -0.0237444378, 0.00811526924, 0.0113225784, 0.0117816897, 0.00194637128, 0.0258654, -0.0501788743, -0.0166702494, 0.000330390059, 0.0169547703, -0.040117234, 0.0235633794, 0.000763433462, -0.0221149176, 0.00257199071, 0.0487562791, -0.00830279291, -0.0132948151, 0.00956373196, -0.0179635193, -0.0323317498, 0.024597995, -0.0101133715, 0.00186392537, -0.0301331915, -0.00982238539, 0.0484458953, 0.0118786851, -0.0184549633, 0.00147675269, 0.0169935673, 0.00856144726, -0.0157908257, 0.0182609726, -0.0124994544, 0.0280380938, -0.0154157784, 0.00220340863, 0.021882128, -0.0131654888, -0.0133206807, -0.0133853443, -0.0100163762, -0.0305729024, 0.0148855373, 0.00353062712, -0.0174332801, -0.0159589518, -0.0197352991, -0.0172780864, -0.0144975567, 0.0266154967, 0.00812820159, 0.0191403963, 0.0258007366, -0.00637905439, -0.0025590579, 0.0185842905, 0.0194895789, 8.71441662e-05, -0.0129003683, 0.000590054435, 0.0199939534, -0.00416109618, 0.0143682295, 0.0147044798, 0.0107276747, -0.0228132829, -0.00942147151, -0.0706642717, 0.0178859234, -0.0133594787, -0.0242488123, 0.0150277968, 0.00590701075, -0.0014508873, -0.0163469333, 0.00726171117, 0.0103849582, -0.0118722189, 0.02974521, -0.0235504471, -0.00511164963, -0.00136035832, -0.00811526924, -0.0145622203, 0.00269323471, 0.0096089961, 0.0295124203, -0.00432275515, -0.00630469108, 0.0282708816, 0.00343363173, -0.00706772041, -0.0114454394, -0.0133982766, 0.0307539608, -0.0147820758, -0.00764969178, 0.00944087096, -0.0262921788, 0.0145622203, 0.0109927952, 0.0269776117, -0.017872991, 0.00957019813, 0.00624649413, 0.0206923205, 0.0172522217, -0.0186360199, -0.00135389203, 0.0128227714, -0.0341681913, -0.012156738, 0.0220761187, -0.0231366, 0.00936974119, 0.0197094344, 0.0153252492, 0.0310643446, 0.0225675609, -0.0166702494, -0.00828339439, -0.00380868, -0.0323058851, 0.0386946388, -0.00736517273, 0.00373431714, -0.0314523242, 0.0218303967, 0.0125253201, -0.0209639072, -0.0134241423, -0.00967366, 0.00688666245, 0.00630469108, 0.0139026521, 0.0129391663, -0.0331335776, -0.0204853974, -0.00171843253, -0.00109766296, 0.00763675943, 0.000888314797, 0.00109281309, 0.0138767874, 0.0216234736, -0.0138509218, -0.00824459642, 0.00184775947, -0.0100551741, -0.0113161122, 0.0136827966, 0.0249730442, 0.0152088553, -0.0110833235, -0.0128292385, 0.0180799142, 0.00158102252, -0.0090334909, -0.00191727281, 0.000899630948, 0.0109604634, -0.0125899836, -0.0105142854, -0.0318144411, -0.00589084486, 0.0362115614, 0.0133077484, 0.0126093822, -0.0121244062, -0.0057712174, -0.0120726749, -0.0147820758, -0.00189787371, -0.00256875739, -0.0214036182, -0.00422899285, -0.0088782981, 0.0102556311, 0.0127193099, -0.00461697392, 0.00191565615, -0.0273655932, 0.0180281829, 0.00139269012, -0.0201750118, -0.008167, 0.025813669, 0.0181187131, 0.0155063067, 0.0312195383, -0.0303401146, -0.000688262109, 0.000625619374, 0.0196059737, -0.0312195383, -0.000596924918, -0.023990158, 0.00437448593, -0.0248307828, -0.0168642402, -0.00288237538, -0.0203560703, 0.00166670175, -0.0100163762, 0.00807647128, -0.0188300107, 0.0423933901, 0.00610100105, -0.00312001375, -0.000750904903, -0.0207440499, 0.00562895741, 0.000388385146, 0.0043033557, -0.0370133854, -0.0119239492, 0.00311354757, 0.0147174122, 0.0128098391, -0.0380480029, -0.0274949204, 0.0105272178, -0.0147691434, 0.00473660138, -0.00124962209, -0.00775315333, 0.0201232806, 0.0210285708, 0.00203366694, -0.00678966753, 0.00537030352, -0.0116652949, 0.0314781927, 0.00461374084, 0.00232141954, -0.056852147, 0.00294380588, -0.0067961337, -0.00411906512, -0.0143552972, 0.0111738527, -0.00400590384, 0.00875543803, 0.00225675618, 0.0229814071, 0.022050254, -0.0265379, 0.0188170783, -0.0234211199, -0.010779405, 0.0215846766, 0.0102685634, -0.0167866442, -0.0158296246, -0.00936327502\], metadata={'author': 'Harper Lee', 'theme': 'Mafia', 'year': 1960}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, hash='3475334d04bbe4606cb77728d5dc0784f16c8db3f190f3692e6310906c821927', text='To Kill a Mockingbird', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.531934)\]

Back to top

[Previous A Simple to Advanced Guide with Auto-Retrieval (with Pinecone + Arize Phoenix)](https://docs.llamaindex.ai/en/stable/examples/vector_stores/pinecone_auto_retriever/)[Next Postgres Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/postgres/)
