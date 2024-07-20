Title: Building Response Synthesis from Scratch

URL Source: https://docs.llamaindex.ai/en/stable/examples/low_level/response_synthesis/

Markdown Content:
Building Response Synthesis from Scratch - LlamaIndex


In this tutorial, we show you how to build the "LLM synthesis" component of a RAG pipeline from scratch. Given a set of retrieved Nodes, we'll show you how to synthesize a response even if the retrieved context overflows the context window.

We'll walk through some synthesis strategies:

*   Create and Refine
*   Tree Summarization

We're essentially unpacking our "Response Synthesis" module and exposing that for the user.

We use OpenAI as a default LLM but you're free to plug in any LLM you wish.

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/response_synthesis/#setup)
-------------------------------------------------------------------------------------------

We build an empty Pinecone Index, and define the necessary LlamaIndex wrappers/abstractions so that we can load/index data and get back a vector retriever.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-readers\-file pymupdf
%pip install llama\-index\-vector\-stores\-pinecone
%pip install llama\-index\-llms\-openai

%pip install llama-index-readers-file pymupdf %pip install llama-index-vector-stores-pinecone %pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

#### Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/response_synthesis/#load-data)

In \[ \]:

Copied!

!mkdir data
!wget \--user\-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" \-O "data/llama2.pdf"

!mkdir data !wget --user-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" -O "data/llama2.pdf"

In \[ \]:

Copied!

from pathlib import Path
from llama\_index.readers.file import PyMuPDFReader

from pathlib import Path from llama\_index.readers.file import PyMuPDFReader

In \[ \]:

Copied!

loader \= PyMuPDFReader()
documents \= loader.load(file\_path\="./data/llama2.pdf")

loader = PyMuPDFReader() documents = loader.load(file\_path="./data/llama2.pdf")

#### Build Pinecone Index, Get Retriever[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/response_synthesis/#build-pinecone-index-get-retriever)

We use our high-level LlamaIndex abstractions to 1) ingest data into Pinecone, and then 2) get a vector retriever.

Note that we set chunk sizes to 1024.

In \[ \]:

Copied!

import pinecone
import os

api\_key \= os.environ\["PINECONE\_API\_KEY"\]
pinecone.init(api\_key\=api\_key, environment\="us-west1-gcp")

import pinecone import os api\_key = os.environ\["PINECONE\_API\_KEY"\] pinecone.init(api\_key=api\_key, environment="us-west1-gcp")

