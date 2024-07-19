Title: Pandas Query Engine - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/query_engine/pandas_query_engine/

Markdown Content:
Pandas Query Engine - LlamaIndex


This guide shows you how to use our `PandasQueryEngine`: convert natural language to Pandas python code using LLMs.

The input to the `PandasQueryEngine` is a Pandas dataframe, and the output is a response. The LLM infers dataframe operations to perform in order to retrieve the result.

**WARNING:** This tool provides the LLM access to the `eval` function. Arbitrary code execution is possible on the machine running this tool. While some level of filtering is done on code, this tool is not recommended to be used in a production setting without heavy sandboxing or virtual machines.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

!pip install llama\-index llama\-index\-experimental

!pip install llama-index llama-index-experimental

In \[ \]:

Copied!

import logging
import sys
from IPython.display import Markdown, display

import pandas as pd
from llama\_index.experimental.query\_engine import PandasQueryEngine

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys from IPython.display import Markdown, display import pandas as pd from llama\_index.experimental.query\_engine import PandasQueryEngine logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

Let's start on a Toy DataFrame[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/pandas_query_engine/#lets-start-on-a-toy-dataframe)
------------------------------------------------------------------------------------------------------------------------------------------------

Here let's load a very simple dataframe containing city and population pairs, and run the `PandasQueryEngine` on it.

By setting `verbose=True` we can see the intermediate generated instructions.

In \[ \]:

Copied!

\# Test on some sample data
df \= pd.DataFrame(
    {
        "city": \["Toronto", "Tokyo", "Berlin"\],
        "population": \[2930000, 13960000, 3645000\],
    }
)

\# Test on some sample data df = pd.DataFrame( { "city": \["Toronto", "Tokyo", "Berlin"\], "population": \[2930000, 13960000, 3645000\], } )

In \[ \]:

Copied!

query\_engine \= PandasQueryEngine(df\=df, verbose\=True)

query\_engine = PandasQueryEngine(df=df, verbose=True)

In \[ \]:

Copied!

response \= query\_engine.query(
    "What is the city with the highest population?",
)

