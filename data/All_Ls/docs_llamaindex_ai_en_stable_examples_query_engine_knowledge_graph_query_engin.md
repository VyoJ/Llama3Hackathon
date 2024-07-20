Title: Knowledge Graph Query Engine - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/query_engine/knowledge_graph_query_engine/

Markdown Content:
Knowledge Graph Query Engine - LlamaIndex


Creating a Knowledge Graph usually involves specialized and complex tasks. However, by utilizing the Llama Index (LLM), the KnowledgeGraphIndex, and the GraphStore, we can facilitate the creation of a relatively effective Knowledge Graph from any data source supported by [Llama Hub](https://llamahub.ai/).

Furthermore, querying a Knowledge Graph often requires domain-specific knowledge related to the storage system, such as Cypher. But, with the assistance of the LLM and the LlamaIndex KnowledgeGraphQueryEngine, this can be accomplished using Natural Language!

In this demonstration, we will guide you through the steps to:

*   Extract and Set Up a Knowledge Graph using the Llama Index
*   Query a Knowledge Graph using Cypher
*   Query a Knowledge Graph using Natural Language

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-readers\-wikipedia
%pip install llama\-index\-llms\-azure\-openai
%pip install llama\-index\-graph\-stores\-nebula
%pip install llama\-index\-llms\-openai
%pip install llama\-index\-embeddings\-azure\-openai

%pip install llama-index-readers-wikipedia %pip install llama-index-llms-azure-openai %pip install llama-index-graph-stores-nebula %pip install llama-index-llms-openai %pip install llama-index-embeddings-azure-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

Let's first get ready for basic preparation of Llama Index.

### OpenAI[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/knowledge_graph_query_engine/#openai)

In \[ \]:

Copied!

\# For OpenAI

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import logging
import sys

logging.basicConfig(
    stream\=sys.stdout, level\=logging.INFO
)  \# logging.DEBUG for more verbose output

\# define LLM
from llama\_index.llms.openai import OpenAI
from llama\_index.core import Settings

Settings.llm \= OpenAI(temperature\=0, model\="gpt-3.5-turbo")
Settings.chunk\_size \= 512

\# For OpenAI import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..." import logging import sys logging.basicConfig( stream=sys.stdout, level=logging.INFO ) # logging.DEBUG for more verbose output # define LLM from llama\_index.llms.openai import OpenAI from llama\_index.core import Settings Settings.llm = OpenAI(temperature=0, model="gpt-3.5-turbo") Settings.chunk\_size = 512

### Azure[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/knowledge_graph_query_engine/#azure)

In \[ \]:

Copied!

from llama\_index.llms.azure\_openai import AzureOpenAI
from llama\_index.embeddings.azure\_openai import AzureOpenAIEmbedding

\# For Azure OpenAI
api\_key \= "<api-key>"
azure\_endpoint \= "https://<your-resource-name>.openai.azure.com/"
api\_version \= "2023-07-01-preview"

llm \= AzureOpenAI(
    model\="gpt-35-turbo-16k",
    deployment\_name\="my-custom-llm",
    api\_key\=api\_key,
    azure\_endpoint\=azure\_endpoint,
    api\_version\=api\_version,
)

\# You need to deploy your own embedding model as well as your own chat completion model
embed\_model \= AzureOpenAIEmbedding(
    model\="text-embedding-ada-002",
    deployment\_name\="my-custom-embedding",
    api\_key\=api\_key,
    azure\_endpoint\=azure\_endpoint,
    api\_version\=api\_version,
)

from llama\_index.llms.azure\_openai import AzureOpenAI from llama\_index.embeddings.azure\_openai import AzureOpenAIEmbedding # For Azure OpenAI api\_key = "" azure\_endpoint = "https://.openai.azure.com/" api\_version = "2023-07-01-preview" llm = AzureOpenAI( model="gpt-35-turbo-16k", deployment\_name="my-custom-llm", api\_key=api\_key, azure\_endpoint=azure\_endpoint, api\_version=api\_version, ) # You need to deploy your own embedding model as well as your own chat completion model embed\_model = AzureOpenAIEmbedding( model="text-embedding-ada-002", deployment\_name="my-custom-embedding", api\_key=api\_key, azure\_endpoint=azure\_endpoint, api\_version=api\_version, )

In \[ \]:

Copied!

from llama\_index.core import Settings

Settings.llm \= llm
Settings.embed\_model \= embed\_model
Settings.chunk\_size \= 512

from llama\_index.core import Settings Settings.llm = llm Settings.embed\_model = embed\_model Settings.chunk\_size = 512

Prepare for NebulaGraph[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/knowledge_graph_query_engine/#prepare-for-nebulagraph)
--------------------------------------------------------------------------------------------------------------------------------------------

Before next step to creating the Knowledge Graph, let's ensure we have a running NebulaGraph with defined data schema.

In \[ \]:

Copied!

\# Create a NebulaGraph (version 3.5.0 or newer) cluster with:
\# Option 0 for machines with Docker: \`curl -fsSL nebula-up.siwei.io/install.sh | bash\`
\# Option 1 for Desktop: NebulaGraph Docker Extension https://hub.docker.com/extensions/weygu/nebulagraph-dd-ext

\# If not, create it with the following commands from NebulaGraph's console:
\# CREATE SPACE llamaindex(vid\_type=FIXED\_STRING(256), partition\_num=1, replica\_factor=1);
\# :sleep 10;
\# USE llamaindex;
\# CREATE TAG entity(name string);
\# CREATE EDGE relationship(relationship string);
\# :sleep 10;
\# CREATE TAG INDEX entity\_index ON entity(name(256));

%pip install ipython\-ngql nebula3\-python

os.environ\["NEBULA\_USER"\] \= "root"
os.environ\["NEBULA\_PASSWORD"\] \= "nebula"  \# default is "nebula"
os.environ\[
    "NEBULA\_ADDRESS"
\] \= "127.0.0.1:9669"  \# assumed we have NebulaGraph installed locally

space\_name \= "llamaindex"
edge\_types, rel\_prop\_names \= \["relationship"\], \[
    "relationship"
\]  \# default, could be omit if create from an empty kg
tags \= \["entity"\]  \# default, could be omit if create from an empty kg

\# Create a NebulaGraph (version 3.5.0 or newer) cluster with: # Option 0 for machines with Docker: \`curl -fsSL nebula-up.siwei.io/install.sh | bash\` # Option 1 for Desktop: NebulaGraph Docker Extension https://hub.docker.com/extensions/weygu/nebulagraph-dd-ext # If not, create it with the following commands from NebulaGraph's console: # CREATE SPACE llamaindex(vid\_type=FIXED\_STRING(256), partition\_num=1, replica\_factor=1); # :sleep 10; # USE llamaindex; # CREATE TAG entity(name string); # CREATE EDGE relationship(relationship string); # :sleep 10; # CREATE TAG INDEX entity\_index ON entity(name(256)); %pip install ipython-ngql nebula3-python os.environ\["NEBULA\_USER"\] = "root" os.environ\["NEBULA\_PASSWORD"\] = "nebula" # default is "nebula" os.environ\[ "NEBULA\_ADDRESS" \] = "127.0.0.1:9669" # assumed we have NebulaGraph installed locally space\_name = "llamaindex" edge\_types, rel\_prop\_names = \["relationship"\], \[ "relationship" \] # default, could be omit if create from an empty kg tags = \["entity"\] # default, could be omit if create from an empty kg

Requirement already satisfied: ipython-ngql in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (0.5)
Requirement already satisfied: nebula3-python in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (3.4.0)
Requirement already satisfied: pandas in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from ipython-ngql) (2.0.3)
Requirement already satisfied: Jinja2 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from ipython-ngql) (3.1.2)
Requirement already satisfied: pytz>=2021.1 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from nebula3-python) (2023.3)
Requirement already satisfied: future>=0.18.0 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from nebula3-python) (0.18.3)
Requirement already satisfied: httplib2>=0.20.0 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from nebula3-python) (0.22.0)
Requirement already satisfied: six>=1.16.0 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from nebula3-python) (1.16.0)
Requirement already satisfied: pyparsing!=3.0.0,!=3.0.1,!=3.0.2,!=3.0.3,<4,>=2.4.2 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from httplib2>=0.20.0->nebula3-python) (3.0.9)
Requirement already satisfied: MarkupSafe>=2.0 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from Jinja2->ipython-ngql) (2.1.3)
Requirement already satisfied: tzdata>=2022.1 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from pandas->ipython-ngql) (2023.3)
Requirement already satisfied: numpy>=1.20.3 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from pandas->ipython-ngql) (1.25.2)
Requirement already satisfied: python-dateutil>=2.8.2 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from pandas->ipython-ngql) (2.8.2)
WARNING: You are using pip version 21.2.4; however, version 23.2.1 is available.
You should consider upgrading via the '/Users/loganmarkewich/llama\_index/llama-index/bin/python -m pip install --upgrade pip' command.
Note: you may need to restart the kernel to use updated packages.

