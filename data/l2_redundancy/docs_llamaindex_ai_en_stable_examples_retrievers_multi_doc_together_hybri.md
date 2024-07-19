Title: Chunk + Document Hybrid Retrieval with Long-Context Embeddings (Together.ai)

URL Source: https://docs.llamaindex.ai/en/stable/examples/retrievers/multi_doc_together_hybrid/

Markdown Content:
Chunk + Document Hybrid Retrieval with Long-Context Embeddings (Together.ai) - LlamaIndex


This notebook shows how to use long-context together.ai embedding models for advanced RAG. We index each document by running the embedding model over the entire document text, as well as embedding each chunk. We then define a custom retriever that can compute both node similarity as well as document similarity.

Visit [https://together.ai](https://together.ai/) and sign up to get an API key.

Setup and Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/multi_doc_together_hybrid/#setup-and-download-data)
---------------------------------------------------------------------------------------------------------------------------------------

We load in our documentation. For the sake of speed we load in just 10 pages, but of course if you want to stress test your model you should load in all of it.

In \[ \]:

Copied!

%pip install llama\-index\-embeddings\-together
%pip install llama\-index\-llms\-openai
%pip install llama\-index\-embeddings\-openai
%pip install llama\-index\-readers\-file

%pip install llama-index-embeddings-together %pip install llama-index-llms-openai %pip install llama-index-embeddings-openai %pip install llama-index-readers-file

In \[ \]:

Copied!

domain \= "docs.llamaindex.ai"
docs\_url \= "https://docs.llamaindex.ai/en/latest/"
!wget \-e robots\=off \--recursive \--no\-clobber \--page\-requisites \--html\-extension \--convert\-links \--restrict\-file\-names\=windows \--domains {domain} \--no\-parent {docs\_url}

domain = "docs.llamaindex.ai" docs\_url = "https://docs.llamaindex.ai/en/latest/" !wget -e robots=off --recursive --no-clobber --page-requisites --html-extension --convert-links --restrict-file-names=windows --domains {domain} --no-parent {docs\_url}

In \[ \]:

Copied!

from llama\_index.readers.file import UnstructuredReader
from pathlib import Path
from llama\_index.llms.openai import OpenAI
from llama\_index.core import Document

from llama\_index.readers.file import UnstructuredReader from pathlib import Path from llama\_index.llms.openai import OpenAI from llama\_index.core import Document

In \[ \]:

Copied!

reader \= UnstructuredReader()
\# all\_files\_gen = Path("./docs.llamaindex.ai/").rglob("\*")
\# all\_files = \[f.resolve() for f in all\_files\_gen\]
\# all\_html\_files = \[f for f in all\_files if f.suffix.lower()  ".html"\] # curate a subset all\_html\_files = \[ "docs.llamaindex.ai/en/latest/index.html", "docs.llamaindex.ai/en/latest/contributing/contributing.html", "docs.llamaindex.ai/en/latest/understanding/understanding.html", "docs.llamaindex.ai/en/latest/understanding/using\_llms/using\_llms.html", "docs.llamaindex.ai/en/latest/understanding/using\_llms/privacy.html", "docs.llamaindex.ai/en/latest/understanding/loading/llamahub.html", "docs.llamaindex.ai/en/latest/optimizing/production\_rag.html", "docs.llamaindex.ai/en/latest/module\_guides/models/llms.html", \] # TODO: set to higher value if you want more docs doc\_limit = 10 docs = \[\] for idx, f in enumerate(all\_html\_files): if idx > doc\_limit: break print(f"Idx {idx}/{len(all\_html\_files)}") loaded\_docs = reader.load\_data(file=f, split\_documents=True) # Hardcoded Index. Everything before this is ToC for all pages # Adjust this start\_idx to suit your needs start\_idx = 64 loaded\_doc = Document( id\_=str(f), text="\\n\\n".join(\[d.get\_content() for d in loaded\_docs\[start\_idx:\]\]), metadata={"path": str(f)}, ) print(str(f)) docs.append(loaded\_doc)

\[nltk\_data\] Downloading package punkt to /Users/jerryliu/nltk\_data...
\[nltk\_data\]   Package punkt is already up-to-date!
\[nltk\_data\] Downloading package averaged\_perceptron\_tagger to
\[nltk\_data\]     /Users/jerryliu/nltk\_data...
\[nltk\_data\]   Package averaged\_perceptron\_tagger is already up-to-
\[nltk\_data\]       date!

Idx 0/8
docs.llamaindex.ai/en/latest/index.html
Idx 1/8
docs.llamaindex.ai/en/latest/contributing/contributing.html
Idx 2/8
docs.llamaindex.ai/en/latest/understanding/understanding.html
Idx 3/8
docs.llamaindex.ai/en/latest/understanding/using\_llms/using\_llms.html
Idx 4/8
docs.llamaindex.ai/en/latest/understanding/using\_llms/privacy.html
Idx 5/8
docs.llamaindex.ai/en/latest/understanding/loading/llamahub.html
Idx 6/8
docs.llamaindex.ai/en/latest/optimizing/production\_rag.html
Idx 7/8
docs.llamaindex.ai/en/latest/module\_guides/models/llms.html

Building Hybrid Retrieval with Chunk Embedding + Parent Embedding[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/multi_doc_together_hybrid/#building-hybrid-retrieval-with-chunk-embedding-parent-embedding)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Define a custom retriever that does the following:

*   First retrieve relevant chunks based on embedding similarity
*   For each chunk, lookup the source document embedding.
*   Weight it by an alpha.

This is essentially vector retrieval with a reranking step that reweights the node similarities.

In \[ \]:

Copied!

\# You can set the API key in the embeddings or env
\# import os
\# os.environ\["TOEGETHER\_API\_KEY"\] = "your-api-key"

from llama\_index.embeddings.together import TogetherEmbedding
from llama\_index.embeddings.openai import OpenAIEmbedding
from llama\_index.llms.openai import OpenAI

api\_key \= "<api\_key>"

embed\_model \= TogetherEmbedding(
    model\_name\="togethercomputer/m2-bert-80M-32k-retrieval", api\_key\=api\_key
)

llm \= OpenAI(temperature\=0, model\="gpt-3.5-turbo")

\# You can set the API key in the embeddings or env # import os # os.environ\["TOEGETHER\_API\_KEY"\] = "your-api-key" from llama\_index.embeddings.together import TogetherEmbedding from llama\_index.embeddings.openai import OpenAIEmbedding from llama\_index.llms.openai import OpenAI api\_key = "" embed\_model = TogetherEmbedding( model\_name="togethercomputer/m2-bert-80M-32k-retrieval", api\_key=api\_key ) llm = OpenAI(temperature=0, model="gpt-3.5-turbo")

### Create Document Store[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/multi_doc_together_hybrid/#create-document-store)

Create docstore for original documents. Embed each document, and put in docstore.

We will refer to this later in our hybrid retrieval algorithm!

In \[ \]:

Copied!

from llama\_index.core.storage.docstore import SimpleDocumentStore

for doc in docs:
    embedding \= embed\_model.get\_text\_embedding(doc.get\_content())
    doc.embedding \= embedding

docstore \= SimpleDocumentStore()
docstore.add\_documents(docs)

from llama\_index.core.storage.docstore import SimpleDocumentStore for doc in docs: embedding = embed\_model.get\_text\_embedding(doc.get\_content()) doc.embedding = embedding docstore = SimpleDocumentStore() docstore.add\_documents(docs)

### Build Vector Index[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/multi_doc_together_hybrid/#build-vector-index)

Let's build the vector index of chunks. Each chunk will also have a reference to its source document through its `index_id` (which can then be used to lookup the source document in the docstore).

In \[ \]:

Copied!

from llama\_index.core.schema import IndexNode
from llama\_index.core import (
    load\_index\_from\_storage,
    StorageContext,
    VectorStoreIndex,
)
from llama\_index.core.node\_parser import SentenceSplitter
from llama\_index.core import SummaryIndex
from llama\_index.core.retrievers import RecursiveRetriever
import os
from tqdm.notebook import tqdm
import pickle

def build\_index(docs, out\_path: str \= "storage/chunk\_index"):
    nodes \= \[\]

    splitter \= SentenceSplitter(chunk\_size\=512, chunk\_overlap\=70)
    for idx, doc in enumerate(tqdm(docs)):
        \# print('Splitting: ' + str(idx))

        cur\_nodes \= splitter.get\_nodes\_from\_documents(\[doc\])
        for cur\_node in cur\_nodes:
            \# ID will be base + parent
            file\_path \= doc.metadata\["path"\]
            new\_node \= IndexNode(
                text\=cur\_node.text or "None",
                index\_id\=str(file\_path),
                metadata\=doc.metadata
                \# obj=doc
            )
            nodes.append(new\_node)
    print("num nodes: " + str(len(nodes)))

    \# save index to disk
    if not os.path.exists(out\_path):
        index \= VectorStoreIndex(nodes, embed\_model\=embed\_model)
        index.set\_index\_id("simple\_index")
        index.storage\_context.persist(f"./{out\_path}")
    else:
        \# rebuild storage context
        storage\_context \= StorageContext.from\_defaults(
            persist\_dir\=f"./{out\_path}"
        )
        \# load index
        index \= load\_index\_from\_storage(
            storage\_context, index\_id\="simple\_index", embed\_model\=embed\_model
        )

    return index

from llama\_index.core.schema import IndexNode from llama\_index.core import ( load\_index\_from\_storage, StorageContext, VectorStoreIndex, ) from llama\_index.core.node\_parser import SentenceSplitter from llama\_index.core import SummaryIndex from llama\_index.core.retrievers import RecursiveRetriever import os from tqdm.notebook import tqdm import pickle def build\_index(docs, out\_path: str = "storage/chunk\_index"): nodes = \[\] splitter = SentenceSplitter(chunk\_size=512, chunk\_overlap=70) for idx, doc in enumerate(tqdm(docs)): # print('Splitting: ' + str(idx)) cur\_nodes = splitter.get\_nodes\_from\_documents(\[doc\]) for cur\_node in cur\_nodes: # ID will be base + parent file\_path = doc.metadata\["path"\] new\_node = IndexNode( text=cur\_node.text or "None", index\_id=str(file\_path), metadata=doc.metadata # obj=doc ) nodes.append(new\_node) print("num nodes: " + str(len(nodes))) # save index to disk if not os.path.exists(out\_path): index = VectorStoreIndex(nodes, embed\_model=embed\_model) index.set\_index\_id("simple\_index") index.storage\_context.persist(f"./{out\_path}") else: # rebuild storage context storage\_context = StorageContext.from\_defaults( persist\_dir=f"./{out\_path}" ) # load index index = load\_index\_from\_storage( storage\_context, index\_id="simple\_index", embed\_model=embed\_model ) return index

In \[ \]:

Copied!

index \= build\_index(docs)

index = build\_index(docs)

### Define Hybrid Retriever[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/multi_doc_together_hybrid/#define-hybrid-retriever)

We define a hybrid retriever that can first fetch chunks by vector similarity, and then reweight it based on similarity with the parent document (using an alpha parameter).

In \[ \]:

Copied!

from llama\_index.core.retrievers import BaseRetriever
from llama\_index.core.indices.query.embedding\_utils import get\_top\_k\_embeddings
from llama\_index.core import QueryBundle
from llama\_index.core.schema import NodeWithScore
from typing import List, Any, Optional

class HybridRetriever(BaseRetriever):
    """Hybrid retriever."""

    def \_\_init\_\_(
        self,
        vector\_index,
        docstore,
        similarity\_top\_k: int \= 2,
        out\_top\_k: Optional\[int\] \= None,
        alpha: float \= 0.5,
        \*\*kwargs: Any,
    ) \-> None:
        """Init params."""
        super().\_\_init\_\_(\*\*kwargs)
        self.\_vector\_index \= vector\_index
        self.\_embed\_model \= vector\_index.\_embed\_model
        self.\_retriever \= vector\_index.as\_retriever(
            similarity\_top\_k\=similarity\_top\_k
        )
        self.\_out\_top\_k \= out\_top\_k or similarity\_top\_k
        self.\_docstore \= docstore
        self.\_alpha \= alpha

    def \_retrieve(self, query\_bundle: QueryBundle) \-> List\[NodeWithScore\]:
        """Retrieve nodes given query."""

        \# first retrieve chunks
        nodes \= self.\_retriever.retrieve(query\_bundle.query\_str)

        \# get documents, and embedding similiaryt between query and documents

        \## get doc embeddings
        docs \= \[self.\_docstore.get\_document(n.node.index\_id) for n in nodes\]
        doc\_embeddings \= \[d.embedding for d in docs\]
        query\_embedding \= self.\_embed\_model.get\_query\_embedding(
            query\_bundle.query\_str
        )

        \## compute doc similarities
        doc\_similarities, doc\_idxs \= get\_top\_k\_embeddings(
            query\_embedding, doc\_embeddings
        )

        \## compute final similarity with doc similarities and original node similarity
        result\_tups \= \[\]
        for doc\_idx, doc\_similarity in zip(doc\_idxs, doc\_similarities):
            node \= nodes\[doc\_idx\]
            \# weight alpha \* node similarity + (1-alpha) \* doc similarity
            full\_similarity \= (self.\_alpha \* node.score) + (
                (1 \- self.\_alpha) \* doc\_similarity
            )
            print(
                f"Doc {doc\_idx} (node score, doc similarity, full similarity): {(node.score, doc\_similarity, full\_similarity)}"
            )
            result\_tups.append((full\_similarity, node))

        result\_tups \= sorted(result\_tups, key\=lambda x: x\[0\], reverse\=True)
        \# update scores
        for full\_score, node in result\_tups:
            node.score \= full\_score

        return \[n for \_, n in result\_tups\]\[:out\_top\_k\]

from llama\_index.core.retrievers import BaseRetriever from llama\_index.core.indices.query.embedding\_utils import get\_top\_k\_embeddings from llama\_index.core import QueryBundle from llama\_index.core.schema import NodeWithScore from typing import List, Any, Optional class HybridRetriever(BaseRetriever): """Hybrid retriever.""" def \_\_init\_\_( self, vector\_index, docstore, similarity\_top\_k: int = 2, out\_top\_k: Optional\[int\] = None, alpha: float = 0.5, \*\*kwargs: Any, ) -> None: """Init params.""" super().\_\_init\_\_(\*\*kwargs) self.\_vector\_index = vector\_index self.\_embed\_model = vector\_index.\_embed\_model self.\_retriever = vector\_index.as\_retriever( similarity\_top\_k=similarity\_top\_k ) self.\_out\_top\_k = out\_top\_k or similarity\_top\_k self.\_docstore = docstore self.\_alpha = alpha def \_retrieve(self, query\_bundle: QueryBundle) -> List\[NodeWithScore\]: """Retrieve nodes given query.""" # first retrieve chunks nodes = self.\_retriever.retrieve(query\_bundle.query\_str) # get documents, and embedding similiaryt between query and documents ## get doc embeddings docs = \[self.\_docstore.get\_document(n.node.index\_id) for n in nodes\] doc\_embeddings = \[d.embedding for d in docs\] query\_embedding = self.\_embed\_model.get\_query\_embedding( query\_bundle.query\_str ) ## compute doc similarities doc\_similarities, doc\_idxs = get\_top\_k\_embeddings( query\_embedding, doc\_embeddings ) ## compute final similarity with doc similarities and original node similarity result\_tups = \[\] for doc\_idx, doc\_similarity in zip(doc\_idxs, doc\_similarities): node = nodes\[doc\_idx\] # weight alpha \* node similarity + (1-alpha) \* doc similarity full\_similarity = (self.\_alpha \* node.score) + ( (1 - self.\_alpha) \* doc\_similarity ) print( f"Doc {doc\_idx} (node score, doc similarity, full similarity): {(node.score, doc\_similarity, full\_similarity)}" ) result\_tups.append((full\_similarity, node)) result\_tups = sorted(result\_tups, key=lambda x: x\[0\], reverse=True) # update scores for full\_score, node in result\_tups: node.score = full\_score return \[n for \_, n in result\_tups\]\[:out\_top\_k\]

In \[ \]:

Copied!

top\_k \= 10
out\_top\_k \= 3
hybrid\_retriever \= HybridRetriever(
    index, docstore, similarity\_top\_k\=top\_k, out\_top\_k\=3, alpha\=0.5
)
base\_retriever \= index.as\_retriever(similarity\_top\_k\=out\_top\_k)

top\_k = 10 out\_top\_k = 3 hybrid\_retriever = HybridRetriever( index, docstore, similarity\_top\_k=top\_k, out\_top\_k=3, alpha=0.5 ) base\_retriever = index.as\_retriever(similarity\_top\_k=out\_top\_k)

In \[ \]:

Copied!

def show\_nodes(nodes, out\_len: int \= 200):
    for idx, n in enumerate(nodes):
        print(f"\\n\\n >>>>>>>>>>>> ID {n.id\_}: {n.metadata\['path'\]}")
        print(n.get\_content()\[:out\_len\])

def show\_nodes(nodes, out\_len: int = 200): for idx, n in enumerate(nodes): print(f"\\n\\n >>>>>>>>>>>> ID {n.id\_}: {n.metadata\['path'\]}") print(n.get\_content()\[:out\_len\])

In \[ \]:

Copied!

query\_str \= "Tell me more about the LLM interface and where they're used"

query\_str = "Tell me more about the LLM interface and where they're used"

In \[ \]:

Copied!

nodes \= hybrid\_retriever.retrieve(query\_str)

nodes = hybrid\_retriever.retrieve(query\_str)

Doc 0 (node score, doc similarity, full similarity): (0.8951729860296237, 0.888711859390314, 0.8919424227099688)
Doc 3 (node score, doc similarity, full similarity): (0.7606735418349336, 0.888711859390314, 0.8246927006126239)
Doc 1 (node score, doc similarity, full similarity): (0.8008658562229534, 0.888711859390314, 0.8447888578066337)
Doc 4 (node score, doc similarity, full similarity): (0.7083936595542725, 0.888711859390314, 0.7985527594722932)
Doc 2 (node score, doc similarity, full similarity): (0.7627518988051541, 0.7151744680533735, 0.7389631834292638)
Doc 5 (node score, doc similarity, full similarity): (0.6576277615091234, 0.6506473659825045, 0.654137563745814)
Doc 7 (node score, doc similarity, full similarity): (0.6141130778320664, 0.6159139530209246, 0.6150135154264955)
Doc 6 (node score, doc similarity, full similarity): (0.6225339833394525, 0.24827341793941335, 0.43540370063943296)
Doc 8 (node score, doc similarity, full similarity): (0.5672766061523489, 0.24827341793941335, 0.4077750120458811)
Doc 9 (node score, doc similarity, full similarity): (0.5671131641337652, 0.24827341793941335, 0.4076932910365893)

In \[ \]:

Copied!

show\_nodes(nodes)

show\_nodes(nodes)

 >>>>>>>>>>>> ID 2c7b42d3-520c-4510-ba34-d2f2dfd5d8f5: docs.llamaindex.ai/en/latest/module\_guides/models/llms.html
Contributing: Anyone is welcome to contribute new LLMs to the documentation. Simply copy an existing notebook, setup and test your LLM, and open a PR with your results.

If you have ways to improve th


 >>>>>>>>>>>> ID 72cc9101-5b36-4821-bd50-e707dac8dca1: docs.llamaindex.ai/en/latest/module\_guides/models/llms.html
Using LLMs

Concept

Picking the proper Large Language Model (LLM) is one of the first steps you need to consider when building any LLM application over your data.

LLMs are a core component of Llam


 >>>>>>>>>>>> ID 7c2be7c7-44aa-4f11-b670-e402e5ac35a5: docs.llamaindex.ai/en/latest/module\_guides/models/llms.html
If you change the LLM, you may need to update this tokenizer to ensure accurate token counts, chunking, and prompting.

The single requirement for a tokenizer is that it is a callable function, that t

In \[ \]:

Copied!

base\_nodes \= base\_retriever.retrieve(query\_str)

base\_nodes = base\_retriever.retrieve(query\_str)

In \[ \]:

Copied!

show\_nodes(base\_nodes)

show\_nodes(base\_nodes)

 >>>>>>>>>>>> ID 2c7b42d3-520c-4510-ba34-d2f2dfd5d8f5: docs.llamaindex.ai/en/latest/module\_guides/models/llms.html
Contributing: Anyone is welcome to contribute new LLMs to the documentation. Simply copy an existing notebook, setup and test your LLM, and open a PR with your results.

If you have ways to improve th


 >>>>>>>>>>>> ID 72cc9101-5b36-4821-bd50-e707dac8dca1: docs.llamaindex.ai/en/latest/module\_guides/models/llms.html
Using LLMs

Concept

Picking the proper Large Language Model (LLM) is one of the first steps you need to consider when building any LLM application over your data.

LLMs are a core component of Llam


 >>>>>>>>>>>> ID 252fc99b-2817-4913-bcbf-4dd8ef509b8c: docs.llamaindex.ai/en/latest/index.html
These could be APIs, PDFs, SQL, and (much) more.

Data indexes structure your data in intermediate representations that are easy and performant for LLMs to consume.

Engines provide natural language a

Run Some Queries[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/multi_doc_together_hybrid/#run-some-queries)
-------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core.query\_engine import RetrieverQueryEngine

query\_engine \= RetrieverQueryEngine(hybrid\_retriever)
base\_query\_engine \= index.as\_query\_engine(similarity\_top\_k\=out\_top\_k)

from llama\_index.core.query\_engine import RetrieverQueryEngine query\_engine = RetrieverQueryEngine(hybrid\_retriever) base\_query\_engine = index.as\_query\_engine(similarity\_top\_k=out\_top\_k)

In \[ \]:

Copied!

response \= query\_engine.query(query\_str)
print(str(response))

response = query\_engine.query(query\_str) print(str(response))

Doc 0 (node score, doc similarity, full similarity): (0.8951729860296237, 0.888711859390314, 0.8919424227099688)
Doc 3 (node score, doc similarity, full similarity): (0.7606735418349336, 0.888711859390314, 0.8246927006126239)
Doc 1 (node score, doc similarity, full similarity): (0.8008658562229534, 0.888711859390314, 0.8447888578066337)
Doc 4 (node score, doc similarity, full similarity): (0.7083936595542725, 0.888711859390314, 0.7985527594722932)
Doc 2 (node score, doc similarity, full similarity): (0.7627518988051541, 0.7151744680533735, 0.7389631834292638)
Doc 5 (node score, doc similarity, full similarity): (0.6576277615091234, 0.6506473659825045, 0.654137563745814)
Doc 7 (node score, doc similarity, full similarity): (0.6141130778320664, 0.6159139530209246, 0.6150135154264955)
Doc 6 (node score, doc similarity, full similarity): (0.6225339833394525, 0.24827341793941335, 0.43540370063943296)
Doc 8 (node score, doc similarity, full similarity): (0.5672766061523489, 0.24827341793941335, 0.4077750120458811)
Doc 9 (node score, doc similarity, full similarity): (0.5671131641337652, 0.24827341793941335, 0.4076932910365893)
The LLM interface is a unified interface provided by LlamaIndex for defining Large Language Models (LLMs) from different sources such as OpenAI, Hugging Face, or LangChain. This interface eliminates the need to write the boilerplate code for defining the LLM interface yourself. The LLM interface supports text completion and chat endpoints, as well as streaming and non-streaming endpoints. It also supports both synchronous and asynchronous endpoints.

LLMs are a core component of LlamaIndex and can be used as standalone modules or plugged into other core LlamaIndex modules such as indices, retrievers, and query engines. They are primarily used during the response synthesis step, which occurs after retrieval. Depending on the type of index being used, LLMs may also be used during index construction, insertion, and query traversal.

To use LLMs, you can import the necessary modules and instantiate the LLM object. You can then use the LLM object to generate responses or complete text prompts. LlamaIndex provides examples and code snippets to help you get started with using LLMs.

It's important to note that tokenization plays a crucial role in LLMs. LlamaIndex uses a global tokenizer by default, but if you change the LLM, you may need to update the tokenizer to ensure accurate token counts, chunking, and prompting. LlamaIndex provides instructions on how to set a global tokenizer using libraries like tiktoken or Hugging Face's AutoTokenizer.

Overall, LLMs are powerful tools for building LlamaIndex applications and can be customized within the LlamaIndex abstractions. While LLMs from paid APIs like OpenAI and Anthropic are generally considered more reliable, local open-source models are gaining popularity due to their customizability and transparency. LlamaIndex offers integrations with various LLMs and provides documentation on their compatibility and performance. Contributions to improve the setup and performance of existing LLMs or to add new LLMs are welcome.

In \[ \]:

Copied!

base\_response \= base\_query\_engine.query(query\_str)
print(str(base\_response))

base\_response = base\_query\_engine.query(query\_str) print(str(base\_response))

The LLM interface is a unified interface provided by LlamaIndex for defining Large Language Model (LLM) modules. It allows users to easily integrate LLMs from different providers such as OpenAI, Hugging Face, or LangChain into their applications without having to write the boilerplate code for defining the LLM interface themselves.

LLMs are a core component of LlamaIndex and can be used as standalone modules or plugged into other core LlamaIndex modules such as indices, retrievers, and query engines. They are primarily used during the response synthesis step, which occurs after retrieval. Depending on the type of index being used, LLMs may also be used during index construction, insertion, and query traversal.

The LLM interface supports various functionalities, including text completion and chat endpoints. It also provides support for streaming and non-streaming endpoints, as well as synchronous and asynchronous endpoints.

To use LLMs, you can import the necessary modules and make use of the provided functions. For example, you can use the OpenAI module to interact with the gpt-3.5-turbo LLM by calling the \`OpenAI()\` function. You can then use the \`complete()\` function to generate completions based on a given prompt.

It's important to note that LlamaIndex uses a global tokenizer called cl100k from tiktoken by default for all token counting. If you change the LLM being used, you may need to update the tokenizer to ensure accurate token counts, chunking, and prompting.

Overall, LLMs and the LLM interface provided by LlamaIndex are essential for building LLM applications and integrating them into the LlamaIndex ecosystem.

Back to top

[Previous Ensemble Retrieval Guide](https://docs.llamaindex.ai/en/stable/examples/retrievers/ensemble_retrieval/)[Next Pathway Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/pathway_retriever/)
