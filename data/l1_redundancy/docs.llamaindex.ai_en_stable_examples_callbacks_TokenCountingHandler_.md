Title: Token Counting Handler - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/callbacks/TokenCountingHandler/

Markdown Content:
Token Counting Handler - LlamaIndex


This notebook walks through how to use the TokenCountingHandler and how it can be used to track your prompt, completion, and embedding token usage over time.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai

%pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/TokenCountingHandler/#setup)
---------------------------------------------------------------------------------------------

Here, we setup the callback and the serivce context. We set global settings so that we don't have to worry about passing it into indexes and queries.

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..."

In \[ \]:

Copied!

import tiktoken
from llama\_index.core.callbacks import CallbackManager, TokenCountingHandler
from llama\_index.llms.openai import OpenAI
from llama\_index.core import Settings

token\_counter \= TokenCountingHandler(
    tokenizer\=tiktoken.encoding\_for\_model("gpt-3.5-turbo").encode
)

Settings.llm \= OpenAI(model\="gpt-3.5-turbo", temperature\=0.2)
Settings.callback\_manager \= CallbackManager(\[token\_counter\])

import tiktoken from llama\_index.core.callbacks import CallbackManager, TokenCountingHandler from llama\_index.llms.openai import OpenAI from llama\_index.core import Settings token\_counter = TokenCountingHandler( tokenizer=tiktoken.encoding\_for\_model("gpt-3.5-turbo").encode ) Settings.llm = OpenAI(model="gpt-3.5-turbo", temperature=0.2) Settings.callback\_manager = CallbackManager(\[token\_counter\])

