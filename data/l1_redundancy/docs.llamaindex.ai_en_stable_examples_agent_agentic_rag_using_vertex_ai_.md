Title: Agentic rag using vertex ai

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/

Markdown Content:
Agentic rag using vertex ai - LlamaIndex


       

Build Agentic RAG with Llamaindex for Vertex AI[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/#build-agentic-rag-with-llamaindex-for-vertex-ai)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/docs/examples/agent/agentic_rag_using_vertex_ai.ipynb)

### Pre-requisites[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/#pre-requisites)

*   Set up a Google Cloud project
*   Create a Google Cloud storage bucket

#### References:[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/#references)

1.  Set up Vertex AI Vector Search

*   [https://colab.sandbox.google.com/github/run-llama/llama\_index/blob/main/docs/docs/examples/vector\_stores/VertexAIVectorSearchDemo.ipynb#scrollTo=\_X0bKO2mnBHK](https://colab.sandbox.google.com/github/run-llama/llama_index/blob/main/docs/docs/examples/vector_stores/VertexAIVectorSearchDemo.ipynb#scrollTo=_X0bKO2mnBHK)

2.  Building Agentic RAG with Llamaindex Tutorial

*   [https://learn.deeplearning.ai/courses/building-agentic-rag-with-llamaindex/lesson/2/router-query-engine](https://learn.deeplearning.ai/courses/building-agentic-rag-with-llamaindex/lesson/2/router-query-engine)

### Install Libraries[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/#install-libraries)

In \[ \]:

Copied!

!pip install \--upgrade google\-cloud\-aiplatform llama\-index\-vector\-stores\-vertexaivectorsearch llama\-index llama\_index\-llms\-vertex

!pip install --upgrade google-cloud-aiplatform llama-index-vector-stores-vertexaivectorsearch llama-index llama\_index-llms-vertex

### Restart current runtime[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/#restart-current-runtime)

To use the newly installed packages in this Jupyter runtime, you must restart the runtime. You can do this by running the cell below, which will restart the current kernel.

In \[ \]:

Copied!

\# Colab only
\# Automatically restart kernel after installs so that your environment can access the new packages
import IPython

app \= IPython.Application.instance()
app.kernel.do\_shutdown(True)

\# Colab only # Automatically restart kernel after installs so that your environment can access the new packages import IPython app = IPython.Application.instance() app.kernel.do\_shutdown(True)

### Authenticate your notebook environment (Colab only)[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/#authenticate-your-notebook-environment-colab-only)

If you are running this notebook on Google Colab, you will need to authenticate your environment. To do this, run the new cell below. This step is not required if you are using [Vertex AI Workbench](https://cloud.google.com/vertex-ai-workbench).

In \[ \]:

Copied!

\# Colab only
import sys

if "google.colab" in sys.modules:
    from google.colab import auth

    auth.authenticate\_user()

\# Colab only import sys if "google.colab" in sys.modules: from google.colab import auth auth.authenticate\_user()

In \[ \]:

Copied!

\# If you're using JupyterLab instance, uncomment and run the below code.
#!gcloud auth login

\# If you're using JupyterLab instance, uncomment and run the below code. #!gcloud auth login

### Define Google Cloud project information and initialize Vertex AI[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/#define-google-cloud-project-information-and-initialize-vertex-ai)

Initialize the Vertex AI SDK for Python for your project:

In \[ \]:

Copied!

\# TODO : Set values as per your requirements

\# Project and Storage Constants
PROJECT\_ID \= "<your project>"
REGION \= "<your region>"
GCS\_BUCKET\_NAME \= f"{PROJECT\_ID}"
GCS\_BUCKET\_URI \= f"gs://{GCS\_BUCKET\_NAME}"

\# The number of dimensions for the textembedding-gecko@003 is 768
\# If other embedder is used, the dimensions would probably need to change.
VS\_DIMENSIONS \= 768

\# Vertex AI Vector Search Index configuration
\# parameter description here
\# https://cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.MatchingEngineIndex#google\_cloud\_aiplatform\_MatchingEngineIndex\_create\_tree\_ah\_index
VS\_INDEX\_NAME \= "vertex\_vector\_search\_index"  \# @param {type:"string"}
VS\_INDEX\_ENDPOINT\_NAME \= "vector\_search\_endpoint"  \# @param {type:"string"}

\# TODO : Set values as per your requirements # Project and Storage Constants PROJECT\_ID = "" REGION = "" GCS\_BUCKET\_NAME = f"{PROJECT\_ID}" GCS\_BUCKET\_URI = f"gs://{GCS\_BUCKET\_NAME}" # The number of dimensions for the textembedding-gecko@003 is 768 # If other embedder is used, the dimensions would probably need to change. VS\_DIMENSIONS = 768 # Vertex AI Vector Search Index configuration # parameter description here # https://cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.MatchingEngineIndex#google\_cloud\_aiplatform\_MatchingEngineIndex\_create\_tree\_ah\_index VS\_INDEX\_NAME = "vertex\_vector\_search\_index" # @param {type:"string"} VS\_INDEX\_ENDPOINT\_NAME = "vector\_search\_endpoint" # @param {type:"string"}

In \[ \]:

Copied!

from google.cloud import aiplatform

aiplatform.init(project\=PROJECT\_ID, location\=REGION)

from google.cloud import aiplatform aiplatform.init(project=PROJECT\_ID, location=REGION)

### Download Sample Documents for Testing[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/#download-sample-documents-for-testing)

In \[ \]:

Copied!

urls \= \[
    "https://openreview.net/pdf?id=VtmBAGCN7o",
    "https://openreview.net/pdf?id=6PmJoRfdaK",
    "https://openreview.net/pdf?id=LzPWWPAdY4",
    "https://openreview.net/pdf?id=VTF8yNQM66",
    "https://openreview.net/pdf?id=hSyW5go0v8",
    "https://openreview.net/pdf?id=9WD9KwssyT",
    "https://openreview.net/pdf?id=yV6fD7LYkF",
    "https://openreview.net/pdf?id=hnrB5YHoYu",
    "https://openreview.net/pdf?id=WbWtOYIzIK",
    "https://openreview.net/pdf?id=c5pwL0Soay",
    "https://openreview.net/pdf?id=TpD2aG1h0D",
\]

papers \= \[
    "metagpt.pdf",
    "longlora.pdf",
    "loftq.pdf",
    "swebench.pdf",
    "selfrag.pdf",
    "zipformer.pdf",
    "values.pdf",
    "finetune\_fair\_diffusion.pdf",
    "knowledge\_card.pdf",
    "metra.pdf",
    "vr\_mcl.pdf",
\]
import requests

def download\_file(url, file\_path):
    """Downloads a file from a given URL and saves it to the specified file path.

    Args:
        url: The URL of the file to download.
        file\_path: The path to save the downloaded file.
    """

    response \= requests.get(url, stream\=True)
    response.raise\_for\_status()  \# Raise an exception for non-200 status codes

    with open(file\_path, "wb") as f:
        for chunk in response.iter\_content(chunk\_size\=1024):
            if chunk:  \# Filter out keep-alive new chunks
                f.write(chunk)

    print(f"Downloaded file from {url} to {file\_path}")

for url, paper in zip(urls, papers):
    download\_file(url, paper)

urls = \[ "https://openreview.net/pdf?id=VtmBAGCN7o", "https://openreview.net/pdf?id=6PmJoRfdaK", "https://openreview.net/pdf?id=LzPWWPAdY4", "https://openreview.net/pdf?id=VTF8yNQM66", "https://openreview.net/pdf?id=hSyW5go0v8", "https://openreview.net/pdf?id=9WD9KwssyT", "https://openreview.net/pdf?id=yV6fD7LYkF", "https://openreview.net/pdf?id=hnrB5YHoYu", "https://openreview.net/pdf?id=WbWtOYIzIK", "https://openreview.net/pdf?id=c5pwL0Soay", "https://openreview.net/pdf?id=TpD2aG1h0D", \] papers = \[ "metagpt.pdf", "longlora.pdf", "loftq.pdf", "swebench.pdf", "selfrag.pdf", "zipformer.pdf", "values.pdf", "finetune\_fair\_diffusion.pdf", "knowledge\_card.pdf", "metra.pdf", "vr\_mcl.pdf", \] import requests def download\_file(url, file\_path): """Downloads a file from a given URL and saves it to the specified file path. Args: url: The URL of the file to download. file\_path: The path to save the downloaded file. """ response = requests.get(url, stream=True) response.raise\_for\_status() # Raise an exception for non-200 status codes with open(file\_path, "wb") as f: for chunk in response.iter\_content(chunk\_size=1024): if chunk: # Filter out keep-alive new chunks f.write(chunk) print(f"Downloaded file from {url} to {file\_path}") for url, paper in zip(urls, papers): download\_file(url, paper)

### Enable async for the notebook[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/#enable-async-for-the-notebook)

In \[ \]:

Copied!

import nest\_asyncio

nest\_asyncio.apply()

import nest\_asyncio nest\_asyncio.apply()

### Set Up Vector Store[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/#set-up-vector-store)

Here're two options for using Vector Search

*   Option 1: Createa a new Vertex AI Vector Search
*   Option 2: If you have an existing Vector Search store, you can use the existing one.

### Option 1: Create a new Vertex AI Vector Search[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/#option-1-create-a-new-vertex-ai-vector-search)

Create an empty index

In \[ \]:

Copied!

\# check if index exists
index\_names \= \[
    index.resource\_name
    for index in aiplatform.MatchingEngineIndex.list(
        filter\=f"display\_name={VS\_INDEX\_NAME}"
    )
\]

if len(index\_names) \ 0: print(f"Creating Vector Search index {VS\_INDEX\_NAME} ...") vs\_index = aiplatform.MatchingEngineIndex.create\_tree\_ah\_index( display\_name=VS\_INDEX\_NAME, dimensions=VS\_DIMENSIONS, distance\_measure\_type="DOT\_PRODUCT\_DISTANCE", approximate\_neighbors\_count=150, shard\_size="SHARD\_SIZE\_SMALL", index\_update\_method="STREAM\_UPDATE", # allowed values BATCH\_UPDATE , STREAM\_UPDATE ) print( f"Vector Search index {vs\_index.display\_name} created with resource name {vs\_index.resource\_name}" ) else: vs\_index = aiplatform.MatchingEngineIndex(index\_name=index\_names\[0\]) print( f"Vector Search index {vs\_index.display\_name} exists with resource name {vs\_index.resource\_name}" )

Create an endpoint

In \[ \]:

Copied!

endpoint\_names \= \[
    endpoint.resource\_name
    for endpoint in aiplatform.MatchingEngineIndexEndpoint.list(
        filter\=f"display\_name={VS\_INDEX\_ENDPOINT\_NAME}"
    )
\]

if len(endpoint\_names) \ 0: print( f"Creating Vector Search index endpoint {VS\_INDEX\_ENDPOINT\_NAME} ..." ) vs\_endpoint = aiplatform.MatchingEngineIndexEndpoint.create( display\_name=VS\_INDEX\_ENDPOINT\_NAME, public\_endpoint\_enabled=True ) print( f"Vector Search index endpoint {vs\_endpoint.display\_name} created with resource name {vs\_endpoint.resource\_name}" ) else: vs\_endpoint = aiplatform.MatchingEngineIndexEndpoint( index\_endpoint\_name=endpoint\_names\[0\] ) print( f"Vector Search index endpoint {vs\_endpoint.display\_name} exists with resource name {vs\_endpoint.resource\_name}" )

Deploy index to endpoint

In \[ \]:

Copied!

\# check if endpoint exists
\# it takes about 30 mins to finish
index\_endpoints \= \[
    (deployed\_index.index\_endpoint, deployed\_index.deployed\_index\_id)
    for deployed\_index in vs\_index.deployed\_indexes
\]

if len(index\_endpoints) \ 0: print( f"Deploying Vector Search index {vs\_index.display\_name} at endpoint {vs\_endpoint.display\_name} ..." ) vs\_deployed\_index = vs\_endpoint.deploy\_index( index=vs\_index, deployed\_index\_id=VS\_INDEX\_NAME, display\_name=VS\_INDEX\_NAME, machine\_type="e2-standard-16", min\_replica\_count=1, max\_replica\_count=1, ) print( f"Vector Search index {vs\_index.display\_name} is deployed at endpoint {vs\_deployed\_index.display\_name}" ) else: vs\_deployed\_index = aiplatform.MatchingEngineIndexEndpoint( index\_endpoint\_name=index\_endpoints\[0\]\[0\] ) print( f"Vector Search index {vs\_index.display\_name} is already deployed at endpoint {vs\_deployed\_index.display\_name}" )

### Option 2: Use an existing Vertex AI Vector Search[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/#option-2-use-an-existing-vertex-ai-vector-search)

In \[ \]:

Copied!

\# TODO : replace 1234567890123456789 with your actual index ID
vs\_index \= aiplatform.MatchingEngineIndex(index\_name\="<your index id>")

\# TODO : replace 1234567890123456789 with your actual endpoint ID
vs\_endpoint \= aiplatform.MatchingEngineIndexEndpoint(
    index\_endpoint\_name\="<your endpoint id>"
)

\# TODO : replace 1234567890123456789 with your actual index ID vs\_index = aiplatform.MatchingEngineIndex(index\_name="") # TODO : replace 1234567890123456789 with your actual endpoint ID vs\_endpoint = aiplatform.MatchingEngineIndexEndpoint( index\_endpoint\_name="" )

### Import libraries[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/#import-libraries)

In \[ \]:

Copied!

\# import modules needed
from llama\_index.core import (
    StorageContext,
    Settings,
    VectorStoreIndex,
    SummaryIndex,
    SimpleDirectoryReader,
)
from llama\_index.core.schema import TextNode
from llama\_index.core.vector\_stores.types import (
    MetadataFilters,
    MetadataFilter,
    FilterOperator,
)
from llama\_index.llms.vertex import Vertex
from llama\_index.embeddings.vertex import VertexTextEmbedding
from llama\_index.vector\_stores.vertexaivectorsearch import VertexAIVectorStore

from typing import List, Optional
from llama\_index.core.vector\_stores import FilterCondition
from llama\_index.core.tools import FunctionTool
from llama\_index.core import SimpleDirectoryReader
from llama\_index.core.node\_parser import SentenceSplitter

from llama\_index.core.tools import QueryEngineTool
from llama\_index.core.vector\_stores import MetadataFilters
from pathlib import Path

from llama\_index.core.agent import FunctionCallingAgentWorker
from llama\_index.core.agent import AgentRunner

\# import modules needed from llama\_index.core import ( StorageContext, Settings, VectorStoreIndex, SummaryIndex, SimpleDirectoryReader, ) from llama\_index.core.schema import TextNode from llama\_index.core.vector\_stores.types import ( MetadataFilters, MetadataFilter, FilterOperator, ) from llama\_index.llms.vertex import Vertex from llama\_index.embeddings.vertex import VertexTextEmbedding from llama\_index.vector\_stores.vertexaivectorsearch import VertexAIVectorStore from typing import List, Optional from llama\_index.core.vector\_stores import FilterCondition from llama\_index.core.tools import FunctionTool from llama\_index.core import SimpleDirectoryReader from llama\_index.core.node\_parser import SentenceSplitter from llama\_index.core.tools import QueryEngineTool from llama\_index.core.vector\_stores import MetadataFilters from pathlib import Path from llama\_index.core.agent import FunctionCallingAgentWorker from llama\_index.core.agent import AgentRunner

### Set up Vector Search Store[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/#set-up-vector-search-store)

In \[ \]:

Copied!

\# setup vector store
vector\_store \= VertexAIVectorStore(
    project\_id\=PROJECT\_ID,
    region\=REGION,
    index\_id\=vs\_index.name,
    endpoint\_id\=vs\_endpoint.name,
    gcs\_bucket\_name\=GCS\_BUCKET\_NAME,
)

\# set storage context
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

\# setup vector store vector\_store = VertexAIVectorStore( project\_id=PROJECT\_ID, region=REGION, index\_id=vs\_index.name, endpoint\_id=vs\_endpoint.name, gcs\_bucket\_name=GCS\_BUCKET\_NAME, ) # set storage context storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store)

In \[ \]:

Copied!

\# configure embedding model
embed\_model \= VertexTextEmbedding(
    model\_name\="textembedding-gecko@003",
    project\=PROJECT\_ID,
    location\=REGION,
)

vertex\_gemini \= Vertex(
    model\="gemini-1.5-pro-preview-0514", temperature\=0, additional\_kwargs\={}
)

\# setup the index/query process, ie the embedding model (and completion if used)
Settings.embed\_model \= embed\_model
Settings.llm \= vertex\_gemini

\# configure embedding model embed\_model = VertexTextEmbedding( model\_name="textembedding-gecko@003", project=PROJECT\_ID, location=REGION, ) vertex\_gemini = Vertex( model="gemini-1.5-pro-preview-0514", temperature=0, additional\_kwargs={} ) # setup the index/query process, ie the embedding model (and completion if used) Settings.embed\_model = embed\_model Settings.llm = vertex\_gemini

### Task 1: Router query engine[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/#task-1-router-query-engine)

#### Create vector index[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/#create-vector-index)

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader(input\_files\=\["metagpt.pdf"\]).load\_data()

\# load documents documents = SimpleDirectoryReader(input\_files=\["metagpt.pdf"\]).load\_data()

In \[ \]:

Copied!

\# define index from vector store
vector\_index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

\# define index from vector store vector\_index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

In \[ \]:

Copied!

splitter \= SentenceSplitter(chunk\_size\=1024)
nodes \= splitter.get\_nodes\_from\_documents(documents)

splitter = SentenceSplitter(chunk\_size=1024) nodes = splitter.get\_nodes\_from\_documents(documents)

#### Create summary index[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/#create-summary-index)

In \[ \]:

Copied!

summary\_index \= SummaryIndex(nodes)

summary\_index = SummaryIndex(nodes)

#### Create query engine from vector store[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/#create-query-engine-from-vector-store)

In \[ \]:

Copied!

summary\_query\_engine \= summary\_index.as\_query\_engine(
    response\_mode\="tree\_summarize",
    use\_async\=True,
)
vector\_query\_engine \= vector\_index.as\_query\_engine()

summary\_query\_engine = summary\_index.as\_query\_engine( response\_mode="tree\_summarize", use\_async=True, ) vector\_query\_engine = vector\_index.as\_query\_engine()

In \[ \]:

Copied!

summary\_query\_engine.query("what's the summary of the document?")

summary\_query\_engine.query("what's the summary of the document?")

#### Create tools from query engines[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/#create-tools-from-query-engines)

In \[ \]:

Copied!

summary\_tool \= QueryEngineTool.from\_defaults(
    query\_engine\=summary\_query\_engine,
    description\=("Useful for summarization questions related to MetaGPT"),
)

vector\_tool \= QueryEngineTool.from\_defaults(
    query\_engine\=vector\_query\_engine,
    description\=(
        "Useful for retrieving specific context from the MetaGPT paper."
    ),
)

summary\_tool = QueryEngineTool.from\_defaults( query\_engine=summary\_query\_engine, description=("Useful for summarization questions related to MetaGPT"), ) vector\_tool = QueryEngineTool.from\_defaults( query\_engine=vector\_query\_engine, description=( "Useful for retrieving specific context from the MetaGPT paper." ), )

In \[ \]:

Copied!

from llama\_index.core.query\_engine.router\_query\_engine import RouterQueryEngine
from llama\_index.core.selectors import LLMSingleSelector

query\_engine \= RouterQueryEngine(
    selector\=LLMSingleSelector.from\_defaults(),
    query\_engine\_tools\=\[
        summary\_tool,
        vector\_tool,
    \],
    verbose\=True,
)

from llama\_index.core.query\_engine.router\_query\_engine import RouterQueryEngine from llama\_index.core.selectors import LLMSingleSelector query\_engine = RouterQueryEngine( selector=LLMSingleSelector.from\_defaults(), query\_engine\_tools=\[ summary\_tool, vector\_tool, \], verbose=True, )

In \[ \]:

Copied!

response \= query\_engine.query("What is the summary of the document?")
print(str(response))

response = query\_engine.query("What is the summary of the document?") print(str(response))

In \[ \]:

Copied!

print(len(response.source\_nodes))

print(len(response.source\_nodes))

In \[ \]:

Copied!

response \= query\_engine.query(
    "How do agents share information with other agents?"
)
print(str(response))

response = query\_engine.query( "How do agents share information with other agents?" ) print(str(response))

### Task 2: Tool calling[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/#task-2-tool-calling)

#### Create auto-retrieval tools with parameters[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/#create-auto-retrieval-tools-with-parameters)

In \[ \]:

Copied!

query\_engine \= vector\_index.as\_query\_engine(
    similarity\_top\_k\=2,
    filters\=MetadataFilters.from\_dicts(\[{"key": "page\_label", "value": "2"}\]),
)

response \= query\_engine.query(
    "What are some high-level results of MetaGPT?",
)

query\_engine = vector\_index.as\_query\_engine( similarity\_top\_k=2, filters=MetadataFilters.from\_dicts(\[{"key": "page\_label", "value": "2"}\]), ) response = query\_engine.query( "What are some high-level results of MetaGPT?", )

In \[ \]:

Copied!

summary\_query\_engine \= summary\_index.as\_query\_engine(
    response\_mode\="tree\_summarize",
    use\_async\=True,
)

summary\_tool \= QueryEngineTool.from\_defaults(
    query\_engine\=summary\_query\_engine,
    description\=("Useful for summarization questions related to MetaGPT"),
)

summary\_query\_engine = summary\_index.as\_query\_engine( response\_mode="tree\_summarize", use\_async=True, ) summary\_tool = QueryEngineTool.from\_defaults( query\_engine=summary\_query\_engine, description=("Useful for summarization questions related to MetaGPT"), )

In \[ \]:

Copied!

print(str(response))

print(str(response))

In \[ \]:

Copied!

for n in response.source\_nodes:
    print(n.metadata)

for n in response.source\_nodes: print(n.metadata)

#### Define auto-retrieval tools for function calling[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/#define-auto-retrieval-tools-for-function-calling)

In \[ \]:

Copied!

def vector\_query(query: str, page\_numbers: List\[str\]) \-> str:
    """Perform a vector search over an index.

    query (str): the string query to be embedded.
    page\_numbers (List\[str\]): Filter by set of pages. Leave BLANK if we want to perform a vector search
        over all pages. Otherwise, filter by the set of specified pages.

    """

    metadata\_dicts \= \[{"key": "page\_label", "value": p} for p in page\_numbers\]

    query\_engine \= vector\_index.as\_query\_engine(
        similarity\_top\_k\=2,
        filters\=MetadataFilters.from\_dicts(
            metadata\_dicts, condition\=FilterCondition.OR
        ),
    )
    response \= query\_engine.query(query)
    return response

vector\_query\_tool \= FunctionTool.from\_defaults(
    fn\=vector\_query,
    \# name='vector\_query'
)

def vector\_query(query: str, page\_numbers: List\[str\]) -> str: """Perform a vector search over an index. query (str): the string query to be embedded. page\_numbers (List\[str\]): Filter by set of pages. Leave BLANK if we want to perform a vector search over all pages. Otherwise, filter by the set of specified pages. """ metadata\_dicts = \[{"key": "page\_label", "value": p} for p in page\_numbers\] query\_engine = vector\_index.as\_query\_engine( similarity\_top\_k=2, filters=MetadataFilters.from\_dicts( metadata\_dicts, condition=FilterCondition.OR ), ) response = query\_engine.query(query) return response vector\_query\_tool = FunctionTool.from\_defaults( fn=vector\_query, # name='vector\_query' )

In \[ \]:

Copied!

def summary\_query(
    query: str,
) \-> str:
    """Perform a summary of document
    query (str): the string query to be embedded.
    """
    summary\_engine \= summary\_index.as\_query\_engine(
        response\_mode\="tree\_summarize",
        use\_async\=True,
    )

    response \= summary\_engine.query(query)
    return response

summary\_tool \= FunctionTool.from\_defaults(
    fn\=summary\_query,
    \# name='summary\_query'
)

def summary\_query( query: str, ) -> str: """Perform a summary of document query (str): the string query to be embedded. """ summary\_engine = summary\_index.as\_query\_engine( response\_mode="tree\_summarize", use\_async=True, ) response = summary\_engine.query(query) return response summary\_tool = FunctionTool.from\_defaults( fn=summary\_query, # name='summary\_query' )

In \[ \]:

Copied!

response \= vertex\_gemini.predict\_and\_call(
    \[vector\_query\_tool, summary\_tool\],
    "What are the MetaGPT comparisons with ChatDev described on page 8?",
    verbose\=True,
)

response = vertex\_gemini.predict\_and\_call( \[vector\_query\_tool, summary\_tool\], "What are the MetaGPT comparisons with ChatDev described on page 8?", verbose=True, )

In \[ \]:

Copied!

for n in response.source\_nodes:
    print(n.metadata)

for n in response.source\_nodes: print(n.metadata)

In \[ \]:

Copied!

response \= vertex\_gemini.predict\_and\_call(
    \[summary\_tool, vector\_query\_tool\],
    "What is a summary of the paper?",
    verbose\=True,
)

response = vertex\_gemini.predict\_and\_call( \[summary\_tool, vector\_query\_tool\], "What is a summary of the paper?", verbose=True, )

### Task 3: Building an Agent Reasoning Loop[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/#task-3-building-an-agent-reasoning-loop)

In \[ \]:

Copied!

\# TODO: abstract all of this into a function that takes in a PDF file name
def get\_doc\_tools(
    file\_path: str,
    name: str,
) \-> str:
    """Get vector query and summary query tools from a document."""

    \# load documents
    documents \= SimpleDirectoryReader(input\_files\=\[file\_path\]).load\_data()
    splitter \= SentenceSplitter(chunk\_size\=1024)
    nodes \= splitter.get\_nodes\_from\_documents(documents)
    vector\_index \= VectorStoreIndex.from\_documents(
        documents, storage\_context\=storage\_context
    )
    summary\_index \= SummaryIndex(nodes)

    def vector\_query(
        query: str, page\_numbers: Optional\[List\[str\]\] \= None
    ) \-> str:
        """Use to answer questions over the MetaGPT paper.

        Useful if you have specific questions over the MetaGPT paper.
        Always leave page\_numbers as None UNLESS there is a specific page you want to search for.

        Args:
            query (str): the string query to be embedded.
            page\_numbers (Optional\[List\[str\]\]): Filter by set of pages. Leave as NONE
                if we want to perform a vector search
                over all pages. Otherwise, filter by the set of specified pages.

        """

        page\_numbers \= page\_numbers or \[\]
        metadata\_dicts \= \[
            {"key": "page\_label", "value": p} for p in page\_numbers
        \]

        query\_engine \= vector\_index.as\_query\_engine(
            similarity\_top\_k\=2,
            filters\=MetadataFilters.from\_dicts(
                metadata\_dicts, condition\=FilterCondition.OR
            ),
        )
        response \= query\_engine.query(query)
        return response

    vector\_query\_tool \= FunctionTool.from\_defaults(
        name\=f"vector\_tool\_{name}", fn\=vector\_query
    )

    def summary\_query(
        query: str,
    ) \-> str:
        """Perform a summary of document
        query (str): the string query to be embedded.
        """
        summary\_engine \= summary\_index.as\_query\_engine(
            response\_mode\="tree\_summarize",
            use\_async\=True,
        )

        response \= summary\_engine.query(query)
        return response

    summary\_tool \= FunctionTool.from\_defaults(
        fn\=summary\_query, name\=f"summary\_tool\_{name}"
    )

    return vector\_query\_tool, summary\_tool

\# TODO: abstract all of this into a function that takes in a PDF file name def get\_doc\_tools( file\_path: str, name: str, ) -> str: """Get vector query and summary query tools from a document.""" # load documents documents = SimpleDirectoryReader(input\_files=\[file\_path\]).load\_data() splitter = SentenceSplitter(chunk\_size=1024) nodes = splitter.get\_nodes\_from\_documents(documents) vector\_index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context ) summary\_index = SummaryIndex(nodes) def vector\_query( query: str, page\_numbers: Optional\[List\[str\]\] = None ) -> str: """Use to answer questions over the MetaGPT paper. Useful if you have specific questions over the MetaGPT paper. Always leave page\_numbers as None UNLESS there is a specific page you want to search for. Args: query (str): the string query to be embedded. page\_numbers (Optional\[List\[str\]\]): Filter by set of pages. Leave as NONE if we want to perform a vector search over all pages. Otherwise, filter by the set of specified pages. """ page\_numbers = page\_numbers or \[\] metadata\_dicts = \[ {"key": "page\_label", "value": p} for p in page\_numbers \] query\_engine = vector\_index.as\_query\_engine( similarity\_top\_k=2, filters=MetadataFilters.from\_dicts( metadata\_dicts, condition=FilterCondition.OR ), ) response = query\_engine.query(query) return response vector\_query\_tool = FunctionTool.from\_defaults( name=f"vector\_tool\_{name}", fn=vector\_query ) def summary\_query( query: str, ) -> str: """Perform a summary of document query (str): the string query to be embedded. """ summary\_engine = summary\_index.as\_query\_engine( response\_mode="tree\_summarize", use\_async=True, ) response = summary\_engine.query(query) return response summary\_tool = FunctionTool.from\_defaults( fn=summary\_query, name=f"summary\_tool\_{name}" ) return vector\_query\_tool, summary\_tool

In \[ \]:

Copied!

vector\_query\_tool, summary\_tool \= get\_doc\_tools("metagpt.pdf", "metagpt")

vector\_query\_tool, summary\_tool = get\_doc\_tools("metagpt.pdf", "metagpt")

In \[ \]:

Copied!

\# Create Vertex AI client
vertex\_gemini \= Vertex(model\="gemini-1.5-pro-preview-0514")

\# Create Vertex AI client vertex\_gemini = Vertex(model="gemini-1.5-pro-preview-0514")

In \[ \]:

Copied!

\# Create Agent Runner
agent\_worker \= FunctionCallingAgentWorker.from\_tools(
    \[vector\_query\_tool, summary\_tool\], llm\=vertex\_gemini, verbose\=True
)
agent \= AgentRunner(agent\_worker)

\# Create Agent Runner agent\_worker = FunctionCallingAgentWorker.from\_tools( \[vector\_query\_tool, summary\_tool\], llm=vertex\_gemini, verbose=True ) agent = AgentRunner(agent\_worker)

In \[ \]:

Copied!

response \= agent.query(
    "what are agent roles in MetaGPT, "
    "and then how they communicate with each other."
)

response = agent.query( "what are agent roles in MetaGPT, " "and then how they communicate with each other." )

### Task 4: Multi-document agent[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/#task-4-multi-document-agent)

In \[ \]:

Copied!

papers \= \[
    "metagpt.pdf",
    "longlora.pdf",
    "loftq.pdf",
    "swebench.pdf",
    "selfrag.pdf",
    "zipformer.pdf",
    "values.pdf",
    "finetune\_fair\_diffusion.pdf",
    "knowledge\_card.pdf",
    "metra.pdf",
\]

papers = \[ "metagpt.pdf", "longlora.pdf", "loftq.pdf", "swebench.pdf", "selfrag.pdf", "zipformer.pdf", "values.pdf", "finetune\_fair\_diffusion.pdf", "knowledge\_card.pdf", "metra.pdf", \]

In \[ \]:

Copied!

paper\_to\_tools\_dict \= {}
for paper in papers:
    print(f"Getting tools for paper: {paper}")
    vector\_tool, summary\_tool \= get\_doc\_tools(paper, Path(paper).stem)
    paper\_to\_tools\_dict\[paper\] \= \[vector\_tool, summary\_tool\]

paper\_to\_tools\_dict = {} for paper in papers: print(f"Getting tools for paper: {paper}") vector\_tool, summary\_tool = get\_doc\_tools(paper, Path(paper).stem) paper\_to\_tools\_dict\[paper\] = \[vector\_tool, summary\_tool\]

In \[ \]:

Copied!

all\_tools \= \[t for paper in papers for t in paper\_to\_tools\_dict\[paper\]\]

all\_tools = \[t for paper in papers for t in paper\_to\_tools\_dict\[paper\]\]

In \[ \]:

Copied!

\# define an "object" index and retriever over these tools
from llama\_index.core import VectorStoreIndex
from llama\_index.core.objects import ObjectIndex

obj\_index \= ObjectIndex.from\_objects(
    all\_tools,
    index\_cls\=VectorStoreIndex,
)

\# define an "object" index and retriever over these tools from llama\_index.core import VectorStoreIndex from llama\_index.core.objects import ObjectIndex obj\_index = ObjectIndex.from\_objects( all\_tools, index\_cls=VectorStoreIndex, )

In \[ \]:

Copied!

obj\_retriever \= obj\_index.as\_retriever(similarity\_top\_k\=3)

obj\_retriever = obj\_index.as\_retriever(similarity\_top\_k=3)

In \[ \]:

Copied!

agent\_worker \= FunctionCallingAgentWorker.from\_tools(
    tool\_retriever\=obj\_retriever,
    llm\=vertex\_gemini,
    system\_prompt\=""" \\
You are an agent designed to answer queries over a set of given papers.
Please use the tools provided to answer a question as possible. Do not rely on prior knowledge. Summarize your answer\\

""",
    verbose\=True,
)
agent \= AgentRunner(agent\_worker)

agent\_worker = FunctionCallingAgentWorker.from\_tools( tool\_retriever=obj\_retriever, llm=vertex\_gemini, system\_prompt=""" \\ You are an agent designed to answer queries over a set of given papers. Please use the tools provided to answer a question as possible. Do not rely on prior knowledge. Summarize your answer\\ """, verbose=True, ) agent = AgentRunner(agent\_worker)

In \[ \]:

Copied!

response \= agent.query(
    "What is the evaluation dataset used in MetaGPT? Compare it against SWE-Bench"
)
print(str(response))

response = agent.query( "What is the evaluation dataset used in MetaGPT? Compare it against SWE-Bench" ) print(str(response))

In \[ \]:

Copied!

response \= agent.query(
    "Compare and contrast the LoRA papers (LongLoRA, LoftQ). "
    "Analyze the approach in each paper first. "
)

response = agent.query( "Compare and contrast the LoRA papers (LongLoRA, LoftQ). " "Analyze the approach in each paper first. " )

Back to top

[Previous Building an Agent around a Query Pipeline](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/query_pipeline_agent/)[Next Agentic rag with llamaindex and vertexai managed index](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_with_llamaindex_and_vertexai_managed_index/)

Hi, how can I help you?

🦙
