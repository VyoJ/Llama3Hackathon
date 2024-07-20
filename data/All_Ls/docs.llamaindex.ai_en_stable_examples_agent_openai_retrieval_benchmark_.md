Title: Benchmarking OpenAI Retrieval API (through Assistant Agent)

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/openai_retrieval_benchmark/

Markdown Content:
Benchmarking OpenAI Retrieval API (through Assistant Agent) - LlamaIndex


[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/docs/examples/agent/openai_retrieval_benchmark.ipynb)

This guide benchmarks the Retrieval Tool from the [OpenAI Assistant API](https://platform.openai.com/docs/assistants/overview), by using our `OpenAIAssistantAgent`. We run over the Llama 2 paper, and compare generation quality against a naive RAG pipeline.

In \[ \]:

Copied!

%pip install llama\-index\-readers\-file pymupdf
%pip install llama\-index\-agent\-openai
%pip install llama\-index\-llms\-openai

%pip install llama-index-readers-file pymupdf %pip install llama-index-agent-openai %pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import nest\_asyncio

nest\_asyncio.apply()

import nest\_asyncio nest\_asyncio.apply()

Setup Data[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_retrieval_benchmark/#setup-data)
---------------------------------------------------------------------------------------------------------

Here we load the Llama 2 paper and chunk it.

In \[ \]:

Copied!

!mkdir \-p 'data/'
!wget \--user\-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" \-O "data/llama2.pdf"

!mkdir -p 'data/' !wget --user-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" -O "data/llama2.pdf"

\--2023-11-08 21:53:52--  https://arxiv.org/pdf/2307.09288.pdf
Resolving arxiv.org (arxiv.org)... 128.84.21.199
Connecting to arxiv.org (arxiv.org)|128.84.21.199|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 13661300 (13M) \[application/pdf\]
Saving to: ‘data/llama2.pdf’

data/llama2.pdf     100%\[>\]  59.23K  --.-KB/s    in 0.02s   

2023-11-08 22:20:12 (2.87 MB/s) - ‘data/llama2\_eval\_qr\_dataset.json’ saved \[60656/60656\]

In \[ \]:

Copied!

from llama\_index.core.evaluation import QueryResponseDataset

\# optional
eval\_dataset \= QueryResponseDataset.from\_json(
    "data/llama2\_eval\_qr\_dataset.json"
)

from llama\_index.core.evaluation import QueryResponseDataset # optional eval\_dataset = QueryResponseDataset.from\_json( "data/llama2\_eval\_qr\_dataset.json" )

#### Option 2: Generate New Dataset[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_retrieval_benchmark/#option-2-generate-new-dataset)

If you choose this option, you can choose to generate a new dataset from scratch. This allows you to play around with our `DatasetGenerator` settings to make sure it suits your needs.

In \[ \]:

Copied!

from llama\_index.core.evaluation import DatasetGenerator, QueryResponseDataset
from llama\_index.llms.openai import OpenAI

from llama\_index.core.evaluation import DatasetGenerator, QueryResponseDataset from llama\_index.llms.openai import OpenAI

In \[ \]:

Copied!

\# NOTE: run this if the dataset isn't already saved
\# Note: we only generate from the first 20 nodes, since the rest are references
llm \= OpenAI(model\="gpt-4-1106-preview")
dataset\_generator \= DatasetGenerator(
    nodes\[:20\],
    llm\=llm,
    show\_progress\=True,
    num\_questions\_per\_chunk\=3,
)
eval\_dataset \= await dataset\_generator.agenerate\_dataset\_from\_nodes(num\=60)
eval\_dataset.save\_json("data/llama2\_eval\_qr\_dataset.json")

\# NOTE: run this if the dataset isn't already saved # Note: we only generate from the first 20 nodes, since the rest are references llm = OpenAI(model="gpt-4-1106-preview") dataset\_generator = DatasetGenerator( nodes\[:20\], llm=llm, show\_progress=True, num\_questions\_per\_chunk=3, ) eval\_dataset = await dataset\_generator.agenerate\_dataset\_from\_nodes(num=60) eval\_dataset.save\_json("data/llama2\_eval\_qr\_dataset.json")

In \[ \]:

Copied!

\# optional
eval\_dataset \= QueryResponseDataset.from\_json(
    "data/llama2\_eval\_qr\_dataset.json"
)

\# optional eval\_dataset = QueryResponseDataset.from\_json( "data/llama2\_eval\_qr\_dataset.json" )

### Eval Modules[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_retrieval_benchmark/#eval-modules)

We define two evaluation modules: correctness and semantic similarity - both comparing quality of predicted response with actual response.

In \[ \]:

Copied!

from llama\_index.core.evaluation.eval\_utils import (
    get\_responses,
    get\_results\_df,
)
from llama\_index.core.evaluation import (
    CorrectnessEvaluator,
    SemanticSimilarityEvaluator,
    BatchEvalRunner,
)
from llama\_index.llms.openai import OpenAI

from llama\_index.core.evaluation.eval\_utils import ( get\_responses, get\_results\_df, ) from llama\_index.core.evaluation import ( CorrectnessEvaluator, SemanticSimilarityEvaluator, BatchEvalRunner, ) from llama\_index.llms.openai import OpenAI

In \[ \]:

Copied!

eval\_llm \= OpenAI(model\="gpt-4-1106-preview")
evaluator\_c \= CorrectnessEvaluator(llm\=eval\_llm)
evaluator\_s \= SemanticSimilarityEvaluator(llm\=eval\_llm)
evaluator\_dict \= {
    "correctness": evaluator\_c,
    "semantic\_similarity": evaluator\_s,
}
batch\_runner \= BatchEvalRunner(evaluator\_dict, workers\=2, show\_progress\=True)

eval\_llm = OpenAI(model="gpt-4-1106-preview") evaluator\_c = CorrectnessEvaluator(llm=eval\_llm) evaluator\_s = SemanticSimilarityEvaluator(llm=eval\_llm) evaluator\_dict = { "correctness": evaluator\_c, "semantic\_similarity": evaluator\_s, } batch\_runner = BatchEvalRunner(evaluator\_dict, workers=2, show\_progress=True)

In \[ \]:

Copied!

import numpy as np
import time
import os
import pickle
from tqdm import tqdm

def get\_responses\_sync(
    eval\_qs, query\_engine, show\_progress\=True, save\_path\=None
):
    if show\_progress:
        eval\_qs\_iter \= tqdm(eval\_qs)
    else:
        eval\_qs\_iter \= eval\_qs
    pred\_responses \= \[\]
    start\_time \= time.time()
    for eval\_q in eval\_qs\_iter:
        print(f"eval q: {eval\_q}")
        pred\_response \= agent.query(eval\_q)
        print(f"predicted response: {pred\_response}")
        pred\_responses.append(pred\_response)
        if save\_path is not None:
            \# save intermediate responses (to cache in case something breaks)
            avg\_time \= (time.time() \- start\_time) / len(pred\_responses)
            pickle.dump(
                {"pred\_responses": pred\_responses, "avg\_time": avg\_time},
                open(save\_path, "wb"),
            )
    return pred\_responses

async def run\_evals(
    query\_engine,
    eval\_qa\_pairs,
    batch\_runner,
    disable\_async\_for\_preds\=False,
    save\_path\=None,
):
    \# then evaluate
    \# TODO: evaluate a sample of generated results
    eval\_qs \= \[q for q, \_ in eval\_qa\_pairs\]
    eval\_answers \= \[a for \_, a in eval\_qa\_pairs\]

    if save\_path is not None:
        if not os.path.exists(save\_path):
            start\_time \= time.time()
            if disable\_async\_for\_preds:
                pred\_responses \= get\_responses\_sync(
                    eval\_qs,
                    query\_engine,
                    show\_progress\=True,
                    save\_path\=save\_path,
                )
            else:
                pred\_responses \= get\_responses(
                    eval\_qs, query\_engine, show\_progress\=True
                )
            avg\_time \= (time.time() \- start\_time) / len(eval\_qs)
            pickle.dump(
                {"pred\_responses": pred\_responses, "avg\_time": avg\_time},
                open(save\_path, "wb"),
            )
        else:
            \# \[optional\] load
            pickled\_dict \= pickle.load(open(save\_path, "rb"))
            pred\_responses \= pickled\_dict\["pred\_responses"\]
            avg\_time \= pickled\_dict\["avg\_time"\]
    else:
        start\_time \= time.time()
        pred\_responses \= get\_responses(
            eval\_qs, query\_engine, show\_progress\=True
        )
        avg\_time \= (time.time() \- start\_time) / len(eval\_qs)

    eval\_results \= await batch\_runner.aevaluate\_responses(
        eval\_qs, responses\=pred\_responses, reference\=eval\_answers
    )
    return eval\_results, {"avg\_time": avg\_time}

import numpy as np import time import os import pickle from tqdm import tqdm def get\_responses\_sync( eval\_qs, query\_engine, show\_progress=True, save\_path=None ): if show\_progress: eval\_qs\_iter = tqdm(eval\_qs) else: eval\_qs\_iter = eval\_qs pred\_responses = \[\] start\_time = time.time() for eval\_q in eval\_qs\_iter: print(f"eval q: {eval\_q}") pred\_response = agent.query(eval\_q) print(f"predicted response: {pred\_response}") pred\_responses.append(pred\_response) if save\_path is not None: # save intermediate responses (to cache in case something breaks) avg\_time = (time.time() - start\_time) / len(pred\_responses) pickle.dump( {"pred\_responses": pred\_responses, "avg\_time": avg\_time}, open(save\_path, "wb"), ) return pred\_responses async def run\_evals( query\_engine, eval\_qa\_pairs, batch\_runner, disable\_async\_for\_preds=False, save\_path=None, ): # then evaluate # TODO: evaluate a sample of generated results eval\_qs = \[q for q, \_ in eval\_qa\_pairs\] eval\_answers = \[a for \_, a in eval\_qa\_pairs\] if save\_path is not None: if not os.path.exists(save\_path): start\_time = time.time() if disable\_async\_for\_preds: pred\_responses = get\_responses\_sync( eval\_qs, query\_engine, show\_progress=True, save\_path=save\_path, ) else: pred\_responses = get\_responses( eval\_qs, query\_engine, show\_progress=True ) avg\_time = (time.time() - start\_time) / len(eval\_qs) pickle.dump( {"pred\_responses": pred\_responses, "avg\_time": avg\_time}, open(save\_path, "wb"), ) else: # \[optional\] load pickled\_dict = pickle.load(open(save\_path, "rb")) pred\_responses = pickled\_dict\["pred\_responses"\] avg\_time = pickled\_dict\["avg\_time"\] else: start\_time = time.time() pred\_responses = get\_responses( eval\_qs, query\_engine, show\_progress=True ) avg\_time = (time.time() - start\_time) / len(eval\_qs) eval\_results = await batch\_runner.aevaluate\_responses( eval\_qs, responses=pred\_responses, reference=eval\_answers ) return eval\_results, {"avg\_time": avg\_time}

Construct Assistant with Built-In Retrieval[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_retrieval_benchmark/#construct-assistant-with-built-in-retrieval)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Let's construct the assistant by also passing it the built-in OpenAI Retrieval tool.

Here, we upload and pass in the file during assistant-creation time.

In \[ \]:

Copied!

from llama\_index.agent.openai import OpenAIAssistantAgent

from llama\_index.agent.openai import OpenAIAssistantAgent

In \[ \]:

Copied!

agent \= OpenAIAssistantAgent.from\_new(
    name\="SEC Analyst",
    instructions\="You are a QA assistant designed to analyze sec filings.",
    openai\_tools\=\[{"type": "retrieval"}\],
    instructions\_prefix\="Please address the user as Jerry.",
    files\=\["data/llama2.pdf"\],
    verbose\=True,
)

agent = OpenAIAssistantAgent.from\_new( name="SEC Analyst", instructions="You are a QA assistant designed to analyze sec filings.", openai\_tools=\[{"type": "retrieval"}\], instructions\_prefix="Please address the user as Jerry.", files=\["data/llama2.pdf"\], verbose=True, )

In \[ \]:

Copied!

response \= agent.query(
    "What are the key differences between Llama 2 and Llama 2-Chat?"
)

response = agent.query( "What are the key differences between Llama 2 and Llama 2-Chat?" )

In \[ \]:

Copied!

print(str(response))

print(str(response))

The key differences between Llama 2 and Llama 2-Chat, as indicated by the document, focus on their performance in safety evaluations, particularly when tested with adversarial prompts. Here are some of the differences highlighted within the safety evaluation section of Llama 2-Chat:

1. Safety Human Evaluation: Llama 2-Chat was assessed with roughly 2000 adversarial prompts, among which 1351 were single-turn and 623 were multi-turn. The responses were judged for safety violations on a five-point Likert scale, where a rating of 1 or 2 indicated a violation. The evaluation aimed to gauge the model’s safety by its rate of generating responses with safety violations and its helpfulness to users.

2. Violation Percentage and Mean Rating: Llama 2-Chat exhibited a low overall violation percentage across different model sizes and a high mean rating for safety and helpfulness, which suggests a strong performance in safety evaluations.

3. Inter-Rater Reliability: The reliability of the safety assessments was measured using Gwet’s AC1/2 statistic, showing a high degree of agreement among annotators with an average inter-rater reliability score of 0.92 for Llama 2-Chat annotations.

4. Single-turn and Multi-turn Conversations: The evaluation revealed that multi-turn conversations generally lead to more safety violations across models, but Llama 2-Chat performed well compared to baselines, particularly in multi-turn scenarios.

5. Violation Percentage Per Risk Category: Llama 2-Chat had a relatively higher number of violations in the unqualified advice category, possibly due to a lack of appropriate disclaimers in its responses.

6. Improvements in Fine-Tuned Llama 2-Chat: The document also mentions that the fine-tuned Llama 2-Chat showed significant improvement over the pre-trained Llama 2 in terms of truthfulness and toxicity. The percentage of toxic generations dropped to effectively 0% for Llama 2-Chat of all sizes, which was the lowest among all compared models, indicating a notable enhancement in safety.

These points detail the evaluations and improvements emphasizing safety that distinguish Llama 2-Chat from Llama 2【9†source】.

Benchmark[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_retrieval_benchmark/#benchmark)
-------------------------------------------------------------------------------------------------------

We run the agent over our evaluation dataset. We benchmark against a standard top-k RAG pipeline (k=2) with gpt-4-turbo.

**NOTE**: During our time of testing (November 2023), the Assistant API is heavily rate-limited, and can take ~1-2 hours to generate responses over 60 datapoints.

#### Define Baseline Index + RAG Pipeline[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_retrieval_benchmark/#define-baseline-index-rag-pipeline)

In \[ \]:

Copied!

llm \= OpenAI(model\="gpt-4-1106-preview")
base\_index \= VectorStoreIndex(nodes)
base\_query\_engine \= base\_index.as\_query\_engine(similarity\_top\_k\=2, llm\=llm)

llm = OpenAI(model="gpt-4-1106-preview") base\_index = VectorStoreIndex(nodes) base\_query\_engine = base\_index.as\_query\_engine(similarity\_top\_k=2, llm=llm)

#### Run Evals over Baseline[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_retrieval_benchmark/#run-evals-over-baseline)

In \[ \]:

Copied!

base\_eval\_results, base\_extra\_info \= await run\_evals(
    base\_query\_engine,
    eval\_dataset.qr\_pairs,
    batch\_runner,
    save\_path\="data/llama2\_preds\_base.pkl",
)

base\_eval\_results, base\_extra\_info = await run\_evals( base\_query\_engine, eval\_dataset.qr\_pairs, batch\_runner, save\_path="data/llama2\_preds\_base.pkl", )

In \[ \]:

Copied!

results\_df \= get\_results\_df(
    \[base\_eval\_results\],
    \["Base Query Engine"\],
    \["correctness", "semantic\_similarity"\],
)
display(results\_df)

results\_df = get\_results\_df( \[base\_eval\_results\], \["Base Query Engine"\], \["correctness", "semantic\_similarity"\], ) display(results\_df)

|  | names | correctness | semantic\_similarity |
| --- | --- | --- | --- |
| 0 | Base Query Engine | 4.05 | 0.964245 |

#### Run Evals over Assistant API[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_retrieval_benchmark/#run-evals-over-assistant-api)

In \[ \]:

Copied!

assistant\_eval\_results, assistant\_extra\_info \= await run\_evals(
    agent,
    eval\_dataset.qr\_pairs\[:55\],
    batch\_runner,
    save\_path\="data/llama2\_preds\_assistant.pkl",
    disable\_async\_for\_preds\=True,
)

assistant\_eval\_results, assistant\_extra\_info = await run\_evals( agent, eval\_dataset.qr\_pairs\[:55\], batch\_runner, save\_path="data/llama2\_preds\_assistant.pkl", disable\_async\_for\_preds=True, )

#### Get Results[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_retrieval_benchmark/#get-results)

Here we see...that our basic RAG pipeline does better.

Take these numbers with a grain of salt. The goal here is to give you a script so you can run this on your own data.

That said it's surprising the Retrieval API doesn't give immediately better out of the box performance.

In \[ \]:

Copied!

results\_df \= get\_results\_df(
    \[assistant\_eval\_results, base\_eval\_results\],
    \["Retrieval API", "Base Query Engine"\],
    \["correctness", "semantic\_similarity"\],
)
display(results\_df)
print(f"Base Avg Time: {base\_extra\_info\['avg\_time'\]}")
print(f"Assistant Avg Time: {assistant\_extra\_info\['avg\_time'\]}")

results\_df = get\_results\_df( \[assistant\_eval\_results, base\_eval\_results\], \["Retrieval API", "Base Query Engine"\], \["correctness", "semantic\_similarity"\], ) display(results\_df) print(f"Base Avg Time: {base\_extra\_info\['avg\_time'\]}") print(f"Assistant Avg Time: {assistant\_extra\_info\['avg\_time'\]}")

|  | names | correctness | semantic\_similarity |
| --- | --- | --- | --- |
| 0 | Retrieval API | 3.536364 | 0.952647 |
| 1 | Base Query Engine | 4.050000 | 0.964245 |

Base Avg Time: 0.25683316787083943
Assistant Avg Time: 75.43605598536405

Back to top

[Previous OpenAI agent: specifying a forced function call](https://docs.llamaindex.ai/en/stable/examples/agent/openai_forced_function_call/)[Next ReAct Agent - A Simple Intro with Calculator Tools](https://docs.llamaindex.ai/en/stable/examples/agent/react_agent/)

Hi, how can I help you?

🦙
