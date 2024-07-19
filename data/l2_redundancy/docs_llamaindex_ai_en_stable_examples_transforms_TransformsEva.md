Title: Transforms Evaluation - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/transforms/TransformsEval/

Markdown Content:
Transforms Evaluation - LlamaIndex


[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/docs/examples/transforms/TransformsEval.ipynb)

Here we try out different transformations and evaluate their quality.

*   First we try out different parsers (PDF, JSON)
*   Then we try out different extractors

In \[ \]:

Copied!

%pip install llama\-index\-readers\-file
%pip install llama\-index\-llms\-openai
%pip install llama\-index\-embeddings\-openai

%pip install llama-index-readers-file %pip install llama-index-llms-openai %pip install llama-index-embeddings-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

Load Data + Setup[¶](https://docs.llamaindex.ai/en/stable/examples/transforms/TransformsEval/#load-data-setup)
--------------------------------------------------------------------------------------------------------------

Load in the Tesla data.

In \[ \]:

Copied!

import pandas as pd

pd.set\_option("display.max\_rows", None)
pd.set\_option("display.max\_columns", None)
pd.set\_option("display.width", None)
pd.set\_option("display.max\_colwidth", None)

import pandas as pd pd.set\_option("display.max\_rows", None) pd.set\_option("display.max\_columns", None) pd.set\_option("display.width", None) pd.set\_option("display.max\_colwidth", None)

In \[ \]:

Copied!

!wget "https://www.dropbox.com/scl/fi/mlaymdy1ni1ovyeykhhuk/tesla\_2021\_10k.htm?rlkey=qf9k4zn0ejrbm716j0gg7r802&dl=1" \-O tesla\_2021\_10k.htm
!wget "https://www.dropbox.com/scl/fi/rkw0u959yb4w8vlzz76sa/tesla\_2020\_10k.htm?rlkey=tfkdshswpoupav5tqigwz1mp7&dl=1" \-O tesla\_2020\_10k.htm

!wget "https://www.dropbox.com/scl/fi/mlaymdy1ni1ovyeykhhuk/tesla\_2021\_10k.htm?rlkey=qf9k4zn0ejrbm716j0gg7r802&dl=1" -O tesla\_2021\_10k.htm !wget "https://www.dropbox.com/scl/fi/rkw0u959yb4w8vlzz76sa/tesla\_2020\_10k.htm?rlkey=tfkdshswpoupav5tqigwz1mp7&dl=1" -O tesla\_2020\_10k.htm

In \[ \]:

Copied!

from llama\_index.readers.file import FlatReader
from pathlib import Path

reader \= FlatReader()
docs \= reader.load\_data(Path("./tesla\_2020\_10k.htm"))

from llama\_index.readers.file import FlatReader from pathlib import Path reader = FlatReader() docs = reader.load\_data(Path("./tesla\_2020\_10k.htm"))

Generate Eval Dataset / Define Eval Functions[¶](https://docs.llamaindex.ai/en/stable/examples/transforms/TransformsEval/#generate-eval-dataset-define-eval-functions)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Generate a "golden" eval dataset from the Tesla documents.

Also define eval functions for running a pipeline.

Here we define an ingestion pipeline purely for generating a synthetic eval dataset.

In \[ \]:

Copied!

from llama\_index.core.evaluation import DatasetGenerator, QueryResponseDataset
from llama\_index.llms.openai import OpenAI
from llama\_index.embeddings.openai import OpenAIEmbedding
from llama\_index.readers.file import FlatReader
from llama\_index.core.node\_parser import HTMLNodeParser, SentenceSplitter
from llama\_index.core.ingestion import IngestionPipeline
from pathlib import Path

import nest\_asyncio

nest\_asyncio.apply()

from llama\_index.core.evaluation import DatasetGenerator, QueryResponseDataset from llama\_index.llms.openai import OpenAI from llama\_index.embeddings.openai import OpenAIEmbedding from llama\_index.readers.file import FlatReader from llama\_index.core.node\_parser import HTMLNodeParser, SentenceSplitter from llama\_index.core.ingestion import IngestionPipeline from pathlib import Path import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

reader \= FlatReader()
docs \= reader.load\_data(Path("./tesla\_2020\_10k.htm"))

pipeline \= IngestionPipeline(
    documents\=docs,
    transformations\=\[
        HTMLNodeParser.from\_defaults(),
        SentenceSplitter(chunk\_size\=1024, chunk\_overlap\=200),
        OpenAIEmbedding(),
    \],
)
eval\_nodes \= pipeline.run(documents\=docs)

reader = FlatReader() docs = reader.load\_data(Path("./tesla\_2020\_10k.htm")) pipeline = IngestionPipeline( documents=docs, transformations=\[ HTMLNodeParser.from\_defaults(), SentenceSplitter(chunk\_size=1024, chunk\_overlap=200), OpenAIEmbedding(), \], ) eval\_nodes = pipeline.run(documents=docs)

In \[ \]:

Copied!

\# NOTE: run this if the dataset isn't already saved
\# Note: we only generate from the first 20 nodes, since the rest are references
\# eval\_llm = OpenAI(model="gpt-4-1106-preview")
eval\_llm \= OpenAI(model\="gpt-3.5-turbo")

dataset\_generator \= DatasetGenerator(
    eval\_nodes\[:100\],
    llm\=eval\_llm,
    show\_progress\=True,
    num\_questions\_per\_chunk\=3,
)

\# NOTE: run this if the dataset isn't already saved # Note: we only generate from the first 20 nodes, since the rest are references # eval\_llm = OpenAI(model="gpt-4-1106-preview") eval\_llm = OpenAI(model="gpt-3.5-turbo") dataset\_generator = DatasetGenerator( eval\_nodes\[:100\], llm=eval\_llm, show\_progress=True, num\_questions\_per\_chunk=3, )

In \[ \]:

Copied!

eval\_dataset \= await dataset\_generator.agenerate\_dataset\_from\_nodes(num\=100)

eval\_dataset = await dataset\_generator.agenerate\_dataset\_from\_nodes(num=100)

In \[ \]:

Copied!

len(eval\_dataset.qr\_pairs)

len(eval\_dataset.qr\_pairs)

Out\[ \]:

100

In \[ \]:

Copied!

eval\_dataset.save\_json("data/tesla10k\_eval\_dataset.json")

eval\_dataset.save\_json("data/tesla10k\_eval\_dataset.json")

In \[ \]:

Copied!

\# optional
eval\_dataset \= QueryResponseDataset.from\_json(
    "data/tesla10k\_eval\_dataset.json"
)

\# optional eval\_dataset = QueryResponseDataset.from\_json( "data/tesla10k\_eval\_dataset.json" )

In \[ \]:

Copied!

eval\_qs \= eval\_dataset.questions
qr\_pairs \= eval\_dataset.qr\_pairs
ref\_response\_strs \= \[r for (\_, r) in qr\_pairs\]

eval\_qs = eval\_dataset.questions qr\_pairs = eval\_dataset.qr\_pairs ref\_response\_strs = \[r for (\_, r) in qr\_pairs\]

### Run Evals[¶](https://docs.llamaindex.ai/en/stable/examples/transforms/TransformsEval/#run-evals)

In \[ \]:

Copied!

from llama\_index.core.evaluation import (
    CorrectnessEvaluator,
    SemanticSimilarityEvaluator,
)
from llama\_index.core.evaluation.eval\_utils import (
    get\_responses,
    get\_results\_df,
)
from llama\_index.core.evaluation import BatchEvalRunner

from llama\_index.core.evaluation import ( CorrectnessEvaluator, SemanticSimilarityEvaluator, ) from llama\_index.core.evaluation.eval\_utils import ( get\_responses, get\_results\_df, ) from llama\_index.core.evaluation import BatchEvalRunner

In \[ \]:

Copied!

evaluator\_c \= CorrectnessEvaluator(llm\=eval\_llm)
evaluator\_s \= SemanticSimilarityEvaluator(llm\=eval\_llm)
evaluator\_dict \= {
    "correctness": evaluator\_c,
    "semantic\_similarity": evaluator\_s,
}
batch\_eval\_runner \= BatchEvalRunner(
    evaluator\_dict, workers\=2, show\_progress\=True
)

evaluator\_c = CorrectnessEvaluator(llm=eval\_llm) evaluator\_s = SemanticSimilarityEvaluator(llm=eval\_llm) evaluator\_dict = { "correctness": evaluator\_c, "semantic\_similarity": evaluator\_s, } batch\_eval\_runner = BatchEvalRunner( evaluator\_dict, workers=2, show\_progress=True )

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex

async def run\_evals(
    pipeline, batch\_eval\_runner, docs, eval\_qs, eval\_responses\_ref
):
    \# get query engine
    nodes \= pipeline.run(documents\=docs)
    \# define vector index (top-k = 2)
    vector\_index \= VectorStoreIndex(nodes)
    query\_engine \= vector\_index.as\_query\_engine()

    pred\_responses \= get\_responses(eval\_qs, query\_engine, show\_progress\=True)
    eval\_results \= await batch\_eval\_runner.aevaluate\_responses(
        eval\_qs, responses\=pred\_responses, reference\=eval\_responses\_ref
    )
    return eval\_results

from llama\_index.core import VectorStoreIndex async def run\_evals( pipeline, batch\_eval\_runner, docs, eval\_qs, eval\_responses\_ref ): # get query engine nodes = pipeline.run(documents=docs) # define vector index (top-k = 2) vector\_index = VectorStoreIndex(nodes) query\_engine = vector\_index.as\_query\_engine() pred\_responses = get\_responses(eval\_qs, query\_engine, show\_progress=True) eval\_results = await batch\_eval\_runner.aevaluate\_responses( eval\_qs, responses=pred\_responses, reference=eval\_responses\_ref ) return eval\_results

1\. Try out Different Sentence Splitter (Overlaps)[¶](https://docs.llamaindex.ai/en/stable/examples/transforms/TransformsEval/#1-try-out-different-sentence-splitter-overlaps)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The chunking strategy matters! Here we try the sentence splitter with different overlap values, to see how it impacts performance.

The `IngestionPipeline` lets us concisely define an e2e transformation pipeline for RAG, and we define variants where each corresponds to a different sentence splitter configuration (while keeping other steps fixed).

In \[ \]:

Copied!

from llama\_index.core.node\_parser import HTMLNodeParser, SentenceSplitter

\# For clarity in the demo, make small splits without overlap
sent\_parser\_o0 \= SentenceSplitter(chunk\_size\=1024, chunk\_overlap\=0)
sent\_parser\_o200 \= SentenceSplitter(chunk\_size\=1024, chunk\_overlap\=200)
sent\_parser\_o500 \= SentenceSplitter(chunk\_size\=1024, chunk\_overlap\=600)

html\_parser \= HTMLNodeParser.from\_defaults()

parser\_dict \= {
    "sent\_parser\_o0": sent\_parser\_o0,
    "sent\_parser\_o200": sent\_parser\_o200,
    "sent\_parser\_o500": sent\_parser\_o500,
}

from llama\_index.core.node\_parser import HTMLNodeParser, SentenceSplitter # For clarity in the demo, make small splits without overlap sent\_parser\_o0 = SentenceSplitter(chunk\_size=1024, chunk\_overlap=0) sent\_parser\_o200 = SentenceSplitter(chunk\_size=1024, chunk\_overlap=200) sent\_parser\_o500 = SentenceSplitter(chunk\_size=1024, chunk\_overlap=600) html\_parser = HTMLNodeParser.from\_defaults() parser\_dict = { "sent\_parser\_o0": sent\_parser\_o0, "sent\_parser\_o200": sent\_parser\_o200, "sent\_parser\_o500": sent\_parser\_o500, }

Define a separate pipeline for each parser.

In \[ \]:

Copied!

from llama\_index.embeddings.openai import OpenAIEmbedding
from llama\_index.core.ingestion import IngestionPipeline

\# generate a pipeline for each parser
\# keep embedding model fixed
pipeline\_dict \= {}
for k, parser in parser\_dict.items():
    pipeline \= IngestionPipeline(
        documents\=docs,
        transformations\=\[
            html\_parser,
            parser,
            OpenAIEmbedding(),
        \],
    )
    pipeline\_dict\[k\] \= pipeline

from llama\_index.embeddings.openai import OpenAIEmbedding from llama\_index.core.ingestion import IngestionPipeline # generate a pipeline for each parser # keep embedding model fixed pipeline\_dict = {} for k, parser in parser\_dict.items(): pipeline = IngestionPipeline( documents=docs, transformations=\[ html\_parser, parser, OpenAIEmbedding(), \], ) pipeline\_dict\[k\] = pipeline

In \[ \]:

Copied!

eval\_results\_dict \= {}
for k, pipeline in pipeline\_dict.items():
    eval\_results \= await run\_evals(
        pipeline, batch\_eval\_runner, docs, eval\_qs, ref\_response\_strs
    )
    eval\_results\_dict\[k\] \= eval\_results

eval\_results\_dict = {} for k, pipeline in pipeline\_dict.items(): eval\_results = await run\_evals( pipeline, batch\_eval\_runner, docs, eval\_qs, ref\_response\_strs ) eval\_results\_dict\[k\] = eval\_results

In \[ \]:

Copied!

\# \[tmp\] save eval results
import pickle

pickle.dump(eval\_results\_dict, open("eval\_results\_1.pkl", "wb"))

\# \[tmp\] save eval results import pickle pickle.dump(eval\_results\_dict, open("eval\_results\_1.pkl", "wb"))

In \[ \]:

Copied!

eval\_results\_list \= list(eval\_results\_dict.items())

results\_df \= get\_results\_df(
    \[v for \_, v in eval\_results\_list\],
    \[k for k, \_ in eval\_results\_list\],
    \["correctness", "semantic\_similarity"\],
)
display(results\_df)

eval\_results\_list = list(eval\_results\_dict.items()) results\_df = get\_results\_df( \[v for \_, v in eval\_results\_list\], \[k for k, \_ in eval\_results\_list\], \["correctness", "semantic\_similarity"\], ) display(results\_df)

|  | names | correctness | semantic\_similarity |
| --- | --- | --- | --- |
| 0 | sent\_parser\_o0 | 4.310 | 0.972838 |
| 1 | sent\_parser\_o200 | 4.335 | 0.978842 |
| 2 | sent\_parser\_o500 | 4.270 | 0.971759 |

In \[ \]:

Copied!

\# \[optional\] persist cache in folders so we can reuse
for k, pipeline in pipeline\_dict.items():
    pipeline.cache.persist(f"./cache/{k}.json")

\# \[optional\] persist cache in folders so we can reuse for k, pipeline in pipeline\_dict.items(): pipeline.cache.persist(f"./cache/{k}.json")

2\. Try out Different Extractors[¶](https://docs.llamaindex.ai/en/stable/examples/transforms/TransformsEval/#2-try-out-different-extractors)
--------------------------------------------------------------------------------------------------------------------------------------------

Similarly, metadata extraction can be quite important for good performance. We experiment with this as a last step in an overall ingestion pipeline, and define different ingestion pipeline variants corresponding to different extractors.

We define the set of document extractors we want to try out.

We keep the parsers fixed (HTML parser, sentence splitter w/ overlap 200) and the embedding model fixed (OpenAIEmbedding).

In \[ \]:

Copied!

from llama\_index.core.extractors import (
    TitleExtractor,
    QuestionsAnsweredExtractor,
    SummaryExtractor,
)
from llama\_index.core.node\_parser import HTMLNodeParser, SentenceSplitter

\# generate a pipeline for each extractor
\# keep embedding model fixed
extractor\_dict \= {
    \# "title": TitleExtractor(),
    "summary": SummaryExtractor(in\_place\=False),
    "qa": QuestionsAnsweredExtractor(in\_place\=False),
    "default": None,
}

\# these are the parsers that will run beforehand
html\_parser \= HTMLNodeParser.from\_defaults()
sent\_parser\_o200 \= SentenceSplitter(chunk\_size\=1024, chunk\_overlap\=200)

from llama\_index.core.extractors import ( TitleExtractor, QuestionsAnsweredExtractor, SummaryExtractor, ) from llama\_index.core.node\_parser import HTMLNodeParser, SentenceSplitter # generate a pipeline for each extractor # keep embedding model fixed extractor\_dict = { # "title": TitleExtractor(), "summary": SummaryExtractor(in\_place=False), "qa": QuestionsAnsweredExtractor(in\_place=False), "default": None, } # these are the parsers that will run beforehand html\_parser = HTMLNodeParser.from\_defaults() sent\_parser\_o200 = SentenceSplitter(chunk\_size=1024, chunk\_overlap=200)

In \[ \]:

Copied!

pipeline\_dict \= {}
html\_parser \= HTMLNodeParser.from\_defaults()
for k, extractor in extractor\_dict.items():
    if k \ "default": transformations = \[ html\_parser, sent\_parser\_o200, OpenAIEmbedding(), \] else: transformations = \[ html\_parser, sent\_parser\_o200, extractor, OpenAIEmbedding(), \] pipeline = IngestionPipeline(transformations=transformations) pipeline\_dict\[k\] = pipeline

In \[ \]:

Copied!

eval\_results\_dict\_2 \= {}
for k, pipeline in pipeline\_dict.items():
    eval\_results \= await run\_evals(
        pipeline, batch\_eval\_runner, docs, eval\_qs, ref\_response\_strs
    )
    eval\_results\_dict\_2\[k\] \= eval\_results

eval\_results\_dict\_2 = {} for k, pipeline in pipeline\_dict.items(): eval\_results = await run\_evals( pipeline, batch\_eval\_runner, docs, eval\_qs, ref\_response\_strs ) eval\_results\_dict\_2\[k\] = eval\_results

In \[ \]:

Copied!

eval\_results\_list\_2 \= list(eval\_results\_dict\_2.items())

results\_df \= get\_results\_df(
    \[v for \_, v in eval\_results\_list\_2\],
    \[k for k, \_ in eval\_results\_list\_2\],
    \["correctness", "semantic\_similarity"\],
)
display(results\_df)

eval\_results\_list\_2 = list(eval\_results\_dict\_2.items()) results\_df = get\_results\_df( \[v for \_, v in eval\_results\_list\_2\], \[k for k, \_ in eval\_results\_list\_2\], \["correctness", "semantic\_similarity"\], ) display(results\_df)

|  | names | correctness | semantic\_similarity |
| --- | --- | --- | --- |
| 0 | summary | 4.315 | 0.976951 |
| 1 | qa | 4.355 | 0.978807 |
| 2 | default | 4.305 | 0.978451 |

In \[ \]:

Copied!

\# \[optional\] persist cache in folders so we can reuse
for k, pipeline in pipeline\_dict.items():
    pipeline.cache.persist(f"./cache/{k}.json")

\# \[optional\] persist cache in folders so we can reuse for k, pipeline in pipeline\_dict.items(): pipeline.cache.persist(f"./cache/{k}.json")

3\. Try out Multiple Extractors (with Caching)[¶](https://docs.llamaindex.ai/en/stable/examples/transforms/TransformsEval/#3-try-out-multiple-extractors-with-caching)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

TODO

Each extraction step can be expensive due to LLM calls. What if we want to experiment with multiple extractors?

We take advantage of **caching** so that all previous extractor calls are cached, and we only experiment with the final extractor call. The `IngestionPipeline` gives us a clean abstraction to play around with the final extractor.

Try out different extractors

Back to top

[Previous Evaluation Query Engine Tool](https://docs.llamaindex.ai/en/stable/examples/tools/eval_query_engine_tool/)[Next 10K Analysis](https://docs.llamaindex.ai/en/stable/examples/usecases/10k_sub_question/)
