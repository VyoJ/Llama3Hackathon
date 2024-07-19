Title: Function Calling Mistral Agent - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/mistral_agent/

Markdown Content:
Function Calling Mistral Agent - LlamaIndex


This notebook shows you how to use our Mistral agent, powered by function calling capabilities.

Initial Setup[¶](https://docs.llamaindex.ai/en/stable/examples/agent/mistral_agent/#initial-setup)
--------------------------------------------------------------------------------------------------

Let's start by importing some simple building blocks.

The main thing we need is:

1.  the OpenAI API (using our own `llama_index` LLM class)
2.  a place to keep conversation history
3.  a definition for tools that our agent can use.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-mistralai
%pip install llama\-index\-embeddings\-mistralai

%pip install llama-index-llms-mistralai %pip install llama-index-embeddings-mistralai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import json
from typing import Sequence, List

from llama\_index.llms.mistralai import MistralAI
from llama\_index.core.llms import ChatMessage
from llama\_index.core.tools import BaseTool, FunctionTool

import nest\_asyncio

nest\_asyncio.apply()

import json from typing import Sequence, List from llama\_index.llms.mistralai import MistralAI from llama\_index.core.llms import ChatMessage from llama\_index.core.tools import BaseTool, FunctionTool import nest\_asyncio nest\_asyncio.apply()

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

Make sure your MISTRAL\_API\_KEY is set. Otherwise explicitly specify the `api_key` parameter.

In \[ \]:

Copied!

llm \= MistralAI(model\="mistral-large-latest")

llm = MistralAI(model="mistral-large-latest")

Initialize Mistral Agent[¶](https://docs.llamaindex.ai/en/stable/examples/agent/mistral_agent/#initialize-mistral-agent)
------------------------------------------------------------------------------------------------------------------------

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

### Chat[¶](https://docs.llamaindex.ai/en/stable/examples/agent/mistral_agent/#chat)

In \[ \]:

Copied!

response \= agent.chat("What is (121 + 2) \* 5?")
print(str(response))

response = agent.chat("What is (121 + 2) \* 5?") print(str(response))

Added user message to memory: What is (121 + 2) \* 5?

Calling function: add with args: {"a": 121, "b": 2}

Calling function: multiply with args: {"a": 123, "b": 5}
assistant: The result of (121 + 2) \* 5 is 615.

In \[ \]:

Copied!

\# inspect sources
print(response.sources)

\# inspect sources print(response.sources)

\[ToolOutput(content='123', tool\_name='add', raw\_input={'args': (), 'kwargs': {'a': 121, 'b': 2}}, raw\_output=123), ToolOutput(content='615', tool\_name='multiply', raw\_input={'args': (), 'kwargs': {'a': 123, 'b': 5}}, raw\_output=615)\]

### Async Chat[¶](https://docs.llamaindex.ai/en/stable/examples/agent/mistral_agent/#async-chat)

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
assistant: The result of (121 \* 3) + (5 \* 8) is 403.

Mistral Agent over RAG Pipeline[¶](https://docs.llamaindex.ai/en/stable/examples/agent/mistral_agent/#mistral-agent-over-rag-pipeline)
--------------------------------------------------------------------------------------------------------------------------------------

Build a Mistral agent over a simple 10K document. We use both Mistral embeddings and mistral-medium to construct the RAG pipeline, and pass it to the Mistral agent as a tool.

In \[ \]:

Copied!

!mkdir \-p 'data/10k/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' \-O 'data/10k/uber\_2021.pdf'

!mkdir -p 'data/10k/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' -O 'data/10k/uber\_2021.pdf'

\--2024-03-23 11:13:41--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 2606:50c0:8003::154, 2606:50c0:8002::154, 2606:50c0:8001::154, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|2606:50c0:8003::154|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1880483 (1.8M) \[application/octet-stream\]
Saving to: ‘data/10k/uber\_2021.pdf’

data/10k/uber\_2021. 100%\[ Calling Function  Calling Function ===
Calling function: uber\_10k with args: {"input": "What are the tailwinds for Uber in 2021?"}
assistant: Based on the information provided, here are the risk factors for Uber in 2021:

1. Failure to offer or develop autonomous vehicle technologies, which could result in inferior performance or safety concerns compared to competitors.
2. Dependence on high-quality personnel and the potential impact of attrition or unsuccessful succession planning on the business.
3. Security or data privacy breaches, unauthorized access, or destruction of proprietary, employee, or user data.
4. Cyberattacks, such as malware, ransomware, viruses, spamming, and phishing attacks, which could harm the company's reputation and operations.
5. Climate change risks, including physical and transitional risks, that may adversely impact the business if not managed effectively.
6. Reliance on third parties to maintain open marketplaces for distributing products and providing software, which could negatively affect the business if interfered with.
7. The need for additional capital to support business growth, which may not be available on reasonable terms or at all.
8. Difficulties in identifying, acquiring, and integrating suitable businesses, which could harm operating results and prospects.
9. Legal and regulatory risks, including extensive government regulation and oversight related to payment and financial services.
10. Intellectual property risks, such as the inability to protect intellectual property or claims of misappropriation by third parties.
11. Volatility in the market price of common stock, which could result in steep declines and loss of investment for shareholders.
12. Economic risks related to the COVID-19 pandemic, which has adversely impacted and could continue to adversely impact the business, financial condition, and results of operations.
13. The potential reclassification of Drivers as employees, workers, or quasi-employees, which could result in material costs associated with defending, settling, or resolving lawsuits and demands for arbitration.

On the other hand, here are some tailwinds for Uber in 2021:

1. Launch of Uber One, a single cross-platform membership program in the United States, which offers discounts, special pricing, priority service, and exclusive perks across rides, delivery, and grocery offerings.
2. Introduction of a "Super App" view on iOS

Back to top

[Previous Vector Memory](https://docs.llamaindex.ai/en/stable/examples/agent/memory/vector_memory/)[Next Multi-Document Agents (V1)](https://docs.llamaindex.ai/en/stable/examples/agent/multi_document_agents-v1/)

Hi, how can I help you?

🦙
