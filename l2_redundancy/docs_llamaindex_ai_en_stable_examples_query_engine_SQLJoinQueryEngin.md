Title: SQL Join Query Engine - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLJoinQueryEngine/

Markdown Content:
SQL Join Query Engine - LlamaIndex


In this tutorial, we show you how to use our SQLJoinQueryEngine.

This query engine allows you to combine insights from your structured tables with your unstructured data. It first decides whether to query your structured tables for insights. Once it does, it can then infer a corresponding query to the vector store in order to fetch corresponding documents.

**NOTE:** Any Text-to-SQL application should be aware that executing arbitrary SQL queries can be a security risk. It is recommended to take precautions as needed, such as using restricted roles, read-only databases, sandboxing, etc.

### Setup[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLJoinQueryEngine/#setup)

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-readers\-wikipedia
%pip install llama\-index\-llms\-openai

%pip install llama-index-readers-wikipedia %pip install llama-index-llms-openai

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

### Create Common Objects[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLJoinQueryEngine/#create-common-objects)

This includes a `ServiceContext` object containing abstractions such as the LLM and chunk size. This also includes a `StorageContext` object containing our vector store abstractions.

In \[ \]:

Copied!

\# # define pinecone index
\# import pinecone
\# import os

\# api\_key = os.environ\['PINECONE\_API\_KEY'\]
\# pinecone.init(api\_key=api\_key, environment="us-west1-gcp")

\# # dimensions are for text-embedding-ada-002
\# # pinecone.create\_index("quickstart", dimension=1536, metric="euclidean", pod\_type="p1")
\# pinecone\_index = pinecone.Index("quickstart")

\# # define pinecone index # import pinecone # import os # api\_key = os.environ\['PINECONE\_API\_KEY'\] # pinecone.init(api\_key=api\_key, environment="us-west1-gcp") # # dimensions are for text-embedding-ada-002 # # pinecone.create\_index("quickstart", dimension=1536, metric="euclidean", pod\_type="p1") # pinecone\_index = pinecone.Index("quickstart")

In \[ \]:

Copied!

\# # OPTIONAL: delete all
\# pinecone\_index.delete(deleteAll=True)

\# # OPTIONAL: delete all # pinecone\_index.delete(deleteAll=True)

### Create Database Schema + Test Data[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLJoinQueryEngine/#create-database-schema-test-data)

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

### Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLJoinQueryEngine/#load-data)

We first show how to convert a Document into a set of Nodes, and insert into a DocumentStore.

In \[ \]:

Copied!

\# install wikipedia python package
!pip install wikipedia

\# install wikipedia python package !pip install wikipedia

Requirement already satisfied: wikipedia in /Users/jerryliu/Programming/gpt\_index/.venv/lib/python3.10/site-packages (1.4.0)
Requirement already satisfied: beautifulsoup4 in /Users/jerryliu/Programming/gpt\_index/.venv/lib/python3.10/site-packages (from wikipedia) (4.12.2)
Requirement already satisfied: requests<3.0.0,>=2.0.0 in /Users/jerryliu/Programming/gpt\_index/.venv/lib/python3.10/site-packages (from wikipedia) (2.28.2)
Requirement already satisfied: certifi>=2017.4.17 in /Users/jerryliu/Programming/gpt\_index/.venv/lib/python3.10/site-packages (from requests<3.0.0,>=2.0.0->wikipedia) (2022.12.7)
Requirement already satisfied: charset-normalizer<4,>=2 in /Users/jerryliu/Programming/gpt\_index/.venv/lib/python3.10/site-packages (from requests<3.0.0,>=2.0.0->wikipedia) (3.1.0)
Requirement already satisfied: idna<4,>=2.5 in /Users/jerryliu/Programming/gpt\_index/.venv/lib/python3.10/site-packages (from requests<3.0.0,>=2.0.0->wikipedia) (3.4)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/jerryliu/Programming/gpt\_index/.venv/lib/python3.10/site-packages (from requests<3.0.0,>=2.0.0->wikipedia) (1.26.15)
Requirement already satisfied: soupsieve>1.2 in /Users/jerryliu/Programming/gpt\_index/.venv/lib/python3.10/site-packages (from beautifulsoup4->wikipedia) (2.4.1)

