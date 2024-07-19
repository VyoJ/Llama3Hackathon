Title: Query Pipeline with Async/Parallel Execution

URL Source: https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_async/

Markdown Content:
Query Pipeline with Async/Parallel Execution - LlamaIndex


Here we showcase our query pipeline with async + parallel execution.

We do this by setting up a RAG pipeline that does the following:

1.  Send query to multiple RAG query engines.
2.  Combine results.

In the process we'll also show some nice abstractions for joining results (e.g. our `ArgPackComponent()`)

Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_async/#load-data)
----------------------------------------------------------------------------------------------------

Load in the Paul Graham essay as an example.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai

%pip install llama-index-llms-openai

In \[ \]:

Copied!

!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt' \-O pg\_essay.txt

!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt' -O pg\_essay.txt

\--2024-01-10 12:31:00--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.111.133, 185.199.110.133, 185.199.108.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.111.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 75042 (73K) \[text/plain\]
Saving to: ‘pg\_essay.txt’

pg\_essay.txt        100%\[>\]  73.28K  --.-KB/s    in 0.01s   

2024-01-10 12:31:00 (6.32 MB/s) - ‘pg\_essay.txt’ saved \[75042/75042\]

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

reader \= SimpleDirectoryReader(input\_files\=\["pg\_essay.txt"\])
documents \= reader.load\_data()

from llama\_index.core import SimpleDirectoryReader reader = SimpleDirectoryReader(input\_files=\["pg\_essay.txt"\]) documents = reader.load\_data()

