Title: Building Data Ingestion from Scratch

URL Source: https://docs.llamaindex.ai/en/stable/examples/low_level/ingestion/

Markdown Content:
Building Data Ingestion from Scratch - LlamaIndex


In this tutorial, we show you how to build a data ingestion pipeline into a vector database.

We use Pinecone as the vector database.

We will show how to do the following:

1.  How to load in documents.
2.  How to use a text splitter to split documents.
3.  How to **manually** construct nodes from each text chunk.
4.  \[Optional\] Add metadata to each Node.
5.  How to generate embeddings for each text chunk.
6.  How to insert into a vector database.

Pinecone[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/ingestion/#pinecone)
----------------------------------------------------------------------------------------

You will need a [pinecone.io](https://www.pinecone.io/) api key for this tutorial. You can [sign up for free](https://app.pinecone.io/?sessionType=signup) to get a Starter account.

If you create a Starter account, you can name your application anything you like.

Once you have an account, navigate to 'API Keys' in the Pinecone console. You can use the default key or create a new one for this tutorial.

Save your api key and its environment (`gcp_starter` for free accounts). You will need them below.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-embeddings\-openai
%pip install llama\-index\-vector\-stores\-pinecone
%pip install llama\-index\-llms\-openai

%pip install llama-index-embeddings-openai %pip install llama-index-vector-stores-pinecone %pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

OpenAI[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/ingestion/#openai)
------------------------------------------------------------------------------------

You will need an [OpenAI](https://openai.com/) api key for this tutorial. Login to your [platform.openai.com](https://platform.openai.com/) account, click on your profile picture in the upper right corner, and choose 'API Keys' from the menu. Create an API key for this tutorial and save it. You will need it below.

Environment[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/ingestion/#environment)
----------------------------------------------------------------------------------------------

First we add our dependencies.

In \[ \]:

Copied!

!pip \-q install python\-dotenv pinecone\-client llama\-index pymupdf

!pip -q install python-dotenv pinecone-client llama-index pymupdf

#### Set Environment Variables[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/ingestion/#set-environment-variables)

We create a file for our environment variables. Do not commit this file or share it!

Note: Google Colabs will let you create but not open a .env

In \[ \]:

Copied!

dotenv\_path \= (
    "env"  \# Google Colabs will not let you open a .env, but you can set
)
with open(dotenv\_path, "w") as f:
    f.write('PINECONE\_API\_KEY="<your api key>"\\n')
    f.write('PINECONE\_ENVIRONMENT="gcp-starter"\\n')
    f.write('OPENAI\_API\_KEY="<your api key>"\\n')

dotenv\_path = ( "env" # Google Colabs will not let you open a .env, but you can set ) with open(dotenv\_path, "w") as f: f.write('PINECONE\_API\_KEY=""\\n') f.write('PINECONE\_ENVIRONMENT="gcp-starter"\\n') f.write('OPENAI\_API\_KEY=""\\n')

Set your OpenAI api key, and Pinecone api key and environment in the file we created.

In \[ \]:

Copied!

import os
from dotenv import load\_dotenv

import os from dotenv import load\_dotenv

In \[ \]:

Copied!

load\_dotenv(dotenv\_path\=dotenv\_path)

load\_dotenv(dotenv\_path=dotenv\_path)

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/ingestion/#setup)
----------------------------------------------------------------------------------

We build an empty Pinecone Index, and define the necessary LlamaIndex wrappers/abstractions so that we can start loading data into Pinecone.

Note: Do not save your API keys in the code or add pinecone\_env to your repo!

In \[ \]:

Copied!

import pinecone

import pinecone

In \[ \]:

Copied!

api\_key \= os.environ\["PINECONE\_API\_KEY"\]
environment \= os.environ\["PINECONE\_ENVIRONMENT"\]
pinecone.init(api\_key\=api\_key, environment\=environment)

api\_key = os.environ\["PINECONE\_API\_KEY"\] environment = os.environ\["PINECONE\_ENVIRONMENT"\] pinecone.init(api\_key=api\_key, environment=environment)

In \[ \]:

Copied!

index\_name \= "llamaindex-rag-fs"

index\_name = "llamaindex-rag-fs"

In \[ \]:

Copied!

\# \[Optional\] Delete the index before re-running the tutorial.
\# pinecone.delete\_index(index\_name)

\# \[Optional\] Delete the index before re-running the tutorial. # pinecone.delete\_index(index\_name)

In \[ \]:

Copied!

\# dimensions are for text-embedding-ada-002
pinecone.create\_index(
    index\_name, dimension\=1536, metric\="euclidean", pod\_type\="p1"
)

\# dimensions are for text-embedding-ada-002 pinecone.create\_index( index\_name, dimension=1536, metric="euclidean", pod\_type="p1" )

In \[ \]:

Copied!

pinecone\_index \= pinecone.Index(index\_name)

pinecone\_index = pinecone.Index(index\_name)

In \[ \]:

Copied!

\# \[Optional\] drop contents in index - will not work on free accounts
pinecone\_index.delete(deleteAll\=True)

\# \[Optional\] drop contents in index - will not work on free accounts pinecone\_index.delete(deleteAll=True)

#### Create PineconeVectorStore[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/ingestion/#create-pineconevectorstore)

Simple wrapper abstraction to use in LlamaIndex. Wrap in StorageContext so we can easily load in Nodes.

In \[ \]:

Copied!

from llama\_index.vector\_stores.pinecone import PineconeVectorStore

from llama\_index.vector\_stores.pinecone import PineconeVectorStore

In \[ \]:

Copied!

vector\_store \= PineconeVectorStore(pinecone\_index\=pinecone\_index)

vector\_store = PineconeVectorStore(pinecone\_index=pinecone\_index)

Build an Ingestion Pipeline from Scratch[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/ingestion/#build-an-ingestion-pipeline-from-scratch)
--------------------------------------------------------------------------------------------------------------------------------------------------------

We show how to build an ingestion pipeline as mentioned in the introduction.

Note that steps (2) and (3) can be handled via our `NodeParser` abstractions, which handle splitting and node creation.

For the purposes of this tutorial, we show you how to create these objects manually.

### 1\. Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/ingestion/#1-load-data)

In \[ \]:

Copied!

!mkdir data
!wget \--user\-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" \-O "data/llama2.pdf"

!mkdir data !wget --user-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" -O "data/llama2.pdf"

\--2023-10-13 01:45:14--  https://arxiv.org/pdf/2307.09288.pdf
Resolving arxiv.org (arxiv.org)... 128.84.21.199
Connecting to arxiv.org (arxiv.org)|128.84.21.199|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 13661300 (13M) \[application/pdf\]
Saving to: ‘data/llama2.pdf’

data/llama2.pdf     100%\[>\]  13.03M  7.59MB/s    in 1.7s    

2023-10-13 01:45:16 (7.59 MB/s) - ‘data/llama2.pdf’ saved \[13661300/13661300\]

In \[ \]:

Copied!

import fitz

import fitz

In \[ \]:

Copied!

file\_path \= "./data/llama2.pdf"
doc \= fitz.open(file\_path)

file\_path = "./data/llama2.pdf" doc = fitz.open(file\_path)

### 2\. Use a Text Splitter to Split Documents[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/ingestion/#2-use-a-text-splitter-to-split-documents)

Here we import our `SentenceSplitter` to split document texts into smaller chunks, while preserving paragraphs/sentences as much as possible.

In \[ \]:

Copied!

from llama\_index.core.node\_parser import SentenceSplitter

from llama\_index.core.node\_parser import SentenceSplitter

In \[ \]:

Copied!

text\_parser \= SentenceSplitter(
    chunk\_size\=1024,
    \# separator=" ",
)

text\_parser = SentenceSplitter( chunk\_size=1024, # separator=" ", )

In \[ \]:

Copied!

text\_chunks \= \[\]
\# maintain relationship with source doc index, to help inject doc metadata in (3)
doc\_idxs \= \[\]
for doc\_idx, page in enumerate(doc):
    page\_text \= page.get\_text("text")
    cur\_text\_chunks \= text\_parser.split\_text(page\_text)
    text\_chunks.extend(cur\_text\_chunks)
    doc\_idxs.extend(\[doc\_idx\] \* len(cur\_text\_chunks))

text\_chunks = \[\] # maintain relationship with source doc index, to help inject doc metadata in (3) doc\_idxs = \[\] for doc\_idx, page in enumerate(doc): page\_text = page.get\_text("text") cur\_text\_chunks = text\_parser.split\_text(page\_text) text\_chunks.extend(cur\_text\_chunks) doc\_idxs.extend(\[doc\_idx\] \* len(cur\_text\_chunks))

### 3\. Manually Construct Nodes from Text Chunks[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/ingestion/#3-manually-construct-nodes-from-text-chunks)

We convert each chunk into a `TextNode` object, a low-level data abstraction in LlamaIndex that stores content but also allows defining metadata + relationships with other Nodes.

We inject metadata from the document into each node.

This essentially replicates logic in our `SentenceSplitter`.

In \[ \]:

Copied!

from llama\_index.core.schema import TextNode

from llama\_index.core.schema import TextNode

In \[ \]:

Copied!

nodes \= \[\]
for idx, text\_chunk in enumerate(text\_chunks):
    node \= TextNode(
        text\=text\_chunk,
    )
    src\_doc\_idx \= doc\_idxs\[idx\]
    src\_page \= doc\[src\_doc\_idx\]
    nodes.append(node)

nodes = \[\] for idx, text\_chunk in enumerate(text\_chunks): node = TextNode( text=text\_chunk, ) src\_doc\_idx = doc\_idxs\[idx\] src\_page = doc\[src\_doc\_idx\] nodes.append(node)

In \[ \]:

Copied!

print(nodes\[0\].metadata)

print(nodes\[0\].metadata)

In \[ \]:

Copied!

\# print a sample node
print(nodes\[0\].get\_content(metadata\_mode\="all"))

\# print a sample node print(nodes\[0\].get\_content(metadata\_mode="all"))

### \[Optional\] 4. Extract Metadata from each Node[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/ingestion/#optional-4-extract-metadata-from-each-node)

We extract metadata from each Node using our Metadata extractors.

This will add more metadata to each Node.

In \[ \]:

Copied!

from llama\_index.core.extractors import (
    QuestionsAnsweredExtractor,
    TitleExtractor,
)
from llama\_index.core.ingestion import IngestionPipeline
from llama\_index.llms.openai import OpenAI

llm \= OpenAI(model\="gpt-3.5-turbo")

extractors \= \[
    TitleExtractor(nodes\=5, llm\=llm),
    QuestionsAnsweredExtractor(questions\=3, llm\=llm),
\]

from llama\_index.core.extractors import ( QuestionsAnsweredExtractor, TitleExtractor, ) from llama\_index.core.ingestion import IngestionPipeline from llama\_index.llms.openai import OpenAI llm = OpenAI(model="gpt-3.5-turbo") extractors = \[ TitleExtractor(nodes=5, llm=llm), QuestionsAnsweredExtractor(questions=3, llm=llm), \]

In \[ \]:

Copied!

pipeline \= IngestionPipeline(
    transformations\=extractors,
)
nodes \= await pipeline.arun(nodes\=nodes, in\_place\=False)

pipeline = IngestionPipeline( transformations=extractors, ) nodes = await pipeline.arun(nodes=nodes, in\_place=False)

In \[ \]:

Copied!

print(nodes\[0\].metadata)

print(nodes\[0\].metadata)

### 5\. Generate Embeddings for each Node[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/ingestion/#5-generate-embeddings-for-each-node)

Generate document embeddings for each Node using our OpenAI embedding model (`text-embedding-ada-002`).

Store these on the `embedding` property on each Node.

In \[ \]:

Copied!

from llama\_index.embeddings.openai import OpenAIEmbedding

embed\_model \= OpenAIEmbedding()

from llama\_index.embeddings.openai import OpenAIEmbedding embed\_model = OpenAIEmbedding()

In \[ \]:

Copied!

for node in nodes:
    node\_embedding \= embed\_model.get\_text\_embedding(
        node.get\_content(metadata\_mode\="all")
    )
    node.embedding \= node\_embedding

for node in nodes: node\_embedding = embed\_model.get\_text\_embedding( node.get\_content(metadata\_mode="all") ) node.embedding = node\_embedding

### 6\. Load Nodes into a Vector Store[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/ingestion/#6-load-nodes-into-a-vector-store)

We now insert these nodes into our `PineconeVectorStore`.

**NOTE**: We skip the VectorStoreIndex abstraction, which is a higher-level abstraction that handles ingestion as well. We use `VectorStoreIndex` in the next section to fast-track retrieval/querying.

In \[ \]:

Copied!

vector\_store.add(nodes)

vector\_store.add(nodes)

Retrieve and Query from the Vector Store[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/ingestion/#retrieve-and-query-from-the-vector-store)
--------------------------------------------------------------------------------------------------------------------------------------------------------

Now that our ingestion is complete, we can retrieve/query this vector store.

**NOTE**: We can use our high-level `VectorStoreIndex` abstraction here. See the next section to see how to define retrieval at a lower-level!

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex
from llama\_index.core import StorageContext

from llama\_index.core import VectorStoreIndex from llama\_index.core import StorageContext

In \[ \]:

Copied!

index \= VectorStoreIndex.from\_vector\_store(vector\_store)

index = VectorStoreIndex.from\_vector\_store(vector\_store)

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()

query\_engine = index.as\_query\_engine()

In \[ \]:

Copied!

query\_str \= "Can you tell me about the key concepts for safety finetuning"

query\_str = "Can you tell me about the key concepts for safety finetuning"

In \[ \]:

Copied!

response \= query\_engine.query(query\_str)

response = query\_engine.query(query\_str)

In \[ \]:

Copied!

print(str(response))

print(str(response))

Back to top

[Previous Building an Advanced Fusion Retriever from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/fusion_retriever/)[Next Building RAG from Scratch (Open-source only!)](https://docs.llamaindex.ai/en/stable/examples/low_level/oss_ingestion_retrieval/)

Hi, how can I help you?

🦙
