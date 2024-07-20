Title: Ollama Embeddings - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/embeddings/ollama_embedding/

Markdown Content:
Ollama Embeddings - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-embeddings\-ollama

%pip install llama-index-embeddings-ollama

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

from llama\_index.embeddings.ollama import OllamaEmbedding

ollama\_embedding \= OllamaEmbedding(
    model\_name\="llama2",
    base\_url\="http://localhost:11434",
    ollama\_additional\_kwargs\={"mirostat": 0},
)

pass\_embedding \= ollama\_embedding.get\_text\_embedding\_batch(
    \["This is a passage!", "This is another passage"\], show\_progress\=True
)
print(pass\_embedding)

query\_embedding \= ollama\_embedding.get\_query\_embedding("Where is blue?")
print(query\_embedding)

from llama\_index.embeddings.ollama import OllamaEmbedding ollama\_embedding = OllamaEmbedding( model\_name="llama2", base\_url="http://localhost:11434", ollama\_additional\_kwargs={"mirostat": 0}, ) pass\_embedding = ollama\_embedding.get\_text\_embedding\_batch( \["This is a passage!", "This is another passage"\], show\_progress=True ) print(pass\_embedding) query\_embedding = ollama\_embedding.get\_query\_embedding("Where is blue?") print(query\_embedding)

Back to top

[Previous OctoAI Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/octoai/)[Next Local Embeddings with OpenVINO](https://docs.llamaindex.ai/en/stable/examples/embeddings/openvino/)
