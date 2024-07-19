Title: Redis Docstore+Index Store Demo - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/docstore/RedisDocstoreIndexStoreDemo/

Markdown Content:
Redis Docstore+Index Store Demo - LlamaIndex


This guide shows you how to directly use our `DocumentStore` abstraction and `IndexStore` abstraction backed by Redis. By putting nodes in the docstore, this allows you to define multiple indices over the same underlying docstore, instead of duplicating data across indices.

The index itself is also stored in Redis through the `IndexStore`.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-storage\-docstore\-redis
%pip install llama\-index\-storage\-index\-store\-redis
%pip install llama\-index\-llms\-openai

%pip install llama-index-storage-docstore-redis %pip install llama-index-storage-index-store-redis %pip install llama-index-llms-openai

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
from llama\_index.core import ComposableGraph
from llama\_index.llms.openai import OpenAI
from llama\_index.core.response.notebook\_utils import display\_response
from llama\_index.core import Settings

from llama\_index.core import SimpleDirectoryReader, StorageContext from llama\_index.core import VectorStoreIndex, SimpleKeywordTableIndex from llama\_index.core import SummaryIndex from llama\_index.core import ComposableGraph from llama\_index.llms.openai import OpenAI from llama\_index.core.response.notebook\_utils import display\_response from llama\_index.core import Settings

INFO:numexpr.utils:Note: NumExpr detected 16 cores but "NUMEXPR\_MAX\_THREADS" not set, so enforcing safe limit of 8.
Note: NumExpr detected 16 cores but "NUMEXPR\_MAX\_THREADS" not set, so enforcing safe limit of 8.
INFO:numexpr.utils:NumExpr defaulting to 8 threads.
NumExpr defaulting to 8 threads.

/home/loganm/miniconda3/envs/llama-index/lib/python3.11/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user\_install.html
  from .autonotebook import tqdm as notebook\_tqdm

#### Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/docstore/RedisDocstoreIndexStoreDemo/#download-data)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

#### Load Documents[¶](https://docs.llamaindex.ai/en/stable/examples/docstore/RedisDocstoreIndexStoreDemo/#load-documents)

In \[ \]:

Copied!

reader \= SimpleDirectoryReader("./data/paul\_graham/")
documents \= reader.load\_data()

reader = SimpleDirectoryReader("./data/paul\_graham/") documents = reader.load\_data()

#### Parse into Nodes[¶](https://docs.llamaindex.ai/en/stable/examples/docstore/RedisDocstoreIndexStoreDemo/#parse-into-nodes)

In \[ \]:

Copied!

from llama\_index.core.node\_parser import SentenceSplitter

nodes \= SentenceSplitter().get\_nodes\_from\_documents(documents)

from llama\_index.core.node\_parser import SentenceSplitter nodes = SentenceSplitter().get\_nodes\_from\_documents(documents)

#### Add to Docstore[¶](https://docs.llamaindex.ai/en/stable/examples/docstore/RedisDocstoreIndexStoreDemo/#add-to-docstore)

In \[ \]:

Copied!

REDIS\_HOST \= os.getenv("REDIS\_HOST", "127.0.0.1")
REDIS\_PORT \= os.getenv("REDIS\_PORT", 6379)

REDIS\_HOST = os.getenv("REDIS\_HOST", "127.0.0.1") REDIS\_PORT = os.getenv("REDIS\_PORT", 6379)

In \[ \]:

Copied!

from llama\_index.storage.docstore.redis import RedisDocumentStore
from llama\_index.storage.index\_store.redis import RedisIndexStore

from llama\_index.storage.docstore.redis import RedisDocumentStore from llama\_index.storage.index\_store.redis import RedisIndexStore

/home/loganm/miniconda3/envs/llama-index/lib/python3.11/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user\_install.html
  from .autonotebook import tqdm as notebook\_tqdm

In \[ \]:

Copied!

storage\_context \= StorageContext.from\_defaults(
    docstore\=RedisDocumentStore.from\_host\_and\_port(
        host\=REDIS\_HOST, port\=REDIS\_PORT, namespace\="llama\_index"
    ),
    index\_store\=RedisIndexStore.from\_host\_and\_port(
        host\=REDIS\_HOST, port\=REDIS\_PORT, namespace\="llama\_index"
    ),
)

storage\_context = StorageContext.from\_defaults( docstore=RedisDocumentStore.from\_host\_and\_port( host=REDIS\_HOST, port=REDIS\_PORT, namespace="llama\_index" ), index\_store=RedisIndexStore.from\_host\_and\_port( host=REDIS\_HOST, port=REDIS\_PORT, namespace="llama\_index" ), )

In \[ \]:

Copied!

storage\_context.docstore.add\_documents(nodes)

storage\_context.docstore.add\_documents(nodes)

In \[ \]:

Copied!

