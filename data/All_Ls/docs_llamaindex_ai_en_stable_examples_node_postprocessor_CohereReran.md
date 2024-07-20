Title: Cohere Rerank - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/CohereRerank/

Markdown Content:
Cohere Rerank - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index \> /dev/null
%pip install llama\-index\-postprocessor\-cohere\-rerank \> /dev/null

%pip install llama-index > /dev/null %pip install llama-index-postprocessor-cohere-rerank > /dev/null

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

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

\# build index
index \= VectorStoreIndex.from\_documents(documents\=documents)

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data() # build index index = VectorStoreIndex.from\_documents(documents=documents)

#### Retrieve top 10 most relevant nodes, then filter with Cohere Rerank[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/CohereRerank/#retrieve-top-10-most-relevant-nodes-then-filter-with-cohere-rerank)

In \[ \]:

Copied!

import os
from llama\_index.postprocessor.cohere\_rerank import CohereRerank

api\_key \= os.environ\["COHERE\_API\_KEY"\]
cohere\_rerank \= CohereRerank(api\_key\=api\_key, top\_n\=2)

import os from llama\_index.postprocessor.cohere\_rerank import CohereRerank api\_key = os.environ\["COHERE\_API\_KEY"\] cohere\_rerank = CohereRerank(api\_key=api\_key, top\_n=2)

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(
    similarity\_top\_k\=10,
    node\_postprocessors\=\[cohere\_rerank\],
)
response \= query\_engine.query(
    "What did Sam Altman do in this essay?",
)

query\_engine = index.as\_query\_engine( similarity\_top\_k=10, node\_postprocessors=\[cohere\_rerank\], ) response = query\_engine.query( "What did Sam Altman do in this essay?", )

In \[ \]:

Copied!

pprint\_response(response, show\_source\=True)

pprint\_response(response, show\_source=True)

Final Response: Sam Altman was asked if he wanted to be the president
of Y Combinator. Initially, he declined as he wanted to start a
startup focused on making nuclear reactors. However, after persistent
persuasion, he eventually agreed to become the president of Y
Combinator starting with the winter 2014 batch.
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Source Node 1/2
Node ID: 7ecf4eb2-215d-45e4-ba08-44d9219c7fa6
Similarity: 0.93033177
Text: When I was dealing with some urgent problem during YC, there was
about a 60% chance it had to do with HN, and a 40% chance it had do
with everything else combined. \[17\]  As well as HN, I wrote all of
YC's internal software in Arc. But while I continued to work a good
deal in Arc, I gradually stopped working on Arc, partly because I
didn't have t...
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Source Node 2/2
Node ID: 88be17e9-e0a0-49e1-9ff8-f2b7aa7493ed
Similarity: 0.86269903
Text: Up till that point YC had been controlled by the original LLC we
four had started. But we wanted YC to last for a long time, and to do
that it couldn't be controlled by the founders. So if Sam said yes,
we'd let him reorganize YC. Robert and I would retire, and Jessica and
Trevor would become ordinary partners.  When we asked Sam if he wanted
to...

### Directly retrieve top 2 most similar nodes[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/CohereRerank/#directly-retrieve-top-2-most-similar-nodes)

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

Final Response: Sam Altman was asked to become the president of Y
Combinator, initially declined the offer to pursue starting a startup
focused on nuclear reactors, but eventually agreed to take over
starting with the winter 2014 batch.
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Source Node 1/2
Node ID: 7ecf4eb2-215d-45e4-ba08-44d9219c7fa6
Similarity: 0.8308840369082053
Text: When I was dealing with some urgent problem during YC, there was
about a 60% chance it had to do with HN, and a 40% chance it had do
with everything else combined. \[17\]  As well as HN, I wrote all of
YC's internal software in Arc. But while I continued to work a good
deal in Arc, I gradually stopped working on Arc, partly because I
didn't have t...
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Source Node 2/2
Node ID: 88be17e9-e0a0-49e1-9ff8-f2b7aa7493ed
Similarity: 0.8230144027954406
Text: Up till that point YC had been controlled by the original LLC we
four had started. But we wanted YC to last for a long time, and to do
that it couldn't be controlled by the founders. So if Sam said yes,
we'd let him reorganize YC. Robert and I would retire, and Jessica and
Trevor would become ordinary partners.  When we asked Sam if he wanted
to...

Back to top

[Previous Semantic double merging chunking](https://docs.llamaindex.ai/en/stable/examples/node_parsers/semantic_double_merging_chunking/)[Next Colbert Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/ColbertRerank/)

Hi, how can I help you?

🦙
