Title: Multi-Tenancy RAG with LlamaIndex - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/multi_tenancy/multi_tenancy_rag/

Markdown Content:
Multi-Tenancy RAG with LlamaIndex - LlamaIndex


In this notebook you will look into building Multi-Tenancy RAG System using LlamaIndex.

1.  Setup
2.  Download Data
3.  Load Data
4.  Create Index
5.  Create Ingestion Pipeline
6.  Update Metadata and Insert documents
7.  Define Query Engines for each user
8.  Querying

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/multi_tenancy/multi_tenancy_rag/#setup)
----------------------------------------------------------------------------------------------

You should ensure you have `llama-index` and `pypdf` is installed.

In \[ \]:

Copied!

!pip install llama\-index pypdf

!pip install llama-index pypdf

### Set OpenAI Key[¶](https://docs.llamaindex.ai/en/stable/examples/multi_tenancy/multi_tenancy_rag/#set-openai-key)

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "YOUR OPENAI API KEY"

import os os.environ\["OPENAI\_API\_KEY"\] = "YOUR OPENAI API KEY"

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex
from llama\_index.core.vector\_stores import MetadataFilters, ExactMatchFilter
from llama\_index.core import SimpleDirectoryReader
from llama\_index.core.ingestion import IngestionPipeline
from llama\_index.core.node\_parser import SentenceSplitter

from IPython.display import HTML

from llama\_index.core import VectorStoreIndex from llama\_index.core.vector\_stores import MetadataFilters, ExactMatchFilter from llama\_index.core import SimpleDirectoryReader from llama\_index.core.ingestion import IngestionPipeline from llama\_index.core.node\_parser import SentenceSplitter from IPython.display import HTML

Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/multi_tenancy/multi_tenancy_rag/#download-data)
--------------------------------------------------------------------------------------------------------------

We will use `An LLM Compiler for Parallel Function Calling` and `Dense X Retrieval: What Retrieval Granularity Should We Use?` papers for the demonstartions.

In \[ \]:

Copied!

!wget \--user\-agent "Mozilla" "https://arxiv.org/pdf/2312.04511.pdf" \-O "llm\_compiler.pdf"
!wget \--user\-agent "Mozilla" "https://arxiv.org/pdf/2312.06648.pdf" \-O "dense\_x\_retrieval.pdf"

!wget --user-agent "Mozilla" "https://arxiv.org/pdf/2312.04511.pdf" -O "llm\_compiler.pdf" !wget --user-agent "Mozilla" "https://arxiv.org/pdf/2312.06648.pdf" -O "dense\_x\_retrieval.pdf"

\--2024-01-15 14:29:26--  https://arxiv.org/pdf/2312.04511.pdf
Resolving arxiv.org (arxiv.org)... 151.101.131.42, 151.101.67.42, 151.101.3.42, ...
Connecting to arxiv.org (arxiv.org)|151.101.131.42|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 755837 (738K) \[application/pdf\]
Saving to: ‘llm\_compiler.pdf’


llm\_compiler.pdf      0%\[                    \]       0  --.-KB/s               
llm\_compiler.pdf    100%\[>\]   1.05M  --.-KB/s    in 0.005s  

2024-01-15 14:29:26 (208 MB/s) - ‘dense\_x\_retrieval.pdf’ saved \[1103758/1103758\]

Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/multi_tenancy/multi_tenancy_rag/#load-data)
------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

reader \= SimpleDirectoryReader(input\_files\=\["dense\_x\_retrieval.pdf"\])
documents\_jerry \= reader.load\_data()

reader \= SimpleDirectoryReader(input\_files\=\["llm\_compiler.pdf"\])
documents\_ravi \= reader.load\_data()

reader = SimpleDirectoryReader(input\_files=\["dense\_x\_retrieval.pdf"\]) documents\_jerry = reader.load\_data() reader = SimpleDirectoryReader(input\_files=\["llm\_compiler.pdf"\]) documents\_ravi = reader.load\_data()

