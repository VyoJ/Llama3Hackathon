Title: SQL Auto Vector Query Engine

URL Source: https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLAutoVectorQueryEngine/

Markdown Content:
SQL Auto Vector Query Engine - LlamaIndex


In this tutorial, we show you how to use our SQLAutoVectorQueryEngine.

This query engine allows you to combine insights from your structured tables with your unstructured data. It first decides whether to query your structured tables for insights. Once it does, it can then infer a corresponding query to the vector store in order to fetch corresponding documents.

**NOTE:** Any Text-to-SQL application should be aware that executing arbitrary SQL queries can be a security risk. It is recommended to take precautions as needed, such as using restricted roles, read-only databases, sandboxing, etc.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-pinecone
%pip install llama\-index\-readers\-wikipedia
%pip install llama\-index\-llms\-openai

%pip install llama-index-vector-stores-pinecone %pip install llama-index-readers-wikipedia %pip install llama-index-llms-openai

In \[ \]:

Copied!

import openai
import os

os.environ\["OPENAI\_API\_KEY"\] \= "\[You API key\]"

import openai import os os.environ\["OPENAI\_API\_KEY"\] = "\[You API key\]"

### Setup[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLAutoVectorQueryEngine/#setup)

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

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

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

\# NOTE: This is ONLY necessary in jupyter notebook. # Details: Jupyter runs an event-loop behind the scenes. # This results in nested event-loops when we start an event-loop to make async queries. # This is normally not allowed, we use nest\_asyncio to allow it for convenience. import nest\_asyncio nest\_asyncio.apply() import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

### Create Common Objects[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLAutoVectorQueryEngine/#create-common-objects)

This includes a `ServiceContext` object containing abstractions such as the LLM and chunk size. This also includes a `StorageContext` object containing our vector store abstractions.

In \[ \]:

Copied!

\# define pinecone index
import pinecone
import os

api\_key \= os.environ\["PINECONE\_API\_KEY"\]
pinecone.init(api\_key\=api\_key, environment\="us-west1-gcp-free")

\# dimensions are for text-embedding-ada-002
\# pinecone.create\_index("quickstart", dimension=1536, metric="euclidean", pod\_type="p1")
pinecone\_index \= pinecone.Index("quickstart")

\# define pinecone index import pinecone import os api\_key = os.environ\["PINECONE\_API\_KEY"\] pinecone.init(api\_key=api\_key, environment="us-west1-gcp-free") # dimensions are for text-embedding-ada-002 # pinecone.create\_index("quickstart", dimension=1536, metric="euclidean", pod\_type="p1") pinecone\_index = pinecone.Index("quickstart")

/Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages/pinecone/index.py:4: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user\_install.html
  from tqdm.autonotebook import tqdm

In \[ \]:

Copied!

\# OPTIONAL: delete all
pinecone\_index.delete(deleteAll\=True)

\# OPTIONAL: delete all pinecone\_index.delete(deleteAll=True)

Out\[ \]:

{}

In \[ \]:

Copied!

from llama\_index.core import StorageContext
from llama\_index.vector\_stores.pinecone import PineconeVectorStore
from llama\_index.core import VectorStoreIndex

\# define pinecone vector index
vector\_store \= PineconeVectorStore(
    pinecone\_index\=pinecone\_index, namespace\="wiki\_cities"
)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
vector\_index \= VectorStoreIndex(\[\], storage\_context\=storage\_context)

from llama\_index.core import StorageContext from llama\_index.vector\_stores.pinecone import PineconeVectorStore from llama\_index.core import VectorStoreIndex # define pinecone vector index vector\_store = PineconeVectorStore( pinecone\_index=pinecone\_index, namespace="wiki\_cities" ) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) vector\_index = VectorStoreIndex(\[\], storage\_context=storage\_context)

### Create Database Schema + Test Data[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLAutoVectorQueryEngine/#create-database-schema-test-data)

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

### Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLAutoVectorQueryEngine/#load-data)

We first show how to convert a Document into a set of Nodes, and insert into a DocumentStore.

In \[ \]:

Copied!

\# install wikipedia python package
!pip install wikipedia

\# install wikipedia python package !pip install wikipedia

