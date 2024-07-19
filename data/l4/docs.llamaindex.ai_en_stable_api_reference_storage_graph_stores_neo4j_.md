Title: Neo4j - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/

Markdown Content:
Neo4j - LlamaIndex
===============
             

[Skip to content](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jGraphStore)

[![Image 1: logo](https://docs.llamaindex.ai/en/stable/_static/assets/LlamaSquareBlack.svg)](https://docs.llamaindex.ai/en/stable/ "LlamaIndex")

LlamaIndex

Neo4j

  

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
            *    Neo4j [Neo4j](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/)
                
                Table of contents
                
                *   [Neo4jGraphStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jGraphStore)
                    
                    *   [get](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jGraphStore.get)
                    *   [get\_rel\_map](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jGraphStore.get_rel_map)
                    *   [upsert\_triplet](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jGraphStore.upsert_triplet)
                    *   [delete](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jGraphStore.delete)
                    *   [refresh\_schema](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jGraphStore.refresh_schema)
                    *   [get\_schema](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jGraphStore.get_schema)
                    
                *   [Neo4jPropertyGraphStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jPropertyGraphStore)
                    
                    *   [refresh\_schema](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jPropertyGraphStore.refresh_schema)
                    *   [upsert\_relations](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jPropertyGraphStore.upsert_relations)
                    *   [get](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jPropertyGraphStore.get)
                    *   [get\_rel\_map](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jPropertyGraphStore.get_rel_map)
                    *   [vector\_query](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jPropertyGraphStore.vector_query)
                    *   [delete](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jPropertyGraphStore.delete)
                    
                
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

*   [Neo4jGraphStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jGraphStore)
    
    *   [get](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jGraphStore.get)
    *   [get\_rel\_map](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jGraphStore.get_rel_map)
    *   [upsert\_triplet](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jGraphStore.upsert_triplet)
    *   [delete](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jGraphStore.delete)
    *   [refresh\_schema](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jGraphStore.refresh_schema)
    *   [get\_schema](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jGraphStore.get_schema)
    
*   [Neo4jPropertyGraphStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jPropertyGraphStore)
    
    *   [refresh\_schema](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jPropertyGraphStore.refresh_schema)
    *   [upsert\_relations](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jPropertyGraphStore.upsert_relations)
    *   [get](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jPropertyGraphStore.get)
    *   [get\_rel\_map](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jPropertyGraphStore.get_rel_map)
    *   [vector\_query](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jPropertyGraphStore.vector_query)
    *   [delete](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jPropertyGraphStore.delete)
    

Neo4j
=====

Neo4jGraphStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jGraphStore "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[GraphStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/#llama_index.core.graph_stores.types.GraphStore "llama_index.core.graph_stores.types.GraphStore")`

Source code in `llama-index-integrations/graph_stores/llama-index-graph-stores-neo4j/llama_index/graph_stores/neo4j/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 37</span>
<span class="normal"> 38</span>
<span class="normal"> 39</span>
<span class="normal"> 40</span>
<span class="normal"> 41</span>
<span class="normal"> 42</span>
<span class="normal"> 43</span>
<span class="normal"> 44</span>
<span class="normal"> 45</span>
<span class="normal"> 46</span>
<span class="normal"> 47</span>
<span class="normal"> 48</span>
<span class="normal"> 49</span>
<span class="normal"> 50</span>
<span class="normal"> 51</span>
<span class="normal"> 52</span>
<span class="normal"> 53</span>
<span class="normal"> 54</span>
<span class="normal"> 55</span>
<span class="normal"> 56</span>
<span class="normal"> 57</span>
<span class="normal"> 58</span>
<span class="normal"> 59</span>
<span class="normal"> 60</span>
<span class="normal"> 61</span>
<span class="normal"> 62</span>
<span class="normal"> 63</span>
<span class="normal"> 64</span>
<span class="normal"> 65</span>
<span class="normal"> 66</span>
<span class="normal"> 67</span>
<span class="normal"> 68</span>
<span class="normal"> 69</span>
<span class="normal"> 70</span>
<span class="normal"> 71</span>
<span class="normal"> 72</span>
<span class="normal"> 73</span>
<span class="normal"> 74</span>
<span class="normal"> 75</span>
<span class="normal"> 76</span>
<span class="normal"> 77</span>
<span class="normal"> 78</span>
<span class="normal"> 79</span>
<span class="normal"> 80</span>
<span class="normal"> 81</span>
<span class="normal"> 82</span>
<span class="normal"> 83</span>
<span class="normal"> 84</span>
<span class="normal"> 85</span>
<span class="normal"> 86</span>
<span class="normal"> 87</span>
<span class="normal"> 88</span>
<span class="normal"> 89</span>
<span class="normal"> 90</span>
<span class="normal"> 91</span>
<span class="normal"> 92</span>
<span class="normal"> 93</span>
<span class="normal"> 94</span>
<span class="normal"> 95</span>
<span class="normal"> 96</span>
<span class="normal"> 97</span>
<span class="normal"> 98</span>
<span class="normal"> 99</span>
<span class="normal">100</span>
<span class="normal">101</span>
<span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span>
<span class="normal">107</span>
<span class="normal">108</span>
<span class="normal">109</span>
<span class="normal">110</span>
<span class="normal">111</span>
<span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span>
<span class="normal">119</span>
<span class="normal">120</span>
<span class="normal">121</span>
<span class="normal">122</span>
<span class="normal">123</span>
<span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span>
<span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span>
<span class="normal">160</span>
<span class="normal">161</span>
<span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span>
<span class="normal">165</span>
<span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
<span class="normal">225</span>
<span class="normal">226</span>
<span class="normal">227</span>
<span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span>
<span class="normal">231</span>
<span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span>
<span class="normal">236</span>
<span class="normal">237</span>
<span class="normal">238</span>
<span class="normal">239</span>
<span class="normal">240</span>
<span class="normal">241</span>
<span class="normal">242</span>
<span class="normal">243</span>
<span class="normal">244</span>
<span class="normal">245</span>
<span class="normal">246</span>
<span class="normal">247</span>
<span class="normal">248</span>
<span class="normal">249</span>
<span class="normal">250</span>
<span class="normal">251</span>
<span class="normal">252</span>
<span class="normal">253</span>
<span class="normal">254</span>
<span class="normal">255</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">Neo4jGraphStore</span><span class="p">(</span><span class="n">GraphStore</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">username</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">password</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">database</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"neo4j"</span><span class="p">,</span>
        <span class="n">node_label</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"Entity"</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">node_label</span> <span class="o">=</span> <span class="n">node_label</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span> <span class="o">=</span> <span class="n">neo4j</span><span class="o">.</span><span class="n">GraphDatabase</span><span class="o">.</span><span class="n">driver</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">auth</span><span class="o">=</span><span class="p">(</span><span class="n">username</span><span class="p">,</span> <span class="n">password</span><span class="p">))</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_database</span> <span class="o">=</span> <span class="n">database</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">schema</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">structured_schema</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="c1"># Verify connection</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span> <span class="k">as</span> <span class="n">driver</span><span class="p">:</span>
                <span class="n">driver</span><span class="o">.</span><span class="n">verify_connectivity</span><span class="p">()</span>
        <span class="k">except</span> <span class="n">neo4j</span><span class="o">.</span><span class="n">exceptions</span><span class="o">.</span><span class="n">ServiceUnavailable</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Could not connect to Neo4j database. "</span>
                <span class="s2">"Please ensure that the url is correct"</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="n">neo4j</span><span class="o">.</span><span class="n">exceptions</span><span class="o">.</span><span class="n">AuthError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Could not connect to Neo4j database. "</span>
                <span class="s2">"Please ensure that the username and password are correct"</span>
            <span class="p">)</span>
        <span class="c1"># Set schema</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">refresh_schema</span><span class="p">()</span>
        <span class="k">except</span> <span class="n">neo4j</span><span class="o">.</span><span class="n">exceptions</span><span class="o">.</span><span class="n">ClientError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Could not use APOC procedures. "</span>
                <span class="s2">"Please ensure the APOC plugin is installed in Neo4j and that "</span>
                <span class="s2">"'apoc.meta.data()' is allowed in Neo4j configuration "</span>
            <span class="p">)</span>
        <span class="c1"># Create constraint for faster insert and retrieval</span>
        <span class="k">try</span><span class="p">:</span>  <span class="c1"># Using Neo4j 5</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">query</span><span class="p">(</span>
<span class="w">                </span><span class="sd">"""</span>
<span class="sd">                CREATE CONSTRAINT IF NOT EXISTS FOR (n:%s) REQUIRE n.id IS UNIQUE;</span>
<span class="sd">                """</span>
                <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">)</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>  <span class="c1"># Using Neo4j &lt;5</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">query</span><span class="p">(</span>
<span class="w">                </span><span class="sd">"""</span>
<span class="sd">                CREATE CONSTRAINT IF NOT EXISTS ON (n:%s) ASSERT n.id IS UNIQUE;</span>
<span class="sd">                """</span>
                <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">)</span>
            <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span>

    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">subj</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Get triplets."""</span>
        <span class="n">query</span> <span class="o">=</span> <span class="s2">"""</span>
<span class="s2">            MATCH (n1:</span><span class="si">%s</span><span class="s2">)-[r]-&gt;(n2:</span><span class="si">%s</span><span class="s2">)</span>
<span class="s2">            WHERE n1.id = $subj</span>
<span class="s2">            RETURN type(r), n2.id;</span>
<span class="s2">        """</span>

        <span class="n">prepared_statement</span> <span class="o">=</span> <span class="n">query</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">)</span>

        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span><span class="o">.</span><span class="n">session</span><span class="p">(</span><span class="n">database</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_database</span><span class="p">)</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
            <span class="n">data</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">prepared_statement</span><span class="p">,</span> <span class="p">{</span><span class="s2">"subj"</span><span class="p">:</span> <span class="n">subj</span><span class="p">})</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">record</span><span class="o">.</span><span class="n">values</span><span class="p">()</span> <span class="k">for</span> <span class="n">record</span> <span class="ow">in</span> <span class="n">data</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">get_rel_map</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">subjs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span> <span class="n">limit</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">30</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]:</span>
<span class="w">        </span><span class="sd">"""Get flat rel map."""</span>
        <span class="c1"># The flat means for multi-hop relation path, we could get</span>
        <span class="c1"># knowledge like: subj -&gt; rel -&gt; obj -&gt; rel -&gt; obj -&gt; rel -&gt; obj.</span>
        <span class="c1"># This type of knowledge is useful for some tasks.</span>
        <span class="c1"># +-------------+------------------------------------+</span>
        <span class="c1"># | subj        | flattened_rels                     |</span>
        <span class="c1"># +-------------+------------------------------------+</span>
        <span class="c1"># | "player101" | [95, "player125", 2002, "team204"] |</span>
        <span class="c1"># | "player100" | [1997, "team204"]                  |</span>
        <span class="c1"># ...</span>
        <span class="c1"># +-------------+------------------------------------+</span>

        <span class="n">rel_map</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">if</span> <span class="n">subjs</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">or</span> <span class="nb">len</span><span class="p">(</span><span class="n">subjs</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
            <span class="c1"># unlike simple graph_store, we don't do get_all here</span>
            <span class="k">return</span> <span class="n">rel_map</span>

        <span class="n">query</span> <span class="o">=</span> <span class="p">(</span>
            <span class="sa">f</span><span class="s2">"""MATCH p=(n1:</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="si">}</span><span class="s2">)-[*1..</span><span class="si">{</span><span class="n">depth</span><span class="si">}</span><span class="s2">]-&gt;() """</span>
            <span class="sa">f</span><span class="s2">"""WHERE toLower(n1.id) IN </span><span class="si">{</span><span class="p">[</span><span class="n">subj</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">subj</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="n">subjs</span><span class="p">]</span><span class="w"> </span><span class="k">if</span><span class="w"> </span><span class="n">subjs</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="p">[]</span><span class="si">}</span><span class="s2">"""</span>
            <span class="s2">"UNWIND relationships(p) AS rel "</span>
            <span class="s2">"WITH n1.id AS subj, p, apoc.coll.flatten(apoc.coll.toSet("</span>
            <span class="s2">"collect([type(rel), endNode(rel).id]))) AS flattened_rels "</span>
            <span class="sa">f</span><span class="s2">"RETURN subj, collect(flattened_rels) AS flattened_rels LIMIT </span><span class="si">{</span><span class="n">limit</span><span class="si">}</span><span class="s2">"</span>
        <span class="p">)</span>

        <span class="n">data</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="p">{</span><span class="s2">"subjs"</span><span class="p">:</span> <span class="n">subjs</span><span class="p">}))</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">data</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">rel_map</span>

        <span class="k">for</span> <span class="n">record</span> <span class="ow">in</span> <span class="n">data</span><span class="p">:</span>
            <span class="n">rel_map</span><span class="p">[</span><span class="n">record</span><span class="p">[</span><span class="s2">"subj"</span><span class="p">]]</span> <span class="o">=</span> <span class="n">record</span><span class="p">[</span><span class="s2">"flattened_rels"</span><span class="p">]</span>
        <span class="k">return</span> <span class="n">rel_map</span>

    <span class="k">def</span> <span class="nf">upsert_triplet</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">subj</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">rel</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Add triplet."""</span>
        <span class="n">query</span> <span class="o">=</span> <span class="s2">"""</span>
<span class="s2">            MERGE (n1:`</span><span class="si">%s</span><span class="s2">` {id:$subj})</span>
<span class="s2">            MERGE (n2:`</span><span class="si">%s</span><span class="s2">` {id:$obj})</span>
<span class="s2">            MERGE (n1)-[:`</span><span class="si">%s</span><span class="s2">`]-&gt;(n2)</span>
<span class="s2">        """</span>

        <span class="n">prepared_statement</span> <span class="o">=</span> <span class="n">query</span> <span class="o">%</span> <span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">,</span>
            <span class="n">rel</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">" "</span><span class="p">,</span> <span class="s2">"_"</span><span class="p">)</span><span class="o">.</span><span class="n">upper</span><span class="p">(),</span>
        <span class="p">)</span>

        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span><span class="o">.</span><span class="n">session</span><span class="p">(</span><span class="n">database</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_database</span><span class="p">)</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
            <span class="n">session</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">prepared_statement</span><span class="p">,</span> <span class="p">{</span><span class="s2">"subj"</span><span class="p">:</span> <span class="n">subj</span><span class="p">,</span> <span class="s2">"obj"</span><span class="p">:</span> <span class="n">obj</span><span class="p">})</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">subj</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">rel</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete triplet."""</span>

        <span class="k">def</span> <span class="nf">delete_rel</span><span class="p">(</span><span class="n">subj</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">rel</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span><span class="o">.</span><span class="n">session</span><span class="p">(</span><span class="n">database</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_database</span><span class="p">)</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
                <span class="n">session</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
                    <span class="p">(</span>
                        <span class="s2">"MATCH (n1:</span><span class="si">{}</span><span class="s2">)-[r:</span><span class="si">{}</span><span class="s2">]-&gt;(n2:</span><span class="si">{}</span><span class="s2">) WHERE n1.id = $subj AND n2.id"</span>
                        <span class="s2">" = $obj DELETE r"</span>
                    <span class="p">)</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">,</span> <span class="n">rel</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">),</span>
                    <span class="p">{</span><span class="s2">"subj"</span><span class="p">:</span> <span class="n">subj</span><span class="p">,</span> <span class="s2">"obj"</span><span class="p">:</span> <span class="n">obj</span><span class="p">},</span>
                <span class="p">)</span>

        <span class="k">def</span> <span class="nf">delete_entity</span><span class="p">(</span><span class="n">entity</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span><span class="o">.</span><span class="n">session</span><span class="p">(</span><span class="n">database</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_database</span><span class="p">)</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
                <span class="n">session</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
                    <span class="s2">"MATCH (n:</span><span class="si">%s</span><span class="s2">) WHERE n.id = $entity DELETE n"</span> <span class="o">%</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">,</span>
                    <span class="p">{</span><span class="s2">"entity"</span><span class="p">:</span> <span class="n">entity</span><span class="p">},</span>
                <span class="p">)</span>

        <span class="k">def</span> <span class="nf">check_edges</span><span class="p">(</span><span class="n">entity</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
            <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span><span class="o">.</span><span class="n">session</span><span class="p">(</span><span class="n">database</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_database</span><span class="p">)</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
                <span class="n">is_exists_result</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
                    <span class="s2">"MATCH (n1:</span><span class="si">%s</span><span class="s2">)--() WHERE n1.id = $entity RETURN count(*)"</span>
                    <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">),</span>
                    <span class="p">{</span><span class="s2">"entity"</span><span class="p">:</span> <span class="n">entity</span><span class="p">},</span>
                <span class="p">)</span>
                <span class="k">return</span> <span class="nb">bool</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">is_exists_result</span><span class="p">))</span>

        <span class="n">delete_rel</span><span class="p">(</span><span class="n">subj</span><span class="p">,</span> <span class="n">obj</span><span class="p">,</span> <span class="n">rel</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">check_edges</span><span class="p">(</span><span class="n">subj</span><span class="p">):</span>
            <span class="n">delete_entity</span><span class="p">(</span><span class="n">subj</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">check_edges</span><span class="p">(</span><span class="n">obj</span><span class="p">):</span>
            <span class="n">delete_entity</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">refresh_schema</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Refreshes the Neo4j graph schema information.</span>
<span class="sd">        """</span>
        <span class="n">node_properties</span> <span class="o">=</span> <span class="p">[</span><span class="n">el</span><span class="p">[</span><span class="s2">"output"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">node_properties_query</span><span class="p">)]</span>
        <span class="n">rel_properties</span> <span class="o">=</span> <span class="p">[</span><span class="n">el</span><span class="p">[</span><span class="s2">"output"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">rel_properties_query</span><span class="p">)]</span>
        <span class="n">relationships</span> <span class="o">=</span> <span class="p">[</span><span class="n">el</span><span class="p">[</span><span class="s2">"output"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">rel_query</span><span class="p">)]</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">structured_schema</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"node_props"</span><span class="p">:</span> <span class="p">{</span><span class="n">el</span><span class="p">[</span><span class="s2">"labels"</span><span class="p">]:</span> <span class="n">el</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">node_properties</span><span class="p">},</span>
            <span class="s2">"rel_props"</span><span class="p">:</span> <span class="p">{</span><span class="n">el</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]:</span> <span class="n">el</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">rel_properties</span><span class="p">},</span>
            <span class="s2">"relationships"</span><span class="p">:</span> <span class="n">relationships</span><span class="p">,</span>
        <span class="p">}</span>

        <span class="c1"># Format node properties</span>
        <span class="n">formatted_node_props</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">node_properties</span><span class="p">:</span>
            <span class="n">props_str</span> <span class="o">=</span> <span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                <span class="p">[</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s1">'property'</span><span class="p">]</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s1">'type'</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span> <span class="k">for</span> <span class="n">prop</span> <span class="ow">in</span> <span class="n">el</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]]</span>
            <span class="p">)</span>
            <span class="n">formatted_node_props</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">el</span><span class="p">[</span><span class="s1">'labels'</span><span class="p">]</span><span class="si">}</span><span class="s2"> </span><span class="se">{{</span><span class="si">{</span><span class="n">props_str</span><span class="si">}</span><span class="se">}}</span><span class="s2">"</span><span class="p">)</span>

        <span class="c1"># Format relationship properties</span>
        <span class="n">formatted_rel_props</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">rel_properties</span><span class="p">:</span>
            <span class="n">props_str</span> <span class="o">=</span> <span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                <span class="p">[</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s1">'property'</span><span class="p">]</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s1">'type'</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span> <span class="k">for</span> <span class="n">prop</span> <span class="ow">in</span> <span class="n">el</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]]</span>
            <span class="p">)</span>
            <span class="n">formatted_rel_props</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">el</span><span class="p">[</span><span class="s1">'type'</span><span class="p">]</span><span class="si">}</span><span class="s2"> </span><span class="se">{{</span><span class="si">{</span><span class="n">props_str</span><span class="si">}</span><span class="se">}}</span><span class="s2">"</span><span class="p">)</span>

        <span class="c1"># Format relationships</span>
        <span class="n">formatted_rels</span> <span class="o">=</span> <span class="p">[</span>
            <span class="sa">f</span><span class="s2">"(:</span><span class="si">{</span><span class="n">el</span><span class="p">[</span><span class="s1">'start'</span><span class="p">]</span><span class="si">}</span><span class="s2">)-[:</span><span class="si">{</span><span class="n">el</span><span class="p">[</span><span class="s1">'type'</span><span class="p">]</span><span class="si">}</span><span class="s2">]-&gt;(:</span><span class="si">{</span><span class="n">el</span><span class="p">[</span><span class="s1">'end'</span><span class="p">]</span><span class="si">}</span><span class="s2">)"</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">relationships</span>
        <span class="p">]</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">schema</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
            <span class="p">[</span>
                <span class="s2">"Node properties are the following:"</span><span class="p">,</span>
                <span class="s2">","</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">formatted_node_props</span><span class="p">),</span>
                <span class="s2">"Relationship properties are the following:"</span><span class="p">,</span>
                <span class="s2">","</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">formatted_rel_props</span><span class="p">),</span>
                <span class="s2">"The relationships are the following:"</span><span class="p">,</span>
                <span class="s2">","</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">formatted_rels</span><span class="p">),</span>
            <span class="p">]</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_schema</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">refresh</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get the schema of the Neo4jGraph store."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">schema</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">refresh</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">schema</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">refresh_schema</span><span class="p">()</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"get_schema() schema:</span><span class="se">\n</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">schema</span>

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">param_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="p">{})</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span><span class="o">.</span><span class="n">session</span><span class="p">(</span><span class="n">database</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_database</span><span class="p">)</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
            <span class="n">result</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">param_map</span><span class="p">)</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">d</span><span class="o">.</span><span class="n">data</span><span class="p">()</span> <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">result</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### get [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jGraphStore.get "Permanent link")

```
get(subj: str) -> List[List[str]]
```

Get triplets.

Source code in `llama-index-integrations/graph_stores/llama-index-graph-stores-neo4j/llama_index/graph_stores/neo4j/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 95</span>
<span class="normal"> 96</span>
<span class="normal"> 97</span>
<span class="normal"> 98</span>
<span class="normal"> 99</span>
<span class="normal">100</span>
<span class="normal">101</span>
<span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span>
<span class="normal">107</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">subj</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Get triplets."""</span>
    <span class="n">query</span> <span class="o">=</span> <span class="s2">"""</span>
<span class="s2">        MATCH (n1:</span><span class="si">%s</span><span class="s2">)-[r]-&gt;(n2:</span><span class="si">%s</span><span class="s2">)</span>
<span class="s2">        WHERE n1.id = $subj</span>
<span class="s2">        RETURN type(r), n2.id;</span>
<span class="s2">    """</span>

    <span class="n">prepared_statement</span> <span class="o">=</span> <span class="n">query</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">)</span>

    <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span><span class="o">.</span><span class="n">session</span><span class="p">(</span><span class="n">database</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_database</span><span class="p">)</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
        <span class="n">data</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">prepared_statement</span><span class="p">,</span> <span class="p">{</span><span class="s2">"subj"</span><span class="p">:</span> <span class="n">subj</span><span class="p">})</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">record</span><span class="o">.</span><span class="n">values</span><span class="p">()</span> <span class="k">for</span> <span class="n">record</span> <span class="ow">in</span> <span class="n">data</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### get\_rel\_map [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jGraphStore.get_rel_map "Permanent link")

```
get_rel_map(subjs: Optional[List[str]] = None, depth: int = 2, limit: int = 30) -> Dict[str, List[List[str]]]
```

Get flat rel map.

Source code in `llama-index-integrations/graph_stores/llama-index-graph-stores-neo4j/llama_index/graph_stores/neo4j/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">109</span>
<span class="normal">110</span>
<span class="normal">111</span>
<span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span>
<span class="normal">119</span>
<span class="normal">120</span>
<span class="normal">121</span>
<span class="normal">122</span>
<span class="normal">123</span>
<span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span>
<span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_rel_map</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">subjs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span> <span class="n">limit</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">30</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]]:</span>
<span class="w">    </span><span class="sd">"""Get flat rel map."""</span>
    <span class="c1"># The flat means for multi-hop relation path, we could get</span>
    <span class="c1"># knowledge like: subj -&gt; rel -&gt; obj -&gt; rel -&gt; obj -&gt; rel -&gt; obj.</span>
    <span class="c1"># This type of knowledge is useful for some tasks.</span>
    <span class="c1"># +-------------+------------------------------------+</span>
    <span class="c1"># | subj        | flattened_rels                     |</span>
    <span class="c1"># +-------------+------------------------------------+</span>
    <span class="c1"># | "player101" | [95, "player125", 2002, "team204"] |</span>
    <span class="c1"># | "player100" | [1997, "team204"]                  |</span>
    <span class="c1"># ...</span>
    <span class="c1"># +-------------+------------------------------------+</span>

    <span class="n">rel_map</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="k">if</span> <span class="n">subjs</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">or</span> <span class="nb">len</span><span class="p">(</span><span class="n">subjs</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
        <span class="c1"># unlike simple graph_store, we don't do get_all here</span>
        <span class="k">return</span> <span class="n">rel_map</span>

    <span class="n">query</span> <span class="o">=</span> <span class="p">(</span>
        <span class="sa">f</span><span class="s2">"""MATCH p=(n1:</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="si">}</span><span class="s2">)-[*1..</span><span class="si">{</span><span class="n">depth</span><span class="si">}</span><span class="s2">]-&gt;() """</span>
        <span class="sa">f</span><span class="s2">"""WHERE toLower(n1.id) IN </span><span class="si">{</span><span class="p">[</span><span class="n">subj</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">subj</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="n">subjs</span><span class="p">]</span><span class="w"> </span><span class="k">if</span><span class="w"> </span><span class="n">subjs</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="p">[]</span><span class="si">}</span><span class="s2">"""</span>
        <span class="s2">"UNWIND relationships(p) AS rel "</span>
        <span class="s2">"WITH n1.id AS subj, p, apoc.coll.flatten(apoc.coll.toSet("</span>
        <span class="s2">"collect([type(rel), endNode(rel).id]))) AS flattened_rels "</span>
        <span class="sa">f</span><span class="s2">"RETURN subj, collect(flattened_rels) AS flattened_rels LIMIT </span><span class="si">{</span><span class="n">limit</span><span class="si">}</span><span class="s2">"</span>
    <span class="p">)</span>

    <span class="n">data</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="p">{</span><span class="s2">"subjs"</span><span class="p">:</span> <span class="n">subjs</span><span class="p">}))</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">data</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">rel_map</span>

    <span class="k">for</span> <span class="n">record</span> <span class="ow">in</span> <span class="n">data</span><span class="p">:</span>
        <span class="n">rel_map</span><span class="p">[</span><span class="n">record</span><span class="p">[</span><span class="s2">"subj"</span><span class="p">]]</span> <span class="o">=</span> <span class="n">record</span><span class="p">[</span><span class="s2">"flattened_rels"</span><span class="p">]</span>
    <span class="k">return</span> <span class="n">rel_map</span>
</code></pre></div></td></tr></tbody></table>

### upsert\_triplet [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jGraphStore.upsert_triplet "Permanent link")

```
upsert_triplet(subj: str, rel: str, obj: str) -> None
```

Add triplet.

Source code in `llama-index-integrations/graph_stores/llama-index-graph-stores-neo4j/llama_index/graph_stores/neo4j/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span>
<span class="normal">160</span>
<span class="normal">161</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">upsert_triplet</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">subj</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">rel</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Add triplet."""</span>
    <span class="n">query</span> <span class="o">=</span> <span class="s2">"""</span>
<span class="s2">        MERGE (n1:`</span><span class="si">%s</span><span class="s2">` {id:$subj})</span>
<span class="s2">        MERGE (n2:`</span><span class="si">%s</span><span class="s2">` {id:$obj})</span>
<span class="s2">        MERGE (n1)-[:`</span><span class="si">%s</span><span class="s2">`]-&gt;(n2)</span>
<span class="s2">    """</span>

    <span class="n">prepared_statement</span> <span class="o">=</span> <span class="n">query</span> <span class="o">%</span> <span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">,</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">,</span>
        <span class="n">rel</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">" "</span><span class="p">,</span> <span class="s2">"_"</span><span class="p">)</span><span class="o">.</span><span class="n">upper</span><span class="p">(),</span>
    <span class="p">)</span>

    <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span><span class="o">.</span><span class="n">session</span><span class="p">(</span><span class="n">database</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_database</span><span class="p">)</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
        <span class="n">session</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">prepared_statement</span><span class="p">,</span> <span class="p">{</span><span class="s2">"subj"</span><span class="p">:</span> <span class="n">subj</span><span class="p">,</span> <span class="s2">"obj"</span><span class="p">:</span> <span class="n">obj</span><span class="p">})</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jGraphStore.delete "Permanent link")

```
delete(subj: str, rel: str, obj: str) -> None
```

Delete triplet.

Source code in `llama-index-integrations/graph_stores/llama-index-graph-stores-neo4j/llama_index/graph_stores/neo4j/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">163</span>
<span class="normal">164</span>
<span class="normal">165</span>
<span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">subj</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">rel</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete triplet."""</span>

    <span class="k">def</span> <span class="nf">delete_rel</span><span class="p">(</span><span class="n">subj</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">rel</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span><span class="o">.</span><span class="n">session</span><span class="p">(</span><span class="n">database</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_database</span><span class="p">)</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
            <span class="n">session</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
                <span class="p">(</span>
                    <span class="s2">"MATCH (n1:</span><span class="si">{}</span><span class="s2">)-[r:</span><span class="si">{}</span><span class="s2">]-&gt;(n2:</span><span class="si">{}</span><span class="s2">) WHERE n1.id = $subj AND n2.id"</span>
                    <span class="s2">" = $obj DELETE r"</span>
                <span class="p">)</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">,</span> <span class="n">rel</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">),</span>
                <span class="p">{</span><span class="s2">"subj"</span><span class="p">:</span> <span class="n">subj</span><span class="p">,</span> <span class="s2">"obj"</span><span class="p">:</span> <span class="n">obj</span><span class="p">},</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">delete_entity</span><span class="p">(</span><span class="n">entity</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span><span class="o">.</span><span class="n">session</span><span class="p">(</span><span class="n">database</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_database</span><span class="p">)</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
            <span class="n">session</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
                <span class="s2">"MATCH (n:</span><span class="si">%s</span><span class="s2">) WHERE n.id = $entity DELETE n"</span> <span class="o">%</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">,</span>
                <span class="p">{</span><span class="s2">"entity"</span><span class="p">:</span> <span class="n">entity</span><span class="p">},</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">check_edges</span><span class="p">(</span><span class="n">entity</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span><span class="o">.</span><span class="n">session</span><span class="p">(</span><span class="n">database</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_database</span><span class="p">)</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
            <span class="n">is_exists_result</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
                <span class="s2">"MATCH (n1:</span><span class="si">%s</span><span class="s2">)--() WHERE n1.id = $entity RETURN count(*)"</span>
                <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">),</span>
                <span class="p">{</span><span class="s2">"entity"</span><span class="p">:</span> <span class="n">entity</span><span class="p">},</span>
            <span class="p">)</span>
            <span class="k">return</span> <span class="nb">bool</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">is_exists_result</span><span class="p">))</span>

    <span class="n">delete_rel</span><span class="p">(</span><span class="n">subj</span><span class="p">,</span> <span class="n">obj</span><span class="p">,</span> <span class="n">rel</span><span class="p">)</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">check_edges</span><span class="p">(</span><span class="n">subj</span><span class="p">):</span>
        <span class="n">delete_entity</span><span class="p">(</span><span class="n">subj</span><span class="p">)</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">check_edges</span><span class="p">(</span><span class="n">obj</span><span class="p">):</span>
        <span class="n">delete_entity</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### refresh\_schema [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jGraphStore.refresh_schema "Permanent link")

```
refresh_schema() -> None
```

Refreshes the Neo4j graph schema information.

Source code in `llama-index-integrations/graph_stores/llama-index-graph-stores-neo4j/llama_index/graph_stores/neo4j/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
<span class="normal">225</span>
<span class="normal">226</span>
<span class="normal">227</span>
<span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span>
<span class="normal">231</span>
<span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span>
<span class="normal">236</span>
<span class="normal">237</span>
<span class="normal">238</span>
<span class="normal">239</span>
<span class="normal">240</span>
<span class="normal">241</span>
<span class="normal">242</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">refresh_schema</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Refreshes the Neo4j graph schema information.</span>
<span class="sd">    """</span>
    <span class="n">node_properties</span> <span class="o">=</span> <span class="p">[</span><span class="n">el</span><span class="p">[</span><span class="s2">"output"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">node_properties_query</span><span class="p">)]</span>
    <span class="n">rel_properties</span> <span class="o">=</span> <span class="p">[</span><span class="n">el</span><span class="p">[</span><span class="s2">"output"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">rel_properties_query</span><span class="p">)]</span>
    <span class="n">relationships</span> <span class="o">=</span> <span class="p">[</span><span class="n">el</span><span class="p">[</span><span class="s2">"output"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">rel_query</span><span class="p">)]</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">structured_schema</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"node_props"</span><span class="p">:</span> <span class="p">{</span><span class="n">el</span><span class="p">[</span><span class="s2">"labels"</span><span class="p">]:</span> <span class="n">el</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">node_properties</span><span class="p">},</span>
        <span class="s2">"rel_props"</span><span class="p">:</span> <span class="p">{</span><span class="n">el</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]:</span> <span class="n">el</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">rel_properties</span><span class="p">},</span>
        <span class="s2">"relationships"</span><span class="p">:</span> <span class="n">relationships</span><span class="p">,</span>
    <span class="p">}</span>

    <span class="c1"># Format node properties</span>
    <span class="n">formatted_node_props</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">node_properties</span><span class="p">:</span>
        <span class="n">props_str</span> <span class="o">=</span> <span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
            <span class="p">[</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s1">'property'</span><span class="p">]</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s1">'type'</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span> <span class="k">for</span> <span class="n">prop</span> <span class="ow">in</span> <span class="n">el</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]]</span>
        <span class="p">)</span>
        <span class="n">formatted_node_props</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">el</span><span class="p">[</span><span class="s1">'labels'</span><span class="p">]</span><span class="si">}</span><span class="s2"> </span><span class="se">{{</span><span class="si">{</span><span class="n">props_str</span><span class="si">}</span><span class="se">}}</span><span class="s2">"</span><span class="p">)</span>

    <span class="c1"># Format relationship properties</span>
    <span class="n">formatted_rel_props</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">rel_properties</span><span class="p">:</span>
        <span class="n">props_str</span> <span class="o">=</span> <span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
            <span class="p">[</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s1">'property'</span><span class="p">]</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s1">'type'</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span> <span class="k">for</span> <span class="n">prop</span> <span class="ow">in</span> <span class="n">el</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]]</span>
        <span class="p">)</span>
        <span class="n">formatted_rel_props</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">el</span><span class="p">[</span><span class="s1">'type'</span><span class="p">]</span><span class="si">}</span><span class="s2"> </span><span class="se">{{</span><span class="si">{</span><span class="n">props_str</span><span class="si">}</span><span class="se">}}</span><span class="s2">"</span><span class="p">)</span>

    <span class="c1"># Format relationships</span>
    <span class="n">formatted_rels</span> <span class="o">=</span> <span class="p">[</span>
        <span class="sa">f</span><span class="s2">"(:</span><span class="si">{</span><span class="n">el</span><span class="p">[</span><span class="s1">'start'</span><span class="p">]</span><span class="si">}</span><span class="s2">)-[:</span><span class="si">{</span><span class="n">el</span><span class="p">[</span><span class="s1">'type'</span><span class="p">]</span><span class="si">}</span><span class="s2">]-&gt;(:</span><span class="si">{</span><span class="n">el</span><span class="p">[</span><span class="s1">'end'</span><span class="p">]</span><span class="si">}</span><span class="s2">)"</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">relationships</span>
    <span class="p">]</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">schema</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
        <span class="p">[</span>
            <span class="s2">"Node properties are the following:"</span><span class="p">,</span>
            <span class="s2">","</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">formatted_node_props</span><span class="p">),</span>
            <span class="s2">"Relationship properties are the following:"</span><span class="p">,</span>
            <span class="s2">","</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">formatted_rel_props</span><span class="p">),</span>
            <span class="s2">"The relationships are the following:"</span><span class="p">,</span>
            <span class="s2">","</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">formatted_rels</span><span class="p">),</span>
        <span class="p">]</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_schema [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jGraphStore.get_schema "Permanent link")

```
get_schema(refresh: bool = False) -> str
```

Get the schema of the Neo4jGraph store.

Source code in `llama-index-integrations/graph_stores/llama-index-graph-stores-neo4j/llama_index/graph_stores/neo4j/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">244</span>
<span class="normal">245</span>
<span class="normal">246</span>
<span class="normal">247</span>
<span class="normal">248</span>
<span class="normal">249</span>
<span class="normal">250</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_schema</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">refresh</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get the schema of the Neo4jGraph store."""</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">schema</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">refresh</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">schema</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">refresh_schema</span><span class="p">()</span>
    <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"get_schema() schema:</span><span class="se">\n</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">schema</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">schema</span>
</code></pre></div></td></tr></tbody></table>

Neo4jPropertyGraphStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jPropertyGraphStore "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `PropertyGraphStore`

Neo4j Property Graph Store.

This class implements a Neo4j property graph store.

If you are using local Neo4j instead of aura, here's a helpful command for launching the docker container:

```
dockerrun\
-p7474:7474-p7687:7687\
-v$PWD/data:/data-v$PWD/plugins:/plugins\
--nameneo4j-apoc\
-eNEO4J_apoc_export_file_enabled=true\
-eNEO4J_apoc_import_file_enabled=true\
-eNEO4J_apoc_import_file_use__neo4j__config=true\
-eNEO4JLABS_PLUGINS=\\[\"apoc\"\\]\
neo4j:latest
```

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `username` | `str` | 
The username for the Neo4j database.



 | _required_ |
| `password` | `str` | 

The password for the Neo4j database.



 | _required_ |
| `url` | `str` | 

The URL for the Neo4j database.



 | _required_ |
| `database` | `Optional[str]` | 

The name of the database to connect to. Defaults to "neo4j".



 | `'neo4j'` |

**Examples:**

`pip install llama-index-graph-stores-neo4j`

```
from llama_index.core.indices.property_graph import PropertyGraphIndex
from llama_index.graph_stores.neo4j import Neo4jPropertyGraphStore

# Create a Neo4jPropertyGraphStore instance
graph_store = Neo4jPropertyGraphStore(
    username="neo4j",
    password="neo4j",
    url="bolt://localhost:7687",
    database="neo4j"
)

# create the index
index = PropertyGraphIndex.from_documents(
    documents,
    property_graph_store=graph_store,
)
```

Source code in `llama-index-integrations/graph_stores/llama-index-graph-stores-neo4j/llama_index/graph_stores/neo4j/neo4j_property_graph.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 73</span>
<span class="normal"> 74</span>
<span class="normal"> 75</span>
<span class="normal"> 76</span>
<span class="normal"> 77</span>
<span class="normal"> 78</span>
<span class="normal"> 79</span>
<span class="normal"> 80</span>
<span class="normal"> 81</span>
<span class="normal"> 82</span>
<span class="normal"> 83</span>
<span class="normal"> 84</span>
<span class="normal"> 85</span>
<span class="normal"> 86</span>
<span class="normal"> 87</span>
<span class="normal"> 88</span>
<span class="normal"> 89</span>
<span class="normal"> 90</span>
<span class="normal"> 91</span>
<span class="normal"> 92</span>
<span class="normal"> 93</span>
<span class="normal"> 94</span>
<span class="normal"> 95</span>
<span class="normal"> 96</span>
<span class="normal"> 97</span>
<span class="normal"> 98</span>
<span class="normal"> 99</span>
<span class="normal">100</span>
<span class="normal">101</span>
<span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span>
<span class="normal">107</span>
<span class="normal">108</span>
<span class="normal">109</span>
<span class="normal">110</span>
<span class="normal">111</span>
<span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span>
<span class="normal">119</span>
<span class="normal">120</span>
<span class="normal">121</span>
<span class="normal">122</span>
<span class="normal">123</span>
<span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span>
<span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span>
<span class="normal">160</span>
<span class="normal">161</span>
<span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span>
<span class="normal">165</span>
<span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
<span class="normal">225</span>
<span class="normal">226</span>
<span class="normal">227</span>
<span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span>
<span class="normal">231</span>
<span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span>
<span class="normal">236</span>
<span class="normal">237</span>
<span class="normal">238</span>
<span class="normal">239</span>
<span class="normal">240</span>
<span class="normal">241</span>
<span class="normal">242</span>
<span class="normal">243</span>
<span class="normal">244</span>
<span class="normal">245</span>
<span class="normal">246</span>
<span class="normal">247</span>
<span class="normal">248</span>
<span class="normal">249</span>
<span class="normal">250</span>
<span class="normal">251</span>
<span class="normal">252</span>
<span class="normal">253</span>
<span class="normal">254</span>
<span class="normal">255</span>
<span class="normal">256</span>
<span class="normal">257</span>
<span class="normal">258</span>
<span class="normal">259</span>
<span class="normal">260</span>
<span class="normal">261</span>
<span class="normal">262</span>
<span class="normal">263</span>
<span class="normal">264</span>
<span class="normal">265</span>
<span class="normal">266</span>
<span class="normal">267</span>
<span class="normal">268</span>
<span class="normal">269</span>
<span class="normal">270</span>
<span class="normal">271</span>
<span class="normal">272</span>
<span class="normal">273</span>
<span class="normal">274</span>
<span class="normal">275</span>
<span class="normal">276</span>
<span class="normal">277</span>
<span class="normal">278</span>
<span class="normal">279</span>
<span class="normal">280</span>
<span class="normal">281</span>
<span class="normal">282</span>
<span class="normal">283</span>
<span class="normal">284</span>
<span class="normal">285</span>
<span class="normal">286</span>
<span class="normal">287</span>
<span class="normal">288</span>
<span class="normal">289</span>
<span class="normal">290</span>
<span class="normal">291</span>
<span class="normal">292</span>
<span class="normal">293</span>
<span class="normal">294</span>
<span class="normal">295</span>
<span class="normal">296</span>
<span class="normal">297</span>
<span class="normal">298</span>
<span class="normal">299</span>
<span class="normal">300</span>
<span class="normal">301</span>
<span class="normal">302</span>
<span class="normal">303</span>
<span class="normal">304</span>
<span class="normal">305</span>
<span class="normal">306</span>
<span class="normal">307</span>
<span class="normal">308</span>
<span class="normal">309</span>
<span class="normal">310</span>
<span class="normal">311</span>
<span class="normal">312</span>
<span class="normal">313</span>
<span class="normal">314</span>
<span class="normal">315</span>
<span class="normal">316</span>
<span class="normal">317</span>
<span class="normal">318</span>
<span class="normal">319</span>
<span class="normal">320</span>
<span class="normal">321</span>
<span class="normal">322</span>
<span class="normal">323</span>
<span class="normal">324</span>
<span class="normal">325</span>
<span class="normal">326</span>
<span class="normal">327</span>
<span class="normal">328</span>
<span class="normal">329</span>
<span class="normal">330</span>
<span class="normal">331</span>
<span class="normal">332</span>
<span class="normal">333</span>
<span class="normal">334</span>
<span class="normal">335</span>
<span class="normal">336</span>
<span class="normal">337</span>
<span class="normal">338</span>
<span class="normal">339</span>
<span class="normal">340</span>
<span class="normal">341</span>
<span class="normal">342</span>
<span class="normal">343</span>
<span class="normal">344</span>
<span class="normal">345</span>
<span class="normal">346</span>
<span class="normal">347</span>
<span class="normal">348</span>
<span class="normal">349</span>
<span class="normal">350</span>
<span class="normal">351</span>
<span class="normal">352</span>
<span class="normal">353</span>
<span class="normal">354</span>
<span class="normal">355</span>
<span class="normal">356</span>
<span class="normal">357</span>
<span class="normal">358</span>
<span class="normal">359</span>
<span class="normal">360</span>
<span class="normal">361</span>
<span class="normal">362</span>
<span class="normal">363</span>
<span class="normal">364</span>
<span class="normal">365</span>
<span class="normal">366</span>
<span class="normal">367</span>
<span class="normal">368</span>
<span class="normal">369</span>
<span class="normal">370</span>
<span class="normal">371</span>
<span class="normal">372</span>
<span class="normal">373</span>
<span class="normal">374</span>
<span class="normal">375</span>
<span class="normal">376</span>
<span class="normal">377</span>
<span class="normal">378</span>
<span class="normal">379</span>
<span class="normal">380</span>
<span class="normal">381</span>
<span class="normal">382</span>
<span class="normal">383</span>
<span class="normal">384</span>
<span class="normal">385</span>
<span class="normal">386</span>
<span class="normal">387</span>
<span class="normal">388</span>
<span class="normal">389</span>
<span class="normal">390</span>
<span class="normal">391</span>
<span class="normal">392</span>
<span class="normal">393</span>
<span class="normal">394</span>
<span class="normal">395</span>
<span class="normal">396</span>
<span class="normal">397</span>
<span class="normal">398</span>
<span class="normal">399</span>
<span class="normal">400</span>
<span class="normal">401</span>
<span class="normal">402</span>
<span class="normal">403</span>
<span class="normal">404</span>
<span class="normal">405</span>
<span class="normal">406</span>
<span class="normal">407</span>
<span class="normal">408</span>
<span class="normal">409</span>
<span class="normal">410</span>
<span class="normal">411</span>
<span class="normal">412</span>
<span class="normal">413</span>
<span class="normal">414</span>
<span class="normal">415</span>
<span class="normal">416</span>
<span class="normal">417</span>
<span class="normal">418</span>
<span class="normal">419</span>
<span class="normal">420</span>
<span class="normal">421</span>
<span class="normal">422</span>
<span class="normal">423</span>
<span class="normal">424</span>
<span class="normal">425</span>
<span class="normal">426</span>
<span class="normal">427</span>
<span class="normal">428</span>
<span class="normal">429</span>
<span class="normal">430</span>
<span class="normal">431</span>
<span class="normal">432</span>
<span class="normal">433</span>
<span class="normal">434</span>
<span class="normal">435</span>
<span class="normal">436</span>
<span class="normal">437</span>
<span class="normal">438</span>
<span class="normal">439</span>
<span class="normal">440</span>
<span class="normal">441</span>
<span class="normal">442</span>
<span class="normal">443</span>
<span class="normal">444</span>
<span class="normal">445</span>
<span class="normal">446</span>
<span class="normal">447</span>
<span class="normal">448</span>
<span class="normal">449</span>
<span class="normal">450</span>
<span class="normal">451</span>
<span class="normal">452</span>
<span class="normal">453</span>
<span class="normal">454</span>
<span class="normal">455</span>
<span class="normal">456</span>
<span class="normal">457</span>
<span class="normal">458</span>
<span class="normal">459</span>
<span class="normal">460</span>
<span class="normal">461</span>
<span class="normal">462</span>
<span class="normal">463</span>
<span class="normal">464</span>
<span class="normal">465</span>
<span class="normal">466</span>
<span class="normal">467</span>
<span class="normal">468</span>
<span class="normal">469</span>
<span class="normal">470</span>
<span class="normal">471</span>
<span class="normal">472</span>
<span class="normal">473</span>
<span class="normal">474</span>
<span class="normal">475</span>
<span class="normal">476</span>
<span class="normal">477</span>
<span class="normal">478</span>
<span class="normal">479</span>
<span class="normal">480</span>
<span class="normal">481</span>
<span class="normal">482</span>
<span class="normal">483</span>
<span class="normal">484</span>
<span class="normal">485</span>
<span class="normal">486</span>
<span class="normal">487</span>
<span class="normal">488</span>
<span class="normal">489</span>
<span class="normal">490</span>
<span class="normal">491</span>
<span class="normal">492</span>
<span class="normal">493</span>
<span class="normal">494</span>
<span class="normal">495</span>
<span class="normal">496</span>
<span class="normal">497</span>
<span class="normal">498</span>
<span class="normal">499</span>
<span class="normal">500</span>
<span class="normal">501</span>
<span class="normal">502</span>
<span class="normal">503</span>
<span class="normal">504</span>
<span class="normal">505</span>
<span class="normal">506</span>
<span class="normal">507</span>
<span class="normal">508</span>
<span class="normal">509</span>
<span class="normal">510</span>
<span class="normal">511</span>
<span class="normal">512</span>
<span class="normal">513</span>
<span class="normal">514</span>
<span class="normal">515</span>
<span class="normal">516</span>
<span class="normal">517</span>
<span class="normal">518</span>
<span class="normal">519</span>
<span class="normal">520</span>
<span class="normal">521</span>
<span class="normal">522</span>
<span class="normal">523</span>
<span class="normal">524</span>
<span class="normal">525</span>
<span class="normal">526</span>
<span class="normal">527</span>
<span class="normal">528</span>
<span class="normal">529</span>
<span class="normal">530</span>
<span class="normal">531</span>
<span class="normal">532</span>
<span class="normal">533</span>
<span class="normal">534</span>
<span class="normal">535</span>
<span class="normal">536</span>
<span class="normal">537</span>
<span class="normal">538</span>
<span class="normal">539</span>
<span class="normal">540</span>
<span class="normal">541</span>
<span class="normal">542</span>
<span class="normal">543</span>
<span class="normal">544</span>
<span class="normal">545</span>
<span class="normal">546</span>
<span class="normal">547</span>
<span class="normal">548</span>
<span class="normal">549</span>
<span class="normal">550</span>
<span class="normal">551</span>
<span class="normal">552</span>
<span class="normal">553</span>
<span class="normal">554</span>
<span class="normal">555</span>
<span class="normal">556</span>
<span class="normal">557</span>
<span class="normal">558</span>
<span class="normal">559</span>
<span class="normal">560</span>
<span class="normal">561</span>
<span class="normal">562</span>
<span class="normal">563</span>
<span class="normal">564</span>
<span class="normal">565</span>
<span class="normal">566</span>
<span class="normal">567</span>
<span class="normal">568</span>
<span class="normal">569</span>
<span class="normal">570</span>
<span class="normal">571</span>
<span class="normal">572</span>
<span class="normal">573</span>
<span class="normal">574</span>
<span class="normal">575</span>
<span class="normal">576</span>
<span class="normal">577</span>
<span class="normal">578</span>
<span class="normal">579</span>
<span class="normal">580</span>
<span class="normal">581</span>
<span class="normal">582</span>
<span class="normal">583</span>
<span class="normal">584</span>
<span class="normal">585</span>
<span class="normal">586</span>
<span class="normal">587</span>
<span class="normal">588</span>
<span class="normal">589</span>
<span class="normal">590</span>
<span class="normal">591</span>
<span class="normal">592</span>
<span class="normal">593</span>
<span class="normal">594</span>
<span class="normal">595</span>
<span class="normal">596</span>
<span class="normal">597</span>
<span class="normal">598</span>
<span class="normal">599</span>
<span class="normal">600</span>
<span class="normal">601</span>
<span class="normal">602</span>
<span class="normal">603</span>
<span class="normal">604</span>
<span class="normal">605</span>
<span class="normal">606</span>
<span class="normal">607</span>
<span class="normal">608</span>
<span class="normal">609</span>
<span class="normal">610</span>
<span class="normal">611</span>
<span class="normal">612</span>
<span class="normal">613</span>
<span class="normal">614</span>
<span class="normal">615</span>
<span class="normal">616</span>
<span class="normal">617</span>
<span class="normal">618</span>
<span class="normal">619</span>
<span class="normal">620</span>
<span class="normal">621</span>
<span class="normal">622</span>
<span class="normal">623</span>
<span class="normal">624</span>
<span class="normal">625</span>
<span class="normal">626</span>
<span class="normal">627</span>
<span class="normal">628</span>
<span class="normal">629</span>
<span class="normal">630</span>
<span class="normal">631</span>
<span class="normal">632</span>
<span class="normal">633</span>
<span class="normal">634</span>
<span class="normal">635</span>
<span class="normal">636</span>
<span class="normal">637</span>
<span class="normal">638</span>
<span class="normal">639</span>
<span class="normal">640</span>
<span class="normal">641</span>
<span class="normal">642</span>
<span class="normal">643</span>
<span class="normal">644</span>
<span class="normal">645</span>
<span class="normal">646</span>
<span class="normal">647</span>
<span class="normal">648</span>
<span class="normal">649</span>
<span class="normal">650</span>
<span class="normal">651</span>
<span class="normal">652</span>
<span class="normal">653</span>
<span class="normal">654</span>
<span class="normal">655</span>
<span class="normal">656</span>
<span class="normal">657</span>
<span class="normal">658</span>
<span class="normal">659</span>
<span class="normal">660</span>
<span class="normal">661</span>
<span class="normal">662</span>
<span class="normal">663</span>
<span class="normal">664</span>
<span class="normal">665</span>
<span class="normal">666</span>
<span class="normal">667</span>
<span class="normal">668</span>
<span class="normal">669</span>
<span class="normal">670</span>
<span class="normal">671</span>
<span class="normal">672</span>
<span class="normal">673</span>
<span class="normal">674</span>
<span class="normal">675</span>
<span class="normal">676</span>
<span class="normal">677</span>
<span class="normal">678</span>
<span class="normal">679</span>
<span class="normal">680</span>
<span class="normal">681</span>
<span class="normal">682</span>
<span class="normal">683</span>
<span class="normal">684</span>
<span class="normal">685</span>
<span class="normal">686</span>
<span class="normal">687</span>
<span class="normal">688</span>
<span class="normal">689</span>
<span class="normal">690</span>
<span class="normal">691</span>
<span class="normal">692</span>
<span class="normal">693</span>
<span class="normal">694</span>
<span class="normal">695</span>
<span class="normal">696</span>
<span class="normal">697</span>
<span class="normal">698</span>
<span class="normal">699</span>
<span class="normal">700</span>
<span class="normal">701</span>
<span class="normal">702</span>
<span class="normal">703</span>
<span class="normal">704</span>
<span class="normal">705</span>
<span class="normal">706</span>
<span class="normal">707</span>
<span class="normal">708</span>
<span class="normal">709</span>
<span class="normal">710</span>
<span class="normal">711</span>
<span class="normal">712</span>
<span class="normal">713</span>
<span class="normal">714</span>
<span class="normal">715</span>
<span class="normal">716</span>
<span class="normal">717</span>
<span class="normal">718</span>
<span class="normal">719</span>
<span class="normal">720</span>
<span class="normal">721</span>
<span class="normal">722</span>
<span class="normal">723</span>
<span class="normal">724</span>
<span class="normal">725</span>
<span class="normal">726</span>
<span class="normal">727</span>
<span class="normal">728</span>
<span class="normal">729</span>
<span class="normal">730</span>
<span class="normal">731</span>
<span class="normal">732</span>
<span class="normal">733</span>
<span class="normal">734</span>
<span class="normal">735</span>
<span class="normal">736</span>
<span class="normal">737</span>
<span class="normal">738</span>
<span class="normal">739</span>
<span class="normal">740</span>
<span class="normal">741</span>
<span class="normal">742</span>
<span class="normal">743</span>
<span class="normal">744</span>
<span class="normal">745</span>
<span class="normal">746</span>
<span class="normal">747</span>
<span class="normal">748</span>
<span class="normal">749</span>
<span class="normal">750</span>
<span class="normal">751</span>
<span class="normal">752</span>
<span class="normal">753</span>
<span class="normal">754</span>
<span class="normal">755</span>
<span class="normal">756</span>
<span class="normal">757</span>
<span class="normal">758</span>
<span class="normal">759</span>
<span class="normal">760</span>
<span class="normal">761</span>
<span class="normal">762</span>
<span class="normal">763</span>
<span class="normal">764</span>
<span class="normal">765</span>
<span class="normal">766</span>
<span class="normal">767</span>
<span class="normal">768</span>
<span class="normal">769</span>
<span class="normal">770</span>
<span class="normal">771</span>
<span class="normal">772</span>
<span class="normal">773</span>
<span class="normal">774</span>
<span class="normal">775</span>
<span class="normal">776</span>
<span class="normal">777</span>
<span class="normal">778</span>
<span class="normal">779</span>
<span class="normal">780</span>
<span class="normal">781</span>
<span class="normal">782</span>
<span class="normal">783</span>
<span class="normal">784</span>
<span class="normal">785</span>
<span class="normal">786</span>
<span class="normal">787</span>
<span class="normal">788</span>
<span class="normal">789</span>
<span class="normal">790</span>
<span class="normal">791</span>
<span class="normal">792</span>
<span class="normal">793</span>
<span class="normal">794</span>
<span class="normal">795</span>
<span class="normal">796</span>
<span class="normal">797</span>
<span class="normal">798</span>
<span class="normal">799</span>
<span class="normal">800</span>
<span class="normal">801</span>
<span class="normal">802</span>
<span class="normal">803</span>
<span class="normal">804</span>
<span class="normal">805</span>
<span class="normal">806</span>
<span class="normal">807</span>
<span class="normal">808</span>
<span class="normal">809</span>
<span class="normal">810</span>
<span class="normal">811</span>
<span class="normal">812</span>
<span class="normal">813</span>
<span class="normal">814</span>
<span class="normal">815</span>
<span class="normal">816</span>
<span class="normal">817</span>
<span class="normal">818</span>
<span class="normal">819</span>
<span class="normal">820</span>
<span class="normal">821</span>
<span class="normal">822</span>
<span class="normal">823</span>
<span class="normal">824</span>
<span class="normal">825</span>
<span class="normal">826</span>
<span class="normal">827</span>
<span class="normal">828</span>
<span class="normal">829</span>
<span class="normal">830</span>
<span class="normal">831</span>
<span class="normal">832</span>
<span class="normal">833</span>
<span class="normal">834</span>
<span class="normal">835</span>
<span class="normal">836</span>
<span class="normal">837</span>
<span class="normal">838</span>
<span class="normal">839</span>
<span class="normal">840</span>
<span class="normal">841</span>
<span class="normal">842</span>
<span class="normal">843</span>
<span class="normal">844</span>
<span class="normal">845</span>
<span class="normal">846</span>
<span class="normal">847</span>
<span class="normal">848</span>
<span class="normal">849</span>
<span class="normal">850</span>
<span class="normal">851</span>
<span class="normal">852</span>
<span class="normal">853</span>
<span class="normal">854</span>
<span class="normal">855</span>
<span class="normal">856</span>
<span class="normal">857</span>
<span class="normal">858</span>
<span class="normal">859</span>
<span class="normal">860</span>
<span class="normal">861</span>
<span class="normal">862</span>
<span class="normal">863</span>
<span class="normal">864</span>
<span class="normal">865</span>
<span class="normal">866</span>
<span class="normal">867</span>
<span class="normal">868</span>
<span class="normal">869</span>
<span class="normal">870</span>
<span class="normal">871</span>
<span class="normal">872</span>
<span class="normal">873</span>
<span class="normal">874</span>
<span class="normal">875</span>
<span class="normal">876</span>
<span class="normal">877</span>
<span class="normal">878</span>
<span class="normal">879</span>
<span class="normal">880</span>
<span class="normal">881</span>
<span class="normal">882</span>
<span class="normal">883</span>
<span class="normal">884</span>
<span class="normal">885</span>
<span class="normal">886</span>
<span class="normal">887</span>
<span class="normal">888</span>
<span class="normal">889</span>
<span class="normal">890</span>
<span class="normal">891</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">Neo4jPropertyGraphStore</span><span class="p">(</span><span class="n">PropertyGraphStore</span><span class="p">):</span>
<span class="w">    </span><span class="sa">r</span><span class="sd">"""</span>
<span class="sd">    Neo4j Property Graph Store.</span>

<span class="sd">    This class implements a Neo4j property graph store.</span>

<span class="sd">    If you are using local Neo4j instead of aura, here's a helpful</span>
<span class="sd">    command for launching the docker container:</span>

<span class="sd">    ```bash</span>
<span class="sd">    docker run \</span>
<span class="sd">        -p 7474:7474 -p 7687:7687 \</span>
<span class="sd">        -v $PWD/data:/data -v $PWD/plugins:/plugins \</span>
<span class="sd">        --name neo4j-apoc \</span>
<span class="sd">        -e NEO4J_apoc_export_file_enabled=true \</span>
<span class="sd">        -e NEO4J_apoc_import_file_enabled=true \</span>
<span class="sd">        -e NEO4J_apoc_import_file_use__neo4j__config=true \</span>
<span class="sd">        -e NEO4JLABS_PLUGINS=\\[\"apoc\"\\] \</span>
<span class="sd">        neo4j:latest</span>
<span class="sd">    ```</span>

<span class="sd">    Args:</span>
<span class="sd">        username (str): The username for the Neo4j database.</span>
<span class="sd">        password (str): The password for the Neo4j database.</span>
<span class="sd">        url (str): The URL for the Neo4j database.</span>
<span class="sd">        database (Optional[str]): The name of the database to connect to. Defaults to "neo4j".</span>

<span class="sd">    Examples:</span>
<span class="sd">        `pip install llama-index-graph-stores-neo4j`</span>

<span class="sd">        ```python</span>
<span class="sd">        from llama_index.core.indices.property_graph import PropertyGraphIndex</span>
<span class="sd">        from llama_index.graph_stores.neo4j import Neo4jPropertyGraphStore</span>

<span class="sd">        # Create a Neo4jPropertyGraphStore instance</span>
<span class="sd">        graph_store = Neo4jPropertyGraphStore(</span>
<span class="sd">            username="neo4j",</span>
<span class="sd">            password="neo4j",</span>
<span class="sd">            url="bolt://localhost:7687",</span>
<span class="sd">            database="neo4j"</span>
<span class="sd">        )</span>

<span class="sd">        # create the index</span>
<span class="sd">        index = PropertyGraphIndex.from_documents(</span>
<span class="sd">            documents,</span>
<span class="sd">            property_graph_store=graph_store,</span>
<span class="sd">        )</span>
<span class="sd">        ```</span>
<span class="sd">    """</span>

    <span class="n">supports_structured_queries</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">supports_vector_queries</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">text_to_cypher_template</span><span class="p">:</span> <span class="n">PromptTemplate</span> <span class="o">=</span> <span class="n">DEFAULT_CYPHER_TEMPALTE</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">username</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">password</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">database</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"neo4j"</span><span class="p">,</span>
        <span class="n">refresh_schema</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">sanitize_query_output</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">enhanced_schema</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">neo4j_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">sanitize_query_output</span> <span class="o">=</span> <span class="n">sanitize_query_output</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">enhanced_schema</span> <span class="o">=</span> <span class="n">enhanced_schema</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span> <span class="o">=</span> <span class="n">neo4j</span><span class="o">.</span><span class="n">GraphDatabase</span><span class="o">.</span><span class="n">driver</span><span class="p">(</span>
            <span class="n">url</span><span class="p">,</span> <span class="n">auth</span><span class="o">=</span><span class="p">(</span><span class="n">username</span><span class="p">,</span> <span class="n">password</span><span class="p">),</span> <span class="o">**</span><span class="n">neo4j_kwargs</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_async_driver</span> <span class="o">=</span> <span class="n">neo4j</span><span class="o">.</span><span class="n">AsyncGraphDatabase</span><span class="o">.</span><span class="n">driver</span><span class="p">(</span>
            <span class="n">url</span><span class="p">,</span>
            <span class="n">auth</span><span class="o">=</span><span class="p">(</span><span class="n">username</span><span class="p">,</span> <span class="n">password</span><span class="p">),</span>
            <span class="o">**</span><span class="n">neo4j_kwargs</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_database</span> <span class="o">=</span> <span class="n">database</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">structured_schema</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">if</span> <span class="n">refresh_schema</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">refresh_schema</span><span class="p">()</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span>

    <span class="k">def</span> <span class="nf">refresh_schema</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Refresh the schema."""</span>
        <span class="n">node_query_results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
            <span class="n">node_properties_query</span><span class="p">,</span>
            <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"EXCLUDED_LABELS"</span><span class="p">:</span> <span class="p">[</span><span class="o">*</span><span class="n">EXCLUDED_LABELS</span><span class="p">,</span> <span class="n">BASE_ENTITY_LABEL</span><span class="p">]},</span>
        <span class="p">)</span>
        <span class="n">node_properties</span> <span class="o">=</span> <span class="p">(</span>
            <span class="p">[</span><span class="n">el</span><span class="p">[</span><span class="s2">"output"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">node_query_results</span><span class="p">]</span> <span class="k">if</span> <span class="n">node_query_results</span> <span class="k">else</span> <span class="p">[]</span>
        <span class="p">)</span>

        <span class="n">rels_query_result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
            <span class="n">rel_properties_query</span><span class="p">,</span> <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"EXCLUDED_LABELS"</span><span class="p">:</span> <span class="n">EXCLUDED_RELS</span><span class="p">}</span>
        <span class="p">)</span>
        <span class="n">rel_properties</span> <span class="o">=</span> <span class="p">(</span>
            <span class="p">[</span><span class="n">el</span><span class="p">[</span><span class="s2">"output"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">rels_query_result</span><span class="p">]</span> <span class="k">if</span> <span class="n">rels_query_result</span> <span class="k">else</span> <span class="p">[]</span>
        <span class="p">)</span>

        <span class="n">rel_objs_query_result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
            <span class="n">rel_query</span><span class="p">,</span>
            <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"EXCLUDED_LABELS"</span><span class="p">:</span> <span class="p">[</span><span class="o">*</span><span class="n">EXCLUDED_LABELS</span><span class="p">,</span> <span class="n">BASE_ENTITY_LABEL</span><span class="p">]},</span>
        <span class="p">)</span>
        <span class="n">relationships</span> <span class="o">=</span> <span class="p">(</span>
            <span class="p">[</span><span class="n">el</span><span class="p">[</span><span class="s2">"output"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">rel_objs_query_result</span><span class="p">]</span>
            <span class="k">if</span> <span class="n">rel_objs_query_result</span>
            <span class="k">else</span> <span class="p">[]</span>
        <span class="p">)</span>

        <span class="c1"># Get constraints &amp; indexes</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">constraint</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span><span class="s2">"SHOW CONSTRAINTS"</span><span class="p">)</span>
            <span class="n">index</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
                <span class="s2">"CALL apoc.schema.nodes() YIELD label, properties, type, size, "</span>
                <span class="s2">"valuesSelectivity WHERE type = 'RANGE' RETURN *, "</span>
                <span class="s2">"size * valuesSelectivity as distinctValues"</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="p">(</span>
            <span class="n">neo4j</span><span class="o">.</span><span class="n">exceptions</span><span class="o">.</span><span class="n">ClientError</span>
        <span class="p">):</span>  <span class="c1"># Read-only user might not have access to schema information</span>
            <span class="n">constraint</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="n">index</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">structured_schema</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"node_props"</span><span class="p">:</span> <span class="p">{</span><span class="n">el</span><span class="p">[</span><span class="s2">"labels"</span><span class="p">]:</span> <span class="n">el</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">node_properties</span><span class="p">},</span>
            <span class="s2">"rel_props"</span><span class="p">:</span> <span class="p">{</span><span class="n">el</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]:</span> <span class="n">el</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">rel_properties</span><span class="p">},</span>
            <span class="s2">"relationships"</span><span class="p">:</span> <span class="n">relationships</span><span class="p">,</span>
            <span class="s2">"metadata"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"constraint"</span><span class="p">:</span> <span class="n">constraint</span><span class="p">,</span> <span class="s2">"index"</span><span class="p">:</span> <span class="n">index</span><span class="p">},</span>
        <span class="p">}</span>
        <span class="n">schema_counts</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
            <span class="s2">"CALL apoc.meta.graphSample() YIELD nodes, relationships "</span>
            <span class="s2">"RETURN nodes, [rel in relationships | {name:apoc.any.property"</span>
            <span class="s2">"(rel, 'type'), count: apoc.any.property(rel, 'count')}]"</span>
            <span class="s2">" AS relationships"</span>
        <span class="p">)</span>
        <span class="c1"># Update node info</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">schema_counts</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"nodes"</span><span class="p">,</span> <span class="p">[]):</span>
            <span class="c1"># Skip bloom labels</span>
            <span class="k">if</span> <span class="n">node</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span> <span class="ow">in</span> <span class="n">EXCLUDED_LABELS</span><span class="p">:</span>
                <span class="k">continue</span>
            <span class="n">node_props</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_schema</span><span class="p">[</span><span class="s2">"node_props"</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">node</span><span class="p">[</span><span class="s2">"name"</span><span class="p">])</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">node_props</span><span class="p">:</span>  <span class="c1"># The node has no properties</span>
                <span class="k">continue</span>
            <span class="n">enhanced_cypher</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_enhanced_schema_cypher</span><span class="p">(</span>
                <span class="n">node</span><span class="p">[</span><span class="s2">"name"</span><span class="p">],</span> <span class="n">node_props</span><span class="p">,</span> <span class="n">node</span><span class="p">[</span><span class="s2">"count"</span><span class="p">]</span> <span class="o">&lt;</span> <span class="n">EXHAUSTIVE_SEARCH_LIMIT</span>
            <span class="p">)</span>
            <span class="n">enhanced_info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span><span class="n">enhanced_cypher</span><span class="p">)[</span><span class="mi">0</span><span class="p">][</span><span class="s2">"output"</span><span class="p">]</span>
            <span class="k">for</span> <span class="n">prop</span> <span class="ow">in</span> <span class="n">node_props</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">prop</span><span class="p">[</span><span class="s2">"property"</span><span class="p">]</span> <span class="ow">in</span> <span class="n">enhanced_info</span><span class="p">:</span>
                    <span class="n">prop</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">enhanced_info</span><span class="p">[</span><span class="n">prop</span><span class="p">[</span><span class="s2">"property"</span><span class="p">]])</span>
        <span class="c1"># Update rel info</span>
        <span class="k">for</span> <span class="n">rel</span> <span class="ow">in</span> <span class="n">schema_counts</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"relationships"</span><span class="p">,</span> <span class="p">[]):</span>
            <span class="c1"># Skip bloom labels</span>
            <span class="k">if</span> <span class="n">rel</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span> <span class="ow">in</span> <span class="n">EXCLUDED_RELS</span><span class="p">:</span>
                <span class="k">continue</span>
            <span class="n">rel_props</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_schema</span><span class="p">[</span><span class="s2">"rel_props"</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">rel</span><span class="p">[</span><span class="s2">"name"</span><span class="p">])</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">rel_props</span><span class="p">:</span>  <span class="c1"># The rel has no properties</span>
                <span class="k">continue</span>
            <span class="n">enhanced_cypher</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_enhanced_schema_cypher</span><span class="p">(</span>
                <span class="n">rel</span><span class="p">[</span><span class="s2">"name"</span><span class="p">],</span>
                <span class="n">rel_props</span><span class="p">,</span>
                <span class="n">rel</span><span class="p">[</span><span class="s2">"count"</span><span class="p">]</span> <span class="o">&lt;</span> <span class="n">EXHAUSTIVE_SEARCH_LIMIT</span><span class="p">,</span>
                <span class="n">is_relationship</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">enhanced_info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span><span class="n">enhanced_cypher</span><span class="p">)[</span><span class="mi">0</span><span class="p">][</span><span class="s2">"output"</span><span class="p">]</span>
                <span class="k">for</span> <span class="n">prop</span> <span class="ow">in</span> <span class="n">rel_props</span><span class="p">:</span>
                    <span class="k">if</span> <span class="n">prop</span><span class="p">[</span><span class="s2">"property"</span><span class="p">]</span> <span class="ow">in</span> <span class="n">enhanced_info</span><span class="p">:</span>
                        <span class="n">prop</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">enhanced_info</span><span class="p">[</span><span class="n">prop</span><span class="p">[</span><span class="s2">"property"</span><span class="p">]])</span>
            <span class="k">except</span> <span class="n">neo4j</span><span class="o">.</span><span class="n">exceptions</span><span class="o">.</span><span class="n">ClientError</span><span class="p">:</span>
                <span class="c1"># Sometimes the types are not consistent in the db</span>
                <span class="k">pass</span>

    <span class="k">def</span> <span class="nf">upsert_nodes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">LabelledNode</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="c1"># Lists to hold separated types</span>
        <span class="n">entity_dicts</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">chunk_dicts</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="c1"># Sort by type</span>
        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="n">EntityNode</span><span class="p">):</span>
                <span class="n">entity_dicts</span><span class="o">.</span><span class="n">append</span><span class="p">({</span><span class="o">**</span><span class="n">item</span><span class="o">.</span><span class="n">dict</span><span class="p">(),</span> <span class="s2">"id"</span><span class="p">:</span> <span class="n">item</span><span class="o">.</span><span class="n">id</span><span class="p">})</span>
            <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="n">ChunkNode</span><span class="p">):</span>
                <span class="n">chunk_dicts</span><span class="o">.</span><span class="n">append</span><span class="p">({</span><span class="o">**</span><span class="n">item</span><span class="o">.</span><span class="n">dict</span><span class="p">(),</span> <span class="s2">"id"</span><span class="p">:</span> <span class="n">item</span><span class="o">.</span><span class="n">id</span><span class="p">})</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="c1"># Log that we do not support these types of nodes</span>
                <span class="c1"># Or raise an error?</span>
                <span class="k">pass</span>

        <span class="k">if</span> <span class="n">chunk_dicts</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
<span class="w">                </span><span class="sd">"""</span>
<span class="sd">                UNWIND $data AS row</span>
<span class="sd">                MERGE (c:Chunk {id: row.id})</span>
<span class="sd">                SET c.text = row.text</span>
<span class="sd">                WITH c, row</span>
<span class="sd">                SET c += row.properties</span>
<span class="sd">                WITH c, row.embedding AS embedding</span>
<span class="sd">                WHERE embedding IS NOT NULL</span>
<span class="sd">                CALL db.create.setNodeVectorProperty(c, 'embedding', embedding)</span>
<span class="sd">                RETURN count(*)</span>
<span class="sd">                """</span><span class="p">,</span>
                <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"data"</span><span class="p">:</span> <span class="n">chunk_dicts</span><span class="p">},</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="n">entity_dicts</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
<span class="w">                </span><span class="sd">"""</span>
<span class="sd">                UNWIND $data AS row</span>
<span class="sd">                MERGE (e:`__Entity__` {id: row.id})</span>
<span class="sd">                SET e += apoc.map.clean(row.properties, [], [])</span>
<span class="sd">                SET e.name = row.name</span>
<span class="sd">                WITH e, row</span>
<span class="sd">                CALL apoc.create.addLabels(e, [row.label])</span>
<span class="sd">                YIELD node</span>
<span class="sd">                WITH e, row</span>
<span class="sd">                CALL {</span>
<span class="sd">                    WITH e, row</span>
<span class="sd">                    WITH e, row</span>
<span class="sd">                    WHERE row.embedding IS NOT NULL</span>
<span class="sd">                    CALL db.create.setNodeVectorProperty(e, 'embedding', row.embedding)</span>
<span class="sd">                    RETURN count(*) AS count</span>
<span class="sd">                }</span>
<span class="sd">                WITH e, row WHERE row.properties.triplet_source_id IS NOT NULL</span>
<span class="sd">                MERGE (c:Chunk {id: row.properties.triplet_source_id})</span>
<span class="sd">                MERGE (e)&lt;-[:MENTIONS]-(c)</span>
<span class="sd">                """</span><span class="p">,</span>
                <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"data"</span><span class="p">:</span> <span class="n">entity_dicts</span><span class="p">},</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">upsert_relations</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">relations</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Relation</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Add relations."""</span>
        <span class="n">params</span> <span class="o">=</span> <span class="p">[</span><span class="n">r</span><span class="o">.</span><span class="n">dict</span><span class="p">()</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">relations</span><span class="p">]</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
<span class="w">            </span><span class="sd">"""</span>
<span class="sd">            UNWIND $data AS row</span>
<span class="sd">            MERGE (source {id: row.source_id})</span>
<span class="sd">            ON CREATE SET source:Chunk</span>
<span class="sd">            MERGE (target {id: row.target_id})</span>
<span class="sd">            ON CREATE SET target:Chunk</span>
<span class="sd">            WITH source, target, row</span>
<span class="sd">            CALL apoc.merge.relationship(source, row.label, {}, row.properties, target) YIELD rel</span>
<span class="sd">            RETURN count(*)</span>
<span class="sd">            """</span><span class="p">,</span>
            <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"data"</span><span class="p">:</span> <span class="n">params</span><span class="p">},</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">properties</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">LabelledNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get nodes."""</span>
        <span class="n">cypher_statement</span> <span class="o">=</span> <span class="s2">"MATCH (e) "</span>

        <span class="n">params</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">if</span> <span class="n">properties</span> <span class="ow">or</span> <span class="n">ids</span><span class="p">:</span>
            <span class="n">cypher_statement</span> <span class="o">+=</span> <span class="s2">"WHERE "</span>

        <span class="k">if</span> <span class="n">ids</span><span class="p">:</span>
            <span class="n">cypher_statement</span> <span class="o">+=</span> <span class="s2">"e.id in $ids "</span>
            <span class="n">params</span><span class="p">[</span><span class="s2">"ids"</span><span class="p">]</span> <span class="o">=</span> <span class="n">ids</span>

        <span class="k">if</span> <span class="n">properties</span><span class="p">:</span>
            <span class="n">prop_list</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">prop</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">properties</span><span class="p">):</span>
                <span class="n">prop_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"e.`</span><span class="si">{</span><span class="n">prop</span><span class="si">}</span><span class="s2">` = $property_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
                <span class="n">params</span><span class="p">[</span><span class="sa">f</span><span class="s2">"property_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">"</span><span class="p">]</span> <span class="o">=</span> <span class="n">properties</span><span class="p">[</span><span class="n">prop</span><span class="p">]</span>
            <span class="n">cypher_statement</span> <span class="o">+=</span> <span class="s2">" AND "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">prop_list</span><span class="p">)</span>

        <span class="n">return_statement</span> <span class="o">=</span> <span class="s2">"""</span>
<span class="s2">        WITH e</span>
<span class="s2">        RETURN e.id AS name,</span>
<span class="s2">               [l in labels(e) WHERE l &lt;&gt; '__Entity__' | l][0] AS type,</span>
<span class="s2">               e{.* , embedding: Null, id: Null} AS properties</span>
<span class="s2">        """</span>
        <span class="n">cypher_statement</span> <span class="o">+=</span> <span class="n">return_statement</span>

        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span><span class="n">cypher_statement</span><span class="p">,</span> <span class="n">param_map</span><span class="o">=</span><span class="n">params</span><span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">response</span> <span class="k">if</span> <span class="n">response</span> <span class="k">else</span> <span class="p">[]</span>

        <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">record</span> <span class="ow">in</span> <span class="n">response</span><span class="p">:</span>
            <span class="c1"># text indicates a chunk node</span>
            <span class="c1"># none on the type indicates an implicit node, likely a chunk node</span>
            <span class="k">if</span> <span class="s2">"text"</span> <span class="ow">in</span> <span class="n">record</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]</span> <span class="ow">or</span> <span class="n">record</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">text</span> <span class="o">=</span> <span class="n">record</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"text"</span><span class="p">,</span> <span class="s2">""</span><span class="p">)</span>
                <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">ChunkNode</span><span class="p">(</span>
                        <span class="n">id_</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"name"</span><span class="p">],</span>
                        <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
                        <span class="n">properties</span><span class="o">=</span><span class="n">remove_empty_values</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]),</span>
                    <span class="p">)</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">EntityNode</span><span class="p">(</span>
                        <span class="n">name</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"name"</span><span class="p">],</span>
                        <span class="n">label</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"type"</span><span class="p">],</span>
                        <span class="n">properties</span><span class="o">=</span><span class="n">remove_empty_values</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]),</span>
                    <span class="p">)</span>
                <span class="p">)</span>

        <span class="k">return</span> <span class="n">nodes</span>

    <span class="k">def</span> <span class="nf">get_triplets</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">entity_names</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">relation_names</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">properties</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Triplet</span><span class="p">]:</span>
        <span class="c1"># TODO: handle ids of chunk nodes</span>
        <span class="n">cypher_statement</span> <span class="o">=</span> <span class="s2">"MATCH (e:`__Entity__`) "</span>

        <span class="n">params</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">if</span> <span class="n">entity_names</span> <span class="ow">or</span> <span class="n">properties</span> <span class="ow">or</span> <span class="n">ids</span><span class="p">:</span>
            <span class="n">cypher_statement</span> <span class="o">+=</span> <span class="s2">"WHERE "</span>

        <span class="k">if</span> <span class="n">entity_names</span><span class="p">:</span>
            <span class="n">cypher_statement</span> <span class="o">+=</span> <span class="s2">"e.name in $entity_names "</span>
            <span class="n">params</span><span class="p">[</span><span class="s2">"entity_names"</span><span class="p">]</span> <span class="o">=</span> <span class="n">entity_names</span>

        <span class="k">if</span> <span class="n">ids</span><span class="p">:</span>
            <span class="n">cypher_statement</span> <span class="o">+=</span> <span class="s2">"e.id in $ids "</span>
            <span class="n">params</span><span class="p">[</span><span class="s2">"ids"</span><span class="p">]</span> <span class="o">=</span> <span class="n">ids</span>

        <span class="k">if</span> <span class="n">properties</span><span class="p">:</span>
            <span class="n">prop_list</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">prop</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">properties</span><span class="p">):</span>
                <span class="n">prop_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"e.`</span><span class="si">{</span><span class="n">prop</span><span class="si">}</span><span class="s2">` = $property_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
                <span class="n">params</span><span class="p">[</span><span class="sa">f</span><span class="s2">"property_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">"</span><span class="p">]</span> <span class="o">=</span> <span class="n">properties</span><span class="p">[</span><span class="n">prop</span><span class="p">]</span>
            <span class="n">cypher_statement</span> <span class="o">+=</span> <span class="s2">" AND "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">prop_list</span><span class="p">)</span>

        <span class="n">return_statement</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"""</span>
<span class="s2">        WITH e</span>
<span class="s2">        CALL </span><span class="se">{{</span>
<span class="s2">            WITH e</span>
<span class="s2">            MATCH (e)-[r</span><span class="si">{</span><span class="s1">':`'</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="s1">'`|`'</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">relation_names</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="s1">'`'</span><span class="w"> </span><span class="k">if</span><span class="w"> </span><span class="n">relation_names</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="s1">''</span><span class="si">}</span><span class="s2">]-&gt;(t)</span>
<span class="s2">            RETURN e.name AS source_id, [l in labels(e) WHERE l &lt;&gt; '__Entity__' | l][0] AS source_type,</span>
<span class="s2">                   e</span><span class="se">{{</span><span class="s2">.* , embedding: Null, name: Null</span><span class="se">}}</span><span class="s2"> AS source_properties,</span>
<span class="s2">                   type(r) AS type,</span>
<span class="s2">                   t.name AS target_id, [l in labels(t) WHERE l &lt;&gt; '__Entity__' | l][0] AS target_type,</span>
<span class="s2">                   t</span><span class="se">{{</span><span class="s2">.* , embedding: Null, name: Null</span><span class="se">}}</span><span class="s2"> AS target_properties</span>
<span class="s2">            UNION ALL</span>
<span class="s2">            WITH e</span>
<span class="s2">            MATCH (e)&lt;-[r</span><span class="si">{</span><span class="s1">':`'</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="s1">'`|`'</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">relation_names</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="s1">'`'</span><span class="w"> </span><span class="k">if</span><span class="w"> </span><span class="n">relation_names</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="s1">''</span><span class="si">}</span><span class="s2">]-(t)</span>
<span class="s2">            RETURN t.name AS source_id, [l in labels(t) WHERE l &lt;&gt; '__Entity__' | l][0] AS source_type,</span>
<span class="s2">                   e</span><span class="se">{{</span><span class="s2">.* , embedding: Null, name: Null</span><span class="se">}}</span><span class="s2"> AS source_properties,</span>
<span class="s2">                   type(r) AS type,</span>
<span class="s2">                   e.name AS target_id, [l in labels(e) WHERE l &lt;&gt; '__Entity__' | l][0] AS target_type,</span>
<span class="s2">                   t</span><span class="se">{{</span><span class="s2">.* , embedding: Null, name: Null</span><span class="se">}}</span><span class="s2"> AS target_properties</span>
<span class="s2">        </span><span class="se">}}</span>
<span class="s2">        RETURN source_id, source_type, type, target_id, target_type, source_properties, target_properties"""</span>
        <span class="n">cypher_statement</span> <span class="o">+=</span> <span class="n">return_statement</span>

        <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span><span class="n">cypher_statement</span><span class="p">,</span> <span class="n">param_map</span><span class="o">=</span><span class="n">params</span><span class="p">)</span>
        <span class="n">data</span> <span class="o">=</span> <span class="n">data</span> <span class="k">if</span> <span class="n">data</span> <span class="k">else</span> <span class="p">[]</span>

        <span class="n">triples</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">record</span> <span class="ow">in</span> <span class="n">data</span><span class="p">:</span>
            <span class="n">source</span> <span class="o">=</span> <span class="n">EntityNode</span><span class="p">(</span>
                <span class="n">name</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"source_id"</span><span class="p">],</span>
                <span class="n">label</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"source_type"</span><span class="p">],</span>
                <span class="n">properties</span><span class="o">=</span><span class="n">remove_empty_values</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"source_properties"</span><span class="p">]),</span>
            <span class="p">)</span>
            <span class="n">target</span> <span class="o">=</span> <span class="n">EntityNode</span><span class="p">(</span>
                <span class="n">name</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"target_id"</span><span class="p">],</span>
                <span class="n">label</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"target_type"</span><span class="p">],</span>
                <span class="n">properties</span><span class="o">=</span><span class="n">remove_empty_values</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"target_properties"</span><span class="p">]),</span>
            <span class="p">)</span>
            <span class="n">rel</span> <span class="o">=</span> <span class="n">Relation</span><span class="p">(</span>
                <span class="n">source_id</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"source_id"</span><span class="p">],</span>
                <span class="n">target_id</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"target_id"</span><span class="p">],</span>
                <span class="n">label</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"type"</span><span class="p">],</span>
            <span class="p">)</span>
            <span class="n">triples</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="n">source</span><span class="p">,</span> <span class="n">rel</span><span class="p">,</span> <span class="n">target</span><span class="p">])</span>
        <span class="k">return</span> <span class="n">triples</span>

    <span class="k">def</span> <span class="nf">get_rel_map</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">graph_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">LabelledNode</span><span class="p">],</span>
        <span class="n">depth</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span>
        <span class="n">limit</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">30</span><span class="p">,</span>
        <span class="n">ignore_rels</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Triplet</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get depth-aware rel map."""</span>
        <span class="n">triples</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="n">ids</span> <span class="o">=</span> <span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">id</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">graph_nodes</span><span class="p">]</span>
        <span class="c1"># Needs some optimization</span>
        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"""</span>
<span class="s2">            WITH $ids AS id_list</span>
<span class="s2">            UNWIND range(0, size(id_list) - 1) AS idx</span>
<span class="s2">            MATCH (e:`__Entity__`)</span>
<span class="s2">            WHERE e.id = id_list[idx]</span>
<span class="s2">            MATCH p=(e)-[r*1..</span><span class="si">{</span><span class="n">depth</span><span class="si">}</span><span class="s2">]-(other)</span>
<span class="s2">            WHERE ALL(rel in relationships(p) WHERE type(rel) &lt;&gt; 'MENTIONS')</span>
<span class="s2">            UNWIND relationships(p) AS rel</span>
<span class="s2">            WITH distinct rel, idx</span>
<span class="s2">            WITH startNode(rel) AS source,</span>
<span class="s2">                type(rel) AS type,</span>
<span class="s2">                endNode(rel) AS endNode,</span>
<span class="s2">                idx</span>
<span class="s2">            LIMIT toInteger($limit)</span>
<span class="s2">            RETURN source.id AS source_id, [l in labels(source) WHERE l &lt;&gt; '__Entity__' | l][0] AS source_type,</span>
<span class="s2">                source</span><span class="se">{{</span><span class="s2">.* , embedding: Null, id: Null</span><span class="se">}}</span><span class="s2"> AS source_properties,</span>
<span class="s2">                type,</span>
<span class="s2">                endNode.id AS target_id, [l in labels(endNode) WHERE l &lt;&gt; '__Entity__' | l][0] AS target_type,</span>
<span class="s2">                endNode</span><span class="se">{{</span><span class="s2">.* , embedding: Null, id: Null</span><span class="se">}}</span><span class="s2"> AS target_properties,</span>
<span class="s2">                idx</span>
<span class="s2">            ORDER BY idx</span>
<span class="s2">            LIMIT toInteger($limit)</span>
<span class="s2">            """</span><span class="p">,</span>
            <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"ids"</span><span class="p">:</span> <span class="n">ids</span><span class="p">,</span> <span class="s2">"limit"</span><span class="p">:</span> <span class="n">limit</span><span class="p">},</span>
        <span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">response</span> <span class="k">if</span> <span class="n">response</span> <span class="k">else</span> <span class="p">[]</span>

        <span class="n">ignore_rels</span> <span class="o">=</span> <span class="n">ignore_rels</span> <span class="ow">or</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">record</span> <span class="ow">in</span> <span class="n">response</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">record</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]</span> <span class="ow">in</span> <span class="n">ignore_rels</span><span class="p">:</span>
                <span class="k">continue</span>

            <span class="n">source</span> <span class="o">=</span> <span class="n">EntityNode</span><span class="p">(</span>
                <span class="n">name</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"source_id"</span><span class="p">],</span>
                <span class="n">label</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"source_type"</span><span class="p">],</span>
                <span class="n">properties</span><span class="o">=</span><span class="n">remove_empty_values</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"source_properties"</span><span class="p">]),</span>
            <span class="p">)</span>
            <span class="n">target</span> <span class="o">=</span> <span class="n">EntityNode</span><span class="p">(</span>
                <span class="n">name</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"target_id"</span><span class="p">],</span>
                <span class="n">label</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"target_type"</span><span class="p">],</span>
                <span class="n">properties</span><span class="o">=</span><span class="n">remove_empty_values</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"target_properties"</span><span class="p">]),</span>
            <span class="p">)</span>
            <span class="n">rel</span> <span class="o">=</span> <span class="n">Relation</span><span class="p">(</span>
                <span class="n">source_id</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"source_id"</span><span class="p">],</span>
                <span class="n">target_id</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"target_id"</span><span class="p">],</span>
                <span class="n">label</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"type"</span><span class="p">],</span>
            <span class="p">)</span>
            <span class="n">triples</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="n">source</span><span class="p">,</span> <span class="n">rel</span><span class="p">,</span> <span class="n">target</span><span class="p">])</span>

        <span class="k">return</span> <span class="n">triples</span>

    <span class="k">def</span> <span class="nf">structured_query</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">param_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
        <span class="n">param_map</span> <span class="o">=</span> <span class="n">param_map</span> <span class="ow">or</span> <span class="p">{}</span>

        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span><span class="o">.</span><span class="n">session</span><span class="p">(</span><span class="n">database</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_database</span><span class="p">)</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
            <span class="n">result</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">param_map</span><span class="p">)</span>
            <span class="n">full_result</span> <span class="o">=</span> <span class="p">[</span><span class="n">d</span><span class="o">.</span><span class="n">data</span><span class="p">()</span> <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">result</span><span class="p">]</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">sanitize_query_output</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">value_sanitize</span><span class="p">(</span><span class="n">full_result</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">full_result</span>

    <span class="k">def</span> <span class="nf">vector_query</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">LabelledNode</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Query the graph store with a vector store query."""</span>
        <span class="n">conditions</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">:</span>
            <span class="n">conditions</span> <span class="o">=</span> <span class="p">[</span>
                <span class="sa">f</span><span class="s2">"e.</span><span class="si">{</span><span class="nb">filter</span><span class="o">.</span><span class="n">key</span><span class="si">}</span><span class="s2"> </span><span class="si">{</span><span class="nb">filter</span><span class="o">.</span><span class="n">operator</span><span class="o">.</span><span class="n">value</span><span class="si">}</span><span class="s2"> </span><span class="si">{</span><span class="nb">filter</span><span class="o">.</span><span class="n">value</span><span class="si">}</span><span class="s2">"</span>
                <span class="k">for</span> <span class="nb">filter</span> <span class="ow">in</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="o">.</span><span class="n">filters</span>
            <span class="p">]</span>
        <span class="n">filters</span> <span class="o">=</span> <span class="p">(</span>
            <span class="sa">f</span><span class="s2">" </span><span class="si">{</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="o">.</span><span class="n">condition</span><span class="o">.</span><span class="n">value</span><span class="si">}</span><span class="s2"> "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">conditions</span><span class="p">)</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"=="</span><span class="p">,</span> <span class="s2">"="</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">conditions</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
            <span class="k">else</span> <span class="s2">"1 = 1"</span>
        <span class="p">)</span>

        <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"""MATCH (e:`__Entity__`)</span>
<span class="s2">            WHERE e.embedding IS NOT NULL AND size(e.embedding) = $dimension AND (</span><span class="si">{</span><span class="n">filters</span><span class="si">}</span><span class="s2">)</span>
<span class="s2">            WITH e, vector.similarity.cosine(e.embedding, $embedding) AS score</span>
<span class="s2">            ORDER BY score DESC LIMIT toInteger($limit)</span>
<span class="s2">            RETURN e.id AS name,</span>
<span class="s2">               [l in labels(e) WHERE l &lt;&gt; '__Entity__' | l][0] AS type,</span>
<span class="s2">               e</span><span class="se">{{</span><span class="s2">.* , embedding: Null, name: Null, id: Null</span><span class="se">}}</span><span class="s2"> AS properties,</span>
<span class="s2">               score"""</span><span class="p">,</span>
            <span class="n">param_map</span><span class="o">=</span><span class="p">{</span>
                <span class="s2">"embedding"</span><span class="p">:</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">,</span>
                <span class="s2">"dimension"</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">),</span>
                <span class="s2">"limit"</span><span class="p">:</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">)</span>
        <span class="n">data</span> <span class="o">=</span> <span class="n">data</span> <span class="k">if</span> <span class="n">data</span> <span class="k">else</span> <span class="p">[]</span>

        <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">scores</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">record</span> <span class="ow">in</span> <span class="n">data</span><span class="p">:</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">EntityNode</span><span class="p">(</span>
                <span class="n">name</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"name"</span><span class="p">],</span>
                <span class="n">label</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"type"</span><span class="p">],</span>
                <span class="n">properties</span><span class="o">=</span><span class="n">remove_empty_values</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]),</span>
            <span class="p">)</span>
            <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
            <span class="n">scores</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"score"</span><span class="p">])</span>

        <span class="k">return</span> <span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">scores</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">entity_names</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">relation_names</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">properties</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete matching data."""</span>
        <span class="k">if</span> <span class="n">entity_names</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
                <span class="s2">"MATCH (n) WHERE n.name IN $entity_names DETACH DELETE n"</span><span class="p">,</span>
                <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"entity_names"</span><span class="p">:</span> <span class="n">entity_names</span><span class="p">},</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="n">ids</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
                <span class="s2">"MATCH (n) WHERE n.id IN $ids DETACH DELETE n"</span><span class="p">,</span>
                <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"ids"</span><span class="p">:</span> <span class="n">ids</span><span class="p">},</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="n">relation_names</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">rel</span> <span class="ow">in</span> <span class="n">relation_names</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span><span class="sa">f</span><span class="s2">"MATCH ()-[r:`</span><span class="si">{</span><span class="n">rel</span><span class="si">}</span><span class="s2">`]-&gt;() DELETE r"</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">properties</span><span class="p">:</span>
            <span class="n">cypher</span> <span class="o">=</span> <span class="s2">"MATCH (e) WHERE "</span>
            <span class="n">prop_list</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="n">params</span> <span class="o">=</span> <span class="p">{}</span>
            <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">prop</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">properties</span><span class="p">):</span>
                <span class="n">prop_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"e.`</span><span class="si">{</span><span class="n">prop</span><span class="si">}</span><span class="s2">` = $property_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
                <span class="n">params</span><span class="p">[</span><span class="sa">f</span><span class="s2">"property_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">"</span><span class="p">]</span> <span class="o">=</span> <span class="n">properties</span><span class="p">[</span><span class="n">prop</span><span class="p">]</span>
            <span class="n">cypher</span> <span class="o">+=</span> <span class="s2">" AND "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">prop_list</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span><span class="n">cypher</span> <span class="o">+</span> <span class="s2">" DETACH DELETE e"</span><span class="p">,</span> <span class="n">param_map</span><span class="o">=</span><span class="n">params</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_enhanced_schema_cypher</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">label_or_type</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">properties</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]],</span>
        <span class="n">exhaustive</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span>
        <span class="n">is_relationship</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">is_relationship</span><span class="p">:</span>
            <span class="n">match_clause</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"MATCH ()-[n:`</span><span class="si">{</span><span class="n">label_or_type</span><span class="si">}</span><span class="s2">`]-&gt;()"</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">match_clause</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"MATCH (n:`</span><span class="si">{</span><span class="n">label_or_type</span><span class="si">}</span><span class="s2">`)"</span>

        <span class="n">with_clauses</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">return_clauses</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">output_dict</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">if</span> <span class="n">exhaustive</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">prop</span> <span class="ow">in</span> <span class="n">properties</span><span class="p">:</span>
                <span class="n">prop_name</span> <span class="o">=</span> <span class="n">prop</span><span class="p">[</span><span class="s2">"property"</span><span class="p">]</span>
                <span class="n">prop_type</span> <span class="o">=</span> <span class="n">prop</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]</span>
                <span class="k">if</span> <span class="n">prop_type</span> <span class="o">==</span> <span class="s2">"STRING"</span><span class="p">:</span>
                    <span class="n">with_clauses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"collect(distinct substring(toString(n.`</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">`), 0, 50)) "</span>
                        <span class="sa">f</span><span class="s2">"AS `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_values`"</span>
                    <span class="p">)</span>
                    <span class="n">return_clauses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"values:`</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_values`[..</span><span class="si">{</span><span class="n">DISTINCT_VALUE_LIMIT</span><span class="si">}</span><span class="s2">],"</span>
                        <span class="sa">f</span><span class="s2">" distinct_count: size(`</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_values`)"</span>
                    <span class="p">)</span>
                <span class="k">elif</span> <span class="n">prop_type</span> <span class="ow">in</span> <span class="p">[</span>
                    <span class="s2">"INTEGER"</span><span class="p">,</span>
                    <span class="s2">"FLOAT"</span><span class="p">,</span>
                    <span class="s2">"DATE"</span><span class="p">,</span>
                    <span class="s2">"DATE_TIME"</span><span class="p">,</span>
                    <span class="s2">"LOCAL_DATE_TIME"</span><span class="p">,</span>
                <span class="p">]:</span>
                    <span class="n">with_clauses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"min(n.`</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">`) AS `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_min`"</span><span class="p">)</span>
                    <span class="n">with_clauses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"max(n.`</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">`) AS `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_max`"</span><span class="p">)</span>
                    <span class="n">with_clauses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"count(distinct n.`</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">`) AS `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_distinct`"</span>
                    <span class="p">)</span>
                    <span class="n">return_clauses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"min: toString(`</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_min`), "</span>
                        <span class="sa">f</span><span class="s2">"max: toString(`</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_max`), "</span>
                        <span class="sa">f</span><span class="s2">"distinct_count: `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_distinct`"</span>
                    <span class="p">)</span>
                <span class="k">elif</span> <span class="n">prop_type</span> <span class="o">==</span> <span class="s2">"LIST"</span><span class="p">:</span>
                    <span class="n">with_clauses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"min(size(n.`</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">`)) AS `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_size_min`, "</span>
                        <span class="sa">f</span><span class="s2">"max(size(n.`</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">`)) AS `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_size_max`"</span>
                    <span class="p">)</span>
                    <span class="n">return_clauses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"min_size: `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_size_min`, "</span>
                        <span class="sa">f</span><span class="s2">"max_size: `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_size_max`"</span>
                    <span class="p">)</span>
                <span class="k">elif</span> <span class="n">prop_type</span> <span class="ow">in</span> <span class="p">[</span><span class="s2">"BOOLEAN"</span><span class="p">,</span> <span class="s2">"POINT"</span><span class="p">,</span> <span class="s2">"DURATION"</span><span class="p">]:</span>
                    <span class="k">continue</span>
                <span class="n">output_dict</span><span class="p">[</span><span class="n">prop_name</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"{"</span> <span class="o">+</span> <span class="n">return_clauses</span><span class="o">.</span><span class="n">pop</span><span class="p">()</span> <span class="o">+</span> <span class="s2">"}"</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># Just sample 5 random nodes</span>
            <span class="n">match_clause</span> <span class="o">+=</span> <span class="s2">" WITH n LIMIT 5"</span>
            <span class="k">for</span> <span class="n">prop</span> <span class="ow">in</span> <span class="n">properties</span><span class="p">:</span>
                <span class="n">prop_name</span> <span class="o">=</span> <span class="n">prop</span><span class="p">[</span><span class="s2">"property"</span><span class="p">]</span>
                <span class="n">prop_type</span> <span class="o">=</span> <span class="n">prop</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]</span>

                <span class="c1"># Check if indexed property, we can still do exhaustive</span>
                <span class="n">prop_index</span> <span class="o">=</span> <span class="p">[</span>
                    <span class="n">el</span>
                    <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_schema</span><span class="p">[</span><span class="s2">"metadata"</span><span class="p">][</span><span class="s2">"index"</span><span class="p">]</span>
                    <span class="k">if</span> <span class="n">el</span><span class="p">[</span><span class="s2">"label"</span><span class="p">]</span> <span class="o">==</span> <span class="n">label_or_type</span>
                    <span class="ow">and</span> <span class="n">el</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]</span> <span class="o">==</span> <span class="p">[</span><span class="n">prop_name</span><span class="p">]</span>
                    <span class="ow">and</span> <span class="n">el</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]</span> <span class="o">==</span> <span class="s2">"RANGE"</span>
                <span class="p">]</span>
                <span class="k">if</span> <span class="n">prop_type</span> <span class="o">==</span> <span class="s2">"STRING"</span><span class="p">:</span>
                    <span class="k">if</span> <span class="p">(</span>
                        <span class="n">prop_index</span>
                        <span class="ow">and</span> <span class="n">prop_index</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"size"</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span>
                        <span class="ow">and</span> <span class="n">prop_index</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"distinctValues"</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="n">DISTINCT_VALUE_LIMIT</span>
                    <span class="p">):</span>
                        <span class="n">distinct_values</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">query</span><span class="p">(</span>
                            <span class="sa">f</span><span class="s2">"CALL apoc.schema.properties.distinct("</span>
                            <span class="sa">f</span><span class="s2">"'</span><span class="si">{</span><span class="n">label_or_type</span><span class="si">}</span><span class="s2">', '</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">') YIELD value"</span>
                        <span class="p">)[</span><span class="mi">0</span><span class="p">][</span><span class="s2">"value"</span><span class="p">]</span>
                        <span class="n">return_clauses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                            <span class="sa">f</span><span class="s2">"values: </span><span class="si">{</span><span class="n">distinct_values</span><span class="si">}</span><span class="s2">,"</span>
                            <span class="sa">f</span><span class="s2">" distinct_count: </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">distinct_values</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span>
                        <span class="p">)</span>
                    <span class="k">else</span><span class="p">:</span>
                        <span class="n">with_clauses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                            <span class="sa">f</span><span class="s2">"collect(distinct substring(n.`</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">`, 0, 50)) "</span>
                            <span class="sa">f</span><span class="s2">"AS `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_values`"</span>
                        <span class="p">)</span>
                        <span class="n">return_clauses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"values: `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_values`"</span><span class="p">)</span>
                <span class="k">elif</span> <span class="n">prop_type</span> <span class="ow">in</span> <span class="p">[</span>
                    <span class="s2">"INTEGER"</span><span class="p">,</span>
                    <span class="s2">"FLOAT"</span><span class="p">,</span>
                    <span class="s2">"DATE"</span><span class="p">,</span>
                    <span class="s2">"DATE_TIME"</span><span class="p">,</span>
                    <span class="s2">"LOCAL_DATE_TIME"</span><span class="p">,</span>
                <span class="p">]:</span>
                    <span class="k">if</span> <span class="ow">not</span> <span class="n">prop_index</span><span class="p">:</span>
                        <span class="n">with_clauses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                            <span class="sa">f</span><span class="s2">"collect(distinct toString(n.`</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">`)) "</span>
                            <span class="sa">f</span><span class="s2">"AS `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_values`"</span>
                        <span class="p">)</span>
                        <span class="n">return_clauses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"values: `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_values`"</span><span class="p">)</span>
                    <span class="k">else</span><span class="p">:</span>
                        <span class="n">with_clauses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                            <span class="sa">f</span><span class="s2">"min(n.`</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">`) AS `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_min`"</span>
                        <span class="p">)</span>
                        <span class="n">with_clauses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                            <span class="sa">f</span><span class="s2">"max(n.`</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">`) AS `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_max`"</span>
                        <span class="p">)</span>
                        <span class="n">with_clauses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                            <span class="sa">f</span><span class="s2">"count(distinct n.`</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">`) AS `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_distinct`"</span>
                        <span class="p">)</span>
                        <span class="n">return_clauses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                            <span class="sa">f</span><span class="s2">"min: toString(`</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_min`), "</span>
                            <span class="sa">f</span><span class="s2">"max: toString(`</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_max`), "</span>
                            <span class="sa">f</span><span class="s2">"distinct_count: `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_distinct`"</span>
                        <span class="p">)</span>

                <span class="k">elif</span> <span class="n">prop_type</span> <span class="o">==</span> <span class="s2">"LIST"</span><span class="p">:</span>
                    <span class="n">with_clauses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"min(size(n.`</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">`)) AS `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_size_min`, "</span>
                        <span class="sa">f</span><span class="s2">"max(size(n.`</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">`)) AS `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_size_max`"</span>
                    <span class="p">)</span>
                    <span class="n">return_clauses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"min_size: `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_size_min`, "</span>
                        <span class="sa">f</span><span class="s2">"max_size: `</span><span class="si">{</span><span class="n">prop_name</span><span class="si">}</span><span class="s2">_size_max`"</span>
                    <span class="p">)</span>
                <span class="k">elif</span> <span class="n">prop_type</span> <span class="ow">in</span> <span class="p">[</span><span class="s2">"BOOLEAN"</span><span class="p">,</span> <span class="s2">"POINT"</span><span class="p">,</span> <span class="s2">"DURATION"</span><span class="p">]:</span>
                    <span class="k">continue</span>

                <span class="n">output_dict</span><span class="p">[</span><span class="n">prop_name</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"{"</span> <span class="o">+</span> <span class="n">return_clauses</span><span class="o">.</span><span class="n">pop</span><span class="p">()</span> <span class="o">+</span> <span class="s2">"}"</span>

        <span class="n">with_clause</span> <span class="o">=</span> <span class="s2">"WITH "</span> <span class="o">+</span> <span class="s2">",</span><span class="se">\n</span><span class="s2">     "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">with_clauses</span><span class="p">)</span>
        <span class="n">return_clause</span> <span class="o">=</span> <span class="p">(</span>
            <span class="s2">"RETURN {"</span>
            <span class="o">+</span> <span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="sa">f</span><span class="s2">"`</span><span class="si">{</span><span class="n">k</span><span class="si">}</span><span class="s2">`: </span><span class="si">{</span><span class="n">v</span><span class="si">}</span><span class="s2">"</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">output_dict</span><span class="o">.</span><span class="n">items</span><span class="p">())</span>
            <span class="o">+</span> <span class="s2">"} AS output"</span>
        <span class="p">)</span>

        <span class="c1"># Combine all parts of the Cypher query</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">match_clause</span><span class="si">}</span><span class="se">\n</span><span class="si">{</span><span class="n">with_clause</span><span class="si">}</span><span class="se">\n</span><span class="si">{</span><span class="n">return_clause</span><span class="si">}</span><span class="s2">"</span>

    <span class="k">def</span> <span class="nf">get_schema</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">refresh</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">refresh</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">refresh_schema</span><span class="p">()</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_schema</span>

    <span class="k">def</span> <span class="nf">get_schema_str</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">refresh</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">schema</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_schema</span><span class="p">(</span><span class="n">refresh</span><span class="o">=</span><span class="n">refresh</span><span class="p">)</span>

        <span class="n">formatted_node_props</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">formatted_rel_props</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">enhanced_schema</span><span class="p">:</span>
            <span class="c1"># Enhanced formatting for nodes</span>
            <span class="k">for</span> <span class="n">node_type</span><span class="p">,</span> <span class="n">properties</span> <span class="ow">in</span> <span class="n">schema</span><span class="p">[</span><span class="s2">"node_props"</span><span class="p">]</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                <span class="n">formatted_node_props</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"- **</span><span class="si">{</span><span class="n">node_type</span><span class="si">}</span><span class="s2">**"</span><span class="p">)</span>
                <span class="k">for</span> <span class="n">prop</span> <span class="ow">in</span> <span class="n">properties</span><span class="p">:</span>
                    <span class="n">example</span> <span class="o">=</span> <span class="s2">""</span>
                    <span class="k">if</span> <span class="n">prop</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]</span> <span class="o">==</span> <span class="s2">"STRING"</span> <span class="ow">and</span> <span class="n">prop</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"values"</span><span class="p">):</span>
                        <span class="k">if</span> <span class="n">prop</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"distinct_count"</span><span class="p">,</span> <span class="mi">11</span><span class="p">)</span> <span class="o">&gt;</span> <span class="n">DISTINCT_VALUE_LIMIT</span><span class="p">:</span>
                            <span class="n">example</span> <span class="o">=</span> <span class="p">(</span>
                                <span class="sa">f</span><span class="s1">'Example: "</span><span class="si">{</span><span class="n">clean_string_values</span><span class="p">(</span><span class="n">prop</span><span class="p">[</span><span class="s2">"values"</span><span class="p">][</span><span class="mi">0</span><span class="p">])</span><span class="si">}</span><span class="s1">"'</span>
                                <span class="k">if</span> <span class="n">prop</span><span class="p">[</span><span class="s2">"values"</span><span class="p">]</span>
                                <span class="k">else</span> <span class="s2">""</span>
                            <span class="p">)</span>
                        <span class="k">else</span><span class="p">:</span>  <span class="c1"># If less than 10 possible values return all</span>
                            <span class="n">example</span> <span class="o">=</span> <span class="p">(</span>
                                <span class="p">(</span>
                                    <span class="s2">"Available options: "</span>
                                    <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="p">[</span><span class="n">clean_string_values</span><span class="p">(</span><span class="n">el</span><span class="p">)</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">el</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="n">prop</span><span class="p">[</span><span class="s2">"values"</span><span class="p">]]</span><span class="si">}</span><span class="s1">'</span>
                                <span class="p">)</span>
                                <span class="k">if</span> <span class="n">prop</span><span class="p">[</span><span class="s2">"values"</span><span class="p">]</span>
                                <span class="k">else</span> <span class="s2">""</span>
                            <span class="p">)</span>

                    <span class="k">elif</span> <span class="n">prop</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]</span> <span class="ow">in</span> <span class="p">[</span>
                        <span class="s2">"INTEGER"</span><span class="p">,</span>
                        <span class="s2">"FLOAT"</span><span class="p">,</span>
                        <span class="s2">"DATE"</span><span class="p">,</span>
                        <span class="s2">"DATE_TIME"</span><span class="p">,</span>
                        <span class="s2">"LOCAL_DATE_TIME"</span><span class="p">,</span>
                    <span class="p">]:</span>
                        <span class="k">if</span> <span class="n">prop</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"min"</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                            <span class="n">example</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">'Min: </span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s2">"min"</span><span class="p">]</span><span class="si">}</span><span class="s1">, Max: </span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s2">"max"</span><span class="p">]</span><span class="si">}</span><span class="s1">'</span>
                        <span class="k">else</span><span class="p">:</span>
                            <span class="n">example</span> <span class="o">=</span> <span class="p">(</span>
                                <span class="sa">f</span><span class="s1">'Example: "</span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s2">"values"</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span><span class="si">}</span><span class="s1">"'</span>
                                <span class="k">if</span> <span class="n">prop</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"values"</span><span class="p">)</span>
                                <span class="k">else</span> <span class="s2">""</span>
                            <span class="p">)</span>
                    <span class="k">elif</span> <span class="n">prop</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]</span> <span class="o">==</span> <span class="s2">"LIST"</span><span class="p">:</span>
                        <span class="c1"># Skip embeddings</span>
                        <span class="k">if</span> <span class="ow">not</span> <span class="n">prop</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"min_size"</span><span class="p">)</span> <span class="ow">or</span> <span class="n">prop</span><span class="p">[</span><span class="s2">"min_size"</span><span class="p">]</span> <span class="o">&gt;</span> <span class="n">LIST_LIMIT</span><span class="p">:</span>
                            <span class="k">continue</span>
                        <span class="n">example</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">'Min Size: </span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s2">"min_size"</span><span class="p">]</span><span class="si">}</span><span class="s1">, Max Size: </span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s2">"max_size"</span><span class="p">]</span><span class="si">}</span><span class="s1">'</span>
                    <span class="n">formatted_node_props</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"  - `</span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s1">'property'</span><span class="p">]</span><span class="si">}</span><span class="s2">`: </span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s1">'type'</span><span class="p">]</span><span class="si">}</span><span class="s2"> </span><span class="si">{</span><span class="n">example</span><span class="si">}</span><span class="s2">"</span>
                    <span class="p">)</span>

            <span class="c1"># Enhanced formatting for relationships</span>
            <span class="k">for</span> <span class="n">rel_type</span><span class="p">,</span> <span class="n">properties</span> <span class="ow">in</span> <span class="n">schema</span><span class="p">[</span><span class="s2">"rel_props"</span><span class="p">]</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                <span class="n">formatted_rel_props</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"- **</span><span class="si">{</span><span class="n">rel_type</span><span class="si">}</span><span class="s2">**"</span><span class="p">)</span>
                <span class="k">for</span> <span class="n">prop</span> <span class="ow">in</span> <span class="n">properties</span><span class="p">:</span>
                    <span class="n">example</span> <span class="o">=</span> <span class="s2">""</span>
                    <span class="k">if</span> <span class="n">prop</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]</span> <span class="o">==</span> <span class="s2">"STRING"</span><span class="p">:</span>
                        <span class="k">if</span> <span class="n">prop</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"distinct_count"</span><span class="p">,</span> <span class="mi">11</span><span class="p">)</span> <span class="o">&gt;</span> <span class="n">DISTINCT_VALUE_LIMIT</span><span class="p">:</span>
                            <span class="n">example</span> <span class="o">=</span> <span class="p">(</span>
                                <span class="sa">f</span><span class="s1">'Example: "</span><span class="si">{</span><span class="n">clean_string_values</span><span class="p">(</span><span class="n">prop</span><span class="p">[</span><span class="s2">"values"</span><span class="p">][</span><span class="mi">0</span><span class="p">])</span><span class="si">}</span><span class="s1">"'</span>
                                <span class="k">if</span> <span class="n">prop</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"values"</span><span class="p">)</span>
                                <span class="k">else</span> <span class="s2">""</span>
                            <span class="p">)</span>
                        <span class="k">else</span><span class="p">:</span>  <span class="c1"># If less than 10 possible values return all</span>
                            <span class="n">example</span> <span class="o">=</span> <span class="p">(</span>
                                <span class="p">(</span>
                                    <span class="s2">"Available options: "</span>
                                    <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="p">[</span><span class="n">clean_string_values</span><span class="p">(</span><span class="n">el</span><span class="p">)</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">el</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="n">prop</span><span class="p">[</span><span class="s2">"values"</span><span class="p">]]</span><span class="si">}</span><span class="s1">'</span>
                                <span class="p">)</span>
                                <span class="k">if</span> <span class="n">prop</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"values"</span><span class="p">)</span>
                                <span class="k">else</span> <span class="s2">""</span>
                            <span class="p">)</span>
                    <span class="k">elif</span> <span class="n">prop</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]</span> <span class="ow">in</span> <span class="p">[</span>
                        <span class="s2">"INTEGER"</span><span class="p">,</span>
                        <span class="s2">"FLOAT"</span><span class="p">,</span>
                        <span class="s2">"DATE"</span><span class="p">,</span>
                        <span class="s2">"DATE_TIME"</span><span class="p">,</span>
                        <span class="s2">"LOCAL_DATE_TIME"</span><span class="p">,</span>
                    <span class="p">]:</span>
                        <span class="k">if</span> <span class="n">prop</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"min"</span><span class="p">):</span>  <span class="c1"># If we have min/max</span>
                            <span class="n">example</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">'Min: </span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s2">"min"</span><span class="p">]</span><span class="si">}</span><span class="s1">, Max:  </span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s2">"max"</span><span class="p">]</span><span class="si">}</span><span class="s1">'</span>
                        <span class="k">else</span><span class="p">:</span>  <span class="c1"># return a single value</span>
                            <span class="n">example</span> <span class="o">=</span> <span class="p">(</span>
                                <span class="sa">f</span><span class="s1">'Example: "</span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s2">"values"</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span><span class="si">}</span><span class="s1">"'</span>
                                <span class="k">if</span> <span class="n">prop</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"values"</span><span class="p">)</span>
                                <span class="k">else</span> <span class="s2">""</span>
                            <span class="p">)</span>
                    <span class="k">elif</span> <span class="n">prop</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]</span> <span class="o">==</span> <span class="s2">"LIST"</span><span class="p">:</span>
                        <span class="c1"># Skip embeddings</span>
                        <span class="k">if</span> <span class="n">prop</span><span class="p">[</span><span class="s2">"min_size"</span><span class="p">]</span> <span class="o">&gt;</span> <span class="n">LIST_LIMIT</span><span class="p">:</span>
                            <span class="k">continue</span>
                        <span class="n">example</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">'Min Size: </span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s2">"min_size"</span><span class="p">]</span><span class="si">}</span><span class="s1">, Max Size: </span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s2">"max_size"</span><span class="p">]</span><span class="si">}</span><span class="s1">'</span>
                    <span class="n">formatted_rel_props</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"  - `</span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s1">'property'</span><span class="p">]</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s1">'type'</span><span class="p">]</span><span class="si">}</span><span class="s2">` </span><span class="si">{</span><span class="n">example</span><span class="si">}</span><span class="s2">"</span>
                    <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># Format node properties</span>
            <span class="k">for</span> <span class="n">label</span><span class="p">,</span> <span class="n">props</span> <span class="ow">in</span> <span class="n">schema</span><span class="p">[</span><span class="s2">"node_props"</span><span class="p">]</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                <span class="n">props_str</span> <span class="o">=</span> <span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                    <span class="p">[</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s1">'property'</span><span class="p">]</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s1">'type'</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span> <span class="k">for</span> <span class="n">prop</span> <span class="ow">in</span> <span class="n">props</span><span class="p">]</span>
                <span class="p">)</span>
                <span class="n">formatted_node_props</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">label</span><span class="si">}</span><span class="s2"> </span><span class="se">{{</span><span class="si">{</span><span class="n">props_str</span><span class="si">}</span><span class="se">}}</span><span class="s2">"</span><span class="p">)</span>

            <span class="c1"># Format relationship properties using structured_schema</span>
            <span class="k">for</span> <span class="nb">type</span><span class="p">,</span> <span class="n">props</span> <span class="ow">in</span> <span class="n">schema</span><span class="p">[</span><span class="s2">"rel_props"</span><span class="p">]</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                <span class="n">props_str</span> <span class="o">=</span> <span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                    <span class="p">[</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s1">'property'</span><span class="p">]</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">prop</span><span class="p">[</span><span class="s1">'type'</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span> <span class="k">for</span> <span class="n">prop</span> <span class="ow">in</span> <span class="n">props</span><span class="p">]</span>
                <span class="p">)</span>
                <span class="n">formatted_rel_props</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="nb">type</span><span class="si">}</span><span class="s2"> </span><span class="se">{{</span><span class="si">{</span><span class="n">props_str</span><span class="si">}</span><span class="se">}}</span><span class="s2">"</span><span class="p">)</span>

        <span class="c1"># Format relationships</span>
        <span class="n">formatted_rels</span> <span class="o">=</span> <span class="p">[</span>
            <span class="sa">f</span><span class="s2">"(:</span><span class="si">{</span><span class="n">el</span><span class="p">[</span><span class="s1">'start'</span><span class="p">]</span><span class="si">}</span><span class="s2">)-[:</span><span class="si">{</span><span class="n">el</span><span class="p">[</span><span class="s1">'type'</span><span class="p">]</span><span class="si">}</span><span class="s2">]-&gt;(:</span><span class="si">{</span><span class="n">el</span><span class="p">[</span><span class="s1">'end'</span><span class="p">]</span><span class="si">}</span><span class="s2">)"</span>
            <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">schema</span><span class="p">[</span><span class="s2">"relationships"</span><span class="p">]</span>
        <span class="p">]</span>

        <span class="k">return</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
            <span class="p">[</span>
                <span class="s2">"Node properties:"</span><span class="p">,</span>
                <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">formatted_node_props</span><span class="p">),</span>
                <span class="s2">"Relationship properties:"</span><span class="p">,</span>
                <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">formatted_rel_props</span><span class="p">),</span>
                <span class="s2">"The relationships:"</span><span class="p">,</span>
                <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">formatted_rels</span><span class="p">),</span>
            <span class="p">]</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### refresh\_schema [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jPropertyGraphStore.refresh_schema "Permanent link")

```
refresh_schema() -> None
```

Refresh the schema.

Source code in `llama-index-integrations/graph_stores/llama-index-graph-stores-neo4j/llama_index/graph_stores/neo4j/neo4j_property_graph.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span>
<span class="normal">160</span>
<span class="normal">161</span>
<span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span>
<span class="normal">165</span>
<span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
<span class="normal">225</span>
<span class="normal">226</span>
<span class="normal">227</span>
<span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span>
<span class="normal">231</span>
<span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span>
<span class="normal">236</span>
<span class="normal">237</span>
<span class="normal">238</span>
<span class="normal">239</span>
<span class="normal">240</span>
<span class="normal">241</span>
<span class="normal">242</span>
<span class="normal">243</span>
<span class="normal">244</span>
<span class="normal">245</span>
<span class="normal">246</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">refresh_schema</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Refresh the schema."""</span>
    <span class="n">node_query_results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
        <span class="n">node_properties_query</span><span class="p">,</span>
        <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"EXCLUDED_LABELS"</span><span class="p">:</span> <span class="p">[</span><span class="o">*</span><span class="n">EXCLUDED_LABELS</span><span class="p">,</span> <span class="n">BASE_ENTITY_LABEL</span><span class="p">]},</span>
    <span class="p">)</span>
    <span class="n">node_properties</span> <span class="o">=</span> <span class="p">(</span>
        <span class="p">[</span><span class="n">el</span><span class="p">[</span><span class="s2">"output"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">node_query_results</span><span class="p">]</span> <span class="k">if</span> <span class="n">node_query_results</span> <span class="k">else</span> <span class="p">[]</span>
    <span class="p">)</span>

    <span class="n">rels_query_result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
        <span class="n">rel_properties_query</span><span class="p">,</span> <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"EXCLUDED_LABELS"</span><span class="p">:</span> <span class="n">EXCLUDED_RELS</span><span class="p">}</span>
    <span class="p">)</span>
    <span class="n">rel_properties</span> <span class="o">=</span> <span class="p">(</span>
        <span class="p">[</span><span class="n">el</span><span class="p">[</span><span class="s2">"output"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">rels_query_result</span><span class="p">]</span> <span class="k">if</span> <span class="n">rels_query_result</span> <span class="k">else</span> <span class="p">[]</span>
    <span class="p">)</span>

    <span class="n">rel_objs_query_result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
        <span class="n">rel_query</span><span class="p">,</span>
        <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"EXCLUDED_LABELS"</span><span class="p">:</span> <span class="p">[</span><span class="o">*</span><span class="n">EXCLUDED_LABELS</span><span class="p">,</span> <span class="n">BASE_ENTITY_LABEL</span><span class="p">]},</span>
    <span class="p">)</span>
    <span class="n">relationships</span> <span class="o">=</span> <span class="p">(</span>
        <span class="p">[</span><span class="n">el</span><span class="p">[</span><span class="s2">"output"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">rel_objs_query_result</span><span class="p">]</span>
        <span class="k">if</span> <span class="n">rel_objs_query_result</span>
        <span class="k">else</span> <span class="p">[]</span>
    <span class="p">)</span>

    <span class="c1"># Get constraints &amp; indexes</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">constraint</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span><span class="s2">"SHOW CONSTRAINTS"</span><span class="p">)</span>
        <span class="n">index</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
            <span class="s2">"CALL apoc.schema.nodes() YIELD label, properties, type, size, "</span>
            <span class="s2">"valuesSelectivity WHERE type = 'RANGE' RETURN *, "</span>
            <span class="s2">"size * valuesSelectivity as distinctValues"</span>
        <span class="p">)</span>
    <span class="k">except</span> <span class="p">(</span>
        <span class="n">neo4j</span><span class="o">.</span><span class="n">exceptions</span><span class="o">.</span><span class="n">ClientError</span>
    <span class="p">):</span>  <span class="c1"># Read-only user might not have access to schema information</span>
        <span class="n">constraint</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">index</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">structured_schema</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"node_props"</span><span class="p">:</span> <span class="p">{</span><span class="n">el</span><span class="p">[</span><span class="s2">"labels"</span><span class="p">]:</span> <span class="n">el</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">node_properties</span><span class="p">},</span>
        <span class="s2">"rel_props"</span><span class="p">:</span> <span class="p">{</span><span class="n">el</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]:</span> <span class="n">el</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">rel_properties</span><span class="p">},</span>
        <span class="s2">"relationships"</span><span class="p">:</span> <span class="n">relationships</span><span class="p">,</span>
        <span class="s2">"metadata"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"constraint"</span><span class="p">:</span> <span class="n">constraint</span><span class="p">,</span> <span class="s2">"index"</span><span class="p">:</span> <span class="n">index</span><span class="p">},</span>
    <span class="p">}</span>
    <span class="n">schema_counts</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
        <span class="s2">"CALL apoc.meta.graphSample() YIELD nodes, relationships "</span>
        <span class="s2">"RETURN nodes, [rel in relationships | {name:apoc.any.property"</span>
        <span class="s2">"(rel, 'type'), count: apoc.any.property(rel, 'count')}]"</span>
        <span class="s2">" AS relationships"</span>
    <span class="p">)</span>
    <span class="c1"># Update node info</span>
    <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">schema_counts</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"nodes"</span><span class="p">,</span> <span class="p">[]):</span>
        <span class="c1"># Skip bloom labels</span>
        <span class="k">if</span> <span class="n">node</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span> <span class="ow">in</span> <span class="n">EXCLUDED_LABELS</span><span class="p">:</span>
            <span class="k">continue</span>
        <span class="n">node_props</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_schema</span><span class="p">[</span><span class="s2">"node_props"</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">node</span><span class="p">[</span><span class="s2">"name"</span><span class="p">])</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">node_props</span><span class="p">:</span>  <span class="c1"># The node has no properties</span>
            <span class="k">continue</span>
        <span class="n">enhanced_cypher</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_enhanced_schema_cypher</span><span class="p">(</span>
            <span class="n">node</span><span class="p">[</span><span class="s2">"name"</span><span class="p">],</span> <span class="n">node_props</span><span class="p">,</span> <span class="n">node</span><span class="p">[</span><span class="s2">"count"</span><span class="p">]</span> <span class="o">&lt;</span> <span class="n">EXHAUSTIVE_SEARCH_LIMIT</span>
        <span class="p">)</span>
        <span class="n">enhanced_info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span><span class="n">enhanced_cypher</span><span class="p">)[</span><span class="mi">0</span><span class="p">][</span><span class="s2">"output"</span><span class="p">]</span>
        <span class="k">for</span> <span class="n">prop</span> <span class="ow">in</span> <span class="n">node_props</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">prop</span><span class="p">[</span><span class="s2">"property"</span><span class="p">]</span> <span class="ow">in</span> <span class="n">enhanced_info</span><span class="p">:</span>
                <span class="n">prop</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">enhanced_info</span><span class="p">[</span><span class="n">prop</span><span class="p">[</span><span class="s2">"property"</span><span class="p">]])</span>
    <span class="c1"># Update rel info</span>
    <span class="k">for</span> <span class="n">rel</span> <span class="ow">in</span> <span class="n">schema_counts</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"relationships"</span><span class="p">,</span> <span class="p">[]):</span>
        <span class="c1"># Skip bloom labels</span>
        <span class="k">if</span> <span class="n">rel</span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span> <span class="ow">in</span> <span class="n">EXCLUDED_RELS</span><span class="p">:</span>
            <span class="k">continue</span>
        <span class="n">rel_props</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_schema</span><span class="p">[</span><span class="s2">"rel_props"</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">rel</span><span class="p">[</span><span class="s2">"name"</span><span class="p">])</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">rel_props</span><span class="p">:</span>  <span class="c1"># The rel has no properties</span>
            <span class="k">continue</span>
        <span class="n">enhanced_cypher</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_enhanced_schema_cypher</span><span class="p">(</span>
            <span class="n">rel</span><span class="p">[</span><span class="s2">"name"</span><span class="p">],</span>
            <span class="n">rel_props</span><span class="p">,</span>
            <span class="n">rel</span><span class="p">[</span><span class="s2">"count"</span><span class="p">]</span> <span class="o">&lt;</span> <span class="n">EXHAUSTIVE_SEARCH_LIMIT</span><span class="p">,</span>
            <span class="n">is_relationship</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">enhanced_info</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span><span class="n">enhanced_cypher</span><span class="p">)[</span><span class="mi">0</span><span class="p">][</span><span class="s2">"output"</span><span class="p">]</span>
            <span class="k">for</span> <span class="n">prop</span> <span class="ow">in</span> <span class="n">rel_props</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">prop</span><span class="p">[</span><span class="s2">"property"</span><span class="p">]</span> <span class="ow">in</span> <span class="n">enhanced_info</span><span class="p">:</span>
                    <span class="n">prop</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">enhanced_info</span><span class="p">[</span><span class="n">prop</span><span class="p">[</span><span class="s2">"property"</span><span class="p">]])</span>
        <span class="k">except</span> <span class="n">neo4j</span><span class="o">.</span><span class="n">exceptions</span><span class="o">.</span><span class="n">ClientError</span><span class="p">:</span>
            <span class="c1"># Sometimes the types are not consistent in the db</span>
            <span class="k">pass</span>
</code></pre></div></td></tr></tbody></table>

### upsert\_relations [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jPropertyGraphStore.upsert_relations "Permanent link")

```
upsert_relations(relations: List[Relation]) -> None
```

Add relations.

Source code in `llama-index-integrations/graph_stores/llama-index-graph-stores-neo4j/llama_index/graph_stores/neo4j/neo4j_property_graph.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">305</span>
<span class="normal">306</span>
<span class="normal">307</span>
<span class="normal">308</span>
<span class="normal">309</span>
<span class="normal">310</span>
<span class="normal">311</span>
<span class="normal">312</span>
<span class="normal">313</span>
<span class="normal">314</span>
<span class="normal">315</span>
<span class="normal">316</span>
<span class="normal">317</span>
<span class="normal">318</span>
<span class="normal">319</span>
<span class="normal">320</span>
<span class="normal">321</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">upsert_relations</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">relations</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Relation</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Add relations."""</span>
    <span class="n">params</span> <span class="o">=</span> <span class="p">[</span><span class="n">r</span><span class="o">.</span><span class="n">dict</span><span class="p">()</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">relations</span><span class="p">]</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        UNWIND $data AS row</span>
<span class="sd">        MERGE (source {id: row.source_id})</span>
<span class="sd">        ON CREATE SET source:Chunk</span>
<span class="sd">        MERGE (target {id: row.target_id})</span>
<span class="sd">        ON CREATE SET target:Chunk</span>
<span class="sd">        WITH source, target, row</span>
<span class="sd">        CALL apoc.merge.relationship(source, row.label, {}, row.properties, target) YIELD rel</span>
<span class="sd">        RETURN count(*)</span>
<span class="sd">        """</span><span class="p">,</span>
        <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"data"</span><span class="p">:</span> <span class="n">params</span><span class="p">},</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jPropertyGraphStore.get "Permanent link")

```
get(properties: Optional[dict] = None, ids: Optional[List[str]] = None) -> List[LabelledNode]
```

Get nodes.

Source code in `llama-index-integrations/graph_stores/llama-index-graph-stores-neo4j/llama_index/graph_stores/neo4j/neo4j_property_graph.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">323</span>
<span class="normal">324</span>
<span class="normal">325</span>
<span class="normal">326</span>
<span class="normal">327</span>
<span class="normal">328</span>
<span class="normal">329</span>
<span class="normal">330</span>
<span class="normal">331</span>
<span class="normal">332</span>
<span class="normal">333</span>
<span class="normal">334</span>
<span class="normal">335</span>
<span class="normal">336</span>
<span class="normal">337</span>
<span class="normal">338</span>
<span class="normal">339</span>
<span class="normal">340</span>
<span class="normal">341</span>
<span class="normal">342</span>
<span class="normal">343</span>
<span class="normal">344</span>
<span class="normal">345</span>
<span class="normal">346</span>
<span class="normal">347</span>
<span class="normal">348</span>
<span class="normal">349</span>
<span class="normal">350</span>
<span class="normal">351</span>
<span class="normal">352</span>
<span class="normal">353</span>
<span class="normal">354</span>
<span class="normal">355</span>
<span class="normal">356</span>
<span class="normal">357</span>
<span class="normal">358</span>
<span class="normal">359</span>
<span class="normal">360</span>
<span class="normal">361</span>
<span class="normal">362</span>
<span class="normal">363</span>
<span class="normal">364</span>
<span class="normal">365</span>
<span class="normal">366</span>
<span class="normal">367</span>
<span class="normal">368</span>
<span class="normal">369</span>
<span class="normal">370</span>
<span class="normal">371</span>
<span class="normal">372</span>
<span class="normal">373</span>
<span class="normal">374</span>
<span class="normal">375</span>
<span class="normal">376</span>
<span class="normal">377</span>
<span class="normal">378</span>
<span class="normal">379</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">properties</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">LabelledNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get nodes."""</span>
    <span class="n">cypher_statement</span> <span class="o">=</span> <span class="s2">"MATCH (e) "</span>

    <span class="n">params</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="k">if</span> <span class="n">properties</span> <span class="ow">or</span> <span class="n">ids</span><span class="p">:</span>
        <span class="n">cypher_statement</span> <span class="o">+=</span> <span class="s2">"WHERE "</span>

    <span class="k">if</span> <span class="n">ids</span><span class="p">:</span>
        <span class="n">cypher_statement</span> <span class="o">+=</span> <span class="s2">"e.id in $ids "</span>
        <span class="n">params</span><span class="p">[</span><span class="s2">"ids"</span><span class="p">]</span> <span class="o">=</span> <span class="n">ids</span>

    <span class="k">if</span> <span class="n">properties</span><span class="p">:</span>
        <span class="n">prop_list</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">prop</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">properties</span><span class="p">):</span>
            <span class="n">prop_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"e.`</span><span class="si">{</span><span class="n">prop</span><span class="si">}</span><span class="s2">` = $property_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="n">params</span><span class="p">[</span><span class="sa">f</span><span class="s2">"property_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">"</span><span class="p">]</span> <span class="o">=</span> <span class="n">properties</span><span class="p">[</span><span class="n">prop</span><span class="p">]</span>
        <span class="n">cypher_statement</span> <span class="o">+=</span> <span class="s2">" AND "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">prop_list</span><span class="p">)</span>

    <span class="n">return_statement</span> <span class="o">=</span> <span class="s2">"""</span>
<span class="s2">    WITH e</span>
<span class="s2">    RETURN e.id AS name,</span>
<span class="s2">           [l in labels(e) WHERE l &lt;&gt; '__Entity__' | l][0] AS type,</span>
<span class="s2">           e{.* , embedding: Null, id: Null} AS properties</span>
<span class="s2">    """</span>
    <span class="n">cypher_statement</span> <span class="o">+=</span> <span class="n">return_statement</span>

    <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span><span class="n">cypher_statement</span><span class="p">,</span> <span class="n">param_map</span><span class="o">=</span><span class="n">params</span><span class="p">)</span>
    <span class="n">response</span> <span class="o">=</span> <span class="n">response</span> <span class="k">if</span> <span class="n">response</span> <span class="k">else</span> <span class="p">[]</span>

    <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">record</span> <span class="ow">in</span> <span class="n">response</span><span class="p">:</span>
        <span class="c1"># text indicates a chunk node</span>
        <span class="c1"># none on the type indicates an implicit node, likely a chunk node</span>
        <span class="k">if</span> <span class="s2">"text"</span> <span class="ow">in</span> <span class="n">record</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]</span> <span class="ow">or</span> <span class="n">record</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">=</span> <span class="n">record</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"text"</span><span class="p">,</span> <span class="s2">""</span><span class="p">)</span>
            <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">ChunkNode</span><span class="p">(</span>
                    <span class="n">id_</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"name"</span><span class="p">],</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
                    <span class="n">properties</span><span class="o">=</span><span class="n">remove_empty_values</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]),</span>
                <span class="p">)</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">EntityNode</span><span class="p">(</span>
                    <span class="n">name</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"name"</span><span class="p">],</span>
                    <span class="n">label</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"type"</span><span class="p">],</span>
                    <span class="n">properties</span><span class="o">=</span><span class="n">remove_empty_values</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]),</span>
                <span class="p">)</span>
            <span class="p">)</span>

    <span class="k">return</span> <span class="n">nodes</span>
</code></pre></div></td></tr></tbody></table>

### get\_rel\_map [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jPropertyGraphStore.get_rel_map "Permanent link")

```
get_rel_map(graph_nodes: List[LabelledNode], depth: int = 2, limit: int = 30, ignore_rels: Optional[List[str]] = None) -> List[Triplet]
```

Get depth-aware rel map.

Source code in `llama-index-integrations/graph_stores/llama-index-graph-stores-neo4j/llama_index/graph_stores/neo4j/neo4j_property_graph.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">455</span>
<span class="normal">456</span>
<span class="normal">457</span>
<span class="normal">458</span>
<span class="normal">459</span>
<span class="normal">460</span>
<span class="normal">461</span>
<span class="normal">462</span>
<span class="normal">463</span>
<span class="normal">464</span>
<span class="normal">465</span>
<span class="normal">466</span>
<span class="normal">467</span>
<span class="normal">468</span>
<span class="normal">469</span>
<span class="normal">470</span>
<span class="normal">471</span>
<span class="normal">472</span>
<span class="normal">473</span>
<span class="normal">474</span>
<span class="normal">475</span>
<span class="normal">476</span>
<span class="normal">477</span>
<span class="normal">478</span>
<span class="normal">479</span>
<span class="normal">480</span>
<span class="normal">481</span>
<span class="normal">482</span>
<span class="normal">483</span>
<span class="normal">484</span>
<span class="normal">485</span>
<span class="normal">486</span>
<span class="normal">487</span>
<span class="normal">488</span>
<span class="normal">489</span>
<span class="normal">490</span>
<span class="normal">491</span>
<span class="normal">492</span>
<span class="normal">493</span>
<span class="normal">494</span>
<span class="normal">495</span>
<span class="normal">496</span>
<span class="normal">497</span>
<span class="normal">498</span>
<span class="normal">499</span>
<span class="normal">500</span>
<span class="normal">501</span>
<span class="normal">502</span>
<span class="normal">503</span>
<span class="normal">504</span>
<span class="normal">505</span>
<span class="normal">506</span>
<span class="normal">507</span>
<span class="normal">508</span>
<span class="normal">509</span>
<span class="normal">510</span>
<span class="normal">511</span>
<span class="normal">512</span>
<span class="normal">513</span>
<span class="normal">514</span>
<span class="normal">515</span>
<span class="normal">516</span>
<span class="normal">517</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_rel_map</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">graph_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">LabelledNode</span><span class="p">],</span>
    <span class="n">depth</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span>
    <span class="n">limit</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">30</span><span class="p">,</span>
    <span class="n">ignore_rels</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Triplet</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get depth-aware rel map."""</span>
    <span class="n">triples</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="n">ids</span> <span class="o">=</span> <span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">id</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">graph_nodes</span><span class="p">]</span>
    <span class="c1"># Needs some optimization</span>
    <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
        <span class="sa">f</span><span class="s2">"""</span>
<span class="s2">        WITH $ids AS id_list</span>
<span class="s2">        UNWIND range(0, size(id_list) - 1) AS idx</span>
<span class="s2">        MATCH (e:`__Entity__`)</span>
<span class="s2">        WHERE e.id = id_list[idx]</span>
<span class="s2">        MATCH p=(e)-[r*1..</span><span class="si">{</span><span class="n">depth</span><span class="si">}</span><span class="s2">]-(other)</span>
<span class="s2">        WHERE ALL(rel in relationships(p) WHERE type(rel) &lt;&gt; 'MENTIONS')</span>
<span class="s2">        UNWIND relationships(p) AS rel</span>
<span class="s2">        WITH distinct rel, idx</span>
<span class="s2">        WITH startNode(rel) AS source,</span>
<span class="s2">            type(rel) AS type,</span>
<span class="s2">            endNode(rel) AS endNode,</span>
<span class="s2">            idx</span>
<span class="s2">        LIMIT toInteger($limit)</span>
<span class="s2">        RETURN source.id AS source_id, [l in labels(source) WHERE l &lt;&gt; '__Entity__' | l][0] AS source_type,</span>
<span class="s2">            source</span><span class="se">{{</span><span class="s2">.* , embedding: Null, id: Null</span><span class="se">}}</span><span class="s2"> AS source_properties,</span>
<span class="s2">            type,</span>
<span class="s2">            endNode.id AS target_id, [l in labels(endNode) WHERE l &lt;&gt; '__Entity__' | l][0] AS target_type,</span>
<span class="s2">            endNode</span><span class="se">{{</span><span class="s2">.* , embedding: Null, id: Null</span><span class="se">}}</span><span class="s2"> AS target_properties,</span>
<span class="s2">            idx</span>
<span class="s2">        ORDER BY idx</span>
<span class="s2">        LIMIT toInteger($limit)</span>
<span class="s2">        """</span><span class="p">,</span>
        <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"ids"</span><span class="p">:</span> <span class="n">ids</span><span class="p">,</span> <span class="s2">"limit"</span><span class="p">:</span> <span class="n">limit</span><span class="p">},</span>
    <span class="p">)</span>
    <span class="n">response</span> <span class="o">=</span> <span class="n">response</span> <span class="k">if</span> <span class="n">response</span> <span class="k">else</span> <span class="p">[]</span>

    <span class="n">ignore_rels</span> <span class="o">=</span> <span class="n">ignore_rels</span> <span class="ow">or</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">record</span> <span class="ow">in</span> <span class="n">response</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">record</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]</span> <span class="ow">in</span> <span class="n">ignore_rels</span><span class="p">:</span>
            <span class="k">continue</span>

        <span class="n">source</span> <span class="o">=</span> <span class="n">EntityNode</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"source_id"</span><span class="p">],</span>
            <span class="n">label</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"source_type"</span><span class="p">],</span>
            <span class="n">properties</span><span class="o">=</span><span class="n">remove_empty_values</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"source_properties"</span><span class="p">]),</span>
        <span class="p">)</span>
        <span class="n">target</span> <span class="o">=</span> <span class="n">EntityNode</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"target_id"</span><span class="p">],</span>
            <span class="n">label</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"target_type"</span><span class="p">],</span>
            <span class="n">properties</span><span class="o">=</span><span class="n">remove_empty_values</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"target_properties"</span><span class="p">]),</span>
        <span class="p">)</span>
        <span class="n">rel</span> <span class="o">=</span> <span class="n">Relation</span><span class="p">(</span>
            <span class="n">source_id</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"source_id"</span><span class="p">],</span>
            <span class="n">target_id</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"target_id"</span><span class="p">],</span>
            <span class="n">label</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"type"</span><span class="p">],</span>
        <span class="p">)</span>
        <span class="n">triples</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="n">source</span><span class="p">,</span> <span class="n">rel</span><span class="p">,</span> <span class="n">target</span><span class="p">])</span>

    <span class="k">return</span> <span class="n">triples</span>
