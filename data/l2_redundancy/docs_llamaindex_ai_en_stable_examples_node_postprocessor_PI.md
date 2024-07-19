Title: PII Masking - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/PII/

Markdown Content:
PII Masking - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai
%pip install llama\-index\-llms\-huggingface

%pip install llama-index-llms-openai %pip install llama-index-llms-huggingface

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

from llama\_index.core.postprocessor import (
    PIINodePostprocessor,
    NERPIINodePostprocessor,
)
from llama\_index.llms.huggingface import HuggingFaceLLM
from llama\_index.core import Document, VectorStoreIndex
from llama\_index.core.schema import TextNode

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout)) from llama\_index.core.postprocessor import ( PIINodePostprocessor, NERPIINodePostprocessor, ) from llama\_index.llms.huggingface import HuggingFaceLLM from llama\_index.core import Document, VectorStoreIndex from llama\_index.core.schema import TextNode

INFO:numexpr.utils:Note: NumExpr detected 16 cores but "NUMEXPR\_MAX\_THREADS" not set, so enforcing safe limit of 8.
Note: NumExpr detected 16 cores but "NUMEXPR\_MAX\_THREADS" not set, so enforcing safe limit of 8.
INFO:numexpr.utils:NumExpr defaulting to 8 threads.
NumExpr defaulting to 8 threads.

/home/loganm/miniconda3/envs/llama-index/lib/python3.11/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user\_install.html
  from .autonotebook import tqdm as notebook\_tqdm

In \[ \]:

Copied!

\# load documents
text \= """
Hello Paulo Santos. The latest statement for your credit card account \\
1111-0000-1111-0000 was mailed to 123 Any Street, Seattle, WA 98109.
"""
node \= TextNode(text\=text)

\# load documents text = """ Hello Paulo Santos. The latest statement for your credit card account \\ 1111-0000-1111-0000 was mailed to 123 Any Street, Seattle, WA 98109. """ node = TextNode(text=text)

### Option 1: Use NER Model for PII Masking[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/PII/#option-1-use-ner-model-for-pii-masking)

Use a Hugging Face NER model for PII Masking

In \[ \]:

Copied!

processor \= NERPIINodePostprocessor()

processor = NERPIINodePostprocessor()

In \[ \]:

Copied!

from llama\_index.core.schema import NodeWithScore

new\_nodes \= processor.postprocess\_nodes(\[NodeWithScore(node\=node)\])

from llama\_index.core.schema import NodeWithScore new\_nodes = processor.postprocess\_nodes(\[NodeWithScore(node=node)\])

