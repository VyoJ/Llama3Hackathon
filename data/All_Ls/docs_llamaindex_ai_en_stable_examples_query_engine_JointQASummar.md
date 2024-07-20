Title: Joint QA Summary Query Engine

URL Source: https://docs.llamaindex.ai/en/stable/examples/query_engine/JointQASummary/

Markdown Content:
Joint QA Summary Query Engine - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai

%pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import nest\_asyncio

nest\_asyncio.apply()

import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/JointQASummary/#download-data)
----------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/JointQASummary/#load-data)
--------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

reader \= SimpleDirectoryReader("./data/paul\_graham/")
documents \= reader.load\_data()

from llama\_index.core import SimpleDirectoryReader reader = SimpleDirectoryReader("./data/paul\_graham/") documents = reader.load\_data()

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI

gpt4 \= OpenAI(temperature\=0, model\="gpt-4")

chatgpt \= OpenAI(temperature\=0, model\="gpt-3.5-turbo")

from llama\_index.llms.openai import OpenAI gpt4 = OpenAI(temperature=0, model="gpt-4") chatgpt = OpenAI(temperature=0, model="gpt-3.5-turbo")

In \[ \]:

Copied!

from llama\_index.core.composability import QASummaryQueryEngineBuilder

\# NOTE: can also specify an existing docstore, summary text, qa\_text, etc.
query\_engine\_builder \= QASummaryQueryEngineBuilder(
    llm\=gpt4,
)
query\_engine \= query\_engine\_builder.build\_from\_documents(documents)

from llama\_index.core.composability import QASummaryQueryEngineBuilder # NOTE: can also specify an existing docstore, summary text, qa\_text, etc. query\_engine\_builder = QASummaryQueryEngineBuilder( llm=gpt4, ) query\_engine = query\_engine\_builder.build\_from\_documents(documents)

INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total embedding token usage: 20729 tokens
> \[build\_index\_from\_nodes\] Total embedding token usage: 20729 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total embedding token usage: 0 tokens
> \[build\_index\_from\_nodes\] Total embedding token usage: 0 tokens

In \[ \]:

Copied!

response \= query\_engine.query(
    "Can you give me a summary of the author's life?",
)

response = query\_engine.query( "Can you give me a summary of the author's life?", )

INFO:llama\_index.query\_engine.router\_query\_engine:Selecting query engine 1 because: This choice is relevant because it is specifically for summarization queries, which matches the request for a summary of the author's life..
Selecting query engine 1 because: This choice is relevant because it is specifically for summarization queries, which matches the request for a summary of the author's life..
INFO:llama\_index.indices.common\_tree.base:> Building index from nodes: 6 chunks
> Building index from nodes: 6 chunks
INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total LLM token usage: 1012 tokens
> \[get\_response\] Total LLM token usage: 1012 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total embedding token usage: 0 tokens
> \[get\_response\] Total embedding token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total LLM token usage: 23485 tokens
> \[get\_response\] Total LLM token usage: 23485 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total embedding token usage: 0 tokens
> \[get\_response\] Total embedding token usage: 0 tokens

In \[ \]:

Copied!

response \= query\_engine.query(
    "What did the author do growing up?",
)

response = query\_engine.query( "What did the author do growing up?", )

INFO:llama\_index.query\_engine.router\_query\_engine:Selecting query engine 0 because: This choice is relevant because it involves retrieving specific context from documents, which is needed to answer the question about the author's activities growing up..
Selecting query engine 0 because: This choice is relevant because it involves retrieving specific context from documents, which is needed to answer the question about the author's activities growing up..
INFO:llama\_index.token\_counter.token\_counter:> \[retrieve\] Total LLM token usage: 0 tokens
> \[retrieve\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[retrieve\] Total embedding token usage: 8 tokens
> \[retrieve\] Total embedding token usage: 8 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total LLM token usage: 1893 tokens
> \[get\_response\] Total LLM token usage: 1893 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total embedding token usage: 0 tokens
> \[get\_response\] Total embedding token usage: 0 tokens

In \[ \]:

Copied!

response \= query\_engine.query(
    "What did the author do during his time in art school?",
)

response = query\_engine.query( "What did the author do during his time in art school?", )

INFO:llama\_index.query\_engine.router\_query\_engine:Selecting query engine 0 because: This choice is relevant because it involves retrieving specific context from documents, which is needed to answer the question about the author's activities in art school..
Selecting query engine 0 because: This choice is relevant because it involves retrieving specific context from documents, which is needed to answer the question about the author's activities in art school..
INFO:llama\_index.token\_counter.token\_counter:> \[retrieve\] Total LLM token usage: 0 tokens
> \[retrieve\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[retrieve\] Total embedding token usage: 12 tokens
> \[retrieve\] Total embedding token usage: 12 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total LLM token usage: 1883 tokens
> \[get\_response\] Total LLM token usage: 1883 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total embedding token usage: 0 tokens
> \[get\_response\] Total embedding token usage: 0 tokens

Back to top

[Previous JSONalyze Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/JSONalyze_query_engine/)[Next Retriever Router Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/RetrieverRouterQueryEngine/)

Hi, how can I help you?

🦙
