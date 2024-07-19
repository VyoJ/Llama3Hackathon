Title: Building an Advanced Fusion Retriever from Scratch

URL Source: https://docs.llamaindex.ai/en/stable/examples/low_level/fusion_retriever/

Markdown Content:
Building an Advanced Fusion Retriever from Scratch - LlamaIndex


In this tutorial, we show you how to build an advanced retriever from scratch.

Specifically, we show you how to build our `QueryFusionRetriever` from scratch.

This is heavily inspired from the RAG-fusion repo here: [https://github.com/Raudaschl/rag-fusion](https://github.com/Raudaschl/rag-fusion).

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/fusion_retriever/#setup)
-----------------------------------------------------------------------------------------

We load documents and build a simple vector index.

In \[ \]:

Copied!

%pip install llama\-index\-readers\-file pymupdf
%pip install llama\-index\-llms\-openai
%pip install llama\-index\-retrievers\-bm25

%pip install llama-index-readers-file pymupdf %pip install llama-index-llms-openai %pip install llama-index-retrievers-bm25

In \[ \]:

Copied!

import nest\_asyncio

nest\_asyncio.apply()

import nest\_asyncio nest\_asyncio.apply()

#### Load Documents[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/fusion_retriever/#load-documents)

In \[ \]:

Copied!

!mkdir data
!wget \--user\-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" \-O "data/llama2.pdf"

!mkdir data !wget --user-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" -O "data/llama2.pdf"

\--2024-04-03 09:32:31--  https://arxiv.org/pdf/2307.09288.pdf
Resolving arxiv.org (arxiv.org)... 151.101.3.42, 151.101.131.42, 151.101.67.42, ...
Connecting to arxiv.org (arxiv.org)|151.101.3.42|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 13661300 (13M) \[application/pdf\]
Saving to: ‘data/llama2.pdf’

data/llama2.pdf     100%\[>\]  13.03M  7.44MB/s    in 1.8s    

2024-04-03 09:32:33 (7.44 MB/s) - ‘data/llama2.pdf’ saved \[13661300/13661300\]

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

from pathlib import Path
from llama\_index.readers.file import PyMuPDFReader

loader \= PyMuPDFReader()
documents \= loader.load(file\_path\="./data/llama2.pdf")

from pathlib import Path from llama\_index.readers.file import PyMuPDFReader loader = PyMuPDFReader() documents = loader.load(file\_path="./data/llama2.pdf")

#### Setup Models[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/fusion_retriever/#setup-models)

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..."

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI
from llama\_index.embeddings.openai import OpenAIEmbedding

llm \= OpenAI(model\="gpt-3.5-turbo", temperature\=0.1)
embed\_model \= OpenAIEmbedding(
    model\="text-embedding-3-small", embed\_batch\_size\=256
)

from llama\_index.llms.openai import OpenAI from llama\_index.embeddings.openai import OpenAIEmbedding llm = OpenAI(model="gpt-3.5-turbo", temperature=0.1) embed\_model = OpenAIEmbedding( model="text-embedding-3-small", embed\_batch\_size=256 )

#### Load into Vector Store[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/fusion_retriever/#load-into-vector-store)

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex
from llama\_index.core.node\_parser import SentenceSplitter

splitter \= SentenceSplitter(chunk\_size\=1024)
index \= VectorStoreIndex.from\_documents(
    documents, transformations\=\[splitter\], embed\_model\=embed\_model
)

from llama\_index.core import VectorStoreIndex from llama\_index.core.node\_parser import SentenceSplitter splitter = SentenceSplitter(chunk\_size=1024) index = VectorStoreIndex.from\_documents( documents, transformations=\[splitter\], embed\_model=embed\_model )

Define Advanced Retriever[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/fusion_retriever/#define-advanced-retriever)
---------------------------------------------------------------------------------------------------------------------------------

We define an advanced retriever that performs the following steps:

1.  Query generation/rewriting: generate multiple queries given the original user query
2.  Perform retrieval for each query over an ensemble of retrievers.
3.  Reranking/fusion: fuse results from all queries, and apply a reranking step to "fuse" the top relevant results!

Then in the next section we'll plug this into our response synthesis module.

### Step 1: Query Generation/Rewriting[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/fusion_retriever/#step-1-query-generationrewriting)

The first step is to generate queries from the original query to better match the query intent, and increase precision/recall of the retrieved results. For instance, we might be able to rewrite the query into smaller queries.

We can do this by prompting ChatGPT.

In \[ \]:

Copied!

from llama\_index.core import PromptTemplate

from llama\_index.core import PromptTemplate

In \[ \]:

Copied!

query\_str \= "How do the models developed in this work compare to open-source chat models based on the benchmarks tested?"

query\_str = "How do the models developed in this work compare to open-source chat models based on the benchmarks tested?"

In \[ \]:

Copied!

query\_gen\_prompt\_str \= (
    "You are a helpful assistant that generates multiple search queries based on a "
    "single input query. Generate {num\_queries} search queries, one on each line, "
    "related to the following input query:\\n"
    "Query: {query}\\n"
    "Queries:\\n"
)
query\_gen\_prompt \= PromptTemplate(query\_gen\_prompt\_str)

query\_gen\_prompt\_str = ( "You are a helpful assistant that generates multiple search queries based on a " "single input query. Generate {num\_queries} search queries, one on each line, " "related to the following input query:\\n" "Query: {query}\\n" "Queries:\\n" ) query\_gen\_prompt = PromptTemplate(query\_gen\_prompt\_str)

In \[ \]:

Copied!

def generate\_queries(llm, query\_str: str, num\_queries: int \= 4):
    fmt\_prompt \= query\_gen\_prompt.format(
        num\_queries\=num\_queries \- 1, query\=query\_str
    )
    response \= llm.complete(fmt\_prompt)
    queries \= response.text.split("\\n")
    return queries

def generate\_queries(llm, query\_str: str, num\_queries: int = 4): fmt\_prompt = query\_gen\_prompt.format( num\_queries=num\_queries - 1, query=query\_str ) response = llm.complete(fmt\_prompt) queries = response.text.split("\\n") return queries

In \[ \]:

Copied!

queries \= generate\_queries(llm, query\_str, num\_queries\=4)

queries = generate\_queries(llm, query\_str, num\_queries=4)

In \[ \]:

Copied!

print(queries)

print(queries)

\['1. Comparison of models developed in this work to open-source chat models in benchmark testing', '2. Performance evaluation of models developed in this work versus open-source chat models on tested benchmarks', '3. Analysis of differences between models developed in this work and open-source chat models in benchmark assessments'\]

### Step 2: Perform Vector Search for Each Query[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/fusion_retriever/#step-2-perform-vector-search-for-each-query)

Now we run retrieval for each query. This means that we fetch the top-k most relevant results from each vector store.

**NOTE**: We can also have multiple retrievers. Then the total number of queries we run is N_M, where N is number of retrievers and M is number of generated queries. Hence there will also be N_M retrieved lists.

Here we'll use the retriever provided from our vector store. If you want to see how to build this from scratch please see [our tutorial on this](https://docs.llamaindex.ai/en/latest/examples/low_level/retrieval.html#put-this-into-a-retriever).

In \[ \]:

Copied!

from tqdm.asyncio import tqdm

async def run\_queries(queries, retrievers):
    """Run queries against retrievers."""
    tasks \= \[\]
    for query in queries:
        for i, retriever in enumerate(retrievers):
            tasks.append(retriever.aretrieve(query))

    task\_results \= await tqdm.gather(\*tasks)

    results\_dict \= {}
    for i, (query, query\_result) in enumerate(zip(queries, task\_results)):
        results\_dict\[(query, i)\] \= query\_result

    return results\_dict

from tqdm.asyncio import tqdm async def run\_queries(queries, retrievers): """Run queries against retrievers.""" tasks = \[\] for query in queries: for i, retriever in enumerate(retrievers): tasks.append(retriever.aretrieve(query)) task\_results = await tqdm.gather(\*tasks) results\_dict = {} for i, (query, query\_result) in enumerate(zip(queries, task\_results)): results\_dict\[(query, i)\] = query\_result return results\_dict

In \[ \]:

Copied!

\# get retrievers
from llama\_index.retrievers.bm25 import BM25Retriever

\## vector retriever
vector\_retriever \= index.as\_retriever(similarity\_top\_k\=2)

\## bm25 retriever
bm25\_retriever \= BM25Retriever.from\_defaults(
    docstore\=index.docstore, similarity\_top\_k\=2
)

\# get retrievers from llama\_index.retrievers.bm25 import BM25Retriever ## vector retriever vector\_retriever = index.as\_retriever(similarity\_top\_k=2) ## bm25 retriever bm25\_retriever = BM25Retriever.from\_defaults( docstore=index.docstore, similarity\_top\_k=2 )

In \[ \]:

Copied!

results\_dict \= await run\_queries(queries, \[vector\_retriever, bm25\_retriever\])

results\_dict = await run\_queries(queries, \[vector\_retriever, bm25\_retriever\])

  0%|          | 0/6 \[00:00<?, ?it/s\]

100%|██████████| 6/6 \[00:00<00:00, 11.14it/s\]

### Step 3: Perform Fusion[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/fusion_retriever/#step-3-perform-fusion)

The next step here is to perform fusion: combining the results from several retrievers into one and re-ranking.

Note that a given node might be retrieved multiple times from different retrievers, so there needs to be a way to de-dup and rerank the node given the multiple retrievals.

We'll show you how to perform "reciprocal rank fusion": for each node, add up its reciprocal rank in every list where it's retrieved.

Then reorder nodes by highest score to least.

Full paper here: [https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf](https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf)

In \[ \]:

Copied!

from typing import List
from llama\_index.core.schema import NodeWithScore

def fuse\_results(results\_dict, similarity\_top\_k: int \= 2):
    """Fuse results."""
    k \= 60.0  \# \`k\` is a parameter used to control the impact of outlier rankings.
    fused\_scores \= {}
    text\_to\_node \= {}

    \# compute reciprocal rank scores
    for nodes\_with\_scores in results\_dict.values():
        for rank, node\_with\_score in enumerate(
            sorted(
                nodes\_with\_scores, key\=lambda x: x.score or 0.0, reverse\=True
            )
        ):
            text \= node\_with\_score.node.get\_content()
            text\_to\_node\[text\] \= node\_with\_score
            if text not in fused\_scores:
                fused\_scores\[text\] \= 0.0
            fused\_scores\[text\] += 1.0 / (rank + k)

    \# sort results
    reranked\_results \= dict(
        sorted(fused\_scores.items(), key\=lambda x: x\[1\], reverse\=True)
    )

    \# adjust node scores
    reranked\_nodes: List\[NodeWithScore\] \= \[\]
    for text, score in reranked\_results.items():
        reranked\_nodes.append(text\_to\_node\[text\])
        reranked\_nodes\[\-1\].score \= score

    return reranked\_nodes\[:similarity\_top\_k\]

from typing import List from llama\_index.core.schema import NodeWithScore def fuse\_results(results\_dict, similarity\_top\_k: int = 2): """Fuse results.""" k = 60.0 # \`k\` is a parameter used to control the impact of outlier rankings. fused\_scores = {} text\_to\_node = {} # compute reciprocal rank scores for nodes\_with\_scores in results\_dict.values(): for rank, node\_with\_score in enumerate( sorted( nodes\_with\_scores, key=lambda x: x.score or 0.0, reverse=True ) ): text = node\_with\_score.node.get\_content() text\_to\_node\[text\] = node\_with\_score if text not in fused\_scores: fused\_scores\[text\] = 0.0 fused\_scores\[text\] += 1.0 / (rank + k) # sort results reranked\_results = dict( sorted(fused\_scores.items(), key=lambda x: x\[1\], reverse=True) ) # adjust node scores reranked\_nodes: List\[NodeWithScore\] = \[\] for text, score in reranked\_results.items(): reranked\_nodes.append(text\_to\_node\[text\]) reranked\_nodes\[-1\].score = score return reranked\_nodes\[:similarity\_top\_k\]

In \[ \]:

Copied!

final\_results \= fuse\_results(results\_dict)

final\_results = fuse\_results(results\_dict)

In \[ \]:

Copied!

for n in final\_results:
    print(n.score, "\\n", n.text, "\\n\*\*\*\*\*\*\*\*\\n")

for n in final\_results: print(n.score, "\\n", n.text, "\\n\*\*\*\*\*\*\*\*\\n")

0.03333333333333333 
 Figure 12: Human evaluation results for Llama 2-Chat models compared to open- and closed-source models
across ~4,000 helpfulness prompts with three raters per prompt.
The largest Llama 2-Chat model is competitive with ChatGPT. Llama 2-Chat 70B model has a win rate of
36% and a tie rate of 31.5% relative to ChatGPT. Llama 2-Chat 70B model outperforms PaLM-bison chat
model by a large percentage on our prompt set. More results and analysis is available in Section A.3.7.
Inter-Rater Reliability (IRR).
In our human evaluations, three different annotators provided independent
assessments for each model generation comparison. High IRR scores (closer to 1.0) are typically seen as
better from a data quality perspective, however, context is important. Highly subjective tasks like evaluating
the overall helpfulness of LLM generations will usually have lower IRR scores than more objective labelling
tasks. There are relatively few public benchmarks for these contexts, so we feel sharing our analysis here will
benefit the research community.
We used Gwet’s AC1/2 statistic (Gwet, 2008, 2014) to measure inter-rater reliability (IRR), as we found it to
be the most stable metric across different measurement scenarios. On the 7-point Likert scale helpfulness
task that is used in our analysis, Gwet’s AC2 score varies between 0.37 and 0.55 depending on the specific
model comparison. We see scores on the lower end of that range for ratings from model comparisons with
similar win rates to each other (like the Llama 2-Chat-70B-chat vs. ChatGPT comparison). We see scores on
the higher end of that range for ratings from model comparisons with a more clear winner (like the Llama
2-Chat-34b-chat vs. Falcon-40b-instruct).
Limitations of human evaluations.
While our results indicate that Llama 2-Chat is on par with ChatGPT
on human evaluations, it is important to note that human evaluations have several limitations.
• By academic and research standards, we have a large prompt set of 4k prompts. However, it does not cover
real-world usage of these models, which will likely cover a significantly larger number of use cases.
• Diversity of the prompts could be another factor in our results. For example, our prompt set does not
include any coding- or reasoning-related prompts.
• We only evaluate the final generation of a multi-turn conversation. A more interesting evaluation could be
to ask the models to complete a task and rate the overall experience with the model over multiple turns.
• Human evaluation for generative models is inherently subjective and noisy. As a result, evaluation on a
different set of prompts or with different instructions could result in different results.
19 
\*\*\*\*\*\*\*\*

0.03306010928961749 
 Llama 2: Open Foundation and Fine-Tuned Chat Models
Hugo Touvron∗
Louis Martin†
Kevin Stone†
Peter Albert Amjad Almahairi Yasmine Babaei Nikolay Bashlykov Soumya Batra
Prajjwal Bhargava Shruti Bhosale Dan Bikel Lukas Blecher Cristian Canton Ferrer Moya Chen
Guillem Cucurull David Esiobu Jude Fernandes Jeremy Fu Wenyin Fu Brian Fuller
Cynthia Gao Vedanuj Goswami Naman Goyal Anthony Hartshorn Saghar Hosseini Rui Hou
Hakan Inan Marcin Kardas Viktor Kerkez Madian Khabsa Isabel Kloumann Artem Korenev
Punit Singh Koura Marie-Anne Lachaux Thibaut Lavril Jenya Lee Diana Liskovich
Yinghai Lu Yuning Mao Xavier Martinet Todor Mihaylov Pushkar Mishra
Igor Molybog Yixin Nie Andrew Poulton Jeremy Reizenstein Rashi Rungta Kalyan Saladi
Alan Schelten Ruan Silva Eric Michael Smith Ranjan Subramanian Xiaoqing Ellen Tan Binh Tang
Ross Taylor Adina Williams Jian Xiang Kuan Puxin Xu Zheng Yan Iliyan Zarov Yuchen Zhang
Angela Fan Melanie Kambadur Sharan Narang Aurelien Rodriguez Robert Stojnic
Sergey Edunov
Thomas Scialom∗
GenAI, Meta
Abstract
In this work, we develop and release Llama 2, a collection of pretrained and fine-tuned
large language models (LLMs) ranging in scale from 7 billion to 70 billion parameters.
Our fine-tuned LLMs, called Llama 2-Chat, are optimized for dialogue use cases. Our
models outperform open-source chat models on most benchmarks we tested, and based on
our human evaluations for helpfulness and safety, may be a suitable substitute for closed-
source models. We provide a detailed description of our approach to fine-tuning and safety
improvements of Llama 2-Chat in order to enable the community to build on our work and
contribute to the responsible development of LLMs.
∗Equal contribution, corresponding authors: {tscialom, htouvron}@meta.com
†Second author
Contributions for all the authors can be found in Section A.1.
arXiv:2307.09288v2  \[cs.CL\]  19 Jul 2023 
\*\*\*\*\*\*\*\*

**Analysis**: The above code has a few straightforward components.

1.  Go through each node in each retrieved list, and add it's reciprocal rank to the node's ID. The node's ID is the hash of it's text for dedup purposes.
2.  Sort results by highest-score to lowest.
3.  Adjust node scores.

Plug into RetrieverQueryEngine[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/fusion_retriever/#plug-into-retrieverqueryengine)
-------------------------------------------------------------------------------------------------------------------------------------------

Now we're ready to define this as a custom retriever, and plug it into our `RetrieverQueryEngine` (which does retrieval and synthesis).

In \[ \]:

Copied!

from typing import List

from llama\_index.core import QueryBundle
from llama\_index.core.retrievers import BaseRetriever
from llama\_index.core.schema import NodeWithScore
import asyncio

class FusionRetriever(BaseRetriever):
    """Ensemble retriever with fusion."""

    def \_\_init\_\_(
        self,
        llm,
        retrievers: List\[BaseRetriever\],
        similarity\_top\_k: int \= 2,
    ) \-> None:
        """Init params."""
        self.\_retrievers \= retrievers
        self.\_similarity\_top\_k \= similarity\_top\_k
        self.\_llm \= llm
        super().\_\_init\_\_()

    def \_retrieve(self, query\_bundle: QueryBundle) \-> List\[NodeWithScore\]:
        """Retrieve."""
        queries \= generate\_queries(
            self.\_llm, query\_bundle.query\_str, num\_queries\=4
        )
        results \= asyncio.run(run\_queries(queries, self.\_retrievers))
        final\_results \= fuse\_results(
            results, similarity\_top\_k\=self.\_similarity\_top\_k
        )

        return final\_results

from typing import List from llama\_index.core import QueryBundle from llama\_index.core.retrievers import BaseRetriever from llama\_index.core.schema import NodeWithScore import asyncio class FusionRetriever(BaseRetriever): """Ensemble retriever with fusion.""" def \_\_init\_\_( self, llm, retrievers: List\[BaseRetriever\], similarity\_top\_k: int = 2, ) -> None: """Init params.""" self.\_retrievers = retrievers self.\_similarity\_top\_k = similarity\_top\_k self.\_llm = llm super().\_\_init\_\_() def \_retrieve(self, query\_bundle: QueryBundle) -> List\[NodeWithScore\]: """Retrieve.""" queries = generate\_queries( self.\_llm, query\_bundle.query\_str, num\_queries=4 ) results = asyncio.run(run\_queries(queries, self.\_retrievers)) final\_results = fuse\_results( results, similarity\_top\_k=self.\_similarity\_top\_k ) return final\_results

In \[ \]:

Copied!

from llama\_index.core.query\_engine import RetrieverQueryEngine

fusion\_retriever \= FusionRetriever(
    llm, \[vector\_retriever, bm25\_retriever\], similarity\_top\_k\=2
)

query\_engine \= RetrieverQueryEngine(fusion\_retriever)

from llama\_index.core.query\_engine import RetrieverQueryEngine fusion\_retriever = FusionRetriever( llm, \[vector\_retriever, bm25\_retriever\], similarity\_top\_k=2 ) query\_engine = RetrieverQueryEngine(fusion\_retriever)

In \[ \]:

Copied!

response \= query\_engine.query(query\_str)

response = query\_engine.query(query\_str)

In \[ \]:

Copied!

print(str(response))

print(str(response))

The models developed in this work, specifically the Llama 2-Chat models, outperform open-source chat models on most benchmarks that were tested.

Back to top

[Previous Building Evaluation from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/evaluation/)[Next Building Data Ingestion from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/ingestion/)

Hi, how can I help you?

🦙
