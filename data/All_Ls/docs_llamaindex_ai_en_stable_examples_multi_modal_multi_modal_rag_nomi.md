Title: Multi-Modal RAG using Nomic Embed and Anthropic.

URL Source: https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_rag_nomic/

Markdown Content:
Multi-Modal RAG using Nomic Embed and Anthropic. - LlamaIndex


In this notebook, we show how to build a Multi-Modal RAG system using LlamaIndex, Nomic Embed, and Anthropic.

Wikipedia Text embedding index: [Nomic Embed Text v1.5](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5)

Wikipedia Images embedding index: [Nomic Embed Text v1.5](https://huggingface.co/nomic-ai/nomic-embed-vision-v1.5)

Query encoder:

*   Encoder query text for text index using Nomic Embed Text
*   Encoder query text for image index using Nomic Embed Vision

Framework: [LlamaIndex](https://github.com/run-llama/llama_index)

Steps:

1.  Download texts and images raw files for Wikipedia articles
2.  Build text index for vector store using Nomic Embed Text embeddings
3.  Build image index for vector store using Nomic Embed Vision embeddings
4.  Retrieve relevant text and image simultaneously using different query encoding embeddings and vector stores
5.  Pass retrieved texts and images to Claude 3

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-qdrant llama\-index\-multi\-modal\-llms\-anthropic llama\-index\-embeddings\-nomic

%pip install llama-index-vector-stores-qdrant llama-index-multi-modal-llms-anthropic llama-index-embeddings-nomic

In \[ \]:

Copied!

%pip install llama\_index ftfy regex tqdm
%pip install matplotlib scikit\-image
%pip install \-U qdrant\_client
%pip install wikipedia

%pip install llama\_index ftfy regex tqdm %pip install matplotlib scikit-image %pip install -U qdrant\_client %pip install wikipedia

Load and Download Multi-Modal datasets including texts and images from Wikipedia[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_rag_nomic/#load-and-download-multi-modal-datasets-including-texts-and-images-from-wikipedia)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Parse wikipedia articles and save into local folder

In \[ \]:

Copied!

from pathlib import Path
import requests

wiki\_titles \= \[
    "batman",
    "Vincent van Gogh",
    "San Francisco",
    "iPhone",
    "Tesla Model S",
    "BTS",
\]

data\_path \= Path("data\_wiki")

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

    if not data\_path.exists():
        Path.mkdir(data\_path)

    with open(data\_path / f"{title}.txt", "w") as fp:
        fp.write(wiki\_text)

from pathlib import Path import requests wiki\_titles = \[ "batman", "Vincent van Gogh", "San Francisco", "iPhone", "Tesla Model S", "BTS", \] data\_path = Path("data\_wiki") for title in wiki\_titles: response = requests.get( "https://en.wikipedia.org/w/api.php", params={ "action": "query", "format": "json", "titles": title, "prop": "extracts", "explaintext": True, }, ).json() page = next(iter(response\["query"\]\["pages"\].values())) wiki\_text = page\["extract"\] if not data\_path.exists(): Path.mkdir(data\_path) with open(data\_path / f"{title}.txt", "w") as fp: fp.write(wiki\_text)

Parse Wikipedia Images and texts. Load into local folder[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_rag_nomic/#parse-wikipedia-images-and-texts-load-into-local-folder)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

import wikipedia
import urllib.request
from pathlib import Path
import time

image\_path \= Path("data\_wiki")
image\_uuid \= 0
\# image\_metadata\_dict stores images metadata including image uuid, filename and path
image\_metadata\_dict \= {}
MAX\_IMAGES\_PER\_WIKI \= 30

wiki\_titles \= \[
    "San Francisco",
    "Batman",
    "Vincent van Gogh",
    "iPhone",
    "Tesla Model S",
    "BTS band",
\]

\# create folder for images only
if not image\_path.exists():
    Path.mkdir(image\_path)

\# Download images for wiki pages
\# Assign UUID for each image
for title in wiki\_titles:
    images\_per\_wiki \= 0
    print(title)
    try:
        page\_py \= wikipedia.page(title)
        list\_img\_urls \= page\_py.images
        for url in list\_img\_urls:
            if url.endswith(".jpg") or url.endswith(".png"):
                image\_uuid += 1
                image\_file\_name \= title + "\_" + url.split("/")\[\-1\]

                \# img\_path could be s3 path pointing to the raw image file in the future
                image\_metadata\_dict\[image\_uuid\] \= {
                    "filename": image\_file\_name,
                    "img\_path": "./" + str(image\_path / f"{image\_uuid}.jpg"),
                }

                \# Create a request with a valid User-Agent header
                req \= urllib.request.Request(
                    url,
                    data\=None,
                    headers\={
                        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
                    },
                )

                \# Open the URL and save the image
                with urllib.request.urlopen(req) as response, open(
                    image\_path / f"{image\_uuid}.jpg", "wb"
                ) as out\_file:
                    out\_file.write(response.read())

                images\_per\_wiki += 1
                \# Limit the number of images downloaded per wiki page to 15
                if images\_per\_wiki \> MAX\_IMAGES\_PER\_WIKI:
                    break

                \# Add a delay between requests to avoid overwhelming the server
                time.sleep(1)  \# Adjust the delay as needed

    except Exception as e:
        print(e)
        print(f"{images\_per\_wiki\=}")
        continue

import wikipedia import urllib.request from pathlib import Path import time image\_path = Path("data\_wiki") image\_uuid = 0 # image\_metadata\_dict stores images metadata including image uuid, filename and path image\_metadata\_dict = {} MAX\_IMAGES\_PER\_WIKI = 30 wiki\_titles = \[ "San Francisco", "Batman", "Vincent van Gogh", "iPhone", "Tesla Model S", "BTS band", \] # create folder for images only if not image\_path.exists(): Path.mkdir(image\_path) # Download images for wiki pages # Assign UUID for each image for title in wiki\_titles: images\_per\_wiki = 0 print(title) try: page\_py = wikipedia.page(title) list\_img\_urls = page\_py.images for url in list\_img\_urls: if url.endswith(".jpg") or url.endswith(".png"): image\_uuid += 1 image\_file\_name = title + "\_" + url.split("/")\[-1\] # img\_path could be s3 path pointing to the raw image file in the future image\_metadata\_dict\[image\_uuid\] = { "filename": image\_file\_name, "img\_path": "./" + str(image\_path / f"{image\_uuid}.jpg"), } # Create a request with a valid User-Agent header req = urllib.request.Request( url, data=None, headers={ "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36" }, ) # Open the URL and save the image with urllib.request.urlopen(req) as response, open( image\_path / f"{image\_uuid}.jpg", "wb" ) as out\_file: out\_file.write(response.read()) images\_per\_wiki += 1 # Limit the number of images downloaded per wiki page to 15 if images\_per\_wiki > MAX\_IMAGES\_PER\_WIKI: break # Add a delay between requests to avoid overwhelming the server time.sleep(1) # Adjust the delay as needed except Exception as e: print(e) print(f"{images\_per\_wiki=}") continue

San Francisco
Batman
Vincent van Gogh
iPhone
Tesla Model S
BTS band

In \[ \]:

Copied!

import os

os.environ\["NOMIC\_API\_KEY"\] \= ""
os.environ\["ANTHROPIC\_API\_KEY"\] \= ""

import os os.environ\["NOMIC\_API\_KEY"\] = "" os.environ\["ANTHROPIC\_API\_KEY"\] = ""

Build Multi Modal Vector Store using Text and Image embeddings under different collections[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_rag_nomic/#build-multi-modal-vector-store-using-text-and-image-embeddings-under-different-collections)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

import qdrant\_client
from llama\_index.core import SimpleDirectoryReader
from llama\_index.vector\_stores.qdrant import QdrantVectorStore
from llama\_index.core import VectorStoreIndex, StorageContext
from llama\_index.core.indices import MultiModalVectorStoreIndex
from llama\_index.embeddings.nomic import NomicEmbedding

\# Create a local Qdrant vector store
client \= qdrant\_client.QdrantClient(path\="qdrant\_db")

text\_store \= QdrantVectorStore(
    client\=client, collection\_name\="text\_collection"
)
image\_store \= QdrantVectorStore(
    client\=client, collection\_name\="image\_collection"
)
storage\_context \= StorageContext.from\_defaults(
    vector\_store\=text\_store, image\_store\=image\_store
)
embedding\_model \= NomicEmbedding(
    model\_name\="nomic-embed-text-v1.5",
    vision\_model\_name\="nomic-embed-vision-v1.5",
)

\# Create the MultiModal index
documents \= SimpleDirectoryReader("./data\_wiki/").load\_data()
index \= MultiModalVectorStoreIndex.from\_documents(
    documents,
    storage\_context\=storage\_context,
    embed\_model\=embedding\_model,
    image\_embed\_model\=embedding\_model,
)

import qdrant\_client from llama\_index.core import SimpleDirectoryReader from llama\_index.vector\_stores.qdrant import QdrantVectorStore from llama\_index.core import VectorStoreIndex, StorageContext from llama\_index.core.indices import MultiModalVectorStoreIndex from llama\_index.embeddings.nomic import NomicEmbedding # Create a local Qdrant vector store client = qdrant\_client.QdrantClient(path="qdrant\_db") text\_store = QdrantVectorStore( client=client, collection\_name="text\_collection" ) image\_store = QdrantVectorStore( client=client, collection\_name="image\_collection" ) storage\_context = StorageContext.from\_defaults( vector\_store=text\_store, image\_store=image\_store ) embedding\_model = NomicEmbedding( model\_name="nomic-embed-text-v1.5", vision\_model\_name="nomic-embed-vision-v1.5", ) # Create the MultiModal index documents = SimpleDirectoryReader("./data\_wiki/").load\_data() index = MultiModalVectorStoreIndex.from\_documents( documents, storage\_context=storage\_context, embed\_model=embedding\_model, image\_embed\_model=embedding\_model, )

/Users/zach/Library/Caches/pypoetry/virtualenvs/llama-index-cFuSqcva-py3.12/lib/python3.12/site-packages/PIL/Image.py:3218: DecompressionBombWarning: Image size (101972528 pixels) exceeds limit of 89478485 pixels, could be decompression bomb DOS attack.
  warnings.warn(

### Plot downloaded Images from Wikipedia[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_rag_nomic/#plot-downloaded-images-from-wikipedia)

In \[ \]:

Copied!

from PIL import Image
import matplotlib.pyplot as plt
import os

def plot\_images(image\_metadata\_dict):
    original\_images\_urls \= \[\]
    images\_shown \= 0
    for image\_id in image\_metadata\_dict:
        img\_path \= image\_metadata\_dict\[image\_id\]\["img\_path"\]
        if os.path.isfile(img\_path):
            filename \= image\_metadata\_dict\[image\_id\]\["filename"\]
            image \= Image.open(img\_path).convert("RGB")

            plt.subplot(9, 9, len(original\_images\_urls) + 1)
            plt.imshow(image)
            plt.xticks(\[\])
            plt.yticks(\[\])

            original\_images\_urls.append(filename)
            images\_shown += 1
            if images\_shown \>= 81:
                break

    plt.tight\_layout()

plot\_images(image\_metadata\_dict)

from PIL import Image import matplotlib.pyplot as plt import os def plot\_images(image\_metadata\_dict): original\_images\_urls = \[\] images\_shown = 0 for image\_id in image\_metadata\_dict: img\_path = image\_metadata\_dict\[image\_id\]\["img\_path"\] if os.path.isfile(img\_path): filename = image\_metadata\_dict\[image\_id\]\["filename"\] image = Image.open(img\_path).convert("RGB") plt.subplot(9, 9, len(original\_images\_urls) + 1) plt.imshow(image) plt.xticks(\[\]) plt.yticks(\[\]) original\_images\_urls.append(filename) images\_shown += 1 if images\_shown >= 81: break plt.tight\_layout() plot\_images(image\_metadata\_dict)

/Users/zach/Library/Caches/pypoetry/virtualenvs/llama-index-cFuSqcva-py3.12/lib/python3.12/site-packages/PIL/Image.py:3218: DecompressionBombWarning: Image size (101972528 pixels) exceeds limit of 89478485 pixels, could be decompression bomb DOS attack.
  warnings.warn(

![Image 4: No description has been provided for this image](blob:https://docs.llamaindex.ai/be3ff87a716e53948b375ed70ba58a92)

In \[ \]:

Copied!

def plot\_images(image\_paths):
    images\_shown \= 0
    plt.figure(figsize\=(16, 9))
    for img\_path in image\_paths:
        if os.path.isfile(img\_path):
            image \= Image.open(img\_path)

            plt.subplot(2, 3, images\_shown + 1)
            plt.imshow(image)
            plt.xticks(\[\])
            plt.yticks(\[\])

            images\_shown += 1
            if images\_shown \>= 9:
                break

def plot\_images(image\_paths): images\_shown = 0 plt.figure(figsize=(16, 9)) for img\_path in image\_paths: if os.path.isfile(img\_path): image = Image.open(img\_path) plt.subplot(2, 3, images\_shown + 1) plt.imshow(image) plt.xticks(\[\]) plt.yticks(\[\]) images\_shown += 1 if images\_shown >= 9: break

Get Multi-Modal retrieval results for some example queries[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_rag_nomic/#get-multi-modal-retrieval-results-for-some-example-queries)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

test\_query \= "Who are the band members in BTS?"
\# generate  retrieval results
retriever \= index.as\_retriever(similarity\_top\_k\=3, image\_similarity\_top\_k\=5)
retrieval\_results \= retriever.retrieve(test\_query)

test\_query = "Who are the band members in BTS?" # generate retrieval results retriever = index.as\_retriever(similarity\_top\_k=3, image\_similarity\_top\_k=5) retrieval\_results = retriever.retrieve(test\_query)

In \[ \]:

Copied!

from llama\_index.core.response.notebook\_utils import display\_source\_node
from llama\_index.core.schema import ImageNode

retrieved\_image \= \[\]
for res\_node in retrieval\_results:
    if isinstance(res\_node.node, ImageNode):
        retrieved\_image.append(res\_node.node.metadata\["file\_path"\])
    else:
        display\_source\_node(res\_node, source\_length\=200)

plot\_images(retrieved\_image)

from llama\_index.core.response.notebook\_utils import display\_source\_node from llama\_index.core.schema import ImageNode retrieved\_image = \[\] for res\_node in retrieval\_results: if isinstance(res\_node.node, ImageNode): retrieved\_image.append(res\_node.node.metadata\["file\_path"\]) else: display\_source\_node(res\_node, source\_length=200) plot\_images(retrieved\_image)

**Node ID:** 57e904ab-803b-4bf0-8d39-d4c07b80fa7a  
**Similarity:** 0.8063886499053818  
**Text:** BTS (Korean: 방탄소년단; RR: Bangtan Sonyeondan; lit. Bulletproof Boy Scouts), also known as the Bangtan Boys, is a South Korean boy band formed in 2010. The band consists of Jin, Suga, J-Hope, RM, Jimi...

**Node ID:** 2deb16e2-d4a6-4725-9a9d-e72c910885c3  
**Similarity:** 0.7790615531161136  
**Text:** 

BTS are known for their philanthropic endeavors. Several members of the band have been inducted into prestigious donation clubs, such as the UNICEF Honors Club and the Green N...

**Node ID:** d80dd35c-be67-4226-b0b8-fbff4981a3cf  
**Similarity:** 0.7593813810748964  
**Text:**  BTS stands for the Korean phrase Bangtan Sonyeondan (Korean: 방탄소년단; Hanja: 防彈少年團), which translates literally to 'Bulletproof Boy Scouts'. According to member J-Hope, the name signifies ...

![Image 5: No description has been provided for this image](blob:https://docs.llamaindex.ai/d7c641b9ba55469d447946182622f342)

In \[ \]:

Copied!

test\_query \= "What are Vincent van Gogh's famous paintings"
\# generate  retrieval results
retriever \= index.as\_retriever(similarity\_top\_k\=3, image\_similarity\_top\_k\=5)
retrieval\_results \= retriever.retrieve(test\_query)

retrieved\_image \= \[\]
for res\_node in retrieval\_results:
    if isinstance(res\_node.node, ImageNode):
        retrieved\_image.append(res\_node.node.metadata\["file\_path"\])
    else:
        display\_source\_node(res\_node, source\_length\=200)

plot\_images(retrieved\_image)

test\_query = "What are Vincent van Gogh's famous paintings" # generate retrieval results retriever = index.as\_retriever(similarity\_top\_k=3, image\_similarity\_top\_k=5) retrieval\_results = retriever.retrieve(test\_query) retrieved\_image = \[\] for res\_node in retrieval\_results: if isinstance(res\_node.node, ImageNode): retrieved\_image.append(res\_node.node.metadata\["file\_path"\]) else: display\_source\_node(res\_node, source\_length=200) plot\_images(retrieved\_image)

**Node ID:** e385577c-b150-4ead-9758-039461125962  
**Similarity:** 0.83218262953011  
**Text:** Vincent Willem van Gogh (Dutch: \[ˈvɪnsɛnt ˈʋɪləɱ‿vɑŋ‿ˈɣɔx\] ; 30 March 1853 – 29 July 1890) was a Dutch Post-Impressionist painter who is among the most famous and influential figures in the history...

**Node ID:** a3edf96b-47ca-48ec-969f-d3a47febd539  
**Similarity:** 0.8288469749568774  
**Text:** This novel and the 1956 film further enhanced his fame, especially in the United States where Stone surmised only a few hundred people had heard of Van Gogh prior to his surprise best-selling book....

**Node ID:** 4e8de603-dac6-4ead-8851-85b4526ac8ca  
**Similarity:** 0.8060470396548032  
**Text:** Ten paintings were shown at the Société des Artistes Indépendants, in Brussels in January 1890. French president Marie François Sadi Carnot was said to have been impressed by Van Gogh's work. After...

![Image 6: No description has been provided for this image](blob:https://docs.llamaindex.ai/04aaf963e7b9130ec16e016c2c590594)

In \[ \]:

Copied!

test\_query \= "What are the popular tourist attraction in San Francisco"
\# generate  retrieval results
retriever \= index.as\_retriever(similarity\_top\_k\=3, image\_similarity\_top\_k\=5)
retrieval\_results \= retriever.retrieve(test\_query)

retrieved\_image \= \[\]
for res\_node in retrieval\_results:
    if isinstance(res\_node.node, ImageNode):
        retrieved\_image.append(res\_node.node.metadata\["file\_path"\])
    else:
        display\_source\_node(res\_node, source\_length\=200)

plot\_images(retrieved\_image)

test\_query = "What are the popular tourist attraction in San Francisco" # generate retrieval results retriever = index.as\_retriever(similarity\_top\_k=3, image\_similarity\_top\_k=5) retrieval\_results = retriever.retrieve(test\_query) retrieved\_image = \[\] for res\_node in retrieval\_results: if isinstance(res\_node.node, ImageNode): retrieved\_image.append(res\_node.node.metadata\["file\_path"\]) else: display\_source\_node(res\_node, source\_length=200) plot\_images(retrieved\_image)

**Node ID:** c2b89622-c61a-4b70-bbc1-1b3708464426  
**Similarity:** 0.7699549146961432  
**Text:** San Francisco was ranked fifth in the world and second in the United States on the Global Financial Centres Index as of September 2023. Despite a continuing exodus of businesses from the downtown a...

**Node ID:** 0363c291-80d0-4766-85b6-02407b46e8e1  
**Similarity:** 0.7672793963976988  
**Text:** However, by 2016, San Francisco was rated low by small businesses in a Business Friendliness Survey.

Like many U.S. cities, San Francisco once had a significant manufacturing sector employing near...

**Node ID:** 676c2719-7da8-4044-aa70-f84b8e45281e  
**Similarity:** 0.7605001448191087  
**Text:** 

Several of San Francisco's parks and nearly all of its beaches form part of the regional Golden Gate National Recreation Area, one of the most visited units of the Natio...

![Image 7: No description has been provided for this image](blob:https://docs.llamaindex.ai/0a06cf749bfb4ee401bf5684cb28724e)

In \[ \]:

Copied!

test\_query \= "Which company makes Tesla"
\# generate  retrieval results
retriever \= index.as\_retriever(similarity\_top\_k\=3, image\_similarity\_top\_k\=5)
retrieval\_results \= retriever.retrieve(test\_query)

retrieved\_image \= \[\]
for res\_node in retrieval\_results:
    if isinstance(res\_node.node, ImageNode):
        retrieved\_image.append(res\_node.node.metadata\["file\_path"\])
    else:
        display\_source\_node(res\_node, source\_length\=200)

plot\_images(retrieved\_image)

test\_query = "Which company makes Tesla" # generate retrieval results retriever = index.as\_retriever(similarity\_top\_k=3, image\_similarity\_top\_k=5) retrieval\_results = retriever.retrieve(test\_query) retrieved\_image = \[\] for res\_node in retrieval\_results: if isinstance(res\_node.node, ImageNode): retrieved\_image.append(res\_node.node.metadata\["file\_path"\]) else: display\_source\_node(res\_node, source\_length=200) plot\_images(retrieved\_image)

**Node ID:** 63c77d12-3420-4c1c-bc35-edcf968238c0  
**Similarity:** 0.7183866127180777  
**Text:** The Tesla Model S is a battery electric executive car with a liftback body style built by Tesla, Inc. since 2012. The Model S features a battery-powered dual-motor, all-wheel drive layout, although...

**Node ID:** 6e95a173-44b6-4837-b424-86ce223ce801  
**Similarity:** 0.7103282638750231  
**Text:** 

Tesla sells its cars directly to consumers without a dealer network, as other manufacturers have done and as many states require by legislation. In support of its approa...

**Node ID:** 30fe5ba5-7790-44d4-a1ac-17d5ffff6e70  
**Similarity:** 0.7057133871456653  
**Text:** 

\

The first nine Australian units were delivered in Sydney on December 9, 2014. Tesla opened its first store and service centre in St Leonards, and ...

![Image 8: No description has been provided for this image](blob:https://docs.llamaindex.ai/2691b9e60c54c0e41ce0bdef40cc77bd)

In \[ \]:

Copied!

test\_query \= "what is the main character in Batman"
\# generate  retrieval results
retriever \= index.as\_retriever(similarity\_top\_k\=3, image\_similarity\_top\_k\=5)
retrieval\_results \= retriever.retrieve(test\_query)

retrieved\_image \= \[\]
for res\_node in retrieval\_results:
    if isinstance(res\_node.node, ImageNode):
        retrieved\_image.append(res\_node.node.metadata\["file\_path"\])
    else:
        display\_source\_node(res\_node, source\_length\=200)

plot\_images(retrieved\_image)

test\_query = "what is the main character in Batman" # generate retrieval results retriever = index.as\_retriever(similarity\_top\_k=3, image\_similarity\_top\_k=5) retrieval\_results = retriever.retrieve(test\_query) retrieved\_image = \[\] for res\_node in retrieval\_results: if isinstance(res\_node.node, ImageNode): retrieved\_image.append(res\_node.node.metadata\["file\_path"\]) else: display\_source\_node(res\_node, source\_length=200) plot\_images(retrieved\_image)

**Node ID:** 9df946c8-2d86-43ef-ad49-52d02fc9ca9f  
**Similarity:** 0.813633584027285  
**Text:** Batman is a superhero appearing in American comic books published by DC Comics. The character was created by artist Bob Kane and writer Bill Finger, and debuted in the 27th issue of the comic book ...

**Node ID:** cd23d57f-1baa-4b64-98e8-f137437f1977  
**Similarity:** 0.8057558559295224  
**Text:**  Batman's primary character traits can be summarized as "wealth; physical prowess; deductive abilities and obsession". The details and tone of Batman comic books have varied ov...

**Node ID:** 5e49c94a-54de-493b-a31e-5cf3567a96cb  
**Similarity:** 0.7948625863921873  
**Text:** 

\

Batman's secret identity is Bruce Wayne, a wealthy American industrialist. As a child, Bruce witnessed the murder of his parents, Dr. Thomas Wayne and ...

![Image 9: No description has been provided for this image](blob:https://docs.llamaindex.ai/95637b45e274e5a240e19038ef05fb30)

Multimodal RAG with Claude 3[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_rag_nomic/#multimodal-rag-with-claude-3)
----------------------------------------------------------------------------------------------------------------------------------------------

Using Nomic Embed and Claude 3, we can now perform Multimodal RAG! The images and texts are passed to Claude 3 to reason over.

In \[ \]:

Copied!

from llama\_index.multi\_modal\_llms.anthropic import AnthropicMultiModal

query\_engine \= index.as\_query\_engine(
    llm\=AnthropicMultiModal(), similarity\_top\_k\=2, image\_similarity\_top\_k\=1
)

from llama\_index.multi\_modal\_llms.anthropic import AnthropicMultiModal query\_engine = index.as\_query\_engine( llm=AnthropicMultiModal(), similarity\_top\_k=2, image\_similarity\_top\_k=1 )

In \[ \]:

Copied!

response \= query\_engine.query(
    "What are Vincent van Gogh's famous paintings and popular subjects?"
)

response = query\_engine.query( "What are Vincent van Gogh's famous paintings and popular subjects?" )

In \[ \]:

Copied!

print(str(response))

print(str(response))

Based on the provided context, some of Vincent van Gogh's most famous paintings and popular subjects include:

- Landscapes, still lifes, portraits, and self-portraits characterized by bold colors and dramatic brushwork. This contributed to the rise of expressionism in modern art.

- In his early works, he depicted mostly still lifes and peasant laborers. 

- After moving to Arles in southern France in 1888, his paintings grew brighter and he turned his attention to depicting the natural world, including local olive groves, wheat fields and sunflowers.

- Some of his most expensive paintings that have sold for over $100 million (in today's equivalent prices) include Portrait of Dr Gachet, Portrait of Joseph Roulin, and Irises. 

- The Metropolitan Museum of Art acquired his painting Wheat Field with Cypresses in 1993 for $57 million.

So in summary, Van Gogh is especially well-known for his vibrant, expressive landscapes of places he lived like Arles, portraits, and still life paintings of subjects like sunflowers, olive groves and wheat fields. His bold use of color and thick, dramatic brushstrokes were highly influential on later art movements.

Back to top

[Previous Multi-Modal GPT4V Pydantic Program](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_pydantic/)[Next Multi-Modal Retrieval using GPT text embedding and CLIP image embedding for Wikipedia Articles](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_retrieval/)

Hi, how can I help you?

🦙
