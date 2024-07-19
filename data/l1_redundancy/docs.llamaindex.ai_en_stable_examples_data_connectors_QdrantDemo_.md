Title: Qdrant Reader - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/data_connectors/QdrantDemo/

Markdown Content:
Qdrant Reader - LlamaIndex


In \[ \]:

Copied!

%pip install llama\-index\-readers\-qdrant

%pip install llama-index-readers-qdrant

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

from llama\_index.readers.qdrant import QdrantReader

from llama\_index.readers.qdrant import QdrantReader

In \[ \]:

Copied!

reader \= QdrantReader(host\="localhost")

reader = QdrantReader(host="localhost")

In \[ \]:

Copied!

\# the query\_vector is an embedding representation of your query\_vector
\# Example query vector:
\#   query\_vector=\[0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3\]

query\_vector \= \[n1, n2, n3, ...\]

\# the query\_vector is an embedding representation of your query\_vector # Example query vector: # query\_vector=\[0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3\] query\_vector = \[n1, n2, n3, ...\]

In \[ \]:

Copied!

\# NOTE: Required args are collection\_name, query\_vector.
\# See the Python client: https://github.com/qdrant/qdrant\_client
\# for more details.
documents \= reader.load\_data(
    collection\_name\="demo", query\_vector\=query\_vector, limit\=5
)

\# NOTE: Required args are collection\_name, query\_vector. # See the Python client: https://github.com/qdrant/qdrant\_client # for more details. documents = reader.load\_data( collection\_name="demo", query\_vector=query\_vector, limit=5 )

### Create index[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/QdrantDemo/#create-index)

In \[ \]:

Copied!

index \= SummaryIndex.from\_documents(documents)

index = SummaryIndex.from\_documents(documents)

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

[Previous Psychic Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/PsychicDemo/)[Next Slack Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/SlackDemo/)
