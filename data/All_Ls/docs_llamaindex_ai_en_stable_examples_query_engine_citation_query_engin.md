Title: CitationQueryEngine - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/query_engine/citation_query_engine/

Markdown Content:
CitationQueryEngine - LlamaIndex


This notebook walks through how to use the CitationQueryEngine

The CitationQueryEngine can be used with any existing index.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-embeddings\-openai
%pip install llama\-index\-llms\-openai

%pip install llama-index-embeddings-openai %pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/citation_query_engine/#setup)
-------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

import os
from llama\_index.llms.openai import OpenAI
from llama\_index.core.query\_engine import CitationQueryEngine
from llama\_index.core.retrievers import VectorIndexRetriever
from llama\_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load\_index\_from\_storage,
)

import os from llama\_index.llms.openai import OpenAI from llama\_index.core.query\_engine import CitationQueryEngine from llama\_index.core.retrievers import VectorIndexRetriever from llama\_index.core import ( VectorStoreIndex, SimpleDirectoryReader, StorageContext, load\_index\_from\_storage, )

/home/loganm/miniconda3/envs/llama-index/lib/python3.11/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user\_install.html
  from .autonotebook import tqdm as notebook\_tqdm

In \[ \]:

Copied!

from llama\_index.embeddings.openai import OpenAIEmbedding
from llama\_index.llms.openai import OpenAI
from llama\_index.core import Settings

Settings.llm \= OpenAI(model\="gpt-3.5-turbo")
Settings.embed\_model \= OpenAIEmbedding(model\="text-embedding-3-small")

from llama\_index.embeddings.openai import OpenAIEmbedding from llama\_index.llms.openai import OpenAI from llama\_index.core import Settings Settings.llm = OpenAI(model="gpt-3.5-turbo") Settings.embed\_model = OpenAIEmbedding(model="text-embedding-3-small")

Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/citation_query_engine/#download-data)
-----------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

In \[ \]:

Copied!

if not os.path.exists("./citation"):
    documents \= SimpleDirectoryReader("./data/paul\_graham").load\_data()
    index \= VectorStoreIndex.from\_documents(
        documents,
    )
    index.storage\_context.persist(persist\_dir\="./citation")
else:
    index \= load\_index\_from\_storage(
        StorageContext.from\_defaults(persist\_dir\="./citation"),
    )

if not os.path.exists("./citation"): documents = SimpleDirectoryReader("./data/paul\_graham").load\_data() index = VectorStoreIndex.from\_documents( documents, ) index.storage\_context.persist(persist\_dir="./citation") else: index = load\_index\_from\_storage( StorageContext.from\_defaults(persist\_dir="./citation"), )

