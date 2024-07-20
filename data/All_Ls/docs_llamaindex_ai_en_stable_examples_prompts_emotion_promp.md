Title: EmotionPrompt in RAG - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/prompts/emotion_prompt/

Markdown Content:
EmotionPrompt in RAG - LlamaIndex


Inspired by the "[Large Language Models Understand and Can Be Enhanced by Emotional Stimuli](https://arxiv.org/pdf/2307.11760.pdf)" by Li et al., in this guide we show you how to evaluate the effects of emotional stimuli on your RAG pipeline:

1.  Setup the RAG pipeline with a basic vector index with the core QA template.
2.  Create some candidate stimuli (inspired by Fig. 2 of the paper)
3.  For each candidate stimulit, prepend to QA prompt and evaluate.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai
%pip install llama\-index\-readers\-file pymupdf

%pip install llama-index-llms-openai %pip install llama-index-readers-file pymupdf

In \[ \]:

Copied!

import nest\_asyncio

nest\_asyncio.apply()

import nest\_asyncio nest\_asyncio.apply()

Setup Data[¶](https://docs.llamaindex.ai/en/stable/examples/prompts/emotion_prompt/#setup-data)
-----------------------------------------------------------------------------------------------

We use the Llama 2 paper as the input data source for our RAG pipeline.

In \[ \]:

Copied!

!mkdir data && wget \--user\-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" \-O "data/llama2.pdf"

!mkdir data && wget --user-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" -O "data/llama2.pdf"

mkdir: data: File exists

In \[ \]:

Copied!

from pathlib import Path
from llama\_index.readers.file import PyMuPDFReader
from llama\_index.core import Document
from llama\_index.core.node\_parser import SentenceSplitter
from llama\_index.core.schema import IndexNode

from pathlib import Path from llama\_index.readers.file import PyMuPDFReader from llama\_index.core import Document from llama\_index.core.node\_parser import SentenceSplitter from llama\_index.core.schema import IndexNode

In \[ \]:

Copied!

docs0 \= PyMuPDFReader().load(file\_path\=Path("./data/llama2.pdf"))
doc\_text \= "\\n\\n".join(\[d.get\_content() for d in docs0\])
docs \= \[Document(text\=doc\_text)\]
node\_parser \= SentenceSplitter(chunk\_size\=1024)
base\_nodes \= node\_parser.get\_nodes\_from\_documents(docs)

docs0 = PyMuPDFReader().load(file\_path=Path("./data/llama2.pdf")) doc\_text = "\\n\\n".join(\[d.get\_content() for d in docs0\]) docs = \[Document(text=doc\_text)\] node\_parser = SentenceSplitter(chunk\_size=1024) base\_nodes = node\_parser.get\_nodes\_from\_documents(docs)

Setup Vector Index over this Data[¶](https://docs.llamaindex.ai/en/stable/examples/prompts/emotion_prompt/#setup-vector-index-over-this-data)
---------------------------------------------------------------------------------------------------------------------------------------------

We load this data into an in-memory vector store (embedded with OpenAI embeddings).

We'll be aggressively optimizing the QA prompt for this RAG pipeline.

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex
from llama\_index.llms.openai import OpenAI
from llama\_index.core import Settings

Settings.llm \= OpenAI(model\="gpt-3.5-turbo")

from llama\_index.core import VectorStoreIndex from llama\_index.llms.openai import OpenAI from llama\_index.core import Settings Settings.llm = OpenAI(model="gpt-3.5-turbo")

In \[ \]:

Copied!

index \= VectorStoreIndex(base\_nodes)

query\_engine \= index.as\_query\_engine(similarity\_top\_k\=2)

index = VectorStoreIndex(base\_nodes) query\_engine = index.as\_query\_engine(similarity\_top\_k=2)

Evaluation Setup[¶](https://docs.llamaindex.ai/en/stable/examples/prompts/emotion_prompt/#evaluation-setup)
-----------------------------------------------------------------------------------------------------------

#### Golden Dataset[¶](https://docs.llamaindex.ai/en/stable/examples/prompts/emotion_prompt/#golden-dataset)

Here we load in a "golden" dataset.

**NOTE**: We pull this in from Dropbox. For details on how to generate a dataset please see our `DatasetGenerator` module.

In \[ \]:

Copied!

!wget "https://www.dropbox.com/scl/fi/fh9vsmmm8vu0j50l3ss38/llama2\_eval\_qr\_dataset.json?rlkey=kkoaez7aqeb4z25gzc06ak6kb&dl=1" \-O data/llama2\_eval\_qr\_dataset.json

!wget "https://www.dropbox.com/scl/fi/fh9vsmmm8vu0j50l3ss38/llama2\_eval\_qr\_dataset.json?rlkey=kkoaez7aqeb4z25gzc06ak6kb&dl=1" -O data/llama2\_eval\_qr\_dataset.json

\--2023-11-04 00:34:09--  https://www.dropbox.com/scl/fi/fh9vsmmm8vu0j50l3ss38/llama2\_eval\_qr\_dataset.json?rlkey=kkoaez7aqeb4z25gzc06ak6kb&dl=1
Resolving www.dropbox.com (www.dropbox.com)... 2620:100:6017:18::a27d:212, 162.125.2.18
Connecting to www.dropbox.com (www.dropbox.com)|2620:100:6017:18::a27d:212|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://uc68b925272ee59de768b72ea323.dl.dropboxusercontent.com/cd/0/inline/CG4XGYSusXrgPle6I3vucuwf-NIN10QWldJ7wlc3wdzYWbv9OQey0tvB4qGxJ5W0BxL7cX-zn7Kxj5QReEbi1RNYOx1XMT9qwgMm2xWjW5a9seqV4AI8V7C0M2plvH5U1Yw/file?dl=1# \[following\]
--2023-11-04 00:34:09--  https://uc68b925272ee59de768b72ea323.dl.dropboxusercontent.com/cd/0/inline/CG4XGYSusXrgPle6I3vucuwf-NIN10QWldJ7wlc3wdzYWbv9OQey0tvB4qGxJ5W0BxL7cX-zn7Kxj5QReEbi1RNYOx1XMT9qwgMm2xWjW5a9seqV4AI8V7C0M2plvH5U1Yw/file?dl=1
Resolving uc68b925272ee59de768b72ea323.dl.dropboxusercontent.com (uc68b925272ee59de768b72ea323.dl.dropboxusercontent.com)... 2620:100:6017:15::a27d:20f, 162.125.2.15
Connecting to uc68b925272ee59de768b72ea323.dl.dropboxusercontent.com (uc68b925272ee59de768b72ea323.dl.dropboxusercontent.com)|2620:100:6017:15::a27d:20f|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 60656 (59K) \[application/binary\]
Saving to: ‘data/llama2\_eval\_qr\_dataset.json’

data/llama2\_eval\_qr 100%\[>\]  59.23K  --.-KB/s    in 0.04s   

2023-11-04 00:34:10 (1.48 MB/s) - ‘data/llama2\_eval\_qr\_dataset.json’ saved \[60656/60656\]

In \[ \]:

Copied!

from llama\_index.core.evaluation import QueryResponseDataset

from llama\_index.core.evaluation import QueryResponseDataset

In \[ \]:

Copied!

\# optional
eval\_dataset \= QueryResponseDataset.from\_json(
    "data/llama2\_eval\_qr\_dataset.json"
)

\# optional eval\_dataset = QueryResponseDataset.from\_json( "data/llama2\_eval\_qr\_dataset.json" )

#### Get Evaluator[¶](https://docs.llamaindex.ai/en/stable/examples/prompts/emotion_prompt/#get-evaluator)

In \[ \]:

Copied!

from llama\_index.core.evaluation.eval\_utils import get\_responses

from llama\_index.core.evaluation.eval\_utils import get\_responses

In \[ \]:

Copied!

from llama\_index.core.evaluation import CorrectnessEvaluator, BatchEvalRunner

evaluator\_c \= CorrectnessEvaluator()
evaluator\_dict \= {"correctness": evaluator\_c}
batch\_runner \= BatchEvalRunner(evaluator\_dict, workers\=2, show\_progress\=True)

from llama\_index.core.evaluation import CorrectnessEvaluator, BatchEvalRunner evaluator\_c = CorrectnessEvaluator() evaluator\_dict = {"correctness": evaluator\_c} batch\_runner = BatchEvalRunner(evaluator\_dict, workers=2, show\_progress=True)

#### Define Correctness Eval Function[¶](https://docs.llamaindex.ai/en/stable/examples/prompts/emotion_prompt/#define-correctness-eval-function)

In \[ \]:

Copied!

import numpy as np

async def get\_correctness(query\_engine, eval\_qa\_pairs, batch\_runner):
    \# then evaluate
    \# TODO: evaluate a sample of generated results
    eval\_qs \= \[q for q, \_ in eval\_qa\_pairs\]
    eval\_answers \= \[a for \_, a in eval\_qa\_pairs\]
    pred\_responses \= get\_responses(eval\_qs, query\_engine, show\_progress\=True)

    eval\_results \= await batch\_runner.aevaluate\_responses(
        eval\_qs, responses\=pred\_responses, reference\=eval\_answers
    )
    avg\_correctness \= np.array(
        \[r.score for r in eval\_results\["correctness"\]\]
    ).mean()
    return avg\_correctness

import numpy as np async def get\_correctness(query\_engine, eval\_qa\_pairs, batch\_runner): # then evaluate # TODO: evaluate a sample of generated results eval\_qs = \[q for q, \_ in eval\_qa\_pairs\] eval\_answers = \[a for \_, a in eval\_qa\_pairs\] pred\_responses = get\_responses(eval\_qs, query\_engine, show\_progress=True) eval\_results = await batch\_runner.aevaluate\_responses( eval\_qs, responses=pred\_responses, reference=eval\_answers ) avg\_correctness = np.array( \[r.score for r in eval\_results\["correctness"\]\] ).mean() return avg\_correctness

Try Out Emotion Prompts[¶](https://docs.llamaindex.ai/en/stable/examples/prompts/emotion_prompt/#try-out-emotion-prompts)
-------------------------------------------------------------------------------------------------------------------------

We pul some emotion stimuli from the paper to try out.

In \[ \]:

Copied!

emotion\_stimuli\_dict \= {
    "ep01": "Write your answer and give me a confidence score between 0-1 for your answer. ",
    "ep02": "This is very important to my career. ",
    "ep03": "You'd better be sure.",
    \# add more from the paper here!!
}

\# NOTE: ep06 is the combination of ep01, ep02, ep03
emotion\_stimuli\_dict\["ep06"\] \= (
    emotion\_stimuli\_dict\["ep01"\]
    + emotion\_stimuli\_dict\["ep02"\]
    + emotion\_stimuli\_dict\["ep03"\]
)

emotion\_stimuli\_dict = { "ep01": "Write your answer and give me a confidence score between 0-1 for your answer. ", "ep02": "This is very important to my career. ", "ep03": "You'd better be sure.", # add more from the paper here!! } # NOTE: ep06 is the combination of ep01, ep02, ep03 emotion\_stimuli\_dict\["ep06"\] = ( emotion\_stimuli\_dict\["ep01"\] + emotion\_stimuli\_dict\["ep02"\] + emotion\_stimuli\_dict\["ep03"\] )

#### Initialize base QA Prompt[¶](https://docs.llamaindex.ai/en/stable/examples/prompts/emotion_prompt/#initialize-base-qa-prompt)

In \[ \]:

Copied!

QA\_PROMPT\_KEY \= "response\_synthesizer:text\_qa\_template"

QA\_PROMPT\_KEY = "response\_synthesizer:text\_qa\_template"

In \[ \]:

Copied!

from llama\_index.core import PromptTemplate

from llama\_index.core import PromptTemplate

In \[ \]:

Copied!

qa\_tmpl\_str \= """\\
Context information is below. 
\---------------------
{context\_str}
\---------------------
Given the context information and not prior knowledge, \\
answer the query.
{emotion\_str}
Query: {query\_str}
Answer: \\
"""
qa\_tmpl \= PromptTemplate(qa\_tmpl\_str)

qa\_tmpl\_str = """\\ Context information is below. --------------------- {context\_str} --------------------- Given the context information and not prior knowledge, \\ answer the query. {emotion\_str} Query: {query\_str} Answer: \\ """ qa\_tmpl = PromptTemplate(qa\_tmpl\_str)

#### Prepend emotions[¶](https://docs.llamaindex.ai/en/stable/examples/prompts/emotion_prompt/#prepend-emotions)

In \[ \]:

Copied!

async def run\_and\_evaluate(
    query\_engine, eval\_qa\_pairs, batch\_runner, emotion\_stimuli\_str, qa\_tmpl
):
    """Run and evaluate."""
    new\_qa\_tmpl \= qa\_tmpl.partial\_format(emotion\_str\=emotion\_stimuli\_str)

    old\_qa\_tmpl \= query\_engine.get\_prompts()\[QA\_PROMPT\_KEY\]
    query\_engine.update\_prompts({QA\_PROMPT\_KEY: new\_qa\_tmpl})
    avg\_correctness \= await get\_correctness(
        query\_engine, eval\_qa\_pairs, batch\_runner
    )
    query\_engine.update\_prompts({QA\_PROMPT\_KEY: old\_qa\_tmpl})
    return avg\_correctness

async def run\_and\_evaluate( query\_engine, eval\_qa\_pairs, batch\_runner, emotion\_stimuli\_str, qa\_tmpl ): """Run and evaluate.""" new\_qa\_tmpl = qa\_tmpl.partial\_format(emotion\_str=emotion\_stimuli\_str) old\_qa\_tmpl = query\_engine.get\_prompts()\[QA\_PROMPT\_KEY\] query\_engine.update\_prompts({QA\_PROMPT\_KEY: new\_qa\_tmpl}) avg\_correctness = await get\_correctness( query\_engine, eval\_qa\_pairs, batch\_runner ) query\_engine.update\_prompts({QA\_PROMPT\_KEY: old\_qa\_tmpl}) return avg\_correctness

In \[ \]:

Copied!

\# try out ep01
correctness\_ep01 \= await run\_and\_evaluate(
    query\_engine,
    eval\_dataset.qr\_pairs,
    batch\_runner,
    emotion\_stimuli\_dict\["ep01"\],
    qa\_tmpl,
)

\# try out ep01 correctness\_ep01 = await run\_and\_evaluate( query\_engine, eval\_dataset.qr\_pairs, batch\_runner, emotion\_stimuli\_dict\["ep01"\], qa\_tmpl, )

100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 60/60 \[00:10<00:00,  5.48it/s\]
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 60/60 \[01:23<00:00,  1.39s/it\]

In \[ \]:

Copied!

print(correctness\_ep01)

print(correctness\_ep01)

3.7916666666666665

In \[ \]:

Copied!

\# try out ep02
correctness\_ep02 \= await run\_and\_evaluate(
    query\_engine,
    eval\_dataset.qr\_pairs,
    batch\_runner,
    emotion\_stimuli\_dict\["ep02"\],
    qa\_tmpl,
)

\# try out ep02 correctness\_ep02 = await run\_and\_evaluate( query\_engine, eval\_dataset.qr\_pairs, batch\_runner, emotion\_stimuli\_dict\["ep02"\], qa\_tmpl, )

100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 60/60 \[00:10<00:00,  5.62it/s\]
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 60/60 \[01:21<00:00,  1.36s/it\]
/var/folders/1r/c3h91d9s49xblwfvz79s78\_c0000gn/T/ipykernel\_80474/3350915737.py:2: RuntimeWarning: coroutine 'run\_and\_evaluate' was never awaited
  correctness\_ep02 = await run\_and\_evaluate(
RuntimeWarning: Enable tracemalloc to get the object allocation traceback

In \[ \]:

Copied!

print(correctness\_ep02)

print(correctness\_ep02)

3.941666666666667

In \[ \]:

Copied!

\# try none
correctness\_base \= await run\_and\_evaluate(
    query\_engine, eval\_dataset.qr\_pairs, batch\_runner, "", qa\_tmpl
)

\# try none correctness\_base = await run\_and\_evaluate( query\_engine, eval\_dataset.qr\_pairs, batch\_runner, "", qa\_tmpl )

100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 60/60 \[00:12<00:00,  4.92it/s\]
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 60/60 \[01:59<00:00,  2.00s/it\]
/var/folders/1r/c3h91d9s49xblwfvz79s78\_c0000gn/T/ipykernel\_80474/997505056.py:2: RuntimeWarning: coroutine 'run\_and\_evaluate' was never awaited
  correctness\_base = await run\_and\_evaluate(
RuntimeWarning: Enable tracemalloc to get the object allocation traceback

In \[ \]:

Copied!

print(correctness\_base)

print(correctness\_base)

3.8916666666666666

Back to top

[Previous Advanced Prompt Techniques (Variable Mappings, Functions)](https://docs.llamaindex.ai/en/stable/examples/prompts/advanced_prompts/)[Next Accessing/Customizing Prompts within Higher-Level Modules](https://docs.llamaindex.ai/en/stable/examples/prompts/prompt_mixin/)

Hi, how can I help you?

🦙
