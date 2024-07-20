Title: Twitter Reader - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/data_connectors/TwitterDemo/

Markdown Content:
Twitter Reader - LlamaIndex


In \[ \]:

Copied!

%pip install llama\-index\-readers\-twitter

%pip install llama-index-readers-twitter

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

from llama\_index.core import VectorStoreIndex
from llama\_index.readers.twitter import TwitterTweetReader
from IPython.display import Markdown, display
import os

from llama\_index.core import VectorStoreIndex from llama\_index.readers.twitter import TwitterTweetReader from IPython.display import Markdown, display import os

In \[ \]:

Copied!

\# create an app in https://developer.twitter.com/en/apps
BEARER\_TOKEN \= "<bearer\_token>"

\# create an app in https://developer.twitter.com/en/apps BEARER\_TOKEN = ""

In \[ \]:

Copied!

\# create reader, specify twitter handles
reader \= TwitterTweetReader(BEARER\_TOKEN)
documents \= reader.load\_data(\["@twitter\_handle1"\])

\# create reader, specify twitter handles reader = TwitterTweetReader(BEARER\_TOKEN) documents = reader.load\_data(\["@twitter\_handle1"\])

In \[ \]:

Copied!

index \= VectorStoreIndex.from\_documents(documents)

index = VectorStoreIndex.from\_documents(documents)

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

[Previous Slack Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/SlackDemo/)[Next Weaviate Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WeaviateDemo/)
