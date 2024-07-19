Title: Sub Question Query Engine - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/query_engine/sub_question_query_engine/

Markdown Content:
Sub Question Query Engine - LlamaIndex


In this tutorial, we showcase how to use a **sub question query engine** to tackle the problem of answering a complex query using multiple data sources.  
It first breaks down the complex query into sub questions for each relevant data source, then gather all the intermediate reponses and synthesizes a final response.

### Preparation[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/sub_question_query_engine/#preparation)

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import nest\_asyncio

nest\_asyncio.apply()

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..." import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.core.tools import QueryEngineTool, ToolMetadata
from llama\_index.core.query\_engine import SubQuestionQueryEngine
from llama\_index.core.callbacks import CallbackManager, LlamaDebugHandler
from llama\_index.core import Settings

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.core.tools import QueryEngineTool, ToolMetadata from llama\_index.core.query\_engine import SubQuestionQueryEngine from llama\_index.core.callbacks import CallbackManager, LlamaDebugHandler from llama\_index.core import Settings

In \[ \]:

Copied!

\# Using the LlamaDebugHandler to print the trace of the sub questions
\# captured by the SUB\_QUESTION callback event type
llama\_debug \= LlamaDebugHandler(print\_trace\_on\_end\=True)
callback\_manager \= CallbackManager(\[llama\_debug\])

Settings.callback\_manager \= callback\_manager

\# Using the LlamaDebugHandler to print the trace of the sub questions # captured by the SUB\_QUESTION callback event type llama\_debug = LlamaDebugHandler(print\_trace\_on\_end=True) callback\_manager = CallbackManager(\[llama\_debug\]) Settings.callback\_manager = callback\_manager

### Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/sub_question_query_engine/#download-data)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

Will not apply HSTS. The HSTS database must be a regular and non-world-writable file.
ERROR: could not open HSTS store at '/home/loganm/.wget-hsts'. HSTS will be disabled.
--2024-01-28 11:27:04--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.111.133, 185.199.108.133, 185.199.109.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.111.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 75042 (73K) \[text/plain\]
Saving to: ‘data/paul\_graham/paul\_graham\_essay.txt’

data/paul\_graham/pa 100%\[")

\# iterate through sub\_question items captured in SUB\_QUESTION event from llama\_index.core.callbacks import CBEventType, EventPayload for i, (start\_event, end\_event) in enumerate( llama\_debug.get\_event\_pairs(CBEventType.SUB\_QUESTION) ): qa\_pair = end\_event.payload\[EventPayload.SUB\_QUESTION\] print("Sub Question " + str(i) + ": " + qa\_pair.sub\_q.sub\_question.strip()) print("Answer: " + qa\_pair.answer.strip()) print("
Sub Question 1: What did Paul Graham work on during YC?
Answer: During his time at YC, Paul Graham worked on various projects. He wrote all of YC's internal software in Arc and also worked on Hacker News (HN), which was a news aggregator initially meant for startup founders but later changed to engage intellectual curiosity. Additionally, he wrote essays and worked on helping the startups in the YC program with their problems.


Back to top

[Previous Joint Tabular/Semantic QA over Tesla 10K](https://docs.llamaindex.ai/en/stable/examples/query_engine/sec_tables/tesla_10q_table/)[Next An Introduction to LlamaIndex Query Pipelines](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/)
