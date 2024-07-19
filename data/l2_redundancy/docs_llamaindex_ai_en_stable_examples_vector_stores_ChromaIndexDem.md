Title: Chroma - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/ChromaIndexDemo/

Markdown Content:
Chroma - LlamaIndex


> [Chroma](https://docs.trychroma.com/getting-started) is a AI-native open-source vector database focused on developer productivity and happiness. Chroma is licensed under Apache 2.0.

 [![Image 4: Discord](https://img.shields.io/discord/1073293645303795742)](https://discord.gg/MMeYNTmh3x)   [![Image 5: License](https://img.shields.io/static/v1?label=license&message=Apache%202.0&color=white)](https://github.com/chroma-core/chroma/blob/master/LICENSE)   ![Image 6: Integration Tests](https://github.com/chroma-core/chroma/actions/workflows/chroma-integration-test.yml/badge.svg?branch=main)

*   [Website](https://www.trychroma.com/)
*   [Documentation](https://docs.trychroma.com/)
*   [Twitter](https://twitter.com/trychroma)
*   [Discord](https://discord.gg/MMeYNTmh3x)

Chroma is fully-typed, fully-tested and fully-documented.

Install Chroma with:

pip install chromadb

Chroma runs in various modes. See below for examples of each integrated with LlamaIndex.

*   `in-memory` - in a python script or jupyter notebook
*   `in-memory with persistance` - in a script or notebook and save/load to disk
*   `in a docker container` - as a server running your local machine or in the cloud

Like any other database, you can:

*   `.add`
*   `.get`
*   `.update`
*   `.upsert`
*   `.delete`
*   `.peek`
*   and `.query` runs the similarity search.

View full docs at [docs](https://docs.trychroma.com/reference/Collection).

Basic Example[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ChromaIndexDemo/#basic-example)
------------------------------------------------------------------------------------------------------------

In this basic example, we take the Paul Graham essay, split it into chunks, embed it using an open-source embedding model, load it into Chroma, and then query it.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-chroma
%pip install llama\-index\-embeddings\-huggingface

%pip install llama-index-vector-stores-chroma %pip install llama-index-embeddings-huggingface

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

#### Creating a Chroma Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ChromaIndexDemo/#creating-a-chroma-index)

In \[ \]:

Copied!

\# !pip install llama-index chromadb --quiet
\# !pip install chromadb
\# !pip install sentence-transformers
\# !pip install pydantic1.10.11

In \[ \]:

Copied!

\# import
from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.vector\_stores.chroma import ChromaVectorStore
from llama\_index.core import StorageContext
from llama\_index.embeddings.huggingface import HuggingFaceEmbedding
from IPython.display import Markdown, display
import chromadb

\# import from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.vector\_stores.chroma import ChromaVectorStore from llama\_index.core import StorageContext from llama\_index.embeddings.huggingface import HuggingFaceEmbedding from IPython.display import Markdown, display import chromadb

In \[ \]:

Copied!

\# set up OpenAI
import os
import getpass

os.environ\["OPENAI\_API\_KEY"\] \= getpass.getpass("OpenAI API Key:")
import openai

openai.api\_key \= os.environ\["OPENAI\_API\_KEY"\]

\# set up OpenAI import os import getpass os.environ\["OPENAI\_API\_KEY"\] = getpass.getpass("OpenAI API Key:") import openai openai.api\_key = os.environ\["OPENAI\_API\_KEY"\]

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

In \[ \]:

Copied!

\# create client and a new collection
chroma\_client \= chromadb.EphemeralClient()
chroma\_collection \= chroma\_client.create\_collection("quickstart")

\# define embedding function
embed\_model \= HuggingFaceEmbedding(model\_name\="BAAI/bge-base-en-v1.5")

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

\# set up ChromaVectorStore and load in data
vector\_store \= ChromaVectorStore(chroma\_collection\=chroma\_collection)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context, embed\_model\=embed\_model
)

\# Query Data
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did the author do growing up?")
display(Markdown(f"<b>{response}</b>"))

\# create client and a new collection chroma\_client = chromadb.EphemeralClient() chroma\_collection = chroma\_client.create\_collection("quickstart") # define embedding function embed\_model = HuggingFaceEmbedding(model\_name="BAAI/bge-base-en-v1.5") # load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data() # set up ChromaVectorStore and load in data vector\_store = ChromaVectorStore(chroma\_collection=chroma\_collection) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context, embed\_model=embed\_model ) # Query Data query\_engine = index.as\_query\_engine() response = query\_engine.query("What did the author do growing up?") display(Markdown(f"**{response}**"))

/Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user\_install.html
  from .autonotebook import tqdm as notebook\_tqdm
/Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages/bitsandbytes/cextension.py:34: UserWarning: The installed version of bitsandbytes was compiled without GPU support. 8-bit optimizers, 8-bit multiplication, and GPU quantization are unavailable.
  warn("The installed version of bitsandbytes was compiled without GPU support. "

'NoneType' object has no attribute 'cadam32bit\_grad\_fp32'

**The author worked on writing and programming growing up. They wrote short stories and tried writing programs on an IBM 1401 computer. Later, they got a microcomputer and started programming more extensively.**

Basic Example (including saving to disk)[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ChromaIndexDemo/#basic-example-including-saving-to-disk)
----------------------------------------------------------------------------------------------------------------------------------------------------------------

Extending the previous example, if you want to save to disk, simply initialize the Chroma client and pass the directory where you want the data to be saved to.

`Caution`: Chroma makes a best-effort to automatically save data to disk, however multiple in-memory clients can stomp each other's work. As a best practice, only have one client per path running at any given time.

In \[ \]:

Copied!

\# save to disk

db \= chromadb.PersistentClient(path\="./chroma\_db")
chroma\_collection \= db.get\_or\_create\_collection("quickstart")
vector\_store \= ChromaVectorStore(chroma\_collection\=chroma\_collection)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context, embed\_model\=embed\_model
)

\# load from disk
db2 \= chromadb.PersistentClient(path\="./chroma\_db")
chroma\_collection \= db2.get\_or\_create\_collection("quickstart")
vector\_store \= ChromaVectorStore(chroma\_collection\=chroma\_collection)
index \= VectorStoreIndex.from\_vector\_store(
    vector\_store,
    embed\_model\=embed\_model,
)

\# Query Data from the persisted index
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did the author do growing up?")
display(Markdown(f"<b>{response}</b>"))

\# save to disk db = chromadb.PersistentClient(path="./chroma\_db") chroma\_collection = db.get\_or\_create\_collection("quickstart") vector\_store = ChromaVectorStore(chroma\_collection=chroma\_collection) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context, embed\_model=embed\_model ) # load from disk db2 = chromadb.PersistentClient(path="./chroma\_db") chroma\_collection = db2.get\_or\_create\_collection("quickstart") vector\_store = ChromaVectorStore(chroma\_collection=chroma\_collection) index = VectorStoreIndex.from\_vector\_store( vector\_store, embed\_model=embed\_model, ) # Query Data from the persisted index query\_engine = index.as\_query\_engine() response = query\_engine.query("What did the author do growing up?") display(Markdown(f"**{response}**"))

**The author worked on writing and programming growing up. They wrote short stories and tried writing programs on an IBM 1401 computer. Later, they got a microcomputer and started programming games and a word processor.**

Basic Example (using the Docker Container)[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ChromaIndexDemo/#basic-example-using-the-docker-container)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can also run the Chroma Server in a Docker container separately, create a Client to connect to it, and then pass that to LlamaIndex.

Here is how to clone, build, and run the Docker Image:

```
git clone git@github.com:chroma-core/chroma.git
docker-compose up -d --build
```

In \[ \]:

Copied!

\# create the chroma client and add our data
import chromadb

remote\_db \= chromadb.HttpClient()
chroma\_collection \= remote\_db.get\_or\_create\_collection("quickstart")
vector\_store \= ChromaVectorStore(chroma\_collection\=chroma\_collection)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context, embed\_model\=embed\_model
)

\# create the chroma client and add our data import chromadb remote\_db = chromadb.HttpClient() chroma\_collection = remote\_db.get\_or\_create\_collection("quickstart") vector\_store = ChromaVectorStore(chroma\_collection=chroma\_collection) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context, embed\_model=embed\_model )

In \[ \]:

Copied!

\# Query Data from the Chroma Docker index
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did the author do growing up?")
display(Markdown(f"<b>{response}</b>"))

\# Query Data from the Chroma Docker index query\_engine = index.as\_query\_engine() response = query\_engine.query("What did the author do growing up?") display(Markdown(f"**{response}**"))

**Growing up, the author wrote short stories, programmed on an IBM 1401, and wrote programs on a TRS-80 microcomputer. He also took painting classes at Harvard and worked as a de facto studio assistant for a painter. He also tried to start a company to put art galleries online, and wrote software to build online stores.**

Update and Delete[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ChromaIndexDemo/#update-and-delete)
--------------------------------------------------------------------------------------------------------------------

While building toward a real application, you want to go beyond adding data, and also update and delete data.

Chroma has users provide `ids` to simplify the bookkeeping here. `ids` can be the name of the file, or a combined has like `filename_paragraphNumber`, etc.

Here is a basic example showing how to do various operations:

In \[ \]:

Copied!

doc\_to\_update \= chroma\_collection.get(limit\=1)
doc\_to\_update\["metadatas"\]\[0\] \= {
    \*\*doc\_to\_update\["metadatas"\]\[0\],
    \*\*{"author": "Paul Graham"},
}
chroma\_collection.update(
    ids\=\[doc\_to\_update\["ids"\]\[0\]\], metadatas\=\[doc\_to\_update\["metadatas"\]\[0\]\]
)
updated\_doc \= chroma\_collection.get(limit\=1)
print(updated\_doc\["metadatas"\]\[0\])

\# delete the last document
print("count before", chroma\_collection.count())
chroma\_collection.delete(ids\=\[doc\_to\_update\["ids"\]\[0\]\])
print("count after", chroma\_collection.count())

doc\_to\_update = chroma\_collection.get(limit=1) doc\_to\_update\["metadatas"\]\[0\] = { \*\*doc\_to\_update\["metadatas"\]\[0\], \*\*{"author": "Paul Graham"}, } chroma\_collection.update( ids=\[doc\_to\_update\["ids"\]\[0\]\], metadatas=\[doc\_to\_update\["metadatas"\]\[0\]\] ) updated\_doc = chroma\_collection.get(limit=1) print(updated\_doc\["metadatas"\]\[0\]) # delete the last document print("count before", chroma\_collection.count()) chroma\_collection.delete(ids=\[doc\_to\_update\["ids"\]\[0\]\]) print("count after", chroma\_collection.count())

{'\_node\_content': '{"id\_": "be08c8bc-f43e-4a71-ba64-e525921a8319", "embedding": null, "metadata": {}, "excluded\_embed\_metadata\_keys": \[\], "excluded\_llm\_metadata\_keys": \[\], "relationships": {"1": {"node\_id": "2cbecdbb-0840-48b2-8151-00119da0995b", "node\_type": null, "metadata": {}, "hash": "4c702b4df575421e1d1af4b1fd50511b226e0c9863dbfffeccb8b689b8448f35"}, "3": {"node\_id": "6a75604a-fa76-4193-8f52-c72a7b18b154", "node\_type": null, "metadata": {}, "hash": "d6c408ee1fbca650fb669214e6f32ffe363b658201d31c204e85a72edb71772f"}}, "hash": "b4d0b960aa09e693f9dc0d50ef46a3d0bf5a8fb3ac9f3e4bcf438e326d17e0d8", "text": "", "start\_char\_idx": 0, "end\_char\_idx": 4050, "text\_template": "{metadata\_str}\\\\n\\\\n{content}", "metadata\_template": "{key}: {value}", "metadata\_seperator": "\\\\n"}', 'author': 'Paul Graham', 'doc\_id': '2cbecdbb-0840-48b2-8151-00119da0995b', 'document\_id': '2cbecdbb-0840-48b2-8151-00119da0995b', 'ref\_doc\_id': '2cbecdbb-0840-48b2-8151-00119da0995b'}
count before 20
count after 19

Back to top

[Previous Chroma + Fireworks + Nomic with Matryoshka embedding](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ChromaFireworksNomic/)[Next ClickHouse Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ClickHouseIndexDemo/)
