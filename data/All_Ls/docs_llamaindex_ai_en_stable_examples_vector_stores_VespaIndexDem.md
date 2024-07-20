Title: Vespa Vector Store demo - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/VespaIndexDemo/

Markdown Content:
Vespa Vector Store demo - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-vespa llama\-index pyvespa

%pip install llama-index-vector-stores-vespa llama-index pyvespa

#### Setting up API key[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VespaIndexDemo/#setting-up-api-key)

In \[ \]:

Copied!

import os
import openai

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."
openai.api\_key \= os.environ\["OPENAI\_API\_KEY"\]

import os import openai os.environ\["OPENAI\_API\_KEY"\] = "sk-..." openai.api\_key = os.environ\["OPENAI\_API\_KEY"\]

#### Load documents, build the VectorStoreIndex[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VespaIndexDemo/#load-documents-build-the-vectorstoreindex)

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex
from llama\_index.vector\_stores.vespa import VespaVectorStore
from IPython.display import Markdown, display

from llama\_index.core import VectorStoreIndex from llama\_index.vector\_stores.vespa import VespaVectorStore from IPython.display import Markdown, display

Defining some sample data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VespaIndexDemo/#defining-some-sample-data)
-----------------------------------------------------------------------------------------------------------------------------------

Let's insert some documents.

In \[ \]:

Copied!

from llama\_index.core.schema import TextNode

nodes \= \[
    TextNode(
        text\="The Shawshank Redemption",
        metadata\={
            "author": "Stephen King",
            "theme": "Friendship",
            "year": 1994,
        },
    ),
    TextNode(
        text\="The Godfather",
        metadata\={
            "director": "Francis Ford Coppola",
            "theme": "Mafia",
            "year": 1972,
        },
    ),
    TextNode(
        text\="Inception",
        metadata\={
            "director": "Christopher Nolan",
            "theme": "Fiction",
            "year": 2010,
        },
    ),
    TextNode(
        text\="To Kill a Mockingbird",
        metadata\={
            "author": "Harper Lee",
            "theme": "Mafia",
            "year": 1960,
        },
    ),
    TextNode(
        text\="1984",
        metadata\={
            "author": "George Orwell",
            "theme": "Totalitarianism",
            "year": 1949,
        },
    ),
    TextNode(
        text\="The Great Gatsby",
        metadata\={
            "author": "F. Scott Fitzgerald",
            "theme": "The American Dream",
            "year": 1925,
        },
    ),
    TextNode(
        text\="Harry Potter and the Sorcerer's Stone",
        metadata\={
            "author": "J.K. Rowling",
            "theme": "Fiction",
            "year": 1997,
        },
    ),
\]

from llama\_index.core.schema import TextNode nodes = \[ TextNode( text="The Shawshank Redemption", metadata={ "author": "Stephen King", "theme": "Friendship", "year": 1994, }, ), TextNode( text="The Godfather", metadata={ "director": "Francis Ford Coppola", "theme": "Mafia", "year": 1972, }, ), TextNode( text="Inception", metadata={ "director": "Christopher Nolan", "theme": "Fiction", "year": 2010, }, ), TextNode( text="To Kill a Mockingbird", metadata={ "author": "Harper Lee", "theme": "Mafia", "year": 1960, }, ), TextNode( text="1984", metadata={ "author": "George Orwell", "theme": "Totalitarianism", "year": 1949, }, ), TextNode( text="The Great Gatsby", metadata={ "author": "F. Scott Fitzgerald", "theme": "The American Dream", "year": 1925, }, ), TextNode( text="Harry Potter and the Sorcerer's Stone", metadata={ "author": "J.K. Rowling", "theme": "Fiction", "year": 1997, }, ), \]

### Initilizing the VespaVectorStore[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VespaIndexDemo/#initilizing-the-vespavectorstore)

To make it really simple to get started, we provide a template Vespa application that will be deployed upon initializing the vector store.

This is a huge abstraction and there are endless opportunities to tailor and customize the Vespa application to your needs. But for now, let's keep it simple and initialize with the default template.

In \[ \]:

Copied!

from llama\_index.core import StorageContext

vector\_store \= VespaVectorStore()
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex(nodes, storage\_context\=storage\_context)

from llama\_index.core import StorageContext vector\_store = VespaVectorStore() storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex(nodes, storage\_context=storage\_context)

### Deleting documents[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VespaIndexDemo/#deleting-documents)