No model was supplied, defaulted to dbmdz/bert-large-cased-finetuned-conll03-english and revision f2482bf (https://huggingface.co/dbmdz/bert-large-cased-finetuned-conll03-english).
Using a pipeline without specifying a model name and revision in production is not recommended.
/home/loganm/miniconda3/envs/llama-index/lib/python3.11/site-packages/transformers/pipelines/token\_classification.py:169: UserWarning: \`grouped\_entities\` is deprecated and will be removed in version v5.0.0, defaulted to \`aggregation\_strategy="AggregationStrategy.SIMPLE"\` instead.
  warnings.warn(

In \[ \]:

Copied!

\# view redacted text
new\_nodes\[0\].node.get\_text()

\# view redacted text new\_nodes\[0\].node.get\_text()

Out\[ \]:

'Hello \[ORG\_6\]. The latest statement for your credit card account 1111-0000-1111-0000 was mailed to 123 \[ORG\_108\] \[LOC\_112\], \[LOC\_120\], \[LOC\_129\] 98109.'

In \[ \]:

Copied!

\# get mapping in metadata
\# NOTE: this is not sent to the LLM!
new\_nodes\[0\].node.metadata\["\_\_pii\_node\_info\_\_"\]

\# get mapping in metadata # NOTE: this is not sent to the LLM! new\_nodes\[0\].node.metadata\["\_\_pii\_node\_info\_\_"\]

Out\[ \]:

{'\[ORG\_6\]': 'Paulo Santos',
 '\[ORG\_108\]': 'Any',
 '\[LOC\_112\]': 'Street',
 '\[LOC\_120\]': 'Seattle',
 '\[LOC\_129\]': 'WA'}

### Option 2: Use LLM for PII Masking[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/PII/#option-2-use-llm-for-pii-masking)

NOTE: You should be using a _local_ LLM model for PII masking. The example shown is using OpenAI, but normally you'd use an LLM running locally, possibly from huggingface. Examples for local LLMs are [here](https://gpt-index.readthedocs.io/en/latest/how_to/customization/custom_llms.html#example-using-a-huggingface-llm).

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI

processor \= PIINodePostprocessor(llm\=OpenAI())

from llama\_index.llms.openai import OpenAI processor = PIINodePostprocessor(llm=OpenAI())

In \[ \]:

Copied!

from llama\_index.core.schema import NodeWithScore

new\_nodes \= processor.postprocess\_nodes(\[NodeWithScore(node\=node)\])

from llama\_index.core.schema import NodeWithScore new\_nodes = processor.postprocess\_nodes(\[NodeWithScore(node=node)\])

In \[ \]:

Copied!

\# view redacted text
new\_nodes\[0\].node.get\_text()

\# view redacted text new\_nodes\[0\].node.get\_text()

Out\[ \]:

'Hello \[NAME\]. The latest statement for your credit card account \[CREDIT\_CARD\_NUMBER\] was mailed to \[ADDRESS\].'

In \[ \]:

Copied!

\# get mapping in metadata
\# NOTE: this is not sent to the LLM!
new\_nodes\[0\].node.metadata\["\_\_pii\_node\_info\_\_"\]

\# get mapping in metadata # NOTE: this is not sent to the LLM! new\_nodes\[0\].node.metadata\["\_\_pii\_node\_info\_\_"\]

Out\[ \]:

{'NAME': 'Paulo Santos',
 'CREDIT\_CARD\_NUMBER': '1111-0000-1111-0000',
 'ADDRESS': '123 Any Street, Seattle, WA 98109'}

### Option 3: Use Presidio for PII Masking[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/PII/#option-3-use-presidio-for-pii-masking)

Use presidio to identify and anonymize PII

In \[ \]:

Copied!

\# load documents
text \= """
Hello Paulo Santos. The latest statement for your credit card account \\
4095-2609-9393-4932 was mailed to Seattle, WA 98109. \\
IBAN GB90YNTU67299444055881 and social security number is 474-49-7577 were verified on the system. \\
Further communications will be sent to paulo@presidio.site 
"""
presidio\_node \= TextNode(text\=text)

\# load documents text = """ Hello Paulo Santos. The latest statement for your credit card account \\ 4095-2609-9393-4932 was mailed to Seattle, WA 98109. \\ IBAN GB90YNTU67299444055881 and social security number is 474-49-7577 were verified on the system. \\ Further communications will be sent to paulo@presidio.site """ presidio\_node = TextNode(text=text)

In \[ \]:

Copied!

from llama\_index.postprocessor.presidio import PresidioPIINodePostprocessor

processor \= PresidioPIINodePostprocessor()

from llama\_index.postprocessor.presidio import PresidioPIINodePostprocessor processor = PresidioPIINodePostprocessor()

In \[ \]:

Copied!

from llama\_index.core.schema import NodeWithScore

presidio\_new\_nodes \= processor.postprocess\_nodes(
    \[NodeWithScore(node\=presidio\_node)\]
)

from llama\_index.core.schema import NodeWithScore presidio\_new\_nodes = processor.postprocess\_nodes( \[NodeWithScore(node=presidio\_node)\] )

In \[ \]:

Copied!

\# view redacted text
presidio\_new\_nodes\[0\].node.get\_text()

\# view redacted text presidio\_new\_nodes\[0\].node.get\_text()

Out\[ \]:

'\\nHello <PERSON\_1>. The latest statement for your credit card account <CREDIT\_CARD\_1> was mailed to <LOCATION\_2>, <LOCATION\_1>. IBAN <IBAN\_CODE\_1> and social security number is <US\_SSN\_1> were verified on the system. Further communications will be sent to <EMAIL\_ADDRESS\_1> \\n'

In \[ \]:

Copied!

\# get mapping in metadata
\# NOTE: this is not sent to the LLM!
presidio\_new\_nodes\[0\].node.metadata\["\_\_pii\_node\_info\_\_"\]

\# get mapping in metadata # NOTE: this is not sent to the LLM! presidio\_new\_nodes\[0\].node.metadata\["\_\_pii\_node\_info\_\_"\]

Out\[ \]:

{'<EMAIL\_ADDRESS\_1>': 'paulo@presidio.site',
 '<US\_SSN\_1>': '474-49-7577',
 '<IBAN\_CODE\_1>': 'GB90YNTU67299444055881',
 '<LOCATION\_1>': 'WA 98109',
 '<LOCATION\_2>': 'Seattle',
 '<CREDIT\_CARD\_1>': '4095-2609-9393-4932',
 '<PERSON\_1>': 'Paulo Santos'}

### Feed Nodes to Index[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/PII/#feed-nodes-to-index)

In \[ \]:

Copied!

\# feed into index
index \= VectorStoreIndex(\[n.node for n in new\_nodes\])

\# feed into index index = VectorStoreIndex(\[n.node for n in new\_nodes\])

INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total embedding token usage: 30 tokens
> \[build\_index\_from\_nodes\] Total embedding token usage: 30 tokens

In \[ \]:

Copied!

response \= index.as\_query\_engine().query(
    "What address was the statement mailed to?"
)
print(str(response))

response = index.as\_query\_engine().query( "What address was the statement mailed to?" ) print(str(response))

INFO:llama\_index.token\_counter.token\_counter:> \[retrieve\] Total LLM token usage: 0 tokens
> \[retrieve\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[retrieve\] Total embedding token usage: 8 tokens
> \[retrieve\] Total embedding token usage: 8 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total LLM token usage: 71 tokens
> \[get\_response\] Total LLM token usage: 71 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total embedding token usage: 0 tokens
> \[get\_response\] Total embedding token usage: 0 tokens

\[ADDRESS\]

Back to top

[Previous Sentence Embedding OptimizerThis postprocessor optimizes token usage by removing sentences that are not relevant to the query (this is done using embeddings).The percentile cutoff is a measure for using the top percentage of relevant sentences. The threshold cutoff can be specified instead, which uses a raw similarity cutoff for picking which sentences to keep.](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/OptimizerDemo/)[Next Forward/Backward Augmentation](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/PrevNextPostprocessorDemo/)

Hi, how can I help you?

🦙
