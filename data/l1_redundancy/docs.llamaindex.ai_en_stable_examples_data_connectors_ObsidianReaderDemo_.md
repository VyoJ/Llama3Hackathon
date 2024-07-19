Title: Obsidian Reader - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/data_connectors/ObsidianReaderDemo/

Markdown Content:
Obsidian Reader - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-readers\-obsidian

%pip install llama-index-readers-obsidian

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

%env OPENAI\_API\_KEY\=sk\-\*\*\*\*\*\*\*\*\*\*\*\*

%env OPENAI\_API\_KEY=sk-\*\*\*\*\*\*\*\*\*\*\*\*

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

In \[ \]:

Copied!

from llama\_index.readers.obsidian import ObsidianReader
from llama\_index.core import VectorStoreIndex

from llama\_index.readers.obsidian import ObsidianReader from llama\_index.core import VectorStoreIndex

In \[ \]:

Copied!

documents \= ObsidianReader(
    "/Users/hursh/vault"
).load\_data()  \# Returns list of documents

documents = ObsidianReader( "/Users/hursh/vault" ).load\_data() # Returns list of documents

In \[ \]:

Copied!

index \= VectorStoreIndex.from\_documents(
    documents
)  \# Initialize index with documents

index = VectorStoreIndex.from\_documents( documents ) # Initialize index with documents

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine()
res \= query\_engine.query("What is the meaning of life?")

\# set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine() res = query\_engine.query("What is the meaning of life?")

\> \[query\] Total LLM token usage: 920 tokens
> \[query\] Total embedding token usage: 7 tokens

In \[ \]:

Copied!

res.response

res.response

Out\[ \]:

'\\nThe meaning of life is subjective and can vary from person to person. It is ultimately up to each individual to decide what they believe is the purpose and value of life. Some may find meaning in their faith, while others may find it in their relationships, work, or hobbies. Ultimately, it is up to each individual to decide what brings them joy and fulfillment and to pursue that path.'

Back to top

[Previous Notion Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/NotionDemo/)[Next Pathway Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/PathwayReaderDemo/)
