Title: Property Graph Construction with Predefined Schemas

URL Source: https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_advanced/

Markdown Content:
Property Graph Construction with Predefined Schemas - LlamaIndex


[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/docs/examples/property_graph/property_graph_advanced.ipynb)

In this notebook, we walk through using Neo4j, Ollama and Huggingface to build a property graph.

Specifically, we will be using the `SchemaLLMPathExtractor` which allows us to specify an exact schema containing possible entity types, relation types, and defining how they can be connected together.

This is useful for when you have a specific graph you want to build, and want to limit what the LLM is predicting.

In \[ \]:

Copied!

%pip install llama\-index
%pip install llama\-index\-llms\-ollama
%pip install llama\-index\-embeddings\-huggingface
\# Optional
%pip install llama\-index\-graph\-stores\-neo4j
%pip install llama\-index\-graph\-stores\-nebula

%pip install llama-index %pip install llama-index-llms-ollama %pip install llama-index-embeddings-huggingface # Optional %pip install llama-index-graph-stores-neo4j %pip install llama-index-graph-stores-nebula

Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_advanced/#load-data)
-------------------------------------------------------------------------------------------------------------

First, lets download some sample data to play with.

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

\--2024-06-26 11:12:16--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.110.133, 185.199.109.133, 185.199.111.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.110.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 75042 (73K) \[text/plain\]
Saving to: ‘data/paul\_graham/paul\_graham\_essay.txt’

data/paul\_graham/pa 100%\[>\]  73.28K  --.-KB/s    in 0.007s  

2024-06-26 11:12:16 (10.4 MB/s) - ‘data/paul\_graham/paul\_graham\_essay.txt’ saved \[75042/75042\]

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

from llama\_index.core import SimpleDirectoryReader documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data()

