Title: OpenVINO Rerank - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/openvino_rerank/

Markdown Content:
OpenVINO Rerank - LlamaIndex


[OpenVINO™](https://github.com/openvinotoolkit/openvino) is an open-source toolkit for optimizing and deploying AI inference. The OpenVINO™ Runtime supports various hardware [devices](https://github.com/openvinotoolkit/openvino?tab=readme-ov-file#supported-hardware-matrix) including x86 and ARM CPUs, and Intel GPUs. It can help to boost deep learning performance in Computer Vision, Automatic Speech Recognition, Natural Language Processing and other common tasks.

Hugging Face rerank model can be supported by OpenVINO through `OpenVINORerank` class.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-postprocessor\-openvino\-rerank
%pip install llama\-index\-embeddings\-openvino

%pip install llama-index-postprocessor-openvino-rerank %pip install llama-index-embeddings-openvino

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/openvino_rerank/#download-data)
-----------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

\# build index
index \= VectorStoreIndex.from\_documents(documents\=documents)

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader # load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data() # build index index = VectorStoreIndex.from\_documents(documents=documents)

Download Embedding, Rerank models and LLM[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/openvino_rerank/#download-embedding-rerank-models-and-llm)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.embeddings.huggingface\_openvino import OpenVINOEmbedding

OpenVINOEmbedding.create\_and\_save\_openvino\_model(
    "BAAI/bge-small-en-v1.5", "./embedding\_ov"
)

from llama\_index.embeddings.huggingface\_openvino import OpenVINOEmbedding OpenVINOEmbedding.create\_and\_save\_openvino\_model( "BAAI/bge-small-en-v1.5", "./embedding\_ov" )

In \[ \]:

Copied!

from llama\_index.postprocessor.openvino\_rerank import OpenVINORerank

OpenVINORerank.create\_and\_save\_openvino\_model(
    "BAAI/bge-reranker-large", "./rerank\_ov"
)

from llama\_index.postprocessor.openvino\_rerank import OpenVINORerank OpenVINORerank.create\_and\_save\_openvino\_model( "BAAI/bge-reranker-large", "./rerank\_ov" )

In \[ \]:

Copied!

!optimum\-cli export openvino \--model HuggingFaceH4/zephyr\-7b\-beta \--weight\-format int4 llm\_ov

!optimum-cli export openvino --model HuggingFaceH4/zephyr-7b-beta --weight-format int4 llm\_ov

Retrieve top 10 most relevant nodes, then filter with OpenVINO Rerank[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/openvino_rerank/#retrieve-top-10-most-relevant-nodes-then-filter-with-openvino-rerank)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.postprocessor.openvino\_rerank import OpenVINORerank
from llama\_index.llms.openvino import OpenVINOLLM
from llama\_index.core import Settings

Settings.embed\_model \= OpenVINOEmbedding(folder\_name\="./embedding\_ov")
Settings.llm \= OpenVINOLLM(model\_name\="./llm\_ov", tokenizer\_name\="./llm\_ov")

ov\_rerank \= OpenVINORerank(model\="./rerank\_ov", device\="cpu", top\_n\=2)

from llama\_index.postprocessor.openvino\_rerank import OpenVINORerank from llama\_index.llms.openvino import OpenVINOLLM from llama\_index.core import Settings Settings.embed\_model = OpenVINOEmbedding(folder\_name="./embedding\_ov") Settings.llm = OpenVINOLLM(model\_name="./llm\_ov", tokenizer\_name="./llm\_ov") ov\_rerank = OpenVINORerank(model="./rerank\_ov", device="cpu", top\_n=2)

In \[ \]:

Copied!

index \= VectorStoreIndex.from\_documents(documents\=documents)

index = VectorStoreIndex.from\_documents(documents=documents)

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(
    similarity\_top\_k\=10,
    node\_postprocessors\=\[ov\_rerank\],
)
response \= query\_engine.query(
    "What did Sam Altman do in this essay?",
)

query\_engine = index.as\_query\_engine( similarity\_top\_k=10, node\_postprocessors=\[ov\_rerank\], ) response = query\_engine.query( "What did Sam Altman do in this essay?", )

In \[ \]:

Copied!

print(response)

print(response)

Sam Altman was asked by the author, Paul Graham, to become the president of Y Combinator (YC), a startup accelerator. Initially, Sam declined the offer as he wanted to start a startup to make nuclear reactors. However, the author continued to persuade him, and in October 2013, Sam agreed to take over YC starting with the winter 2014 batch. The author then stepped back from running YC and focused on other activities, including painting and writing essays.

In \[ \]:

Copied!

print(response.get\_formatted\_sources(length\=200))

print(response.get\_formatted\_sources(length=200))

\> Source (Doc id: ae4297fa-670c-403c-a355-6fffe7e16835): Why not organize a summer program where they'd start startups instead? We wouldn't feel guilty for being in a sense fake investors, because they would in a similar sense be fake founders. So while ...

> Source (Doc id: c55eddb9-33f8-46bb-82a1-cb7fa0c7f5b6): This seemed strange advice, because YC was doing great. But if there was one thing rarer than Rtm offering advice, it was Rtm being wrong. So this set me thinking. It was true that on my current tr...

### Directly retrieve top 2 most similar nodes[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/openvino_rerank/#directly-retrieve-top-2-most-similar-nodes)

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(
    similarity\_top\_k\=2,
)
response \= query\_engine.query(
    "What did Sam Altman do in this essay?",
)

query\_engine = index.as\_query\_engine( similarity\_top\_k=2, ) response = query\_engine.query( "What did Sam Altman do in this essay?", )

Retrieved context is irrelevant and response is hallucinated.

In \[ \]:

Copied!

print(response)

print(response)

Sam Altman is mentioned in the essay as the person who was asked to become the president of Y Combinator. He initially declined the offer but later agreed to take over starting with the winter 2014 batch. The author also mentions that they left running Y Combinator more and more to Sam, partly so he could learn the job, and partly because they were focused on their mother, who had cancer and passed away in January 2014.

In \[ \]:

Copied!

print(response.get\_formatted\_sources(length\=200))

print(response.get\_formatted\_sources(length=200))

\> Source (Doc id: c55eddb9-33f8-46bb-82a1-cb7fa0c7f5b6): This seemed strange advice, because YC was doing great. But if there was one thing rarer than Rtm offering advice, it was Rtm being wrong. So this set me thinking. It was true that on my current tr...

> Source (Doc id: 6b2c335f-1390-4e92-9171-3ba5d24b3826): I knew that online essays would be a marginal medium at first. Socially they'd seem more like rants posted by nutjobs on their GeoCities sites than the genteel and beautifully typeset compositions ...

For more information refer to:

*   [OpenVINO LLM guide](https://docs.openvino.ai/2024/learn-openvino/llm_inference_guide.html).
    
*   [OpenVINO Documentation](https://docs.openvino.ai/2024/home.html).
    
*   [OpenVINO Get Started Guide](https://www.intel.com/content/www/us/en/content-details/819067/openvino-get-started-guide.html).
    
*   [RAG example with LlamaIndex](https://github.com/openvinotoolkit/openvino_notebooks/tree/latest/notebooks/llm-rag-llamaindex).
    

Back to top

[Previous VoyageAI Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/VoyageAIRerank/)[Next RankGPT Reranker Demonstration (Van Gogh Wiki)](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/rankGPT/)

Hi, how can I help you?

🦙