In \[ \]:

Copied!

node\_to\_delete \= nodes\[0\].node\_id
node\_to\_delete

node\_to\_delete = nodes\[0\].node\_id node\_to\_delete

In \[ \]:

Copied!

vector\_store.delete(ref\_doc\_id\=node\_to\_delete)

vector\_store.delete(ref\_doc\_id=node\_to\_delete)

Querying[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VespaIndexDemo/#querying)
-------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core.vector\_stores.types import (
    VectorStoreQuery,
    VectorStoreQueryMode,
)

from llama\_index.core.vector\_stores.types import ( VectorStoreQuery, VectorStoreQueryMode, )

In \[ \]:

Copied!

query \= VectorStoreQuery(
    query\_str\="Great Gatsby",
    mode\=VectorStoreQueryMode.TEXT\_SEARCH,
    similarity\_top\_k\=1,
)
result \= vector\_store.query(query)

query = VectorStoreQuery( query\_str="Great Gatsby", mode=VectorStoreQueryMode.TEXT\_SEARCH, similarity\_top\_k=1, ) result = vector\_store.query(query)

In \[ \]:

Copied!

result

result

As retriever[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VespaIndexDemo/#as-retriever)
---------------------------------------------------------------------------------------------------------

### Default query mode (text search)[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VespaIndexDemo/#default-query-mode-text-search)

In \[ \]:

Copied!

retriever \= index.as\_retriever(vector\_store\_query\_mode\="default")
results \= retriever.retrieve("Who directed inception?")
display(Markdown(f"\*\*Retrieved nodes:\*\*\\n {results}"))

retriever = index.as\_retriever(vector\_store\_query\_mode="default") results = retriever.retrieve("Who directed inception?") display(Markdown(f"\*\*Retrieved nodes:\*\*\\n {results}"))

In \[ \]:

Copied!

retriever \= index.as\_retriever(vector\_store\_query\_mode\="semantic\_hybrid")
results \= retriever.retrieve("Who wrote Harry Potter?")
display(Markdown(f"\*\*Retrieved nodes:\*\*\\n {results}"))

retriever = index.as\_retriever(vector\_store\_query\_mode="semantic\_hybrid") results = retriever.retrieve("Who wrote Harry Potter?") display(Markdown(f"\*\*Retrieved nodes:\*\*\\n {results}"))

### As query engine[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VespaIndexDemo/#as-query-engine)

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("Who directed inception?")
display(Markdown(f"\*\*Response:\*\* {response}"))

query\_engine = index.as\_query\_engine() response = query\_engine.query("Who directed inception?") display(Markdown(f"\*\*Response:\*\* {response}"))

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(
    vector\_store\_query\_mode\="semantic\_hybrid", verbose\=True
)
response \= query\_engine.query(
    "When was the book about the wizard boy published and what was it called?"
)
display(Markdown(f"\*\*Response:\*\* {response}"))
display(Markdown(f"\*\*Sources:\*\* {response.source\_nodes}"))

query\_engine = index.as\_query\_engine( vector\_store\_query\_mode="semantic\_hybrid", verbose=True ) response = query\_engine.query( "When was the book about the wizard boy published and what was it called?" ) display(Markdown(f"\*\*Response:\*\* {response}")) display(Markdown(f"\*\*Sources:\*\* {response.source\_nodes}"))

Using metadata filters[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VespaIndexDemo/#using-metadata-filters)
-----------------------------------------------------------------------------------------------------------------------------

**NOTE**: This metadata filtering is done by llama-index, outside of vespa. For native and much more performant filtering, you should use Vespa's own filtering capabilities.

See [Vespa's documentation](https://docs.vespa.ai/en/reference/query-language-reference.html) for more information.

In \[ \]:

Copied!

from llama\_index.core.vector\_stores import (
    FilterOperator,
    FilterCondition,
    MetadataFilter,
    MetadataFilters,
)

\# Let's define a filter that will only allow nodes that has the theme "Fiction" OR is published after 1997

filters \= MetadataFilters(
    filters\=\[
        MetadataFilter(key\="theme", value\="Fiction"),
        MetadataFilter(key\="year", value\=1997, operator\=FilterOperator.GT),
    \],
    condition\=FilterCondition.OR,
)

retriever \= index.as\_retriever(filters\=filters)
result \= retriever.retrieve("Harry Potter")
display(Markdown(f"\*\*Result:\*\* {result}"))

from llama\_index.core.vector\_stores import ( FilterOperator, FilterCondition, MetadataFilter, MetadataFilters, ) # Let's define a filter that will only allow nodes that has the theme "Fiction" OR is published after 1997 filters = MetadataFilters( filters=\[ MetadataFilter(key="theme", value="Fiction"), MetadataFilter(key="year", value=1997, operator=FilterOperator.GT), \], condition=FilterCondition.OR, ) retriever = index.as\_retriever(filters=filters) result = retriever.retrieve("Harry Potter") display(Markdown(f"\*\*Result:\*\* {result}"))

Abstraction level of this integration[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VespaIndexDemo/#abstraction-level-of-this-integration)
-----------------------------------------------------------------------------------------------------------------------------------------------------------

To make it really simple to get started, we provide a template Vespa application that will be deployed upon initializing the vector store. This removes some of the complexity of setting up Vespa for the first time, but for serious use cases, we strongly recommend that you read the [Vespa documentation](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VespaIndexDemo/docs.vespa.ai) and tailor the application to your needs.

### The template[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VespaIndexDemo/#the-template)

The provided template Vespa application can be seen below:

from vespa.package import (
    ApplicationPackage,
    Field,
    Schema,
    Document,
    HNSW,
    RankProfile,
    Component,
    Parameter,
    FieldSet,
    GlobalPhaseRanking,
    Function,
)

hybrid\_template \= ApplicationPackage(
    name\="hybridsearch",
    schema\=\[
        Schema(
            name\="doc",
            document\=Document(
                fields\=\[
                    Field(name\="id", type\="string", indexing\=\["summary"\]),
                    Field(name\="metadata", type\="string", indexing\=\["summary"\]),
                    Field(
                        name\="text",
                        type\="string",
                        indexing\=\["index", "summary"\],
                        index\="enable-bm25",
                        bolding\=True,
                    ),
                    Field(
                        name\="embedding",
                        type\="tensor<float>(x\[384\])",
                        indexing\=\[
                            "input text",
                            "embed",
                            "index",
                            "attribute",
                        \],
                        ann\=HNSW(distance\_metric\="angular"),
                        is\_document\_field\=False,
                    ),
                \]
            ),
            fieldsets\=\[FieldSet(name\="default", fields\=\["text", "metadata"\])\],
            rank\_profiles\=\[
                RankProfile(
                    name\="bm25",
                    inputs\=\[("query(q)", "tensor<float>(x\[384\])")\],
                    functions\=\[Function(name\="bm25sum", expression\="bm25(text)")\],
                    first\_phase\="bm25sum",
                ),
                RankProfile(
                    name\="semantic",
                    inputs\=\[("query(q)", "tensor<float>(x\[384\])")\],
                    first\_phase\="closeness(field, embedding)",
                ),
                RankProfile(
                    name\="fusion",
                    inherits\="bm25",
                    inputs\=\[("query(q)", "tensor<float>(x\[384\])")\],
                    first\_phase\="closeness(field, embedding)",
                    global\_phase\=GlobalPhaseRanking(
                        expression\="reciprocal\_rank\_fusion(bm25sum, closeness(field, embedding))",
                        rerank\_count\=1000,
                    ),
                ),
            \],
        )
    \],
    components\=\[
        Component(
            id\="e5",
            type\="hugging-face-embedder",
            parameters\=\[
                Parameter(
                    "transformer-model",
                    {
                        "url": "https://github.com/vespa-engine/sample-apps/raw/master/simple-semantic-search/model/e5-small-v2-int8.onnx"
                    },
                ),
                Parameter(
                    "tokenizer-model",
                    {
                        "url": "https://raw.githubusercontent.com/vespa-engine/sample-apps/master/simple-semantic-search/model/tokenizer.json"
                    },
                ),
            \],
        )
    \],
)

Note that the fields `id`, `metadata`, `text`, and `embedding` are required for the integration to work. The schema name must also be `doc`, and the rank profiles must be named `bm25`, `semantic`, and `fusion`.

Other than that you are free to modify as you see fit by switching out embedding models, adding more fields, or changing the ranking expressions.

For more details, check out this Pyvespa example notebook on [hybrid search](https://pyvespa.readthedocs.io/en/latest/getting-started-pyvespa.html).

Back to top

[Previous Google Vertex AI Vector Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VertexAIVectorSearchDemo/)[Next Weaviate Vector Store - Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo-Hybrid/)
