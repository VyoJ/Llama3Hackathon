Title: Milvus Vector Store With Hybrid Retrieval

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusHybridIndexDemo/

Markdown Content:
Milvus Vector Store With Hybrid Retrieval - LlamaIndex


In this notebook we are going to show a quick demo of using the MilvusVectorStore with hybrid retrieval. (Milvus version should higher than 2.4.0)

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-milvus

%pip install llama-index-vector-stores-milvus

BGE-M3 from FlagEmbedding is used as the default sparse embedding method, so it needs to be installed along with llama-index.

In \[ \]:

Copied!

! pip install llama\-index
! pip install FlagEmbedding

! pip install llama-index ! pip install FlagEmbedding

In \[ \]:

Copied!

import logging
import sys

\# Uncomment to see debug logs
\# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
\# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader, Document
from llama\_index.vector\_stores.milvus import MilvusVectorStore
from IPython.display import Markdown, display
import textwrap

import logging import sys # Uncomment to see debug logs # logging.basicConfig(stream=sys.stdout, level=logging.DEBUG) # logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout)) from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader, Document from llama\_index.vector\_stores.milvus import MilvusVectorStore from IPython.display import Markdown, display import textwrap

### Setup OpenAI[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusHybridIndexDemo/#setup-openai)

Lets first begin by adding the openai api key. This will allow us to access openai for embeddings and to use chatgpt.

In \[ \]:

Copied!

import openai

openai.api\_key \= "sk-"

import openai openai.api\_key = "sk-"

Download Data

In \[ \]:

Copied!

! mkdir \-p 'data/paul\_graham/'
! wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

! mkdir -p 'data/paul\_graham/' ! wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

\--2024-04-25 17:44:59--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.111.133, 185.199.108.133, 185.199.109.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.111.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 75042 (73K) \[text/plain\]
Saving to: ‘data/paul\_graham/paul\_graham\_essay.txt’

data/paul\_graham/pa 100%\[>\]  73.28K  --.-KB/s    in 0.07s   

2024-04-25 17:45:00 (994 KB/s) - ‘data/paul\_graham/paul\_graham\_essay.txt’ saved \[75042/75042\]

### Generate our data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusHybridIndexDemo/#generate-our-data)

With our LLM set, lets start using the Milvus Index. As a first example, lets generate a document from the file found in the `data/paul_graham/` folder. In this folder there is a single essay from Paul Graham titled `What I Worked On`. To generate the documents we will use the SimpleDirectoryReader.

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

print("Document ID:", documents\[0\].doc\_id)

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data() print("Document ID:", documents\[0\].doc\_id)

Document ID: ca3f5dbc-f772-41da-9a4f-bb4884691793

### Create an index across the data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusHybridIndexDemo/#create-an-index-across-the-data)

Now that we have a document, we can can create an index and insert the document. For the index we will use a MilvusVectorStore. MilvusVectorStore takes in a few arguments:

*   `uri (str, optional)`: The URI to connect to, comes in the form of "[http://address:port](http://address:port)". Defaults to "[http://localhost:19530](http://localhost:19530/)".
    
*   `token (str, optional)`: The token for log in. Empty if not using rbac, if using rbac it will most likely be "username:password". Defaults to "".
    
*   `collection_name (str, optional)`: The name of the collection where data will be stored. Defaults to "llamalection".
    
*   `dim (int, optional)`: The dimension of the embeddings. If it is not provided, collection creation will be done on first insert. Defaults to None.
    
*   `embedding_field (str, optional)`: The name of the embedding field for the collection, defaults to DEFAULT\_EMBEDDING\_KEY.
    
*   `doc_id_field (str, optional)`: The name of the doc\_id field for the collection, defaults to DEFAULT\_DOC\_ID\_KEY.
    
*   `similarity_metric (str, optional)`: The similarity metric to use, currently supports IP and L2. Defaults to "IP".
    
*   `consistency_level (str, optional)`: Which consistency level to use for a newly created collection. Defaults to "Strong".
    
