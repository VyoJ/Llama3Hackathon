Title: LangChain Embeddings - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/embeddings/Langchain/

Markdown Content:
LangChain Embeddings - LlamaIndex


This guide shows you how to use embedding models from [LangChain](https://python.langchain.com/docs/integrations/text_embedding/).

[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jerryjliu/llama_index/blob/main/docs/docs/examples/embeddings/Langchain.ipynb)

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-embeddings\-langchain

%pip install llama-index-embeddings-langchain

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

from langchain.embeddings import HuggingFaceEmbeddings
from llama\_index.embeddings.langchain import LangchainEmbedding

lc\_embed\_model \= HuggingFaceEmbeddings(
    model\_name\="sentence-transformers/all-mpnet-base-v2"
)
embed\_model \= LangchainEmbedding(lc\_embed\_model)

from langchain.embeddings import HuggingFaceEmbeddings from llama\_index.embeddings.langchain import LangchainEmbedding lc\_embed\_model = HuggingFaceEmbeddings( model\_name="sentence-transformers/all-mpnet-base-v2" ) embed\_model = LangchainEmbedding(lc\_embed\_model)

In \[ \]:

Copied!

\# Basic embedding example
embeddings \= embed\_model.get\_text\_embedding(
    "It is raining cats and dogs here!"
)
print(len(embeddings), embeddings\[:10\])

\# Basic embedding example embeddings = embed\_model.get\_text\_embedding( "It is raining cats and dogs here!" ) print(len(embeddings), embeddings\[:10\])

768 \[-0.005906202830374241, 0.04911914840340614, -0.04757878929376602, -0.04320324584841728, 0.02837090566754341, -0.017371710389852524, -0.04422023147344589, -0.019035547971725464, 0.04941621795296669, -0.03839121758937836\]

Back to top

[Previous Anyscale Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/Anyscale/)[Next OpenAI Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/OpenAI/)