Requirement already satisfied: wikipedia in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (1.4.0)
Requirement already satisfied: beautifulsoup4 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from wikipedia) (4.12.2)
Requirement already satisfied: requests<3.0.0,>=2.0.0 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from wikipedia) (2.31.0)
Requirement already satisfied: idna<4,>=2.5 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from requests<3.0.0,>=2.0.0->wikipedia) (3.4)
Requirement already satisfied: charset-normalizer<4,>=2 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from requests<3.0.0,>=2.0.0->wikipedia) (3.2.0)
Requirement already satisfied: certifi>=2017.4.17 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from requests<3.0.0,>=2.0.0->wikipedia) (2023.5.7)
Requirement already satisfied: urllib3<3,>=1.21.1 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from requests<3.0.0,>=2.0.0->wikipedia) (1.26.16)
Requirement already satisfied: soupsieve>1.2 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from beautifulsoup4->wikipedia) (2.4.1)
WARNING: You are using pip version 21.2.4; however, version 23.2 is available.
You should consider upgrading via the '/Users/loganmarkewich/llama\_index/llama-index/bin/python3 -m pip install --upgrade pip' command.

In \[ \]:

Copied!

from llama\_index.readers.wikipedia import WikipediaReader

cities \= \["Toronto", "Berlin", "Tokyo"\]
wiki\_docs \= WikipediaReader().load\_data(pages\=cities)

from llama\_index.readers.wikipedia import WikipediaReader cities = \["Toronto", "Berlin", "Tokyo"\] wiki\_docs = WikipediaReader().load\_data(pages=cities)

### Build SQL Index[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLAutoVectorQueryEngine/#build-sql-index)

In \[ \]:

Copied!

from llama\_index.core import SQLDatabase

sql\_database \= SQLDatabase(engine, include\_tables\=\["city\_stats"\])

from llama\_index.core import SQLDatabase sql\_database = SQLDatabase(engine, include\_tables=\["city\_stats"\])

In \[ \]:

Copied!

from llama\_index.core.query\_engine import NLSQLTableQueryEngine

sql\_query\_engine \= NLSQLTableQueryEngine(
    sql\_database\=sql\_database,
    tables\=\["city\_stats"\],
)

from llama\_index.core.query\_engine import NLSQLTableQueryEngine sql\_query\_engine = NLSQLTableQueryEngine( sql\_database=sql\_database, tables=\["city\_stats"\], )

### Build Vector Index[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLAutoVectorQueryEngine/#build-vector-index)

In \[ \]:

Copied!

from llama\_index.core import Settings

\# Insert documents into vector index
\# Each document has metadata of the city attached
for city, wiki\_doc in zip(cities, wiki\_docs):
    nodes \= Settings.node\_parser.get\_nodes\_from\_documents(\[wiki\_doc\])
    \# add metadata to each node
    for node in nodes:
        node.metadata \= {"title": city}
    vector\_index.insert\_nodes(nodes)

from llama\_index.core import Settings # Insert documents into vector index # Each document has metadata of the city attached for city, wiki\_doc in zip(cities, wiki\_docs): nodes = Settings.node\_parser.get\_nodes\_from\_documents(\[wiki\_doc\]) # add metadata to each node for node in nodes: node.metadata = {"title": city} vector\_index.insert\_nodes(nodes)

Upserted vectors: 100%|██████████| 20/20 \[00:00<00:00, 22.37it/s\]
Upserted vectors: 100%|██████████| 22/22 \[00:00<00:00, 23.14it/s\]
Upserted vectors: 100%|██████████| 13/13 \[00:00<00:00, 17.67it/s\]

### Define Query Engines, Set as Tools[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLAutoVectorQueryEngine/#define-query-engines-set-as-tools)

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI
from llama\_index.core.retrievers import VectorIndexAutoRetriever
from llama\_index.core.vector\_stores import MetadataInfo, VectorStoreInfo
from llama\_index.core.query\_engine import RetrieverQueryEngine

vector\_store\_info \= VectorStoreInfo(
    content\_info\="articles about different cities",
    metadata\_info\=\[
        MetadataInfo(
            name\="title", type\="str", description\="The name of the city"
        ),
    \],
)
vector\_auto\_retriever \= VectorIndexAutoRetriever(
    vector\_index, vector\_store\_info\=vector\_store\_info
)

retriever\_query\_engine \= RetrieverQueryEngine.from\_args(
    vector\_auto\_retriever, llm\=OpenAI(model\="gpt-4")
)

