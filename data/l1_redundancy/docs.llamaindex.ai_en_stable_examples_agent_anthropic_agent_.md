Title: Function Calling Anthropic Agent - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/anthropic_agent/

Markdown Content:
Function Calling Anthropic Agent - LlamaIndex


This notebook shows you how to use our Anthropic agent, powered by function calling capabilities.

**NOTE:** Only claude-3 models support function calling using Anthropic's API.

Initial Setup[¶](https://docs.llamaindex.ai/en/stable/examples/agent/anthropic_agent/#initial-setup)
----------------------------------------------------------------------------------------------------

Let's start by importing some simple building blocks.

The main thing we need is:

1.  the Anthropic API (using our own `llama_index` LLM class)
2.  a place to keep conversation history
3.  a definition for tools that our agent can use.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-anthropic
%pip install llama\-index\-embeddings\-openai

%pip install llama-index-llms-anthropic %pip install llama-index-embeddings-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

from llama\_index.llms.anthropic import Anthropic
from llama\_index.core.tools import FunctionTool

import nest\_asyncio

nest\_asyncio.apply()

from llama\_index.llms.anthropic import Anthropic from llama\_index.core.tools import FunctionTool import nest\_asyncio nest\_asyncio.apply()

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

Make sure your ANTHROPIC\_API\_KEY is set. Otherwise explicitly specify the `api_key` parameter.

In \[ \]:

Copied!

llm \= Anthropic(model\="claude-3-opus-20240229", api\_key\="sk-ant-...")

llm = Anthropic(model="claude-3-opus-20240229", api\_key="sk-ant-...")

Initialize Anthropic Agent[¶](https://docs.llamaindex.ai/en/stable/examples/agent/anthropic_agent/#initialize-anthropic-agent)
------------------------------------------------------------------------------------------------------------------------------

Here we initialize a simple Mistral agent with calculator functions.

In \[ \]:

Copied!

from llama\_index.core.agent import FunctionCallingAgentWorker

agent\_worker \= FunctionCallingAgentWorker.from\_tools(
    \[multiply\_tool, add\_tool\],
    llm\=llm,
    verbose\=True,
    allow\_parallel\_tool\_calls\=False,
)
agent \= agent\_worker.as\_agent()

from llama\_index.core.agent import FunctionCallingAgentWorker agent\_worker = FunctionCallingAgentWorker.from\_tools( \[multiply\_tool, add\_tool\], llm=llm, verbose=True, allow\_parallel\_tool\_calls=False, ) agent = agent\_worker.as\_agent()

### Chat[¶](https://docs.llamaindex.ai/en/stable/examples/agent/anthropic_agent/#chat)

In \[ \]:

Copied!

response \= agent.chat("What is (121 + 2) \* 5?")
print(str(response))

response = agent.chat("What is (121 + 2) \* 5?") print(str(response))

Added user message to memory: What is (121 + 2) \* 5?

Calling function: add with args: {"a": 121, "b": 2}

Calling function: multiply with args: {"a": 123, "b": 5}
assistant: Therefore, (121 + 2) \* 5 = 615

In \[ \]:

Copied!

\# inspect sources
print(response.sources)

\# inspect sources print(response.sources)

\[ToolOutput(content='123', tool\_name='add', raw\_input={'args': (), 'kwargs': {'a': 121, 'b': 2}}, raw\_output=123), ToolOutput(content='615', tool\_name='multiply', raw\_input={'args': (), 'kwargs': {'a': 123, 'b': 5}}, raw\_output=615)\]

### Async Chat[¶](https://docs.llamaindex.ai/en/stable/examples/agent/anthropic_agent/#async-chat)

Also let's re-enable parallel function calling so that we can call two `multiply` operations simultaneously.

In \[ \]:

Copied!

\# enable parallel function calling
agent\_worker \= FunctionCallingAgentWorker.from\_tools(
    \[multiply\_tool, add\_tool\],
    llm\=llm,
    verbose\=True,
    allow\_parallel\_tool\_calls\=True,
)
agent \= agent\_worker.as\_agent()
response \= await agent.achat("What is (121 \* 3) + (5 \* 8)?")
print(str(response))

\# enable parallel function calling agent\_worker = FunctionCallingAgentWorker.from\_tools( \[multiply\_tool, add\_tool\], llm=llm, verbose=True, allow\_parallel\_tool\_calls=True, ) agent = agent\_worker.as\_agent() response = await agent.achat("What is (121 \* 3) + (5 \* 8)?") print(str(response))

Added user message to memory: What is (121 \* 3) + (5 \* 8)?

Calling function: multiply with args: {"a": 121, "b": 3}

Calling function: multiply with args: {"a": 5, "b": 8}

Calling function: add with args: {"a": 363, "b": 40}
assistant: Therefore, the result of (121 \* 3) + (5 \* 8) is 403.

Anthropic Agent over RAG Pipeline[¶](https://docs.llamaindex.ai/en/stable/examples/agent/anthropic_agent/#anthropic-agent-over-rag-pipeline)
--------------------------------------------------------------------------------------------------------------------------------------------

Build a Anthropic agent over a simple 10K document. We use OpenAI embeddings and claude-3-haiku-20240307 to construct the RAG pipeline, and pass it to the Anthropic Opus agent as a tool.

In \[ \]:

Copied!

!mkdir \-p 'data/10k/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' \-O 'data/10k/uber\_2021.pdf'

!mkdir -p 'data/10k/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' -O 'data/10k/uber\_2021.pdf'

\--2024-04-04 18:12:42--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.111.133, 185.199.108.133, 185.199.109.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.111.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1880483 (1.8M) \[application/octet-stream\]
Saving to: ‘data/10k/uber\_2021.pdf’

data/10k/uber\_2021. 100%\[ Calling Function ===
Calling function: uber\_10k with args: {"input": "What were some of the key risk factors and tailwinds mentioned for Uber's business in 2021?"}
assistant: In summary, some of the key risk factors Uber faced in 2021 included regulatory challenges, IP protection, staying competitive with new technologies, seasonality and forecasting challenges due to COVID-19, and risks of international expansion. However, Uber also benefited from tailwinds like accelerated growth in food delivery due to the pandemic and adapting well to new remote work arrangements.

Back to top

[Previous Agentic rag with llamaindex and vertexai managed index](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_with_llamaindex_and_vertexai_managed_index/)[Next Function Calling AWS Bedrock Converse Agent](https://docs.llamaindex.ai/en/stable/examples/agent/bedrock_converse_agent/)

Hi, how can I help you?

🦙
