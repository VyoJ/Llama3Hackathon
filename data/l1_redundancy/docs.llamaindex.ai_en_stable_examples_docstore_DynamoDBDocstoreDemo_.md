Title: Dynamo DB Docstore Demo - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/docstore/DynamoDBDocstoreDemo/

Markdown Content:
Dynamo DB Docstore Demo - LlamaIndex


This guide shows you how to directly use our `DocumentStore` abstraction backed by DynamoDB. By putting nodes in the docstore, this allows you to define multiple indices over the same underlying docstore, instead of duplicating data across indices.

[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jerryjliu/llama_index/blob/main/docs/docs/examples/docstore/DynamoDBDocstoreDemo.ipynb)

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-storage\-docstore\-dynamodb
%pip install llama\-index\-storage\-index\-store\-dynamodb
%pip install llama\-index\-vector\-stores\-dynamodb
%pip install llama\-index\-llms\-openai

%pip install llama-index-storage-docstore-dynamodb %pip install llama-index-storage-index-store-dynamodb %pip install llama-index-vector-stores-dynamodb %pip install llama-index-llms-openai

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
import os

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys import os logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader, StorageContext
from llama\_index.core import VectorStoreIndex, SimpleKeywordTableIndex
from llama\_index.core import SummaryIndex
from llama\_index.llms.openai import OpenAI
from llama\_index.core.response.notebook\_utils import display\_response
from llama\_index.core import Settings

from llama\_index.core import SimpleDirectoryReader, StorageContext from llama\_index.core import VectorStoreIndex, SimpleKeywordTableIndex from llama\_index.core import SummaryIndex from llama\_index.llms.openai import OpenAI from llama\_index.core.response.notebook\_utils import display\_response from llama\_index.core import Settings

#### Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/docstore/DynamoDBDocstoreDemo/#download-data)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

#### Load Documents[¶](https://docs.llamaindex.ai/en/stable/examples/docstore/DynamoDBDocstoreDemo/#load-documents)

In \[ \]:

Copied!

reader \= SimpleDirectoryReader("./data/paul\_graham/")
documents \= reader.load\_data()

reader = SimpleDirectoryReader("./data/paul\_graham/") documents = reader.load\_data()

#### Parse into Nodes[¶](https://docs.llamaindex.ai/en/stable/examples/docstore/DynamoDBDocstoreDemo/#parse-into-nodes)

In \[ \]:

Copied!

from llama\_index.core.node\_parser import SentenceSplitter

nodes \= SentenceSplitter().get\_nodes\_from\_documents(documents)

from llama\_index.core.node\_parser import SentenceSplitter nodes = SentenceSplitter().get\_nodes\_from\_documents(documents)

#### Add to Docstore[¶](https://docs.llamaindex.ai/en/stable/examples/docstore/DynamoDBDocstoreDemo/#add-to-docstore)

In \[ \]:

Copied!

TABLE\_NAME \= os.environ\["DYNAMODB\_TABLE\_NAME"\]

TABLE\_NAME = os.environ\["DYNAMODB\_TABLE\_NAME"\]

In \[ \]:

Copied!

from llama\_index.storage.docstore.dynamodb import DynamoDBDocumentStore
from llama\_index.storage.index\_store.dynamodb import DynamoDBIndexStore
from llama\_index.vector\_stores.dynamodb import DynamoDBVectorStore

from llama\_index.storage.docstore.dynamodb import DynamoDBDocumentStore from llama\_index.storage.index\_store.dynamodb import DynamoDBIndexStore from llama\_index.vector\_stores.dynamodb import DynamoDBVectorStore

In \[ \]:

Copied!

storage\_context \= StorageContext.from\_defaults(
    docstore\=DynamoDBDocumentStore.from\_table\_name(table\_name\=TABLE\_NAME),
    index\_store\=DynamoDBIndexStore.from\_table\_name(table\_name\=TABLE\_NAME),
    vector\_store\=DynamoDBVectorStore.from\_table\_name(table\_name\=TABLE\_NAME),
)

storage\_context = StorageContext.from\_defaults( docstore=DynamoDBDocumentStore.from\_table\_name(table\_name=TABLE\_NAME), index\_store=DynamoDBIndexStore.from\_table\_name(table\_name=TABLE\_NAME), vector\_store=DynamoDBVectorStore.from\_table\_name(table\_name=TABLE\_NAME), )

In \[ \]:

Copied!

storage\_context.docstore.add\_documents(nodes)

storage\_context.docstore.add\_documents(nodes)

#### Define & Add Multiple Indexes[¶](https://docs.llamaindex.ai/en/stable/examples/docstore/DynamoDBDocstoreDemo/#define-add-multiple-indexes)

Each index uses the same underlying Node.

In \[ \]:

Copied!

\# https://gpt-index.readthedocs.io/en/latest/api\_reference/indices/list.html
summary\_index \= SummaryIndex(nodes, storage\_context\=storage\_context)

\# https://gpt-index.readthedocs.io/en/latest/api\_reference/indices/list.html summary\_index = SummaryIndex(nodes, storage\_context=storage\_context)

In \[ \]:

Copied!

\# https://gpt-index.readthedocs.io/en/latest/api\_reference/indices/vector\_store.html
vector\_index \= VectorStoreIndex(nodes, storage\_context\=storage\_context)

\# https://gpt-index.readthedocs.io/en/latest/api\_reference/indices/vector\_store.html vector\_index = VectorStoreIndex(nodes, storage\_context=storage\_context)

