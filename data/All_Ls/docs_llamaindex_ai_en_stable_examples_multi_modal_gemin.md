Title: Multi-Modal LLM using Google's Gemini model for image understanding and build Retrieval Augmented Generation with LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/multi_modal/gemini/

Markdown Content:
Multi-Modal LLM using Google's Gemini model for image understanding and build Retrieval Augmented Generation with LlamaIndex - LlamaIndex


In this notebook, we show how to use Google's Gemini Vision models for image understanding.

First, we show several functions we are now supporting for Gemini:

*   `complete` (both sync and async): for a single prompt and list of images
*   `chat` (both sync and async): for multiple chat messages
*   `stream complete` (both sync and async): for steaming output of complete
*   `stream chat` (both sync and async): for steaming output of chat

For the 2nd part of this notebook, we try to use `Gemini` + `Pydantic` to parse structured information for images from Google Maps.

*   Define the desired Pydantic class with attribution fields
*   Let `gemini-pro-vision` model understand each image and output structured results

For the 3rd part of this notebook, we propose using Gemini & LlamaIndex to build a simple `Retrieval Augmented Generation` Flow for a small Google Maps restaurant dataset.

*   Build vector index based on the structured outputs from Step 2
*   Using the `gemini-pro` model to synthesize the results and recommends restaurants based on user query.

Note: `google-generativeai` is only available for certain countries and regions.

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