from llama\_index.llms.openai import OpenAI from llama\_index.core.retrievers import VectorIndexAutoRetriever from llama\_index.core.vector\_stores import MetadataInfo, VectorStoreInfo from llama\_index.core.query\_engine import RetrieverQueryEngine vector\_store\_info = VectorStoreInfo( content\_info="articles about different cities", metadata\_info=\[ MetadataInfo( name="title", type="str", description="The name of the city" ), \], ) vector\_auto\_retriever = VectorIndexAutoRetriever( vector\_index, vector\_store\_info=vector\_store\_info ) retriever\_query\_engine = RetrieverQueryEngine.from\_args( vector\_auto\_retriever, llm=OpenAI(model="gpt-4") )

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
vector\_tool \= QueryEngineTool.from\_defaults(
    query\_engine\=retriever\_query\_engine,
    description\=(
        f"Useful for answering semantic questions about different cities"
    ),
)

from llama\_index.core.tools import QueryEngineTool sql\_tool = QueryEngineTool.from\_defaults( query\_engine=sql\_query\_engine, description=( "Useful for translating a natural language query into a SQL query over" " a table containing: city\_stats, containing the population/country of" " each city" ), ) vector\_tool = QueryEngineTool.from\_defaults( query\_engine=retriever\_query\_engine, description=( f"Useful for answering semantic questions about different cities" ), )

### Define SQLAutoVectorQueryEngine[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLAutoVectorQueryEngine/#define-sqlautovectorqueryengine)

In \[ \]:

Copied!

from llama\_index.core.query\_engine import SQLAutoVectorQueryEngine

query\_engine \= SQLAutoVectorQueryEngine(
    sql\_tool, vector\_tool, llm\=OpenAI(model\="gpt-4")
)

from llama\_index.core.query\_engine import SQLAutoVectorQueryEngine query\_engine = SQLAutoVectorQueryEngine( sql\_tool, vector\_tool, llm=OpenAI(model="gpt-4") )

In \[ \]:

Copied!

response \= query\_engine.query(
    "Tell me about the arts and culture of the city with the highest"
    " population"
)

response = query\_engine.query( "Tell me about the arts and culture of the city with the highest" " population" )

Querying SQL database: Useful for translating a natural language query into a SQL query over a table containing city\_stats, containing the population/country of each city
INFO:llama\_index.query\_engine.sql\_join\_query\_engine:> Querying SQL database: Useful for translating a natural language query into a SQL query over a table containing city\_stats, containing the population/country of each city
> Querying SQL database: Useful for translating a natural language query into a SQL query over a table containing city\_stats, containing the population/country of each city
INFO:llama\_index.indices.struct\_store.sql\_query:> Table desc str: Table 'city\_stats' has columns: city\_name (VARCHAR(16)), population (INTEGER), country (VARCHAR(16)) and foreign keys: .
> Table desc str: Table 'city\_stats' has columns: city\_name (VARCHAR(16)), population (INTEGER), country (VARCHAR(16)) and foreign keys: .
SQL query: SELECT city\_name, population FROM city\_stats ORDER BY population DESC LIMIT 1;
SQL response: 
Tokyo is the city with the highest population, with 13.96 million people. It is a vibrant city with a rich culture and a wide variety of art forms. From traditional Japanese art such as calligraphy and woodblock prints to modern art galleries and museums, Tokyo has something for everyone. There are also many festivals and events throughout the year that celebrate the city's culture and art.
Transformed query given SQL response: What are some specific cultural festivals, events, and notable art galleries or museums in Tokyo?
INFO:llama\_index.query\_engine.sql\_join\_query\_engine:> Transformed query given SQL response: What are some specific cultural festivals, events, and notable art galleries or museums in Tokyo?
> Transformed query given SQL response: What are some specific cultural festivals, events, and notable art galleries or museums in Tokyo?
INFO:llama\_index.indices.vector\_store.retrievers.auto\_retriever.auto\_retriever:Using query str: cultural festivals events art galleries museums Tokyo
Using query str: cultural festivals events art galleries museums Tokyo
INFO:llama\_index.indices.vector\_store.retrievers.auto\_retriever.auto\_retriever:Using filters: {'title': 'Tokyo'}
Using filters: {'title': 'Tokyo'}
INFO:llama\_index.indices.vector\_store.retrievers.auto\_retriever.auto\_retriever:Using top\_k: 2
Using top\_k: 2
query engine response: The context information mentions the Tokyo National Museum, which houses 37% of the country's artwork national treasures. It also mentions the Studio Ghibli anime center as a subcultural attraction. However, the text does not provide information on specific cultural festivals or events in Tokyo.
INFO:llama\_index.query\_engine.sql\_join\_query\_engine:> query engine response: The context information mentions the Tokyo National Museum, which houses 37% of the country's artwork national treasures. It also mentions the Studio Ghibli anime center as a subcultural attraction. However, the text does not provide information on specific cultural festivals or events in Tokyo.
> query engine response: The context information mentions the Tokyo National Museum, which houses 37% of the country's artwork national treasures. It also mentions the Studio Ghibli anime center as a subcultural attraction. However, the text does not provide information on specific cultural festivals or events in Tokyo.
Final response: Tokyo, the city with the highest population of 13.96 million people, is known for its vibrant culture and diverse art forms. It is home to traditional Japanese art such as calligraphy and woodblock prints, as well as modern art galleries and museums. Notably, the Tokyo National Museum houses 37% of the country's artwork national treasures, and the Studio Ghibli anime center is a popular subcultural attraction. While there are many festivals and events throughout the year that celebrate the city's culture and art, specific examples were not provided in the available information.

