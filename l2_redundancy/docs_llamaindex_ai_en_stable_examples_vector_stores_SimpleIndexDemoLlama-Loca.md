Title: Local Llama2 + VectorStoreIndex - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemoLlama-Local/

Markdown Content:
Local Llama2 + VectorStoreIndex - LlamaIndex


This notebook walks through the proper setup to use llama-2 with LlamaIndex locally. Note that you need a decent GPU to run this notebook, ideally an A100 with at least 40GB of memory.

Specifically, we look at using a vector store index.

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemoLlama-Local/#setup)
-------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

%pip install llama\-index\-llms\-huggingface
%pip install llama\-index\-embeddings\-huggingface

%pip install llama-index-llms-huggingface %pip install llama-index-embeddings-huggingface

In \[ \]:

Copied!

!pip install llama\-index ipywidgets

!pip install llama-index ipywidgets

### Set Up[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemoLlama-Local/#set-up)

**IMPORTANT**: Please sign in to HF hub with an account that has access to the llama2 models, using `huggingface-cli login` in your console. For more details, please see: [https://ai.meta.com/resources/models-and-libraries/llama-downloads/](https://ai.meta.com/resources/models-and-libraries/llama-downloads/).

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

from IPython.display import Markdown, display

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout)) from IPython.display import Markdown, display

In \[ \]:

Copied!

import torch
from llama\_index.llms.huggingface import HuggingFaceLLM
from llama\_index.core import PromptTemplate

\# Model names (make sure you have access on HF)
LLAMA2\_7B \= "meta-llama/Llama-2-7b-hf"
LLAMA2\_7B\_CHAT \= "meta-llama/Llama-2-7b-chat-hf"
LLAMA2\_13B \= "meta-llama/Llama-2-13b-hf"
LLAMA2\_13B\_CHAT \= "meta-llama/Llama-2-13b-chat-hf"
LLAMA2\_70B \= "meta-llama/Llama-2-70b-hf"
LLAMA2\_70B\_CHAT \= "meta-llama/Llama-2-70b-chat-hf"

selected\_model \= LLAMA2\_13B\_CHAT

SYSTEM\_PROMPT \= """You are an AI assistant that answers questions in a friendly manner, based on the given source documents. Here are some rules you always follow:
\- Generate human readable output, avoid creating output with gibberish text.
\- Generate only the requested output, don't include any other language before or after the requested output.
\- Never say thank you, that you are happy to help, that you are an AI agent, etc. Just answer directly.
\- Generate professional language typically used in business documents in North America.
\- Never generate offensive or foul language.
"""

query\_wrapper\_prompt \= PromptTemplate(
    "\[INST\]<<SYS>>\\n" + SYSTEM\_PROMPT + "<</SYS>>\\n\\n{query\_str}\[/INST\] "
)

llm \= HuggingFaceLLM(
    context\_window\=4096,
    max\_new\_tokens\=2048,
    generate\_kwargs\={"temperature": 0.0, "do\_sample": False},
    query\_wrapper\_prompt\=query\_wrapper\_prompt,
    tokenizer\_name\=selected\_model,
    model\_name\=selected\_model,
    device\_map\="auto",
    \# change these settings below depending on your GPU
    model\_kwargs\={"torch\_dtype": torch.float16, "load\_in\_8bit": True},
)

