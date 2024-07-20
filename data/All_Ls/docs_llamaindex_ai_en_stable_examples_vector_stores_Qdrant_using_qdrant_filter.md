Title: Qdrant Vector Store - Default Qdrant Filters

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/Qdrant_using_qdrant_filters/

Markdown Content:
Qdrant Vector Store - Default Qdrant Filters - LlamaIndex


Example on how to use Filters from the qdrant\_client SDK directly in your Retriever / Query Engine

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-qdrant

%pip install llama-index-vector-stores-qdrant

In \[ \]:

Copied!

!pip3 install llama\-index qdrant\_client

!pip3 install llama-index qdrant\_client

In \[ \]:

Copied!

import openai
import qdrant\_client
from IPython.display import Markdown, display
from llama\_index.core import VectorStoreIndex
from llama\_index.core import StorageContext
from llama\_index.vector\_stores.qdrant import QdrantVectorStore
from qdrant\_client.http.models import Filter, FieldCondition, MatchValue

client \= qdrant\_client.QdrantClient(location\=":memory:")
from llama\_index.core.schema import TextNode

nodes \= \[
    TextNode(
        text\="りんごとは",
        metadata\={"author": "Tanaka", "fruit": "apple", "city": "Tokyo"},
    ),
    TextNode(
        text\="Was ist Apfel?",
        metadata\={"author": "David", "fruit": "apple", "city": "Berlin"},
    ),
    TextNode(
        text\="Orange like the sun",
        metadata\={"author": "Jane", "fruit": "orange", "city": "Hong Kong"},
    ),
    TextNode(
        text\="Grape is...",
        metadata\={"author": "Jane", "fruit": "grape", "city": "Hong Kong"},
    ),
    TextNode(
        text\="T-dot > G-dot",
        metadata\={"author": "George", "fruit": "grape", "city": "Toronto"},
    ),
    TextNode(
        text\="6ix Watermelons",
        metadata\={
            "author": "George",
            "fruit": "watermelon",
            "city": "Toronto",
        },
    ),
\]

openai.api\_key \= "YOUR\_API\_KEY"
vector\_store \= QdrantVectorStore(
    client\=client, collection\_name\="fruit\_collection"
)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex(nodes, storage\_context\=storage\_context)

\# Use filters directly from qdrant\_client python library
\# View python examples here for more info https://qdrant.tech/documentation/concepts/filtering/

filters \= Filter(
    should\=\[
        Filter(
            must\=\[
                FieldCondition(
                    key\="fruit",
                    match\=MatchValue(value\="apple"),
                ),
                FieldCondition(
                    key\="city",
                    match\=MatchValue(value\="Tokyo"),
                ),
            \]
        ),
        Filter(
            must\=\[
                FieldCondition(
                    key\="fruit",
                    match\=MatchValue(value\="grape"),
                ),
                FieldCondition(
                    key\="city",
                    match\=MatchValue(value\="Toronto"),
                ),
            \]
        ),
    \]
)

retriever \= index.as\_retriever(vector\_store\_kwargs\={"qdrant\_filters": filters})

response \= retriever.retrieve("Who makes grapes?")
for node in response:
    print("node", node.score)
    print("node", node.text)
    print("node", node.metadata)

import openai import qdrant\_client from IPython.display import Markdown, display from llama\_index.core import VectorStoreIndex from llama\_index.core import StorageContext from llama\_index.vector\_stores.qdrant import QdrantVectorStore from qdrant\_client.http.models import Filter, FieldCondition, MatchValue client = qdrant\_client.QdrantClient(location=":memory:") from llama\_index.core.schema import TextNode nodes = \[ TextNode( text="りんごとは", metadata={"author": "Tanaka", "fruit": "apple", "city": "Tokyo"}, ), TextNode( text="Was ist Apfel?", metadata={"author": "David", "fruit": "apple", "city": "Berlin"}, ), TextNode( text="Orange like the sun", metadata={"author": "Jane", "fruit": "orange", "city": "Hong Kong"}, ), TextNode( text="Grape is...", metadata={"author": "Jane", "fruit": "grape", "city": "Hong Kong"}, ), TextNode( text="T-dot > G-dot", metadata={"author": "George", "fruit": "grape", "city": "Toronto"}, ), TextNode( text="6ix Watermelons", metadata={ "author": "George", "fruit": "watermelon", "city": "Toronto", }, ), \] openai.api\_key = "YOUR\_API\_KEY" vector\_store = QdrantVectorStore( client=client, collection\_name="fruit\_collection" ) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex(nodes, storage\_context=storage\_context) # Use filters directly from qdrant\_client python library # View python examples here for more info https://qdrant.tech/documentation/concepts/filtering/ filters = Filter( should=\[ Filter( must=\[ FieldCondition( key="fruit", match=MatchValue(value="apple"), ), FieldCondition( key="city", match=MatchValue(value="Tokyo"), ), \] ), Filter( must=\[ FieldCondition( key="fruit", match=MatchValue(value="grape"), ), FieldCondition( key="city", match=MatchValue(value="Toronto"), ), \] ), \] ) retriever = index.as\_retriever(vector\_store\_kwargs={"qdrant\_filters": filters}) response = retriever.retrieve("Who makes grapes?") for node in response: print("node", node.score) print("node", node.text) print("node", node.metadata)

Back to top

[Previous Qdrant Vector Store - Metadata Filter](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Qdrant_metadata_filter/)[Next Redis Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RedisIndexDemo/)