In \[ \]:

Copied!

print(str(response))

print(str(response))

Tokyo, the city with the highest population of 13.96 million people, is known for its vibrant culture and diverse art forms. It is home to traditional Japanese art such as calligraphy and woodblock prints, as well as modern art galleries and museums. Notably, the Tokyo National Museum houses 37% of the country's artwork national treasures, and the Studio Ghibli anime center is a popular subcultural attraction. While there are many festivals and events throughout the year that celebrate the city's culture and art, specific examples were not provided in the available information.

In \[ \]:

Copied!

response \= query\_engine.query("Tell me about the history of Berlin")

response = query\_engine.query("Tell me about the history of Berlin")

Querying other query engine: Useful for answering semantic questions about different cities
INFO:llama\_index.query\_engine.sql\_join\_query\_engine:> Querying other query engine: Useful for answering semantic questions about different cities
> Querying other query engine: Useful for answering semantic questions about different cities
INFO:llama\_index.indices.vector\_store.retrievers.auto\_retriever.auto\_retriever:Using query str: history of Berlin
Using query str: history of Berlin
INFO:llama\_index.indices.vector\_store.retrievers.auto\_retriever.auto\_retriever:Using filters: {'title': 'Berlin'}
Using filters: {'title': 'Berlin'}
INFO:llama\_index.indices.vector\_store.retrievers.auto\_retriever.auto\_retriever:Using top\_k: 2
Using top\_k: 2
Query Engine response: Berlin's history dates back to around 60,000 BC, with the earliest human traces found in the area. A Mesolithic deer antler mask found in Biesdorf (Berlin) was dated around 9000 BC. During Neolithic times, a large number of communities existed in the area and in the Bronze Age, up to 1000 people lived in 50 villages. Early Germanic tribes took settlement from 500 BC and Slavic settlements and castles began around 750 AD.

The earliest evidence of middle age settlements in the area of today's Berlin are remnants of a house foundation dated to 1174, found in excavations in Berlin Mitte, and a wooden beam dated from approximately 1192. The first written records of towns in the area of present-day Berlin date from the late 12th century. Spandau is first mentioned in 1197 and Köpenick in 1209, although these areas did not join Berlin until 1920. 

The central part of Berlin can be traced back to two towns. Cölln on the Fischerinsel is first mentioned in a 1237 document, and Berlin, across the Spree in what is now called the Nikolaiviertel, is referenced in a document from 1244. 1237 is considered the founding date of the city. The two towns over time formed close economic and social ties, and profited from the staple right on the two important trade routes Via Imperii and from Bruges to Novgorod. In 1307, they formed an alliance with a common external policy, their internal administrations still being separated. In 1415, Frederick I became the elector of the Margraviate of Brandenburg, which he ruled until 1440.

The name Berlin has its roots in the language of West Slavic inhabitants of the area of today's Berlin, and may be related to the Old Polabian stem berl-/birl- ("swamp"). or Proto-Slavic bьrlogъ, (lair, den). Since the Ber- at the beginning sounds like the German word Bär ("bear"), a bear appears in the coat of arms of the city. It is therefore an example of canting arms.

In \[ \]:

Copied!

print(str(response))

print(str(response))

