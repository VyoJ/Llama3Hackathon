Title: Query Pipeline over Pandas DataFrames

URL Source: https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_pandas/

Markdown Content:
Query Pipeline over Pandas DataFrames - LlamaIndex


This is a simple example that builds a query pipeline that can perform structured operations over a Pandas DataFrame to satisfy a user query, using LLMs to infer the set of operations.

This can be treated as the "from-scratch" version of our `PandasQueryEngine`.

WARNING: This tool provides the LLM access to the `eval` function. Arbitrary code execution is possible on the machine running this tool. This tool is not recommended to be used in a production setting, and would require heavy sandboxing or virtual machines.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai llama\-index\-experimental

%pip install llama-index-llms-openai llama-index-experimental

In \[ \]:

Copied!

from llama\_index.core.query\_pipeline import (
    QueryPipeline as QP,
    Link,
    InputComponent,
)
from llama\_index.experimental.query\_engine.pandas import (
    PandasInstructionParser,
)
from llama\_index.llms.openai import OpenAI
from llama\_index.core import PromptTemplate

from llama\_index.core.query\_pipeline import ( QueryPipeline as QP, Link, InputComponent, ) from llama\_index.experimental.query\_engine.pandas import ( PandasInstructionParser, ) from llama\_index.llms.openai import OpenAI from llama\_index.core import PromptTemplate

Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_pandas/#download-data)
-------------------------------------------------------------------------------------------------------------

Here we load the Titanic CSV dataset.

In \[ \]:

Copied!

!wget 'https://raw.githubusercontent.com/jerryjliu/llama\_index/main/docs/docs/examples/data/csv/titanic\_train.csv' \-O 'titanic\_train.csv'

!wget 'https://raw.githubusercontent.com/jerryjliu/llama\_index/main/docs/docs/examples/data/csv/titanic\_train.csv' -O 'titanic\_train.csv'

\--2024-01-13 18:39:07--  https://raw.githubusercontent.com/jerryjliu/llama\_index/main/docs/docs/examples/data/csv/titanic\_train.csv
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 2606:50c0:8003::154, 2606:50c0:8001::154, 2606:50c0:8002::154, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|2606:50c0:8003::154|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 57726 (56K) \[text/plain\]
Saving to: ‘titanic\_train.csv’

titanic\_train.csv   100%\[>\]  56.37K  --.-KB/s    in 0.007s  

2024-01-13 18:39:07 (7.93 MB/s) - ‘titanic\_train.csv’ saved \[57726/57726\]

In \[ \]:

Copied!

import pandas as pd

df \= pd.read\_csv("./titanic\_train.csv")

import pandas as pd df = pd.read\_csv("./titanic\_train.csv")

