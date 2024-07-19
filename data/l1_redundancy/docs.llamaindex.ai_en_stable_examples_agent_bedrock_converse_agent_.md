Title: Function Calling AWS Bedrock Converse Agent

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/bedrock_converse_agent/

Markdown Content:
Function Calling AWS Bedrock Converse Agent - LlamaIndex


This notebook shows you how to use our AWS Bedrock Converse agent, powered by function calling capabilities.

Initial Setup[¶](https://docs.llamaindex.ai/en/stable/examples/agent/bedrock_converse_agent/#initial-setup)
-----------------------------------------------------------------------------------------------------------

Let's start by importing some simple building blocks.

The main thing we need is:

1.  AWS credentials with access to Bedrock and the Claude Haiku LLM
2.  a place to keep conversation history
3.  a definition for tools that our agent can use.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-bedrock\-converse
%pip install llama\-index\-embeddings\-huggingface

%pip install llama-index-llms-bedrock-converse %pip install llama-index-embeddings-huggingface

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

from llama\_index.llms.bedrock\_converse import BedrockConverse
from llama\_index.core.tools import FunctionTool

import nest\_asyncio

nest\_asyncio.apply()

from llama\_index.llms.bedrock\_converse import BedrockConverse from llama\_index.core.tools import FunctionTool import nest\_asyncio nest\_asyncio.apply()

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

Make sure to set your AWS credentials, either the `profile_name` or the keys below.

In \[ \]:

Copied!

llm \= BedrockConverse(
    model\="anthropic.claude-3-haiku-20240307-v1:0",
    \# NOTE replace with your own AWS credentials
    aws\_access\_key\_id\="AWS Access Key ID to use",
    aws\_secret\_access\_key\="AWS Secret Access Key to use",
    aws\_session\_token\="AWS Session Token to use",
    region\_name\="AWS Region to use, eg. us-east-1",
)

llm = BedrockConverse( model="anthropic.claude-3-haiku-20240307-v1:0", # NOTE replace with your own AWS credentials aws\_access\_key\_id="AWS Access Key ID to use", aws\_secret\_access\_key="AWS Secret Access Key to use", aws\_session\_token="AWS Session Token to use", region\_name="AWS Region to use, eg. us-east-1", )

Initialize AWS Bedrock Converse Agent[¶](https://docs.llamaindex.ai/en/stable/examples/agent/bedrock_converse_agent/#initialize-aws-bedrock-converse-agent)
-----------------------------------------------------------------------------------------------------------------------------------------------------------

Here we initialize a simple AWS Bedrock Converse agent with calculator functions.

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

### Chat[¶](https://docs.llamaindex.ai/en/stable/examples/agent/bedrock_converse_agent/#chat)

In \[ \]:

Copied!

response \= agent.chat("What is (121 + 2) \* 5?")

response = agent.chat("What is (121 + 2) \* 5?")

In \[ \]:

Copied!

\# inspect sources
print(str(response))
print(response.sources)

\# inspect sources print(str(response)) print(response.sources)

AWS Bedrock Converse Agent over RAG Pipeline[¶](https://docs.llamaindex.ai/en/stable/examples/agent/bedrock_converse_agent/#aws-bedrock-converse-agent-over-rag-pipeline)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Build an AWS Bedrock Converse agent over a simple 10K document. We use both HuggingFace embeddings and `BAAI/bge-small-en-v1.5` to construct the RAG pipeline, and pass it to the AWS Bedrock Converse agent as a tool.

In \[ \]:

Copied!

!mkdir \-p 'data/10k/'
!curl \-o 'data/10k/uber\_2021.pdf' 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf'

!mkdir -p 'data/10k/' !curl -o 'data/10k/uber\_2021.pdf' 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf'

In \[ \]:

Copied!

from llama\_index.core.tools import QueryEngineTool, ToolMetadata
from llama\_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama\_index.embeddings.huggingface import HuggingFaceEmbedding
from llama\_index.llms.bedrock\_converse import BedrockConverse

embed\_model \= HuggingFaceEmbedding(model\_name\="BAAI/bge-small-en-v1.5")
query\_llm \= BedrockConverse(
    model\="anthropic.claude-3-haiku-20240307-v1:0",
    \# NOTE replace with your own AWS credentials
    aws\_access\_key\_id\="AWS Access Key ID to use",
    aws\_secret\_access\_key\="AWS Secret Access Key to use",
    aws\_session\_token\="AWS Session Token to use",
    region\_name\="AWS Region to use, eg. us-east-1",
)

\# load data
uber\_docs \= SimpleDirectoryReader(
    input\_files\=\["./data/10k/uber\_2021.pdf"\]
).load\_data()
\# build index
uber\_index \= VectorStoreIndex.from\_documents(
    uber\_docs, embed\_model\=embed\_model
)
uber\_engine \= uber\_index.as\_query\_engine(similarity\_top\_k\=3, llm\=query\_llm)
query\_engine\_tool \= QueryEngineTool(
    query\_engine\=uber\_engine,
    metadata\=ToolMetadata(
        name\="uber\_10k",
        description\=(
            "Provides information about Uber financials for year 2021. "
            "Use a detailed plain text question as input to the tool."
        ),
    ),
)

from llama\_index.core.tools import QueryEngineTool, ToolMetadata from llama\_index.core import SimpleDirectoryReader, VectorStoreIndex from llama\_index.embeddings.huggingface import HuggingFaceEmbedding from llama\_index.llms.bedrock\_converse import BedrockConverse embed\_model = HuggingFaceEmbedding(model\_name="BAAI/bge-small-en-v1.5") query\_llm = BedrockConverse( model="anthropic.claude-3-haiku-20240307-v1:0", # NOTE replace with your own AWS credentials aws\_access\_key\_id="AWS Access Key ID to use", aws\_secret\_access\_key="AWS Secret Access Key to use", aws\_session\_token="AWS Session Token to use", region\_name="AWS Region to use, eg. us-east-1", ) # load data uber\_docs = SimpleDirectoryReader( input\_files=\["./data/10k/uber\_2021.pdf"\] ).load\_data() # build index uber\_index = VectorStoreIndex.from\_documents( uber\_docs, embed\_model=embed\_model ) uber\_engine = uber\_index.as\_query\_engine(similarity\_top\_k=3, llm=query\_llm) query\_engine\_tool = QueryEngineTool( query\_engine=uber\_engine, metadata=ToolMetadata( name="uber\_10k", description=( "Provides information about Uber financials for year 2021. " "Use a detailed plain text question as input to the tool." ), ), )

In \[ \]:

Copied!

from llama\_index.core.agent import FunctionCallingAgentWorker

agent\_worker \= FunctionCallingAgentWorker.from\_tools(
    \[query\_engine\_tool\], llm\=llm, verbose\=True
)
agent \= agent\_worker.as\_agent()

from llama\_index.core.agent import FunctionCallingAgentWorker agent\_worker = FunctionCallingAgentWorker.from\_tools( \[query\_engine\_tool\], llm=llm, verbose=True ) agent = agent\_worker.as\_agent()

In \[ \]:

Copied!

response \= agent.chat(
    "Tell me both the risk factors and tailwinds for Uber? Do two parallel tool calls."
)

response = agent.chat( "Tell me both the risk factors and tailwinds for Uber? Do two parallel tool calls." )

In \[ \]:

Copied!

print(str(response))

print(str(response))

Back to top

[Previous Function Calling Anthropic Agent](https://docs.llamaindex.ai/en/stable/examples/agent/anthropic_agent/)[Next Chain-of-Abstraction LlamaPack](https://docs.llamaindex.ai/en/stable/examples/agent/coa_agent/)

Hi, how can I help you?

🦙
