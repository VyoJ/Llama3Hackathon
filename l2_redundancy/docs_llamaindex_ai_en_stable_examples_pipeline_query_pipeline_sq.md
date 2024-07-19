Title: Query Pipeline for Advanced Text-to-SQL

URL Source: https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_sql/

Markdown Content:
Query Pipeline for Advanced Text-to-SQL - LlamaIndex


In this guide we show you how to setup a text-to-SQL pipeline over your data with our [query pipeline](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/root.html) syntax.

This gives you flexibility to enhance text-to-SQL with additional techniques. We show these in the below sections:

1.  **Query-Time Table Retrieval**: Dynamically retrieve relevant tables in the text-to-SQL prompt.
2.  **Query-Time Sample Row retrieval**: Embed/Index each row, and dynamically retrieve example rows for each table in the text-to-SQL prompt.

Our out-of-the box pipelines include our `NLSQLTableQueryEngine` and `SQLTableRetrieverQueryEngine`. (if you want to check out our text-to-SQL guide using these modules, take a look [here](https://docs.llamaindex.ai/en/stable/examples/index_structs/struct_indices/SQLIndexDemo.html)). This guide implements an advanced version of those modules, giving you the utmost flexibility to apply this to your own setting.

**NOTE:** Any Text-to-SQL application should be aware that executing arbitrary SQL queries can be a security risk. It is recommended to take precautions as needed, such as using restricted roles, read-only databases, sandboxing, etc.

Load and Ingest Data[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_sql/#load-and-ingest-data)
------------------------------------------------------------------------------------------------------------------------

### Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_sql/#load-data)

We use the [WikiTableQuestions dataset](https://ppasupat.github.io/WikiTableQuestions/) (Pasupat and Liang 2015) as our test dataset.

We go through all the csv's in one folder, store each in a sqlite database (we will then build an object index over each table schema).

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai

%pip install llama-index-llms-openai

In \[ \]:

Copied!

!wget "https://github.com/ppasupat/WikiTableQuestions/releases/download/v1.0.2/WikiTableQuestions-1.0.2-compact.zip" \-O data.zip
!unzip data.zip

!wget "https://github.com/ppasupat/WikiTableQuestions/releases/download/v1.0.2/WikiTableQuestions-1.0.2-compact.zip" -O data.zip !unzip data.zip

In \[ \]:

Copied!

import pandas as pd
from pathlib import Path

data\_dir \= Path("./WikiTableQuestions/csv/200-csv")
csv\_files \= sorted(\[f for f in data\_dir.glob("\*.csv")\])
dfs \= \[\]
for csv\_file in csv\_files:
    print(f"processing file: {csv\_file}")
    try:
        df \= pd.read\_csv(csv\_file)
        dfs.append(df)
    except Exception as e:
        print(f"Error parsing {csv\_file}: {str(e)}")

import pandas as pd from pathlib import Path data\_dir = Path("./WikiTableQuestions/csv/200-csv") csv\_files = sorted(\[f for f in data\_dir.glob("\*.csv")\]) dfs = \[\] for csv\_file in csv\_files: print(f"processing file: {csv\_file}") try: df = pd.read\_csv(csv\_file) dfs.append(df) except Exception as e: print(f"Error parsing {csv\_file}: {str(e)}")

### Extract Table Name and Summary from each Table[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_sql/#extract-table-name-and-summary-from-each-table)

Here we use gpt-3.5 to extract a table name (with underscores) and summary from each table with our Pydantic program.

In \[ \]:

Copied!

tableinfo\_dir \= "WikiTableQuestions\_TableInfo"
!mkdir {tableinfo\_dir}

tableinfo\_dir = "WikiTableQuestions\_TableInfo" !mkdir {tableinfo\_dir}

In \[ \]:

Copied!

from llama\_index.core.program import LLMTextCompletionProgram
from llama\_index.core.bridge.pydantic import BaseModel, Field
from llama\_index.llms.openai import OpenAI

class TableInfo(BaseModel):
    """Information regarding a structured table."""

    table\_name: str \= Field(
        ..., description\="table name (must be underscores and NO spaces)"
    )
    table\_summary: str \= Field(
        ..., description\="short, concise summary/caption of the table"
    )

prompt\_str \= """\\
Give me a summary of the table with the following JSON format.

\- The table name must be unique to the table and describe it while being concise. 
\- Do NOT output a generic table name (e.g. table, my\_table).

Do NOT make the table name one of the following: {exclude\_table\_name\_list}

Table:
{table\_str}

Summary: """

program \= LLMTextCompletionProgram.from\_defaults(
    output\_cls\=TableInfo,
    llm\=OpenAI(model\="gpt-3.5-turbo"),
    prompt\_template\_str\=prompt\_str,
)

from llama\_index.core.program import LLMTextCompletionProgram from llama\_index.core.bridge.pydantic import BaseModel, Field from llama\_index.llms.openai import OpenAI class TableInfo(BaseModel): """Information regarding a structured table.""" table\_name: str = Field( ..., description="table name (must be underscores and NO spaces)" ) table\_summary: str = Field( ..., description="short, concise summary/caption of the table" ) prompt\_str = """\\ Give me a summary of the table with the following JSON format. - The table name must be unique to the table and describe it while being concise. - Do NOT output a generic table name (e.g. table, my\_table). Do NOT make the table name one of the following: {exclude\_table\_name\_list} Table: {table\_str} Summary: """ program = LLMTextCompletionProgram.from\_defaults( output\_cls=TableInfo, llm=OpenAI(model="gpt-3.5-turbo"), prompt\_template\_str=prompt\_str, )

In \[ \]:

Copied!

import json

def \_get\_tableinfo\_with\_index(idx: int) \-> str:
    results\_gen \= Path(tableinfo\_dir).glob(f"{idx}\_\*")
    results\_list \= list(results\_gen)
    if len(results\_list) \ 1:
        path \= results\_list\[0\]
        return TableInfo.parse\_file(path)
    else:
        raise ValueError(
            f"More than one file matching index: {list(results\_gen)}"
        )

table\_names \= set()
table\_infos \= \[\]
for idx, df in enumerate(dfs):
    table\_info \= \_get\_tableinfo\_with\_index(idx)
    if table\_info:
        table\_infos.append(table\_info)
    else:
        while True:
            df\_str \= df.head(10).to\_csv()
            table\_info \= program(
                table\_str\=df\_str,
                exclude\_table\_name\_list\=str(list(table\_names)),
            )
            table\_name \= table\_info.table\_name
            print(f"Processed table: {table\_name}")
            if table\_name not in table\_names:
                table\_names.add(table\_name)
                break
            else:
                \# try again
                print(f"Table name {table\_name} already exists, trying again.")
                pass

        out\_file \= f"{tableinfo\_dir}/{idx}\_{table\_name}.json"
        json.dump(table\_info.dict(), open(out\_file, "w"))
    table\_infos.append(table\_info)

import json def \_get\_tableinfo\_with\_index(idx: int) -> str: results\_gen = Path(tableinfo\_dir).glob(f"{idx}\_\*") results\_list = list(results\_gen) if len(results\_list)  1: path = results\_list\[0\] return TableInfo.parse\_file(path) else: raise ValueError( f"More than one file matching index: {list(results\_gen)}" ) table\_names = set() table\_infos = \[\] for idx, df in enumerate(dfs): table\_info = \_get\_tableinfo\_with\_index(idx) if table\_info: table\_infos.append(table\_info) else: while True: df\_str = df.head(10).to\_csv() table\_info = program( table\_str=df\_str, exclude\_table\_name\_list=str(list(table\_names)), ) table\_name = table\_info.table\_name print(f"Processed table: {table\_name}") if table\_name not in table\_names: table\_names.add(table\_name) break else: # try again print(f"Table name {table\_name} already exists, trying again.") pass out\_file = f"{tableinfo\_dir}/{idx}\_{table\_name}.json" json.dump(table\_info.dict(), open(out\_file, "w")) table\_infos.append(table\_info)

### Put Data in SQL Database[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_sql/#put-data-in-sql-database)

We use `sqlalchemy`, a popular SQL database toolkit, to load all the tables.

In \[ \]:

Copied!

\# put data into sqlite db
from sqlalchemy import (
    create\_engine,
    MetaData,
    Table,
    Column,
    String,
    Integer,
)
import re

\# Function to create a sanitized column name
def sanitize\_column\_name(col\_name):
    \# Remove special characters and replace spaces with underscores
    return re.sub(r"\\W+", "\_", col\_name)

\# Function to create a table from a DataFrame using SQLAlchemy
def create\_table\_from\_dataframe(
    df: pd.DataFrame, table\_name: str, engine, metadata\_obj
):
    \# Sanitize column names
    sanitized\_columns \= {col: sanitize\_column\_name(col) for col in df.columns}
    df \= df.rename(columns\=sanitized\_columns)

    \# Dynamically create columns based on DataFrame columns and data types
    columns \= \[
        Column(col, String if dtype \ "object" else Integer) for col, dtype in zip(df.columns, df.dtypes) \] # Create a table with the defined columns table = Table(table\_name, metadata\_obj, \*columns) # Create the table in the database metadata\_obj.create\_all(engine) # Insert data from DataFrame into the table with engine.connect() as conn: for \_, row in df.iterrows(): insert\_stmt = table.insert().values(\*\*row.to\_dict()) conn.execute(insert\_stmt) conn.commit() engine = create\_engine("sqlite:///:memory:") metadata\_obj = MetaData() for idx, df in enumerate(dfs): tableinfo = \_get\_tableinfo\_with\_index(idx) print(f"Creating table: {tableinfo.table\_name}") create\_table\_from\_dataframe(df, tableinfo.table\_name, engine, metadata\_obj)

In \[ \]:

Copied!

\# setup Arize Phoenix for logging/observability
import phoenix as px
import llama\_index.core

px.launch\_app()
llama\_index.core.set\_global\_handler("arize\_phoenix")

\# setup Arize Phoenix for logging/observability import phoenix as px import llama\_index.core px.launch\_app() llama\_index.core.set\_global\_handler("arize\_phoenix")

🌍 To view the Phoenix app in your browser, visit http://127.0.0.1:6006/
📺 To view the Phoenix app in a notebook, run \`px.active\_session().view()\`
📖 For more information on how to use Phoenix, check out https://docs.arize.com/phoenix

Advanced Capability 1: Text-to-SQL with Query-Time Table Retrieval.[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_sql/#advanced-capability-1-text-to-sql-with-query-time-table-retrieval)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We now show you how to setup an e2e text-to-SQL with table retrieval.

### Define Modules[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_sql/#define-modules)

Here we define the core modules.

1.  Object index + retriever to store table schemas
2.  SQLDatabase object to connect to the above tables + SQLRetriever.
3.  Text-to-SQL Prompt
4.  Response synthesis Prompt
5.  LLM

Object index, retriever, SQLDatabase

In \[ \]:

Copied!

from llama\_index.core.objects import (
    SQLTableNodeMapping,
    ObjectIndex,
    SQLTableSchema,
)
from llama\_index.core import SQLDatabase, VectorStoreIndex

sql\_database \= SQLDatabase(engine)

table\_node\_mapping \= SQLTableNodeMapping(sql\_database)
table\_schema\_objs \= \[
    SQLTableSchema(table\_name\=t.table\_name, context\_str\=t.table\_summary)
    for t in table\_infos
\]  \# add a SQLTableSchema for each table

obj\_index \= ObjectIndex.from\_objects(
    table\_schema\_objs,
    table\_node\_mapping,
    VectorStoreIndex,
)
obj\_retriever \= obj\_index.as\_retriever(similarity\_top\_k\=3)

from llama\_index.core.objects import ( SQLTableNodeMapping, ObjectIndex, SQLTableSchema, ) from llama\_index.core import SQLDatabase, VectorStoreIndex sql\_database = SQLDatabase(engine) table\_node\_mapping = SQLTableNodeMapping(sql\_database) table\_schema\_objs = \[ SQLTableSchema(table\_name=t.table\_name, context\_str=t.table\_summary) for t in table\_infos \] # add a SQLTableSchema for each table obj\_index = ObjectIndex.from\_objects( table\_schema\_objs, table\_node\_mapping, VectorStoreIndex, ) obj\_retriever = obj\_index.as\_retriever(similarity\_top\_k=3)

SQLRetriever + Table Parser

In \[ \]:

Copied!

from llama\_index.core.retrievers import SQLRetriever
from typing import List
from llama\_index.core.query\_pipeline import FnComponent

sql\_retriever \= SQLRetriever(sql\_database)

def get\_table\_context\_str(table\_schema\_objs: List\[SQLTableSchema\]):
    """Get table context string."""
    context\_strs \= \[\]
    for table\_schema\_obj in table\_schema\_objs:
        table\_info \= sql\_database.get\_single\_table\_info(
            table\_schema\_obj.table\_name
        )
        if table\_schema\_obj.context\_str:
            table\_opt\_context \= " The table description is: "
            table\_opt\_context += table\_schema\_obj.context\_str
            table\_info += table\_opt\_context

        context\_strs.append(table\_info)
    return "\\n\\n".join(context\_strs)

table\_parser\_component \= FnComponent(fn\=get\_table\_context\_str)

from llama\_index.core.retrievers import SQLRetriever from typing import List from llama\_index.core.query\_pipeline import FnComponent sql\_retriever = SQLRetriever(sql\_database) def get\_table\_context\_str(table\_schema\_objs: List\[SQLTableSchema\]): """Get table context string.""" context\_strs = \[\] for table\_schema\_obj in table\_schema\_objs: table\_info = sql\_database.get\_single\_table\_info( table\_schema\_obj.table\_name ) if table\_schema\_obj.context\_str: table\_opt\_context = " The table description is: " table\_opt\_context += table\_schema\_obj.context\_str table\_info += table\_opt\_context context\_strs.append(table\_info) return "\\n\\n".join(context\_strs) table\_parser\_component = FnComponent(fn=get\_table\_context\_str)

Text-to-SQL Prompt + Output Parser

In \[ \]:

Copied!

from llama\_index.core.prompts.default\_prompts import DEFAULT\_TEXT\_TO\_SQL\_PROMPT
from llama\_index.core import PromptTemplate
from llama\_index.core.query\_pipeline import FnComponent
from llama\_index.core.llms import ChatResponse

def parse\_response\_to\_sql(response: ChatResponse) \-> str:
    """Parse response to SQL."""
    response \= response.message.content
    sql\_query\_start \= response.find("SQLQuery:")
    if sql\_query\_start != \-1:
        response \= response\[sql\_query\_start:\]
        \# TODO: move to removeprefix after Python 3.9+
        if response.startswith("SQLQuery:"):
            response \= response\[len("SQLQuery:") :\]
    sql\_result\_start \= response.find("SQLResult:")
    if sql\_result\_start != \-1:
        response \= response\[:sql\_result\_start\]
    return response.strip().strip("\`\`\`").strip()

sql\_parser\_component \= FnComponent(fn\=parse\_response\_to\_sql)

text2sql\_prompt \= DEFAULT\_TEXT\_TO\_SQL\_PROMPT.partial\_format(
    dialect\=engine.dialect.name
)
print(text2sql\_prompt.template)

from llama\_index.core.prompts.default\_prompts import DEFAULT\_TEXT\_TO\_SQL\_PROMPT from llama\_index.core import PromptTemplate from llama\_index.core.query\_pipeline import FnComponent from llama\_index.core.llms import ChatResponse def parse\_response\_to\_sql(response: ChatResponse) -> str: """Parse response to SQL.""" response = response.message.content sql\_query\_start = response.find("SQLQuery:") if sql\_query\_start != -1: response = response\[sql\_query\_start:\] # TODO: move to removeprefix after Python 3.9+ if response.startswith("SQLQuery:"): response = response\[len("SQLQuery:") :\] sql\_result\_start = response.find("SQLResult:") if sql\_result\_start != -1: response = response\[:sql\_result\_start\] return response.strip().strip("\`\`\`").strip() sql\_parser\_component = FnComponent(fn=parse\_response\_to\_sql) text2sql\_prompt = DEFAULT\_TEXT\_TO\_SQL\_PROMPT.partial\_format( dialect=engine.dialect.name ) print(text2sql\_prompt.template)

Given an input question, first create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer. You can order the results by a relevant column to return the most interesting examples in the database.

Never query for all the columns from a specific table, only ask for a few relevant columns given the question.

Pay attention to use only the column names that you can see in the schema description. Be careful to not query for columns that do not exist. Pay attention to which column is in which table. Also, qualify column names with the table name when needed. You are required to use the following format, each taking one line:

Question: Question here
SQLQuery: SQL Query to run
SQLResult: Result of the SQLQuery
Answer: Final answer here

Only use tables listed below.
{schema}

Question: {query\_str}
SQLQuery: 

Response Synthesis Prompt

In \[ \]:

Copied!

response\_synthesis\_prompt\_str \= (
    "Given an input question, synthesize a response from the query results.\\n"
    "Query: {query\_str}\\n"
    "SQL: {sql\_query}\\n"
    "SQL Response: {context\_str}\\n"
    "Response: "
)
response\_synthesis\_prompt \= PromptTemplate(
    response\_synthesis\_prompt\_str,
)

response\_synthesis\_prompt\_str = ( "Given an input question, synthesize a response from the query results.\\n" "Query: {query\_str}\\n" "SQL: {sql\_query}\\n" "SQL Response: {context\_str}\\n" "Response: " ) response\_synthesis\_prompt = PromptTemplate( response\_synthesis\_prompt\_str, )

In \[ \]:

Copied!

llm \= OpenAI(model\="gpt-3.5-turbo")

llm = OpenAI(model="gpt-3.5-turbo")

### Define Query Pipeline[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_sql/#define-query-pipeline)

Now that the components are in place, let's define the query pipeline!

In \[ \]:

Copied!

from llama\_index.core.query\_pipeline import (
    QueryPipeline as QP,
    Link,
    InputComponent,
    CustomQueryComponent,
)

qp \= QP(
    modules\={
        "input": InputComponent(),
        "table\_retriever": obj\_retriever,
        "table\_output\_parser": table\_parser\_component,
        "text2sql\_prompt": text2sql\_prompt,
        "text2sql\_llm": llm,
        "sql\_output\_parser": sql\_parser\_component,
        "sql\_retriever": sql\_retriever,
        "response\_synthesis\_prompt": response\_synthesis\_prompt,
        "response\_synthesis\_llm": llm,
    },
    verbose\=True,
)

from llama\_index.core.query\_pipeline import ( QueryPipeline as QP, Link, InputComponent, CustomQueryComponent, ) qp = QP( modules={ "input": InputComponent(), "table\_retriever": obj\_retriever, "table\_output\_parser": table\_parser\_component, "text2sql\_prompt": text2sql\_prompt, "text2sql\_llm": llm, "sql\_output\_parser": sql\_parser\_component, "sql\_retriever": sql\_retriever, "response\_synthesis\_prompt": response\_synthesis\_prompt, "response\_synthesis\_llm": llm, }, verbose=True, )

In \[ \]:

Copied!

qp.add\_chain(\["input", "table\_retriever", "table\_output\_parser"\])
qp.add\_link("input", "text2sql\_prompt", dest\_key\="query\_str")
qp.add\_link("table\_output\_parser", "text2sql\_prompt", dest\_key\="schema")
qp.add\_chain(
    \["text2sql\_prompt", "text2sql\_llm", "sql\_output\_parser", "sql\_retriever"\]
)
qp.add\_link(
    "sql\_output\_parser", "response\_synthesis\_prompt", dest\_key\="sql\_query"
)
qp.add\_link(
    "sql\_retriever", "response\_synthesis\_prompt", dest\_key\="context\_str"
)
qp.add\_link("input", "response\_synthesis\_prompt", dest\_key\="query\_str")
qp.add\_link("response\_synthesis\_prompt", "response\_synthesis\_llm")

qp.add\_chain(\["input", "table\_retriever", "table\_output\_parser"\]) qp.add\_link("input", "text2sql\_prompt", dest\_key="query\_str") qp.add\_link("table\_output\_parser", "text2sql\_prompt", dest\_key="schema") qp.add\_chain( \["text2sql\_prompt", "text2sql\_llm", "sql\_output\_parser", "sql\_retriever"\] ) qp.add\_link( "sql\_output\_parser", "response\_synthesis\_prompt", dest\_key="sql\_query" ) qp.add\_link( "sql\_retriever", "response\_synthesis\_prompt", dest\_key="context\_str" ) qp.add\_link("input", "response\_synthesis\_prompt", dest\_key="query\_str") qp.add\_link("response\_synthesis\_prompt", "response\_synthesis\_llm")

### Visualize Query Pipeline[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_sql/#visualize-query-pipeline)

A really nice property of the query pipeline syntax is you can easily visualize it in a graph via networkx.

In \[ \]:

Copied!

from pyvis.network import Network

net \= Network(notebook\=True, cdn\_resources\="in\_line", directed\=True)
net.from\_nx(qp.dag)

from pyvis.network import Network net = Network(notebook=True, cdn\_resources="in\_line", directed=True) net.from\_nx(qp.dag)

In \[ \]:

Copied!

\# Save the network as "text2sql\_dag.html"
net.write\_html("text2sql\_dag.html")

\# Save the network as "text2sql\_dag.html" net.write\_html("text2sql\_dag.html")

In \[ \]:

Copied!

from IPython.display import display, HTML

\# Read the contents of the HTML file
with open("text2sql\_dag.html", "r") as file:
    html\_content \= file.read()

\# Display the HTML content
display(HTML(html\_content))

from IPython.display import display, HTML # Read the contents of the HTML file with open("text2sql\_dag.html", "r") as file: html\_content = file.read() # Display the HTML content display(HTML(html\_content))

### Run Some Queries![¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_sql/#run-some-queries)

Now we're ready to run some queries across this entire pipeline.

In \[ \]:

Copied!

response \= qp.run(
    query\="What was the year that The Notorious B.I.G was signed to Bad Boy?"
)
print(str(response))

response = qp.run( query="What was the year that The Notorious B.I.G was signed to Bad Boy?" ) print(str(response))

\> Running module input with input: 
query: What was the year that The Notorious B.I.G was signed to Bad Boy?

\> Running module table\_retriever with input: 
input: What was the year that The Notorious B.I.G was signed to Bad Boy?

\> Running module table\_output\_parser with input: 
table\_schema\_objs: \[SQLTableSchema(table\_name='Bad\_Boy\_Artists', context\_str='List of artists signed to Bad Boy Records and their album releases'), SQLTableSchema(table\_name='Bad\_Boy\_Artists', context\_str='List of artis...

\> Running module text2sql\_prompt with input: 
query\_str: What was the year that The Notorious B.I.G was signed to Bad Boy?
schema: Table 'Bad\_Boy\_Artists' has columns: Act (VARCHAR), Year\_signed (INTEGER), \_Albums\_released\_under\_Bad\_Boy (VARCHAR), and foreign keys: . The table description is: List of artists signed to Bad Boy Rec...

\> Running module text2sql\_llm with input: 
messages: Given an input question, first create a syntactically correct sqlite query to run, then look at the results of the query and return the answer. You can order the results by a relevant column to return...

\> Running module sql\_output\_parser with input: 
response: assistant: SELECT Year\_signed
FROM Bad\_Boy\_Artists
WHERE Act = 'The Notorious B.I.G'
SQLResult: 1993
Answer: The Notorious B.I.G was signed to Bad Boy in 1993.

RAW RESPONSE  SELECT Year\_signed
FROM Bad\_Boy\_Artists
WHERE Act = 'The Notorious B.I.G'
SQLResult: 1993
Answer: The Notorious B.I.G was signed to Bad Boy in 1993.
\> Running module sql\_retriever with input: 
input: SELECT Year\_signed
FROM Bad\_Boy\_Artists
WHERE Act = 'The Notorious B.I.G'

\> Running module response\_synthesis\_prompt with input: 
query\_str: What was the year that The Notorious B.I.G was signed to Bad Boy?
sql\_query: SELECT Year\_signed
FROM Bad\_Boy\_Artists
WHERE Act = 'The Notorious B.I.G'
context\_str: \[NodeWithScore(node=TextNode(id\_='4ae2f8fc-b803-4238-8433-7a431c2df391', embedding=None, metadata={}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, hash='c336a1cbf9...

\> Running module response\_synthesis\_llm with input: 
messages: Given an input question, synthesize a response from the query results.
Query: What was the year that The Notorious B.I.G was signed to Bad Boy?
SQL: SELECT Year\_signed
FROM Bad\_Boy\_Artists
WHERE Act =...

assistant: The Notorious B.I.G was signed to Bad Boy in 1993.

In \[ \]:

Copied!

response \= qp.run(query\="Who won best director in the 1972 academy awards")
print(str(response))

response = qp.run(query="Who won best director in the 1972 academy awards") print(str(response))

\> Running module input with input: 
query: Who won best directory in the 1972 academy awards

\> Running module table\_retriever with input: 
input: Who won best directory in the 1972 academy awards

\> Running module table\_output\_parser with input: 
table\_schema\_objs: \[SQLTableSchema(table\_name='Academy\_Awards\_1972', context\_str='List of award categories and nominees for the 1972 Academy Awards'), SQLTableSchema(table\_name='Academy\_Awards\_1972', context\_str='List o...

\> Running module text2sql\_prompt with input: 
query\_str: Who won best directory in the 1972 academy awards
schema: Table 'Academy\_Awards\_1972' has columns: Award (VARCHAR), Category (VARCHAR), Nominee (VARCHAR), Result (VARCHAR), and foreign keys: . The table description is: List of award categories and nominees f...

\> Running module text2sql\_llm with input: 
messages: Given an input question, first create a syntactically correct sqlite query to run, then look at the results of the query and return the answer. You can order the results by a relevant column to return...

\> Running module sql\_output\_parser with input: 
response: assistant: SELECT Nominee
FROM Academy\_Awards\_1972
WHERE Category = 'Best Director' AND Result = 'Won'
SQLResult: The result of the SQLQuery will be the name of the director who won the Best Director ...

RAW RESPONSE  SELECT Nominee
FROM Academy\_Awards\_1972
WHERE Category = 'Best Director' AND Result = 'Won'
SQLResult: The result of the SQLQuery will be the name of the director who won the Best Director award in the 1972 Academy Awards.
Answer: The winner of the Best Director award in the 1972 Academy Awards was \[Director's Name\].
\> Running module sql\_retriever with input: 
input: SELECT Nominee
FROM Academy\_Awards\_1972
WHERE Category = 'Best Director' AND Result = 'Won'

\> Running module response\_synthesis\_prompt with input: 
query\_str: Who won best directory in the 1972 academy awards
sql\_query: SELECT Nominee
FROM Academy\_Awards\_1972
WHERE Category = 'Best Director' AND Result = 'Won'
context\_str: \[NodeWithScore(node=TextNode(id\_='2ebd2cb3-7836-4f93-9898-4c0798da4a41', embedding=None, metadata={}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, hash='a74ca5f33c...

\> Running module response\_synthesis\_llm with input: 
messages: Given an input question, synthesize a response from the query results.
Query: Who won best directory in the 1972 academy awards
SQL: SELECT Nominee
FROM Academy\_Awards\_1972
WHERE Category = 'Best Dire...

assistant: The winner for Best Director in the 1972 Academy Awards was William Friedkin.

In \[ \]:

Copied!

response \= qp.run(query\="What was the term of Pasquale Preziosa?")
print(str(response))

response = qp.run(query="What was the term of Pasquale Preziosa?") print(str(response))

\> Running module input with input: 
query: What was the term of Pasquale Preziosa?

\> Running module table\_retriever with input: 
input: What was the term of Pasquale Preziosa?

\> Running module table\_output\_parser with input: 
table\_schema\_objs: \[SQLTableSchema(table\_name='Italian\_Presidents', context\_str='List of Italian Presidents and their terms in office'), SQLTableSchema(table\_name='Italian\_Presidents', context\_str='List of Italian Presi...

\> Running module text2sql\_prompt with input: 
query\_str: What was the term of Pasquale Preziosa?
schema: Table 'Italian\_Presidents' has columns: Name (VARCHAR), Term\_start (VARCHAR), Term\_end (VARCHAR), and foreign keys: . The table description is: List of Italian Presidents and their terms in office

Ta...

\> Running module text2sql\_llm with input: 
messages: Given an input question, first create a syntactically correct sqlite query to run, then look at the results of the query and return the answer. You can order the results by a relevant column to return...

\> Running module sql\_output\_parser with input: 
response: assistant: SELECT Term\_start, Term\_end
FROM Italian\_Presidents
WHERE Name = 'Pasquale Preziosa'
SQLResult: Term\_start = '2006-05-18', Term\_end = '2006-05-22'
Answer: Pasquale Preziosa's term was from ...

RAW RESPONSE  SELECT Term\_start, Term\_end
FROM Italian\_Presidents
WHERE Name = 'Pasquale Preziosa'
SQLResult: Term\_start = '2006-05-18', Term\_end = '2006-05-22'
Answer: Pasquale Preziosa's term was from May 18, 2006 to May 22, 2006.
\> Running module sql\_retriever with input: 
input: SELECT Term\_start, Term\_end
FROM Italian\_Presidents
WHERE Name = 'Pasquale Preziosa'

\> Running module response\_synthesis\_prompt with input: 
query\_str: What was the term of Pasquale Preziosa?
sql\_query: SELECT Term\_start, Term\_end
FROM Italian\_Presidents
WHERE Name = 'Pasquale Preziosa'
context\_str: \[NodeWithScore(node=TextNode(id\_='75dfe777-3186-4a57-8969-9e33fb8ab41a', embedding=None, metadata={}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, hash='99f2d91e91...

\> Running module response\_synthesis\_llm with input: 
messages: Given an input question, synthesize a response from the query results.
Query: What was the term of Pasquale Preziosa?
SQL: SELECT Term\_start, Term\_end
FROM Italian\_Presidents
WHERE Name = 'Pasquale Pr...

assistant: Pasquale Preziosa's term started on 25 February 2013 and he is currently the incumbent.

2\. Advanced Capability 2: Text-to-SQL with Query-Time Row Retrieval (along with Table Retrieval)[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_sql/#2-advanced-capability-2-text-to-sql-with-query-time-row-retrieval-along-with-table-retrieval)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

One problem in the previous example is that if the user asks a query that asks for "The Notorious BIG" but the artist is stored as "The Notorious B.I.G", then the generated SELECT statement will likely not return any matches.

We can alleviate this problem by fetching a small number of example rows per table. A naive option would be to just take the first k rows. Instead, we embed, index, and retrieve k relevant rows given the user query to give the text-to-SQL LLM the most contextually relevant information for SQL generation.

We now extend our query pipeline.

### Index Each Table[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_sql/#index-each-table)

We embed/index the rows of each table, resulting in one index per table.

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, load\_index\_from\_storage
from sqlalchemy import text
from llama\_index.core.schema import TextNode
from llama\_index.core import StorageContext
import os
from pathlib import Path
from typing import Dict

def index\_all\_tables(
    sql\_database: SQLDatabase, table\_index\_dir: str \= "table\_index\_dir"
) \-> Dict\[str, VectorStoreIndex\]:
    """Index all tables."""
    if not Path(table\_index\_dir).exists():
        os.makedirs(table\_index\_dir)

    vector\_index\_dict \= {}
    engine \= sql\_database.engine
    for table\_name in sql\_database.get\_usable\_table\_names():
        print(f"Indexing rows in table: {table\_name}")
        if not os.path.exists(f"{table\_index\_dir}/{table\_name}"):
            \# get all rows from table
            with engine.connect() as conn:
                cursor \= conn.execute(text(f'SELECT \* FROM "{table\_name}"'))
                result \= cursor.fetchall()
                row\_tups \= \[\]
                for row in result:
                    row\_tups.append(tuple(row))

            \# index each row, put into vector store index
            nodes \= \[TextNode(text\=str(t)) for t in row\_tups\]

            \# put into vector store index (use OpenAIEmbeddings by default)
            index \= VectorStoreIndex(nodes)

            \# save index
            index.set\_index\_id("vector\_index")
            index.storage\_context.persist(f"{table\_index\_dir}/{table\_name}")
        else:
            \# rebuild storage context
            storage\_context \= StorageContext.from\_defaults(
                persist\_dir\=f"{table\_index\_dir}/{table\_name}"
            )
            \# load index
            index \= load\_index\_from\_storage(
                storage\_context, index\_id\="vector\_index"
            )
        vector\_index\_dict\[table\_name\] \= index

    return vector\_index\_dict

vector\_index\_dict \= index\_all\_tables(sql\_database)

from llama\_index.core import VectorStoreIndex, load\_index\_from\_storage from sqlalchemy import text from llama\_index.core.schema import TextNode from llama\_index.core import StorageContext import os from pathlib import Path from typing import Dict def index\_all\_tables( sql\_database: SQLDatabase, table\_index\_dir: str = "table\_index\_dir" ) -> Dict\[str, VectorStoreIndex\]: """Index all tables.""" if not Path(table\_index\_dir).exists(): os.makedirs(table\_index\_dir) vector\_index\_dict = {} engine = sql\_database.engine for table\_name in sql\_database.get\_usable\_table\_names(): print(f"Indexing rows in table: {table\_name}") if not os.path.exists(f"{table\_index\_dir}/{table\_name}"): # get all rows from table with engine.connect() as conn: cursor = conn.execute(text(f'SELECT \* FROM "{table\_name}"')) result = cursor.fetchall() row\_tups = \[\] for row in result: row\_tups.append(tuple(row)) # index each row, put into vector store index nodes = \[TextNode(text=str(t)) for t in row\_tups\] # put into vector store index (use OpenAIEmbeddings by default) index = VectorStoreIndex(nodes) # save index index.set\_index\_id("vector\_index") index.storage\_context.persist(f"{table\_index\_dir}/{table\_name}") else: # rebuild storage context storage\_context = StorageContext.from\_defaults( persist\_dir=f"{table\_index\_dir}/{table\_name}" ) # load index index = load\_index\_from\_storage( storage\_context, index\_id="vector\_index" ) vector\_index\_dict\[table\_name\] = index return vector\_index\_dict vector\_index\_dict = index\_all\_tables(sql\_database)

Indexing rows in table: Academy\_Awards\_1972
Indexing rows in table: Actress\_Awards
Indexing rows in table: Actress\_Awards\_Table
Indexing rows in table: Actress\_Filmography
Indexing rows in table: Afrikaans\_Language\_Translations
Indexing rows in table: Airport\_Information
Indexing rows in table: Average\_Temperature\_Precipitation
Indexing rows in table: Average\_Temperature\_and\_Precipitation
Indexing rows in table: BBC\_Radio\_Costs
Indexing rows in table: Bad\_Boy\_Artists
Indexing rows in table: Boxing\_Matches
Indexing rows in table: Club\_Performance\_Norway
Indexing rows in table: Disappeared\_Persons
Indexing rows in table: Drop Events
Indexing rows in table: European\_Football\_Standings
Indexing rows in table: Football\_Team\_Records
Indexing rows in table: Gortynia\_Municipalities
Indexing rows in table: Grammy\_Awards
Indexing rows in table: Italian\_Presidents
Indexing rows in table: Kentucky\_Derby\_Winners
Indexing rows in table: Kinase\_Cancer\_Relationships
Indexing rows in table: Kodachrome\_Film
Indexing rows in table: New\_Mexico\_Officials
Indexing rows in table: Number\_Encoding\_Probability
Indexing rows in table: Peak\_Chart\_Positions
Indexing rows in table: Political Positions of Lord Beaverbrook
Indexing rows in table: Radio\_Stations
Indexing rows in table: Renaissance\_Discography
Indexing rows in table: Schools\_in\_Ohio
Indexing rows in table: Temperature\_and\_Precipitation
Indexing rows in table: Voter\_Party\_Statistics
Indexing rows in table: Voter\_Registration\_Statistics
Indexing rows in table: Yamato\_District\_Area\_Population
Indexing rows in table: Yearly\_Deaths\_and\_Accidents

In \[ \]:

Copied!

test\_retriever \= vector\_index\_dict\["Bad\_Boy\_Artists"\].as\_retriever(
    similarity\_top\_k\=1
)
nodes \= test\_retriever.retrieve("P. Diddy")
print(nodes\[0\].get\_content())

test\_retriever = vector\_index\_dict\["Bad\_Boy\_Artists"\].as\_retriever( similarity\_top\_k=1 ) nodes = test\_retriever.retrieve("P. Diddy") print(nodes\[0\].get\_content())

('Diddy', 1993, '6')

### Define Expanded Table Parser Component[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_sql/#define-expanded-table-parser-component)

We expand the capability of our `table_parser_component` to not only return the relevant table schemas, but also return relevant rows per table schema.

It now takes in both `table_schema_objs` (output of table retriever), but also the original `query_str` which will then be used for vector retrieval of relevant rows.

In \[ \]:

Copied!

from llama\_index.core.retrievers import SQLRetriever
from typing import List
from llama\_index.core.query\_pipeline import FnComponent

sql\_retriever \= SQLRetriever(sql\_database)

def get\_table\_context\_and\_rows\_str(
    query\_str: str, table\_schema\_objs: List\[SQLTableSchema\]
):
    """Get table context string."""
    context\_strs \= \[\]
    for table\_schema\_obj in table\_schema\_objs:
        \# first append table info + additional context
        table\_info \= sql\_database.get\_single\_table\_info(
            table\_schema\_obj.table\_name
        )
        if table\_schema\_obj.context\_str:
            table\_opt\_context \= " The table description is: "
            table\_opt\_context += table\_schema\_obj.context\_str
            table\_info += table\_opt\_context

        \# also lookup vector index to return relevant table rows
        vector\_retriever \= vector\_index\_dict\[
            table\_schema\_obj.table\_name
        \].as\_retriever(similarity\_top\_k\=2)
        relevant\_nodes \= vector\_retriever.retrieve(query\_str)
        if len(relevant\_nodes) \> 0:
            table\_row\_context \= "\\nHere are some relevant example rows (values in the same order as columns above)\\n"
            for node in relevant\_nodes:
                table\_row\_context += str(node.get\_content()) + "\\n"
            table\_info += table\_row\_context

        context\_strs.append(table\_info)
    return "\\n\\n".join(context\_strs)

table\_parser\_component \= FnComponent(fn\=get\_table\_context\_and\_rows\_str)

from llama\_index.core.retrievers import SQLRetriever from typing import List from llama\_index.core.query\_pipeline import FnComponent sql\_retriever = SQLRetriever(sql\_database) def get\_table\_context\_and\_rows\_str( query\_str: str, table\_schema\_objs: List\[SQLTableSchema\] ): """Get table context string.""" context\_strs = \[\] for table\_schema\_obj in table\_schema\_objs: # first append table info + additional context table\_info = sql\_database.get\_single\_table\_info( table\_schema\_obj.table\_name ) if table\_schema\_obj.context\_str: table\_opt\_context = " The table description is: " table\_opt\_context += table\_schema\_obj.context\_str table\_info += table\_opt\_context # also lookup vector index to return relevant table rows vector\_retriever = vector\_index\_dict\[ table\_schema\_obj.table\_name \].as\_retriever(similarity\_top\_k=2) relevant\_nodes = vector\_retriever.retrieve(query\_str) if len(relevant\_nodes) > 0: table\_row\_context = "\\nHere are some relevant example rows (values in the same order as columns above)\\n" for node in relevant\_nodes: table\_row\_context += str(node.get\_content()) + "\\n" table\_info += table\_row\_context context\_strs.append(table\_info) return "\\n\\n".join(context\_strs) table\_parser\_component = FnComponent(fn=get\_table\_context\_and\_rows\_str)

### Define Expanded Query Pipeline[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_sql/#define-expanded-query-pipeline)

This looks similar to the query pipeline in section 1, but with an upgraded table\_parser\_component.

In \[ \]:

Copied!

from llama\_index.core.query\_pipeline import (
    QueryPipeline as QP,
    Link,
    InputComponent,
    CustomQueryComponent,
)

qp \= QP(
    modules\={
        "input": InputComponent(),
        "table\_retriever": obj\_retriever,
        "table\_output\_parser": table\_parser\_component,
        "text2sql\_prompt": text2sql\_prompt,
        "text2sql\_llm": llm,
        "sql\_output\_parser": sql\_parser\_component,
        "sql\_retriever": sql\_retriever,
        "response\_synthesis\_prompt": response\_synthesis\_prompt,
        "response\_synthesis\_llm": llm,
    },
    verbose\=True,
)

from llama\_index.core.query\_pipeline import ( QueryPipeline as QP, Link, InputComponent, CustomQueryComponent, ) qp = QP( modules={ "input": InputComponent(), "table\_retriever": obj\_retriever, "table\_output\_parser": table\_parser\_component, "text2sql\_prompt": text2sql\_prompt, "text2sql\_llm": llm, "sql\_output\_parser": sql\_parser\_component, "sql\_retriever": sql\_retriever, "response\_synthesis\_prompt": response\_synthesis\_prompt, "response\_synthesis\_llm": llm, }, verbose=True, )

In \[ \]:

Copied!

qp.add\_link("input", "table\_retriever")
qp.add\_link("input", "table\_output\_parser", dest\_key\="query\_str")
qp.add\_link(
    "table\_retriever", "table\_output\_parser", dest\_key\="table\_schema\_objs"
)
qp.add\_link("input", "text2sql\_prompt", dest\_key\="query\_str")
qp.add\_link("table\_output\_parser", "text2sql\_prompt", dest\_key\="schema")
qp.add\_chain(
    \["text2sql\_prompt", "text2sql\_llm", "sql\_output\_parser", "sql\_retriever"\]
)
qp.add\_link(
    "sql\_output\_parser", "response\_synthesis\_prompt", dest\_key\="sql\_query"
)
qp.add\_link(
    "sql\_retriever", "response\_synthesis\_prompt", dest\_key\="context\_str"
)
qp.add\_link("input", "response\_synthesis\_prompt", dest\_key\="query\_str")
qp.add\_link("response\_synthesis\_prompt", "response\_synthesis\_llm")

qp.add\_link("input", "table\_retriever") qp.add\_link("input", "table\_output\_parser", dest\_key="query\_str") qp.add\_link( "table\_retriever", "table\_output\_parser", dest\_key="table\_schema\_objs" ) qp.add\_link("input", "text2sql\_prompt", dest\_key="query\_str") qp.add\_link("table\_output\_parser", "text2sql\_prompt", dest\_key="schema") qp.add\_chain( \["text2sql\_prompt", "text2sql\_llm", "sql\_output\_parser", "sql\_retriever"\] ) qp.add\_link( "sql\_output\_parser", "response\_synthesis\_prompt", dest\_key="sql\_query" ) qp.add\_link( "sql\_retriever", "response\_synthesis\_prompt", dest\_key="context\_str" ) qp.add\_link("input", "response\_synthesis\_prompt", dest\_key="query\_str") qp.add\_link("response\_synthesis\_prompt", "response\_synthesis\_llm")

In \[ \]:

Copied!

from pyvis.network import Network

net \= Network(notebook\=True, cdn\_resources\="in\_line", directed\=True)
net.from\_nx(qp.dag)
net.show("text2sql\_dag.html")

from pyvis.network import Network net = Network(notebook=True, cdn\_resources="in\_line", directed=True) net.from\_nx(qp.dag) net.show("text2sql\_dag.html")

### Run Some Queries[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_sql/#run-some-queries)

We can now ask about relevant entries even if it doesn't exactly match the entry in the database.

In \[ \]:

Copied!

response \= qp.run(
    query\="What was the year that The Notorious BIG was signed to Bad Boy?"
)
print(str(response))

response = qp.run( query="What was the year that The Notorious BIG was signed to Bad Boy?" ) print(str(response))

\> Running module input with input: 
query: What was the year that The Notorious BIG was signed to Bad Boy?

\> Running module table\_retriever with input: 
input: What was the year that The Notorious BIG was signed to Bad Boy?

\> Running module table\_output\_parser with input: 
query\_str: What was the year that The Notorious BIG was signed to Bad Boy?
table\_schema\_objs: \[SQLTableSchema(table\_name='Bad\_Boy\_Artists', context\_str='List of artists signed to Bad Boy Records and their album releases'), SQLTableSchema(table\_name='Bad\_Boy\_Artists', context\_str='List of artis...

\> Running module text2sql\_prompt with input: 
query\_str: What was the year that The Notorious BIG was signed to Bad Boy?
schema: Table 'Bad\_Boy\_Artists' has columns: Act (VARCHAR), Year\_signed (INTEGER), \_Albums\_released\_under\_Bad\_Boy (VARCHAR), and foreign keys: . The table description is: List of artists signed to Bad Boy Rec...

\> Running module text2sql\_llm with input: 
messages: Given an input question, first create a syntactically correct sqlite query to run, then look at the results of the query and return the answer. You can order the results by a relevant column to return...

\> Running module sql\_output\_parser with input: 
response: assistant: SELECT Year\_signed
FROM Bad\_Boy\_Artists
WHERE Act = 'The Notorious B.I.G'
SQLResult: 1993
Answer: The Notorious BIG was signed to Bad Boy in 1993.

RAW RESPONSE  SELECT Year\_signed
FROM Bad\_Boy\_Artists
WHERE Act = 'The Notorious B.I.G'
SQLResult: 1993
Answer: The Notorious BIG was signed to Bad Boy in 1993.
\> Running module sql\_retriever with input: 
input: SELECT Year\_signed
FROM Bad\_Boy\_Artists
WHERE Act = 'The Notorious B.I.G'

\> Running module response\_synthesis\_prompt with input: 
query\_str: What was the year that The Notorious BIG was signed to Bad Boy?
sql\_query: SELECT Year\_signed
FROM Bad\_Boy\_Artists
WHERE Act = 'The Notorious B.I.G'
context\_str: \[NodeWithScore(node=TextNode(id\_='23214862-784c-4f2b-b489-39d61ea96580', embedding=None, metadata={}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, hash='c336a1cbf9...

\> Running module response\_synthesis\_llm with input: 
messages: Given an input question, synthesize a response from the query results.
Query: What was the year that The Notorious BIG was signed to Bad Boy?
SQL: SELECT Year\_signed
FROM Bad\_Boy\_Artists
WHERE Act = '...

assistant: The Notorious BIG was signed to Bad Boy in 1993.

Back to top

[Previous Query Pipeline with Routing](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_routing/)[Next HyDE Query Transform](https://docs.llamaindex.ai/en/stable/examples/query_transformations/HyDEQueryTransformDemo/)