*   `overwrite (bool, optional)`: Whether to overwrite existing collection with same name. Defaults to False.
    
*   `text_key (str, optional)`: What key text is stored in in the passed collection. Used when bringing your own collection. Defaults to None.
    
*   `index_config (dict, optional)`: The configuration used for building the Milvus index. Defaults to None.
    
*   `search_config (dict, optional)`: The configuration used for searching the Milvus index. Note that this must be compatible with the index type specified by index\_config. Defaults to None.
    
*   `batch_size (int)`: Configures the number of documents processed in one batch when inserting data into Milvus. Defaults to DEFAULT\_BATCH\_SIZE.
    
*   `enable_sparse (bool)`: A boolean flag indicating whether to enable support for sparse embeddings for hybrid retrieval. Defaults to False.
    
*   `sparse_embedding_function (BaseSparseEmbeddingFunction, optional)`: If enable\_sparse is True, this object should be provided to convert text to a sparse embedding.
    
*   `hybrid_ranker (str)`: Specifies the type of ranker used in hybrid search queries. Currently only supports \['RRFRanker','WeightedRanker'\]. Defaults to "RRFRanker".
    
*   `hybrid_ranker_params (dict)`: Configuration parameters for the hybrid ranker.
    
    *   For "RRFRanker", it should include:
        
        *   'k' (int): A parameter used in Reciprocal Rank Fusion (RRF). This value is used to calculate the rank scores as part of the RRF algorithm, which combines multiple ranking strategies into a single score to improve search relevance.
    *   For "WeightedRanker", it should include:
        
        *   'weights' (list of float): A list of exactly two weights:
            *   The weight for the dense embedding component.
            *   The weight for the sparse embedding component.
        
        These weights are used to adjust the importance of the dense and sparse components of the embeddings in the hybrid retrieval process.
        
    
    Defaults to an empty dictionary, implying that the ranker will operate with its predefined default settings.
    

Now, let's begin creating a MilvusVectorStore for hybrid retrieval. We need to set `enable_sparse` to True to enable sparse embedding generation, and we also need to configure the RRFRanker for reranking. For more details, please refer to [Milvus Reranking](https://milvus.io/docs/reranking.md).

In \[ \]:

Copied!

\# Create an index over the documnts
from llama\_index.core import StorageContext
import os

vector\_store \= MilvusVectorStore(
    dim\=1536,
    overwrite\=True,
    enable\_sparse\=True,
    hybrid\_ranker\="RRFRanker",
    hybrid\_ranker\_params\={"k": 60},
)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

\# Create an index over the documnts from llama\_index.core import StorageContext import os vector\_store = MilvusVectorStore( dim=1536, overwrite=True, enable\_sparse=True, hybrid\_ranker="RRFRanker", hybrid\_ranker\_params={"k": 60}, ) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

Sparse embedding function is not provided, using default.

Fetching 30 files:   0%|          | 0/30 \[00:00<?, ?it/s\]

\----------using 2\*GPUs----------

### Query the data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusHybridIndexDemo/#query-the-data)

Now that we have our document stored in the index, we can ask questions against the index while enable hybrid mode by specifying `vector_store_query_mode`. The index will use the data stored in itself as the knowledge base for chatgpt.

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(vector\_store\_query\_mode\="hybrid")
response \= query\_engine.query("What did the author learn?")
print(textwrap.fill(str(response), 100))

query\_engine = index.as\_query\_engine(vector\_store\_query\_mode="hybrid") response = query\_engine.query("What did the author learn?") print(textwrap.fill(str(response), 100))

The author learned that the field of AI, as practiced at the time, was not as promising as initially
believed. The author realized that the approach of using explicit data structures to represent
concepts in AI was not effective in truly understanding natural language. This led the author to
shift focus from traditional AI to exploring Lisp for its own merits, ultimately deciding to write a
book about Lisp hacking.

In \[ \]:

Copied!

response \= query\_engine.query("What was a hard moment for the author?")
print(textwrap.fill(str(response), 100))

response = query\_engine.query("What was a hard moment for the author?") print(textwrap.fill(str(response), 100))

