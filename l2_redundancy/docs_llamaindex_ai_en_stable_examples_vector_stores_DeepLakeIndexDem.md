Title: Deep Lake Vector Store Quickstart

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/DeepLakeIndexDemo/

Markdown Content:
Deep Lake Vector Store Quickstart - LlamaIndex


Deep Lake can be installed using pip.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-deeplake

%pip install llama-index-vector-stores-deeplake

In \[ \]:

Copied!

!pip install llama\-index
!pip install deeplake

!pip install llama-index !pip install deeplake

Next, let's import the required modules and set the needed environmental variables:

In \[ \]:

Copied!

import os
import textwrap

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader, Document
from llama\_index.vector\_stores.deeplake import DeepLakeVectorStore

os.environ\["OPENAI\_API\_KEY"\] \= "sk-\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*"
os.environ\["ACTIVELOOP\_TOKEN"\] \= "\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*"

import os import textwrap from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader, Document from llama\_index.vector\_stores.deeplake import DeepLakeVectorStore os.environ\["OPENAI\_API\_KEY"\] = "sk-\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*" os.environ\["ACTIVELOOP\_TOKEN"\] = "\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*"

We are going to embed and store one of Paul Graham's essays in a Deep Lake Vector Store stored locally. First, we download the data to a directory called `data/paul_graham`

In \[ \]:

Copied!

import urllib.request

urllib.request.urlretrieve(
    "https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt",
    "data/paul\_graham/paul\_graham\_essay.txt",
)

import urllib.request urllib.request.urlretrieve( "https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt", "data/paul\_graham/paul\_graham\_essay.txt", )

We can now create documents from the source data file.

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()
print(
    "Document ID:",
    documents\[0\].doc\_id,
    "Document Hash:",
    documents\[0\].hash,
)

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data() print( "Document ID:", documents\[0\].doc\_id, "Document Hash:", documents\[0\].hash, )

Document ID: a98b6686-e666-41a9-a0bc-b79f0d666bde Document Hash: beaa54b3e9cea641e91e6975d2207af4f4200f4b2d629725d688f272372ce5bb

Finally, let's create the Deep Lake Vector Store and populate it with data. We use a default tensor configuration, which creates tensors with `text (str)`, `metadata(json)`, `id (str, auto-populated)`, `embedding (float32)`. [Learn more about tensor customizability here](https://docs.activeloop.ai/example-code/getting-started/vector-store/step-4-customizing-vector-stores).

In \[ \]:

Copied!

from llama\_index.core import StorageContext

dataset\_path \= "./dataset/paul\_graham"

\# Create an index over the documents
vector\_store \= DeepLakeVectorStore(dataset\_path\=dataset\_path, overwrite\=True)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

from llama\_index.core import StorageContext dataset\_path = "./dataset/paul\_graham" # Create an index over the documents vector\_store = DeepLakeVectorStore(dataset\_path=dataset\_path, overwrite=True) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

Uploading data to deeplake dataset.

100%|██████████| 22/22 \[00:00<00:00, 684.80it/s\]

Dataset(path='./dataset/paul\_graham', tensors=\['text', 'metadata', 'embedding', 'id'\])

  tensor      htype      shape      dtype  compression
  -------    -------    -------    -------  ------- 
   text       text      (22, 1)      str     None   
 metadata     json      (22, 1)      str     None   
 embedding  embedding  (22, 1536)  float32   None   
    id        text      (22, 1)      str     None   

Performing Vector Search[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DeepLakeIndexDemo/#performing-vector-search)
------------------------------------------------------------------------------------------------------------------------------------

Deep Lake offers highly-flexible vector search and hybrid search options [discussed in detail in these tutorials](https://docs.activeloop.ai/example-code/tutorials/vector-store/vector-search-options). In this Quickstart, we show a simple example using default options.

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()
response \= query\_engine.query(
    "What did the author learn?",
)

query\_engine = index.as\_query\_engine() response = query\_engine.query( "What did the author learn?", )

In \[ \]:

Copied!

print(textwrap.fill(str(response), 100))

print(textwrap.fill(str(response), 100))

  The author learned that working on things that are not prestigious can be a good thing, as it can
lead to discovering something real and avoiding the wrong track. The author also learned that
ignorance can be beneficial, as it can lead to discovering something new and unexpected. The author
also learned the importance of working hard, even at the parts of the job they don't like, in order
to set an example for others. The author also learned the value of unsolicited advice, as it can be
beneficial in unexpected ways, such as when Robert Morris suggested that the author should make sure
Y Combinator wasn't the last cool thing they did.

In \[ \]:

Copied!

response \= query\_engine.query("What was a hard moment for the author?")

response = query\_engine.query("What was a hard moment for the author?")

In \[ \]:

Copied!

print(textwrap.fill(str(response), 100))

print(textwrap.fill(str(response), 100))

The author experienced a hard moment when one of his programs on the IBM 1401 computer did not
terminate. This was a social as well as a technical error, as the data center manager's expression
made clear.

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What was a hard moment for the author?")
print(textwrap.fill(str(response), 100))

query\_engine = index.as\_query\_engine() response = query\_engine.query("What was a hard moment for the author?") print(textwrap.fill(str(response), 100))

The author experienced a hard moment when one of his programs on the IBM 1401 computer did not
terminate. This was a social as well as a technical error, as the data center manager's expression
made clear.

Deleting items from the database[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DeepLakeIndexDemo/#deleting-items-from-the-database)
----------------------------------------------------------------------------------------------------------------------------------------------------

To find the id of a document to delete, you can query the underlying deeplake dataset directly

In \[ \]:

Copied!

import deeplake

ds \= deeplake.load(dataset\_path)

idx \= ds.id\[0\].numpy().tolist()
idx

import deeplake ds = deeplake.load(dataset\_path) idx = ds.id\[0\].numpy().tolist() idx

./dataset/paul\_graham loaded successfully.

Out\[ \]:

\['42f8220e-673d-4c65-884d-5a48a1a15b03'\]

In \[ \]:

Copied!

index.delete(idx\[0\])

index.delete(idx\[0\])

Back to top

[Previous Databricks Vector Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DatabricksVectorSearchDemo/)[Next DocArray Hnsw Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DocArrayHnswIndexDemo/)
