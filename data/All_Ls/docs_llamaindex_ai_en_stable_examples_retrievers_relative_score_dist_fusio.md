Title: Relative Score Fusion and Distribution-Based Score Fusion

URL Source: https://docs.llamaindex.ai/en/stable/examples/retrievers/relative_score_dist_fusion/

Markdown Content:
Relative Score Fusion and Distribution-Based Score Fusion - LlamaIndex


In this example, we demonstrate using QueryFusionRetriever with two methods which aim to improve on Reciprocal Rank Fusion:

1.  Relative Score Fusion ([Weaviate](https://weaviate.io/blog/hybrid-search-fusion-algorithms))
2.  Distribution-Based Score Fusion ([Mazzeschi: blog post](https://medium.com/plain-simple-software/distribution-based-score-fusion-dbsf-a-new-approach-to-vector-search-ranking-f87c37488b18))

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai
%pip install llama\-index\-retrievers\-bm25

%pip install llama-index-llms-openai %pip install llama-index-retrievers-bm25

In \[ \]:

Copied!

import os
import openai

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."
openai.api\_key \= os.environ\["OPENAI\_API\_KEY"\]

import os import openai os.environ\["OPENAI\_API\_KEY"\] = "sk-..." openai.api\_key = os.environ\["OPENAI\_API\_KEY"\]

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/relative_score_dist_fusion/#setup)
----------------------------------------------------------------------------------------------------

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

from llama\_index.core import SimpleDirectoryReader documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data()

Next, we will setup a vector index over the documentation.

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex
from llama\_index.core.node\_parser import SentenceSplitter

splitter \= SentenceSplitter(chunk\_size\=256)

index \= VectorStoreIndex.from\_documents(
    documents, transformations\=\[splitter\], show\_progress\=True
)

from llama\_index.core import VectorStoreIndex from llama\_index.core.node\_parser import SentenceSplitter splitter = SentenceSplitter(chunk\_size=256) index = VectorStoreIndex.from\_documents( documents, transformations=\[splitter\], show\_progress=True )

Parsing nodes: 100%|██████████| 1/1 \[00:00<00:00,  7.55it/s\]
Generating embeddings: 100%|██████████| 504/504 \[00:03<00:00, 128.32it/s\]

Create a Hybrid Fusion Retriever using Relative Score Fusion[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/relative_score_dist_fusion/#create-a-hybrid-fusion-retriever-using-relative-score-fusion)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this step, we fuse our index with a BM25 based retriever. This will enable us to capture both semantic relations and keywords in our input queries.

Since both of these retrievers calculate a score, we can use the `QueryFusionRetriever` to re-sort our nodes without using an additional models or excessive computation.

The following example uses the [Relative Score Fusion](https://weaviate.io/blog/hybrid-search-fusion-algorithms) algorithm from Weaviate, which applies a MinMax scaler to each result set, then makes a weighted sum. Here, we'll give the vector retriever slightly more weight than BM25 (0.6 vs. 0.4).

First, we create our retrievers. Each will retrieve the top-10 most similar nodes.

In \[ \]:

Copied!

from llama\_index.retrievers.bm25 import BM25Retriever

vector\_retriever \= index.as\_retriever(similarity\_top\_k\=5)

bm25\_retriever \= BM25Retriever.from\_defaults(
    docstore\=index.docstore, similarity\_top\_k\=10
)

from llama\_index.retrievers.bm25 import BM25Retriever vector\_retriever = index.as\_retriever(similarity\_top\_k=5) bm25\_retriever = BM25Retriever.from\_defaults( docstore=index.docstore, similarity\_top\_k=10 )

Next, we can create our fusion retriever, which well return the top-10 most similar nodes from the 20 returned nodes from the retrievers.

Note that the vector and BM25 retrievers may have returned all the same nodes, only in different orders; in this case, it simply acts as a re-ranker.

In \[ \]:

Copied!

from llama\_index.core.retrievers import QueryFusionRetriever

retriever \= QueryFusionRetriever(
    \[vector\_retriever, bm25\_retriever\],
    retriever\_weights\=\[0.6, 0.4\],
    similarity\_top\_k\=10,
    num\_queries\=1,  \# set this to 1 to disable query generation
    mode\="relative\_score",
    use\_async\=True,
    verbose\=True,
)

from llama\_index.core.retrievers import QueryFusionRetriever retriever = QueryFusionRetriever( \[vector\_retriever, bm25\_retriever\], retriever\_weights=\[0.6, 0.4\], similarity\_top\_k=10, num\_queries=1, # set this to 1 to disable query generation mode="relative\_score", use\_async=True, verbose=True, )

In \[ \]:

Copied!

\# apply nested async to run in a notebook
import nest\_asyncio

nest\_asyncio.apply()

\# apply nested async to run in a notebook import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

nodes\_with\_scores \= retriever.retrieve(
    "What happened at Interleafe and Viaweb?"
)

nodes\_with\_scores = retriever.retrieve( "What happened at Interleafe and Viaweb?" )

In \[ \]:

Copied!

for node in nodes\_with\_scores:
    print(f"Score: {node.score:.2f} - {node.text\[:100\]}...\\n\-----")

for node in nodes\_with\_scores: print(f"Score: {node.score:.2f} - {node.text\[:100\]}...\\n-----")

Score: 0.60 - You wouldn't need versions, or ports, or any of that crap. At Interleaf there had been a whole group...
-----
Score: 0.59 - The UI was horrible, but it proved you could build a whole store through the browser, without any cl...
-----
Score: 0.40 - We were determined to be the Microsoft Word, not the Interleaf. Which meant being easy to use and in...
-----
Score: 0.36 - In its time, the editor was one of the best general-purpose site builders. I kept the code tight and...
-----
Score: 0.25 - I kept the code tight and didn't have to integrate with any other software except Robert's and Trevo...
-----
Score: 0.25 - If all I'd had to do was work on this software, the next 3 years would have been the easiest of my l...
-----
Score: 0.21 - To find out, we decided to try making a version of our store builder that you could control through ...
-----
Score: 0.11 - But the most important thing I learned, and which I used in both Viaweb and Y Combinator, is that th...
-----
Score: 0.11 - The next year, from the summer of 1998 to the summer of 1999, must have been the least productive of...
-----
Score: 0.07 - The point is that it was really cheap, less than half market price.

\[8\] Most software you can launc...
-----

### Distribution-Based Score Fusion[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/relative_score_dist_fusion/#distribution-based-score-fusion)

A variant on Relative Score Fusion, [Distribution-Based Score Fusion](https://medium.com/plain-simple-software/distribution-based-score-fusion-dbsf-a-new-approach-to-vector-search-ranking-f87c37488b18) scales the scores a bit differently - based on the mean and standard deviation of the scores for each result set.

In \[ \]:

Copied!

from llama\_index.core.retrievers import QueryFusionRetriever

retriever \= QueryFusionRetriever(
    \[vector\_retriever, bm25\_retriever\],
    retriever\_weights\=\[0.6, 0.4\],
    similarity\_top\_k\=10,
    num\_queries\=1,  \# set this to 1 to disable query generation
    mode\="dist\_based\_score",
    use\_async\=True,
    verbose\=True,
)

nodes\_with\_scores \= retriever.retrieve(
    "What happened at Interleafe and Viaweb?"
)

for node in nodes\_with\_scores:
    print(f"Score: {node.score:.2f} - {node.text\[:100\]}...\\n\-----")

from llama\_index.core.retrievers import QueryFusionRetriever retriever = QueryFusionRetriever( \[vector\_retriever, bm25\_retriever\], retriever\_weights=\[0.6, 0.4\], similarity\_top\_k=10, num\_queries=1, # set this to 1 to disable query generation mode="dist\_based\_score", use\_async=True, verbose=True, ) nodes\_with\_scores = retriever.retrieve( "What happened at Interleafe and Viaweb?" ) for node in nodes\_with\_scores: print(f"Score: {node.score:.2f} - {node.text\[:100\]}...\\n-----")

Score: 0.42 - You wouldn't need versions, or ports, or any of that crap. At Interleaf there had been a whole group...
-----
Score: 0.41 - The UI was horrible, but it proved you could build a whole store through the browser, without any cl...
-----
Score: 0.32 - We were determined to be the Microsoft Word, not the Interleaf. Which meant being easy to use and in...
-----
Score: 0.30 - In its time, the editor was one of the best general-purpose site builders. I kept the code tight and...
-----
Score: 0.27 - To find out, we decided to try making a version of our store builder that you could control through ...
-----
Score: 0.24 - I kept the code tight and didn't have to integrate with any other software except Robert's and Trevo...
-----
Score: 0.24 - If all I'd had to do was work on this software, the next 3 years would have been the easiest of my l...
-----
Score: 0.20 - Now we felt like we were really onto something. I had visions of a whole new generation of software ...
-----
Score: 0.20 - Users wouldn't need anything more than a browser.

This kind of software, known as a web app, is com...
-----
Score: 0.18 - But the most important thing I learned, and which I used in both Viaweb and Y Combinator, is that th...
-----

Use in a Query Engine![¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/relative_score_dist_fusion/#use-in-a-query-engine)
-------------------------------------------------------------------------------------------------------------------------------------

Now, we can plug our retriever into a query engine to synthesize natural language responses.

In \[ \]:

Copied!

from llama\_index.core.query\_engine import RetrieverQueryEngine

query\_engine \= RetrieverQueryEngine.from\_args(retriever)

from llama\_index.core.query\_engine import RetrieverQueryEngine query\_engine = RetrieverQueryEngine.from\_args(retriever)

In \[ \]:

Copied!

response \= query\_engine.query("What happened at Interleafe and Viaweb?")

response = query\_engine.query("What happened at Interleafe and Viaweb?")

In \[ \]:

Copied!

from llama\_index.core.response.notebook\_utils import display\_response

display\_response(response)

from llama\_index.core.response.notebook\_utils import display\_response display\_response(response)

**`Final Response:`** At Interleaf, there was a group called Release Engineering that was as large as the group writing the software. They had to deal with versions, ports, and other complexities. In contrast, at Viaweb, the software could be updated directly on the server, simplifying the process. Viaweb was founded with $10,000 in seed funding, and the software allowed building a whole store through the browser without the need for client software or command line inputs on the server. The company aimed to be easy to use and inexpensive, offering low monthly prices for their services.

Back to top

[Previous Recursive Retriever + Node References](https://docs.llamaindex.ai/en/stable/examples/retrievers/recursive_retriever_nodes/)[Next Router Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/router_retriever/)
