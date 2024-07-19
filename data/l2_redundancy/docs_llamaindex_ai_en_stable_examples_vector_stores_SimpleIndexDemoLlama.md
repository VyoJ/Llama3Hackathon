Title: Llama2 + VectorStoreIndex - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemoLlama2/

Markdown Content:
Llama2 + VectorStoreIndex - LlamaIndex


This notebook walks through the proper setup to use llama-2 with LlamaIndex. Specifically, we look at using a vector store index.

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemoLlama2/#setup)
--------------------------------------------------------------------------------------------------

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-replicate

%pip install llama-index-llms-replicate

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

### Keys[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemoLlama2/#keys)

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."
os.environ\["REPLICATE\_API\_TOKEN"\] \= "YOUR\_REPLICATE\_TOKEN"

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..." os.environ\["REPLICATE\_API\_TOKEN"\] = "YOUR\_REPLICATE\_TOKEN"

### Load documents, build the VectorStoreIndex[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemoLlama2/#load-documents-build-the-vectorstoreindex)

In \[ \]:

Copied!

\# Optional logging
\# import logging
\# import sys

\# logging.basicConfig(stream=sys.stdout, level=logging.INFO)
\# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader

from IPython.display import Markdown, display

\# Optional logging # import logging # import sys # logging.basicConfig(stream=sys.stdout, level=logging.INFO) # logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout)) from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from IPython.display import Markdown, display

In \[ \]:

Copied!

from llama\_index.llms.replicate import Replicate
from llama\_index.core.llms.llama\_utils import (
    messages\_to\_prompt,
    completion\_to\_prompt,
)

\# The replicate endpoint
LLAMA\_13B\_V2\_CHAT \= "a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5"

\# inject custom system prompt into llama-2
def custom\_completion\_to\_prompt(completion: str) \-> str:
    return completion\_to\_prompt(
        completion,
        system\_prompt\=(
            "You are a Q&A assistant. Your goal is to answer questions as "
            "accurately as possible is the instructions and context provided."
        ),
    )

llm \= Replicate(
    model\=LLAMA\_13B\_V2\_CHAT,
    temperature\=0.01,
    \# override max tokens since it's interpreted
    \# as context window instead of max tokens
    context\_window\=4096,
    \# override completion representation for llama 2
    completion\_to\_prompt\=custom\_completion\_to\_prompt,
    \# if using llama 2 for data agents, also override the message representation
    messages\_to\_prompt\=messages\_to\_prompt,
)

from llama\_index.llms.replicate import Replicate from llama\_index.core.llms.llama\_utils import ( messages\_to\_prompt, completion\_to\_prompt, ) # The replicate endpoint LLAMA\_13B\_V2\_CHAT = "a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5" # inject custom system prompt into llama-2 def custom\_completion\_to\_prompt(completion: str) -> str: return completion\_to\_prompt( completion, system\_prompt=( "You are a Q&A assistant. Your goal is to answer questions as " "accurately as possible is the instructions and context provided." ), ) llm = Replicate( model=LLAMA\_13B\_V2\_CHAT, temperature=0.01, # override max tokens since it's interpreted # as context window instead of max tokens context\_window=4096, # override completion representation for llama 2 completion\_to\_prompt=custom\_completion\_to\_prompt, # if using llama 2 for data agents, also override the message representation messages\_to\_prompt=messages\_to\_prompt, )

In \[ \]:

Copied!

from llama\_index.core import Settings

Settings.llm \= llm

from llama\_index.core import Settings Settings.llm = llm

Download Data

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data()

In \[ \]:

Copied!

index \= VectorStoreIndex.from\_documents(documents)

index = VectorStoreIndex.from\_documents(documents)

Querying[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemoLlama2/#querying)
--------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine()

\# set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine()

In \[ \]:

Copied!

response \= query\_engine.query("What did the author do growing up?")
display(Markdown(f"<b>{response}</b>"))

response = query\_engine.query("What did the author do growing up?") display(Markdown(f"**{response}**"))

**Based on the context information provided, the author's activities growing up were:**

1.  Writing short stories, which were "awful" and had "hardly any plot."
2.  Programming on an IBM 1401 computer in 9th grade, using an early version of Fortran language.
3.  Building simple games, a program to predict the height of model rockets, and a word processor for his father.
4.  Reading science fiction novels, such as "The Moon is a Harsh Mistress" by Heinlein, which inspired him to work on AI.
5.  Living in Florence, Italy, and walking through the city's streets to the Accademia.

Please note that these activities are mentioned in the text and are not based on prior knowledge or assumptions.

### Streaming Support[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemoLlama2/#streaming-support)

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(streaming\=True)
response \= query\_engine.query("What happened at interleaf?")
for token in response.response\_gen:
    print(token, end\="")

query\_engine = index.as\_query\_engine(streaming=True) response = query\_engine.query("What happened at interleaf?") for token in response.response\_gen: print(token, end="")

 Based on the context information provided, it appears that the author worked at Interleaf, a company that made software for creating and managing documents. The author mentions that Interleaf was "on the way down" and that the company's Release Engineering group was large compared to the group that actually wrote the software. It is inferred that Interleaf was experiencing financial difficulties and that the author was nervous about money. However, there is no explicit mention of what specifically happened at Interleaf.

Back to top

[Previous Local Llama2 + VectorStoreIndex](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemoLlama-Local/)[Next Simple Vector Stores - Maximum Marginal Relevance Retrieval](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemoMMR/)
