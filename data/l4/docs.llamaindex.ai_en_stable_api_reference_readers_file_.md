Title: File - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/readers/file/

Markdown Content:
File - LlamaIndex
===============
             

[Skip to content](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.CSVReader)

[![Image 1: logo](https://docs.llamaindex.ai/en/stable/_static/assets/LlamaSquareBlack.svg)](https://docs.llamaindex.ai/en/stable/ "LlamaIndex")

LlamaIndex

File

  

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
        *    File [File](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/)
            
            Table of contents
            
            *   [CSVReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.CSVReader)
                
                *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.CSVReader.load_data)
                
            *   [DocxReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.DocxReader)
                
                *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.DocxReader.load_data)
                
            *   [EpubReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.EpubReader)
                
                *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.EpubReader.load_data)
                
            *   [FlatReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.FlatReader)
                
                *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.FlatReader.load_data)
                
            *   [HTMLTagReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.HTMLTagReader)
            *   [HWPReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.HWPReader)
                
                *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.HWPReader.load_data)
                
            *   [IPYNBReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.IPYNBReader)
                
                *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.IPYNBReader.load_data)
                
            *   [ImageCaptionReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.ImageCaptionReader)
                
                *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.ImageCaptionReader.load_data)
                
            *   [ImageReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.ImageReader)
                
                *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.ImageReader.load_data)
                
            *   [ImageTabularChartReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.ImageTabularChartReader)
                
                *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.ImageTabularChartReader.load_data)
                
            *   [ImageVisionLLMReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.ImageVisionLLMReader)
                
                *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.ImageVisionLLMReader.load_data)
                
            *   [MarkdownReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MarkdownReader)
                
                *   [markdown\_to\_tups](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MarkdownReader.markdown_to_tups)
                *   [remove\_images](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MarkdownReader.remove_images)
                *   [remove\_hyperlinks](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MarkdownReader.remove_hyperlinks)
                *   [parse\_tups](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MarkdownReader.parse_tups)
                *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MarkdownReader.load_data)
                
            *   [MboxReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MboxReader)
                
                *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MboxReader.load_data)
                
            *   [PDFReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PDFReader)
                
                *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PDFReader.load_data)
                
            *   [PagedCSVReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PagedCSVReader)
                
                *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PagedCSVReader.load_data)
                
            *   [PandasCSVReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PandasCSVReader)
                
                *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PandasCSVReader.load_data)
                
            *   [PandasExcelReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PandasExcelReader)
                
                *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PandasExcelReader.load_data)
                
            *   [PptxReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PptxReader)
                
                *   [caption\_image](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PptxReader.caption_image)
                *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PptxReader.load_data)
                
            *   [PyMuPDFReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PyMuPDFReader)
                
                *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PyMuPDFReader.load_data)
                *   [load](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PyMuPDFReader.load)
                
            *   [RTFReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.RTFReader)
                
                *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.RTFReader.load_data)
                
            *   [UnstructuredReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.UnstructuredReader)
                
                *   [from\_api](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.UnstructuredReader.from_api)
                *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.UnstructuredReader.load_data)
                
            *   [VideoAudioReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.VideoAudioReader)
                
                *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.VideoAudioReader.load_data)
                
            *   [XMLReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.XMLReader)
                
                *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.XMLReader.load_data)
                
            
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

*   [CSVReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.CSVReader)
    
    *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.CSVReader.load_data)
    
*   [DocxReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.DocxReader)
    
    *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.DocxReader.load_data)
    
*   [EpubReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.EpubReader)
    
    *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.EpubReader.load_data)
    
*   [FlatReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.FlatReader)
    
    *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.FlatReader.load_data)
    
*   [HTMLTagReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.HTMLTagReader)
*   [HWPReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.HWPReader)
    
    *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.HWPReader.load_data)
    
*   [IPYNBReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.IPYNBReader)
    
    *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.IPYNBReader.load_data)
    
*   [ImageCaptionReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.ImageCaptionReader)
    
    *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.ImageCaptionReader.load_data)
    
*   [ImageReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.ImageReader)
    
    *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.ImageReader.load_data)
    
*   [ImageTabularChartReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.ImageTabularChartReader)
    
    *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.ImageTabularChartReader.load_data)
    
*   [ImageVisionLLMReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.ImageVisionLLMReader)
    
    *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.ImageVisionLLMReader.load_data)
    
*   [MarkdownReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MarkdownReader)
    
    *   [markdown\_to\_tups](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MarkdownReader.markdown_to_tups)
    *   [remove\_images](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MarkdownReader.remove_images)
    *   [remove\_hyperlinks](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MarkdownReader.remove_hyperlinks)
    *   [parse\_tups](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MarkdownReader.parse_tups)
    *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MarkdownReader.load_data)
    
*   [MboxReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MboxReader)
    
    *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MboxReader.load_data)
    
*   [PDFReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PDFReader)
    
    *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PDFReader.load_data)
    
*   [PagedCSVReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PagedCSVReader)
    
    *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PagedCSVReader.load_data)
    
*   [PandasCSVReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PandasCSVReader)
    
    *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PandasCSVReader.load_data)
    
*   [PandasExcelReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PandasExcelReader)
    
    *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PandasExcelReader.load_data)
    
*   [PptxReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PptxReader)
    
    *   [caption\_image](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PptxReader.caption_image)
    *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PptxReader.load_data)
    
*   [PyMuPDFReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PyMuPDFReader)
    
    *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PyMuPDFReader.load_data)
    *   [load](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PyMuPDFReader.load)
    
*   [RTFReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.RTFReader)
    
    *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.RTFReader.load_data)
    
*   [UnstructuredReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.UnstructuredReader)
    
    *   [from\_api](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.UnstructuredReader.from_api)
    *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.UnstructuredReader.load_data)
    
*   [VideoAudioReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.VideoAudioReader)
    
    *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.VideoAudioReader.load_data)
    
*   [XMLReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.XMLReader)
    
    *   [load\_data](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.XMLReader.load_data)
    

File
====

CSVReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.CSVReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

CSV parser.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `concat_rows` | `bool` | 
whether to concatenate all rows into one document. If set to False, a Document will be created for each row. True by default.



 | `True` |

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/tabular/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">CSVReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""CSV parser.</span>

<span class="sd">    Args:</span>
<span class="sd">        concat_rows (bool): whether to concatenate all rows into one document.</span>
<span class="sd">            If set to False, a Document will be created for each row.</span>
<span class="sd">            True by default.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">concat_rows</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_concat_rows</span> <span class="o">=</span> <span class="n">concat_rows</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Union[str, List[str]]: a string or a List of strings.</span>

<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">csv</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"csv module is required to read CSV files."</span><span class="p">)</span>
        <span class="n">text_list</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span> <span class="k">as</span> <span class="n">fp</span><span class="p">:</span>
            <span class="n">csv_reader</span> <span class="o">=</span> <span class="n">csv</span><span class="o">.</span><span class="n">reader</span><span class="p">(</span><span class="n">fp</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">csv_reader</span><span class="p">:</span>
                <span class="n">text_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">row</span><span class="p">))</span>

        <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"filename"</span><span class="p">:</span> <span class="n">file</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="s2">"extension"</span><span class="p">:</span> <span class="n">file</span><span class="o">.</span><span class="n">suffix</span><span class="p">}</span>
        <span class="k">if</span> <span class="n">extra_info</span><span class="p">:</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="o">**</span><span class="n">metadata</span><span class="p">,</span> <span class="o">**</span><span class="n">extra_info</span><span class="p">}</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_concat_rows</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_list</span><span class="p">),</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">)]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">)</span> <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">text_list</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.CSVReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file.

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
Union\[str, List\[str\]\]: a string or a List of strings.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/tabular/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file.</span>

<span class="sd">    Returns:</span>
<span class="sd">        Union[str, List[str]]: a string or a List of strings.</span>

<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">import</span> <span class="nn">csv</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"csv module is required to read CSV files."</span><span class="p">)</span>
    <span class="n">text_list</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span> <span class="k">as</span> <span class="n">fp</span><span class="p">:</span>
        <span class="n">csv_reader</span> <span class="o">=</span> <span class="n">csv</span><span class="o">.</span><span class="n">reader</span><span class="p">(</span><span class="n">fp</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">csv_reader</span><span class="p">:</span>
            <span class="n">text_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s2">", "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">row</span><span class="p">))</span>

    <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"filename"</span><span class="p">:</span> <span class="n">file</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="s2">"extension"</span><span class="p">:</span> <span class="n">file</span><span class="o">.</span><span class="n">suffix</span><span class="p">}</span>
    <span class="k">if</span> <span class="n">extra_info</span><span class="p">:</span>
        <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="o">**</span><span class="n">metadata</span><span class="p">,</span> <span class="o">**</span><span class="n">extra_info</span><span class="p">}</span>

    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_concat_rows</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_list</span><span class="p">),</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">)]</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">)</span> <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">text_list</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

DocxReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.DocxReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Docx parser.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/docs/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">100</span>
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
<span class="normal">130</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">DocxReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Docx parser."""</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file."""</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">Path</span><span class="p">):</span>
            <span class="n">file</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">docx2txt</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"docx2txt is required to read Microsoft Word files: "</span>
                <span class="s2">"`pip install docx2txt`"</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
            <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                <span class="n">text</span> <span class="o">=</span> <span class="n">docx2txt</span><span class="o">.</span><span class="n">process</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">=</span> <span class="n">docx2txt</span><span class="o">.</span><span class="n">process</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
        <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"file_name"</span><span class="p">:</span> <span class="n">file</span><span class="o">.</span><span class="n">name</span><span class="p">}</span>
        <span class="k">if</span> <span class="n">extra_info</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">metadata</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">extra_info</span><span class="p">)</span>

        <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span> <span class="ow">or</span> <span class="p">{})]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.DocxReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None, fs: Optional[AbstractFileSystem] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/docs/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">103</span>
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
<span class="normal">130</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file."""</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">Path</span><span class="p">):</span>
        <span class="n">file</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>

    <span class="k">try</span><span class="p">:</span>
        <span class="kn">import</span> <span class="nn">docx2txt</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
            <span class="s2">"docx2txt is required to read Microsoft Word files: "</span>
            <span class="s2">"`pip install docx2txt`"</span>
        <span class="p">)</span>

    <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
        <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">=</span> <span class="n">docx2txt</span><span class="o">.</span><span class="n">process</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">text</span> <span class="o">=</span> <span class="n">docx2txt</span><span class="o">.</span><span class="n">process</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
    <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"file_name"</span><span class="p">:</span> <span class="n">file</span><span class="o">.</span><span class="n">name</span><span class="p">}</span>
    <span class="k">if</span> <span class="n">extra_info</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">metadata</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">extra_info</span><span class="p">)</span>

    <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span> <span class="ow">or</span> <span class="p">{})]</span>
</code></pre></div></td></tr></tbody></table>

EpubReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.EpubReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Epub Parser.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/epub/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">EpubReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Epub Parser."""</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">ebooklib</span>
            <span class="kn">import</span> <span class="nn">html2text</span>
            <span class="kn">from</span> <span class="nn">ebooklib</span> <span class="kn">import</span> <span class="n">epub</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"Please install extra dependencies that are required for "</span>
                <span class="s2">"the EpubReader: "</span>
                <span class="s2">"`pip install EbookLib html2text`"</span>
            <span class="p">)</span>
        <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
                <span class="s2">"fs was specified but EpubReader doesn't support loading "</span>
                <span class="s2">"from fsspec filesystems. Will load from local filesystem instead."</span>
            <span class="p">)</span>

        <span class="n">text_list</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">book</span> <span class="o">=</span> <span class="n">epub</span><span class="o">.</span><span class="n">read_epub</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">options</span><span class="o">=</span><span class="p">{</span><span class="s2">"ignore_ncx"</span><span class="p">:</span> <span class="kc">True</span><span class="p">})</span>

        <span class="c1"># Iterate through all chapters.</span>
        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">book</span><span class="o">.</span><span class="n">get_items</span><span class="p">():</span>
            <span class="c1"># Chapters are typically located in epub documents items.</span>
            <span class="k">if</span> <span class="n">item</span><span class="o">.</span><span class="n">get_type</span><span class="p">()</span> <span class="o">==</span> <span class="n">ebooklib</span><span class="o">.</span><span class="n">ITEM_DOCUMENT</span><span class="p">:</span>
                <span class="n">text_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">html2text</span><span class="o">.</span><span class="n">html2text</span><span class="p">(</span><span class="n">item</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">))</span>
                <span class="p">)</span>

        <span class="n">text</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_list</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.EpubReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None, fs: Optional[AbstractFileSystem] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/epub/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file."""</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">import</span> <span class="nn">ebooklib</span>
        <span class="kn">import</span> <span class="nn">html2text</span>
        <span class="kn">from</span> <span class="nn">ebooklib</span> <span class="kn">import</span> <span class="n">epub</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
            <span class="s2">"Please install extra dependencies that are required for "</span>
            <span class="s2">"the EpubReader: "</span>
            <span class="s2">"`pip install EbookLib html2text`"</span>
        <span class="p">)</span>
    <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
            <span class="s2">"fs was specified but EpubReader doesn't support loading "</span>
            <span class="s2">"from fsspec filesystems. Will load from local filesystem instead."</span>
        <span class="p">)</span>

    <span class="n">text_list</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">book</span> <span class="o">=</span> <span class="n">epub</span><span class="o">.</span><span class="n">read_epub</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">options</span><span class="o">=</span><span class="p">{</span><span class="s2">"ignore_ncx"</span><span class="p">:</span> <span class="kc">True</span><span class="p">})</span>

    <span class="c1"># Iterate through all chapters.</span>
    <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">book</span><span class="o">.</span><span class="n">get_items</span><span class="p">():</span>
        <span class="c1"># Chapters are typically located in epub documents items.</span>
        <span class="k">if</span> <span class="n">item</span><span class="o">.</span><span class="n">get_type</span><span class="p">()</span> <span class="o">==</span> <span class="n">ebooklib</span><span class="o">.</span><span class="n">ITEM_DOCUMENT</span><span class="p">:</span>
            <span class="n">text_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">html2text</span><span class="o">.</span><span class="n">html2text</span><span class="p">(</span><span class="n">item</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">))</span>
            <span class="p">)</span>

    <span class="n">text</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_list</span><span class="p">)</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})]</span>
</code></pre></div></td></tr></tbody></table>

FlatReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.FlatReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Flat reader.

Extract raw text from a file and save the file type in the metadata

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/flat/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 9</span>
<span class="normal">10</span>
<span class="normal">11</span>
<span class="normal">12</span>
<span class="normal">13</span>
<span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">FlatReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Flat reader.</span>

<span class="sd">    Extract raw text from a file and save the file type in the metadata</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file into string."""</span>
        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">content</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
        <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"filename"</span><span class="p">:</span> <span class="n">file</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="s2">"extension"</span><span class="p">:</span> <span class="n">file</span><span class="o">.</span><span class="n">suffix</span><span class="p">}</span>
        <span class="k">if</span> <span class="n">extra_info</span><span class="p">:</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="o">**</span><span class="n">metadata</span><span class="p">,</span> <span class="o">**</span><span class="n">extra_info</span><span class="p">}</span>

        <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">content</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">)]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.FlatReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file into string.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/flat/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file into string."""</span>
    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
        <span class="n">content</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
    <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"filename"</span><span class="p">:</span> <span class="n">file</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="s2">"extension"</span><span class="p">:</span> <span class="n">file</span><span class="o">.</span><span class="n">suffix</span><span class="p">}</span>
    <span class="k">if</span> <span class="n">extra_info</span><span class="p">:</span>
        <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="o">**</span><span class="n">metadata</span><span class="p">,</span> <span class="o">**</span><span class="n">extra_info</span><span class="p">}</span>

    <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">content</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">)]</span>
</code></pre></div></td></tr></tbody></table>

HTMLTagReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.HTMLTagReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Read HTML files and extract text from a specific tag with BeautifulSoup.

By default, reads the text from the `<section>` tag.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/html/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">11</span>
<span class="normal">12</span>
<span class="normal">13</span>
<span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">HTMLTagReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Read HTML files and extract text from a specific tag with BeautifulSoup.</span>

<span class="sd">    By default, reads the text from the ``&lt;section&gt;`` tag.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">tag</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"section"</span><span class="p">,</span>
        <span class="n">ignore_no_id</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_tag</span> <span class="o">=</span> <span class="n">tag</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_ignore_no_id</span> <span class="o">=</span> <span class="n">ignore_no_id</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">bs4</span> <span class="kn">import</span> <span class="n">BeautifulSoup</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"bs4 is required to read HTML files."</span><span class="p">)</span>

        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">)</span> <span class="k">as</span> <span class="n">html_file</span><span class="p">:</span>
            <span class="n">soup</span> <span class="o">=</span> <span class="n">BeautifulSoup</span><span class="p">(</span><span class="n">html_file</span><span class="p">,</span> <span class="s2">"html.parser"</span><span class="p">)</span>

        <span class="n">tags</span> <span class="o">=</span> <span class="n">soup</span><span class="o">.</span><span class="n">find_all</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_tag</span><span class="p">)</span>
        <span class="n">docs</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">tags</span><span class="p">:</span>
            <span class="n">tag_id</span> <span class="o">=</span> <span class="n">tag</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"id"</span><span class="p">)</span>
            <span class="n">tag_text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_extract_text_from_tag</span><span class="p">(</span><span class="n">tag</span><span class="p">)</span>

            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_ignore_no_id</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">tag_id</span><span class="p">:</span>
                <span class="k">continue</span>

            <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"tag"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tag</span><span class="p">,</span>
                <span class="s2">"tag_id"</span><span class="p">:</span> <span class="n">tag_id</span><span class="p">,</span>
                <span class="s2">"file_path"</span><span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">file</span><span class="p">),</span>
            <span class="p">}</span>
            <span class="n">metadata</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span>

            <span class="n">doc</span> <span class="o">=</span> <span class="n">Document</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">tag_text</span><span class="p">,</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">doc</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">docs</span>

    <span class="k">def</span> <span class="nf">_extract_text_from_tag</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tag</span><span class="p">:</span> <span class="s2">"Tag"</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">bs4</span> <span class="kn">import</span> <span class="n">NavigableString</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"bs4 is required to read HTML files."</span><span class="p">)</span>

        <span class="n">texts</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">elem</span> <span class="ow">in</span> <span class="n">tag</span><span class="o">.</span><span class="n">children</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">elem</span><span class="p">,</span> <span class="n">NavigableString</span><span class="p">):</span>
                <span class="k">if</span> <span class="n">elem</span><span class="o">.</span><span class="n">strip</span><span class="p">():</span>
                    <span class="n">texts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">elem</span><span class="o">.</span><span class="n">strip</span><span class="p">())</span>
            <span class="k">elif</span> <span class="n">elem</span><span class="o">.</span><span class="n">name</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tag</span><span class="p">:</span>
                <span class="k">continue</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">texts</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">elem</span><span class="o">.</span><span class="n">get_text</span><span class="p">()</span><span class="o">.</span><span class="n">strip</span><span class="p">())</span>
        <span class="k">return</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">texts</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

HWPReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.HWPReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Hwp Parser.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/docs/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">133</span>
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
<span class="normal">242</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">HWPReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Hwp Parser."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">FILE_HEADER_SECTION</span> <span class="o">=</span> <span class="s2">"FileHeader"</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">HWP_SUMMARY_SECTION</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\x05</span><span class="s2">HwpSummaryInformation"</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">SECTION_NAME_LENGTH</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="s2">"Section"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">BODYTEXT_SECTION</span> <span class="o">=</span> <span class="s2">"BodyText"</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">HWP_TEXT_TAGS</span> <span class="o">=</span> <span class="p">[</span><span class="mi">67</span><span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">text</span> <span class="o">=</span> <span class="s2">""</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data and extract table from Hwp file.</span>

<span class="sd">        Args:</span>
<span class="sd">            file (Path): Path for the Hwp file.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]</span>
<span class="sd">        """</span>
        <span class="kn">import</span> <span class="nn">olefile</span>

        <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
                <span class="s2">"fs was specified but HWPReader doesn't support loading "</span>
                <span class="s2">"from fsspec filesystems. Will load from local filesystem instead."</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">Path</span><span class="p">):</span>
            <span class="n">file</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
        <span class="n">load_file</span> <span class="o">=</span> <span class="n">olefile</span><span class="o">.</span><span class="n">OleFileIO</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
        <span class="n">file_dir</span> <span class="o">=</span> <span class="n">load_file</span><span class="o">.</span><span class="n">listdir</span><span class="p">()</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_valid</span><span class="p">(</span><span class="n">file_dir</span><span class="p">)</span> <span class="ow">is</span> <span class="kc">False</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s2">"Not Valid HwpFile"</span><span class="p">)</span>

        <span class="n">result_text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_text</span><span class="p">(</span><span class="n">load_file</span><span class="p">,</span> <span class="n">file_dir</span><span class="p">)</span>
        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_text_to_document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">result_text</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">result</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">is_valid</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dirs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
        <span class="k">if</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">FILE_HEADER_SECTION</span><span class="p">]</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">dirs</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">False</span>

        <span class="k">return</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">HWP_SUMMARY_SECTION</span><span class="p">]</span> <span class="ow">in</span> <span class="n">dirs</span>

    <span class="k">def</span> <span class="nf">get_body_sections</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dirs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
        <span class="n">m</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">dirs</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">d</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">BODYTEXT_SECTION</span><span class="p">:</span>
                <span class="n">m</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="n">d</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="bp">self</span><span class="o">.</span><span class="n">SECTION_NAME_LENGTH</span> <span class="p">:]))</span>

        <span class="k">return</span> <span class="p">[</span><span class="s2">"BodyText/Section"</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">m</span><span class="p">)]</span>

    <span class="k">def</span> <span class="nf">_text_to_document</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Document</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span>

    <span class="k">def</span> <span class="nf">get_text</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">text</span>

        <span class="c1"># 전체 text 추출</span>

    <span class="k">def</span> <span class="nf">_get_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">load_file</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">file_dirs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">sections</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_body_sections</span><span class="p">(</span><span class="n">file_dirs</span><span class="p">)</span>
        <span class="n">text</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="k">for</span> <span class="n">section</span> <span class="ow">in</span> <span class="n">sections</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">+=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_text_from_section</span><span class="p">(</span><span class="n">load_file</span><span class="p">,</span> <span class="n">section</span><span class="p">)</span>
            <span class="n">text</span> <span class="o">+=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">text</span> <span class="o">=</span> <span class="n">text</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">text</span>

    <span class="k">def</span> <span class="nf">is_compressed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">load_file</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
        <span class="n">header</span> <span class="o">=</span> <span class="n">load_file</span><span class="o">.</span><span class="n">openstream</span><span class="p">(</span><span class="s2">"FileHeader"</span><span class="p">)</span>
        <span class="n">header_data</span> <span class="o">=</span> <span class="n">header</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
        <span class="k">return</span> <span class="p">(</span><span class="n">header_data</span><span class="p">[</span><span class="mi">36</span><span class="p">]</span> <span class="o">&amp;</span> <span class="mi">1</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span>

    <span class="k">def</span> <span class="nf">get_text_from_section</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">load_file</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">section</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">bodytext</span> <span class="o">=</span> <span class="n">load_file</span><span class="o">.</span><span class="n">openstream</span><span class="p">(</span><span class="n">section</span><span class="p">)</span>
        <span class="n">data</span> <span class="o">=</span> <span class="n">bodytext</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>

        <span class="n">unpacked_data</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">zlib</span><span class="o">.</span><span class="n">decompress</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="o">-</span><span class="mi">15</span><span class="p">)</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_compressed</span><span class="p">(</span><span class="n">load_file</span><span class="p">)</span> <span class="k">else</span> <span class="n">data</span>
        <span class="p">)</span>
        <span class="n">size</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">unpacked_data</span><span class="p">)</span>

        <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span>

        <span class="n">text</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">size</span><span class="p">:</span>
            <span class="n">header</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack_from</span><span class="p">(</span><span class="s2">"&lt;I"</span><span class="p">,</span> <span class="n">unpacked_data</span><span class="p">,</span> <span class="n">i</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
            <span class="n">rec_type</span> <span class="o">=</span> <span class="n">header</span> <span class="o">&amp;</span> <span class="mh">0x3FF</span>
            <span class="p">(</span><span class="n">header</span> <span class="o">&gt;&gt;</span> <span class="mi">10</span><span class="p">)</span> <span class="o">&amp;</span> <span class="mh">0x3FF</span>
            <span class="n">rec_len</span> <span class="o">=</span> <span class="p">(</span><span class="n">header</span> <span class="o">&gt;&gt;</span> <span class="mi">20</span><span class="p">)</span> <span class="o">&amp;</span> <span class="mh">0xFFF</span>

            <span class="k">if</span> <span class="n">rec_type</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">HWP_TEXT_TAGS</span><span class="p">:</span>
                <span class="n">rec_data</span> <span class="o">=</span> <span class="n">unpacked_data</span><span class="p">[</span><span class="n">i</span> <span class="o">+</span> <span class="mi">4</span> <span class="p">:</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">4</span> <span class="o">+</span> <span class="n">rec_len</span><span class="p">]</span>
                <span class="n">text</span> <span class="o">+=</span> <span class="n">rec_data</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s2">"utf-16"</span><span class="p">)</span>
                <span class="n">text</span> <span class="o">+=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span>

            <span class="n">i</span> <span class="o">+=</span> <span class="mi">4</span> <span class="o">+</span> <span class="n">rec_len</span>

        <span class="k">return</span> <span class="n">text</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.HWPReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None, fs: Optional[AbstractFileSystem] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data and extract table from Hwp file.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `file` | `Path` | 
Path for the Hwp file.



 | _required_ |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]



 |

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/docs/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">145</span>
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
<span class="normal">176</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data and extract table from Hwp file.</span>

<span class="sd">    Args:</span>
<span class="sd">        file (Path): Path for the Hwp file.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]</span>
<span class="sd">    """</span>
    <span class="kn">import</span> <span class="nn">olefile</span>

    <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
            <span class="s2">"fs was specified but HWPReader doesn't support loading "</span>
            <span class="s2">"from fsspec filesystems. Will load from local filesystem instead."</span>
        <span class="p">)</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">Path</span><span class="p">):</span>
        <span class="n">file</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
    <span class="n">load_file</span> <span class="o">=</span> <span class="n">olefile</span><span class="o">.</span><span class="n">OleFileIO</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
    <span class="n">file_dir</span> <span class="o">=</span> <span class="n">load_file</span><span class="o">.</span><span class="n">listdir</span><span class="p">()</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_valid</span><span class="p">(</span><span class="n">file_dir</span><span class="p">)</span> <span class="ow">is</span> <span class="kc">False</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s2">"Not Valid HwpFile"</span><span class="p">)</span>

    <span class="n">result_text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_text</span><span class="p">(</span><span class="n">load_file</span><span class="p">,</span> <span class="n">file_dir</span><span class="p">)</span>
    <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_text_to_document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">result_text</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">)</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">result</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

IPYNBReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.IPYNBReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Image parser.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/ipynb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">10</span>
<span class="normal">11</span>
<span class="normal">12</span>
<span class="normal">13</span>
<span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">IPYNBReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Image parser."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">parser_config</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">concatenate</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span> <span class="o">=</span> <span class="n">parser_config</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_concatenate</span> <span class="o">=</span> <span class="n">concatenate</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file."""</span>
        <span class="k">if</span> <span class="n">file</span><span class="o">.</span><span class="n">name</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s2">".ipynb"</span><span class="p">):</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="kn">import</span> <span class="nn">nbconvert</span>
            <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"Please install nbconvert 'pip install nbconvert' "</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
            <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                <span class="n">string</span> <span class="o">=</span> <span class="n">nbconvert</span><span class="o">.</span><span class="n">exporters</span><span class="o">.</span><span class="n">ScriptExporter</span><span class="p">()</span><span class="o">.</span><span class="n">from_file</span><span class="p">(</span><span class="n">f</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">string</span> <span class="o">=</span> <span class="n">nbconvert</span><span class="o">.</span><span class="n">exporters</span><span class="o">.</span><span class="n">ScriptExporter</span><span class="p">()</span><span class="o">.</span><span class="n">from_file</span><span class="p">(</span><span class="n">file</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
        <span class="c1"># split each In[] cell into a separate string</span>
        <span class="n">splits</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="sa">r</span><span class="s2">"In\[\d+\]:"</span><span class="p">,</span> <span class="n">string</span><span class="p">)</span>
        <span class="c1"># remove the first element, which is empty</span>
        <span class="n">splits</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_concatenate</span><span class="p">:</span>
            <span class="n">docs</span> <span class="o">=</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">splits</span><span class="p">),</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">docs</span> <span class="o">=</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">s</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">splits</span><span class="p">]</span>
        <span class="k">return</span> <span class="n">docs</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.IPYNBReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None, fs: Optional[AbstractFileSystem] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/ipynb/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file."""</span>
    <span class="k">if</span> <span class="n">file</span><span class="o">.</span><span class="n">name</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s2">".ipynb"</span><span class="p">):</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">nbconvert</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"Please install nbconvert 'pip install nbconvert' "</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
        <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">string</span> <span class="o">=</span> <span class="n">nbconvert</span><span class="o">.</span><span class="n">exporters</span><span class="o">.</span><span class="n">ScriptExporter</span><span class="p">()</span><span class="o">.</span><span class="n">from_file</span><span class="p">(</span><span class="n">f</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">string</span> <span class="o">=</span> <span class="n">nbconvert</span><span class="o">.</span><span class="n">exporters</span><span class="o">.</span><span class="n">ScriptExporter</span><span class="p">()</span><span class="o">.</span><span class="n">from_file</span><span class="p">(</span><span class="n">file</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
    <span class="c1"># split each In[] cell into a separate string</span>
    <span class="n">splits</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="sa">r</span><span class="s2">"In\[\d+\]:"</span><span class="p">,</span> <span class="n">string</span><span class="p">)</span>
    <span class="c1"># remove the first element, which is empty</span>
    <span class="n">splits</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>

    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_concatenate</span><span class="p">:</span>
        <span class="n">docs</span> <span class="o">=</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">splits</span><span class="p">),</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})]</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">docs</span> <span class="o">=</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">s</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">splits</span><span class="p">]</span>
    <span class="k">return</span> <span class="n">docs</span>
</code></pre></div></td></tr></tbody></table>

ImageCaptionReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.ImageCaptionReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Image parser.

Caption image using Blip.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/image_caption/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 9</span>
<span class="normal">10</span>
<span class="normal">11</span>
<span class="normal">12</span>
<span class="normal">13</span>
<span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span>
<span class="normal">97</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ImageCaptionReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Image parser.</span>

<span class="sd">    Caption image using Blip.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">parser_config</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">keep_image</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="k">if</span> <span class="n">parser_config</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">            </span><span class="sd">"""Init parser."""</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="kn">import</span> <span class="nn">sentencepiece</span>  <span class="c1"># noqa</span>
                <span class="kn">import</span> <span class="nn">torch</span>
                <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>  <span class="c1"># noqa</span>
                <span class="kn">from</span> <span class="nn">transformers</span> <span class="kn">import</span> <span class="n">BlipForConditionalGeneration</span><span class="p">,</span> <span class="n">BlipProcessor</span>
            <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                    <span class="s2">"Please install extra dependencies that are required for "</span>
                    <span class="s2">"the ImageCaptionReader: "</span>
                    <span class="s2">"`pip install torch transformers sentencepiece Pillow`"</span>
                <span class="p">)</span>

            <span class="n">device</span> <span class="o">=</span> <span class="n">infer_torch_device</span><span class="p">()</span>
            <span class="n">dtype</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">float16</span> <span class="k">if</span> <span class="n">torch</span><span class="o">.</span><span class="n">cuda</span><span class="o">.</span><span class="n">is_available</span><span class="p">()</span> <span class="k">else</span> <span class="n">torch</span><span class="o">.</span><span class="n">float32</span>

            <span class="n">processor</span> <span class="o">=</span> <span class="n">BlipProcessor</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span>
                <span class="s2">"Salesforce/blip-image-captioning-large"</span>
            <span class="p">)</span>
            <span class="n">model</span> <span class="o">=</span> <span class="n">BlipForConditionalGeneration</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span>
                <span class="s2">"Salesforce/blip-image-captioning-large"</span><span class="p">,</span> <span class="n">torch_dtype</span><span class="o">=</span><span class="n">dtype</span>
            <span class="p">)</span>

            <span class="n">parser_config</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"processor"</span><span class="p">:</span> <span class="n">processor</span><span class="p">,</span>
                <span class="s2">"model"</span><span class="p">:</span> <span class="n">model</span><span class="p">,</span>
                <span class="s2">"device"</span><span class="p">:</span> <span class="n">device</span><span class="p">,</span>
                <span class="s2">"dtype"</span><span class="p">:</span> <span class="n">dtype</span><span class="p">,</span>
            <span class="p">}</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span> <span class="o">=</span> <span class="n">parser_config</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_keep_image</span> <span class="o">=</span> <span class="n">keep_image</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span> <span class="o">=</span> <span class="n">prompt</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file."""</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.img_utils</span> <span class="kn">import</span> <span class="n">img_2_b64</span>
        <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>

        <span class="c1"># load document image</span>
        <span class="n">image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">image</span><span class="o">.</span><span class="n">mode</span> <span class="o">!=</span> <span class="s2">"RGB"</span><span class="p">:</span>
            <span class="n">image</span> <span class="o">=</span> <span class="n">image</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="s2">"RGB"</span><span class="p">)</span>

        <span class="c1"># Encode image into base64 string and keep in document</span>
        <span class="n">image_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_keep_image</span><span class="p">:</span>
            <span class="n">image_str</span> <span class="o">=</span> <span class="n">img_2_b64</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>

        <span class="c1"># Parse image into text</span>
        <span class="n">model</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"model"</span><span class="p">]</span>
        <span class="n">processor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"processor"</span><span class="p">]</span>

        <span class="n">device</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"device"</span><span class="p">]</span>
        <span class="n">dtype</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"dtype"</span><span class="p">]</span>
        <span class="n">model</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>

        <span class="c1"># unconditional image captioning</span>

        <span class="n">inputs</span> <span class="o">=</span> <span class="n">processor</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span><span class="p">,</span> <span class="n">return_tensors</span><span class="o">=</span><span class="s2">"pt"</span><span class="p">)</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">,</span> <span class="n">dtype</span><span class="p">)</span>

        <span class="n">out</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span><span class="o">**</span><span class="n">inputs</span><span class="p">)</span>
        <span class="n">text_str</span> <span class="o">=</span> <span class="n">processor</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">out</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">skip_special_tokens</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

        <span class="k">return</span> <span class="p">[</span>
            <span class="n">ImageDocument</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">text_str</span><span class="p">,</span>
                <span class="n">image</span><span class="o">=</span><span class="n">image_str</span><span class="p">,</span>
                <span class="n">image_path</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">file</span><span class="p">),</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{},</span>
            <span class="p">)</span>
        <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.ImageCaptionReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/image_caption/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span>
