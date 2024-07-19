Title: Streaming - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/customization/streaming/SimpleIndexDemo-streaming/

Markdown Content:
Streaming - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout)) from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader

INFO:numexpr.utils:Note: NumExpr detected 12 cores but "NUMEXPR\_MAX\_THREADS" not set, so enforcing safe limit of 8.
Note: NumExpr detected 12 cores but "NUMEXPR\_MAX\_THREADS" not set, so enforcing safe limit of 8.
INFO:numexpr.utils:NumExpr defaulting to 8 threads.
NumExpr defaulting to 8 threads.

/Users/suo/miniconda3/envs/llama/lib/python3.9/site-packages/deeplake/util/check\_latest\_version.py:32: UserWarning: A newer version of deeplake (3.6.7) is available. It's recommended that you update to the latest version using \`pip install -U deeplake\`.
  warnings.warn(

#### Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/customization/streaming/SimpleIndexDemo-streaming/#download-data)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

#### Load documents, build the VectorStoreIndex[¶](https://docs.llamaindex.ai/en/stable/examples/customization/streaming/SimpleIndexDemo-streaming/#load-documents-build-the-vectorstoreindex)

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham").load\_data()

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham").load\_data()

In \[ \]:

Copied!

index \= VectorStoreIndex.from\_documents(documents)

index = VectorStoreIndex.from\_documents(documents)

#### Query Index[¶](https://docs.llamaindex.ai/en/stable/examples/customization/streaming/SimpleIndexDemo-streaming/#query-index)

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine(streaming\=True, similarity\_top\_k\=1)
response\_stream \= query\_engine.query(
    "What did the author do growing up?",
)

\# set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine(streaming=True, similarity\_top\_k=1) response\_stream = query\_engine.query( "What did the author do growing up?", )

In \[ \]:

Copied!

response\_stream.print\_response\_stream()

response\_stream.print\_response\_stream()

The author grew up writing short stories and programming on an IBM 1401. He also nagged his father to buy him a TRS-80 microcomputer, on which he wrote simple games, a program to predict how high his model rockets would fly, and a word processor. He eventually went to college to study philosophy, but found it boring and switched to AI.

Back to top

[Previous Completion Prompts Customization](https://docs.llamaindex.ai/en/stable/examples/customization/prompts/completion_prompts/)[Next Streaming for Chat Engine - Condense Question Mode](https://docs.llamaindex.ai/en/stable/examples/customization/streaming/chat_engine_condense_question_stream_response/)
