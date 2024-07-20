Title: Multi-Modal LLM using Anthropic model for image reasoning

URL Source: https://docs.llamaindex.ai/en/stable/examples/multi_modal/anthropic_multi_modal/

Markdown Content:
Multi-Modal LLM using Anthropic model for image reasoning - LlamaIndex


Anthropic has recently released its latest Multi modal models: Claude 3 Opus, Claude 3 Sonnet.

1.  Claude 3 Opus - claude-3-opus-20240229
    
2.  Claude 3 Sonnet - claude-3-sonnet-20240229
    

In this notebook, we show how to use Anthropic MultiModal LLM class/abstraction for image understanding/reasoning.

We also show several functions we are now supporting for Anthropic MultiModal LLM:

*   `complete` (both sync and async): for a single prompt and list of images
*   `chat` (both sync and async): for multiple chat messages
*   `stream complete` (both sync and async): for steaming output of complete
*   `stream chat` (both sync and async): for steaming output of chat

In \[ \]:

Copied!

!pip install llama\-index\-multi\-modal\-llms\-anthropic
!pip install llama\-index\-vector\-stores\-qdrant
!pip install matplotlib

!pip install llama-index-multi-modal-llms-anthropic !pip install llama-index-vector-stores-qdrant !pip install matplotlib

