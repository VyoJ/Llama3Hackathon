Title: OpenAI Agent with Tool Call Parser

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_tool_call_parser/

Markdown Content:
OpenAI Agent with Tool Call Parser - LlamaIndex


Unfortunately, the tool calls by OpenAI are not always valid json, especially from older versions of the API. Up to and including the OpenAI API version 1106, this issue is relatively frequent if the argument is a long string (e.g. a python script), see for example [here](https://community.openai.com/t/malformed-json-in-gpt4-1106-function-arguments/685884).

With the default tool call parser, the OpenAI Agent will fail to parse these tool calls and tries to fix the tool call in the next step. This needs another llm call, which is slow and expensive.

This notebook demonstrates how to define a custom tool call parser that can handle certain kinds of malformed function calls. The following steps are copied from the OpenAI Agent notebook, with the addition of a custom tool call parser.

Initial Setup[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_tool_call_parser/#initial-setup)
------------------------------------------------------------------------------------------------------------------

Let's start by importing some simple building blocks.

The main thing we need is:

1.  the OpenAI API (using our own `llama_index` LLM class)
2.  a place to keep conversation history
3.  a definition for tools that our agent can use.

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
from llama\_index.core.tools import FunctionTool

import nest\_asyncio

nest\_asyncio.apply()

import json from llama\_index.core.tools import FunctionTool import nest\_asyncio nest\_asyncio.apply()

Let's define some very simple calculator tools for our agent.

In \[ \]:

Copied!

def multiply(a: int, b: int) \-> int:
    """Multiple two integers and returns the result integer"""
    return a \* b

multiply\_tool \= FunctionTool.from\_defaults(fn\=multiply)

def multiply(a: int, b: int) -> int: """Multiple two integers and returns the result integer""" return a \* b multiply\_tool = FunctionTool.from\_defaults(fn=multiply)

In \[ \]:

Copied!

def add(a: int, b: int) \-> int:
    """Add two integers and returns the result integer"""
    return a + b

add\_tool \= FunctionTool.from\_defaults(fn\=add)

def add(a: int, b: int) -> int: """Add two integers and returns the result integer""" return a + b add\_tool = FunctionTool.from\_defaults(fn=add)

Definition of the Tool Call Parser[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_tool_call_parser/#definition-of-the-tool-call-parser)
------------------------------------------------------------------------------------------------------------------------------------------------------------

Sometimes, OpenAI tool calls are not valid json

When defining your own Tool Call Parser, you need to define a function that takes a OpenAIToolCall and returns a dictionary. The dictionary will be passed as \*\*kwargs to the tool function.

The Parser should throw a ValueError if the tool call can't be parsed. This will be returned to the agent and it will try to fix the call on the next step.

In \[ \]:

Copied!

from typing import Dict
from llama\_index.llms.openai.utils import OpenAIToolCall
import re

\# The same parser is available as
\# from llama\_index.agent.openai import advanced\_tool\_call\_parser

def custom\_tool\_call\_parser(tool\_call: OpenAIToolCall) \-> Dict:
    r"""Parse tool calls that are not standard json.
    Also parses tool calls of the following forms:
    variable = \\"\\"\\"Some long text\\"\\"\\"
    variable = "Some long text"'
    variable = '''Some long text'''
    variable = 'Some long text'
    """
    arguments\_str \= tool\_call.function.arguments
    if len(arguments\_str.strip()) \ 0: # OpenAI returns an empty string for functions containing no args return {} try: tool\_call = json.loads(arguments\_str) if not isinstance(tool\_call, dict): raise ValueError("Tool call must be a dictionary") return tool\_call except json.JSONDecodeError as e: # pattern to match variable names and content within quotes pattern = r'(\[a-zA-Z\_\]\[a-zA-Z\_0-9\]\*)\\s\*=\\s\*\["\\'\]+(.\*?)\["\\'\]+' match = re.search(pattern, arguments\_str) if match: variable\_name = match.group(1) # This is the variable name content = match.group(2) # This is the content within the quotes return {variable\_name: content} raise ValueError(f"Invalid tool call: {e!s}")

Defining the OpenAI Agent with Tool Call Parser[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_tool_call_parser/#defining-the-openai-agent-with-tool-call-parser)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.agent.openai import OpenAIAgent
from llama\_index.llms.openai import OpenAI

from llama\_index.agent.openai import OpenAIAgent from llama\_index.llms.openai import OpenAI

In \[ \]:

Copied!

llm \= OpenAI(model\="gpt-3.5-turbo-0613")
agent \= OpenAIAgent.from\_tools(
    \[multiply\_tool, add\_tool\],
    llm\=llm,
    verbose\=True,
    tool\_call\_parser\=custom\_tool\_call\_parser,
)

llm = OpenAI(model="gpt-3.5-turbo-0613") agent = OpenAIAgent.from\_tools( \[multiply\_tool, add\_tool\], llm=llm, verbose=True, tool\_call\_parser=custom\_tool\_call\_parser, )

### Chat[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_tool_call_parser/#chat)

In \[ \]:

Copied!

response \= agent.chat("What is (121 \* 3) + 42?")
print(str(response))

response = agent.chat("What is (121 \* 3) + 42?") print(str(response))

Added user message to memory: What is (121 \* 3) + 42?

Calling function: multiply with args: {
  "a": 121,
  "b": 3
}
Got output: 363
 Calling Function 

(121 \* 3) + 42 is equal to 405.

In \[ \]:

Copied!

\# inspect sources
print(response.sources)

\# inspect sources print(response.sources)

\[ToolOutput(content='363', tool\_name='multiply', raw\_input={'args': (), 'kwargs': {'a': 121, 'b': 3}}, raw\_output=363), ToolOutput(content='405', tool\_name='add', raw\_input={'args': (), 'kwargs': {'a': 363, 'b': 42}}, raw\_output=405)\]

Back to top

[Previous Retrieval-Augmented OpenAI Agent](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_retrieval/)[Next OpenAI Agent with Query Engine Tools](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_with_query_engine/)

Hi, how can I help you?

🦙