<span class="normal">97</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file."""</span>
    <span class="kn">from</span> <span class="nn">llama_index.core.img_utils</span> <span class="kn">import</span> <span class="n">img_2_b64</span>
    <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>

    <span class="c1"># load document image</span>
    <span class="n">image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">image</span><span class="o">.</span><span class="n">mode</span> <span class="o">!=</span> <span class="s2">"RGB"</span><span class="p">:</span>
        <span class="n">image</span> <span class="o">=</span> <span class="n">image</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="s2">"RGB"</span><span class="p">)</span>

    <span class="c1"># Encode image into base64 string and keep in document</span>
    <span class="n">image_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_keep_image</span><span class="p">:</span>
        <span class="n">image_str</span> <span class="o">=</span> <span class="n">img_2_b64</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>

    <span class="c1"># Parse image into text</span>
    <span class="n">model</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"model"</span><span class="p">]</span>
    <span class="n">processor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"processor"</span><span class="p">]</span>

    <span class="n">device</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"device"</span><span class="p">]</span>
    <span class="n">dtype</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"dtype"</span><span class="p">]</span>
    <span class="n">model</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>

    <span class="c1"># unconditional image captioning</span>

    <span class="n">inputs</span> <span class="o">=</span> <span class="n">processor</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span><span class="p">,</span> <span class="n">return_tensors</span><span class="o">=</span><span class="s2">"pt"</span><span class="p">)</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">,</span> <span class="n">dtype</span><span class="p">)</span>

    <span class="n">out</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span><span class="o">**</span><span class="n">inputs</span><span class="p">)</span>
    <span class="n">text_str</span> <span class="o">=</span> <span class="n">processor</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">out</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">skip_special_tokens</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

    <span class="k">return</span> <span class="p">[</span>
        <span class="n">ImageDocument</span><span class="p">(</span>
            <span class="n">text</span><span class="o">=</span><span class="n">text_str</span><span class="p">,</span>
            <span class="n">image</span><span class="o">=</span><span class="n">image_str</span><span class="p">,</span>
            <span class="n">image_path</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">file</span><span class="p">),</span>
            <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{},</span>
        <span class="p">)</span>
    <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

ImageReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.ImageReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Image parser.

Extract text from images using DONUT or pytesseract.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/image/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 17</span>
<span class="normal"> 18</span>
<span class="normal"> 19</span>
<span class="normal"> 20</span>
<span class="normal"> 21</span>
<span class="normal"> 22</span>
<span class="normal"> 23</span>
<span class="normal"> 24</span>
<span class="normal"> 25</span>
<span class="normal"> 26</span>
<span class="normal"> 27</span>
<span class="normal"> 28</span>
<span class="normal"> 29</span>
<span class="normal"> 30</span>
<span class="normal"> 31</span>
<span class="normal"> 32</span>
<span class="normal"> 33</span>
<span class="normal"> 34</span>
<span class="normal"> 35</span>
<span class="normal"> 36</span>
<span class="normal"> 37</span>
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
<span class="normal">150</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ImageReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Image parser.</span>

<span class="sd">    Extract text from images using DONUT or pytesseract.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">parser_config</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">keep_image</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">parse_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">text_type</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"text"</span><span class="p">,</span>
        <span class="n">pytesseract_model_kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">{},</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Init parser."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_text_type</span> <span class="o">=</span> <span class="n">text_type</span>
        <span class="k">if</span> <span class="n">parser_config</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">parse_text</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">text_type</span> <span class="o">==</span> <span class="s2">"plain_text"</span><span class="p">:</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="kn">import</span> <span class="nn">pytesseract</span>
                <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
                    <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                        <span class="s2">"Please install extra dependencies that are required for "</span>
                        <span class="s2">"the ImageReader when text_type is 'plain_text': "</span>
                        <span class="s2">"`pip install pytesseract`"</span>
                    <span class="p">)</span>
                <span class="n">processor</span> <span class="o">=</span> <span class="kc">None</span>
                <span class="n">model</span> <span class="o">=</span> <span class="n">pytesseract</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="kn">import</span> <span class="nn">sentencepiece</span>  <span class="c1"># noqa</span>
                    <span class="kn">import</span> <span class="nn">torch</span>  <span class="c1"># noqa</span>
                    <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>  <span class="c1"># noqa</span>
                    <span class="kn">from</span> <span class="nn">transformers</span> <span class="kn">import</span> <span class="n">DonutProcessor</span><span class="p">,</span> <span class="n">VisionEncoderDecoderModel</span>
                <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
                    <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                        <span class="s2">"Please install extra dependencies that are required for "</span>
                        <span class="s2">"the ImageCaptionReader: "</span>
                        <span class="s2">"`pip install torch transformers sentencepiece Pillow`"</span>
                    <span class="p">)</span>

                <span class="n">processor</span> <span class="o">=</span> <span class="n">DonutProcessor</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span>
                    <span class="s2">"naver-clova-ix/donut-base-finetuned-cord-v2"</span>
                <span class="p">)</span>
                <span class="n">model</span> <span class="o">=</span> <span class="n">VisionEncoderDecoderModel</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span>
                    <span class="s2">"naver-clova-ix/donut-base-finetuned-cord-v2"</span>
                <span class="p">)</span>
            <span class="n">parser_config</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"processor"</span><span class="p">:</span> <span class="n">processor</span><span class="p">,</span> <span class="s2">"model"</span><span class="p">:</span> <span class="n">model</span><span class="p">}</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span> <span class="o">=</span> <span class="n">parser_config</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_keep_image</span> <span class="o">=</span> <span class="n">keep_image</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_parse_text</span> <span class="o">=</span> <span class="n">parse_text</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_pytesseract_model_kwargs</span> <span class="o">=</span> <span class="n">pytesseract_model_kwargs</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file."""</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.img_utils</span> <span class="kn">import</span> <span class="n">img_2_b64</span>
        <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>

        <span class="c1"># load document image</span>
        <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
            <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">path</span><span class="o">=</span><span class="n">file</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                <span class="n">image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">image</span><span class="o">.</span><span class="n">mode</span> <span class="o">!=</span> <span class="s2">"RGB"</span><span class="p">:</span>
            <span class="n">image</span> <span class="o">=</span> <span class="n">image</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="s2">"RGB"</span><span class="p">)</span>

        <span class="c1"># Encode image into base64 string and keep in document</span>
        <span class="n">image_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_keep_image</span><span class="p">:</span>
            <span class="n">image_str</span> <span class="o">=</span> <span class="n">img_2_b64</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>

        <span class="c1"># Parse image into text</span>
        <span class="n">text_str</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_text</span><span class="p">:</span>
            <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
            <span class="n">model</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"model"</span><span class="p">]</span>
            <span class="n">processor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"processor"</span><span class="p">]</span>

            <span class="k">if</span> <span class="n">processor</span><span class="p">:</span>
                <span class="n">device</span> <span class="o">=</span> <span class="n">infer_torch_device</span><span class="p">()</span>
                <span class="n">model</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>

                <span class="c1"># prepare decoder inputs</span>
                <span class="n">task_prompt</span> <span class="o">=</span> <span class="s2">"&lt;s_cord-v2&gt;"</span>
                <span class="n">decoder_input_ids</span> <span class="o">=</span> <span class="n">processor</span><span class="o">.</span><span class="n">tokenizer</span><span class="p">(</span>
                    <span class="n">task_prompt</span><span class="p">,</span> <span class="n">add_special_tokens</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">return_tensors</span><span class="o">=</span><span class="s2">"pt"</span>
                <span class="p">)</span><span class="o">.</span><span class="n">input_ids</span>

                <span class="n">pixel_values</span> <span class="o">=</span> <span class="n">processor</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="n">return_tensors</span><span class="o">=</span><span class="s2">"pt"</span><span class="p">)</span><span class="o">.</span><span class="n">pixel_values</span>

                <span class="n">outputs</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span>
                    <span class="n">pixel_values</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">),</span>
                    <span class="n">decoder_input_ids</span><span class="o">=</span><span class="n">decoder_input_ids</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">),</span>
                    <span class="n">max_length</span><span class="o">=</span><span class="n">model</span><span class="o">.</span><span class="n">decoder</span><span class="o">.</span><span class="n">config</span><span class="o">.</span><span class="n">max_position_embeddings</span><span class="p">,</span>
                    <span class="n">early_stopping</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                    <span class="n">pad_token_id</span><span class="o">=</span><span class="n">processor</span><span class="o">.</span><span class="n">tokenizer</span><span class="o">.</span><span class="n">pad_token_id</span><span class="p">,</span>
                    <span class="n">eos_token_id</span><span class="o">=</span><span class="n">processor</span><span class="o">.</span><span class="n">tokenizer</span><span class="o">.</span><span class="n">eos_token_id</span><span class="p">,</span>
                    <span class="n">use_cache</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                    <span class="n">num_beams</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
                    <span class="n">bad_words_ids</span><span class="o">=</span><span class="p">[[</span><span class="n">processor</span><span class="o">.</span><span class="n">tokenizer</span><span class="o">.</span><span class="n">unk_token_id</span><span class="p">]],</span>
                    <span class="n">return_dict_in_generate</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="p">)</span>

                <span class="n">sequence</span> <span class="o">=</span> <span class="n">processor</span><span class="o">.</span><span class="n">batch_decode</span><span class="p">(</span><span class="n">outputs</span><span class="o">.</span><span class="n">sequences</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
                <span class="n">sequence</span> <span class="o">=</span> <span class="n">sequence</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">processor</span><span class="o">.</span><span class="n">tokenizer</span><span class="o">.</span><span class="n">eos_token</span><span class="p">,</span> <span class="s2">""</span><span class="p">)</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span>
                    <span class="n">processor</span><span class="o">.</span><span class="n">tokenizer</span><span class="o">.</span><span class="n">pad_token</span><span class="p">,</span> <span class="s2">""</span>
                <span class="p">)</span>
                <span class="c1"># remove first task start token</span>
                <span class="n">text_str</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="sa">r</span><span class="s2">"&lt;.*?&gt;"</span><span class="p">,</span> <span class="s2">""</span><span class="p">,</span> <span class="n">sequence</span><span class="p">,</span> <span class="n">count</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="kn">import</span> <span class="nn">pytesseract</span>

                <span class="n">model</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">pytesseract</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"model"</span><span class="p">])</span>
                <span class="n">text_str</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">image_to_string</span><span class="p">(</span>
                    <span class="n">image</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_pytesseract_model_kwargs</span>
                <span class="p">)</span>

        <span class="k">return</span> <span class="p">[</span>
            <span class="n">ImageDocument</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">text_str</span><span class="p">,</span>
                <span class="n">image</span><span class="o">=</span><span class="n">image_str</span><span class="p">,</span>
                <span class="n">image_path</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">file</span><span class="p">),</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{},</span>
            <span class="p">)</span>
        <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.ImageReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None, fs: Optional[AbstractFileSystem] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/image/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 72</span>
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
<span class="normal">150</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file."""</span>
    <span class="kn">from</span> <span class="nn">llama_index.core.img_utils</span> <span class="kn">import</span> <span class="n">img_2_b64</span>
    <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>

    <span class="c1"># load document image</span>
    <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
        <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">path</span><span class="o">=</span><span class="n">file</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">image</span><span class="o">.</span><span class="n">mode</span> <span class="o">!=</span> <span class="s2">"RGB"</span><span class="p">:</span>
        <span class="n">image</span> <span class="o">=</span> <span class="n">image</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="s2">"RGB"</span><span class="p">)</span>

    <span class="c1"># Encode image into base64 string and keep in document</span>
    <span class="n">image_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_keep_image</span><span class="p">:</span>
        <span class="n">image_str</span> <span class="o">=</span> <span class="n">img_2_b64</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>

    <span class="c1"># Parse image into text</span>
    <span class="n">text_str</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_text</span><span class="p">:</span>
        <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
        <span class="n">model</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"model"</span><span class="p">]</span>
        <span class="n">processor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"processor"</span><span class="p">]</span>

        <span class="k">if</span> <span class="n">processor</span><span class="p">:</span>
            <span class="n">device</span> <span class="o">=</span> <span class="n">infer_torch_device</span><span class="p">()</span>
            <span class="n">model</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>

            <span class="c1"># prepare decoder inputs</span>
            <span class="n">task_prompt</span> <span class="o">=</span> <span class="s2">"&lt;s_cord-v2&gt;"</span>
            <span class="n">decoder_input_ids</span> <span class="o">=</span> <span class="n">processor</span><span class="o">.</span><span class="n">tokenizer</span><span class="p">(</span>
                <span class="n">task_prompt</span><span class="p">,</span> <span class="n">add_special_tokens</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">return_tensors</span><span class="o">=</span><span class="s2">"pt"</span>
            <span class="p">)</span><span class="o">.</span><span class="n">input_ids</span>

            <span class="n">pixel_values</span> <span class="o">=</span> <span class="n">processor</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="n">return_tensors</span><span class="o">=</span><span class="s2">"pt"</span><span class="p">)</span><span class="o">.</span><span class="n">pixel_values</span>

            <span class="n">outputs</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span>
                <span class="n">pixel_values</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">),</span>
                <span class="n">decoder_input_ids</span><span class="o">=</span><span class="n">decoder_input_ids</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">),</span>
                <span class="n">max_length</span><span class="o">=</span><span class="n">model</span><span class="o">.</span><span class="n">decoder</span><span class="o">.</span><span class="n">config</span><span class="o">.</span><span class="n">max_position_embeddings</span><span class="p">,</span>
                <span class="n">early_stopping</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">pad_token_id</span><span class="o">=</span><span class="n">processor</span><span class="o">.</span><span class="n">tokenizer</span><span class="o">.</span><span class="n">pad_token_id</span><span class="p">,</span>
                <span class="n">eos_token_id</span><span class="o">=</span><span class="n">processor</span><span class="o">.</span><span class="n">tokenizer</span><span class="o">.</span><span class="n">eos_token_id</span><span class="p">,</span>
                <span class="n">use_cache</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">num_beams</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
                <span class="n">bad_words_ids</span><span class="o">=</span><span class="p">[[</span><span class="n">processor</span><span class="o">.</span><span class="n">tokenizer</span><span class="o">.</span><span class="n">unk_token_id</span><span class="p">]],</span>
                <span class="n">return_dict_in_generate</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="n">sequence</span> <span class="o">=</span> <span class="n">processor</span><span class="o">.</span><span class="n">batch_decode</span><span class="p">(</span><span class="n">outputs</span><span class="o">.</span><span class="n">sequences</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
            <span class="n">sequence</span> <span class="o">=</span> <span class="n">sequence</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">processor</span><span class="o">.</span><span class="n">tokenizer</span><span class="o">.</span><span class="n">eos_token</span><span class="p">,</span> <span class="s2">""</span><span class="p">)</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span>
                <span class="n">processor</span><span class="o">.</span><span class="n">tokenizer</span><span class="o">.</span><span class="n">pad_token</span><span class="p">,</span> <span class="s2">""</span>
            <span class="p">)</span>
            <span class="c1"># remove first task start token</span>
            <span class="n">text_str</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="sa">r</span><span class="s2">"&lt;.*?&gt;"</span><span class="p">,</span> <span class="s2">""</span><span class="p">,</span> <span class="n">sequence</span><span class="p">,</span> <span class="n">count</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">pytesseract</span>

            <span class="n">model</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">pytesseract</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"model"</span><span class="p">])</span>
            <span class="n">text_str</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">image_to_string</span><span class="p">(</span>
                <span class="n">image</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_pytesseract_model_kwargs</span>
            <span class="p">)</span>

    <span class="k">return</span> <span class="p">[</span>
        <span class="n">ImageDocument</span><span class="p">(</span>
            <span class="n">text</span><span class="o">=</span><span class="n">text_str</span><span class="p">,</span>
            <span class="n">image</span><span class="o">=</span><span class="n">image_str</span><span class="p">,</span>
            <span class="n">image_path</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">file</span><span class="p">),</span>
            <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{},</span>
        <span class="p">)</span>
    <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

ImageTabularChartReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.ImageTabularChartReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Image parser.

Extract tabular data from a chart or figure.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/image_deplot/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 8</span>
<span class="normal"> 9</span>
<span class="normal">10</span>
<span class="normal">11</span>
<span class="normal">12</span>
<span class="normal">13</span>
<span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ImageTabularChartReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Image parser.</span>

<span class="sd">    Extract tabular data from a chart or figure.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">parser_config</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">keep_image</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">max_output_tokens</span><span class="o">=</span><span class="mi">512</span><span class="p">,</span>
        <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"Generate underlying data table of the figure below:"</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="k">if</span> <span class="n">parser_config</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="kn">import</span> <span class="nn">torch</span>
                <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>  <span class="c1"># noqa: F401</span>
                <span class="kn">from</span> <span class="nn">transformers</span> <span class="kn">import</span> <span class="p">(</span>
                    <span class="n">Pix2StructForConditionalGeneration</span><span class="p">,</span>
                    <span class="n">Pix2StructProcessor</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                    <span class="s2">"Please install extra dependencies that are required for "</span>
                    <span class="s2">"the ImageCaptionReader: "</span>
                    <span class="s2">"`pip install torch transformers Pillow`"</span>
                <span class="p">)</span>

            <span class="n">device</span> <span class="o">=</span> <span class="s2">"cuda"</span> <span class="k">if</span> <span class="n">torch</span><span class="o">.</span><span class="n">cuda</span><span class="o">.</span><span class="n">is_available</span><span class="p">()</span> <span class="k">else</span> <span class="s2">"cpu"</span>
            <span class="n">dtype</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">float16</span> <span class="k">if</span> <span class="n">torch</span><span class="o">.</span><span class="n">cuda</span><span class="o">.</span><span class="n">is_available</span><span class="p">()</span> <span class="k">else</span> <span class="n">torch</span><span class="o">.</span><span class="n">float32</span>
            <span class="n">processor</span> <span class="o">=</span> <span class="n">Pix2StructProcessor</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span><span class="s2">"google/deplot"</span><span class="p">)</span>
            <span class="n">model</span> <span class="o">=</span> <span class="n">Pix2StructForConditionalGeneration</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span>
                <span class="s2">"google/deplot"</span><span class="p">,</span> <span class="n">torch_dtype</span><span class="o">=</span><span class="n">dtype</span>
            <span class="p">)</span>
            <span class="n">parser_config</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"processor"</span><span class="p">:</span> <span class="n">processor</span><span class="p">,</span>
                <span class="s2">"model"</span><span class="p">:</span> <span class="n">model</span><span class="p">,</span>
                <span class="s2">"device"</span><span class="p">:</span> <span class="n">device</span><span class="p">,</span>
                <span class="s2">"dtype"</span><span class="p">:</span> <span class="n">dtype</span><span class="p">,</span>
            <span class="p">}</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span> <span class="o">=</span> <span class="n">parser_config</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_keep_image</span> <span class="o">=</span> <span class="n">keep_image</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_max_output_tokens</span> <span class="o">=</span> <span class="n">max_output_tokens</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span> <span class="o">=</span> <span class="n">prompt</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file."""</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.img_utils</span> <span class="kn">import</span> <span class="n">img_2_b64</span>
        <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>

        <span class="c1"># load document image</span>
        <span class="n">image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">image</span><span class="o">.</span><span class="n">mode</span> <span class="o">!=</span> <span class="s2">"RGB"</span><span class="p">:</span>
            <span class="n">image</span> <span class="o">=</span> <span class="n">image</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="s2">"RGB"</span><span class="p">)</span>

        <span class="c1"># Encode image into base64 string and keep in document</span>
        <span class="n">image_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_keep_image</span><span class="p">:</span>
            <span class="n">image_str</span> <span class="o">=</span> <span class="n">img_2_b64</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>

        <span class="c1"># Parse image into text</span>
        <span class="n">model</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"model"</span><span class="p">]</span>
        <span class="n">processor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"processor"</span><span class="p">]</span>

        <span class="n">device</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"device"</span><span class="p">]</span>
        <span class="n">dtype</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"dtype"</span><span class="p">]</span>
        <span class="n">model</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>

        <span class="c1"># unconditional image captioning</span>

        <span class="n">inputs</span> <span class="o">=</span> <span class="n">processor</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span><span class="p">,</span> <span class="n">return_tensors</span><span class="o">=</span><span class="s2">"pt"</span><span class="p">)</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">,</span> <span class="n">dtype</span><span class="p">)</span>

        <span class="n">out</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span><span class="o">**</span><span class="n">inputs</span><span class="p">,</span> <span class="n">max_new_tokens</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_max_output_tokens</span><span class="p">)</span>
        <span class="n">text_str</span> <span class="o">=</span> <span class="s2">"Figure or chart with tabular data: "</span> <span class="o">+</span> <span class="n">processor</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span>
            <span class="n">out</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">skip_special_tokens</span><span class="o">=</span><span class="kc">True</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="p">[</span>
            <span class="n">ImageDocument</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">text_str</span><span class="p">,</span>
                <span class="n">image</span><span class="o">=</span><span class="n">image_str</span><span class="p">,</span>
                <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{},</span>
            <span class="p">)</span>
        <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.ImageTabularChartReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/image_deplot/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file."""</span>
    <span class="kn">from</span> <span class="nn">llama_index.core.img_utils</span> <span class="kn">import</span> <span class="n">img_2_b64</span>
    <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>

    <span class="c1"># load document image</span>
    <span class="n">image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">image</span><span class="o">.</span><span class="n">mode</span> <span class="o">!=</span> <span class="s2">"RGB"</span><span class="p">:</span>
        <span class="n">image</span> <span class="o">=</span> <span class="n">image</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="s2">"RGB"</span><span class="p">)</span>

    <span class="c1"># Encode image into base64 string and keep in document</span>
    <span class="n">image_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_keep_image</span><span class="p">:</span>
        <span class="n">image_str</span> <span class="o">=</span> <span class="n">img_2_b64</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>

    <span class="c1"># Parse image into text</span>
    <span class="n">model</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"model"</span><span class="p">]</span>
    <span class="n">processor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"processor"</span><span class="p">]</span>

    <span class="n">device</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"device"</span><span class="p">]</span>
    <span class="n">dtype</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"dtype"</span><span class="p">]</span>
    <span class="n">model</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>

    <span class="c1"># unconditional image captioning</span>

    <span class="n">inputs</span> <span class="o">=</span> <span class="n">processor</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span><span class="p">,</span> <span class="n">return_tensors</span><span class="o">=</span><span class="s2">"pt"</span><span class="p">)</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">,</span> <span class="n">dtype</span><span class="p">)</span>

    <span class="n">out</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span><span class="o">**</span><span class="n">inputs</span><span class="p">,</span> <span class="n">max_new_tokens</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_max_output_tokens</span><span class="p">)</span>
    <span class="n">text_str</span> <span class="o">=</span> <span class="s2">"Figure or chart with tabular data: "</span> <span class="o">+</span> <span class="n">processor</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span>
        <span class="n">out</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">skip_special_tokens</span><span class="o">=</span><span class="kc">True</span>
    <span class="p">)</span>

    <span class="k">return</span> <span class="p">[</span>
        <span class="n">ImageDocument</span><span class="p">(</span>
            <span class="n">text</span><span class="o">=</span><span class="n">text_str</span><span class="p">,</span>
            <span class="n">image</span><span class="o">=</span><span class="n">image_str</span><span class="p">,</span>
            <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{},</span>
        <span class="p">)</span>
    <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

ImageVisionLLMReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.ImageVisionLLMReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Image parser.

Caption image using Blip2 (a multimodal VisionLLM similar to GPT4).

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/image_vision_llm/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 9</span>
<span class="normal">10</span>
<span class="normal">11</span>
<span class="normal">12</span>
<span class="normal">13</span>
<span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ImageVisionLLMReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Image parser.</span>

<span class="sd">    Caption image using Blip2 (a multimodal VisionLLM similar to GPT4).</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">parser_config</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">keep_image</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"Question: describe what you see in this image. Answer:"</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="k">if</span> <span class="n">parser_config</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="kn">import</span> <span class="nn">sentencepiece</span>  <span class="c1"># noqa</span>
                <span class="kn">import</span> <span class="nn">torch</span>
                <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>  <span class="c1"># noqa</span>
                <span class="kn">from</span> <span class="nn">transformers</span> <span class="kn">import</span> <span class="n">Blip2ForConditionalGeneration</span><span class="p">,</span> <span class="n">Blip2Processor</span>
            <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                    <span class="s2">"Please install extra dependencies that are required for "</span>
                    <span class="s2">"the ImageCaptionReader: "</span>
                    <span class="s2">"`pip install torch transformers sentencepiece Pillow`"</span>
                <span class="p">)</span>

            <span class="n">device</span> <span class="o">=</span> <span class="n">infer_torch_device</span><span class="p">()</span>
            <span class="n">dtype</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">float16</span> <span class="k">if</span> <span class="n">torch</span><span class="o">.</span><span class="n">cuda</span><span class="o">.</span><span class="n">is_available</span><span class="p">()</span> <span class="k">else</span> <span class="n">torch</span><span class="o">.</span><span class="n">float32</span>
            <span class="n">processor</span> <span class="o">=</span> <span class="n">Blip2Processor</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span><span class="s2">"Salesforce/blip2-opt-2.7b"</span><span class="p">)</span>
            <span class="n">model</span> <span class="o">=</span> <span class="n">Blip2ForConditionalGeneration</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span>
                <span class="s2">"Salesforce/blip2-opt-2.7b"</span><span class="p">,</span> <span class="n">torch_dtype</span><span class="o">=</span><span class="n">dtype</span>
            <span class="p">)</span>
            <span class="n">parser_config</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"processor"</span><span class="p">:</span> <span class="n">processor</span><span class="p">,</span>
                <span class="s2">"model"</span><span class="p">:</span> <span class="n">model</span><span class="p">,</span>
                <span class="s2">"device"</span><span class="p">:</span> <span class="n">device</span><span class="p">,</span>
                <span class="s2">"dtype"</span><span class="p">:</span> <span class="n">dtype</span><span class="p">,</span>
            <span class="p">}</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span> <span class="o">=</span> <span class="n">parser_config</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_keep_image</span> <span class="o">=</span> <span class="n">keep_image</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span> <span class="o">=</span> <span class="n">prompt</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file."""</span>
        <span class="kn">from</span> <span class="nn">llama_index.core.img_utils</span> <span class="kn">import</span> <span class="n">img_2_b64</span>
        <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>

        <span class="c1"># load document image</span>
        <span class="n">image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">image</span><span class="o">.</span><span class="n">mode</span> <span class="o">!=</span> <span class="s2">"RGB"</span><span class="p">:</span>
            <span class="n">image</span> <span class="o">=</span> <span class="n">image</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="s2">"RGB"</span><span class="p">)</span>

        <span class="c1"># Encode image into base64 string and keep in document</span>
        <span class="n">image_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_keep_image</span><span class="p">:</span>
            <span class="n">image_str</span> <span class="o">=</span> <span class="n">img_2_b64</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>

        <span class="c1"># Parse image into text</span>
        <span class="n">model</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"model"</span><span class="p">]</span>
        <span class="n">processor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"processor"</span><span class="p">]</span>

        <span class="n">device</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"device"</span><span class="p">]</span>
        <span class="n">dtype</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"dtype"</span><span class="p">]</span>
        <span class="n">model</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>

        <span class="c1"># unconditional image captioning</span>

        <span class="n">inputs</span> <span class="o">=</span> <span class="n">processor</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span><span class="p">,</span> <span class="n">return_tensors</span><span class="o">=</span><span class="s2">"pt"</span><span class="p">)</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">,</span> <span class="n">dtype</span><span class="p">)</span>

        <span class="n">out</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span><span class="o">**</span><span class="n">inputs</span><span class="p">)</span>
        <span class="n">text_str</span> <span class="o">=</span> <span class="n">processor</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">out</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">skip_special_tokens</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

        <span class="k">return</span> <span class="p">[</span>
            <span class="n">ImageDocument</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">text_str</span><span class="p">,</span>
                <span class="n">image</span><span class="o">=</span><span class="n">image_str</span><span class="p">,</span>
                <span class="n">image_path</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">file</span><span class="p">),</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{},</span>
            <span class="p">)</span>
        <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.ImageVisionLLMReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/image_vision_llm/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file."""</span>
    <span class="kn">from</span> <span class="nn">llama_index.core.img_utils</span> <span class="kn">import</span> <span class="n">img_2_b64</span>
    <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>

    <span class="c1"># load document image</span>
    <span class="n">image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">image</span><span class="o">.</span><span class="n">mode</span> <span class="o">!=</span> <span class="s2">"RGB"</span><span class="p">:</span>
        <span class="n">image</span> <span class="o">=</span> <span class="n">image</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="s2">"RGB"</span><span class="p">)</span>

    <span class="c1"># Encode image into base64 string and keep in document</span>
    <span class="n">image_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_keep_image</span><span class="p">:</span>
        <span class="n">image_str</span> <span class="o">=</span> <span class="n">img_2_b64</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>

    <span class="c1"># Parse image into text</span>
    <span class="n">model</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"model"</span><span class="p">]</span>
    <span class="n">processor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"processor"</span><span class="p">]</span>

    <span class="n">device</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"device"</span><span class="p">]</span>
    <span class="n">dtype</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parser_config</span><span class="p">[</span><span class="s2">"dtype"</span><span class="p">]</span>
    <span class="n">model</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>

    <span class="c1"># unconditional image captioning</span>

    <span class="n">inputs</span> <span class="o">=</span> <span class="n">processor</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span><span class="p">,</span> <span class="n">return_tensors</span><span class="o">=</span><span class="s2">"pt"</span><span class="p">)</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">,</span> <span class="n">dtype</span><span class="p">)</span>

    <span class="n">out</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span><span class="o">**</span><span class="n">inputs</span><span class="p">)</span>
    <span class="n">text_str</span> <span class="o">=</span> <span class="n">processor</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">out</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">skip_special_tokens</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

    <span class="k">return</span> <span class="p">[</span>
        <span class="n">ImageDocument</span><span class="p">(</span>
            <span class="n">text</span><span class="o">=</span><span class="n">text_str</span><span class="p">,</span>
            <span class="n">image</span><span class="o">=</span><span class="n">image_str</span><span class="p">,</span>
            <span class="n">image_path</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">file</span><span class="p">),</span>
            <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{},</span>
        <span class="p">)</span>
    <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

MarkdownReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MarkdownReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Markdown parser.

Extract text from markdown files. Returns dictionary with keys as headers and values as the text between headers.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/markdown/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 16</span>
<span class="normal"> 17</span>
<span class="normal"> 18</span>
<span class="normal"> 19</span>
<span class="normal"> 20</span>
<span class="normal"> 21</span>
<span class="normal"> 22</span>
<span class="normal"> 23</span>
<span class="normal"> 24</span>
<span class="normal"> 25</span>
<span class="normal"> 26</span>
<span class="normal"> 27</span>
<span class="normal"> 28</span>
<span class="normal"> 29</span>
<span class="normal"> 30</span>
<span class="normal"> 31</span>
<span class="normal"> 32</span>
<span class="normal"> 33</span>
<span class="normal"> 34</span>
<span class="normal"> 35</span>
<span class="normal"> 36</span>
<span class="normal"> 37</span>
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
<span class="normal">124</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MarkdownReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Markdown parser.</span>

<span class="sd">    Extract text from markdown files.</span>
<span class="sd">    Returns dictionary with keys as headers and values as the text between headers.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="n">remove_hyperlinks</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">remove_images</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_remove_hyperlinks</span> <span class="o">=</span> <span class="n">remove_hyperlinks</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_remove_images</span> <span class="o">=</span> <span class="n">remove_images</span>

    <span class="k">def</span> <span class="nf">markdown_to_tups</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">markdown_text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="nb">str</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Convert a markdown file to a dictionary.</span>

<span class="sd">        The keys are the headers and the values are the text under each header.</span>

<span class="sd">        """</span>
        <span class="n">markdown_tups</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">lines</span> <span class="o">=</span> <span class="n">markdown_text</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>

        <span class="n">current_header</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="n">current_lines</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">in_code_block</span> <span class="o">=</span> <span class="kc">False</span>

        <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">lines</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">line</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">"```"</span><span class="p">):</span>
                <span class="c1"># This is the end of a code block if we are already in it, and vice versa.</span>
                <span class="n">in_code_block</span> <span class="o">=</span> <span class="ow">not</span> <span class="n">in_code_block</span>

            <span class="n">header_match</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="sa">r</span><span class="s2">"^#+\s"</span><span class="p">,</span> <span class="n">line</span><span class="p">)</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">in_code_block</span> <span class="ow">and</span> <span class="n">header_match</span><span class="p">:</span>
                <span class="c1"># Upon first header, skip if current text chunk is empty</span>
                <span class="k">if</span> <span class="n">current_header</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">or</span> <span class="nb">len</span><span class="p">(</span><span class="n">current_lines</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
                    <span class="n">markdown_tups</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">current_header</span><span class="p">,</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">current_lines</span><span class="p">)))</span>

                <span class="n">current_header</span> <span class="o">=</span> <span class="n">line</span>
                <span class="n">current_lines</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">current_lines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">line</span><span class="p">)</span>

        <span class="c1"># Append final text chunk</span>
        <span class="n">markdown_tups</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">current_header</span><span class="p">,</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">current_lines</span><span class="p">)))</span>

        <span class="c1"># Postprocess the tuples before returning</span>
        <span class="k">return</span> <span class="p">[</span>
            <span class="p">(</span>
                <span class="n">key</span> <span class="k">if</span> <span class="n">key</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="sa">r</span><span class="s2">"#"</span><span class="p">,</span> <span class="s2">""</span><span class="p">,</span> <span class="n">key</span><span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">(),</span>
                <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="sa">r</span><span class="s2">"&lt;.*?&gt;"</span><span class="p">,</span> <span class="s2">""</span><span class="p">,</span> <span class="n">value</span><span class="p">),</span>
            <span class="p">)</span>
            <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">markdown_tups</span>
        <span class="p">]</span>

    <span class="k">def</span> <span class="nf">remove_images</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">content</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Remove images in markdown content."""</span>
        <span class="n">pattern</span> <span class="o">=</span> <span class="sa">r</span><span class="s2">"!</span><span class="si">{1}</span><span class="s2">\[\[(.*)\]\]"</span>
        <span class="k">return</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="n">pattern</span><span class="p">,</span> <span class="s2">""</span><span class="p">,</span> <span class="n">content</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">remove_hyperlinks</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">content</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Remove hyperlinks in markdown content."""</span>
        <span class="n">pattern</span> <span class="o">=</span> <span class="sa">r</span><span class="s2">"\[(.*?)\]\((.*?)\)"</span>
        <span class="k">return</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="n">pattern</span><span class="p">,</span> <span class="sa">r</span><span class="s2">"\1"</span><span class="p">,</span> <span class="n">content</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_init_parser</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize the parser with the config."""</span>
        <span class="k">return</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">parse_tups</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">filepath</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">errors</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"ignore"</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="nb">str</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Parse file into tuples."""</span>
        <span class="n">fs</span> <span class="o">=</span> <span class="n">fs</span> <span class="ow">or</span> <span class="n">LocalFileSystem</span><span class="p">()</span>
        <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">filepath</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">content</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_remove_hyperlinks</span><span class="p">:</span>
            <span class="n">content</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">remove_hyperlinks</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_remove_images</span><span class="p">:</span>
            <span class="n">content</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">remove_images</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">markdown_to_tups</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file into string."""</span>
        <span class="n">tups</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">parse_tups</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">)</span>
        <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="c1"># TODO: don't include headers right now</span>
        <span class="k">for</span> <span class="n">header</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">tups</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">header</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">value</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{}))</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="sa">f</span><span class="s2">"</span><span class="se">\n\n</span><span class="si">{</span><span class="n">header</span><span class="si">}</span><span class="se">\n</span><span class="si">{</span><span class="n">value</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span>
                <span class="p">)</span>
        <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

### markdown\_to\_tups [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MarkdownReader.markdown_to_tups "Permanent link")

```
markdown_to_tups(markdown_text: str) -> List[Tuple[Optional[str], str]]
```

Convert a markdown file to a dictionary.

The keys are the headers and the values are the text under each header.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/markdown/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">markdown_to_tups</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">markdown_text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="nb">str</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Convert a markdown file to a dictionary.</span>

<span class="sd">    The keys are the headers and the values are the text under each header.</span>

<span class="sd">    """</span>
    <span class="n">markdown_tups</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">lines</span> <span class="o">=</span> <span class="n">markdown_text</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>

    <span class="n">current_header</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="n">current_lines</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">in_code_block</span> <span class="o">=</span> <span class="kc">False</span>

    <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">lines</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">line</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">"```"</span><span class="p">):</span>
            <span class="c1"># This is the end of a code block if we are already in it, and vice versa.</span>
            <span class="n">in_code_block</span> <span class="o">=</span> <span class="ow">not</span> <span class="n">in_code_block</span>

        <span class="n">header_match</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="sa">r</span><span class="s2">"^#+\s"</span><span class="p">,</span> <span class="n">line</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">in_code_block</span> <span class="ow">and</span> <span class="n">header_match</span><span class="p">:</span>
            <span class="c1"># Upon first header, skip if current text chunk is empty</span>
            <span class="k">if</span> <span class="n">current_header</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">or</span> <span class="nb">len</span><span class="p">(</span><span class="n">current_lines</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
                <span class="n">markdown_tups</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">current_header</span><span class="p">,</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">current_lines</span><span class="p">)))</span>

            <span class="n">current_header</span> <span class="o">=</span> <span class="n">line</span>
            <span class="n">current_lines</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">current_lines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">line</span><span class="p">)</span>

    <span class="c1"># Append final text chunk</span>
    <span class="n">markdown_tups</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">current_header</span><span class="p">,</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">current_lines</span><span class="p">)))</span>

    <span class="c1"># Postprocess the tuples before returning</span>
    <span class="k">return</span> <span class="p">[</span>
        <span class="p">(</span>
            <span class="n">key</span> <span class="k">if</span> <span class="n">key</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="sa">r</span><span class="s2">"#"</span><span class="p">,</span> <span class="s2">""</span><span class="p">,</span> <span class="n">key</span><span class="p">)</span><span class="o">.</span><span class="n">strip</span><span class="p">(),</span>
            <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="sa">r</span><span class="s2">"&lt;.*?&gt;"</span><span class="p">,</span> <span class="s2">""</span><span class="p">,</span> <span class="n">value</span><span class="p">),</span>
        <span class="p">)</span>
        <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">markdown_tups</span>
    <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### remove\_images [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MarkdownReader.remove_images "Permanent link")