response = query\_engine.query( "What is the city with the highest population?", )

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
> Pandas Instructions:
\`\`\`
df\['city'\]\[df\['population'\].idxmax()\]
\`\`\`
> Pandas Output: Tokyo

In \[ \]:

Copied!

display(Markdown(f"<b>{response}</b>"))

display(Markdown(f"**{response}**"))

**Tokyo**

In \[ \]:

Copied!

\# get pandas python instructions
print(response.metadata\["pandas\_instruction\_str"\])

\# get pandas python instructions print(response.metadata\["pandas\_instruction\_str"\])

df\['city'\]\[df\['population'\].idxmax()\]

We can also take the step of using an LLM to synthesize a response.

In \[ \]:

Copied!

query\_engine \= PandasQueryEngine(df\=df, verbose\=True, synthesize\_response\=True)
response \= query\_engine.query(
    "What is the city with the highest population? Give both the city and population",
)
print(str(response))

query\_engine = PandasQueryEngine(df=df, verbose=True, synthesize\_response=True) response = query\_engine.query( "What is the city with the highest population? Give both the city and population", ) print(str(response))

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
> Pandas Instructions:
\`\`\`
df.loc\[df\['population'\].idxmax()\]
\`\`\`
> Pandas Output: city             Tokyo
population    13960000
Name: 1, dtype: object
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
The city with the highest population is Tokyo, with a population of 13,960,000.

Analyzing the Titanic Dataset[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/pandas_query_engine/#analyzing-the-titanic-dataset)
-----------------------------------------------------------------------------------------------------------------------------------------------

The Titanic dataset is one of the most popular tabular datasets in introductory machine learning Source: [https://www.kaggle.com/c/titanic](https://www.kaggle.com/c/titanic)

#### Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/pandas_query_engine/#download-data)

In \[ \]:

Copied!

!wget 'https://raw.githubusercontent.com/jerryjliu/llama\_index/main/docs/docs/examples/data/csv/titanic\_train.csv' \-O 'titanic\_train.csv'

!wget 'https://raw.githubusercontent.com/jerryjliu/llama\_index/main/docs/docs/examples/data/csv/titanic\_train.csv' -O 'titanic\_train.csv'

\--2024-01-13 17:45:15--  https://raw.githubusercontent.com/jerryjliu/llama\_index/main/docs/docs/examples/data/csv/titanic\_train.csv
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 2606:50c0:8003::154, 2606:50c0:8002::154, 2606:50c0:8001::154, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|2606:50c0:8003::154|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 57726 (56K) \[text/plain\]
Saving to: ‘titanic\_train.csv’

titanic\_train.csv   100%\[>\]  56.37K  --.-KB/s    in 0.009s  

2024-01-13 17:45:15 (6.45 MB/s) - ‘titanic\_train.csv’ saved \[57726/57726\]

In \[ \]:

Copied!

df \= pd.read\_csv("./titanic\_train.csv")

df = pd.read\_csv("./titanic\_train.csv")

In \[ \]:

Copied!

query\_engine \= PandasQueryEngine(df\=df, verbose\=True)

query\_engine = PandasQueryEngine(df=df, verbose=True)

In \[ \]:

Copied!

response \= query\_engine.query(
    "What is the correlation between survival and age?",
)

response = query\_engine.query( "What is the correlation between survival and age?", )

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
> Pandas Instructions:
\`\`\`
df\['survived'\].corr(df\['age'\])
\`\`\`
> Pandas Output: -0.07722109457217755

In \[ \]:

Copied!

display(Markdown(f"<b>{response}</b>"))

display(Markdown(f"**{response}**"))

**\-0.07722109457217755**

In \[ \]:

Copied!

\# get pandas python instructions
print(response.metadata\["pandas\_instruction\_str"\])

\# get pandas python instructions print(response.metadata\["pandas\_instruction\_str"\])

df\['survived'\].corr(df\['age'\])

Additional Steps[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/pandas_query_engine/#additional-steps)
---------------------------------------------------------------------------------------------------------------------

### Analyzing / Modifying prompts[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/pandas_query_engine/#analyzing-modifying-prompts)

Let's look at the prompts!

In \[ \]:

Copied!

from llama\_index.core import PromptTemplate

from llama\_index.core import PromptTemplate

In \[ \]:

Copied!

query\_engine \= PandasQueryEngine(df\=df, verbose\=True)
prompts \= query\_engine.get\_prompts()
print(prompts\["pandas\_prompt"\].template)

query\_engine = PandasQueryEngine(df=df, verbose=True) prompts = query\_engine.get\_prompts() print(prompts\["pandas\_prompt"\].template)

You are working with a pandas dataframe in Python.
The name of the dataframe is \`df\`.
This is the result of \`print(df.head())\`:
{df\_str}

Follow these instructions:
{instruction\_str}
Query: {query\_str}

Expression:

In \[ \]:

Copied!

print(prompts\["response\_synthesis\_prompt"\].template)

print(prompts\["response\_synthesis\_prompt"\].template)

Given an input question, synthesize a response from the query results.
Query: {query\_str}

Pandas Instructions (optional):
{pandas\_instructions}

Pandas Output: {pandas\_output}

Response: 

You can update prompts as well:

In \[ \]:

Copied!

new\_prompt \= PromptTemplate(
    """\\
You are working with a pandas dataframe in Python.
The name of the dataframe is \`df\`.
This is the result of \`print(df.head())\`:
{df\_str}

Follow these instructions:
{instruction\_str}
Query: {query\_str}

Expression: """
)

query\_engine.update\_prompts({"pandas\_prompt": new\_prompt})

new\_prompt = PromptTemplate( """\\ You are working with a pandas dataframe in Python. The name of the dataframe is \`df\`. This is the result of \`print(df.head())\`: {df\_str} Follow these instructions: {instruction\_str} Query: {query\_str} Expression: """ ) query\_engine.update\_prompts({"pandas\_prompt": new\_prompt})

This is the instruction string (that you can customize by passing in `instruction_str` on initialization)

In \[ \]:

Copied!

instruction\_str \= """\\
1\. Convert the query to executable Python code using Pandas.
2\. The final line of code should be a Python expression that can be called with the \`eval()\` function.
3\. The code should represent a solution to the query.
4\. PRINT ONLY THE EXPRESSION.
5\. Do not quote the expression.
"""

instruction\_str = """\\ 1. Convert the query to executable Python code using Pandas. 2. The final line of code should be a Python expression that can be called with the \`eval()\` function. 3. The code should represent a solution to the query. 4. PRINT ONLY THE EXPRESSION. 5. Do not quote the expression. """

### Implementing Query Engine using Query Pipeline Syntax[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/pandas_query_engine/#implementing-query-engine-using-query-pipeline-syntax)

If you want to learn to construct your own Pandas Query Engine using our Query Pipeline syntax and the prompt components above, check out our below tutorial.

[Setting up a Pandas DataFrame query engine with Query Pipelines](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_pandas.html)

Back to top

[Previous Structured Hierarchical Retrieval](https://docs.llamaindex.ai/en/stable/examples/query_engine/multi_doc_auto_retrieval/multi_doc_auto_retrieval/)[Next Recursive Retriever + Query Engine Demo](https://docs.llamaindex.ai/en/stable/examples/query_engine/pdf_tables/recursive_retriever/)

Hi, how can I help you?

🦙
