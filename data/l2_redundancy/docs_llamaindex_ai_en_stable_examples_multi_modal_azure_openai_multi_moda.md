Title: Multi-Modal LLM using Azure OpenAI GPT-4V model for image reasoning

URL Source: https://docs.llamaindex.ai/en/stable/examples/multi_modal/azure_openai_multi_modal/

Markdown Content:
Multi-Modal LLM using Azure OpenAI GPT-4V model for image reasoning - LlamaIndex


In this notebook, we show how to use **Azure** OpenAI GPT4V MultiModal LLM class/abstraction for image understanding/reasoning. For a more complete example, please visit [this notebook](https://github.com/run-llama/llama_index/blob/main/docs/docs/examples/multi_modal/openai_multi_modal.ipynb).

In \[ \]:

Copied!

%pip install llama\-index\-multi\-modal\-llms\-azure\-openai

%pip install llama-index-multi-modal-llms-azure-openai

In \[ \]:

Copied!

!pip install openai

!pip install openai

Prerequisites[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/azure_openai_multi_modal/#prerequisites)
-------------------------------------------------------------------------------------------------------------------

1.  Setup an Azure subscription - you can create one for free [here](https://azure.microsoft.com/en-us/free/cognitive-services/)
2.  Apply for access to Azure OpenAI Service [here](https://customervoice.microsoft.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR7en2Ais5pxKtso_Pz4b1_xUOFA5Qk1UWDRBMjg0WFhPMkIzTzhKQ1dWNyQlQCN0PWcu)
3.  Create a resource in the Azure portal [here](https://portal.azure.com/?microsoft_azure_marketplace_ItemHideKey=microsoft_openai_tip#create/Microsoft.CognitiveServicesOpenAI)
4.  Deploy a model in Azure OpenAI Studio [here](https://oai.azure.com/)

You can find more details in [this guide.](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/create-resource?pivots=web-portal)

Note down the **"model name"** and **"deployment name"**, you'll need it when connecting to your LLM.

Use GPT4V to understand Images from URLs / base64[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/azure_openai_multi_modal/#use-gpt4v-to-understand-images-from-urls-base64)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

import os

os.environ\["AZURE\_OPENAI\_API\_KEY"\] \= "<your-api-key>"
os.environ\[
    "AZURE\_OPENAI\_ENDPOINT"
\] \= "https://<your-resource-name>.openai.azure.com/"
os.environ\["OPENAI\_API\_VERSION"\] \= "2023-12-01-preview"

import os os.environ\["AZURE\_OPENAI\_API\_KEY"\] = "" os.environ\[ "AZURE\_OPENAI\_ENDPOINT" \] = "https://.openai.azure.com/" os.environ\["OPENAI\_API\_VERSION"\] = "2023-12-01-preview"

Initialize `AzureOpenAIMultiModal` and Load Images from URLs[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/azure_openai_multi_modal/#initialize-azureopenaimultimodal-and-load-images-from-urls)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Unlike normal `OpenAI`, you need to pass a `engine` argument in addition to `model`. The `engine` is the name of your model deployment you selected in Azure OpenAI Studio.

In \[ \]:

Copied!

from llama\_index.multi\_modal\_llms.azure\_openai import AzureOpenAIMultiModal

from llama\_index.multi\_modal\_llms.azure\_openai import AzureOpenAIMultiModal

In \[ \]:

Copied!

azure\_openai\_mm\_llm \= AzureOpenAIMultiModal(
    engine\="gpt-4-vision-preview",
    api\_version\="2023-12-01-preview",
    model\="gpt-4-vision-preview",
    max\_new\_tokens\=300,
)

azure\_openai\_mm\_llm = AzureOpenAIMultiModal( engine="gpt-4-vision-preview", api\_version="2023-12-01-preview", model="gpt-4-vision-preview", max\_new\_tokens=300, )

Alternatively, you can also skip setting environment variables, and pass the parameters in directly via constructor.

In \[ \]:

Copied!

azure\_openai\_mm\_llm \= AzureOpenAIMultiModal(
    azure\_endpoint\="https://<your-endpoint>.openai.azure.com",
    engine\="gpt-4-vision-preview",
    api\_version\="2023-12-01-preview",
    model\="gpt-4-vision-preview",
    max\_new\_tokens\=300,
)

azure\_openai\_mm\_llm = AzureOpenAIMultiModal( azure\_endpoint="https://.openai.azure.com", engine="gpt-4-vision-preview", api\_version="2023-12-01-preview", model="gpt-4-vision-preview", max\_new\_tokens=300, )

In \[ \]:

Copied!

import base64
import requests
from llama\_index.core.schema import ImageDocument

image\_url \= "https://www.visualcapitalist.com/wp-content/uploads/2023/10/US\_Mortgage\_Rate\_Surge-Sept-11-1.jpg"

response \= requests.get(image\_url)
if response.status\_code != 200:
    raise ValueError("Error: Could not retrieve image from URL.")
base64str \= base64.b64encode(response.content).decode("utf-8")

image\_document \= ImageDocument(image\=base64str, image\_mimetype\="image/jpeg")

import base64 import requests from llama\_index.core.schema import ImageDocument image\_url = "https://www.visualcapitalist.com/wp-content/uploads/2023/10/US\_Mortgage\_Rate\_Surge-Sept-11-1.jpg" response = requests.get(image\_url) if response.status\_code != 200: raise ValueError("Error: Could not retrieve image from URL.") base64str = base64.b64encode(response.content).decode("utf-8") image\_document = ImageDocument(image=base64str, image\_mimetype="image/jpeg")

In \[ \]:

Copied!

from IPython.display import HTML

HTML(f'<img width=400 src="data:image/jpeg;base64,{base64str}"/>')

from IPython.display import HTML HTML(f'![Image 4: No description has been provided for this image](blob:https://docs.llamaindex.ai/750544a66affeaa0faa2b16cf8db037a)')

Out\[ \]:

![Image 5: No description has been provided for this image](blob:https://docs.llamaindex.ai/c810484b7e0e286f0b956672e08963cd)

### Complete a prompt with an image[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/azure_openai_multi_modal/#complete-a-prompt-with-an-image)

In \[ \]:

Copied!

complete\_response \= azure\_openai\_mm\_llm.complete(
    prompt\="Describe the images as an alternative text",
    image\_documents\=\[image\_document\],
)

complete\_response = azure\_openai\_mm\_llm.complete( prompt="Describe the images as an alternative text", image\_documents=\[image\_document\], )

In \[ \]:

Copied!

print(complete\_response)

print(complete\_response)

The image is a line graph showing the U.S. 30-year fixed-rate mortgage percentage rate and existing home sales from 2015 to 2021. The mortgage rate is represented by a red line, while the home sales are represented by a blue line. The graph shows that the mortgage rate has reached its highest level in over 20 years, while home sales have fluctuated over the same period. There is also a note that the data is sourced from the U.S. Federal Reserve, Trading Economics, and Visual Capitalist.

Back to top

[Previous Multi-Modal LLM using Anthropic model for image reasoning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/anthropic_multi_modal/)[Next Multi-Modal LLM using DashScope qwen-vl model for image reasoning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/dashscope_multi_modal/)

Hi, how can I help you?

🦙