Graph Construction[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_advanced/#graph-construction)
-------------------------------------------------------------------------------------------------------------------------------

To construct our graph, we are going to take advantage of the `SchemaLLMPathExtractor` to construct our graph.

Given some schema for a graph, we can extract entities and relations that follow this schema, rather than letting the LLM decide entities and relations at random.

In \[ \]:

Copied!

import nest\_asyncio

nest\_asyncio.apply()

import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

from typing import Literal
from llama\_index.llms.ollama import Ollama
from llama\_index.core.indices.property\_graph import SchemaLLMPathExtractor

\# best practice to use upper-case
entities \= Literal\["PERSON", "PLACE", "ORGANIZATION"\]
relations \= Literal\["HAS", "PART\_OF", "WORKED\_ON", "WORKED\_WITH", "WORKED\_AT"\]

\# define which entities can have which relations
validation\_schema \= {
    "PERSON": \["HAS", "PART\_OF", "WORKED\_ON", "WORKED\_WITH", "WORKED\_AT"\],
    "PLACE": \["HAS", "PART\_OF", "WORKED\_AT"\],
    "ORGANIZATION": \["HAS", "PART\_OF", "WORKED\_WITH"\],
}
validation\_schema \= \[
    ("ORGANIZATION", "HAS", "PERSON"),
    ("PERSON", "WORKED\_AT", "ORGANIZATION"),
    ("PERSON", "WORKED\_WITH", "PERSON"),
    ("PERSON", "WORKED\_ON", "ORGANIZATION"),
    ("PERSON", "PART\_OF", "ORGANIZATION"),
    ("ORGANIZATION", "PART\_OF", "ORGANIZATION"),
    ("PERSON", "WORKED\_AT", "PLACE"),
\]

kg\_extractor \= SchemaLLMPathExtractor(
    llm\=Ollama(model\="llama3", json\_mode\=True, request\_timeout\=3600),
    possible\_entities\=entities,
    possible\_relations\=relations,
    kg\_validation\_schema\=validation\_schema,
    \# if false, allows for values outside of the schema
    \# useful for using the schema as a suggestion
    strict\=True,
)

from typing import Literal from llama\_index.llms.ollama import Ollama from llama\_index.core.indices.property\_graph import SchemaLLMPathExtractor # best practice to use upper-case entities = Literal\["PERSON", "PLACE", "ORGANIZATION"\] relations = Literal\["HAS", "PART\_OF", "WORKED\_ON", "WORKED\_WITH", "WORKED\_AT"\] # define which entities can have which relations validation\_schema = { "PERSON": \["HAS", "PART\_OF", "WORKED\_ON", "WORKED\_WITH", "WORKED\_AT"\], "PLACE": \["HAS", "PART\_OF", "WORKED\_AT"\], "ORGANIZATION": \["HAS", "PART\_OF", "WORKED\_WITH"\], } validation\_schema = \[ ("ORGANIZATION", "HAS", "PERSON"), ("PERSON", "WORKED\_AT", "ORGANIZATION"), ("PERSON", "WORKED\_WITH", "PERSON"), ("PERSON", "WORKED\_ON", "ORGANIZATION"), ("PERSON", "PART\_OF", "ORGANIZATION"), ("ORGANIZATION", "PART\_OF", "ORGANIZATION"), ("PERSON", "WORKED\_AT", "PLACE"), \] kg\_extractor = SchemaLLMPathExtractor( llm=Ollama(model="llama3", json\_mode=True, request\_timeout=3600), possible\_entities=entities, possible\_relations=relations, kg\_validation\_schema=validation\_schema, # if false, allows for values outside of the schema # useful for using the schema as a suggestion strict=True, )

Now, You can use SimplePropertyGraph, Neo4j, or NebulaGraph to store the graph.

**Option 1. Neo4j**

To launch Neo4j locally, first ensure you have docker installed. Then, you can launch the database with the following docker command

docker run \\
    \-p 7474:7474 \-p 7687:7687 \\
    \-v $PWD/data:/data \-v $PWD/plugins:/plugins \\
    \--name neo4j-apoc \\
    \-e NEO4J\_apoc\_export\_file\_enabled\=true \\
    \-e NEO4J\_apoc\_import\_file\_enabled\=true \\
    \-e NEO4J\_apoc\_import\_file\_use\_\_neo4j\_\_config\=true \\
    \-e NEO4JLABS\_PLUGINS\=\\\[\\"apoc\\"\\\] \\
    neo4j:latest

From here, you can open the db at [http://localhost:7474/](http://localhost:7474/). On this page, you will be asked to sign in. Use the default username/password of `neo4j` and `neo4j`.

Once you login for the first time, you will be asked to change the password.

After this, you are ready to create your first property graph!

In \[ \]:

Copied!

from llama\_index.graph\_stores.neo4j import Neo4jPropertyGraphStore

graph\_store \= Neo4jPropertyGraphStore(
    username\="neo4j",
    password\="<password>",
    url\="bolt://localhost:7687",
)
vec\_store \= None

from llama\_index.graph\_stores.neo4j import Neo4jPropertyGraphStore graph\_store = Neo4jPropertyGraphStore( username="neo4j", password="", url="bolt://localhost:7687", ) vec\_store = None

**Option 2. NebulaGraph**

To launch NebulaGraph locally, first ensure you have docker installed. Then, you can launch the database with the following docker command.

mkdir nebula-docker-compose
cd nebula-docker-compose
curl \--output docker-compose.yaml https://raw.githubusercontent.com/vesoft-inc/nebula-docker-compose/master/docker-compose-lite.yaml
docker compose up

After this, you are ready to create your first property graph!

> Other options/details for deploying NebulaGraph can be found in the [docs](https://docs.nebula-graph.io/):
> 
> *   [ad-hoc cluster in Google Colab](https://docs.nebula-graph.io/master/4.deployment-and-installation/2.compile-and-install-nebula-graph/8.deploy-nebula-graph-with-lite/).
> *   [Docker Desktop Extension](https://docs.nebula-graph.io/master/2.quick-start/1.quick-start-workflow/).

In \[ \]:

Copied!

from llama\_index.graph\_stores.nebula import NebulaPropertyGraphStore
from llama\_index.core.vector\_stores.simple import SimpleVectorStore

graph\_store \= NebulaPropertyGraphStore(
    space\="llamaindex\_nebula\_property\_graph", overwrite\=True
)
vec\_store \= SimpleVectorStore()

from llama\_index.graph\_stores.nebula import NebulaPropertyGraphStore from llama\_index.core.vector\_stores.simple import SimpleVectorStore graph\_store = NebulaPropertyGraphStore( space="llamaindex\_nebula\_property\_graph", overwrite=True ) vec\_store = SimpleVectorStore()

_If you want to explore the graph with NebulaGraph Jupyter extension_, run the following commands. Or just skip them.

In \[ \]:

Copied!

%pip install jupyter\-nebulagraph

%pip install jupyter-nebulagraph

In \[ \]:

Copied!

\# load NebulaGraph Jupyter extension to enable %ngql magic
%load\_ext ngql
\# connect to NebulaGraph service
%ngql \--address 127.0.0.1 \--port 9669 \--user root \--password nebula
%ngql CREATE SPACE IF NOT EXISTS llamaindex\_nebula\_property\_graph(vid\_type\=FIXED\_STRING(256));

\# load NebulaGraph Jupyter extension to enable %ngql magic %load\_ext ngql # connect to NebulaGraph service %ngql --address 127.0.0.1 --port 9669 --user root --password nebula %ngql CREATE SPACE IF NOT EXISTS llamaindex\_nebula\_property\_graph(vid\_type=FIXED\_STRING(256));

In \[ \]:

Copied!

\# use the graph space, which is similar to "use database" in MySQL
\# The space was created in async way, so we need to wait for a while before using it, retry it if failed
%ngql USE llamaindex\_nebula\_property\_graph;

\# use the graph space, which is similar to "use database" in MySQL # The space was created in async way, so we need to wait for a while before using it, retry it if failed %ngql USE llamaindex\_nebula\_property\_graph;

**Start building!**

**NOTE:** Using a local model will be slower when extracting compared to API based models. Local models (like Ollama) are typically limited to sequential processing. Expect this to take about 10 minutes on an M2 Max.

In \[ \]:

Copied!

from llama\_index.core import PropertyGraphIndex
from llama\_index.embeddings.huggingface import HuggingFaceEmbedding

index \= PropertyGraphIndex.from\_documents(
    documents,
    kg\_extractors\=\[kg\_extractor\],
    embed\_model\=HuggingFaceEmbedding(model\_name\="BAAI/bge-small-en-v1.5"),
    property\_graph\_store\=graph\_store,
    vector\_store\=vec\_store,
    show\_progress\=True,
)

from llama\_index.core import PropertyGraphIndex from llama\_index.embeddings.huggingface import HuggingFaceEmbedding index = PropertyGraphIndex.from\_documents( documents, kg\_extractors=\[kg\_extractor\], embed\_model=HuggingFaceEmbedding(model\_name="BAAI/bge-small-en-v1.5"), property\_graph\_store=graph\_store, vector\_store=vec\_store, show\_progress=True, )

If we inspect the graph created, we can see that it only includes the relations and entity types that we defined!

In \[ \]:

Copied!

\# If using NebulaGraph Jupyter extension
%ngql MATCH p\=()\-\[\]\->() RETURN p LIMIT 20;

\# If using NebulaGraph Jupyter extension %ngql MATCH p=()-\[\]->() RETURN p LIMIT 20;

In \[ \]:

Copied!

%ng\_draw

%ng\_draw

Or Neo4j:

![Image 4: local graph](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_advanced/local_kg.png)

For information on all `kg_extractors`, see [the documentation](https://docs.llamaindex.ai/en/stable/examples/module_guides/indexing/lpg_index_guide.md#construction).

Querying[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_advanced/#querying)
-----------------------------------------------------------------------------------------------------------

Now that our graph is created, we can query it.

As is the theme with this notebook, we will be using a lower-level API and constructing all our retrievers ourselves!

In \[ \]:

Copied!

from llama\_index.core.indices.property\_graph import (
    LLMSynonymRetriever,
    VectorContextRetriever,
)

llm\_synonym \= LLMSynonymRetriever(
    index.property\_graph\_store,
    llm\=Ollama(model\="llama3", request\_timeout\=3600),
    include\_text\=False,
)
vector\_context \= VectorContextRetriever(
    index.property\_graph\_store,
    embed\_model\=HuggingFaceEmbedding(model\_name\="BAAI/bge-small-en-v1.5"),
    include\_text\=False,
)

from llama\_index.core.indices.property\_graph import ( LLMSynonymRetriever, VectorContextRetriever, ) llm\_synonym = LLMSynonymRetriever( index.property\_graph\_store, llm=Ollama(model="llama3", request\_timeout=3600), include\_text=False, ) vector\_context = VectorContextRetriever( index.property\_graph\_store, embed\_model=HuggingFaceEmbedding(model\_name="BAAI/bge-small-en-v1.5"), include\_text=False, )

In \[ \]:

Copied!

retriever \= index.as\_retriever(
    sub\_retrievers\=\[
        llm\_synonym,
        vector\_context,
    \]
)

retriever = index.as\_retriever( sub\_retrievers=\[ llm\_synonym, vector\_context, \] )

In \[ \]:

Copied!

nodes \= retriever.retrieve("What happened at Interleaf?")

for node in nodes:
    print(node.text)

nodes = retriever.retrieve("What happened at Interleaf?") for node in nodes: print(node.text)

Interleaf -> HAS -> Paul Graham
Interleaf -> HAS -> Emacs
Interleaf -> HAS -> Release Engineering
Interleaf -> HAS -> Viaweb
Interleaf -> HAS -> Y Combinator
Interleaf -> HAS -> impressive technology
Interleaf -> HAS -> smart people

We can also create a query engine with similar syntax.

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(
    sub\_retrievers\=\[
        llm\_synonym,
        vector\_context,
    \],
    llm\=Ollama(model\="llama3", request\_timeout\=3600),
)

response \= query\_engine.query("What happened at Interleaf?")

print(str(response))

query\_engine = index.as\_query\_engine( sub\_retrievers=\[ llm\_synonym, vector\_context, \], llm=Ollama(model="llama3", request\_timeout=3600), ) response = query\_engine.query("What happened at Interleaf?") print(str(response))

Paul Graham worked there, as well as other smart people. Emacs was also present.

For more info on all retrievers, see the [complete guide](https://docs.llamaindex.ai/en/stable/examples/module_guides/indexing/lpg_index_guide.md#retrieval-and-querying).

Back to top

[Previous Using a Property Graph Store](https://docs.llamaindex.ai/en/stable/examples/property_graph/graph_store/)[Next Property Graph Index](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_basic/)

Hi, how can I help you?

🦙
