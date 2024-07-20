Title: ChatGPT - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-ChatGPT/

Markdown Content:
ChatGPT - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai

%pip install llama-index-llms-openai

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
from llama\_index.core import Settings
from llama\_index.llms.openai import OpenAI
from IPython.display import Markdown, display

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout)) from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.core import Settings from llama\_index.llms.openai import OpenAI from IPython.display import Markdown, display

#### Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-ChatGPT/#download-data)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

#### Load documents, build the VectorStoreIndex[¶](https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-ChatGPT/#load-documents-build-the-vectorstoreindex)

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham").load\_data()

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham").load\_data()

In \[ \]:

Copied!

\# set global settings config
llm \= OpenAI(temperature\=0, model\="gpt-3.5-turbo")
Settings.llm \= llm
Settings.chunk\_size \= 512

\# set global settings config llm = OpenAI(temperature=0, model="gpt-3.5-turbo") Settings.llm = llm Settings.chunk\_size = 512

In \[ \]:

Copied!

index \= VectorStoreIndex.from\_documents(documents)

index = VectorStoreIndex.from\_documents(documents)

#### Query Index[¶](https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-ChatGPT/#query-index)

By default, with the help of langchain's PromptSelector abstraction, we use a modified refine prompt tailored for ChatGPT-use if the ChatGPT model is used.

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(
    similarity\_top\_k\=3,
    streaming\=True,
)
response \= query\_engine.query(
    "What did the author do growing up?",
)

query\_engine = index.as\_query\_engine( similarity\_top\_k=3, streaming=True, ) response = query\_engine.query( "What did the author do growing up?", )

INFO:llama\_index.token\_counter.token\_counter:> \[retrieve\] Total LLM token usage: 0 tokens
> \[retrieve\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[retrieve\] Total embedding token usage: 8 tokens
> \[retrieve\] Total embedding token usage: 8 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total LLM token usage: 0 tokens
> \[get\_response\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total embedding token usage: 0 tokens
> \[get\_response\] Total embedding token usage: 0 tokens

In \[ \]:

Copied!

response.print\_response\_stream()

response.print\_response\_stream()

Before college, the author worked on writing short stories and programming on an IBM 1401 using an early version of Fortran. They also worked on programming with microcomputers and eventually created a new dialect of Lisp called Arc. They later realized the potential of publishing essays on the web and began writing and publishing them. The author also worked on spam filters, painting, and cooking for groups.

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(
    similarity\_top\_k\=5,
    streaming\=True,
)
response \= query\_engine.query(
    "What did the author do during his time at RISD?",
)

query\_engine = index.as\_query\_engine( similarity\_top\_k=5, streaming=True, ) response = query\_engine.query( "What did the author do during his time at RISD?", )

INFO:llama\_index.token\_counter.token\_counter:> \[retrieve\] Total LLM token usage: 0 tokens
> \[retrieve\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[retrieve\] Total embedding token usage: 12 tokens
> \[retrieve\] Total embedding token usage: 12 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total LLM token usage: 0 tokens
> \[get\_response\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total embedding token usage: 0 tokens
> \[get\_response\] Total embedding token usage: 0 tokens

In \[ \]:

Copied!

response.print\_response\_stream()

response.print\_response\_stream()

The author attended RISD and took classes in fundamental subjects like drawing, color, and design. They also learned a lot in the color class they took, but otherwise, they were basically teaching themselves to paint. The author dropped out of RISD in 1993.

**Refine Prompt**: Here is the chat refine prompt

In \[ \]:

Copied!

from llama\_index.core.prompts.chat\_prompts import CHAT\_REFINE\_PROMPT

from llama\_index.core.prompts.chat\_prompts import CHAT\_REFINE\_PROMPT

In \[ \]:

Copied!

dict(CHAT\_REFINE\_PROMPT.prompt)

dict(CHAT\_REFINE\_PROMPT.prompt)

#### Query Index (Using the standard Refine Prompt)[¶](https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-ChatGPT/#query-index-using-the-standard-refine-prompt)

If we use the "standard" refine prompt (where the prompt is one text template instead of multiple messages), we find that the results over ChatGPT are worse.

In \[ \]:

Copied!

from llama\_index.core.prompts.default\_prompts import DEFAULT\_REFINE\_PROMPT

from llama\_index.core.prompts.default\_prompts import DEFAULT\_REFINE\_PROMPT

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(
    refine\_template\=DEFAULT\_REFINE\_PROMPT,
    similarity\_top\_k\=5,
    streaming\=True,
)
response \= query\_engine.query(
    "What did the author do during his time at RISD?",
)

query\_engine = index.as\_query\_engine( refine\_template=DEFAULT\_REFINE\_PROMPT, similarity\_top\_k=5, streaming=True, ) response = query\_engine.query( "What did the author do during his time at RISD?", )

In \[ \]:

Copied!

response.print\_response\_stream()

response.print\_response\_stream()

Back to top

[Previous Azure OpenAI](https://docs.llamaindex.ai/en/stable/examples/customization/llms/AzureOpenAI/)[Next HuggingFace LLM - Camel-5b](https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-Huggingface_camel/)
