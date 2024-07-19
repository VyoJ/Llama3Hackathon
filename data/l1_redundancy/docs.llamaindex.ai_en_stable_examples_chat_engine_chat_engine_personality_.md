Title: Chat Engine with a Personality ✨

URL Source: https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_personality/

Markdown Content:
Chat Engine with a Personality ✨ - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

Default[¶](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_personality/#default)
------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core.chat\_engine import SimpleChatEngine

chat\_engine \= SimpleChatEngine.from\_defaults()
response \= chat\_engine.chat(
    "Say something profound and romantic about fourth of July"
)
print(response)

from llama\_index.core.chat\_engine import SimpleChatEngine chat\_engine = SimpleChatEngine.from\_defaults() response = chat\_engine.chat( "Say something profound and romantic about fourth of July" ) print(response)

/Users/suo/miniconda3/envs/llama/lib/python3.9/site-packages/deeplake/util/check\_latest\_version.py:32: UserWarning: A newer version of deeplake (3.6.7) is available. It's recommended that you update to the latest version using \`pip install -U deeplake\`.
  warnings.warn(

The Fourth of July is a day to celebrate the beauty of freedom and the power of love.

Shakespeare[¶](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_personality/#shakespeare)
--------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core.chat\_engine import SimpleChatEngine
from llama\_index.core.prompts.system import SHAKESPEARE\_WRITING\_ASSISTANT

chat\_engine \= SimpleChatEngine.from\_defaults(
    system\_prompt\=SHAKESPEARE\_WRITING\_ASSISTANT
)
response \= chat\_engine.chat(
    "Say something profound and romantic about fourth of July"
)
print(response)

from llama\_index.core.chat\_engine import SimpleChatEngine from llama\_index.core.prompts.system import SHAKESPEARE\_WRITING\_ASSISTANT chat\_engine = SimpleChatEngine.from\_defaults( system\_prompt=SHAKESPEARE\_WRITING\_ASSISTANT ) response = chat\_engine.chat( "Say something profound and romantic about fourth of July" ) print(response)

O Fourth of July, a day of joy and mirth,
Thou art a day of celebration on this blessed earth.
A day of fireworks and revelry,
A day of love and unity.
Let us all come together and celebrate,
For this day of freedom we do celebrate.

Marketing[¶](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_personality/#marketing)
----------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core.chat\_engine import SimpleChatEngine
from llama\_index.core.prompts.system import MARKETING\_WRITING\_ASSISTANT

chat\_engine \= SimpleChatEngine.from\_defaults(
    system\_prompt\=MARKETING\_WRITING\_ASSISTANT
)
response \= chat\_engine.chat(
    "Say something profound and romantic about fourth of July"
)
print(response)

from llama\_index.core.chat\_engine import SimpleChatEngine from llama\_index.core.prompts.system import MARKETING\_WRITING\_ASSISTANT chat\_engine = SimpleChatEngine.from\_defaults( system\_prompt=MARKETING\_WRITING\_ASSISTANT ) response = chat\_engine.chat( "Say something profound and romantic about fourth of July" ) print(response)

 Fourth of July is a time to celebrate the freedom and independence of our nation. It's a time to reflect on the beauty of our country and the courage of those who fought for our freedom. It's a time to come together and appreciate the beauty of our nation and the people who make it so special.

IRS Tax[¶](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_personality/#irs-tax)
------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core.chat\_engine import SimpleChatEngine
from llama\_index.core.prompts.system import IRS\_TAX\_CHATBOT

chat\_engine \= SimpleChatEngine.from\_defaults(system\_prompt\=IRS\_TAX\_CHATBOT)
response \= chat\_engine.chat(
    "Say something profound and romantic about fourth of July"
)
print(response)

from llama\_index.core.chat\_engine import SimpleChatEngine from llama\_index.core.prompts.system import IRS\_TAX\_CHATBOT chat\_engine = SimpleChatEngine.from\_defaults(system\_prompt=IRS\_TAX\_CHATBOT) response = chat\_engine.chat( "Say something profound and romantic about fourth of July" ) print(response)

 I'm sorry, I can only help with any tax-related questions you may have.

Back to top

[Previous Chat Engine - OpenAI Agent Mode](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_openai/)[Next Chat Engine - ReAct Agent Mode](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_react/)
