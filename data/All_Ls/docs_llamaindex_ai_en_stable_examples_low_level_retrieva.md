Title: Building Retrieval from Scratch - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/low_level/retrieval/

Markdown Content:
Building Retrieval from Scratch - LlamaIndex


In this tutorial, we show you how to build a standard retriever against a vector database, that will fetch nodes via top-k similarity.

We use Pinecone as the vector database. We load in nodes using our high-level ingestion abstractions (to see how to build this from scratch, see our previous tutorial!).

We will show how to do the following:

1.  How to generate a query embedding
2.  How to query the vector database using different search modes (dense, sparse, hybrid)
3.  How to parse results into a set of Nodes
4.  How to put this in a custom retriever

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/retrieval/#setup)
----------------------------------------------------------------------------------

We build an empty Pinecone Index, and define the necessary LlamaIndex wrappers/abstractions so that we can start loading data into Pinecone.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-readers\-file pymupdf
%pip install llama\-index\-vector\-stores\-pinecone
%pip install llama\-index\-embeddings\-openai

%pip install llama-index-readers-file pymupdf %pip install llama-index-vector-stores-pinecone %pip install llama-index-embeddings-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

#### Build Pinecone Index[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/retrieval/#build-pinecone-index)

In \[ \]:

Copied!

import pinecone
import os

api\_key \= os.environ\["PINECONE\_API\_KEY"\]
pinecone.init(api\_key\=api\_key, environment\="us-west1-gcp")

import pinecone import os api\_key = os.environ\["PINECONE\_API\_KEY"\] pinecone.init(api\_key=api\_key, environment="us-west1-gcp")

In \[ \]:

Copied!

\# dimensions are for text-embedding-ada-002
pinecone.create\_index(
    "quickstart", dimension\=1536, metric\="euclidean", pod\_type\="p1"
)

\# dimensions are for text-embedding-ada-002 pinecone.create\_index( "quickstart", dimension=1536, metric="euclidean", pod\_type="p1" )

In \[ \]:

Copied!

pinecone\_index \= pinecone.Index("quickstart")

pinecone\_index = pinecone.Index("quickstart")

In \[ \]:

Copied!

\# \[Optional\] drop contents in index
pinecone\_index.delete(deleteAll\=True)

\# \[Optional\] drop contents in index pinecone\_index.delete(deleteAll=True)

#### Create PineconeVectorStore[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/retrieval/#create-pineconevectorstore)

Simple wrapper abstraction to use in LlamaIndex. Wrap in StorageContext so we can easily load in Nodes.

In \[ \]:

Copied!

from llama\_index.vector\_stores.pinecone import PineconeVectorStore

from llama\_index.vector\_stores.pinecone import PineconeVectorStore

In \[ \]:

Copied!

vector\_store \= PineconeVectorStore(pinecone\_index\=pinecone\_index)

vector\_store = PineconeVectorStore(pinecone\_index=pinecone\_index)

#### Load Documents[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/retrieval/#load-documents)

In \[ \]:

Copied!

!mkdir data
!wget \--user\-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" \-O "data/llama2.pdf"

!mkdir data !wget --user-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" -O "data/llama2.pdf"

In \[ \]:

Copied!

from pathlib import Path
from llama\_index.readers.file import PyMuPDFReader

from pathlib import Path from llama\_index.readers.file import PyMuPDFReader

In \[ \]:

Copied!

loader \= PyMuPDFReader()
documents \= loader.load(file\_path\="./data/llama2.pdf")

loader = PyMuPDFReader() documents = loader.load(file\_path="./data/llama2.pdf")

#### Load into Vector Store[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/retrieval/#load-into-vector-store)

Load in documents into the PineconeVectorStore.

**NOTE**: We use high-level ingestion abstractions here, with `VectorStoreIndex.from_documents.` We'll refrain from using `VectorStoreIndex` for the rest of this tutorial.

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex
from llama\_index.core.node\_parser import SentenceSplitter
from llama\_index.core import StorageContext

from llama\_index.core import VectorStoreIndex from llama\_index.core.node\_parser import SentenceSplitter from llama\_index.core import StorageContext

In \[ \]:

Copied!

splitter \= SentenceSplitter(chunk\_size\=1024)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents, transformations\=\[splitter\], storage\_context\=storage\_context
)

