Title: Tair Vector Store - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/TairIndexDemo/

Markdown Content:
Tair Vector Store - LlamaIndex


In this notebook we are going to show a quick demo of using the TairVectorStore.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-tair

%pip install llama-index-vector-stores-tair

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import os
import sys
import logging
import textwrap

import warnings

warnings.filterwarnings("ignore")

\# stop huggingface warnings
os.environ\["TOKENIZERS\_PARALLELISM"\] \= "false"

\# Uncomment to see debug logs
\# logging.basicConfig(stream=sys.stdout, level=logging.INFO)
\# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from llama\_index.core import (
    GPTVectorStoreIndex,
    SimpleDirectoryReader,
    Document,
)
from llama\_index.vector\_stores.tair import TairVectorStore
from IPython.display import Markdown, display

import os import sys import logging import textwrap import warnings warnings.filterwarnings("ignore") # stop huggingface warnings os.environ\["TOKENIZERS\_PARALLELISM"\] = "false" # Uncomment to see debug logs # logging.basicConfig(stream=sys.stdout, level=logging.INFO) # logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout)) from llama\_index.core import ( GPTVectorStoreIndex, SimpleDirectoryReader, Document, ) from llama\_index.vector\_stores.tair import TairVectorStore from IPython.display import Markdown, display

### Setup OpenAI[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TairIndexDemo/#setup-openai)

Lets first begin by adding the openai api key. This will allow us to access openai for embeddings and to use chatgpt.

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-<your key here>"

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-"

### Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TairIndexDemo/#download-data)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

### Read in a dataset[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TairIndexDemo/#read-in-a-dataset)

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham").load\_data()
print(
    "Document ID:",
    documents\[0\].doc\_id,
    "Document Hash:",
    documents\[0\].doc\_hash,
)

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham").load\_data() print( "Document ID:", documents\[0\].doc\_id, "Document Hash:", documents\[0\].doc\_hash, )

### Build index from documents[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TairIndexDemo/#build-index-from-documents)

Let's build a vector index with `GPTVectorStoreIndex`, using `TairVectorStore` as its backend. Replace `tair_url` with the actual url of your Tair instance.

In \[ \]:

Copied!

from llama\_index.core import StorageContext

tair\_url \= "redis://{username}:{password}@r-bp\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*.redis.rds.aliyuncs.com:{port}"

vector\_store \= TairVectorStore(
    tair\_url\=tair\_url, index\_name\="pg\_essays", overwrite\=True
)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= GPTVectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

from llama\_index.core import StorageContext tair\_url = "redis://{username}:{password}@r-bp\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*.redis.rds.aliyuncs.com:{port}" vector\_store = TairVectorStore( tair\_url=tair\_url, index\_name="pg\_essays", overwrite=True ) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = GPTVectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

### Query the data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TairIndexDemo/#query-the-data)

Now we can use the index as knowledge base and ask questions to it.

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did the author learn?")
print(textwrap.fill(str(response), 100))

query\_engine = index.as\_query\_engine() response = query\_engine.query("What did the author learn?") print(textwrap.fill(str(response), 100))

In \[ \]:

Copied!

response \= query\_engine.query("What was a hard moment for the author?")
print(textwrap.fill(str(response), 100))

response = query\_engine.query("What was a hard moment for the author?") print(textwrap.fill(str(response), 100))

### Deleting documents[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TairIndexDemo/#deleting-documents)

To delete a document from the index, use `delete` method.

In \[ \]:

Copied!

document\_id \= documents\[0\].doc\_id
document\_id

document\_id = documents\[0\].doc\_id document\_id

In \[ \]:

Copied!

info \= vector\_store.client.tvs\_get\_index("pg\_essays")
print("Number of documents", int(info\["data\_count"\]))

info = vector\_store.client.tvs\_get\_index("pg\_essays") print("Number of documents", int(info\["data\_count"\]))

In \[ \]:

Copied!

vector\_store.delete(document\_id)

vector\_store.delete(document\_id)

In \[ \]:

Copied!

info \= vector\_store.client.tvs\_get\_index("pg\_essays")
print("Number of documents", int(info\["data\_count"\]))

info = vector\_store.client.tvs\_get\_index("pg\_essays") print("Number of documents", int(info\["data\_count"\]))

### Deleting index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TairIndexDemo/#deleting-index)

Delete the entire index using `delete_index` method.

In \[ \]:

Copied!

vector\_store.delete\_index()

vector\_store.delete\_index()

In \[ \]:

Copied!

print("Check index existence:", vector\_store.client.\_index\_exists())

print("Check index existence:", vector\_store.client.\_index\_exists())

Back to top

[Previous Supabase Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SupabaseVectorIndexDemo/)[Next Tencent Cloud VectorDB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TencentVectorDBIndexDemo/)
