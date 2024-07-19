Title: Reciprocal Rerank Fusion Retriever - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/retrievers/reciprocal_rerank_fusion/

Markdown Content:
Reciprocal Rerank Fusion Retriever - LlamaIndex


In this example, we walk through how you can combine retrieval results from multiple queries and multiple indexes.

The retrieved nodes will be reranked according to the `Reciprocal Rerank Fusion` algorithm demonstrated in this [paper](https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf). It provides an effecient method for rerranking retrieval results without excessive computation or reliance on external models.

Full credits go to @Raduaschl on github for their [example implementation here](https://github.com/Raudaschl/rag-fusion).

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

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/reciprocal_rerank_fusion/#setup)
--------------------------------------------------------------------------------------------------

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

\--2024-02-12 17:59:58--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 2606:50c0:8003::154, 2606:50c0:8001::154, 2606:50c0:8002::154, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|2606:50c0:8003::154|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 75042 (73K) \[text/plain\]
Saving to: ‘data/paul\_graham/paul\_graham\_essay.txt’

data/paul\_graham/pa 100%\[>\]  73.28K   327KB/s    in 0.2s    

2024-02-12 17:59:59 (327 KB/s) - ‘data/paul\_graham/paul\_graham\_essay.txt’ saved \[75042/75042\]

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

index \= VectorStoreIndex.from\_documents(documents, transformations\=\[splitter\])

from llama\_index.core import VectorStoreIndex from llama\_index.core.node\_parser import SentenceSplitter splitter = SentenceSplitter(chunk\_size=256) index = VectorStoreIndex.from\_documents(documents, transformations=\[splitter\])

Create a Hybrid Fusion Retriever[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/reciprocal_rerank_fusion/#create-a-hybrid-fusion-retriever)
--------------------------------------------------------------------------------------------------------------------------------------------------------

In this step, we fuse our index with a BM25 based retriever. This will enable us to capture both semantic relations and keywords in our input queries.

Since both of these retrievers calculate a score, we can use the reciprocal rerank algorithm to re-sort our nodes without using an additional models or excessive computation.

This setup will also query 4 times, once with your original query, and generate 3 more queries.

By default, it uses the following prompt to generate extra queries:

QUERY\_GEN\_PROMPT \= (
    "You are a helpful assistant that generates multiple search queries based on a "
    "single input query. Generate {num\_queries} search queries, one on each line, "
    "related to the following input query:\\n"
    "Query: {query}\\n"
    "Queries:\\n"
)

First, we create our retrievers. Each will retrieve the top-2 most similar nodes:

In \[ \]:

Copied!

from llama\_index.retrievers.bm25 import BM25Retriever

vector\_retriever \= index.as\_retriever(similarity\_top\_k\=2)

bm25\_retriever \= BM25Retriever.from\_defaults(
    docstore\=index.docstore, similarity\_top\_k\=2
)

from llama\_index.retrievers.bm25 import BM25Retriever vector\_retriever = index.as\_retriever(similarity\_top\_k=2) bm25\_retriever = BM25Retriever.from\_defaults( docstore=index.docstore, similarity\_top\_k=2 )

Next, we can create our fusion retriever, which well return the top-2 most similar nodes from the 4 returned nodes from the retrievers:

In \[ \]:

Copied!

from llama\_index.core.retrievers import QueryFusionRetriever

retriever \= QueryFusionRetriever(
    \[vector\_retriever, bm25\_retriever\],
    similarity\_top\_k\=2,
    num\_queries\=4,  \# set this to 1 to disable query generation
    mode\="reciprocal\_rerank",
    use\_async\=True,
    verbose\=True,
    \# query\_gen\_prompt="...",  # we could override the query generation prompt here
)

from llama\_index.core.retrievers import QueryFusionRetriever retriever = QueryFusionRetriever( \[vector\_retriever, bm25\_retriever\], similarity\_top\_k=2, num\_queries=4, # set this to 1 to disable query generation mode="reciprocal\_rerank", use\_async=True, verbose=True, # query\_gen\_prompt="...", # we could override the query generation prompt here )

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

Generated queries:
1. What were the major events or milestones in the history of Interleafe and Viaweb?
2. Can you provide a timeline of the key developments and achievements of Interleafe and Viaweb?
3. What were the successes and failures of Interleafe and Viaweb as companies?

In \[ \]:

Copied!

for node in nodes\_with\_scores:
    print(f"Score: {node.score:.2f} - {node.text}...\\n\-----\\n")

for node in nodes\_with\_scores: print(f"Score: {node.score:.2f} - {node.text}...\\n-----\\n")

Score: 0.03 - The UI was horrible, but it proved you could build a whole store through the browser, without any client software or typing anything into the command line on the server.

Now we felt like we were really onto something. I had visions of a whole new generation of software working this way. You wouldn't need versions, or ports, or any of that crap. At Interleaf there had been a whole group called Release Engineering that seemed to be at least as big as the group that actually wrote the software. Now you could just update the software right on the server.

We started a new company we called Viaweb, after the fact that our software worked via the web, and we got $10,000 in seed funding from Idelle's husband Julian. In return for that and doing the initial legal work and giving us business advice, we gave him 10% of the company. Ten years later this deal became the model for Y Combinator's. We knew founders needed something like this, because we'd needed it ourselves....
-----

Score: 0.03 - Now we felt like we were really onto something. I had visions of a whole new generation of software working this way. You wouldn't need versions, or ports, or any of that crap. At Interleaf there had been a whole group called Release Engineering that seemed to be at least as big as the group that actually wrote the software. Now you could just update the software right on the server.

We started a new company we called Viaweb, after the fact that our software worked via the web, and we got $10,000 in seed funding from Idelle's husband Julian. In return for that and doing the initial legal work and giving us business advice, we gave him 10% of the company. Ten years later this deal became the model for Y Combinator's. We knew founders needed something like this, because we'd needed it ourselves.

At this stage I had a negative net worth, because the thousand dollars or so I had in the bank was more than counterbalanced by what I owed the government in taxes. (Had I diligently set aside the proper proportion of the money I'd made consulting for Interleaf?...
-----

As we can see, both retruned nodes correctly mention Viaweb and Interleaf!

Use in a Query Engine![¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/reciprocal_rerank_fusion/#use-in-a-query-engine)
-----------------------------------------------------------------------------------------------------------------------------------

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

Generated queries:
1. What were the major events or milestones in the history of Interleafe and Viaweb?
2. Can you provide a timeline of the key developments and achievements of Interleafe and Viaweb?
3. What were the outcomes or impacts of Interleafe and Viaweb on the respective industries they operated in?

In \[ \]:

Copied!

from llama\_index.core.response.notebook\_utils import display\_response

display\_response(response)

from llama\_index.core.response.notebook\_utils import display\_response display\_response(response)

**`Final Response:`** At Interleaf, there was a group called Release Engineering that was as big as the group that actually wrote the software. This suggests that there was a significant focus on managing versions and ports of the software. However, at Viaweb, the founders realized that they could update the software directly on the server, eliminating the need for versions and ports. They started Viaweb, a company that built software that worked via the web. They received $10,000 in seed funding and gave 10% of the company to Julian, who provided the funding and business advice. This deal later became the model for Y Combinator's.

Back to top

[Previous Pathway Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/pathway_retriever/)[Next Recursive Retriever + Node References + Braintrust](https://docs.llamaindex.ai/en/stable/examples/retrievers/recurisve_retriever_nodes_braintrust/)
