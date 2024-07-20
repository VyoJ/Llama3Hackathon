Title: Google Gemini Embeddings - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/embeddings/gemini/

Markdown Content:
Google Gemini Embeddings - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-embeddings\-gemini

%pip install llama-index-embeddings-gemini

In \[ \]:

Copied!

!pip install llama\-index 'google-generativeai>=0.3.0' matplotlib

!pip install llama-index 'google-generativeai>=0.3.0' matplotlib

In \[ \]:

Copied!

import os

GOOGLE\_API\_KEY \= ""  \# add your GOOGLE API key here
os.environ\["GOOGLE\_API\_KEY"\] \= GOOGLE\_API\_KEY

import os GOOGLE\_API\_KEY = "" # add your GOOGLE API key here os.environ\["GOOGLE\_API\_KEY"\] = GOOGLE\_API\_KEY

In \[ \]:

Copied!

\# imports
from llama\_index.embeddings.gemini import GeminiEmbedding

\# imports from llama\_index.embeddings.gemini import GeminiEmbedding

In \[ \]:

Copied!

\# get API key and create embeddings

model\_name \= "models/embedding-001"

embed\_model \= GeminiEmbedding(
    model\_name\=model\_name, api\_key\=GOOGLE\_API\_KEY, title\="this is a document"
)

embeddings \= embed\_model.get\_text\_embedding("Google Gemini Embeddings.")

\# get API key and create embeddings model\_name = "models/embedding-001" embed\_model = GeminiEmbedding( model\_name=model\_name, api\_key=GOOGLE\_API\_KEY, title="this is a document" ) embeddings = embed\_model.get\_text\_embedding("Google Gemini Embeddings.")

/Users/haotianzhang/llama\_index/venv/lib/python3.11/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user\_install.html
  from .autonotebook import tqdm as notebook\_tqdm

In \[ \]:

Copied!

print(f"Dimension of embeddings: {len(embeddings)}")

print(f"Dimension of embeddings: {len(embeddings)}")

Dimension of embeddings: 768

In \[ \]:

Copied!

embeddings\[:5\]

embeddings\[:5\]

Out\[ \]:

\[0.028174246, -0.0290093, -0.013280814, 0.008629, 0.025442218\]

In \[ \]:

Copied!

embeddings \= embed\_model.get\_query\_embedding("Google Gemini Embeddings.")
embeddings\[:5\]

embeddings = embed\_model.get\_query\_embedding("Google Gemini Embeddings.") embeddings\[:5\]

Out\[ \]:

\[0.028174246, -0.0290093, -0.013280814, 0.008629, 0.025442218\]

In \[ \]:

Copied!

embeddings \= embed\_model.get\_text\_embedding(
    \["Google Gemini Embeddings.", "Google is awesome."\]
)

embeddings = embed\_model.get\_text\_embedding( \["Google Gemini Embeddings.", "Google is awesome."\] )

In \[ \]:

Copied!

print(f"Dimension of embeddings: {len(embeddings)}")
print(embeddings\[0\]\[:5\])
print(embeddings\[1\]\[:5\])

print(f"Dimension of embeddings: {len(embeddings)}") print(embeddings\[0\]\[:5\]) print(embeddings\[1\]\[:5\])

Dimension of embeddings: 2
\[0.028174246, -0.0290093, -0.013280814, 0.008629, 0.025442218\]
\[0.009427786, -0.009968997, -0.03341217, -0.025396815, 0.03210592\]

In \[ \]:

Copied!

embedding \= await embed\_model.aget\_text\_embedding("Google Gemini Embeddings.")
print(embedding\[:5\])

embedding = await embed\_model.aget\_text\_embedding("Google Gemini Embeddings.") print(embedding\[:5\])

\[0.028174246, -0.0290093, -0.013280814, 0.008629, 0.025442218\]

In \[ \]:

Copied!

embeddings \= await embed\_model.aget\_text\_embedding\_batch(
    \[
        "Google Gemini Embeddings.",
        "Google is awesome.",
        "Llamaindex is awesome.",
    \]
)
print(embeddings\[0\]\[:5\])
print(embeddings\[1\]\[:5\])
print(embeddings\[2\]\[:5\])

embeddings = await embed\_model.aget\_text\_embedding\_batch( \[ "Google Gemini Embeddings.", "Google is awesome.", "Llamaindex is awesome.", \] ) print(embeddings\[0\]\[:5\]) print(embeddings\[1\]\[:5\]) print(embeddings\[2\]\[:5\])

\[0.028174246, -0.0290093, -0.013280814, 0.008629, 0.025442218\]
\[0.009427786, -0.009968997, -0.03341217, -0.025396815, 0.03210592\]
\[0.013159992, -0.021570021, -0.060150445, -0.042500723, 0.041159637\]

In \[ \]:

Copied!

embedding \= await embed\_model.aget\_query\_embedding("Google Gemini Embeddings.")
print(embedding\[:5\])

embedding = await embed\_model.aget\_query\_embedding("Google Gemini Embeddings.") print(embedding\[:5\])

\[0.028174246, -0.0290093, -0.013280814, 0.008629, 0.025442218\]

Back to top

[Previous Fireworks Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/fireworks/)[Next Google PaLM Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/google_palm/)
