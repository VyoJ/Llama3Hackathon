Title: DashVector Reader - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/data_connectors/DashvectorReaderDemo/

Markdown Content:
DashVector Reader - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-readers\-dashvector

%pip install llama-index-readers-dashvector

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import logging
import sys
import os

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys import os logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

In \[ \]:

Copied!

api\_key \= os.environ\["DASHVECTOR\_API\_KEY"\]

api\_key = os.environ\["DASHVECTOR\_API\_KEY"\]

In \[ \]:

Copied!

from llama\_index.readers.dashvector import DashVectorReader

reader \= DashVectorReader(api\_key\=api\_key)

from llama\_index.readers.dashvector import DashVectorReader reader = DashVectorReader(api\_key=api\_key)

In \[ \]:

Copied!

import numpy as np

\# the id\_to\_text\_map specifies a mapping from the ID specified in DashVector to your text.
id\_to\_text\_map \= {
    "id1": "text blob 1",
    "id2": "text blob 2",
}

\# the query\_vector is an embedding representation of your query\_vector
query\_vector \= \[n1, n2, n3, ...\]

import numpy as np # the id\_to\_text\_map specifies a mapping from the ID specified in DashVector to your text. id\_to\_text\_map = { "id1": "text blob 1", "id2": "text blob 2", } # the query\_vector is an embedding representation of your query\_vector query\_vector = \[n1, n2, n3, ...\]

In \[ \]:

Copied!

\# NOTE: Required args are index\_name, id\_to\_text\_map, vector.
\# In addition, we can pass through the metadata filter that meet the SQL syntax.
\# See the Python client: https://pypi.org/project/dashvector/ for more details.
documents \= reader.load\_data(
    collection\_name\="quickstart",
    id\_to\_text\_map\=id\_to\_text\_map,
    top\_k\=3,
    vector\=query\_vector,
    filter\="key = 'value'",
)

\# NOTE: Required args are index\_name, id\_to\_text\_map, vector. # In addition, we can pass through the metadata filter that meet the SQL syntax. # See the Python client: https://pypi.org/project/dashvector/ for more details. documents = reader.load\_data( collection\_name="quickstart", id\_to\_text\_map=id\_to\_text\_map, top\_k=3, vector=query\_vector, filter="key = 'value'", )

### Create index[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/DashvectorReaderDemo/#create-index)

In \[ \]:

Copied!

from llama\_index.core import ListIndex
from IPython.display import Markdown, display

index \= ListIndex.from\_documents(documents)

from llama\_index.core import ListIndex from IPython.display import Markdown, display index = ListIndex.from\_documents(documents)

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

[Previous Chroma Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/ChromaDemo/)[Next Database Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/DatabaseReaderDemo/)
