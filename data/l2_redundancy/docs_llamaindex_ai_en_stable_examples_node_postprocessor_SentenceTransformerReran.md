Title: SentenceTransformerRerank - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/SentenceTransformerRerank/

Markdown Content:
SentenceTransformerRerank - LlamaIndex


       

[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/docs/examples/node_postprocessor/SentenceTransformerRerank.ipynb)

Rerank can speed up an LLM query without sacrificing accuracy (and in fact, probably improving it). It does so by pruning away irrelevant nodes from the context.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-embeddings\-huggingface
%pip install llama\-index\-llms\-openai

%pip install llama-index-embeddings-huggingface %pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham").load\_data()

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham").load\_data()

In \[ \]:

Copied!

from llama\_index.core import Settings
from llama\_index.embeddings.huggingface import HuggingFaceEmbedding
from llama\_index.llms.openai import OpenAI

Settings.llm \= OpenAI(model\="gpt-3.5-turbo")
Settings.embed\_model \= HuggingFaceEmbedding(
    model\_name\="BAAI/bge-small-en-v1.5"
)

from llama\_index.core import Settings from llama\_index.embeddings.huggingface import HuggingFaceEmbedding from llama\_index.llms.openai import OpenAI Settings.llm = OpenAI(model="gpt-3.5-turbo") Settings.embed\_model = HuggingFaceEmbedding( model\_name="BAAI/bge-small-en-v1.5" )

/home/jonch/.local/lib/python3.10/site-packages/tqdm/auto.py:22: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user\_install.html
  from .autonotebook import tqdm as notebook\_tqdm

In \[ \]:

Copied!

\# build index
index \= VectorStoreIndex.from\_documents(documents\=documents)

\# build index index = VectorStoreIndex.from\_documents(documents=documents)

In \[ \]:

Copied!

from llama\_index.core.postprocessor import SentenceTransformerRerank

rerank \= SentenceTransformerRerank(
    model\="cross-encoder/ms-marco-MiniLM-L-2-v2", top\_n\=3
)

from llama\_index.core.postprocessor import SentenceTransformerRerank rerank = SentenceTransformerRerank( model="cross-encoder/ms-marco-MiniLM-L-2-v2", top\_n=3 )

First, we try with reranking. We time the query to see how long it takes to process the output from the retrieved context.

In \[ \]:

Copied!

from time import time

from time import time

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(
    similarity\_top\_k\=10, node\_postprocessors\=\[rerank\]
)

now \= time()
response \= query\_engine.query(
    "Which grad schools did the author apply for and why?",
)
print(f"Elapsed: {round(time() \- now, 2)}s")

query\_engine = index.as\_query\_engine( similarity\_top\_k=10, node\_postprocessors=\[rerank\] ) now = time() response = query\_engine.query( "Which grad schools did the author apply for and why?", ) print(f"Elapsed: {round(time() - now, 2)}s")

Elapsed: 4.03s

In \[ \]:

Copied!

print(response)

print(response)

The author applied to three grad schools: MIT and Yale, which were renowned for AI at the time, and Harvard, which the author had visited because a friend went there and it was also home to Bill Woods, who had invented the type of parser the author used in his SHRDLU clone. The author chose these schools because he wanted to learn about AI and Lisp, and these schools were known for their expertise in these areas.

In \[ \]:

Copied!

print(response.get\_formatted\_sources(length\=200))

print(response.get\_formatted\_sources(length=200))

\> Source (Doc id: 08074ca9-1806-4e49-84de-102a97f1f220): been explored. But all I wanted was to get out of grad school, and my rapidly written dissertation sufficed, just barely.

Meanwhile I was applying to art schools. I applied to two: RISD in the US,...

> Source (Doc id: 737f4526-2752-45e8-a59a-e1e4528cc025): about money, because I could sense that Interleaf was on the way down. Freelance Lisp hacking work was very rare, and I didn't want to have to program in another language, which in those days would...

> Source (Doc id: b8883569-44f9-454c-9f62-15e926d04b98): showed Terry Winograd using SHRDLU. I haven't tried rereading The Moon is a Harsh Mistress, so I don't know how well it has aged, but when I read it I was drawn entirely into its world. It seemed o...

Next, we try without rerank

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(similarity\_top\_k\=10)

now \= time()
response \= query\_engine.query(
    "Which grad schools did the author apply for and why?",
)

