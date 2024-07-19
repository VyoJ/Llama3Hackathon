Title: Slack Reader - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/data_connectors/SlackDemo/

Markdown Content:
Slack Reader - LlamaIndex


Demonstrates our Slack data connector

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-readers\-slack

%pip install llama-index-readers-slack

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

from llama\_index.core import SummaryIndex
from llama\_index.readers.slack import SlackReader
from IPython.display import Markdown, display
import os

from llama\_index.core import SummaryIndex from llama\_index.readers.slack import SlackReader from IPython.display import Markdown, display import os

Load data using Channel IDs

In \[ \]:

Copied!

slack\_token \= os.getenv("SLACK\_BOT\_TOKEN")
channel\_ids \= \["<channel\_id>"\]
documents \= SlackReader(slack\_token\=slack\_token).load\_data(
    channel\_ids\=channel\_ids
)

slack\_token = os.getenv("SLACK\_BOT\_TOKEN") channel\_ids = \[""\] documents = SlackReader(slack\_token=slack\_token).load\_data( channel\_ids=channel\_ids )

Load data using Channel Names/Regex Patterns

In \[ \]:

Copied!

slack\_token \= os.getenv("SLACK\_BOT\_TOKEN")
channel\_patterns \= \["<channel\_name>", "<regex\_pattern>"\]
slack\_reader \= SlackReader(slack\_token\=slack\_token)
channel\_ids \= slack\_reader.get\_channel\_ids(channel\_patterns\=channel\_patterns)
documents \= slack\_reader.load\_data(channel\_ids\=channel\_ids)

slack\_token = os.getenv("SLACK\_BOT\_TOKEN") channel\_patterns = \["", ""\] slack\_reader = SlackReader(slack\_token=slack\_token) channel\_ids = slack\_reader.get\_channel\_ids(channel\_patterns=channel\_patterns) documents = slack\_reader.load\_data(channel\_ids=channel\_ids)

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

[Previous Qdrant Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/QdrantDemo/)[Next Twitter Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/TwitterDemo/)
