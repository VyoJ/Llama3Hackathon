Title: Neo4j Property Graph Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_neo4j/

Markdown Content:
Neo4j Property Graph Index - LlamaIndex


[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/docs/examples/property_graph/property_graph_neo4j.ipynb)

Neo4j is a production-grade graph database, capable of storing a property graph, performing vector search, filtering, and more.

The easiest way to get started is with a cloud-hosted instance using [Neo4j Aura](https://neo4j.com/cloud/platform/aura-graph-database/)

For this notebook, we will instead cover how to run the database locally with docker.

If you already have an existing graph, please skip to the end of this notebook.

In \[ \]:

Copied!

%pip install llama\-index llama\-index\-graph\-stores\-neo4j

%pip install llama-index llama-index-graph-stores-neo4j

Docker Setup[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_neo4j/#docker-setup)
----------------------------------------------------------------------------------------------------------------

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

Env Setup[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_neo4j/#env-setup)
----------------------------------------------------------------------------------------------------------

We need just a few environment setups to get started.

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-proj-..."

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-proj-..."

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

In \[ \]:

Copied!

import nest\_asyncio

nest\_asyncio.apply()

import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

from llama\_index.core import SimpleDirectoryReader documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data()

/Users/loganmarkewich/Library/Caches/pypoetry/virtualenvs/llama-index-caVs7DDe-py3.11/lib/python3.11/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user\_install.html
  from .autonotebook import tqdm as notebook\_tqdm

Index Construction[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_neo4j/#index-construction)
----------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.graph\_stores.neo4j import Neo4jPropertyGraphStore

\# Note: used to be \`Neo4jPGStore\`
graph\_store \= Neo4jPropertyGraphStore(
    username\="neo4j",
    password\="llamaindex",
    url\="bolt://localhost:7687",
)

from llama\_index.graph\_stores.neo4j import Neo4jPropertyGraphStore # Note: used to be \`Neo4jPGStore\` graph\_store = Neo4jPropertyGraphStore( username="neo4j", password="llamaindex", url="bolt://localhost:7687", )

In \[ \]:

Copied!

from llama\_index.core import PropertyGraphIndex
from llama\_index.embeddings.openai import OpenAIEmbedding
from llama\_index.llms.openai import OpenAI
from llama\_index.core.indices.property\_graph import SchemaLLMPathExtractor

index \= PropertyGraphIndex.from\_documents(
    documents,
    embed\_model\=OpenAIEmbedding(model\_name\="text-embedding-3-small"),
    kg\_extractors\=\[
        SchemaLLMPathExtractor(
            llm\=OpenAI(model\="gpt-3.5-turbo", temperature\=0.0)
        )
    \],
    property\_graph\_store\=graph\_store,
    show\_progress\=True,
)

from llama\_index.core import PropertyGraphIndex from llama\_index.embeddings.openai import OpenAIEmbedding from llama\_index.llms.openai import OpenAI from llama\_index.core.indices.property\_graph import SchemaLLMPathExtractor index = PropertyGraphIndex.from\_documents( documents, embed\_model=OpenAIEmbedding(model\_name="text-embedding-3-small"), kg\_extractors=\[ SchemaLLMPathExtractor( llm=OpenAI(model="gpt-3.5-turbo", temperature=0.0) ) \], property\_graph\_store=graph\_store, show\_progress=True, )

Parsing nodes: 100%|██████████| 1/1 \[00:00<00:00, 21.63it/s\]
Extracting paths from text with schema: 100%|██████████| 22/22 \[01:06<00:00,  3.02s/it\]
Generating embeddings: 100%|██████████| 1/1 \[00:00<00:00,  1.06it/s\]
Generating embeddings: 100%|██████████| 1/1 \[00:00<00:00,  1.89it/s\]

Now that the graph is created, we can explore it in the UI by visting [http://localhost:7474/](http://localhost:7474/).

The easiest way to see the entire graph is to use a cypher command like `"match n=() return n"` at the top.

To delete an entire graph, a useful command is `"match n=() detach delete n"`.

Querying and Retrieval[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_neo4j/#querying-and-retrieval)
------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

retriever \= index.as\_retriever(
    include\_text\=False,  \# include source text in returned nodes, default True
)

nodes \= retriever.retrieve("What happened at Interleaf and Viaweb?")

for node in nodes:
    print(node.text)

retriever = index.as\_retriever( include\_text=False, # include source text in returned nodes, default True ) nodes = retriever.retrieve("What happened at Interleaf and Viaweb?") for node in nodes: print(node.text)

Interleaf -> Got crushed by -> Moore's law
Interleaf -> Made -> Scripting language
Interleaf -> Had -> Smart people
Interleaf -> Inspired by -> Emacs
Interleaf -> Had -> Few years to live
Interleaf -> Made -> Software
Interleaf -> Had done -> Something bold
Interleaf -> Added -> Scripting language
Interleaf -> Built -> Impressive technology
Interleaf -> Was -> Company
Viaweb -> Was -> Profitable
Viaweb -> Was -> Growing rapidly
Viaweb -> Suggested -> Hospital
Idea -> Was clear from -> Experience
Idea -> Would have to be embodied as -> Company
Painting department -> Seemed to be -> Rigorous

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(include\_text\=True)

response \= query\_engine.query("What happened at Interleaf and Viaweb?")

print(str(response))

query\_engine = index.as\_query\_engine(include\_text=True) response = query\_engine.query("What happened at Interleaf and Viaweb?") print(str(response))

Interleaf had smart people and built impressive technology but got crushed by Moore's Law. Viaweb was profitable and growing rapidly.

Loading from an existing Graph[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_neo4j/#loading-from-an-existing-graph)
----------------------------------------------------------------------------------------------------------------------------------------------------

If you have an existing graph (either created with LlamaIndex or otherwise), we can connect to and use it!

**NOTE:** If your graph was created outside of LlamaIndex, the most useful retrievers will be [text to cypher](https://docs.llamaindex.ai/en/stable/examples/module_guides/indexing/lpg_index_guide.md#texttocypherretriever) or [cypher templates](https://docs.llamaindex.ai/en/stable/examples/module_guides/indexing/lpg_index_guide.md#cyphertemplateretriever). Other retrievers rely on properties that LlamaIndex inserts.

In \[ \]:

Copied!

from llama\_index.graph\_stores.neo4j import Neo4jPropertyGraphStore
from llama\_index.core import PropertyGraphIndex
from llama\_index.embeddings.openai import OpenAIEmbedding
from llama\_index.llms.openai import OpenAI

graph\_store \= Neo4jPropertyGraphStore(
    username\="neo4j",
    password\="794613852",
    url\="bolt://localhost:7687",
)

index \= PropertyGraphIndex.from\_existing(
    property\_graph\_store\=graph\_store,
    llm\=OpenAI(model\="gpt-3.5-turbo", temperature\=0.3),
    embed\_model\=OpenAIEmbedding(model\_name\="text-embedding-3-small"),
)

from llama\_index.graph\_stores.neo4j import Neo4jPropertyGraphStore from llama\_index.core import PropertyGraphIndex from llama\_index.embeddings.openai import OpenAIEmbedding from llama\_index.llms.openai import OpenAI graph\_store = Neo4jPropertyGraphStore( username="neo4j", password="794613852", url="bolt://localhost:7687", ) index = PropertyGraphIndex.from\_existing( property\_graph\_store=graph\_store, llm=OpenAI(model="gpt-3.5-turbo", temperature=0.3), embed\_model=OpenAIEmbedding(model\_name="text-embedding-3-small"), )

From here, we can still insert more documents!

In \[ \]:

Copied!

from llama\_index.core import Document

document \= Document(text\="LlamaIndex is great!")

index.insert(document)

from llama\_index.core import Document document = Document(text="LlamaIndex is great!") index.insert(document)

In \[ \]:

Copied!

nodes \= index.as\_retriever(include\_text\=False).retrieve("LlamaIndex")

print(nodes\[0\].text)

nodes = index.as\_retriever(include\_text=False).retrieve("LlamaIndex") print(nodes\[0\].text)

Llamaindex -> Is -> Great

For full details on construction, retrieval, querying of a property graph, see the [full docs page](https://docs.llamaindex.ai/en/stable/examples/module_guides/indexing/lpg_index_guide.md).

Back to top

[Previous Defining a Custom Property Graph Retriever](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_custom_retriever/)[Next Retriever Query Engine with Custom Retrievers - Simple Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/query_engine/CustomRetrievers/)

Hi, how can I help you?

🦙
