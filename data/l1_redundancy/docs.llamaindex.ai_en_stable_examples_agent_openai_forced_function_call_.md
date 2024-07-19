Title: OpenAI agent: specifying a forced function call

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/openai_forced_function_call/

Markdown Content:
OpenAI agent: specifying a forced function call - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-agent\-openai
%pip install llama\-index\-llms\-openai

%pip install llama-index-agent-openai %pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import json
from typing import Sequence, List

from llama\_index.llms.openai import OpenAI
from llama\_index.core.llms import ChatMessage
from llama\_index.core.tools import BaseTool, FunctionTool
from llama\_index.agent.openai import OpenAIAgent

import json from typing import Sequence, List from llama\_index.llms.openai import OpenAI from llama\_index.core.llms import ChatMessage from llama\_index.core.tools import BaseTool, FunctionTool from llama\_index.agent.openai import OpenAIAgent

In \[ \]:

Copied!

def add(a: int, b: int) \-> int:
    """Add two integers and returns the result integer"""
    return a + b

add\_tool \= FunctionTool.from\_defaults(fn\=add)

def useless\_tool() \-> int:
    """This is a uselss tool."""
    return "This is a uselss output."

useless\_tool \= FunctionTool.from\_defaults(fn\=useless\_tool)

def add(a: int, b: int) -> int: """Add two integers and returns the result integer""" return a + b add\_tool = FunctionTool.from\_defaults(fn=add) def useless\_tool() -> int: """This is a uselss tool.""" return "This is a uselss output." useless\_tool = FunctionTool.from\_defaults(fn=useless\_tool)

In \[ \]:

Copied!

llm \= OpenAI(model\="gpt-3.5-turbo-0613")
agent \= OpenAIAgent.from\_tools(\[useless\_tool, add\_tool\], llm\=llm, verbose\=True)

llm = OpenAI(model="gpt-3.5-turbo-0613") agent = OpenAIAgent.from\_tools(\[useless\_tool, add\_tool\], llm=llm, verbose=True)

### "Auto" function call[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_forced_function_call/#auto-function-call)

The agent automatically selects the useful "add" tool

In \[ \]:

Copied!

response \= agent.chat(
    "What is 5 + 2?", tool\_choice\="auto"
)  \# note function\_call param is deprecated
\# use tool\_choice instead

response = agent.chat( "What is 5 + 2?", tool\_choice="auto" ) # note function\_call param is deprecated # use tool\_choice instead

STARTING TURN 1
---------------


Calling function: add with args: {
  "a": 5,
  "b": 2
}
Got output: 7
 Calling Function 

STARTING TURN 2
---------------


Calling function: add with args: {
  "a": 5,
  "b": 2
}
Got output: 7


STARTING TURN 3
---------------

In \[ \]:

Copied!

print(response)

print(response)

The product of 5 and 2 is 10.

### "None" function call[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_forced_function_call/#none-function-call)

The agent is forced to not use a tool

In \[ \]:

Copied!

response \= agent.chat("What is 5 \* 2?", tool\_choice\="none")

response = agent.chat("What is 5 \* 2?", tool\_choice="none")

STARTING TURN 1
---------------

In \[ \]:

Copied!

print(response)

print(response)

The product of 5 and 2 is 10.

Back to top

[Previous OpenAI Assistant Advanced Retrieval Cookbook](https://docs.llamaindex.ai/en/stable/examples/agent/openai_assistant_query_cookbook/)[Next Benchmarking OpenAI Retrieval API (through Assistant Agent)](https://docs.llamaindex.ai/en/stable/examples/agent/openai_retrieval_benchmark/)

Hi, how can I help you?

🦙