\[notice\] A new release of pip available: 22.3.1 -> 23.1.2
\[notice\] To update, run: pip install --upgrade pip

In \[ \]:

Copied!

from llama\_index.readers.wikipedia import WikipediaReader

cities \= \["Toronto", "Berlin", "Tokyo"\]
wiki\_docs \= WikipediaReader().load\_data(pages\=cities)

from llama\_index.readers.wikipedia import WikipediaReader cities = \["Toronto", "Berlin", "Tokyo"\] wiki\_docs = WikipediaReader().load\_data(pages=cities)

### Build SQL Index[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLJoinQueryEngine/#build-sql-index)

In \[ \]:

Copied!

from llama\_index.core import SQLDatabase

sql\_database \= SQLDatabase(engine, include\_tables\=\["city\_stats"\])

from llama\_index.core import SQLDatabase sql\_database = SQLDatabase(engine, include\_tables=\["city\_stats"\])

### Build Vector Index[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLJoinQueryEngine/#build-vector-index)

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI
from llama\_index.core import VectorStoreIndex

\# Insert documents into vector index
\# Each document has metadata of the city attached

vector\_indices \= {}
vector\_query\_engines \= {}

for city, wiki\_doc in zip(cities, wiki\_docs):
    vector\_index \= VectorStoreIndex.from\_documents(\[wiki\_doc\])
    \# modify default llm to be gpt-3.5 for quick/cheap queries
    query\_engine \= vector\_index.as\_query\_engine(
        similarity\_top\_k\=2, llm\=OpenAI(model\="gpt-3.5-turbo")
    )
    vector\_indices\[city\] \= vector\_index
    vector\_query\_engines\[city\] \= query\_engine

from llama\_index.llms.openai import OpenAI from llama\_index.core import VectorStoreIndex # Insert documents into vector index # Each document has metadata of the city attached vector\_indices = {} vector\_query\_engines = {} for city, wiki\_doc in zip(cities, wiki\_docs): vector\_index = VectorStoreIndex.from\_documents(\[wiki\_doc\]) # modify default llm to be gpt-3.5 for quick/cheap queries query\_engine = vector\_index.as\_query\_engine( similarity\_top\_k=2, llm=OpenAI(model="gpt-3.5-turbo") ) vector\_indices\[city\] = vector\_index vector\_query\_engines\[city\] = query\_engine

### Define Query Engines, Set as Tools[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLJoinQueryEngine/#define-query-engines-set-as-tools)

In \[ \]:

Copied!

from llama\_index.core.query\_engine import NLSQLTableQueryEngine

sql\_query\_engine \= NLSQLTableQueryEngine(
    sql\_database\=sql\_database,
    tables\=\["city\_stats"\],
)

from llama\_index.core.query\_engine import NLSQLTableQueryEngine sql\_query\_engine = NLSQLTableQueryEngine( sql\_database=sql\_database, tables=\["city\_stats"\], )

In \[ \]:

Copied!

from llama\_index.core.tools import QueryEngineTool
from llama\_index.core.tools import ToolMetadata
from llama\_index.core.query\_engine import SubQuestionQueryEngine

query\_engine\_tools \= \[\]
for city in cities:
    query\_engine \= vector\_query\_engines\[city\]

    query\_engine\_tool \= QueryEngineTool(
        query\_engine\=query\_engine,
        metadata\=ToolMetadata(
            name\=city, description\=f"Provides information about {city}"
        ),
    )
    query\_engine\_tools.append(query\_engine\_tool)

s\_engine \= SubQuestionQueryEngine.from\_defaults(
    query\_engine\_tools\=query\_engine\_tools, llm\=OpenAI(model\="gpt-3.5-turbo")
)

from llama\_index.core.retrievers import VectorIndexAutoRetriever
from llama\_index.core.vector\_stores import MetadataInfo, VectorStoreInfo
from llama\_index.core.query\_engine import RetrieverQueryEngine

