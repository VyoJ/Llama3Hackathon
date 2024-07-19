Title: Defining a Custom Property Graph Retriever

URL Source: https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_custom_retriever/

Markdown Content:
Defining a Custom Property Graph Retriever - LlamaIndex


[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/docs/examples/property_graph/property_graph_custom_retriever.ipynb)

This guide shows you how to define a custom retriever against a property graph.

It is more involved than using our out-of-the-box graph retrievers, but allows you to have granular control over the retrieval process so that it's better tailored for your application.

We show you how to define an advanced retrieval flow by directly leveraging the property graph store. We'll execute both vector search and text-to-cypher retrieval, and then combine the results through a reranking module.

In \[ \]:

Copied!

%pip install llama\-index
%pip install llama\-index\-graph\-stores\-neo4j
%pip install llama\-index\-postprocessor\-cohere\-rerank

%pip install llama-index %pip install llama-index-graph-stores-neo4j %pip install llama-index-postprocessor-cohere-rerank

Setup and Build the Property Graph[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_custom_retriever/#setup-and-build-the-property-graph)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

import nest\_asyncio

nest\_asyncio.apply()

import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..."

#### Load Paul Graham Essay[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_custom_retriever/#load-paul-graham-essay)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

from llama\_index.core import SimpleDirectoryReader documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data()

/Users/loganmarkewich/Library/Caches/pypoetry/virtualenvs/llama-index-bXUwlEfH-py3.11/lib/python3.11/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user\_install.html
  from .autonotebook import tqdm as notebook\_tqdm

#### Define Default LLMs[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_custom_retriever/#define-default-llms)

In \[ \]:

Copied!

from llama\_index.embeddings.openai import OpenAIEmbedding
from llama\_index.llms.openai import OpenAI

llm \= OpenAI(model\="gpt-3.5-turbo", temperature\=0.3)
embed\_model \= OpenAIEmbedding(model\_name\="text-embedding-3-small")

from llama\_index.embeddings.openai import OpenAIEmbedding from llama\_index.llms.openai import OpenAI llm = OpenAI(model="gpt-3.5-turbo", temperature=0.3) embed\_model = OpenAIEmbedding(model\_name="text-embedding-3-small")

/Users/loganmarkewich/Library/Caches/pypoetry/virtualenvs/llama-index-bXUwlEfH-py3.11/lib/python3.11/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user\_install.html
  from .autonotebook import tqdm as notebook\_tqdm

#### Setup Neo4j[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_custom_retriever/#setup-neo4j)

To launch Neo4j locally, first ensure you have docker installed. Then, you can launch the database with the following docker command

```
docker run \
    -p 7474:7474 -p 7687:7687 \
    -v $PWD/data:/data -v $PWD/plugins:/plugins \
    --name neo4j-apoc \
    -e NEO4J_apoc_export_file_enabled=true \
    -e NEO4J_apoc_import_file_enabled=true \
    -e NEO4J_apoc_import_file_use__neo4j__config=true \
    -e NEO4JLABS_PLUGINS=\[\"apoc\"\] \
    neo4j:latest

```

From here, you can open the db at [http://localhost:7474/](http://localhost:7474/). On this page, you will be asked to sign in. Use the default username/password of neo4j and neo4j.

In \[ \]:

Copied!

from llama\_index.graph\_stores.neo4j import Neo4jPropertyGraphStore

graph\_store \= Neo4jPropertyGraphStore(
    username\="neo4j",
    password\="llamaindex",
    url\="bolt://localhost:7687",
)

from llama\_index.graph\_stores.neo4j import Neo4jPropertyGraphStore graph\_store = Neo4jPropertyGraphStore( username="neo4j", password="llamaindex", url="bolt://localhost:7687", )

#### Build the Property Graph[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_custom_retriever/#build-the-property-graph)

In \[ \]:

Copied!

from llama\_index.core import PropertyGraphIndex

index \= PropertyGraphIndex.from\_documents(
    documents,
    llm\=llm,
    embed\_model\=embed\_model,
    property\_graph\_store\=graph\_store,
    show\_progress\=True,
)

from llama\_index.core import PropertyGraphIndex index = PropertyGraphIndex.from\_documents( documents, llm=llm, embed\_model=embed\_model, property\_graph\_store=graph\_store, show\_progress=True, )

Define Custom Retriever[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_custom_retriever/#define-custom-retriever)
-------------------------------------------------------------------------------------------------------------------------------------------------

Now we define a custom retriever by subclassing `CustomPGRetriever`.

#### 1\. Initialization[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_custom_retriever/#1-initialization)

We initialize two pre-existing property graph retrievers: the `VectorContextRetriever` and the `TextToCypherRetriever`, as well as the cohere reranker.

#### 2\. Define `custom_retrieve`[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_custom_retriever/#2-define-custom_retrieve)

We then define the `custom_retrieve` function. It passes nodes through the two retrievers and gets back a final ranked list.

The return type here can be a string, `TextNode`, `NodeWithScore`, or a list of one of those types.

In \[ \]:

Copied!

from llama\_index.core.retrievers import (
    CustomPGRetriever,
    VectorContextRetriever,
    TextToCypherRetriever,
)
from llama\_index.core.graph\_stores import PropertyGraphStore
from llama\_index.core.vector\_stores.types import VectorStore
from llama\_index.core.embeddings import BaseEmbedding
from llama\_index.core.prompts import PromptTemplate
from llama\_index.core.llms import LLM
from llama\_index.postprocessor.cohere\_rerank import CohereRerank

from typing import Optional, Any, Union

class MyCustomRetriever(CustomPGRetriever):
    """Custom retriever with cohere reranking."""

    def init(
        self,
        \## vector context retriever params
        embed\_model: Optional\[BaseEmbedding\] \= None,
        vector\_store: Optional\[VectorStore\] \= None,
        similarity\_top\_k: int \= 4,
        path\_depth: int \= 1,
        \## text-to-cypher params
        llm: Optional\[LLM\] \= None,
        text\_to\_cypher\_template: Optional\[Union\[PromptTemplate, str\]\] \= None,
        \## cohere reranker params
        cohere\_api\_key: Optional\[str\] \= None,
        cohere\_top\_n: int \= 2,
        \*\*kwargs: Any,
    ) \-> None:
        """Uses any kwargs passed in from class constructor."""

        self.vector\_retriever \= VectorContextRetriever(
            self.graph\_store,
            include\_text\=self.include\_text,
            embed\_model\=embed\_model,
            vector\_store\=vector\_store,
            similarity\_top\_k\=similarity\_top\_k,
            path\_depth\=path\_depth,
        )

        self.cypher\_retriever \= TextToCypherRetriever(
            self.graph\_store,
            llm\=llm,
            text\_to\_cypher\_template\=text\_to\_cypher\_template
            \## NOTE: you can attach other parameters here if you'd like
        )

        self.reranker \= CohereRerank(
            api\_key\=cohere\_api\_key, top\_n\=cohere\_top\_n
        )

    def custom\_retrieve(self, query\_str: str) \-> str:
        """Define custom retriever with reranking.

        Could return \`str\`, \`TextNode\`, \`NodeWithScore\`, or a list of those.
        """
        nodes\_1 \= self.vector\_retriever.retrieve(query\_str)
        nodes\_2 \= self.cypher\_retriever.retrieve(query\_str)
        reranked\_nodes \= self.reranker.postprocess\_nodes(
            nodes\_1 + nodes\_2, query\_str\=query\_str
        )

        \## TMP: please change
        final\_text \= "\\n\\n".join(
            \[n.get\_content(metadata\_mode\="llm") for n in reranked\_nodes\]
        )

        return final\_text

    \# optional async method
    \# async def acustom\_retrieve(self, query\_str: str) -> str:
    \#     ...

from llama\_index.core.retrievers import ( CustomPGRetriever, VectorContextRetriever, TextToCypherRetriever, ) from llama\_index.core.graph\_stores import PropertyGraphStore from llama\_index.core.vector\_stores.types import VectorStore from llama\_index.core.embeddings import BaseEmbedding from llama\_index.core.prompts import PromptTemplate from llama\_index.core.llms import LLM from llama\_index.postprocessor.cohere\_rerank import CohereRerank from typing import Optional, Any, Union class MyCustomRetriever(CustomPGRetriever): """Custom retriever with cohere reranking.""" def init( self, ## vector context retriever params embed\_model: Optional\[BaseEmbedding\] = None, vector\_store: Optional\[VectorStore\] = None, similarity\_top\_k: int = 4, path\_depth: int = 1, ## text-to-cypher params llm: Optional\[LLM\] = None, text\_to\_cypher\_template: Optional\[Union\[PromptTemplate, str\]\] = None, ## cohere reranker params cohere\_api\_key: Optional\[str\] = None, cohere\_top\_n: int = 2, \*\*kwargs: Any, ) -> None: """Uses any kwargs passed in from class constructor.""" self.vector\_retriever = VectorContextRetriever( self.graph\_store, include\_text=self.include\_text, embed\_model=embed\_model, vector\_store=vector\_store, similarity\_top\_k=similarity\_top\_k, path\_depth=path\_depth, ) self.cypher\_retriever = TextToCypherRetriever( self.graph\_store, llm=llm, text\_to\_cypher\_template=text\_to\_cypher\_template ## NOTE: you can attach other parameters here if you'd like ) self.reranker = CohereRerank( api\_key=cohere\_api\_key, top\_n=cohere\_top\_n ) def custom\_retrieve(self, query\_str: str) -> str: """Define custom retriever with reranking. Could return \`str\`, \`TextNode\`, \`NodeWithScore\`, or a list of those. """ nodes\_1 = self.vector\_retriever.retrieve(query\_str) nodes\_2 = self.cypher\_retriever.retrieve(query\_str) reranked\_nodes = self.reranker.postprocess\_nodes( nodes\_1 + nodes\_2, query\_str=query\_str ) ## TMP: please change final\_text = "\\n\\n".join( \[n.get\_content(metadata\_mode="llm") for n in reranked\_nodes\] ) return final\_text # optional async method # async def acustom\_retrieve(self, query\_str: str) -> str: # ...

Test out the Custom Retriever[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_custom_retriever/#test-out-the-custom-retriever)
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Now let's initialize and test out the custom retriever against our data!

To build a full RAG pipeline, we use the `RetrieverQueryEngine` to combine our retriever with the LLM synthesis module - this is also used under the hood for the property graph index.

In \[ \]:

Copied!

custom\_sub\_retriever \= MyCustomRetriever(
    index.property\_graph\_store,
    include\_text\=True,
    vector\_store\=index.vector\_store,
    cohere\_api\_key\="...",
)

custom\_sub\_retriever = MyCustomRetriever( index.property\_graph\_store, include\_text=True, vector\_store=index.vector\_store, cohere\_api\_key="...", )

In \[ \]:

Copied!

from llama\_index.core.query\_engine import RetrieverQueryEngine

query\_engine \= RetrieverQueryEngine.from\_args(
    index.as\_retriever(sub\_retrievers\=\[custom\_sub\_retriever\]), llm\=llm
)

from llama\_index.core.query\_engine import RetrieverQueryEngine query\_engine = RetrieverQueryEngine.from\_args( index.as\_retriever(sub\_retrievers=\[custom\_sub\_retriever\]), llm=llm )

#### Try out a 'baseline'[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_custom_retriever/#try-out-a-baseline)

We compare against a baseline retriever that's the vector context only.

In \[ \]:

Copied!

base\_retriever \= VectorContextRetriever(
    index.property\_graph\_store, include\_text\=True
)
base\_query\_engine \= index.as\_query\_engine(sub\_retrievers\=\[base\_retriever\])

base\_retriever = VectorContextRetriever( index.property\_graph\_store, include\_text=True ) base\_query\_engine = index.as\_query\_engine(sub\_retrievers=\[base\_retriever\])

### Try out some Queries[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_custom_retriever/#try-out-some-queries)

In \[ \]:

Copied!

response \= query\_engine.query("Did the author like programming?")
print(str(response))

response = query\_engine.query("Did the author like programming?") print(str(response))

The author found working on programming challenging but satisfying, as indicated by the intense effort put into the project and the sense of accomplishment derived from solving complex problems while working on the code.

In \[ \]:

Copied!

response \= base\_query\_engine.query("Did the author like programming?")
print(str(response))

response = base\_query\_engine.query("Did the author like programming?") print(str(response))

The author enjoyed programming, as evidenced by their early experiences with computers, such as writing simple games, creating programs for predicting rocket flights, and developing a word processor. These experiences indicate a genuine interest and enjoyment in programming activities.

Back to top

[Previous Property Graph Index](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_basic/)[Next Neo4j Property Graph Index](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_neo4j/)

Hi, how can I help you?

🦙
