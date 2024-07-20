Title: Recursive Retriever + Node References + Braintrust

URL Source: https://docs.llamaindex.ai/en/stable/examples/retrievers/recurisve_retriever_nodes_braintrust/

Markdown Content:
Recursive Retriever + Node References + Braintrust - LlamaIndex


This guide shows how you can use recursive retrieval to traverse node relationships and fetch nodes based on "references".

Node references are a powerful concept. When you first perform retrieval, you may want to retrieve the reference as opposed to the raw text. You can have multiple references point to the same node.

In this guide we explore some different usages of node references:

*   **Chunk references**: Different chunk sizes referring to a bigger chunk
*   **Metadata references**: Summaries + Generated Questions referring to a bigger chunk

We evaluate how well our recursive retrieval + node reference methods work using [Braintrust](https://www.braintrustdata.com/). Braintrust is the enterprise-grade stack for building AI products. From evaluations, to prompt playground, to data management, we take uncertainty and tedium out of incorporating AI into your business.

You can see example evaluation dashboards here for the:

*   [base retriever](https://www.braintrustdata.com/app/braintrustdata.com/p/llamaindex-recurisve-retrievers/baseRetriever)
*   [recursive metadata retreiver](https://www.braintrustdata.com/app/braintrustdata.com/p/llamaindex-recurisve-retrievers/recursiveMetadataRetriever)
*   [recursive chunk retriever](https://www.braintrustdata.com/app/braintrustdata.com/p/llamaindex-recurisve-retrievers/recursiveChunkRetriever)

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai
%pip install llama\-index\-readers\-file

%pip install llama-index-llms-openai %pip install llama-index-readers-file

In \[ \]:

Copied!

%load\_ext autoreload
%autoreload 2
\# NOTE: Replace YOUR\_OPENAI\_API\_KEY with your OpenAI API Key and YOUR\_BRAINTRUST\_API\_KEY with your BrainTrust API key. Do not put it in quotes.
\# Signup for Braintrust at https://braintrustdata.com/ and get your API key at https://www.braintrustdata.com/app/braintrustdata.com/settings/api-keys
\# NOTE: Replace YOUR\_OPENAI\_KEY with your OpenAI API Key and YOUR\_BRAINTRUST\_API\_KEY with your BrainTrust API key. Do not put it in quotes.
%env OPENAI\_API\_KEY\=
%env BRAINTRUST\_API\_KEY\=
%env TOKENIZERS\_PARALLELISM\=true \# This is needed to avoid a warning message from Chroma

%load\_ext autoreload %autoreload 2 # NOTE: Replace YOUR\_OPENAI\_API\_KEY with your OpenAI API Key and YOUR\_BRAINTRUST\_API\_KEY with your BrainTrust API key. Do not put it in quotes. # Signup for Braintrust at https://braintrustdata.com/ and get your API key at https://www.braintrustdata.com/app/braintrustdata.com/settings/api-keys # NOTE: Replace YOUR\_OPENAI\_KEY with your OpenAI API Key and YOUR\_BRAINTRUST\_API\_KEY with your BrainTrust API key. Do not put it in quotes. %env OPENAI\_API\_KEY= %env BRAINTRUST\_API\_KEY= %env TOKENIZERS\_PARALLELISM=true # This is needed to avoid a warning message from Chroma

In \[ \]:

Copied!

%pip install \-U llama\_hub llama\_index braintrust autoevals pypdf pillow transformers torch torchvision

%pip install -U llama\_hub llama\_index braintrust autoevals pypdf pillow transformers torch torchvision

Load Data + Setup[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/recurisve_retriever_nodes_braintrust/#load-data-setup)
------------------------------------------------------------------------------------------------------------------------------------

In this section we download the Llama 2 paper and create an initial set of nodes (chunk size 1024).

In \[ \]:

Copied!

!mkdir data
!wget \--user\-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" \-O "data/llama2.pdf"

!mkdir data !wget --user-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" -O "data/llama2.pdf"

In \[ \]:

Copied!

from pathlib import Path
from llama\_index.readers.file import PDFReader
from llama\_index.core.response.notebook\_utils import display\_source\_node
from llama\_index.core.retrievers import RecursiveRetriever
from llama\_index.core.query\_engine import RetrieverQueryEngine
from llama\_index.core import VectorStoreIndex
from llama\_index.llms.openai import OpenAI
import json

from pathlib import Path from llama\_index.readers.file import PDFReader from llama\_index.core.response.notebook\_utils import display\_source\_node from llama\_index.core.retrievers import RecursiveRetriever from llama\_index.core.query\_engine import RetrieverQueryEngine from llama\_index.core import VectorStoreIndex from llama\_index.llms.openai import OpenAI import json

In \[ \]:

Copied!

loader \= PDFReader()
docs0 \= loader.load\_data(file\=Path("./data/llama2.pdf"))

loader = PDFReader() docs0 = loader.load\_data(file=Path("./data/llama2.pdf"))

In \[ \]:

Copied!

from llama\_index.core import Document

doc\_text \= "\\n\\n".join(\[d.get\_content() for d in docs0\])
docs \= \[Document(text\=doc\_text)\]

from llama\_index.core import Document doc\_text = "\\n\\n".join(\[d.get\_content() for d in docs0\]) docs = \[Document(text=doc\_text)\]

In \[ \]:

Copied!

from llama\_index.core.node\_parser import SentenceSplitter
from llama\_index.core.schema import IndexNode

from llama\_index.core.node\_parser import SentenceSplitter from llama\_index.core.schema import IndexNode

In \[ \]:

Copied!

node\_parser \= SentenceSplitter(chunk\_size\=1024)

node\_parser = SentenceSplitter(chunk\_size=1024)

In \[ \]:

Copied!

base\_nodes \= node\_parser.get\_nodes\_from\_documents(docs)
\# set node ids to be a constant
for idx, node in enumerate(base\_nodes):
    node.id\_ \= f"node-{idx}"

base\_nodes = node\_parser.get\_nodes\_from\_documents(docs) # set node ids to be a constant for idx, node in enumerate(base\_nodes): node.id\_ = f"node-{idx}"

In \[ \]:

Copied!

from llama\_index.core.embeddings import resolve\_embed\_model

embed\_model \= resolve\_embed\_model("local:BAAI/bge-small-en")
llm \= OpenAI(model\="gpt-3.5-turbo")

from llama\_index.core.embeddings import resolve\_embed\_model embed\_model = resolve\_embed\_model("local:BAAI/bge-small-en") llm = OpenAI(model="gpt-3.5-turbo")

Baseline Retriever[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/recurisve_retriever_nodes_braintrust/#baseline-retriever)
----------------------------------------------------------------------------------------------------------------------------------------

Define a baseline retriever that simply fetches the top-k raw text nodes by embedding similarity.

In \[ \]:

Copied!

base\_index \= VectorStoreIndex(base\_nodes, embed\_model\=embed\_model)
base\_retriever \= base\_index.as\_retriever(similarity\_top\_k\=2)

base\_index = VectorStoreIndex(base\_nodes, embed\_model=embed\_model) base\_retriever = base\_index.as\_retriever(similarity\_top\_k=2)

In \[ \]:

Copied!

retrievals \= base\_retriever.retrieve(
    "Can you tell me about the key concepts for safety finetuning"
)

retrievals = base\_retriever.retrieve( "Can you tell me about the key concepts for safety finetuning" )

In \[ \]:

Copied!

for n in retrievals:
    display\_source\_node(n, source\_length\=1500)

for n in retrievals: display\_source\_node(n, source\_length=1500)

In \[ \]:

Copied!

query\_engine\_base \= RetrieverQueryEngine.from\_args(base\_retriever, llm\=llm)

query\_engine\_base = RetrieverQueryEngine.from\_args(base\_retriever, llm=llm)

In \[ \]:

Copied!

response \= query\_engine\_base.query(
    "Can you tell me about the key concepts for safety finetuning"
)
print(str(response))

response = query\_engine\_base.query( "Can you tell me about the key concepts for safety finetuning" ) print(str(response))

Chunk References: Smaller Child Chunks Referring to Bigger Parent Chunk[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/recurisve_retriever_nodes_braintrust/#chunk-references-smaller-child-chunks-referring-to-bigger-parent-chunk)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this usage example, we show how to build a graph of smaller chunks pointing to bigger parent chunks.

During query-time, we retrieve smaller chunks, but we follow references to bigger chunks. This allows us to have more context for synthesis.

In \[ \]:

Copied!

sub\_chunk\_sizes \= \[128, 256, 512\]
sub\_node\_parsers \= \[SentenceSplitter(chunk\_size\=c) for c in sub\_chunk\_sizes\]

all\_nodes \= \[\]

for base\_node in base\_nodes:
    for n in sub\_node\_parsers:
        sub\_nodes \= n.get\_nodes\_from\_documents(\[base\_node\])
        sub\_inodes \= \[
            IndexNode.from\_text\_node(sn, base\_node.node\_id) for sn in sub\_nodes
        \]
        all\_nodes.extend(sub\_inodes)

    \# also add original node to node
    original\_node \= IndexNode.from\_text\_node(base\_node, base\_node.node\_id)
    all\_nodes.append(original\_node)

sub\_chunk\_sizes = \[128, 256, 512\] sub\_node\_parsers = \[SentenceSplitter(chunk\_size=c) for c in sub\_chunk\_sizes\] all\_nodes = \[\] for base\_node in base\_nodes: for n in sub\_node\_parsers: sub\_nodes = n.get\_nodes\_from\_documents(\[base\_node\]) sub\_inodes = \[ IndexNode.from\_text\_node(sn, base\_node.node\_id) for sn in sub\_nodes \] all\_nodes.extend(sub\_inodes) # also add original node to node original\_node = IndexNode.from\_text\_node(base\_node, base\_node.node\_id) all\_nodes.append(original\_node)

In \[ \]:

Copied!

all\_nodes\_dict \= {n.node\_id: n for n in all\_nodes}

all\_nodes\_dict = {n.node\_id: n for n in all\_nodes}

In \[ \]:

Copied!

vector\_index\_chunk \= VectorStoreIndex(all\_nodes, embed\_model\=embed\_model)

vector\_index\_chunk = VectorStoreIndex(all\_nodes, embed\_model=embed\_model)

In \[ \]:

Copied!

vector\_retriever\_chunk \= vector\_index\_chunk.as\_retriever(similarity\_top\_k\=2)

vector\_retriever\_chunk = vector\_index\_chunk.as\_retriever(similarity\_top\_k=2)

In \[ \]:

Copied!

retriever\_chunk \= RecursiveRetriever(
    "vector",
    retriever\_dict\={"vector": vector\_retriever\_chunk},
    node\_dict\=all\_nodes\_dict,
    verbose\=True,
)

retriever\_chunk = RecursiveRetriever( "vector", retriever\_dict={"vector": vector\_retriever\_chunk}, node\_dict=all\_nodes\_dict, verbose=True, )

In \[ \]:

Copied!

nodes \= retriever\_chunk.retrieve(
    "Can you tell me about the key concepts for safety finetuning"
)
for node in nodes:
    display\_source\_node(node, source\_length\=2000)

nodes = retriever\_chunk.retrieve( "Can you tell me about the key concepts for safety finetuning" ) for node in nodes: display\_source\_node(node, source\_length=2000)

In \[ \]:

Copied!

query\_engine\_chunk \= RetrieverQueryEngine.from\_args(retriever\_chunk, llm\=llm)

query\_engine\_chunk = RetrieverQueryEngine.from\_args(retriever\_chunk, llm=llm)

In \[ \]:

Copied!

response \= query\_engine\_chunk.query(
    "Can you tell me about the key concepts for safety finetuning"
)
print(str(response))

response = query\_engine\_chunk.query( "Can you tell me about the key concepts for safety finetuning" ) print(str(response))

Metadata References: Summaries + Generated Questions referring to a bigger chunk[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/recurisve_retriever_nodes_braintrust/#metadata-references-summaries-generated-questions-referring-to-a-bigger-chunk)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this usage example, we show how to define additional context that references the source node.

This additional context includes summaries as well as generated questions.

During query-time, we retrieve smaller chunks, but we follow references to bigger chunks. This allows us to have more context for synthesis.

In \[ \]:

Copied!

from llama\_index.core.node\_parser import SentenceSplitter
from llama\_index.core.schema import IndexNode
from llama\_index.core.extractors import (
    SummaryExtractor,
    QuestionsAnsweredExtractor,
)

from llama\_index.core.node\_parser import SentenceSplitter from llama\_index.core.schema import IndexNode from llama\_index.core.extractors import ( SummaryExtractor, QuestionsAnsweredExtractor, )

In \[ \]:

Copied!

extractors \= \[
    SummaryExtractor(summaries\=\["self"\], show\_progress\=True),
    QuestionsAnsweredExtractor(questions\=5, show\_progress\=True),
\]

extractors = \[ SummaryExtractor(summaries=\["self"\], show\_progress=True), QuestionsAnsweredExtractor(questions=5, show\_progress=True), \]

In \[ \]:

Copied!

\# run metadata extractor across base nodes, get back dictionaries
metadata\_dicts \= \[\]
for extractor in extractors:
    metadata\_dicts.extend(extractor.extract(base\_nodes))

\# run metadata extractor across base nodes, get back dictionaries metadata\_dicts = \[\] for extractor in extractors: metadata\_dicts.extend(extractor.extract(base\_nodes))

In \[ \]:

Copied!

\# cache metadata dicts
def save\_metadata\_dicts(path):
    with open(path, "w") as fp:
        for m in metadata\_dicts:
            fp.write(json.dumps(m) + "\\n")

def load\_metadata\_dicts(path):
    with open(path, "r") as fp:
        metadata\_dicts \= \[json.loads(l) for l in fp.readlines()\]
        return metadata\_dicts

\# cache metadata dicts def save\_metadata\_dicts(path): with open(path, "w") as fp: for m in metadata\_dicts: fp.write(json.dumps(m) + "\\n") def load\_metadata\_dicts(path): with open(path, "r") as fp: metadata\_dicts = \[json.loads(l) for l in fp.readlines()\] return metadata\_dicts

In \[ \]:

Copied!

save\_metadata\_dicts("data/llama2\_metadata\_dicts.jsonl")

save\_metadata\_dicts("data/llama2\_metadata\_dicts.jsonl")

In \[ \]:

Copied!

metadata\_dicts \= load\_metadata\_dicts("data/llama2\_metadata\_dicts.jsonl")

metadata\_dicts = load\_metadata\_dicts("data/llama2\_metadata\_dicts.jsonl")

In \[ \]:

Copied!

\# all nodes consists of source nodes, along with metadata
import copy

all\_nodes \= copy.deepcopy(base\_nodes)
for idx, d in enumerate(metadata\_dicts):
    inode\_q \= IndexNode(
        text\=d\["questions\_this\_excerpt\_can\_answer"\],
        index\_id\=base\_nodes\[idx\].node\_id,
    )
    inode\_s \= IndexNode(
        text\=d\["section\_summary"\], index\_id\=base\_nodes\[idx\].node\_id
    )
    all\_nodes.extend(\[inode\_q, inode\_s\])

\# all nodes consists of source nodes, along with metadata import copy all\_nodes = copy.deepcopy(base\_nodes) for idx, d in enumerate(metadata\_dicts): inode\_q = IndexNode( text=d\["questions\_this\_excerpt\_can\_answer"\], index\_id=base\_nodes\[idx\].node\_id, ) inode\_s = IndexNode( text=d\["section\_summary"\], index\_id=base\_nodes\[idx\].node\_id ) all\_nodes.extend(\[inode\_q, inode\_s\])

In \[ \]:

Copied!

all\_nodes\_dict \= {n.node\_id: n for n in all\_nodes}

all\_nodes\_dict = {n.node\_id: n for n in all\_nodes}

In \[ \]:

Copied!

\## Load index into vector index
from llama\_index.core import VectorStoreIndex
from llama\_index.llms.openai import OpenAI

llm \= OpenAI(model\="gpt-3.5-turbo")

vector\_index\_metadata \= VectorStoreIndex(all\_nodes)

\## Load index into vector index from llama\_index.core import VectorStoreIndex from llama\_index.llms.openai import OpenAI llm = OpenAI(model="gpt-3.5-turbo") vector\_index\_metadata = VectorStoreIndex(all\_nodes)

In \[ \]:

Copied!

vector\_retriever\_metadata \= vector\_index\_metadata.as\_retriever(
    similarity\_top\_k\=2
)

vector\_retriever\_metadata = vector\_index\_metadata.as\_retriever( similarity\_top\_k=2 )

In \[ \]:

Copied!

retriever\_metadata \= RecursiveRetriever(
    "vector",
    retriever\_dict\={"vector": vector\_retriever\_metadata},
    node\_dict\=all\_nodes\_dict,
    verbose\=True,
)

retriever\_metadata = RecursiveRetriever( "vector", retriever\_dict={"vector": vector\_retriever\_metadata}, node\_dict=all\_nodes\_dict, verbose=True, )

In \[ \]:

Copied!

nodes \= retriever\_metadata.retrieve(
    "Can you tell me about the key concepts for safety finetuning"
)
for node in nodes:
    display\_source\_node(node, source\_length\=2000)

nodes = retriever\_metadata.retrieve( "Can you tell me about the key concepts for safety finetuning" ) for node in nodes: display\_source\_node(node, source\_length=2000)

In \[ \]:

Copied!

query\_engine\_metadata \= RetrieverQueryEngine.from\_args(
    retriever\_metadata, llm\=llm
)

query\_engine\_metadata = RetrieverQueryEngine.from\_args( retriever\_metadata, llm=llm )

In \[ \]:

Copied!

response \= query\_engine\_metadata.query(
    "Can you tell me about the key concepts for safety finetuning"
)
print(str(response))

response = query\_engine\_metadata.query( "Can you tell me about the key concepts for safety finetuning" ) print(str(response))

Evaluation[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/recurisve_retriever_nodes_braintrust/#evaluation)
------------------------------------------------------------------------------------------------------------------------

We evaluate how well our recursive retrieval + node reference methods work using [Braintrust](https://www.braintrustdata.com/). Braintrust is the enterprise-grade stack for building AI products. From evaluations, to prompt playground, to data management, we take uncertainty and tedium out of incorporating AI into your business.

We evaluate both chunk references as well as metadata references. We use embedding similarity lookup to retrieve the reference nodes. We compare both methods against a baseline retriever where we fetch the raw nodes directly. In terms of metrics, we evaluate using both hit-rate and MRR.

You can see example evaluation dashboards here for the:

*   [base retriever](https://www.braintrustdata.com/app/braintrustdata.com/p/llamaindex-recurisve-retrievers/baseRetriever)
*   [recursive metadata retreiver](https://www.braintrustdata.com/app/braintrustdata.com/p/llamaindex-recurisve-retrievers/recursiveMetadataRetriever)
*   [recursive chunk retriever](https://www.braintrustdata.com/app/braintrustdata.com/p/llamaindex-recurisve-retrievers/recursiveChunkRetriever)

### Dataset Generation[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/recurisve_retriever_nodes_braintrust/#dataset-generation)

We first generate a dataset of questions from the set of text chunks.

In \[ \]:

Copied!

from llama\_index.core.evaluation import (
    generate\_question\_context\_pairs,
    EmbeddingQAFinetuneDataset,
)
import nest\_asyncio

nest\_asyncio.apply()

from llama\_index.core.evaluation import ( generate\_question\_context\_pairs, EmbeddingQAFinetuneDataset, ) import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

eval\_dataset \= generate\_question\_context\_pairs(base\_nodes)

eval\_dataset = generate\_question\_context\_pairs(base\_nodes)

In \[ \]:

Copied!

eval\_dataset.save\_json("data/llama2\_eval\_dataset.json")

eval\_dataset.save\_json("data/llama2\_eval\_dataset.json")

In \[ \]:

Copied!

\# optional
eval\_dataset \= EmbeddingQAFinetuneDataset.from\_json(
    "data/llama2\_eval\_dataset.json"
)

\# optional eval\_dataset = EmbeddingQAFinetuneDataset.from\_json( "data/llama2\_eval\_dataset.json" )

### Compare Results[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/recurisve_retriever_nodes_braintrust/#compare-results)

We run evaluations on each of the retrievers to measure hit rate and MRR.

We find that retrievers with node references (either chunk or metadata) tend to perform better than retrieving the raw chunks.

In \[ \]:

Copied!

import pandas as pd

\# set vector retriever similarity top k to higher
top\_k \= 10

def display\_results(names, results\_arr):
    """Display results from evaluate."""

    hit\_rates \= \[\]
    mrrs \= \[\]
    for name, eval\_results in zip(names, results\_arr):
        metric\_dicts \= \[\]
        for eval\_result in eval\_results:
            metric\_dict \= eval\_result.metric\_vals\_dict
            metric\_dicts.append(metric\_dict)
        results\_df \= pd.DataFrame(metric\_dicts)

        hit\_rate \= results\_df\["hit\_rate"\].mean()
        mrr \= results\_df\["mrr"\].mean()
        hit\_rates.append(hit\_rate)
        mrrs.append(mrr)

    final\_df \= pd.DataFrame(
        {"retrievers": names, "hit\_rate": hit\_rates, "mrr": mrrs}
    )
    display(final\_df)

import pandas as pd # set vector retriever similarity top k to higher top\_k = 10 def display\_results(names, results\_arr): """Display results from evaluate.""" hit\_rates = \[\] mrrs = \[\] for name, eval\_results in zip(names, results\_arr): metric\_dicts = \[\] for eval\_result in eval\_results: metric\_dict = eval\_result.metric\_vals\_dict metric\_dicts.append(metric\_dict) results\_df = pd.DataFrame(metric\_dicts) hit\_rate = results\_df\["hit\_rate"\].mean() mrr = results\_df\["mrr"\].mean() hit\_rates.append(hit\_rate) mrrs.append(mrr) final\_df = pd.DataFrame( {"retrievers": names, "hit\_rate": hit\_rates, "mrr": mrrs} ) display(final\_df)

Let's define some scoring functions and define our dataset data variable.

In \[ \]:

Copied!

queries \= eval\_dataset.queries
relevant\_docs \= eval\_dataset.relevant\_docs
data \= \[
    ({"input": queries\[query\], "expected": relevant\_docs\[query\]})
    for query in queries.keys()
\]

def hitRateScorer(input, expected, output\=None):
    is\_hit \= any(\[id in expected for id in output\])
    return 1 if is\_hit else 0

def mrrScorer(input, expected, output\=None):
    for i, id in enumerate(output):
        if id in expected:
            return 1 / (i + 1)
    return 0

queries = eval\_dataset.queries relevant\_docs = eval\_dataset.relevant\_docs data = \[ ({"input": queries\[query\], "expected": relevant\_docs\[query\]}) for query in queries.keys() \] def hitRateScorer(input, expected, output=None): is\_hit = any(\[id in expected for id in output\]) return 1 if is\_hit else 0 def mrrScorer(input, expected, output=None): for i, id in enumerate(output): if id in expected: return 1 / (i + 1) return 0

In \[ \]:

Copied!

import braintrust

\# Evaluate the chunk retriever
vector\_retriever\_chunk \= vector\_index\_chunk.as\_retriever(similarity\_top\_k\=10)
retriever\_chunk \= RecursiveRetriever(
    "vector",
    retriever\_dict\={"vector": vector\_retriever\_chunk},
    node\_dict\=all\_nodes\_dict,
    verbose\=False,
)

def runChunkRetriever(input, hooks):
    retrieved\_nodes \= retriever\_chunk.retrieve(input)
    retrieved\_ids \= \[node.node.node\_id for node in retrieved\_nodes\]
    return retrieved\_ids

chunkEval \= await braintrust.Eval(
    name\="llamaindex-recurisve-retrievers",
    data\=data,
    task\=runChunkRetriever,
    scores\=\[hitRateScorer, mrrScorer\],
)

import braintrust # Evaluate the chunk retriever vector\_retriever\_chunk = vector\_index\_chunk.as\_retriever(similarity\_top\_k=10) retriever\_chunk = RecursiveRetriever( "vector", retriever\_dict={"vector": vector\_retriever\_chunk}, node\_dict=all\_nodes\_dict, verbose=False, ) def runChunkRetriever(input, hooks): retrieved\_nodes = retriever\_chunk.retrieve(input) retrieved\_ids = \[node.node.node\_id for node in retrieved\_nodes\] return retrieved\_ids chunkEval = await braintrust.Eval( name="llamaindex-recurisve-retrievers", data=data, task=runChunkRetriever, scores=\[hitRateScorer, mrrScorer\], )

In \[ \]:

Copied!

\# Evaluate the metadata retriever

vector\_retriever\_metadata \= vector\_index\_metadata.as\_retriever(
    similarity\_top\_k\=10
)
retriever\_metadata \= RecursiveRetriever(
    "vector",
    retriever\_dict\={"vector": vector\_retriever\_metadata},
    node\_dict\=all\_nodes\_dict,
    verbose\=False,
)

def runMetaDataRetriever(input, hooks):
    retrieved\_nodes \= retriever\_metadata.retrieve(input)
    retrieved\_ids \= \[node.node.node\_id for node in retrieved\_nodes\]
    return retrieved\_ids

metadataEval \= await braintrust.Eval(
    name\="llamaindex-recurisve-retrievers",
    data\=data,
    task\=runMetaDataRetriever,
    scores\=\[hitRateScorer, mrrScorer\],
)

\# Evaluate the metadata retriever vector\_retriever\_metadata = vector\_index\_metadata.as\_retriever( similarity\_top\_k=10 ) retriever\_metadata = RecursiveRetriever( "vector", retriever\_dict={"vector": vector\_retriever\_metadata}, node\_dict=all\_nodes\_dict, verbose=False, ) def runMetaDataRetriever(input, hooks): retrieved\_nodes = retriever\_metadata.retrieve(input) retrieved\_ids = \[node.node.node\_id for node in retrieved\_nodes\] return retrieved\_ids metadataEval = await braintrust.Eval( name="llamaindex-recurisve-retrievers", data=data, task=runMetaDataRetriever, scores=\[hitRateScorer, mrrScorer\], )

In \[ \]:

Copied!

\# Evaluate the base retriever
base\_retriever \= base\_index.as\_retriever(similarity\_top\_k\=10)

def runBaseRetriever(input, hooks):
    retrieved\_nodes \= base\_retriever.retrieve(input)
    retrieved\_ids \= \[node.node.node\_id for node in retrieved\_nodes\]
    return retrieved\_ids

baseEval \= await braintrust.Eval(
    name\="llamaindex-recurisve-retrievers",
    data\=data,
    task\=runBaseRetriever,
    scores\=\[hitRateScorer, mrrScorer\],
)

\# Evaluate the base retriever base\_retriever = base\_index.as\_retriever(similarity\_top\_k=10) def runBaseRetriever(input, hooks): retrieved\_nodes = base\_retriever.retrieve(input) retrieved\_ids = \[node.node.node\_id for node in retrieved\_nodes\] return retrieved\_ids baseEval = await braintrust.Eval( name="llamaindex-recurisve-retrievers", data=data, task=runBaseRetriever, scores=\[hitRateScorer, mrrScorer\], )

Back to top

[Previous Reciprocal Rerank Fusion Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/reciprocal_rerank_fusion/)[Next Recursive Retriever + Node References](https://docs.llamaindex.ai/en/stable/examples/retrievers/recursive_retriever_nodes/)
