Title: Docstore Demo - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/docstore/DocstoreDemo/

Markdown Content:
Docstore Demo - LlamaIndex


This guide shows you how to directly use our `DocumentStore` abstraction. By putting nodes in the docstore, this allows you to define multiple indices over the same underlying docstore, instead of duplicating data across indices.

[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jerryjliu/llama_index/blob/main/docs/docs/examples/docstore/DocstoreDemo.ipynb)

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai

%pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import nest\_asyncio

nest\_asyncio.apply()

import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader
from llama\_index.core import VectorStoreIndex, SimpleKeywordTableIndex
from llama\_index.core import SummaryIndex
from llama\_index.core import ComposableGraph
from llama\_index.llms.openai import OpenAI
from llama\_index.core import Settings

from llama\_index.core import SimpleDirectoryReader from llama\_index.core import VectorStoreIndex, SimpleKeywordTableIndex from llama\_index.core import SummaryIndex from llama\_index.core import ComposableGraph from llama\_index.llms.openai import OpenAI from llama\_index.core import Settings

#### Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/docstore/DocstoreDemo/#download-data)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

#### Load Documents[¶](https://docs.llamaindex.ai/en/stable/examples/docstore/DocstoreDemo/#load-documents)

In \[ \]:

Copied!

reader \= SimpleDirectoryReader("./data/paul\_graham/")
documents \= reader.load\_data()

reader = SimpleDirectoryReader("./data/paul\_graham/") documents = reader.load\_data()

#### Parse into Nodes[¶](https://docs.llamaindex.ai/en/stable/examples/docstore/DocstoreDemo/#parse-into-nodes)

In \[ \]:

Copied!

from llama\_index.core.node\_parser import SentenceSplitter

nodes \= SentenceSplitter().get\_nodes\_from\_documents(documents)

from llama\_index.core.node\_parser import SentenceSplitter nodes = SentenceSplitter().get\_nodes\_from\_documents(documents)

#### Add to Docstore[¶](https://docs.llamaindex.ai/en/stable/examples/docstore/DocstoreDemo/#add-to-docstore)

In \[ \]:

Copied!

from llama\_index.core.storage.docstore import SimpleDocumentStore

docstore \= SimpleDocumentStore()
docstore.add\_documents(nodes)

from llama\_index.core.storage.docstore import SimpleDocumentStore docstore = SimpleDocumentStore() docstore.add\_documents(nodes)

#### Define Multiple Indexes[¶](https://docs.llamaindex.ai/en/stable/examples/docstore/DocstoreDemo/#define-multiple-indexes)

Each index uses the same underlying Node.

In \[ \]:

Copied!

from llama\_index.core import StorageContext

storage\_context \= StorageContext.from\_defaults(docstore\=docstore)
summary\_index \= SummaryIndex(nodes, storage\_context\=storage\_context)
vector\_index \= VectorStoreIndex(nodes, storage\_context\=storage\_context)
keyword\_table\_index \= SimpleKeywordTableIndex(
    nodes, storage\_context\=storage\_context
)

from llama\_index.core import StorageContext storage\_context = StorageContext.from\_defaults(docstore=docstore) summary\_index = SummaryIndex(nodes, storage\_context=storage\_context) vector\_index = VectorStoreIndex(nodes, storage\_context=storage\_context) keyword\_table\_index = SimpleKeywordTableIndex( nodes, storage\_context=storage\_context )

In \[ \]:

Copied!

\# NOTE: the docstore sitll has the same nodes
len(storage\_context.docstore.docs)

\# NOTE: the docstore sitll has the same nodes len(storage\_context.docstore.docs)

Out\[ \]:

6

#### Test out some Queries[¶](https://docs.llamaindex.ai/en/stable/examples/docstore/DocstoreDemo/#test-out-some-queries)

In \[ \]:

Copied!

llm \= OpenAI(temperature\=0, model\="gpt-3.5-turbo")

Settings.llm \= llm
Settings.chunk\_size \= 1024

llm = OpenAI(temperature=0, model="gpt-3.5-turbo") Settings.llm = llm Settings.chunk\_size = 1024

WARNING:llama\_index.llm\_predictor.base:Unknown max input size for gpt-3.5-turbo, using defaults.
Unknown max input size for gpt-3.5-turbo, using defaults.

In \[ \]:

Copied!

query\_engine \= summary\_index.as\_query\_engine()
response \= query\_engine.query("What is a summary of this document?")

query\_engine = summary\_index.as\_query\_engine() response = query\_engine.query("What is a summary of this document?")

In \[ \]:

Copied!

query\_engine \= vector\_index.as\_query\_engine()
response \= query\_engine.query("What did the author do growing up?")

query\_engine = vector\_index.as\_query\_engine() response = query\_engine.query("What did the author do growing up?")

In \[ \]:

Copied!

query\_engine \= keyword\_table\_index.as\_query\_engine()
response \= query\_engine.query("What did the author do after his time at YC?")

query\_engine = keyword\_table\_index.as\_query\_engine() response = query\_engine.query("What did the author do after his time at YC?")

In \[ \]:

Copied!

print(response)

print(response)

After his time at YC, the author decided to take a break and focus on painting. He spent most of 2014 painting and then, in November, he ran out of steam and stopped. He then moved to Florence, Italy to attend the Accademia di Belle Arti di Firenze, where he studied painting and drawing. He also started painting still lives in his bedroom at night. In March 2015, he started working on Lisp again and wrote a new Lisp, called Bel, in itself in Arc. He wrote essays through 2020, but also started to think about other things he could work on. He wrote an essay for himself to answer the question of how he should choose what to do next and then wrote a more detailed version for others to read. He also created the Y Combinator logo, which was an inside joke referencing the Viaweb logo, a white V on a red circle, so he made the YC logo a white Y on an orange square. He also created a fund for YC for a couple of years, but after Heroku got bought, he had enough money to go back to being self-funded. He also disliked the term "deal flow" because it implies that the number of new startups at any given time

Back to top

[Previous Demo: Azure Table Storage as a Docstore](https://docs.llamaindex.ai/en/stable/examples/docstore/AzureDocstoreDemo/)[Next Dynamo DB Docstore Demo](https://docs.llamaindex.ai/en/stable/examples/docstore/DynamoDBDocstoreDemo/)
