Title: Ensemble Retrieval Guide - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/retrievers/ensemble_retrieval/

Markdown Content:
Ensemble Retrieval Guide - LlamaIndex


Oftentimes when building a RAG applications there are many retreival parameters/strategies to decide from (from chunk size to vector vs. keyword vs. hybrid search, for instance).

Thought: what if we could try a bunch of strategies at once, and have any AI/reranker/LLM prune the results?

This achieves two purposes:

*   Better (albeit more costly) retrieved results by pooling results from multiple strategies, assuming the reranker is good
*   A way to benchmark different retrieval strategies against each other (w.r.t reranker)

This guide showcases this over the Llama 2 paper. We do ensemble retrieval over different chunk sizes and also different indices.

**NOTE**: A closely related guide is our [Ensemble Query Engine Guide](https://gpt-index.readthedocs.io/en/stable/examples/query_engine/ensemble_qury_engine.html) - make sure to check it out!

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai
%pip install llama\-index\-postprocessor\-cohere\-rerank
%pip install llama\-index\-readers\-file pymupdf

%pip install llama-index-llms-openai %pip install llama-index-postprocessor-cohere-rerank %pip install llama-index-readers-file pymupdf

In \[ \]:

Copied!

%load\_ext autoreload
%autoreload 2

%load\_ext autoreload %autoreload 2

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/ensemble_retrieval/#setup)
--------------------------------------------------------------------------------------------

Here we define the necessary imports.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

\# NOTE: This is ONLY necessary in jupyter notebook.
\# Details: Jupyter runs an event-loop behind the scenes.
\#          This results in nested event-loops when we start an event-loop to make async queries.
\#          This is normally not allowed, we use nest\_asyncio to allow it for convenience.
import nest\_asyncio

nest\_asyncio.apply()

\# NOTE: This is ONLY necessary in jupyter notebook. # Details: Jupyter runs an event-loop behind the scenes. # This results in nested event-loops when we start an event-loop to make async queries. # This is normally not allowed, we use nest\_asyncio to allow it for convenience. import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().handlers \= \[\]
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

from llama\_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
)
from llama\_index.core import SummaryIndex
from llama\_index.core.response.notebook\_utils import display\_response
from llama\_index.llms.openai import OpenAI

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().handlers = \[\] logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout)) from llama\_index.core import ( VectorStoreIndex, SimpleDirectoryReader, StorageContext, ) from llama\_index.core import SummaryIndex from llama\_index.core.response.notebook\_utils import display\_response from llama\_index.llms.openai import OpenAI

Note: NumExpr detected 12 cores but "NUMEXPR\_MAX\_THREADS" not set, so enforcing safe limit of 8.
NumExpr defaulting to 8 threads.

Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/ensemble_retrieval/#load-data)
----------------------------------------------------------------------------------------------------

In this section we first load in the Llama 2 paper as a single document. We then chunk it multiple times, according to different chunk sizes. We build a separate vector index corresponding to each chunk size.

In \[ \]:

Copied!

!wget \--user\-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" \-O "data/llama2.pdf"

!wget --user-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" -O "data/llama2.pdf"

\--2023-09-28 12:56:38--  https://arxiv.org/pdf/2307.09288.pdf
Resolving arxiv.org (arxiv.org)... 128.84.21.199
Connecting to arxiv.org (arxiv.org)|128.84.21.199|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 13661300 (13M) \[application/pdf\]
Saving to: ‘data/llama2.pdf’