In \[ \]:

Copied!

\# https://gpt-index.readthedocs.io/en/latest/api\_reference/indices/table.html
keyword\_table\_index \= SimpleKeywordTableIndex(
    nodes, storage\_context\=storage\_context
)

\# https://gpt-index.readthedocs.io/en/latest/api\_reference/indices/table.html keyword\_table\_index = SimpleKeywordTableIndex( nodes, storage\_context=storage\_context )

In \[ \]:

Copied!

\# NOTE: the docstore still has the same nodes
len(storage\_context.docstore.docs)

\# NOTE: the docstore still has the same nodes len(storage\_context.docstore.docs)

#### Test out saving and loading[¶](https://docs.llamaindex.ai/en/stable/examples/docstore/DynamoDBDocstoreDemo/#test-out-saving-and-loading)

In \[ \]:

Copied!

\# NOTE: docstore, index\_store, and vector\_index is persisted in DynamoDB by default when they are created
\# NOTE: You can also persist simple vector store to disk by using the command below
storage\_context.persist()

\# NOTE: docstore, index\_store, and vector\_index is persisted in DynamoDB by default when they are created # NOTE: You can also persist simple vector store to disk by using the command below storage\_context.persist()

In \[ \]:

Copied!

\# note down index IDs
list\_id \= summary\_index.index\_id
vector\_id \= vector\_index.index\_id
keyword\_id \= keyword\_table\_index.index\_id

\# note down index IDs list\_id = summary\_index.index\_id vector\_id = vector\_index.index\_id keyword\_id = keyword\_table\_index.index\_id

In \[ \]:

Copied!

from llama\_index.core import load\_index\_from\_storage

\# re-create storage context
storage\_context \= StorageContext.from\_defaults(
    docstore\=DynamoDBDocumentStore.from\_table\_name(table\_name\=TABLE\_NAME),
    index\_store\=DynamoDBIndexStore.from\_table\_name(table\_name\=TABLE\_NAME),
    vector\_store\=DynamoDBVectorStore.from\_table\_name(table\_name\=TABLE\_NAME),
)

summary\_index \= load\_index\_from\_storage(
    storage\_context\=storage\_context, index\_id\=list\_id
)
keyword\_table\_index \= load\_index\_from\_storage(
    storage\_context\=storage\_context, index\_id\=keyword\_id
)

\# You need to add "vector\_store=DynamoDBVectorStore.from\_table\_name(table\_name=TABLE\_NAME)" to StorageContext to load vector index from DynamoDB
vector\_index \= load\_index\_from\_storage(
    storage\_context\=storage\_context, index\_id\=vector\_id
)

from llama\_index.core import load\_index\_from\_storage # re-create storage context storage\_context = StorageContext.from\_defaults( docstore=DynamoDBDocumentStore.from\_table\_name(table\_name=TABLE\_NAME), index\_store=DynamoDBIndexStore.from\_table\_name(table\_name=TABLE\_NAME), vector\_store=DynamoDBVectorStore.from\_table\_name(table\_name=TABLE\_NAME), ) summary\_index = load\_index\_from\_storage( storage\_context=storage\_context, index\_id=list\_id ) keyword\_table\_index = load\_index\_from\_storage( storage\_context=storage\_context, index\_id=keyword\_id ) # You need to add "vector\_store=DynamoDBVectorStore.from\_table\_name(table\_name=TABLE\_NAME)" to StorageContext to load vector index from DynamoDB vector\_index = load\_index\_from\_storage( storage\_context=storage\_context, index\_id=vector\_id )

#### Test out some Queries[¶](https://docs.llamaindex.ai/en/stable/examples/docstore/DynamoDBDocstoreDemo/#test-out-some-queries)

In \[ \]:

Copied!

chatgpt \= OpenAI(temperature\=0, model\="gpt-3.5-turbo")

Settings.llm \= chatgpt
Settings.chunk\_size \= 1024

chatgpt = OpenAI(temperature=0, model="gpt-3.5-turbo") Settings.llm = chatgpt Settings.chunk\_size = 1024

In \[ \]:

Copied!

query\_engine \= summary\_index.as\_query\_engine()
list\_response \= query\_engine.query("What is a summary of this document?")

query\_engine = summary\_index.as\_query\_engine() list\_response = query\_engine.query("What is a summary of this document?")

In \[ \]:

Copied!

display\_response(list\_response)

display\_response(list\_response)

In \[ \]:

Copied!

query\_engine \= vector\_index.as\_query\_engine()
vector\_response \= query\_engine.query("What did the author do growing up?")

query\_engine = vector\_index.as\_query\_engine() vector\_response = query\_engine.query("What did the author do growing up?")

In \[ \]:

Copied!

display\_response(vector\_response)

display\_response(vector\_response)

In \[ \]:

Copied!

query\_engine \= keyword\_table\_index.as\_query\_engine()
keyword\_response \= query\_engine.query(
    "What did the author do after his time at YC?"
)

query\_engine = keyword\_table\_index.as\_query\_engine() keyword\_response = query\_engine.query( "What did the author do after his time at YC?" )

In \[ \]:

Copied!

display\_response(keyword\_response)

display\_response(keyword\_response)

Back to top

[Previous Docstore Demo](https://docs.llamaindex.ai/en/stable/examples/docstore/DocstoreDemo/)[Next Firestore Demo](https://docs.llamaindex.ai/en/stable/examples/docstore/FirestoreDemo/)