/Users/jerryliu/Programming/gpt\_index/.venv/lib/python3.10/site-packages/pinecone/index.py:4: TqdmExperimentalWarning: Using \`tqdm.autonotebook.tqdm\` in notebook mode. Use \`tqdm.tqdm\` instead to force console mode (e.g. in jupyter console)
  from tqdm.autonotebook import tqdm

In \[ \]:

Copied!

\# dimensions are for text-embedding-ada-002
pinecone.create\_index(
    "quickstart", dimension\=1536, metric\="euclidean", pod\_type\="p1"
)

\# dimensions are for text-embedding-ada-002 pinecone.create\_index( "quickstart", dimension=1536, metric="euclidean", pod\_type="p1" )

In \[ \]:

Copied!

pinecone\_index \= pinecone.Index("quickstart")

pinecone\_index = pinecone.Index("quickstart")

In \[ \]:

Copied!

\# \[Optional\] drop contents in index
pinecone\_index.delete(deleteAll\=True)

\# \[Optional\] drop contents in index pinecone\_index.delete(deleteAll=True)

Out\[ \]:

{}

In \[ \]:

Copied!

from llama\_index.vector\_stores.pinecone import PineconeVectorStore
from llama\_index.core import VectorStoreIndex
from llama\_index.core.node\_parser import SentenceSplitter
from llama\_index.core import StorageContext

from llama\_index.vector\_stores.pinecone import PineconeVectorStore from llama\_index.core import VectorStoreIndex from llama\_index.core.node\_parser import SentenceSplitter from llama\_index.core import StorageContext

In \[ \]:

Copied!

vector\_store \= PineconeVectorStore(pinecone\_index\=pinecone\_index)
\# NOTE: set chunk size of 1024
splitter \= SentenceSplitter(chunk\_size\=1024)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents, transformations\=\[splitter\], storage\_context\=storage\_context
)

vector\_store = PineconeVectorStore(pinecone\_index=pinecone\_index) # NOTE: set chunk size of 1024 splitter = SentenceSplitter(chunk\_size=1024) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, transformations=\[splitter\], storage\_context=storage\_context )

In \[ \]:

Copied!

retriever \= index.as\_retriever()

retriever = index.as\_retriever()

#### Given an example question, get a retrieved set of nodes.[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/response_synthesis/#given-an-example-question-get-a-retrieved-set-of-nodes)

We use the retriever to get a set of relevant nodes given a user query. These nodes will then be passed to the response synthesis modules below.

In \[ \]:

Copied!

query\_str \= (
    "Can you tell me about results from RLHF using both model-based and"
    " human-based evaluation?"
)

query\_str = ( "Can you tell me about results from RLHF using both model-based and" " human-based evaluation?" )

In \[ \]:

Copied!

retrieved\_nodes \= retriever.retrieve(query\_str)

retrieved\_nodes = retriever.retrieve(query\_str)

Building Response Synthesis with LLMs[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/response_synthesis/#building-response-synthesis-with-llms)
-----------------------------------------------------------------------------------------------------------------------------------------------------------

In this section we'll show how to use LLMs + Prompts to build a response synthesis module.

We'll start from simple strategies (simply stuffing context into a prompt), to more advanced strategies that can handle context overflows.

### 1\. Try a Simple Prompt[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/response_synthesis/#1-try-a-simple-prompt)

We first try to synthesize the response using a single input prompt + LLM call.

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI
from llama\_index.core import PromptTemplate

llm \= OpenAI(model\="text-davinci-003")

from llama\_index.llms.openai import OpenAI from llama\_index.core import PromptTemplate llm = OpenAI(model="text-davinci-003")

In \[ \]:

Copied!

qa\_prompt \= PromptTemplate(
    """\\
Context information is below.
\---------------------
{context\_str}
\---------------------
Given the context information and not prior knowledge, answer the query.
Query: {query\_str}
Answer: \\
"""
)

qa\_prompt = PromptTemplate( """\\ Context information is below. --------------------- {context\_str} --------------------- Given the context information and not prior knowledge, answer the query. Query: {query\_str} Answer: \\ """ )

Given an example question, retrieve the set of relevant nodes and try to put it all in the prompt, separated by newlines.

In \[ \]:

Copied!

query\_str \= (
    "Can you tell me about results from RLHF using both model-based and"
    " human-based evaluation?"
)

query\_str = ( "Can you tell me about results from RLHF using both model-based and" " human-based evaluation?" )

In \[ \]:

Copied!

retrieved\_nodes \= retriever.retrieve(query\_str)

retrieved\_nodes = retriever.retrieve(query\_str)

In \[ \]:

Copied!

def generate\_response(retrieved\_nodes, query\_str, qa\_prompt, llm):
    context\_str \= "\\n\\n".join(\[r.get\_content() for r in retrieved\_nodes\])
    fmt\_qa\_prompt \= qa\_prompt.format(
        context\_str\=context\_str, query\_str\=query\_str
    )
    response \= llm.complete(fmt\_qa\_prompt)
    return str(response), fmt\_qa\_prompt

def generate\_response(retrieved\_nodes, query\_str, qa\_prompt, llm): context\_str = "\\n\\n".join(\[r.get\_content() for r in retrieved\_nodes\]) fmt\_qa\_prompt = qa\_prompt.format( context\_str=context\_str, query\_str=query\_str ) response = llm.complete(fmt\_qa\_prompt) return str(response), fmt\_qa\_prompt

In \[ \]:

Copied!

response, fmt\_qa\_prompt \= generate\_response(
    retrieved\_nodes, query\_str, qa\_prompt, llm
)

response, fmt\_qa\_prompt = generate\_response( retrieved\_nodes, query\_str, qa\_prompt, llm )

In \[ \]:

Copied!

print(f"\*\*\*\*\*Response\*\*\*\*\*\*:\\n{response}\\n\\n")

print(f"\*\*\*\*\*Response\*\*\*\*\*\*:\\n{response}\\n\\n")

\*\*\*\*\*Response\*\*\*\*\*\*:

RLHF used both model-based and human-based evaluation to select the best-performing models among several ablations. Model-based evaluation was used to measure the robustness of the reward model by collecting a test set of prompts for both helpfulness and safety, and asking three annotators to judge the quality of the answers based on a 7-point Likert scale. Human evaluation was used to validate major model versions. Additionally, a more general reward was trained to ensure the measure wouldn't diverge from the human preferences. Results showed that the reward models were well calibrated with the human preference annotations.

In \[ \]:

Copied!

print(f"\*\*\*\*\*Formatted Prompt\*\*\*\*\*:\\n{fmt\_qa\_prompt}\\n\\n")

print(f"\*\*\*\*\*Formatted Prompt\*\*\*\*\*:\\n{fmt\_qa\_prompt}\\n\\n")

\*\*\*\*\*Formatted Prompt\*\*\*\*\*:
Context information is below.
---------------------
3.4
RLHF Results
3.4.1
Model-Based Evaluation
Evaluating LLMs is a challenging open-research problem. Human evaluation, while a gold standard, can
be complicated by various HCI considerations (Clark et al., 2021; Gehrmann et al., 2023), and is not always
scalable. Thus, to select the best-performing models among several ablations at each iteration from RLHF-V1
to V5, we first observed the improvement of the rewards from the latest reward models, to save costs and
increase iteration speed. We later validated major model versions with human evaluations.
How Far Can Model-Based Evaluation Go?
To measure the robustness of our reward model, we collected
a test set of prompts for both helpfulness and safety, and asked three annotators to judge the quality of the
answers based on a 7-point Likert scale (the higher the better). We observe that our reward models overall
are well calibrated with our human preference annotations, as illustrated in Figure 29 in the appendix. This
confirms the relevance of using our reward as a point-wise metric, despite being trained with a Pairwise
Ranking Loss.
Still, as Goodhart’s Law states, when a measure becomes a target, it ceases to be a good measure. To ensure
our measure won’t diverge from the human preferences, we additionally used a more general reward, trained
17

5
Discussion
Here, we discuss the interesting properties we have observed with RLHF (Section 5.1). We then discuss the
limitations of Llama 2-Chat (Section 5.2). Lastly, we present our strategy for responsibly releasing these
models (Section 5.3).
5.1
Learnings and Observations
Our tuning process revealed several interesting results, such as Llama 2-Chat’s abilities to temporally
organize its knowledge, or to call APIs for external tools.
SFT (Mix)
SFT (Annotation)
RLHF (V1)
0.0
0.2
0.4
0.6
0.8
1.0
Reward Model Score
RLHF (V2)
Figure 20: Distribution shift for progressive versions of Llama 2-Chat, from SFT models towards RLHF.
Beyond Human Supervision.
At the outset of the project, many among us expressed a preference for
supervised annotation, attracted by its denser signal. Meanwhile reinforcement learning, known for its insta-
bility, seemed a somewhat shadowy field for those in the NLP research community. However, reinforcement
learning proved highly effective, particularly given its cost and time effectiveness. Our findings underscore
that the crucial determinant of RLHF’s success lies in the synergy it fosters between humans and LLMs
throughout the annotation process.
Even with proficient annotators, each individual writes with significant variation. A model fine-tuned on
SFT annotation learns this diversity, including, unfortunately, the tail-end of poorly executed annotation. Fur-
thermore, the model’s performance is capped by the writing abilities of the most skilled annotators. Human
annotators are arguably less subject to discrepancy when comparing two outputs’ preference annotation
for RLHF. Consequently, the reward mechanism swiftly learns to assign low scores to undesirable tail-end
distribution and aligns towards the human preference. This phenomena is illustrated in Figure 20, where we
can see that the worst answers are progressively removed, shifting the distribution to the right.
In addition, during annotation, the model has the potential to venture into writing trajectories that even the
best annotators may not chart. Nonetheless, humans can still provide valuable feedback when comparing two
answers, beyond their own writing competencies. Drawing a parallel, while we may not all be accomplished
artists, our ability to appreciate and critique art remains intact. We posit that the superior writing abilities of
LLMs, as manifested in surpassing human annotators in certain tasks, are fundamentally driven by RLHF, as
documented in Gilardi et al. (2023) and Huang et al. (2023). Supervised data may no longer be the gold
standard, and this evolving circumstance compels a re-evaluation of the concept of “supervision.”
In-Context Temperature Rescaling.
We have observed an intriguing phenomenon related to RLHF, a feature
not previously reported to the best of our knowledge: the dynamic re-scaling of temperature contingent upon
the context. As indicated in Figure 8, the temperature appears to be influenced by RLHF. Yet, intriguingly,
our findings also revealed that the shifts are not uniformly applied across all prompts, as shown in Figure 21.
For instance, when it comes to prompts associated with creativity, such as “Write a poem,” an increase in
temperature continues to generate diversity across our various RLHF iterations. This can be observed in the
Self-BLEU slope, which mirrors a pattern comparable to that of the SFT model.
On the other hand, for prompts based on factual information, such as “What is the capital of ?” the Self-BLEU
slope diminishes over time. This pattern suggests that despite the rising temperature, the model learns to
consistently provide the same response to factual prompts.
32
---------------------
Given the context information and not prior knowledge, answer the query.
Query: Can you tell me about results from RLHF using both model-based and human-based evaluation?
Answer: 

**Problem**: What if we set the top-k retriever to a higher value? The context would overflow!

In \[ \]:

Copied!

retriever \= index.as\_retriever(similarity\_top\_k\=6)
retrieved\_nodes \= retriever.retrieve(query\_str)

retriever = index.as\_retriever(similarity\_top\_k=6) retrieved\_nodes = retriever.retrieve(query\_str)

In \[ \]:

Copied!

response, fmt\_qa\_prompt \= generate\_response(
    retrieved\_nodes, query\_str, qa\_prompt, llm
)
print(f"Response (k=5): {response}")

response, fmt\_qa\_prompt = generate\_response( retrieved\_nodes, query\_str, qa\_prompt, llm ) print(f"Response (k=5): {response}")

\---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In\[34\], line 1
\----> 1 response, fmt\_qa\_prompt \= generate\_response(retrieved\_nodes, query\_str, qa\_prompt, llm)
      2 print(f'Response (k=5): {response}')

Cell In\[16\], line 4, in generate\_response(retrieved\_nodes, query\_str, qa\_prompt, llm)
      2 context\_str \= "\\n\\n".join(\[r.get\_content() for r in retrieved\_nodes\])
      3 fmt\_qa\_prompt \= qa\_prompt.format(context\_str\=context\_str, query\_str\=query\_str)
\----> 4 response \= llm.complete(fmt\_qa\_prompt)
      5 return str(response), fmt\_qa\_prompt

File ~/Programming/gpt\_index/llama\_index/llms/base.py:277, in llm\_completion\_callback.<locals>.wrap.<locals>.wrapped\_llm\_predict(\_self, \*args, \*\*kwargs)
    267 with wrapper\_logic(\_self) as callback\_manager:
    268     event\_id \= callback\_manager.on\_event\_start(
    269         CBEventType.LLM,
    270         payload\={
   (...)
    274         },
    275     )
\--> 277     f\_return\_val \= f(\_self, \*args, \*\*kwargs)
    278     if isinstance(f\_return\_val, Generator):
    279         \# intercept the generator and add a callback to the end
    280         def wrapped\_gen() \-\> CompletionResponseGen:

File ~/Programming/gpt\_index/llama\_index/llms/openai.py:144, in OpenAI.complete(self, prompt, \*\*kwargs)
    142 else:
    143     complete\_fn \= self.\_complete
\--> 144 return complete\_fn(prompt, \*\*kwargs)

File ~/Programming/gpt\_index/llama\_index/llms/openai.py:281, in OpenAI.\_complete(self, prompt, \*\*kwargs)
    278 all\_kwargs \= self.\_get\_all\_kwargs(\*\*kwargs)
    279 if self.max\_tokens is None:
    280     \# NOTE: non-chat completion endpoint requires max\_tokens to be set
\--> 281     max\_tokens \= self.\_get\_max\_token\_for\_prompt(prompt)
    282     all\_kwargs\["max\_tokens"\] \= max\_tokens
    284 response \= completion\_with\_retry(
    285     is\_chat\_model\=self.\_is\_chat\_model,
    286     max\_retries\=self.max\_retries,
   (...)
    289     \*\*all\_kwargs,
    290 )

File ~/Programming/gpt\_index/llama\_index/llms/openai.py:343, in OpenAI.\_get\_max\_token\_for\_prompt(self, prompt)
    341 max\_token \= context\_window \- len(tokens)
    342 if max\_token <\= 0:
\--> 343     raise ValueError(
    344         f"The prompt is too long for the model. "
    345         f"Please use a prompt that is less than {context\_window} tokens."
    346     )
    347 return max\_token

ValueError: The prompt is too long for the model. Please use a prompt that is less than 4097 tokens.

### 2\. Try a "Create and Refine" strategy[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/response_synthesis/#2-try-a-create-and-refine-strategy)

To deal with context overflows, we can try a strategy where we synthesize a response sequentially through all nodes. Start with the first node and generate an initial response. Then for subsequent nodes, refine the answer using additional context.

This requires us to define a "refine" prompt as well.

In \[ \]:

Copied!

refine\_prompt \= PromptTemplate(
    """\\
The original query is as follows: {query\_str}
We have provided an existing answer: {existing\_answer}
We have the opportunity to refine the existing answer \\
(only if needed) with some more context below.
\------------
{context\_str}
\------------
Given the new context, refine the original answer to better answer the query. \\
If the context isn't useful, return the original answer.
Refined Answer: \\
"""
)

refine\_prompt = PromptTemplate( """\\ The original query is as follows: {query\_str} We have provided an existing answer: {existing\_answer} We have the opportunity to refine the existing answer \\ (only if needed) with some more context below. ------------ {context\_str} ------------ Given the new context, refine the original answer to better answer the query. \\ If the context isn't useful, return the original answer. Refined Answer: \\ """ )

In \[ \]:

Copied!

from llama\_index.core.response.notebook\_utils import display\_source\_node

def generate\_response\_cr(
    retrieved\_nodes, query\_str, qa\_prompt, refine\_prompt, llm
):
    """Generate a response using create and refine strategy.

    The first node uses the 'QA' prompt.
    All subsequent nodes use the 'refine' prompt.

    """
    cur\_response \= None
    fmt\_prompts \= \[\]
    for idx, node in enumerate(retrieved\_nodes):
        print(f"\[Node {idx}\]")
        display\_source\_node(node, source\_length\=2000)
        context\_str \= node.get\_content()
        if idx \ 0: fmt\_prompt = qa\_prompt.format( context\_str=context\_str, query\_str=query\_str ) else: fmt\_prompt = refine\_prompt.format( context\_str=context\_str, query\_str=query\_str, existing\_answer=str(cur\_response), ) cur\_response = llm.complete(fmt\_prompt) fmt\_prompts.append(fmt\_prompt) return str(cur\_response), fmt\_prompts

In \[ \]:

Copied!

response, fmt\_prompts \= generate\_response\_cr(
    retrieved\_nodes, query\_str, qa\_prompt, refine\_prompt, llm
)

response, fmt\_prompts = generate\_response\_cr( retrieved\_nodes, query\_str, qa\_prompt, refine\_prompt, llm )

In \[ \]:

Copied!

print(str(response))

print(str(response))

In \[ \]:

Copied!

\# view a sample qa prompt
print(fmt\_prompts\[0\])

\# view a sample qa prompt print(fmt\_prompts\[0\])

In \[ \]:

Copied!

\# view a sample refine prompt
print(fmt\_prompts\[1\])

\# view a sample refine prompt print(fmt\_prompts\[1\])

**Observation**: This is an initial step, but obviously there are inefficiencies. One is the fact that it's quite slow - we make sequential calls. The second piece is that each LLM call is inefficient - we are only inserting a single node, but not "stuffing" the prompt with as much context as necessary.

### 3\. Try a Hierarchical Summarization Strategy[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/response_synthesis/#3-try-a-hierarchical-summarization-strategy)

Another approach is to try a hierarchical summarization strategy. We generate an answer for each node independently, and then hierarchically combine the answers. This "combine" step could happen once, or for maximum generality can happen recursively until there is one "root" node. That "root" node is then returned as the answer.

We implement this approach below. We have a fixed number of children of 5, so we hierarchically combine 5 children at a time.

**NOTE**: In LlamaIndex this is referred to as "tree\_summarize", in LangChain this is referred to as map-reduce.

In \[ \]:

Copied!

def combine\_results(
    texts,
    query\_str,
    qa\_prompt,
    llm,
    cur\_prompt\_list,
    num\_children\=10,
):
    new\_texts \= \[\]
    for idx in range(0, len(texts), num\_children):
        text\_batch \= texts\[idx : idx + num\_children\]
        context\_str \= "\\n\\n".join(\[t for t in text\_batch\])
        fmt\_qa\_prompt \= qa\_prompt.format(
            context\_str\=context\_str, query\_str\=query\_str
        )
        combined\_response \= llm.complete(fmt\_qa\_prompt)
        new\_texts.append(str(combined\_response))
        cur\_prompt\_list.append(fmt\_qa\_prompt)

    if len(new\_texts) \ 1: return new\_texts\[0\] else: return combine\_results( new\_texts, query\_str, qa\_prompt, llm, num\_children=num\_children ) def generate\_response\_hs( retrieved\_nodes, query\_str, qa\_prompt, llm, num\_children=10 ): """Generate a response using hierarchical summarization strategy. Combine num\_children nodes hierarchically until we get one root node. """ fmt\_prompts = \[\] node\_responses = \[\] for node in retrieved\_nodes: context\_str = node.get\_content() fmt\_qa\_prompt = qa\_prompt.format( context\_str=context\_str, query\_str=query\_str ) node\_response = llm.complete(fmt\_qa\_prompt) node\_responses.append(node\_response) fmt\_prompts.append(fmt\_qa\_prompt) response\_txt = combine\_results( \[str(r) for r in node\_responses\], query\_str, qa\_prompt, llm, fmt\_prompts, num\_children=num\_children, ) return response\_txt, fmt\_prompts

In \[ \]:

Copied!

response, fmt\_prompts \= generate\_response\_hs(
    retrieved\_nodes, query\_str, qa\_prompt, llm
)

response, fmt\_prompts = generate\_response\_hs( retrieved\_nodes, query\_str, qa\_prompt, llm )

In \[ \]:

Copied!

print(str(response))

print(str(response))

The results from RLHF using both model-based and human-based evaluation showed that Llama 2-Chat models outperformed open-source models by a significant margin on both single turn and multi-turn prompts. For human-based evaluation, we compared Llama 2-Chat models to open-source models and closed-source models on over 4,000 single and multi-turn prompts. The results showed that Llama 2-Chat models outperformed the other models by a significant margin on both single turn and multi-turn prompts. The human preference annotation agreement rate was also higher on more distinct responses than similar pairs. The largest RLHF model was competitive with ChatGPT, with a win rate of 36% and a tie rate of 31.5% relative to ChatGPT. RLHF 70B model also outperformed PaLM-bison chat model by a large percentage on the prompt set.

**Observation**: Note that the answer is much more concise than the create-and-refine approach. This is a well-known phemonenon - the reason is because hierarchical summarization tends to compress information at each stage, whereas create and refine encourages adding on more information with each node.

**Observation**: Similar to the above section, there are inefficiencies. We are still generating an answer for each node independently that we can try to optimize away.

Our `ResponseSynthesizer` module handles this!

#### 4\. \[Optional\] Let's create an async version of hierarchical summarization![¶](https://docs.llamaindex.ai/en/stable/examples/low_level/response_synthesis/#4-optional-lets-create-an-async-version-of-hierarchical-summarization)

A pro of the hierarchical summarization approach is that the LLM calls can be parallelized, leading to big speedups in response synthesis.

We implement an async version below. We use asyncio.gather to execute coroutines (LLM calls) for each Node concurrently.

In \[ \]:

Copied!

import nest\_asyncio
import asyncio

nest\_asyncio.apply()

import nest\_asyncio import asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

async def acombine\_results(
    texts,
    query\_str,
    qa\_prompt,
    llm,
    cur\_prompt\_list,
    num\_children\=10,
):
    fmt\_prompts \= \[\]
    for idx in range(0, len(texts), num\_children):
        text\_batch \= texts\[idx : idx + num\_children\]
        context\_str \= "\\n\\n".join(\[t for t in text\_batch\])
        fmt\_qa\_prompt \= qa\_prompt.format(
            context\_str\=context\_str, query\_str\=query\_str
        )
        fmt\_prompts.append(fmt\_qa\_prompt)
        cur\_prompt\_list.append(fmt\_qa\_prompt)

    tasks \= \[llm.acomplete(p) for p in fmt\_prompts\]
    combined\_responses \= await asyncio.gather(\*tasks)
    new\_texts \= \[str(r) for r in combined\_responses\]

    if len(new\_texts) \ 1: return new\_texts\[0\] else: return await acombine\_results( new\_texts, query\_str, qa\_prompt, llm, num\_children=num\_children ) async def agenerate\_response\_hs( retrieved\_nodes, query\_str, qa\_prompt, llm, num\_children=10 ): """Generate a response using hierarchical summarization strategy. Combine num\_children nodes hierarchically until we get one root node. """ fmt\_prompts = \[\] node\_responses = \[\] for node in retrieved\_nodes: context\_str = node.get\_content() fmt\_qa\_prompt = qa\_prompt.format( context\_str=context\_str, query\_str=query\_str ) fmt\_prompts.append(fmt\_qa\_prompt) tasks = \[llm.acomplete(p) for p in fmt\_prompts\] node\_responses = await asyncio.gather(\*tasks) response\_txt = combine\_results( \[str(r) for r in node\_responses\], query\_str, qa\_prompt, llm, fmt\_prompts, num\_children=num\_children, ) return response\_txt, fmt\_prompts

In \[ \]:

Copied!

response, fmt\_prompts \= await agenerate\_response\_hs(
    retrieved\_nodes, query\_str, qa\_prompt, llm
)

response, fmt\_prompts = await agenerate\_response\_hs( retrieved\_nodes, query\_str, qa\_prompt, llm )

In \[ \]:

Copied!

print(str(response))

print(str(response))

 Results from RLHF using both model-based and human-based evaluation show that larger models generally obtain higher performance for a similar volume of data. Additionally, the accuracy on more distinct responses matters the most to improve Llama 2-Chat performance. The human preference annotation agreement rate is also higher on more distinct responses than similar pairs. Furthermore, two main algorithms were explored for RLHF fine-tuning: Proximal Policy Optimization (PPO) and Rejection Sampling fine-tuning. The largest Llama 2-Chat model was found to be competitive with ChatGPT, with a win rate of 36% and a tie rate of 31.5% relative to ChatGPT. Additionally, Llama 2-Chat 70B model outperformed PaLM-bison chat model by a large percentage on our prompt set. Inter-Rater Reliability (IRR) was measured using Gwet’s AC1/2 statistic, with scores varying between 0.37 and 0.55 depending on the specific model comparison.

Let's put it all together![¶](https://docs.llamaindex.ai/en/stable/examples/low_level/response_synthesis/#lets-put-it-all-together)
-----------------------------------------------------------------------------------------------------------------------------------

Let's define a simple query engine that can be initialized with a retriever, prompt, llm etc. And have it implement a simple `query` function. We also implement an async version, can be used if you completed part 4 above!

**NOTE**: We skip subclassing our own `QueryEngine` abstractions. This is a big TODO to make it more easily sub-classable!

In \[ \]:

Copied!

from llama\_index.core.retrievers import BaseRetriever
from llama\_index.core.llms import LLM
from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Response:
    response: str
    source\_nodes: Optional\[List\] \= None

    def \_\_str\_\_(self):
        return self.response

class MyQueryEngine:
    """My query engine.

    Uses the tree summarize response synthesis module by default.

    """

    def \_\_init\_\_(
        self,
        retriever: BaseRetriever,
        qa\_prompt: PromptTemplate,
        llm: LLM,
        num\_children\=10,
    ) \-> None:
        self.\_retriever \= retriever
        self.\_qa\_prompt \= qa\_prompt
        self.\_llm \= llm
        self.\_num\_children \= num\_children

    def query(self, query\_str: str):
        retrieved\_nodes \= self.\_retriever.retrieve(query\_str)
        response\_txt, \_ \= generate\_response\_hs(
            retrieved\_nodes,
            query\_str,
            self.\_qa\_prompt,
            self.\_llm,
            num\_children\=self.\_num\_children,
        )
        response \= Response(response\_txt, source\_nodes\=retrieved\_nodes)
        return response

    async def aquery(self, query\_str: str):
        retrieved\_nodes \= await self.\_retriever.aretrieve(query\_str)
        response\_txt, \_ \= await agenerate\_response\_hs(
            retrieved\_nodes,
            query\_str,
            self.\_qa\_prompt,
            self.\_llm,
            num\_children\=self.\_num\_children,
        )
        response \= Response(response\_txt, source\_nodes\=retrieved\_nodes)
        return response

from llama\_index.core.retrievers import BaseRetriever from llama\_index.core.llms import LLM from dataclasses import dataclass from typing import Optional, List @dataclass class Response: response: str source\_nodes: Optional\[List\] = None def \_\_str\_\_(self): return self.response class MyQueryEngine: """My query engine. Uses the tree summarize response synthesis module by default. """ def \_\_init\_\_( self, retriever: BaseRetriever, qa\_prompt: PromptTemplate, llm: LLM, num\_children=10, ) -> None: self.\_retriever = retriever self.\_qa\_prompt = qa\_prompt self.\_llm = llm self.\_num\_children = num\_children def query(self, query\_str: str): retrieved\_nodes = self.\_retriever.retrieve(query\_str) response\_txt, \_ = generate\_response\_hs( retrieved\_nodes, query\_str, self.\_qa\_prompt, self.\_llm, num\_children=self.\_num\_children, ) response = Response(response\_txt, source\_nodes=retrieved\_nodes) return response async def aquery(self, query\_str: str): retrieved\_nodes = await self.\_retriever.aretrieve(query\_str) response\_txt, \_ = await agenerate\_response\_hs( retrieved\_nodes, query\_str, self.\_qa\_prompt, self.\_llm, num\_children=self.\_num\_children, ) response = Response(response\_txt, source\_nodes=retrieved\_nodes) return response

In \[ \]:

Copied!

query\_engine \= MyQueryEngine(retriever, qa\_prompt, llm, num\_children\=10)

query\_engine = MyQueryEngine(retriever, qa\_prompt, llm, num\_children=10)

In \[ \]:

Copied!

response \= query\_engine.query(query\_str)

response = query\_engine.query(query\_str)

In \[ \]:

Copied!

print(str(response))

print(str(response))

The results from RLHF using both model-based and human-based evaluation showed that larger models generally obtained higher performance for a similar volume of data. The accuracy on more distinct responses was higher than on similar pairs, indicating that learning to model human preferences becomes challenging when deciding between two similar model responses. Additionally, the largest Llama 2-Chat model was found to be competitive with ChatGPT, with a win rate of 36% and a tie rate of 31.5% relative to ChatGPT. Llama 2-Chat 70B model was also found to outperform PaLM-bison chat model by a large percentage on the prompt set. Inter-Rater Reliability (IRR) was measured using Gwet’s AC1/2 statistic, with scores varying between 0.37 and 0.55 depending on the specific model comparison.

In \[ \]:

Copied!

response \= await query\_engine.aquery(query\_str)

response = await query\_engine.aquery(query\_str)

In \[ \]:

Copied!

print(str(response))

print(str(response))

The results from RLHF using both model-based and human-based evaluation showed that larger models generally obtained higher performance for a similar volume of data. The accuracy on more distinct responses was higher than on similar pairs, indicating that learning to model human preferences becomes challenging when deciding between two similar model responses. Additionally, the largest Llama 2-Chat model was found to be competitive with ChatGPT, with a win rate of 36% and a tie rate of 31.5%. Human evaluations were conducted using a 7-point Likert scale helpfulness task, with Gwet’s AC2 score varying between 0.37 and 0.55 depending on the specific model comparison.

Back to top

[Previous Building RAG from Scratch (Open-source only!)](https://docs.llamaindex.ai/en/stable/examples/low_level/oss_ingestion_retrieval/)[Next Building Retrieval from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/retrieval/)

Hi, how can I help you?

🦙
