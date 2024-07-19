Title: LongContextReorder - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/LongContextReorder/

Markdown Content:
LongContextReorder - LlamaIndex


Models struggle to access significant details found in the center of extended contexts. [A study](https://arxiv.org/abs/2307.03172) observed that the best performance typically arises when crucial data is positioned at the start or conclusion of the input context. Additionally, as the input context lengthens, performance drops notably, even in models designed for long contexts.

This module will re-order the retrieved nodes, which can be helpful in cases where a large top-k is needed. The reordering process works as follows:

1.  Input nodes are sorted based on their relevance scores.
2.  Sorted nodes are then reordered in an alternating pattern:
    *   Even-indexed nodes are placed at the beginning of the new list.
    *   Odd-indexed nodes are placed at the end of the new list.

This approach ensures that the highest-scored (most relevant) nodes are positioned at the beginning and end of the list, with lower-scored nodes in the middle.

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/LongContextReorder/#setup)
----------------------------------------------------------------------------------------------------

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

import os
import openai

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import os import openai os.environ\["OPENAI\_API\_KEY"\] = "sk-..."

In \[ \]:

Copied!

from llama\_index.embeddings.huggingface import HuggingFaceEmbedding
from llama\_index.llms.openai import OpenAI
from llama\_index.core import Settings

Settings.llm \= OpenAI(model\="gpt-3.5-turbo-instruct", temperature\=0.1)
Settings.embed\_model \= HuggingFaceEmbedding(model\_name\="BAAI/bge-base-en-v1.5")

from llama\_index.embeddings.huggingface import HuggingFaceEmbedding from llama\_index.llms.openai import OpenAI from llama\_index.core import Settings Settings.llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.1) Settings.embed\_model = HuggingFaceEmbedding(model\_name="BAAI/bge-base-en-v1.5")

/home/loganm/miniconda3/envs/llama-index/lib/python3.11/site-packages/torch/cuda/\_\_init\_\_.py:546: UserWarning: Can't initialize NVML
  warnings.warn("Can't initialize NVML")

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

from llama\_index.core import SimpleDirectoryReader documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data()

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex

index \= VectorStoreIndex.from\_documents(documents)

from llama\_index.core import VectorStoreIndex index = VectorStoreIndex.from\_documents(documents)

Run Query[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/LongContextReorder/#run-query)
------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core.postprocessor import LongContextReorder

reorder \= LongContextReorder()

reorder\_engine \= index.as\_query\_engine(
    node\_postprocessors\=\[reorder\], similarity\_top\_k\=5
)
base\_engine \= index.as\_query\_engine(similarity\_top\_k\=5)

from llama\_index.core.postprocessor import LongContextReorder reorder = LongContextReorder() reorder\_engine = index.as\_query\_engine( node\_postprocessors=\[reorder\], similarity\_top\_k=5 ) base\_engine = index.as\_query\_engine(similarity\_top\_k=5)

In \[ \]:

Copied!

from llama\_index.core.response.notebook\_utils import display\_response

base\_response \= base\_engine.query("Did the author meet Sam Altman?")
display\_response(base\_response)

from llama\_index.core.response.notebook\_utils import display\_response base\_response = base\_engine.query("Did the author meet Sam Altman?") display\_response(base\_response)

**`Final Response:`** Yes, the author met Sam Altman when they asked him to be the president of Y Combinator. This was during the time when the author was in a PhD program in computer science and also pursuing their passion for art. They were applying to art schools and eventually ended up attending RISD.

In \[ \]:

Copied!

reorder\_response \= reorder\_engine.query("Did the author meet Sam Altman?")
display\_response(reorder\_response)

reorder\_response = reorder\_engine.query("Did the author meet Sam Altman?") display\_response(reorder\_response)

**`Final Response:`** Yes, the author met Sam Altman when they asked him to be the president of Y Combinator. This meeting occurred at a party at the author's house, where they were introduced by a mutual friend, Jessica Livingston. Jessica later went on to compile a book of interviews with startup founders, and the author shared their thoughts on the flaws of venture capital with her during her job search at a Boston VC firm.

Inspect Order Diffrences[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/LongContextReorder/#inspect-order-diffrences)
------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

print(base\_response.get\_formatted\_sources())

print(base\_response.get\_formatted\_sources())

\> Source (Doc id: 81bc66bb-2c45-4697-9f08-9f848bd78b12): \[17\]

As well as HN, I wrote all of YC's internal software in Arc. But while I continued to work ...

> Source (Doc id: bd660905-e4e0-4d02-a113-e3810b59c5d1): \[19\] One way to get more precise about the concept of invented vs discovered is to talk about spa...

> Source (Doc id: 3932e4a4-f17e-4dd2-9d25-5f0e65910dc5): Not so much because it was badly written as because the problem is so convoluted. When you're wor...

> Source (Doc id: 0d801f0a-4a99-475d-aa7c-ad5d601947ea): \[10\]

Wow, I thought, there's an audience. If I write something and put it on the web, anyone can...

> Source (Doc id: bf726802-4d0d-4ee5-ab2e-ffa8a5461bc4): I was briefly tempted, but they were so slow by present standards; what was the point? No one els...

In \[ \]:

Copied!

print(reorder\_response.get\_formatted\_sources())

print(reorder\_response.get\_formatted\_sources())

\> Source (Doc id: 81bc66bb-2c45-4697-9f08-9f848bd78b12): \[17\]

As well as HN, I wrote all of YC's internal software in Arc. But while I continued to work ...

> Source (Doc id: 3932e4a4-f17e-4dd2-9d25-5f0e65910dc5): Not so much because it was badly written as because the problem is so convoluted. When you're wor...

> Source (Doc id: bf726802-4d0d-4ee5-ab2e-ffa8a5461bc4): I was briefly tempted, but they were so slow by present standards; what was the point? No one els...

> Source (Doc id: 0d801f0a-4a99-475d-aa7c-ad5d601947ea): \[10\]

Wow, I thought, there's an audience. If I write something and put it on the web, anyone can...

> Source (Doc id: bd660905-e4e0-4d02-a113-e3810b59c5d1): \[19\] One way to get more precise about the concept of invented vs discovered is to talk about spa...

Back to top

[Previous LLM Reranker Demonstration (2021 Lyft 10-k)](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/LLMReranker-Lyft-10k/)[Next Metadata Replacement + Node Sentence Window](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/MetadataReplacementDemo/)

Hi, how can I help you?

🦙
