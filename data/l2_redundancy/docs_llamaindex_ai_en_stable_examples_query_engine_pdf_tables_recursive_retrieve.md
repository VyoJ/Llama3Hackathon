Title: Recursive Retriever + Query Engine Demo

URL Source: https://docs.llamaindex.ai/en/stable/examples/query_engine/pdf_tables/recursive_retriever/

Markdown Content:
Recursive Retriever + Query Engine Demo - LlamaIndex


In this demo, we walk through a use case of showcasing our "RecursiveRetriever" module over hierarchical data.

The concept of recursive retrieval is that we not only explore the directly most relevant nodes, but also explore node relationships to additional retrievers/query engines and execute them. For instance, a node may represent a concise summary of a structured table, and link to a SQL/Pandas query engine over that structured table. Then if the node is retrieved, we want to also query the underlying query engine for the answer.

This can be especially useful for documents with hierarchical relationships. In this example, we walk through a Wikipedia article about billionaires (in PDF form), which contains both text and a variety of embedded structured tables. We first create a Pandas query engine over each table, but also represent each table by an `IndexNode` (stores a link to the query engine); this Node is stored along with other Nodes in a vector store.

During query-time, if an `IndexNode` is fetched, then the underlying query engine/retriever will be queried.

**Notes about Setup**

We use `camelot` to extract text-based tables from PDFs.

In \[ \]:

Copied!

%pip install llama\-index\-embeddings\-openai
%pip install llama\-index\-readers\-file pymupdf
%pip install llama\-index\-llms\-openai
%pip install llama\-index\-experimental

%pip install llama-index-embeddings-openai %pip install llama-index-readers-file pymupdf %pip install llama-index-llms-openai %pip install llama-index-experimental

In \[ \]:

Copied!

import camelot

\# https://en.wikipedia.org/wiki/The\_World%27s\_Billionaires
from llama\_index.core import VectorStoreIndex
from llama\_index.experimental.query\_engine import PandasQueryEngine
from llama\_index.core.schema import IndexNode
from llama\_index.llms.openai import OpenAI

from llama\_index.readers.file import PyMuPDFReader
from typing import List

import camelot # https://en.wikipedia.org/wiki/The\_World%27s\_Billionaires from llama\_index.core import VectorStoreIndex from llama\_index.experimental.query\_engine import PandasQueryEngine from llama\_index.core.schema import IndexNode from llama\_index.llms.openai import OpenAI from llama\_index.readers.file import PyMuPDFReader from typing import List

