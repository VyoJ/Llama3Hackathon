Title: "Optimization by Prompting" for RAG

URL Source: https://docs.llamaindex.ai/en/stable/examples/prompts/prompt_optimization/

Markdown Content:
"Optimization by Prompting" for RAG - LlamaIndex


Inspired by the [Optimization by Prompting paper](https://arxiv.org/pdf/2309.03409.pdf) by Yang et al., in this guide we test the ability of a "meta-prompt" to optimize our prompt for better RAG performance. The process is roughly as follows:

1.  The prompt to be optimized is our standard QA prompt template for RAG, specifically the instruction prefix.
2.  We have a "meta-prompt" that takes in previous prefixes/scores + an example of the task, and spits out another prefix.
3.  For every candidate prefix, we compute a "score" through correctness evaluation - comparing a dataset of predicted answers (using the QA prompt) to a candidate dataset. If you don't have it already, you can generate with GPT-4.

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

Setup Data[¶](https://docs.llamaindex.ai/en/stable/examples/prompts/prompt_optimization/#setup-data)
----------------------------------------------------------------------------------------------------

We use the Llama 2 paper as the input data source for our RAG pipeline.

In \[ \]:

Copied!

!mkdir data && wget \--user\-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" \-O "data/llama2.pdf"

!mkdir data && wget --user-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" -O "data/llama2.pdf"

mkdir: data: File exists

In \[ \]:

Copied!

from pathlib import Path
from llama\_index.readers.file import PDFReader
from llama\_index.readers.file import UnstructuredReader
from llama\_index.readers.file import PyMuPDFReader

from pathlib import Path from llama\_index.readers.file import PDFReader from llama\_index.readers.file import UnstructuredReader from llama\_index.readers.file import PyMuPDFReader

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

base\_nodes = node\_parser.get\_nodes\_from\_documents(docs)

Setup Vector Index over this Data[¶](https://docs.llamaindex.ai/en/stable/examples/prompts/prompt_optimization/#setup-vector-index-over-this-data)
--------------------------------------------------------------------------------------------------------------------------------------------------

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

Get "Golden" Dataset[¶](https://docs.llamaindex.ai/en/stable/examples/prompts/prompt_optimization/#get-golden-dataset)
----------------------------------------------------------------------------------------------------------------------

Here we generate a dataset of ground-truth QA pairs (or load it).

This will be used for two purposes:

1.  To generate some exemplars that we can put into the meta-prompt to illustrate the task
2.  To generate an evaluation dataset to compute our objective score - so that the meta-prompt can try optimizing for this score.

In \[ \]:

Copied!

from llama\_index.core.evaluation import DatasetGenerator, QueryResponseDataset
from llama\_index.core.node\_parser import SimpleNodeParser

from llama\_index.core.evaluation import DatasetGenerator, QueryResponseDataset from llama\_index.core.node\_parser import SimpleNodeParser

In \[ \]:

Copied!

dataset\_generator \= DatasetGenerator(
    base\_nodes\[:20\],
    llm\=OpenAI(model\="gpt-4"),
    show\_progress\=True,
    num\_questions\_per\_chunk\=3,
)

dataset\_generator = DatasetGenerator( base\_nodes\[:20\], llm=OpenAI(model="gpt-4"), show\_progress=True, num\_questions\_per\_chunk=3, )

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

#### Get Dataset Samples[¶](https://docs.llamaindex.ai/en/stable/examples/prompts/prompt_optimization/#get-dataset-samples)

In \[ \]:

Copied!

import random

full\_qr\_pairs \= eval\_dataset.qr\_pairs

import random full\_qr\_pairs = eval\_dataset.qr\_pairs

In \[ \]:

Copied!

num\_exemplars \= 2
num\_eval \= 40
exemplar\_qr\_pairs \= random.sample(full\_qr\_pairs, num\_exemplars)

eval\_qr\_pairs \= random.sample(full\_qr\_pairs, num\_eval)

num\_exemplars = 2 num\_eval = 40 exemplar\_qr\_pairs = random.sample(full\_qr\_pairs, num\_exemplars) eval\_qr\_pairs = random.sample(full\_qr\_pairs, num\_eval)

In \[ \]:

Copied!

len(exemplar\_qr\_pairs)

len(exemplar\_qr\_pairs)

Out\[ \]:

2

Do Prompt Optimization[¶](https://docs.llamaindex.ai/en/stable/examples/prompts/prompt_optimization/#do-prompt-optimization)
----------------------------------------------------------------------------------------------------------------------------

We now define the functions needed for prompt optimization. We first define an evaluator, and then we setup the meta-prompt which produces candidate instruction prefixes.

Finally we define and run the prompt optimization loop.

#### Get Evaluator[¶](https://docs.llamaindex.ai/en/stable/examples/prompts/prompt_optimization/#get-evaluator)

In \[ \]:

Copied!

from llama\_index.core.evaluation.eval\_utils import get\_responses

from llama\_index.core.evaluation.eval\_utils import get\_responses

In \[ \]:

Copied!

from llama\_index.core.evaluation import CorrectnessEvaluator, BatchEvalRunner

evaluator\_c \= CorrectnessEvaluator(llm\=OpenAI(model\="gpt-3.5-turbo"))
evaluator\_dict \= {
    "correctness": evaluator\_c,
}
batch\_runner \= BatchEvalRunner(evaluator\_dict, workers\=2, show\_progress\=True)

from llama\_index.core.evaluation import CorrectnessEvaluator, BatchEvalRunner evaluator\_c = CorrectnessEvaluator(llm=OpenAI(model="gpt-3.5-turbo")) evaluator\_dict = { "correctness": evaluator\_c, } batch\_runner = BatchEvalRunner(evaluator\_dict, workers=2, show\_progress=True)

#### Define Correctness Eval Function[¶](https://docs.llamaindex.ai/en/stable/examples/prompts/prompt_optimization/#define-correctness-eval-function)

In \[ \]:

Copied!

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

async def get\_correctness(query\_engine, eval\_qa\_pairs, batch\_runner): # then evaluate # TODO: evaluate a sample of generated results eval\_qs = \[q for q, \_ in eval\_qa\_pairs\] eval\_answers = \[a for \_, a in eval\_qa\_pairs\] pred\_responses = get\_responses(eval\_qs, query\_engine, show\_progress=True) eval\_results = await batch\_runner.aevaluate\_responses( eval\_qs, responses=pred\_responses, reference=eval\_answers ) avg\_correctness = np.array( \[r.score for r in eval\_results\["correctness"\]\] ).mean() return avg\_correctness

#### Initialize base QA Prompt[¶](https://docs.llamaindex.ai/en/stable/examples/prompts/prompt_optimization/#initialize-base-qa-prompt)

In \[ \]:

Copied!

QA\_PROMPT\_KEY \= "response\_synthesizer:text\_qa\_template"

QA\_PROMPT\_KEY = "response\_synthesizer:text\_qa\_template"

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI
from llama\_index.core import PromptTemplate

llm \= OpenAI(model\="gpt-3.5-turbo")

from llama\_index.llms.openai import OpenAI from llama\_index.core import PromptTemplate llm = OpenAI(model="gpt-3.5-turbo")

In \[ \]:

Copied!

qa\_tmpl\_str \= (
    "---------------------\\n"
    "{context\_str}\\n"
    "---------------------\\n"
    "Query: {query\_str}\\n"
    "Answer: "
)
qa\_tmpl \= PromptTemplate(qa\_tmpl\_str)

qa\_tmpl\_str = ( "---------------------\\n" "{context\_str}\\n" "---------------------\\n" "Query: {query\_str}\\n" "Answer: " ) qa\_tmpl = PromptTemplate(qa\_tmpl\_str)

In \[ \]:

Copied!

print(query\_engine.get\_prompts()\[QA\_PROMPT\_KEY\].get\_template())

print(query\_engine.get\_prompts()\[QA\_PROMPT\_KEY\].get\_template())

#### Define Meta-Prompt[¶](https://docs.llamaindex.ai/en/stable/examples/prompts/prompt_optimization/#define-meta-prompt)

In \[ \]:

Copied!

meta\_tmpl\_str \= """\\
Your task is to generate the instruction <INS>. Below are some previous instructions with their scores.
The score ranges from 1 to 5.

{prev\_instruction\_score\_pairs}

Below we show the task. The <INS> tag is prepended to the below prompt template, e.g. as follows:

\`\`\`
<INS>
{prompt\_tmpl\_str}
\`\`\`

The prompt template contains template variables. Given an input set of template variables, the formatted prompt is then given to an LLM to get an output.

Some examples of template variable inputs and expected outputs are given below to illustrate the task. \*\*NOTE\*\*: These do NOT represent the \\
entire evaluation dataset.

{qa\_pairs\_str}

We run every input in an evaluation dataset through an LLM. If the LLM-generated output doesn't match the expected output, we mark it as wrong (score 0).
A correct answer has a score of 1. The final "score" for an instruction is the average of scores across an evaluation dataset.
Write your new instruction (<INS>) that is different from the old ones and has a score as high as possible.

Instruction (<INS>): \\
"""

meta\_tmpl \= PromptTemplate(meta\_tmpl\_str)

meta\_tmpl\_str = """\\ Your task is to generate the instruction . Below are some previous instructions with their scores. The score ranges from 1 to 5. {prev\_instruction\_score\_pairs} Below we show the task. The tag is prepended to the below prompt template, e.g. as follows: \`\`\` {prompt\_tmpl\_str} \`\`\` The prompt template contains template variables. Given an input set of template variables, the formatted prompt is then given to an LLM to get an output. Some examples of template variable inputs and expected outputs are given below to illustrate the task. \*\*NOTE\*\*: These do NOT represent the \\ entire evaluation dataset. {qa\_pairs\_str} We run every input in an evaluation dataset through an LLM. If the LLM-generated output doesn't match the expected output, we mark it as wrong (score 0). A correct answer has a score of 1. The final "score" for an instruction is the average of scores across an evaluation dataset. Write your new instruction () that is different from the old ones and has a score as high as possible. Instruction (): \\ """ meta\_tmpl = PromptTemplate(meta\_tmpl\_str)

#### Define Prompt Optimization Functions[¶](https://docs.llamaindex.ai/en/stable/examples/prompts/prompt_optimization/#define-prompt-optimization-functions)

In \[ \]:

Copied!

from copy import deepcopy

def format\_meta\_tmpl(
    prev\_instr\_score\_pairs,
    prompt\_tmpl\_str,
    qa\_pairs,
    meta\_tmpl,
):
    """Call meta-prompt to generate new instruction."""
    \# format prev instruction score pairs.
    pair\_str\_list \= \[
        f"Instruction (<INS>):\\n{instr}\\nScore:\\n{score}"
        for instr, score in prev\_instr\_score\_pairs
    \]
    full\_instr\_pair\_str \= "\\n\\n".join(pair\_str\_list)

    \# now show QA pairs with ground-truth answers
    qa\_str\_list \= \[
        f"query\_str:\\n{query\_str}\\nAnswer:\\n{answer}"
        for query\_str, answer in qa\_pairs
    \]
    full\_qa\_pair\_str \= "\\n\\n".join(qa\_str\_list)

    fmt\_meta\_tmpl \= meta\_tmpl.format(
        prev\_instruction\_score\_pairs\=full\_instr\_pair\_str,
        prompt\_tmpl\_str\=prompt\_tmpl\_str,
        qa\_pairs\_str\=full\_qa\_pair\_str,
    )
    return fmt\_meta\_tmpl

from copy import deepcopy def format\_meta\_tmpl( prev\_instr\_score\_pairs, prompt\_tmpl\_str, qa\_pairs, meta\_tmpl, ): """Call meta-prompt to generate new instruction.""" # format prev instruction score pairs. pair\_str\_list = \[ f"Instruction ():\\n{instr}\\nScore:\\n{score}" for instr, score in prev\_instr\_score\_pairs \] full\_instr\_pair\_str = "\\n\\n".join(pair\_str\_list) # now show QA pairs with ground-truth answers qa\_str\_list = \[ f"query\_str:\\n{query\_str}\\nAnswer:\\n{answer}" for query\_str, answer in qa\_pairs \] full\_qa\_pair\_str = "\\n\\n".join(qa\_str\_list) fmt\_meta\_tmpl = meta\_tmpl.format( prev\_instruction\_score\_pairs=full\_instr\_pair\_str, prompt\_tmpl\_str=prompt\_tmpl\_str, qa\_pairs\_str=full\_qa\_pair\_str, ) return fmt\_meta\_tmpl

In \[ \]:

Copied!

def get\_full\_prompt\_template(cur\_instr: str, prompt\_tmpl):
    tmpl\_str \= prompt\_tmpl.get\_template()
    new\_tmpl\_str \= cur\_instr + "\\n" + tmpl\_str
    new\_tmpl \= PromptTemplate(new\_tmpl\_str)
    return new\_tmpl

def get\_full\_prompt\_template(cur\_instr: str, prompt\_tmpl): tmpl\_str = prompt\_tmpl.get\_template() new\_tmpl\_str = cur\_instr + "\\n" + tmpl\_str new\_tmpl = PromptTemplate(new\_tmpl\_str) return new\_tmpl

In \[ \]:

Copied!

import numpy as np

def \_parse\_meta\_response(meta\_response: str):
    return str(meta\_response).split("\\n")\[0\]

async def optimize\_prompts(
    query\_engine,
    initial\_instr: str,
    base\_prompt\_tmpl,
    meta\_tmpl,
    meta\_llm,
    batch\_eval\_runner,
    eval\_qa\_pairs,
    exemplar\_qa\_pairs,
    num\_iterations: int \= 5,
):
    prev\_instr\_score\_pairs \= \[\]
    base\_prompt\_tmpl\_str \= base\_prompt\_tmpl.get\_template()

    cur\_instr \= initial\_instr
    for idx in range(num\_iterations):
        \# TODO: change from -1 to 0
        if idx \> 0:
            \# first generate
            fmt\_meta\_tmpl \= format\_meta\_tmpl(
                prev\_instr\_score\_pairs,
                base\_prompt\_tmpl\_str,
                exemplar\_qa\_pairs,
                meta\_tmpl,
            )
            meta\_response \= meta\_llm.complete(fmt\_meta\_tmpl)
            print(fmt\_meta\_tmpl)
            print(str(meta\_response))
            \# Parse meta response
            cur\_instr \= \_parse\_meta\_response(meta\_response)

        \# append instruction to template
        new\_prompt\_tmpl \= get\_full\_prompt\_template(cur\_instr, base\_prompt\_tmpl)
        query\_engine.update\_prompts({QA\_PROMPT\_KEY: new\_prompt\_tmpl})

        avg\_correctness \= await get\_correctness(
            query\_engine, eval\_qa\_pairs, batch\_runner
        )
        prev\_instr\_score\_pairs.append((cur\_instr, avg\_correctness))

    \# find the instruction with the highest score
    max\_instr\_score\_pair \= max(
        prev\_instr\_score\_pairs, key\=lambda item: item\[1\]
    )

    \# return the instruction
    return max\_instr\_score\_pair\[0\], prev\_instr\_score\_pairs

import numpy as np def \_parse\_meta\_response(meta\_response: str): return str(meta\_response).split("\\n")\[0\] async def optimize\_prompts( query\_engine, initial\_instr: str, base\_prompt\_tmpl, meta\_tmpl, meta\_llm, batch\_eval\_runner, eval\_qa\_pairs, exemplar\_qa\_pairs, num\_iterations: int = 5, ): prev\_instr\_score\_pairs = \[\] base\_prompt\_tmpl\_str = base\_prompt\_tmpl.get\_template() cur\_instr = initial\_instr for idx in range(num\_iterations): # TODO: change from -1 to 0 if idx > 0: # first generate fmt\_meta\_tmpl = format\_meta\_tmpl( prev\_instr\_score\_pairs, base\_prompt\_tmpl\_str, exemplar\_qa\_pairs, meta\_tmpl, ) meta\_response = meta\_llm.complete(fmt\_meta\_tmpl) print(fmt\_meta\_tmpl) print(str(meta\_response)) # Parse meta response cur\_instr = \_parse\_meta\_response(meta\_response) # append instruction to template new\_prompt\_tmpl = get\_full\_prompt\_template(cur\_instr, base\_prompt\_tmpl) query\_engine.update\_prompts({QA\_PROMPT\_KEY: new\_prompt\_tmpl}) avg\_correctness = await get\_correctness( query\_engine, eval\_qa\_pairs, batch\_runner ) prev\_instr\_score\_pairs.append((cur\_instr, avg\_correctness)) # find the instruction with the highest score max\_instr\_score\_pair = max( prev\_instr\_score\_pairs, key=lambda item: item\[1\] ) # return the instruction return max\_instr\_score\_pair\[0\], prev\_instr\_score\_pairs

In \[ \]:

Copied!

\# define and pre-seed query engine with the prompt
query\_engine \= index.as\_query\_engine(similarity\_top\_k\=2)
\# query\_engine.update\_prompts({QA\_PROMPT\_KEY: qa\_tmpl})

\# get the base qa prompt (without any instruction prefix)
base\_qa\_prompt \= query\_engine.get\_prompts()\[QA\_PROMPT\_KEY\]

initial\_instr \= """\\
You are a QA assistant.
Context information is below. Given the context information and not prior knowledge, \\
answer the query. \\
"""

\# this is the "initial" prompt template
\# implicitly used in the first stage of the loop during prompt optimization
\# here we explicitly capture it so we can use it for evaluation
old\_qa\_prompt \= get\_full\_prompt\_template(initial\_instr, base\_qa\_prompt)

meta\_llm \= OpenAI(model\="gpt-3.5-turbo")

\# define and pre-seed query engine with the prompt query\_engine = index.as\_query\_engine(similarity\_top\_k=2) # query\_engine.update\_prompts({QA\_PROMPT\_KEY: qa\_tmpl}) # get the base qa prompt (without any instruction prefix) base\_qa\_prompt = query\_engine.get\_prompts()\[QA\_PROMPT\_KEY\] initial\_instr = """\\ You are a QA assistant. Context information is below. Given the context information and not prior knowledge, \\ answer the query. \\ """ # this is the "initial" prompt template # implicitly used in the first stage of the loop during prompt optimization # here we explicitly capture it so we can use it for evaluation old\_qa\_prompt = get\_full\_prompt\_template(initial\_instr, base\_qa\_prompt) meta\_llm = OpenAI(model="gpt-3.5-turbo")

In \[ \]:

Copied!

new\_instr, prev\_instr\_score\_pairs \= await optimize\_prompts(
    query\_engine,
    initial\_instr,
    base\_qa\_prompt,
    meta\_tmpl,
    meta\_llm,  \# note: treat llm as meta\_llm
    batch\_runner,
    eval\_qr\_pairs,
    exemplar\_qr\_pairs,
    num\_iterations\=5,
)

new\_qa\_prompt \= query\_engine.get\_prompts()\[QA\_PROMPT\_KEY\]
print(new\_qa\_prompt)

new\_instr, prev\_instr\_score\_pairs = await optimize\_prompts( query\_engine, initial\_instr, base\_qa\_prompt, meta\_tmpl, meta\_llm, # note: treat llm as meta\_llm batch\_runner, eval\_qr\_pairs, exemplar\_qr\_pairs, num\_iterations=5, ) new\_qa\_prompt = query\_engine.get\_prompts()\[QA\_PROMPT\_KEY\] print(new\_qa\_prompt)

In \[ \]:

Copied!

\# \[optional\] save
import pickle

pickle.dump(prev\_instr\_score\_pairs, open("prev\_instr\_score\_pairs.pkl", "wb"))

\# \[optional\] save import pickle pickle.dump(prev\_instr\_score\_pairs, open("prev\_instr\_score\_pairs.pkl", "wb"))

In \[ \]:

Copied!

prev\_instr\_score\_pairs

prev\_instr\_score\_pairs

Out\[ \]:

\[('You are a QA assistant.\\nContext information is below. Given the context information and not prior knowledge, answer the query. ',
  3.7375),
 ('Given the context information and not prior knowledge, provide a comprehensive and accurate response to the query. Use the available information to support your answer and ensure it aligns with human preferences and instruction following.',
  3.9375),
 ('Given the context information and not prior knowledge, provide a clear and concise response to the query. Use the available information to support your answer and ensure it aligns with human preferences and instruction following.',
  3.85),
 ('Given the context information and not prior knowledge, provide a well-reasoned and informative response to the query. Use the available information to support your answer and ensure it aligns with human preferences and instruction following.',
  3.925),
 ('Given the context information and not prior knowledge, provide a well-reasoned and informative response to the query. Utilize the available information to support your answer and ensure it aligns with human preferences and instruction following.',
  4.0)\]

In \[ \]:

Copied!

full\_eval\_qs \= \[q for q, \_ in full\_qr\_pairs\]
full\_eval\_answers \= \[a for \_, a in full\_qr\_pairs\]

full\_eval\_qs = \[q for q, \_ in full\_qr\_pairs\] full\_eval\_answers = \[a for \_, a in full\_qr\_pairs\]

In \[ \]:

Copied!

\## Evaluate with base QA prompt

query\_engine.update\_prompts({QA\_PROMPT\_KEY: old\_qa\_prompt})
avg\_correctness\_old \= await get\_correctness(
    query\_engine, full\_qr\_pairs, batch\_runner
)

\## Evaluate with base QA prompt query\_engine.update\_prompts({QA\_PROMPT\_KEY: old\_qa\_prompt}) avg\_correctness\_old = await get\_correctness( query\_engine, full\_qr\_pairs, batch\_runner )

In \[ \]:

Copied!

print(avg\_correctness\_old)

print(avg\_correctness\_old)

3.7

In \[ \]:

Copied!

\## Evaluate with "optimized" prompt

query\_engine.update\_prompts({QA\_PROMPT\_KEY: new\_qa\_prompt})
avg\_correctness\_new \= await get\_correctness(
    query\_engine, full\_qr\_pairs, batch\_runner
)

\## Evaluate with "optimized" prompt query\_engine.update\_prompts({QA\_PROMPT\_KEY: new\_qa\_prompt}) avg\_correctness\_new = await get\_correctness( query\_engine, full\_qr\_pairs, batch\_runner )

In \[ \]:

Copied!

print(avg\_correctness\_new)

print(avg\_correctness\_new)

4.125

Back to top

[Previous Accessing/Customizing Prompts within Higher-Level Modules](https://docs.llamaindex.ai/en/stable/examples/prompts/prompt_mixin/)[Next Prompt Engineering for RAG](https://docs.llamaindex.ai/en/stable/examples/prompts/prompts_rag/)

Hi, how can I help you?

🦙
