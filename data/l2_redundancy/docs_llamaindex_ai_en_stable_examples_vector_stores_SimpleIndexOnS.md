Title: S3/R2 Storage - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexOnS3/

Markdown Content:
S3/R2 Storage - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

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

from llama\_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    load\_index\_from\_storage,
    StorageContext,
)
from IPython.display import Markdown, display

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout)) from llama\_index.core import ( VectorStoreIndex, SimpleDirectoryReader, load\_index\_from\_storage, StorageContext, ) from IPython.display import Markdown, display

INFO:numexpr.utils:Note: NumExpr detected 32 cores but "NUMEXPR\_MAX\_THREADS" not set, so enforcing safe limit of 8.
Note: NumExpr detected 32 cores but "NUMEXPR\_MAX\_THREADS" not set, so enforcing safe limit of 8.
INFO:numexpr.utils:NumExpr defaulting to 8 threads.
NumExpr defaulting to 8 threads.

/home/hua/code/llama\_index/.hermit/python/lib/python3.10/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user\_install.html
  from .autonotebook import tqdm as notebook\_tqdm

In \[ \]:

Copied!

import dotenv
import s3fs
import os

dotenv.load\_dotenv("../../../.env")

AWS\_KEY \= os.environ\["AWS\_ACCESS\_KEY\_ID"\]
AWS\_SECRET \= os.environ\["AWS\_SECRET\_ACCESS\_KEY"\]
R2\_ACCOUNT\_ID \= os.environ\["R2\_ACCOUNT\_ID"\]

assert AWS\_KEY is not None and AWS\_KEY != ""

s3 \= s3fs.S3FileSystem(
    key\=AWS\_KEY,
    secret\=AWS\_SECRET,
    endpoint\_url\=f"https://{R2\_ACCOUNT\_ID}.r2.cloudflarestorage.com",
    s3\_additional\_kwargs\={"ACL": "public-read"},
)

import dotenv import s3fs import os dotenv.load\_dotenv("../../../.env") AWS\_KEY = os.environ\["AWS\_ACCESS\_KEY\_ID"\] AWS\_SECRET = os.environ\["AWS\_SECRET\_ACCESS\_KEY"\] R2\_ACCOUNT\_ID = os.environ\["R2\_ACCOUNT\_ID"\] assert AWS\_KEY is not None and AWS\_KEY != "" s3 = s3fs.S3FileSystem( key=AWS\_KEY, secret=AWS\_SECRET, endpoint\_url=f"https://{R2\_ACCOUNT\_ID}.r2.cloudflarestorage.com", s3\_additional\_kwargs={"ACL": "public-read"}, )

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()
print(len(documents))

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data() print(len(documents))

1

In \[ \]:

Copied!

index \= VectorStoreIndex.from\_documents(documents, fs\=s3)

index = VectorStoreIndex.from\_documents(documents, fs=s3)

INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total embedding token usage: 20729 tokens
> \[build\_index\_from\_nodes\] Total embedding token usage: 20729 tokens

In \[ \]:

Copied!

\# save index to disk
index.set\_index\_id("vector\_index")
index.storage\_context.persist("llama-index/storage\_demo", fs\=s3)

\# save index to disk index.set\_index\_id("vector\_index") index.storage\_context.persist("llama-index/storage\_demo", fs=s3)

In \[ \]:

Copied!

s3.listdir("llama-index/storage\_demo")

s3.listdir("llama-index/storage\_demo")

Out\[ \]:

\[{'Key': 'llama-index/storage\_demo/docstore.json',
  'LastModified': datetime.datetime(2023, 5, 14, 20, 23, 53, 213000, tzinfo=tzutc()),
  'ETag': '"3993f79a6f7cf908a8e53450a2876cf0"',
  'Size': 107529,
  'StorageClass': 'STANDARD',
  'type': 'file',
  'size': 107529,
  'name': 'llama-index/storage\_demo/docstore.json'},
 {'Key': 'llama-index/storage\_demo/index\_store.json',
  'LastModified': datetime.datetime(2023, 5, 14, 20, 23, 53, 783000, tzinfo=tzutc()),
  'ETag': '"5b084883bf0b08e3c2b979af7c16be43"',
  'Size': 3105,
  'StorageClass': 'STANDARD',
  'type': 'file',
  'size': 3105,
  'name': 'llama-index/storage\_demo/index\_store.json'},
 {'Key': 'llama-index/storage\_demo/vector\_store.json',
  'LastModified': datetime.datetime(2023, 5, 14, 20, 23, 54, 232000, tzinfo=tzutc()),
  'ETag': '"75535cf22c23bcd8ead21b8a52e9517a"',
  'Size': 829290,
  'StorageClass': 'STANDARD',
  'type': 'file',
  'size': 829290,
  'name': 'llama-index/storage\_demo/vector\_store.json'}\]

In \[ \]:

Copied!

\# load index from s3
sc \= StorageContext.from\_defaults(
    persist\_dir\="llama-index/storage\_demo", fs\=s3
)

\# load index from s3 sc = StorageContext.from\_defaults( persist\_dir="llama-index/storage\_demo", fs=s3 )

In \[ \]:

Copied!

index2 \= load\_index\_from\_storage(sc, "vector\_index")

index2 = load\_index\_from\_storage(sc, "vector\_index")

INFO:llama\_index.indices.loading:Loading indices with ids: \['vector\_index'\]
Loading indices with ids: \['vector\_index'\]

In \[ \]:

Copied!

index2.docstore.docs.keys()

index2.docstore.docs.keys()

Out\[ \]:

dict\_keys(\['f8891670-813b-4cfa-9025-fcdc8ba73449', '985a2c69-9da5-40cf-ba30-f984921187c1', 'c55f077c-0bfb-4036-910c-6fd5f26f7372', 'b47face6-f25b-4381-bb8d-164f179d6888', '16304ef7-2378-4776-b86d-e8ed64c8fb58', '62dfdc7a-6a2f-4d5f-9033-851fbc56c14a', 'a51ef189-3924-494b-84cf-e23df673e29c', 'f94aca2b-34ac-4ec4-ac41-d31cd3b7646f', 'ad89e2fb-e0fc-4615-a380-8245bd6546af', '3dbba979-ca08-4321-b4de-be5236ac2e11', '634b2d6d-0bff-4384-898f-b521470db8ac', 'ee9551ba-7a44-493d-997b-8eeab9c04e25', 'b21fe2b5-d8e3-4895-8424-fa9e3da76711', 'bd2609e8-8b52-49e8-8ee7-41b64b3ce9e1', 'a08b739e-efd9-4a61-8517-c4f9cea8cf7d', '8d4babaf-37f1-454a-8be4-b67e1b8e428f', '05389153-4567-4e53-a2ea-bc3e020ee1b2', 'd29531a5-c5d2-4e1d-ab99-56f2b4bb7f37', '2ccb3c63-3407-4acf-b5bb-045caa588bbc', 'a0b1bebb-3dcd-4bf8-9ebb-a4cd2cb82d53', '21517b34-6c1b-4607-bf89-7ab59b85fba6', 'f2487d52-1e5e-4482-a182-218680ef306e', '979998ce-39ee-41bc-a9be-b3ed68d7c304', '3e658f36-a13e-407a-8624-0adf9e842676'\])

Back to top

[Previous Simple Vector Stores - Maximum Marginal Relevance Retrieval](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemoMMR/)[Next Supabase Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SupabaseVectorIndexDemo/)
