Title: Query Pipeline with Routing - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_routing/

Markdown Content:
Query Pipeline with Routing - LlamaIndex


Here we showcase our query pipeline with routing.

Routing lets us dynamically choose underlying query pipelines to use given the query and a set of choices.

We offer this as an out-of-the-box abstraction in our [Router Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/RouterQueryEngine.html) guide. Here we show you how to compose a similar pipeline using our Query Pipeline syntax - this allows you to not only define query engines but easily stitch it into a chain/DAG with other modules across the compute graph.

Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_routing/#load-data)
------------------------------------------------------------------------------------------------------

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

Setup Query Pipeline with Routing[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_routing/#setup-query-pipeline-with-routing)
------------------------------------------------------------------------------------------------------------------------------------------------------

### Define Modules[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_routing/#define-modules)

We define llm, vector index, summary index, and prompt templates.

In \[ \]:

Copied!

from llama\_index.core.query\_pipeline import QueryPipeline, InputComponent
from typing import Dict, Any, List, Optional
from llama\_index.llms.openai import OpenAI
from llama\_index.core import Document, VectorStoreIndex
from llama\_index.core import SummaryIndex
from llama\_index.core.response\_synthesizers import TreeSummarize
from llama\_index.core.schema import NodeWithScore, TextNode
from llama\_index.core import PromptTemplate
from llama\_index.core.selectors import LLMSingleSelector

\# define HyDE template
hyde\_str \= """\\
Please write a passage to answer the question: {query\_str}

Try to include as many key details as possible.

Passage: """
hyde\_prompt \= PromptTemplate(hyde\_str)

\# define llm
llm \= OpenAI(model\="gpt-3.5-turbo")

\# define synthesizer
summarizer \= TreeSummarize(llm\=llm)

\# define vector retriever
vector\_index \= VectorStoreIndex.from\_documents(documents)
vector\_query\_engine \= vector\_index.as\_query\_engine(similarity\_top\_k\=2)

\# define summary query prompts + retrievers
summary\_index \= SummaryIndex.from\_documents(documents)
summary\_qrewrite\_str \= """\\
Here's a question:
{query\_str}

You are responsible for feeding the question to an agent that given context will try to answer the question.
The context may or may not be relevant. Rewrite the question to highlight the fact that
only some pieces of context (or none) maybe be relevant.
"""
summary\_qrewrite\_prompt \= PromptTemplate(summary\_qrewrite\_str)
summary\_query\_engine \= summary\_index.as\_query\_engine()

\# define selector
selector \= LLMSingleSelector.from\_defaults()

from llama\_index.core.query\_pipeline import QueryPipeline, InputComponent from typing import Dict, Any, List, Optional from llama\_index.llms.openai import OpenAI from llama\_index.core import Document, VectorStoreIndex from llama\_index.core import SummaryIndex from llama\_index.core.response\_synthesizers import TreeSummarize from llama\_index.core.schema import NodeWithScore, TextNode from llama\_index.core import PromptTemplate from llama\_index.core.selectors import LLMSingleSelector # define HyDE template hyde\_str = """\\ Please write a passage to answer the question: {query\_str} Try to include as many key details as possible. Passage: """ hyde\_prompt = PromptTemplate(hyde\_str) # define llm llm = OpenAI(model="gpt-3.5-turbo") # define synthesizer summarizer = TreeSummarize(llm=llm) # define vector retriever vector\_index = VectorStoreIndex.from\_documents(documents) vector\_query\_engine = vector\_index.as\_query\_engine(similarity\_top\_k=2) # define summary query prompts + retrievers summary\_index = SummaryIndex.from\_documents(documents) summary\_qrewrite\_str = """\\ Here's a question: {query\_str} You are responsible for feeding the question to an agent that given context will try to answer the question. The context may or may not be relevant. Rewrite the question to highlight the fact that only some pieces of context (or none) maybe be relevant. """ summary\_qrewrite\_prompt = PromptTemplate(summary\_qrewrite\_str) summary\_query\_engine = summary\_index.as\_query\_engine() # define selector selector = LLMSingleSelector.from\_defaults()

### Construct Query Pipelines[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_routing/#construct-query-pipelines)

Define a query pipeline for vector index, summary index, and join it together with a router.

In \[ \]:

Copied!

\# define summary query pipeline
from llama\_index.core.query\_pipeline import RouterComponent

vector\_chain \= QueryPipeline(chain\=\[vector\_query\_engine\])
summary\_chain \= QueryPipeline(
    chain\=\[summary\_qrewrite\_prompt, llm, summary\_query\_engine\], verbose\=True
)

choices \= \[
    "This tool answers specific questions about the document (not summary questions across the document)",
    "This tool answers summary questions about the document (not specific questions)",
\]

router\_c \= RouterComponent(
    selector\=selector,
    choices\=choices,
    components\=\[vector\_chain, summary\_chain\],
    verbose\=True,
)
\# top-level pipeline
qp \= QueryPipeline(chain\=\[router\_c\], verbose\=True)

\# define summary query pipeline from llama\_index.core.query\_pipeline import RouterComponent vector\_chain = QueryPipeline(chain=\[vector\_query\_engine\]) summary\_chain = QueryPipeline( chain=\[summary\_qrewrite\_prompt, llm, summary\_query\_engine\], verbose=True ) choices = \[ "This tool answers specific questions about the document (not summary questions across the document)", "This tool answers summary questions about the document (not specific questions)", \] router\_c = RouterComponent( selector=selector, choices=choices, components=\[vector\_chain, summary\_chain\], verbose=True, ) # top-level pipeline qp = QueryPipeline(chain=\[router\_c\], verbose=True)

Try out Queries[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_routing/#try-out-queries)
------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

\# compare with sync method
response \= qp.run("What did the author do during his time in YC?")
print(str(response))

\# compare with sync method response = qp.run("What did the author do during his time in YC?") print(str(response))

\> Running module c0a87442-3165-443d-9709-960e6ddafe7f with input: 
query: What did the author do during his time in YC?

Selecting component 0: The author used a tool to answer specific questions about the document, which suggests that he was engaged in analyzing and extracting specific information from the document during his time in YC..
During his time in YC, the author worked on various tasks related to running Y Combinator. This included selecting and helping founders, dealing with disputes between cofounders, figuring out when people were lying, and fighting with people who maltreated the startups. The author also worked on writing essays and internal software for YC.

In \[ \]:

Copied!

response \= qp.run("What is a summary of this document?")
print(str(response))

response = qp.run("What is a summary of this document?") print(str(response))

\> Running module c0a87442-3165-443d-9709-960e6ddafe7f with input: 
query: What is a summary of this document?

Selecting component 1: The summary questions about the document are answered by this tool..
\> Running module 0e7e9d49-4c92-45a9-b3bf-0e6ab76b51f9 with input: 
query\_str: What is a summary of this document?

\> Running module b0ece4e3-e6cd-4229-8663-b0cd0638683c with input: 
messages: Here's a question:
What is a summary of this document?

You are responsible for feeding the question to an agent that given context will try to answer the question.
The context may or may not be relev...

\> Running module f247ae78-a71c-4347-ba49-d9357ee93636 with input: 
input: assistant: What is the summary of the document?

The document discusses the development and evolution of Lisp as a programming language. It highlights how Lisp was originally created as a formal model of computation and later transformed into a programming language with the assistance of Steve Russell. The document also emphasizes the unique power and elegance of Lisp in comparison to other languages.

Back to top

[Previous Query Pipeline over Pandas DataFrames](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_pandas/)[Next Query Pipeline for Advanced Text-to-SQL](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_sql/)