\# vector\_store\_info = VectorStoreInfo(
\#     content\_info='articles about different cities',
\#     metadata\_info=\[
\#         MetadataInfo(
\#             name='title',
\#             type='str',
\#             description='The name of the city'),
\#     \]
\# )
\# vector\_auto\_retriever = VectorIndexAutoRetriever(vector\_index, vector\_store\_info=vector\_store\_info, llm=OpenAI(model='gpt-4')

\# retriever\_query\_engine = RetrieverQueryEngine.from\_args(
\#     vector\_auto\_retriever, llm=OpenAI(model='gpt-3.5-turbo')
\# )

from llama\_index.core.tools import QueryEngineTool from llama\_index.core.tools import ToolMetadata from llama\_index.core.query\_engine import SubQuestionQueryEngine query\_engine\_tools = \[\] for city in cities: query\_engine = vector\_query\_engines\[city\] query\_engine\_tool = QueryEngineTool( query\_engine=query\_engine, metadata=ToolMetadata( name=city, description=f"Provides information about {city}" ), ) query\_engine\_tools.append(query\_engine\_tool) s\_engine = SubQuestionQueryEngine.from\_defaults( query\_engine\_tools=query\_engine\_tools, llm=OpenAI(model="gpt-3.5-turbo") ) from llama\_index.core.retrievers import VectorIndexAutoRetriever from llama\_index.core.vector\_stores import MetadataInfo, VectorStoreInfo from llama\_index.core.query\_engine import RetrieverQueryEngine # vector\_store\_info = VectorStoreInfo( # content\_info='articles about different cities', # metadata\_info=\[ # MetadataInfo( # name='title', # type='str', # description='The name of the city'), # \] # ) # vector\_auto\_retriever = VectorIndexAutoRetriever(vector\_index, vector\_store\_info=vector\_store\_info, llm=OpenAI(model='gpt-4') # retriever\_query\_engine = RetrieverQueryEngine.from\_args( # vector\_auto\_retriever, llm=OpenAI(model='gpt-3.5-turbo') # )

In \[ \]:

Copied!

sql\_tool \= QueryEngineTool.from\_defaults(
    query\_engine\=sql\_query\_engine,
    description\=(
        "Useful for translating a natural language query into a SQL query over"
        " a table containing: city\_stats, containing the population/country of"
        " each city"
    ),
)
s\_engine\_tool \= QueryEngineTool.from\_defaults(
    query\_engine\=s\_engine,
    description\=(
        f"Useful for answering semantic questions about different cities"
    ),
)

sql\_tool = QueryEngineTool.from\_defaults( query\_engine=sql\_query\_engine, description=( "Useful for translating a natural language query into a SQL query over" " a table containing: city\_stats, containing the population/country of" " each city" ), ) s\_engine\_tool = QueryEngineTool.from\_defaults( query\_engine=s\_engine, description=( f"Useful for answering semantic questions about different cities" ), )

### Define SQLJoinQueryEngine[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLJoinQueryEngine/#define-sqljoinqueryengine)

In \[ \]:

Copied!

from llama\_index.core.query\_engine import SQLJoinQueryEngine

query\_engine \= SQLJoinQueryEngine(
    sql\_tool, s\_engine\_tool, llm\=OpenAI(model\="gpt-4")
)