data/llama2.pdf     100%\[ metadata\_value:
                mrr \= 1 / (idx + 1)
                break
            else:
                continue

        \# normalize AP, set in dict
        value\_to\_mrr\_dict\[metadata\_value\] \= mrr

    df \= pd.DataFrame(value\_to\_mrr\_dict, index\=\["MRR"\])
    df.style.set\_caption("Mean Reciprocal Rank")
    return df

\# compute the average precision for each chunk size based on positioning in combined ranking from collections import defaultdict import pandas as pd def mrr\_all(metadata\_values, metadata\_key, source\_nodes): # source nodes is a ranked list # go through each value, find out positioning in source\_nodes value\_to\_mrr\_dict = {} for metadata\_value in metadata\_values: mrr = 0 for idx, source\_node in enumerate(source\_nodes): if source\_node.node.metadata\[metadata\_key\] == metadata\_value: mrr = 1 / (idx + 1) break else: continue # normalize AP, set in dict value\_to\_mrr\_dict\[metadata\_value\] = mrr df = pd.DataFrame(value\_to\_mrr\_dict, index=\["MRR"\]) df.style.set\_caption("Mean Reciprocal Rank") return df

In \[ \]:

Copied!

\# Compute the Mean Reciprocal Rank for each chunk size (higher is better)
\# we can see that chunk size of 256 has the highest ranked results.
print("Mean Reciprocal Rank for each Chunk Size")
mrr\_all(chunk\_sizes, "chunk\_size", response.source\_nodes)

\# Compute the Mean Reciprocal Rank for each chunk size (higher is better) # we can see that chunk size of 256 has the highest ranked results. print("Mean Reciprocal Rank for each Chunk Size") mrr\_all(chunk\_sizes, "chunk\_size", response.source\_nodes)

Mean Reciprocal Rank for each Chunk Size

Out\[ \]:

|  | 128 | 256 | 512 | 1024 |
| --- | --- | --- | --- | --- |
| MRR | 0.333333 | 1.0 | 0.5 | 0.25 |

Evaluation[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/ensemble_retrieval/#evaluation)
------------------------------------------------------------------------------------------------------

We more rigorously evaluate how well an ensemble retriever works compared to the "baseline" retriever.

We define/load an eval benchmark dataset and then run different evaluations over it.

**WARNING**: This can be _expensive_, especially with GPT-4. Use caution and tune the sample size to fit your budget.

In \[ \]:

Copied!

from llama\_index.core.evaluation import DatasetGenerator, QueryResponseDataset
from llama\_index.llms.openai import OpenAI
import nest\_asyncio

nest\_asyncio.apply()

from llama\_index.core.evaluation import DatasetGenerator, QueryResponseDataset from llama\_index.llms.openai import OpenAI import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

\# NOTE: run this if the dataset isn't already saved
eval\_llm \= OpenAI(model\="gpt-4")
\# generate questions from the largest chunks (1024)
dataset\_generator \= DatasetGenerator(
    nodes\_list\[\-1\],
    llm\=eval\_llm,
    show\_progress\=True,
    num\_questions\_per\_chunk\=2,
)

\# NOTE: run this if the dataset isn't already saved eval\_llm = OpenAI(model="gpt-4") # generate questions from the largest chunks (1024) dataset\_generator = DatasetGenerator( nodes\_list\[-1\], llm=eval\_llm, show\_progress=True, num\_questions\_per\_chunk=2, )

In \[ \]:

Copied!

eval\_dataset \= await dataset\_generator.agenerate\_dataset\_from\_nodes(num\=60)

eval\_dataset = await dataset\_generator.agenerate\_dataset\_from\_nodes(num=60)

In \[ \]:

Copied!

eval\_dataset.save\_json("data/llama2\_eval\_qr\_dataset.json")

eval\_dataset.save\_json("data/llama2\_eval\_qr\_dataset.json")

In \[ \]:

Copied!

\# optional
eval\_dataset \= QueryResponseDataset.from\_json(
    "data/llama2\_eval\_qr\_dataset.json"
)

\# optional eval\_dataset = QueryResponseDataset.from\_json( "data/llama2\_eval\_qr\_dataset.json" )

### Compare Results[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/ensemble_retrieval/#compare-results)

In \[ \]:

Copied!

import asyncio
import nest\_asyncio

nest\_asyncio.apply()

import asyncio import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

from llama\_index.core.evaluation import (
    CorrectnessEvaluator,
    SemanticSimilarityEvaluator,
    RelevancyEvaluator,
    FaithfulnessEvaluator,
    PairwiseComparisonEvaluator,
)

\# NOTE: can uncomment other evaluators
evaluator\_c \= CorrectnessEvaluator(llm\=eval\_llm)
evaluator\_s \= SemanticSimilarityEvaluator(llm\=eval\_llm)
evaluator\_r \= RelevancyEvaluator(llm\=eval\_llm)
evaluator\_f \= FaithfulnessEvaluator(llm\=eval\_llm)

pairwise\_evaluator \= PairwiseComparisonEvaluator(llm\=eval\_llm)

from llama\_index.core.evaluation import ( CorrectnessEvaluator, SemanticSimilarityEvaluator, RelevancyEvaluator, FaithfulnessEvaluator, PairwiseComparisonEvaluator, ) # NOTE: can uncomment other evaluators evaluator\_c = CorrectnessEvaluator(llm=eval\_llm) evaluator\_s = SemanticSimilarityEvaluator(llm=eval\_llm) evaluator\_r = RelevancyEvaluator(llm=eval\_llm) evaluator\_f = FaithfulnessEvaluator(llm=eval\_llm) pairwise\_evaluator = PairwiseComparisonEvaluator(llm=eval\_llm)

In \[ \]:

Copied!

from llama\_index.core.evaluation.eval\_utils import (
    get\_responses,
    get\_results\_df,
)
from llama\_index.core.evaluation import BatchEvalRunner

max\_samples \= 60

eval\_qs \= eval\_dataset.questions
qr\_pairs \= eval\_dataset.qr\_pairs
ref\_response\_strs \= \[r for (\_, r) in qr\_pairs\]

\# resetup base query engine and ensemble query engine
\# base query engine
base\_query\_engine \= vector\_indices\[\-1\].as\_query\_engine(similarity\_top\_k\=2)
\# ensemble query engine
reranker \= CohereRerank(top\_n\=4)
query\_engine \= RetrieverQueryEngine(retriever, node\_postprocessors\=\[reranker\])

from llama\_index.core.evaluation.eval\_utils import ( get\_responses, get\_results\_df, ) from llama\_index.core.evaluation import BatchEvalRunner max\_samples = 60 eval\_qs = eval\_dataset.questions qr\_pairs = eval\_dataset.qr\_pairs ref\_response\_strs = \[r for (\_, r) in qr\_pairs\] # resetup base query engine and ensemble query engine # base query engine base\_query\_engine = vector\_indices\[-1\].as\_query\_engine(similarity\_top\_k=2) # ensemble query engine reranker = CohereRerank(top\_n=4) query\_engine = RetrieverQueryEngine(retriever, node\_postprocessors=\[reranker\])

In \[ \]:

Copied!

base\_pred\_responses \= get\_responses(
    eval\_qs\[:max\_samples\], base\_query\_engine, show\_progress\=True
)

base\_pred\_responses = get\_responses( eval\_qs\[:max\_samples\], base\_query\_engine, show\_progress=True )

In \[ \]:

Copied!

pred\_responses \= get\_responses(
    eval\_qs\[:max\_samples\], query\_engine, show\_progress\=True
)

pred\_responses = get\_responses( eval\_qs\[:max\_samples\], query\_engine, show\_progress=True )

In \[ \]:

Copied!

import numpy as np

pred\_response\_strs \= \[str(p) for p in pred\_responses\]
base\_pred\_response\_strs \= \[str(p) for p in base\_pred\_responses\]

import numpy as np pred\_response\_strs = \[str(p) for p in pred\_responses\] base\_pred\_response\_strs = \[str(p) for p in base\_pred\_responses\]

In \[ \]:

Copied!

evaluator\_dict \= {
    "correctness": evaluator\_c,
    "faithfulness": evaluator\_f,
    \# "relevancy": evaluator\_r,
    "semantic\_similarity": evaluator\_s,
}
batch\_runner \= BatchEvalRunner(evaluator\_dict, workers\=1, show\_progress\=True)

evaluator\_dict = { "correctness": evaluator\_c, "faithfulness": evaluator\_f, # "relevancy": evaluator\_r, "semantic\_similarity": evaluator\_s, } batch\_runner = BatchEvalRunner(evaluator\_dict, workers=1, show\_progress=True)

In \[ \]:

Copied!

eval\_results \= await batch\_runner.aevaluate\_responses(
    queries\=eval\_qs\[:max\_samples\],
    responses\=pred\_responses\[:max\_samples\],
    reference\=ref\_response\_strs\[:max\_samples\],
)

eval\_results = await batch\_runner.aevaluate\_responses( queries=eval\_qs\[:max\_samples\], responses=pred\_responses\[:max\_samples\], reference=ref\_response\_strs\[:max\_samples\], )

In \[ \]:

Copied!

base\_eval\_results \= await batch\_runner.aevaluate\_responses(
    queries\=eval\_qs\[:max\_samples\],
    responses\=base\_pred\_responses\[:max\_samples\],
    reference\=ref\_response\_strs\[:max\_samples\],
)

base\_eval\_results = await batch\_runner.aevaluate\_responses( queries=eval\_qs\[:max\_samples\], responses=base\_pred\_responses\[:max\_samples\], reference=ref\_response\_strs\[:max\_samples\], )

In \[ \]:

Copied!

results\_df \= get\_results\_df(
    \[eval\_results, base\_eval\_results\],
    \["Ensemble Retriever", "Base Retriever"\],
    \["correctness", "faithfulness", "semantic\_similarity"\],
)
display(results\_df)

results\_df = get\_results\_df( \[eval\_results, base\_eval\_results\], \["Ensemble Retriever", "Base Retriever"\], \["correctness", "faithfulness", "semantic\_similarity"\], ) display(results\_df)

|  | names | correctness | faithfulness | semantic\_similarity |
| --- | --- | --- | --- | --- |
| 0 | Ensemble Retriever | 4.375000 | 0.983333 | 0.964546 |
| 1 | Base Retriever | 4.066667 | 0.983333 | 0.956692 |

In \[ \]:

Copied!

batch\_runner \= BatchEvalRunner(
    {"pairwise": pairwise\_evaluator}, workers\=3, show\_progress\=True
)

pairwise\_eval\_results \= await batch\_runner.aevaluate\_response\_strs(
    queries\=eval\_qs\[:max\_samples\],
    response\_strs\=pred\_response\_strs\[:max\_samples\],
    reference\=base\_pred\_response\_strs\[:max\_samples\],
)

batch\_runner = BatchEvalRunner( {"pairwise": pairwise\_evaluator}, workers=3, show\_progress=True ) pairwise\_eval\_results = await batch\_runner.aevaluate\_response\_strs( queries=eval\_qs\[:max\_samples\], response\_strs=pred\_response\_strs\[:max\_samples\], reference=base\_pred\_response\_strs\[:max\_samples\], )

In \[ \]:

Copied!

results\_df \= get\_results\_df(
    \[eval\_results, base\_eval\_results\],
    \["Ensemble Retriever", "Base Retriever"\],
    \["pairwise"\],
)
display(results\_df)

results\_df = get\_results\_df( \[eval\_results, base\_eval\_results\], \["Ensemble Retriever", "Base Retriever"\], \["pairwise"\], ) display(results\_df)

Out\[ \]:

|  | names | pairwise |
| --- | --- | --- |
| 0 | Pairwise Comparison | 0.5 |

Back to top

[Previous Activeloop Deep Memory](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/)[Next Chunk + Document Hybrid Retrieval with Long-Context Embeddings (Together.ai)](https://docs.llamaindex.ai/en/stable/examples/retrievers/multi_doc_together_hybrid/)
