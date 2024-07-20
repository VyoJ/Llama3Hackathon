Title: Discord Reader - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/data_connectors/DiscordDemo/

Markdown Content:
Discord Reader - LlamaIndex


Demonstrates our Discord data connector

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-readers\-discord

%pip install llama-index-readers-discord

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

\# This is due to the fact that we use asyncio.loop\_until\_complete in
\# the DiscordReader. Since the Jupyter kernel itself runs on
\# an event loop, we need to add some help with nesting
!pip install nest\_asyncio
import nest\_asyncio

nest\_asyncio.apply()

\# This is due to the fact that we use asyncio.loop\_until\_complete in # the DiscordReader. Since the Jupyter kernel itself runs on # an event loop, we need to add some help with nesting !pip install nest\_asyncio import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

from llama\_index.core import SummaryIndex
from llama\_index.readers.discord import DiscordReader
from IPython.display import Markdown, display
import os

from llama\_index.core import SummaryIndex from llama\_index.readers.discord import DiscordReader from IPython.display import Markdown, display import os

In \[ \]:

Copied!

discord\_token \= os.getenv("DISCORD\_TOKEN")
channel\_ids \= \[1057178784895348746\]  \# Replace with your channel\_id
documents \= DiscordReader(discord\_token\=discord\_token).load\_data(
    channel\_ids\=channel\_ids
)

discord\_token = os.getenv("DISCORD\_TOKEN") channel\_ids = \[1057178784895348746\] # Replace with your channel\_id documents = DiscordReader(discord\_token=discord\_token).load\_data( channel\_ids=channel\_ids )

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

[Previous DeepLake Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/DeepLakeReader/)[Next Faiss Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/FaissDemo/)
