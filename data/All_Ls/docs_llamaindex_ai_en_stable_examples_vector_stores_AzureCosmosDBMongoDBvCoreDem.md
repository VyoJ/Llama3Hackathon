Title: Azure CosmosDB MongoDB Vector Store

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureCosmosDBMongoDBvCoreDemo/

Markdown Content:
Azure CosmosDB MongoDB Vector Store - LlamaIndex


In this notebook we are going to show how to use Azure Cosmosdb Mongodb vCore to perform vector searches in LlamaIndex. We will create the embedding using Azure Open AI.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-embeddings\-openai
%pip install llama\-index\-vector\-stores\-azurecosmosmongo
%pip install llama\-index\-llms\-azure\-openai

%pip install llama-index-embeddings-openai %pip install llama-index-vector-stores-azurecosmosmongo %pip install llama-index-llms-azure-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import os
import json
import openai
from llama\_index.llms.azure\_openai import AzureOpenAI
from llama\_index.embeddings.openai import OpenAIEmbedding
from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader

import os import json import openai from llama\_index.llms.azure\_openai import AzureOpenAI from llama\_index.embeddings.openai import OpenAIEmbedding from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader

### Setup Azure OpenAI[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureCosmosDBMongoDBvCoreDemo/#setup-azure-openai)

The first step is to configure the models. They will be used to create embeddings for the documents loaded into the db and for llm completions.

In \[ \]:

Copied!

import os

\# Set up the AzureOpenAI instance
llm \= AzureOpenAI(
    model\_name\=os.getenv("OPENAI\_MODEL\_COMPLETION"),
    deployment\_name\=os.getenv("OPENAI\_MODEL\_COMPLETION"),
    api\_base\=os.getenv("OPENAI\_API\_BASE"),
    api\_key\=os.getenv("OPENAI\_API\_KEY"),
    api\_type\=os.getenv("OPENAI\_API\_TYPE"),
    api\_version\=os.getenv("OPENAI\_API\_VERSION"),
    temperature\=0,
)

\# Set up the OpenAIEmbedding instance
embed\_model \= OpenAIEmbedding(
    model\=os.getenv("OPENAI\_MODEL\_EMBEDDING"),
    deployment\_name\=os.getenv("OPENAI\_DEPLOYMENT\_EMBEDDING"),
    api\_base\=os.getenv("OPENAI\_API\_BASE"),
    api\_key\=os.getenv("OPENAI\_API\_KEY"),
    api\_type\=os.getenv("OPENAI\_API\_TYPE"),
    api\_version\=os.getenv("OPENAI\_API\_VERSION"),
)

import os # Set up the AzureOpenAI instance llm = AzureOpenAI( model\_name=os.getenv("OPENAI\_MODEL\_COMPLETION"), deployment\_name=os.getenv("OPENAI\_MODEL\_COMPLETION"), api\_base=os.getenv("OPENAI\_API\_BASE"), api\_key=os.getenv("OPENAI\_API\_KEY"), api\_type=os.getenv("OPENAI\_API\_TYPE"), api\_version=os.getenv("OPENAI\_API\_VERSION"), temperature=0, ) # Set up the OpenAIEmbedding instance embed\_model = OpenAIEmbedding( model=os.getenv("OPENAI\_MODEL\_EMBEDDING"), deployment\_name=os.getenv("OPENAI\_DEPLOYMENT\_EMBEDDING"), api\_base=os.getenv("OPENAI\_API\_BASE"), api\_key=os.getenv("OPENAI\_API\_KEY"), api\_type=os.getenv("OPENAI\_API\_TYPE"), api\_version=os.getenv("OPENAI\_API\_VERSION"), )

In \[ \]:

Copied!

from llama\_index.core import Settings

Settings.llm \= llm
Settings.embed\_model \= embed\_model

from llama\_index.core import Settings Settings.llm = llm Settings.embed\_model = embed\_model

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

### Loading documents[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureCosmosDBMongoDBvCoreDemo/#loading-documents)

Load the documents stored in the `data/paul_graham/` using the SimpleDirectoryReader

In \[ \]:

Copied!

documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

print("Document ID:", documents\[0\].doc\_id)

documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data() print("Document ID:", documents\[0\].doc\_id)

Document ID: c432ff1c-61ea-4c91-bd89-62be29078e79

### Create the index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureCosmosDBMongoDBvCoreDemo/#create-the-index)

Here we establish the connection to an Azure Cosmosdb mongodb vCore cluster and create an vector search index.

In \[ \]:

Copied!

import pymongo
from llama\_index.vector\_stores.azurecosmosmongo import (
    AzureCosmosDBMongoDBVectorSearch,
)
from llama\_index.core import VectorStoreIndex
from llama\_index.core import StorageContext
from llama\_index.core import SimpleDirectoryReader

connection\_string \= os.environ.get("AZURE\_COSMOSDB\_MONGODB\_URI")
mongodb\_client \= pymongo.MongoClient(connection\_string)
store \= AzureCosmosDBMongoDBVectorSearch(
    mongodb\_client\=mongodb\_client,
    db\_name\="demo\_vectordb",
    collection\_name\="paul\_graham\_essay",
)
storage\_context \= StorageContext.from\_defaults(vector\_store\=store)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

import pymongo from llama\_index.vector\_stores.azurecosmosmongo import ( AzureCosmosDBMongoDBVectorSearch, ) from llama\_index.core import VectorStoreIndex from llama\_index.core import StorageContext from llama\_index.core import SimpleDirectoryReader connection\_string = os.environ.get("AZURE\_COSMOSDB\_MONGODB\_URI") mongodb\_client = pymongo.MongoClient(connection\_string) store = AzureCosmosDBMongoDBVectorSearch( mongodb\_client=mongodb\_client, db\_name="demo\_vectordb", collection\_name="paul\_graham\_essay", ) storage\_context = StorageContext.from\_defaults(vector\_store=store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

### Query the index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureCosmosDBMongoDBvCoreDemo/#query-the-index)

We can now ask questions using our index.

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did the author love working on?")

query\_engine = index.as\_query\_engine() response = query\_engine.query("What did the author love working on?")

In \[ \]:

Copied!

import textwrap

print(textwrap.fill(str(response), 100))

import textwrap print(textwrap.fill(str(response), 100))

The author loved working on multiple projects that were not their thesis while in grad school,
including Lisp hacking and writing On Lisp. They eventually wrote a dissertation on applications of
continuations in just 5 weeks to graduate. Afterward, they applied to art schools and were accepted
into the BFA program at RISD.

In \[ \]:

Copied!

response \= query\_engine.query("What did he/she do in summer of 2016?")

response = query\_engine.query("What did he/she do in summer of 2016?")

In \[ \]:

Copied!

print(textwrap.fill(str(response), 100))

print(textwrap.fill(str(response), 100))

The person moved to England with their family in the summer of 2016.

Back to top

[Previous Azure AI Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureAISearchIndexDemo/)[Next Bagel Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BagelAutoRetriever/)
