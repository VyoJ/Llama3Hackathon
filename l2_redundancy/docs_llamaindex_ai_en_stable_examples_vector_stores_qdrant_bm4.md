Title: Hybrid Search with Qdrant BM42

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_bm42/

Markdown Content:
Hybrid Search with Qdrant BM42 - LlamaIndex


Qdrant recently released a new lightweight approach to sparse embeddings, [BM42](https://qdrant.tech/articles/bm42/).

In this notebook, we walk through how to use BM42 with llama-index, for effecient hybrid search.

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_bm42/#setup)
----------------------------------------------------------------------------------------

First, we need a few packages

*   `llama-index`
*   `llama-index-vector-stores-qdrant`
*   `fastembed` or `fastembed-gpu`

`llama-index` will automatically run fastembed models on GPU if the provided libraries are installed. Check out their [full installation guide](https://qdrant.github.io/fastembed/examples/FastEmbed_GPU/).

In \[ \]:

Copied!

%pip install llama\-index llama\-index\-vector\-stores\-qdrant fastembed

%pip install llama-index llama-index-vector-stores-qdrant fastembed

(Optional) Test the fastembed package[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_bm42/#optional-test-the-fastembed-package)
------------------------------------------------------------------------------------------------------------------------------------------------------

To confirm the installation worked (and also to confirm GPU usage, if used), we can run the following code.

This will first download (and cache) the model locally, and then embed it.

In \[ \]:

Copied!

from fastembed import SparseTextEmbedding

model \= SparseTextEmbedding(
    model\_name\="Qdrant/bm42-all-minilm-l6-v2-attentions",
    \# if using fastembed-gpu with cuda+onnx installed
    \# providers=\["CudaExecutionProvider"\],
)

embeddings \= model.embed(\["hello world", "goodbye world"\])

indices, values \= zip(
    \*\[
        (embedding.indices.tolist(), embedding.values.tolist())
        for embedding in embeddings
    \]
)

print(indices\[0\], values\[0\])

from fastembed import SparseTextEmbedding model = SparseTextEmbedding( model\_name="Qdrant/bm42-all-minilm-l6-v2-attentions", # if using fastembed-gpu with cuda+onnx installed # providers=\["CudaExecutionProvider"\], ) embeddings = model.embed(\["hello world", "goodbye world"\]) indices, values = zip( \*\[ (embedding.indices.tolist(), embedding.values.tolist()) for embedding in embeddings \] ) print(indices\[0\], values\[0\])

Fetching 6 files:   0%|          | 0/6 \[00:00<?, ?it/s\]

\[613153351, 74040069\] \[0.3703993395381275, 0.3338314745830077\]

Construct our Hybrid Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_bm42/#construct-our-hybrid-index)
----------------------------------------------------------------------------------------------------------------------------------

In llama-index, we can construct a hybrid index in just a few lines of code.

If you've tried hybrid in the past with splade, you will notice that this is much faster!

### Loading Data[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_bm42/#loading-data)

Here, we use `llama-parse` to read in the Llama2 paper! Using the JSON result mode, we can get detailed data about each page, including layout and images. For now, we will use the page numbers and text.

You can get a free api key for `llama-parse` by visiting [https://cloud.llamaindex.ai](https://cloud.llamaindex.ai/)

In \[ \]:

Copied!

!mkdir \-p 'data/'
!wget \--user\-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" \-O "data/llama2.pdf"

!mkdir -p 'data/' !wget --user-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" -O "data/llama2.pdf"

In \[ \]:

Copied!

import nest\_asyncio

nest\_asyncio.apply()

import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

from llama\_parse import LlamaParse
from llama\_index.core import Document

parser \= LlamaParse(result\_type\="text", api\_key\="llx-...")

\# get per-page results, along with detailed layout info and metadata
json\_data \= parser.get\_json\_result("data/llama2.pdf")

documents \= \[\]
for document\_json in json\_data:
    for page in document\_json\["pages"\]:
        documents.append(
            Document(text\=page\["text"\], metadata\={"page\_number": page\["page"\]})
        )

from llama\_parse import LlamaParse from llama\_index.core import Document parser = LlamaParse(result\_type="text", api\_key="llx-...") # get per-page results, along with detailed layout info and metadata json\_data = parser.get\_json\_result("data/llama2.pdf") documents = \[\] for document\_json in json\_data: for page in document\_json\["pages"\]: documents.append( Document(text=page\["text"\], metadata={"page\_number": page\["page"\]}) )

Started parsing the file under job\_id cac11eca-4058-4a89-a94a-5603dea3d851

### Construct the Index /w Qdrant[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_bm42/#construct-the-index-w-qdrant)

With our nodes, we can construct our index with Qdrant and BM42!

In this case, Qdrant is being hosted in a docker container.

You can pull the latest:

```
docker pull qdrant/qdrant
```

And then to launch:

```
docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant
```

In \[ \]:

Copied!

import qdrant\_client
from llama\_index.vector\_stores.qdrant import QdrantVectorStore

client \= qdrant\_client.QdrantClient("http://localhost:6333")
aclient \= qdrant\_client.AsyncQdrantClient("http://localhost:6333")

\# delete collection if it exists
if client.collection\_exists("llama2\_bm42"):
    client.delete\_collection("llama2\_bm42")

vector\_store \= QdrantVectorStore(
    collection\_name\="llama2\_bm42",
    client\=client,
    aclient\=aclient,
    fastembed\_sparse\_model\="Qdrant/bm42-all-minilm-l6-v2-attentions",
)

import qdrant\_client from llama\_index.vector\_stores.qdrant import QdrantVectorStore client = qdrant\_client.QdrantClient("http://localhost:6333") aclient = qdrant\_client.AsyncQdrantClient("http://localhost:6333") # delete collection if it exists if client.collection\_exists("llama2\_bm42"): client.delete\_collection("llama2\_bm42") vector\_store = QdrantVectorStore( collection\_name="llama2\_bm42", client=client, aclient=aclient, fastembed\_sparse\_model="Qdrant/bm42-all-minilm-l6-v2-attentions", )

Both client and aclient are provided. If using \`:memory:\` mode, the data between clients is not synced.

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, StorageContext
from llama\_index.embeddings.openai import OpenAIEmbedding

storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents,
    \# our dense embedding model
    embed\_model\=OpenAIEmbedding(
        model\_name\="text-embedding-3-small", api\_key\="sk-proj-..."
    ),
    storage\_context\=storage\_context,
)

from llama\_index.core import VectorStoreIndex, StorageContext from llama\_index.embeddings.openai import OpenAIEmbedding storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, # our dense embedding model embed\_model=OpenAIEmbedding( model\_name="text-embedding-3-small", api\_key="sk-proj-..." ), storage\_context=storage\_context, )

As we can see, both the dense and sparse embeddings were generated super quickly!

Even though the sparse model is running locally on CPU, its very small and fast.

Test out the Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_bm42/#test-out-the-index)
------------------------------------------------------------------------------------------------------------------

Using the powers of sparse embeddings, we can query for some very specific facts, and get the correct data.

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI

chat\_engine \= index.as\_chat\_engine(
    chat\_mode\="condense\_plus\_context",
    llm\=OpenAI(model\="gpt-4o", api\_key\="sk-proj-..."),
)

from llama\_index.llms.openai import OpenAI chat\_engine = index.as\_chat\_engine( chat\_mode="condense\_plus\_context", llm=OpenAI(model="gpt-4o", api\_key="sk-proj-..."), )

In \[ \]:

Copied!

response \= chat\_engine.chat("What training hardware was used for Llama2?")
print(str(response))

response = chat\_engine.chat("What training hardware was used for Llama2?") print(str(response))

The training hardware for Llama 2 included Meta’s Research Super Cluster (RSC) and internal production clusters. Both clusters utilized NVIDIA A100 GPUs. There were two key differences between these clusters:

1. \*\*Interconnect Type\*\*:
   - RSC used NVIDIA Quantum InfiniBand.
   - The internal production cluster used a RoCE (RDMA over Converged Ethernet) solution based on commodity Ethernet switches.

2. \*\*Per-GPU Power Consumption Cap\*\*:
   - RSC had a power consumption cap of 400W per GPU.
   - The internal production cluster had a power consumption cap of 350W per GPU.

This setup allowed for a comparison of the suitability of these different types of interconnects for large-scale training.

In \[ \]:

Copied!

response \= chat\_engine.chat("What is the main idea of Llama2?")
print(str(response))

response = chat\_engine.chat("What is the main idea of Llama2?") print(str(response))

The main idea of Llama 2 is to provide an updated and improved version of the original Llama model, designed to be more efficient, scalable, and safe for various applications, including research and commercial use. Here are the key aspects of Llama 2:

1. \*\*Enhanced Pretraining\*\*: Llama 2 is trained on a new mix of publicly available data, with a 40% increase in the size of the pretraining corpus compared to Llama 1. This aims to improve the model's performance and knowledge base.

2. \*\*Improved Architecture\*\*: The model incorporates several architectural enhancements, such as increased context length and grouped-query attention (GQA), to improve inference scalability and overall performance.

3. \*\*Safety and Responsiveness\*\*: Llama 2-Chat, a fine-tuned version of Llama 2, is optimized for dialogue use cases. It undergoes supervised fine-tuning and iterative refinement using Reinforcement Learning with Human Feedback (RLHF) to ensure safer and more helpful interactions.

4. \*\*Open Release\*\*: Meta is releasing Llama 2 models with 7B, 13B, and 70B parameters to the general public for research and commercial use, promoting transparency and collaboration in the AI community.

5. \*\*Responsible Use\*\*: The release includes guidelines and code examples to facilitate the safe deployment of Llama 2 and Llama 2-Chat, emphasizing the importance of safety testing and tuning tailored to specific applications.

Overall, Llama 2 aims to be a more robust, scalable, and safer large language model that can be widely used and further developed by the AI community.

In \[ \]:

Copied!

response \= chat\_engine.chat("What was Llama2 evaluated and compared against?")
print(str(response))

response = chat\_engine.chat("What was Llama2 evaluated and compared against?") print(str(response))

Llama 2 was evaluated and compared against several other models, both open-source and closed-source, across a variety of benchmarks. Here are the key comparisons:

### Open-Source Models:
1. \*\*Llama 1\*\*: Llama 2 models were compared to their predecessors, Llama 1 models. For example, Llama 2 70B showed improvements of approximately 5 points on MMLU and 8 points on BBH compared to Llama 1 65B.
2. \*\*MPT Models\*\*: Llama 2 7B and 30B models outperformed MPT models of corresponding sizes in all categories except code benchmarks.
3. \*\*Falcon Models\*\*: Llama 2 7B and 34B models outperformed Falcon 7B and 40B models across all benchmark categories.

### Closed-Source Models:
1. \*\*GPT-3.5\*\*: Llama 2 70B was compared to GPT-3.5, showing close performance on MMLU and GSM8K but a significant gap on coding benchmarks.
2. \*\*PaLM (540B)\*\*: Llama 2 70B performed on par or better than PaLM (540B) on almost all benchmarks.
3. \*\*GPT-4 and PaLM-2-L\*\*: There remains a large performance gap between Llama 2 70B and these more advanced models.

### Benchmarks:
Llama 2 was evaluated on a variety of benchmarks, including:
1. \*\*MMLU (Massive Multitask Language Understanding)\*\*: Evaluated in a 5-shot setting.
2. \*\*BBH (Big Bench Hard)\*\*: Evaluated in a 3-shot setting.
3. \*\*AGI Eval\*\*: Evaluated in 3-5 shot settings, focusing on English tasks.
4. \*\*GSM8K\*\*: For math problem-solving.
5. \*\*Human-Eval and MBPP\*\*: For code generation.
6. \*\*NaturalQuestions and TriviaQA\*\*: For world knowledge.
7. \*\*SQUAD and QUAC\*\*: For reading comprehension.
8. \*\*BoolQ, PIQA, SIQA, Hella-Swag, ARC-e, ARC-c, NQ, TQA\*\*: Various other benchmarks for different aspects of language understanding and reasoning.

These evaluations demonstrate that Llama 2 models generally outperform their predecessors and other open-source models, while also being competitive with some of the leading closed-source models.

Loading from existing store[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_bm42/#loading-from-existing-store)
------------------------------------------------------------------------------------------------------------------------------------

With your vector index created, we can easily connect back to it!

In \[ \]:

Copied!

import qdrant\_client
from llama\_index.core import VectorStoreIndex
from llama\_index.embeddings.openai import OpenAIEmbedding
from llama\_index.vector\_stores.qdrant import QdrantVectorStore

client \= qdrant\_client.QdrantClient("http://localhost:6333")
aclient \= qdrant\_client.AsyncQdrantClient("http://localhost:6333")

\# delete collection if it exists
if client.collection\_exists("llama2\_bm42"):
    client.delete\_collection("llama2\_bm42")

vector\_store \= QdrantVectorStore(
    collection\_name\="llama2\_bm42",
    client\=client,
    aclient\=aclient,
    fastembed\_sparse\_model\="Qdrant/bm42-all-minilm-l6-v2-attentions",
)

loaded\_index \= VectorStoreIndex.from\_vector\_store(
    vector\_store,
    embed\_model\=OpenAIEmbedding(
        model\="text-embedding-3-small", api\_key\="sk-proj-..."
    ),
)

import qdrant\_client from llama\_index.core import VectorStoreIndex from llama\_index.embeddings.openai import OpenAIEmbedding from llama\_index.vector\_stores.qdrant import QdrantVectorStore client = qdrant\_client.QdrantClient("http://localhost:6333") aclient = qdrant\_client.AsyncQdrantClient("http://localhost:6333") # delete collection if it exists if client.collection\_exists("llama2\_bm42"): client.delete\_collection("llama2\_bm42") vector\_store = QdrantVectorStore( collection\_name="llama2\_bm42", client=client, aclient=aclient, fastembed\_sparse\_model="Qdrant/bm42-all-minilm-l6-v2-attentions", ) loaded\_index = VectorStoreIndex.from\_vector\_store( vector\_store, embed\_model=OpenAIEmbedding( model="text-embedding-3-small", api\_key="sk-proj-..." ), )

Back to top

[Previous Postgres Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/postgres/)[Next Qdrant Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_hybrid/)
