Title: Qdrant Hybrid Search - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_hybrid/

Markdown Content:
Qdrant Hybrid Search - LlamaIndex


Qdrant supports hybrid search by combining search results from `sparse` and `dense` vectors.

`dense` vectors are the ones you have probably already been using -- embedding models from OpenAI, BGE, SentenceTransformers, etc. are typically `dense` embedding models. They create a numerical representation of a piece of text, represented as a long list of numbers. These `dense` vectors can capture rich semantics across the entire piece of text.

`sparse` vectors are slightly different. They use a specialized approach or model (TF-IDF, BM25, SPLADE, etc.) for generating vectors. These vectors are typically mostly zeros, making them `sparse` vectors. These `sparse` vectors are great at capturing specific keywords and similar small details.

This notebook walks through setting up and customizing hybrid search with Qdrant and `"prithvida/Splade_PP_en_v1"` variants from Huggingface.

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_hybrid/#setup)
------------------------------------------------------------------------------------------

First, we setup our env and load our data.

In \[ \]:

Copied!

%pip install \-U llama\-index llama\-index\-vector\-stores\-qdrant fastembed

%pip install -U llama-index llama-index-vector-stores-qdrant fastembed

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..."

In \[ \]:

Copied!

!mkdir \-p 'data/'
!wget \--user\-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" \-O "data/llama2.pdf"

!mkdir -p 'data/' !wget --user-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" -O "data/llama2.pdf"

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

documents \= SimpleDirectoryReader("./data/").load\_data()

from llama\_index.core import SimpleDirectoryReader documents = SimpleDirectoryReader("./data/").load\_data()

Indexing Data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_hybrid/#indexing-data)
----------------------------------------------------------------------------------------------------------

Now, we can index our data.

Hybrid search with Qdrant must be enabled from the beginning -- we can simply set `enable_hybrid=True`.

This will run sparse vector generation locally using the `"prithvida/Splade_PP_en_v1"` using fastembed, in addition to generating dense vectors with OpenAI.

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, StorageContext
from llama\_index.core import Settings
from llama\_index.vector\_stores.qdrant import QdrantVectorStore
from qdrant\_client import QdrantClient, AsyncQdrantClient

\# creates a persistant index to disk
client \= QdrantClient(host\="localhost", port\=6333)
aclient \= AsyncQdrantClient(host\="localhost", port\=6333)

\# create our vector store with hybrid indexing enabled
\# batch\_size controls how many nodes are encoded with sparse vectors at once
vector\_store \= QdrantVectorStore(
    "llama2\_paper",
    client\=client,
    aclient\=aclient,
    enable\_hybrid\=True,
    batch\_size\=20,
)

storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
Settings.chunk\_size \= 512

index \= VectorStoreIndex.from\_documents(
    documents,
    storage\_context\=storage\_context,
)

from llama\_index.core import VectorStoreIndex, StorageContext from llama\_index.core import Settings from llama\_index.vector\_stores.qdrant import QdrantVectorStore from qdrant\_client import QdrantClient, AsyncQdrantClient # creates a persistant index to disk client = QdrantClient(host="localhost", port=6333) aclient = AsyncQdrantClient(host="localhost", port=6333) # create our vector store with hybrid indexing enabled # batch\_size controls how many nodes are encoded with sparse vectors at once vector\_store = QdrantVectorStore( "llama2\_paper", client=client, aclient=aclient, enable\_hybrid=True, batch\_size=20, ) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) Settings.chunk\_size = 512 index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context, )