from llama\_index.core.query\_engine import SQLJoinQueryEngine query\_engine = SQLJoinQueryEngine( sql\_tool, s\_engine\_tool, llm=OpenAI(model="gpt-4") )

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
Generated 3 sub questions.
\[Tokyo\] Q: What are some specific cultural festivals in Tokyo?
\[Tokyo\] Q: What are some specific events in Tokyo?
\[Tokyo\] Q: What are some notable art galleries or museums in Tokyo?
INFO:openai:message='OpenAI API response' path=https://api.openai.com/v1/completions processing\_ms=3069 request\_id=eb3df12fea7d51eb93300180480dc90b response\_code=200
message='OpenAI API response' path=https://api.openai.com/v1/completions processing\_ms=3069 request\_id=eb3df12fea7d51eb93300180480dc90b response\_code=200
\[Tokyo\] A: 
Some specific cultural festivals in Tokyo include the Sannō at Hie Shrine, the Sanja at Asakusa Shrine, the biennial Kanda Festivals, the annual fireworks display over the Sumida River, picnics under the cherry blossoms in Ueno Park, Inokashira Park, and the Shinjuku Gyoen National Garden, and Harajuku's youth style, fashion and cosplay.
INFO:openai:message='OpenAI API response' path=https://api.openai.com/v1/completions processing\_ms=3530 request\_id=ae31aacec5e68590b9cc4a63ee97b66a response\_code=200
message='OpenAI API response' path=https://api.openai.com/v1/completions processing\_ms=3530 request\_id=ae31aacec5e68590b9cc4a63ee97b66a response\_code=200
\[Tokyo\] A: 
Some specific events in Tokyo include the 1964 Summer Olympics, the October 2011 artistic gymnastics world championships, the 2019 Rugby World Cup, the 2020 Summer Olympics and Paralympics (rescheduled to 2021 due to the COVID-19 pandemic in Japan), the Asian Network of Major Cities 21, the Council of Local Authorities for International Relations, the C40 Cities Climate Leadership Group, and various international academic and scientific research collaborations.
INFO:openai:message='OpenAI API response' path=https://api.openai.com/v1/completions processing\_ms=5355 request\_id=81bff9133777221cde8d15d58134ee8f response\_code=200
message='OpenAI API response' path=https://api.openai.com/v1/completions processing\_ms=5355 request\_id=81bff9133777221cde8d15d58134ee8f response\_code=200
\[Tokyo\] A: 
Some notable art galleries and museums in Tokyo include the Tokyo National Museum, the National Museum of Western Art, the Nezu Museum, the National Diet Library, the National Archives, the National Museum of Modern Art, the New National Theater Tokyo, the Edo-Tokyo Museum, the National Museum of Emerging Science and Innovation, and the Studio Ghibli anime center.
query engine response: 
Some specific cultural festivals, events, and notable art galleries or museums in Tokyo include the Sannō at Hie Shrine, the Sanja at Asakusa Shrine, the biennial Kanda Festivals, the annual fireworks display over the Sumida River, picnics under the cherry blossoms in Ueno Park, Inokashira Park, and the Shinjuku Gyoen National Garden, Harajuku's youth style, fashion and cosplay, the 1964 Summer Olympics, the October 2011 artistic gymnastics world championships, the 2019 Rugby World Cup, the 2020 Summer Olympics and Paralympics (rescheduled to 2021 due to the COVID-19 pandemic in Japan), the Asian Network of Major Cities 21, the Council of Local Authorities for International Relations, the C40 Cities Climate Leadership Group, various international academic and scientific research collaborations, the Tokyo National Museum, the National Museum of Western Art, the Nezu Museum, the National Diet Library, the National Archives, the National Museum of Modern Art, the New National Theater Tokyo, the Edo-Tokyo Museum, the National Museum of Emerging Science and Innovation, and the Studio Ghibli anime center.
INFO:llama\_index.query\_engine.sql\_join\_query\_engine:> query engine response: 
Some specific cultural festivals, events, and notable art galleries or museums in Tokyo include the Sannō at Hie Shrine, the Sanja at Asakusa Shrine, the biennial Kanda Festivals, the annual fireworks display over the Sumida River, picnics under the cherry blossoms in Ueno Park, Inokashira Park, and the Shinjuku Gyoen National Garden, Harajuku's youth style, fashion and cosplay, the 1964 Summer Olympics, the October 2011 artistic gymnastics world championships, the 2019 Rugby World Cup, the 2020 Summer Olympics and Paralympics (rescheduled to 2021 due to the COVID-19 pandemic in Japan), the Asian Network of Major Cities 21, the Council of Local Authorities for International Relations, the C40 Cities Climate Leadership Group, various international academic and scientific research collaborations, the Tokyo National Museum, the National Museum of Western Art, the Nezu Museum, the National Diet Library, the National Archives, the National Museum of Modern Art, the New National Theater Tokyo, the Edo-Tokyo Museum, the National Museum of Emerging Science and Innovation, and the Studio Ghibli anime center.
> query engine response: 
Some specific cultural festivals, events, and notable art galleries or museums in Tokyo include the Sannō at Hie Shrine, the Sanja at Asakusa Shrine, the biennial Kanda Festivals, the annual fireworks display over the Sumida River, picnics under the cherry blossoms in Ueno Park, Inokashira Park, and the Shinjuku Gyoen National Garden, Harajuku's youth style, fashion and cosplay, the 1964 Summer Olympics, the October 2011 artistic gymnastics world championships, the 2019 Rugby World Cup, the 2020 Summer Olympics and Paralympics (rescheduled to 2021 due to the COVID-19 pandemic in Japan), the Asian Network of Major Cities 21, the Council of Local Authorities for International Relations, the C40 Cities Climate Leadership Group, various international academic and scientific research collaborations, the Tokyo National Museum, the National Museum of Western Art, the Nezu Museum, the National Diet Library, the National Archives, the National Museum of Modern Art, the New National Theater Tokyo, the Edo-Tokyo Museum, the National Museum of Emerging Science and Innovation, and the Studio Ghibli anime center.
Final response: Tokyo, the city with the highest population of 13.96 million people, is known for its vibrant culture and diverse art forms. It hosts a variety of cultural festivals and events such as the Sannō at Hie Shrine, the Sanja at Asakusa Shrine, the biennial Kanda Festivals, and the annual fireworks display over the Sumida River. Residents and visitors often enjoy picnics under the cherry blossoms in Ueno Park, Inokashira Park, and the Shinjuku Gyoen National Garden. Harajuku's youth style, fashion, and cosplay are also notable cultural aspects of Tokyo. The city has hosted several international events including the 1964 Summer Olympics, the 2019 Rugby World Cup, and the 2020 Summer Olympics and Paralympics (rescheduled to 2021 due to the COVID-19 pandemic). 

