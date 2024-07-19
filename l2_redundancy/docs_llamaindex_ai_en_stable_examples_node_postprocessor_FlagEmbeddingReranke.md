Title: FlagEmbeddingReranker - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/FlagEmbeddingReranker/

Markdown Content:
FlagEmbeddingReranker - LlamaIndex


       

[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/docs/examples/node_postprocessor/SentenceTransformerRerank.ipynb)

Rerank can speed up an LLM query without sacrificing accuracy (and in fact, probably improving it). It does so by pruning away irrelevant nodes from the context.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-embeddings\-huggingface
%pip install llama\-index\-llms\-openai
%pip install llama\-index\-postprocessor\-flag\-embedding\-reranker

%pip install llama-index-embeddings-huggingface %pip install llama-index-llms-openai %pip install llama-index-postprocessor-flag-embedding-reranker

In \[ \]:

Copied!

!pip install llama\-index
!pip install git+https://github.com/FlagOpen/FlagEmbedding.git

!pip install llama-index !pip install git+https://github.com/FlagOpen/FlagEmbedding.git

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

import os

OPENAI\_API\_KEY \= "sk-"
os.environ\["OPENAI\_API\_KEY"\] \= OPENAI\_API\_KEY

import os OPENAI\_API\_KEY = "sk-" os.environ\["OPENAI\_API\_KEY"\] = OPENAI\_API\_KEY

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham").load\_data()

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham").load\_data()

In \[ \]:

Copied!

from llama\_index.embeddings.huggingface import HuggingFaceEmbedding
from llama\_index.llms.openai import OpenAI
from llama\_index.core import Settings

Settings.llm \= OpenAI(model\="gpt-3.5-turbo")
Settings.embed\_model \= HuggingFaceEmbedding(
    model\_name\="BAAI/bge-small-en-v1.5"
)

from llama\_index.embeddings.huggingface import HuggingFaceEmbedding from llama\_index.llms.openai import OpenAI from llama\_index.core import Settings Settings.llm = OpenAI(model="gpt-3.5-turbo") Settings.embed\_model = HuggingFaceEmbedding( model\_name="BAAI/bge-small-en-v1.5" )

In \[ \]:

Copied!

\# build index
index \= VectorStoreIndex.from\_documents(documents\=documents)

\# build index index = VectorStoreIndex.from\_documents(documents=documents)

In \[ \]:

Copied!

from llama\_index.postprocessor.flag\_embedding\_reranker import (
    FlagEmbeddingReranker,
)

rerank \= FlagEmbeddingReranker(model\="BAAI/bge-reranker-large", top\_n\=5)

from llama\_index.postprocessor.flag\_embedding\_reranker import ( FlagEmbeddingReranker, ) rerank = FlagEmbeddingReranker(model="BAAI/bge-reranker-large", top\_n=5)

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

Elapsed: 5.37s

In \[ \]:

Copied!

print(response)

print(response)

The author applied to three grad schools: MIT, Yale, and Harvard. The reason for applying to these schools was because they were renowned for AI at the time and the author wanted to pursue a career in artificial intelligence.

In \[ \]:

Copied!

print(response.get\_formatted\_sources(length\=200))

print(response.get\_formatted\_sources(length=200))

\> Source (Doc id: f7e7f522-40ae-416a-917e-a70e59979105): I didn't want to drop out of grad school, but how else was I going to get out? I remember when my friend Robert Morris got kicked out of Cornell for writing the internet worm of 1988, I was envious...

> Source (Doc id: df6c6b73-b488-4506-9ab1-ae5e8d499d44): So I looked around to see what I could salvage from the wreckage of my plans, and there was Lisp. I knew from experience that Lisp was interesting for its own sake and not just for its association ...

> Source (Doc id: 8ee64ca0-3a8d-49d2-a41d-cbf1e10216fd): \[15\] We got 225 applications for the Summer Founders Program, and we were surprised to find that a lot of them were from people who'd already graduated, or were about to that spring. Already this S...