```
remove_images(content: str) -> str
```

Remove images in markdown content.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/markdown/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">remove_images</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">content</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Remove images in markdown content."""</span>
    <span class="n">pattern</span> <span class="o">=</span> <span class="sa">r</span><span class="s2">"!</span><span class="si">{1}</span><span class="s2">\[\[(.*)\]\]"</span>
    <span class="k">return</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="n">pattern</span><span class="p">,</span> <span class="s2">""</span><span class="p">,</span> <span class="n">content</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### remove\_hyperlinks [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MarkdownReader.remove_hyperlinks "Permanent link")

```
remove_hyperlinks(content: str) -> str
```

Remove hyperlinks in markdown content.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/markdown/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">remove_hyperlinks</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">content</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Remove hyperlinks in markdown content."""</span>
    <span class="n">pattern</span> <span class="o">=</span> <span class="sa">r</span><span class="s2">"\[(.*?)\]\((.*?)\)"</span>
    <span class="k">return</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="n">pattern</span><span class="p">,</span> <span class="sa">r</span><span class="s2">"\1"</span><span class="p">,</span> <span class="n">content</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### parse\_tups [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MarkdownReader.parse_tups "Permanent link")

```
parse_tups(filepath: Path, errors: str = 'ignore', fs: Optional[AbstractFileSystem] = None) -> List[Tuple[Optional[str], str]]
```

Parse file into tuples.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/markdown/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 91</span>
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
<span class="normal">105</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">parse_tups</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">filepath</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
    <span class="n">errors</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"ignore"</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="nb">str</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Parse file into tuples."""</span>
    <span class="n">fs</span> <span class="o">=</span> <span class="n">fs</span> <span class="ow">or</span> <span class="n">LocalFileSystem</span><span class="p">()</span>
    <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">filepath</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
        <span class="n">content</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">encoding</span><span class="o">=</span><span class="s2">"utf-8"</span><span class="p">)</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_remove_hyperlinks</span><span class="p">:</span>
        <span class="n">content</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">remove_hyperlinks</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_remove_images</span><span class="p">:</span>
        <span class="n">content</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">remove_images</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">markdown_to_tups</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MarkdownReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None, fs: Optional[AbstractFileSystem] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file into string.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/markdown/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">107</span>
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
<span class="normal">124</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file into string."""</span>
    <span class="n">tups</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">parse_tups</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">)</span>
    <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="c1"># TODO: don't include headers right now</span>
    <span class="k">for</span> <span class="n">header</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">tups</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">header</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">value</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{}))</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="sa">f</span><span class="s2">"</span><span class="se">\n\n</span><span class="si">{</span><span class="n">header</span><span class="si">}</span><span class="se">\n</span><span class="si">{</span><span class="n">value</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span>
            <span class="p">)</span>
    <span class="k">return</span> <span class="n">results</span>
</code></pre></div></td></tr></tbody></table>

MboxReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MboxReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Mbox parser.

Extract messages from mailbox files. Returns string including date, subject, sender, receiver and content for each message.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/mbox/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 18</span>
<span class="normal"> 19</span>
<span class="normal"> 20</span>
<span class="normal"> 21</span>
<span class="normal"> 22</span>
<span class="normal"> 23</span>
<span class="normal"> 24</span>
<span class="normal"> 25</span>
<span class="normal"> 26</span>
<span class="normal"> 27</span>
<span class="normal"> 28</span>
<span class="normal"> 29</span>
<span class="normal"> 30</span>
<span class="normal"> 31</span>
<span class="normal"> 32</span>
<span class="normal"> 33</span>
<span class="normal"> 34</span>
<span class="normal"> 35</span>
<span class="normal"> 36</span>
<span class="normal"> 37</span>
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
<span class="normal">117</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MboxReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Mbox parser.</span>

<span class="sd">    Extract messages from mailbox files.</span>
<span class="sd">    Returns string including date, subject, sender, receiver and</span>
<span class="sd">    content for each message.</span>

