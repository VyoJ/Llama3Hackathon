Title: Multi-Step Query Engine - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/query_transformations/SimpleIndexDemo-multistep/

Markdown Content:
Multi-Step Query Engine - LlamaIndex


We have a multi-step query engine that's able to decompose a complex query into sequential subquestions. This guide walks you through how to set it up!

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai

%pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

#### Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/query_transformations/SimpleIndexDemo-multistep/#download-data)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

#### Load documents, build the VectorStoreIndex[¶](https://docs.llamaindex.ai/en/stable/examples/query_transformations/SimpleIndexDemo-multistep/#load-documents-build-the-vectorstoreindex)

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..."

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.llms.openai import OpenAI
from IPython.display import Markdown, display

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.llms.openai import OpenAI from IPython.display import Markdown, display

In \[ \]:

Copied!

\# LLM (gpt-3.5)
gpt35 \= OpenAI(temperature\=0, model\="gpt-3.5-turbo")

\# LLM (gpt-4)
gpt4 \= OpenAI(temperature\=0, model\="gpt-4")

\# LLM (gpt-3.5) gpt35 = OpenAI(temperature=0, model="gpt-3.5-turbo") # LLM (gpt-4) gpt4 = OpenAI(temperature=0, model="gpt-4")

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data()

In \[ \]:

Copied!

index \= VectorStoreIndex.from\_documents(documents)

index = VectorStoreIndex.from\_documents(documents)

#### Query Index[¶](https://docs.llamaindex.ai/en/stable/examples/query_transformations/SimpleIndexDemo-multistep/#query-index)

In \[ \]:

Copied!

from llama\_index.core.indices.query.query\_transform.base import (
    StepDecomposeQueryTransform,
)

\# gpt-4
step\_decompose\_transform \= StepDecomposeQueryTransform(llm\=gpt4, verbose\=True)

\# gpt-3
step\_decompose\_transform\_gpt3 \= StepDecomposeQueryTransform(
    llm\=gpt35, verbose\=True
)

from llama\_index.core.indices.query.query\_transform.base import ( StepDecomposeQueryTransform, ) # gpt-4 step\_decompose\_transform = StepDecomposeQueryTransform(llm=gpt4, verbose=True) # gpt-3 step\_decompose\_transform\_gpt3 = StepDecomposeQueryTransform( llm=gpt35, verbose=True )

In \[ \]:

Copied!

index\_summary \= "Used to answer questions about the author"

index\_summary = "Used to answer questions about the author"

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
from llama\_index.core.query\_engine import MultiStepQueryEngine

query\_engine \= index.as\_query\_engine(llm\=gpt4)
query\_engine \= MultiStepQueryEngine(
    query\_engine\=query\_engine,
    query\_transform\=step\_decompose\_transform,
    index\_summary\=index\_summary,
)
response\_gpt4 \= query\_engine.query(
    "Who was in the first batch of the accelerator program the author"
    " started?",
)

\# set Logging to DEBUG for more detailed outputs from llama\_index.core.query\_engine import MultiStepQueryEngine query\_engine = index.as\_query\_engine(llm=gpt4) query\_engine = MultiStepQueryEngine( query\_engine=query\_engine, query\_transform=step\_decompose\_transform, index\_summary=index\_summary, ) response\_gpt4 = query\_engine.query( "Who was in the first batch of the accelerator program the author" " started?", )

\> Current query: Who was in the first batch of the accelerator program the author started?
\> New query: Who is the author of the accelerator program?
\> Current query: Who was in the first batch of the accelerator program the author started?
\> New query: Who was in the first batch of the accelerator program started by Paul Graham?
\> Current query: Who was in the first batch of the accelerator program the author started?
\> New query: None

In \[ \]:

Copied!

display(Markdown(f"<b>{response\_gpt4}</b>"))

display(Markdown(f"**{response\_gpt4}**"))

**In the first batch of the accelerator program started by the author, the participants included the founders of Reddit, Justin Kan and Emmett Shear who later founded Twitch, Aaron Swartz who had helped write the RSS spec and later became a martyr for open access, and Sam Altman who later became the second president of YC.**

In \[ \]:

Copied!

sub\_qa \= response\_gpt4.metadata\["sub\_qa"\]
tuples \= \[(t\[0\], t\[1\].response) for t in sub\_qa\]
print(tuples)

sub\_qa = response\_gpt4.metadata\["sub\_qa"\] tuples = \[(t\[0\], t\[1\].response) for t in sub\_qa\] print(tuples)

\[('Who is the author of the accelerator program?', 'The author of the accelerator program is Paul Graham.'), ('Who was in the first batch of the accelerator program started by Paul Graham?', 'The first batch of the accelerator program started by Paul Graham included the founders of Reddit, Justin Kan and Emmett Shear who later founded Twitch, Aaron Swartz who had helped write the RSS spec and later became a martyr for open access, and Sam Altman who later became the second president of YC.')\]

In \[ \]:

Copied!

response\_gpt4 \= query\_engine.query(
    "In which city did the author found his first company, Viaweb?",
)

response\_gpt4 = query\_engine.query( "In which city did the author found his first company, Viaweb?", )

\> Current query: In which city did the author found his first company, Viaweb?
\> New query: Who is the author who founded Viaweb?
\> Current query: In which city did the author found his first company, Viaweb?
\> New query: In which city did Paul Graham found his first company, Viaweb?
\> Current query: In which city did the author found his first company, Viaweb?
\> New query: None

In \[ \]:

Copied!

print(response\_gpt4)

print(response\_gpt4)

The author founded his first company, Viaweb, in Cambridge.

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(llm\=gpt35)
query\_engine \= MultiStepQueryEngine(
    query\_engine\=query\_engine,
    query\_transform\=step\_decompose\_transform\_gpt3,
    index\_summary\=index\_summary,
)

response\_gpt3 \= query\_engine.query(
    "In which city did the author found his first company, Viaweb?",
)

query\_engine = index.as\_query\_engine(llm=gpt35) query\_engine = MultiStepQueryEngine( query\_engine=query\_engine, query\_transform=step\_decompose\_transform\_gpt3, index\_summary=index\_summary, ) response\_gpt3 = query\_engine.query( "In which city did the author found his first company, Viaweb?", )

\> Current query: In which city did the author found his first company, Viaweb?
\> New query: None

In \[ \]:

Copied!

print(response\_gpt3)

print(response\_gpt3)

Empty Response

Back to top

[Previous HyDE Query Transform](https://docs.llamaindex.ai/en/stable/examples/query_transformations/HyDEQueryTransformDemo/)[Next Query Transform Cookbook](https://docs.llamaindex.ai/en/stable/examples/query_transformations/query_transform_cookbook/)