Define Modules[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_pandas/#define-modules)
---------------------------------------------------------------------------------------------------------------

Here we define the set of modules:

1.  Pandas prompt to infer pandas instructions from user query
2.  Pandas output parser to execute pandas instructions on dataframe, get back dataframe
3.  Response synthesis prompt to synthesize a final response given the dataframe
4.  LLM

The pandas output parser specifically is designed to safely execute Python code. It includes a lot of safety checks that may be annoying to write from scratch. This includes only importing from a set of approved modules (e.g. no modules that would alter the file system like `os`), and also making sure that no private/dunder methods are being called.

In \[ \]:

Copied!

instruction\_str \= (
    "1. Convert the query to executable Python code using Pandas.\\n"
    "2. The final line of code should be a Python expression that can be called with the \`eval()\` function.\\n"
    "3. The code should represent a solution to the query.\\n"
    "4. PRINT ONLY THE EXPRESSION.\\n"
    "5. Do not quote the expression.\\n"
)

pandas\_prompt\_str \= (
    "You are working with a pandas dataframe in Python.\\n"
    "The name of the dataframe is \`df\`.\\n"
    "This is the result of \`print(df.head())\`:\\n"
    "{df\_str}\\n\\n"
    "Follow these instructions:\\n"
    "{instruction\_str}\\n"
    "Query: {query\_str}\\n\\n"
    "Expression:"
)
response\_synthesis\_prompt\_str \= (
    "Given an input question, synthesize a response from the query results.\\n"
    "Query: {query\_str}\\n\\n"
    "Pandas Instructions (optional):\\n{pandas\_instructions}\\n\\n"
    "Pandas Output: {pandas\_output}\\n\\n"
    "Response: "
)

pandas\_prompt \= PromptTemplate(pandas\_prompt\_str).partial\_format(
    instruction\_str\=instruction\_str, df\_str\=df.head(5)
)
pandas\_output\_parser \= PandasInstructionParser(df)
response\_synthesis\_prompt \= PromptTemplate(response\_synthesis\_prompt\_str)
llm \= OpenAI(model\="gpt-3.5-turbo")

instruction\_str = ( "1. Convert the query to executable Python code using Pandas.\\n" "2. The final line of code should be a Python expression that can be called with the \`eval()\` function.\\n" "3. The code should represent a solution to the query.\\n" "4. PRINT ONLY THE EXPRESSION.\\n" "5. Do not quote the expression.\\n" ) pandas\_prompt\_str = ( "You are working with a pandas dataframe in Python.\\n" "The name of the dataframe is \`df\`.\\n" "This is the result of \`print(df.head())\`:\\n" "{df\_str}\\n\\n" "Follow these instructions:\\n" "{instruction\_str}\\n" "Query: {query\_str}\\n\\n" "Expression:" ) response\_synthesis\_prompt\_str = ( "Given an input question, synthesize a response from the query results.\\n" "Query: {query\_str}\\n\\n" "Pandas Instructions (optional):\\n{pandas\_instructions}\\n\\n" "Pandas Output: {pandas\_output}\\n\\n" "Response: " ) pandas\_prompt = PromptTemplate(pandas\_prompt\_str).partial\_format( instruction\_str=instruction\_str, df\_str=df.head(5) ) pandas\_output\_parser = PandasInstructionParser(df) response\_synthesis\_prompt = PromptTemplate(response\_synthesis\_prompt\_str) llm = OpenAI(model="gpt-3.5-turbo")

Build Query Pipeline[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_pandas/#build-query-pipeline)
---------------------------------------------------------------------------------------------------------------------------

Looks like this: input query\_str -> pandas\_prompt -> llm1 -> pandas\_output\_parser -> response\_synthesis\_prompt -> llm2

Additional connections to response\_synthesis\_prompt: llm1 -> pandas\_instructions, and pandas\_output\_parser -> pandas\_output.

In \[ \]:

Copied!

qp \= QP(
    modules\={
        "input": InputComponent(),
        "pandas\_prompt": pandas\_prompt,
        "llm1": llm,
        "pandas\_output\_parser": pandas\_output\_parser,
        "response\_synthesis\_prompt": response\_synthesis\_prompt,
        "llm2": llm,
    },
    verbose\=True,
)
qp.add\_chain(\["input", "pandas\_prompt", "llm1", "pandas\_output\_parser"\])
qp.add\_links(
    \[
        Link("input", "response\_synthesis\_prompt", dest\_key\="query\_str"),
        Link(
            "llm1", "response\_synthesis\_prompt", dest\_key\="pandas\_instructions"
        ),
        Link(
            "pandas\_output\_parser",
            "response\_synthesis\_prompt",
            dest\_key\="pandas\_output",
        ),
    \]
)
\# add link from response synthesis prompt to llm2
qp.add\_link("response\_synthesis\_prompt", "llm2")

qp = QP( modules={ "input": InputComponent(), "pandas\_prompt": pandas\_prompt, "llm1": llm, "pandas\_output\_parser": pandas\_output\_parser, "response\_synthesis\_prompt": response\_synthesis\_prompt, "llm2": llm, }, verbose=True, ) qp.add\_chain(\["input", "pandas\_prompt", "llm1", "pandas\_output\_parser"\]) qp.add\_links( \[ Link("input", "response\_synthesis\_prompt", dest\_key="query\_str"), Link( "llm1", "response\_synthesis\_prompt", dest\_key="pandas\_instructions" ), Link( "pandas\_output\_parser", "response\_synthesis\_prompt", dest\_key="pandas\_output", ), \] ) # add link from response synthesis prompt to llm2 qp.add\_link("response\_synthesis\_prompt", "llm2")

Run Query[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_pandas/#run-query)
-----------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

response \= qp.run(
    query\_str\="What is the correlation between survival and age?",
)

response = qp.run( query\_str="What is the correlation between survival and age?", )

\> Running module input with input: 
query\_str: What is the correlation between survival and age?

\> Running module pandas\_prompt with input: 
query\_str: What is the correlation between survival and age?

\> Running module llm1 with input: 
messages: You are working with a pandas dataframe in Python.
The name of the dataframe is \`df\`.
This is the result of \`print(df.head())\`:
   survived  pclass                                               name  ...

\> Running module pandas\_output\_parser with input: 
input: assistant: df\['survived'\].corr(df\['age'\])

\> Running module response\_synthesis\_prompt with input: 
query\_str: What is the correlation between survival and age?
pandas\_instructions: assistant: df\['survived'\].corr(df\['age'\])
pandas\_output: -0.07722109457217755

\> Running module llm2 with input: 
messages: Given an input question, synthesize a response from the query results.
Query: What is the correlation between survival and age?

Pandas Instructions (optional):
df\['survived'\].corr(df\['age'\])

Pandas ...

In \[ \]:

Copied!

print(response.message.content)

print(response.message.content)

The correlation between survival and age is -0.0772. This indicates a weak negative correlation, suggesting that as age increases, the likelihood of survival slightly decreases.

Back to top

[Previous Query Pipeline Chat Engine](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_memory/)[Next Query Pipeline with Routing](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_routing/)
