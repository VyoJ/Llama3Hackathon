Title: HuggingFace LLM - StableLM - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-Huggingface_stablelm/

Markdown Content:
HuggingFace LLM - StableLM - LlamaIndex


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

#### Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-Huggingface_stablelm/#download-data)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

#### Load documents, build the VectorStoreIndex[¶](https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-Huggingface_stablelm/#load-documents-build-the-vectorstoreindex)

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham").load\_data()

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham").load\_data()

In \[ \]:

Copied!

\# setup prompts - specific to StableLM
from llama\_index.core import PromptTemplate

system\_prompt \= """<|SYSTEM|># StableLM Tuned (Alpha version)
\- StableLM is a helpful and harmless open-source AI language model developed by StabilityAI.
\- StableLM is excited to be able to help the user, but will refuse to do anything that could be considered harmful to the user.
\- StableLM is more than just an information source, StableLM is also able to write poetry, short stories, and make jokes.
\- StableLM will refuse to participate in anything that could harm a human.
"""

\# This will wrap the default prompts that are internal to llama-index
query\_wrapper\_prompt \= PromptTemplate("<|USER|>{query\_str}<|ASSISTANT|>")

\# setup prompts - specific to StableLM from llama\_index.core import PromptTemplate system\_prompt = """<|SYSTEM|># StableLM Tuned (Alpha version) - StableLM is a helpful and harmless open-source AI language model developed by StabilityAI. - StableLM is excited to be able to help the user, but will refuse to do anything that could be considered harmful to the user. - StableLM is more than just an information source, StableLM is also able to write poetry, short stories, and make jokes. - StableLM will refuse to participate in anything that could harm a human. """ # This will wrap the default prompts that are internal to llama-index query\_wrapper\_prompt = PromptTemplate("<|USER|>{query\_str}<|ASSISTANT|>")

In \[ \]:

Copied!

import torch

llm \= HuggingFaceLLM(
    context\_window\=4096,
    max\_new\_tokens\=256,
    generate\_kwargs\={"temperature": 0.7, "do\_sample": False},
    system\_prompt\=system\_prompt,
    query\_wrapper\_prompt\=query\_wrapper\_prompt,
    tokenizer\_name\="StabilityAI/stablelm-tuned-alpha-3b",
    model\_name\="StabilityAI/stablelm-tuned-alpha-3b",
    device\_map\="auto",
    stopping\_ids\=\[50278, 50279, 50277, 1, 0\],
    tokenizer\_kwargs\={"max\_length": 4096},
    \# uncomment this if using CUDA to reduce memory usage
    \# model\_kwargs={"torch\_dtype": torch.float16}
)

Settings.llm \= llm
Settings.chunk\_size \= 1024

import torch llm = HuggingFaceLLM( context\_window=4096, max\_new\_tokens=256, generate\_kwargs={"temperature": 0.7, "do\_sample": False}, system\_prompt=system\_prompt, query\_wrapper\_prompt=query\_wrapper\_prompt, tokenizer\_name="StabilityAI/stablelm-tuned-alpha-3b", model\_name="StabilityAI/stablelm-tuned-alpha-3b", device\_map="auto", stopping\_ids=\[50278, 50279, 50277, 1, 0\], tokenizer\_kwargs={"max\_length": 4096}, # uncomment this if using CUDA to reduce memory usage # model\_kwargs={"torch\_dtype": torch.float16} ) Settings.llm = llm Settings.chunk\_size = 1024

Loading checkpoint shards: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 \[00:24<00:00, 12.21s/it\]

In \[ \]:

Copied!

index \= VectorStoreIndex.from\_documents(documents)

index = VectorStoreIndex.from\_documents(documents)

INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total embedding token usage: 20729 tokens
> \[build\_index\_from\_nodes\] Total embedding token usage: 20729 tokens

#### Query Index[¶](https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-Huggingface_stablelm/#query-index)

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

Setting \`pad\_token\_id\` to \`eos\_token\_id\`:0 for open-end generation.

INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total LLM token usage: 2126 tokens
> \[get\_response\] Total LLM token usage: 2126 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total embedding token usage: 0 tokens
> \[get\_response\] Total embedding token usage: 0 tokens

In \[ \]:

Copied!

print(response)

print(response)

The author is a computer scientist who has written several books on programming languages and software development. He worked on the IBM 1401 and wrote a program to calculate pi. He also wrote a program to predict how high a rocket ship would fly. The program was written in Fortran and used a TRS-80 microcomputer. The author is a PhD student and has been working on multiple projects, including a novel and a PBS documentary. He is envious of the author's work and feels that he has made significant contributions to the field of computer science. He is working on multiple projects and is envious of the author's work. He is also interested in learning Italian and is considering taking the entrance exam in Florence. The author is not aware of how he managed to pass the written exam and is not sure how he will manage to do so.

#### Query Index - Streaming[¶](https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-Huggingface_stablelm/#query-index-streaming)

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
INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total LLM token usage: 0 tokens

Setting \`pad\_token\_id\` to \`eos\_token\_id\`:0 for open-end generation.

\> \[get\_response\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total embedding token usage: 0 tokens
> \[get\_response\] Total embedding token usage: 0 tokens

In \[ \]:

Copied!

\# can be slower to start streaming since llama-index often involves many LLM calls
response\_stream.print\_response\_stream()

\# can be slower to start streaming since llama-index often involves many LLM calls response\_stream.print\_response\_stream()

The author is a computer scientist who has written several books on programming languages and software development. He worked on the IBM 1401 and wrote a program to calculate pi. He also wrote a program to predict how high a rocket ship would fly. The program was written in Fortran and used a TRS-80 microcomputer. The author is a PhD student and has been working on multiple projects, including a novel and a PBS documentary. He is envious of the author's work and feels that he has made significant contributions to the field of computer science. He is working on multiple projects and is envious of the author's work. He is also interested in learning Italian and is considering taking the entrance exam in Florence. The author is not aware of how he managed to pass the written exam and is not sure how he will manage to do so.<|USER|>

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

[Previous HuggingFace LLM - Camel-5b](https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-Huggingface_camel/)[Next Chat Prompts Customization](https://docs.llamaindex.ai/en/stable/examples/customization/prompts/chat_prompts/)