print(f"Elapsed: {round(time() \- now, 2)}s")

query\_engine = index.as\_query\_engine(similarity\_top\_k=10) now = time() response = query\_engine.query( "Which grad schools did the author apply for and why?", ) print(f"Elapsed: {round(time() - now, 2)}s")

Elapsed: 28.13s

In \[ \]:

Copied!

print(response)

print(response)

The author applied to three grad schools: MIT and Yale, which were renowned for AI at the time, and Harvard, which the author had visited because a friend went there and was also home to Bill Woods, who had invented the type of parser the author used in his SHRDLU clone. The author chose these schools because he was interested in Artificial Intelligence and wanted to pursue it further, and they were the most renowned for it at the time. He was also inspired by a novel by Heinlein called The Moon is a Harsh Mistress, which featured an intelligent computer called Mike, and a PBS documentary that showed Terry Winograd using SHRDLU. Additionally, the author had dropped out of RISD, where he had been learning to paint, and was looking for a new challenge. He was drawn to the idea of pursuing AI, as it was a field that was rapidly growing and he wanted to be part of the cutting edge of technology. He was also inspired by the idea of creating something unique and innovative, as he had done with his SHRDLU clone, and wanted to continue to explore the possibilities of AI.

In \[ \]:

Copied!

print(response.get\_formatted\_sources(length\=200))

print(response.get\_formatted\_sources(length=200))

\> Source (Doc id: 08074ca9-1806-4e49-84de-102a97f1f220): been explored. But all I wanted was to get out of grad school, and my rapidly written dissertation sufficed, just barely.

Meanwhile I was applying to art schools. I applied to two: RISD in the US,...

> Source (Doc id: 737f4526-2752-45e8-a59a-e1e4528cc025): about money, because I could sense that Interleaf was on the way down. Freelance Lisp hacking work was very rare, and I didn't want to have to program in another language, which in those days would...

> Source (Doc id: b8883569-44f9-454c-9f62-15e926d04b98): showed Terry Winograd using SHRDLU. I haven't tried rereading The Moon is a Harsh Mistress, so I don't know how well it has aged, but when I read it I was drawn entirely into its world. It seemed o...

> Source (Doc id: 599f469b-9a92-4952-8753-a063c31a953b): I didn't know but would turn out to like a lot: a woman called Jessica Livingston. A couple days later I asked her out.

Jessica was in charge of marketing at a Boston investment bank. This bank th...

> Source (Doc id: c865f333-b731-4a8b-a99f-eec54eaa1e6b): Like McCarthy's original Lisp, it's a spec rather than an implementation, although like McCarthy's Lisp it's a spec expressed as code.

Now that I could write essays again, I wrote a bunch about to...

> Source (Doc id: 69c6b190-2d4e-4128-b9c4-4fd31af2df65): 1960 paper.

But if so there's no reason to suppose that this is the limit of the language that might be known to them. Presumably aliens need numbers and errors and I/O too. So it seems likely the...

> Source (Doc id: c9c95028-a49e-440e-a953-7aabe6b9996d): What I Worked On

February 2021

Before college the two main things I worked on, outside of school, were writing and programming. I didn't write essays. I wrote what beginning writers were supposed...

> Source (Doc id: 7f0c11db-d6f0-41f9-95bc-1feab914f58f): that big, bureaucratic customers are a dangerous source of money, and that there's not much overlap between conventional office hours and the optimal time for hacking, or conventional offices and t...

> Source (Doc id: c143a6c2-5f5d-49c5-bc1e-b9caa0ce4931): must tell readers things they don't already know, and some people dislike being told such things.

\[11\] People put plenty of stuff on the internet in the 90s of course, but putting something online...

> Source (Doc id: 6e281eec-6964-414b-be61-bcc509d95903): which I'd created years before using Viaweb but had never used for anything. In one day it got 30,000 page views. What on earth had happened? The referring urls showed that someone had posted it on...

As we can see, the query engine with reranking produced a much more concise output in much lower time (4s v.s. 28s). While both responses were essentially correct, the query engine without reranking included a lot of irrelevant information - a phenomenon we could attribute to "pollution of the context window".

Back to top

[Previous Recency Filtering](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/RecencyPostprocessorDemo/)[Next Time-Weighted Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/TimeWeightedPostprocessorDemo/)

Hi, how can I help you?

🦙
