Title: Metal Vector Store - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/MetalIndexDemo/

Markdown Content:
Metal Vector Store - LlamaIndex


Creating a Metal Vector Store[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MetalIndexDemo/#creating-a-metal-vector-store)
-------------------------------------------------------------------------------------------------------------------------------------------

1.  Register an account for [Metal](https://app.getmetal.io/)
2.  Generate an API key in [Metal's Settings](https://app.getmetal.io/settings/organization). Save the `api_key` + `client_id`
3.  Generate an Index in [Metal's Dashboard](https://app.getmetal.io/). Save the `index_id`

Load data into your Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MetalIndexDemo/#load-data-into-your-index)
-----------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-metal

%pip install llama-index-vector-stores-metal

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.vector\_stores.metal import MetalVectorStore
from IPython.display import Markdown, display

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.vector\_stores.metal import MetalVectorStore from IPython.display import Markdown, display

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

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data()

In \[ \]:

Copied!

\# initialize Metal Vector Store
from llama\_index.core import StorageContext

api\_key \= "api key"
client\_id \= "client id"
index\_id \= "index id"

vector\_store \= MetalVectorStore(
    api\_key\=api\_key,
    client\_id\=client\_id,
    index\_id\=index\_id,
)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

\# initialize Metal Vector Store from llama\_index.core import StorageContext api\_key = "api key" client\_id = "client id" index\_id = "index id" vector\_store = MetalVectorStore( api\_key=api\_key, client\_id=client\_id, index\_id=index\_id, ) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

Query Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MetalIndexDemo/#query-index)
-------------------------------------------------------------------------------------------------------

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

Back to top

[Previous Lantern Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanternIndexDemo/)[Next Milvus Vector Store With Hybrid Retrieval](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusHybridIndexDemo/)
