Title: SQL Router Query Engine - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLRouterQueryEngine/

Markdown Content:
SQL Router Query Engine - LlamaIndex


In this tutorial, we define a custom router query engine that can route to either a SQL database or a vector database.

**NOTE:** Any Text-to-SQL application should be aware that executing arbitrary SQL queries can be a security risk. It is recommended to take precautions as needed, such as using restricted roles, read-only databases, sandboxing, etc.

### Setup[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLRouterQueryEngine/#setup)

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-readers\-wikipedia

%pip install llama-index-readers-wikipedia

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

\# NOTE: This is ONLY necessary in jupyter notebook.
\# Details: Jupyter runs an event-loop behind the scenes.
\#          This results in nested event-loops when we start an event-loop to make async queries.
\#          This is normally not allowed, we use nest\_asyncio to allow it for convenience.
import nest\_asyncio

nest\_asyncio.apply()

\# NOTE: This is ONLY necessary in jupyter notebook. # Details: Jupyter runs an event-loop behind the scenes. # This results in nested event-loops when we start an event-loop to make async queries. # This is normally not allowed, we use nest\_asyncio to allow it for convenience. import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

from llama\_index.core import VectorStoreIndex, SQLDatabase
from llama\_index.readers.wikipedia import WikipediaReader

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout)) from llama\_index.core import VectorStoreIndex, SQLDatabase from llama\_index.readers.wikipedia import WikipediaReader

INFO:numexpr.utils:Note: NumExpr detected 12 cores but "NUMEXPR\_MAX\_THREADS" not set, so enforcing safe limit of 8.
Note: NumExpr detected 12 cores but "NUMEXPR\_MAX\_THREADS" not set, so enforcing safe limit of 8.
INFO:numexpr.utils:NumExpr defaulting to 8 threads.
NumExpr defaulting to 8 threads.

/Users/jerryliu/Programming/gpt\_index/.venv/lib/python3.10/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user\_install.html
  from .autonotebook import tqdm as notebook\_tqdm

### Create Database Schema + Test Data[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLRouterQueryEngine/#create-database-schema-test-data)

Here we introduce a toy scenario where there are 100 tables (too big to fit into the prompt)

In \[ \]:

Copied!

from sqlalchemy import (
    create\_engine,
    MetaData,
    Table,
    Column,
    String,
    Integer,
    select,
    column,
)

from sqlalchemy import ( create\_engine, MetaData, Table, Column, String, Integer, select, column, )

In \[ \]:

Copied!

engine \= create\_engine("sqlite:///:memory:", future\=True)
metadata\_obj \= MetaData()

engine = create\_engine("sqlite:///:memory:", future=True) metadata\_obj = MetaData()

In \[ \]:

Copied!

\# create city SQL table
table\_name \= "city\_stats"
city\_stats\_table \= Table(
    table\_name,
    metadata\_obj,
    Column("city\_name", String(16), primary\_key\=True),
    Column("population", Integer),
    Column("country", String(16), nullable\=False),
)

metadata\_obj.create\_all(engine)

\# create city SQL table table\_name = "city\_stats" city\_stats\_table = Table( table\_name, metadata\_obj, Column("city\_name", String(16), primary\_key=True), Column("population", Integer), Column("country", String(16), nullable=False), ) metadata\_obj.create\_all(engine)

In \[ \]:

Copied!

\# print tables
metadata\_obj.tables.keys()

\# print tables metadata\_obj.tables.keys()

Out\[ \]:

dict\_keys(\['city\_stats'\])

We introduce some test data into the `city_stats` table

In \[ \]:

Copied!

from sqlalchemy import insert

rows \= \[
    {"city\_name": "Toronto", "population": 2930000, "country": "Canada"},
    {"city\_name": "Tokyo", "population": 13960000, "country": "Japan"},
    {"city\_name": "Berlin", "population": 3645000, "country": "Germany"},
\]
for row in rows:
    stmt \= insert(city\_stats\_table).values(\*\*row)
    with engine.begin() as connection:
        cursor \= connection.execute(stmt)

