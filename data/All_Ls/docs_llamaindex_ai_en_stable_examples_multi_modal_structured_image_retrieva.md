Title: Semi-structured Image Retrieval - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/multi_modal/structured_image_retrieval/

Markdown Content:
Semi-structured Image Retrieval - LlamaIndex


In this notebook we show you how to perform semi-structured retrieval over images.

Given a set of images, we can infer structured outputs from them using Gemini Pro Vision.

We can then index these structured outputs in a vector database. We then take full advantage of semantic search + metadata filter capabilities with **auto-retrieval**: this allows us to ask both structured and semantic questions over this data!

(An alternative is to put this data into a SQL database, letting you do text-to-SQL. These techniques are quite closely related).

In \[ \]:

Copied!

%pip install llama\-index\-multi\-modal\-llms\-gemini
%pip install llama\-index\-vector\-stores\-qdrant
%pip install llama\-index\-embeddings\-gemini
%pip install llama\-index\-llms\-gemini

%pip install llama-index-multi-modal-llms-gemini %pip install llama-index-vector-stores-qdrant %pip install llama-index-embeddings-gemini %pip install llama-index-llms-gemini

In \[ \]:

Copied!

!pip install llama\-index 'google-generativeai>=0.3.0' matplotlib qdrant\_client

!pip install llama-index 'google-generativeai>=0.3.0' matplotlib qdrant\_client

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/structured_image_retrieval/#setup)
-----------------------------------------------------------------------------------------------------

### Get Google API Key[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/structured_image_retrieval/#get-google-api-key)

In \[ \]:

Copied!

import os

GOOGLE\_API\_KEY \= ""  \# add your GOOGLE API key here
os.environ\["GOOGLE\_API\_KEY"\] \= GOOGLE\_API\_KEY

import os GOOGLE\_API\_KEY = "" # add your GOOGLE API key here os.environ\["GOOGLE\_API\_KEY"\] = GOOGLE\_API\_KEY

### Download Images[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/structured_image_retrieval/#download-images)

