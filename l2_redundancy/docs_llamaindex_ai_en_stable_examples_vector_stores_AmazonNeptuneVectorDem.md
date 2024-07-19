Title: Amazon Neptune - Neptune Analytics vector store

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/AmazonNeptuneVectorDemo/

Markdown Content:
Amazon Neptune - Neptune Analytics vector store - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-neptune

%pip install llama-index-vector-stores-neptune

Initiate Neptune Analytics vector wrapper[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AmazonNeptuneVectorDemo/#initiate-neptune-analytics-vector-wrapper)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.vector\_stores.neptune import NeptuneAnalyticsVectorStore

graph\_identifier \= ""
embed\_dim \= 1536

neptune\_vector\_store \= NeptuneAnalyticsVectorStore(
    graph\_identifier\=graph\_identifier, embedding\_dimension\=1536
)

from llama\_index.vector\_stores.neptune import NeptuneAnalyticsVectorStore graph\_identifier = "" embed\_dim = 1536 neptune\_vector\_store = NeptuneAnalyticsVectorStore( graph\_identifier=graph\_identifier, embedding\_dimension=1536 )

Load documents, build the VectorStoreIndex[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AmazonNeptuneVectorDemo/#load-documents-build-the-vectorstoreindex)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from IPython.display import Markdown, display

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from IPython.display import Markdown, display

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham").load\_data()

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham").load\_data()

In \[ \]:

Copied!

from llama\_index.core import StorageContext

storage\_context \= StorageContext.from\_defaults(
    vector\_store\=neptune\_vector\_store
)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

from llama\_index.core import StorageContext storage\_context = StorageContext.from\_defaults( vector\_store=neptune\_vector\_store ) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What happened at interleaf?")
display(Markdown(f"<b>{response}</b>"))

query\_engine = index.as\_query\_engine() response = query\_engine.query("What happened at interleaf?") display(Markdown(f"**{response}**"))

Back to top

[Previous Alibaba Cloud OpenSearch Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AlibabaCloudOpenSearchIndexDemo/)[Next AnalyticDB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AnalyticDBDemo/)