Create an Empty Index[¶](https://docs.llamaindex.ai/en/stable/examples/multi_tenancy/multi_tenancy_rag/#create-an-empty-index)
------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

index \= VectorStoreIndex.from\_documents(documents\=\[\])

index = VectorStoreIndex.from\_documents(documents=\[\])

Create Ingestion Pipeline[¶](https://docs.llamaindex.ai/en/stable/examples/multi_tenancy/multi_tenancy_rag/#create-ingestion-pipeline)
--------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

pipeline \= IngestionPipeline(
    transformations\=\[
        SentenceSplitter(chunk\_size\=512, chunk\_overlap\=20),
    \]
)

pipeline = IngestionPipeline( transformations=\[ SentenceSplitter(chunk\_size=512, chunk\_overlap=20), \] )

Update Metadata and Insert Documents[¶](https://docs.llamaindex.ai/en/stable/examples/multi_tenancy/multi_tenancy_rag/#update-metadata-and-insert-documents)
------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

for document in documents\_jerry:
    document.metadata\["user"\] \= "Jerry"

nodes \= pipeline.run(documents\=documents\_jerry)
\# Insert nodes into the index
index.insert\_nodes(nodes)

for document in documents\_jerry: document.metadata\["user"\] = "Jerry" nodes = pipeline.run(documents=documents\_jerry) # Insert nodes into the index index.insert\_nodes(nodes)

In \[ \]:

Copied!

for document in documents\_ravi:
    document.metadata\["user"\] \= "Ravi"

nodes \= pipeline.run(documents\=documents\_ravi)
\# Insert nodes into the index
index.insert\_nodes(nodes)

for document in documents\_ravi: document.metadata\["user"\] = "Ravi" nodes = pipeline.run(documents=documents\_ravi) # Insert nodes into the index index.insert\_nodes(nodes)

Define Query Engines[¶](https://docs.llamaindex.ai/en/stable/examples/multi_tenancy/multi_tenancy_rag/#define-query-engines)
----------------------------------------------------------------------------------------------------------------------------

Define query engines for both the users with necessary filters.

In \[ \]:

Copied!

\# For Jerry
jerry\_query\_engine \= index.as\_query\_engine(
    filters\=MetadataFilters(
        filters\=\[
            ExactMatchFilter(
                key\="user",
                value\="Jerry",
            )
        \]
    ),
    similarity\_top\_k\=3,
)

\# For Ravi
ravi\_query\_engine \= index.as\_query\_engine(
    filters\=MetadataFilters(
        filters\=\[
            ExactMatchFilter(
                key\="user",
                value\="Ravi",
            )
        \]
    ),
    similarity\_top\_k\=3,
)

\# For Jerry jerry\_query\_engine = index.as\_query\_engine( filters=MetadataFilters( filters=\[ ExactMatchFilter( key="user", value="Jerry", ) \] ), similarity\_top\_k=3, ) # For Ravi ravi\_query\_engine = index.as\_query\_engine( filters=MetadataFilters( filters=\[ ExactMatchFilter( key="user", value="Ravi", ) \] ), similarity\_top\_k=3, )

Querying[¶](https://docs.llamaindex.ai/en/stable/examples/multi_tenancy/multi_tenancy_rag/#querying)
----------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

\# Jerry has Dense X Rerieval paper and should be able to answer following question.
response \= jerry\_query\_engine.query(
    "what are propositions mentioned in the paper?"
)
\# Print response
display(HTML(f'<p style="font-size:20px">{response.response}</p>'))

\# Jerry has Dense X Rerieval paper and should be able to answer following question. response = jerry\_query\_engine.query( "what are propositions mentioned in the paper?" ) # Print response display(HTML(f'{response.response}

'))

The paper mentions propositions as an alternative retrieval unit choice. Propositions are defined as atomic expressions of meanings in text that correspond to distinct pieces of meaning in the text. They are minimal and cannot be further split into separate propositions. Each proposition is contextualized and self-contained, including all the necessary context from the text to interpret its meaning. The paper demonstrates the concept of propositions using an example about the Leaning Tower of Pisa, where the passage is split into three propositions, each corresponding to a distinct factoid about the tower.

In \[ \]:

Copied!

\# Ravi has LLMCompiler paper
response \= ravi\_query\_engine.query("what are steps involved in LLMCompiler?")

\# Print response
display(HTML(f'<p style="font-size:20px">{response.response}</p>'))

\# Ravi has LLMCompiler paper response = ravi\_query\_engine.query("what are steps involved in LLMCompiler?") # Print response display(HTML(f'{response.response}

'))

LLMCompiler consists of three key components: an LLM Planner, a Task Fetching Unit, and an Executor. The LLM Planner identifies the execution flow by defining different function calls and their dependencies based on user inputs. The Task Fetching Unit dispatches the function calls that can be executed in parallel after substituting variables with the actual outputs of preceding tasks. Finally, the Executor executes the dispatched function calling tasks using the associated tools. These components work together to optimize the parallel function calling performance of LLMs.

In \[ \]:

Copied!

\# This should not be answered as Jerry does not have information about LLMCompiler
response \= jerry\_query\_engine.query("what are steps involved in LLMCompiler?")

\# Print response
display(HTML(f'<p style="font-size:20px">{response.response}</p>'))

\# This should not be answered as Jerry does not have information about LLMCompiler response = jerry\_query\_engine.query("what are steps involved in LLMCompiler?") # Print response display(HTML(f'{response.response}

'))

The steps involved in LLMCompiler are not mentioned in the given context information.

Back to top

[Previous Semi-structured Image Retrieval](https://docs.llamaindex.ai/en/stable/examples/multi_modal/structured_image_retrieval/)[Next Semantic Chunker](https://docs.llamaindex.ai/en/stable/examples/node_parsers/semantic_chunking/)

Hi, how can I help you?

🦙
