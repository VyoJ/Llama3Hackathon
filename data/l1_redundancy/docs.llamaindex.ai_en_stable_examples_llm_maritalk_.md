Title: Maritalk - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/llm/maritalk/

Markdown Content:
Maritalk - LlamaIndex


Introduction[¶](https://docs.llamaindex.ai/en/stable/examples/llm/maritalk/#introduction)
-----------------------------------------------------------------------------------------

MariTalk is an assistant developed by the Brazilian company [Maritaca AI](https://www.maritaca.ai/). MariTalk is based on language models that have been specially trained to understand Portuguese well.

This notebook demonstrates how to use MariTalk with Llama Index through two examples:

1.  Get pet name suggestions with chat method;
2.  Classify film reviews as negative or positive with few-shot examples with complete method.

Installation[¶](https://docs.llamaindex.ai/en/stable/examples/llm/maritalk/#installation)
-----------------------------------------------------------------------------------------

If you're opening this Notebook on colab, you will probably need to install LlamaIndex.

In \[ \]:

Copied!

!pip install llama\-index
!pip install llama\-index\-llms\-maritalk
!pip install asyncio

!pip install llama-index !pip install llama-index-llms-maritalk !pip install asyncio

API Key[¶](https://docs.llamaindex.ai/en/stable/examples/llm/maritalk/#api-key)
-------------------------------------------------------------------------------

You will need an API key that can be obtained from chat.maritaca.ai ("Chaves da API" section).

### Example 1 - Pet Name Suggestions with Chat[¶](https://docs.llamaindex.ai/en/stable/examples/llm/maritalk/#example-1-pet-name-suggestions-with-chat)

In \[ \]:

Copied!

from llama\_index.core.llms import ChatMessage
from llama\_index.llms.maritalk import Maritalk

import asyncio

\# To customize your API key, do this
\# otherwise it will lookup MARITALK\_API\_KEY from your env variable
llm \= Maritalk(api\_key\="<your\_maritalk\_api\_key>", model\="sabia-2-medium")

\# Call chat with a list of messages
messages \= \[
    ChatMessage(
        role\="system",
        content\="You are an assistant specialized in suggesting pet names. Given the animal, you must suggest 4 names.",
    ),
    ChatMessage(role\="user", content\="I have a dog."),
\]

\# Sync chat
response \= llm.chat(messages)
print(response)

\# Async chat
async def get\_dog\_name(llm, messages):
    response \= await llm.achat(messages)
    print(response)

asyncio.run(get\_dog\_name(llm, messages))

from llama\_index.core.llms import ChatMessage from llama\_index.llms.maritalk import Maritalk import asyncio # To customize your API key, do this # otherwise it will lookup MARITALK\_API\_KEY from your env variable llm = Maritalk(api\_key="", model="sabia-2-medium") # Call chat with a list of messages messages = \[ ChatMessage( role="system", content="You are an assistant specialized in suggesting pet names. Given the animal, you must suggest 4 names.", ), ChatMessage(role="user", content="I have a dog."), \] # Sync chat response = llm.chat(messages) print(response) # Async chat async def get\_dog\_name(llm, messages): response = await llm.achat(messages) print(response) asyncio.run(get\_dog\_name(llm, messages))

#### Stream Generation[¶](https://docs.llamaindex.ai/en/stable/examples/llm/maritalk/#stream-generation)

For tasks involving the generation of long text, such as creating an extensive article or translating a large document, it can be advantageous to receive the response in parts, as the text is generated, instead of waiting for the complete text. This makes the application more responsive and efficient, especially when the generated text is extensive. We offer two approaches to meet this need: one synchronous and another asynchronous.

In \[ \]:

Copied!

\# Sync streaming chat
response \= llm.stream\_chat(messages)
for chunk in response:
    print(chunk.delta, end\="", flush\=True)

\# Async streaming chat
async def get\_dog\_name\_streaming(llm, messages):
    async for chunk in await llm.astream\_chat(messages):
        print(chunk.delta, end\="", flush\=True)

asyncio.run(get\_dog\_name\_streaming(llm, messages))

\# Sync streaming chat response = llm.stream\_chat(messages) for chunk in response: print(chunk.delta, end="", flush=True) # Async streaming chat async def get\_dog\_name\_streaming(llm, messages): async for chunk in await llm.astream\_chat(messages): print(chunk.delta, end="", flush=True) asyncio.run(get\_dog\_name\_streaming(llm, messages))

### Example 2 - Few-shot Examples with Complete[¶](https://docs.llamaindex.ai/en/stable/examples/llm/maritalk/#example-2-few-shot-examples-with-complete)

We recommend using the `llm.complete()` method when using the model with few-shot examples

In \[ \]:

Copied!

prompt \= """Classifique a resenha de filme como "positiva" ou "negativa".

Resenha: Gostei muito do filme, é o melhor do ano!
Classe: positiva

Resenha: O filme deixa muito a desejar.
Classe: negativa

Resenha: Apesar de longo, valeu o ingresso..
Classe:"""

\# Sync complete
response \= llm.complete(prompt)
print(response)

\# Async complete
async def classify\_review(llm, prompt):
    response \= await llm.acomplete(prompt)
    print(response)

asyncio.run(classify\_review(llm, prompt))

prompt = """Classifique a resenha de filme como "positiva" ou "negativa". Resenha: Gostei muito do filme, é o melhor do ano! Classe: positiva Resenha: O filme deixa muito a desejar. Classe: negativa Resenha: Apesar de longo, valeu o ingresso.. Classe:""" # Sync complete response = llm.complete(prompt) print(response) # Async complete async def classify\_review(llm, prompt): response = await llm.acomplete(prompt) print(response) asyncio.run(classify\_review(llm, prompt))

In \[ \]:

Copied!

\# Sync streaming complete
response \= llm.stream\_complete(prompt)
for chunk in response:
    print(chunk.delta, end\="", flush\=True)

\# Async streaming complete
async def classify\_review\_streaming(llm, prompt):
    async for chunk in await llm.astream\_complete(prompt):
        print(chunk.delta, end\="", flush\=True)

asyncio.run(classify\_review\_streaming(llm, prompt))

\# Sync streaming complete response = llm.stream\_complete(prompt) for chunk in response: print(chunk.delta, end="", flush=True) # Async streaming complete async def classify\_review\_streaming(llm, prompt): async for chunk in await llm.astream\_complete(prompt): print(chunk.delta, end="", flush=True) asyncio.run(classify\_review\_streaming(llm, prompt))

Back to top

[Previous LocalAI](https://docs.llamaindex.ai/en/stable/examples/llm/localai/)[Next MistralRS LLM](https://docs.llamaindex.ai/en/stable/examples/llm/mistral_rs/)