Prepare for StorageContext with graph\_store as NebulaGraphStore

In \[ \]:

Copied!

from llama\_index.core import StorageContext
from llama\_index.graph\_stores.nebula import NebulaGraphStore

graph\_store \= NebulaGraphStore(
    space\_name\=space\_name,
    edge\_types\=edge\_types,
    rel\_prop\_names\=rel\_prop\_names,
    tags\=tags,
)
storage\_context \= StorageContext.from\_defaults(graph\_store\=graph\_store)

from llama\_index.core import StorageContext from llama\_index.graph\_stores.nebula import NebulaGraphStore graph\_store = NebulaGraphStore( space\_name=space\_name, edge\_types=edge\_types, rel\_prop\_names=rel\_prop\_names, tags=tags, ) storage\_context = StorageContext.from\_defaults(graph\_store=graph\_store)

(Optional)Build the Knowledge Graph with LlamaIndex[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/knowledge_graph_query_engine/#optionalbuild-the-knowledge-graph-with-llamaindex)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

With the help of Llama Index and LLM defined, we could build Knowledge Graph from given documents.

If we have a Knowledge Graph on NebulaGraphStore already, this step could be skipped

### Step 1, load data from Wikipedia for "Guardians of the Galaxy Vol. 3"[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/knowledge_graph_query_engine/#step-1-load-data-from-wikipedia-for-guardians-of-the-galaxy-vol-3)

In \[ \]:

Copied!

from llama\_index.core import download\_loader

from llama\_index.readers.wikipedia import WikipediaReader

loader \= WikipediaReader()

documents \= loader.load\_data(
    pages\=\["Guardians of the Galaxy Vol. 3"\], auto\_suggest\=False
)

from llama\_index.core import download\_loader from llama\_index.readers.wikipedia import WikipediaReader loader = WikipediaReader() documents = loader.load\_data( pages=\["Guardians of the Galaxy Vol. 3"\], auto\_suggest=False )

### Step 2, Generate a KnowledgeGraphIndex with NebulaGraph as graph\_store[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/knowledge_graph_query_engine/#step-2-generate-a-knowledgegraphindex-with-nebulagraph-as-graph_store)

Then, we will create a KnowledgeGraphIndex to enable Graph based RAG, see [here](https://gpt-index.readthedocs.io/en/latest/examples/index_structs/knowledge_graph/KnowledgeGraphIndex_vs_VectorStoreIndex_vs_CustomIndex_combined.html) for deails, apart from that, we have a Knowledge Graph up and running for other purposes, too!

In \[ \]:

Copied!

from llama\_index.core import KnowledgeGraphIndex

kg\_index \= KnowledgeGraphIndex.from\_documents(
    documents,
    storage\_context\=storage\_context,
    max\_triplets\_per\_chunk\=10,
    space\_name\=space\_name,
    edge\_types\=edge\_types,
    rel\_prop\_names\=rel\_prop\_names,
    tags\=tags,
    include\_embeddings\=True,
)

from llama\_index.core import KnowledgeGraphIndex kg\_index = KnowledgeGraphIndex.from\_documents( documents, storage\_context=storage\_context, max\_triplets\_per\_chunk=10, space\_name=space\_name, edge\_types=edge\_types, rel\_prop\_names=rel\_prop\_names, tags=tags, include\_embeddings=True, )

Now we have a Knowledge Graph on NebulaGraph cluster under space named `llamaindex` about the 'Guardians of the Galaxy Vol. 3' movie, let's play with it a little bit.

In \[ \]:

Copied!

\# install related packages, password is nebula by default
%pip install ipython\-ngql networkx pyvis
%load\_ext ngql
%ngql \--address 127.0.0.1 \--port 9669 \--user root \--password <password\>

\# install related packages, password is nebula by default %pip install ipython-ngql networkx pyvis %load\_ext ngql %ngql --address 127.0.0.1 --port 9669 --user root --password

Requirement already satisfied: ipython-ngql in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (0.5)
Requirement already satisfied: networkx in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (3.1)
Requirement already satisfied: pyvis in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (0.3.2)
Requirement already satisfied: Jinja2 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from ipython-ngql) (3.1.2)
Requirement already satisfied: pandas in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from ipython-ngql) (2.0.3)
Requirement already satisfied: nebula3-python in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from ipython-ngql) (3.4.0)
Requirement already satisfied: jsonpickle>=1.4.1 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from pyvis) (3.0.1)
Requirement already satisfied: ipython>=5.3.0 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from pyvis) (8.10.0)
Requirement already satisfied: backcall in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from ipython>=5.3.0->pyvis) (0.2.0)
Requirement already satisfied: pickleshare in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from ipython>=5.3.0->pyvis) (0.7.5)
Requirement already satisfied: prompt-toolkit<3.1.0,>=3.0.30 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from ipython>=5.3.0->pyvis) (3.0.39)
Requirement already satisfied: appnope in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from ipython>=5.3.0->pyvis) (0.1.3)
Requirement already satisfied: pygments>=2.4.0 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from ipython>=5.3.0->pyvis) (2.15.1)
Requirement already satisfied: traitlets>=5 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from ipython>=5.3.0->pyvis) (5.9.0)
Requirement already satisfied: pexpect>4.3 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from ipython>=5.3.0->pyvis) (4.8.0)
Requirement already satisfied: stack-data in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from ipython>=5.3.0->pyvis) (0.6.2)
Requirement already satisfied: decorator in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from ipython>=5.3.0->pyvis) (5.1.1)
Requirement already satisfied: jedi>=0.16 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from ipython>=5.3.0->pyvis) (0.18.2)
Requirement already satisfied: matplotlib-inline in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from ipython>=5.3.0->pyvis) (0.1.6)
Requirement already satisfied: parso<0.9.0,>=0.8.0 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from jedi>=0.16->ipython>=5.3.0->pyvis) (0.8.3)
Requirement already satisfied: MarkupSafe>=2.0 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from Jinja2->ipython-ngql) (2.1.3)
Requirement already satisfied: ptyprocess>=0.5 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from pexpect>4.3->ipython>=5.3.0->pyvis) (0.7.0)
Requirement already satisfied: wcwidth in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from prompt-toolkit<3.1.0,>=3.0.30->ipython>=5.3.0->pyvis) (0.2.6)
Requirement already satisfied: six>=1.16.0 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from nebula3-python->ipython-ngql) (1.16.0)
Requirement already satisfied: pytz>=2021.1 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from nebula3-python->ipython-ngql) (2023.3)
Requirement already satisfied: future>=0.18.0 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from nebula3-python->ipython-ngql) (0.18.3)
Requirement already satisfied: httplib2>=0.20.0 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from nebula3-python->ipython-ngql) (0.22.0)
Requirement already satisfied: pyparsing!=3.0.0,!=3.0.1,!=3.0.2,!=3.0.3,<4,>=2.4.2 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from httplib2>=0.20.0->nebula3-python->ipython-ngql) (3.0.9)
Requirement already satisfied: python-dateutil>=2.8.2 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from pandas->ipython-ngql) (2.8.2)
Requirement already satisfied: numpy>=1.20.3 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from pandas->ipython-ngql) (1.25.2)
Requirement already satisfied: tzdata>=2022.1 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from pandas->ipython-ngql) (2023.3)
Requirement already satisfied: executing>=1.2.0 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from stack-data->ipython>=5.3.0->pyvis) (1.2.0)
Requirement already satisfied: pure-eval in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from stack-data->ipython>=5.3.0->pyvis) (0.2.2)
Requirement already satisfied: asttokens>=2.1.0 in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from stack-data->ipython>=5.3.0->pyvis) (2.2.1)
WARNING: You are using pip version 21.2.4; however, version 23.2.1 is available.
You should consider upgrading via the '/Users/loganmarkewich/llama\_index/llama-index/bin/python -m pip install --upgrade pip' command.
Note: you may need to restart the kernel to use updated packages.
Connection Pool Created
INFO:nebula3.logger:Get connection to ('127.0.0.1', 9669)
\[ERROR\]:
 'IPythonNGQL' object has no attribute '\_decode\_value'

