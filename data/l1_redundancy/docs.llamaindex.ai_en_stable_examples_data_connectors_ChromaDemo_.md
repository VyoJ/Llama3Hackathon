Title: Chroma Reader - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/data_connectors/ChromaDemo/

Markdown Content:
Chroma Reader - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-readers\-chroma

%pip install llama-index-readers-chroma

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

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

In \[ \]:

Copied!

from llama\_index.readers.chroma import ChromaReader

from llama\_index.readers.chroma import ChromaReader

In \[ \]:

Copied!

\# The chroma reader loads data from a persisted Chroma collection.
\# This requires a collection name and a persist directory.

reader \= ChromaReader(
    collection\_name\="chroma\_collection",
    persist\_directory\="examples/data\_connectors/chroma\_collection",
)

\# The chroma reader loads data from a persisted Chroma collection. # This requires a collection name and a persist directory. reader = ChromaReader( collection\_name="chroma\_collection", persist\_directory="examples/data\_connectors/chroma\_collection", )

In \[ \]:

Copied!

\# the query\_vector is an embedding representation of your query.
\# Example query vector:
\#   query\_vector=\[0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3\]

query\_vector \= \[n1, n2, n3, ...\]

\# the query\_vector is an embedding representation of your query. # Example query vector: # query\_vector=\[0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3\] query\_vector = \[n1, n2, n3, ...\]

In \[ \]:

Copied!

\# NOTE: Required args are collection\_name, query\_vector.
\# See the Python client: https://github.com/chroma-core/chroma
\# for more details.
documents \= reader.load\_data(
    collection\_name\="demo", query\_vector\=query\_vector, limit\=5
)

\# NOTE: Required args are collection\_name, query\_vector. # See the Python client: https://github.com/chroma-core/chroma # for more details. documents = reader.load\_data( collection\_name="demo", query\_vector=query\_vector, limit=5 )

### Create index[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/ChromaDemo/#create-index)

In \[ \]:

Copied!

from llama\_index.core import SummaryIndex

index \= SummaryIndex.from\_documents(documents)

from llama\_index.core import SummaryIndex index = SummaryIndex.from\_documents(documents)

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("<query\_text>")

\# set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine() response = query\_engine.query("")

In \[ \]:

Copied!

display(Markdown(f"<b>{response}</b>"))

display(Markdown(f"**{response}**"))

Back to top

[Previous Streaming for Chat Engine - Condense Question Mode](https://docs.llamaindex.ai/en/stable/examples/customization/streaming/chat_engine_condense_question_stream_response/)[Next DashVector Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/DashvectorReaderDemo/)
