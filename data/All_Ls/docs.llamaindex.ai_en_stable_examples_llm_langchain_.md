Title: Langchain - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/llm/langchain/

Markdown Content:
Langchain - LlamaIndex


       

[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jerryjliu/llama_index/blob/main/docs/docs/examples/llm/langchain.ipynb)

LangChain LLM[¶](https://docs.llamaindex.ai/en/stable/examples/llm/langchain/#langchain-llm)
--------------------------------------------------------------------------------------------

In \[ \]:

Copied!

%pip install llama\-index\-llms\-langchain

%pip install llama-index-llms-langchain

In \[ \]:

Copied!

from langchain.llms import OpenAI

from langchain.llms import OpenAI

In \[ \]:

Copied!

from llama\_index.llms.langchain import LangChainLLM

from llama\_index.llms.langchain import LangChainLLM

In \[ \]:

Copied!

llm \= LangChainLLM(llm\=OpenAI())

llm = LangChainLLM(llm=OpenAI())

In \[ \]:

Copied!

response\_gen \= llm.stream\_complete("Hi this is")

response\_gen = llm.stream\_complete("Hi this is")

In \[ \]:

Copied!

for delta in response\_gen:
    print(delta.delta, end\="")

for delta in response\_gen: print(delta.delta, end="")

 a test

Hello! Welcome to the test. What would you like to learn about?

Back to top

[Previous Konko](https://docs.llamaindex.ai/en/stable/examples/llm/konko/)[Next LiteLLM](https://docs.llamaindex.ai/en/stable/examples/llm/litellm/)
