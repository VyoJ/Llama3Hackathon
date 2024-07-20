Title: MistralAI Embeddings - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/embeddings/mistralai/

Markdown Content:
MistralAI Embeddings - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-embeddings\-mistralai

%pip install llama-index-embeddings-mistralai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

\# imports
from llama\_index.embeddings.mistralai import MistralAIEmbedding

\# imports from llama\_index.embeddings.mistralai import MistralAIEmbedding

In \[ \]:

Copied!

\# get API key and create embeddings
api\_key \= "YOUR API KEY"
model\_name \= "mistral-embed"
embed\_model \= MistralAIEmbedding(model\_name\=model\_name, api\_key\=api\_key)

embeddings \= embed\_model.get\_text\_embedding("La Plateforme - The Platform")

\# get API key and create embeddings api\_key = "YOUR API KEY" model\_name = "mistral-embed" embed\_model = MistralAIEmbedding(model\_name=model\_name, api\_key=api\_key) embeddings = embed\_model.get\_text\_embedding("La Plateforme - The Platform")

In \[ \]:

Copied!

print(f"Dimension of embeddings: {len(embeddings)}")

print(f"Dimension of embeddings: {len(embeddings)}")

Dimension of embeddings: 1024

In \[ \]:

Copied!

embeddings\[:5\]

embeddings\[:5\]

Out\[ \]:

\[-0.0299224853515625,
 -0.0028362274169921875,
 0.0282745361328125,
 -0.034759521484375,
 -0.0017366409301757812\]

Back to top

[Previous LLMRails Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/llm_rails/)[Next Mixedbread AI Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/mixedbreadai/)
