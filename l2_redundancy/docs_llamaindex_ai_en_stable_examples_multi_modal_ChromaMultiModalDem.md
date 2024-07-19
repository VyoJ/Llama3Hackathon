Title: Chroma Multi-Modal Demo with LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/multi_modal/ChromaMultiModalDemo/

Markdown Content:
Chroma Multi-Modal Demo with LlamaIndex - LlamaIndex


> [Chroma](https://docs.trychroma.com/getting-started) is a AI-native open-source vector database focused on developer productivity and happiness. Chroma is licensed under Apache 2.0.

 [![Image 4: Discord](https://img.shields.io/discord/1073293645303795742)](https://discord.gg/MMeYNTmh3x)   [![Image 5: License](https://img.shields.io/static/v1?label=license&message=Apache%202.0&color=white)](https://github.com/chroma-core/chroma/blob/master/LICENSE)   ![Image 6: Integration Tests](https://github.com/chroma-core/chroma/actions/workflows/chroma-integration-test.yml/badge.svg?branch=main)

*   [Website](https://www.trychroma.com/)
*   [Documentation](https://docs.trychroma.com/)
*   [Twitter](https://twitter.com/trychroma)
*   [Discord](https://discord.gg/MMeYNTmh3x)

Chroma is fully-typed, fully-tested and fully-documented.

Install Chroma with:

pip install chromadb

Chroma runs in various modes. See below for examples of each integrated with LangChain.

*   `in-memory` - in a python script or jupyter notebook
*   `in-memory with persistance` - in a script or notebook and save/load to disk
*   `in a docker container` - as a server running your local machine or in the cloud

Like any other database, you can:

*   `.add`
*   `.get`
*   `.update`
*   `.upsert`
*   `.delete`
*   `.peek`
*   and `.query` runs the similarity search.

View full docs at [docs](https://docs.trychroma.com/reference/Collection).

Basic Example[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/ChromaMultiModalDemo/#basic-example)
---------------------------------------------------------------------------------------------------------------

In this basic example, we take the a Paul Graham essay, split it into chunks, embed it using an open-source embedding model, load it into Chroma, and then query it.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-qdrant
%pip install llama\-index\-embeddings\-huggingface
%pip install llama\-index\-vector\-stores\-chroma

%pip install llama-index-vector-stores-qdrant %pip install llama-index-embeddings-huggingface %pip install llama-index-vector-stores-chroma

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

#### Creating a Chroma Index[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/ChromaMultiModalDemo/#creating-a-chroma-index)

In \[ \]:

Copied!

!pip install llama\-index chromadb \--quiet
!pip install chromadb\1.10.11
!pip install open\-clip\-torch

!pip install llama-index chromadb --quiet !pip install chromadb1.10.11 !pip install open-clip-torch

In \[ \]:

Copied!

\# import
from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.vector\_stores.chroma import ChromaVectorStore
from llama\_index.core import StorageContext
from llama\_index.embeddings.huggingface import HuggingFaceEmbedding
from IPython.display import Markdown, display
import chromadb

\# import from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.vector\_stores.chroma import ChromaVectorStore from llama\_index.core import StorageContext from llama\_index.embeddings.huggingface import HuggingFaceEmbedding from IPython.display import Markdown, display import chromadb

In \[ \]:

Copied!

\# set up OpenAI
import os
import openai

OPENAI\_API\_KEY \= ""
openai.api\_key \= OPENAI\_API\_KEY
os.environ\["OPENAI\_API\_KEY"\] \= OPENAI\_API\_KEY

\# set up OpenAI import os import openai OPENAI\_API\_KEY = "" openai.api\_key = OPENAI\_API\_KEY os.environ\["OPENAI\_API\_KEY"\] = OPENAI\_API\_KEY

Download Images and Texts from Wikipedia[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/ChromaMultiModalDemo/#download-images-and-texts-from-wikipedia)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

import requests

def get\_wikipedia\_images(title):
    response \= requests.get(
        "https://en.wikipedia.org/w/api.php",
        params\={
            "action": "query",
            "format": "json",
            "titles": title,
            "prop": "imageinfo",
            "iiprop": "url|dimensions|mime",
            "generator": "images",
            "gimlimit": "50",
        },
    ).json()
    image\_urls \= \[\]
    for page in response\["query"\]\["pages"\].values():
        if page\["imageinfo"\]\[0\]\["url"\].endswith(".jpg") or page\["imageinfo"\]\[
            0
        \]\["url"\].endswith(".png"):
            image\_urls.append(page\["imageinfo"\]\[0\]\["url"\])
    return image\_urls

import requests def get\_wikipedia\_images(title): response = requests.get( "https://en.wikipedia.org/w/api.php", params={ "action": "query", "format": "json", "titles": title, "prop": "imageinfo", "iiprop": "url|dimensions|mime", "generator": "images", "gimlimit": "50", }, ).json() image\_urls = \[\] for page in response\["query"\]\["pages"\].values(): if page\["imageinfo"\]\[0\]\["url"\].endswith(".jpg") or page\["imageinfo"\]\[ 0 \]\["url"\].endswith(".png"): image\_urls.append(page\["imageinfo"\]\[0\]\["url"\]) return image\_urls

In \[ \]:

Copied!

from pathlib import Path
import urllib.request

image\_uuid \= 0
MAX\_IMAGES\_PER\_WIKI \= 20

wiki\_titles \= {
    "Tesla Model X",
    "Pablo Picasso",
    "Rivian",
    "The Lord of the Rings",
    "The Matrix",
    "The Simpsons",
}

data\_path \= Path("mixed\_wiki")
if not data\_path.exists():
    Path.mkdir(data\_path)

for title in wiki\_titles:
    response \= requests.get(
        "https://en.wikipedia.org/w/api.php",
        params\={
            "action": "query",
            "format": "json",
            "titles": title,
            "prop": "extracts",
            "explaintext": True,
        },
    ).json()
    page \= next(iter(response\["query"\]\["pages"\].values()))
    wiki\_text \= page\["extract"\]

    with open(data\_path / f"{title}.txt", "w") as fp:
        fp.write(wiki\_text)

    images\_per\_wiki \= 0
    try:
        \# page\_py = wikipedia.page(title)
        list\_img\_urls \= get\_wikipedia\_images(title)
        \# print(list\_img\_urls)

        for url in list\_img\_urls:
            if url.endswith(".jpg") or url.endswith(".png"):
                image\_uuid += 1
                \# image\_file\_name = title + "\_" + url.split("/")\[-1\]

                urllib.request.urlretrieve(
                    url, data\_path / f"{image\_uuid}.jpg"
                )
                images\_per\_wiki += 1
                \# Limit the number of images downloaded per wiki page to 15
                if images\_per\_wiki \> MAX\_IMAGES\_PER\_WIKI:
                    break
    except:
        print(str(Exception("No images found for Wikipedia page: ")) + title)
        continue

from pathlib import Path import urllib.request image\_uuid = 0 MAX\_IMAGES\_PER\_WIKI = 20 wiki\_titles = { "Tesla Model X", "Pablo Picasso", "Rivian", "The Lord of the Rings", "The Matrix", "The Simpsons", } data\_path = Path("mixed\_wiki") if not data\_path.exists(): Path.mkdir(data\_path) for title in wiki\_titles: response = requests.get( "https://en.wikipedia.org/w/api.php", params={ "action": "query", "format": "json", "titles": title, "prop": "extracts", "explaintext": True, }, ).json() page = next(iter(response\["query"\]\["pages"\].values())) wiki\_text = page\["extract"\] with open(data\_path / f"{title}.txt", "w") as fp: fp.write(wiki\_text) images\_per\_wiki = 0 try: # page\_py = wikipedia.page(title) list\_img\_urls = get\_wikipedia\_images(title) # print(list\_img\_urls) for url in list\_img\_urls: if url.endswith(".jpg") or url.endswith(".png"): image\_uuid += 1 # image\_file\_name = title + "\_" + url.split("/")\[-1\] urllib.request.urlretrieve( url, data\_path / f"{image\_uuid}.jpg" ) images\_per\_wiki += 1 # Limit the number of images downloaded per wiki page to 15 if images\_per\_wiki > MAX\_IMAGES\_PER\_WIKI: break except: print(str(Exception("No images found for Wikipedia page: ")) + title) continue

Set the embedding model[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/ChromaMultiModalDemo/#set-the-embedding-model)
-----------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from chromadb.utils.embedding\_functions import OpenCLIPEmbeddingFunction

\# set defalut text and image embedding functions
embedding\_function \= OpenCLIPEmbeddingFunction()

from chromadb.utils.embedding\_functions import OpenCLIPEmbeddingFunction # set defalut text and image embedding functions embedding\_function = OpenCLIPEmbeddingFunction()

/Users/haotianzhang/llama\_index/venv/lib/python3.11/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user\_install.html
  from .autonotebook import tqdm as notebook\_tqdm

Build Chroma Multi-Modal Index with LlamaIndex[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/ChromaMultiModalDemo/#build-chroma-multi-modal-index-with-llamaindex)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core.indices import MultiModalVectorStoreIndex
from llama\_index.vector\_stores.qdrant import QdrantVectorStore
from llama\_index.core import SimpleDirectoryReader, StorageContext
from chromadb.utils.data\_loaders import ImageLoader

image\_loader \= ImageLoader()

\# create client and a new collection
chroma\_client \= chromadb.EphemeralClient()
chroma\_collection \= chroma\_client.create\_collection(
    "multimodal\_collection",
    embedding\_function\=embedding\_function,
    data\_loader\=image\_loader,
)

\# load documents
documents \= SimpleDirectoryReader("./mixed\_wiki/").load\_data()

\# set up ChromaVectorStore and load in data
vector\_store \= ChromaVectorStore(chroma\_collection\=chroma\_collection)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents,
    storage\_context\=storage\_context,
)

from llama\_index.core.indices import MultiModalVectorStoreIndex from llama\_index.vector\_stores.qdrant import QdrantVectorStore from llama\_index.core import SimpleDirectoryReader, StorageContext from chromadb.utils.data\_loaders import ImageLoader image\_loader = ImageLoader() # create client and a new collection chroma\_client = chromadb.EphemeralClient() chroma\_collection = chroma\_client.create\_collection( "multimodal\_collection", embedding\_function=embedding\_function, data\_loader=image\_loader, ) # load documents documents = SimpleDirectoryReader("./mixed\_wiki/").load\_data() # set up ChromaVectorStore and load in data vector\_store = ChromaVectorStore(chroma\_collection=chroma\_collection) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context, )

Retrieve results from Multi-Modal Index[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/ChromaMultiModalDemo/#retrieve-results-from-multi-modal-index)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

retriever \= index.as\_retriever(similarity\_top\_k\=50)
retrieval\_results \= retriever.retrieve("Picasso famous paintings")

retriever = index.as\_retriever(similarity\_top\_k=50) retrieval\_results = retriever.retrieve("Picasso famous paintings")

In \[ \]:

Copied!

\# print(retrieval\_results)
from llama\_index.core.schema import ImageNode
from llama\_index.core.response.notebook\_utils import (
    display\_source\_node,
    display\_image\_uris,
)

image\_results \= \[\]
MAX\_RES \= 5
cnt \= 0
for r in retrieval\_results:
    if isinstance(r.node, ImageNode):
        image\_results.append(r.node.metadata\["file\_path"\])
    else:
        if cnt < MAX\_RES:
            display\_source\_node(r)
        cnt += 1

display\_image\_uris(image\_results, \[3, 3\], top\_k\=2)

\# print(retrieval\_results) from llama\_index.core.schema import ImageNode from llama\_index.core.response.notebook\_utils import ( display\_source\_node, display\_image\_uris, ) image\_results = \[\] MAX\_RES = 5 cnt = 0 for r in retrieval\_results: if isinstance(r.node, ImageNode): image\_results.append(r.node.metadata\["file\_path"\]) else: if cnt < MAX\_RES: display\_source\_node(r) cnt += 1 display\_image\_uris(image\_results, \[3, 3\], top\_k=2)

**Node ID:** 13adcbba-fe8b-4d51-9139-fb1c55ffc6be  
**Similarity:** 0.774399292477267  
**Text:**  Picasso's influence was and remains immense and widely acknowledged by his ...

**Node ID:** 4100593e-6b6a-4b5f-8384-98d1c2468204  
**Similarity:** 0.7695965506408678  
**Text:**  Picasso was one of 250 sculptors who exhibited in t...

**Node ID:** aeed9d43-f9c5-42a9-a7b9-1a3c005e3745  
**Similarity:** 0.7693110304140338  
**Text:** Pablo Ruiz Picasso (25 October 1881 – 8 April 1973) was a Spanish painter, sculptor, printmaker, ...

**Node ID:** 5a6613b6-b599-4e40-92f2-231e10ed54f6  
**Similarity:** 0.7656537748231977  
**Text:**  In the 1940s, a Swiss insurance company based in Basel had bought two pain...

**Node ID:** cc17454c-030d-4f86-a12e-342d0582f4d3  
**Similarity:** 0.7639671751819532  
**Text:** 

Picasso was exceptionally prolific throughout his long lifetime. At hi...

![Image 7: No description has been provided for this image](blob:https://docs.llamaindex.ai/4519b26f21b54f1fe8ecca1ceff93786)

Back to top

[Previous Pydantic Extractor](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/PydanticExtractor/)[Next Multi-Modal LLM using Anthropic model for image reasoning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/anthropic_multi_modal/)

Hi, how can I help you?

🦙
