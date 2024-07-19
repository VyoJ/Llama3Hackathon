Title: mixedbread Rerank Cookbook - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/cookbooks/mixedbread_reranker/

Markdown Content:
mixedbread Rerank Cookbook - LlamaIndex


mixedbread.ai has released three fully open-source reranker models under the Apache 2.0 license. For more in-depth information, you can check out their detailed [blog post](https://www.mixedbread.ai/blog/mxbai-rerank-v1). The following are the three models:

1.  `mxbai-rerank-xsmall-v1`
2.  `mxbai-rerank-base-v1`
3.  `mxbai-rerank-large-v1`

In this notebook, we'll demonstrate how to use the `mxbai-rerank-base-v1` model with the `SentenceTransformerRerank` module in LlamaIndex. This setup allows you to seamlessly swap in any reranker model of your choice using the `SentenceTransformerRerank` module to enhance your RAG pipeline.

### Installation[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/mixedbread_reranker/#installation)

In \[ \]:

Copied!

!pip install llama\-index
!pip install sentence\-transformers

!pip install llama-index !pip install sentence-transformers

### Set API Keys[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/mixedbread_reranker/#set-api-keys)

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "YOUR OPENAI API KEY"

import os os.environ\["OPENAI\_API\_KEY"\] = "YOUR OPENAI API KEY"

In \[ \]:

Copied!

from llama\_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
)

from llama\_index.core.postprocessor import SentenceTransformerRerank

from llama\_index.core import ( VectorStoreIndex, SimpleDirectoryReader, ) from llama\_index.core.postprocessor import SentenceTransformerRerank

### Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/mixedbread_reranker/#download-data)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

\--2024-03-01 09:52:09--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.110.133, 185.199.108.133, 185.199.109.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.110.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 75042 (73K) \[text/plain\]
Saving to: ‘data/paul\_graham/paul\_graham\_essay.txt’

data/paul\_graham/pa 100%\[>\]  73.28K  --.-KB/s    in 0.007s  

2024-03-01 09:52:09 (9.86 MB/s) - ‘data/paul\_graham/paul\_graham\_essay.txt’ saved \[75042/75042\]

### Load Documents[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/mixedbread_reranker/#load-documents)

In \[ \]:

Copied!

documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data()

### Build Index[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/mixedbread_reranker/#build-index)

In \[ \]:

Copied!

index \= VectorStoreIndex.from\_documents(documents\=documents)

index = VectorStoreIndex.from\_documents(documents=documents)

### Define postprocessor for `mxbai-rerank-base-v1` reranker[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/mixedbread_reranker/#define-postprocessor-for-mxbai-rerank-base-v1-reranker)

In \[ \]:

Copied!

from llama\_index.core.postprocessor import SentenceTransformerRerank

postprocessor \= SentenceTransformerRerank(
    model\="mixedbread-ai/mxbai-rerank-base-v1", top\_n\=2
)

from llama\_index.core.postprocessor import SentenceTransformerRerank postprocessor = SentenceTransformerRerank( model="mixedbread-ai/mxbai-rerank-base-v1", top\_n=2 )

### Create Query Engine[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/mixedbread_reranker/#create-query-engine)

We will first retrieve 10 relevant nodes and pick top-2 nodes using the defined postprocessor.

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(
    similarity\_top\_k\=10,
    node\_postprocessors\=\[postprocessor\],
)

query\_engine = index.as\_query\_engine( similarity\_top\_k=10, node\_postprocessors=\[postprocessor\], )

### Test Queries[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/mixedbread_reranker/#test-queries)

In \[ \]:

Copied!

response \= query\_engine.query(
    "Why did Sam Altman decline the offer of becoming president of Y Combinator?",
)

print(response)

response = query\_engine.query( "Why did Sam Altman decline the offer of becoming president of Y Combinator?", ) print(response)

Sam Altman initially declined the offer of becoming president of Y Combinator because he wanted to start a startup focused on making nuclear reactors.

In \[ \]:

Copied!

response \= query\_engine.query(
    "Why did Paul Graham start YC?",
)

print(response)

response = query\_engine.query( "Why did Paul Graham start YC?", ) print(response)

Paul Graham started YC because he and his partners wanted to create an investment firm where they could implement their own ideas and provide the kind of support to startups that they felt was lacking when they were founders themselves. They aimed to not only make seed investments but also assist startups with various aspects of setting up a company, similar to the help they had received from others in the past.

Back to top

[Previous MistralAI Cookbook](https://docs.llamaindex.ai/en/stable/examples/cookbooks/mistralai/)[Next Prometheus-2 Cookbook](https://docs.llamaindex.ai/en/stable/examples/cookbooks/prometheus2_cookbook/)