Berlin's history dates back to around 60,000 BC, with the earliest human traces found in the area. A Mesolithic deer antler mask found in Biesdorf (Berlin) was dated around 9000 BC. During Neolithic times, a large number of communities existed in the area and in the Bronze Age, up to 1000 people lived in 50 villages. Early Germanic tribes took settlement from 500 BC and Slavic settlements and castles began around 750 AD.

The earliest evidence of middle age settlements in the area of today's Berlin are remnants of a house foundation dated to 1174, found in excavations in Berlin Mitte, and a wooden beam dated from approximately 1192. The first written records of towns in the area of present-day Berlin date from the late 12th century. Spandau is first mentioned in 1197 and Köpenick in 1209, although these areas did not join Berlin until 1920. 

The central part of Berlin can be traced back to two towns. Cölln on the Fischerinsel is first mentioned in a 1237 document, and Berlin, across the Spree in what is now called the Nikolaiviertel, is referenced in a document from 1244. 1237 is considered the founding date of the city. The two towns over time formed close economic and social ties, and profited from the staple right on the two important trade routes Via Imperii and from Bruges to Novgorod. In 1307, they formed an alliance with a common external policy, their internal administrations still being separated. In 1415, Frederick I became the elector of the Margraviate of Brandenburg, which he ruled until 1440.

The name Berlin has its roots in the language of West Slavic inhabitants of the area of today's Berlin, and may be related to the Old Polabian stem berl-/birl- ("swamp"). or Proto-Slavic bьrlogъ, (lair, den). Since the Ber- at the beginning sounds like the German word Bär ("bear"), a bear appears in the coat of arms of the city. It is therefore an example of canting arms.

In \[ \]:

Copied!

response \= query\_engine.query(
    "Can you give me the country corresponding to each city?"
)

response = query\_engine.query( "Can you give me the country corresponding to each city?" )

Querying SQL database: Useful for translating a natural language query into a SQL query over a table containing: city\_stats, containing the population/country of each city
INFO:llama\_index.query\_engine.sql\_join\_query\_engine:> Querying SQL database: Useful for translating a natural language query into a SQL query over a table containing: city\_stats, containing the population/country of each city
> Querying SQL database: Useful for translating a natural language query into a SQL query over a table containing: city\_stats, containing the population/country of each city
INFO:llama\_index.indices.struct\_store.sql\_query:> Table desc str: Table 'city\_stats' has columns: city\_name (VARCHAR(16)), population (INTEGER), country (VARCHAR(16)) and foreign keys: .
> Table desc str: Table 'city\_stats' has columns: city\_name (VARCHAR(16)), population (INTEGER), country (VARCHAR(16)) and foreign keys: .
SQL query: SELECT city\_name, country FROM city\_stats;
SQL response:  Toronto is in Canada, Tokyo is in Japan, and Berlin is in Germany.
Transformed query given SQL response: What countries are New York, San Francisco, and other cities in?
INFO:llama\_index.query\_engine.sql\_join\_query\_engine:> Transformed query given SQL response: What countries are New York, San Francisco, and other cities in?
> Transformed query given SQL response: What countries are New York, San Francisco, and other cities in?
INFO:llama\_index.indices.vector\_store.retrievers.auto\_retriever.auto\_retriever:Using query str: New York San Francisco
Using query str: New York San Francisco
INFO:llama\_index.indices.vector\_store.retrievers.auto\_retriever.auto\_retriever:Using filters: {'title': 'San Francisco'}
Using filters: {'title': 'San Francisco'}
INFO:llama\_index.indices.vector\_store.retrievers.auto\_retriever.auto\_retriever:Using top\_k: 2
Using top\_k: 2
query engine response: None
INFO:llama\_index.query\_engine.sql\_join\_query\_engine:> query engine response: None
> query engine response: None
Final response: The country corresponding to each city is as follows: Toronto is in Canada, Tokyo is in Japan, and Berlin is in Germany. Unfortunately, I do not have information on the countries for New York, San Francisco, and other cities.

In \[ \]:

Copied!

print(str(response))

print(str(response))

The country corresponding to each city is as follows: Toronto is in Canada, Tokyo is in Japan, and Berlin is in Germany. Unfortunately, I do not have information on the countries for New York, San Francisco, and other cities.

Back to top

[Previous Router Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/RouterQueryEngine/)[Next SQL Join Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLJoinQueryEngine/)

Hi, how can I help you?

🦙
