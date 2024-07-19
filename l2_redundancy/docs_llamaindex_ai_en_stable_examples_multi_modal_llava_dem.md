Title: LlaVa Demo with LlamaIndex - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/multi_modal/llava_demo/

Markdown Content:
LlaVa Demo with LlamaIndex - LlamaIndex


In this example, we illustrate how we use LlaVa for belowing tasks:

*   Retrieval Augmented Image Captioning
*   Pydantic Structured Output
*   Multi-Modal Retrieval-Augmented Generation (RAG) using Llava-13b

Context for LLaVA: Large Language and Vision Assistant

*   [Website](https://llava-vl.github.io/)
*   [Paper](https://arxiv.org/abs/2304.08485)
*   [Github](https://github.com/haotian-liu/LLaVA)
*   LLaVA 13b is now supported in Replicate: [See here.](https://replicate.com/yorickvp/llava-13b)

For LlamaIndex: LlaVa+Replicate enables us to run image understanding locally and combine the multi-modal knowledge with our RAG knowledge based system.

Retrieval Augmented Image Captioning using Llava-13b[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/llava_demo/#retrieval-augmented-image-captioning-using-llava-13b)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Using Replicate serving LLaVa model through LlamaIndex[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/llava_demo/#using-replicate-serving-llava-model-through-llamaindex)

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-qdrant
%pip install llama\-index\-readers\-file
%pip install llama\-index\-multi\-modal\-llms\-replicate

%pip install llama-index-vector-stores-qdrant %pip install llama-index-readers-file %pip install llama-index-multi-modal-llms-replicate

In \[ \]:

Copied!

%pip install unstructured replicate
%pip install llama\_index ftfy regex tqdm
%pip install git+https://github.com/openai/CLIP.git
%pip install torch torchvision
%pip install matplotlib scikit\-image
%pip install \-U qdrant\_client

%pip install unstructured replicate %pip install llama\_index ftfy regex tqdm %pip install git+https://github.com/openai/CLIP.git %pip install torch torchvision %pip install matplotlib scikit-image %pip install -U qdrant\_client

UsageError: Line magic function \`%\` not found.

In \[ \]:

Copied!

import os

REPLICATE\_API\_TOKEN \= "..."  \# Your Relicate API token here
os.environ\["REPLICATE\_API\_TOKEN"\] \= REPLICATE\_API\_TOKEN

import os REPLICATE\_API\_TOKEN = "..." # Your Relicate API token here os.environ\["REPLICATE\_API\_TOKEN"\] = REPLICATE\_API\_TOKEN

Perform Data Extraction from Tesla 10K file[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/llava_demo/#perform-data-extraction-from-tesla-10k-file)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

In these sections we use Unstructured to parse out the table and non-table elements.

### Extract Elements[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/llava_demo/#extract-elements)

We use Unstructured to extract table and non-table elements from the 10-K filing.

In \[ \]:

Copied!

!wget "https://www.dropbox.com/scl/fi/mlaymdy1ni1ovyeykhhuk/tesla\_2021\_10k.htm?rlkey=qf9k4zn0ejrbm716j0gg7r802&dl=1" \-O tesla\_2021\_10k.htm
!wget "https://docs.google.com/uc?export=download&id=1UU0xc3uLXs-WG0aDQSXjGacUkp142rLS" \-O texas.jpg

!wget "https://www.dropbox.com/scl/fi/mlaymdy1ni1ovyeykhhuk/tesla\_2021\_10k.htm?rlkey=qf9k4zn0ejrbm716j0gg7r802&dl=1" -O tesla\_2021\_10k.htm !wget "https://docs.google.com/uc?export=download&id=1UU0xc3uLXs-WG0aDQSXjGacUkp142rLS" -O texas.jpg

In \[ \]:

Copied!

from llama\_index.readers.file import FlatReader
from pathlib import Path
from llama\_index.core.node\_parser import UnstructuredElementNodeParser

reader \= FlatReader()
docs\_2021 \= reader.load\_data(Path("tesla\_2021\_10k.htm"))
node\_parser \= UnstructuredElementNodeParser()

from llama\_index.readers.file import FlatReader from pathlib import Path from llama\_index.core.node\_parser import UnstructuredElementNodeParser reader = FlatReader() docs\_2021 = reader.load\_data(Path("tesla\_2021\_10k.htm")) node\_parser = UnstructuredElementNodeParser()

In \[ \]:

Copied!

import openai

OPENAI\_API\_KEY \= "..."
openai.api\_key \= OPENAI\_API\_KEY  \# add your openai api key here
os.environ\["OPENAI\_API\_KEY"\] \= OPENAI\_API\_KEY

import openai OPENAI\_API\_KEY = "..." openai.api\_key = OPENAI\_API\_KEY # add your openai api key here os.environ\["OPENAI\_API\_KEY"\] = OPENAI\_API\_KEY

In \[ \]:

Copied!

import os
import pickle

if not os.path.exists("2021\_nodes.pkl"):
    raw\_nodes\_2021 \= node\_parser.get\_nodes\_from\_documents(docs\_2021)
    pickle.dump(raw\_nodes\_2021, open("2021\_nodes.pkl", "wb"))
else:
    raw\_nodes\_2021 \= pickle.load(open("2021\_nodes.pkl", "rb"))

import os import pickle if not os.path.exists("2021\_nodes.pkl"): raw\_nodes\_2021 = node\_parser.get\_nodes\_from\_documents(docs\_2021) pickle.dump(raw\_nodes\_2021, open("2021\_nodes.pkl", "wb")) else: raw\_nodes\_2021 = pickle.load(open("2021\_nodes.pkl", "rb"))

In \[ \]:

Copied!

nodes\_2021, objects\_2021 \= node\_parser.get\_nodes\_and\_objects(raw\_nodes\_2021)

nodes\_2021, objects\_2021 = node\_parser.get\_nodes\_and\_objects(raw\_nodes\_2021)

Setup Composable Retriever[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/llava_demo/#setup-composable-retriever)
-------------------------------------------------------------------------------------------------------------------------------

Now that we've extracted tables and their summaries, we can setup a composable retriever in LlamaIndex to query these tables.

### Construct Retrievers[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/llava_demo/#construct-retrievers)

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex

\# construct top-level vector index + query engine
vector\_index \= VectorStoreIndex(nodes\=nodes\_2021, objects\=objects\_2021)
query\_engine \= vector\_index.as\_query\_engine(similarity\_top\_k\=5, verbose\=True)

from llama\_index.core import VectorStoreIndex # construct top-level vector index + query engine vector\_index = VectorStoreIndex(nodes=nodes\_2021, objects=objects\_2021) query\_engine = vector\_index.as\_query\_engine(similarity\_top\_k=5, verbose=True)

In \[ \]:

Copied!

from PIL import Image
import matplotlib.pyplot as plt

imageUrl \= "./texas.jpg"
image \= Image.open(imageUrl).convert("RGB")

plt.figure(figsize\=(16, 5))
plt.imshow(image)

from PIL import Image import matplotlib.pyplot as plt imageUrl = "./texas.jpg" image = Image.open(imageUrl).convert("RGB") plt.figure(figsize=(16, 5)) plt.imshow(image)

Out\[ \]:

<matplotlib.image.AxesImage at 0x7f1b2e09b790>

![Image 4: No description has been provided for this image](blob:https://docs.llamaindex.ai/70ffa0e1389ed4610e1b780a607706a3)

### Running LLaVa model using Replicate through LlamaIndex for image understanding[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/llava_demo/#running-llava-model-using-replicate-through-llamaindex-for-image-understanding)

In \[ \]:

Copied!

from llama\_index.multi\_modal\_llms.replicate import ReplicateMultiModal
from llama\_index.core.schema import ImageDocument
from llama\_index.multi\_modal\_llms.replicate.base import (
    REPLICATE\_MULTI\_MODAL\_LLM\_MODELS,
)

print(imageUrl)

llava\_multi\_modal\_llm \= ReplicateMultiModal(
    model\=REPLICATE\_MULTI\_MODAL\_LLM\_MODELS\["llava-13b"\],
    max\_new\_tokens\=200,
    temperature\=0.1,
)

prompt \= "which Tesla factory is shown in the image? Please answer just the name of the factory."

llava\_response \= llava\_multi\_modal\_llm.complete(
    prompt\=prompt,
    image\_documents\=\[ImageDocument(image\_path\=imageUrl)\],
)

from llama\_index.multi\_modal\_llms.replicate import ReplicateMultiModal from llama\_index.core.schema import ImageDocument from llama\_index.multi\_modal\_llms.replicate.base import ( REPLICATE\_MULTI\_MODAL\_LLM\_MODELS, ) print(imageUrl) llava\_multi\_modal\_llm = ReplicateMultiModal( model=REPLICATE\_MULTI\_MODAL\_LLM\_MODELS\["llava-13b"\], max\_new\_tokens=200, temperature=0.1, ) prompt = "which Tesla factory is shown in the image? Please answer just the name of the factory." llava\_response = llava\_multi\_modal\_llm.complete( prompt=prompt, image\_documents=\[ImageDocument(image\_path=imageUrl)\], )

./texas.jpg

In \[ \]:

Copied!

print(llava\_response.text)

print(llava\_response.text)

Gigafactory

### Retrieve relevant information from LlamaIndex knowledge base based on LLaVa image understanding to augment `Image Captioning`[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/llava_demo/#retrieve-relevant-information-from-llamaindex-knowledge-base-based-on-llava-image-understanding-to-augment-image-captioning)

In \[ \]:

Copied!

rag\_response \= query\_engine.query(llava\_response.text)

rag\_response = query\_engine.query(llava\_response.text)

In \[ \]:

Copied!

print(rag\_response)

print(rag\_response)

Gigafactory is a term used by Tesla to describe its expansive manufacturing facilities that are strategically located in various regions worldwide. These factories are specifically designed to produce a range of Tesla products, including electric vehicles, battery cells, and energy storage solutions. Currently, Tesla operates Gigafactories in Nevada, New York, Shanghai, and Berlin, with plans to establish another one in Texas. The primary objective of these Gigafactories is to significantly enhance Tesla's production capabilities, drive down costs, and optimize operational efficiency across its manufacturing operations.

Multi-Modal Pydantic Program with LLaVa[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/llava_demo/#multi-modal-pydantic-program-with-llava)
---------------------------------------------------------------------------------------------------------------------------------------------------------

### Initialize the Instagram Ads Pydantic Class[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/llava_demo/#initialize-the-instagram-ads-pydantic-class)

In \[ \]:

Copied!

input\_image\_path \= Path("instagram\_images")
if not input\_image\_path.exists():
    Path.mkdir(input\_image\_path)

input\_image\_path = Path("instagram\_images") if not input\_image\_path.exists(): Path.mkdir(input\_image\_path)

In \[ \]:

Copied!

!wget "https://docs.google.com/uc?export=download&id=12ZpBBFkYu-jzz1iz356U5kMikn4uN9ww" \-O ./instagram\_images/jordan.png

!wget "https://docs.google.com/uc?export=download&id=12ZpBBFkYu-jzz1iz356U5kMikn4uN9ww" -O ./instagram\_images/jordan.png

Will not apply HSTS. The HSTS database must be a regular and non-world-writable file.
ERROR: could not open HSTS store at '/home/loganm/.wget-hsts'. HSTS will be disabled.
--2024-01-15 14:39:59--  https://docs.google.com/uc?export=download&id=12ZpBBFkYu-jzz1iz356U5kMikn4uN9ww
Resolving docs.google.com (docs.google.com)... 142.251.32.78, 2607:f8b0:400b:807::200e
Connecting to docs.google.com (docs.google.com)|142.251.32.78|:443... connected.
HTTP request sent, awaiting response... 303 See Other
Location: https://drive.usercontent.google.com/download?id=12ZpBBFkYu-jzz1iz356U5kMikn4uN9ww&export=download \[following\]
--2024-01-15 14:40:00--  https://drive.usercontent.google.com/download?id=12ZpBBFkYu-jzz1iz356U5kMikn4uN9ww&export=download
Resolving drive.usercontent.google.com (drive.usercontent.google.com)... 142.251.32.65, 2607:f8b0:400b:802::2001
Connecting to drive.usercontent.google.com (drive.usercontent.google.com)|142.251.32.65|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2722061 (2.6M) \[image/png\]
Saving to: ‘./instagram\_images/jordan.png’

./instagram\_images/ 100%\[ Jordan "6 Rings" shoe  Sneaker collecting ===

The shoes have had a large impact on the rise of "sneakerhead" culture. In the 1980s, collecting sneakers became more common, as well as trading and reselling them. As n...

![Image 7: No description has been provided for this image](blob:https://docs.llamaindex.ai/34a4f57d712e7488ed282b06d9d1ddfe)

### Synthesis the RAG results using retrieved texts and images[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/llava_demo/#synthesis-the-rag-results-using-retrieved-texts-and-images)

In \[ \]:

Copied!

from llama\_index.core import PromptTemplate
from llama\_index.core.query\_engine import SimpleMultiModalQueryEngine

qa\_tmpl\_str \= (
    "Context information is below.\\n"
    "---------------------\\n"
    "{context\_str}\\n"
    "---------------------\\n"
    "Given the context information and not prior knowledge, "
    "answer the query.\\n"
    "Query: {query\_str}\\n"
    "Answer: "
)
qa\_tmpl \= PromptTemplate(qa\_tmpl\_str)

query\_engine \= index.as\_query\_engine(
    llm\=llava\_multi\_modal\_llm,
    text\_qa\_template\=qa\_tmpl,
    similarity\_top\_k\=2,
    image\_similarity\_top\_k\=1,
)

query\_str \= "Tell me more about the " + pydantic\_response.brand + " brand."
response \= query\_engine.query(query\_str)

from llama\_index.core import PromptTemplate from llama\_index.core.query\_engine import SimpleMultiModalQueryEngine qa\_tmpl\_str = ( "Context information is below.\\n" "---------------------\\n" "{context\_str}\\n" "---------------------\\n" "Given the context information and not prior knowledge, " "answer the query.\\n" "Query: {query\_str}\\n" "Answer: " ) qa\_tmpl = PromptTemplate(qa\_tmpl\_str) query\_engine = index.as\_query\_engine( llm=llava\_multi\_modal\_llm, text\_qa\_template=qa\_tmpl, similarity\_top\_k=2, image\_similarity\_top\_k=1, ) query\_str = "Tell me more about the " + pydantic\_response.brand + " brand." response = query\_engine.query(query\_str)

In \[ \]:

Copied!

print(response)

print(response)

The Air Jordan brand is a line of basketball shoes produced by Nike, Inc. It was created for Michael Jordan, a basketball player who played for the Chicago Bulls during the 1980s and 1990s. The first Air Jordan shoe was released in 1985, and it has since become one of the most iconic and successful shoe lines in history. The shoes are known for their distinctive design, high-quality materials, and innovative technology, which has helped to establish the Air Jordan brand as a leader in the athletic footwear industry. The brand has also expanded to include apparel, accessories, and other products, and has become a cultural phenomenon, with a significant impact on fashion, music, and popular culture.

Back to top

[Previous Image to Image Retrieval using CLIP embedding and image correlation reasoning using GPT4V](https://docs.llamaindex.ai/en/stable/examples/multi_modal/image_to_image_retrieval/)[Next Retrieval-Augmented Image Captioning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/llava_multi_modal_tesla_10q/)

Hi, how can I help you?

🦙
