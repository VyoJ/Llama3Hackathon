Title: Google PaLM Embeddings - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/embeddings/google_palm/

Markdown Content:
Google PaLM Embeddings - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-embeddings\-google

%pip install llama-index-embeddings-google

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

\# imports
from llama\_index.embeddings.google import GooglePaLMEmbedding

\# imports from llama\_index.embeddings.google import GooglePaLMEmbedding

In \[ \]:

Copied!

\# get API key and create embeddings

model\_name \= "models/embedding-gecko-001"
api\_key \= "YOUR API KEY"

embed\_model \= GooglePaLMEmbedding(model\_name\=model\_name, api\_key\=api\_key)

embeddings \= embed\_model.get\_text\_embedding("Google PaLM Embeddings.")

\# get API key and create embeddings model\_name = "models/embedding-gecko-001" api\_key = "YOUR API KEY" embed\_model = GooglePaLMEmbedding(model\_name=model\_name, api\_key=api\_key) embeddings = embed\_model.get\_text\_embedding("Google PaLM Embeddings.")

/opt/homebrew/lib/python3.11/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user\_install.html
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

\[0.028517298, -0.0028859433, -0.035110522, 0.021982985, -0.0039763353\]

Back to top

[Previous Google Gemini Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/gemini/)[Next Gradient Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/gradient/)