Default Settings[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/pdf_tables/recursive_retriever/#default-settings)
--------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "YOUR\_API\_KEY"

import os os.environ\["OPENAI\_API\_KEY"\] = "YOUR\_API\_KEY"

In \[ \]:

Copied!

from llama\_index.embeddings.openai import OpenAIEmbedding
from llama\_index.llms.openai import OpenAI
from llama\_index.core import Settings

Settings.llm \= OpenAI(model\="gpt-3.5-turbo")
Settings.embed\_model \= OpenAIEmbedding(model\="text-embedding-3-small")

from llama\_index.embeddings.openai import OpenAIEmbedding from llama\_index.llms.openai import OpenAI from llama\_index.core import Settings Settings.llm = OpenAI(model="gpt-3.5-turbo") Settings.embed\_model = OpenAIEmbedding(model="text-embedding-3-small")

Load in Document (and Tables)[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/pdf_tables/recursive_retriever/#load-in-document-and-tables)
--------------------------------------------------------------------------------------------------------------------------------------------------------

We use our `PyMuPDFReader` to read in the main text of the document.

We also use `camelot` to extract some structured tables from the document

In \[ \]:

Copied!

file\_path \= "billionaires\_page.pdf"

file\_path = "billionaires\_page.pdf"

In \[ \]:

Copied!

\# initialize PDF reader
reader \= PyMuPDFReader()

\# initialize PDF reader reader = PyMuPDFReader()

In \[ \]:

Copied!

docs \= reader.load(file\_path)

docs = reader.load(file\_path)

In \[ \]:

Copied!

\# use camelot to parse tables
def get\_tables(path: str, pages: List\[int\]):
    table\_dfs \= \[\]
    for page in pages:
        table\_list \= camelot.read\_pdf(path, pages\=str(page))
        table\_df \= table\_list\[0\].df
        table\_df \= (
            table\_df.rename(columns\=table\_df.iloc\[0\])
            .drop(table\_df.index\[0\])
            .reset\_index(drop\=True)
        )
        table\_dfs.append(table\_df)
    return table\_dfs

\# use camelot to parse tables def get\_tables(path: str, pages: List\[int\]): table\_dfs = \[\] for page in pages: table\_list = camelot.read\_pdf(path, pages=str(page)) table\_df = table\_list\[0\].df table\_df = ( table\_df.rename(columns=table\_df.iloc\[0\]) .drop(table\_df.index\[0\]) .reset\_index(drop=True) ) table\_dfs.append(table\_df) return table\_dfs

In \[ \]:

Copied!

table\_dfs \= get\_tables(file\_path, pages\=\[3, 25\])

table\_dfs = get\_tables(file\_path, pages=\[3, 25\])

In \[ \]:

Copied!

\# shows list of top billionaires in 2023
table\_dfs\[0\]

\# shows list of top billionaires in 2023 table\_dfs\[0\]

Out\[ \]:

|  | No. | Name | Net worth\\n(USD) | Age | Nationality | Primary source(s) of wealth |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | Bernard Arnault &\\nfamily | $211 billion | 74 | France | LVMH |
| 1 | 2 | Elon Musk | $180 billion | 51 | United\\nStates | Tesla, SpaceX, X Corp. |
| 2 | 3 | Jeff Bezos | $114 billion | 59 | United\\nStates | Amazon |
| 3 | 4 | Larry Ellison | $107 billion | 78 | United\\nStates | Oracle Corporation |
| 4 | 5 | Warren Buffett | $106 billion | 92 | United\\nStates | Berkshire Hathaway |
| 5 | 6 | Bill Gates | $104 billion | 67 | United\\nStates | Microsoft |
| 6 | 7 | Michael Bloomberg | $94.5 billion | 81 | United\\nStates | Bloomberg L.P. |
| 7 | 8 | Carlos Slim & family | $93 billion | 83 | Mexico | Telmex, América Móvil, Grupo\\nCarso |
| 8 | 9 | Mukesh Ambani | $83.4 billion | 65 | India | Reliance Industries |
| 9 | 10 | Steve Ballmer | $80.7 billion | 67 | United\\nStates | Microsoft |

In \[ \]:

Copied!

\# shows list of top billionaires
table\_dfs\[1\]

\# shows list of top billionaires table\_dfs\[1\]

Out\[ \]:

|  | Year | Number of billionaires | Group's combined net worth |
| --- | --- | --- | --- |
| 0 | 2023\[2\] | 2,640 | $12.2 trillion |
| 1 | 2022\[6\] | 2,668 | $12.7 trillion |
| 2 | 2021\[11\] | 2,755 | $13.1 trillion |
| 3 | 2020 | 2,095 | $8.0 trillion |
| 4 | 2019 | 2,153 | $8.7 trillion |
| 5 | 2018 | 2,208 | $9.1 trillion |
| 6 | 2017 | 2,043 | $7.7 trillion |
| 7 | 2016 | 1,810 | $6.5 trillion |
| 8 | 2015\[18\] | 1,826 | $7.1 trillion |
| 9 | 2014\[67\] | 1,645 | $6.4 trillion |
| 10 | 2013\[68\] | 1,426 | $5.4 trillion |
| 11 | 2012 | 1,226 | $4.6 trillion |
| 12 | 2011 | 1,210 | $4.5 trillion |
| 13 | 2010 | 1,011 | $3.6 trillion |
| 14 | 2009 | 793 | $2.4 trillion |
| 15 | 2008 | 1,125 | $4.4 trillion |
| 16 | 2007 | 946 | $3.5 trillion |
| 17 | 2006 | 793 | $2.6 trillion |
| 18 | 2005 | 691 | $2.2 trillion |
| 19 | 2004 | 587 | $1.9 trillion |
| 20 | 2003 | 476 | $1.4 trillion |
| 21 | 2002 | 497 | $1.5 trillion |
| 22 | 2001 | 538 | $1.8 trillion |
| 23 | 2000 | 470 | $898 billion |
| 24 | Sources: Forbes.\[18\]\[67\]\[66\]\[68\] |  |  |

Create Pandas Query Engines[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/pdf_tables/recursive_retriever/#create-pandas-query-engines)
------------------------------------------------------------------------------------------------------------------------------------------------------

We create a pandas query engine over each structured table.

These can be executed on their own to answer queries about each table.

**WARNING:** This tool provides the LLM access to the `eval` function. Arbitrary code execution is possible on the machine running this tool. While some level of filtering is done on code, this tool is not recommended to be used in a production setting without heavy sandboxing or virtual machines.

In \[ \]:

Copied!

\# define query engines over these tables
llm \= OpenAI(model\="gpt-4")

df\_query\_engines \= \[
    PandasQueryEngine(table\_df, llm\=llm) for table\_df in table\_dfs
\]

\# define query engines over these tables llm = OpenAI(model="gpt-4") df\_query\_engines = \[ PandasQueryEngine(table\_df, llm=llm) for table\_df in table\_dfs \]

In \[ \]:

Copied!

response \= df\_query\_engines\[0\].query(
    "What's the net worth of the second richest billionaire in 2023?"
)
print(str(response))

response = df\_query\_engines\[0\].query( "What's the net worth of the second richest billionaire in 2023?" ) print(str(response))

$180 billion

In \[ \]:

Copied!

response \= df\_query\_engines\[1\].query(
    "How many billionaires were there in 2009?"
)
print(str(response))

response = df\_query\_engines\[1\].query( "How many billionaires were there in 2009?" ) print(str(response))

793

Build Vector Index[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/pdf_tables/recursive_retriever/#build-vector-index)
------------------------------------------------------------------------------------------------------------------------------------

Build vector index over the chunked document as well as over the additional `IndexNode` objects linked to the tables.

In \[ \]:

Copied!

from llama\_index.core import Settings

doc\_nodes \= Settings.node\_parser.get\_nodes\_from\_documents(docs)

from llama\_index.core import Settings doc\_nodes = Settings.node\_parser.get\_nodes\_from\_documents(docs)

In \[ \]:

Copied!

\# define index nodes
summaries \= \[
    (
        "This node provides information about the world's richest billionaires"
        " in 2023"
    ),
    (
        "This node provides information on the number of billionaires and"
        " their combined net worth from 2000 to 2023."
    ),
\]

df\_nodes \= \[
    IndexNode(text\=summary, index\_id\=f"pandas{idx}")
    for idx, summary in enumerate(summaries)
\]

df\_id\_query\_engine\_mapping \= {
    f"pandas{idx}": df\_query\_engine
    for idx, df\_query\_engine in enumerate(df\_query\_engines)
}

\# define index nodes summaries = \[ ( "This node provides information about the world's richest billionaires" " in 2023" ), ( "This node provides information on the number of billionaires and" " their combined net worth from 2000 to 2023." ), \] df\_nodes = \[ IndexNode(text=summary, index\_id=f"pandas{idx}") for idx, summary in enumerate(summaries) \] df\_id\_query\_engine\_mapping = { f"pandas{idx}": df\_query\_engine for idx, df\_query\_engine in enumerate(df\_query\_engines) }

In \[ \]:

Copied!

\# construct top-level vector index + query engine
vector\_index \= VectorStoreIndex(doc\_nodes + df\_nodes)
vector\_retriever \= vector\_index.as\_retriever(similarity\_top\_k\=1)

\# construct top-level vector index + query engine vector\_index = VectorStoreIndex(doc\_nodes + df\_nodes) vector\_retriever = vector\_index.as\_retriever(similarity\_top\_k=1)

Use `RecursiveRetriever` in our `RetrieverQueryEngine`[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/pdf_tables/recursive_retriever/#use-recursiveretriever-in-our-retrieverqueryengine)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We define a `RecursiveRetriever` object to recursively retrieve/query nodes. We then put this in our `RetrieverQueryEngine` along with a `ResponseSynthesizer` to synthesize a response.

We pass in mappings from id to retriever and id to query engine. We then pass in a root id representing the retriever we query first.

In \[ \]:

Copied!

\# baseline vector index (that doesn't include the extra df nodes).
\# used to benchmark
vector\_index0 \= VectorStoreIndex(doc\_nodes)
vector\_query\_engine0 \= vector\_index0.as\_query\_engine()

\# baseline vector index (that doesn't include the extra df nodes). # used to benchmark vector\_index0 = VectorStoreIndex(doc\_nodes) vector\_query\_engine0 = vector\_index0.as\_query\_engine()

In \[ \]:

Copied!

from llama\_index.core.retrievers import RecursiveRetriever
from llama\_index.core.query\_engine import RetrieverQueryEngine
from llama\_index.core import get\_response\_synthesizer

recursive\_retriever \= RecursiveRetriever(
    "vector",
    retriever\_dict\={"vector": vector\_retriever},
    query\_engine\_dict\=df\_id\_query\_engine\_mapping,
    verbose\=True,
)

response\_synthesizer \= get\_response\_synthesizer(response\_mode\="compact")

query\_engine \= RetrieverQueryEngine.from\_args(
    recursive\_retriever, response\_synthesizer\=response\_synthesizer
)

from llama\_index.core.retrievers import RecursiveRetriever from llama\_index.core.query\_engine import RetrieverQueryEngine from llama\_index.core import get\_response\_synthesizer recursive\_retriever = RecursiveRetriever( "vector", retriever\_dict={"vector": vector\_retriever}, query\_engine\_dict=df\_id\_query\_engine\_mapping, verbose=True, ) response\_synthesizer = get\_response\_synthesizer(response\_mode="compact") query\_engine = RetrieverQueryEngine.from\_args( recursive\_retriever, response\_synthesizer=response\_synthesizer )

In \[ \]:

Copied!

response \= query\_engine.query(
    "What's the net worth of the second richest billionaire in 2023?"
)

response = query\_engine.query( "What's the net worth of the second richest billionaire in 2023?" )

Retrieving with query id None: What's the net worth of the second richest billionaire in 2023?
Retrieved node with id, entering: pandas0
Retrieving with query id pandas0: What's the net worth of the second richest billionaire in 2023?
Got response: $180 billion

In \[ \]:

Copied!

response.source\_nodes\[0\].node.get\_content()

response.source\_nodes\[0\].node.get\_content()

Out\[ \]:

"Query: What's the net worth of the second richest billionaire in 2023?\\nResponse: $180\\xa0billion"

In \[ \]:

Copied!

str(response)

str(response)

Out\[ \]:

'$180 billion.'

In \[ \]:

Copied!

response \= query\_engine.query("How many billionaires were there in 2009?")

response = query\_engine.query("How many billionaires were there in 2009?")

Retrieving with query id None: How many billionaires were there in 2009?
Retrieved node with id, entering: pandas1
Retrieving with query id pandas1: How many billionaires were there in 2009?
Got response: 793

In \[ \]:

Copied!

str(response)

str(response)

Out\[ \]:

'793'

In \[ \]:

Copied!

response \= vector\_query\_engine0.query(
    "How many billionaires were there in 2009?"
)

response = vector\_query\_engine0.query( "How many billionaires were there in 2009?" )

In \[ \]:

Copied!

print(response.source\_nodes\[0\].node.get\_content())

print(response.source\_nodes\[0\].node.get\_content())

In \[ \]:

Copied!

print(str(response))

print(str(response))

Based on the context information, it is not possible to determine the exact number of billionaires in 2009. The provided information only mentions the number of billionaires in 2013 and 2014.

In \[ \]:

Copied!

response.source\_nodes\[0\].node.get\_content()

response.source\_nodes\[0\].node.get\_content()

In \[ \]:

Copied!

response \= query\_engine.query(
    "Which billionaires are excluded from this list?"
)

response = query\_engine.query( "Which billionaires are excluded from this list?" )

In \[ \]:

Copied!

print(str(response))

print(str(response))

Royal families and dictators whose wealth is contingent on a position are excluded from this list.

Back to top

[Previous Pandas Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/pandas_query_engine/)[Next \[Beta\] Text-to-SQL with PGVector](https://docs.llamaindex.ai/en/stable/examples/query_engine/pgvector_sql_query_engine/)
