Title: Anyscale Embeddings - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/embeddings/Anyscale/

Markdown Content:
Anyscale Embeddings - LlamaIndex


This guide shows you how to use Anyscale Embeddings through [Anyscale Endpoints](https://docs.endpoints.anyscale.com/).

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-embeddings\-anyscale

%pip install llama-index-embeddings-anyscale

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

from llama\_index.embeddings.anyscale import AnyscaleEmbedding

embed\_model \= AnyscaleEmbedding(
    api\_key\=ANYSCALE\_ENDPOINT\_TOKEN, embed\_batch\_size\=10
)

from llama\_index.embeddings.anyscale import AnyscaleEmbedding embed\_model = AnyscaleEmbedding( api\_key=ANYSCALE\_ENDPOINT\_TOKEN, embed\_batch\_size=10 )

In \[ \]:

Copied!

\# Basic embedding example
embeddings \= embed\_model.get\_text\_embedding(
    "It is raining cats and dogs here!"
)
print(len(embeddings), embeddings\[:10\])

\# Basic embedding example embeddings = embed\_model.get\_text\_embedding( "It is raining cats and dogs here!" ) print(len(embeddings), embeddings\[:10\])

Back to top

[Previous Redis Docstore+Index Store Demo](https://docs.llamaindex.ai/en/stable/examples/docstore/RedisDocstoreIndexStoreDemo/)[Next LangChain Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/Langchain/)
