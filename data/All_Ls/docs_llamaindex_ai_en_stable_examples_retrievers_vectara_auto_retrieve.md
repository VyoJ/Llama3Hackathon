Title: Auto-Retrieval from a Vectara Index

URL Source: https://docs.llamaindex.ai/en/stable/examples/retrievers/vectara_auto_retriever/

Markdown Content:
Auto-Retrieval from a Vectara Index - LlamaIndex


This guide shows how to perform **auto-retrieval** in LlamaIndex with Vectara.

With Auto-retrieval we interpret a retrieval query before submitting it to Vectara to identify potential rewrites of the query as a shorter query along with some metadata filtering.

For example, a query like "what is the revenue in 2022" might be rewritten as "what is the revenue" along with a filter of "doc.year = 2022". Let's see how this works via an example.

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/vectara_auto_retriever/#setup)
------------------------------------------------------------------------------------------------

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

!pip install llama\_index llama\-index\-llms\-openai llama\-index\-indices\-managed\-vectara

!pip install llama\_index llama-index-llms-openai llama-index-indices-managed-vectara

Requirement already satisfied: llama\_index in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (0.10.37)
Requirement already satisfied: llama-index-llms-openai in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (0.1.19)
Requirement already satisfied: llama-index-indices-managed-vectara in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (0.1.3)
Requirement already satisfied: llama-index-agent-openai<0.3.0,>=0.1.4 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama\_index) (0.1.5)
Requirement already satisfied: llama-index-cli<0.2.0,>=0.1.2 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama\_index) (0.1.7)
Requirement already satisfied: llama-index-core<0.11.0,>=0.10.35 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama\_index) (0.10.37)
Requirement already satisfied: llama-index-embeddings-openai<0.2.0,>=0.1.5 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama\_index) (0.1.6)
Requirement already satisfied: llama-index-indices-managed-llama-cloud<0.2.0,>=0.1.2 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama\_index) (0.1.3)
Requirement already satisfied: llama-index-legacy<0.10.0,>=0.9.48 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama\_index) (0.9.48)
Requirement already satisfied: llama-index-multi-modal-llms-openai<0.2.0,>=0.1.3 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama\_index) (0.1.4)
Requirement already satisfied: llama-index-program-openai<0.2.0,>=0.1.3 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama\_index) (0.1.4)
Requirement already satisfied: llama-index-question-gen-openai<0.2.0,>=0.1.2 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama\_index) (0.1.3)
Requirement already satisfied: llama-index-readers-file<0.2.0,>=0.1.4 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama\_index) (0.1.6)
Requirement already satisfied: llama-index-readers-llama-parse<0.2.0,>=0.1.2 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama\_index) (0.1.3)
Requirement already satisfied: llama-index-vector-stores-chroma<0.2.0,>=0.1.1 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-cli<0.2.0,>=0.1.2->llama\_index) (0.1.5)
Requirement already satisfied: PyYAML>=6.0.1 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.35->llama\_index) (6.0.1)
Requirement already satisfied: SQLAlchemy>=1.4.49 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from SQLAlchemy\[asyncio\]>=1.4.49->llama-index-core<0.11.0,>=0.10.35->llama\_index) (2.0.14)
Requirement already satisfied: aiohttp<4.0.0,>=3.8.6 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.35->llama\_index) (3.9.5)
Requirement already satisfied: dataclasses-json in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.35->llama\_index) (0.6.5)
Requirement already satisfied: deprecated>=1.2.9.3 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.35->llama\_index) (1.2.14)
Requirement already satisfied: dirtyjson<2.0.0,>=1.0.8 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.35->llama\_index) (1.0.8)
Requirement already satisfied: fsspec>=2023.5.0 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.35->llama\_index) (2024.3.1)
Requirement already satisfied: httpx in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.35->llama\_index) (0.27.0)
Requirement already satisfied: jsonpath-ng<2.0.0,>=1.6.0 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.35->llama\_index) (1.6.1)
Requirement already satisfied: llamaindex-py-client<0.2.0,>=0.1.18 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.35->llama\_index) (0.1.18)
Requirement already satisfied: nest-asyncio<2.0.0,>=1.5.8 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.35->llama\_index) (1.6.0)
Requirement already satisfied: networkx>=3.0 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.35->llama\_index) (3.2.1)
Requirement already satisfied: nltk<4.0.0,>=3.8.1 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.35->llama\_index) (3.8.1)
Requirement already satisfied: numpy in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.35->llama\_index) (1.26.4)
Requirement already satisfied: openai>=1.1.0 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.35->llama\_index) (1.30.1)
Requirement already satisfied: pandas in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.35->llama\_index) (2.2.2)
Requirement already satisfied: pillow>=9.0.0 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.35->llama\_index) (10.3.0)
Requirement already satisfied: requests>=2.31.0 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.35->llama\_index) (2.31.0)
Requirement already satisfied: spacy<4.0.0,>=3.7.1 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.35->llama\_index) (3.7.4)
Requirement already satisfied: tenacity<9.0.0,>=8.2.0 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.35->llama\_index) (8.2.3)
Requirement already satisfied: tiktoken>=0.3.3 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.35->llama\_index) (0.6.0)
Requirement already satisfied: tqdm<5.0.0,>=4.66.1 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.35->llama\_index) (4.66.4)
Requirement already satisfied: typing-extensions>=4.5.0 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.35->llama\_index) (4.11.0)
Requirement already satisfied: typing-inspect>=0.8.0 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.35->llama\_index) (0.9.0)
Requirement already satisfied: wrapt in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.35->llama\_index) (1.16.0)
Requirement already satisfied: beautifulsoup4<5.0.0,>=4.12.3 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-readers-file<0.2.0,>=0.1.4->llama\_index) (4.12.3)
Requirement already satisfied: bs4<0.0.3,>=0.0.2 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-readers-file<0.2.0,>=0.1.4->llama\_index) (0.0.2)
Requirement already satisfied: pymupdf<2.0.0,>=1.23.21 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-readers-file<0.2.0,>=0.1.4->llama\_index) (1.23.26)
Requirement already satisfied: pypdf<5.0.0,>=4.0.1 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-readers-file<0.2.0,>=0.1.4->llama\_index) (4.2.0)
Requirement already satisfied: llama-parse<0.4.0,>=0.3.3 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-readers-llama-parse<0.2.0,>=0.1.2->llama\_index) (0.3.5)
Requirement already satisfied: aiosignal>=1.1.2 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.6->llama-index-core<0.11.0,>=0.10.35->llama\_index) (1.3.1)
Requirement already satisfied: attrs>=17.3.0 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.6->llama-index-core<0.11.0,>=0.10.35->llama\_index) (23.2.0)
Requirement already satisfied: frozenlist>=1.1.1 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.6->llama-index-core<0.11.0,>=0.10.35->llama\_index) (1.4.1)
Requirement already satisfied: multidict<7.0,>=4.5 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.6->llama-index-core<0.11.0,>=0.10.35->llama\_index) (6.0.5)
Requirement already satisfied: yarl<2.0,>=1.0 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.6->llama-index-core<0.11.0,>=0.10.35->llama\_index) (1.9.4)
Requirement already satisfied: soupsieve>1.2 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from beautifulsoup4<5.0.0,>=4.12.3->llama-index-readers-file<0.2.0,>=0.1.4->llama\_index) (2.5)
Requirement already satisfied: ply in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from jsonpath-ng<2.0.0,>=1.6.0->llama-index-core<0.11.0,>=0.10.35->llama\_index) (3.11)
Requirement already satisfied: chromadb<0.5.0,>=0.4.22 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (0.4.24)
Requirement already satisfied: onnxruntime<2.0.0,>=1.17.0 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (1.18.0)
Requirement already satisfied: tokenizers<0.16.0,>=0.15.1 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (0.15.2)
Requirement already satisfied: pydantic>=1.10 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from llamaindex-py-client<0.2.0,>=0.1.18->llama-index-core<0.11.0,>=0.10.35->llama\_index) (2.7.1)
Requirement already satisfied: anyio in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from httpx->llama-index-core<0.11.0,>=0.10.35->llama\_index) (4.3.0)
Requirement already satisfied: certifi in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from httpx->llama-index-core<0.11.0,>=0.10.35->llama\_index) (2024.2.2)
Requirement already satisfied: httpcore1.\*->httpx->llama-index-core<0.11.0,>=0.10.35->llama\_index) (0.14.0)
Requirement already satisfied: click in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from nltk<4.0.0,>=3.8.1->llama-index-core<0.11.0,>=0.10.35->llama\_index) (8.1.7)
Requirement already satisfied: joblib in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from nltk<4.0.0,>=3.8.1->llama-index-core<0.11.0,>=0.10.35->llama\_index) (1.4.2)
Requirement already satisfied: regex>=2021.8.3 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from nltk<4.0.0,>=3.8.1->llama-index-core<0.11.0,>=0.10.35->llama\_index) (2024.4.28)
Requirement already satisfied: distro<2,>=1.7.0 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from openai>=1.1.0->llama-index-core<0.11.0,>=0.10.35->llama\_index) (1.9.0)
Requirement already satisfied: PyMuPDFb0.7.3 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (0.7.3)
Requirement already satisfied: fastapi>=0.95.2 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (0.110.0)
Requirement already satisfied: uvicorn>=0.18.3 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from uvicorn\[standard\]>=0.18.3->chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (0.27.1)
Requirement already satisfied: posthog>=2.4.0 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (3.5.0)
Requirement already satisfied: pulsar-client>=3.1.0 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (3.4.0)
Requirement already satisfied: opentelemetry-api>=1.2.0 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (1.21.0)
Requirement already satisfied: opentelemetry-exporter-otlp-proto-grpc>=1.2.0 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (1.21.0)
Requirement already satisfied: opentelemetry-instrumentation-fastapi>=0.41b0 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (0.42b0)
Requirement already satisfied: opentelemetry-sdk>=1.2.0 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (1.21.0)
Requirement already satisfied: pypika>=0.48.9 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (0.48.9)
Requirement already satisfied: overrides>=7.3.1 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (7.7.0)
Requirement already satisfied: importlib-resources in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (6.1.2)
Requirement already satisfied: grpcio>=1.58.0 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (1.63.0)
Requirement already satisfied: bcrypt>=4.0.1 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (4.1.2)
Requirement already satisfied: kubernetes>=28.1.0 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (29.0.0)
Requirement already satisfied: mmh3>=4.0.1 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (4.1.0)
Requirement already satisfied: orjson>=3.9.12 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (3.9.15)
Requirement already satisfied: language-data>=1.2 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from langcodes<4.0.0,>=3.2.0->spacy<4.0.0,>=3.7.1->llama-index-core<0.11.0,>=0.10.35->llama\_index) (1.2.0)
Requirement already satisfied: coloredlogs in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from onnxruntime<2.0.0,>=1.17.0->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (15.0.1)
Requirement already satisfied: flatbuffers in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from onnxruntime<2.0.0,>=1.17.0->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (24.3.25)
Requirement already satisfied: protobuf in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from onnxruntime<2.0.0,>=1.17.0->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (4.25.3)
Requirement already satisfied: sympy in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from onnxruntime<2.0.0,>=1.17.0->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (1.12)
Requirement already satisfied: annotated-types>=0.4.0 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from pydantic>=1.10->llamaindex-py-client<0.2.0,>=0.1.18->llama-index-core<0.11.0,>=0.10.35->llama\_index) (0.6.0)
Requirement already satisfied: pydantic-core1.21.0 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (1.21.0)
Requirement already satisfied: opentelemetry-proto0.42b0 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from opentelemetry-instrumentation-fastapi>=0.41b0->chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (0.42b0)
Requirement already satisfied: opentelemetry-instrumentation0.42b0 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from opentelemetry-instrumentation-fastapi>=0.41b0->chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (0.42b0)
Requirement already satisfied: opentelemetry-util-http0.42b0->opentelemetry-instrumentation-fastapi>=0.41b0->chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (3.7.2)
Requirement already satisfied: monotonic>=1.5 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from posthog>=2.4.0->chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (1.6)
Requirement already satisfied: httptools>=0.5.0 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from uvicorn\[standard\]>=0.18.3->chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (0.6.1)
Requirement already satisfied: python-dotenv>=0.13 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from uvicorn\[standard\]>=0.18.3->chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (1.0.0)
Requirement already satisfied: uvloop!=0.15.0,!=0.15.1,>=0.14.0 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from uvicorn\[standard\]>=0.18.3->chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (0.19.0)
Requirement already satisfied: watchfiles>=0.13 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from uvicorn\[standard\]>=0.18.3->chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (0.21.0)
Requirement already satisfied: websockets>=10.4 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from uvicorn\[standard\]>=0.18.3->chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (12.0)
Requirement already satisfied: humanfriendly>=9.1 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from coloredlogs->onnxruntime<2.0.0,>=1.17.0->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (10.0)
Requirement already satisfied: mpmath>=0.19 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from sympy->onnxruntime<2.0.0,>=1.17.0->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (1.3.0)
Requirement already satisfied: cachetools<6.0,>=2.0.0 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from google-auth>=1.0.1->kubernetes>=28.1.0->chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (5.3.3)
Requirement already satisfied: pyasn1-modules>=0.2.1 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from google-auth>=1.0.1->kubernetes>=28.1.0->chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (0.4.0)
Requirement already satisfied: rsa<5,>=3.1.4 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from google-auth>=1.0.1->kubernetes>=28.1.0->chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (4.9)
Requirement already satisfied: zipp>=0.5 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from importlib-metadata<7.0,>=6.0->opentelemetry-api>=1.2.0->chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (3.18.1)
Requirement already satisfied: pyasn1<0.7.0,>=0.4.6 in /Users/ofer/miniconda3/envs/langchain/lib/python3.11/site-packages (from pyasn1-modules>=0.2.1->google-auth>=1.0.1->kubernetes>=28.1.0->chromadb<0.5.0,>=0.4.22->llama-index-vector-stores-chroma<0.2.0,>=0.1.1->llama-index-cli<0.2.0,>=0.1.2->llama\_index) (0.6.0)

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