Setup Query Pipeline[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_async/#setup-query-pipeline)
--------------------------------------------------------------------------------------------------------------------------

We setup a parallel query pipeline that executes multiple chunk sizes at once, and combines the results.

### Define Modules[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_async/#define-modules)

This includes:

*   LLM
*   Chunk Sizes
*   Query Engines

In \[ \]:

Copied!

from llama\_index.core.query\_pipeline import (
    QueryPipeline,
    InputComponent,
    ArgPackComponent,
)
from typing import Dict, Any, List, Optional
from llama\_index.core.llama\_pack import BaseLlamaPack
from llama\_index.core.llms import LLM
from llama\_index.llms.openai import OpenAI
from llama\_index.core import Document, VectorStoreIndex
from llama\_index.core.response\_synthesizers import TreeSummarize
from llama\_index.core.schema import NodeWithScore, TextNode
from llama\_index.core.node\_parser import SentenceSplitter

llm \= OpenAI(model\="gpt-3.5-turbo")
chunk\_sizes \= \[128, 256, 512, 1024\]
query\_engines \= {}
for chunk\_size in chunk\_sizes:
    splitter \= SentenceSplitter(chunk\_size\=chunk\_size, chunk\_overlap\=0)
    nodes \= splitter.get\_nodes\_from\_documents(documents)
    vector\_index \= VectorStoreIndex(nodes)
    query\_engines\[str(chunk\_size)\] \= vector\_index.as\_query\_engine(llm\=llm)

from llama\_index.core.query\_pipeline import ( QueryPipeline, InputComponent, ArgPackComponent, ) from typing import Dict, Any, List, Optional from llama\_index.core.llama\_pack import BaseLlamaPack from llama\_index.core.llms import LLM from llama\_index.llms.openai import OpenAI from llama\_index.core import Document, VectorStoreIndex from llama\_index.core.response\_synthesizers import TreeSummarize from llama\_index.core.schema import NodeWithScore, TextNode from llama\_index.core.node\_parser import SentenceSplitter llm = OpenAI(model="gpt-3.5-turbo") chunk\_sizes = \[128, 256, 512, 1024\] query\_engines = {} for chunk\_size in chunk\_sizes: splitter = SentenceSplitter(chunk\_size=chunk\_size, chunk\_overlap=0) nodes = splitter.get\_nodes\_from\_documents(documents) vector\_index = VectorStoreIndex(nodes) query\_engines\[str(chunk\_size)\] = vector\_index.as\_query\_engine(llm=llm)

### Construct Query Pipeline[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_async/#construct-query-pipeline)

Connect input to multiple query engines, and join the results.

In \[ \]:

Copied!

\# construct query pipeline
p \= QueryPipeline(verbose\=True)
module\_dict \= {
    \*\*query\_engines,
    "input": InputComponent(),
    "summarizer": TreeSummarize(),
    "join": ArgPackComponent(
        convert\_fn\=lambda x: NodeWithScore(node\=TextNode(text\=str(x)))
    ),
}
p.add\_modules(module\_dict)
\# add links from input to query engine (id'ed by chunk\_size)
for chunk\_size in chunk\_sizes:
    p.add\_link("input", str(chunk\_size))
    p.add\_link(str(chunk\_size), "join", dest\_key\=str(chunk\_size))
p.add\_link("join", "summarizer", dest\_key\="nodes")
p.add\_link("input", "summarizer", dest\_key\="query\_str")

\# construct query pipeline p = QueryPipeline(verbose=True) module\_dict = { \*\*query\_engines, "input": InputComponent(), "summarizer": TreeSummarize(), "join": ArgPackComponent( convert\_fn=lambda x: NodeWithScore(node=TextNode(text=str(x))) ), } p.add\_modules(module\_dict) # add links from input to query engine (id'ed by chunk\_size) for chunk\_size in chunk\_sizes: p.add\_link("input", str(chunk\_size)) p.add\_link(str(chunk\_size), "join", dest\_key=str(chunk\_size)) p.add\_link("join", "summarizer", dest\_key="nodes") p.add\_link("input", "summarizer", dest\_key="query\_str")

Try out Queries[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_async/#try-out-queries)
----------------------------------------------------------------------------------------------------------------

Let's compare the async performance vs. synchronous performance!

In our experiments we get a 2x speedup.

In \[ \]:

Copied!

import time

start\_time \= time.time()
response \= await p.arun(input\="What did the author do during his time in YC?")
print(str(response))
end\_time \= time.time()
print(f"Time taken: {end\_time \- start\_time}")

import time start\_time = time.time() response = await p.arun(input="What did the author do during his time in YC?") print(str(response)) end\_time = time.time() print(f"Time taken: {end\_time - start\_time}")

\> Running modules and inputs in parallel: 
Module key: input. Input: 
input: What did the author do during his time in YC?

\> Running modules and inputs in parallel: 
Module key: 128. Input: 
input: What did the author do during his time in YC?

Module key: 256. Input: 
input: What did the author do during his time in YC?

Module key: 512. Input: 
input: What did the author do during his time in YC?

Module key: 1024. Input: 
input: What did the author do during his time in YC?

\> Running modules and inputs in parallel: 
Module key: join. Input: 
128: The author worked on solving the problems of startups that were part of the YC program.
256: The author worked on YC's internal software in Arc and also wrote essays during his time in YC.
512: During his time in YC, the author worked on various projects. Initially, he intended to do three things: hack, write essays, and work on YC. However, as YC grew and he became more excited about it, it...
1024: During his time in YC, the author worked on YC's internal software in Arc and wrote essays. He also worked on various projects related to YC, such as helping startups and solving their problems. Addit...

\> Running modules and inputs in parallel: 
Module key: summarizer. Input: 
query\_str: What did the author do during his time in YC?
nodes: \[NodeWithScore(node=TextNode(id\_='7e0b0aeb-04e3-4518-b534-2cf68c07ae1f', embedding=None, metadata={}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, hash='fe9144af45...

During his time in YC, the author worked on various projects, including YC's internal software in Arc and writing essays. He also helped startups and solved their problems, and was involved in disputes between cofounders. Additionally, the author worked hard to ensure the success of YC and dealt with people who maltreated startups.
Time taken: 3.943013906478882

In \[ \]:

Copied!

\# compare with sync method

start\_time \= time.time()
response \= p.run(input\="What did the author do during his time in YC?")
print(str(response))
end\_time \= time.time()
print(f"Time taken: {end\_time \- start\_time}")

\# compare with sync method start\_time = time.time() response = p.run(input="What did the author do during his time in YC?") print(str(response)) end\_time = time.time() print(f"Time taken: {end\_time - start\_time}")

\> Running module input with input: 
input: What did the author do during his time in YC?

\> Running module 128 with input: 
input: What did the author do during his time in YC?

\> Running module 256 with input: 
input: What did the author do during his time in YC?

\> Running module 512 with input: 
input: What did the author do during his time in YC?

\> Running module 1024 with input: 
input: What did the author do during his time in YC?

\> Running module join with input: 
128: The author worked on solving the problems of startups that were part of the YC program.
256: The author worked on YC's internal software in Arc and also wrote essays.
512: During his time in YC, the author worked on various projects. Initially, he intended to do three things: hack, write essays, and work on YC. However, as YC grew and he became more excited about it, it...
1024: During his time in YC, the author worked on YC's internal software in Arc, wrote essays, and worked on various projects related to YC. He also engaged in solving the problems faced by startups that we...

\> Running module summarizer with input: 
query\_str: What did the author do during his time in YC?
nodes: \[NodeWithScore(node=TextNode(id\_='4d698e2f-811e-42ce-bd0d-9b5615b0bbfd', embedding=None, metadata={}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, hash='fe9144af45...

During his time in YC, the author worked on YC's internal software in Arc, wrote essays, and worked on various projects related to YC. He also engaged in solving the problems faced by startups that were part of YC's program. Additionally, the author mentioned working on tasks he didn't particularly enjoy, such as resolving disputes between cofounders and dealing with people who mistreated startups.
Time taken: 7.640604019165039

Back to top

[Previous An Introduction to LlamaIndex Query Pipelines](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/)[Next Query Pipeline Chat Engine](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_memory/)