<span class="sd">    """</span>

    <span class="n">DEFAULT_MESSAGE_FORMAT</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="p">(</span>
        <span class="s2">"Date: </span><span class="si">{_date}</span><span class="se">\n</span><span class="s2">"</span>
        <span class="s2">"From: </span><span class="si">{_from}</span><span class="se">\n</span><span class="s2">"</span>
        <span class="s2">"To: </span><span class="si">{_to}</span><span class="se">\n</span><span class="s2">"</span>
        <span class="s2">"Subject: </span><span class="si">{_subject}</span><span class="se">\n</span><span class="s2">"</span>
        <span class="s2">"Content: </span><span class="si">{_content}</span><span class="s2">"</span>
    <span class="p">)</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="n">max_count</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span>
        <span class="n">message_format</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_MESSAGE_FORMAT</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">bs4</span> <span class="kn">import</span> <span class="n">BeautifulSoup</span>  <span class="c1"># noqa</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"`beautifulsoup4` package not found: `pip install beautifulsoup4`"</span>
            <span class="p">)</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">max_count</span> <span class="o">=</span> <span class="n">max_count</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">message_format</span> <span class="o">=</span> <span class="n">message_format</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file into string."""</span>
        <span class="c1"># Import required libraries</span>
        <span class="kn">import</span> <span class="nn">mailbox</span>
        <span class="kn">from</span> <span class="nn">email.parser</span> <span class="kn">import</span> <span class="n">BytesParser</span>
        <span class="kn">from</span> <span class="nn">email.policy</span> <span class="kn">import</span> <span class="n">default</span>

        <span class="kn">from</span> <span class="nn">bs4</span> <span class="kn">import</span> <span class="n">BeautifulSoup</span>

        <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
                <span class="s2">"fs was specified but MboxReader doesn't support loading "</span>
                <span class="s2">"from fsspec filesystems. Will load from local filesystem instead."</span>
            <span class="p">)</span>

        <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="n">results</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="c1"># Load file using mailbox</span>
        <span class="n">bytes_parser</span> <span class="o">=</span> <span class="n">BytesParser</span><span class="p">(</span><span class="n">policy</span><span class="o">=</span><span class="n">default</span><span class="p">)</span><span class="o">.</span><span class="n">parse</span>
        <span class="n">mbox</span> <span class="o">=</span> <span class="n">mailbox</span><span class="o">.</span><span class="n">mbox</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">factory</span><span class="o">=</span><span class="n">bytes_parser</span><span class="p">)</span>  <span class="c1"># type: ignore</span>

        <span class="c1"># Iterate through all messages</span>
        <span class="k">for</span> <span class="n">_</span><span class="p">,</span> <span class="n">_msg</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">mbox</span><span class="p">):</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">msg</span><span class="p">:</span> <span class="n">mailbox</span><span class="o">.</span><span class="n">mboxMessage</span> <span class="o">=</span> <span class="n">_msg</span>
                <span class="c1"># Parse multipart messages</span>
                <span class="k">if</span> <span class="n">msg</span><span class="o">.</span><span class="n">is_multipart</span><span class="p">():</span>
                    <span class="k">for</span> <span class="n">part</span> <span class="ow">in</span> <span class="n">msg</span><span class="o">.</span><span class="n">walk</span><span class="p">():</span>
                        <span class="n">ctype</span> <span class="o">=</span> <span class="n">part</span><span class="o">.</span><span class="n">get_content_type</span><span class="p">()</span>
                        <span class="n">cdispo</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">part</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"Content-Disposition"</span><span class="p">))</span>
                        <span class="k">if</span> <span class="n">ctype</span> <span class="o">==</span> <span class="s2">"text/plain"</span> <span class="ow">and</span> <span class="s2">"attachment"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">cdispo</span><span class="p">:</span>
                            <span class="n">content</span> <span class="o">=</span> <span class="n">part</span><span class="o">.</span><span class="n">get_payload</span><span class="p">(</span><span class="n">decode</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>  <span class="c1"># decode</span>
                            <span class="k">break</span>
                <span class="c1"># Get plain message payload for non-multipart messages</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">content</span> <span class="o">=</span> <span class="n">msg</span><span class="o">.</span><span class="n">get_payload</span><span class="p">(</span><span class="n">decode</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

                <span class="c1"># Parse message HTML content and remove unneeded whitespace</span>
                <span class="n">soup</span> <span class="o">=</span> <span class="n">BeautifulSoup</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
                <span class="n">stripped_content</span> <span class="o">=</span> <span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">soup</span><span class="o">.</span><span class="n">get_text</span><span class="p">()</span><span class="o">.</span><span class="n">split</span><span class="p">())</span>
                <span class="c1"># Format message to include date, sender, receiver and subject</span>
                <span class="n">msg_string</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">message_format</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
                    <span class="n">_date</span><span class="o">=</span><span class="n">msg</span><span class="p">[</span><span class="s2">"date"</span><span class="p">],</span>
                    <span class="n">_from</span><span class="o">=</span><span class="n">msg</span><span class="p">[</span><span class="s2">"from"</span><span class="p">],</span>
                    <span class="n">_to</span><span class="o">=</span><span class="n">msg</span><span class="p">[</span><span class="s2">"to"</span><span class="p">],</span>
                    <span class="n">_subject</span><span class="o">=</span><span class="n">msg</span><span class="p">[</span><span class="s2">"subject"</span><span class="p">],</span>
                    <span class="n">_content</span><span class="o">=</span><span class="n">stripped_content</span><span class="p">,</span>
                <span class="p">)</span>
                <span class="c1"># Add message string to results</span>
                <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">msg_string</span><span class="p">)</span>
            <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Failed to parse message:</span><span class="se">\n</span><span class="si">{</span><span class="n">_msg</span><span class="si">}</span><span class="se">\n</span><span class="s2"> with exception </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

            <span class="c1"># Increment counter and return if max count is met</span>
            <span class="n">i</span> <span class="o">+=</span> <span class="mi">1</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_count</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="ow">and</span> <span class="n">i</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_count</span><span class="p">:</span>
                <span class="k">break</span>

        <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">result</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span> <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">results</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.MboxReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None, fs: Optional[AbstractFileSystem] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file into string.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/mbox/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 54</span>
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
<span class="normal">117</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file into string."""</span>
    <span class="c1"># Import required libraries</span>
    <span class="kn">import</span> <span class="nn">mailbox</span>
    <span class="kn">from</span> <span class="nn">email.parser</span> <span class="kn">import</span> <span class="n">BytesParser</span>
    <span class="kn">from</span> <span class="nn">email.policy</span> <span class="kn">import</span> <span class="n">default</span>

    <span class="kn">from</span> <span class="nn">bs4</span> <span class="kn">import</span> <span class="n">BeautifulSoup</span>

    <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span>
            <span class="s2">"fs was specified but MboxReader doesn't support loading "</span>
            <span class="s2">"from fsspec filesystems. Will load from local filesystem instead."</span>
        <span class="p">)</span>

    <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="n">results</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="c1"># Load file using mailbox</span>
    <span class="n">bytes_parser</span> <span class="o">=</span> <span class="n">BytesParser</span><span class="p">(</span><span class="n">policy</span><span class="o">=</span><span class="n">default</span><span class="p">)</span><span class="o">.</span><span class="n">parse</span>
    <span class="n">mbox</span> <span class="o">=</span> <span class="n">mailbox</span><span class="o">.</span><span class="n">mbox</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">factory</span><span class="o">=</span><span class="n">bytes_parser</span><span class="p">)</span>  <span class="c1"># type: ignore</span>

    <span class="c1"># Iterate through all messages</span>
    <span class="k">for</span> <span class="n">_</span><span class="p">,</span> <span class="n">_msg</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">mbox</span><span class="p">):</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">msg</span><span class="p">:</span> <span class="n">mailbox</span><span class="o">.</span><span class="n">mboxMessage</span> <span class="o">=</span> <span class="n">_msg</span>
            <span class="c1"># Parse multipart messages</span>
            <span class="k">if</span> <span class="n">msg</span><span class="o">.</span><span class="n">is_multipart</span><span class="p">():</span>
                <span class="k">for</span> <span class="n">part</span> <span class="ow">in</span> <span class="n">msg</span><span class="o">.</span><span class="n">walk</span><span class="p">():</span>
                    <span class="n">ctype</span> <span class="o">=</span> <span class="n">part</span><span class="o">.</span><span class="n">get_content_type</span><span class="p">()</span>
                    <span class="n">cdispo</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">part</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"Content-Disposition"</span><span class="p">))</span>
                    <span class="k">if</span> <span class="n">ctype</span> <span class="o">==</span> <span class="s2">"text/plain"</span> <span class="ow">and</span> <span class="s2">"attachment"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">cdispo</span><span class="p">:</span>
                        <span class="n">content</span> <span class="o">=</span> <span class="n">part</span><span class="o">.</span><span class="n">get_payload</span><span class="p">(</span><span class="n">decode</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>  <span class="c1"># decode</span>
                        <span class="k">break</span>
            <span class="c1"># Get plain message payload for non-multipart messages</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">content</span> <span class="o">=</span> <span class="n">msg</span><span class="o">.</span><span class="n">get_payload</span><span class="p">(</span><span class="n">decode</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

            <span class="c1"># Parse message HTML content and remove unneeded whitespace</span>
            <span class="n">soup</span> <span class="o">=</span> <span class="n">BeautifulSoup</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
            <span class="n">stripped_content</span> <span class="o">=</span> <span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">soup</span><span class="o">.</span><span class="n">get_text</span><span class="p">()</span><span class="o">.</span><span class="n">split</span><span class="p">())</span>
            <span class="c1"># Format message to include date, sender, receiver and subject</span>
            <span class="n">msg_string</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">message_format</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
                <span class="n">_date</span><span class="o">=</span><span class="n">msg</span><span class="p">[</span><span class="s2">"date"</span><span class="p">],</span>
                <span class="n">_from</span><span class="o">=</span><span class="n">msg</span><span class="p">[</span><span class="s2">"from"</span><span class="p">],</span>
                <span class="n">_to</span><span class="o">=</span><span class="n">msg</span><span class="p">[</span><span class="s2">"to"</span><span class="p">],</span>
                <span class="n">_subject</span><span class="o">=</span><span class="n">msg</span><span class="p">[</span><span class="s2">"subject"</span><span class="p">],</span>
                <span class="n">_content</span><span class="o">=</span><span class="n">stripped_content</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="c1"># Add message string to results</span>
            <span class="n">results</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">msg_string</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">warning</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Failed to parse message:</span><span class="se">\n</span><span class="si">{</span><span class="n">_msg</span><span class="si">}</span><span class="se">\n</span><span class="s2"> with exception </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="c1"># Increment counter and return if max count is met</span>
        <span class="n">i</span> <span class="o">+=</span> <span class="mi">1</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_count</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="ow">and</span> <span class="n">i</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_count</span><span class="p">:</span>
            <span class="k">break</span>

    <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">result</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span> <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">results</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

PDFReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PDFReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

PDF parser.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/docs/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span>
<span class="normal">97</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PDFReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""PDF parser."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">return_full_document</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Initialize PDFReader.</span>
<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">return_full_document</span> <span class="o">=</span> <span class="n">return_full_document</span>

    <span class="nd">@retry</span><span class="p">(</span>
        <span class="n">stop</span><span class="o">=</span><span class="n">stop_after_attempt</span><span class="p">(</span><span class="n">RETRY_TIMES</span><span class="p">),</span>
    <span class="p">)</span>
    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file."""</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">Path</span><span class="p">):</span>
            <span class="n">file</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">pypdf</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"pypdf is required to read PDF files: `pip install pypdf`"</span>
            <span class="p">)</span>
        <span class="n">fs</span> <span class="o">=</span> <span class="n">fs</span> <span class="ow">or</span> <span class="n">get_default_fs</span><span class="p">()</span>
        <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="s2">"rb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">fp</span><span class="p">:</span>
            <span class="c1"># Load the file in memory if the filesystem is not the default one to avoid</span>
            <span class="c1"># issues with pypdf</span>
            <span class="n">stream</span> <span class="o">=</span> <span class="n">fp</span> <span class="k">if</span> <span class="n">is_default_fs</span><span class="p">(</span><span class="n">fs</span><span class="p">)</span> <span class="k">else</span> <span class="n">io</span><span class="o">.</span><span class="n">BytesIO</span><span class="p">(</span><span class="n">fp</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>

            <span class="c1"># Create a PDF object</span>
            <span class="n">pdf</span> <span class="o">=</span> <span class="n">pypdf</span><span class="o">.</span><span class="n">PdfReader</span><span class="p">(</span><span class="n">stream</span><span class="p">)</span>

            <span class="c1"># Get the number of pages in the PDF document</span>
            <span class="n">num_pages</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">pdf</span><span class="o">.</span><span class="n">pages</span><span class="p">)</span>

            <span class="n">docs</span> <span class="o">=</span> <span class="p">[]</span>

            <span class="c1"># This block returns a whole PDF as a single Document</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">return_full_document</span><span class="p">:</span>
                <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"file_name"</span><span class="p">:</span> <span class="n">file</span><span class="o">.</span><span class="n">name</span><span class="p">}</span>
                <span class="k">if</span> <span class="n">extra_info</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="n">metadata</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">extra_info</span><span class="p">)</span>

                <span class="c1"># Join text extracted from each page</span>
                <span class="n">text</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                    <span class="n">pdf</span><span class="o">.</span><span class="n">pages</span><span class="p">[</span><span class="n">page</span><span class="p">]</span><span class="o">.</span><span class="n">extract_text</span><span class="p">()</span> <span class="k">for</span> <span class="n">page</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">num_pages</span><span class="p">)</span>
                <span class="p">)</span>

                <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">))</span>

            <span class="c1"># This block returns each page of a PDF as its own Document</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="c1"># Iterate over every page</span>

                <span class="k">for</span> <span class="n">page</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">num_pages</span><span class="p">):</span>
                    <span class="c1"># Extract the text from the page</span>
                    <span class="n">page_text</span> <span class="o">=</span> <span class="n">pdf</span><span class="o">.</span><span class="n">pages</span><span class="p">[</span><span class="n">page</span><span class="p">]</span><span class="o">.</span><span class="n">extract_text</span><span class="p">()</span>
                    <span class="n">page_label</span> <span class="o">=</span> <span class="n">pdf</span><span class="o">.</span><span class="n">page_labels</span><span class="p">[</span><span class="n">page</span><span class="p">]</span>

                    <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"page_label"</span><span class="p">:</span> <span class="n">page_label</span><span class="p">,</span> <span class="s2">"file_name"</span><span class="p">:</span> <span class="n">file</span><span class="o">.</span><span class="n">name</span><span class="p">}</span>
                    <span class="k">if</span> <span class="n">extra_info</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                        <span class="n">metadata</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">extra_info</span><span class="p">)</span>

                    <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">page_text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">))</span>

            <span class="k">return</span> <span class="n">docs</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PDFReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None, fs: Optional[AbstractFileSystem] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/docs/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span>
<span class="normal">97</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@retry</span><span class="p">(</span>
    <span class="n">stop</span><span class="o">=</span><span class="n">stop_after_attempt</span><span class="p">(</span><span class="n">RETRY_TIMES</span><span class="p">),</span>
<span class="p">)</span>
<span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file."""</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">Path</span><span class="p">):</span>
        <span class="n">file</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>

    <span class="k">try</span><span class="p">:</span>
        <span class="kn">import</span> <span class="nn">pypdf</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
            <span class="s2">"pypdf is required to read PDF files: `pip install pypdf`"</span>
        <span class="p">)</span>
    <span class="n">fs</span> <span class="o">=</span> <span class="n">fs</span> <span class="ow">or</span> <span class="n">get_default_fs</span><span class="p">()</span>
    <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="s2">"rb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">fp</span><span class="p">:</span>
        <span class="c1"># Load the file in memory if the filesystem is not the default one to avoid</span>
        <span class="c1"># issues with pypdf</span>
        <span class="n">stream</span> <span class="o">=</span> <span class="n">fp</span> <span class="k">if</span> <span class="n">is_default_fs</span><span class="p">(</span><span class="n">fs</span><span class="p">)</span> <span class="k">else</span> <span class="n">io</span><span class="o">.</span><span class="n">BytesIO</span><span class="p">(</span><span class="n">fp</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>

        <span class="c1"># Create a PDF object</span>
        <span class="n">pdf</span> <span class="o">=</span> <span class="n">pypdf</span><span class="o">.</span><span class="n">PdfReader</span><span class="p">(</span><span class="n">stream</span><span class="p">)</span>

        <span class="c1"># Get the number of pages in the PDF document</span>
        <span class="n">num_pages</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">pdf</span><span class="o">.</span><span class="n">pages</span><span class="p">)</span>

        <span class="n">docs</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="c1"># This block returns a whole PDF as a single Document</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">return_full_document</span><span class="p">:</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"file_name"</span><span class="p">:</span> <span class="n">file</span><span class="o">.</span><span class="n">name</span><span class="p">}</span>
            <span class="k">if</span> <span class="n">extra_info</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">metadata</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">extra_info</span><span class="p">)</span>

            <span class="c1"># Join text extracted from each page</span>
            <span class="n">text</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                <span class="n">pdf</span><span class="o">.</span><span class="n">pages</span><span class="p">[</span><span class="n">page</span><span class="p">]</span><span class="o">.</span><span class="n">extract_text</span><span class="p">()</span> <span class="k">for</span> <span class="n">page</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">num_pages</span><span class="p">)</span>
            <span class="p">)</span>

            <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">))</span>

        <span class="c1"># This block returns each page of a PDF as its own Document</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># Iterate over every page</span>

            <span class="k">for</span> <span class="n">page</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">num_pages</span><span class="p">):</span>
                <span class="c1"># Extract the text from the page</span>
                <span class="n">page_text</span> <span class="o">=</span> <span class="n">pdf</span><span class="o">.</span><span class="n">pages</span><span class="p">[</span><span class="n">page</span><span class="p">]</span><span class="o">.</span><span class="n">extract_text</span><span class="p">()</span>
                <span class="n">page_label</span> <span class="o">=</span> <span class="n">pdf</span><span class="o">.</span><span class="n">page_labels</span><span class="p">[</span><span class="n">page</span><span class="p">]</span>

                <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"page_label"</span><span class="p">:</span> <span class="n">page_label</span><span class="p">,</span> <span class="s2">"file_name"</span><span class="p">:</span> <span class="n">file</span><span class="o">.</span><span class="n">name</span><span class="p">}</span>
                <span class="k">if</span> <span class="n">extra_info</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="n">metadata</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">extra_info</span><span class="p">)</span>

                <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">page_text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">docs</span>
</code></pre></div></td></tr></tbody></table>

PagedCSVReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PagedCSVReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Paged CSV parser.

Displayed each row in an LLM-friendly format on a separate document.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `encoding` | `str` | 
Encoding used to open the file. utf-8 by default.



 | `'utf-8'` |

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/paged_csv/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PagedCSVReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Paged CSV parser.</span>

<span class="sd">    Displayed each row in an LLM-friendly format on a separate document.</span>

<span class="sd">    Args:</span>
<span class="sd">        encoding (str): Encoding used to open the file.</span>
<span class="sd">            utf-8 by default.</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">encoding</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"utf-8"</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_encoding</span> <span class="o">=</span> <span class="n">encoding</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">delimiter</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">","</span><span class="p">,</span>
        <span class="n">quotechar</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">'"'</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file."""</span>
        <span class="kn">import</span> <span class="nn">csv</span>

        <span class="n">docs</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_encoding</span><span class="p">)</span> <span class="k">as</span> <span class="n">fp</span><span class="p">:</span>
            <span class="n">csv_reader</span> <span class="o">=</span> <span class="n">csv</span><span class="o">.</span><span class="n">DictReader</span><span class="p">(</span><span class="n">f</span><span class="o">=</span><span class="n">fp</span><span class="p">,</span> <span class="n">delimiter</span><span class="o">=</span><span class="n">delimiter</span><span class="p">,</span> <span class="n">quotechar</span><span class="o">=</span><span class="n">quotechar</span><span class="p">)</span>  <span class="c1"># type: ignore</span>
            <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">csv_reader</span><span class="p">:</span>
                <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">Document</span><span class="p">(</span>
                        <span class="n">text</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                            <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">k</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">v</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="si">}</span><span class="s2">"</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">row</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
                        <span class="p">),</span>
                        <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{},</span>
                    <span class="p">)</span>
                <span class="p">)</span>
        <span class="k">return</span> <span class="n">docs</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PagedCSVReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None, delimiter: str = ',', quotechar: str = '"') -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/paged_csv/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">delimiter</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">","</span><span class="p">,</span>
    <span class="n">quotechar</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">'"'</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file."""</span>
    <span class="kn">import</span> <span class="nn">csv</span>

    <span class="n">docs</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_encoding</span><span class="p">)</span> <span class="k">as</span> <span class="n">fp</span><span class="p">:</span>
        <span class="n">csv_reader</span> <span class="o">=</span> <span class="n">csv</span><span class="o">.</span><span class="n">DictReader</span><span class="p">(</span><span class="n">f</span><span class="o">=</span><span class="n">fp</span><span class="p">,</span> <span class="n">delimiter</span><span class="o">=</span><span class="n">delimiter</span><span class="p">,</span> <span class="n">quotechar</span><span class="o">=</span><span class="n">quotechar</span><span class="p">)</span>  <span class="c1"># type: ignore</span>
        <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">csv_reader</span><span class="p">:</span>
            <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">Document</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
                        <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">k</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">v</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="si">}</span><span class="s2">"</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">row</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
                    <span class="p">),</span>
                    <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{},</span>
                <span class="p">)</span>
            <span class="p">)</span>
    <span class="k">return</span> <span class="n">docs</span>