In \[ \]:

Copied!

from llama\_index.core.schema import TextNode
from llama\_index.core.indices.managed.types import ManagedIndexQueryMode
from llama\_index.indices.managed.vectara import VectaraIndex
from llama\_index.indices.managed.vectara import VectaraAutoRetriever

from llama\_index.core.vector\_stores import MetadataInfo, VectorStoreInfo

from llama\_index.llms.openai import OpenAI

from llama\_index.core.schema import TextNode from llama\_index.core.indices.managed.types import ManagedIndexQueryMode from llama\_index.indices.managed.vectara import VectaraIndex from llama\_index.indices.managed.vectara import VectaraAutoRetriever from llama\_index.core.vector\_stores import MetadataInfo, VectorStoreInfo from llama\_index.llms.openai import OpenAI

Defining Some Sample Data[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/vectara_auto_retriever/#defining-some-sample-data)
----------------------------------------------------------------------------------------------------------------------------------------

We first define a dataset of movies:

1.  Each node describes a movie.
2.  The `text` describes the movie, whereas `metadata` defines certain metadata fields like year, director, rating or genre.

In Vectara you will need to [define](https://docs.vectara.com/docs/learn/metadata-search-filtering/filter-overview) these metadata fields in your coprus as filterable attributes so that filtering can occur with them.

In \[ \]:

Copied!

nodes \= \[
    TextNode(
        text\=(
            "A pragmatic paleontologist touring an almost complete theme park on an island "
            + "in Central America is tasked with protecting a couple of kids after a power "
            + "failure causes the park's cloned dinosaurs to run loose."
        ),
        metadata\={"year": 1993, "rating": 7.7, "genre": "science fiction"},
    ),
    TextNode(
        text\=(
            "A thief who steals corporate secrets through the use of dream-sharing technology "
            + "is given the inverse task of planting an idea into the mind of a C.E.O., "
            + "but his tragic past may doom the project and his team to disaster."
        ),
        metadata\={
            "year": 2010,
            "director": "Christopher Nolan",
            "rating": 8.2,
        },
    ),
    TextNode(
        text\="Barbie suffers a crisis that leads her to question her world and her existence.",
        metadata\={
            "year": 2023,
            "director": "Greta Gerwig",
            "genre": "fantasy",
            "rating": 9.5,
        },
    ),
    TextNode(
        text\=(
            "A cowboy doll is profoundly threatened and jealous when a new spaceman action "
            + "figure supplants him as top toy in a boy's bedroom."
        ),
        metadata\={"year": 1995, "genre": "animated", "rating": 8.3},
    ),
    TextNode(
        text\=(
            "When Woody is stolen by a toy collector, Buzz and his friends set out on a "
            + "rescue mission to save Woody before he becomes a museum toy property with his "
            + "roundup gang Jessie, Prospector, and Bullseye. "
        ),
        metadata\={"year": 1999, "genre": "animated", "rating": 7.9},
    ),
    TextNode(
        text\=(
            "The toys are mistakenly delivered to a day-care center instead of the attic "
            + "right before Andy leaves for college, and it's up to Woody to convince the "
            + "other toys that they weren't abandoned and to return home."
        ),
        metadata\={"year": 2010, "genre": "animated", "rating": 8.3},
    ),
\]

nodes = \[ TextNode( text=( "A pragmatic paleontologist touring an almost complete theme park on an island " + "in Central America is tasked with protecting a couple of kids after a power " + "failure causes the park's cloned dinosaurs to run loose." ), metadata={"year": 1993, "rating": 7.7, "genre": "science fiction"}, ), TextNode( text=( "A thief who steals corporate secrets through the use of dream-sharing technology " + "is given the inverse task of planting an idea into the mind of a C.E.O., " + "but his tragic past may doom the project and his team to disaster." ), metadata={ "year": 2010, "director": "Christopher Nolan", "rating": 8.2, }, ), TextNode( text="Barbie suffers a crisis that leads her to question her world and her existence.", metadata={ "year": 2023, "director": "Greta Gerwig", "genre": "fantasy", "rating": 9.5, }, ), TextNode( text=( "A cowboy doll is profoundly threatened and jealous when a new spaceman action " + "figure supplants him as top toy in a boy's bedroom." ), metadata={"year": 1995, "genre": "animated", "rating": 8.3}, ), TextNode( text=( "When Woody is stolen by a toy collector, Buzz and his friends set out on a " + "rescue mission to save Woody before he becomes a museum toy property with his " + "roundup gang Jessie, Prospector, and Bullseye. " ), metadata={"year": 1999, "genre": "animated", "rating": 7.9}, ), TextNode( text=( "The toys are mistakenly delivered to a day-care center instead of the attic " + "right before Andy leaves for college, and it's up to Woody to convince the " + "other toys that they weren't abandoned and to return home." ), metadata={"year": 2010, "genre": "animated", "rating": 8.3}, ), \]

Then we load our sample data into our Vectara Index.

In \[ \]:

Copied!

import os

os.environ\["VECTARA\_API\_KEY"\] \= "<YOUR\_VECTARA\_API\_KEY>"
os.environ\["VECTARA\_CORPUS\_ID"\] \= "<YOUR\_VECTARA\_CORPUS\_ID>"
os.environ\["VECTARA\_CUSTOMER\_ID"\] \= "<YOUR\_VECTARA\_CUSTOMER\_ID>"

index \= VectaraIndex(nodes\=nodes)

import os os.environ\["VECTARA\_API\_KEY"\] = "" os.environ\["VECTARA\_CORPUS\_ID"\] = "" os.environ\["VECTARA\_CUSTOMER\_ID"\] = "" index = VectaraIndex(nodes=nodes)

Defining the `VectorStoreInfo`[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/vectara_auto_retriever/#defining-the-vectorstoreinfo)
------------------------------------------------------------------------------------------------------------------------------------------------

We define a `VectorStoreInfo` object, which contains a structured description of the metadata filters suported by our Vectara Index. This information is later on usedin the auto-retrieval prompt, enabling the LLM to infer the metadata filters to use for a specific query.

In \[ \]:

Copied!

vector\_store\_info \= VectorStoreInfo(
    content\_info\="information about a movie",
    metadata\_info\=\[
        MetadataInfo(
            name\="genre",
            description\="""
                The genre of the movie. 
                One of \['science fiction', 'fantasy', 'comedy', 'drama', 'thriller', 'romance', 'action', 'animated'\]
            """,
            type\="string",
        ),
        MetadataInfo(
            name\="year",
            description\="The year the movie was released",
            type\="integer",
        ),
        MetadataInfo(
            name\="director",
            description\="The name of the movie director",
            type\="string",
        ),
        MetadataInfo(
            name\="rating",
            description\="A 1-10 rating for the movie",
            type\="float",
        ),
    \],
)

vector\_store\_info = VectorStoreInfo( content\_info="information about a movie", metadata\_info=\[ MetadataInfo( name="genre", description=""" The genre of the movie. One of \['science fiction', 'fantasy', 'comedy', 'drama', 'thriller', 'romance', 'action', 'animated'\] """, type="string", ), MetadataInfo( name="year", description="The year the movie was released", type="integer", ), MetadataInfo( name="director", description="The name of the movie director", type="string", ), MetadataInfo( name="rating", description="A 1-10 rating for the movie", type="float", ), \], )

Running auto-retrieval[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/vectara_auto_retriever/#running-auto-retrieval)
----------------------------------------------------------------------------------------------------------------------------------

Now let's create a `VectaraAutoRetriever` instance and try `retrieve()`:

In \[ \]:

Copied!

from llama\_index.indices.managed.vectara import VectaraAutoRetriever
from llama\_index.llms.openai import OpenAI

llm \= OpenAI(model\="gpt-3.5-turbo", temperature\=0)

retriever \= VectaraAutoRetriever(
    index,
    vector\_store\_info\=vector\_store\_info,
    llm\=llm,
    verbose\=True,
)

from llama\_index.indices.managed.vectara import VectaraAutoRetriever from llama\_index.llms.openai import OpenAI llm = OpenAI(model="gpt-3.5-turbo", temperature=0) retriever = VectaraAutoRetriever( index, vector\_store\_info=vector\_store\_info, llm=llm, verbose=True, )

In \[ \]:

Copied!

retriever.retrieve("movie directed by Greta Gerwig")

retriever.retrieve("movie directed by Greta Gerwig")

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
Using query str: movie directed by Greta Gerwig
Using implicit filters: \[('director', ' 'Greta Gerwig')

Out\[ \]:

\[NodeWithScore(node=TextNode(id\_='935c2319f66122e1c4189ccf32164b362d4b6bc2af4ede77fc47fd126546ba8d', embedding=None, metadata={'lang': 'eng', 'offset': '0', 'len': '79', 'year': '2023', 'director': 'Greta Gerwig', 'genre': 'fantasy', 'rating': '9.5'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='Barbie suffers a crisis that leads her to question her world and her existence.', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.61976165)\]

In \[ \]:

Copied!

retriever.retrieve("a movie with a rating above 8")

retriever.retrieve("a movie with a rating above 8")

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
Using query str: movie with rating above 8
Using implicit filters: \[('rating', '>', 8)\]
final filter string: (doc.rating > '8')

Out\[ \]:

\[NodeWithScore(node=TextNode(id\_='a55396c48ddb51e593676d37a18efa8da1cbab6fd206c9029ced924e386c12b5', embedding=None, metadata={'lang': 'eng', 'offset': '0', 'len': '129', 'year': '1995', 'genre': 'animated', 'rating': '8.3'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text="A cowboy doll is profoundly threatened and jealous when a new spaceman action figure supplants him as top toy in a boy's bedroom.", start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.5414715),
 NodeWithScore(node=TextNode(id\_='b1e87de59678f3f1831327948a716f6e5a217c9b8cee4c08d5555d337825fca8', embedding=None, metadata={'lang': 'eng', 'offset': '0', 'len': '220', 'year': '2010', 'director': 'Christopher Nolan', 'rating': '8.2'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O., but his tragic past may doom the project and his team to disaster.', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.50233454),
 NodeWithScore(node=TextNode(id\_='935c2319f66122e1c4189ccf32164b362d4b6bc2af4ede77fc47fd126546ba8d', embedding=None, metadata={'lang': 'eng', 'offset': '0', 'len': '79', 'year': '2023', 'director': 'Greta Gerwig', 'genre': 'fantasy', 'rating': '9.5'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='Barbie suffers a crisis that leads her to question her world and her existence.', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.500028),
 NodeWithScore(node=TextNode(id\_='a860d7045527b4659a1a1171f922e30bee754ddcf83e0ec8423238f9f634f118', embedding=None, metadata={'lang': 'eng', 'offset': '0', 'len': '209', 'year': '2010', 'genre': 'animated', 'rating': '8.3'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text="The toys are mistakenly delivered to a day-care center instead of the attic right before Andy leaves for college, and it's up to Woody to convince the other toys that they weren't abandoned and to return home.", start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.47051564)\]

We can also include standard `VectaraRetriever` arguments in the `VectaraAutoRetriever`. For example, if we want to include a `filter` that would be added to any additional filtering from the query itself, we can do it as follows:

Back to top

[Previous Simple Fusion Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/simple_fusion/)[Next VideoDB Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/videodb_retriever/)
