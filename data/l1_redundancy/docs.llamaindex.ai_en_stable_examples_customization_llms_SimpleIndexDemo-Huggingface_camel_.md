Title: HuggingFace LLM - Camel-5b - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-Huggingface_camel/

Markdown Content:
HuggingFace LLM - Camel-5b - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-huggingface

%pip install llama-index-llms-huggingface

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.llms.huggingface import HuggingFaceLLM
from llama\_index.core import Settings

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout)) from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.llms.huggingface import HuggingFaceLLM from llama\_index.core import Settings

INFO:numexpr.utils:Note: NumExpr detected 16 cores but "NUMEXPR\_MAX\_THREADS" not set, so enforcing safe limit of 8.
Note: NumExpr detected 16 cores but "NUMEXPR\_MAX\_THREADS" not set, so enforcing safe limit of 8.
INFO:numexpr.utils:NumExpr defaulting to 8 threads.
NumExpr defaulting to 8 threads.

/home/loganm/miniconda3/envs/gpt\_index/lib/python3.11/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user\_install.html
  from .autonotebook import tqdm as notebook\_tqdm

#### Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-Huggingface_camel/#download-data)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

#### Load documents, build the VectorStoreIndex[¶](https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-Huggingface_camel/#load-documents-build-the-vectorstoreindex)

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data()

In \[ \]:

Copied!

\# setup prompts - specific to StableLM
from llama\_index.core import PromptTemplate

\# This will wrap the default prompts that are internal to llama-index
\# taken from https://huggingface.co/Writer/camel-5b-hf
query\_wrapper\_prompt \= PromptTemplate(
    "Below is an instruction that describes a task. "
    "Write a response that appropriately completes the request.\\n\\n"
    "### Instruction:\\n{query\_str}\\n\\n\### Response:"
)

\# setup prompts - specific to StableLM from llama\_index.core import PromptTemplate # This will wrap the default prompts that are internal to llama-index # taken from https://huggingface.co/Writer/camel-5b-hf query\_wrapper\_prompt = PromptTemplate( "Below is an instruction that describes a task. " "Write a response that appropriately completes the request.\\n\\n" "### Instruction:\\n{query\_str}\\n\\n### Response:" )

In \[ \]:

Copied!

import torch

llm \= HuggingFaceLLM(
    context\_window\=2048,
    max\_new\_tokens\=256,
    generate\_kwargs\={"temperature": 0.25, "do\_sample": False},
    query\_wrapper\_prompt\=query\_wrapper\_prompt,
    tokenizer\_name\="Writer/camel-5b-hf",
    model\_name\="Writer/camel-5b-hf",
    device\_map\="auto",
    tokenizer\_kwargs\={"max\_length": 2048},
    \# uncomment this if using CUDA to reduce memory usage
    \# model\_kwargs={"torch\_dtype": torch.float16}
)

Settings.chunk\_size \= 512
Settings.llm \= llm

import torch llm = HuggingFaceLLM( context\_window=2048, max\_new\_tokens=256, generate\_kwargs={"temperature": 0.25, "do\_sample": False}, query\_wrapper\_prompt=query\_wrapper\_prompt, tokenizer\_name="Writer/camel-5b-hf", model\_name="Writer/camel-5b-hf", device\_map="auto", tokenizer\_kwargs={"max\_length": 2048}, # uncomment this if using CUDA to reduce memory usage # model\_kwargs={"torch\_dtype": torch.float16} ) Settings.chunk\_size = 512 Settings.llm = llm

Loading checkpoint shards: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3/3 \[00:43<00:00, 14.34s/it\]

In \[ \]:

Copied!

index \= VectorStoreIndex.from\_documents(documents)

index = VectorStoreIndex.from\_documents(documents)

INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total embedding token usage: 27212 tokens
> \[build\_index\_from\_nodes\] Total embedding token usage: 27212 tokens

#### Query Index[¶](https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-Huggingface_camel/#query-index)

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did the author do growing up?")

\# set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine() response = query\_engine.query("What did the author do growing up?")

INFO:llama\_index.token\_counter.token\_counter:> \[retrieve\] Total LLM token usage: 0 tokens
> \[retrieve\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[retrieve\] Total embedding token usage: 8 tokens
> \[retrieve\] Total embedding token usage: 8 tokens

Token indices sequence length is longer than the specified maximum sequence length for this model (954 > 512). Running this sequence through the model will result in indexing errors
Setting \`pad\_token\_id\` to \`eos\_token\_id\`:50256 for open-end generation.

INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total LLM token usage: 1026 tokens
> \[get\_response\] Total LLM token usage: 1026 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total embedding token usage: 0 tokens
> \[get\_response\] Total embedding token usage: 0 tokens

In \[ \]:

Copied!

print(response)

print(response)

The author grew up in a small town in England, attended a prestigious private school, and then went to Cambridge University, where he studied computer science. Afterward, he worked on web infrastructure, wrote essays, and then realized he could write about startups. He then started giving talks, wrote a book, and started interviewing founders for a book on startups.

#### Query Index - Streaming[¶](https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-Huggingface_camel/#query-index-streaming)

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(streaming\=True)

query\_engine = index.as\_query\_engine(streaming=True)

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
response\_stream \= query\_engine.query("What did the author do growing up?")

\# set Logging to DEBUG for more detailed outputs response\_stream = query\_engine.query("What did the author do growing up?")

INFO:llama\_index.token\_counter.token\_counter:> \[retrieve\] Total LLM token usage: 0 tokens
> \[retrieve\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[retrieve\] Total embedding token usage: 8 tokens
> \[retrieve\] Total embedding token usage: 8 tokens

Setting \`pad\_token\_id\` to \`eos\_token\_id\`:50256 for open-end generation.

INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total LLM token usage: 0 tokens
> \[get\_response\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total embedding token usage: 0 tokens
> \[get\_response\] Total embedding token usage: 0 tokens

In \[ \]:

Copied!

\# can be slower to start streaming since llama-index often involves many LLM calls
response\_stream.print\_response\_stream()

\# can be slower to start streaming since llama-index often involves many LLM calls response\_stream.print\_response\_stream()

The author grew up in a small town in England, attended a prestigious private school, and then went to Cambridge University, where he studied computer science. Afterward, he worked on web infrastructure, wrote essays, and then realized he could write about startups. He then started giving talks, wrote a book, and started interviewing founders for a book on startups.<|endoftext|>

In \[ \]:

Copied!

\# can also get a normal response object
response \= response\_stream.get\_response()
print(response)

\# can also get a normal response object response = response\_stream.get\_response() print(response)

In \[ \]:

Copied!

\# can also iterate over the generator yourself
generated\_text \= ""
for text in response.response\_gen:
    generated\_text += text

\# can also iterate over the generator yourself generated\_text = "" for text in response.response\_gen: generated\_text += text

Back to top

[Previous ChatGPT](https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-ChatGPT/)[Next HuggingFace LLM - StableLM](https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-Huggingface_stablelm/)
