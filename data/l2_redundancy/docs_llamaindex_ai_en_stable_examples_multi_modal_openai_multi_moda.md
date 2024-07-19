Title: Multi-Modal LLM using OpenAI GPT-4V model for image reasoning

URL Source: https://docs.llamaindex.ai/en/stable/examples/multi_modal/openai_multi_modal/

Markdown Content:
Multi-Modal LLM using OpenAI GPT-4V model for image reasoning - LlamaIndex


In this notebook, we show how to use OpenAI GPT4V MultiModal LLM class/abstraction for image understanding/reasoning.

We also show several functions we are now supporting for OpenAI GPT4V LLM:

*   `complete` (both sync and async): for a single prompt and list of images
*   `chat` (both sync and async): for multiple chat messages
*   `stream complete` (both sync and async): for steaming output of complete
*   `stream chat` (both sync and async): for steaming output of chat

In \[ \]:

Copied!

%pip install llama\-index\-multi\-modal\-llms\-openai

%pip install llama-index-multi-modal-llms-openai

In \[ \]:

Copied!

!pip install openai matplotlib

!pip install openai matplotlib

Use GPT4V to understand Images from URLs[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/openai_multi_modal/#use-gpt4v-to-understand-images-from-urls)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

import os

OPENAI\_API\_KEY \= "sk-"  \# Your OpenAI API token here
os.environ\["OPENAI\_API\_KEY"\] \= OPENAI\_API\_KEY

import os OPENAI\_API\_KEY = "sk-" # Your OpenAI API token here os.environ\["OPENAI\_API\_KEY"\] = OPENAI\_API\_KEY

Initialize `OpenAIMultiModal` and Load Images from URLs[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/openai_multi_modal/#initialize-openaimultimodal-and-load-images-from-urls)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/openai_multi_modal/#)
-----------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.multi\_modal\_llms.openai import OpenAIMultiModal

from llama\_index.core.multi\_modal\_llms.generic\_utils import load\_image\_urls

image\_urls \= \[
    \# "https://www.visualcapitalist.com/wp-content/uploads/2023/10/US\_Mortgage\_Rate\_Surge-Sept-11-1.jpg",
    \# "https://www.sportsnet.ca/wp-content/uploads/2023/11/CP1688996471-1040x572.jpg",
    "https://res.cloudinary.com/hello-tickets/image/upload/c\_limit,f\_auto,q\_auto,w\_1920/v1640835927/o3pfl41q7m5bj8jardk0.jpg",
    \# "https://www.cleverfiles.com/howto/wp-content/uploads/2018/03/minion.jpg",
\]

image\_documents \= load\_image\_urls(image\_urls)

openai\_mm\_llm \= OpenAIMultiModal(
    model\="gpt-4o", api\_key\=OPENAI\_API\_KEY, max\_new\_tokens\=300
)

from llama\_index.multi\_modal\_llms.openai import OpenAIMultiModal from llama\_index.core.multi\_modal\_llms.generic\_utils import load\_image\_urls image\_urls = \[ # "https://www.visualcapitalist.com/wp-content/uploads/2023/10/US\_Mortgage\_Rate\_Surge-Sept-11-1.jpg", # "https://www.sportsnet.ca/wp-content/uploads/2023/11/CP1688996471-1040x572.jpg", "https://res.cloudinary.com/hello-tickets/image/upload/c\_limit,f\_auto,q\_auto,w\_1920/v1640835927/o3pfl41q7m5bj8jardk0.jpg", # "https://www.cleverfiles.com/howto/wp-content/uploads/2018/03/minion.jpg", \] image\_documents = load\_image\_urls(image\_urls) openai\_mm\_llm = OpenAIMultiModal( model="gpt-4o", api\_key=OPENAI\_API\_KEY, max\_new\_tokens=300 )

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

https://res.cloudinary.com/hello-tickets/image/upload/c\_limit,f\_auto,q\_auto,w\_1920/v1640835927/o3pfl41q7m5bj8jardk0.jpg

Out\[ \]:

<matplotlib.image.AxesImage at 0x17ef8c7d0>

![Image 4: No description has been provided for this image](blob:https://docs.llamaindex.ai/e5f9d5cc70e3adc5ad94c014f602cb9b)

### Complete a prompt with a bunch of images[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/openai_multi_modal/#complete-a-prompt-with-a-bunch-of-images)

In \[ \]:

Copied!

complete\_response \= openai\_mm\_llm.complete(
    prompt\="Describe the images as an alternative text",
    image\_documents\=image\_documents,
)

complete\_response = openai\_mm\_llm.complete( prompt="Describe the images as an alternative text", image\_documents=image\_documents, )

In \[ \]:

Copied!

print(complete\_response)

print(complete\_response)

The image shows the Colosseum in Rome illuminated at night with the colors of the Italian flag: green, white, and red. The ancient amphitheater's multiple arches are vividly lit, contrasting with the dark blue sky in the background. Some construction or restoration work appears to be in progress at the base of the structure, and a few people can be seen walking near the site.

### Steam Complete a prompt with a bunch of images[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/openai_multi_modal/#steam-complete-a-prompt-with-a-bunch-of-images)

In \[ \]:

Copied!

stream\_complete\_response \= openai\_mm\_llm.stream\_complete(
    prompt\="give me more context for this image",
    image\_documents\=image\_documents,
)

stream\_complete\_response = openai\_mm\_llm.stream\_complete( prompt="give me more context for this image", image\_documents=image\_documents, )

In \[ \]:

Copied!

for r in stream\_complete\_response:
    print(r.delta, end\="")

for r in stream\_complete\_response: print(r.delta, end="")

This image shows the Colosseum, also known as the Flavian Amphitheatre, which is an iconic symbol of Imperial Rome and is located in the center of Rome, Italy. It is one of the world's most famous landmarks and is considered one of the greatest works of Roman architecture and engineering.

The Colosseum is illuminated at night with the colors of the Italian flag: green, white, and red. This lighting could be for a special occasion or event, such as a national holiday, a cultural celebration, or in solidarity with a cause. The use of lighting to display the national colors is a way to highlight the structure's significance to Italy and its people.

The Colosseum was built in the first century AD under the emperors of the Flavian dynasty and was used for gladiatorial contests and public spectacles such as mock sea battles, animal hunts, executions, re-enactments of famous battles, and dramas based on Classical mythology. It could hold between 50,000 and 80,000 spectators and was used for entertainment in the Roman Empire for over 400 years.

Today, the Colosseum is a major tourist attraction, drawing millions of visitors each year. It also serves as a powerful reminder of the Roman Empire's history and its lasting influence on the world.

### Chat through a list of chat messages[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/openai_multi_modal/#chat-through-a-list-of-chat-messages)

In \[ \]:

Copied!

from llama\_index.multi\_modal\_llms.openai.utils import (
    generate\_openai\_multi\_modal\_chat\_message,
)

chat\_msg\_1 \= generate\_openai\_multi\_modal\_chat\_message(
    prompt\="Describe the images as an alternative text",
    role\="user",
    image\_documents\=image\_documents,
)

chat\_msg\_2 \= generate\_openai\_multi\_modal\_chat\_message(
    prompt\="The image is a graph showing the surge in US mortgage rates. It is a visual representation of data, with a title at the top and labels for the x and y-axes. Unfortunately, without seeing the image, I cannot provide specific details about the data or the exact design of the graph.",
    role\="assistant",
)

chat\_msg\_3 \= generate\_openai\_multi\_modal\_chat\_message(
    prompt\="can I know more?",
    role\="user",
)

chat\_messages \= \[chat\_msg\_1, chat\_msg\_2, chat\_msg\_3\]
chat\_response \= openai\_mm\_llm.chat(
    \# prompt="Describe the images as an alternative text",
    messages\=chat\_messages,
)

from llama\_index.multi\_modal\_llms.openai.utils import ( generate\_openai\_multi\_modal\_chat\_message, ) chat\_msg\_1 = generate\_openai\_multi\_modal\_chat\_message( prompt="Describe the images as an alternative text", role="user", image\_documents=image\_documents, ) chat\_msg\_2 = generate\_openai\_multi\_modal\_chat\_message( prompt="The image is a graph showing the surge in US mortgage rates. It is a visual representation of data, with a title at the top and labels for the x and y-axes. Unfortunately, without seeing the image, I cannot provide specific details about the data or the exact design of the graph.", role="assistant", ) chat\_msg\_3 = generate\_openai\_multi\_modal\_chat\_message( prompt="can I know more?", role="user", ) chat\_messages = \[chat\_msg\_1, chat\_msg\_2, chat\_msg\_3\] chat\_response = openai\_mm\_llm.chat( # prompt="Describe the images as an alternative text", messages=chat\_messages, )

In \[ \]:

Copied!

for msg in chat\_messages:
    print(msg.role, msg.content)

for msg in chat\_messages: print(msg.role, msg.content)

MessageRole.USER \[{'type': 'text', 'text': 'Describe the images as an alternative text'}, {'type': 'image\_url', 'image\_url': 'https://res.cloudinary.com/hello-tickets/image/upload/c\_limit,f\_auto,q\_auto,w\_1920/v1640835927/o3pfl41q7m5bj8jardk0.jpg'}\]
MessageRole.ASSISTANT The image is a graph showing the surge in US mortgage rates. It is a visual representation of data, with a title at the top and labels for the x and y-axes. Unfortunately, without seeing the image, I cannot provide specific details about the data or the exact design of the graph.
MessageRole.USER can I know more?

In \[ \]:

Copied!

print(chat\_response)

print(chat\_response)

assistant: I apologize for the confusion earlier. The image actually shows the Colosseum in Rome, Italy, illuminated at night with the colors of the Italian flag: green, white, and red. The ancient amphitheater is captured in a twilight setting, with the sky transitioning from blue to black. The lighting accentuates the arches and the texture of the stone, creating a dramatic and colorful display. There are some people and a street visible in the foreground, with construction barriers indicating some ongoing work or preservation efforts.

### Stream Chat through a list of chat messages[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/openai_multi_modal/#stream-chat-through-a-list-of-chat-messages)

In \[ \]:

Copied!

stream\_chat\_response \= openai\_mm\_llm.stream\_chat(
    \# prompt="Describe the images as an alternative text",
    messages\=chat\_messages,
)

stream\_chat\_response = openai\_mm\_llm.stream\_chat( # prompt="Describe the images as an alternative text", messages=chat\_messages, )

In \[ \]:

Copied!

for r in stream\_chat\_response:
    print(r.delta, end\="")

for r in stream\_chat\_response: print(r.delta, end="")

I apologize for the confusion earlier. The image actually shows the Colosseum in Rome, Italy, illuminated at night with the colors of the Italian flag: green, white, and red. The ancient amphitheater is captured in a twilight setting, with the sky transitioning from blue to black. The lighting accentuates the arches and the texture of the stone, creating a dramatic and patriotic display. There are a few people visible at the base of the Colosseum, and some construction barriers suggest maintenance or archaeological work may be taking place.

### Async Complete[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/openai_multi_modal/#async-complete)

In \[ \]:

Copied!

response\_acomplete \= await openai\_mm\_llm.acomplete(
    prompt\="Describe the images as an alternative text",
    image\_documents\=image\_documents,
)

response\_acomplete = await openai\_mm\_llm.acomplete( prompt="Describe the images as an alternative text", image\_documents=image\_documents, )

In \[ \]:

Copied!

print(response\_acomplete)

print(response\_acomplete)

The image shows the Colosseum in Rome, Italy, illuminated at night with the colors of the Italian flag: green, white, and red. The ancient amphitheater's iconic arches are vividly lit, and the structure stands out against the dark blue evening sky. A few people can be seen near the base of the Colosseum, and there is some construction fencing visible in the foreground.

### Async Steam Complete[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/openai_multi_modal/#async-steam-complete)

In \[ \]:

Copied!

response\_astream\_complete \= await openai\_mm\_llm.astream\_complete(
    prompt\="Describe the images as an alternative text",
    image\_documents\=image\_documents,
)

response\_astream\_complete = await openai\_mm\_llm.astream\_complete( prompt="Describe the images as an alternative text", image\_documents=image\_documents, )

In \[ \]:

Copied!

async for delta in response\_astream\_complete:
    print(delta.delta, end\="")

async for delta in response\_astream\_complete: print(delta.delta, end="")

The image shows the Colosseum in Rome, Italy, illuminated at night with the colors of the Italian flag: green, white, and red. The ancient amphitheater's iconic arches are vividly lit, and the structure stands out against the dark blue evening sky. Some construction or restoration work appears to be in progress at the base of the Colosseum, indicated by scaffolding and barriers. A few individuals can be seen near the structure, giving a sense of scale to the massive edifice.

### Async Chat[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/openai_multi_modal/#async-chat)

In \[ \]:

Copied!

achat\_response \= await openai\_mm\_llm.achat(
    messages\=chat\_messages,
)

achat\_response = await openai\_mm\_llm.achat( messages=chat\_messages, )

In \[ \]:

Copied!

print(achat\_response)

print(achat\_response)

assistant: I apologize for the confusion in my previous response. Let me provide you with an accurate description of the image you've provided.

The image shows the Colosseum in Rome, Italy, illuminated at night with the colors of the Italian flag: green, white, and red. The ancient amphitheater is captured in a moment of twilight, with the sky transitioning from blue to black, highlighting the structure's iconic arches and the illuminated colors. There are some people and a street visible in the foreground, with construction barriers indicating some ongoing work or preservation efforts. The Colosseum's grandeur and historical significance are emphasized by the lighting and the dusk setting.

### Async stream Chat[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/openai_multi_modal/#async-stream-chat)

In \[ \]:

Copied!

astream\_chat\_response \= await openai\_mm\_llm.astream\_chat(
    messages\=chat\_messages,
)

astream\_chat\_response = await openai\_mm\_llm.astream\_chat( messages=chat\_messages, )

In \[ \]:

Copied!

async for delta in astream\_chat\_response:
    print(delta.delta, end\="")

async for delta in astream\_chat\_response: print(delta.delta, end="")

I apologize for the confusion in my previous response. The image actually depicts the Colosseum in Rome, Italy, illuminated at night with the colors of the Italian flag: green, white, and red. The ancient amphitheater is shown with its iconic arched openings, and the lighting accentuates its grandeur against the evening sky. There are a few people and some construction barriers visible at the base, indicating ongoing preservation efforts or public works.

Complete with Two images[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/openai_multi_modal/#complete-with-two-images)
-----------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

image\_urls \= \[
    "https://www.visualcapitalist.com/wp-content/uploads/2023/10/US\_Mortgage\_Rate\_Surge-Sept-11-1.jpg",
    "https://www.sportsnet.ca/wp-content/uploads/2023/11/CP1688996471-1040x572.jpg",
    \# "https://res.cloudinary.com/hello-tickets/image/upload/c\_limit,f\_auto,q\_auto,w\_1920/v1640835927/o3pfl41q7m5bj8jardk0.jpg",
    \# "https://www.cleverfiles.com/howto/wp-content/uploads/2018/03/minion.jpg",
\]

image\_documents\_1 \= load\_image\_urls(image\_urls)

response\_multi \= openai\_mm\_llm.complete(
    prompt\="is there any relationship between those images?",
    image\_documents\=image\_documents\_1,
)
print(response\_multi)

image\_urls = \[ "https://www.visualcapitalist.com/wp-content/uploads/2023/10/US\_Mortgage\_Rate\_Surge-Sept-11-1.jpg", "https://www.sportsnet.ca/wp-content/uploads/2023/11/CP1688996471-1040x572.jpg", # "https://res.cloudinary.com/hello-tickets/image/upload/c\_limit,f\_auto,q\_auto,w\_1920/v1640835927/o3pfl41q7m5bj8jardk0.jpg", # "https://www.cleverfiles.com/howto/wp-content/uploads/2018/03/minion.jpg", \] image\_documents\_1 = load\_image\_urls(image\_urls) response\_multi = openai\_mm\_llm.complete( prompt="is there any relationship between those images?", image\_documents=image\_documents\_1, ) print(response\_multi)

No, there is no direct relationship between these two images. The first image is an infographic showing the surge in U.S. mortgage rates and its comparison with existing home sales, indicating economic data. The second image is of a person holding a trophy, which seems to be related to a sports achievement or recognition. The content of the two images pertains to entirely different subjects—one is focused on economic information, while the other is related to an individual's achievement in a likely sporting context.

Use GPT4V to understand images from local files[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/openai_multi_modal/#use-gpt4v-to-understand-images-from-local-files)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

\# put your local directore here
image\_documents \= SimpleDirectoryReader("./images\_wiki").load\_data()

response \= openai\_mm\_llm.complete(
    prompt\="Describe the images as an alternative text",
    image\_documents\=image\_documents,
)

from llama\_index.core import SimpleDirectoryReader # put your local directore here image\_documents = SimpleDirectoryReader("./images\_wiki").load\_data() response = openai\_mm\_llm.complete( prompt="Describe the images as an alternative text", image\_documents=image\_documents, )

In \[ \]:

Copied!

from PIL import Image
import matplotlib.pyplot as plt

img \= Image.open("./images\_wiki/3.jpg")
plt.imshow(img)

from PIL import Image import matplotlib.pyplot as plt img = Image.open("./images\_wiki/3.jpg") plt.imshow(img)

Out\[ \]:

<matplotlib.image.AxesImage at 0x297eec110>

![Image 5: No description has been provided for this image](blob:https://docs.llamaindex.ai/a0285f81b957396ce56127c59d5c3501)

In \[ \]:

Copied!

print(response)

print(response)

You are looking at a close-up image of a glass Coca-Cola bottle. The label on the bottle features the iconic Coca-Cola logo with additional text underneath it commemorating the 2002 FIFA World Cup hosted by Korea/Japan. The label also indicates that the bottle contains 250 ml of the product. In the background with a shallow depth of field, you can see the blurred image of another Coca-Cola bottle, emphasizing the focus on the one in the foreground. The overall lighting and detail provide a clear view of the bottle and its labeling.

Back to top

[Previous Multimodal Ollama Cookbook](https://docs.llamaindex.ai/en/stable/examples/multi_modal/ollama_cookbook/)[Next Multi-Modal LLM using Replicate LlaVa, Fuyu 8B, MiniGPT4 models for image reasoning](https://docs.llamaindex.ai/en/stable/examples/multi_modal/replicate_multi_modal/)

Hi, how can I help you?

🦙