from sqlalchemy import insert rows = \[ {"city\_name": "Toronto", "population": 2930000, "country": "Canada"}, {"city\_name": "Tokyo", "population": 13960000, "country": "Japan"}, {"city\_name": "Berlin", "population": 3645000, "country": "Germany"}, \] for row in rows: stmt = insert(city\_stats\_table).values(\*\*row) with engine.begin() as connection: cursor = connection.execute(stmt)

In \[ \]:

Copied!

with engine.connect() as connection:
    cursor \= connection.exec\_driver\_sql("SELECT \* FROM city\_stats")
    print(cursor.fetchall())

with engine.connect() as connection: cursor = connection.exec\_driver\_sql("SELECT \* FROM city\_stats") print(cursor.fetchall())

\[('Toronto', 2930000, 'Canada'), ('Tokyo', 13960000, 'Japan'), ('Berlin', 3645000, 'Germany')\]

### Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLRouterQueryEngine/#load-data)

We first show how to convert a Document into a set of Nodes, and insert into a DocumentStore.

In \[ \]:

Copied!

\# install wikipedia python package
!pip install wikipedia

\# install wikipedia python package !pip install wikipedia

Requirement already satisfied: wikipedia in /Users/jerryliu/Programming/gpt\_index/.venv/lib/python3.10/site-packages (1.4.0)
Requirement already satisfied: requests<3.0.0,>=2.0.0 in /Users/jerryliu/Programming/gpt\_index/.venv/lib/python3.10/site-packages (from wikipedia) (2.28.2)
Requirement already satisfied: beautifulsoup4 in /Users/jerryliu/Programming/gpt\_index/.venv/lib/python3.10/site-packages (from wikipedia) (4.12.2)
Requirement already satisfied: idna<4,>=2.5 in /Users/jerryliu/Programming/gpt\_index/.venv/lib/python3.10/site-packages (from requests<3.0.0,>=2.0.0->wikipedia) (3.4)
Requirement already satisfied: charset-normalizer<4,>=2 in /Users/jerryliu/Programming/gpt\_index/.venv/lib/python3.10/site-packages (from requests<3.0.0,>=2.0.0->wikipedia) (3.1.0)
Requirement already satisfied: certifi>=2017.4.17 in /Users/jerryliu/Programming/gpt\_index/.venv/lib/python3.10/site-packages (from requests<3.0.0,>=2.0.0->wikipedia) (2022.12.7)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/jerryliu/Programming/gpt\_index/.venv/lib/python3.10/site-packages (from requests<3.0.0,>=2.0.0->wikipedia) (1.26.15)
Requirement already satisfied: soupsieve>1.2 in /Users/jerryliu/Programming/gpt\_index/.venv/lib/python3.10/site-packages (from beautifulsoup4->wikipedia) (2.4.1)

\[notice\] A new release of pip available: 22.3.1 -> 23.1.2
\[notice\] To update, run: pip install --upgrade pip

In \[ \]:

Copied!

cities \= \["Toronto", "Berlin", "Tokyo"\]
wiki\_docs \= WikipediaReader().load\_data(pages\=cities)

cities = \["Toronto", "Berlin", "Tokyo"\] wiki\_docs = WikipediaReader().load\_data(pages=cities)

### Build SQL Index[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLRouterQueryEngine/#build-sql-index)

In \[ \]:

Copied!

sql\_database \= SQLDatabase(engine, include\_tables\=\["city\_stats"\])

sql\_database = SQLDatabase(engine, include\_tables=\["city\_stats"\])

In \[ \]:

Copied!

from llama\_index.core.query\_engine import NLSQLTableQueryEngine

from llama\_index.core.query\_engine import NLSQLTableQueryEngine

In \[ \]:

Copied!

sql\_query\_engine \= NLSQLTableQueryEngine(
    sql\_database\=sql\_database,
    tables\=\["city\_stats"\],
)

sql\_query\_engine = NLSQLTableQueryEngine( sql\_database=sql\_database, tables=\["city\_stats"\], )

INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total embedding token usage: 0 tokens
> \[build\_index\_from\_nodes\] Total embedding token usage: 0 tokens

