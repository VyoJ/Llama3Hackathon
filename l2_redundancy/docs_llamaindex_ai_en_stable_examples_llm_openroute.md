Title: OpenRouter - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/llm/openrouter/

Markdown Content:
OpenRouter - LlamaIndex


OpenRouter provides a standardized API to access many LLMs at the best price offered. You can find out more on their [homepage](https://openrouter.ai/).

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openrouter

%pip install llama-index-llms-openrouter

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

from llama\_index.llms.openrouter import OpenRouter
from llama\_index.core.llms import ChatMessage

from llama\_index.llms.openrouter import OpenRouter from llama\_index.core.llms import ChatMessage

Call `chat` with ChatMessage List[¶](https://docs.llamaindex.ai/en/stable/examples/llm/openrouter/#call-chat-with-chatmessage-list)
-----------------------------------------------------------------------------------------------------------------------------------

You need to either set env var `OPENROUTER_API_KEY` or set api\_key in the class constructor

In \[ \]:

Copied!

\# import os
\# os.environ\['OPENROUTER\_API\_KEY'\] = '<your-api-key>'

llm \= OpenRouter(
    api\_key\="<your-api-key>",
    max\_tokens\=256,
    context\_window\=4096,
    model\="gryphe/mythomax-l2-13b",
)

\# import os # os.environ\['OPENROUTER\_API\_KEY'\] = '' llm = OpenRouter( api\_key="", max\_tokens=256, context\_window=4096, model="gryphe/mythomax-l2-13b", )

In \[ \]:

Copied!

message \= ChatMessage(role\="user", content\="Tell me a joke")
resp \= llm.chat(\[message\])
print(resp)

message = ChatMessage(role="user", content="Tell me a joke") resp = llm.chat(\[message\]) print(resp)

assistant: Why did the tomato turn red? Because it saw the salad dressing!

### Streaming[¶](https://docs.llamaindex.ai/en/stable/examples/llm/openrouter/#streaming)

In \[ \]:

Copied!

message \= ChatMessage(role\="user", content\="Tell me a story in 250 words")
resp \= llm.stream\_chat(\[message\])
for r in resp:
    print(r.delta, end\="")

message = ChatMessage(role="user", content="Tell me a story in 250 words") resp = llm.stream\_chat(\[message\]) for r in resp: print(r.delta, end="")

Once upon a time, there was a young girl named Maria who lived in a small village surrounded by lush green forests. Maria was a kind and gentle soul, loved by everyone in the village. She spent most of her days exploring the forests, discovering new species of plants and animals, and helping the villagers with their daily chores.

One day, while Maria was out on a walk, she stumbled upon a hidden path she had never seen before. The path was overgrown with weeds and vines, but something about it called to her. She decided to follow it, and it led her deeper and deeper into the forest.

As she walked, the trees grew taller and the air grew colder. Maria began to feel a sense of unease, but she was determined to see where the path led. Finally, she came to a clearing, and in the center of it stood an enormous tree, its trunk as wide as a house.

Maria approached the tree and saw that it was covered in strange symbols. She reached out to touch one of the symbols, and suddenly, the tree began to glow. The glow grew brighter and brighter, until Maria

Call `complete` with Prompt[¶](https://docs.llamaindex.ai/en/stable/examples/llm/openrouter/#call-complete-with-prompt)
-----------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

resp \= llm.complete("Tell me a joke")
print(resp)

resp = llm.complete("Tell me a joke") print(resp)

Sure, here's a joke for you:

Why couldn't the bicycle stand up by itself?

Because it was two-tired!

I hope that brought a smile to your face!

In \[ \]:

Copied!

resp \= llm.stream\_complete("Tell me a story in 250 words")
for r in resp:
    print(r.delta, end\="")

resp = llm.stream\_complete("Tell me a story in 250 words") for r in resp: print(r.delta, end="")

Once upon a time, there was a young girl named Maria. She lived in a small village surrounded by lush green forests and sparkling rivers. Maria was a kind and gentle soul, loved by everyone in the village. She spent her days helping her parents with their farm work and exploring the surrounding nature.

One day, while wandering in the forest, Maria stumbled upon a hidden path she had never seen before. She decided to follow it, and it led her to a beautiful meadow filled with wildflowers. In the center of the meadow, she found a small pond, where she saw her own reflection in the water.

As she gazed into the pond, Maria saw a figure approaching her. It was a wise old woman, who introduced herself as the guardian of the meadow. The old woman told Maria that she had been chosen to receive a special gift, one that would bring her great joy and happiness.

The old woman then presented Maria with a small, delicate flower. She told her that this flower had the power to heal any wound, both physical and emotional. Maria was amazed and grateful, and she promised to use the flower wisely.

Model Configuration[¶](https://docs.llamaindex.ai/en/stable/examples/llm/openrouter/#model-configuration)
---------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

\# View options at https://openrouter.ai/models
\# This example uses Mistral's MoE, Mixtral:
llm \= OpenRouter(model\="mistralai/mixtral-8x7b-instruct")

\# View options at https://openrouter.ai/models # This example uses Mistral's MoE, Mixtral: llm = OpenRouter(model="mistralai/mixtral-8x7b-instruct")

In \[ \]:

Copied!

resp \= llm.complete("Write a story about a dragon who can code in Rust")
print(resp)

resp = llm.complete("Write a story about a dragon who can code in Rust") print(resp)

Back to top

[Previous OpenLLM](https://docs.llamaindex.ai/en/stable/examples/llm/openllm/)[Next OpenVINO LLMs](https://docs.llamaindex.ai/en/stable/examples/llm/openvino/)

Hi, how can I help you?

🦙