Both client and aclient are provided. If using \`:memory:\` mode, the data between clients is not synced.

Fetching 9 files:   0%|          | 0/9 \[00:00<?, ?it/s\]

.gitattributes:   0%|          | 0.00/1.52k \[00:00<?, ?B/s\]

generation\_config.json:   0%|          | 0.00/90.0 \[00:00<?, ?B/s\]

tokenizer.json:   0%|          | 0.00/712k \[00:00<?, ?B/s\]

config.json:   0%|          | 0.00/755 \[00:00<?, ?B/s\]

tokenizer\_config.json:   0%|          | 0.00/1.38k \[00:00<?, ?B/s\]

README.md:   0%|          | 0.00/133 \[00:00<?, ?B/s\]

model.onnx:   0%|          | 0.00/532M \[00:00<?, ?B/s\]

vocab.txt:   0%|          | 0.00/232k \[00:00<?, ?B/s\]

special\_tokens\_map.json:   0%|          | 0.00/695 \[00:00<?, ?B/s\]

Fetching 9 files:   0%|          | 0/9 \[00:00<?, ?it/s\]

Hybrid Queries[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_hybrid/#hybrid-queries)
------------------------------------------------------------------------------------------------------------

When querying with hybrid mode, we can set `similarity_top_k` and `sparse_top_k` separately.

`sparse_top_k` represents how many nodes will be retrieved from each dense and sparse query. For example, if `sparse_top_k=5` is set, that means I will retrieve 5 nodes using sparse vectors and 5 nodes using dense vectors.

`similarity_top_k` controls the final number of returned nodes. In the above setting, we end up with 10 nodes. A fusion algorithm is applied to rank and order the nodes from different vector spaces ([relative score fusion](https://weaviate.io/blog/hybrid-search-fusion-algorithms#relative-score-fusion) in this case). `similarity_top_k=2` means the top two nodes after fusion are returned.

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(
    similarity\_top\_k\=2, sparse\_top\_k\=12, vector\_store\_query\_mode\="hybrid"
)

query\_engine = index.as\_query\_engine( similarity\_top\_k=2, sparse\_top\_k=12, vector\_store\_query\_mode="hybrid" )

In \[ \]:

Copied!

from IPython.display import display, Markdown

response \= query\_engine.query(
    "How was Llama2 specifically trained differently from Llama1?"
)

display(Markdown(str(response)))

from IPython.display import display, Markdown response = query\_engine.query( "How was Llama2 specifically trained differently from Llama1?" ) display(Markdown(str(response)))

Llama 2 was specifically trained differently from Llama 1 by making changes such as performing more robust data cleaning, updating data mixes, training on 40% more total tokens, doubling the context length, and using grouped-query attention (GQA) to improve inference scalability for larger models. Additionally, Llama 2 adopted most of the pretraining setting and model architecture from Llama 1 but included architectural enhancements like increased context length and grouped-query attention.

In \[ \]:

Copied!

print(len(response.source\_nodes))

print(len(response.source\_nodes))

2

Lets compare to not using hybrid search at all!

In \[ \]:

Copied!

from IPython.display import display, Markdown

query\_engine \= index.as\_query\_engine(
    similarity\_top\_k\=2,
    \# sparse\_top\_k=10,
    \# vector\_store\_query\_mode="hybrid"
)

response \= query\_engine.query(
    "How was Llama2 specifically trained differently from Llama1?"
)
display(Markdown(str(response)))

from IPython.display import display, Markdown query\_engine = index.as\_query\_engine( similarity\_top\_k=2, # sparse\_top\_k=10, # vector\_store\_query\_mode="hybrid" ) response = query\_engine.query( "How was Llama2 specifically trained differently from Llama1?" ) display(Markdown(str(response)))

Llama 2 was specifically trained differently from Llama 1 by making changes to improve performance, such as performing more robust data cleaning, updating data mixes, training on 40% more total tokens, doubling the context length, and using grouped-query attention (GQA) to improve inference scalability for larger models.

### Async Support[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_hybrid/#async-support)

And of course, async queries are also supported (note that in-memory Qdrant data is not shared between async and sync clients!)

In \[ \]:

Copied!

import nest\_asyncio

nest\_asyncio.apply()

import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, StorageContext
from llama\_index.core import Settings
from llama\_index.vector\_stores.qdrant import QdrantVectorStore

\# create our vector store with hybrid indexing enabled
vector\_store \= QdrantVectorStore(
    collection\_name\="llama2\_paper",
    client\=client,
    aclient\=aclient,
    enable\_hybrid\=True,
    batch\_size\=20,
)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
Settings.chunk\_size \= 512

index \= VectorStoreIndex.from\_documents(
    documents,
    storage\_context\=storage\_context,
    use\_async\=True,
)

query\_engine \= index.as\_query\_engine(similarity\_top\_k\=2, sparse\_top\_k\=10)

response \= await query\_engine.aquery(
    "What baseline models are measured against in the paper?"
)

from llama\_index.core import VectorStoreIndex, StorageContext from llama\_index.core import Settings from llama\_index.vector\_stores.qdrant import QdrantVectorStore # create our vector store with hybrid indexing enabled vector\_store = QdrantVectorStore( collection\_name="llama2\_paper", client=client, aclient=aclient, enable\_hybrid=True, batch\_size=20, ) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) Settings.chunk\_size = 512 index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context, use\_async=True, ) query\_engine = index.as\_query\_engine(similarity\_top\_k=2, sparse\_top\_k=10) response = await query\_engine.aquery( "What baseline models are measured against in the paper?" )

\[Advanced\] Customizing Hybrid Search with Qdrant[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_hybrid/#advanced-customizing-hybrid-search-with-qdrant)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this section, we walk through various settings that can be used to fully customize the hybrid search experience

### Customizing Sparse Vector Generation[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_hybrid/#customizing-sparse-vector-generation)

Sparse vector generation can be done using a single model, or sometimes distinct seperate models for queries and documents. Here we use two -- `"naver/efficient-splade-VI-BT-large-doc"` and `"naver/efficient-splade-VI-BT-large-query"`

Below is the sample code for generating the sparse vectors and how you can set the functionality in the constructor. You can use this and customize as needed.

In \[ \]:

Copied!

from typing import Any, List, Tuple
import torch
from transformers import AutoTokenizer, AutoModelForMaskedLM

doc\_tokenizer \= AutoTokenizer.from\_pretrained(
    "naver/efficient-splade-VI-BT-large-doc"
)
doc\_model \= AutoModelForMaskedLM.from\_pretrained(
    "naver/efficient-splade-VI-BT-large-doc"
)

query\_tokenizer \= AutoTokenizer.from\_pretrained(
    "naver/efficient-splade-VI-BT-large-query"
)
query\_model \= AutoModelForMaskedLM.from\_pretrained(
    "naver/efficient-splade-VI-BT-large-query"
)

def sparse\_doc\_vectors(
    texts: List\[str\],
) \-> Tuple\[List\[List\[int\]\], List\[List\[float\]\]\]:
    """
    Computes vectors from logits and attention mask using ReLU, log, and max operations.
    """
    tokens \= doc\_tokenizer(
        texts, truncation\=True, padding\=True, return\_tensors\="pt"
    )
    if torch.cuda.is\_available():
        tokens \= tokens.to("cuda")

    output \= doc\_model(\*\*tokens)
    logits, attention\_mask \= output.logits, tokens.attention\_mask
    relu\_log \= torch.log(1 + torch.relu(logits))
    weighted\_log \= relu\_log \* attention\_mask.unsqueeze(\-1)
    tvecs, \_ \= torch.max(weighted\_log, dim\=1)

    \# extract the vectors that are non-zero and their indices
    indices \= \[\]
    vecs \= \[\]
    for batch in tvecs:
        indices.append(batch.nonzero(as\_tuple\=True)\[0\].tolist())
        vecs.append(batch\[indices\[\-1\]\].tolist())

    return indices, vecs

def sparse\_query\_vectors(
    texts: List\[str\],
) \-> Tuple\[List\[List\[int\]\], List\[List\[float\]\]\]:
    """
    Computes vectors from logits and attention mask using ReLU, log, and max operations.
    """
    \# TODO: compute sparse vectors in batches if max length is exceeded
    tokens \= query\_tokenizer(
        texts, truncation\=True, padding\=True, return\_tensors\="pt"
    )
    if torch.cuda.is\_available():
        tokens \= tokens.to("cuda")

    output \= query\_model(\*\*tokens)
    logits, attention\_mask \= output.logits, tokens.attention\_mask
    relu\_log \= torch.log(1 + torch.relu(logits))
    weighted\_log \= relu\_log \* attention\_mask.unsqueeze(\-1)
    tvecs, \_ \= torch.max(weighted\_log, dim\=1)

    \# extract the vectors that are non-zero and their indices
    indices \= \[\]
    vecs \= \[\]
    for batch in tvecs:
        indices.append(batch.nonzero(as\_tuple\=True)\[0\].tolist())
        vecs.append(batch\[indices\[\-1\]\].tolist())

    return indices, vecs

from typing import Any, List, Tuple import torch from transformers import AutoTokenizer, AutoModelForMaskedLM doc\_tokenizer = AutoTokenizer.from\_pretrained( "naver/efficient-splade-VI-BT-large-doc" ) doc\_model = AutoModelForMaskedLM.from\_pretrained( "naver/efficient-splade-VI-BT-large-doc" ) query\_tokenizer = AutoTokenizer.from\_pretrained( "naver/efficient-splade-VI-BT-large-query" ) query\_model = AutoModelForMaskedLM.from\_pretrained( "naver/efficient-splade-VI-BT-large-query" ) def sparse\_doc\_vectors( texts: List\[str\], ) -> Tuple\[List\[List\[int\]\], List\[List\[float\]\]\]: """ Computes vectors from logits and attention mask using ReLU, log, and max operations. """ tokens = doc\_tokenizer( texts, truncation=True, padding=True, return\_tensors="pt" ) if torch.cuda.is\_available(): tokens = tokens.to("cuda") output = doc\_model(\*\*tokens) logits, attention\_mask = output.logits, tokens.attention\_mask relu\_log = torch.log(1 + torch.relu(logits)) weighted\_log = relu\_log \* attention\_mask.unsqueeze(-1) tvecs, \_ = torch.max(weighted\_log, dim=1) # extract the vectors that are non-zero and their indices indices = \[\] vecs = \[\] for batch in tvecs: indices.append(batch.nonzero(as\_tuple=True)\[0\].tolist()) vecs.append(batch\[indices\[-1\]\].tolist()) return indices, vecs def sparse\_query\_vectors( texts: List\[str\], ) -> Tuple\[List\[List\[int\]\], List\[List\[float\]\]\]: """ Computes vectors from logits and attention mask using ReLU, log, and max operations. """ # TODO: compute sparse vectors in batches if max length is exceeded tokens = query\_tokenizer( texts, truncation=True, padding=True, return\_tensors="pt" ) if torch.cuda.is\_available(): tokens = tokens.to("cuda") output = query\_model(\*\*tokens) logits, attention\_mask = output.logits, tokens.attention\_mask relu\_log = torch.log(1 + torch.relu(logits)) weighted\_log = relu\_log \* attention\_mask.unsqueeze(-1) tvecs, \_ = torch.max(weighted\_log, dim=1) # extract the vectors that are non-zero and their indices indices = \[\] vecs = \[\] for batch in tvecs: indices.append(batch.nonzero(as\_tuple=True)\[0\].tolist()) vecs.append(batch\[indices\[-1\]\].tolist()) return indices, vecs

In \[ \]:

Copied!

vector\_store \= QdrantVectorStore(
    "llama2\_paper",
    client\=client,
    enable\_hybrid\=True,
    sparse\_doc\_fn\=sparse\_doc\_vectors,
    sparse\_query\_fn\=sparse\_query\_vectors,
)

vector\_store = QdrantVectorStore( "llama2\_paper", client=client, enable\_hybrid=True, sparse\_doc\_fn=sparse\_doc\_vectors, sparse\_query\_fn=sparse\_query\_vectors, )

### Customizing `hybrid_fusion_fn()`[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_hybrid/#customizing-hybrid_fusion_fn)

By default, when running hbyrid queries with Qdrant, Relative Score Fusion is used to combine the nodes retrieved from both sparse and dense queries.

You can customize this function to be any other method (plain deduplication, Reciprocal Rank Fusion, etc.).

Below is the default code for our relative score fusion approach and how you can pass it into the constructor.

In \[ \]:

Copied!

from llama\_index.core.vector\_stores import VectorStoreQueryResult

def relative\_score\_fusion(
    dense\_result: VectorStoreQueryResult,
    sparse\_result: VectorStoreQueryResult,
    alpha: float \= 0.5,  \# passed in from the query engine
    top\_k: int \= 2,  \# passed in from the query engine i.e. similarity\_top\_k
) \-> VectorStoreQueryResult:
    """
    Fuse dense and sparse results using relative score fusion.
    """
    \# sanity check
    assert dense\_result.nodes is not None
    assert dense\_result.similarities is not None
    assert sparse\_result.nodes is not None
    assert sparse\_result.similarities is not None

    \# deconstruct results
    sparse\_result\_tuples \= list(
        zip(sparse\_result.similarities, sparse\_result.nodes)
    )
    sparse\_result\_tuples.sort(key\=lambda x: x\[0\], reverse\=True)

    dense\_result\_tuples \= list(
        zip(dense\_result.similarities, dense\_result.nodes)
    )
    dense\_result\_tuples.sort(key\=lambda x: x\[0\], reverse\=True)

    \# track nodes in both results
    all\_nodes\_dict \= {x.node\_id: x for x in dense\_result.nodes}
    for node in sparse\_result.nodes:
        if node.node\_id not in all\_nodes\_dict:
            all\_nodes\_dict\[node.node\_id\] \= node

    \# normalize sparse similarities from 0 to 1
    sparse\_similarities \= \[x\[0\] for x in sparse\_result\_tuples\]
    max\_sparse\_sim \= max(sparse\_similarities)
    min\_sparse\_sim \= min(sparse\_similarities)
    sparse\_similarities \= \[
        (x \- min\_sparse\_sim) / (max\_sparse\_sim \- min\_sparse\_sim)
        for x in sparse\_similarities
    \]
    sparse\_per\_node \= {
        sparse\_result\_tuples\[i\]\[1\].node\_id: x
        for i, x in enumerate(sparse\_similarities)
    }

    \# normalize dense similarities from 0 to 1
    dense\_similarities \= \[x\[0\] for x in dense\_result\_tuples\]
    max\_dense\_sim \= max(dense\_similarities)
    min\_dense\_sim \= min(dense\_similarities)
    dense\_similarities \= \[
        (x \- min\_dense\_sim) / (max\_dense\_sim \- min\_dense\_sim)
        for x in dense\_similarities
    \]
    dense\_per\_node \= {
        dense\_result\_tuples\[i\]\[1\].node\_id: x
        for i, x in enumerate(dense\_similarities)
    }

    \# fuse the scores
    fused\_similarities \= \[\]
    for node\_id in all\_nodes\_dict:
        sparse\_sim \= sparse\_per\_node.get(node\_id, 0)
        dense\_sim \= dense\_per\_node.get(node\_id, 0)
        fused\_sim \= alpha \* (sparse\_sim + dense\_sim)
        fused\_similarities.append((fused\_sim, all\_nodes\_dict\[node\_id\]))

    fused\_similarities.sort(key\=lambda x: x\[0\], reverse\=True)
    fused\_similarities \= fused\_similarities\[:top\_k\]

    \# create final response object
    return VectorStoreQueryResult(
        nodes\=\[x\[1\] for x in fused\_similarities\],
        similarities\=\[x\[0\] for x in fused\_similarities\],
        ids\=\[x\[1\].node\_id for x in fused\_similarities\],
    )

from llama\_index.core.vector\_stores import VectorStoreQueryResult def relative\_score\_fusion( dense\_result: VectorStoreQueryResult, sparse\_result: VectorStoreQueryResult, alpha: float = 0.5, # passed in from the query engine top\_k: int = 2, # passed in from the query engine i.e. similarity\_top\_k ) -> VectorStoreQueryResult: """ Fuse dense and sparse results using relative score fusion. """ # sanity check assert dense\_result.nodes is not None assert dense\_result.similarities is not None assert sparse\_result.nodes is not None assert sparse\_result.similarities is not None # deconstruct results sparse\_result\_tuples = list( zip(sparse\_result.similarities, sparse\_result.nodes) ) sparse\_result\_tuples.sort(key=lambda x: x\[0\], reverse=True) dense\_result\_tuples = list( zip(dense\_result.similarities, dense\_result.nodes) ) dense\_result\_tuples.sort(key=lambda x: x\[0\], reverse=True) # track nodes in both results all\_nodes\_dict = {x.node\_id: x for x in dense\_result.nodes} for node in sparse\_result.nodes: if node.node\_id not in all\_nodes\_dict: all\_nodes\_dict\[node.node\_id\] = node # normalize sparse similarities from 0 to 1 sparse\_similarities = \[x\[0\] for x in sparse\_result\_tuples\] max\_sparse\_sim = max(sparse\_similarities) min\_sparse\_sim = min(sparse\_similarities) sparse\_similarities = \[ (x - min\_sparse\_sim) / (max\_sparse\_sim - min\_sparse\_sim) for x in sparse\_similarities \] sparse\_per\_node = { sparse\_result\_tuples\[i\]\[1\].node\_id: x for i, x in enumerate(sparse\_similarities) } # normalize dense similarities from 0 to 1 dense\_similarities = \[x\[0\] for x in dense\_result\_tuples\] max\_dense\_sim = max(dense\_similarities) min\_dense\_sim = min(dense\_similarities) dense\_similarities = \[ (x - min\_dense\_sim) / (max\_dense\_sim - min\_dense\_sim) for x in dense\_similarities \] dense\_per\_node = { dense\_result\_tuples\[i\]\[1\].node\_id: x for i, x in enumerate(dense\_similarities) } # fuse the scores fused\_similarities = \[\] for node\_id in all\_nodes\_dict: sparse\_sim = sparse\_per\_node.get(node\_id, 0) dense\_sim = dense\_per\_node.get(node\_id, 0) fused\_sim = alpha \* (sparse\_sim + dense\_sim) fused\_similarities.append((fused\_sim, all\_nodes\_dict\[node\_id\])) fused\_similarities.sort(key=lambda x: x\[0\], reverse=True) fused\_similarities = fused\_similarities\[:top\_k\] # create final response object return VectorStoreQueryResult( nodes=\[x\[1\] for x in fused\_similarities\], similarities=\[x\[0\] for x in fused\_similarities\], ids=\[x\[1\].node\_id for x in fused\_similarities\], )

In \[ \]:

Copied!

vector\_store \= QdrantVectorStore(
    "llama2\_paper",
    client\=client,
    enable\_hybrid\=True,
    hybrid\_fusion\_fn\=relative\_score\_fusion,
)

vector\_store = QdrantVectorStore( "llama2\_paper", client=client, enable\_hybrid=True, hybrid\_fusion\_fn=relative\_score\_fusion, )

You may have noticed the alpha parameter in the above function. This can be set directely in the `as_query_engine()` call, which will set it in the vector index retriever.

In \[ \]:

Copied!

index.as\_query\_engine(alpha\=0.5, similarity\_top\_k\=2)

index.as\_query\_engine(alpha=0.5, similarity\_top\_k=2)

### Customizing Hybrid Qdrant Collections[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_hybrid/#customizing-hybrid-qdrant-collections)

Instead of letting llama-index do it, you can also configure your Qdrant hybrid collections ahead of time.

**NOTE:** The names of vector configs must be `text-dense` and `text-sparse` if creating a hybrid index.

In \[ \]:

Copied!

from qdrant\_client import models

client.recreate\_collection(
    collection\_name\="llama2\_paper",
    vectors\_config\={
        "text-dense": models.VectorParams(
            size\=1536,  \# openai vector size
            distance\=models.Distance.COSINE,
        )
    },
    sparse\_vectors\_config\={
        "text-sparse": models.SparseVectorParams(
            index\=models.SparseIndexParams()
        )
    },
)

\# enable hybrid since we created a sparse collection
vector\_store \= QdrantVectorStore(
    collection\_name\="llama2\_paper", client\=client, enable\_hybrid\=True
)

from qdrant\_client import models client.recreate\_collection( collection\_name="llama2\_paper", vectors\_config={ "text-dense": models.VectorParams( size=1536, # openai vector size distance=models.Distance.COSINE, ) }, sparse\_vectors\_config={ "text-sparse": models.SparseVectorParams( index=models.SparseIndexParams() ) }, ) # enable hybrid since we created a sparse collection vector\_store = QdrantVectorStore( collection\_name="llama2\_paper", client=client, enable\_hybrid=True )

Back to top

[Previous Hybrid Search with Qdrant BM42](https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_bm42/)[Next Component Guides](https://docs.llamaindex.ai/en/stable/module_guides/)