Create the CitationQueryEngine w/ Default Arguments[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/citation_query_engine/#create-the-citationqueryengine-w-default-arguments)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

query\_engine \= CitationQueryEngine.from\_args(
    index,
    similarity\_top\_k\=3,
    \# here we can control how granular citation sources are, the default is 512
    citation\_chunk\_size\=512,
)

query\_engine = CitationQueryEngine.from\_args( index, similarity\_top\_k=3, # here we can control how granular citation sources are, the default is 512 citation\_chunk\_size=512, )

In \[ \]:

Copied!

response \= query\_engine.query("What did the author do growing up?")

response = query\_engine.query("What did the author do growing up?")

In \[ \]:

Copied!

print(response)

print(response)

Before college, the author worked on writing short stories and programming on an IBM 1401 using an early version of Fortran \[1\]. They later got a TRS-80 computer and wrote simple games, a program to predict rocket heights, and a word processor \[2\].

In \[ \]:

Copied!

\# source nodes are 6, because the original chunks of 1024-sized nodes were broken into more granular nodes
print(len(response.source\_nodes))

\# source nodes are 6, because the original chunks of 1024-sized nodes were broken into more granular nodes print(len(response.source\_nodes))

6

### Inspecting the Actual Source[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/citation_query_engine/#inspecting-the-actual-source)

Sources start counting at 1, but python arrays start counting at zero!

Let's confirm the source makes sense.

In \[ \]:

Copied!

print(response.source\_nodes\[0\].node.get\_text())

print(response.source\_nodes\[0\].node.get\_text())

Source 1:
What I Worked On

February 2021

Before college the two main things I worked on, outside of school, were writing and programming. I didn't write essays. I wrote what beginning writers were supposed to write then, and probably still are: short stories. My stories were awful. They had hardly any plot, just characters with strong feelings, which I imagined made them deep.

The first programs I tried writing were on the IBM 1401 that our school district used for what was then called "data processing." This was in 9th grade, so I was 13 or 14. The school district's 1401 happened to be in the basement of our junior high school, and my friend Rich Draves and I got permission to use it. It was like a mini Bond villain's lair down there, with all these alien-looking machines — CPU, disk drives, printer, card reader — sitting up on a raised floor under bright fluorescent lights.

The language we used was an early version of Fortran. You had to type programs on punch cards, then stack them in the card reader and press a button to load the program into memory and run it. The result would ordinarily be to print something on the spectacularly loud printer.

I was puzzled by the 1401. I couldn't figure out what to do with it. And in retrospect there's not much I could have done with it. The only form of input to programs was data stored on punched cards, and I didn't have any data stored on punched cards. The only other option was to do things that didn't rely on any input, like calculate approximations of pi, but I didn't know enough math to do anything interesting of that type. So I'm not surprised I can't remember any programs I wrote, because they can't have done much. My clearest memory is of the moment I learned it was possible for programs not to terminate, when one of mine didn't. On a machine without time-sharing, this was a social as well as a technical error, as the data center manager's expression made clear.

With microcomputers, everything changed. Now you could have a computer sitting right in front of you, on a desk, that could respond to your keystrokes as it was running instead of just churning through a stack of punch cards and then stopping.

In \[ \]:

Copied!

print(response.source\_nodes\[1\].node.get\_text())

print(response.source\_nodes\[1\].node.get\_text())

Source 2:
\[1\]

The first of my friends to get a microcomputer built it himself. It was sold as a kit by Heathkit. I remember vividly how impressed and envious I felt watching him sitting in front of it, typing programs right into the computer.

Computers were expensive in those days and it took me years of nagging before I convinced my father to buy one, a TRS-80, in about 1980. The gold standard then was the Apple II, but a TRS-80 was good enough. This was when I really started programming. I wrote simple games, a program to predict how high my model rockets would fly, and a word processor that my father used to write at least one book. There was only room in memory for about 2 pages of text, so he'd write 2 pages at a time and then print them out, but it was a lot better than a typewriter.

Though I liked programming, I didn't plan to study it in college. In college I was going to study philosophy, which sounded much more powerful. It seemed, to my naive high school self, to be the study of the ultimate truths, compared to which the things studied in other fields would be mere domain knowledge. What I discovered when I got to college was that the other fields took up so much of the space of ideas that there wasn't much left for these supposed ultimate truths. All that seemed left for philosophy were edge cases that people in other fields felt could safely be ignored.

I couldn't have put this into words when I was 18. All I knew at the time was that I kept taking philosophy courses and they kept being boring. So I decided to switch to AI.

AI was in the air in the mid 1980s, but there were two things especially that made me want to work on it: a novel by Heinlein called The Moon is a Harsh Mistress, which featured an intelligent computer called Mike, and a PBS documentary that showed Terry Winograd using SHRDLU. I haven't tried rereading The

Adjusting Settings[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/citation_query_engine/#adjusting-settings)
---------------------------------------------------------------------------------------------------------------------------

Note that setting the chunk size larger than the original chunk size of the nodes will have no effect.

The default node chunk size is 1024, so here, we are not making our citation nodes any more granular.

In \[ \]:

Copied!

query\_engine \= CitationQueryEngine.from\_args(
    index,
    \# increase the citation chunk size!
    citation\_chunk\_size\=1024,
    similarity\_top\_k\=3,
)

query\_engine = CitationQueryEngine.from\_args( index, # increase the citation chunk size! citation\_chunk\_size=1024, similarity\_top\_k=3, )

In \[ \]:

Copied!

response \= query\_engine.query("What did the author do growing up?")

response = query\_engine.query("What did the author do growing up?")

In \[ \]:

Copied!

print(response)

print(response)

Before college, the author worked on writing short stories and programming on an IBM 1401 using an early version of Fortran \[1\].

In \[ \]:

Copied!

\# should be less source nodes now!
print(len(response.source\_nodes))

\# should be less source nodes now! print(len(response.source\_nodes))

3

### Inspecting the Actual Source[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/citation_query_engine/#inspecting-the-actual-source)

Sources start counting at 1, but python arrays start counting at zero!

Let's confirm the source makes sense.

In \[ \]:

Copied!

print(response.source\_nodes\[0\].node.get\_text())

print(response.source\_nodes\[0\].node.get\_text())

Source 1:
What I Worked On

February 2021

Before college the two main things I worked on, outside of school, were writing and programming. I didn't write essays. I wrote what beginning writers were supposed to write then, and probably still are: short stories. My stories were awful. They had hardly any plot, just characters with strong feelings, which I imagined made them deep.

The first programs I tried writing were on the IBM 1401 that our school district used for what was then called "data processing." This was in 9th grade, so I was 13 or 14. The school district's 1401 happened to be in the basement of our junior high school, and my friend Rich Draves and I got permission to use it. It was like a mini Bond villain's lair down there, with all these alien-looking machines — CPU, disk drives, printer, card reader — sitting up on a raised floor under bright fluorescent lights.

The language we used was an early version of Fortran. You had to type programs on punch cards, then stack them in the card reader and press a button to load the program into memory and run it. The result would ordinarily be to print something on the spectacularly loud printer.

I was puzzled by the 1401. I couldn't figure out what to do with it. And in retrospect there's not much I could have done with it. The only form of input to programs was data stored on punched cards, and I didn't have any data stored on punched cards. The only other option was to do things that didn't rely on any input, like calculate approximations of pi, but I didn't know enough math to do anything interesting of that type. So I'm not surprised I can't remember any programs I wrote, because they can't have done much. My clearest memory is of the moment I learned it was possible for programs not to terminate, when one of mine didn't. On a machine without time-sharing, this was a social as well as a technical error, as the data center manager's expression made clear.

With microcomputers, everything changed. Now you could have a computer sitting right in front of you, on a desk, that could respond to your keystrokes as it was running instead of just churning through a stack of punch cards and then stopping. \[1\]

The first of my friends to get a microcomputer built it himself. It was sold as a kit by Heathkit. I remember vividly how impressed and envious I felt watching him sitting in front of it, typing programs right into the computer.

Computers were expensive in those days and it took me years of nagging before I convinced my father to buy one, a TRS-80, in about 1980. The gold standard then was the Apple II, but a TRS-80 was good enough. This was when I really started programming. I wrote simple games, a program to predict how high my model rockets would fly, and a word processor that my father used to write at least one book. There was only room in memory for about 2 pages of text, so he'd write 2 pages at a time and then print them out, but it was a lot better than a typewriter.

Though I liked programming, I didn't plan to study it in college. In college I was going to study philosophy, which sounded much more powerful. It seemed, to my naive high school self, to be the study of the ultimate truths, compared to which the things studied in other fields would be mere domain knowledge. What I discovered when I got to college was that the other fields took up so much of the space of ideas that there wasn't much left for these supposed ultimate truths. All that seemed left for philosophy were edge cases that people in other fields felt could safely be ignored.

I couldn't have put this into words when I was 18. All I knew at the time was that I kept taking philosophy courses and they kept being boring. So I decided to switch to AI.

AI was in the air in the mid 1980s, but there were two things especially that made me want to work on it: a novel by Heinlein called The Moon is a Harsh Mistress, which featured an intelligent computer called Mike, and a PBS documentary that showed Terry Winograd using SHRDLU. I haven't tried rereading The

Back to top

[Previous SQL Router Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLRouterQueryEngine/)[Next Cogniswitch query engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/cogniswitch_query_engine/)