Use Gemini to understand Images from URLs[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gemini/#use-gemini-to-understand-images-from-urls)
---------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

%env GOOGLE\_API\_KEY\=...

%env GOOGLE\_API\_KEY=...

In \[ \]:

Copied!

import os

GOOGLE\_API\_KEY \= ""  \# add your GOOGLE API key here
os.environ\["GOOGLE\_API\_KEY"\] \= GOOGLE\_API\_KEY

import os GOOGLE\_API\_KEY = "" # add your GOOGLE API key here os.environ\["GOOGLE\_API\_KEY"\] = GOOGLE\_API\_KEY

Initialize `GeminiMultiModal` and Load Images from URLs[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gemini/#initialize-geminimultimodal-and-load-images-from-urls)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.multi\_modal\_llms.gemini import GeminiMultiModal

from llama\_index.core.multi\_modal\_llms.generic\_utils import load\_image\_urls

image\_urls \= \[
    "https://storage.googleapis.com/generativeai-downloads/data/scene.jpg",
    \# Add yours here!
\]

image\_documents \= load\_image\_urls(image\_urls)

gemini\_pro \= GeminiMultiModal(model\_name\="models/gemini-pro-vision")

from llama\_index.multi\_modal\_llms.gemini import GeminiMultiModal from llama\_index.core.multi\_modal\_llms.generic\_utils import load\_image\_urls image\_urls = \[ "https://storage.googleapis.com/generativeai-downloads/data/scene.jpg", # Add yours here! \] image\_documents = load\_image\_urls(image\_urls) gemini\_pro = GeminiMultiModal(model\_name="models/gemini-pro-vision")

In \[ \]:

Copied!

from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt

img\_response \= requests.get(image\_urls\[0\])
print(image\_urls\[0\])
img \= Image.open(BytesIO(img\_response.content))
plt.imshow(img)

from PIL import Image import requests from io import BytesIO import matplotlib.pyplot as plt img\_response = requests.get(image\_urls\[0\]) print(image\_urls\[0\]) img = Image.open(BytesIO(img\_response.content)) plt.imshow(img)

https://storage.googleapis.com/generativeai-downloads/data/scene.jpg

Out\[ \]:

<matplotlib.image.AxesImage at 0x2a0699ed0>

![Image 4: No description has been provided for this image](blob:https://docs.llamaindex.ai/23143a12383305b445e8005d5a0b6a4c)

### Complete a prompt with a bunch of images[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gemini/#complete-a-prompt-with-a-bunch-of-images)

In \[ \]:

Copied!

complete\_response \= gemini\_pro.complete(
    prompt\="Identify the city where this photo was taken.",
    image\_documents\=image\_documents,
)

complete\_response = gemini\_pro.complete( prompt="Identify the city where this photo was taken.", image\_documents=image\_documents, )

In \[ \]:

Copied!

print(complete\_response)

print(complete\_response)

 New York City

### Steam Complete a prompt with a bunch of images[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gemini/#steam-complete-a-prompt-with-a-bunch-of-images)

In \[ \]:

Copied!

stream\_complete\_response \= gemini\_pro.stream\_complete(
    prompt\="Give me more context for this image",
    image\_documents\=image\_documents,
)

stream\_complete\_response = gemini\_pro.stream\_complete( prompt="Give me more context for this image", image\_documents=image\_documents, )

In \[ \]:

Copied!

for r in stream\_complete\_response:
    print(r.text, end\="")

for r in stream\_complete\_response: print(r.text, end="")

 This is an alleyway in New York City. It is between two tall buildings and there is a bridge going over the alleyway. The buildings are made of red brick and there are fire escapes on the buildings. The alleyway is empty except for a few trash cans.

### Async Complete[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gemini/#async-complete)

In \[ \]:

Copied!

response\_acomplete \= await gemini\_pro.acomplete(
    prompt\="Describe the images as an alternative text",
    image\_documents\=image\_documents,
)

response\_acomplete = await gemini\_pro.acomplete( prompt="Describe the images as an alternative text", image\_documents=image\_documents, )

In \[ \]:

Copied!

print(response\_acomplete)

print(response\_acomplete)

### Async Steam Complete[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gemini/#async-steam-complete)

In \[ \]:

Copied!

response\_astream\_complete \= await gemini\_pro.astream\_complete(
    prompt\="Describe the images as an alternative text",
    image\_documents\=image\_documents,
)

response\_astream\_complete = await gemini\_pro.astream\_complete( prompt="Describe the images as an alternative text", image\_documents=image\_documents, )

In \[ \]:

Copied!

async for delta in response\_astream\_complete:
    print(delta.text, end\="")

async for delta in response\_astream\_complete: print(delta.text, end="")

Complete with Two images[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gemini/#complete-with-two-images)
-----------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

image\_urls \= \[
    "https://www.sportsnet.ca/wp-content/uploads/2023/11/CP1688996471-1040x572.jpg",
    "https://res.cloudinary.com/hello-tickets/image/upload/c\_limit,f\_auto,q\_auto,w\_1920/v1640835927/o3pfl41q7m5bj8jardk0.jpg",
    \# "https://www.cleverfiles.com/howto/wp-content/uploads/2018/03/minion.jpg",
\]

image\_documents\_1 \= load\_image\_urls(image\_urls)

response\_multi \= gemini\_pro.complete(
    prompt\="is there any relationship between those images?",
    image\_documents\=image\_documents\_1,
)
print(response\_multi)

image\_urls = \[ "https://www.sportsnet.ca/wp-content/uploads/2023/11/CP1688996471-1040x572.jpg", "https://res.cloudinary.com/hello-tickets/image/upload/c\_limit,f\_auto,q\_auto,w\_1920/v1640835927/o3pfl41q7m5bj8jardk0.jpg", # "https://www.cleverfiles.com/howto/wp-content/uploads/2018/03/minion.jpg", \] image\_documents\_1 = load\_image\_urls(image\_urls) response\_multi = gemini\_pro.complete( prompt="is there any relationship between those images?", image\_documents=image\_documents\_1, ) print(response\_multi)

2nd Part: `Gemini` + `Pydantic` for Structured Output Parsing from an Image[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gemini/#2nd-part-gemini-pydantic-for-structured-output-parsing-from-an-image)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Leveraging Gemini for the image reasoning
*   Use Pydantic program to generate structured output from the image reasoning results of Gemini

In \[ \]:

Copied!

import google.generativeai as genai

genai.configure(
    api\_key\=GOOGLE\_API\_KEY,
    client\_options\={"api\_endpoint": "generativelanguage.googleapis.com"},
)

import google.generativeai as genai genai.configure( api\_key=GOOGLE\_API\_KEY, client\_options={"api\_endpoint": "generativelanguage.googleapis.com"}, )

List available Gemini Models from `google.generativeai`. Make sure your API key has access to belowing models

In \[ \]:

Copied!

for m in genai.list\_models():
    if "generateContent" in m.supported\_generation\_methods:
        print(m.name)

for m in genai.list\_models(): if "generateContent" in m.supported\_generation\_methods: print(m.name)

models/gemini-pro
models/gemini-pro-vision

### Download example images for Gemini to understand[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gemini/#download-example-images-for-gemini-to-understand)

In \[ \]:

Copied!

from pathlib import Path

input\_image\_path \= Path("google\_restaurants")
if not input\_image\_path.exists():
    Path.mkdir(input\_image\_path)

from pathlib import Path input\_image\_path = Path("google\_restaurants") if not input\_image\_path.exists(): Path.mkdir(input\_image\_path)

In \[ \]:

Copied!

!wget "https://docs.google.com/uc?export=download&id=1Pg04p6ss0FlBgz00noHAOAJ1EYXiosKg" \-O ./google\_restaurants/miami.png
!wget "https://docs.google.com/uc?export=download&id=1dYZy17bD6pSsEyACXx9fRMNx93ok-kTJ" \-O ./google\_restaurants/orlando.png
!wget "https://docs.google.com/uc?export=download&id=1ShPnYVc1iL\_TA1t7ErCFEAHT74-qvMrn" \-O ./google\_restaurants/sf.png
!wget "https://docs.google.com/uc?export=download&id=1WjISWnatHjwL4z5VD\_9o09ORWhRJuYqm" \-O ./google\_restaurants/toronto.png

!wget "https://docs.google.com/uc?export=download&id=1Pg04p6ss0FlBgz00noHAOAJ1EYXiosKg" -O ./google\_restaurants/miami.png !wget "https://docs.google.com/uc?export=download&id=1dYZy17bD6pSsEyACXx9fRMNx93ok-kTJ" -O ./google\_restaurants/orlando.png !wget "https://docs.google.com/uc?export=download&id=1ShPnYVc1iL\_TA1t7ErCFEAHT74-qvMrn" -O ./google\_restaurants/sf.png !wget "https://docs.google.com/uc?export=download&id=1WjISWnatHjwL4z5VD\_9o09ORWhRJuYqm" -O ./google\_restaurants/toronto.png

### Define the Pydantic Class for the Structured Parser[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gemini/#define-the-pydantic-class-for-the-structured-parser)

In \[ \]:

Copied!

from pydantic import BaseModel
from PIL import Image
import matplotlib.pyplot as plt

class GoogleRestaurant(BaseModel):
    """Data model for a Google Restaurant."""

    restaurant: str
    food: str
    location: str
    category: str
    hours: str
    price: str
    rating: float
    review: str
    description: str
    nearby\_tourist\_places: str

google\_image\_url \= "./google\_restaurants/miami.png"
image \= Image.open(google\_image\_url).convert("RGB")

plt.figure(figsize\=(16, 5))
plt.imshow(image)

from pydantic import BaseModel from PIL import Image import matplotlib.pyplot as plt class GoogleRestaurant(BaseModel): """Data model for a Google Restaurant.""" restaurant: str food: str location: str category: str hours: str price: str rating: float review: str description: str nearby\_tourist\_places: str google\_image\_url = "./google\_restaurants/miami.png" image = Image.open(google\_image\_url).convert("RGB") plt.figure(figsize=(16, 5)) plt.imshow(image)

Out\[ \]:

<matplotlib.image.AxesImage at 0x293e35210>

![Image 5: No description has been provided for this image](blob:https://docs.llamaindex.ai/bcf5b5c007e0f265bb8733de45e4aa9d)

### Call the Pydantic Program and Generate Structured Output[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gemini/#call-the-pydantic-program-and-generate-structured-output)

In \[ \]:

Copied!

from llama\_index.multi\_modal\_llms.gemini import GeminiMultiModal
from llama\_index.core.program import MultiModalLLMCompletionProgram
from llama\_index.core.output\_parsers import PydanticOutputParser

prompt\_template\_str \= """\\
    can you summarize what is in the image\\
    and return the answer with json format \\
"""

def pydantic\_gemini(
    model\_name, output\_class, image\_documents, prompt\_template\_str
):
    gemini\_llm \= GeminiMultiModal(
        api\_key\=GOOGLE\_API\_KEY, model\_name\=model\_name
    )

    llm\_program \= MultiModalLLMCompletionProgram.from\_defaults(
        output\_parser\=PydanticOutputParser(output\_class),
        image\_documents\=image\_documents,
        prompt\_template\_str\=prompt\_template\_str,
        multi\_modal\_llm\=gemini\_llm,
        verbose\=True,
    )

    response \= llm\_program()
    return response

from llama\_index.multi\_modal\_llms.gemini import GeminiMultiModal from llama\_index.core.program import MultiModalLLMCompletionProgram from llama\_index.core.output\_parsers import PydanticOutputParser prompt\_template\_str = """\\ can you summarize what is in the image\\ and return the answer with json format \\ """ def pydantic\_gemini( model\_name, output\_class, image\_documents, prompt\_template\_str ): gemini\_llm = GeminiMultiModal( api\_key=GOOGLE\_API\_KEY, model\_name=model\_name ) llm\_program = MultiModalLLMCompletionProgram.from\_defaults( output\_parser=PydanticOutputParser(output\_class), image\_documents=image\_documents, prompt\_template\_str=prompt\_template\_str, multi\_modal\_llm=gemini\_llm, verbose=True, ) response = llm\_program() return response

### Generate the Pydantic Structured Output via Gemini Vision Model[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gemini/#generate-the-pydantic-structured-output-via-gemini-vision-model)

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

google\_image\_documents \= SimpleDirectoryReader(
    "./google\_restaurants"
).load\_data()

results \= \[\]
for img\_doc in google\_image\_documents:
    pydantic\_response \= pydantic\_gemini(
        "models/gemini-pro-vision",
        GoogleRestaurant,
        \[img\_doc\],
        prompt\_template\_str,
    )
    \# only output the results for miami for example along with image
    if "miami" in img\_doc.image\_path:
        for r in pydantic\_response:
            print(r)
    results.append(pydantic\_response)

from llama\_index.core import SimpleDirectoryReader google\_image\_documents = SimpleDirectoryReader( "./google\_restaurants" ).load\_data() results = \[\] for img\_doc in google\_image\_documents: pydantic\_response = pydantic\_gemini( "models/gemini-pro-vision", GoogleRestaurant, \[img\_doc\], prompt\_template\_str, ) # only output the results for miami for example along with image if "miami" in img\_doc.image\_path: for r in pydantic\_response: print(r) results.append(pydantic\_response)

('restaurant', 'La Mar by Gaston Acurio')
('food', 'South American')
('location', '500 Brickell Key Dr, Miami, FL 33131')
('category', 'Restaurant')
('hours', 'Open ⋅ Closes 11 PM')
('price', 3.0)
('rating', 4)
('review', '4.4 (2,104)')
('description', 'Chic waterfront find offering Peruvian & fusion fare, plus bars for cocktails, ceviche & anticucho.')
('nearby\_tourist\_places', 'Brickell Key Park')

`Observation`:

*   Gemini perfectly generates all the meta information we need for the Pydantic class
*   It could also recognizes the nearby park from `Google Maps`

3rd Part: Build Multi-Modal RAG for Restaurant Recommendation[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gemini/#3rd-part-build-multi-modal-rag-for-restaurant-recommendation)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Our stack consists of Gemini + LlamaIndex + Pydantic structured output capabilities

### Construct Text Nodes for Building Vector Store. Store metadata and description for each restaurant.[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gemini/#construct-text-nodes-for-building-vector-store-store-metadata-and-description-for-each-restaurant)

In \[ \]:

Copied!

from llama\_index.core.schema import TextNode

nodes \= \[\]
for res in results:
    text\_node \= TextNode()
    metadata \= {}
    for r in res:
        \# set description as text of TextNode
        if r\[0\] \ "description": text\_node.text = r\[1\] else: metadata\[r\[0\]\] = r\[1\] text\_node.metadata = metadata nodes.append(text\_node)

### Using Gemini Embedding for building Vector Store for Dense retrieval. Index Restaurants as nodes into Vector Store[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gemini/#using-gemini-embedding-for-building-vector-store-for-dense-retrieval-index-restaurants-as-nodes-into-vector-store)

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, StorageContext
from llama\_index.embeddings.gemini import GeminiEmbedding
from llama\_index.llms.gemini import Gemini
from llama\_index.vector\_stores.qdrant import QdrantVectorStore
from llama\_index.core import Settings
from llama\_index.core import StorageContext
import qdrant\_client

\# Create a local Qdrant vector store
client \= qdrant\_client.QdrantClient(path\="qdrant\_gemini\_3")

vector\_store \= QdrantVectorStore(client\=client, collection\_name\="collection")

\# Using the embedding model to Gemini
Settings.embed\_model \= GeminiEmbedding(
    model\_name\="models/embedding-001", api\_key\=GOOGLE\_API\_KEY
)
Settings.llm \= Gemini(api\_key\=GOOGLE\_API\_KEY)

storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

index \= VectorStoreIndex(
    nodes\=nodes,
    storage\_context\=storage\_context,
)

from llama\_index.core import VectorStoreIndex, StorageContext from llama\_index.embeddings.gemini import GeminiEmbedding from llama\_index.llms.gemini import Gemini from llama\_index.vector\_stores.qdrant import QdrantVectorStore from llama\_index.core import Settings from llama\_index.core import StorageContext import qdrant\_client # Create a local Qdrant vector store client = qdrant\_client.QdrantClient(path="qdrant\_gemini\_3") vector\_store = QdrantVectorStore(client=client, collection\_name="collection") # Using the embedding model to Gemini Settings.embed\_model = GeminiEmbedding( model\_name="models/embedding-001", api\_key=GOOGLE\_API\_KEY ) Settings.llm = Gemini(api\_key=GOOGLE\_API\_KEY) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex( nodes=nodes, storage\_context=storage\_context, )

### Using Gemini to synthesize the results and recommend the restaurants to user[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gemini/#using-gemini-to-synthesize-the-results-and-recommend-the-restaurants-to-user)

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(
    similarity\_top\_k\=1,
)

response \= query\_engine.query(
    "recommend a Orlando restaurant for me and its nearby tourist places"
)
print(response)

query\_engine = index.as\_query\_engine( similarity\_top\_k=1, ) response = query\_engine.query( "recommend a Orlando restaurant for me and its nearby tourist places" ) print(response)

For a delightful dining experience, I recommend Mythos Restaurant, known for its American cuisine and unique underwater theme. Overlooking Universal Studios' Inland Sea, this restaurant offers a captivating ambiance. After your meal, explore the nearby tourist attractions such as Universal's Islands of Adventure, Skull Island: Reign of Kong, The Wizarding World of Harry Potter, Jurassic Park River Adventure, and Hollywood Rip Ride Rockit, all located near Mythos Restaurant.

Back to top

[Previous Multi-Modal LLM using DashScope qwen-vl model for image reasoning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/dashscope_multi_modal/)[Next Multimodal Structured Outputs: GPT-4o vs. Other GPT-4 Variants](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gpt4o_mm_structured_outputs/)

Hi, how can I help you?

🦙
