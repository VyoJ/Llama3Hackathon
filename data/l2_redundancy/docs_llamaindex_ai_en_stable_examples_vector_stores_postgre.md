Title: Postgres Vector Store - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/postgres/

Markdown Content:
Postgres Vector Store - LlamaIndex


In this notebook we are going to show how to use [Postgresql](https://www.postgresql.org/) and [pgvector](https://github.com/pgvector/pgvector) to perform vector searches in LlamaIndex

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-postgres

%pip install llama-index-vector-stores-postgres

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

Running the following cell will install Postgres with PGVector in Colab.

In \[ \]:

Copied!

!sudo apt update
!echo | sudo apt install \-y postgresql\-common
!echo | sudo /usr/share/postgresql\-common/pgdg/apt.postgresql.org.sh
!echo | sudo apt install postgresql\-15\-pgvector
!sudo service postgresql start
!sudo \-u postgres psql \-c "ALTER USER postgres PASSWORD 'password';"
!sudo \-u postgres psql \-c "CREATE DATABASE vector\_db;"

!sudo apt update !echo | sudo apt install -y postgresql-common !echo | sudo /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh !echo | sudo apt install postgresql-15-pgvector !sudo service postgresql start !sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'password';" !sudo -u postgres psql -c "CREATE DATABASE vector\_db;"

In \[ \]:

Copied!

\# import logging
\# import sys

\# Uncomment to see debug logs
\# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
\# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from llama\_index.core import SimpleDirectoryReader, StorageContext
from llama\_index.core import VectorStoreIndex
from llama\_index.vector\_stores.postgres import PGVectorStore
import textwrap
import openai

\# import logging # import sys # Uncomment to see debug logs # logging.basicConfig(stream=sys.stdout, level=logging.DEBUG) # logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout)) from llama\_index.core import SimpleDirectoryReader, StorageContext from llama\_index.core import VectorStoreIndex from llama\_index.vector\_stores.postgres import PGVectorStore import textwrap import openai

### Setup OpenAI[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/postgres/#setup-openai)

The first step is to configure the openai key. It will be used to created embeddings for the documents loaded into the index

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "<your key>"
openai.api\_key \= os.environ\["OPENAI\_API\_KEY"\]

import os os.environ\["OPENAI\_API\_KEY"\] = "" openai.api\_key = os.environ\["OPENAI\_API\_KEY"\]

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

\--2024-03-14 02:56:30--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.109.133, 185.199.111.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 75042 (73K) \[text/plain\]
Saving to: ‘data/paul\_graham/paul\_graham\_essay.txt’

data/paul\_graham/pa 100%\[>\]   1.67M  --.-KB/s    in 0.02s   

2024-03-14 02:56:46 (106 MB/s) - ‘data/git\_commits/commit\_history.csv’ saved \[1753902/1753902\]

In \[ \]:

Copied!

import csv

with open("data/git\_commits/commit\_history.csv", "r") as f:
    commits \= list(csv.DictReader(f))

print(commits\[0\])
print(len(commits))

import csv with open("data/git\_commits/commit\_history.csv", "r") as f: commits = list(csv.DictReader(f)) print(commits\[0\]) print(len(commits))

{'commit': '44e41c12ab25e36c202f58e068ced262eadc8d16', 'author': 'Lakshmi Narayanan Sreethar<lakshmi@timescale.com>', 'date': 'Tue Sep 5 21:03:21 2023 +0530', 'change summary': 'Fix segfault in set\_integer\_now\_func', 'change details': 'When an invalid function oid is passed to set\_integer\_now\_func, it finds out that the function oid is invalid but before throwing the error, it calls ReleaseSysCache on an invalid tuple causing a segfault. Fixed that by removing the invalid call to ReleaseSysCache.  Fixes #6037 '}
4167

#### Add nodes with custom metadata[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/postgres/#add-nodes-with-custom-metadata)

In \[ \]:

Copied!

\# Create TextNode for each of the first 100 commits
from llama\_index.core.schema import TextNode
from datetime import datetime
import re

nodes \= \[\]
dates \= set()
authors \= set()
for commit in commits\[:100\]:
    author\_email \= commit\["author"\].split("<")\[1\]\[:\-1\]
    commit\_date \= datetime.strptime(
        commit\["date"\], "%a %b %d %H:%M:%S %Y %z"
    ).strftime("%Y-%m-%d")
    commit\_text \= commit\["change summary"\]
    if commit\["change details"\]:
        commit\_text += "\\n\\n" + commit\["change details"\]
    fixes \= re.findall(r"#(\\d+)", commit\_text, re.IGNORECASE)
    nodes.append(
        TextNode(
            text\=commit\_text,
            metadata\={
                "commit\_date": commit\_date,
                "author": author\_email,
                "fixes": fixes,
            },
        )
    )
    dates.add(commit\_date)
    authors.add(author\_email)

print(nodes\[0\])
print(min(dates), "to", max(dates))
print(authors)

\# Create TextNode for each of the first 100 commits from llama\_index.core.schema import TextNode from datetime import datetime import re nodes = \[\] dates = set() authors = set() for commit in commits\[:100\]: author\_email = commit\["author"\].split("<")\[1\]\[:-1\] commit\_date = datetime.strptime( commit\["date"\], "%a %b %d %H:%M:%S %Y %z" ).strftime("%Y-%m-%d") commit\_text = commit\["change summary"\] if commit\["change details"\]: commit\_text += "\\n\\n" + commit\["change details"\] fixes = re.findall(r"#(\\d+)", commit\_text, re.IGNORECASE) nodes.append( TextNode( text=commit\_text, metadata={ "commit\_date": commit\_date, "author": author\_email, "fixes": fixes, }, ) ) dates.add(commit\_date) authors.add(author\_email) print(nodes\[0\]) print(min(dates), "to", max(dates)) print(authors)

Node ID: 69513543-dee5-4c65-b4b8-39295f11e669
Text: Fix segfault in set\_integer\_now\_func  When an invalid function
oid is passed to set\_integer\_now\_func, it finds out that the function
oid is invalid but before throwing the error, it calls ReleaseSysCache
on an invalid tuple causing a segfault. Fixed that by removing the
invalid call to ReleaseSysCache.  Fixes #6037
2023-03-22 to 2023-09-05
{'rafia.sabih@gmail.com', 'erik@timescale.com', 'jguthrie@timescale.com', 'sven@timescale.com', '36882414+akuzm@users.noreply.github.com', 'me@noctarius.com', 'satish.8483@gmail.com', 'nikhil@timescale.com', 'konstantina@timescale.com', 'dmitry@timescale.com', 'mats@timescale.com', 'jan@timescale.com', 'lakshmi@timescale.com', 'fabriziomello@gmail.com', 'engel@sero-systems.de'}

In \[ \]:

Copied!

vector\_store \= PGVectorStore.from\_params(
    database\=db\_name,
    host\=url.host,
    password\=url.password,
    port\=url.port,
    user\=url.username,
    table\_name\="metadata\_filter\_demo3",
    embed\_dim\=1536,  \# openai embedding dimension
)

index \= VectorStoreIndex.from\_vector\_store(vector\_store\=vector\_store)
index.insert\_nodes(nodes)

vector\_store = PGVectorStore.from\_params( database=db\_name, host=url.host, password=url.password, port=url.port, user=url.username, table\_name="metadata\_filter\_demo3", embed\_dim=1536, # openai embedding dimension ) index = VectorStoreIndex.from\_vector\_store(vector\_store=vector\_store) index.insert\_nodes(nodes)

In \[ \]:

Copied!

print(index.as\_query\_engine().query("How did Lakshmi fix the segfault?"))

print(index.as\_query\_engine().query("How did Lakshmi fix the segfault?"))

Lakshmi fixed the segfault by removing the invalid call to ReleaseSysCache that was causing the issue.

#### Apply metadata filters[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/postgres/#apply-metadata-filters)

Now we can filter by commit author or by date when retrieving nodes.

In \[ \]:

Copied!

from llama\_index.core.vector\_stores.types import (
    MetadataFilter,
    MetadataFilters,
)

filters \= MetadataFilters(
    filters\=\[
        MetadataFilter(key\="author", value\="mats@timescale.com"),
        MetadataFilter(key\="author", value\="sven@timescale.com"),
    \],
    condition\="or",
)

retriever \= index.as\_retriever(
    similarity\_top\_k\=10,
    filters\=filters,
)

retrieved\_nodes \= retriever.retrieve("What is this software project about?")

for node in retrieved\_nodes:
    print(node.node.metadata)

from llama\_index.core.vector\_stores.types import ( MetadataFilter, MetadataFilters, ) filters = MetadataFilters( filters=\[ MetadataFilter(key="author", value="mats@timescale.com"), MetadataFilter(key="author", value="sven@timescale.com"), \], condition="or", ) retriever = index.as\_retriever( similarity\_top\_k=10, filters=filters, ) retrieved\_nodes = retriever.retrieve("What is this software project about?") for node in retrieved\_nodes: print(node.node.metadata)

{'commit\_date': '2023-08-07', 'author': 'mats@timescale.com', 'fixes': \[\]}
{'commit\_date': '2023-08-27', 'author': 'sven@timescale.com', 'fixes': \[\]}
{'commit\_date': '2023-07-13', 'author': 'mats@timescale.com', 'fixes': \[\]}
{'commit\_date': '2023-08-07', 'author': 'sven@timescale.com', 'fixes': \[\]}
{'commit\_date': '2023-08-30', 'author': 'sven@timescale.com', 'fixes': \[\]}
{'commit\_date': '2023-08-15', 'author': 'sven@timescale.com', 'fixes': \[\]}
{'commit\_date': '2023-08-23', 'author': 'sven@timescale.com', 'fixes': \[\]}
{'commit\_date': '2023-08-10', 'author': 'mats@timescale.com', 'fixes': \[\]}
{'commit\_date': '2023-07-25', 'author': 'mats@timescale.com', 'fixes': \['5892'\]}
{'commit\_date': '2023-08-21', 'author': 'sven@timescale.com', 'fixes': \[\]}

In \[ \]:

Copied!

filters \= MetadataFilters(
    filters\=\[
        MetadataFilter(key\="commit\_date", value\="2023-08-15", operator\=">="),
        MetadataFilter(key\="commit\_date", value\="2023-08-25", operator\="<="),
    \],
    condition\="and",
)

retriever \= index.as\_retriever(
    similarity\_top\_k\=10,
    filters\=filters,
)

retrieved\_nodes \= retriever.retrieve("What is this software project about?")

for node in retrieved\_nodes:
    print(node.node.metadata)

filters = MetadataFilters( filters=\[ MetadataFilter(key="commit\_date", value="2023-08-15", operator=">="), MetadataFilter(key="commit\_date", value="2023-08-25", operator="<="), \], condition="and", ) retriever = index.as\_retriever( similarity\_top\_k=10, filters=filters, ) retrieved\_nodes = retriever.retrieve("What is this software project about?") for node in retrieved\_nodes: print(node.node.metadata)

{'commit\_date': '2023-08-23', 'author': 'erik@timescale.com', 'fixes': \[\]}
{'commit\_date': '2023-08-17', 'author': 'konstantina@timescale.com', 'fixes': \[\]}
{'commit\_date': '2023-08-15', 'author': '36882414+akuzm@users.noreply.github.com', 'fixes': \[\]}
{'commit\_date': '2023-08-15', 'author': '36882414+akuzm@users.noreply.github.com', 'fixes': \[\]}
{'commit\_date': '2023-08-24', 'author': 'lakshmi@timescale.com', 'fixes': \[\]}
{'commit\_date': '2023-08-15', 'author': 'sven@timescale.com', 'fixes': \[\]}
{'commit\_date': '2023-08-23', 'author': 'sven@timescale.com', 'fixes': \[\]}
{'commit\_date': '2023-08-21', 'author': 'sven@timescale.com', 'fixes': \[\]}
{'commit\_date': '2023-08-20', 'author': 'sven@timescale.com', 'fixes': \[\]}
{'commit\_date': '2023-08-21', 'author': 'sven@timescale.com', 'fixes': \[\]}

#### Apply nested filters[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/postgres/#apply-nested-filters)

In the above examples, we combined multiple filters using AND or OR. We can also combine multiple sets of filters.

e.g. in SQL:

WHERE (commit\_date \>= '2023-08-01' AND commit\_date <= '2023-08-15') AND (author \= 'mats@timescale.com' OR author \= 'sven@timescale.com')

In \[ \]:

Copied!

filters \= MetadataFilters(
    filters\=\[
        MetadataFilters(
            filters\=\[
                MetadataFilter(
                    key\="commit\_date", value\="2023-08-01", operator\=">="
                ),
                MetadataFilter(
                    key\="commit\_date", value\="2023-08-15", operator\="<="
                ),
            \],
            condition\="and",
        ),
        MetadataFilters(
            filters\=\[
                MetadataFilter(key\="author", value\="mats@timescale.com"),
                MetadataFilter(key\="author", value\="sven@timescale.com"),
            \],
            condition\="or",
        ),
    \],
    condition\="and",
)

retriever \= index.as\_retriever(
    similarity\_top\_k\=10,
    filters\=filters,
)

retrieved\_nodes \= retriever.retrieve("What is this software project about?")

for node in retrieved\_nodes:
    print(node.node.metadata)

filters = MetadataFilters( filters=\[ MetadataFilters( filters=\[ MetadataFilter( key="commit\_date", value="2023-08-01", operator=">=" ), MetadataFilter( key="commit\_date", value="2023-08-15", operator="<=" ), \], condition="and", ), MetadataFilters( filters=\[ MetadataFilter(key="author", value="mats@timescale.com"), MetadataFilter(key="author", value="sven@timescale.com"), \], condition="or", ), \], condition="and", ) retriever = index.as\_retriever( similarity\_top\_k=10, filters=filters, ) retrieved\_nodes = retriever.retrieve("What is this software project about?") for node in retrieved\_nodes: print(node.node.metadata)

{'commit\_date': '2023-08-07', 'author': 'mats@timescale.com', 'fixes': \[\]}
{'commit\_date': '2023-08-07', 'author': 'sven@timescale.com', 'fixes': \[\]}
{'commit\_date': '2023-08-15', 'author': 'sven@timescale.com', 'fixes': \[\]}
{'commit\_date': '2023-08-10', 'author': 'mats@timescale.com', 'fixes': \[\]}

The above can be simplified by using the IN operator. `PGVectorStore` supports `in`, `nin`, and `contains` for comparing an element with a list.

In \[ \]:

Copied!

filters \= MetadataFilters(
    filters\=\[
        MetadataFilter(key\="commit\_date", value\="2023-08-01", operator\=">="),
        MetadataFilter(key\="commit\_date", value\="2023-08-15", operator\="<="),
        MetadataFilter(
            key\="author",
            value\=\["mats@timescale.com", "sven@timescale.com"\],
            operator\="in",
        ),
    \],
    condition\="and",
)

retriever \= index.as\_retriever(
    similarity\_top\_k\=10,
    filters\=filters,
)

retrieved\_nodes \= retriever.retrieve("What is this software project about?")

for node in retrieved\_nodes:
    print(node.node.metadata)

filters = MetadataFilters( filters=\[ MetadataFilter(key="commit\_date", value="2023-08-01", operator=">="), MetadataFilter(key="commit\_date", value="2023-08-15", operator="<="), MetadataFilter( key="author", value=\["mats@timescale.com", "sven@timescale.com"\], operator="in", ), \], condition="and", ) retriever = index.as\_retriever( similarity\_top\_k=10, filters=filters, ) retrieved\_nodes = retriever.retrieve("What is this software project about?") for node in retrieved\_nodes: print(node.node.metadata)

{'commit\_date': '2023-08-07', 'author': 'mats@timescale.com', 'fixes': \[\]}
{'commit\_date': '2023-08-07', 'author': 'sven@timescale.com', 'fixes': \[\]}
{'commit\_date': '2023-08-15', 'author': 'sven@timescale.com', 'fixes': \[\]}
{'commit\_date': '2023-08-10', 'author': 'mats@timescale.com', 'fixes': \[\]}

In \[ \]:

Copied!

\# Same thing, with NOT IN
filters \= MetadataFilters(
    filters\=\[
        MetadataFilter(key\="commit\_date", value\="2023-08-01", operator\=">="),
        MetadataFilter(key\="commit\_date", value\="2023-08-15", operator\="<="),
        MetadataFilter(
            key\="author",
            value\=\["mats@timescale.com", "sven@timescale.com"\],
            operator\="nin",
        ),
    \],
    condition\="and",
)

retriever \= index.as\_retriever(
    similarity\_top\_k\=10,
    filters\=filters,
)

retrieved\_nodes \= retriever.retrieve("What is this software project about?")

for node in retrieved\_nodes:
    print(node.node.metadata)

\# Same thing, with NOT IN filters = MetadataFilters( filters=\[ MetadataFilter(key="commit\_date", value="2023-08-01", operator=">="), MetadataFilter(key="commit\_date", value="2023-08-15", operator="<="), MetadataFilter( key="author", value=\["mats@timescale.com", "sven@timescale.com"\], operator="nin", ), \], condition="and", ) retriever = index.as\_retriever( similarity\_top\_k=10, filters=filters, ) retrieved\_nodes = retriever.retrieve("What is this software project about?") for node in retrieved\_nodes: print(node.node.metadata)

{'commit\_date': '2023-08-09', 'author': 'me@noctarius.com', 'fixes': \['5805'\]}
{'commit\_date': '2023-08-15', 'author': '36882414+akuzm@users.noreply.github.com', 'fixes': \[\]}
{'commit\_date': '2023-08-15', 'author': '36882414+akuzm@users.noreply.github.com', 'fixes': \[\]}
{'commit\_date': '2023-08-11', 'author': '36882414+akuzm@users.noreply.github.com', 'fixes': \[\]}
{'commit\_date': '2023-08-09', 'author': 'konstantina@timescale.com', 'fixes': \['5923', '5680', '5774', '5786', '5906', '5912'\]}
{'commit\_date': '2023-08-03', 'author': 'dmitry@timescale.com', 'fixes': \[\]}
{'commit\_date': '2023-08-03', 'author': 'dmitry@timescale.com', 'fixes': \['5908'\]}
{'commit\_date': '2023-08-01', 'author': 'nikhil@timescale.com', 'fixes': \[\]}
{'commit\_date': '2023-08-10', 'author': 'konstantina@timescale.com', 'fixes': \[\]}
{'commit\_date': '2023-08-10', 'author': '36882414+akuzm@users.noreply.github.com', 'fixes': \[\]}

In \[ \]:

Copied!

\# CONTAINS
filters \= MetadataFilters(
    filters\=\[
        MetadataFilter(key\="fixes", value\="5680", operator\="contains"),
    \]
)

retriever \= index.as\_retriever(
    similarity\_top\_k\=10,
    filters\=filters,
)

retrieved\_nodes \= retriever.retrieve("How did these commits fix the issue?")
for node in retrieved\_nodes:
    print(node.node.metadata)

\# CONTAINS filters = MetadataFilters( filters=\[ MetadataFilter(key="fixes", value="5680", operator="contains"), \] ) retriever = index.as\_retriever( similarity\_top\_k=10, filters=filters, ) retrieved\_nodes = retriever.retrieve("How did these commits fix the issue?") for node in retrieved\_nodes: print(node.node.metadata)

{'commit\_date': '2023-08-09', 'author': 'konstantina@timescale.com', 'fixes': \['5923', '5680', '5774', '5786', '5906', '5912'\]}

### PgVector Query Options[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/postgres/#pgvector-query-options)

#### IVFFlat Probes[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/postgres/#ivfflat-probes)

Specify the number of [IVFFlat probes](https://github.com/pgvector/pgvector?tab=readme-ov-file#query-options) (1 by default)

When retrieving from the index, you can specify an appropriate number of IVFFlat probes (higher is better for recall, lower is better for speed)

In \[ \]:

Copied!

retriever \= index.as\_retriever(
    vector\_store\_query\_mode\="hybrid",
    similarity\_top\_k\=5,
    vector\_store\_kwargs\={"ivfflat\_probes": 10},
)

retriever = index.as\_retriever( vector\_store\_query\_mode="hybrid", similarity\_top\_k=5, vector\_store\_kwargs={"ivfflat\_probes": 10}, )

#### HNSW EF Search[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/postgres/#hnsw-ef-search)

Specify the size of the dynamic [candidate list](https://github.com/pgvector/pgvector?tab=readme-ov-file#query-options-1) for search (40 by default)

In \[ \]:

Copied!

retriever \= index.as\_retriever(
    vector\_store\_query\_mode\="hybrid",
    similarity\_top\_k\=5,
    vector\_store\_kwargs\={"hnsw\_ef\_search": 300},
)

retriever = index.as\_retriever( vector\_store\_query\_mode="hybrid", similarity\_top\_k=5, vector\_store\_kwargs={"hnsw\_ef\_search": 300}, )

Back to top

[Previous Pinecone Vector Store - Metadata Filter](https://docs.llamaindex.ai/en/stable/examples/vector_stores/pinecone_metadata_filter/)[Next Hybrid Search with Qdrant BM42](https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_bm42/)
