Title: Multimodal Ollama Cookbook - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/multi_modal/ollama_cookbook/

Markdown Content:
Multimodal Ollama Cookbook - LlamaIndex


[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/docs/examples/multi_modal/ollama_cookbook.ipynb)

This cookbook shows how you can build different multimodal RAG use cases with LLaVa on Ollama.

*   Structured Data Extraction from Images
*   Retrieval-Augmented Image Captioning
*   Multi-modal RAG

Setup Model[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/ollama_cookbook/#setup-model)
------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

!pip install llama\-index\-multi\-modal\-llms\-ollama
!pip install llama\-index\-readers\-file
!pip install unstructured
!pip install llama\-index\-embeddings\-huggingface
!pip install llama\-index\-vector\-stores\-qdrant
!pip install llama\-index\-embeddings\-clip

!pip install llama-index-multi-modal-llms-ollama !pip install llama-index-readers-file !pip install unstructured !pip install llama-index-embeddings-huggingface !pip install llama-index-vector-stores-qdrant !pip install llama-index-embeddings-clip

In \[ \]:

Copied!

from llama\_index.multi\_modal\_llms.ollama import OllamaMultiModal

from llama\_index.multi\_modal\_llms.ollama import OllamaMultiModal

In \[ \]:

Copied!

mm\_model \= OllamaMultiModal(model\="llava:13b")

mm\_model = OllamaMultiModal(model="llava:13b")

Structured Data Extraction from Images[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/ollama_cookbook/#structured-data-extraction-from-images)
------------------------------------------------------------------------------------------------------------------------------------------------------------

Here we show how to use LLaVa to extract information from an image into a structured Pydantic object.

We can do this via our `MultiModalLLMCompletionProgram`. It is instantiated with a prompt template, set of images you'd want to ask questions over, and the desired output Pydantic object.

### Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/ollama_cookbook/#load-data)

Let's first load an image ad for fried chicken.

In \[ \]:

Copied!

from pathlib import Path
from llama\_index.core import SimpleDirectoryReader
from PIL import Image
import matplotlib.pyplot as plt

input\_image\_path \= Path("restaurant\_images")
if not input\_image\_path.exists():
    Path.mkdir(input\_image\_path)

!wget "https://docs.google.com/uc?export=download&id=1GlqcNJhGGbwLKjJK1QJ\_nyswCTQ2K2Fq" \-O ./restaurant\_images/fried\_chicken.png

\# load as image documents
image\_documents \= SimpleDirectoryReader("./restaurant\_images").load\_data()

from pathlib import Path from llama\_index.core import SimpleDirectoryReader from PIL import Image import matplotlib.pyplot as plt input\_image\_path = Path("restaurant\_images") if not input\_image\_path.exists(): Path.mkdir(input\_image\_path) !wget "https://docs.google.com/uc?export=download&id=1GlqcNJhGGbwLKjJK1QJ\_nyswCTQ2K2Fq" -O ./restaurant\_images/fried\_chicken.png # load as image documents image\_documents = SimpleDirectoryReader("./restaurant\_images").load\_data()

In \[ \]:

Copied!

\# display image
imageUrl \= "./restaurant\_images/fried\_chicken.png"
image \= Image.open(imageUrl).convert("RGB")
plt.figure(figsize\=(16, 5))
plt.imshow(image)

\# display image imageUrl = "./restaurant\_images/fried\_chicken.png" image = Image.open(imageUrl).convert("RGB") plt.figure(figsize=(16, 5)) plt.imshow(image)

Out\[ \]:

<matplotlib.image.AxesImage at 0x3efdae470>

![Image 4: No description has been provided for this image](blob:https://docs.llamaindex.ai/bd4c5107f221fe3b5144a474883cfb74)

In \[ \]:

Copied!

from pydantic import BaseModel

class Restaurant(BaseModel):
    """Data model for an restaurant."""

    restaurant: str
    food: str
    discount: str
    price: str
    rating: str
    review: str

from pydantic import BaseModel class Restaurant(BaseModel): """Data model for an restaurant.""" restaurant: str food: str discount: str price: str rating: str review: str

In \[ \]:

Copied!

from llama\_index.core.program import MultiModalLLMCompletionProgram
from llama\_index.core.output\_parsers import PydanticOutputParser

prompt\_template\_str \= """\\
{query\_str}

Return the answer as a Pydantic object. The Pydantic schema is given below:

"""
mm\_program \= MultiModalLLMCompletionProgram.from\_defaults(
    output\_parser\=PydanticOutputParser(Restaurant),
    image\_documents\=image\_documents,
    prompt\_template\_str\=prompt\_template\_str,
    multi\_modal\_llm\=mm\_model,
    verbose\=True,
)

from llama\_index.core.program import MultiModalLLMCompletionProgram from llama\_index.core.output\_parsers import PydanticOutputParser prompt\_template\_str = """\\ {query\_str} Return the answer as a Pydantic object. The Pydantic schema is given below: """ mm\_program = MultiModalLLMCompletionProgram.from\_defaults( output\_parser=PydanticOutputParser(Restaurant), image\_documents=image\_documents, prompt\_template\_str=prompt\_template\_str, multi\_modal\_llm=mm\_model, verbose=True, )

In \[ \]:

Copied!

response \= mm\_program(query\_str\="Can you summarize what is in the image?")
for res in response:
    print(res)

response = mm\_program(query\_str="Can you summarize what is in the image?") for res in response: print(res)

\> Raw output:  \`\`\`
{
    "restaurant": "Buffalo Wild Wings",
    "food": "8 wings or chicken poppers",
    "discount": "20% discount on orders over $25",
    "price": "$8.73 each",
    "rating": "",
    "review": ""
}
\`\`\`
('restaurant', 'Buffalo Wild Wings')
('food', '8 wings or chicken poppers')
('discount', '20% discount on orders over $25')
('price', '$8.73 each')
('rating', '')
('review', '')

Retrieval-Augmented Image Captioning[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/ollama_cookbook/#retrieval-augmented-image-captioning)
--------------------------------------------------------------------------------------------------------------------------------------------------------

Here we show a simple example of a retrieval-augmented image captioning pipeline, expressed via our query pipeline syntax.

In \[ \]:

Copied!

!wget "https://www.dropbox.com/scl/fi/mlaymdy1ni1ovyeykhhuk/tesla\_2021\_10k.htm?rlkey=qf9k4zn0ejrbm716j0gg7r802&dl=1" \-O tesla\_2021\_10k.htm
!wget "https://docs.google.com/uc?export=download&id=1THe1qqM61lretr9N3BmINc\_NWDvuthYf" \-O shanghai.jpg

\# from llama\_index import SimpleDirectoryReader
from pathlib import Path
from llama\_index.readers.file import UnstructuredReader
from llama\_index.core.schema import ImageDocument

loader \= UnstructuredReader()
documents \= loader.load\_data(file\=Path("tesla\_2021\_10k.htm"))

image\_doc \= ImageDocument(image\_path\="./shanghai.jpg")

!wget "https://www.dropbox.com/scl/fi/mlaymdy1ni1ovyeykhhuk/tesla\_2021\_10k.htm?rlkey=qf9k4zn0ejrbm716j0gg7r802&dl=1" -O tesla\_2021\_10k.htm !wget "https://docs.google.com/uc?export=download&id=1THe1qqM61lretr9N3BmINc\_NWDvuthYf" -O shanghai.jpg # from llama\_index import SimpleDirectoryReader from pathlib import Path from llama\_index.readers.file import UnstructuredReader from llama\_index.core.schema import ImageDocument loader = UnstructuredReader() documents = loader.load\_data(file=Path("tesla\_2021\_10k.htm")) image\_doc = ImageDocument(image\_path="./shanghai.jpg")

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex
from llama\_index.core.embeddings import resolve\_embed\_model

embed\_model \= resolve\_embed\_model("local:BAAI/bge-m3")
vector\_index \= VectorStoreIndex.from\_documents(
    documents, embed\_model\=embed\_model
)
query\_engine \= vector\_index.as\_query\_engine()

from llama\_index.core import VectorStoreIndex from llama\_index.core.embeddings import resolve\_embed\_model embed\_model = resolve\_embed\_model("local:BAAI/bge-m3") vector\_index = VectorStoreIndex.from\_documents( documents, embed\_model=embed\_model ) query\_engine = vector\_index.as\_query\_engine()

In \[ \]:

Copied!

from llama\_index.core.prompts import PromptTemplate
from llama\_index.core.query\_pipeline import QueryPipeline, FnComponent

query\_prompt\_str \= """\\
Please expand the initial statement using the provided context from the Tesla 10K report.

{initial\_statement}

"""
query\_prompt\_tmpl \= PromptTemplate(query\_prompt\_str)

\# MM model --> query prompt --> query engine
qp \= QueryPipeline(
    modules\={
        "mm\_model": mm\_model.as\_query\_component(
            partial\={"image\_documents": \[image\_doc\]}
        ),
        "query\_prompt": query\_prompt\_tmpl,
        "query\_engine": query\_engine,
    },
    verbose\=True,
)
qp.add\_chain(\["mm\_model", "query\_prompt", "query\_engine"\])
rag\_response \= qp.run("Which Tesla Factory is shown in the image?")

from llama\_index.core.prompts import PromptTemplate from llama\_index.core.query\_pipeline import QueryPipeline, FnComponent query\_prompt\_str = """\\ Please expand the initial statement using the provided context from the Tesla 10K report. {initial\_statement} """ query\_prompt\_tmpl = PromptTemplate(query\_prompt\_str) # MM model --> query prompt --> query engine qp = QueryPipeline( modules={ "mm\_model": mm\_model.as\_query\_component( partial={"image\_documents": \[image\_doc\]} ), "query\_prompt": query\_prompt\_tmpl, "query\_engine": query\_engine, }, verbose=True, ) qp.add\_chain(\["mm\_model", "query\_prompt", "query\_engine"\]) rag\_response = qp.run("Which Tesla Factory is shown in the image?")

\> Running module mm\_model with input: 
prompt: Which Tesla Factory is shown in the image?

\> Running module query\_prompt with input: 
initial\_statement:  The image you've provided is a photograph of the Tesla Gigafactory, which is located in Shanghai, China. This facility is one of Tesla's large-scale production plants and is used for manufacturing el...

\> Running module query\_engine with input: 
input: Please expand the initial statement using the provided context from the Tesla 10K report.

 The image you've provided is a photograph of the Tesla Gigafactory, which is located in Shanghai, China. Thi...

In \[ \]:

Copied!

print(f"> Retrieval Augmented Response: {rag\_response}")

print(f"> Retrieval Augmented Response: {rag\_response}")

\> Retrieval Augmented Response: The Gigafactory Shanghai in China is an important manufacturing facility for Tesla. It was established to increase the affordability of Tesla vehicles for customers in local markets by reducing transportation and manufacturing costs and eliminating the impact of unfavorable tariffs. The factory allows Tesla to access high volumes of lithium-ion battery cells manufactured by their partner Panasonic, while achieving a significant reduction in the cost of their battery packs. Tesla continues to invest in Gigafactory Shanghai to achieve additional output. This factory is representative of Tesla's plan to improve their manufacturing operations as they establish new factories, incorporating the learnings from their previous ramp-ups.

In \[ \]:

Copied!

rag\_response.source\_nodes\[1\].get\_content()

rag\_response.source\_nodes\[1\].get\_content()

Out\[ \]:

'For example, we are currently constructing Gigafactory Berlin under conditional permits in anticipation of being granted final permits. Moreover, we will have to establish and ramp production of our proprietary battery cells and packs at our new factories, and we additionally intend to incorporate sequential design and manufacturing changes into vehicles manufactured at each new factory. We have limited experience to date with developing and implementing manufacturing innovations outside of the Fremont Factory and Gigafactory Shanghai. In particular, the majority of our design and engineering resources are currently located in California. In order to meet our expectations for our new factories, we must expand and manage localized design and engineering talent and resources. If we experience any issues or delays in meeting our projected timelines, costs, capital efficiency and production capacity for our new factories, expanding and managing teams to implement iterative design and production changes there, maintaining and complying with the terms of any debt financing that we obtain to fund them or generating and maintaining demand for the vehicles we manufacture there, our business, prospects, operating results and financial condition may be harmed.\\n\\nWe will need to maintain and significantly grow our access to battery cells, including through the development and manufacture of our own cells, and control our related costs.\\n\\nWe are dependent on the continued supply of lithium-ion battery cells for our vehicles and energy storage products, and we will require substantially more cells to grow our business according to our plans. Currently, we rely on suppliers such as Panasonic and Contemporary Amperex Technology Co. Limited (CATL) for these cells. We have to date fully qualified only a very limited number\\n\\n16\\n\\nof such suppliers and have limited flexibility in changing suppliers. Any disruption in the supply of battery cells from our suppliers could limit production of our vehicles and energy storage products. In the long term, we intend to supplement cells from our suppliers with cells manufactured by us, which we believe will be more efficient, manufacturable at greater volumes and more cost-effective than currently available cells. However, our efforts to develop and manufacture such battery cells have required, and may continue to require, significant investments, and there can be no assurance that we will be able to achieve these targets in the timeframes that we have planned or at all. If we are unable to do so, we may have to curtail our planned vehicle and energy storage product production or procure additional cells from suppliers at potentially greater costs, either of which may harm our business and operating results.\\n\\nIn addition, the cost of battery cells, whether manufactured by our suppliers or by us, depends in part upon the prices and availability of raw materials such as lithium, nickel, cobalt and/or other metals. The prices for these materials fluctuate and their available supply may be unstable, depending on market conditions and global demand for these materials, including as a result of increased global production of electric vehicles and energy storage products. Any reduced availability of these materials may impact our access to cells and any increases in their prices may reduce our profitability if we cannot recoup the increased costs through increased vehicle prices. Moreover, any such attempts to increase product prices may harm our brand, prospects and operating results.\\n\\nWe face strong competition for our products and services from a growing list of established and new competitors.\\n\\nThe worldwide automotive market is highly competitive today and we expect it will become even more so in the future. For example, Model 3 and Model Y face competition from existing and future automobile manufacturers in the extremely competitive entry-level premium sedan and compact SUV markets. A significant and growing number of established and new automobile manufacturers, as well as other companies, have entered, or are reported to have plans to enter, the market for electric and other alternative fuel vehicles, including hybrid, plug-in hybrid and fully electric vehicles, as well as the market for self-driving technology and other vehicle applications and software platforms. In some cases, our competitors offer or will offer electric vehicles in important markets such as China and Europe, and/or have announced an intention to produce electric vehicles exclusively at some point in the future. Many of our competitors have significantly greater or better-established resources than we do to devote to the design, development, manufacturing, distribution, promotion, sale and support of their products. Increased competition could result in our lower vehicle unit sales, price reductions, revenue shortfalls, loss of customers and loss of market share, which may harm our business, financial condition and operating results.\\n\\nWe also face competition in our energy generation and storage business from other manufacturers, developers, installers and service providers of competing energy technologies, as well as from large utilities. Decreases in the retail or wholesale prices of electricity from utilities or other renewable energy sources could make our products less attractive to customers and lead to an increased rate of residential customer defaults under our existing long-term leases and PPAs.'

Multi-Modal RAG[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/ollama_cookbook/#multi-modal-rag)
--------------------------------------------------------------------------------------------------------------

We index a set of images and text using a local CLIP embedding model. We can index them jointly via our `MultiModalVectorStoreIndex`

**NOTE**: The current implementation blends both images and text. You can and maybe should define separate indexes/retrievers for images and text, letting you use separate embedding/retrieval strategies for each modality).

#### Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/ollama_cookbook/#load-data)

If the `wget` command below doesn't work, manually download and unzip the file [here](https://drive.google.com/file/d/1qQDcaKuzgRGuEC1kxgYL_4mx7vG-v4gC/view?usp=sharing).

In \[ \]:

Copied!

!wget "https://drive.usercontent.google.com/download?id=1qQDcaKuzgRGuEC1kxgYL\_4mx7vG-v4gC&export=download&authuser=1&confirm=t&uuid=f944e95f-a31f-4b55-b68f-8ea67a6e90e5&at=APZUnTVZ6n1aOg7rtkcjBjw7Pt1D:1707010667927" \-O mixed\_wiki.zip

!wget "https://drive.usercontent.google.com/download?id=1qQDcaKuzgRGuEC1kxgYL\_4mx7vG-v4gC&export=download&authuser=1&confirm=t&uuid=f944e95f-a31f-4b55-b68f-8ea67a6e90e5&at=APZUnTVZ6n1aOg7rtkcjBjw7Pt1D:1707010667927" -O mixed\_wiki.zip

In \[ \]:

Copied!

!unzip mixed\_wiki.zip

!unzip mixed\_wiki.zip

In \[ \]:

Copied!

!wget "https://www.dropbox.com/scl/fi/mlaymdy1ni1ovyeykhhuk/tesla\_2021\_10k.htm?rlkey=qf9k4zn0ejrbm716j0gg7r802&dl=1" \-O ./mixed\_wiki/tesla\_2021\_10k.htm

!wget "https://www.dropbox.com/scl/fi/mlaymdy1ni1ovyeykhhuk/tesla\_2021\_10k.htm?rlkey=qf9k4zn0ejrbm716j0gg7r802&dl=1" -O ./mixed\_wiki/tesla\_2021\_10k.htm

### Build Multi-Modal Index[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/ollama_cookbook/#build-multi-modal-index)

This is a special index that jointly indexes both text documents and image documents.

We use a local CLIP model to embed images/text.

In \[ \]:

Copied!

from llama\_index.core.indices.multi\_modal.base import (
    MultiModalVectorStoreIndex,
)
from llama\_index.vector\_stores.qdrant import QdrantVectorStore
from llama\_index.core import SimpleDirectoryReader, StorageContext
from llama\_index.embeddings.clip import ClipEmbedding

import qdrant\_client
from llama\_index import (
    SimpleDirectoryReader,
)

\# Create a local Qdrant vector store
client \= qdrant\_client.QdrantClient(path\="qdrant\_mm\_db")

text\_store \= QdrantVectorStore(
    client\=client, collection\_name\="text\_collection"
)
image\_store \= QdrantVectorStore(
    client\=client, collection\_name\="image\_collection"
)
storage\_context \= StorageContext.from\_defaults(
    vector\_store\=text\_store, image\_store\=image\_store
)

image\_embed\_model \= ClipEmbedding()

\# Create the MultiModal index
documents \= SimpleDirectoryReader("./mixed\_wiki/").load\_data()
index \= MultiModalVectorStoreIndex.from\_documents(
    documents,
    storage\_context\=storage\_context,
    image\_embed\_model\=image\_embed\_model,
)

\# Save it
\# index.storage\_context.persist(persist\_dir="./storage")

\# # Load it
\# from llama\_index import load\_index\_from\_storage

\# storage\_context = StorageContext.from\_defaults(
\#     vector\_store=text\_store, persist\_dir="./storage"
\# )
\# index = load\_index\_from\_storage(storage\_context, image\_store=image\_store)

from llama\_index.core.indices.multi\_modal.base import ( MultiModalVectorStoreIndex, ) from llama\_index.vector\_stores.qdrant import QdrantVectorStore from llama\_index.core import SimpleDirectoryReader, StorageContext from llama\_index.embeddings.clip import ClipEmbedding import qdrant\_client from llama\_index import ( SimpleDirectoryReader, ) # Create a local Qdrant vector store client = qdrant\_client.QdrantClient(path="qdrant\_mm\_db") text\_store = QdrantVectorStore( client=client, collection\_name="text\_collection" ) image\_store = QdrantVectorStore( client=client, collection\_name="image\_collection" ) storage\_context = StorageContext.from\_defaults( vector\_store=text\_store, image\_store=image\_store ) image\_embed\_model = ClipEmbedding() # Create the MultiModal index documents = SimpleDirectoryReader("./mixed\_wiki/").load\_data() index = MultiModalVectorStoreIndex.from\_documents( documents, storage\_context=storage\_context, image\_embed\_model=image\_embed\_model, ) # Save it # index.storage\_context.persist(persist\_dir="./storage") # # Load it # from llama\_index import load\_index\_from\_storage # storage\_context = StorageContext.from\_defaults( # vector\_store=text\_store, persist\_dir="./storage" # ) # index = load\_index\_from\_storage(storage\_context, image\_store=image\_store)

In \[ \]:

Copied!

from llama\_index.core.prompts import PromptTemplate
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

query\_engine \= index.as\_query\_engine(llm\=mm\_model, text\_qa\_template\=qa\_tmpl)

query\_str \= "Tell me more about the Porsche"
response \= query\_engine.query(query\_str)

from llama\_index.core.prompts import PromptTemplate from llama\_index.core.query\_engine import SimpleMultiModalQueryEngine qa\_tmpl\_str = ( "Context information is below.\\n" "---------------------\\n" "{context\_str}\\n" "---------------------\\n" "Given the context information and not prior knowledge, " "answer the query.\\n" "Query: {query\_str}\\n" "Answer: " ) qa\_tmpl = PromptTemplate(qa\_tmpl\_str) query\_engine = index.as\_query\_engine(llm=mm\_model, text\_qa\_template=qa\_tmpl) query\_str = "Tell me more about the Porsche" response = query\_engine.query(query\_str)

In \[ \]:

Copied!

print(str(response))

print(str(response))

 The image shows a Porsche sports car displayed at an auto show. It appears to be the latest model, possibly the Taycan Cross Turismo or a similar variant, which is designed for off-road use and has raised suspension. This type of vehicle combines the performance of a sports car with the utility of an SUV, allowing it to handle rougher terrain and provide more cargo space than a traditional two-door sports car. The design incorporates sleek lines and aerodynamic elements typical of modern electric vehicles, which are often associated with luxury and high performance.

In \[ \]:

Copied!

from PIL import Image
import matplotlib.pyplot as plt
import os

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

from PIL import Image import matplotlib.pyplot as plt import os def plot\_images(image\_paths): images\_shown = 0 plt.figure(figsize=(16, 9)) for img\_path in image\_paths: if os.path.isfile(img\_path): image = Image.open(img\_path) plt.subplot(2, 3, images\_shown + 1) plt.imshow(image) plt.xticks(\[\]) plt.yticks(\[\]) images\_shown += 1 if images\_shown >= 9: break

In \[ \]:

Copied!

\# show sources
from llama\_index.core.response.notebook\_utils import display\_source\_node

for text\_node in response.metadata\["text\_nodes"\]:
    display\_source\_node(text\_node, source\_length\=200)
plot\_images(
    \[n.metadata\["file\_path"\] for n in response.metadata\["image\_nodes"\]\]
)

\# show sources from llama\_index.core.response.notebook\_utils import display\_source\_node for text\_node in response.metadata\["text\_nodes"\]: display\_source\_node(text\_node, source\_length=200) plot\_images( \[n.metadata\["file\_path"\] for n in response.metadata\["image\_nodes"\]\] )

**Node ID:** 3face2c9-3b86-4445-b21e-5b7fc9683adb  
**Similarity:** 0.8281288080117539  
**Text:**  The Porsche Mission E Cross Turismo previewed the Taycan Cross Turismo, and was presented at the 2018 Geneva Motor Show. The design language of the Mission E...

**Node ID:** ef43aa15-30b6-4f0f-bade-fd91f90bfd0b  
**Similarity:** 0.8281039313464207  
**Text:** The Porsche Taycan is a battery electric saloon and shooting brake produced by German automobile manufacturer Porsche. The concept version of the Taycan, named the Porsche Mission E, debuted at the...

![Image 5: No description has been provided for this image](blob:https://docs.llamaindex.ai/d28927bc3292cf4fb313afea1d4bd499)

Back to top

[Previous Multimodal RAG for processing videos using OpenAI GPT4V and LanceDB vectorstore](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_video_RAG/)[Next Multi-Modal LLM using OpenAI GPT-4V model for image reasoning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/openai_multi_modal/)

Hi, how can I help you?

🦙
