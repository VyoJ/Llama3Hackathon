Title: Typesense Vector Store - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/TypesenseDemo/

Markdown Content:
Typesense Vector Store - LlamaIndex


#### Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TypesenseDemo/#download-data)

In \[ \]:

Copied!

%pip install llama\-index\-embeddings\-openai
%pip install llama\-index\-vector\-stores\-typesense

%pip install llama-index-embeddings-openai %pip install llama-index-vector-stores-typesense

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

#### Load documents, build the VectorStoreIndex[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TypesenseDemo/#load-documents-build-the-vectorstoreindex)

In \[ \]:

Copied!

\# import logging
\# import sys

\# logging.basicConfig(stream=sys.stdout, level=logging.INFO)
\# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from llama\_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
)
from IPython.display import Markdown, display

\# import logging # import sys # logging.basicConfig(stream=sys.stdout, level=logging.INFO) # logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout)) from llama\_index.core import ( VectorStoreIndex, SimpleDirectoryReader, StorageContext, ) from IPython.display import Markdown, display

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data()

In \[ \]:

Copied!

from llama\_index.vector\_stores.typesense import TypesenseVectorStore
from typesense import Client

typesense\_client \= Client(
    {
        "api\_key": "xyz",
        "nodes": \[{"host": "localhost", "port": "8108", "protocol": "http"}\],
        "connection\_timeout\_seconds": 2,
    }
)
typesense\_vector\_store \= TypesenseVectorStore(typesense\_client)
storage\_context \= StorageContext.from\_defaults(
    vector\_store\=typesense\_vector\_store
)

index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

from llama\_index.vector\_stores.typesense import TypesenseVectorStore from typesense import Client typesense\_client = Client( { "api\_key": "xyz", "nodes": \[{"host": "localhost", "port": "8108", "protocol": "http"}\], "connection\_timeout\_seconds": 2, } ) typesense\_vector\_store = TypesenseVectorStore(typesense\_client) storage\_context = StorageContext.from\_defaults( vector\_store=typesense\_vector\_store ) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

#### Query Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TypesenseDemo/#query-index)

In \[ \]:

Copied!

from llama\_index.core import QueryBundle
from llama\_index.embeddings.openai import OpenAIEmbedding

\# By default, typesense vector store uses vector search. You need to provide the embedding yourself.
query\_str \= "What did the author do growing up?"
embed\_model \= OpenAIEmbedding()
\# You can also get the settings from the Settings object
from llama\_index.core import Settings

\# embed\_model = Settings.embed\_model
query\_embedding \= embed\_model.get\_agg\_embedding\_from\_queries(query\_str)
query\_bundle \= QueryBundle(query\_str, embedding\=query\_embedding)
response \= index.as\_query\_engine().query(query\_bundle)

display(Markdown(f"<b>{response}</b>"))

from llama\_index.core import QueryBundle from llama\_index.embeddings.openai import OpenAIEmbedding # By default, typesense vector store uses vector search. You need to provide the embedding yourself. query\_str = "What did the author do growing up?" embed\_model = OpenAIEmbedding() # You can also get the settings from the Settings object from llama\_index.core import Settings # embed\_model = Settings.embed\_model query\_embedding = embed\_model.get\_agg\_embedding\_from\_queries(query\_str) query\_bundle = QueryBundle(query\_str, embedding=query\_embedding) response = index.as\_query\_engine().query(query\_bundle) display(Markdown(f"**{response}**"))

**The author grew up skipping a step in the evolution of computers, learning Italian, walking through Florence, painting people, working with technology companies, seeking signature styles at RISD, living in a rent-stabilized apartment, launching software, editing code (including Lisp expressions), writing essays, publishing them online, and receiving feedback from angry readers. He also experienced the exponential growth of commodity processors in the 1990s, which rolled up high-end, special-purpose hardware and software companies. He also learned how to make a little Italian go a long way by stringing together abstract concepts with a few simple verbs. He also experienced the tight coupling of money and coolness in the art world, and the fact that anything expensive comes to be seen as cool, and anything seen as cool will soon become equally expensive. He also experienced the challenge of launching software, as he had to recruit an initial set of users and make sure they had decent-looking stores before launching publicly. He also experienced the first instance of what is now a familiar experience, when he read the comments and found they were full of angry people. He also experienced the difference between putting something online and publishing it online. Finally, he wrote essays about topics he had stacked up, and wrote a more detailed version for others to read.

**

In \[ \]:

Copied!

from llama\_index.core.vector\_stores.types import VectorStoreQueryMode

\# You can also use text search

query\_bundle \= QueryBundle(query\_str\=query\_str)
response \= index.as\_query\_engine(
    vector\_store\_query\_mode\=VectorStoreQueryMode.TEXT\_SEARCH
).query(query\_bundle)
display(Markdown(f"<b>{response}</b>"))

from llama\_index.core.vector\_stores.types import VectorStoreQueryMode # You can also use text search query\_bundle = QueryBundle(query\_str=query\_str) response = index.as\_query\_engine( vector\_store\_query\_mode=VectorStoreQueryMode.TEXT\_SEARCH ).query(query\_bundle) display(Markdown(f"**{response}**"))

**The author grew up during the Internet Bubble and was running a startup. They had to hire more people than they wanted to in order to seem more professional and were at the mercy of their investors until Yahoo bought them. They learned a lot about retail and startups, and had to do a lot of things that they weren't necessarily good at in order to make their business successful.

**

Back to top

[Previous txtai Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TxtaiIndexDemo/)[Next Upstash Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/UpstashVectorDemo/)