In terms of art, Tokyo is home to numerous galleries and museums. These include the Tokyo National Museum, the National Museum of Western Art, the Nezu Museum, the National Diet Library, the National Archives, the National Museum of Modern Art, the New National Theater Tokyo, the Edo-Tokyo Museum, the National Museum of Emerging Science and Innovation, and the Studio Ghibli anime center. These institutions showcase everything from traditional Japanese art such as calligraphy and woodblock prints to modern art and scientific innovations.

In \[ \]:

Copied!

print(str(response))

print(str(response))

Tokyo, the city with the highest population of 13.96 million people, is known for its vibrant culture and diverse art forms. It hosts a variety of cultural festivals and events such as the Sannō at Hie Shrine, the Sanja at Asakusa Shrine, the biennial Kanda Festivals, and the annual fireworks display over the Sumida River. Residents and visitors often enjoy picnics under the cherry blossoms in Ueno Park, Inokashira Park, and the Shinjuku Gyoen National Garden. Harajuku's youth style, fashion, and cosplay are also notable cultural aspects of Tokyo. The city has hosted several international events including the 1964 Summer Olympics, the 2019 Rugby World Cup, and the 2020 Summer Olympics and Paralympics (rescheduled to 2021 due to the COVID-19 pandemic). 

In terms of art, Tokyo is home to numerous galleries and museums. These include the Tokyo National Museum, the National Museum of Western Art, the Nezu Museum, the National Diet Library, the National Archives, the National Museum of Modern Art, the New National Theater Tokyo, the Edo-Tokyo Museum, the National Museum of Emerging Science and Innovation, and the Studio Ghibli anime center. These institutions showcase everything from traditional Japanese art such as calligraphy and woodblock prints to modern art and scientific innovations.

In \[ \]:

Copied!

response \= query\_engine.query(
    "Compare and contrast the demographics of Berlin and Toronto"
)

response = query\_engine.query( "Compare and contrast the demographics of Berlin and Toronto" )

