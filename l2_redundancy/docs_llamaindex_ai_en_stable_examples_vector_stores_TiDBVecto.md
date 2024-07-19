Title: TiDB Vector Store - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/TiDBVector/

Markdown Content:
TiDB Vector Store - LlamaIndex


> [TiDB Cloud](https://tidbcloud.com/), is a comprehensive Database-as-a-Service (DBaaS) solution, that provides dedicated and serverless options. TiDB Serverless is now integrating a built-in vector search into the MySQL landscape. With this enhancement, you can seamlessly develop AI applications using TiDB Serverless without the need for a new database or additional technical stacks. Be among the first to experience it by joining the waitlist for the private beta at [https://tidb.cloud/ai](https://tidb.cloud/ai).

This notebook provides a detailed guide on utilizing the tidb vector search in LlamaIndex.

Setting up environments[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TiDBVector/#setting-up-environments)
---------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-tidbvector
%pip install llama\-index

%pip install llama-index-vector-stores-tidbvector %pip install llama-index

In \[ \]:

Copied!

import textwrap

from llama\_index.core import SimpleDirectoryReader, StorageContext
from llama\_index.core import VectorStoreIndex
from llama\_index.vector\_stores.tidbvector import TiDBVectorStore

import textwrap from llama\_index.core import SimpleDirectoryReader, StorageContext from llama\_index.core import VectorStoreIndex from llama\_index.vector\_stores.tidbvector import TiDBVectorStore

Configure both the OpenAI and TiDB host settings that you will need

In \[ \]:

Copied!

\# Here we useimport getpass
import getpass
import os

os.environ\["OPENAI\_API\_KEY"\] \= getpass.getpass("OpenAI API Key:")
tidb\_connection\_url \= getpass.getpass(
    "TiDB connection URL (format - mysql+pymysql://root@127.0.0.1:4000/test): "
)

\# Here we useimport getpass import getpass import os os.environ\["OPENAI\_API\_KEY"\] = getpass.getpass("OpenAI API Key:") tidb\_connection\_url = getpass.getpass( "TiDB connection URL (format - mysql+pymysql://root@127.0.0.1:4000/test): " )

Prepare data that used to show case

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

In \[ \]:

Copied!

documents \= SimpleDirectoryReader("./data/paul\_graham").load\_data()
print("Document ID:", documents\[0\].doc\_id)
for index, document in enumerate(documents):
    document.metadata \= {"book": "paul\_graham"}

documents = SimpleDirectoryReader("./data/paul\_graham").load\_data() print("Document ID:", documents\[0\].doc\_id) for index, document in enumerate(documents): document.metadata = {"book": "paul\_graham"}

Document ID: d970e919-4469-414b-967e-24dd9b2eb014

Create TiDB Vectore Store[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TiDBVector/#create-tidb-vectore-store)
-------------------------------------------------------------------------------------------------------------------------------

The code snippet below creates a table named `VECTOR_TABLE_NAME` in TiDB, optimized for vector searching. Upon successful execution of this code, you will be able to view and access the `VECTOR_TABLE_NAME` table directly within your TiDB database environment

In \[ \]:

Copied!

VECTOR\_TABLE\_NAME \= "paul\_graham\_test"
tidbvec \= TiDBVectorStore(
    connection\_string\=tidb\_connection\_url,
    table\_name\=VECTOR\_TABLE\_NAME,
    distance\_strategy\="cosine",
    vector\_dimension\=1536,
    drop\_existing\_table\=False,
)

VECTOR\_TABLE\_NAME = "paul\_graham\_test" tidbvec = TiDBVectorStore( connection\_string=tidb\_connection\_url, table\_name=VECTOR\_TABLE\_NAME, distance\_strategy="cosine", vector\_dimension=1536, drop\_existing\_table=False, )

Create a query engine based on tidb vectore store

In \[ \]:

Copied!

storage\_context \= StorageContext.from\_defaults(vector\_store\=tidbvec)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context, show\_progress\=True
)

storage\_context = StorageContext.from\_defaults(vector\_store=tidbvec) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context, show\_progress=True )

/Users/ianz/Work/miniconda3/envs/llama\_index/lib/python3.10/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user\_install.html
  from .autonotebook import tqdm as notebook\_tqdm
Parsing nodes: 100%|██████████| 1/1 \[00:00<00:00,  8.76it/s\]
Generating embeddings: 100%|██████████| 21/21 \[00:02<00:00,  8.22it/s\]

Semantic similarity search[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TiDBVector/#semantic-similarity-search)
---------------------------------------------------------------------------------------------------------------------------------

This section focus on vector search basics and refining results using metadata filters. Please note that tidb vector only supports Deafult VectorStoreQueryMode.

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did the author do?")
print(textwrap.fill(str(response), 100))

query\_engine = index.as\_query\_engine() response = query\_engine.query("What did the author do?") print(textwrap.fill(str(response), 100))

The author worked on writing, programming, building microcomputers, giving talks at conferences,
publishing essays online, developing spam filters, painting, hosting dinner parties, and purchasing
a building for office use.

### Filter with metadata[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TiDBVector/#filter-with-metadata)

perform searches using metadata filters to retrieve a specific number of nearest-neighbor results that align with the applied filters.

In \[ \]:

Copied!

from llama\_index.core.vector\_stores.types import (
    MetadataFilter,
    MetadataFilters,
)

query\_engine \= index.as\_query\_engine(
    filters\=MetadataFilters(
        filters\=\[
            MetadataFilter(key\="book", value\="paul\_graham", operator\="!="),
        \]
    ),
    similarity\_top\_k\=2,
)
response \= query\_engine.query("What did the author learn?")
print(textwrap.fill(str(response), 100))

from llama\_index.core.vector\_stores.types import ( MetadataFilter, MetadataFilters, ) query\_engine = index.as\_query\_engine( filters=MetadataFilters( filters=\[ MetadataFilter(key="book", value="paul\_graham", operator="!="), \] ), similarity\_top\_k=2, ) response = query\_engine.query("What did the author learn?") print(textwrap.fill(str(response), 100))

Empty Response

Query again

In \[ \]:

Copied!

from llama\_index.core.vector\_stores.types import (
    MetadataFilter,
    MetadataFilters,
)

query\_engine \= index.as\_query\_engine(
    filters\=MetadataFilters(
        filters\=\[
            MetadataFilter(key\="book", value\="paul\_graham", operator\=""), \] ), similarity\_top\_k=2, ) response = query\_engine.query("What did the author learn?") print(textwrap.fill(str(response), 100))

The author learned programming on an IBM 1401 using an early version of Fortran in 9th grade, then
later transitioned to working with microcomputers like the TRS-80 and Apple II. Additionally, the
author studied philosophy in college but found it unfulfilling, leading to a switch to studying AI.
Later on, the author attended art school in both the US and Italy, where they observed a lack of
substantial teaching in the painting department.

Delete documents[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TiDBVector/#delete-documents)
-------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

tidbvec.delete(documents\[0\].doc\_id)

tidbvec.delete(documents\[0\].doc\_id)

Check whether the documents had been deleted

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did the author learn?")
print(textwrap.fill(str(response), 100))

query\_engine = index.as\_query\_engine() response = query\_engine.query("What did the author learn?") print(textwrap.fill(str(response), 100))

Empty Response

Back to top

[Previous Tencent Cloud VectorDB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TencentVectorDBIndexDemo/)[Next Timescale Vector Store (PostgreSQL)](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Timescalevector/)
