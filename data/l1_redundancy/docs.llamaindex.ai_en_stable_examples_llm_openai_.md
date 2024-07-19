Title: OpenAI - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/llm/openai/

Markdown Content:
OpenAI - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai

%pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

Basic Usage[¶](https://docs.llamaindex.ai/en/stable/examples/llm/openai/#basic-usage)
-------------------------------------------------------------------------------------

#### Call `complete` with a prompt[¶](https://docs.llamaindex.ai/en/stable/examples/llm/openai/#call-complete-with-a-prompt)

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI

resp \= OpenAI().complete("Paul Graham is ")

from llama\_index.llms.openai import OpenAI resp = OpenAI().complete("Paul Graham is ")

In \[ \]:

Copied!

print(resp)

print(resp)

a computer scientist, entrepreneur, and venture capitalist. He is best known for co-founding the startup accelerator Y Combinator and for his influential essays on startups and technology. Graham has also founded several successful companies, including Viaweb (which was acquired by Yahoo) and the social news website Reddit. He is considered a thought leader in the tech industry and has been a vocal advocate for startup culture and innovation.

#### Call `chat` with a list of messages[¶](https://docs.llamaindex.ai/en/stable/examples/llm/openai/#call-chat-with-a-list-of-messages)

In \[ \]:

Copied!

from llama\_index.core.llms import ChatMessage
from llama\_index.llms.openai import OpenAI

messages \= \[
    ChatMessage(
        role\="system", content\="You are a pirate with a colorful personality"
    ),
    ChatMessage(role\="user", content\="What is your name"),
\]
resp \= OpenAI().chat(messages)

from llama\_index.core.llms import ChatMessage from llama\_index.llms.openai import OpenAI messages = \[ ChatMessage( role="system", content="You are a pirate with a colorful personality" ), ChatMessage(role="user", content="What is your name"), \] resp = OpenAI().chat(messages)

In \[ \]:

Copied!

print(resp)

print(resp)

assistant: Ahoy matey! The name's Captain Rainbowbeard, the most colorful pirate on the seven seas! What can I do for ye today? Arrr!

Streaming[¶](https://docs.llamaindex.ai/en/stable/examples/llm/openai/#streaming)
---------------------------------------------------------------------------------

Using `stream_complete` endpoint

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI

llm \= OpenAI()
resp \= llm.stream\_complete("Paul Graham is ")

from llama\_index.llms.openai import OpenAI llm = OpenAI() resp = llm.stream\_complete("Paul Graham is ")

In \[ \]:

Copied!

for r in resp:
    print(r.delta, end\="")

for r in resp: print(r.delta, end="")

a computer scientist, entrepreneur, and venture capitalist. He is best known for co-founding the startup accelerator Y Combinator and for his work on programming languages and web development. Graham is also a prolific writer and has published several influential essays on technology, startups, and entrepreneurship.

Using `stream_chat` endpoint

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI
from llama\_index.core.llms import ChatMessage

llm \= OpenAI()
messages \= \[
    ChatMessage(
        role\="system", content\="You are a pirate with a colorful personality"
    ),
    ChatMessage(role\="user", content\="What is your name"),
\]
resp \= llm.stream\_chat(messages)

from llama\_index.llms.openai import OpenAI from llama\_index.core.llms import ChatMessage llm = OpenAI() messages = \[ ChatMessage( role="system", content="You are a pirate with a colorful personality" ), ChatMessage(role="user", content="What is your name"), \] resp = llm.stream\_chat(messages)

In \[ \]:

Copied!

for r in resp:
    print(r.delta, end\="")

for r in resp: print(r.delta, end="")

Ahoy matey! The name's Captain Rainbowbeard! Aye, I be a pirate with a love for all things colorful and bright. Me beard be as vibrant as a rainbow, and me ship be the most colorful vessel on the seven seas! What can I do for ye today, me hearty?

Configure Model[¶](https://docs.llamaindex.ai/en/stable/examples/llm/openai/#configure-model)
---------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI

llm \= OpenAI(model\="gpt-3.5-turbo")

from llama\_index.llms.openai import OpenAI llm = OpenAI(model="gpt-3.5-turbo")

In \[ \]:

Copied!

resp \= llm.complete("Paul Graham is ")

resp = llm.complete("Paul Graham is ")

In \[ \]:

Copied!

print(resp)

print(resp)

Paul Graham is an entrepreneur, venture capitalist, and computer scientist. He is best known for his work in the startup world, having co-founded the accelerator Y Combinator and investing in hundreds of startups. He is also a prolific writer, having authored several books on topics such as startups, programming, and technology.

In \[ \]:

Copied!

messages \= \[
    ChatMessage(
        role\="system", content\="You are a pirate with a colorful personality"
    ),
    ChatMessage(role\="user", content\="What is your name"),
\]
resp \= llm.chat(messages)

messages = \[ ChatMessage( role="system", content="You are a pirate with a colorful personality" ), ChatMessage(role="user", content="What is your name"), \] resp = llm.chat(messages)

In \[ \]:

Copied!

print(resp)

print(resp)

assistant: 
My name is Captain Jack Sparrow.

Function Calling[¶](https://docs.llamaindex.ai/en/stable/examples/llm/openai/#function-calling)
-----------------------------------------------------------------------------------------------

OpenAI models have native support for function calling. This conveniently integrates with LlamaIndex tool abstractions, letting you plug in any arbitrary Python function to the LLM.

In the example below, we define a function to generate a Song object.

In \[ \]:

Copied!

from pydantic import BaseModel
from llama\_index.llms.openai.utils import to\_openai\_tool
from llama\_index.core.tools import FunctionTool

class Song(BaseModel):
    """A song with name and artist"""

    name: str
    artist: str

def generate\_song(name: str, artist: str) \-> Song:
    """Generates a song with provided name and artist."""
    return Song(name\=name, artist\=artist)

tool \= FunctionTool.from\_defaults(fn\=generate\_song)

from pydantic import BaseModel from llama\_index.llms.openai.utils import to\_openai\_tool from llama\_index.core.tools import FunctionTool class Song(BaseModel): """A song with name and artist""" name: str artist: str def generate\_song(name: str, artist: str) -> Song: """Generates a song with provided name and artist.""" return Song(name=name, artist=artist) tool = FunctionTool.from\_defaults(fn=generate\_song)

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI

llm \= OpenAI(model\="gpt-3.5-turbo")
response \= llm.predict\_and\_call(\[tool\], "Generate a song")
print(str(response))

from llama\_index.llms.openai import OpenAI llm = OpenAI(model="gpt-3.5-turbo") response = llm.predict\_and\_call(\[tool\], "Generate a song") print(str(response))

name='Sunshine' artist='John Smith'

We can also do multiple function calling.

In \[ \]:

Copied!

llm \= OpenAI(model\="gpt-3.5-turbo")
response \= llm.predict\_and\_call(
    \[tool\],
    "Generate five songs from the Beatles",
    allow\_parallel\_tool\_calls\=True,
)
for s in response.sources:
    print(f"Name: {s.tool\_name}, Input: {s.raw\_input}, Output: {str(s)}")

llm = OpenAI(model="gpt-3.5-turbo") response = llm.predict\_and\_call( \[tool\], "Generate five songs from the Beatles", allow\_parallel\_tool\_calls=True, ) for s in response.sources: print(f"Name: {s.tool\_name}, Input: {s.raw\_input}, Output: {str(s)}")

Name: generate\_song, Input: {'args': (), 'kwargs': {'name': 'Hey Jude', 'artist': 'The Beatles'}}, Output: name='Hey Jude' artist='The Beatles'
Name: generate\_song, Input: {'args': (), 'kwargs': {'name': 'Let It Be', 'artist': 'The Beatles'}}, Output: name='Let It Be' artist='The Beatles'
Name: generate\_song, Input: {'args': (), 'kwargs': {'name': 'Yesterday', 'artist': 'The Beatles'}}, Output: name='Yesterday' artist='The Beatles'
Name: generate\_song, Input: {'args': (), 'kwargs': {'name': 'Come Together', 'artist': 'The Beatles'}}, Output: name='Come Together' artist='The Beatles'
Name: generate\_song, Input: {'args': (), 'kwargs': {'name': 'Help!', 'artist': 'The Beatles'}}, Output: name='Help!' artist='The Beatles'

Structured Prediction[¶](https://docs.llamaindex.ai/en/stable/examples/llm/openai/#structured-prediction)
---------------------------------------------------------------------------------------------------------

An important use case for function calling is extracting structured objects. LlamaIndex provides an intuitive interface for this through `structured_predict` - simply define the target Pydantic class (can be nested), and given a prompt, we extract out the desired object.

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI
from llama\_index.core.prompts import PromptTemplate
from pydantic import BaseModel

class Restaurant(BaseModel):
    """A restaurant with name, city, and cuisine."""

    name: str
    city: str
    cuisine: str

llm \= OpenAI(model\="gpt-3.5-turbo")
prompt\_tmpl \= PromptTemplate(
    "Generate a restaurant in a given city {city\_name}"
)
restaurant\_obj \= llm.structured\_predict(
    Restaurant, prompt\_tmpl, city\_name\="San Francisco"
)

from llama\_index.llms.openai import OpenAI from llama\_index.core.prompts import PromptTemplate from pydantic import BaseModel class Restaurant(BaseModel): """A restaurant with name, city, and cuisine.""" name: str city: str cuisine: str llm = OpenAI(model="gpt-3.5-turbo") prompt\_tmpl = PromptTemplate( "Generate a restaurant in a given city {city\_name}" ) restaurant\_obj = llm.structured\_predict( Restaurant, prompt\_tmpl, city\_name="San Francisco" )

In \[ \]:

Copied!

restaurant\_obj

restaurant\_obj

Out\[ \]:

Restaurant(name='Tasty Bites', city='San Francisco', cuisine='Italian')

Async[¶](https://docs.llamaindex.ai/en/stable/examples/llm/openai/#async)
-------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI

llm \= OpenAI(model\="gpt-3.5-turbo")

from llama\_index.llms.openai import OpenAI llm = OpenAI(model="gpt-3.5-turbo")

In \[ \]:

Copied!

resp \= await llm.acomplete("Paul Graham is ")

resp = await llm.acomplete("Paul Graham is ")

In \[ \]:

Copied!

print(resp)

print(resp)

a computer scientist, entrepreneur, and venture capitalist. He is best known for co-founding the startup accelerator Y Combinator and for his work as an essayist and author on topics related to technology, startups, and entrepreneurship. Graham is also the co-founder of Viaweb, one of the first web-based applications, which was acquired by Yahoo in 1998. He has been a prominent figure in the tech industry for many years and is known for his insightful and thought-provoking writings on a wide range of subjects.

In \[ \]:

Copied!

resp \= await llm.astream\_complete("Paul Graham is ")

resp = await llm.astream\_complete("Paul Graham is ")

In \[ \]:

Copied!

async for delta in resp:
    print(delta.delta, end\="")

async for delta in resp: print(delta.delta, end="")

Paul Graham is an entrepreneur, venture capitalist, and computer scientist. He is best known for his work in the startup world, having co-founded the accelerator Y Combinator and investing in many successful startups such as Airbnb, Dropbox, and Stripe. He is also a prolific writer, having authored several books on topics such as startups, programming, and technology.

Async function calling is also supported.

In \[ \]:

Copied!

llm \= OpenAI(model\="gpt-3.5-turbo")
response \= await llm.apredict\_and\_call(\[tool\], "Generate a song")
print(str(response))

llm = OpenAI(model="gpt-3.5-turbo") response = await llm.apredict\_and\_call(\[tool\], "Generate a song") print(str(response))

name='Sunshine' artist='John Smith'

Set API Key at a per-instance level[¶](https://docs.llamaindex.ai/en/stable/examples/llm/openai/#set-api-key-at-a-per-instance-level)
-------------------------------------------------------------------------------------------------------------------------------------

If desired, you can have separate LLM instances use separate API keys.

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI

llm \= OpenAI(model\="gpt-3.5-turbo", api\_key\="BAD\_KEY")
resp \= OpenAI().complete("Paul Graham is ")
print(resp)

from llama\_index.llms.openai import OpenAI llm = OpenAI(model="gpt-3.5-turbo", api\_key="BAD\_KEY") resp = OpenAI().complete("Paul Graham is ") print(resp)

a computer scientist, entrepreneur, and venture capitalist. He is best known as the co-founder of the startup accelerator Y Combinator. Graham has also written several influential essays on startups and entrepreneurship, which have gained a wide following in the tech industry. He has been involved in the founding and funding of numerous successful startups, including Reddit, Dropbox, and Airbnb. Graham is known for his insightful and often controversial opinions on various topics, including education, inequality, and the future of technology.

Back to top

[Previous Ollama - Gemma](https://docs.llamaindex.ai/en/stable/examples/llm/ollama_gemma/)[Next OpenAI JSON Mode vs. Function Calling for Data Extraction](https://docs.llamaindex.ai/en/stable/examples/llm/openai_json_vs_function_calling/)

Hi, how can I help you?

🦙