Querying SQL database: Useful for translating a natural language query into a SQL query over a table containing city\_stats, containing the population/country of each city
INFO:llama\_index.query\_engine.sql\_join\_query\_engine:> Querying SQL database: Useful for translating a natural language query into a SQL query over a table containing city\_stats, containing the population/country of each city
> Querying SQL database: Useful for translating a natural language query into a SQL query over a table containing city\_stats, containing the population/country of each city
INFO:llama\_index.indices.struct\_store.sql\_query:> Table desc str: Table 'city\_stats' has columns: city\_name (VARCHAR(16)), population (INTEGER), country (VARCHAR(16)) and foreign keys: .
> Table desc str: Table 'city\_stats' has columns: city\_name (VARCHAR(16)), population (INTEGER), country (VARCHAR(16)) and foreign keys: .
SQL query: SELECT city\_name, population, country FROM city\_stats WHERE city\_name IN ('Berlin', 'Toronto');
SQL response:  Berlin and Toronto are both major cities with large populations. Berlin has a population of 3.6 million people and is located in Germany, while Toronto has a population of 2.9 million people and is located in Canada.
Transformed query given SQL response: What are the age, gender, and ethnic breakdowns of the populations in Berlin and Toronto?
INFO:llama\_index.query\_engine.sql\_join\_query\_engine:> Transformed query given SQL response: What are the age, gender, and ethnic breakdowns of the populations in Berlin and Toronto?
> Transformed query given SQL response: What are the age, gender, and ethnic breakdowns of the populations in Berlin and Toronto?
Generated 6 sub questions.
\[Berlin\] Q: What is the age breakdown of the population in Berlin?
\[Berlin\] Q: What is the gender breakdown of the population in Berlin?
\[Berlin\] Q: What is the ethnic breakdown of the population in Berlin?
\[Toronto\] Q: What is the age breakdown of the population in Toronto?
\[Toronto\] Q: What is the gender breakdown of the population in Toronto?
\[Toronto\] Q: What is the ethnic breakdown of the population in Toronto?
INFO:openai:message='OpenAI API response' path=https://api.openai.com/v1/completions processing\_ms=934 request\_id=b6a654edffcb5a12aa8dac775e0342e2 response\_code=200
message='OpenAI API response' path=https://api.openai.com/v1/completions processing\_ms=934 request\_id=b6a654edffcb5a12aa8dac775e0342e2 response\_code=200
\[Berlin\] A: 
It is not possible to answer this question with the given context information.
INFO:openai:message='OpenAI API response' path=https://api.openai.com/v1/completions processing\_ms=1248 request\_id=c3023af7adbb1018a483467bba6de168 response\_code=200
message='OpenAI API response' path=https://api.openai.com/v1/completions processing\_ms=1248 request\_id=c3023af7adbb1018a483467bba6de168 response\_code=200
\[Toronto\] A: 
The gender population of Toronto is 48 per cent male and 52 per cent female. Women outnumber men in all age groups 15 and older.
INFO:openai:message='OpenAI API response' path=https://api.openai.com/v1/completions processing\_ms=2524 request\_id=3a00900922f785b709db15420d83205b response\_code=200
message='OpenAI API response' path=https://api.openai.com/v1/completions processing\_ms=2524 request\_id=3a00900922f785b709db15420d83205b response\_code=200
\[Berlin\] A: 
It is not possible to answer this question with the given context information.
INFO:openai:message='OpenAI API response' path=https://api.openai.com/v1/completions processing\_ms=4415 request\_id=273aa88ce1189e6f09a7d492dd08490a response\_code=200
message='OpenAI API response' path=https://api.openai.com/v1/completions processing\_ms=4415 request\_id=273aa88ce1189e6f09a7d492dd08490a response\_code=200
\[Toronto\] A: 
The median age of the population in Toronto is 39.3 years. Persons aged 14 years and under make up 14.5 per cent of the population, and those aged 65 years and over make up 15.6 per cent. Women outnumber men in all age groups 15 and older.
INFO:openai:message='OpenAI API response' path=https://api.openai.com/v1/completions processing\_ms=4960 request\_id=4cb35c8f2cd448297321211f8e7ab19e response\_code=200
message='OpenAI API response' path=https://api.openai.com/v1/completions processing\_ms=4960 request\_id=4cb35c8f2cd448297321211f8e7ab19e response\_code=200
\[Berlin\] A: 
The ethnic breakdown of the population in Berlin is primarily German, Turkish, Polish, English, Persian, Arabic, Italian, Bulgarian, Russian, Romanian, Kurdish, Serbo-Croatian, French, Spanish, Vietnamese, Lebanese, Palestinian, Serbian, Indian, Bosnian, American, Ukrainian, Chinese, Austrian, Israeli, Thai, Iranian, Egyptian and Syrian.
INFO:openai:message='OpenAI API response' path=https://api.openai.com/v1/completions processing\_ms=5783 request\_id=5293a02bb62560654072ab8cc3235663 response\_code=200
message='OpenAI API response' path=https://api.openai.com/v1/completions processing\_ms=5783 request\_id=5293a02bb62560654072ab8cc3235663 response\_code=200
\[Toronto\] A: 
The ethnic breakdown of the population in Toronto in 2016 was: European (47.9%), Asian (including Middle-Eastern – 40.1%), African (5.5%), Latin/Central/South American (4.2%), and North American aboriginal (1.2%). The largest visible minority groups were South Asian (Indian, Pakistani, Sri Lankan at 12.6%), East Asian (Chinese at 12.5%), and Black (8.9%).
query engine response: 
Berlin:
Age breakdown: It is not possible to answer this question with the given context information.
Gender breakdown: It is not possible to answer this question with the given context information.
Ethnic breakdown: The ethnic breakdown of the population in Berlin is primarily German, Turkish, Polish, English, Persian, Arabic, Italian, Bulgarian, Russian, Romanian, Kurdish, Serbo-Croatian, French, Spanish, Vietnamese, Lebanese, Palestinian, Serbian, Indian, Bosnian, American, Ukrainian, Chinese, Austrian, Israeli, Thai, Iranian, Egyptian and Syrian.

