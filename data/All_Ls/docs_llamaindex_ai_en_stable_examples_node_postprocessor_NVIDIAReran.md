Title: NVIDIA NIMs - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/NVIDIARerank/

Markdown Content:
NVIDIA NIMs - LlamaIndex


The llama-index-postprocessor-nvidia-rerank\` package contains LlamaIndex integrations building applications with models on NVIDIA NIM inference microservice. NIM supports models across domains like chat, embedding, and re-ranking models from the community as well as NVIDIA. These models are optimized by NVIDIA to deliver the best performance on NVIDIA accelerated infrastructure and deployed as a NIM, an easy-to-use, prebuilt containers that deploy anywhere using a single command on NVIDIA accelerated infrastructure.

NVIDIA hosted deployments of NIMs are available to test on the [NVIDIA API catalog](https://build.nvidia.com/). After testing, NIMs can be exported from NVIDIA’s API catalog using the NVIDIA AI Enterprise license and run on-premises or in the cloud, giving enterprises ownership and full control of their IP and AI application.

NIMs are packaged as container images on a per model basis and are distributed as NGC container images through the NVIDIA NGC Catalog. At their core, NIMs provide easy, consistent, and familiar APIs for running inference on an AI model.

NVIDIA's Rerank connector[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/NVIDIARerank/#nvidias-rerank-connector)


Reranking is a critical piece of high accuracy, efficient retrieval pipelines.

Two important use cases:

*   Combining results from multiple data sources
*   Enhancing accuracy for single data sources

Combining results from multiple sources[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/NVIDIARerank/#combining-results-from-multiple-sources)
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Consider a pipeline with data from a semantic store, such as VectorStoreIndex, as well as a BM25 store.

Each store is queried independently and returns results that the individual store considers to be highly relevant. Figuring out the overall relevance of the results is where reranking comes into play.

Follow along with the [Advanced - Hybrid Retriever + Re-Ranking](https://docs.llamaindex.ai/en/stable/examples/retrievers/bm25_retriever/#advanced-hybrid-retriever-re-ranking) use case, substitute [the reranker](https://docs.llamaindex.ai/en/stable/examples/retrievers/bm25_retriever/#re-ranker-setup) with -

Installation[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/NVIDIARerank/#installation)
------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

%pip install \--upgrade \--quiet llama\-index\-postprocessor\-nvidia\-rerank

%pip install --upgrade --quiet llama-index-postprocessor-nvidia-rerank

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/NVIDIARerank/#setup)
----------------------------------------------------------------------------------------------

**To get started:**

1.  Create a free account with [NVIDIA](https://build.nvidia.com/), which hosts NVIDIA AI Foundation models.
    
2.  Click on your model of choice.
    
3.  Under Input select the Python tab, and click `Get API Key`. Then click `Generate Key`.
    
4.  Copy and save the generated key as NVIDIA\_API\_KEY. From there, you should have access to the endpoints.
    

In \[ \]:

Copied!

import getpass
import os

\# del os.environ\['NVIDIA\_API\_KEY'\]  ## delete key and reset
if os.environ.get("NVIDIA\_API\_KEY", "").startswith("nvapi-"):
    print("Valid NVIDIA\_API\_KEY already in environment. Delete to reset")
else:
    nvapi\_key \= getpass.getpass("NVAPI Key (starts with nvapi-): ")
    assert nvapi\_key.startswith(
        "nvapi-"
    ), f"{nvapi\_key\[:5\]}... is not a valid key"
    os.environ\["NVIDIA\_API\_KEY"\] \= nvapi\_key

import getpass import os # del os.environ\['NVIDIA\_API\_KEY'\] ## delete key and reset if os.environ.get("NVIDIA\_API\_KEY", "").startswith("nvapi-"): print("Valid NVIDIA\_API\_KEY already in environment. Delete to reset") else: nvapi\_key = getpass.getpass("NVAPI Key (starts with nvapi-): ") assert nvapi\_key.startswith( "nvapi-" ), f"{nvapi\_key\[:5\]}... is not a valid key" os.environ\["NVIDIA\_API\_KEY"\] = nvapi\_key

Working with API Catalog[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/NVIDIARerank/#working-with-api-catalog)
------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.postprocessor.nvidia\_rerank import NVIDIARerank

reranker \= NVIDIARerank(top\_n\=4)

from llama\_index.postprocessor.nvidia\_rerank import NVIDIARerank reranker = NVIDIARerank(top\_n=4)

Working with NVIDIA NIMs[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/NVIDIARerank/#working-with-nvidia-nims)
------------------------------------------------------------------------------------------------------------------------------------

In addition to connecting to hosted [NVIDIA NIMs](https://ai.nvidia.com/), this connector can be used to connect to local microservice instances. This helps you take your applications local when necessary.

For instructions on how to setup local microservice instances, see [https://developer.nvidia.com/blog/nvidia-nim-offers-optimized-inference-microservices-for-deploying-ai-models-at-scale/](https://developer.nvidia.com/blog/nvidia-nim-offers-optimized-inference-microservices-for-deploying-ai-models-at-scale/)

In \[ \]:

Copied!

from llama\_index.llms.nvidia import NVIDIA

\# connect to a rerank NIM running at localhost:1976
reranker \= NVIDIARerank(base\_url\="http://localhost:1976/v1")

from llama\_index.llms.nvidia import NVIDIA # connect to a rerank NIM running at localhost:1976 reranker = NVIDIARerank(base\_url="http://localhost:1976/v1")

Back to top

[Previous Mixedbread AI Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/MixedbreadAIRerank/)[Next Sentence Embedding OptimizerThis postprocessor optimizes token usage by removing sentences that are not relevant to the query (this is done using embeddings).The percentile cutoff is a measure for using the top percentage of relevant sentences. The threshold cutoff can be specified instead, which uses a raw similarity cutoff for picking which sentences to keep.](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/OptimizerDemo/)

Hi, how can I help you?

🦙