len(storage\_context.docstore.docs)

len(storage\_context.docstore.docs)

Out\[ \]:

20

#### Define Multiple Indexes[¶](https://docs.llamaindex.ai/en/stable/examples/docstore/RedisDocstoreIndexStoreDemo/#define-multiple-indexes)

Each index uses the same underlying Node.

In \[ \]:

Copied!

summary\_index \= SummaryIndex(nodes, storage\_context\=storage\_context)

summary\_index = SummaryIndex(nodes, storage\_context=storage\_context)

INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total embedding token usage: 0 tokens
> \[build\_index\_from\_nodes\] Total embedding token usage: 0 tokens

In \[ \]:

Copied!

vector\_index \= VectorStoreIndex(nodes, storage\_context\=storage\_context)

vector\_index = VectorStoreIndex(nodes, storage\_context=storage\_context)

INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total embedding token usage: 17050 tokens
> \[build\_index\_from\_nodes\] Total embedding token usage: 17050 tokens

In \[ \]:

Copied!

keyword\_table\_index \= SimpleKeywordTableIndex(
    nodes, storage\_context\=storage\_context
)

keyword\_table\_index = SimpleKeywordTableIndex( nodes, storage\_context=storage\_context )

INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total embedding token usage: 0 tokens
> \[build\_index\_from\_nodes\] Total embedding token usage: 0 tokens

In \[ \]:

Copied!

\# NOTE: the docstore still has the same nodes
len(storage\_context.docstore.docs)

\# NOTE: the docstore still has the same nodes len(storage\_context.docstore.docs)

Out\[ \]:

20

#### Test out saving and loading[¶](https://docs.llamaindex.ai/en/stable/examples/docstore/RedisDocstoreIndexStoreDemo/#test-out-saving-and-loading)

In \[ \]:

Copied!

\# NOTE: docstore and index\_store is persisted in Redis by default
\# NOTE: here only need to persist simple vector store to disk
storage\_context.persist(persist\_dir\="./storage")

\# NOTE: docstore and index\_store is persisted in Redis by default # NOTE: here only need to persist simple vector store to disk storage\_context.persist(persist\_dir="./storage")

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
    docstore\=RedisDocumentStore.from\_host\_and\_port(
        host\=REDIS\_HOST, port\=REDIS\_PORT, namespace\="llama\_index"
    ),
    index\_store\=RedisIndexStore.from\_host\_and\_port(
        host\=REDIS\_HOST, port\=REDIS\_PORT, namespace\="llama\_index"
    ),
)

\# load indices
summary\_index \= load\_index\_from\_storage(
    storage\_context\=storage\_context, index\_id\=list\_id
)
vector\_index \= load\_index\_from\_storage(
    storage\_context\=storage\_context, index\_id\=vector\_id
)
keyword\_table\_index \= load\_index\_from\_storage(
    storage\_context\=storage\_context, index\_id\=keyword\_id
)

from llama\_index.core import load\_index\_from\_storage # re-create storage context storage\_context = StorageContext.from\_defaults( docstore=RedisDocumentStore.from\_host\_and\_port( host=REDIS\_HOST, port=REDIS\_PORT, namespace="llama\_index" ), index\_store=RedisIndexStore.from\_host\_and\_port( host=REDIS\_HOST, port=REDIS\_PORT, namespace="llama\_index" ), ) # load indices summary\_index = load\_index\_from\_storage( storage\_context=storage\_context, index\_id=list\_id ) vector\_index = load\_index\_from\_storage( storage\_context=storage\_context, index\_id=vector\_id ) keyword\_table\_index = load\_index\_from\_storage( storage\_context=storage\_context, index\_id=keyword\_id )

INFO:llama\_index.indices.loading:Loading indices with ids: \['24e98f9b-9586-4fc6-8341-8dce895e5bcc'\]
Loading indices with ids: \['24e98f9b-9586-4fc6-8341-8dce895e5bcc'\]
INFO:llama\_index.indices.loading:Loading indices with ids: \['f7b2aeb3-4dad-4750-8177-78d5ae706284'\]
Loading indices with ids: \['f7b2aeb3-4dad-4750-8177-78d5ae706284'\]
INFO:llama\_index.indices.loading:Loading indices with ids: \['9a9198b4-7cb9-4c96-97a7-5f404f43b9cd'\]
Loading indices with ids: \['9a9198b4-7cb9-4c96-97a7-5f404f43b9cd'\]

#### Test out some Queries[¶](https://docs.llamaindex.ai/en/stable/examples/docstore/RedisDocstoreIndexStoreDemo/#test-out-some-queries)

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

INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total LLM token usage: 26111 tokens
> \[get\_response\] Total LLM token usage: 26111 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total embedding token usage: 0 tokens
> \[get\_response\] Total embedding token usage: 0 tokens

