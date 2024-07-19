Title: Retrieval-Augmented OpenAI Agent - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_retrieval/

Markdown Content:
Retrieval-Augmented OpenAI Agent - LlamaIndex


In this tutorial, we show you how to use our `OpenAIAgent` implementation with a tool retriever, to build an agent on top of OpenAI's function API and store/index an arbitrary number of tools. Our indexing/retrieval modules help to remove the complexity of having too many functions to fit in the prompt.

Initial Setup[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_retrieval/#initial-setup)
-----------------------------------------------------------------------------------------------------------

Let's start by importing some simple building blocks.

The main thing we need is:

1.  the OpenAI API
2.  a place to keep conversation history
3.  a definition for tools that our agent can use.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-agent\-openai\-legacy

%pip install llama-index-agent-openai-legacy

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import json
from typing import Sequence

from llama\_index.core.tools import BaseTool, FunctionTool

import json from typing import Sequence from llama\_index.core.tools import BaseTool, FunctionTool

/Users/suo/miniconda3/envs/llama/lib/python3.9/site-packages/deeplake/util/check\_latest\_version.py:32: UserWarning: A newer version of deeplake (3.6.7) is available. It's recommended that you update to the latest version using \`pip install -U deeplake\`.
  warnings.warn(

Let's define some very simple calculator tools for our agent.

In \[ \]:

Copied!

def multiply(a: int, b: int) \-> int:
    """Multiply two integers and returns the result integer"""
    return a \* b

def add(a: int, b: int) \-> int:
    """Add two integers and returns the result integer"""
    return a + b

def useless(a: int, b: int) \-> int:
    """Toy useless function."""
    pass

multiply\_tool \= FunctionTool.from\_defaults(fn\=multiply, name\="multiply")
useless\_tools \= \[
    FunctionTool.from\_defaults(fn\=useless, name\=f"useless\_{str(idx)}")
    for idx in range(28)
\]
add\_tool \= FunctionTool.from\_defaults(fn\=add, name\="add")

all\_tools \= \[multiply\_tool\] + \[add\_tool\] + useless\_tools
all\_tools\_map \= {t.metadata.name: t for t in all\_tools}

def multiply(a: int, b: int) -> int: """Multiply two integers and returns the result integer""" return a \* b def add(a: int, b: int) -> int: """Add two integers and returns the result integer""" return a + b def useless(a: int, b: int) -> int: """Toy useless function.""" pass multiply\_tool = FunctionTool.from\_defaults(fn=multiply, name="multiply") useless\_tools = \[ FunctionTool.from\_defaults(fn=useless, name=f"useless\_{str(idx)}") for idx in range(28) \] add\_tool = FunctionTool.from\_defaults(fn=add, name="add") all\_tools = \[multiply\_tool\] + \[add\_tool\] + useless\_tools all\_tools\_map = {t.metadata.name: t for t in all\_tools}

Building an Object Index[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_retrieval/#building-an-object-index)
---------------------------------------------------------------------------------------------------------------------------------

We have an `ObjectIndex` construct in LlamaIndex that allows the user to use our index data structures over arbitrary objects. The ObjectIndex will handle serialiation to/from the object, and use an underying index (e.g. VectorStoreIndex, SummaryIndex, KeywordTableIndex) as the storage mechanism.

In this case, we have a large collection of Tool objects, and we'd want to define an ObjectIndex over these Tools.

The index comes bundled with a retrieval mechanism, an `ObjectRetriever`.

This can be passed in to our agent so that it can perform Tool retrieval during query-time.

In \[ \]:

Copied!

\# define an "object" index over these tools
from llama\_index.core import VectorStoreIndex
from llama\_index.core.objects import ObjectIndex

obj\_index \= ObjectIndex.from\_objects(
    all\_tools,
    index\_cls\=VectorStoreIndex,
)

\# define an "object" index over these tools from llama\_index.core import VectorStoreIndex from llama\_index.core.objects import ObjectIndex obj\_index = ObjectIndex.from\_objects( all\_tools, index\_cls=VectorStoreIndex, )

`OpenAIAgent` w/ Tool Retrieval[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_retrieval/#openaiagent-w-tool-retrieval)
--------------------------------------------------------------------------------------------------------------------------------------------

We provide a `OpenAIAgent` implementation in LlamaIndex, which can take in an `ObjectRetriever` over a set of `BaseTool` objects.

During query-time, we would first use the `ObjectRetriever` to retrieve a set of relevant Tools. These tools would then be passed into the agent; more specifically, their function signatures would be passed into the OpenAI Function calling API.

In \[ \]:

Copied!

from llama\_index.agent.openai import OpenAIAgent

from llama\_index.agent.openai import OpenAIAgent

In \[ \]:

Copied!

agent \= OpenAIAgent.from\_tools(
    tool\_retriever\=obj\_index.as\_retriever(similarity\_top\_k\=2), verbose\=True
)

agent = OpenAIAgent.from\_tools( tool\_retriever=obj\_index.as\_retriever(similarity\_top\_k=2), verbose=True )

In \[ \]:

Copied!

agent.chat("What's 212 multiplied by 122? Make sure to use Tools")

agent.chat("What's 212 multiplied by 122? Make sure to use Tools")

\
Calling function: multiply with args: {
  "a": 212,
  "b": 122
}
Got output: 25864
 Calling Function 

Out\[ \]:

Response(response='212 added to 122 is 334.', source\_nodes=\[\], metadata=None)

Back to top

[Previous OpenAI Agent Query Planning](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_query_plan/)[Next OpenAI Agent with Tool Call Parser](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_tool_call_parser/)

Hi, how can I help you?

🦙
