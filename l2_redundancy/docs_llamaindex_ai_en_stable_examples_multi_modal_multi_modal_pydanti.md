Title: Multi-Modal GPT4V Pydantic Program - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_pydantic/

Markdown Content:
Multi-Modal GPT4V Pydantic Program - LlamaIndex


In this notebook, we show you how to generate `structured data` with new OpenAI GPT4V API via LlamaIndex. The user just needs to specify a Pydantic object.

We also compared several Large Vision models for this task:

*   GPT4-V
*   Fuyu-8B
*   MiniGPT-4
*   CogVLM
*   Llava-14B

Download Image Locally[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_pydantic/#download-image-locally)
---------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

%pip install llama\-index\-multi\-modal\-llms\-openai
%pip install llama\-index\-multi\-modal\-llms\-replicate

%pip install llama-index-multi-modal-llms-openai %pip install llama-index-multi-modal-llms-replicate

In \[ \]:

Copied!

import os

OPENAI\_API\_KEY \= "sk-<your-openai-api-token>"
os.environ\["OPENAI\_API\_KEY"\] \= OPENAI\_API\_KEY

import os OPENAI\_API\_KEY = "sk-" os.environ\["OPENAI\_API\_KEY"\] = OPENAI\_API\_KEY

In \[ \]:

Copied!

REPLICATE\_API\_TOKEN \= ""  \# Your Relicate API token here
os.environ\["REPLICATE\_API\_TOKEN"\] \= REPLICATE\_API\_TOKEN

REPLICATE\_API\_TOKEN = "" # Your Relicate API token here os.environ\["REPLICATE\_API\_TOKEN"\] = REPLICATE\_API\_TOKEN

In \[ \]:

Copied!

from pathlib import Path

input\_image\_path \= Path("restaurant\_images")
if not input\_image\_path.exists():
    Path.mkdir(input\_image\_path)

from pathlib import Path input\_image\_path = Path("restaurant\_images") if not input\_image\_path.exists(): Path.mkdir(input\_image\_path)

In \[ \]:

Copied!

!wget "https://docs.google.com/uc?export=download&id=1GlqcNJhGGbwLKjJK1QJ\_nyswCTQ2K2Fq" \-O ./restaurant\_images/fried\_chicken.png

!wget "https://docs.google.com/uc?export=download&id=1GlqcNJhGGbwLKjJK1QJ\_nyswCTQ2K2Fq" -O ./restaurant\_images/fried\_chicken.png

Initialize Pydantic Class for Restaurant[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_pydantic/#initialize-pydantic-class-for-restaurant)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

Load OpenAI GPT4V Multi-Modal LLM Model[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_pydantic/#load-openai-gpt4v-multi-modal-llm-model)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.multi\_modal\_llms.openai import OpenAIMultiModal
from llama\_index.core import SimpleDirectoryReader

\# put your local directory here
image\_documents \= SimpleDirectoryReader("./restaurant\_images").load\_data()

openai\_mm\_llm \= OpenAIMultiModal(
    model\="gpt-4o", api\_key\=OPENAI\_API\_KEY, max\_new\_tokens\=1000
)

from llama\_index.multi\_modal\_llms.openai import OpenAIMultiModal from llama\_index.core import SimpleDirectoryReader # put your local directory here image\_documents = SimpleDirectoryReader("./restaurant\_images").load\_data() openai\_mm\_llm = OpenAIMultiModal( model="gpt-4o", api\_key=OPENAI\_API\_KEY, max\_new\_tokens=1000 )

Plot the image[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_pydantic/#plot-the-image)
-----------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from PIL import Image
import matplotlib.pyplot as plt

imageUrl \= "./restaurant\_images/fried\_chicken.png"
image \= Image.open(imageUrl).convert("RGB")

plt.figure(figsize\=(16, 5))
plt.imshow(image)

from PIL import Image import matplotlib.pyplot as plt imageUrl = "./restaurant\_images/fried\_chicken.png" image = Image.open(imageUrl).convert("RGB") plt.figure(figsize=(16, 5)) plt.imshow(image)

Out\[ \]:

<matplotlib.image.AxesImage at 0x2a5cd06d0>

![Image 4: No description has been provided for this image](blob:https://docs.llamaindex.ai/6c7cf2a5f0195ce759bb501d091271b3)

Using Multi-Modal Pydantic Program to generate structured data from GPT4V Output for Restaurant Image[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_pydantic/#using-multi-modal-pydantic-program-to-generate-structured-data-from-gpt4v-output-for-restaurant-image)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core.program import MultiModalLLMCompletionProgram
from llama\_index.core.output\_parsers import PydanticOutputParser

prompt\_template\_str \= """\\
    can you summarize what is in the image\\
    and return the answer with json format \\
"""
openai\_program \= MultiModalLLMCompletionProgram.from\_defaults(
    output\_parser\=PydanticOutputParser(Restaurant),
    image\_documents\=image\_documents,
    prompt\_template\_str\=prompt\_template\_str,
    multi\_modal\_llm\=openai\_mm\_llm,
    verbose\=True,
)

from llama\_index.core.program import MultiModalLLMCompletionProgram from llama\_index.core.output\_parsers import PydanticOutputParser prompt\_template\_str = """\\ can you summarize what is in the image\\ and return the answer with json format \\ """ openai\_program = MultiModalLLMCompletionProgram.from\_defaults( output\_parser=PydanticOutputParser(Restaurant), image\_documents=image\_documents, prompt\_template\_str=prompt\_template\_str, multi\_modal\_llm=openai\_mm\_llm, verbose=True, )

In \[ \]:

Copied!

response \= openai\_program()
for res in response:
    print(res)

response = openai\_program() for res in response: print(res)

('restaurant', 'Not Specified')
('food', '8 Wings or Chicken Poppers')
('discount', 'Black Friday Offer')
('price', '$8.73')
('rating', 'Not Specified')
('review', 'Not Specified')

Test Pydantic for MiniGPT-4, Fuyu-8B, LLaVa-13B, CogVLM models[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_pydantic/#test-pydantic-for-minigpt-4-fuyu-8b-llava-13b-cogvlm-models)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.multi\_modal\_llms.replicate import ReplicateMultiModal
from llama\_index.multi\_modal\_llms.replicate.base import (
    REPLICATE\_MULTI\_MODAL\_LLM\_MODELS,
)

prompt\_template\_str \= """\\
    can you summarize what is in the image\\
    and return the answer with json format \\
"""

def pydantic\_replicate(
    model\_name, output\_class, image\_documents, prompt\_template\_str
):
    mm\_llm \= ReplicateMultiModal(
        model\=REPLICATE\_MULTI\_MODAL\_LLM\_MODELS\[model\_name\],
        temperature\=0.1,
        max\_new\_tokens\=1000,
    )

    llm\_program \= MultiModalLLMCompletionProgram.from\_defaults(
        output\_parser\=PydanticOutputParser(output\_class),
        image\_documents\=image\_documents,
        prompt\_template\_str\=prompt\_template\_str,
        multi\_modal\_llm\=mm\_llm,
        verbose\=True,
    )

    response \= llm\_program()
    print(f"Model: {model\_name}")
    for res in response:
        print(res)

from llama\_index.multi\_modal\_llms.replicate import ReplicateMultiModal from llama\_index.multi\_modal\_llms.replicate.base import ( REPLICATE\_MULTI\_MODAL\_LLM\_MODELS, ) prompt\_template\_str = """\\ can you summarize what is in the image\\ and return the answer with json format \\ """ def pydantic\_replicate( model\_name, output\_class, image\_documents, prompt\_template\_str ): mm\_llm = ReplicateMultiModal( model=REPLICATE\_MULTI\_MODAL\_LLM\_MODELS\[model\_name\], temperature=0.1, max\_new\_tokens=1000, ) llm\_program = MultiModalLLMCompletionProgram.from\_defaults( output\_parser=PydanticOutputParser(output\_class), image\_documents=image\_documents, prompt\_template\_str=prompt\_template\_str, multi\_modal\_llm=mm\_llm, verbose=True, ) response = llm\_program() print(f"Model: {model\_name}") for res in response: print(res)

### Using Fuyu-8B for Pydantic Strucured Output[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_pydantic/#using-fuyu-8b-for-pydantic-strucured-output)

In \[ \]:

Copied!

pydantic\_replicate("fuyu-8b", Restaurant, image\_documents, prompt\_template\_str)

pydantic\_replicate("fuyu-8b", Restaurant, image\_documents, prompt\_template\_str)

### Using LLaVa-13B for Pydantic Strucured Output[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_pydantic/#using-llava-13b-for-pydantic-strucured-output)

In \[ \]:

Copied!

pydantic\_replicate(
    "llava-13b", Restaurant, image\_documents, prompt\_template\_str
)

pydantic\_replicate( "llava-13b", Restaurant, image\_documents, prompt\_template\_str )

### Using MiniGPT-4 for Pydantic Strucured Output[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_pydantic/#using-minigpt-4-for-pydantic-strucured-output)

In \[ \]:

Copied!

pydantic\_replicate(
    "minigpt-4", Restaurant, image\_documents, prompt\_template\_str
)

pydantic\_replicate( "minigpt-4", Restaurant, image\_documents, prompt\_template\_str )

### Using CogVLM for Pydantic Strucured Output[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_pydantic/#using-cogvlm-for-pydantic-strucured-output)

In \[ \]:

Copied!

pydantic\_replicate("cogvlm", Restaurant, image\_documents, prompt\_template\_str)

pydantic\_replicate("cogvlm", Restaurant, image\_documents, prompt\_template\_str)

`Observation`:

*   Only GPT4-V works pretty well for this image pydantic task
*   Other vision model can output part fields

Change to Amazon Product Example[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_pydantic/#change-to-amazon-product-example)
-----------------------------------------------------------------------------------------------------------------------------------------------------

### Download the Amazon Product Image Screenshot[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_pydantic/#download-the-amazon-product-image-screenshot)

In \[ \]:

Copied!

input\_image\_path \= Path("amazon\_images")
if not input\_image\_path.exists():
    Path.mkdir(input\_image\_path)

input\_image\_path = Path("amazon\_images") if not input\_image\_path.exists(): Path.mkdir(input\_image\_path)

In \[ \]:

Copied!

!wget "https://docs.google.com/uc?export=download&id=1p1Y1qAoM68eC4sAvvHaiJyPhdUZS0Gqb" \-O ./amazon\_images/amazon.png

!wget "https://docs.google.com/uc?export=download&id=1p1Y1qAoM68eC4sAvvHaiJyPhdUZS0Gqb" -O ./amazon\_images/amazon.png

Initialize the Amazon Product Pydantic Class[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_pydantic/#initialize-the-amazon-product-pydantic-class)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from pydantic import BaseModel

class Product(BaseModel):
    """Data model for a Amazon Product."""

    title: str
    category: str
    discount: str
    price: str
    rating: str
    review: str
    description: str
    inventory: str

from pydantic import BaseModel class Product(BaseModel): """Data model for a Amazon Product.""" title: str category: str discount: str price: str rating: str review: str description: str inventory: str

### Plot the Image[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_pydantic/#plot-the-image)

In \[ \]:

Copied!

imageUrl \= "./amazon\_images/amazon.png"
image \= Image.open(imageUrl).convert("RGB")

plt.figure(figsize\=(16, 5))
plt.imshow(image)

imageUrl = "./amazon\_images/amazon.png" image = Image.open(imageUrl).convert("RGB") plt.figure(figsize=(16, 5)) plt.imshow(image)

Out\[ \]:

<matplotlib.image.AxesImage at 0x17b96e010>

![Image 5: No description has been provided for this image](blob:https://docs.llamaindex.ai/1d7bde547ecda71f266bbeb7c3fd1c5f)

Using Multi-Modal Pydantic Program to generate structured data from GPT4V Output for Amazon Product Image[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_pydantic/#using-multi-modal-pydantic-program-to-generate-structured-data-from-gpt4v-output-for-amazon-product-image)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

amazon\_image\_documents \= SimpleDirectoryReader("./amazon\_images").load\_data()

prompt\_template\_str \= """\\
    can you summarize what is in the image\\
    and return the answer with json format \\
"""
openai\_program\_amazon \= MultiModalLLMCompletionProgram.from\_defaults(
    output\_parser\=PydanticOutputParser(Product),
    image\_documents\=amazon\_image\_documents,
    prompt\_template\_str\=prompt\_template\_str,
    multi\_modal\_llm\=openai\_mm\_llm,
    verbose\=True,
)

amazon\_image\_documents = SimpleDirectoryReader("./amazon\_images").load\_data() prompt\_template\_str = """\\ can you summarize what is in the image\\ and return the answer with json format \\ """ openai\_program\_amazon = MultiModalLLMCompletionProgram.from\_defaults( output\_parser=PydanticOutputParser(Product), image\_documents=amazon\_image\_documents, prompt\_template\_str=prompt\_template\_str, multi\_modal\_llm=openai\_mm\_llm, verbose=True, )

In \[ \]:

Copied!

response \= openai\_program\_amazon()
for res in response:
    print(res)

response = openai\_program\_amazon() for res in response: print(res)

('title', 'Instant Vortex 5.7QT Air Fryer Oven Combo')
('category', 'Kitchen Appliances')
('discount', '20% off')
('price', '$151.20')
('rating', '4.7 out of 5 stars')
('review', '5086 ratings')
('description', '6-in-1 functionality; air fry, broil, bake, roast, reheat, and dehydrate. EvenCrisp Technology for crispy results. Easy to use touchscreen. Dishwasher safe parts. Cooks food faster and with less oil.')
('inventory', 'In stock')

Test Pydantic for MiniGPT-4, Fuyu-8B, LLaVa-13B, CogVLM models[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_pydantic/#test-pydantic-for-minigpt-4-fuyu-8b-llava-13b-cogvlm-models)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Using Fuyu-8B for Pydantic Strucured Output[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_pydantic/#using-fuyu-8b-for-pydantic-strucured-output)

In \[ \]:

Copied!

pydantic\_replicate(
    "fuyu-8b", Product, amazon\_image\_documents, prompt\_template\_str
)

pydantic\_replicate( "fuyu-8b", Product, amazon\_image\_documents, prompt\_template\_str )

### Using MiniGPT-4 for Pydantic Strucured Output[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_pydantic/#using-minigpt-4-for-pydantic-strucured-output)

In \[ \]:

Copied!

pydantic\_replicate(
    "minigpt-4", Product, amazon\_image\_documents, prompt\_template\_str
)

pydantic\_replicate( "minigpt-4", Product, amazon\_image\_documents, prompt\_template\_str )

### Using CogVLM-4 for Pydantic Strucured Output[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_pydantic/#using-cogvlm-4-for-pydantic-strucured-output)

In \[ \]:

Copied!

pydantic\_replicate(
    "cogvlm", Product, amazon\_image\_documents, prompt\_template\_str
)

pydantic\_replicate( "cogvlm", Product, amazon\_image\_documents, prompt\_template\_str )

Model: cogvlm
('title', 'Instant Vortex 5.7QT Air Fryer Oven Combo')
('category', 'Kitchen Appliances')
('discount', '20% off')
('price', '151.00')
('rating', '4.5 stars')
('review', "Amazon's Choice")
('description', 'Instant Vortex 5.7QT Air Fryer Oven Combo, From the Makers of Instant Pot, Customizable Smart Cooking Programs, Digital Touchscreen, Nonstick and Dishwasher Safe Basket, App with over 100 Recipes')
('inventory', 'In stock')

### Using LlaVa-13B for Pydantic Strucured Output[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_pydantic/#using-llava-13b-for-pydantic-strucured-output)

In \[ \]:

Copied!

pydantic\_replicate(
    "llava-13b", Product, amazon\_image\_documents, prompt\_template\_str
)

pydantic\_replicate( "llava-13b", Product, amazon\_image\_documents, prompt\_template\_str )

Model: llava-13b
('title', 'Instant Vortex 6.5 Qt Air Fryer Oven Combo')
('category', 'Kitchen Appliances')
('discount', '20% off')
('price', '$149.99')
('rating', '4.5 out of 5 stars')
('review', '500+ reviews')
('description', 'The Instant Vortex 6.5 Qt Air Fryer Oven Combo is a versatile and customizable small kitchen appliance that can air fry, bake, roast, broil, and dehydrate. It features a digital touchscreen, non-stick safe basket, and dishwasher safe basket, making it easy to use and clean. With over 1200 recipes, cooking programs, and digital touchscreen, this appliance is perfect for anyone looking to simplify their cooking routine.')
('inventory', 'In Stock')

`Observation`:

*   Only GPT4v, Llava-13B and GogVLM output desired fields
*   Among those 3 models, GPT4V get the most accurate results. Llava-13B and CogVLM got wrong price.

Initialize the Instagram Ads Pydantic Class and compare performance of different Multi-Modal LLMs[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_pydantic/#initialize-the-instagram-ads-pydantic-class-and-compare-performance-of-different-multi-modal-llms)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

In \[ \]:

Copied!

from pydantic import BaseModel

class InsAds(BaseModel):
    """Data model for a Ins Ads."""

    account: str
    brand: str
    product: str
    category: str
    discount: str
    price: str
    comments: str
    review: str
    description: str

from pydantic import BaseModel class InsAds(BaseModel): """Data model for a Ins Ads.""" account: str brand: str product: str category: str discount: str price: str comments: str review: str description: str

In \[ \]:

Copied!

from PIL import Image
import matplotlib.pyplot as plt

imageUrl \= "./instagram\_images/jordan.png"
image \= Image.open(imageUrl).convert("RGB")

plt.figure(figsize\=(16, 5))
plt.imshow(image)

from PIL import Image import matplotlib.pyplot as plt imageUrl = "./instagram\_images/jordan.png" image = Image.open(imageUrl).convert("RGB") plt.figure(figsize=(16, 5)) plt.imshow(image)

Out\[ \]:

<matplotlib.image.AxesImage at 0x16a722890>

![Image 6: No description has been provided for this image](blob:https://docs.llamaindex.ai/a2dffdb6e6bda341aa173dcf34704f46)

In \[ \]:

Copied!

ins\_image\_documents \= SimpleDirectoryReader("./instagram\_images").load\_data()

prompt\_template\_str \= """\\
    can you summarize what is in the image\\
    and return the answer with json format \\
"""
openai\_program\_ins \= MultiModalLLMCompletionProgram.from\_defaults(
    output\_parser\=PydanticOutputParser(InsAds),
    image\_documents\=ins\_image\_documents,
    prompt\_template\_str\=prompt\_template\_str,
    multi\_modal\_llm\=openai\_mm\_llm,
    verbose\=True,
)

response \= openai\_program\_ins()
for res in response:
    print(res)

ins\_image\_documents = SimpleDirectoryReader("./instagram\_images").load\_data() prompt\_template\_str = """\\ can you summarize what is in the image\\ and return the answer with json format \\ """ openai\_program\_ins = MultiModalLLMCompletionProgram.from\_defaults( output\_parser=PydanticOutputParser(InsAds), image\_documents=ins\_image\_documents, prompt\_template\_str=prompt\_template\_str, multi\_modal\_llm=openai\_mm\_llm, verbose=True, ) response = openai\_program\_ins() for res in response: print(res)

('account', 'jordansdaily')
('brand', 'Air Jordan')
('product', 'Air Jordan 2')
('category', 'Footwear')
('discount', 'None')
('price', '$175')
('comments', 'Liked by cemm2k and others')
('review', 'Not available')
('description', "Release date November 18th - Air Jordan 2 'Italy'")

In \[ \]:

Copied!

pydantic\_replicate("fuyu-8b", InsAds, ins\_image\_documents, prompt\_template\_str)

pydantic\_replicate("fuyu-8b", InsAds, ins\_image\_documents, prompt\_template\_str)

In \[ \]:

Copied!

pydantic\_replicate(
    "llava-13b", InsAds, ins\_image\_documents, prompt\_template\_str
)

pydantic\_replicate( "llava-13b", InsAds, ins\_image\_documents, prompt\_template\_str )

In \[ \]:

Copied!

pydantic\_replicate("cogvlm", InsAds, ins\_image\_documents, prompt\_template\_str)

pydantic\_replicate("cogvlm", InsAds, ins\_image\_documents, prompt\_template\_str)

Model: cogvlm
('account', 'jordansdaily')
('brand', 'AIR JORDAN')
('product', '2')
('category', 'ITALY')
('discount', '')
('price', '$175')
('comments', '')
('review', '')
('description', "AIR JORDAN 2 'ITALY' release NOV 18TH $175")

In \[ \]:

Copied!

pydantic\_replicate(
    "minigpt-4", InsAds, ins\_image\_documents, prompt\_template\_str
)

pydantic\_replicate( "minigpt-4", InsAds, ins\_image\_documents, prompt\_template\_str )

`Observation`:

*   Only GPT4v and GogVLM output desired fields
*   Among those 2 models, GPT4V gets more accurate results.

Back to top

[Previous \[Beta\] Multi-modal ReAct Agent](https://docs.llamaindex.ai/en/stable/examples/multi_modal/mm_agent/)[Next Multi-Modal RAG using Nomic Embed and Anthropic.](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_rag_nomic/)

Hi, how can I help you?

🦙
