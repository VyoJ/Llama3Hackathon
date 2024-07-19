Title: OpenAI Embeddings - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/embeddings/OpenAI/

Markdown Content:
OpenAI Embeddings - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-embeddings\-openai

%pip install llama-index-embeddings-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..."

In \[ \]:

Copied!

from llama\_index.embeddings.openai import OpenAIEmbedding
from llama\_index.core import Settings

embed\_model \= OpenAIEmbedding(embed\_batch\_size\=10)
Settings.embed\_model \= embed\_model

from llama\_index.embeddings.openai import OpenAIEmbedding from llama\_index.core import Settings embed\_model = OpenAIEmbedding(embed\_batch\_size=10) Settings.embed\_model = embed\_model

Using OpenAI `text-embedding-3-large` and `text-embedding-3-small`[¶](https://docs.llamaindex.ai/en/stable/examples/embeddings/OpenAI/#using-openai-text-embedding-3-large-and-text-embedding-3-small)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Note, you may have to update your openai client: `pip install -U openai`

In \[ \]:

Copied!

\# get API key and create embeddings
from llama\_index.embeddings.openai import OpenAIEmbedding

embed\_model \= OpenAIEmbedding(model\="text-embedding-3-large")

embeddings \= embed\_model.get\_text\_embedding(
    "Open AI new Embeddings models is great."
)

\# get API key and create embeddings from llama\_index.embeddings.openai import OpenAIEmbedding embed\_model = OpenAIEmbedding(model="text-embedding-3-large") embeddings = embed\_model.get\_text\_embedding( "Open AI new Embeddings models is great." )

In \[ \]:

Copied!

print(embeddings\[:5\])

print(embeddings\[:5\])

\[-0.011500772088766098, 0.02457442320883274, -0.01760469563305378, -0.017763426527380943, 0.029841400682926178\]

In \[ \]:

Copied!

print(len(embeddings))

print(len(embeddings))

3072

In \[ \]:

Copied!

\# get API key and create embeddings
from llama\_index.embeddings.openai import OpenAIEmbedding

embed\_model \= OpenAIEmbedding(
    model\="text-embedding-3-small",
)

embeddings \= embed\_model.get\_text\_embedding(
    "Open AI new Embeddings models is awesome."
)

\# get API key and create embeddings from llama\_index.embeddings.openai import OpenAIEmbedding embed\_model = OpenAIEmbedding( model="text-embedding-3-small", ) embeddings = embed\_model.get\_text\_embedding( "Open AI new Embeddings models is awesome." )

In \[ \]:

Copied!

print(len(embeddings))

print(len(embeddings))

1536

Change the dimension of output embeddings[¶](https://docs.llamaindex.ai/en/stable/examples/embeddings/OpenAI/#change-the-dimension-of-output-embeddings)
--------------------------------------------------------------------------------------------------------------------------------------------------------

Note: Make sure you have the latest OpenAI client

In \[ \]:

Copied!

\# get API key and create embeddings
from llama\_index.embeddings.openai import OpenAIEmbedding

embed\_model \= OpenAIEmbedding(
    model\="text-embedding-3-large",
    dimensions\=512,
)

embeddings \= embed\_model.get\_text\_embedding(
    "Open AI new Embeddings models with different dimensions is awesome."
)
print(len(embeddings))

\# get API key and create embeddings from llama\_index.embeddings.openai import OpenAIEmbedding embed\_model = OpenAIEmbedding( model="text-embedding-3-large", dimensions=512, ) embeddings = embed\_model.get\_text\_embedding( "Open AI new Embeddings models with different dimensions is awesome." ) print(len(embeddings))

512

Back to top

[Previous LangChain Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/Langchain/)[Next Aleph Alpha Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/alephalpha/)