</code></pre></div></td></tr></tbody></table>

### vector\_query [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jPropertyGraphStore.vector_query "Permanent link")

```
vector_query(query: [VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery"), **kwargs: Any) -> Tuple[List[LabelledNode], List[float]]
```

Query the graph store with a vector store query.

Source code in `llama-index-integrations/graph_stores/llama-index-graph-stores-neo4j/llama_index/graph_stores/neo4j/neo4j_property_graph.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">533</span>
<span class="normal">534</span>
<span class="normal">535</span>
<span class="normal">536</span>
<span class="normal">537</span>
<span class="normal">538</span>
<span class="normal">539</span>
<span class="normal">540</span>
<span class="normal">541</span>
<span class="normal">542</span>
<span class="normal">543</span>
<span class="normal">544</span>
<span class="normal">545</span>
<span class="normal">546</span>
<span class="normal">547</span>
<span class="normal">548</span>
<span class="normal">549</span>
<span class="normal">550</span>
<span class="normal">551</span>
<span class="normal">552</span>
<span class="normal">553</span>
<span class="normal">554</span>
<span class="normal">555</span>
<span class="normal">556</span>
<span class="normal">557</span>
<span class="normal">558</span>
<span class="normal">559</span>
<span class="normal">560</span>
<span class="normal">561</span>
<span class="normal">562</span>
<span class="normal">563</span>
<span class="normal">564</span>
<span class="normal">565</span>
<span class="normal">566</span>
<span class="normal">567</span>
<span class="normal">568</span>
<span class="normal">569</span>
<span class="normal">570</span>
<span class="normal">571</span>
<span class="normal">572</span>
<span class="normal">573</span>
<span class="normal">574</span>
<span class="normal">575</span>
<span class="normal">576</span>
<span class="normal">577</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">vector_query</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">LabelledNode</span><span class="p">],</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Query the graph store with a vector store query."""</span>
    <span class="n">conditions</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">:</span>
        <span class="n">conditions</span> <span class="o">=</span> <span class="p">[</span>
            <span class="sa">f</span><span class="s2">"e.</span><span class="si">{</span><span class="nb">filter</span><span class="o">.</span><span class="n">key</span><span class="si">}</span><span class="s2"> </span><span class="si">{</span><span class="nb">filter</span><span class="o">.</span><span class="n">operator</span><span class="o">.</span><span class="n">value</span><span class="si">}</span><span class="s2"> </span><span class="si">{</span><span class="nb">filter</span><span class="o">.</span><span class="n">value</span><span class="si">}</span><span class="s2">"</span>
            <span class="k">for</span> <span class="nb">filter</span> <span class="ow">in</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="o">.</span><span class="n">filters</span>
        <span class="p">]</span>
    <span class="n">filters</span> <span class="o">=</span> <span class="p">(</span>
        <span class="sa">f</span><span class="s2">" </span><span class="si">{</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="o">.</span><span class="n">condition</span><span class="o">.</span><span class="n">value</span><span class="si">}</span><span class="s2"> "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">conditions</span><span class="p">)</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"=="</span><span class="p">,</span> <span class="s2">"="</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">conditions</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
        <span class="k">else</span> <span class="s2">"1 = 1"</span>
    <span class="p">)</span>

    <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
        <span class="sa">f</span><span class="s2">"""MATCH (e:`__Entity__`)</span>
<span class="s2">        WHERE e.embedding IS NOT NULL AND size(e.embedding) = $dimension AND (</span><span class="si">{</span><span class="n">filters</span><span class="si">}</span><span class="s2">)</span>
<span class="s2">        WITH e, vector.similarity.cosine(e.embedding, $embedding) AS score</span>
<span class="s2">        ORDER BY score DESC LIMIT toInteger($limit)</span>
<span class="s2">        RETURN e.id AS name,</span>
<span class="s2">           [l in labels(e) WHERE l &lt;&gt; '__Entity__' | l][0] AS type,</span>
<span class="s2">           e</span><span class="se">{{</span><span class="s2">.* , embedding: Null, name: Null, id: Null</span><span class="se">}}</span><span class="s2"> AS properties,</span>
<span class="s2">           score"""</span><span class="p">,</span>
        <span class="n">param_map</span><span class="o">=</span><span class="p">{</span>
            <span class="s2">"embedding"</span><span class="p">:</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">,</span>
            <span class="s2">"dimension"</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">),</span>
            <span class="s2">"limit"</span><span class="p">:</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">)</span>
    <span class="n">data</span> <span class="o">=</span> <span class="n">data</span> <span class="k">if</span> <span class="n">data</span> <span class="k">else</span> <span class="p">[]</span>

    <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">scores</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">record</span> <span class="ow">in</span> <span class="n">data</span><span class="p">:</span>
        <span class="n">node</span> <span class="o">=</span> <span class="n">EntityNode</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"name"</span><span class="p">],</span>
            <span class="n">label</span><span class="o">=</span><span class="n">record</span><span class="p">[</span><span class="s2">"type"</span><span class="p">],</span>
            <span class="n">properties</span><span class="o">=</span><span class="n">remove_empty_values</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"properties"</span><span class="p">]),</span>
        <span class="p">)</span>
        <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
        <span class="n">scores</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"score"</span><span class="p">])</span>

    <span class="k">return</span> <span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">scores</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neo4j/#llama_index.graph_stores.neo4j.Neo4jPropertyGraphStore.delete "Permanent link")

```
delete(entity_names: Optional[List[str]] = None, relation_names: Optional[List[str]] = None, properties: Optional[dict] = None, ids: Optional[List[str]] = None) -> None
```

Delete matching data.

Source code in `llama-index-integrations/graph_stores/llama-index-graph-stores-neo4j/llama_index/graph_stores/neo4j/neo4j_property_graph.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">579</span>
<span class="normal">580</span>
<span class="normal">581</span>
<span class="normal">582</span>
<span class="normal">583</span>
<span class="normal">584</span>
<span class="normal">585</span>
<span class="normal">586</span>
<span class="normal">587</span>
<span class="normal">588</span>
<span class="normal">589</span>
<span class="normal">590</span>
<span class="normal">591</span>
<span class="normal">592</span>
<span class="normal">593</span>
<span class="normal">594</span>
<span class="normal">595</span>
<span class="normal">596</span>
<span class="normal">597</span>
<span class="normal">598</span>
<span class="normal">599</span>
<span class="normal">600</span>
<span class="normal">601</span>
<span class="normal">602</span>
<span class="normal">603</span>
<span class="normal">604</span>
<span class="normal">605</span>
<span class="normal">606</span>
<span class="normal">607</span>
<span class="normal">608</span>
<span class="normal">609</span>
<span class="normal">610</span>
<span class="normal">611</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">entity_names</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">relation_names</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">properties</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete matching data."""</span>
    <span class="k">if</span> <span class="n">entity_names</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
            <span class="s2">"MATCH (n) WHERE n.name IN $entity_names DETACH DELETE n"</span><span class="p">,</span>
            <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"entity_names"</span><span class="p">:</span> <span class="n">entity_names</span><span class="p">},</span>
        <span class="p">)</span>

    <span class="k">if</span> <span class="n">ids</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span>
            <span class="s2">"MATCH (n) WHERE n.id IN $ids DETACH DELETE n"</span><span class="p">,</span>
            <span class="n">param_map</span><span class="o">=</span><span class="p">{</span><span class="s2">"ids"</span><span class="p">:</span> <span class="n">ids</span><span class="p">},</span>
        <span class="p">)</span>

    <span class="k">if</span> <span class="n">relation_names</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">rel</span> <span class="ow">in</span> <span class="n">relation_names</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span><span class="sa">f</span><span class="s2">"MATCH ()-[r:`</span><span class="si">{</span><span class="n">rel</span><span class="si">}</span><span class="s2">`]-&gt;() DELETE r"</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">properties</span><span class="p">:</span>
        <span class="n">cypher</span> <span class="o">=</span> <span class="s2">"MATCH (e) WHERE "</span>
        <span class="n">prop_list</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">params</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">prop</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">properties</span><span class="p">):</span>
            <span class="n">prop_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">"e.`</span><span class="si">{</span><span class="n">prop</span><span class="si">}</span><span class="s2">` = $property_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="n">params</span><span class="p">[</span><span class="sa">f</span><span class="s2">"property_</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">"</span><span class="p">]</span> <span class="o">=</span> <span class="n">properties</span><span class="p">[</span><span class="n">prop</span><span class="p">]</span>
        <span class="n">cypher</span> <span class="o">+=</span> <span class="s2">" AND "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">prop_list</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">structured_query</span><span class="p">(</span><span class="n">cypher</span> <span class="o">+</span> <span class="s2">" DETACH DELETE e"</span><span class="p">,</span> <span class="n">param_map</span><span class="o">=</span><span class="n">params</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Nebula](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/nebula/)[Next Neptune](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/neptune/)