Dealing with the stress and pressure related to managing Hacker News was a challenging moment for
the author.

### Customized sparse embedding function[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusHybridIndexDemo/#customized-sparse-embedding-function)

Here, we are using the default sparse embedding function, which utilizes the [BGE-M3](https://arxiv.org/abs/2402.03216) model. Below, we describe how to prepare a customized sparse embedding function.

You will need to create a class similar to ExampleEmbeddingFunction. This class should include methods such as:

*   encode\_queries: This method converts texts into list of sparse embeddings for queries.
*   encode\_documents: This method converts text into list of sparse embeddings for documents.

The format of the sparse embedding is a dictionary, where the key (an integer) represents the dimension, and its corresponding value (a float) represents the embedding's magnitude in that dimension.(e.g., {1: 0.5, 2: 0.3}).

In \[ \]:

Copied!

! pip install FlagEmbedding

! pip install FlagEmbedding

In \[ \]:

Copied!

from FlagEmbedding import BGEM3FlagModel
from typing import List
from llama\_index.vector\_stores.milvus.utils import BaseSparseEmbeddingFunction

class ExampleEmbeddingFunction(BaseSparseEmbeddingFunction):
    def \_\_init\_\_(self):
        self.model \= BGEM3FlagModel("BAAI/bge-m3", use\_fp16\=False)

    def encode\_queries(self, queries: List\[str\]):
        outputs \= self.model.encode(
            queries,
            return\_dense\=False,
            return\_sparse\=True,
            return\_colbert\_vecs\=False,
        )\["lexical\_weights"\]
        return \[self.\_to\_standard\_dict(output) for output in outputs\]

    def encode\_documents(self, documents: List\[str\]):
        outputs \= self.model.encode(
            documents,
            return\_dense\=False,
            return\_sparse\=True,
            return\_colbert\_vecs\=False,
        )\["lexical\_weights"\]
        return \[self.\_to\_standard\_dict(output) for output in outputs\]

    def \_to\_standard\_dict(self, raw\_output):
        result \= {}
        for k in raw\_output:
            result\[int(k)\] \= raw\_output\[k\]
        return result

from FlagEmbedding import BGEM3FlagModel from typing import List from llama\_index.vector\_stores.milvus.utils import BaseSparseEmbeddingFunction class ExampleEmbeddingFunction(BaseSparseEmbeddingFunction): def \_\_init\_\_(self): self.model = BGEM3FlagModel("BAAI/bge-m3", use\_fp16=False) def encode\_queries(self, queries: List\[str\]): outputs = self.model.encode( queries, return\_dense=False, return\_sparse=True, return\_colbert\_vecs=False, )\["lexical\_weights"\] return \[self.\_to\_standard\_dict(output) for output in outputs\] def encode\_documents(self, documents: List\[str\]): outputs = self.model.encode( documents, return\_dense=False, return\_sparse=True, return\_colbert\_vecs=False, )\["lexical\_weights"\] return \[self.\_to\_standard\_dict(output) for output in outputs\] def \_to\_standard\_dict(self, raw\_output): result = {} for k in raw\_output: result\[int(k)\] = raw\_output\[k\] return result

now we can use this in our hybrid retrieval.

In \[ \]:

Copied!

vector\_store \= MilvusVectorStore(
    dim\=1536,
    overwrite\=True,
    enable\_sparse\=True,
    sparse\_embedding\_function\=ExampleEmbeddingFunction(),
    hybrid\_ranker\="RRFRanker",
    hybrid\_ranker\_params\={"k": 60},
)

vector\_store = MilvusVectorStore( dim=1536, overwrite=True, enable\_sparse=True, sparse\_embedding\_function=ExampleEmbeddingFunction(), hybrid\_ranker="RRFRanker", hybrid\_ranker\_params={"k": 60}, )

Fetching 30 files:   0%|          | 0/30 \[00:00<?, ?it/s\]

\----------using 2\*GPUs----------

Back to top

[Previous Metal Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MetalIndexDemo/)[Next Milvus Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusIndexDemo/)
