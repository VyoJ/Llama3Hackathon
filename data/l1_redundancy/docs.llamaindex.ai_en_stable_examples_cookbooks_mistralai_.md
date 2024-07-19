Title: MistralAI Cookbook - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/cookbooks/mistralai/

Markdown Content:
MistralAI Cookbook - LlamaIndex


MistralAI released [mixtral-8x22b](https://mistral.ai/news/mixtral-8x22b/).

It is a sparse Mixture-of-Experts (SMoE) model that uses only 39B active parameters out of 141B, offering unparalleled cost efficiency for its size with 64K tokens context window, multilingual, strong maths coding, coding and Function calling capabilities.

This is a cook-book in showcasing the usage of `mixtral-8x22b` model with llama-index.

### Setup LLM and Embedding Model[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/mistralai/#setup-llm-and-embedding-model)

In \[ \]:

Copied!

import nest\_asyncio

nest\_asyncio.apply()

import os

os.environ\["MISTRAL\_API\_KEY"\] \= "<YOUR MISTRAL API KEY>"

from llama\_index.llms.mistralai import MistralAI
from llama\_index.embeddings.mistralai import MistralAIEmbedding
from llama\_index.core import Settings

llm \= MistralAI(model\="open-mixtral-8x22b", temperature\=0.1)
embed\_model \= MistralAIEmbedding(model\_name\="mistral-embed")

Settings.llm \= llm
Settings.embed\_model \= embed\_model

import nest\_asyncio nest\_asyncio.apply() import os os.environ\["MISTRAL\_API\_KEY"\] = "" from llama\_index.llms.mistralai import MistralAI from llama\_index.embeddings.mistralai import MistralAIEmbedding from llama\_index.core import Settings llm = MistralAI(model="open-mixtral-8x22b", temperature=0.1) embed\_model = MistralAIEmbedding(model\_name="mistral-embed") Settings.llm = llm Settings.embed\_model = embed\_model

### Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/mistralai/#download-data)

We will use `Uber-2021` and `Lyft-2021` 10K SEC filings.

In \[ \]:

Copied!

!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' \-O './uber\_2021.pdf'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/lyft\_2021.pdf' \-O './lyft\_2021.pdf'

!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' -O './uber\_2021.pdf' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/lyft\_2021.pdf' -O './lyft\_2021.pdf'

\--2024-04-17 20:33:54--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 2606:50c0:8000::154, 2606:50c0:8001::154, 2606:50c0:8002::154, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|2606:50c0:8000::154|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1880483 (1.8M) \[application/octet-stream\]
Saving to: './uber\_2021.pdf'

./uber\_2021.pdf     100%\[>\]   1.37M  --.-KB/s    in 0.1s    

2024-04-17 20:33:55 (11.6 MB/s) - './lyft\_2021.pdf' saved \[1440303/1440303\]

### Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/mistralai/#load-data)

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

uber\_docs \= SimpleDirectoryReader(input\_files\=\["./uber\_2021.pdf"\]).load\_data()
lyft\_docs \= SimpleDirectoryReader(input\_files\=\["./lyft\_2021.pdf"\]).load\_data()

from llama\_index.core import SimpleDirectoryReader uber\_docs = SimpleDirectoryReader(input\_files=\["./uber\_2021.pdf"\]).load\_data() lyft\_docs = SimpleDirectoryReader(input\_files=\["./lyft\_2021.pdf"\]).load\_data()

### Build RAG on uber and lyft docs[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/mistralai/#build-rag-on-uber-and-lyft-docs)

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex

uber\_index \= VectorStoreIndex.from\_documents(uber\_docs)
uber\_query\_engine \= uber\_index.as\_query\_engine(similarity\_top\_k\=5)

lyft\_index \= VectorStoreIndex.from\_documents(lyft\_docs)
lyft\_query\_engine \= lyft\_index.as\_query\_engine(similarity\_top\_k\=5)

from llama\_index.core import VectorStoreIndex uber\_index = VectorStoreIndex.from\_documents(uber\_docs) uber\_query\_engine = uber\_index.as\_query\_engine(similarity\_top\_k=5) lyft\_index = VectorStoreIndex.from\_documents(lyft\_docs) lyft\_query\_engine = lyft\_index.as\_query\_engine(similarity\_top\_k=5)

In \[ \]:

Copied!

response \= uber\_query\_engine.query("What is the revenue of uber in 2021?")
print(response)

response = uber\_query\_engine.query("What is the revenue of uber in 2021?") print(response)

Uber's revenue in 2021 was $17,455 million.

In \[ \]:

Copied!

response \= lyft\_query\_engine.query("What are lyft investments in 2021?")
print(response)

response = lyft\_query\_engine.query("What are lyft investments in 2021?") print(response)

In 2021, Lyft invested in several areas to advance its mission and maintain its position as a leader in the transportation industry. These investments include:

1. Expansion of Light Vehicles and Lyft Autonomous: Lyft continued to invest in the expansion of its network of Light Vehicles and Lyft Autonomous, focusing on the deployment and scaling of third-party self-driving technology on the Lyft network.

2. Efficient Operations: Lyft remained focused on finding ways to operate more efficiently while continuing to invest in the business.

3. Brand and Social Responsibility: Lyft aimed to build the defining brand of its generation and advocate through its commitment to social and environmental responsibility. This includes initiatives like LyftUp, which aims to make affordable and reliable transportation accessible to people regardless of their income or zip code.

4. Electric Vehicles: Lyft committed to reaching 100% electric vehicles (EVs) on its network by the end of 2030.

5. Driver Experience: Lyft invested in improving the driver experience, including access to rental cars for ridesharing through the Express Drive program and affordable and convenient vehicle maintenance services through Driver Centers and Mobile Services.

6. Marketplace Technology: Lyft invested in its proprietary technology to deliver a convenient and high-quality experience to drivers and riders. This includes investments in mapping, routing, payments, in-app navigation, matching technologies, and data science.

7. Mergers and Acquisitions: Lyft selectively considered acquisitions that contribute to the growth of its current business, help it expand into adjacent markets, or add new capabilities to its network. In the past, Lyft acquired Bikeshare Holdings LLC and Flexdrive, LLC.

8. Intellectual Property: Lyft invested in a patent program to identify and protect its strategic intellectual property in ridesharing, autonomous vehicle-related technology, telecommunications, networking, and other technologies relevant to its business. As of December 31, 2021, Lyft held 343 issued U.S. patents and had 310 U.S. patent applications pending.

9. Trademarks and Service Marks: Lyft had an ongoing trademark and service mark registration program to register its brand names, product names, taglines,

### `FunctionCallingAgent` with RAG QueryEngineTools.[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/mistralai/#functioncallingagent-with-rag-queryenginetools)

Here we use `Fuction Calling` capabilities of the model.

In \[ \]:

Copied!

from llama\_index.core.tools import QueryEngineTool, ToolMetadata
from llama\_index.core.agent import FunctionCallingAgentWorker

query\_engine\_tools \= \[
    QueryEngineTool(
        query\_engine\=lyft\_query\_engine,
        metadata\=ToolMetadata(
            name\="lyft\_10k",
            description\="Provides information about Lyft financials for year 2021",
        ),
    ),
    QueryEngineTool(
        query\_engine\=uber\_query\_engine,
        metadata\=ToolMetadata(
            name\="uber\_10k",
            description\="Provides information about Uber financials for year 2021",
        ),
    ),
\]

agent\_worker \= FunctionCallingAgentWorker.from\_tools(
    query\_engine\_tools,
    llm\=llm,
    verbose\=True,
    allow\_parallel\_tool\_calls\=False,
)
agent \= agent\_worker.as\_agent()

from llama\_index.core.tools import QueryEngineTool, ToolMetadata from llama\_index.core.agent import FunctionCallingAgentWorker query\_engine\_tools = \[ QueryEngineTool( query\_engine=lyft\_query\_engine, metadata=ToolMetadata( name="lyft\_10k", description="Provides information about Lyft financials for year 2021", ), ), QueryEngineTool( query\_engine=uber\_query\_engine, metadata=ToolMetadata( name="uber\_10k", description="Provides information about Uber financials for year 2021", ), ), \] agent\_worker = FunctionCallingAgentWorker.from\_tools( query\_engine\_tools, llm=llm, verbose=True, allow\_parallel\_tool\_calls=False, ) agent = agent\_worker.as\_agent()

In \[ \]:

Copied!

response \= agent.chat("What is the revenue of uber in 2021.")

response = agent.chat("What is the revenue of uber in 2021.")

Added user message to memory: What is the revenue of uber in 2021.

Calling function: uber\_10k with args: {"input": "revenue"}

Uber's revenue is primarily derived from fees paid by Mobility Drivers for using their platforms and related services to facilitate and complete Mobility services. Additionally, revenue is generated from fees paid by end-users for connection services obtained via the platform in certain markets. Uber's revenue also includes immaterial revenue streams such as financial partnerships products and Vehicle Solutions.

Uber's Delivery revenue is derived from Merchants' and Couriers' use of the Delivery platform and related services to facilitate and complete Delivery transactions. In certain markets where Uber is responsible for delivery services, delivery fees charged to end-users are also included in revenue. Advertising revenue from sponsored listing fees paid by merchants and brands in exchange for advertising services is also included in Delivery revenue.

Freight revenue consists of revenue from freight transportation services provided to shippers. After the acquisition of Transplace in the fourth quarter of 2021, Freight revenue also includes revenue from transportation management.

All Other revenue primarily includes collaboration revenue related to Uber's Advanced Technologies Group (ATG) business and revenue from New Mobility offerings and products. ATG collaboration revenue was related to a three-year joint collaboration agreement entered into in 2019. New Mobility offerings and products provided users access to rides through a variety of modes, including dockless e-bikes and e-scooters, platform incubator group offerings, and other immaterial revenue streams.

Uber's revenue is presented in the following tables for the years ended December 31, 2019, 2020, and 2021, respectively (in millions):

| Year Ended December 31, | 2019 | 2020 | 2021 |
| --- | --- | --- | --- |
| Mobility revenue | $10,707 | $6,089 | $6,953 |
| Delivery revenue | 1,401 | 3,904 | 8,362 |
| Freight revenue | 731 | 1,011 | 2,132 |
| All Other revenue | 161 | 135 | 8 |
| Total revenue

Uber's revenue for the year 2021 is presented in the following table:

| Year Ended December 31, | 2019 | 2020 | 2021 |
|---|---|---|---|
| Mobility revenue | $10,707 | $6,089 | $6,953 |
| Delivery revenue | 1,401 | 3,904 | 8,362 |
| Freight revenue | 731 | 1,011 | 2,132 |
| All Other revenue | 161 | 135 | 8 |
| Total revenue | $13,000 | $11,139 | $17,455 |

Uber's total revenue for the year 2021 was $17,455 million.

In \[ \]:

Copied!

print(response)

print(response)

assistant: Uber's revenue for the year 2021 is presented in the following table:

| Year Ended December 31, | 2019 | 2020 | 2021 |
|---|---|---|---|
| Mobility revenue | $10,707 | $6,089 | $6,953 |
| Delivery revenue | 1,401 | 3,904 | 8,362 |
| Freight revenue | 731 | 1,011 | 2,132 |
| All Other revenue | 161 | 135 | 8 |
| Total revenue | $13,000 | $11,139 | $17,455 |

Uber's total revenue for the year 2021 was $17,455 million.

In \[ \]:

Copied!

response \= agent.chat("What are lyft investments in 2021?")

response = agent.chat("What are lyft investments in 2021?")

Added user message to memory: What are lyft investments in 2021?

Calling function: lyft\_10k with args: {"input": "investments"}

The company's investments include cash and cash equivalents, short-term investments, and restricted investments. Cash equivalents consist of certificates of deposits, commercial paper, and corporate bonds with an original maturity of 90 days or less. Short-term investments are comprised of commercial paper, certificates of deposit, and corporate bonds that mature in twelve months or less. Restricted investments are held in trust accounts at third-party financial institutions and include debt security investments in commercial paper, certificates of deposit, corporate bonds, and U.S. government securities. The company also has investments in non-marketable equity securities, which are measured at cost with remeasurements to fair value only upon the occurrence of observable transactions for identical or similar investments of the same issuer or impairment.

Lyft's investments in 2021 include cash and cash equivalents, short-term investments, and restricted investments. Cash equivalents consist of certificates of deposits, commercial paper, and corporate bonds with an original maturity of 90 days or less. Short-term investments are comprised of commercial paper, certificates of deposit, and corporate bonds that mature in twelve months or less. Restricted investments are held in trust accounts at third-party financial institutions and include debt security investments in commercial paper, certificates of deposit, corporate bonds, and U.S. government securities. The company also has investments in non-marketable equity securities, which are measured at cost with remeasurements to fair value only upon the occurrence of observable transactions for identical or similar investments of the same issuer or impairment.

In \[ \]:

Copied!

print(response)

print(response)

assistant: Lyft's investments in 2021 include cash and cash equivalents, short-term investments, and restricted investments. Cash equivalents consist of certificates of deposits, commercial paper, and corporate bonds with an original maturity of 90 days or less. Short-term investments are comprised of commercial paper, certificates of deposit, and corporate bonds that mature in twelve months or less. Restricted investments are held in trust accounts at third-party financial institutions and include debt security investments in commercial paper, certificates of deposit, corporate bonds, and U.S. government securities. The company also has investments in non-marketable equity securities, which are measured at cost with remeasurements to fair value only upon the occurrence of observable transactions for identical or similar investments of the same issuer or impairment.

### Agents and Tools usage[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/mistralai/#agents-and-tools-usage)

In \[ \]:

Copied!

from llama\_index.core.tools import FunctionTool
from llama\_index.core.agent import (
    FunctionCallingAgentWorker,
    ReActAgent,
)

from llama\_index.core.tools import FunctionTool from llama\_index.core.agent import ( FunctionCallingAgentWorker, ReActAgent, )

In \[ \]:

Copied!

def multiply(a: int, b: int) \-> int:
    """Multiply two integers and returns the result integer"""
    return a \* b

def add(a: int, b: int) \-> int:
    """Add two integers and returns the result integer"""
    return a + b

def subtract(a: int, b: int) \-> int:
    """Subtract two integers and returns the result integer"""
    return a \- b

multiply\_tool \= FunctionTool.from\_defaults(fn\=multiply)
add\_tool \= FunctionTool.from\_defaults(fn\=add)
subtract\_tool \= FunctionTool.from\_defaults(fn\=subtract)

def multiply(a: int, b: int) -> int: """Multiply two integers and returns the result integer""" return a \* b def add(a: int, b: int) -> int: """Add two integers and returns the result integer""" return a + b def subtract(a: int, b: int) -> int: """Subtract two integers and returns the result integer""" return a - b multiply\_tool = FunctionTool.from\_defaults(fn=multiply) add\_tool = FunctionTool.from\_defaults(fn=add) subtract\_tool = FunctionTool.from\_defaults(fn=subtract)

### With Function Calling.[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/mistralai/#with-function-calling)

In \[ \]:

Copied!

agent\_worker \= FunctionCallingAgentWorker.from\_tools(
    \[multiply\_tool, add\_tool, subtract\_tool\],
    llm\=llm,
    verbose\=True,
    allow\_parallel\_tool\_calls\=False,
)
agent \= agent\_worker.as\_agent()

agent\_worker = FunctionCallingAgentWorker.from\_tools( \[multiply\_tool, add\_tool, subtract\_tool\], llm=llm, verbose=True, allow\_parallel\_tool\_calls=False, ) agent = agent\_worker.as\_agent()

In \[ \]:

Copied!

response \= agent.chat("What is (26 \* 2) + 2024?")
print(response)

response = agent.chat("What is (26 \* 2) + 2024?") print(response)

Added user message to memory: What is (26 \* 2) + 2024?

Calling function: multiply with args: {"a": 26, "b": 2}

52

Calling function: add with args: {"a": 52, "b": 2024}

2076

The result of (26 \* 2) + 2024 is 2076.
assistant: The result of (26 \* 2) + 2024 is 2076.

### With ReAct Agent[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/mistralai/#with-react-agent)

In \[ \]:

Copied!

agent \= ReActAgent.from\_tools(
    \[multiply\_tool, add\_tool, subtract\_tool\], llm\=llm, verbose\=True
)

agent = ReActAgent.from\_tools( \[multiply\_tool, add\_tool, subtract\_tool\], llm=llm, verbose=True )

In \[ \]:

Copied!

response \= agent.chat("What is (26 \* 2) + 2024?")
print(response)

response = agent.chat("What is (26 \* 2) + 2024?") print(response)

Thought: I need to use a tool to help me answer the question.
Action: multiply
Action Input: {"a": 26, "b": 2}

Observation: 52

Thought: I need to use another tool to continue answering the question.
Action: add
Action Input: {"a": 52, "b": 2024}

Observation: 2076

Thought: I can answer without using any more tools. I'll use the user's language to answer
Answer: (26 \* 2) + 2024 equals 2076.
(26 \* 2) + 2024 equals 2076.

Back to top

[Previous Llama3 Cookbook with Ollama and Replicate](https://docs.llamaindex.ai/en/stable/examples/cookbooks/llama3_cookbook_ollama_replicate/)[Next mixedbread Rerank Cookbook](https://docs.llamaindex.ai/en/stable/examples/cookbooks/mixedbread_reranker/)
