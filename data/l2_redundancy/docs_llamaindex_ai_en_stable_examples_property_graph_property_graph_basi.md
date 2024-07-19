Title: Property Graph Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_basic/

Markdown Content:
Property Graph Index - LlamaIndex


[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/docs/examples/property_graph/property_graph_basic.ipynb)

In this notebook, we demonstrate some basic usage of the `PropertyGraphIndex` in LlamaIndex.

The property graph index here will take unstructured documents, extract a property graph from it, and provide various methods to query that graph.

In \[ \]:

Copied!

%pip install llama\-index

%pip install llama-index

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_basic/#setup)
--------------------------------------------------------------------------------------------------

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

Construction[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_basic/#construction)
----------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core import PropertyGraphIndex
from llama\_index.embeddings.openai import OpenAIEmbedding
from llama\_index.llms.openai import OpenAI

index \= PropertyGraphIndex.from\_documents(
    documents,
    llm\=OpenAI(model\="gpt-3.5-turbo", temperature\=0.3),
    embed\_model\=OpenAIEmbedding(model\_name\="text-embedding-3-small"),
    show\_progress\=True,
)

from llama\_index.core import PropertyGraphIndex from llama\_index.embeddings.openai import OpenAIEmbedding from llama\_index.llms.openai import OpenAI index = PropertyGraphIndex.from\_documents( documents, llm=OpenAI(model="gpt-3.5-turbo", temperature=0.3), embed\_model=OpenAIEmbedding(model\_name="text-embedding-3-small"), show\_progress=True, )

/Users/loganmarkewich/Library/Caches/pypoetry/virtualenvs/llama-index-bXUwlEfH-py3.11/lib/python3.11/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user\_install.html
  from .autonotebook import tqdm as notebook\_tqdm
Parsing nodes: 100%|██████████| 1/1 \[00:00<00:00, 25.46it/s\]
Extracting paths from text: 100%|██████████| 22/22 \[00:12<00:00,  1.72it/s\]
Extracting implicit paths: 100%|██████████| 22/22 \[00:00<00:00, 36186.15it/s\]
Generating embeddings: 100%|██████████| 1/1 \[00:00<00:00,  1.14it/s\]
Generating embeddings: 100%|██████████| 5/5 \[00:00<00:00,  5.43it/s\]

So lets recap what exactly just happened

*   `PropertyGraphIndex.from_documents()` - we loaded documents into an index
*   `Parsing nodes` - the index parsed the documents into nodes
*   `Extracting paths from text` - the nodes were passed to an LLM, and the LLM was prompted to generate knowledge graph triples (i.e. paths)
*   `Extracting implicit paths` - each `node.relationships` property was used to infer implicit paths
*   `Generating embeddings` - embeddings were generated for each text node and graph node (hence this happens twice)

Lets explore what we created! For debugging purposes, the default `SimplePropertyGraphStore` includes a helper to save a `networkx` representation of the graph to an `html` file.

In \[ \]:

Copied!

index.property\_graph\_store.save\_networkx\_graph(name\="./kg.html")

index.property\_graph\_store.save\_networkx\_graph(name="./kg.html")

Opening the html in a browser, we can see our graph!

If you zoom in, each "dense" node with many connections is actually the source chunk, with extracted entities and relations branching off from there.

![Image 4: example graph](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_basic/kg_screenshot.png)

Customizing Low-Level Construction[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_basic/#customizing-low-level-construction)
------------------------------------------------------------------------------------------------------------------------------------------------------------

If we wanted, we can do the same ingestion using the low-level API, leverage `kg_extractors`.

In \[ \]:

Copied!

from llama\_index.core.indices.property\_graph import (
    ImplicitPathExtractor,
    SimpleLLMPathExtractor,
)

index \= PropertyGraphIndex.from\_documents(
    documents,
    embed\_model\=OpenAIEmbedding(model\_name\="text-embedding-3-small"),
    kg\_extractors\=\[
        ImplicitPathExtractor(),
        SimpleLLMPathExtractor(
            llm\=OpenAI(model\="gpt-3.5-turbo", temperature\=0.3),
            num\_workers\=4,
            max\_paths\_per\_chunk\=10,
        ),
    \],
    show\_progress\=True,
)

from llama\_index.core.indices.property\_graph import ( ImplicitPathExtractor, SimpleLLMPathExtractor, ) index = PropertyGraphIndex.from\_documents( documents, embed\_model=OpenAIEmbedding(model\_name="text-embedding-3-small"), kg\_extractors=\[ ImplicitPathExtractor(), SimpleLLMPathExtractor( llm=OpenAI(model="gpt-3.5-turbo", temperature=0.3), num\_workers=4, max\_paths\_per\_chunk=10, ), \], show\_progress=True, )

For a full guide on all extractors, see the [detailed usage page](https://docs.llamaindex.ai/en/stable/examples/module_guides/indexing/lpg_index_guide.md#construction).

Querying[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_basic/#querying)
--------------------------------------------------------------------------------------------------------

Querying a property graph index typically consists of using one or more sub-retrievers and combining results.

Graph retrieval can be thought of

*   selecting node(s)
*   traversing from those nodes

By default, two types of retrieval are used in unison

*   synoynm/keyword expansion - use the LLM to generate synonyms and keywords from the query
*   vector retrieval - use embeddings to find nodes in your graph

Once nodes are found, you can either

*   return the paths adjacent to the selected nodes (i.e. triples)
*   return the paths + the original source text of the chunk (if available)

In \[ \]:

Copied!

retriever \= index.as\_retriever(
    include\_text\=False,  \# include source text, default True
)

nodes \= retriever.retrieve("What happened at Interleaf and Viaweb?")

for node in nodes:
    print(node.text)

retriever = index.as\_retriever( include\_text=False, # include source text, default True ) nodes = retriever.retrieve("What happened at Interleaf and Viaweb?") for node in nodes: print(node.text)

Interleaf -> Was -> On the way down
Viaweb -> Had -> Code editor
Interleaf -> Built -> Impressive technology
Interleaf -> Added -> Scripting language
Interleaf -> Made -> Scripting language
Viaweb -> Suggested -> Take to hospital
Interleaf -> Had done -> Something bold
Viaweb -> Called -> After
Interleaf -> Made -> Dialect of lisp
Interleaf -> Got crushed by -> Moore's law
Dan giffin -> Worked for -> Viaweb
Interleaf -> Had -> Smart people
Interleaf -> Had -> Few years to live
Interleaf -> Made -> Software
Interleaf -> Made -> Software for creating documents
Paul graham -> Started -> Viaweb
Scripting language -> Was -> Dialect of lisp
Scripting language -> Is -> Dialect of lisp
Software -> Will be affected by -> Rapid change
Code editor -> Was -> In viaweb
Software -> Worked via -> Web
Programs -> Typed on -> Punch cards
Computers -> Skipped -> Step
Idea -> Was clear from -> Experience
Apartment -> Wasn't -> Rent-controlled

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(
    include\_text\=True,
)

response \= query\_engine.query("What happened at Interleaf and Viaweb?")

print(str(response))

query\_engine = index.as\_query\_engine( include\_text=True, ) response = query\_engine.query("What happened at Interleaf and Viaweb?") print(str(response))

Interleaf had smart people and built impressive technology, including adding a scripting language that was a dialect of Lisp. However, despite their efforts, they were eventually impacted by Moore's Law and faced challenges. Viaweb, on the other hand, was started by Paul Graham and had a code editor where users could define their own page styles using Lisp expressions. Viaweb also suggested taking someone to the hospital and called something "After."

For full details on customizing retrieval and querying, see [the docs page](https://docs.llamaindex.ai/en/stable/examples/module_guides/indexing/lpg_index_guide.md#retrieval-and-querying).

Storage[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_basic/#storage)
------------------------------------------------------------------------------------------------------

By default, storage happens using our simple in-memory abstractions - `SimpleVectorStore` for embeddings and `SimplePropertyGraphStore` for the property graph.

We can save and load these to/from disk.

In \[ \]:

Copied!

index.storage\_context.persist(persist\_dir\="./storage")

from llama\_index.core import StorageContext, load\_index\_from\_storage

index \= load\_index\_from\_storage(
    StorageContext.from\_defaults(persist\_dir\="./storage")
)

index.storage\_context.persist(persist\_dir="./storage") from llama\_index.core import StorageContext, load\_index\_from\_storage index = load\_index\_from\_storage( StorageContext.from\_defaults(persist\_dir="./storage") )

### Vector Stores[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_basic/#vector-stores)

While some graph databases support vectors (like Neo4j), you can still specify the vector store to use on top of your graph for cases where its not supported, or cases where you want to override.

Below we will combine `ChromaVectorStore` with the default `SimplePropertyGraphStore`.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-chroma

%pip install llama-index-vector-stores-chroma

In \[ \]:

Copied!

from llama\_index.core.graph\_stores import SimplePropertyGraphStore
from llama\_index.vector\_stores.chroma import ChromaVectorStore
import chromadb

client \= chromadb.PersistentClient("./chroma\_db")
collection \= client.get\_or\_create\_collection("my\_graph\_vector\_db")

index \= PropertyGraphIndex.from\_documents(
    documents,
    embed\_model\=OpenAIEmbedding(model\_name\="text-embedding-3-small"),
    graph\_store\=SimplePropertyGraphStore(),
    vector\_store\=ChromaVectorStore(collection\=collection),
    show\_progress\=True,
)

index.storage\_context.persist(persist\_dir\="./storage")

from llama\_index.core.graph\_stores import SimplePropertyGraphStore from llama\_index.vector\_stores.chroma import ChromaVectorStore import chromadb client = chromadb.PersistentClient("./chroma\_db") collection = client.get\_or\_create\_collection("my\_graph\_vector\_db") index = PropertyGraphIndex.from\_documents( documents, embed\_model=OpenAIEmbedding(model\_name="text-embedding-3-small"), graph\_store=SimplePropertyGraphStore(), vector\_store=ChromaVectorStore(collection=collection), show\_progress=True, ) index.storage\_context.persist(persist\_dir="./storage")

Then to load:

In \[ \]:

Copied!

index \= PropertyGraphIndex.from\_existing(
    SimplePropertyGraphStore.from\_persist\_dir("./storage"),
    vector\_store\=ChromaVectorStore(chroma\_collection\=collection),
    llm\=OpenAI(model\="gpt-3.5-turbo", temperature\=0.3),
)

index = PropertyGraphIndex.from\_existing( SimplePropertyGraphStore.from\_persist\_dir("./storage"), vector\_store=ChromaVectorStore(chroma\_collection=collection), llm=OpenAI(model="gpt-3.5-turbo", temperature=0.3), )

This looks slightly different than purely using the storage context, but the syntax is more concise now that we've started to mix things together.

Back to top

[Previous Property Graph Construction with Predefined Schemas](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_advanced/)[Next Defining a Custom Property Graph Retriever](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_custom_retriever/)

Hi, how can I help you?

🦙
