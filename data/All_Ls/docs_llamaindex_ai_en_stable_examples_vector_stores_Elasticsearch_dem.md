Title: Elasticsearch - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/Elasticsearch_demo/

Markdown Content:
Elasticsearch - LlamaIndex


> [Elasticsearch](http://www.github.com/elastic/elasticsearch) is a search database, that supports full text and vector searches.

Basic Example[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Elasticsearch_demo/#basic-example)
---------------------------------------------------------------------------------------------------------------

In this basic example, we take the a Paul Graham essay, split it into chunks, embed it using an open-source embedding model, load it into Elasticsearch, and then query it. For an example using different retrieval strategies see [Elasticsearch Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ElasticsearchIndexDemo/).

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install \-qU llama\-index\-vector\-stores\-elasticsearch llama\-index\-embeddings\-huggingface llama\-index

%pip install -qU llama-index-vector-stores-elasticsearch llama-index-embeddings-huggingface llama-index

In \[ \]:

Copied!

\# import
from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.vector\_stores.elasticsearch import ElasticsearchStore
from llama\_index.core import StorageContext

\# import from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.vector\_stores.elasticsearch import ElasticsearchStore from llama\_index.core import StorageContext

In \[ \]:

Copied!

\# set up OpenAI
import os
import getpass

os.environ\["OPENAI\_API\_KEY"\] \= getpass.getpass("OpenAI API Key:")

\# set up OpenAI import os import getpass os.environ\["OPENAI\_API\_KEY"\] = getpass.getpass("OpenAI API Key:")

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget \-nv 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget -nv 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

2024-05-13 15:10:43 URL:https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt \[75042/75042\] -> "data/paul\_graham/paul\_graham\_essay.txt" \[1\]

In \[ \]:

Copied!

from llama\_index.embeddings.huggingface import HuggingFaceEmbedding
from llama\_index.core import Settings

\# define embedding function
Settings.embed\_model \= HuggingFaceEmbedding(
    model\_name\="BAAI/bge-small-en-v1.5"
)

from llama\_index.embeddings.huggingface import HuggingFaceEmbedding from llama\_index.core import Settings # define embedding function Settings.embed\_model = HuggingFaceEmbedding( model\_name="BAAI/bge-small-en-v1.5" )

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

\# define index
vector\_store \= ElasticsearchStore(
    es\_url\="http://localhost:9200",  \# see Elasticsearch Vector Store for more authentication options
    index\_name\="paul\_graham\_essay",
)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data() # define index vector\_store = ElasticsearchStore( es\_url="http://localhost:9200", # see Elasticsearch Vector Store for more authentication options index\_name="paul\_graham\_essay", ) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

In \[ \]:

Copied!

\# Query Data
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did the author do growing up?")
print(response)

\# Query Data query\_engine = index.as\_query\_engine() response = query\_engine.query("What did the author do growing up?") print(response)

The author worked on writing and programming outside of school. They wrote short stories and tried writing programs on an IBM 1401 computer. They also built a microcomputer kit and started programming on it, writing simple games and a word processor.

Back to top

[Previous Elasticsearch Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ElasticsearchIndexDemo/)[Next Epsilla Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/EpsillaIndexDemo/)