Out\[ \]:

|  | Name |
| --- | --- |
| 0 | llamaindex |

In \[ \]:

Copied!

\# Query some random Relationships with Cypher
%ngql USE llamaindex;
%ngql MATCH ()\-\[e\]\->() RETURN e LIMIT 10

\# Query some random Relationships with Cypher %ngql USE llamaindex; %ngql MATCH ()-\[e\]->() RETURN e LIMIT 10

INFO:nebula3.logger:Get connection to ('127.0.0.1', 9669)
INFO:nebula3.logger:Get connection to ('127.0.0.1', 9669)

Out\[ \]:

|  | e |
| --- | --- |
| 0 | ("A second trailer for the film")-\[:relationsh... |
| 1 | ("Adam McKay")-\[:relationship@-442854342936029... |
| 2 | ("Adam McKay")-\[:relationship@8513344855738553... |
| 3 | ("Asim Chaudhry")-\[:relationship@-803614038978... |
| 4 | ("Bakalova")-\[:relationship@-25325064520311626... |
| 5 | ("Bautista")-\[:relationship@-90386029986457371... |
| 6 | ("Bautista")-\[:relationship@-90386029986457371... |
| 7 | ("Beth Mickle")-\[:relationship@716197657641767... |
| 8 | ("Bradley Cooper")-\[:relationship@138630731832... |
| 9 | ("Bradley Cooper")-\[:relationship@838402633192... |

In \[ \]:

Copied!

\# draw the result

%ng\_draw

\# draw the result %ng\_draw

nebulagraph\_draw.html

Out\[ \]:

Asking the Knowledge Graph[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/knowledge_graph_query_engine/#asking-the-knowledge-graph)
--------------------------------------------------------------------------------------------------------------------------------------------------

Finally, let's demo how to Query Knowledge Graph with Natural language!

Here, we will leverage the `KnowledgeGraphQueryEngine`, with `NebulaGraphStore` as the `storage_context.graph_store`.

In \[ \]:

Copied!

from llama\_index.core.query\_engine import KnowledgeGraphQueryEngine

from llama\_index.core import StorageContext
from llama\_index.graph\_stores.nebula import NebulaGraphStore

query\_engine \= KnowledgeGraphQueryEngine(
    storage\_context\=storage\_context,
    llm\=llm,
    verbose\=True,
)

from llama\_index.core.query\_engine import KnowledgeGraphQueryEngine from llama\_index.core import StorageContext from llama\_index.graph\_stores.nebula import NebulaGraphStore query\_engine = KnowledgeGraphQueryEngine( storage\_context=storage\_context, llm=llm, verbose=True, )

In \[ \]:

Copied!

response \= query\_engine.query(
    "Tell me about Peter Quill?",
)
display(Markdown(f"<b>{response}</b>"))

response = query\_engine.query( "Tell me about Peter Quill?", ) display(Markdown(f"**{response}**"))

Graph Store Query:
\`\`\`
MATCH (p:\`entity\`)-\[:relationship\]->(m:\`entity\`) WHERE p.\`entity\`.\`name\`  'Peter Quill'

RETURN p.`entity`.`name`;

We could see it helps generate the Graph query:

MATCH (p:\`entity\`)\-\[:relationship\]->(e:\`entity\`) 
  WHERE p.\`entity\`.\`name\` \ 'Peter Quill'
RETURN p.\`entity\`.\`name\`, e.relationship, m.\`entity\`.\`name\`;

%%ngql MATCH (p:\`entity\`)-\[e:relationship\]->(m:\`entity\`) WHERE p.\`entity\`.\`name\`  'Peter Quill'
RETURN p, e, m;

%%ngql MATCH (p:\`entity\`)-\[e:relationship\]->(m:\`entity\`) WHERE p.\`entity\`.\`name\` == 'Peter Quill' RETURN p, e, m;

INFO:nebula3.logger:Get connection to ('127.0.0.1', 9669)

Out\[ \]:

|  | p | e | m |
| --- | --- | --- | --- |
| 0 | ("Peter Quill" :entity{name: "Peter Quill"}) | ("Peter Quill")-\[:relationship@-84437522554765... | ("May 2021" :entity{name: "May 2021"}) |
| 1 | ("Peter Quill" :entity{name: "Peter Quill"}) | ("Peter Quill")-\[:relationship@-11770408155938... | ("as a child" :entity{name: "as a child"}) |
| 2 | ("Peter Quill" :entity{name: "Peter Quill"}) | ("Peter Quill")-\[:relationship@-79394488349732... | ("Guardians of the Galaxy" :entity{name: "Guar... |
| 3 | ("Peter Quill" :entity{name: "Peter Quill"}) | ("Peter Quill")-\[:relationship@325695233021653... | ("a group of alien thieves and smugglers" :ent... |
| 4 | ("Peter Quill" :entity{name: "Peter Quill"}) | ("Peter Quill")-\[:relationship@555553046209276... | ("half-Celestial" :entity{name: "half-Celestia... |

In \[ \]:

Copied!

%ng\_draw

%ng\_draw

nebulagraph\_draw.html

Out\[ \]:

The results of this knowledge-fetching query could not be more clear from the renderred graph then.

Back to top

[Previous JSON Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/json_query_engine/)[Next Knowledge Graph RAG Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/knowledge_graph_rag_query_engine/)

Hi, how can I help you?

🦙
