Title: DeepLake Reader - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/data_connectors/DeepLakeReader/

Markdown Content:
DeepLake Reader - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-readers\-deeplake

%pip install llama-index-readers-deeplake

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import getpass
import os
import random
import textwrap

from llama\_index.core import VectorStoreIndex
from llama\_index.readers.deeplake import DeepLakeReader

os.environ\["OPENAI\_API\_KEY"\] \= getpass.getpass("open ai api key: ")

import getpass import os import random import textwrap from llama\_index.core import VectorStoreIndex from llama\_index.readers.deeplake import DeepLakeReader os.environ\["OPENAI\_API\_KEY"\] = getpass.getpass("open ai api key: ")

In \[ \]:

Copied!

reader \= DeepLakeReader()
query\_vector \= \[random.random() for \_ in range(1536)\]
documents \= reader.load\_data(
    query\_vector\=query\_vector,
    dataset\_path\="hub://activeloop/paul\_graham\_essay",
    limit\=5,
)

reader = DeepLakeReader() query\_vector = \[random.random() for \_ in range(1536)\] documents = reader.load\_data( query\_vector=query\_vector, dataset\_path="hub://activeloop/paul\_graham\_essay", limit=5, )

/Users/adilkhansarsen/Documents/work/LlamaIndex/llama\_index/GPTIndex/lib/python3.9/site-packages/deeplake/util/warnings.py:7: UserWarning: Checking out dataset in read only mode as another machine has locked this version for writing.
  warnings.warn(\*args, \*\*kwargs)

-

This dataset can be visualized in Jupyter Notebook by ds.visualize() or at https://app.activeloop.ai/activeloop/paul\_graham\_essay

\\

hub://activeloop/paul\_graham\_essay loaded successfully.

In \[ \]:

Copied!

index \= VectorStoreIndex.from\_documents(documents)
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What was a hard moment for the author?")
print(textwrap.fill(str(response), 100))

index = VectorStoreIndex.from\_documents(documents) query\_engine = index.as\_query\_engine() response = query\_engine.query("What was a hard moment for the author?") print(textwrap.fill(str(response), 100))

INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total embedding token usage: 14220 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[query\] Total LLM token usage: 3975 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[query\] Total embedding token usage: 9 tokens

 A hard moment for the author was when he realized that the AI programs of the time were not going
to be able to understand natural language and bridge the gap between what they could do and actually
understanding natural language. He had expected college to help him understand the ultimate truths,
but instead he found that the other fields took up so much of the space of ideas that there wasn't
much left for these supposed ultimate truths. He also found himself in a situation where the
students and faculty had an arrangement that didn't require either to learn or teach anything, and
he was the only one painting the nude model. He was also painting still lives in his bedroom at
night on scraps of canvas due to his financial situation.

Back to top

[Previous Database Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/DatabaseReaderDemo/)[Next Discord Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/DiscordDemo/)