import torch from llama\_index.llms.huggingface import HuggingFaceLLM from llama\_index.core import PromptTemplate # Model names (make sure you have access on HF) LLAMA2\_7B = "meta-llama/Llama-2-7b-hf" LLAMA2\_7B\_CHAT = "meta-llama/Llama-2-7b-chat-hf" LLAMA2\_13B = "meta-llama/Llama-2-13b-hf" LLAMA2\_13B\_CHAT = "meta-llama/Llama-2-13b-chat-hf" LLAMA2\_70B = "meta-llama/Llama-2-70b-hf" LLAMA2\_70B\_CHAT = "meta-llama/Llama-2-70b-chat-hf" selected\_model = LLAMA2\_13B\_CHAT SYSTEM\_PROMPT = """You are an AI assistant that answers questions in a friendly manner, based on the given source documents. Here are some rules you always follow: - Generate human readable output, avoid creating output with gibberish text. - Generate only the requested output, don't include any other language before or after the requested output. - Never say thank you, that you are happy to help, that you are an AI agent, etc. Just answer directly. - Generate professional language typically used in business documents in North America. - Never generate offensive or foul language. """ query\_wrapper\_prompt = PromptTemplate( "\[INST\]<\>\\n" + SYSTEM\_PROMPT + "<\>\\n\\n{query\_str}\[/INST\] " ) llm = HuggingFaceLLM( context\_window=4096, max\_new\_tokens=2048, generate\_kwargs={"temperature": 0.0, "do\_sample": False}, query\_wrapper\_prompt=query\_wrapper\_prompt, tokenizer\_name=selected\_model, model\_name=selected\_model, device\_map="auto", # change these settings below depending on your GPU model\_kwargs={"torch\_dtype": torch.float16, "load\_in\_8bit": True}, )

In \[ \]:

Copied!

from llama\_index.embeddings.huggingface import HuggingFaceEmbedding

embed\_model \= HuggingFaceEmbedding(model\_name\="BAAI/bge-small-en-v1.5")

from llama\_index.embeddings.huggingface import HuggingFaceEmbedding embed\_model = HuggingFaceEmbedding(model\_name="BAAI/bge-small-en-v1.5")

In \[ \]:

Copied!

from llama\_index.core import Settings

Settings.llm \= llm
Settings.embed\_model \= embed\_model

from llama\_index.core import Settings Settings.llm = llm Settings.embed\_model = embed\_model

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

from llama\_index.core import SimpleDirectoryReader # load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data()

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex

index \= VectorStoreIndex.from\_documents(documents)

from llama\_index.core import VectorStoreIndex index = VectorStoreIndex.from\_documents(documents)

Querying[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemoLlama-Local/#querying)
-------------------------------------------------------------------------------------------------------------

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

**Growing up, the author wrote short stories, programmed on an IBM 1401, and eventually convinced his father to buy him a TRS-80 microcomputer. He wrote simple games, a program to predict how high his model rockets would fly, and a word processor. He studied philosophy in college, but eventually switched to AI. He wrote essays and published them online, and worked on spam filters and painting. He also hosted dinners for a group of friends every Thursday night and bought a building in Cambridge.**

### Streaming Support[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemoLlama-Local/#streaming-support)

In \[ \]:

Copied!

import time

query\_engine \= index.as\_query\_engine(streaming\=True)
response \= query\_engine.query("What happened at interleaf?")

start\_time \= time.time()

token\_count \= 0
for token in response.response\_gen:
    print(token, end\="")
    token\_count += 1

time\_elapsed \= time.time() \- start\_time
tokens\_per\_second \= token\_count / time\_elapsed

print(f"\\n\\nStreamed output at {tokens\_per\_second} tokens/s")

import time query\_engine = index.as\_query\_engine(streaming=True) response = query\_engine.query("What happened at interleaf?") start\_time = time.time() token\_count = 0 for token in response.response\_gen: print(token, end="") token\_count += 1 time\_elapsed = time.time() - start\_time tokens\_per\_second = token\_count / time\_elapsed print(f"\\n\\nStreamed output at {tokens\_per\_second} tokens/s")

At Interleaf, a group of people worked on projects for customers. One of the employees told the narrator about a new thing called HTML, which was a derivative of SGML. The narrator left Interleaf to pursue art school at RISD, but continued to do freelance work for the group. Eventually, the narrator and two of his friends, Robert and Trevor, started a new company called Viaweb to create a web app that allowed users to build stores through the browser. They opened for business in January 1996 with 6 stores. The software had three main parts: the editor, the shopping cart, and the manager.

Streamed output at 26.923490295496002 tokens/s

Back to top

[Previous Simple Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemo/)[Next Llama2 + VectorStoreIndex](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemoLlama2/)
