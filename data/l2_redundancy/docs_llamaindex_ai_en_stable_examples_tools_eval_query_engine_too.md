Title: Evaluation Query Engine Tool - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/tools/eval_query_engine_tool/

Markdown Content:
Evaluation Query Engine Tool - LlamaIndex


In this section we will show you how you can use an `EvalQueryEngineTool` with an agent. Some reasons you may want to use a `EvalQueryEngineTool`:

1.  Use specific kind of evaluation for a tool, and not just the agent's reasoning
2.  Use a different LLM for evaluating tool responses than the agent LLM

An `EvalQueryEngineTool` is built on top of the `QueryEngineTool`. Along with wrapping an existing [query engine](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/root.html), it also must be given an existing [evaluator](https://docs.llamaindex.ai/en/stable/examples/evaluation/answer_and_context_relevancy.html) to evaluate the responses of that query engine.

Install Dependencies[¶](https://docs.llamaindex.ai/en/stable/examples/tools/eval_query_engine_tool/#install-dependencies)
-------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

%pip install llama\-index\-embeddings\-huggingface
%pip install llama\-index\-llms\-openai
%pip install llama\-index\-agents\-openai

%pip install llama-index-embeddings-huggingface %pip install llama-index-llms-openai %pip install llama-index-agents-openai

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..."

Initialize and Set LLM and Local Embedding Model[¶](https://docs.llamaindex.ai/en/stable/examples/tools/eval_query_engine_tool/#initialize-and-set-llm-and-local-embedding-model)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core.settings import Settings
from llama\_index.embeddings.huggingface import HuggingFaceEmbedding
from llama\_index.llms.openai import OpenAI

Settings.embed\_model \= HuggingFaceEmbedding(
    model\_name\="BAAI/bge-small-en-v1.5"
)
Settings.llm \= OpenAI()

from llama\_index.core.settings import Settings from llama\_index.embeddings.huggingface import HuggingFaceEmbedding from llama\_index.llms.openai import OpenAI Settings.embed\_model = HuggingFaceEmbedding( model\_name="BAAI/bge-small-en-v1.5" ) Settings.llm = OpenAI()

Download and Index Data[¶](https://docs.llamaindex.ai/en/stable/examples/tools/eval_query_engine_tool/#download-and-index-data)
-------------------------------------------------------------------------------------------------------------------------------

This is something we are donig for the sake of this demo. In production environments, data stores and indexes should already exist and not be created on the fly.

### Create Storage Contexts[¶](https://docs.llamaindex.ai/en/stable/examples/tools/eval_query_engine_tool/#create-storage-contexts)

In \[ \]:

Copied!

from llama\_index.core import (
    StorageContext,
    load\_index\_from\_storage,
)

try:
    storage\_context \= StorageContext.from\_defaults(
        persist\_dir\="./storage/lyft",
    )
    lyft\_index \= load\_index\_from\_storage(storage\_context)

    storage\_context \= StorageContext.from\_defaults(
        persist\_dir\="./storage/uber"
    )
    uber\_index \= load\_index\_from\_storage(storage\_context)

    index\_loaded \= True
except:
    index\_loaded \= False

from llama\_index.core import ( StorageContext, load\_index\_from\_storage, ) try: storage\_context = StorageContext.from\_defaults( persist\_dir="./storage/lyft", ) lyft\_index = load\_index\_from\_storage(storage\_context) storage\_context = StorageContext.from\_defaults( persist\_dir="./storage/uber" ) uber\_index = load\_index\_from\_storage(storage\_context) index\_loaded = True except: index\_loaded = False

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/10k/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' \-O 'data/10k/uber\_2021.pdf'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/lyft\_2021.pdf' \-O 'data/10k/lyft\_2021.pdf'

!mkdir -p 'data/10k/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' -O 'data/10k/uber\_2021.pdf' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/lyft\_2021.pdf' -O 'data/10k/lyft\_2021.pdf'

### Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/tools/eval_query_engine_tool/#load-data)

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader, VectorStoreIndex

if not index\_loaded:
    \# load data
    lyft\_docs \= SimpleDirectoryReader(
        input\_files\=\["./data/10k/lyft\_2021.pdf"\]
    ).load\_data()
    uber\_docs \= SimpleDirectoryReader(
        input\_files\=\["./data/10k/uber\_2021.pdf"\]
    ).load\_data()

    \# build index
    lyft\_index \= VectorStoreIndex.from\_documents(lyft\_docs)
    uber\_index \= VectorStoreIndex.from\_documents(uber\_docs)

    \# persist index
    lyft\_index.storage\_context.persist(persist\_dir\="./storage/lyft")
    uber\_index.storage\_context.persist(persist\_dir\="./storage/uber")

from llama\_index.core import SimpleDirectoryReader, VectorStoreIndex if not index\_loaded: # load data lyft\_docs = SimpleDirectoryReader( input\_files=\["./data/10k/lyft\_2021.pdf"\] ).load\_data() uber\_docs = SimpleDirectoryReader( input\_files=\["./data/10k/uber\_2021.pdf"\] ).load\_data() # build index lyft\_index = VectorStoreIndex.from\_documents(lyft\_docs) uber\_index = VectorStoreIndex.from\_documents(uber\_docs) # persist index lyft\_index.storage\_context.persist(persist\_dir="./storage/lyft") uber\_index.storage\_context.persist(persist\_dir="./storage/uber")

Create Query Engines[¶](https://docs.llamaindex.ai/en/stable/examples/tools/eval_query_engine_tool/#create-query-engines)
-------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

lyft\_engine \= lyft\_index.as\_query\_engine(similarity\_top\_k\=5)
uber\_engine \= uber\_index.as\_query\_engine(similarity\_top\_k\=5)

lyft\_engine = lyft\_index.as\_query\_engine(similarity\_top\_k=5) uber\_engine = uber\_index.as\_query\_engine(similarity\_top\_k=5)

Create Evaluator[¶](https://docs.llamaindex.ai/en/stable/examples/tools/eval_query_engine_tool/#create-evaluator)
-----------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core.evaluation import RelevancyEvaluator

evaluator \= RelevancyEvaluator()

from llama\_index.core.evaluation import RelevancyEvaluator evaluator = RelevancyEvaluator()

Create Query Engine Tools[¶](https://docs.llamaindex.ai/en/stable/examples/tools/eval_query_engine_tool/#create-query-engine-tools)
-----------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core.tools import ToolMetadata
from llama\_index.core.tools.eval\_query\_engine import EvalQueryEngineTool

query\_engine\_tools \= \[
    EvalQueryEngineTool(
        evaluator\=evaluator,
        query\_engine\=lyft\_engine,
        metadata\=ToolMetadata(
            name\="lyft",
            description\=(
                "Provides information about Lyft's financials for year 2021. "
                "Use a detailed plain text question as input to the tool."
            ),
        ),
    ),
    EvalQueryEngineTool(
        evaluator\=evaluator,
        query\_engine\=uber\_engine,
        metadata\=ToolMetadata(
            name\="uber",
            description\=(
                "Provides information about Uber's financials for year 2021. "
                "Use a detailed plain text question as input to the tool."
            ),
        ),
    ),
\]

from llama\_index.core.tools import ToolMetadata from llama\_index.core.tools.eval\_query\_engine import EvalQueryEngineTool query\_engine\_tools = \[ EvalQueryEngineTool( evaluator=evaluator, query\_engine=lyft\_engine, metadata=ToolMetadata( name="lyft", description=( "Provides information about Lyft's financials for year 2021. " "Use a detailed plain text question as input to the tool." ), ), ), EvalQueryEngineTool( evaluator=evaluator, query\_engine=uber\_engine, metadata=ToolMetadata( name="uber", description=( "Provides information about Uber's financials for year 2021. " "Use a detailed plain text question as input to the tool." ), ), ), \]

Setup OpenAI Agent[¶](https://docs.llamaindex.ai/en/stable/examples/tools/eval_query_engine_tool/#setup-openai-agent)
---------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.agent.openai import OpenAIAgent

agent \= OpenAIAgent.from\_tools(query\_engine\_tools, verbose\=True)

from llama\_index.agent.openai import OpenAIAgent agent = OpenAIAgent.from\_tools(query\_engine\_tools, verbose=True)

Query Engine Fails Evaluation[¶](https://docs.llamaindex.ai/en/stable/examples/tools/eval_query_engine_tool/#query-engine-fails-evaluation)
-------------------------------------------------------------------------------------------------------------------------------------------

For demonstration purposes, we will tell the agent to choose the wrong tool first so that we can observe the effect of the `EvalQueryEngineTool` when evaluation fails. To achieve this, we will `tool_choice` to `lyft` when calling the agent.

This is what we should expect to happen:

1.  The agent will use the `lyft` tool first, which contains the wrong financials, as we have instructed it to do so
2.  The `EvalQueryEngineTool` will evaluate the response of the query engine using its evaluator
3.  The query engine output will fail evaluation because it contains Lyft's financials and not Uber's
4.  The tool will form a response that informs the agent that the tool could not be used, giving a reason
5.  The agent will fallback to the second tool, being `uber`
6.  The query engine output of the second tool will pass evaluation because it contains Uber's financials
7.  The agent will respond with an answer

In \[ \]:

Copied!

response \= await agent.achat(
    "What was Uber's revenue growth in 2021?", tool\_choice\="lyft"
)
print(str(response))

response = await agent.achat( "What was Uber's revenue growth in 2021?", tool\_choice="lyft" ) print(str(response))

Added user message to memory: What was Uber's revenue growth in 2021?

Calling function: lyft with args: {"input":"What was Uber's revenue growth in 2021?"}
Got output: Could not use tool lyft because it failed evaluation.
Reason: NO
 Calling Function 

Uber's revenue grew by 57% in 2021.

Query Engine Passes Evaluation[¶](https://docs.llamaindex.ai/en/stable/examples/tools/eval_query_engine_tool/#query-engine-passes-evaluation)
---------------------------------------------------------------------------------------------------------------------------------------------

Here we are asking a question about Lyft's financials. This is what we should expect to happen:

1.  The agent will use the `lyftk` tool first, simply based on its description as we have **not** set `tool_choice` here
2.  The `EvalQueryEngineTool` will evaluate the response of the query engine using its evaluator
3.  The output of the query engine will pass evaluation because it contains Lyft's financials

In \[ \]:

Copied!

response \= await agent.achat("What was Lyft's revenue growth in 2021?")
print(str(response))

response = await agent.achat("What was Lyft's revenue growth in 2021?") print(str(response))

Added user message to memory: What was Lyft's revenue growth in 2021?

Calling function: lyft with args: {"input": "What was Lyft's revenue growth in 2021?"}
Got output: Lyft's revenue growth in 2021 was $3,208,323, which increased compared to the revenue in 2020 and 2019.
 Calling Function 

Lyft's revenue grew by $3,208,323 in 2021, which increased compared to the revenue in 2020 and 2019.

Back to top

[Previous Cassandra Database Tools](https://docs.llamaindex.ai/en/stable/examples/tools/cassandra/)[Next Transforms Evaluation](https://docs.llamaindex.ai/en/stable/examples/transforms/TransformsEval/)
