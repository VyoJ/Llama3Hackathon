Title: Astra DB - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/AstraDBIndexDemo/

Markdown Content:
Astra DB - LlamaIndex


> [DataStax Astra DB](https://docs.datastax.com/en/astra/home/astra.html) is a serverless vector-capable database built on Apache Cassandra and accessed through an easy-to-use JSON API.

To run this notebook you need a DataStax Astra DB instance running in the cloud (you can get one for free at [datastax.com](https://astra.datastax.com/)).

You should ensure you have `llama-index` and `astrapy` installed:

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-astra\-db

%pip install llama-index-vector-stores-astra-db

In \[ \]:

Copied!

!pip install llama\-index
!pip install "astrapy>=0.6.0"

!pip install llama-index !pip install "astrapy>=0.6.0"

### Please provide database connection parameters and secrets:[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AstraDBIndexDemo/#please-provide-database-connection-parameters-and-secrets)

In \[ \]:

Copied!

import os
import getpass

api\_endpoint \= input(
    "\\nPlease enter your Database Endpoint URL (e.g. 'https://4bc...datastax.com'):"
)

token \= getpass.getpass(
    "\\nPlease enter your 'Database Administrator' Token (e.g. 'AstraCS:...'):"
)

os.environ\["OPENAI\_API\_KEY"\] \= getpass.getpass(
    "\\nPlease enter your OpenAI API Key (e.g. 'sk-...'):"
)

import os import getpass api\_endpoint = input( "\\nPlease enter your Database Endpoint URL (e.g. 'https://4bc...datastax.com'):" ) token = getpass.getpass( "\\nPlease enter your 'Database Administrator' Token (e.g. 'AstraCS:...'):" ) os.environ\["OPENAI\_API\_KEY"\] = getpass.getpass( "\\nPlease enter your OpenAI API Key (e.g. 'sk-...'):" )

### Import needed package dependencies:[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AstraDBIndexDemo/#import-needed-package-dependencies)

In \[ \]:

Copied!

from llama\_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
)
from llama\_index.vector\_stores.astra\_db import AstraDBVectorStore

from llama\_index.core import ( VectorStoreIndex, SimpleDirectoryReader, StorageContext, ) from llama\_index.vector\_stores.astra\_db import AstraDBVectorStore

### Load some example data:[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AstraDBIndexDemo/#load-some-example-data)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

### Read the data:[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AstraDBIndexDemo/#read-the-data)

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()
print(f"Total documents: {len(documents)}")
print(f"First document, id: {documents\[0\].doc\_id}")
print(f"First document, hash: {documents\[0\].hash}")
print(
    "First document, text"
    f" ({len(documents\[0\].text)} characters):\\n{'='\*20}\\n{documents\[0\].text\[:360\]} ..."
)

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data() print(f"Total documents: {len(documents)}") print(f"First document, id: {documents\[0\].doc\_id}") print(f"First document, hash: {documents\[0\].hash}") print( "First document, text" f" ({len(documents\[0\].text)} characters):\\n{'='\*20}\\n{documents\[0\].text\[:360\]} ..." )

### Create the Astra DB Vector Store object:[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AstraDBIndexDemo/#create-the-astra-db-vector-store-object)

In \[ \]:

Copied!

astra\_db\_store \= AstraDBVectorStore(
    token\=token,
    api\_endpoint\=api\_endpoint,
    collection\_name\="astra\_v\_table",
    embedding\_dimension\=1536,
)

astra\_db\_store = AstraDBVectorStore( token=token, api\_endpoint=api\_endpoint, collection\_name="astra\_v\_table", embedding\_dimension=1536, )

### Build the Index from the Documents:[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AstraDBIndexDemo/#build-the-index-from-the-documents)

In \[ \]:

Copied!

storage\_context \= StorageContext.from\_defaults(vector\_store\=astra\_db\_store)

index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

storage\_context = StorageContext.from\_defaults(vector\_store=astra\_db\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

### Query using the index:[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AstraDBIndexDemo/#query-using-the-index)

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("Why did the author choose to work on AI?")

print(response.response)

query\_engine = index.as\_query\_engine() response = query\_engine.query("Why did the author choose to work on AI?") print(response.response)

Back to top

[Previous AnalyticDB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AnalyticDBDemo/)[Next Simple Vector Store - Async Index Creation](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AsyncIndexCreationDemo/)