</code></pre></div></td></tr></tbody></table>

PandasCSVReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PandasCSVReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Pandas-based CSV parser.

Parses CSVs using the separator detection from Pandas `read_csv`function. If special parameters are required, use the `pandas_config` dict.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `concat_rows` | `bool` | 
whether to concatenate all rows into one document. If set to False, a Document will be created for each row. True by default.



 | `True` |
| `col_joiner` | `str` | 

Separator to use for joining cols per row. Set to ", " by default.



 | `', '` |
| `row_joiner` | `str` | 

Separator to use for joining each row. Only used when `concat_rows=True`. Set to "\\n" by default.



 | `'\n'` |
| `pandas_config` | `dict` | 

Options for the `pandas.read_csv` function call. Refer to https://pandas.pydata.org/docs/reference/api/pandas.read\_csv.html for more information. Set to empty dict by default, this means pandas will try to figure out the separators, table head, etc. on its own.



 | `{}` |

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/tabular/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 61</span>
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
<span class="normal">129</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PandasCSVReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sa">r</span><span class="sd">"""Pandas-based CSV parser.</span>

<span class="sd">    Parses CSVs using the separator detection from Pandas `read_csv`function.</span>
<span class="sd">    If special parameters are required, use the `pandas_config` dict.</span>

<span class="sd">    Args:</span>
<span class="sd">        concat_rows (bool): whether to concatenate all rows into one document.</span>
<span class="sd">            If set to False, a Document will be created for each row.</span>
<span class="sd">            True by default.</span>

<span class="sd">        col_joiner (str): Separator to use for joining cols per row.</span>
<span class="sd">            Set to ", " by default.</span>

<span class="sd">        row_joiner (str): Separator to use for joining each row.</span>
<span class="sd">            Only used when `concat_rows=True`.</span>
<span class="sd">            Set to "\n" by default.</span>

<span class="sd">        pandas_config (dict): Options for the `pandas.read_csv` function call.</span>
<span class="sd">            Refer to https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html</span>
<span class="sd">            for more information.</span>
<span class="sd">            Set to empty dict by default, this means pandas will try to figure</span>
<span class="sd">            out the separators, table head, etc. on its own.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="n">concat_rows</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">col_joiner</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">", "</span><span class="p">,</span>
        <span class="n">row_joiner</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span>
        <span class="n">pandas_config</span><span class="p">:</span> <span class="nb">dict</span> <span class="o">=</span> <span class="p">{},</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_concat_rows</span> <span class="o">=</span> <span class="n">concat_rows</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_col_joiner</span> <span class="o">=</span> <span class="n">col_joiner</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_row_joiner</span> <span class="o">=</span> <span class="n">row_joiner</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_pandas_config</span> <span class="o">=</span> <span class="n">pandas_config</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file."""</span>
        <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
            <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                <span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_pandas_config</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_pandas_config</span><span class="p">)</span>

        <span class="n">text_list</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span>
            <span class="k">lambda</span> <span class="n">row</span><span class="p">:</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_col_joiner</span><span class="p">)</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">row</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span><span class="o">.</span><span class="n">tolist</span><span class="p">()),</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span>
        <span class="p">)</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_concat_rows</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[</span>
                <span class="n">Document</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_row_joiner</span><span class="p">)</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_list</span><span class="p">),</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{}</span>
                <span class="p">)</span>
            <span class="p">]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[</span>
                <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span> <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">text_list</span>
            <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PandasCSVReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None, fs: Optional[AbstractFileSystem] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/tabular/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">103</span>
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
<span class="normal">129</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file."""</span>
    <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
        <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_pandas_config</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_pandas_config</span><span class="p">)</span>

    <span class="n">text_list</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span>
        <span class="k">lambda</span> <span class="n">row</span><span class="p">:</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_col_joiner</span><span class="p">)</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">row</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span><span class="o">.</span><span class="n">tolist</span><span class="p">()),</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span>
    <span class="p">)</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>

    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_concat_rows</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">[</span>
            <span class="n">Document</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_row_joiner</span><span class="p">)</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_list</span><span class="p">),</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{}</span>
            <span class="p">)</span>
        <span class="p">]</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">[</span>
            <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span> <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">text_list</span>
        <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

PandasExcelReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PandasExcelReader "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Pandas-based Excel parser.

Parses Excel files using the Pandas `read_excel`function. If special parameters are required, use the `pandas_config` dict.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `concat_rows` | `bool` | 
whether to concatenate all rows into one document. If set to False, a Document will be created for each row. True by default.



 | `True` |
| `sheet_name` | `str | int | None` | 

Defaults to None, for all sheets, otherwise pass a str or int to specify the sheet to read.



 | `None` |
| `pandas_config` | `dict` | 

Options for the `pandas.read_excel` function call. Refer to https://pandas.pydata.org/docs/reference/api/pandas.read\_excel.html for more information. Set to empty dict by default.



 | `{}` |

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/tabular/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">132</span>
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
<span class="normal">231</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PandasExcelReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sa">r</span><span class="sd">"""Pandas-based Excel parser.</span>

<span class="sd">    Parses Excel files using the Pandas `read_excel`function.</span>
<span class="sd">    If special parameters are required, use the `pandas_config` dict.</span>

<span class="sd">    Args:</span>
<span class="sd">        concat_rows (bool): whether to concatenate all rows into one document.</span>
<span class="sd">            If set to False, a Document will be created for each row.</span>
<span class="sd">            True by default.</span>

<span class="sd">        sheet_name (str | int | None): Defaults to None, for all sheets, otherwise pass a str or int to specify the sheet to read.</span>

<span class="sd">        pandas_config (dict): Options for the `pandas.read_excel` function call.</span>
<span class="sd">            Refer to https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html</span>
<span class="sd">            for more information.</span>
<span class="sd">            Set to empty dict by default.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="n">concat_rows</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">sheet_name</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
        <span class="n">pandas_config</span><span class="p">:</span> <span class="nb">dict</span> <span class="o">=</span> <span class="p">{},</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_concat_rows</span> <span class="o">=</span> <span class="n">concat_rows</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_sheet_name</span> <span class="o">=</span> <span class="n">sheet_name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_pandas_config</span> <span class="o">=</span> <span class="n">pandas_config</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file."""</span>
        <span class="n">openpyxl_spec</span> <span class="o">=</span> <span class="n">importlib</span><span class="o">.</span><span class="n">util</span><span class="o">.</span><span class="n">find_spec</span><span class="p">(</span><span class="s2">"openpyxl"</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">openpyxl_spec</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">pass</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"Please install openpyxl to read Excel files. You can install it with 'pip install openpyxl'"</span>
            <span class="p">)</span>

        <span class="c1"># sheet_name of None is all sheets, otherwise indexing starts at 0</span>
        <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
            <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                <span class="n">dfs</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_excel</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sheet_name</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_pandas_config</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">dfs</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_excel</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sheet_name</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_pandas_config</span><span class="p">)</span>

        <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="c1"># handle the case where only a single DataFrame is returned</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">dfs</span><span class="p">,</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">):</span>
            <span class="n">df</span> <span class="o">=</span> <span class="n">dfs</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="s2">""</span><span class="p">)</span>

            <span class="c1"># Convert DataFrame to list of rows</span>
            <span class="n">text_list</span> <span class="o">=</span> <span class="p">(</span>
                <span class="n">df</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">row</span><span class="p">:</span> <span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">row</span><span class="o">.</span><span class="n">values</span><span class="p">),</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>
            <span class="p">)</span>

            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_concat_rows</span><span class="p">:</span>
                <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_list</span><span class="p">),</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">documents</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                    <span class="p">[</span>
                        <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span>
                        <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">text_list</span>
                    <span class="p">]</span>
                <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">df</span> <span class="ow">in</span> <span class="n">dfs</span><span class="o">.</span><span class="n">values</span><span class="p">():</span>
                <span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="s2">""</span><span class="p">)</span>

                <span class="c1"># Convert DataFrame to list of rows</span>
                <span class="n">text_list</span> <span class="o">=</span> <span class="p">(</span>
                    <span class="n">df</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">row</span><span class="p">:</span> <span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">row</span><span class="p">),</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>
                <span class="p">)</span>

                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_concat_rows</span><span class="p">:</span>
                    <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_list</span><span class="p">),</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span>
                    <span class="p">)</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">documents</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                        <span class="p">[</span>
                            <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span>
                            <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">text_list</span>
                        <span class="p">]</span>
                    <span class="p">)</span>

        <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PandasExcelReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None, fs: Optional[AbstractFileSystem] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/tabular/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">166</span>
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
<span class="normal">231</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file."""</span>
    <span class="n">openpyxl_spec</span> <span class="o">=</span> <span class="n">importlib</span><span class="o">.</span><span class="n">util</span><span class="o">.</span><span class="n">find_spec</span><span class="p">(</span><span class="s2">"openpyxl"</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">openpyxl_spec</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">pass</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
            <span class="s2">"Please install openpyxl to read Excel files. You can install it with 'pip install openpyxl'"</span>
        <span class="p">)</span>

    <span class="c1"># sheet_name of None is all sheets, otherwise indexing starts at 0</span>
    <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
        <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">dfs</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_excel</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sheet_name</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_pandas_config</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">dfs</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_excel</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_sheet_name</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_pandas_config</span><span class="p">)</span>

    <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="c1"># handle the case where only a single DataFrame is returned</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">dfs</span><span class="p">,</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">):</span>
        <span class="n">df</span> <span class="o">=</span> <span class="n">dfs</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="s2">""</span><span class="p">)</span>

        <span class="c1"># Convert DataFrame to list of rows</span>
        <span class="n">text_list</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">df</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">row</span><span class="p">:</span> <span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">row</span><span class="o">.</span><span class="n">values</span><span class="p">),</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_concat_rows</span><span class="p">:</span>
            <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_list</span><span class="p">),</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">documents</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                <span class="p">[</span>
                    <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span>
                    <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">text_list</span>
                <span class="p">]</span>
            <span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">df</span> <span class="ow">in</span> <span class="n">dfs</span><span class="o">.</span><span class="n">values</span><span class="p">():</span>
            <span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="s2">""</span><span class="p">)</span>

            <span class="c1"># Convert DataFrame to list of rows</span>
            <span class="n">text_list</span> <span class="o">=</span> <span class="p">(</span>
                <span class="n">df</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">row</span><span class="p">:</span> <span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">row</span><span class="p">),</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>
            <span class="p">)</span>

            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_concat_rows</span><span class="p">:</span>
                <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                    <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_list</span><span class="p">),</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span>
                <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">documents</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                    <span class="p">[</span>
                        <span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})</span>
                        <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">text_list</span>
                    <span class="p">]</span>
                <span class="p">)</span>

    <span class="k">return</span> <span class="n">documents</span>
</code></pre></div></td></tr></tbody></table>

PptxReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PptxReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Powerpoint parser.

Extract text, caption images, and specify slides.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/slides/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 18</span>
<span class="normal"> 19</span>
<span class="normal"> 20</span>
<span class="normal"> 21</span>
<span class="normal"> 22</span>
<span class="normal"> 23</span>
<span class="normal"> 24</span>
<span class="normal"> 25</span>
<span class="normal"> 26</span>
<span class="normal"> 27</span>
<span class="normal"> 28</span>
<span class="normal"> 29</span>
<span class="normal"> 30</span>
<span class="normal"> 31</span>
<span class="normal"> 32</span>
<span class="normal"> 33</span>
<span class="normal"> 34</span>
<span class="normal"> 35</span>
<span class="normal"> 36</span>
<span class="normal"> 37</span>
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
<span class="normal">122</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PptxReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Powerpoint parser.</span>

