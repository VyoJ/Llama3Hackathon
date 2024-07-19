Title: Local Embeddings with OpenVINO - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/embeddings/openvino/

Markdown Content:
Local Embeddings with OpenVINO - LlamaIndex


[OpenVINO™](https://github.com/openvinotoolkit/openvino) is an open-source toolkit for optimizing and deploying AI inference. The OpenVINO™ Runtime supports various hardware [devices](https://github.com/openvinotoolkit/openvino?tab=readme-ov-file#supported-hardware-matrix) including x86 and ARM CPUs, and Intel GPUs. It can help to boost deep learning performance in Computer Vision, Automatic Speech Recognition, Natural Language Processing and other common tasks.

Hugging Face embedding model can be supported by OpenVINO through `OpenVINOEmbedding` class.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-embeddings\-openvino

%pip install llama-index-embeddings-openvino

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

Model Exporter[¶](https://docs.llamaindex.ai/en/stable/examples/embeddings/openvino/#model-exporter)
----------------------------------------------------------------------------------------------------

It is possible to export your model to the OpenVINO IR format with `create_and_save_openvino_model` function, and load the model from local folder.

In \[ \]:

Copied!

from llama\_index.embeddings.huggingface\_openvino import OpenVINOEmbedding

OpenVINOEmbedding.create\_and\_save\_openvino\_model(
    "BAAI/bge-small-en-v1.5", "./bge\_ov"
)

from llama\_index.embeddings.huggingface\_openvino import OpenVINOEmbedding OpenVINOEmbedding.create\_and\_save\_openvino\_model( "BAAI/bge-small-en-v1.5", "./bge\_ov" )

Model Loading[¶](https://docs.llamaindex.ai/en/stable/examples/embeddings/openvino/#model-loading)
--------------------------------------------------------------------------------------------------

If you have an Intel GPU, you can specify `device="gpu"` to run inference on it.

In \[ \]:

Copied!

ov\_embed\_model \= OpenVINOEmbedding(folder\_name\="./bge\_ov", device\="cpu")

ov\_embed\_model = OpenVINOEmbedding(folder\_name="./bge\_ov", device="cpu")

In \[ \]:

Copied!

embeddings \= ov\_embed\_model.get\_text\_embedding("Hello World!")
print(len(embeddings))
print(embeddings\[:5\])

embeddings = ov\_embed\_model.get\_text\_embedding("Hello World!") print(len(embeddings)) print(embeddings\[:5\])

For more information refer to:

*   [OpenVINO LLM guide](https://docs.openvino.ai/2024/learn-openvino/llm_inference_guide.html).
    
*   [OpenVINO Documentation](https://docs.openvino.ai/2024/home.html).
    
*   [OpenVINO Get Started Guide](https://www.intel.com/content/www/us/en/content-details/819067/openvino-get-started-guide.html).
    
*   [RAG example with LlamaIndex](https://github.com/openvinotoolkit/openvino_notebooks/tree/latest/notebooks/llm-rag-llamaindex).
    

Back to top

[Previous Ollama Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/ollama_embedding/)[Next Optimized Embedding Model using Optimum-Intel](https://docs.llamaindex.ai/en/stable/examples/embeddings/optimum_intel/)
