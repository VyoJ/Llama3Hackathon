Title: VoyageAI Rerank - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/VoyageAIRerank/

Markdown Content:
VoyageAI Rerank - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index \> /dev/null
%pip install llama\-index\-postprocessor\-voyageai\-rerank \> /dev/null
%pip install llama\-index\-embeddings\-voyageai \> /dev/null

%pip install llama-index > /dev/null %pip install llama-index-postprocessor-voyageai-rerank > /dev/null %pip install llama-index-embeddings-voyageai > /dev/null

\[notice\] A new release of pip is available: 23.3.2 -> 24.0
\[notice\] To update, run: pip install --upgrade pip
Note: you may need to restart the kernel to use updated packages.

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.core.response.pprint\_utils import pprint\_response

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.core.response.pprint\_utils import pprint\_response

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

\--2024-05-09 17:56:26--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 2606:50c0:8003::154, 2606:50c0:8000::154, 2606:50c0:8002::154, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|2606:50c0:8003::154|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 75042 (73K) \[text/plain\]
Saving to: ‘data/paul\_graham/paul\_graham\_essay.txt’

data/paul\_graham/pa 100%\[>\]  73.28K  --.-KB/s    in 0.009s  

2024-05-09 17:56:26 (7.81 MB/s) - ‘data/paul\_graham/paul\_graham\_essay.txt’ saved \[75042/75042\]

In \[ \]:

Copied!

import os
from llama\_index.embeddings.voyageai import VoyageEmbedding

api\_key \= os.environ\["VOYAGE\_API\_KEY"\]
voyageai\_embeddings \= VoyageEmbedding(
    voyage\_api\_key\=api\_key, model\_name\="voyage-large-2"
)

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

\# build index
index \= VectorStoreIndex.from\_documents(
    documents\=documents, embed\_model\=voyageai\_embeddings
)

import os from llama\_index.embeddings.voyageai import VoyageEmbedding api\_key = os.environ\["VOYAGE\_API\_KEY"\] voyageai\_embeddings = VoyageEmbedding( voyage\_api\_key=api\_key, model\_name="voyage-large-2" ) # load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data() # build index index = VectorStoreIndex.from\_documents( documents=documents, embed\_model=voyageai\_embeddings )

#### Retrieve top 10 most relevant nodes, then filter with VoyageAI Rerank[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/VoyageAIRerank/#retrieve-top-10-most-relevant-nodes-then-filter-with-voyageai-rerank)

In \[ \]:

Copied!

from llama\_index.postprocessor.voyageai\_rerank import VoyageAIRerank

voyageai\_rerank \= VoyageAIRerank(
    api\_key\=api\_key, top\_k\=2, model\="rerank-lite-1", truncation\=True
)

from llama\_index.postprocessor.voyageai\_rerank import VoyageAIRerank voyageai\_rerank = VoyageAIRerank( api\_key=api\_key, top\_k=2, model="rerank-lite-1", truncation=True )

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(
    similarity\_top\_k\=10,
    node\_postprocessors\=\[voyageai\_rerank\],
)
response \= query\_engine.query(
    "What did Sam Altman do in this essay?",
)

query\_engine = index.as\_query\_engine( similarity\_top\_k=10, node\_postprocessors=\[voyageai\_rerank\], ) response = query\_engine.query( "What did Sam Altman do in this essay?", )

In \[ \]:

Copied!

pprint\_response(response, show\_source\=True)

pprint\_response(response, show\_source=True)

### Directly retrieve top 2 most similar nodes[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/VoyageAIRerank/#directly-retrieve-top-2-most-similar-nodes)

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(
    similarity\_top\_k\=2,
)
response \= query\_engine.query(
    "What did Sam Altman do in this essay?",
)

query\_engine = index.as\_query\_engine( similarity\_top\_k=2, ) response = query\_engine.query( "What did Sam Altman do in this essay?", )

Retrieved context is irrelevant and response is hallucinated.

In \[ \]:

Copied!

pprint\_response(response, show\_source\=True)

pprint\_response(response, show\_source=True)

Back to top

[Previous Time-Weighted Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/TimeWeightedPostprocessorDemo/)[Next OpenVINO Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/openvino_rerank/)

Hi, how can I help you?

🦙
