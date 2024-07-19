Title: Sentence Embedding OptimizerThis postprocessor optimizes token usage by removing sentences that are not relevant to the query (this is done using embeddings).The percentile cutoff is a measure for using the top percentage of relevant sentences. The threshold cutoff can be specified instead, which uses a raw similarity cutoff for picking which sentences to keep.

URL Source: https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/OptimizerDemo/

Markdown Content:
Sentence Embedding OptimizerThis postprocessor optimizes token usage by removing sentences that are not relevant to the query (this is done using embeddings).The percentile cutoff is a measure for using the top percentage of relevant sentences. The threshold cutoff can be specified instead, which uses a raw similarity cutoff for picking which sentences to keep. - LlamaIndex


In \[ \]:

Copied!

%pip install llama\-index\-readers\-wikipedia

%pip install llama-index-readers-wikipedia

In \[ \]:

Copied!

\# My OpenAI Key
import os

os.environ\["OPENAI\_API\_KEY"\] \= "INSERT OPENAI KEY"

\# My OpenAI Key import os os.environ\["OPENAI\_API\_KEY"\] = "INSERT OPENAI KEY"

### Setup[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/OptimizerDemo/#setup)

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

from llama\_index.core import download\_loader

from llama\_index.readers.wikipedia import WikipediaReader

loader \= WikipediaReader()
documents \= loader.load\_data(pages\=\["Berlin"\])

from llama\_index.core import download\_loader from llama\_index.readers.wikipedia import WikipediaReader loader = WikipediaReader() documents = loader.load\_data(pages=\["Berlin"\])

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex

index \= VectorStoreIndex.from\_documents(documents)

from llama\_index.core import VectorStoreIndex index = VectorStoreIndex.from\_documents(documents)

<class 'llama\_index.readers.schema.base.Document'>

INFO:root:> \[build\_index\_from\_documents\] Total LLM token usage: 0 tokens
INFO:root:> \[build\_index\_from\_documents\] Total embedding token usage: 18390 tokens

Compare query with and without optimization for LLM token usage, Embedding Model usage on query, Embedding model usage for optimizer, and total time.

In \[ \]:

Copied!

import time
from llama\_index.core import VectorStoreIndex
from llama\_index.core.postprocessor import SentenceEmbeddingOptimizer

print("Without optimization")
start\_time \= time.time()
query\_engine \= index.as\_query\_engine()
res \= query\_engine.query("What is the population of Berlin?")
end\_time \= time.time()
print("Total time elapsed: {}".format(end\_time \- start\_time))
print("Answer: {}".format(res))

print("With optimization")
start\_time \= time.time()
query\_engine \= index.as\_query\_engine(
    node\_postprocessors\=\[SentenceEmbeddingOptimizer(percentile\_cutoff\=0.5)\]
)
res \= query\_engine.query("What is the population of Berlin?")
end\_time \= time.time()
print("Total time elapsed: {}".format(end\_time \- start\_time))
print("Answer: {}".format(res))

print("Alternate optimization cutoff")
start\_time \= time.time()
query\_engine \= index.as\_query\_engine(
    node\_postprocessors\=\[SentenceEmbeddingOptimizer(threshold\_cutoff\=0.7)\]
)
res \= query\_engine.query("What is the population of Berlin?")
end\_time \= time.time()
print("Total time elapsed: {}".format(end\_time \- start\_time))
print("Answer: {}".format(res))

import time from llama\_index.core import VectorStoreIndex from llama\_index.core.postprocessor import SentenceEmbeddingOptimizer print("Without optimization") start\_time = time.time() query\_engine = index.as\_query\_engine() res = query\_engine.query("What is the population of Berlin?") end\_time = time.time() print("Total time elapsed: {}".format(end\_time - start\_time)) print("Answer: {}".format(res)) print("With optimization") start\_time = time.time() query\_engine = index.as\_query\_engine( node\_postprocessors=\[SentenceEmbeddingOptimizer(percentile\_cutoff=0.5)\] ) res = query\_engine.query("What is the population of Berlin?") end\_time = time.time() print("Total time elapsed: {}".format(end\_time - start\_time)) print("Answer: {}".format(res)) print("Alternate optimization cutoff") start\_time = time.time() query\_engine = index.as\_query\_engine( node\_postprocessors=\[SentenceEmbeddingOptimizer(threshold\_cutoff=0.7)\] ) res = query\_engine.query("What is the population of Berlin?") end\_time = time.time() print("Total time elapsed: {}".format(end\_time - start\_time)) print("Answer: {}".format(res))

Without optimization

INFO:root:> \[query\] Total LLM token usage: 3545 tokens
INFO:root:> \[query\] Total embedding token usage: 7 tokens

Total time elapsed: 2.8928110599517822
Answer: 
The population of Berlin in 1949 was approximately 2.2 million inhabitants. After the fall of the Berlin Wall in 1989, the population of Berlin increased to approximately 3.7 million inhabitants.

With optimization

INFO:root:> \[optimize\] Total embedding token usage: 7 tokens
INFO:root:> \[query\] Total LLM token usage: 1779 tokens
INFO:root:> \[query\] Total embedding token usage: 7 tokens

Total time elapsed: 2.346346139907837
Answer: 
The population of Berlin is around 4.5 million.
Alternate optimization cutoff

INFO:root:> \[optimize\] Total embedding token usage: 7 tokens
INFO:root:> \[query\] Total LLM token usage: 3215 tokens
INFO:root:> \[query\] Total embedding token usage: 7 tokens

Total time elapsed: 2.101111888885498
Answer: 
The population of Berlin is around 4.5 million.

Back to top

[Previous NVIDIA NIMs](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/NVIDIARerank/)[Next PII Masking](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/PII/)

Hi, how can I help you?

🦙
