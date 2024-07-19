Title: Colbert Rerank - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/ColbertRerank/

Markdown Content:
Colbert Rerank - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

[Colbert](https://github.com/stanford-futuredata/ColBERT): ColBERT is a fast and accurate retrieval model, enabling scalable BERT-based search over large text collections in tens of milliseconds.

This example shows how we use Colbert-V2 model as a reranker.

In \[ \]:

Copied!

!pip install llama\-index
!pip install llama\-index\-core
!pip install \--quiet transformers torch
!pip install llama\-index\-embeddings\-openai
!pip install llama\-index\-llms\-openai
!pip install llama\-index\-postprocessor\-colbert\-rerank

!pip install llama-index !pip install llama-index-core !pip install --quiet transformers torch !pip install llama-index-embeddings-openai !pip install llama-index-llms-openai !pip install llama-index-postprocessor-colbert-rerank

In \[ \]:

Copied!

from llama\_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
)

from llama\_index.core import ( VectorStoreIndex, SimpleDirectoryReader, )

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-"

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-"

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

\# build index
index \= VectorStoreIndex.from\_documents(documents\=documents)

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data() # build index index = VectorStoreIndex.from\_documents(documents=documents)

#### Retrieve top 10 most relevant nodes, then filter with Colbert Rerank[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/ColbertRerank/#retrieve-top-10-most-relevant-nodes-then-filter-with-colbert-rerank)

In \[ \]:

Copied!

from llama\_index.postprocessor.colbert\_rerank import ColbertRerank

colbert\_reranker \= ColbertRerank(
    top\_n\=5,
    model\="colbert-ir/colbertv2.0",
    tokenizer\="colbert-ir/colbertv2.0",
    keep\_retrieval\_score\=True,
)

query\_engine \= index.as\_query\_engine(
    similarity\_top\_k\=10,
    node\_postprocessors\=\[colbert\_reranker\],
)
response \= query\_engine.query(
    "What did Sam Altman do in this essay?",
)

from llama\_index.postprocessor.colbert\_rerank import ColbertRerank colbert\_reranker = ColbertRerank( top\_n=5, model="colbert-ir/colbertv2.0", tokenizer="colbert-ir/colbertv2.0", keep\_retrieval\_score=True, ) query\_engine = index.as\_query\_engine( similarity\_top\_k=10, node\_postprocessors=\[colbert\_reranker\], ) response = query\_engine.query( "What did Sam Altman do in this essay?", )

In \[ \]:

Copied!

for node in response.source\_nodes:
    print(node.id\_)
    print(node.node.get\_content()\[:120\])
    print("reranking score: ", node.score)
    print("retrieval score: ", node.node.metadata\["retrieval\_score"\])
    print("\*\*\*\*\*\*\*\*\*\*")

for node in response.source\_nodes: print(node.id\_) print(node.node.get\_content()\[:120\]) print("reranking score: ", node.score) print("retrieval score: ", node.node.metadata\["retrieval\_score"\]) print("\*\*\*\*\*\*\*\*\*\*")

50157136-f221-4468-83e1-44e289f44cd5
When I was dealing with some urgent problem during YC, there was about a 60% chance it had to do with HN, and a 40% chan
reranking score:  0.6470144987106323
retrieval score:  0.8309200279065135
\*\*\*\*\*\*\*\*\*\*
87f0d691-b631-4b21-8123-8f71d383046b
Now that I could write essays again, I wrote a bunch about topics I'd had stacked up. I kept writing essays through 2020
reranking score:  0.6377773284912109
retrieval score:  0.8053000783543145
\*\*\*\*\*\*\*\*\*\*
10234ad9-46b1-4be5-8034-92392ac242ed
It's not that unprestigious types of work are good per se. But when you find yourself drawn to some kind of work despite
reranking score:  0.6301894187927246
retrieval score:  0.7975032272825491
\*\*\*\*\*\*\*\*\*\*
bc269bc4-49c7-4804-8575-cd6db47d70b8
It was as weird as it sounds. I resumed all my old patterns, except now there were doors where there hadn't been. Now wh
reranking score:  0.6282549500465393
retrieval score:  0.8026253284729862
\*\*\*\*\*\*\*\*\*\*
ebd7e351-64fc-4627-8ddd-2681d1ac33f8
As Jessica and I were walking home from dinner on March 11, at the corner of Garden and Walker streets, these three thre
reranking score:  0.6245909929275513
retrieval score:  0.7965812262372882
\*\*\*\*\*\*\*\*\*\*

In \[ \]:

Copied!

print(response)

print(response)

Sam Altman became the second president of Y Combinator after Paul Graham decided to step back from running the organization.

In \[ \]:

Copied!

response \= query\_engine.query(
    "Which schools did Paul attend?",
)

response = query\_engine.query( "Which schools did Paul attend?", )

In \[ \]:

Copied!

for node in response.source\_nodes:
    print(node.id\_)
    print(node.node.get\_content()\[:120\])
    print("reranking score: ", node.score)
    print("retrieval score: ", node.node.metadata\["retrieval\_score"\])
    print("\*\*\*\*\*\*\*\*\*\*")

for node in response.source\_nodes: print(node.id\_) print(node.node.get\_content()\[:120\]) print("reranking score: ", node.score) print("retrieval score: ", node.node.metadata\["retrieval\_score"\]) print("\*\*\*\*\*\*\*\*\*\*")

6942863e-dfc5-4a99-b642-967b99b71343
I didn't want to drop out of grad school, but how else was I going to get out? I remember when my friend Robert Morris g
reranking score:  0.6333063840866089
retrieval score:  0.7964996889742813
\*\*\*\*\*\*\*\*\*\*
477c5de0-8e05-494e-95cc-e221881fb5c1
What I Worked On

February 2021

Before college the two main things I worked on, outside of school, were writing and pro
reranking score:  0.5930159091949463
retrieval score:  0.7771872700578062
\*\*\*\*\*\*\*\*\*\*
0448df5c-7950-483d-bc63-15e9110da3bc
\[15\] We got 225 applications for the Summer Founders Program, and we were surprised to find that a lot of them were from
reranking score:  0.5160146951675415
retrieval score:  0.7782554326959897
\*\*\*\*\*\*\*\*\*\*
83af8efd-e992-4fd3-ada4-3c4c6f9971a1
Much to my surprise, the time I spent working on this stuff was not wasted after all. After we started Y Combinator, I w
reranking score:  0.5005874633789062
retrieval score:  0.7800375923908894
\*\*\*\*\*\*\*\*\*\*
bc269bc4-49c7-4804-8575-cd6db47d70b8
It was as weird as it sounds. I resumed all my old patterns, except now there were doors where there hadn't been. Now wh
reranking score:  0.4977223873138428
retrieval score:  0.782688582042514
\*\*\*\*\*\*\*\*\*\*

In \[ \]:

Copied!

print(response)

print(response)

Paul attended Cornell University for his graduate studies and later applied to RISD (Rhode Island School of Design) in the US.

Back to top

[Previous Cohere Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/CohereRerank/)[Next File Based Node Parsers](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/FileNodeProcessors/)

Hi, how can I help you?

🦙