<span class="sd">    Extract text, caption images, and specify slides.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init parser."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">torch</span>  <span class="c1"># noqa</span>
            <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>  <span class="c1"># noqa</span>
            <span class="kn">from</span> <span class="nn">pptx</span> <span class="kn">import</span> <span class="n">Presentation</span>  <span class="c1"># noqa</span>
            <span class="kn">from</span> <span class="nn">transformers</span> <span class="kn">import</span> <span class="p">(</span>
                <span class="n">AutoTokenizer</span><span class="p">,</span>
                <span class="n">VisionEncoderDecoderModel</span><span class="p">,</span>
                <span class="n">ViTFeatureExtractor</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"Please install extra dependencies that are required for "</span>
                <span class="s2">"the PptxReader: "</span>
                <span class="s2">"`pip install torch transformers python-pptx Pillow`"</span>
            <span class="p">)</span>

        <span class="n">model</span> <span class="o">=</span> <span class="n">VisionEncoderDecoderModel</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span>
            <span class="s2">"nlpconnect/vit-gpt2-image-captioning"</span>
        <span class="p">)</span>
        <span class="n">feature_extractor</span> <span class="o">=</span> <span class="n">ViTFeatureExtractor</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span>
            <span class="s2">"nlpconnect/vit-gpt2-image-captioning"</span>
        <span class="p">)</span>
        <span class="n">tokenizer</span> <span class="o">=</span> <span class="n">AutoTokenizer</span><span class="o">.</span><span class="n">from_pretrained</span><span class="p">(</span>
            <span class="s2">"nlpconnect/vit-gpt2-image-captioning"</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">parser_config</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"feature_extractor"</span><span class="p">:</span> <span class="n">feature_extractor</span><span class="p">,</span>
            <span class="s2">"model"</span><span class="p">:</span> <span class="n">model</span><span class="p">,</span>
            <span class="s2">"tokenizer"</span><span class="p">:</span> <span class="n">tokenizer</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">caption_image</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tmp_image_file</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Generate text caption of image."""</span>
        <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>

        <span class="n">model</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">parser_config</span><span class="p">[</span><span class="s2">"model"</span><span class="p">]</span>
        <span class="n">feature_extractor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">parser_config</span><span class="p">[</span><span class="s2">"feature_extractor"</span><span class="p">]</span>
        <span class="n">tokenizer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">parser_config</span><span class="p">[</span><span class="s2">"tokenizer"</span><span class="p">]</span>

        <span class="n">device</span> <span class="o">=</span> <span class="n">infer_torch_device</span><span class="p">()</span>
        <span class="n">model</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>

        <span class="n">max_length</span> <span class="o">=</span> <span class="mi">16</span>
        <span class="n">num_beams</span> <span class="o">=</span> <span class="mi">4</span>
        <span class="n">gen_kwargs</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"max_length"</span><span class="p">:</span> <span class="n">max_length</span><span class="p">,</span> <span class="s2">"num_beams"</span><span class="p">:</span> <span class="n">num_beams</span><span class="p">}</span>

        <span class="n">i_image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">tmp_image_file</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">i_image</span><span class="o">.</span><span class="n">mode</span> <span class="o">!=</span> <span class="s2">"RGB"</span><span class="p">:</span>
            <span class="n">i_image</span> <span class="o">=</span> <span class="n">i_image</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="n">mode</span><span class="o">=</span><span class="s2">"RGB"</span><span class="p">)</span>

        <span class="n">pixel_values</span> <span class="o">=</span> <span class="n">feature_extractor</span><span class="p">(</span>
            <span class="n">images</span><span class="o">=</span><span class="p">[</span><span class="n">i_image</span><span class="p">],</span> <span class="n">return_tensors</span><span class="o">=</span><span class="s2">"pt"</span>
        <span class="p">)</span><span class="o">.</span><span class="n">pixel_values</span>
        <span class="n">pixel_values</span> <span class="o">=</span> <span class="n">pixel_values</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>

        <span class="n">output_ids</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span><span class="n">pixel_values</span><span class="p">,</span> <span class="o">**</span><span class="n">gen_kwargs</span><span class="p">)</span>

        <span class="n">preds</span> <span class="o">=</span> <span class="n">tokenizer</span><span class="o">.</span><span class="n">batch_decode</span><span class="p">(</span><span class="n">output_ids</span><span class="p">,</span> <span class="n">skip_special_tokens</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">preds</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file."""</span>
        <span class="kn">from</span> <span class="nn">pptx</span> <span class="kn">import</span> <span class="n">Presentation</span>

        <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
            <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                <span class="n">presentation</span> <span class="o">=</span> <span class="n">Presentation</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">presentation</span> <span class="o">=</span> <span class="n">Presentation</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
        <span class="n">result</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">slide</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">presentation</span><span class="o">.</span><span class="n">slides</span><span class="p">):</span>
            <span class="n">result</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"</span><span class="se">\n\n</span><span class="s2">Slide #</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">: </span><span class="se">\n</span><span class="s2">"</span>
            <span class="k">for</span> <span class="n">shape</span> <span class="ow">in</span> <span class="n">slide</span><span class="o">.</span><span class="n">shapes</span><span class="p">:</span>
                <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">shape</span><span class="p">,</span> <span class="s2">"image"</span><span class="p">):</span>
                    <span class="n">image</span> <span class="o">=</span> <span class="n">shape</span><span class="o">.</span><span class="n">image</span>
                    <span class="c1"># get image "file" contents</span>
                    <span class="n">image_bytes</span> <span class="o">=</span> <span class="n">image</span><span class="o">.</span><span class="n">blob</span>
                    <span class="c1"># temporarily save the image to feed into model</span>
                    <span class="n">f</span> <span class="o">=</span> <span class="n">tempfile</span><span class="o">.</span><span class="n">NamedTemporaryFile</span><span class="p">(</span><span class="s2">"wb"</span><span class="p">,</span> <span class="n">delete</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
                    <span class="k">try</span><span class="p">:</span>
                        <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">image_bytes</span><span class="p">)</span>
                        <span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
                        <span class="n">result</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"</span><span class="se">\n</span><span class="s2"> Image: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">caption_image</span><span class="p">(</span><span class="n">f</span><span class="o">.</span><span class="n">name</span><span class="p">)</span><span class="si">}</span><span class="se">\n\n</span><span class="s2">"</span>
                    <span class="k">finally</span><span class="p">:</span>
                        <span class="n">os</span><span class="o">.</span><span class="n">unlink</span><span class="p">(</span><span class="n">f</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>

                <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">shape</span><span class="p">,</span> <span class="s2">"text"</span><span class="p">):</span>
                    <span class="n">result</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">shape</span><span class="o">.</span><span class="n">text</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span>

        <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">result</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})]</span>
</code></pre></div></td></tr></tbody></table>

### caption\_image [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PptxReader.caption_image "Permanent link")

```
caption_image(tmp_image_file: str) -> str
```

Generate text caption of image.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/slides/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">caption_image</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tmp_image_file</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Generate text caption of image."""</span>
    <span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>

    <span class="n">model</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">parser_config</span><span class="p">[</span><span class="s2">"model"</span><span class="p">]</span>
    <span class="n">feature_extractor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">parser_config</span><span class="p">[</span><span class="s2">"feature_extractor"</span><span class="p">]</span>
    <span class="n">tokenizer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">parser_config</span><span class="p">[</span><span class="s2">"tokenizer"</span><span class="p">]</span>

    <span class="n">device</span> <span class="o">=</span> <span class="n">infer_torch_device</span><span class="p">()</span>
    <span class="n">model</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>

    <span class="n">max_length</span> <span class="o">=</span> <span class="mi">16</span>
    <span class="n">num_beams</span> <span class="o">=</span> <span class="mi">4</span>
    <span class="n">gen_kwargs</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"max_length"</span><span class="p">:</span> <span class="n">max_length</span><span class="p">,</span> <span class="s2">"num_beams"</span><span class="p">:</span> <span class="n">num_beams</span><span class="p">}</span>

    <span class="n">i_image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">tmp_image_file</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">i_image</span><span class="o">.</span><span class="n">mode</span> <span class="o">!=</span> <span class="s2">"RGB"</span><span class="p">:</span>
        <span class="n">i_image</span> <span class="o">=</span> <span class="n">i_image</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="n">mode</span><span class="o">=</span><span class="s2">"RGB"</span><span class="p">)</span>

    <span class="n">pixel_values</span> <span class="o">=</span> <span class="n">feature_extractor</span><span class="p">(</span>
        <span class="n">images</span><span class="o">=</span><span class="p">[</span><span class="n">i_image</span><span class="p">],</span> <span class="n">return_tensors</span><span class="o">=</span><span class="s2">"pt"</span>
    <span class="p">)</span><span class="o">.</span><span class="n">pixel_values</span>
    <span class="n">pixel_values</span> <span class="o">=</span> <span class="n">pixel_values</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>

    <span class="n">output_ids</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">generate</span><span class="p">(</span><span class="n">pixel_values</span><span class="p">,</span> <span class="o">**</span><span class="n">gen_kwargs</span><span class="p">)</span>

    <span class="n">preds</span> <span class="o">=</span> <span class="n">tokenizer</span><span class="o">.</span><span class="n">batch_decode</span><span class="p">(</span><span class="n">output_ids</span><span class="p">,</span> <span class="n">skip_special_tokens</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">preds</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PptxReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None, fs: Optional[AbstractFileSystem] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/slides/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 88</span>
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
<span class="normal">122</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file."""</span>
    <span class="kn">from</span> <span class="nn">pptx</span> <span class="kn">import</span> <span class="n">Presentation</span>

    <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
        <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">presentation</span> <span class="o">=</span> <span class="n">Presentation</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">presentation</span> <span class="o">=</span> <span class="n">Presentation</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
    <span class="n">result</span> <span class="o">=</span> <span class="s2">""</span>
    <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">slide</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">presentation</span><span class="o">.</span><span class="n">slides</span><span class="p">):</span>
        <span class="n">result</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"</span><span class="se">\n\n</span><span class="s2">Slide #</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s2">: </span><span class="se">\n</span><span class="s2">"</span>
        <span class="k">for</span> <span class="n">shape</span> <span class="ow">in</span> <span class="n">slide</span><span class="o">.</span><span class="n">shapes</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">shape</span><span class="p">,</span> <span class="s2">"image"</span><span class="p">):</span>
                <span class="n">image</span> <span class="o">=</span> <span class="n">shape</span><span class="o">.</span><span class="n">image</span>
                <span class="c1"># get image "file" contents</span>
                <span class="n">image_bytes</span> <span class="o">=</span> <span class="n">image</span><span class="o">.</span><span class="n">blob</span>
                <span class="c1"># temporarily save the image to feed into model</span>
                <span class="n">f</span> <span class="o">=</span> <span class="n">tempfile</span><span class="o">.</span><span class="n">NamedTemporaryFile</span><span class="p">(</span><span class="s2">"wb"</span><span class="p">,</span> <span class="n">delete</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">image_bytes</span><span class="p">)</span>
                    <span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
                    <span class="n">result</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"</span><span class="se">\n</span><span class="s2"> Image: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">caption_image</span><span class="p">(</span><span class="n">f</span><span class="o">.</span><span class="n">name</span><span class="p">)</span><span class="si">}</span><span class="se">\n\n</span><span class="s2">"</span>
                <span class="k">finally</span><span class="p">:</span>
                    <span class="n">os</span><span class="o">.</span><span class="n">unlink</span><span class="p">(</span><span class="n">f</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>

            <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">shape</span><span class="p">,</span> <span class="s2">"text"</span><span class="p">):</span>
                <span class="n">result</span> <span class="o">+=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">shape</span><span class="o">.</span><span class="n">text</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span>

    <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">result</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})]</span>
</code></pre></div></td></tr></tbody></table>

PyMuPDFReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PyMuPDFReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Read PDF files using PyMuPDF library.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/pymu_pdf/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">10</span>
<span class="normal">11</span>
<span class="normal">12</span>
<span class="normal">13</span>
<span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PyMuPDFReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Read PDF files using PyMuPDF library."""</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file_path</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Path</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span>
        <span class="n">metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Loads list of documents from PDF file and also accepts extra information in dict format."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file_path</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Path</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span>
        <span class="n">metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Loads list of documents from PDF file and also accepts extra information in dict format.</span>

<span class="sd">        Args:</span>
<span class="sd">            file_path (Union[Path, str]): file path of PDF file (accepts string or Path).</span>
<span class="sd">            metadata (bool, optional): if metadata to be included or not. Defaults to True.</span>
<span class="sd">            extra_info (Optional[Dict], optional): extra information related to each document in dict format. Defaults to None.</span>

<span class="sd">        Raises:</span>
<span class="sd">            TypeError: if extra_info is not a dictionary.</span>
<span class="sd">            TypeError: if file_path is not a string or Path.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: list of documents.</span>
<span class="sd">        """</span>
        <span class="kn">import</span> <span class="nn">fitz</span>

        <span class="c1"># check if file_path is a string or Path</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="nb">str</span><span class="p">)</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="n">Path</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s2">"file_path must be a string or Path."</span><span class="p">)</span>

        <span class="c1"># open PDF file</span>
        <span class="n">doc</span> <span class="o">=</span> <span class="n">fitz</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file_path</span><span class="p">)</span>

        <span class="c1"># if extra_info is not None, check if it is a dictionary</span>
        <span class="k">if</span> <span class="n">extra_info</span><span class="p">:</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">extra_info</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
                <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s2">"extra_info must be a dictionary."</span><span class="p">)</span>

        <span class="c1"># if metadata is True, add metadata to each document</span>
        <span class="k">if</span> <span class="n">metadata</span><span class="p">:</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">extra_info</span><span class="p">:</span>
                <span class="n">extra_info</span> <span class="o">=</span> <span class="p">{}</span>
            <span class="n">extra_info</span><span class="p">[</span><span class="s2">"total_pages"</span><span class="p">]</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">doc</span><span class="p">)</span>
            <span class="n">extra_info</span><span class="p">[</span><span class="s2">"file_path"</span><span class="p">]</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">file_path</span><span class="p">)</span>

            <span class="c1"># return list of documents</span>
            <span class="k">return</span> <span class="p">[</span>
                <span class="n">Document</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">page</span><span class="o">.</span><span class="n">get_text</span><span class="p">()</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">),</span>
                    <span class="n">extra_info</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span>
                        <span class="n">extra_info</span><span class="p">,</span>
                        <span class="o">**</span><span class="p">{</span>
                            <span class="s2">"source"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">page</span><span class="o">.</span><span class="n">number</span><span class="o">+</span><span class="mi">1</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
                        <span class="p">},</span>
                    <span class="p">),</span>
                <span class="p">)</span>
                <span class="k">for</span> <span class="n">page</span> <span class="ow">in</span> <span class="n">doc</span>
            <span class="p">]</span>

        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[</span>
                <span class="n">Document</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">page</span><span class="o">.</span><span class="n">get_text</span><span class="p">()</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">),</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{}</span>
                <span class="p">)</span>
                <span class="k">for</span> <span class="n">page</span> <span class="ow">in</span> <span class="n">doc</span>
            <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PyMuPDFReader.load_data "Permanent link")

```
load_data(file_path: Union[Path, str], metadata: bool = True, extra_info: Optional[Dict] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Loads list of documents from PDF file and also accepts extra information in dict format.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/pymu_pdf/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">13</span>
<span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file_path</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Path</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span>
    <span class="n">metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Loads list of documents from PDF file and also accepts extra information in dict format."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### load [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.PyMuPDFReader.load "Permanent link")

```
load(file_path: Union[Path, str], metadata: bool = True, extra_info: Optional[Dict] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Loads list of documents from PDF file and also accepts extra information in dict format.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `file_path` | `Union[Path, str]` | 
file path of PDF file (accepts string or Path).



 | _required_ |
| `metadata` | `bool` | 

if metadata to be included or not. Defaults to True.



 | `True` |
| `extra_info` | `Optional[Dict]` | 

extra information related to each document in dict format. Defaults to None.



 | `None` |

**Raises:**

| Type | Description |
| --- | --- |
| `TypeError` | 
if extra\_info is not a dictionary.



 |
| `TypeError` | 

if file\_path is not a string or Path.



 |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: list of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/pymu_pdf/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file_path</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Path</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span>
    <span class="n">metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Loads list of documents from PDF file and also accepts extra information in dict format.</span>

<span class="sd">    Args:</span>
<span class="sd">        file_path (Union[Path, str]): file path of PDF file (accepts string or Path).</span>
<span class="sd">        metadata (bool, optional): if metadata to be included or not. Defaults to True.</span>
<span class="sd">        extra_info (Optional[Dict], optional): extra information related to each document in dict format. Defaults to None.</span>

<span class="sd">    Raises:</span>
<span class="sd">        TypeError: if extra_info is not a dictionary.</span>
<span class="sd">        TypeError: if file_path is not a string or Path.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: list of documents.</span>
<span class="sd">    """</span>
    <span class="kn">import</span> <span class="nn">fitz</span>

    <span class="c1"># check if file_path is a string or Path</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="nb">str</span><span class="p">)</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="n">Path</span><span class="p">):</span>
        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s2">"file_path must be a string or Path."</span><span class="p">)</span>

    <span class="c1"># open PDF file</span>
    <span class="n">doc</span> <span class="o">=</span> <span class="n">fitz</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file_path</span><span class="p">)</span>

    <span class="c1"># if extra_info is not None, check if it is a dictionary</span>
    <span class="k">if</span> <span class="n">extra_info</span><span class="p">:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">extra_info</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s2">"extra_info must be a dictionary."</span><span class="p">)</span>

    <span class="c1"># if metadata is True, add metadata to each document</span>
    <span class="k">if</span> <span class="n">metadata</span><span class="p">:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">extra_info</span><span class="p">:</span>
            <span class="n">extra_info</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="n">extra_info</span><span class="p">[</span><span class="s2">"total_pages"</span><span class="p">]</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">doc</span><span class="p">)</span>
        <span class="n">extra_info</span><span class="p">[</span><span class="s2">"file_path"</span><span class="p">]</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">file_path</span><span class="p">)</span>

        <span class="c1"># return list of documents</span>
        <span class="k">return</span> <span class="p">[</span>
            <span class="n">Document</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">page</span><span class="o">.</span><span class="n">get_text</span><span class="p">()</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">),</span>
                <span class="n">extra_info</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span>
                    <span class="n">extra_info</span><span class="p">,</span>
                    <span class="o">**</span><span class="p">{</span>
                        <span class="s2">"source"</span><span class="p">:</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">page</span><span class="o">.</span><span class="n">number</span><span class="o">+</span><span class="mi">1</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
                    <span class="p">},</span>
                <span class="p">),</span>
            <span class="p">)</span>
            <span class="k">for</span> <span class="n">page</span> <span class="ow">in</span> <span class="n">doc</span>
        <span class="p">]</span>

    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">[</span>
            <span class="n">Document</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">page</span><span class="o">.</span><span class="n">get_text</span><span class="p">()</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">),</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{}</span>
            <span class="p">)</span>
            <span class="k">for</span> <span class="n">page</span> <span class="ow">in</span> <span class="n">doc</span>
        <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

RTFReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.RTFReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