/Users/jerryliu/Programming/gpt\_index/.venv/lib/python3.10/site-packages/langchain/sql\_database.py:227: UserWarning: This method is deprecated - please use \`get\_usable\_table\_names\`.
  warnings.warn(

### Build Vector Index[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLRouterQueryEngine/#build-vector-index)

In \[ \]:

Copied!

\# build a separate vector index per city
\# You could also choose to define a single vector index across all docs, and annotate each chunk by metadata
vector\_indices \= \[\]
for wiki\_doc in wiki\_docs:
    vector\_index \= VectorStoreIndex.from\_documents(\[wiki\_doc\])
    vector\_indices.append(vector\_index)

\# build a separate vector index per city # You could also choose to define a single vector index across all docs, and annotate each chunk by metadata vector\_indices = \[\] for wiki\_doc in wiki\_docs: vector\_index = VectorStoreIndex.from\_documents(\[wiki\_doc\]) vector\_indices.append(vector\_index)

INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total embedding token usage: 20744 tokens
> \[build\_index\_from\_nodes\] Total embedding token usage: 20744 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total embedding token usage: 21947 tokens
> \[build\_index\_from\_nodes\] Total embedding token usage: 21947 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total embedding token usage: 12786 tokens
> \[build\_index\_from\_nodes\] Total embedding token usage: 12786 tokens

### Define Query Engines, Set as Tools[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLRouterQueryEngine/#define-query-engines-set-as-tools)

In \[ \]:

Copied!

vector\_query\_engines \= \[index.as\_query\_engine() for index in vector\_indices\]

vector\_query\_engines = \[index.as\_query\_engine() for index in vector\_indices\]

In \[ \]:

Copied!

from llama\_index.core.tools import QueryEngineTool

sql\_tool \= QueryEngineTool.from\_defaults(
    query\_engine\=sql\_query\_engine,
    description\=(
        "Useful for translating a natural language query into a SQL query over"
        " a table containing: city\_stats, containing the population/country of"
        " each city"
    ),
)
vector\_tools \= \[\]
for city, query\_engine in zip(cities, vector\_query\_engines):
    vector\_tool \= QueryEngineTool.from\_defaults(
        query\_engine\=query\_engine,
        description\=f"Useful for answering semantic questions about {city}",
    )
    vector\_tools.append(vector\_tool)

from llama\_index.core.tools import QueryEngineTool sql\_tool = QueryEngineTool.from\_defaults( query\_engine=sql\_query\_engine, description=( "Useful for translating a natural language query into a SQL query over" " a table containing: city\_stats, containing the population/country of" " each city" ), ) vector\_tools = \[\] for city, query\_engine in zip(cities, vector\_query\_engines): vector\_tool = QueryEngineTool.from\_defaults( query\_engine=query\_engine, description=f"Useful for answering semantic questions about {city}", ) vector\_tools.append(vector\_tool)

### Define Router Query Engine[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLRouterQueryEngine/#define-router-query-engine)

In \[ \]:

Copied!

from llama\_index.core.query\_engine import RouterQueryEngine
from llama\_index.core.selectors import LLMSingleSelector

query\_engine \= RouterQueryEngine(
    selector\=LLMSingleSelector.from\_defaults(),
    query\_engine\_tools\=(\[sql\_tool\] + vector\_tools),
)

from llama\_index.core.query\_engine import RouterQueryEngine from llama\_index.core.selectors import LLMSingleSelector query\_engine = RouterQueryEngine( selector=LLMSingleSelector.from\_defaults(), query\_engine\_tools=(\[sql\_tool\] + vector\_tools), )

In \[ \]:

Copied!

response \= query\_engine.query("Which city has the highest population?")
print(str(response))

response = query\_engine.query("Which city has the highest population?") print(str(response))

INFO:llama\_index.query\_engine.router\_query\_engine:Selecting query engine 0: Useful for translating a natural language query into a SQL query over a table containing: city\_stats, containing the population/country of each city.
Selecting query engine 0: Useful for translating a natural language query into a SQL query over a table containing: city\_stats, containing the population/country of each city.
INFO:llama\_index.indices.struct\_store.sql\_query:> Table desc str: Schema of table city\_stats:
Table 'city\_stats' has columns: city\_name (VARCHAR(16)), population (INTEGER), country (VARCHAR(16)) and foreign keys: .

> Table desc str: Schema of table city\_stats:
Table 'city\_stats' has columns: city\_name (VARCHAR(16)), population (INTEGER), country (VARCHAR(16)) and foreign keys: .

INFO:llama\_index.token\_counter.token\_counter:> \[query\] Total LLM token usage: 347 tokens
> \[query\] Total LLM token usage: 347 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[query\] Total embedding token usage: 0 tokens
> \[query\] Total embedding token usage: 0 tokens
 Tokyo has the highest population, with 13,960,000 people.

In \[ \]:

Copied!

response \= query\_engine.query("Tell me about the historical museums in Berlin")
print(str(response))

response = query\_engine.query("Tell me about the historical museums in Berlin") print(str(response))

INFO:llama\_index.query\_engine.router\_query\_engine:Selecting query engine 2: Useful for answering semantic questions about Berlin.
Selecting query engine 2: Useful for answering semantic questions about Berlin.
INFO:llama\_index.token\_counter.token\_counter:> \[retrieve\] Total LLM token usage: 0 tokens
> \[retrieve\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[retrieve\] Total embedding token usage: 8 tokens
> \[retrieve\] Total embedding token usage: 8 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total LLM token usage: 2031 tokens
> \[get\_response\] Total LLM token usage: 2031 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total embedding token usage: 0 tokens
> \[get\_response\] Total embedding token usage: 0 tokens

Berlin is home to many historical museums, including the Altes Museum, Neues Museum, Alte Nationalgalerie, Pergamon Museum, and Bode Museum, which are all located on Museum Island. The Gemäldegalerie (Painting Gallery) focuses on the paintings of the "old masters" from the 13th to the 18th centuries, while the Neue Nationalgalerie (New National Gallery, built by Ludwig Mies van der Rohe) specializes in 20th-century European painting. The Hamburger Bahnhof, in Moabit, exhibits a major collection of modern and contemporary art. The expanded Deutsches Historisches Museum reopened in the Zeughaus with an overview of German history spanning more than a millennium. The Bauhaus Archive is a museum of 20th-century design from the famous Bauhaus school. Museum Berggruen houses the collection of noted 20th century collector Heinz Berggruen, and features an extensive assortment of works by Picasso, Matisse, Cézanne, and Giacometti, among others. The Kupferstichkabinett Berlin (Museum of Prints and Drawings) is part of the Staatlichen Museen z

In \[ \]:

Copied!

response \= query\_engine.query("Which countries are each city from?")
print(str(response))

response = query\_engine.query("Which countries are each city from?") print(str(response))

INFO:llama\_index.query\_engine.router\_query\_engine:Selecting query engine 0: Useful for translating a natural language query into a SQL query over a table containing: city\_stats, containing the population/country of each city.
Selecting query engine 0: Useful for translating a natural language query into a SQL query over a table containing: city\_stats, containing the population/country of each city.
INFO:llama\_index.indices.struct\_store.sql\_query:> Table desc str: Schema of table city\_stats:
Table 'city\_stats' has columns: city\_name (VARCHAR(16)), population (INTEGER), country (VARCHAR(16)) and foreign keys: .

> Table desc str: Schema of table city\_stats:
Table 'city\_stats' has columns: city\_name (VARCHAR(16)), population (INTEGER), country (VARCHAR(16)) and foreign keys: .

INFO:llama\_index.token\_counter.token\_counter:> \[query\] Total LLM token usage: 334 tokens
> \[query\] Total LLM token usage: 334 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[query\] Total embedding token usage: 0 tokens
> \[query\] Total embedding token usage: 0 tokens
 Toronto is from Canada, Tokyo is from Japan, and Berlin is from Germany.

Back to top

[Previous SQL Join Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLJoinQueryEngine/)[Next CitationQueryEngine](https://docs.llamaindex.ai/en/stable/examples/query_engine/citation_query_engine/)

Hi, how can I help you?

🦙
