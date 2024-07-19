Title: Jina Embeddings - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/embeddings/jinaai_embeddings/

Markdown Content:
Jina Embeddings - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-embeddings\-jinaai
%pip install llama\-index\-llms\-openai

%pip install llama-index-embeddings-jinaai %pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

You may also need other packages that do not come direcly with llama-index

In \[ \]:

Copied!

!pip install Pillow

!pip install Pillow

For this example, you will need an API key which you can get from [https://jina.ai/embeddings/](https://jina.ai/embeddings/)

In \[ \]:

Copied!

\# Initilise with your api key
import os

jinaai\_api\_key \= "YOUR\_JINAAI\_API\_KEY"
os.environ\["JINAAI\_API\_KEY"\] \= jinaai\_api\_key

\# Initilise with your api key import os jinaai\_api\_key = "YOUR\_JINAAI\_API\_KEY" os.environ\["JINAAI\_API\_KEY"\] = jinaai\_api\_key

Embed text and queries with Jina embedding models through JinaAI API[¶](https://docs.llamaindex.ai/en/stable/examples/embeddings/jinaai_embeddings/#embed-text-and-queries-with-jina-embedding-models-through-jinaai-api)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can encode your text and your queries using the JinaEmbedding class

In \[ \]:

Copied!

from llama\_index.embeddings.jinaai import JinaEmbedding

embed\_model \= JinaEmbedding(
    api\_key\=jinaai\_api\_key,
    model\="jina-embeddings-v2-base-en",
)

embeddings \= embed\_model.get\_text\_embedding("This is the text to embed")
print("Text dim:", len(embeddings))
print("Text embed:", embeddings\[:5\])

embeddings \= embed\_model.get\_query\_embedding("This is the query to embed")
print("Query dim:", len(embeddings))
print("Query embed:", embeddings\[:5\])

from llama\_index.embeddings.jinaai import JinaEmbedding embed\_model = JinaEmbedding( api\_key=jinaai\_api\_key, model="jina-embeddings-v2-base-en", ) embeddings = embed\_model.get\_text\_embedding("This is the text to embed") print("Text dim:", len(embeddings)) print("Text embed:", embeddings\[:5\]) embeddings = embed\_model.get\_query\_embedding("This is the query to embed") print("Query dim:", len(embeddings)) print("Query embed:", embeddings\[:5\])

Embed images and queries with Jina CLIP through JinaAI API[¶](https://docs.llamaindex.ai/en/stable/examples/embeddings/jinaai_embeddings/#embed-images-and-queries-with-jina-clip-through-jinaai-api)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can also encode your images and your queries using the JinaEmbedding class

In \[ \]:

Copied!

from llama\_index.embeddings.jinaai import JinaEmbedding
from PIL import Image
import requests
from numpy import dot
from numpy.linalg import norm

embed\_model \= JinaEmbedding(
    api\_key\=jinaai\_api\_key,
    model\="jina-clip-v1",
)

image\_url \= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStMP8S3VbNCqOQd7QQQcbvC\_FLa1HlftCiJw&s"
im \= Image.open(requests.get(image\_url, stream\=True).raw)
print("Image:")
display(im)

image\_embeddings \= embed\_model.get\_image\_embedding(image\_url)
print("Image dim:", len(image\_embeddings))
print("Image embed:", image\_embeddings\[:5\])

text\_embeddings \= embed\_model.get\_text\_embedding(
    "Logo of a pink blue llama on dark background"
)
print("Text dim:", len(text\_embeddings))
print("Text embed:", text\_embeddings\[:5\])

cos\_sim \= dot(image\_embeddings, text\_embeddings) / (
    norm(image\_embeddings) \* norm(text\_embeddings)
)
print("Cosine similarity:", cos\_sim)

from llama\_index.embeddings.jinaai import JinaEmbedding from PIL import Image import requests from numpy import dot from numpy.linalg import norm embed\_model = JinaEmbedding( api\_key=jinaai\_api\_key, model="jina-clip-v1", ) image\_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStMP8S3VbNCqOQd7QQQcbvC\_FLa1HlftCiJw&s" im = Image.open(requests.get(image\_url, stream=True).raw) print("Image:") display(im) image\_embeddings = embed\_model.get\_image\_embedding(image\_url) print("Image dim:", len(image\_embeddings)) print("Image embed:", image\_embeddings\[:5\]) text\_embeddings = embed\_model.get\_text\_embedding( "Logo of a pink blue llama on dark background" ) print("Text dim:", len(text\_embeddings)) print("Text embed:", text\_embeddings\[:5\]) cos\_sim = dot(image\_embeddings, text\_embeddings) / ( norm(image\_embeddings) \* norm(text\_embeddings) ) print("Cosine similarity:", cos\_sim)

Embed in batches[¶](https://docs.llamaindex.ai/en/stable/examples/embeddings/jinaai_embeddings/#embed-in-batches)
-----------------------------------------------------------------------------------------------------------------

You can also embed text in batches, the batch size can be controlled by setting the `embed_batch_size` parameter (the default value will be 10 if not passed, and it should not be larger than 2048)

In \[ \]:

Copied!

embed\_model \= JinaEmbedding(
    api\_key\=jinaai\_api\_key,
    model\="jina-embeddings-v2-base-en",
    embed\_batch\_size\=16,
)

embeddings \= embed\_model.get\_text\_embedding\_batch(
    \["This is the text to embed", "More text can be provided in a batch"\]
)

print(len(embeddings))
print(embeddings\[0\]\[:5\])

embed\_model = JinaEmbedding( api\_key=jinaai\_api\_key, model="jina-embeddings-v2-base-en", embed\_batch\_size=16, ) embeddings = embed\_model.get\_text\_embedding\_batch( \["This is the text to embed", "More text can be provided in a batch"\] ) print(len(embeddings)) print(embeddings\[0\]\[:5\])

Let's build a RAG pipeline using Jina AI Embeddings[¶](https://docs.llamaindex.ai/en/stable/examples/embeddings/jinaai_embeddings/#lets-build-a-rag-pipeline-using-jina-ai-embeddings)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/embeddings/jinaai_embeddings/#download-data)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

#### Imports[¶](https://docs.llamaindex.ai/en/stable/examples/embeddings/jinaai_embeddings/#imports)

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader

from llama\_index.llms.openai import OpenAI
from llama\_index.core.response.notebook\_utils import display\_source\_node

from IPython.display import Markdown, display

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout)) from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.llms.openai import OpenAI from llama\_index.core.response.notebook\_utils import display\_source\_node from IPython.display import Markdown, display

#### Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/embeddings/jinaai_embeddings/#load-data)

In \[ \]:

Copied!

documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data()

#### Build index[¶](https://docs.llamaindex.ai/en/stable/examples/embeddings/jinaai_embeddings/#build-index)

In \[ \]:

Copied!

your\_openai\_key \= "YOUR\_OPENAI\_KEY"
llm \= OpenAI(api\_key\=your\_openai\_key)
embed\_model \= JinaEmbedding(
    api\_key\=jinaai\_api\_key,
    model\="jina-embeddings-v2-base-en",
    embed\_batch\_size\=16,
)

index \= VectorStoreIndex.from\_documents(
    documents\=documents, embed\_model\=embed\_model
)

your\_openai\_key = "YOUR\_OPENAI\_KEY" llm = OpenAI(api\_key=your\_openai\_key) embed\_model = JinaEmbedding( api\_key=jinaai\_api\_key, model="jina-embeddings-v2-base-en", embed\_batch\_size=16, ) index = VectorStoreIndex.from\_documents( documents=documents, embed\_model=embed\_model )

#### Build retriever[¶](https://docs.llamaindex.ai/en/stable/examples/embeddings/jinaai_embeddings/#build-retriever)

In \[ \]:

Copied!

search\_query\_retriever \= index.as\_retriever()

search\_query\_retrieved\_nodes \= search\_query\_retriever.retrieve(
    "What happened after the thesis?"
)

search\_query\_retriever = index.as\_retriever() search\_query\_retrieved\_nodes = search\_query\_retriever.retrieve( "What happened after the thesis?" )

In \[ \]:

Copied!

for n in search\_query\_retrieved\_nodes:
    display\_source\_node(n, source\_length\=2000)

for n in search\_query\_retrieved\_nodes: display\_source\_node(n, source\_length=2000)

Back to top

[Previous Jina 8K Context Window Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/jina_embeddings/)[Next Llamafile Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/llamafile/)
