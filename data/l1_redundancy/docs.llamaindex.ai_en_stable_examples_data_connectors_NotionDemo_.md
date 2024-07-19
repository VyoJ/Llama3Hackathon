Title: Notion Reader - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/data_connectors/NotionDemo/

Markdown Content:
Notion Reader - LlamaIndex


Demonstrates our Notion data connector

In \[ \]:

Copied!

%pip install llama\-index\-readers\-notion

%pip install llama-index-readers-notion

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

from llama\_index.core import SummaryIndex
from llama\_index.readers.notion import NotionPageReader
from IPython.display import Markdown, display
import os

from llama\_index.core import SummaryIndex from llama\_index.readers.notion import NotionPageReader from IPython.display import Markdown, display import os

In \[ \]:

Copied!

integration\_token \= os.getenv("NOTION\_INTEGRATION\_TOKEN")
page\_ids \= \["<page\_id>"\]
documents \= NotionPageReader(integration\_token\=integration\_token).load\_data(
    page\_ids\=page\_ids
)

integration\_token = os.getenv("NOTION\_INTEGRATION\_TOKEN") page\_ids = \[""\] documents = NotionPageReader(integration\_token=integration\_token).load\_data( page\_ids=page\_ids )

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

You can also pass the id of a database to index all the pages in that database:

In \[ \]:

Copied!

database\_id \= "<database-id>"

\# https://developers.notion.com/docs/working-with-databases for how to find your database id

documents \= NotionPageReader(integration\_token\=integration\_token).load\_data(
    database\_id\=database\_id
)

print(documents)

database\_id = "" # https://developers.notion.com/docs/working-with-databases for how to find your database id documents = NotionPageReader(integration\_token=integration\_token).load\_data( database\_id=database\_id ) print(documents)

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
index \= SummaryIndex.from\_documents(documents)
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("<query\_text>")
display(Markdown(f"<b>{response}</b>"))

\# set Logging to DEBUG for more detailed outputs index = SummaryIndex.from\_documents(documents) query\_engine = index.as\_query\_engine() response = query\_engine.query("") display(Markdown(f"**{response}**"))

To list all databases in your Notion workspace:

In \[ \]:

Copied!

reader \= NotionPageReader(integration\_token\=integration\_token)
databases \= reader.list\_databases()
print(databases)

reader = NotionPageReader(integration\_token=integration\_token) databases = reader.list\_databases() print(databases)

Back to top

[Previous MyScale Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/MyScaleReaderDemo/)[Next Obsidian Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/ObsidianReaderDemo/)