RTF (Rich Text Format) Reader. Reads rtf file and convert to Document.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/rtf/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 9</span>
<span class="normal">10</span>
<span class="normal">11</span>
<span class="normal">12</span>
<span class="normal">13</span>
<span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RTFReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""RTF (Rich Text Format) Reader. Reads rtf file and convert to Document."""</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">input_file</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Path</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span>
        <span class="n">extra_info</span><span class="o">=</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
        <span class="o">**</span><span class="n">load_kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from RTF file.</span>

<span class="sd">        Args:</span>
<span class="sd">            input_file (Path | str): Path for the RTF file.</span>
<span class="sd">            extra_info (Dict[str, Any]): Path for the RTF file.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: List of documents.</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">striprtf.striprtf</span> <span class="kn">import</span> <span class="n">rtf_to_text</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"striprtf is required to read RTF files."</span><span class="p">)</span>

        <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">input_file</span><span class="p">))</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">=</span> <span class="n">rtf_to_text</span><span class="p">(</span><span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="o">.</span><span class="n">strip</span><span class="p">())]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.RTFReader.load_data "Permanent link")

```
load_data(input_file: Union[Path, str], extra_info=Dict[str, Any], **load_kwargs: Any) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from RTF file.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `input_file` | `Path | str` | 
Path for the RTF file.



 | _required_ |
| `extra_info` | `Dict[str, Any]` | 

Path for the RTF file.



 | `Dict[str, Any]` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: List of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/rtf/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">12</span>
<span class="normal">13</span>
<span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">input_file</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Path</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span>
    <span class="n">extra_info</span><span class="o">=</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
    <span class="o">**</span><span class="n">load_kwargs</span><span class="p">:</span> <span class="n">Any</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from RTF file.</span>

<span class="sd">    Args:</span>
<span class="sd">        input_file (Path | str): Path for the RTF file.</span>
<span class="sd">        extra_info (Dict[str, Any]): Path for the RTF file.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: List of documents.</span>
<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">from</span> <span class="nn">striprtf.striprtf</span> <span class="kn">import</span> <span class="n">rtf_to_text</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"striprtf is required to read RTF files."</span><span class="p">)</span>

    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">input_file</span><span class="p">))</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
        <span class="n">text</span> <span class="o">=</span> <span class="n">rtf_to_text</span><span class="p">(</span><span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="o">.</span><span class="n">strip</span><span class="p">())]</span>
</code></pre></div></td></tr></tbody></table>

UnstructuredReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.UnstructuredReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

General unstructured text reader for a variety of files.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/unstructured/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 23</span>
<span class="normal"> 24</span>
<span class="normal"> 25</span>
<span class="normal"> 26</span>
<span class="normal"> 27</span>
<span class="normal"> 28</span>
<span class="normal"> 29</span>
<span class="normal"> 30</span>
<span class="normal"> 31</span>
<span class="normal"> 32</span>
<span class="normal"> 33</span>
<span class="normal"> 34</span>
<span class="normal"> 35</span>
<span class="normal"> 36</span>
<span class="normal"> 37</span>
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
<span class="normal">202</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">UnstructuredReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""General unstructured text reader for a variety of files."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">url</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">allowed_metadata_types</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Tuple</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">excluded_metadata_keys</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Set</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize UnstructuredReader.</span>

<span class="sd">        Args:</span>
<span class="sd">            *args (Any): Additional arguments passed to the BaseReader.</span>
<span class="sd">            api_key (str, optional): API key for accessing the Unstructured.io API. If provided, the reader will use the API for parsing files. Defaults to None.</span>
<span class="sd">            url (str, optional): URL for the Unstructured.io API. If not provided and an api_key is given, defaults to "http://localhost:8000". Ignored if api_key is not provided. Defaults to None.</span>
<span class="sd">            allowed_metadata_types (Optional[Tuple], optional): Tuple of types that are allowed in the metadata. Defaults to (str, int, float, type(None)).</span>
<span class="sd">            excluded_metadata_keys (Optional[Set], optional): Set of metadata keys to exclude from the final document. Defaults to {"orig_elements"}.</span>

<span class="sd">        Attributes:</span>
<span class="sd">            api_key (str or None): Stores the API key.</span>
<span class="sd">            use_api (bool): Indicates whether to use the API for parsing files, based on the presence of the api_key.</span>
<span class="sd">            url (str or None): URL for the Unstructured.io API if using the API.</span>
<span class="sd">            allowed_metadata_types (Tuple): Tuple of types that are allowed in the metadata.</span>
<span class="sd">            excluded_metadata_keys (Set): Set of metadata keys to exclude from the final document.</span>
<span class="sd">        """</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">)</span>  <span class="c1"># not passing kwargs to parent bc it cannot accept it</span>

        <span class="k">if</span> <span class="n">Element</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"Unstructured is not installed. Please install it using 'pip install -U unstructured'."</span>
            <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">api_key</span> <span class="o">=</span> <span class="n">api_key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">use_api</span> <span class="o">=</span> <span class="nb">bool</span><span class="p">(</span><span class="n">api_key</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">url</span> <span class="o">=</span> <span class="n">url</span> <span class="ow">or</span> <span class="s2">"http://localhost:8000"</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">use_api</span> <span class="k">else</span> <span class="kc">None</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">allowed_metadata_types</span> <span class="o">=</span> <span class="n">allowed_metadata_types</span> <span class="ow">or</span> <span class="p">(</span>
            <span class="nb">str</span><span class="p">,</span>
            <span class="nb">int</span><span class="p">,</span>
            <span class="nb">float</span><span class="p">,</span>
            <span class="nb">type</span><span class="p">(</span><span class="kc">None</span><span class="p">),</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">excluded_metadata_keys</span> <span class="o">=</span> <span class="n">excluded_metadata_keys</span> <span class="ow">or</span> <span class="p">{</span><span class="s2">"orig_elements"</span><span class="p">}</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_api</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">url</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Set the server url and api key."""</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">api_key</span><span class="p">,</span> <span class="n">url</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Path</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">unstructured_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">document_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">split_documents</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">excluded_metadata_keys</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data using Unstructured.io.</span>

<span class="sd">        Depending on the configuration, if url is set or use_api is True,</span>
<span class="sd">        it'll parse the file using an API call, otherwise it parses it locally.</span>
<span class="sd">        extra_info is extended by the returned metadata if split_documents is True.</span>

<span class="sd">        Args:</span>
<span class="sd">            file (Optional[Path]): Path to the file to be loaded.</span>
<span class="sd">            unstructured_kwargs (Optional[Dict]): Additional arguments for unstructured partitioning.</span>
<span class="sd">            document_kwargs (Optional[Dict]): Additional arguments for document creation.</span>
<span class="sd">            extra_info (Optional[Dict]): Extra information to add to the document metadata.</span>
<span class="sd">            split_documents (Optional[bool]): Whether to split the documents.</span>
<span class="sd">            excluded_metadata_keys (Optional[List[str]]): Keys to exclude from the metadata.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: List of parsed documents.</span>
<span class="sd">        """</span>
        <span class="n">unstructured_kwargs</span> <span class="o">=</span> <span class="n">unstructured_kwargs</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span> <span class="k">if</span> <span class="n">unstructured_kwargs</span> <span class="k">else</span> <span class="p">{}</span>

        <span class="n">elements</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Element</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_partition_elements</span><span class="p">(</span><span class="n">unstructured_kwargs</span><span class="p">,</span> <span class="n">file</span><span class="p">)</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_create_documents</span><span class="p">(</span>
            <span class="n">elements</span><span class="p">,</span>
            <span class="n">document_kwargs</span><span class="p">,</span>
            <span class="n">extra_info</span><span class="p">,</span>
            <span class="n">split_documents</span><span class="p">,</span>
            <span class="n">excluded_metadata_keys</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_partition_elements</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">unstructured_kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">file</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Path</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Element</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Partition the elements from the file or via API.</span>

<span class="sd">        Args:</span>
<span class="sd">            file (Optional[Path]): Path to the file to be loaded.</span>
<span class="sd">            unstructured_kwargs (Dict): Additional arguments for unstructured partitioning.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Element]: List of partitioned elements.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">file</span><span class="p">:</span>
            <span class="n">unstructured_kwargs</span><span class="p">[</span><span class="s2">"filename"</span><span class="p">]</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">use_api</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">unstructured.partition.api</span> <span class="kn">import</span> <span class="n">partition_via_api</span>

            <span class="k">return</span> <span class="n">partition_via_api</span><span class="p">(</span>
                <span class="n">api_key</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">api_key</span><span class="p">,</span>
                <span class="n">api_url</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">url</span> <span class="o">+</span> <span class="s2">"/general/v0/general"</span><span class="p">,</span>
                <span class="o">**</span><span class="n">unstructured_kwargs</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">unstructured.partition.auto</span> <span class="kn">import</span> <span class="n">partition</span>

            <span class="k">return</span> <span class="n">partition</span><span class="p">(</span><span class="o">**</span><span class="n">unstructured_kwargs</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_create_documents</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">elements</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Element</span><span class="p">],</span>
        <span class="n">document_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">],</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">],</span>
        <span class="n">split_documents</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">],</span>
        <span class="n">excluded_metadata_keys</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Create documents from partitioned elements.</span>

<span class="sd">        Args:</span>
<span class="sd">            elements (List): List of partitioned elements.</span>
<span class="sd">            document_kwargs (Optional[Dict]): Additional arguments for document creation.</span>
<span class="sd">            extra_info (Optional[Dict]): Extra information to add to the document metadata.</span>
<span class="sd">            split_documents (Optional[bool]): Whether to split the documents.</span>
<span class="sd">            excluded_metadata_keys (Optional[List[str]]): Keys to exclude from the metadata.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: List of parsed documents.</span>
<span class="sd">        """</span>
        <span class="n">document_kwargs</span> <span class="o">=</span> <span class="n">document_kwargs</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span> <span class="k">if</span> <span class="n">document_kwargs</span> <span class="k">else</span> <span class="p">{}</span>
        <span class="n">docs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">if</span> <span class="n">split_documents</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">sequence_number</span><span class="p">,</span> <span class="n">element</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">elements</span><span class="p">):</span>
                <span class="n">kwargs</span> <span class="o">=</span> <span class="n">document_kwargs</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
                <span class="n">kwargs</span><span class="p">[</span><span class="s2">"text"</span><span class="p">]</span> <span class="o">=</span> <span class="n">element</span><span class="o">.</span><span class="n">text</span>

                <span class="n">excluded_keys</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span>
                    <span class="n">excluded_metadata_keys</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">excluded_metadata_keys</span>
                <span class="p">)</span>
                <span class="n">metadata</span> <span class="o">=</span> <span class="n">extra_info</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span> <span class="k">if</span> <span class="n">extra_info</span> <span class="k">else</span> <span class="p">{}</span>
                <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">element</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                    <span class="k">if</span> <span class="n">key</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">excluded_keys</span><span class="p">:</span>
                        <span class="n">metadata</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span>
                            <span class="n">value</span>
                            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">allowed_metadata_types</span><span class="p">)</span>
                            <span class="k">else</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
                        <span class="p">)</span>

                <span class="n">kwargs</span><span class="p">[</span><span class="s2">"extra_info"</span><span class="p">]</span> <span class="o">=</span> <span class="n">metadata</span>
                <span class="n">kwargs</span><span class="p">[</span><span class="s2">"doc_id"</span><span class="p">]</span> <span class="o">=</span> <span class="n">element</span><span class="o">.</span><span class="n">id_to_hash</span><span class="p">(</span><span class="n">sequence_number</span><span class="p">)</span>

                <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">text_chunks</span> <span class="o">=</span> <span class="p">[</span><span class="s2">" "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">el</span><span class="p">)</span><span class="o">.</span><span class="n">split</span><span class="p">())</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">elements</span><span class="p">]</span>
            <span class="n">text</span> <span class="o">=</span> <span class="s2">"</span><span class="se">\n\n</span><span class="s2">"</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">text_chunks</span><span class="p">)</span>

            <span class="n">kwargs</span> <span class="o">=</span> <span class="n">document_kwargs</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
            <span class="n">kwargs</span><span class="p">[</span><span class="s2">"text"</span><span class="p">]</span> <span class="o">=</span> <span class="n">text</span>

            <span class="n">metadata</span> <span class="o">=</span> <span class="n">extra_info</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span> <span class="k">if</span> <span class="n">extra_info</span> <span class="k">else</span> <span class="p">{}</span>

            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">elements</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
                <span class="n">filename</span> <span class="o">=</span> <span class="n">elements</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">filename</span>
                <span class="n">elements</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">id</span>
                <span class="n">metadata</span><span class="p">[</span><span class="s2">"filename"</span><span class="p">]</span> <span class="o">=</span> <span class="n">filename</span>
                <span class="n">kwargs</span><span class="p">[</span><span class="s2">"doc_id"</span><span class="p">]</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">filename</span><span class="si">}</span><span class="s2">"</span>

            <span class="n">kwargs</span><span class="p">[</span><span class="s2">"extra_info"</span><span class="p">]</span> <span class="o">=</span> <span class="n">metadata</span>

            <span class="n">docs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">docs</span>
</code></pre></div></td></tr></tbody></table>

### from\_api `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.UnstructuredReader.from_api "Permanent link")

```
from_api(api_key: str, url: str = None)
```

Set the server url and api key.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/unstructured/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_api</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">url</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Set the server url and api key."""</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">api_key</span><span class="p">,</span> <span class="n">url</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.UnstructuredReader.load_data "Permanent link")

```
load_data(file: Optional[Path] = None, unstructured_kwargs: Optional[Dict] = None, document_kwargs: Optional[Dict] = None, extra_info: Optional[Dict] = None, split_documents: Optional[bool] = False, excluded_metadata_keys: Optional[List[str]] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data using Unstructured.io.

Depending on the configuration, if url is set or use\_api is True, it'll parse the file using an API call, otherwise it parses it locally. extra\_info is extended by the returned metadata if split\_documents is True.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `file` | `Optional[Path]` | 
Path to the file to be loaded.



 | `None` |
| `unstructured_kwargs` | `Optional[Dict]` | 

Additional arguments for unstructured partitioning.



 | `None` |
| `document_kwargs` | `Optional[Dict]` | 

Additional arguments for document creation.



 | `None` |
| `extra_info` | `Optional[Dict]` | 

Extra information to add to the document metadata.



 | `None` |
| `split_documents` | `Optional[bool]` | 

Whether to split the documents.



 | `False` |
| `excluded_metadata_keys` | `Optional[List[str]]` | 

Keys to exclude from the metadata.



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: List of parsed documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/unstructured/base.py`

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
<span class="normal">109</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Path</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">unstructured_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">document_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">split_documents</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">excluded_metadata_keys</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data using Unstructured.io.</span>

<span class="sd">    Depending on the configuration, if url is set or use_api is True,</span>
<span class="sd">    it'll parse the file using an API call, otherwise it parses it locally.</span>
<span class="sd">    extra_info is extended by the returned metadata if split_documents is True.</span>

<span class="sd">    Args:</span>
<span class="sd">        file (Optional[Path]): Path to the file to be loaded.</span>
<span class="sd">        unstructured_kwargs (Optional[Dict]): Additional arguments for unstructured partitioning.</span>
<span class="sd">        document_kwargs (Optional[Dict]): Additional arguments for document creation.</span>
<span class="sd">        extra_info (Optional[Dict]): Extra information to add to the document metadata.</span>
<span class="sd">        split_documents (Optional[bool]): Whether to split the documents.</span>
<span class="sd">        excluded_metadata_keys (Optional[List[str]]): Keys to exclude from the metadata.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: List of parsed documents.</span>
<span class="sd">    """</span>
    <span class="n">unstructured_kwargs</span> <span class="o">=</span> <span class="n">unstructured_kwargs</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span> <span class="k">if</span> <span class="n">unstructured_kwargs</span> <span class="k">else</span> <span class="p">{}</span>

    <span class="n">elements</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Element</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_partition_elements</span><span class="p">(</span><span class="n">unstructured_kwargs</span><span class="p">,</span> <span class="n">file</span><span class="p">)</span>

    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_create_documents</span><span class="p">(</span>
        <span class="n">elements</span><span class="p">,</span>
        <span class="n">document_kwargs</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">,</span>
        <span class="n">split_documents</span><span class="p">,</span>
        <span class="n">excluded_metadata_keys</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

VideoAudioReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.VideoAudioReader "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

Video audio parser.

Extract text from transcript of video/audio files.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/video_audio/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">VideoAudioReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Video audio parser.</span>

<span class="sd">    Extract text from transcript of video/audio files.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">model_version</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"base"</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init parser."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_model_version</span> <span class="o">=</span> <span class="n">model_version</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">whisper</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"Please install OpenAI whisper model "</span>
                <span class="s2">"'pip install git+https://github.com/openai/whisper.git' "</span>
                <span class="s2">"to use the model"</span>
            <span class="p">)</span>

        <span class="n">model</span> <span class="o">=</span> <span class="n">whisper</span><span class="o">.</span><span class="n">load_model</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_model_version</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">parser_config</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"model"</span><span class="p">:</span> <span class="n">model</span><span class="p">}</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse file."""</span>
        <span class="kn">import</span> <span class="nn">whisper</span>

        <span class="k">if</span> <span class="n">file</span><span class="o">.</span><span class="n">name</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s2">"mp4"</span><span class="p">):</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="kn">from</span> <span class="nn">pydub</span> <span class="kn">import</span> <span class="n">AudioSegment</span>
            <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"Please install pydub 'pip install pydub' "</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
                <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="s2">"rb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                    <span class="n">video</span> <span class="o">=</span> <span class="n">AudioSegment</span><span class="o">.</span><span class="n">from_file</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="nb">format</span><span class="o">=</span><span class="s2">"mp4"</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="c1"># open file</span>
                <span class="n">video</span> <span class="o">=</span> <span class="n">AudioSegment</span><span class="o">.</span><span class="n">from_file</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="nb">format</span><span class="o">=</span><span class="s2">"mp4"</span><span class="p">)</span>

            <span class="c1"># Extract audio from video</span>
            <span class="n">audio</span> <span class="o">=</span> <span class="n">video</span><span class="o">.</span><span class="n">split_to_mono</span><span class="p">()[</span><span class="mi">0</span><span class="p">]</span>

            <span class="n">file_str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">file</span><span class="p">)[:</span><span class="o">-</span><span class="mi">4</span><span class="p">]</span> <span class="o">+</span> <span class="s2">".mp3"</span>
            <span class="c1"># export file</span>
            <span class="n">audio</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="n">file_str</span><span class="p">,</span> <span class="nb">format</span><span class="o">=</span><span class="s2">"mp3"</span><span class="p">)</span>

        <span class="n">model</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">whisper</span><span class="o">.</span><span class="n">Whisper</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">parser_config</span><span class="p">[</span><span class="s2">"model"</span><span class="p">])</span>
        <span class="n">result</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">transcribe</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">file</span><span class="p">))</span>

        <span class="n">transcript</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="s2">"text"</span><span class="p">]</span>

        <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">transcript</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})]</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.VideoAudioReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None, fs: Optional[AbstractFileSystem] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Parse file.

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/video_audio/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Parse file."""</span>
    <span class="kn">import</span> <span class="nn">whisper</span>

    <span class="k">if</span> <span class="n">file</span><span class="o">.</span><span class="n">name</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s2">"mp4"</span><span class="p">):</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">pydub</span> <span class="kn">import</span> <span class="n">AudioSegment</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s2">"Please install pydub 'pip install pydub' "</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">fs</span><span class="p">:</span>
            <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="s2">"rb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
                <span class="n">video</span> <span class="o">=</span> <span class="n">AudioSegment</span><span class="o">.</span><span class="n">from_file</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="nb">format</span><span class="o">=</span><span class="s2">"mp4"</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># open file</span>
            <span class="n">video</span> <span class="o">=</span> <span class="n">AudioSegment</span><span class="o">.</span><span class="n">from_file</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="nb">format</span><span class="o">=</span><span class="s2">"mp4"</span><span class="p">)</span>

        <span class="c1"># Extract audio from video</span>
        <span class="n">audio</span> <span class="o">=</span> <span class="n">video</span><span class="o">.</span><span class="n">split_to_mono</span><span class="p">()[</span><span class="mi">0</span><span class="p">]</span>

        <span class="n">file_str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">file</span><span class="p">)[:</span><span class="o">-</span><span class="mi">4</span><span class="p">]</span> <span class="o">+</span> <span class="s2">".mp3"</span>
        <span class="c1"># export file</span>
        <span class="n">audio</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="n">file_str</span><span class="p">,</span> <span class="nb">format</span><span class="o">=</span><span class="s2">"mp3"</span><span class="p">)</span>

    <span class="n">model</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">whisper</span><span class="o">.</span><span class="n">Whisper</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">parser_config</span><span class="p">[</span><span class="s2">"model"</span><span class="p">])</span>
    <span class="n">result</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">transcribe</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">file</span><span class="p">))</span>

    <span class="n">transcript</span> <span class="o">=</span> <span class="n">result</span><span class="p">[</span><span class="s2">"text"</span><span class="p">]</span>

    <span class="k">return</span> <span class="p">[</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">transcript</span><span class="p">,</span> <span class="n">metadata</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{})]</span>
</code></pre></div></td></tr></tbody></table>

XMLReader [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.XMLReader "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseReader](https://docs.llamaindex.ai/en/stable/api_reference/readers/#llama_index.core.readers.base.BaseReader "llama_index.core.readers.base.BaseReader")`

XML reader.

Reads XML documents with options to help suss out relationships between nodes.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `tree_level_split` | `int` | 
From which level in the xml tree we split documents,



 | `0` |

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/xml/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">XMLReader</span><span class="p">(</span><span class="n">BaseReader</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""XML reader.</span>

<span class="sd">    Reads XML documents with options to help suss out relationships between nodes.</span>

<span class="sd">    Args:</span>
<span class="sd">        tree_level_split (int): From which level in the xml tree we split documents,</span>
<span class="sd">        the default level is the root which is level 0</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tree_level_split</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize with arguments."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">tree_level_split</span> <span class="o">=</span> <span class="n">tree_level_split</span>

    <span class="k">def</span> <span class="nf">_parse_xmlelt_to_document</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">root</span><span class="p">:</span> <span class="n">ET</span><span class="o">.</span><span class="n">Element</span><span class="p">,</span> <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Parse the xml object into a list of Documents.</span>

<span class="sd">        Args:</span>
<span class="sd">            root: The XML Element to be converted.</span>
<span class="sd">            extra_info (Optional[Dict]): Additional information. Default is None.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Document: The documents.</span>
<span class="sd">        """</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="n">_get_leaf_nodes_up_to_level</span><span class="p">(</span><span class="n">root</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">tree_level_split</span><span class="p">)</span>
        <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">content</span> <span class="o">=</span> <span class="n">ET</span><span class="o">.</span><span class="n">tostring</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">"utf8"</span><span class="p">)</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s2">"utf-8"</span><span class="p">)</span>
            <span class="n">content</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="sa">r</span><span class="s2">"^&lt;\?xml.*"</span><span class="p">,</span> <span class="s2">""</span><span class="p">,</span> <span class="n">content</span><span class="p">)</span>
            <span class="n">content</span> <span class="o">=</span> <span class="n">content</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
            <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Document</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">content</span><span class="p">,</span> <span class="n">extra_info</span><span class="o">=</span><span class="n">extra_info</span> <span class="ow">or</span> <span class="p">{}))</span>

        <span class="k">return</span> <span class="n">documents</span>

    <span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
        <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Load data from the input file.</span>

<span class="sd">        Args:</span>
<span class="sd">            file (Path): Path to the input file.</span>
<span class="sd">            extra_info (Optional[Dict]): Additional information. Default is None.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Document]: List of documents.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">Path</span><span class="p">):</span>
            <span class="n">file</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>

        <span class="n">tree</span> <span class="o">=</span> <span class="n">ET</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_xmlelt_to_document</span><span class="p">(</span><span class="n">tree</span><span class="o">.</span><span class="n">getroot</span><span class="p">(),</span> <span class="n">extra_info</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### load\_data [#](https://docs.llamaindex.ai/en/stable/api_reference/readers/file/#llama_index.readers.file.XMLReader.load_data "Permanent link")

```
load_data(file: Path, extra_info: Optional[Dict] = None) -> List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]
```

Load data from the input file.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `file` | `Path` | 
Path to the input file.



 | _required_ |
| `extra_info` | `Optional[Dict]` | 

Additional information. Default is None.



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[[Document](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.Document "llama_index.core.schema.Document")]` | 
List\[Document\]: List of documents.



 |

Source code in `llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/xml/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">load_data</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">file</span><span class="p">:</span> <span class="n">Path</span><span class="p">,</span>
    <span class="n">extra_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Load data from the input file.</span>

<span class="sd">    Args:</span>
<span class="sd">        file (Path): Path to the input file.</span>
<span class="sd">        extra_info (Optional[Dict]): Additional information. Default is None.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Document]: List of documents.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">Path</span><span class="p">):</span>
        <span class="n">file</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>

    <span class="n">tree</span> <span class="o">=</span> <span class="n">ET</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parse_xmlelt_to_document</span><span class="p">(</span><span class="n">tree</span><span class="o">.</span><span class="n">getroot</span><span class="p">(),</span> <span class="n">extra_info</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Feishu wiki](https://docs.llamaindex.ai/en/stable/api_reference/readers/feishu_wiki/)[Next Firebase realtimedb](https://docs.llamaindex.ai/en/stable/api_reference/readers/firebase_realtimedb/)