Use Anthropic to understand Images from Local directory[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/anthropic_multi_modal/#use-anthropic-to-understand-images-from-local-directory)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

import os

os.environ\["ANTHROPIC\_API\_KEY"\] \= ""  \# Your ANTHROPIC API key here

import os os.environ\["ANTHROPIC\_API\_KEY"\] = "" # Your ANTHROPIC API key here

In \[ \]:

Copied!

from PIL import Image
import matplotlib.pyplot as plt

img \= Image.open("../data/images/prometheus\_paper\_card.png")
plt.imshow(img)

from PIL import Image import matplotlib.pyplot as plt img = Image.open("../data/images/prometheus\_paper\_card.png") plt.imshow(img)

Out\[ \]:

<matplotlib.image.AxesImage at 0x10f4ee2d0>

![Image 4: No description has been provided for this image](blob:https://docs.llamaindex.ai/cac34f35b82e7abb3457c174e49b179e)

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader
from llama\_index.multi\_modal\_llms.anthropic import AnthropicMultiModal

\# put your local directore here
image\_documents \= SimpleDirectoryReader(
    input\_files\=\["../data/images/prometheus\_paper\_card.png"\]
).load\_data()

\# Initiated Anthropic MultiModal class
anthropic\_mm\_llm \= AnthropicMultiModal(max\_tokens\=300)

from llama\_index.core import SimpleDirectoryReader from llama\_index.multi\_modal\_llms.anthropic import AnthropicMultiModal # put your local directore here image\_documents = SimpleDirectoryReader( input\_files=\["../data/images/prometheus\_paper\_card.png"\] ).load\_data() # Initiated Anthropic MultiModal class anthropic\_mm\_llm = AnthropicMultiModal(max\_tokens=300)

In \[ \]:

Copied!

response \= anthropic\_mm\_llm.complete(
    prompt\="Describe the images as an alternative text",
    image\_documents\=image\_documents,
)

print(response)

response = anthropic\_mm\_llm.complete( prompt="Describe the images as an alternative text", image\_documents=image\_documents, ) print(response)

The image is a diagram titled "Prometheus: Inducing Fine-Grained Evaluation Capability In Language Models". It outlines the key components and workflow of the Prometheus system.

The main sections are:
1. Contributions: Describes Prometheus as an open-source LLM evaluator using custom rubrics and a feedback collection dataset.
2. Results: States that Prometheus matches or outperforms GPT-4 on 3 evaluation datasets and can function as a reward model. It also enabled reference answers for LM evaluations.
3. Insights: Notes that strong LLMs show high agreement with human evaluations but their close-to-source nature and uncontrolled versioning make them a less than ideal choice for LLM evaluation.
4. Technical Bits: Diagrams the Feedback Collection pipeline which uses GPT-4 to generate score rubrics and instructions, then collects human feedback to train the final Prometheus model.

The bottom includes logos, model details, and a small fire graphic. Overall, it provides a high-level technical overview of the Prometheus LLM evaluation system.

Use `AnthropicMultiModal` to reason images from URLs[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/anthropic_multi_modal/#use-anthropicmultimodal-to-reason-images-from-urls)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt
from llama\_index.core.multi\_modal\_llms.generic\_utils import load\_image\_urls

image\_urls \= \[
    "https://venturebeat.com/wp-content/uploads/2024/03/Screenshot-2024-03-04-at-12.49.41%E2%80%AFAM.png",
    \# Add yours here!
\]

img\_response \= requests.get(image\_urls\[0\])
img \= Image.open(BytesIO(img\_response.content))
plt.imshow(img)

image\_url\_documents \= load\_image\_urls(image\_urls)

from PIL import Image import requests from io import BytesIO import matplotlib.pyplot as plt from llama\_index.core.multi\_modal\_llms.generic\_utils import load\_image\_urls image\_urls = \[ "https://venturebeat.com/wp-content/uploads/2024/03/Screenshot-2024-03-04-at-12.49.41%E2%80%AFAM.png", # Add yours here! \] img\_response = requests.get(image\_urls\[0\]) img = Image.open(BytesIO(img\_response.content)) plt.imshow(img) image\_url\_documents = load\_image\_urls(image\_urls)

![Image 5: No description has been provided for this image](blob:https://docs.llamaindex.ai/abf8d29a265f5f3d4a16b62327480276)

In \[ \]:

Copied!

response \= anthropic\_mm\_llm.complete(
    prompt\="Describe the images as an alternative text",
    image\_documents\=image\_url\_documents,
)

print(response)

response = anthropic\_mm\_llm.complete( prompt="Describe the images as an alternative text", image\_documents=image\_url\_documents, ) print(response)

The image shows a table comparing the benchmark scores of various Claude 3 AI models (Opus, Sonnet, Haiku) against GPT-4, GPT-3.5, and two versions of Gemini (1.0 Ultra and 1.0 Pro) across different academic subjects and tests.

The subjects covered include undergraduate and graduate level knowledge, grade school math, math problem-solving, multilingual math, code, reasoning over text, mixed evaluations, knowledge Q&A, and common knowledge.

The scores are presented as percentages, except for the "Reasoning over text" row which shows raw scores out of a certain number of shots. The Claude 3 models generally perform comparably to GPT-3.5 and GPT-4 on most benchmarks, and outperform the Gemini models on the tasks where scores are available for comparison.

Structured Output Parsing from an Image[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/anthropic_multi_modal/#structured-output-parsing-from-an-image)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this section, we use our multi-modal Pydantic program to generate structured output from an image.

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

\# put your local directore here
image\_documents \= SimpleDirectoryReader(
    input\_files\=\["../data/images/ark\_email\_sample.PNG"\]
).load\_data()

from llama\_index.core import SimpleDirectoryReader # put your local directore here image\_documents = SimpleDirectoryReader( input\_files=\["../data/images/ark\_email\_sample.PNG"\] ).load\_data()

/Users/jerryliu/Programming/gpt\_index/.venv/lib/python3.10/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user\_install.html
  from .autonotebook import tqdm as notebook\_tqdm

In \[ \]:

Copied!

from PIL import Image
import matplotlib.pyplot as plt

img \= Image.open("../data/images/ark\_email\_sample.PNG")
plt.imshow(img)

from PIL import Image import matplotlib.pyplot as plt img = Image.open("../data/images/ark\_email\_sample.PNG") plt.imshow(img)

Out\[ \]:

<matplotlib.image.AxesImage at 0x2a629db40>

![Image 6: No description has been provided for this image](blob:https://docs.llamaindex.ai/9cf56523e964e24289d9d21741db300a)

In \[ \]:

Copied!

from pydantic import BaseModel
from typing import List

class TickerInfo(BaseModel):
    """List of ticker info."""

    direction: str
    ticker: str
    company: str
    shares\_traded: int
    percent\_of\_total\_etf: float

class TickerList(BaseModel):
    """List of stock tickers."""

    fund: str
    tickers: List\[TickerInfo\]

from pydantic import BaseModel from typing import List class TickerInfo(BaseModel): """List of ticker info.""" direction: str ticker: str company: str shares\_traded: int percent\_of\_total\_etf: float class TickerList(BaseModel): """List of stock tickers.""" fund: str tickers: List\[TickerInfo\]

In \[ \]:

Copied!

from llama\_index.multi\_modal\_llms.anthropic import AnthropicMultiModal
from llama\_index.core.program import MultiModalLLMCompletionProgram
from llama\_index.core.output\_parsers import PydanticOutputParser

prompt\_template\_str \= """\\
Can you get the stock information in the image \\
and return the answer? Pick just one fund. 

Make sure the answer is a JSON format corresponding to a Pydantic schema. The Pydantic schema is given below.

"""

\# Initiated Anthropic MultiModal class
anthropic\_mm\_llm \= AnthropicMultiModal(max\_tokens\=300)

llm\_program \= MultiModalLLMCompletionProgram.from\_defaults(
    output\_cls\=TickerList,
    image\_documents\=image\_documents,
    prompt\_template\_str\=prompt\_template\_str,
    multi\_modal\_llm\=anthropic\_mm\_llm,
    verbose\=True,
)

from llama\_index.multi\_modal\_llms.anthropic import AnthropicMultiModal from llama\_index.core.program import MultiModalLLMCompletionProgram from llama\_index.core.output\_parsers import PydanticOutputParser prompt\_template\_str = """\\ Can you get the stock information in the image \\ and return the answer? Pick just one fund. Make sure the answer is a JSON format corresponding to a Pydantic schema. The Pydantic schema is given below. """ # Initiated Anthropic MultiModal class anthropic\_mm\_llm = AnthropicMultiModal(max\_tokens=300) llm\_program = MultiModalLLMCompletionProgram.from\_defaults( output\_cls=TickerList, image\_documents=image\_documents, prompt\_template\_str=prompt\_template\_str, multi\_modal\_llm=anthropic\_mm\_llm, verbose=True, )

In \[ \]:

Copied!

response \= llm\_program()

response = llm\_program()

\> Raw output: {
  "fund": "ARKK",
  "tickers": \[
    {
      "direction": "Buy",
      "ticker": "TSLA",
      "company": "TESLA INC",
      "shares\_traded": 93664,
      "percent\_of\_total\_etf": 0.2453
    },
    {
      "direction": "Buy", 
      "ticker": "TXG",
      "company": "10X GENOMICS INC",
      "shares\_traded": 159506,
      "percent\_of\_total\_etf": 0.0907
    },
    {
      "direction": "Buy",
      "ticker": "CRSP",
      "company": "CRISPR THERAPEUTICS AG",
      "shares\_traded": 86268,
      "percent\_of\_total\_etf": 0.0669
    },
    {
      "direction": "Buy",
      "ticker": "RXRX",
      "company": "RECURSION PHARMACEUTICALS",
      "shares\_traded": 289619,
      "percent\_of\_total\_etf": 0.0391
    }
  \]
}

In \[ \]:

Copied!

print(str(response))

print(str(response))

fund='ARKK' tickers=\[TickerInfo(direction='Buy', ticker='TSLA', company='TESLA INC', shares\_traded=93664, percent\_of\_total\_etf=0.2453), TickerInfo(direction='Buy', ticker='TXG', company='10X GENOMICS INC', shares\_traded=159506, percent\_of\_total\_etf=0.0907), TickerInfo(direction='Buy', ticker='CRSP', company='CRISPR THERAPEUTICS AG', shares\_traded=86268, percent\_of\_total\_etf=0.0669), TickerInfo(direction='Buy', ticker='RXRX', company='RECURSION PHARMACEUTICALS', shares\_traded=289619, percent\_of\_total\_etf=0.0391)\]

Index into a Vector Store[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/anthropic_multi_modal/#index-into-a-vector-store)
----------------------------------------------------------------------------------------------------------------------------------------

In this section we show you how to use Claude 3 to build a RAG pipeline over image data. We first use Claude to extract text from a set of images. We then index the text with an embedding model. Finally, we build a query pipeline over the data.

In \[ \]:

Copied!

\# !wget "https://www.dropbox.com/scl/fi/pvxgohp5ts5mcj2js8drk/mixed\_wiki\_images\_small.zip?rlkey=3zf0z0n2etsjp19tofasaf4vy&dl=1" -O mixed\_wiki\_images\_small.zip
\# !wget "https://www.dropbox.com/scl/fi/vg2h92owduqmarwj7fxnc/mixed\_wiki\_images\_small.zip?rlkey=fejq570ehhil3qgv3gibaliqu&dl=1" -O mixed\_wiki\_images\_small.zip
!wget "https://www.dropbox.com/scl/fi/c1ec6osn0r2ggnitijqhl/mixed\_wiki\_images\_small.zip?rlkey=swwxc7h4qtwlnhmby5fsnderd&dl=1" \-O mixed\_wiki\_images\_small.zip
!unzip mixed\_wiki\_images\_small.zip

\# !wget "https://www.dropbox.com/scl/fi/pvxgohp5ts5mcj2js8drk/mixed\_wiki\_images\_small.zip?rlkey=3zf0z0n2etsjp19tofasaf4vy&dl=1" -O mixed\_wiki\_images\_small.zip # !wget "https://www.dropbox.com/scl/fi/vg2h92owduqmarwj7fxnc/mixed\_wiki\_images\_small.zip?rlkey=fejq570ehhil3qgv3gibaliqu&dl=1" -O mixed\_wiki\_images\_small.zip !wget "https://www.dropbox.com/scl/fi/c1ec6osn0r2ggnitijqhl/mixed\_wiki\_images\_small.zip?rlkey=swwxc7h4qtwlnhmby5fsnderd&dl=1" -O mixed\_wiki\_images\_small.zip !unzip mixed\_wiki\_images\_small.zip

In \[ \]:

Copied!

from llama\_index.multi\_modal\_llms.anthropic import AnthropicMultiModal

anthropic\_mm\_llm \= AnthropicMultiModal(max\_tokens\=300)

from llama\_index.multi\_modal\_llms.anthropic import AnthropicMultiModal anthropic\_mm\_llm = AnthropicMultiModal(max\_tokens=300)

In \[ \]:

Copied!

from llama\_index.core.schema import TextNode
from pathlib import Path
from llama\_index.core import SimpleDirectoryReader

nodes \= \[\]
for img\_file in Path("mixed\_wiki\_images\_small").glob("\*.png"):
    print(img\_file)
    \# put your local directore here
    image\_documents \= SimpleDirectoryReader(input\_files\=\[img\_file\]).load\_data()
    response \= anthropic\_mm\_llm.complete(
        prompt\="Describe the images as an alternative text",
        image\_documents\=image\_documents,
    )
    metadata \= {"img\_file": img\_file}
    nodes.append(TextNode(text\=str(response), metadata\=metadata))

from llama\_index.core.schema import TextNode from pathlib import Path from llama\_index.core import SimpleDirectoryReader nodes = \[\] for img\_file in Path("mixed\_wiki\_images\_small").glob("\*.png"): print(img\_file) # put your local directore here image\_documents = SimpleDirectoryReader(input\_files=\[img\_file\]).load\_data() response = anthropic\_mm\_llm.complete( prompt="Describe the images as an alternative text", image\_documents=image\_documents, ) metadata = {"img\_file": img\_file} nodes.append(TextNode(text=str(response), metadata=metadata))

mixed\_wiki\_images\_small/8.png
mixed\_wiki\_images\_small/14.png
mixed\_wiki\_images\_small/28.png
mixed\_wiki\_images\_small/15.png
mixed\_wiki\_images\_small/11.png
mixed\_wiki\_images\_small/10.png
mixed\_wiki\_images\_small/20.png
mixed\_wiki\_images\_small/23.png
mixed\_wiki\_images\_small/26.png
mixed\_wiki\_images\_small/19.png
mixed\_wiki\_images\_small/4.png
mixed\_wiki\_images\_small/5.png
mixed\_wiki\_images\_small/7.png
mixed\_wiki\_images\_small/6.png
mixed\_wiki\_images\_small/2.png

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, StorageContext
from llama\_index.embeddings.openai import OpenAIEmbedding
from llama\_index.llms.anthropic import Anthropic
from llama\_index.vector\_stores.qdrant import QdrantVectorStore
from llama\_index.core import Settings
from llama\_index.core import StorageContext
import qdrant\_client

\# Create a local Qdrant vector store
client \= qdrant\_client.QdrantClient(path\="qdrant\_mixed\_img")

vector\_store \= QdrantVectorStore(client\=client, collection\_name\="collection")

\# Using the embedding model to Gemini
embed\_model \= OpenAIEmbedding()
anthropic\_mm\_llm \= AnthropicMultiModal(max\_tokens\=300)

storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

index \= VectorStoreIndex(
    nodes\=nodes,
    storage\_context\=storage\_context,
)

from llama\_index.core import VectorStoreIndex, StorageContext from llama\_index.embeddings.openai import OpenAIEmbedding from llama\_index.llms.anthropic import Anthropic from llama\_index.vector\_stores.qdrant import QdrantVectorStore from llama\_index.core import Settings from llama\_index.core import StorageContext import qdrant\_client # Create a local Qdrant vector store client = qdrant\_client.QdrantClient(path="qdrant\_mixed\_img") vector\_store = QdrantVectorStore(client=client, collection\_name="collection") # Using the embedding model to Gemini embed\_model = OpenAIEmbedding() anthropic\_mm\_llm = AnthropicMultiModal(max\_tokens=300) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex( nodes=nodes, storage\_context=storage\_context, )

In \[ \]:

Copied!

from llama\_index.llms.anthropic import Anthropic

query\_engine \= index.as\_query\_engine(llm\=Anthropic())
response \= query\_engine.query("Tell me more about the porsche")

from llama\_index.llms.anthropic import Anthropic query\_engine = index.as\_query\_engine(llm=Anthropic()) response = query\_engine.query("Tell me more about the porsche")

In \[ \]:

Copied!

print(str(response))

print(str(response))

Unfortunately I cannot directly reference the provided context in my answer. However, from the details given, it appears there are images showing a white Porsche Taycan electric sports car. The Taycan seems to have a sleek, aerodynamic design with features like LED headlights, alloy wheels, and a full-width rear light bar. The photos show the Taycan parked indoors, likely a garage or showroom, as well as outdoors on a street in what looks like a residential area. Additional relevant details about the Porsche are not provided in the context, so I cannot elaborate further on the specific vehicle model or its characteristics. Please let me know if you have any other questions!

In \[ \]:

Copied!

from llama\_index.core.response.notebook\_utils import display\_source\_node

for n in response.source\_nodes:
    display\_source\_node(n, metadata\_mode\="all")

from llama\_index.core.response.notebook\_utils import display\_source\_node for n in response.source\_nodes: display\_source\_node(n, metadata\_mode="all")

**Node ID:** e04f2364-8fa2-413c-8d76-4981990e49b9  
**Similarity:** 0.83693930783145  
**Text:** img\_file: mixed\_wiki\_images\_small/11.png

The image shows a white Porsche Taycan Turbo electric s...

**Node ID:** e2de0d05-2e97-43bb-80dd-f28c4e9bcb28  
**Similarity:** 0.8357091967156951  
**Text:** img\_file: mixed\_wiki\_images\_small/2.png

The image shows a white Porsche Taycan electric sports c...

Back to top

[Previous Chroma Multi-Modal Demo with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/multi_modal/ChromaMultiModalDemo/)[Next Multi-Modal LLM using Azure OpenAI GPT-4V model for image reasoning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/azure_openai_multi_modal/)

Hi, how can I help you?

🦙