Toronto:
Age breakdown: The median age of the population in Toronto is 39.3 years. Persons aged 14 years and under make up 14.5 per cent of the population, and those aged 65 years and over make up 15.6 per cent. Women outnumber men in all age groups 15 and older.
Gender breakdown: The gender population of Toronto is 48 per cent male and 52 per cent female. Women outnumber men in all age groups 15 and older.
Ethnic breakdown: The ethnic breakdown of the population in Toronto in 2016 was: European (47.9%), Asian (including Middle-Eastern – 40.1%), African (5.5%), Latin/Central/South American (4.2%), and North American aboriginal (1.2%). The largest visible minority groups were South Asian (Indian, Pakistani, Sri Lankan at 12.6%), East Asian (Chinese at 12.5%), and Black (8.9%).
INFO:llama\_index.query\_engine.sql\_join\_query\_engine:> query engine response: 
Berlin:
Age breakdown: It is not possible to answer this question with the given context information.
Gender breakdown: It is not possible to answer this question with the given context information.
Ethnic breakdown: The ethnic breakdown of the population in Berlin is primarily German, Turkish, Polish, English, Persian, Arabic, Italian, Bulgarian, Russian, Romanian, Kurdish, Serbo-Croatian, French, Spanish, Vietnamese, Lebanese, Palestinian, Serbian, Indian, Bosnian, American, Ukrainian, Chinese, Austrian, Israeli, Thai, Iranian, Egyptian and Syrian.

Toronto:
Age breakdown: The median age of the population in Toronto is 39.3 years. Persons aged 14 years and under make up 14.5 per cent of the population, and those aged 65 years and over make up 15.6 per cent. Women outnumber men in all age groups 15 and older.
Gender breakdown: The gender population of Toronto is 48 per cent male and 52 per cent female. Women outnumber men in all age groups 15 and older.
Ethnic breakdown: The ethnic breakdown of the population in Toronto in 2016 was: European (47.9%), Asian (including Middle-Eastern – 40.1%), African (5.5%), Latin/Central/South American (4.2%), and North American aboriginal (1.2%). The largest visible minority groups were South Asian (Indian, Pakistani, Sri Lankan at 12.6%), East Asian (Chinese at 12.5%), and Black (8.9%).
> query engine response: 
Berlin:
Age breakdown: It is not possible to answer this question with the given context information.
Gender breakdown: It is not possible to answer this question with the given context information.
Ethnic breakdown: The ethnic breakdown of the population in Berlin is primarily German, Turkish, Polish, English, Persian, Arabic, Italian, Bulgarian, Russian, Romanian, Kurdish, Serbo-Croatian, French, Spanish, Vietnamese, Lebanese, Palestinian, Serbian, Indian, Bosnian, American, Ukrainian, Chinese, Austrian, Israeli, Thai, Iranian, Egyptian and Syrian.

