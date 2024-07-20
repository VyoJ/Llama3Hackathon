Title: Awadb Vector Store - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/AwadbDemo/

Markdown Content:
Awadb Vector Store - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-embeddings\-huggingface
%pip install llama\-index\-vector\-stores\-awadb

%pip install llama-index-embeddings-huggingface %pip install llama-index-vector-stores-awadb

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

Creating an Awadb index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AwadbDemo/#creating-an-awadb-index)
--------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

#### Load documents, build the VectorStoreIndex[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AwadbDemo/#load-documents-build-the-vectorstoreindex)

In \[ \]:

Copied!

from llama\_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
)
from IPython.display import Markdown, display
import openai

openai.api\_key \= ""

from llama\_index.core import ( SimpleDirectoryReader, VectorStoreIndex, StorageContext, ) from IPython.display import Markdown, display import openai openai.api\_key = ""

INFO:numexpr.utils:Note: NumExpr detected 12 cores but "NUMEXPR\_MAX\_THREADS" not set, so enforcing safe limit of 8.
Note: NumExpr detected 12 cores but "NUMEXPR\_MAX\_THREADS" not set, so enforcing safe limit of 8.
INFO:numexpr.utils:NumExpr defaulting to 8 threads.
NumExpr defaulting to 8 threads.

#### Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AwadbDemo/#download-data)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

#### Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AwadbDemo/#load-data)

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data()

In \[ \]:

Copied!

from llama\_index.embeddings.huggingface import HuggingFaceEmbedding
from llama\_index.vector\_stores.awadb import AwaDBVectorStore

embed\_model \= HuggingFaceEmbedding(model\_name\="BAAI/bge-small-en-v1.5")

vector\_store \= AwaDBVectorStore()
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context, embed\_model\=embed\_model
)

from llama\_index.embeddings.huggingface import HuggingFaceEmbedding from llama\_index.vector\_stores.awadb import AwaDBVectorStore embed\_model = HuggingFaceEmbedding(model\_name="BAAI/bge-small-en-v1.5") vector\_store = AwaDBVectorStore() storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context, embed\_model=embed\_model )

#### Query Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AwadbDemo/#query-index)

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did the author do growing up?")

\# set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine() response = query\_engine.query("What did the author do growing up?")

In \[ \]:

Copied!

display(Markdown(f"<b>{response}</b>"))

display(Markdown(f"**{response}**"))

**Growing up, the author wrote short stories, experimented with programming on an IBM 1401, nagged his father to buy a TRS-80 computer, wrote simple games, a program to predict how high his model rockets would fly, and a word processor. He also studied philosophy in college, switched to AI, and worked on building the infrastructure of the web. He wrote essays and published them online, had dinners for a group of friends every Thursday night, painted, and bought a building in Cambridge.**

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query(
    "What did the author do after his time at Y Combinator?"
)

\# set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine() response = query\_engine.query( "What did the author do after his time at Y Combinator?" )

In \[ \]:

Copied!

display(Markdown(f"<b>{response}</b>"))

display(Markdown(f"**{response}**"))

**After his time at Y Combinator, the author wrote essays, worked on Lisp, and painted. He also visited his mother in Oregon and helped her get out of a nursing home.**

Back to top

[Previous Simple Vector Store - Async Index Creation](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AsyncIndexCreationDemo/)[Next Azure AI Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureAISearchIndexDemo/)