> Source (Doc id: e95b6077-628a-4422-baad-765638cb6978): It was as weird as it sounds. I resumed all my old patterns, except now there were doors where there hadn't been. Now when I was tired of walking, all I had to do was raise my hand, and (unless it ...

> Source (Doc id: 6c54f961-c5ff-466e-861a-66f5c1c25e36): I couldn't have put this into words when I was 18. All I knew at the time was that I kept taking philosophy courses and they kept being boring. So I decided to switch to AI.

AI was in the air in t...

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

Elapsed: 10.35s

In \[ \]:

Copied!

print(response)

print(response)

The author applied to three grad schools: MIT, Yale, and Harvard. They chose these schools based on their strong reputations in the field of AI at the time. Additionally, Harvard was appealing because it was where Bill Woods, the inventor of the parser used in the author's SHRDLU clone, was located.

In \[ \]:

Copied!

print(response.get\_formatted\_sources(length\=200))

print(response.get\_formatted\_sources(length=200))

\> Source (Doc id: f7e7f522-40ae-416a-917e-a70e59979105): I didn't want to drop out of grad school, but how else was I going to get out? I remember when my friend Robert Morris got kicked out of Cornell for writing the internet worm of 1988, I was envious...

> Source (Doc id: 6c54f961-c5ff-466e-861a-66f5c1c25e36): I couldn't have put this into words when I was 18. All I knew at the time was that I kept taking philosophy courses and they kept being boring. So I decided to switch to AI.

AI was in the air in t...

> Source (Doc id: d258db84-0975-4de0-a19b-752f529d9e5a): What I Worked On

February 2021

Before college the two main things I worked on, outside of school, were writing and programming. I didn't write essays. I wrote what beginning writers were supposed...

> Source (Doc id: 04582ebe-239a-432a-9304-611676593c66): It's not that unprestigious types of work are good per se. But when you find yourself drawn to some kind of work despite its current lack of prestige, it's a sign both that there's something real t...

> Source (Doc id: 8ee64ca0-3a8d-49d2-a41d-cbf1e10216fd): \[15\] We got 225 applications for the Summer Founders Program, and we were surprised to find that a lot of them were from people who'd already graduated, or were about to that spring. Already this S...

> Source (Doc id: d46b4c41-05f8-4492-b978-0ce1863a0f00): Now that I could write essays again, I wrote a bunch about topics I'd had stacked up. I kept writing essays through 2020, but I also started to think about other things I could work on. How should ...

> Source (Doc id: df6c6b73-b488-4506-9ab1-ae5e8d499d44): So I looked around to see what I could salvage from the wreckage of my plans, and there was Lisp. I knew from experience that Lisp was interesting for its own sake and not just for its association ...

> Source (Doc id: d91c08cf-6f7d-4ac5-8cf0-d8bcba4e77ff): It was missing a lot of things you'd want in a programming language. So these had to be added, and when they were, they weren't defined using McCarthy's original axiomatic approach. That wouldn't h...

> Source (Doc id: e95b6077-628a-4422-baad-765638cb6978): It was as weird as it sounds. I resumed all my old patterns, except now there were doors where there hadn't been. Now when I was tired of walking, all I had to do was raise my hand, and (unless it ...

> Source (Doc id: 027ba923-2307-4e28-8e6b-53be8e4db8ec): But Interleaf still had a few years to live yet. \[5\]

Interleaf had done something pretty bold. Inspired by Emacs, they'd added a scripting language, and even made the scripting language a dialect ...

As we can see, the query engine with reranking produced a much more concise output in much lower time (6s v.s. 10s). While both responses were essentially correct, the query engine without reranking included a lot of irrelevant information - a phenomenon we could attribute to "pollution of the context window".

Back to top

[Previous File Based Node Parsers](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/FileNodeProcessors/)[Next Jina Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/JinaRerank/)

Hi, how can I help you?

🦙
