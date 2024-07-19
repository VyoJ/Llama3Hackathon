Title: VearchDemo - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/VearchDemo/

Markdown Content:
VearchDemo - LlamaIndex


       

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

In \[ \]:

Copied!

import openai
from IPython.display import Markdown, display
from llama\_index import SimpleDirectoryReader, StorageContext, VectorStoreIndex

openai.api\_key \= ""

import openai from IPython.display import Markdown, display from llama\_index import SimpleDirectoryReader, StorageContext, VectorStoreIndex openai.api\_key = ""

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/examples/data/paul\_graham/paul\_graham\_essay.txt'
\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()
print("Document ID:", len(documents), documents\[0\].doc\_id)

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' # load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data() print("Document ID:", len(documents), documents\[0\].doc\_id)

Document ID: 1 8d84aefd-ca73-4c1e-b83d-141c1b1b3ba6

In \[ \]:

Copied!

from llama\_index import ServiceContext
from llama\_index.embeddings import HuggingFaceEmbedding
from llama\_index.vector\_stores import VearchVectorStore

"""
vearch cluster
"""
vector\_store \= VearchVectorStore(
    path\_or\_url\="http://liama-index-router.vectorbase.svc.sq01.n.jd.local",
    table\_name\="liama\_index\_test2",
    db\_name\="liama\_index",
    flag\=1,
)

"""
vearch standalone
"""
\# vector\_store = VearchVectorStore(
\#         path\_or\_url = '/data/zhx/zhx/liama\_index/knowledge\_base/liama\_index\_teststandalone',
\#         # path\_or\_url = 'http://liama-index-router.vectorbase.svc.sq01.n.jd.local',
\#         table\_name = 'liama\_index\_teststandalone',
\#         db\_name = 'liama\_index',
\#         flag = 0)

embed\_model \= HuggingFaceEmbedding(model\_name\="BAAI/bge-small-en-v1.5")
service\_context \= ServiceContext.from\_defaults(embed\_model\=embed\_model)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context, service\_context\=service\_context
)

from llama\_index import ServiceContext from llama\_index.embeddings import HuggingFaceEmbedding from llama\_index.vector\_stores import VearchVectorStore """ vearch cluster """ vector\_store = VearchVectorStore( path\_or\_url="http://liama-index-router.vectorbase.svc.sq01.n.jd.local", table\_name="liama\_index\_test2", db\_name="liama\_index", flag=1, ) """ vearch standalone """ # vector\_store = VearchVectorStore( # path\_or\_url = '/data/zhx/zhx/liama\_index/knowledge\_base/liama\_index\_teststandalone', # # path\_or\_url = 'http://liama-index-router.vectorbase.svc.sq01.n.jd.local', # table\_name = 'liama\_index\_teststandalone', # db\_name = 'liama\_index', # flag = 0) embed\_model = HuggingFaceEmbedding(model\_name="BAAI/bge-small-en-v1.5") service\_context = ServiceContext.from\_defaults(embed\_model=embed\_model) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context, service\_context=service\_context )

Loading checkpoint shards:   0%|          | 0/7 \[00:00<?, ?it/s\]

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did the author do growing up?")
display(Markdown(f"<b>{response}</b>"))

query\_engine = index.as\_query\_engine() response = query\_engine.query("What did the author do growing up?") display(Markdown(f"**{response}**"))

**The author did not provide any information about their growing up.**

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()
response \= query\_engine.query(
    "What did the author do after his time at Y Combinator?"
)
display(Markdown(f"<b>{response}</b>"))

query\_engine = index.as\_query\_engine() response = query\_engine.query( "What did the author do after his time at Y Combinator?" ) display(Markdown(f"**{response}**"))

**The author wrote all of Y Combinator's internal software in Arc while continuing to work on Y Combinator, but later stopped working on Arc and focused on writing essays and working on Y Combinator. In 2012, the author's mother had a stroke, and the author realized that Y Combinator was taking up too much of their time and decided to hand it over to someone else. The author suggested this to Robert Morris, who offered unsolicited advice to the author to make sure Y Combinator wasn't the last cool thing the author did. The author ultimately decided to hand over the leadership of Y Combinator to Sam Altman in 2013.**

Back to top

[Previous Upstash Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/UpstashVectorDemo/)[Next Google Vertex AI Vector Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VertexAIVectorSearchDemo/)
