Title: Composable Objects - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/retrievers/composable_retrievers/

Markdown Content:
Composable Objects - LlamaIndex


In this notebook, we show how you can combine multiple objects into a single top-level index.

This approach works by setting up `IndexNode` objects, with an `obj` field that points to a:

*   query engine
*   retriever
*   query pipeline
*   another node!

object \= IndexNode(index\_id\="my\_object", obj\=query\_engine, text\="some text about this object")

Data Setup[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/composable_retrievers/#data-setup)
---------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

%pip install llama\-index\-storage\-docstore\-mongodb
%pip install llama\-index\-vector\-stores\-qdrant
%pip install llama\-index\-storage\-docstore\-firestore
%pip install llama\-index\-retrievers\-bm25
%pip install llama\-index\-storage\-docstore\-redis
%pip install llama\-index\-storage\-docstore\-dynamodb
%pip install llama\-index\-readers\-file pymupdf

%pip install llama-index-storage-docstore-mongodb %pip install llama-index-vector-stores-qdrant %pip install llama-index-storage-docstore-firestore %pip install llama-index-retrievers-bm25 %pip install llama-index-storage-docstore-redis %pip install llama-index-storage-docstore-dynamodb %pip install llama-index-readers-file pymupdf

In \[ \]:

Copied!

!wget \--user\-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" \-O "./llama2.pdf"
!wget \--user\-agent "Mozilla" "https://arxiv.org/pdf/1706.03762.pdf" \-O "./attention.pdf"

!wget --user-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" -O "./llama2.pdf" !wget --user-agent "Mozilla" "https://arxiv.org/pdf/1706.03762.pdf" -O "./attention.pdf"

In \[ \]:

Copied!

from llama\_index.core import download\_loader

from llama\_index.readers.file import PyMuPDFReader

llama2\_docs \= PyMuPDFReader().load\_data(
    file\_path\="./llama2.pdf", metadata\=True
)
attention\_docs \= PyMuPDFReader().load\_data(
    file\_path\="./attention.pdf", metadata\=True
)

from llama\_index.core import download\_loader from llama\_index.readers.file import PyMuPDFReader llama2\_docs = PyMuPDFReader().load\_data( file\_path="./llama2.pdf", metadata=True ) attention\_docs = PyMuPDFReader().load\_data( file\_path="./attention.pdf", metadata=True )

Retriever Setup[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/composable_retrievers/#retriever-setup)
-------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..."

In \[ \]:

Copied!

from llama\_index.core.node\_parser import TokenTextSplitter

nodes \= TokenTextSplitter(
    chunk\_size\=1024, chunk\_overlap\=128
).get\_nodes\_from\_documents(llama2\_docs + attention\_docs)

from llama\_index.core.node\_parser import TokenTextSplitter nodes = TokenTextSplitter( chunk\_size=1024, chunk\_overlap=128 ).get\_nodes\_from\_documents(llama2\_docs + attention\_docs)

In \[ \]:

Copied!

from llama\_index.core.storage.docstore import SimpleDocumentStore
from llama\_index.storage.docstore.redis import RedisDocumentStore
from llama\_index.storage.docstore.mongodb import MongoDocumentStore
from llama\_index.storage.docstore.firestore import FirestoreDocumentStore
from llama\_index.storage.docstore.dynamodb import DynamoDBDocumentStore

docstore \= SimpleDocumentStore()
docstore.add\_documents(nodes)

from llama\_index.core.storage.docstore import SimpleDocumentStore from llama\_index.storage.docstore.redis import RedisDocumentStore from llama\_index.storage.docstore.mongodb import MongoDocumentStore from llama\_index.storage.docstore.firestore import FirestoreDocumentStore from llama\_index.storage.docstore.dynamodb import DynamoDBDocumentStore docstore = SimpleDocumentStore() docstore.add\_documents(nodes)

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, StorageContext
from llama\_index.retrievers.bm25 import BM25Retriever
from llama\_index.vector\_stores.qdrant import QdrantVectorStore
from qdrant\_client import QdrantClient

client \= QdrantClient(path\="./qdrant\_data")
vector\_store \= QdrantVectorStore("composable", client\=client)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

index \= VectorStoreIndex(nodes\=nodes)
vector\_retriever \= index.as\_retriever(similarity\_top\_k\=2)
bm25\_retriever \= BM25Retriever.from\_defaults(
    docstore\=docstore, similarity\_top\_k\=2
)

from llama\_index.core import VectorStoreIndex, StorageContext from llama\_index.retrievers.bm25 import BM25Retriever from llama\_index.vector\_stores.qdrant import QdrantVectorStore from qdrant\_client import QdrantClient client = QdrantClient(path="./qdrant\_data") vector\_store = QdrantVectorStore("composable", client=client) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex(nodes=nodes) vector\_retriever = index.as\_retriever(similarity\_top\_k=2) bm25\_retriever = BM25Retriever.from\_defaults( docstore=docstore, similarity\_top\_k=2 )

Composing Objects[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/composable_retrievers/#composing-objects)
-----------------------------------------------------------------------------------------------------------------------

Here, we construct the `IndexNodes`. Note that the text is what is used to index the node by the top-level index.

For a vector index, the text is embedded, for a keyword index, the text is used for keywords.

In this example, the `SummaryIndex` is used, which does not technically need the text for retrieval, since it always retrieves all nodes.

In \[ \]:

Copied!

from llama\_index.core.schema import IndexNode

vector\_obj \= IndexNode(
    index\_id\="vector", obj\=vector\_retriever, text\="Vector Retriever"
)
bm25\_obj \= IndexNode(
    index\_id\="bm25", obj\=bm25\_retriever, text\="BM25 Retriever"
)

from llama\_index.core.schema import IndexNode vector\_obj = IndexNode( index\_id="vector", obj=vector\_retriever, text="Vector Retriever" ) bm25\_obj = IndexNode( index\_id="bm25", obj=bm25\_retriever, text="BM25 Retriever" )

In \[ \]:

Copied!

from llama\_index.core import SummaryIndex

summary\_index \= SummaryIndex(objects\=\[vector\_obj, bm25\_obj\])

from llama\_index.core import SummaryIndex summary\_index = SummaryIndex(objects=\[vector\_obj, bm25\_obj\])

Querying[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/composable_retrievers/#querying)
-----------------------------------------------------------------------------------------------------

When we query, all objects will be retrieved and used to generate the nodes to get a final answer.

Using `tree_summarize` with `aquery()` ensures concurrent execution and faster responses.

In \[ \]:

Copied!

query\_engine \= summary\_index.as\_query\_engine(
    response\_mode\="tree\_summarize", verbose\=True
)

query\_engine = summary\_index.as\_query\_engine( response\_mode="tree\_summarize", verbose=True )

In \[ \]:

Copied!

response \= await query\_engine.aquery(
    "How does attention work in transformers?"
)

response = await query\_engine.aquery( "How does attention work in transformers?" )

Retrieval entering vector: VectorIndexRetriever
Retrieval entering bm25: BM25Retriever

In \[ \]:

Copied!

print(str(response))

print(str(response))

Attention in transformers works by mapping a query and a set of key-value pairs to an output. The output is computed as a weighted sum of the values, where the weights are determined by the similarity between the query and the keys. In the transformer model, attention is used in three different ways: 

1. Encoder-decoder attention: The queries come from the previous decoder layer, and the memory keys and values come from the output of the encoder. This allows every position in the decoder to attend over all positions in the input sequence.

2. Self-attention in the encoder: In a self-attention layer, all of the keys, values, and queries come from the same place, which is the output of the previous layer in the encoder. Each position in the encoder can attend to all positions in the previous layer of the encoder.

3. Self-attention in the decoder: Similar to the encoder, self-attention layers in the decoder allow each position in the decoder to attend to all positions in the decoder up to and including that position. However, leftward information flow in the decoder is prevented to preserve the auto-regressive property.

Overall, attention in transformers allows the model to jointly attend to information from different representation subspaces at different positions, improving the model's ability to capture dependencies and relationships between different parts of the input sequence.

In \[ \]:

Copied!

response \= await query\_engine.aquery(
    "What is the architecture of Llama2 based on?"
)

response = await query\_engine.aquery( "What is the architecture of Llama2 based on?" )

Retrieval entering vector: VectorIndexRetriever
Retrieval entering bm25: BM25Retriever

In \[ \]:

Copied!

print(str(response))

print(str(response))

The architecture of Llama 2 is based on the transformer model.

In \[ \]:

Copied!

response \= await query\_engine.aquery(
    "What was used before attention in transformers?"
)

response = await query\_engine.aquery( "What was used before attention in transformers?" )

Retrieval entering vector: VectorIndexRetriever
Retrieval entering bm25: BM25Retriever

In \[ \]:

Copied!

print(str(response))

print(str(response))

Recurrent neural networks, such as long short-term memory (LSTM) and gated recurrent neural networks, were commonly used before attention in transformers. These models were widely used in sequence modeling and transduction problems, including language modeling and machine translation.

Note on Saving and Loading[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/composable_retrievers/#note-on-saving-and-loading)
-----------------------------------------------------------------------------------------------------------------------------------------

Since objects aren't technically serializable, when saving and loading, then need to be provided at load time as well.

Here's an example of how I might save/load this setup.

### Save[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/composable_retrievers/#save)

In \[ \]:

Copied!

\# qdrant is already saved automatically!
\# we only need to save the docstore here

\# save our docstore nodes for bm25
docstore.persist("./docstore.json")

\# qdrant is already saved automatically! # we only need to save the docstore here # save our docstore nodes for bm25 docstore.persist("./docstore.json")

### Load[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/composable_retrievers/#load)

In \[ \]:

Copied!

from llama\_index.core.storage.docstore import SimpleDocumentStore
from llama\_index.vector\_stores.qdrant import QdrantVectorStore
from qdrant\_client import QdrantClient

docstore \= SimpleDocumentStore.from\_persist\_path("./docstore.json")

client \= QdrantClient(path\="./qdrant\_data")
vector\_store \= QdrantVectorStore("composable", client\=client)

from llama\_index.core.storage.docstore import SimpleDocumentStore from llama\_index.vector\_stores.qdrant import QdrantVectorStore from qdrant\_client import QdrantClient docstore = SimpleDocumentStore.from\_persist\_path("./docstore.json") client = QdrantClient(path="./qdrant\_data") vector\_store = QdrantVectorStore("composable", client=client)

In \[ \]:

Copied!

index \= VectorStoreIndex.from\_vector\_store(vector\_store)
vector\_retriever \= index.as\_retriever(similarity\_top\_k\=2)
bm25\_retriever \= BM25Retriever.from\_defaults(
    docstore\=docstore, similarity\_top\_k\=2
)

index = VectorStoreIndex.from\_vector\_store(vector\_store) vector\_retriever = index.as\_retriever(similarity\_top\_k=2) bm25\_retriever = BM25Retriever.from\_defaults( docstore=docstore, similarity\_top\_k=2 )

In \[ \]:

Copied!

from llama\_index.core.schema import IndexNode

vector\_obj \= IndexNode(
    index\_id\="vector", obj\=vector\_retriever, text\="Vector Retriever"
)
bm25\_obj \= IndexNode(
    index\_id\="bm25", obj\=bm25\_retriever, text\="BM25 Retriever"
)

from llama\_index.core.schema import IndexNode vector\_obj = IndexNode( index\_id="vector", obj=vector\_retriever, text="Vector Retriever" ) bm25\_obj = IndexNode( index\_id="bm25", obj=bm25\_retriever, text="BM25 Retriever" )

In \[ \]:

Copied!

\# if we had added regular nodes to the summary index, we could save/load that as well
\# summary\_index.persist("./summary\_index.json")
\# summary\_index = load\_index\_from\_storage(storage\_context, objects=objects)

from llama\_index.core import SummaryIndex

summary\_index \= SummaryIndex(objects\=\[vector\_obj, bm25\_obj\])

\# if we had added regular nodes to the summary index, we could save/load that as well # summary\_index.persist("./summary\_index.json") # summary\_index = load\_index\_from\_storage(storage\_context, objects=objects) from llama\_index.core import SummaryIndex summary\_index = SummaryIndex(objects=\[vector\_obj, bm25\_obj\])

Back to top

[Previous BM25 Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/bm25_retriever/)[Next Activeloop Deep Memory](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/)
