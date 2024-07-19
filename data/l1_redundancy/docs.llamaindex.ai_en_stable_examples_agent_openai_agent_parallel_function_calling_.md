Title: Single-Turn Multi-Function Calling OpenAI Agents

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_parallel_function_calling/

Markdown Content:
Single-Turn Multi-Function Calling OpenAI Agents - LlamaIndex


[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/docs/examples/agent/openai_agent_parallel_function_calling.ipynb)

With the latest OpenAI API (v. 1.1.0+), users can now execute multiple function calls within a single turn of `User` and `Agent` dialogue. We've updated our library to enable this new feature as well, and in this notebook we'll show you how it all works!

NOTE: OpenAI refers to this as "Parallel" function calling, but the current implementation doesn't invoke parallel computations of the multiple function calls. So, it's "parallelizable" function calling in terms of our current implementation.

In \[ \]:

Copied!

%pip install llama\-index\-agent\-openai
%pip install llama\-index\-llms\-openai

%pip install llama-index-agent-openai %pip install llama-index-llms-openai

In \[ \]:

Copied!

from llama\_index.agent.openai import OpenAIAgent
from llama\_index.llms.openai import OpenAI
from llama\_index.core.tools import BaseTool, FunctionTool

from llama\_index.agent.openai import OpenAIAgent from llama\_index.llms.openai import OpenAI from llama\_index.core.tools import BaseTool, FunctionTool

### Setup[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_parallel_function_calling/#setup)

If you've seen any of our previous notebooks on OpenAI Agents, then you're already familiar with the cookbook recipe that we have to follow here. But if not, or if you fancy a refresher then all we need to do (at a high level) are the following steps:

1.  Define a set of tools (we'll use `FunctionTool`) since Agents work with tools
2.  Define the `LLM` for the Agent
3.  Define a `OpenAIAgent`

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

In \[ \]:

Copied!

llm \= OpenAI(model\="gpt-3.5-turbo-1106")
agent \= OpenAIAgent.from\_tools(
    \[multiply\_tool, add\_tool\], llm\=llm, verbose\=True
)

llm = OpenAI(model="gpt-3.5-turbo-1106") agent = OpenAIAgent.from\_tools( \[multiply\_tool, add\_tool\], llm=llm, verbose=True )

### Sync mode[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_parallel_function_calling/#sync-mode)

In \[ \]:

Copied!

response \= agent.chat("What is (121 \* 3) + 42?")
print(str(response))

response = agent.chat("What is (121 \* 3) + 42?") print(str(response))

STARTING TURN 1
---------------


Calling function: multiply with args: {"a": 121, "b": 3}
Got output: 363
 Calling Function 

STARTING TURN 2
---------------

The result of (121 \* 3) + 42 is 405.

In \[ \]:

Copied!

response \= agent.stream\_chat("What is (121 \* 3) + 42?")

response = agent.stream\_chat("What is (121 \* 3) + 42?")

STARTING TURN 1
---------------


Calling function: add with args: {"a":363,"b":42}
Got output: 405
 Calling Function 

STARTING TURN 2
---------------

The result of (121 \* 3) + 42 is 405.

In \[ \]:

Copied!

response \= await agent.astream\_chat("What is (121 \* 3) + 42?")

response\_gen \= response.response\_gen

async for token in response.async\_response\_gen():
    print(token, end\="")

response = await agent.astream\_chat("What is (121 \* 3) + 42?") response\_gen = response.response\_gen async for token in response.async\_response\_gen(): print(token, end="")

STARTING TURN 1
---------------


Calling function: multiply with args: {"a": 121, "b": 3}
Got output: 363
 Calling Function 

STARTING TURN 2
---------------

The result of (121 \* 3) + 42 is 405.

### Example from OpenAI docs[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_parallel_function_calling/#example-from-openai-docs)

Here's an example straight from the OpenAI [docs](https://platform.openai.com/docs/guides/function-calling/parallel-function-calling) on Parallel function calling. (Their example gets this done in 76 lines of code, whereas with the `llama_index` library you can get that down to about 18 lines.)

In \[ \]:

Copied!

import json

\# Example dummy function hard coded to return the same weather
\# In production, this could be your backend API or an external API
def get\_current\_weather(location, unit\="fahrenheit"):
    """Get the current weather in a given location"""
    if "tokyo" in location.lower():
        return json.dumps(
            {"location": location, "temperature": "10", "unit": "celsius"}
        )
    elif "san francisco" in location.lower():
        return json.dumps(
            {"location": location, "temperature": "72", "unit": "fahrenheit"}
        )
    else:
        return json.dumps(
            {"location": location, "temperature": "22", "unit": "celsius"}
        )

weather\_tool \= FunctionTool.from\_defaults(fn\=get\_current\_weather)

import json # Example dummy function hard coded to return the same weather # In production, this could be your backend API or an external API def get\_current\_weather(location, unit="fahrenheit"): """Get the current weather in a given location""" if "tokyo" in location.lower(): return json.dumps( {"location": location, "temperature": "10", "unit": "celsius"} ) elif "san francisco" in location.lower(): return json.dumps( {"location": location, "temperature": "72", "unit": "fahrenheit"} ) else: return json.dumps( {"location": location, "temperature": "22", "unit": "celsius"} ) weather\_tool = FunctionTool.from\_defaults(fn=get\_current\_weather)

In \[ \]:

Copied!

llm \= OpenAI(model\="gpt-3.5-turbo-1106")
agent \= OpenAIAgent.from\_tools(\[weather\_tool\], llm\=llm, verbose\=True)
response \= agent.chat(
    "What's the weather like in San Francisco, Tokyo, and Paris?"
)

llm = OpenAI(model="gpt-3.5-turbo-1106") agent = OpenAIAgent.from\_tools(\[weather\_tool\], llm=llm, verbose=True) response = agent.chat( "What's the weather like in San Francisco, Tokyo, and Paris?" )

STARTING TURN 1
---------------


Calling function: get\_current\_weather with args: {"location": "San Francisco", "unit": "fahrenheit"}
Got output: {"location": "San Francisco", "temperature": "72", "unit": "fahrenheit"}
 Calling Function 


Calling function: get\_current\_weather with args: {"location": "Paris", "unit": "fahrenheit"}
Got output: {"location": "Paris", "temperature": "22", "unit": "celsius"}
 Calling Function 

STARTING TURN 2
---------------


Calling function: get\_current\_weather with args: {
  "location": "Tokyo"
}
Got output: {"location": "Tokyo", "temperature": "10", "unit": "celsius"}
 Calling Function 

STARTING TURN 4
---------------

Conclusion[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_parallel_function_calling/#conclusion)
---------------------------------------------------------------------------------------------------------------------

And so, as you can see the `llama_index` library can handle multiple function calls (as well as a single function call) within a single turn of dialogue between the user and the OpenAI agent!

Back to top

[Previous OpenAI Agent Workarounds for Lengthy Tool Descriptions](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_lengthy_tools/)[Next OpenAI Agent + Query Engine Experimental Cookbook](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_query_cookbook/)

Hi, how can I help you?

🦙