Token Counting[¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/TokenCountingHandler/#token-counting)
---------------------------------------------------------------------------------------------------------------

The token counter will track embedding, prompt, and completion token usage. The token counts are **cummulative** and are only reset when you choose to do so, with `token_counter.reset_counts()`.

### Embedding Token Usage[¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/TokenCountingHandler/#embedding-token-usage)

Now that the settings is setup, let's track our embedding token usage.

Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/TokenCountingHandler/#download-data)
-------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

documents \= SimpleDirectoryReader("./data/paul\_graham").load\_data()

from llama\_index.core import SimpleDirectoryReader documents = SimpleDirectoryReader("./data/paul\_graham").load\_data()

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex

index \= VectorStoreIndex.from\_documents(documents)

from llama\_index.core import VectorStoreIndex index = VectorStoreIndex.from\_documents(documents)

In \[ \]:

Copied!

print(token\_counter.total\_embedding\_token\_count)

print(token\_counter.total\_embedding\_token\_count)

20723

That looks right! Before we go any further, lets reset the counts

In \[ \]:

Copied!

token\_counter.reset\_counts()

token\_counter.reset\_counts()

### LLM + Embedding Token Usage[¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/TokenCountingHandler/#llm-embedding-token-usage)

Next, let's test a query and see what the counts look like.

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(similarity\_top\_k\=4)
response \= query\_engine.query("What did the author do growing up?")

query\_engine = index.as\_query\_engine(similarity\_top\_k=4) response = query\_engine.query("What did the author do growing up?")

In \[ \]:

Copied!

print(
    "Embedding Tokens: ",
    token\_counter.total\_embedding\_token\_count,
    "\\n",
    "LLM Prompt Tokens: ",
    token\_counter.prompt\_llm\_token\_count,
    "\\n",
    "LLM Completion Tokens: ",
    token\_counter.completion\_llm\_token\_count,
    "\\n",
    "Total LLM Token Count: ",
    token\_counter.total\_llm\_token\_count,
    "\\n",
)

print( "Embedding Tokens: ", token\_counter.total\_embedding\_token\_count, "\\n", "LLM Prompt Tokens: ", token\_counter.prompt\_llm\_token\_count, "\\n", "LLM Completion Tokens: ", token\_counter.completion\_llm\_token\_count, "\\n", "Total LLM Token Count: ", token\_counter.total\_llm\_token\_count, "\\n", )

Embedding Tokens:  8 
 LLM Prompt Tokens:  4518 
 LLM Completion Tokens:  45 
 Total LLM Token Count:  4563 

### Token Counting + Streaming![¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/TokenCountingHandler/#token-counting-streaming)

The token counting handler also handles token counting during streaming.

Here, token counting will only happen once the stream is completed.

In \[ \]:

Copied!

token\_counter.reset\_counts()

query\_engine \= index.as\_query\_engine(similarity\_top\_k\=4, streaming\=True)
response \= query\_engine.query("What happened at Interleaf?")

\# finish the stream
for token in response.response\_gen:
    \# print(token, end="", flush=True)
    continue

token\_counter.reset\_counts() query\_engine = index.as\_query\_engine(similarity\_top\_k=4, streaming=True) response = query\_engine.query("What happened at Interleaf?") # finish the stream for token in response.response\_gen: # print(token, end="", flush=True) continue

In \[ \]:

Copied!

print(
    "Embedding Tokens: ",
    token\_counter.total\_embedding\_token\_count,
    "\\n",
    "LLM Prompt Tokens: ",
    token\_counter.prompt\_llm\_token\_count,
    "\\n",
    "LLM Completion Tokens: ",
    token\_counter.completion\_llm\_token\_count,
    "\\n",
    "Total LLM Token Count: ",
    token\_counter.total\_llm\_token\_count,
    "\\n",
)

print( "Embedding Tokens: ", token\_counter.total\_embedding\_token\_count, "\\n", "LLM Prompt Tokens: ", token\_counter.prompt\_llm\_token\_count, "\\n", "LLM Completion Tokens: ", token\_counter.completion\_llm\_token\_count, "\\n", "Total LLM Token Count: ", token\_counter.total\_llm\_token\_count, "\\n", )

Embedding Tokens:  6 
 LLM Prompt Tokens:  4563 
 LLM Completion Tokens:  123 
 Total LLM Token Count:  4686 

Advanced Usage[¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/TokenCountingHandler/#advanced-usage)
---------------------------------------------------------------------------------------------------------------

The token counter tracks each token usage event in an object called a `TokenCountingEvent`. This object has the following attributes:

*   prompt -> The prompt string sent to the LLM or Embedding model
*   prompt\_token\_count -> The token count of the LLM prompt
*   completion -> The string completion received from the LLM (not used for embeddings)
*   completion\_token\_count -> The token count of the LLM completion (not used for embeddings)
*   total\_token\_count -> The total prompt + completion tokens for the event
*   event\_id -> A string ID for the event, which aligns with other callback handlers

These events are tracked on the token counter in two lists:

*   llm\_token\_counts
*   embedding\_token\_counts

Let's explore what these look like!

In \[ \]:

Copied!

print("Num LLM token count events: ", len(token\_counter.llm\_token\_counts))
print(
    "Num Embedding token count events: ",
    len(token\_counter.embedding\_token\_counts),
)

print("Num LLM token count events: ", len(token\_counter.llm\_token\_counts)) print( "Num Embedding token count events: ", len(token\_counter.embedding\_token\_counts), )

Num LLM token count events:  2
Num Embedding token count events:  1

This makes sense! The previous query embedded the query text, and then made 2 LLM calls (since the top k was 4, and the default chunk size is 1024, two seperate calls need to be made so the LLM can read all the retrieved text).

Next, let's quickly see what these events look like for a single event.

In \[ \]:

Copied!

print("prompt: ", token\_counter.llm\_token\_counts\[0\].prompt\[:100\], "...\\n")
print(
    "prompt token count: ",
    token\_counter.llm\_token\_counts\[0\].prompt\_token\_count,
    "\\n",
)

print(
    "completion: ", token\_counter.llm\_token\_counts\[0\].completion\[:100\], "...\\n"
)
print(
    "completion token count: ",
    token\_counter.llm\_token\_counts\[0\].completion\_token\_count,
    "\\n",
)

print("total token count", token\_counter.llm\_token\_counts\[0\].total\_token\_count)

print("prompt: ", token\_counter.llm\_token\_counts\[0\].prompt\[:100\], "...\\n") print( "prompt token count: ", token\_counter.llm\_token\_counts\[0\].prompt\_token\_count, "\\n", ) print( "completion: ", token\_counter.llm\_token\_counts\[0\].completion\[:100\], "...\\n" ) print( "completion token count: ", token\_counter.llm\_token\_counts\[0\].completion\_token\_count, "\\n", ) print("total token count", token\_counter.llm\_token\_counts\[0\].total\_token\_count)

prompt:  system: You are an expert Q&A system that is trusted around the world.
Always answer the query using ...

prompt token count:  3873 

completion:  assistant: At Interleaf, the company had added a scripting language inspired by Emacs and made it a  ...

completion token count:  95 

total token count 3968

Back to top

[Previous PromptLayer Handler](https://docs.llamaindex.ai/en/stable/examples/callbacks/PromptLayerHandler/)[Next UpTrain Callback Handler](https://docs.llamaindex.ai/en/stable/examples/callbacks/UpTrainCallback/)