splitter = SentenceSplitter(chunk\_size=1024) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, transformations=\[splitter\], storage\_context=storage\_context )

Define Vector Retriever[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/retrieval/#define-vector-retriever)
----------------------------------------------------------------------------------------------------------------------

Now we're ready to define our retriever against this vector store to retrieve a set of nodes.

We'll show the processes step by step and then wrap it into a function.

In \[ \]:

Copied!

query\_str \= "Can you tell me about the key concepts for safety finetuning"

query\_str = "Can you tell me about the key concepts for safety finetuning"

### 1\. Generate a Query Embedding[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/retrieval/#1-generate-a-query-embedding)

In \[ \]:

Copied!

from llama\_index.embeddings.openai import OpenAIEmbedding

embed\_model \= OpenAIEmbedding()

from llama\_index.embeddings.openai import OpenAIEmbedding embed\_model = OpenAIEmbedding()

In \[ \]:

Copied!

query\_embedding \= embed\_model.get\_query\_embedding(query\_str)

query\_embedding = embed\_model.get\_query\_embedding(query\_str)

### 2\. Query the Vector Database[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/retrieval/#2-query-the-vector-database)

We show how to query the vector database with different modes: default, sparse, and hybrid.

We first construct a `VectorStoreQuery` and then query the vector db.

In \[ \]:

Copied!

\# construct vector store query
from llama\_index.core.vector\_stores import VectorStoreQuery

query\_mode \= "default"
\# query\_mode = "sparse"
\# query\_mode = "hybrid"

vector\_store\_query \= VectorStoreQuery(
    query\_embedding\=query\_embedding, similarity\_top\_k\=2, mode\=query\_mode
)

\# construct vector store query from llama\_index.core.vector\_stores import VectorStoreQuery query\_mode = "default" # query\_mode = "sparse" # query\_mode = "hybrid" vector\_store\_query = VectorStoreQuery( query\_embedding=query\_embedding, similarity\_top\_k=2, mode=query\_mode )

In \[ \]:

Copied!

\# returns a VectorStoreQueryResult
query\_result \= vector\_store.query(vector\_store\_query)
query\_result

\# returns a VectorStoreQueryResult query\_result = vector\_store.query(vector\_store\_query) query\_result

### 3\. Parse Result into a set of Nodes[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/retrieval/#3-parse-result-into-a-set-of-nodes)

The `VectorStoreQueryResult` returns the set of nodes and similarities. We construct a `NodeWithScore` object with this.

In \[ \]:

Copied!

from llama\_index.core.schema import NodeWithScore
from typing import Optional

nodes\_with\_scores \= \[\]
for index, node in enumerate(query\_result.nodes):
    score: Optional\[float\] \= None
    if query\_result.similarities is not None:
        score \= query\_result.similarities\[index\]
    nodes\_with\_scores.append(NodeWithScore(node\=node, score\=score))

from llama\_index.core.schema import NodeWithScore from typing import Optional nodes\_with\_scores = \[\] for index, node in enumerate(query\_result.nodes): score: Optional\[float\] = None if query\_result.similarities is not None: score = query\_result.similarities\[index\] nodes\_with\_scores.append(NodeWithScore(node=node, score=score))

In \[ \]:

Copied!

from llama\_index.core.response.notebook\_utils import display\_source\_node

for node in nodes\_with\_scores:
    display\_source\_node(node, source\_length\=1000)

from llama\_index.core.response.notebook\_utils import display\_source\_node for node in nodes\_with\_scores: display\_source\_node(node, source\_length=1000)

### 4\. Put this into a Retriever[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/retrieval/#4-put-this-into-a-retriever)

Let's put this into a Retriever subclass that can plug into the rest of LlamaIndex workflows!

In \[ \]:

Copied!

from llama\_index.core import QueryBundle
from llama\_index.core.retrievers import BaseRetriever
from typing import Any, List

class PineconeRetriever(BaseRetriever):
    """Retriever over a pinecone vector store."""

    def \_\_init\_\_(
        self,
        vector\_store: PineconeVectorStore,
        embed\_model: Any,
        query\_mode: str \= "default",
        similarity\_top\_k: int \= 2,
    ) \-> None:
        """Init params."""
        self.\_vector\_store \= vector\_store
        self.\_embed\_model \= embed\_model
        self.\_query\_mode \= query\_mode
        self.\_similarity\_top\_k \= similarity\_top\_k
        super().\_\_init\_\_()

    def \_retrieve(self, query\_bundle: QueryBundle) \-> List\[NodeWithScore\]:
        """Retrieve."""
        query\_embedding \= embed\_model.get\_query\_embedding(query\_str)
        vector\_store\_query \= VectorStoreQuery(
            query\_embedding\=query\_embedding,
            similarity\_top\_k\=self.\_similarity\_top\_k,
            mode\=self.\_query\_mode,
        )
        query\_result \= vector\_store.query(vector\_store\_query)

        nodes\_with\_scores \= \[\]
        for index, node in enumerate(query\_result.nodes):
            score: Optional\[float\] \= None
            if query\_result.similarities is not None:
                score \= query\_result.similarities\[index\]
            nodes\_with\_scores.append(NodeWithScore(node\=node, score\=score))

        return nodes\_with\_scores

from llama\_index.core import QueryBundle from llama\_index.core.retrievers import BaseRetriever from typing import Any, List class PineconeRetriever(BaseRetriever): """Retriever over a pinecone vector store.""" def \_\_init\_\_( self, vector\_store: PineconeVectorStore, embed\_model: Any, query\_mode: str = "default", similarity\_top\_k: int = 2, ) -> None: """Init params.""" self.\_vector\_store = vector\_store self.\_embed\_model = embed\_model self.\_query\_mode = query\_mode self.\_similarity\_top\_k = similarity\_top\_k super().\_\_init\_\_() def \_retrieve(self, query\_bundle: QueryBundle) -> List\[NodeWithScore\]: """Retrieve.""" query\_embedding = embed\_model.get\_query\_embedding(query\_str) vector\_store\_query = VectorStoreQuery( query\_embedding=query\_embedding, similarity\_top\_k=self.\_similarity\_top\_k, mode=self.\_query\_mode, ) query\_result = vector\_store.query(vector\_store\_query) nodes\_with\_scores = \[\] for index, node in enumerate(query\_result.nodes): score: Optional\[float\] = None if query\_result.similarities is not None: score = query\_result.similarities\[index\] nodes\_with\_scores.append(NodeWithScore(node=node, score=score)) return nodes\_with\_scores

In \[ \]:

Copied!

retriever \= PineconeRetriever(
    vector\_store, embed\_model, query\_mode\="default", similarity\_top\_k\=2
)

retriever = PineconeRetriever( vector\_store, embed\_model, query\_mode="default", similarity\_top\_k=2 )

In \[ \]:

Copied!

retrieved\_nodes \= retriever.retrieve(query\_str)
for node in retrieved\_nodes:
    display\_source\_node(node, source\_length\=1000)

retrieved\_nodes = retriever.retrieve(query\_str) for node in retrieved\_nodes: display\_source\_node(node, source\_length=1000)

Plug this into our RetrieverQueryEngine to synthesize a response[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/retrieval/#plug-this-into-our-retrieverqueryengine-to-synthesize-a-response)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**NOTE**: We'll cover more on how to build response synthesis from scratch in future tutorials!

In \[ \]:

Copied!

from llama\_index.core.query\_engine import RetrieverQueryEngine

query\_engine \= RetrieverQueryEngine.from\_args(retriever)

from llama\_index.core.query\_engine import RetrieverQueryEngine query\_engine = RetrieverQueryEngine.from\_args(retriever)

In \[ \]:

Copied!

response \= query\_engine.query(query\_str)

response = query\_engine.query(query\_str)

In \[ \]:

Copied!

print(str(response))

print(str(response))

The key concepts for safety fine-tuning include supervised safety fine-tuning, safety RLHF (Reinforcement Learning from Human Feedback), and safety context distillation. Supervised safety fine-tuning involves gathering adversarial prompts and safe demonstrations to train the model to align with safety guidelines. Safety RLHF integrates safety into the RLHF pipeline by training a safety-specific reward model and gathering challenging adversarial prompts for fine-tuning. Safety context distillation refines the RLHF pipeline by generating safer model responses using a safety preprompt and fine-tuning the model on these responses without the preprompt. These concepts are used to mitigate safety risks and improve the safety of the model's responses.

Back to top

[Previous Building Response Synthesis from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/response_synthesis/)[Next Building a Router from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/router/)

Hi, how can I help you?

🦙
