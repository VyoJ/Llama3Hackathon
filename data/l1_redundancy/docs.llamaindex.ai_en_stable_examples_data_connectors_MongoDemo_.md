Title: MongoDB Reader - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/data_connectors/MongoDemo/

Markdown Content:
MongoDB Reader - LlamaIndex


Demonstrates our MongoDB data connector

In \[ \]:

Copied!

%pip install llama\-index\-readers\-mongodb

%pip install llama-index-readers-mongodb

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙 and pymongo.

In \[ \]:

Copied!

!pip install llama\-index pymongo

!pip install llama-index pymongo

In \[ \]:

Copied!

from llama\_index.core import SummaryIndex
from llama\_index.readers.mongodb import SimpleMongoReader
from IPython.display import Markdown, display
import os

from llama\_index.core import SummaryIndex from llama\_index.readers.mongodb import SimpleMongoReader from IPython.display import Markdown, display import os

In \[ \]:

Copied!

host \= "<host>"
port \= "<port>"
db\_name \= "<db\_name>"
collection\_name \= "<collection\_name>"
\# query\_dict is passed into db.collection.find()
query\_dict \= {}
field\_names \= \["text"\]
reader \= SimpleMongoReader(host, port)
documents \= reader.load\_data(
    db\_name, collection\_name, field\_names, query\_dict\=query\_dict
)

host = "" port = "" db\_name = "" collection\_name = "" # query\_dict is passed into db.collection.find() query\_dict = {} field\_names = \["text"\] reader = SimpleMongoReader(host, port) documents = reader.load\_data( db\_name, collection\_name, field\_names, query\_dict=query\_dict )

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

[Previous MilvusReader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/MilvusReaderDemo/)[Next MyScale Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/MyScaleReaderDemo/)