Toronto:
Age breakdown: The median age of the population in Toronto is 39.3 years. Persons aged 14 years and under make up 14.5 per cent of the population, and those aged 65 years and over make up 15.6 per cent. Women outnumber men in all age groups 15 and older.
Gender breakdown: The gender population of Toronto is 48 per cent male and 52 per cent female. Women outnumber men in all age groups 15 and older.
Ethnic breakdown: The ethnic breakdown of the population in Toronto in 2016 was: European (47.9%), Asian (including Middle-Eastern – 40.1%), African (5.5%), Latin/Central/South American (4.2%), and North American aboriginal (1.2%). The largest visible minority groups were South Asian (Indian, Pakistani, Sri Lankan at 12.6%), East Asian (Chinese at 12.5%), and Black (8.9%).
Final response: Berlin and Toronto are both major cities with large populations. Berlin, located in Germany, has a population of 3.6 million people. The ethnic breakdown of the population in Berlin is primarily German, Turkish, Polish, English, Persian, Arabic, Italian, Bulgarian, Russian, Romanian, Kurdish, Serbo-Croatian, French, Spanish, Vietnamese, Lebanese, Palestinian, Serbian, Indian, Bosnian, American, Ukrainian, Chinese, Austrian, Israeli, Thai, Iranian, Egyptian and Syrian. Unfortunately, the age and gender breakdowns for Berlin are not available.

On the other hand, Toronto, located in Canada, has a population of 2.9 million people. The median age of the population in Toronto is 39.3 years. Persons aged 14 years and under make up 14.5 per cent of the population, and those aged 65 years and over make up 15.6 per cent. The gender population of Toronto is 48 per cent male and 52 per cent female, with women outnumbering men in all age groups 15 and older. The ethnic breakdown of the population in Toronto in 2016 was: European (47.9%), Asian (including Middle-Eastern – 40.1%), African (5.5%), Latin/Central/South American (4.2%), and North American aboriginal (1.2%). The largest visible minority groups were South Asian (Indian, Pakistani, Sri Lankan at 12.6%), East Asian (Chinese at 12.5%), and Black (8.9%).

In \[ \]:

Copied!

print(str(response))

print(str(response))

Berlin and Toronto are both major cities with large populations. Berlin, located in Germany, has a population of 3.6 million people. The ethnic breakdown of the population in Berlin is primarily German, Turkish, Polish, English, Persian, Arabic, Italian, Bulgarian, Russian, Romanian, Kurdish, Serbo-Croatian, French, Spanish, Vietnamese, Lebanese, Palestinian, Serbian, Indian, Bosnian, American, Ukrainian, Chinese, Austrian, Israeli, Thai, Iranian, Egyptian and Syrian. Unfortunately, the age and gender breakdowns for Berlin are not available.

On the other hand, Toronto, located in Canada, has a population of 2.9 million people. The median age of the population in Toronto is 39.3 years. Persons aged 14 years and under make up 14.5 per cent of the population, and those aged 65 years and over make up 15.6 per cent. The gender population of Toronto is 48 per cent male and 52 per cent female, with women outnumbering men in all age groups 15 and older. The ethnic breakdown of the population in Toronto in 2016 was: European (47.9%), Asian (including Middle-Eastern – 40.1%), African (5.5%), Latin/Central/South American (4.2%), and North American aboriginal (1.2%). The largest visible minority groups were South Asian (Indian, Pakistani, Sri Lankan at 12.6%), East Asian (Chinese at 12.5%), and Black (8.9%).

Back to top

[Previous SQL Auto Vector Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLAutoVectorQueryEngine/)[Next SQL Router Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/SQLRouterQueryEngine/)

Hi, how can I help you?

🦙