We download the full SROIE v2 dataset from Kaggle [here](https://www.kaggle.com/datasets/urbikn/sroie-datasetv2).

This dataset consists of scanned receipt images. We ignore the ground-truth labels for now, and use the test set images to test out Gemini's capabilities for structured output extraction.

### Get Image Files[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/structured_image_retrieval/#get-image-files)

Now that the images are downloaded, we can get a list of the file names.

In \[ \]:

Copied!

from pathlib import Path
import random
from typing import Optional

from pathlib import Path import random from typing import Optional

In \[ \]:

Copied!

def get\_image\_files(
    dir\_path, sample: Optional\[int\] \= 10, shuffle: bool \= False
):
    dir\_path \= Path(dir\_path)
    image\_paths \= \[\]
    for image\_path in dir\_path.glob("\*.jpg"):
        image\_paths.append(image\_path)

    random.shuffle(image\_paths)
    if sample:
        return image\_paths\[:sample\]
    else:
        return image\_paths

def get\_image\_files( dir\_path, sample: Optional\[int\] = 10, shuffle: bool = False ): dir\_path = Path(dir\_path) image\_paths = \[\] for image\_path in dir\_path.glob("\*.jpg"): image\_paths.append(image\_path) random.shuffle(image\_paths) if sample: return image\_paths\[:sample\] else: return image\_paths

In \[ \]:

Copied!

image\_files \= get\_image\_files("SROIE2019/test/img", sample\=100)

image\_files = get\_image\_files("SROIE2019/test/img", sample=100)

Use Gemini to extract structured outputs[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/structured_image_retrieval/#use-gemini-to-extract-structured-outputs)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Here we use Gemini to extract structured outputs.

1.  Define a ReceiptInfo pydantic class that captures the structured outputs we want to extract. We extract fields like `company`, `date`, `total`, and also `summary`.
2.  Define a `pydantic_gemini` function which will convert input documents into a response.

### Define a ReceiptInfo pydantic class[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/structured_image_retrieval/#define-a-receiptinfo-pydantic-class)

In \[ \]:

Copied!

from pydantic import BaseModel, Field

class ReceiptInfo(BaseModel):
    company: str \= Field(..., description\="Company name")
    date: str \= Field(..., description\="Date field in DD/MM/YYYY format")
    address: str \= Field(..., description\="Address")
    total: float \= Field(..., description\="total amount")
    currency: str \= Field(
        ..., description\="Currency of the country (in abbreviations)"
    )
    summary: str \= Field(
        ...,
        description\="Extracted text summary of the receipt, including items purchased, the type of store, the location, and any other notable salient features (what does the purchase seem to be for?).",
    )

from pydantic import BaseModel, Field class ReceiptInfo(BaseModel): company: str = Field(..., description="Company name") date: str = Field(..., description="Date field in DD/MM/YYYY format") address: str = Field(..., description="Address") total: float = Field(..., description="total amount") currency: str = Field( ..., description="Currency of the country (in abbreviations)" ) summary: str = Field( ..., description="Extracted text summary of the receipt, including items purchased, the type of store, the location, and any other notable salient features (what does the purchase seem to be for?).", )

### Define a `pydantic_gemini` function[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/structured_image_retrieval/#define-a-pydantic_gemini-function)

In \[ \]:

Copied!

from llama\_index.multi\_modal\_llms.gemini import GeminiMultiModal
from llama\_index.core.program import MultiModalLLMCompletionProgram
from llama\_index.core.output\_parsers import PydanticOutputParser

prompt\_template\_str \= """\\
    Can you summarize the image and return a response \\
    with the following JSON format: \\
"""

async def pydantic\_gemini(output\_class, image\_documents, prompt\_template\_str):
    gemini\_llm \= GeminiMultiModal(
        api\_key\=GOOGLE\_API\_KEY, model\_name\="models/gemini-pro-vision"
    )

    llm\_program \= MultiModalLLMCompletionProgram.from\_defaults(
        output\_parser\=PydanticOutputParser(output\_class),
        image\_documents\=image\_documents,
        prompt\_template\_str\=prompt\_template\_str,
        multi\_modal\_llm\=gemini\_llm,
        verbose\=True,
    )

    response \= await llm\_program.acall()
    return response

from llama\_index.multi\_modal\_llms.gemini import GeminiMultiModal from llama\_index.core.program import MultiModalLLMCompletionProgram from llama\_index.core.output\_parsers import PydanticOutputParser prompt\_template\_str = """\\ Can you summarize the image and return a response \\ with the following JSON format: \\ """ async def pydantic\_gemini(output\_class, image\_documents, prompt\_template\_str): gemini\_llm = GeminiMultiModal( api\_key=GOOGLE\_API\_KEY, model\_name="models/gemini-pro-vision" ) llm\_program = MultiModalLLMCompletionProgram.from\_defaults( output\_parser=PydanticOutputParser(output\_class), image\_documents=image\_documents, prompt\_template\_str=prompt\_template\_str, multi\_modal\_llm=gemini\_llm, verbose=True, ) response = await llm\_program.acall() return response

### Run over images[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/structured_image_retrieval/#run-over-images)

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader
from llama\_index.core.async\_utils import run\_jobs

async def aprocess\_image\_file(image\_file):
    \# should load one file
    print(f"Image file: {image\_file}")
    img\_docs \= SimpleDirectoryReader(input\_files\=\[image\_file\]).load\_data()
    output \= await pydantic\_gemini(ReceiptInfo, img\_docs, prompt\_template\_str)
    return output

async def aprocess\_image\_files(image\_files):
    """Process metadata on image files."""

    new\_docs \= \[\]
    tasks \= \[\]
    for image\_file in image\_files:
        task \= aprocess\_image\_file(image\_file)
        tasks.append(task)

    outputs \= await run\_jobs(tasks, show\_progress\=True, workers\=5)
    return outputs

from llama\_index.core import SimpleDirectoryReader from llama\_index.core.async\_utils import run\_jobs async def aprocess\_image\_file(image\_file): # should load one file print(f"Image file: {image\_file}") img\_docs = SimpleDirectoryReader(input\_files=\[image\_file\]).load\_data() output = await pydantic\_gemini(ReceiptInfo, img\_docs, prompt\_template\_str) return output async def aprocess\_image\_files(image\_files): """Process metadata on image files.""" new\_docs = \[\] tasks = \[\] for image\_file in image\_files: task = aprocess\_image\_file(image\_file) tasks.append(task) outputs = await run\_jobs(tasks, show\_progress=True, workers=5) return outputs

In \[ \]:

Copied!

outputs \= await aprocess\_image\_files(image\_files)

outputs = await aprocess\_image\_files(image\_files)

In \[ \]:

Copied!

outputs\[4\]

outputs\[4\]

Out\[ \]:

ReceiptInfo(company='KEDAI BUKU NEW ACHIEVERS', date='15/09/2017', address='NO. 12 & 14, JALAN HIJAUAN JINANG 27/54 TAMAN ALAM MEGAH, SEKSYEN 27 40400 SHAH ALAM, SELANGOR D. E.', total=48.0, currency='MYR', summary='Purchase of books and school supplies at a bookstore.')

### Convert Structured Representation to `TextNode` objects[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/structured_image_retrieval/#convert-structured-representation-to-textnode-objects)

Node objects are the core units that are indexed in vector stores in LlamaIndex. We define a simple converter function to map the `ReceiptInfo` objects to `TextNode` objects.

In \[ \]:

Copied!

from llama\_index.core.schema import TextNode
from typing import List

def get\_nodes\_from\_objs(
    objs: List\[ReceiptInfo\], image\_files: List\[str\]
) \-> TextNode:
    """Get nodes from objects."""
    nodes \= \[\]
    for image\_file, obj in zip(image\_files, objs):
        node \= TextNode(
            text\=obj.summary,
            metadata\={
                "company": obj.company,
                "date": obj.date,
                "address": obj.address,
                "total": obj.total,
                "currency": obj.currency,
                "image\_file": str(image\_file),
            },
            excluded\_embed\_metadata\_keys\=\["image\_file"\],
            excluded\_llm\_metadata\_keys\=\["image\_file"\],
        )
        nodes.append(node)
    return nodes

from llama\_index.core.schema import TextNode from typing import List def get\_nodes\_from\_objs( objs: List\[ReceiptInfo\], image\_files: List\[str\] ) -> TextNode: """Get nodes from objects.""" nodes = \[\] for image\_file, obj in zip(image\_files, objs): node = TextNode( text=obj.summary, metadata={ "company": obj.company, "date": obj.date, "address": obj.address, "total": obj.total, "currency": obj.currency, "image\_file": str(image\_file), }, excluded\_embed\_metadata\_keys=\["image\_file"\], excluded\_llm\_metadata\_keys=\["image\_file"\], ) nodes.append(node) return nodes

In \[ \]:

Copied!

nodes \= get\_nodes\_from\_objs(outputs, image\_files)

nodes = get\_nodes\_from\_objs(outputs, image\_files)

In \[ \]:

Copied!

print(nodes\[0\].get\_content(metadata\_mode\="all"))

print(nodes\[0\].get\_content(metadata\_mode="all"))

company: UNIHAIKKA INTERNATIONAL SDN BHD
date: 13/09/2018
address: 12, Jalan Tampoi 7/4, Kawasan Perindustrian Tampoi, 81200 Johor Bahru, Johor
total: 8.85
currency: MYR
image\_file: SROIE2019/test/img/X51007846371.jpg

The receipt is from a restaurant called Bar Wang Rice. The total amount is 8.85 MYR. The items purchased include chicken, vegetables, and a drink.

### Index these nodes in vector stores[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/structured_image_retrieval/#index-these-nodes-in-vector-stores)

In \[ \]:

Copied!

import qdrant\_client
from llama\_index.vector\_stores.qdrant import QdrantVectorStore
from llama\_index.core import StorageContext
from llama\_index.core import VectorStoreIndex
from llama\_index.embeddings.gemini import GeminiEmbedding
from llama\_index.llms.gemini import Gemini
from llama\_index.core import Settings

\# Create a local Qdrant vector store
client \= qdrant\_client.QdrantClient(path\="qdrant\_gemini")

vector\_store \= QdrantVectorStore(client\=client, collection\_name\="collection")

\# global settings
Settings.embed\_model \= GeminiEmbedding(
    model\_name\="models/embedding-001", api\_key\=GOOGLE\_API\_KEY
)
Settings.llm \= (Gemini(api\_key\=GOOGLE\_API\_KEY),)

storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

index \= VectorStoreIndex(
    nodes\=nodes,
    storage\_context\=storage\_context,
)

import qdrant\_client from llama\_index.vector\_stores.qdrant import QdrantVectorStore from llama\_index.core import StorageContext from llama\_index.core import VectorStoreIndex from llama\_index.embeddings.gemini import GeminiEmbedding from llama\_index.llms.gemini import Gemini from llama\_index.core import Settings # Create a local Qdrant vector store client = qdrant\_client.QdrantClient(path="qdrant\_gemini") vector\_store = QdrantVectorStore(client=client, collection\_name="collection") # global settings Settings.embed\_model = GeminiEmbedding( model\_name="models/embedding-001", api\_key=GOOGLE\_API\_KEY ) Settings.llm = (Gemini(api\_key=GOOGLE\_API\_KEY),) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex( nodes=nodes, storage\_context=storage\_context, )

Define Auto-Retriever[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/structured_image_retrieval/#define-auto-retriever)
-------------------------------------------------------------------------------------------------------------------------------------

Now we can setup our auto-retriever, which can perform semi-structured queries: structured queries through inferring metadata filters, along with semantic search.

We setup our schema definition capturing the receipt info which is fed into the prompt.

In \[ \]:

Copied!

from llama\_index.core.vector\_stores import MetadataInfo, VectorStoreInfo

vector\_store\_info \= VectorStoreInfo(
    content\_info\="Receipts",
    metadata\_info\=\[
        MetadataInfo(
            name\="company",
            description\="The name of the store",
            type\="string",
        ),
        MetadataInfo(
            name\="address",
            description\="The address of the store",
            type\="string",
        ),
        MetadataInfo(
            name\="date",
            description\="The date of the purchase (in DD/MM/YYYY format)",
            type\="string",
        ),
        MetadataInfo(
            name\="total",
            description\="The final amount",
            type\="float",
        ),
        MetadataInfo(
            name\="currency",
            description\="The currency of the country the purchase was made (abbreviation)",
            type\="string",
        ),
    \],
)

from llama\_index.core.vector\_stores import MetadataInfo, VectorStoreInfo vector\_store\_info = VectorStoreInfo( content\_info="Receipts", metadata\_info=\[ MetadataInfo( name="company", description="The name of the store", type="string", ), MetadataInfo( name="address", description="The address of the store", type="string", ), MetadataInfo( name="date", description="The date of the purchase (in DD/MM/YYYY format)", type="string", ), MetadataInfo( name="total", description="The final amount", type="float", ), MetadataInfo( name="currency", description="The currency of the country the purchase was made (abbreviation)", type="string", ), \], )

In \[ \]:

Copied!

from llama\_index.core.retrievers import VectorIndexAutoRetriever

retriever \= VectorIndexAutoRetriever(
    index,
    vector\_store\_info\=vector\_store\_info,
    similarity\_top\_k\=2,
    empty\_query\_top\_k\=10,  \# if only metadata filters are specified, this is the limit
    verbose\=True,
)

from llama\_index.core.retrievers import VectorIndexAutoRetriever retriever = VectorIndexAutoRetriever( index, vector\_store\_info=vector\_store\_info, similarity\_top\_k=2, empty\_query\_top\_k=10, # if only metadata filters are specified, this is the limit verbose=True, )

In \[ \]:

Copied!

\# from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt
from IPython.display import Image

def display\_response(nodes: List\[TextNode\]):
    """Display response."""
    for node in nodes:
        print(node.get\_content(metadata\_mode\="all"))
        \# img = Image.open(open(node.metadata\["image\_file"\], 'rb'))
        display(Image(filename\=node.metadata\["image\_file"\], width\=200))

\# from PIL import Image import requests from io import BytesIO import matplotlib.pyplot as plt from IPython.display import Image def display\_response(nodes: List\[TextNode\]): """Display response.""" for node in nodes: print(node.get\_content(metadata\_mode="all")) # img = Image.open(open(node.metadata\["image\_file"\], 'rb')) display(Image(filename=node.metadata\["image\_file"\], width=200))

Run Some Queries[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/structured_image_retrieval/#run-some-queries)
---------------------------------------------------------------------------------------------------------------------------

Let's try out different types of queries!

In \[ \]:

Copied!

nodes \= retriever.retrieve(
    "Tell me about some restaurant orders of noodles with total < 25"
)
display\_response(nodes)

nodes = retriever.retrieve( "Tell me about some restaurant orders of noodles with total < 25" ) display\_response(nodes)

Using query str: restaurant orders of noodles
Using filters: \[('total', '<', 25)\]
company: Restoran Wan Sheng
date: 23-03-2018
address: No. 2, Jalan Temenggung 19/9, Seksyen 9, Bandar Mahkota Cheras, 43200 Cheras, Selangor
total: 6.7
currency: MYR
image\_file: SROIE2019/test/img/X51005711443.jpg

Teh (B), Cham (B), Bunga Kekwa, Take Away

![Image 3: No description has been provided for this image](blob:https://docs.llamaindex.ai/ed3524f26a782179c6d27906d59be0aa)

company: UNIHAIKKA INTERNATIONAL SDN BHD
date: 19/06/2018
address: 12, Jalan Tampoi 7/4, Kawasan Perindustrian Tampoi 81200 Johor Bahru, Johor
total: 8.45
currency: MYR
image\_file: SROIE2019/test/img/X51007846392.jpg

The receipt is from a restaurant called Bar Wang Rice. The total amount is 8.45 MYR. The items purchased include 1 plate of fried noodles, 1 plate of chicken, and 1 plate of vegetables.

![Image 4: No description has been provided for this image](blob:https://docs.llamaindex.ai/f388bbd7c8d71c75bb3264c4e23625c8)

In \[ \]:

Copied!

nodes \= retriever.retrieve("Tell me about some grocery purchases")
display\_response(nodes)

nodes = retriever.retrieve("Tell me about some grocery purchases") display\_response(nodes)

Using query str: grocery purchases
Using filters: \[\]
company: GARDENIA BAKERIES (KL) SDN BHD
date: 24/09/2017
address: LOT 3, JALAN PELABUR 23/1, 40300 SHAH ALAM, SELANGOR
total: 38.55
currency: RM
image\_file: SROIE2019/test/img/X51006556829.jpg

Purchase of groceries from a supermarket.

![Image 5: No description has been provided for this image](blob:https://docs.llamaindex.ai/cd9bcb645b36e2adb7d3155b77d0c5b8)

company: Segi Cash & Carry Sdn. Bhd
date: 02/02/2017
address: PT17920, SEKSYEN U9,
40150 SHAH ALAM,
SELANGOR DARUL EHSAN
total: 27.0
currency: RM
image\_file: SROIE2019/test/img/X51006335818.jpg

Purchase of groceries at Segi Cash & Carry Sdn. Bhd. on 02/02/2017. The total amount of the purchase is RM27.

![Image 6: No description has been provided for this image](blob:https://docs.llamaindex.ai/8276ee90456a5dda5af74525fc846b79)

Back to top

[Previous Multi-Modal LLM using Replicate LlaVa, Fuyu 8B, MiniGPT4 models for image reasoning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/replicate_multi_modal/)[Next Multi-Tenancy RAG with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/multi_tenancy/multi_tenancy_rag/)

Hi, how can I help you?

🦙