In \[ \]:

Copied!

display\_response(list\_response)

display\_response(list\_response)

**`Final Response:`** This document is a narrative of the author's journey from writing and programming as a young person to pursuing a career in art. It describes his experiences in high school, college, and graduate school, and how he eventually decided to pursue art as a career. He applied to art schools and eventually was accepted to RISD and the Accademia di Belli Arti in Florence. He passed the entrance exam for the Accademia and began studying art there. He then moved to New York and worked freelance while writing a book on Lisp. He eventually started a company to put art galleries online, but it was unsuccessful. He then pivoted to creating software to build online stores, which eventually became successful. He had the idea to run the software on the server and let users control it by clicking on links, which meant users wouldn't need anything more than a browser. This kind of software, known as "internet storefronts," was eventually successful. He and his team worked hard to make the software user-friendly and inexpensive, and eventually the company was bought by Yahoo. After the sale, he left to pursue his dream of painting, and eventually found success in New York. He was able to afford luxuries such as taxis and restaurants, and he experimented with a new kind of still life painting. He also had the idea to create a web app for making web apps, which he eventually pursued and was successful with. He then started Y Combinator, an investment firm that focused on helping startups, with his own money and the help of his friends Robert and Trevor. He wrote essays and books, invited undergrads to apply to the Summer Founders Program, and eventually married Jessica Livingston. After his mother's death, he decided to quit Y Combinator and pursue painting, but eventually ran out of steam and started writing essays and working on Lisp again. He wrote a new Lisp, called Bel, in itself in Arc, and it took him four years to complete. During this time, he worked hard to make the language user-friendly and precise, and he also took time to enjoy life with his family. He encountered various obstacles along the way, such as customs that constrained him even after the restrictions that caused them had disappeared, and he also had to deal with misinterpretations of his essays on forums. In the end, he was successful in creating Bel and was able to pursue his dream of painting.

In \[ \]:

Copied!

query\_engine \= vector\_index.as\_query\_engine()
vector\_response \= query\_engine.query("What did the author do growing up?")

query\_engine = vector\_index.as\_query\_engine() vector\_response = query\_engine.query("What did the author do growing up?")

INFO:llama\_index.token\_counter.token\_counter:> \[retrieve\] Total LLM token usage: 0 tokens
> \[retrieve\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[retrieve\] Total embedding token usage: 8 tokens
> \[retrieve\] Total embedding token usage: 8 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total LLM token usage: 0 tokens
> \[get\_response\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total embedding token usage: 0 tokens
> \[get\_response\] Total embedding token usage: 0 tokens

In \[ \]:

Copied!

display\_response(vector\_response)

display\_response(vector\_response)

**`Final Response:`** None

In \[ \]:

Copied!

query\_engine \= keyword\_table\_index.as\_query\_engine()
keyword\_response \= query\_engine.query(
    "What did the author do after his time at YC?"
)

query\_engine = keyword\_table\_index.as\_query\_engine() keyword\_response = query\_engine.query( "What did the author do after his time at YC?" )

INFO:llama\_index.indices.keyword\_table.retrievers:> Starting query: What did the author do after his time at YC?
> Starting query: What did the author do after his time at YC?
INFO:llama\_index.indices.keyword\_table.retrievers:query keywords: \['action', 'yc', 'after', 'time', 'author'\]
query keywords: \['action', 'yc', 'after', 'time', 'author'\]
INFO:llama\_index.indices.keyword\_table.retrievers:> Extracted keywords: \['yc', 'time'\]
> Extracted keywords: \['yc', 'time'\]
INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total LLM token usage: 10216 tokens
> \[get\_response\] Total LLM token usage: 10216 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total embedding token usage: 0 tokens
> \[get\_response\] Total embedding token usage: 0 tokens

In \[ \]:

Copied!

display\_response(keyword\_response)

display\_response(keyword\_response)

**`Final Response:`** After his time at YC, the author decided to pursue painting and writing. He wanted to see how good he could get if he really focused on it, so he started painting the day after he stopped working on YC. He spent most of the rest of 2014 painting and was able to become better than he had been before. He also wrote essays and started working on Lisp again in March 2015. He then spent 4 years working on a new Lisp, called Bel, which he wrote in itself in Arc. He had to ban himself from writing essays during most of this time, and he moved to England in the summer of 2016. He also wrote a book about Lisp hacking, called On Lisp, which was published in 1993. In the fall of 2019, Bel was finally finished. He also experimented with a new kind of still life painting, and tried to build a web app for making web apps, which he named Aspra. He eventually decided to build a subset of this app as an open source project, which was the new Lisp dialect he called Arc.

Back to top

[Previous MongoDB Demo](https://docs.llamaindex.ai/en/stable/examples/docstore/MongoDocstoreDemo/)[Next Anyscale Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/Anyscale/)
