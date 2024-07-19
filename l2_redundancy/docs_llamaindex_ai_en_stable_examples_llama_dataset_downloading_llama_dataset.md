Title: Downloading a LlamaDataset from LlamaHub

URL Source: https://docs.llamaindex.ai/en/stable/examples/llama_dataset/downloading_llama_datasets/

Markdown Content:
Downloading a LlamaDataset from LlamaHub - LlamaIndex


You can browse our available benchmark datasets via [llamahub.ai](https://llamahub.ai/). This notebook guide depicts how you can download the dataset and its source text documents. In particular, the `download_llama_dataset` will download the evaluation dataset (i.e., `LabelledRagDataset`) as well as the `Document`'s of the source text files used to build the evaluation dataset in the first place.

Finally, in this notebook, we also demonstrate the end to end workflow of downloading an evaluation dataset, making predictions on it using your own RAG pipeline (query engine) and then evaluating these predictions.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai

%pip install llama-index-llms-openai

In \[ \]:

Copied!

from llama\_index.core.llama\_dataset import download\_llama\_dataset

\# download and install dependencies
rag\_dataset, documents \= download\_llama\_dataset(
    "PaulGrahamEssayDataset", "./paul\_graham"
)

from llama\_index.core.llama\_dataset import download\_llama\_dataset # download and install dependencies rag\_dataset, documents = download\_llama\_dataset( "PaulGrahamEssayDataset", "./paul\_graham" )

github url: https://raw.githubusercontent.com/nerdai/llama-hub/datasets/llama\_hub/llama\_datasets/library.json
github url: https://media.githubusercontent.com/media/run-llama/llama\_datasets/main/llama\_datasets/paul\_graham\_essay/rag\_dataset.json
github url: https://media.githubusercontent.com/media/run-llama/llama\_datasets/main/llama\_datasets/paul\_graham\_essay/source.txt

In \[ \]:

Copied!

rag\_dataset.to\_pandas()\[:5\]

rag\_dataset.to\_pandas()\[:5\]

Out\[ \]:

|  | query | reference\_contexts | reference\_answer | reference\_answer\_by | query\_by |
| --- | --- | --- | --- | --- | --- |
| 0 | In the essay, the author mentions his early ex... | \[What I Worked On\\n\\nFebruary 2021\\n\\nBefore c... | The first computer the author used for program... | ai (gpt-4) | ai (gpt-4) |
| 1 | The author switched his major from philosophy ... | \[What I Worked On\\n\\nFebruary 2021\\n\\nBefore c... | The two specific influences that led the autho... | ai (gpt-4) | ai (gpt-4) |
| 2 | In the essay, the author discusses his initial... | \[I couldn't have put this into words when I wa... | The two main influences that initially drew th... | ai (gpt-4) | ai (gpt-4) |
| 3 | The author mentions his shift of interest towa... | \[I couldn't have put this into words when I wa... | The author shifted his interest towards Lisp a... | ai (gpt-4) | ai (gpt-4) |
| 4 | In the essay, the author mentions his interest... | \[So I looked around to see what I could salvag... | The author in the essay is Paul Graham, who wa... | ai (gpt-4) | ai (gpt-4) |

With `documents`, you can build your own RAG pipeline, to then predict and perform evaluations to compare against the benchmarks listed in the `DatasetCard` associated with the datasets [llamahub.ai](https://llamahub.ai/).

### Predictions[¶](https://docs.llamaindex.ai/en/stable/examples/llama_dataset/downloading_llama_datasets/#predictions)

**NOTE**: The rest of the notebook illustrates how to manually perform predictions and subsequent evaluations for demonstrative purposes. Alternatively you can use the `RagEvaluatorPack` that will take care of predicting and evaluating using a RAG system that you would have provided.

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex

\# a basic RAG pipeline, uses defaults
index \= VectorStoreIndex.from\_documents(documents\=documents)
query\_engine \= index.as\_query\_engine()

from llama\_index.core import VectorStoreIndex # a basic RAG pipeline, uses defaults index = VectorStoreIndex.from\_documents(documents=documents) query\_engine = index.as\_query\_engine()

You can now create predictions and perform evaluation manually or download the `PredictAndEvaluatePack` to do this for you in a single line of code.

In \[ \]:

Copied!

import nest\_asyncio

nest\_asyncio.apply()

import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

\# manually
prediction\_dataset \= await rag\_dataset.amake\_predictions\_with(
    query\_engine\=query\_engine, show\_progress\=True
)

\# manually prediction\_dataset = await rag\_dataset.amake\_predictions\_with( query\_engine=query\_engine, show\_progress=True )

100%|███████████████████████████████████████████████████████| 44/44 \[00:08<00:00,  4.90it/s\]

In \[ \]:

Copied!

prediction\_dataset.to\_pandas()\[:5\]

prediction\_dataset.to\_pandas()\[:5\]

Out\[ \]:

|  | response | contexts |
| --- | --- | --- |
| 0 | The author mentions that the first computer he... | \[What I Worked On\\n\\nFebruary 2021\\n\\nBefore c... |
| 1 | The author switched his major from philosophy ... | \[I couldn't have put this into words when I wa... |
| 2 | The author mentions two main influences that i... | \[I couldn't have put this into words when I wa... |
| 3 | The author mentions that he shifted his intere... | \[So I looked around to see what I could salvag... |
| 4 | The author mentions his interest in both compu... | \[What I Worked On\\n\\nFebruary 2021\\n\\nBefore c... |

### Evaluation[¶](https://docs.llamaindex.ai/en/stable/examples/llama_dataset/downloading_llama_datasets/#evaluation)

Now that we have our predictions, we can perform evaluations on two dimensions:

1.  The generated response: how well the predicted response matches the reference answer.
2.  The retrieved contexts: how well the retrieved contexts for the prediction match the reference contexts.

NOTE: For retrieved contexts, we are unable to use standard retrieval metrics such as `hit rate` and `mean reciproccal rank` due to the fact that doing so requires we have the same index that was used to generate the ground truth data. But, it is not necessary for a `LabelledRagDataset` to be even created by an index. As such, we will use `semantic similarity` between the prediction's contexts and the reference contexts as a measure of goodness.

In \[ \]:

Copied!

import tqdm

import tqdm

For evaluating the response, we will use the LLM-As-A-Judge pattern. Specifically, we will use `CorrectnessEvaluator`, `FaithfulnessEvaluator` and `RelevancyEvaluator`.

For evaluating the goodness of the retrieved contexts we will use `SemanticSimilarityEvaluator`.

In \[ \]:

Copied!

\# instantiate the gpt-4 judge
from llama\_index.llms.openai import OpenAI
from llama\_index.core.evaluation import (
    CorrectnessEvaluator,
    FaithfulnessEvaluator,
    RelevancyEvaluator,
    SemanticSimilarityEvaluator,
)

judges \= {}

judges\["correctness"\] \= CorrectnessEvaluator(
    llm\=OpenAI(temperature\=0, model\="gpt-4"),
)

judges\["relevancy"\] \= RelevancyEvaluator(
    llm\=OpenAI(temperature\=0, model\="gpt-4"),
)

judges\["faithfulness"\] \= FaithfulnessEvaluator(
    llm\=OpenAI(temperature\=0, model\="gpt-4"),
)

judges\["semantic\_similarity"\] \= SemanticSimilarityEvaluator()

\# instantiate the gpt-4 judge from llama\_index.llms.openai import OpenAI from llama\_index.core.evaluation import ( CorrectnessEvaluator, FaithfulnessEvaluator, RelevancyEvaluator, SemanticSimilarityEvaluator, ) judges = {} judges\["correctness"\] = CorrectnessEvaluator( llm=OpenAI(temperature=0, model="gpt-4"), ) judges\["relevancy"\] = RelevancyEvaluator( llm=OpenAI(temperature=0, model="gpt-4"), ) judges\["faithfulness"\] = FaithfulnessEvaluator( llm=OpenAI(temperature=0, model="gpt-4"), ) judges\["semantic\_similarity"\] = SemanticSimilarityEvaluator()

Loop through the (`labelled_example`, `prediction`) pais and perform the evaluations on each of them individually.

In \[ \]:

Copied!

evals \= {
    "correctness": \[\],
    "relevancy": \[\],
    "faithfulness": \[\],
    "context\_similarity": \[\],
}

for example, prediction in tqdm.tqdm(
    zip(rag\_dataset.examples, prediction\_dataset.predictions)
):
    correctness\_result \= judges\["correctness"\].evaluate(
        query\=example.query,
        response\=prediction.response,
        reference\=example.reference\_answer,
    )

    relevancy\_result \= judges\["relevancy"\].evaluate(
        query\=example.query,
        response\=prediction.response,
        contexts\=prediction.contexts,
    )

    faithfulness\_result \= judges\["faithfulness"\].evaluate(
        query\=example.query,
        response\=prediction.response,
        contexts\=prediction.contexts,
    )

    semantic\_similarity\_result \= judges\["semantic\_similarity"\].evaluate(
        query\=example.query,
        response\="\\n".join(prediction.contexts),
        reference\="\\n".join(example.reference\_contexts),
    )

    evals\["correctness"\].append(correctness\_result)
    evals\["relevancy"\].append(relevancy\_result)
    evals\["faithfulness"\].append(faithfulness\_result)
    evals\["context\_similarity"\].append(semantic\_similarity\_result)

evals = { "correctness": \[\], "relevancy": \[\], "faithfulness": \[\], "context\_similarity": \[\], } for example, prediction in tqdm.tqdm( zip(rag\_dataset.examples, prediction\_dataset.predictions) ): correctness\_result = judges\["correctness"\].evaluate( query=example.query, response=prediction.response, reference=example.reference\_answer, ) relevancy\_result = judges\["relevancy"\].evaluate( query=example.query, response=prediction.response, contexts=prediction.contexts, ) faithfulness\_result = judges\["faithfulness"\].evaluate( query=example.query, response=prediction.response, contexts=prediction.contexts, ) semantic\_similarity\_result = judges\["semantic\_similarity"\].evaluate( query=example.query, response="\\n".join(prediction.contexts), reference="\\n".join(example.reference\_contexts), ) evals\["correctness"\].append(correctness\_result) evals\["relevancy"\].append(relevancy\_result) evals\["faithfulness"\].append(faithfulness\_result) evals\["context\_similarity"\].append(semantic\_similarity\_result)

44it \[07:15,  9.90s/it\]

In \[ \]:

Copied!

import json

\# saving evaluations
evaluations\_objects \= {
    "context\_similarity": \[e.dict() for e in evals\["context\_similarity"\]\],
    "correctness": \[e.dict() for e in evals\["correctness"\]\],
    "faithfulness": \[e.dict() for e in evals\["faithfulness"\]\],
    "relevancy": \[e.dict() for e in evals\["relevancy"\]\],
}

with open("evaluations.json", "w") as json\_file:
    json.dump(evaluations\_objects, json\_file)

import json # saving evaluations evaluations\_objects = { "context\_similarity": \[e.dict() for e in evals\["context\_similarity"\]\], "correctness": \[e.dict() for e in evals\["correctness"\]\], "faithfulness": \[e.dict() for e in evals\["faithfulness"\]\], "relevancy": \[e.dict() for e in evals\["relevancy"\]\], } with open("evaluations.json", "w") as json\_file: json.dump(evaluations\_objects, json\_file)

Now, we can use our notebook utility functions to view these evaluations.

In \[ \]:

Copied!

import pandas as pd
from llama\_index.core.evaluation.notebook\_utils import get\_eval\_results\_df

deep\_eval\_df, mean\_correctness\_df \= get\_eval\_results\_df(
    \["base\_rag"\] \* len(evals\["correctness"\]),
    evals\["correctness"\],
    metric\="correctness",
)
deep\_eval\_df, mean\_relevancy\_df \= get\_eval\_results\_df(
    \["base\_rag"\] \* len(evals\["relevancy"\]),
    evals\["relevancy"\],
    metric\="relevancy",
)
\_, mean\_faithfulness\_df \= get\_eval\_results\_df(
    \["base\_rag"\] \* len(evals\["faithfulness"\]),
    evals\["faithfulness"\],
    metric\="faithfulness",
)
\_, mean\_context\_similarity\_df \= get\_eval\_results\_df(
    \["base\_rag"\] \* len(evals\["context\_similarity"\]),
    evals\["context\_similarity"\],
    metric\="context\_similarity",
)

mean\_scores\_df \= pd.concat(
    \[
        mean\_correctness\_df.reset\_index(),
        mean\_relevancy\_df.reset\_index(),
        mean\_faithfulness\_df.reset\_index(),
        mean\_context\_similarity\_df.reset\_index(),
    \],
    axis\=0,
    ignore\_index\=True,
)
mean\_scores\_df \= mean\_scores\_df.set\_index("index")
mean\_scores\_df.index \= mean\_scores\_df.index.set\_names(\["metrics"\])

import pandas as pd from llama\_index.core.evaluation.notebook\_utils import get\_eval\_results\_df deep\_eval\_df, mean\_correctness\_df = get\_eval\_results\_df( \["base\_rag"\] \* len(evals\["correctness"\]), evals\["correctness"\], metric="correctness", ) deep\_eval\_df, mean\_relevancy\_df = get\_eval\_results\_df( \["base\_rag"\] \* len(evals\["relevancy"\]), evals\["relevancy"\], metric="relevancy", ) \_, mean\_faithfulness\_df = get\_eval\_results\_df( \["base\_rag"\] \* len(evals\["faithfulness"\]), evals\["faithfulness"\], metric="faithfulness", ) \_, mean\_context\_similarity\_df = get\_eval\_results\_df( \["base\_rag"\] \* len(evals\["context\_similarity"\]), evals\["context\_similarity"\], metric="context\_similarity", ) mean\_scores\_df = pd.concat( \[ mean\_correctness\_df.reset\_index(), mean\_relevancy\_df.reset\_index(), mean\_faithfulness\_df.reset\_index(), mean\_context\_similarity\_df.reset\_index(), \], axis=0, ignore\_index=True, ) mean\_scores\_df = mean\_scores\_df.set\_index("index") mean\_scores\_df.index = mean\_scores\_df.index.set\_names(\["metrics"\])

In \[ \]:

Copied!

mean\_scores\_df

mean\_scores\_df

Out\[ \]:

| rag | base\_rag |
| --- | --- |
| metrics |  |
| --- | --- |
| mean\_correctness\_score | 4.238636 |
| mean\_relevancy\_score | 0.977273 |
| mean\_faithfulness\_score | 0.977273 |
| mean\_context\_similarity\_score | 0.933568 |

On this toy example, we see that the basic RAG pipeline performs quite well against the evaluation benchmark (`rag_dataset`)! For completeness, to perform the above steps instead by using the `RagEvaluatorPack`, use the code provided below:

In \[ \]:

Copied!

from llama\_index.core.llama\_pack import download\_llama\_pack

RagEvaluatorPack \= download\_llama\_pack("RagEvaluatorPack", "./pack")
rag\_evaluator \= RagEvaluatorPack(
    query\_engine\=query\_engine, rag\_dataset\=rag\_dataset, show\_progress\=True
)

############################################################################
\# NOTE: If have a lower tier subscription for OpenAI API like Usage Tier 1 #
\# then you'll need to use different batch\_size and sleep\_time\_in\_seconds.  #
\# For Usage Tier 1, settings that seemed to work well were batch\_size=5,   #
\# and sleep\_time\_in\_seconds=15 (as of December 2023.)                      #
############################################################################

benchmark\_df \= await rag\_evaluator\_pack.arun(
    batch\_size\=20,  \# batches the number of openai api calls to make
    sleep\_time\_in\_seconds\=1,  \# seconds to sleep before making an api call
)

from llama\_index.core.llama\_pack import download\_llama\_pack RagEvaluatorPack = download\_llama\_pack("RagEvaluatorPack", "./pack") rag\_evaluator = RagEvaluatorPack( query\_engine=query\_engine, rag\_dataset=rag\_dataset, show\_progress=True ) ############################################################################ # NOTE: If have a lower tier subscription for OpenAI API like Usage Tier 1 # # then you'll need to use different batch\_size and sleep\_time\_in\_seconds. # # For Usage Tier 1, settings that seemed to work well were batch\_size=5, # # and sleep\_time\_in\_seconds=15 (as of December 2023.) # ############################################################################ benchmark\_df = await rag\_evaluator\_pack.arun( batch\_size=20, # batches the number of openai api calls to make sleep\_time\_in\_seconds=1, # seconds to sleep before making an api call )

Back to top

[Previous Yi](https://docs.llamaindex.ai/en/stable/examples/llm/yi/)[Next Benchmarking RAG Pipelines With A LabelledRagDatatset](https://docs.llamaindex.ai/en/stable/examples/llama_dataset/labelled-rag-datasets/)

Hi, how can I help you?

🦙
