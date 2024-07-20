Title: Agentic rag with llamaindex and vertexai managed index

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_with_llamaindex_and_vertexai_managed_index/

Markdown Content:
Agentic rag with llamaindex and vertexai managed index - LlamaIndex


       

Build Agentic RAG using Vertex AI managed index[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_with_llamaindex_and_vertexai_managed_index/#build-agentic-rag-using-vertex-ai-managed-index)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/docs/examples/agent/agentic_rag_with_llamaindex_and_vertexai_managed_index.ipynb)

Author(s) | [Dave Wang](https://github.com/wadave) |

### Pre-requisites[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_with_llamaindex_and_vertexai_managed_index/#pre-requisites)

*   Set up a Google Cloud project
*   Create a Google Cloud storage bucket

#### References:[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_with_llamaindex_and_vertexai_managed_index/#references)

1.  Use managed Vertex AI index

*   [https://docs.llamaindex.ai/en/stable/examples/managed/VertexAIDemo/](https://docs.llamaindex.ai/en/stable/examples/managed/VertexAIDemo/)

2.  Building Agentic RAG with Llamaindex Tutorial

*   [https://learn.deeplearning.ai/courses/building-agentic-rag-with-llamaindex/lesson/2/router-query-engine](https://learn.deeplearning.ai/courses/building-agentic-rag-with-llamaindex/lesson/2/router-query-engine)

### Install Libraries[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_with_llamaindex_and_vertexai_managed_index/#install-libraries)

In \[ \]:

Copied!

!pip install \--upgrade google\-cloud\-aiplatform llama\-index llama\-index\-vector\-stores\-vertexaivectorsearch llama\_index\-llms\-vertex llama\-index\-llms\-gemini

!pip install --upgrade google-cloud-aiplatform llama-index llama-index-vector-stores-vertexaivectorsearch llama\_index-llms-vertex llama-index-llms-gemini

In \[ \]:

Copied!

!pip install llama\-index\-indices\-managed\-vertexai

!pip install llama-index-indices-managed-vertexai

### Restart current runtime[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_with_llamaindex_and_vertexai_managed_index/#restart-current-runtime)

To use the newly installed packages in this Jupyter runtime, you must restart the runtime. You can do this by running the cell below, which will restart the current kernel.

In \[ \]:

Copied!

\# Colab only
\# Automatically restart kernel after installs so that your environment can access the new packages
import IPython

app \= IPython.Application.instance()
app.kernel.do\_shutdown(True)

\# Colab only # Automatically restart kernel after installs so that your environment can access the new packages import IPython app = IPython.Application.instance() app.kernel.do\_shutdown(True)

### Authenticate your notebook environment (Colab only)[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_with_llamaindex_and_vertexai_managed_index/#authenticate-your-notebook-environment-colab-only)

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

### Import libraries[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_with_llamaindex_and_vertexai_managed_index/#import-libraries)

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

\# import modules needed from llama\_index.core import ( StorageContext, Settings, VectorStoreIndex, SummaryIndex, SimpleDirectoryReader, ) from llama\_index.core.schema import TextNode from llama\_index.core.vector\_stores.types import ( MetadataFilters, MetadataFilter, FilterOperator, ) from llama\_index.llms.vertex import Vertex from llama\_index.embeddings.vertex import VertexTextEmbedding from typing import List, Optional from llama\_index.core.vector\_stores import FilterCondition from llama\_index.core.tools import FunctionTool from llama\_index.core import SimpleDirectoryReader from llama\_index.core.node\_parser import SentenceSplitter from llama\_index.core.tools import QueryEngineTool from llama\_index.core.vector\_stores import MetadataFilters from pathlib import Path from llama\_index.core.agent import FunctionCallingAgentWorker from llama\_index.core.agent import AgentRunner

### Define Google Cloud project information and initialize Vertex AI[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_with_llamaindex_and_vertexai_managed_index/#define-google-cloud-project-information-and-initialize-vertex-ai)

Initialize the Vertex AI SDK for Python for your project:

In \[ \]:

Copied!

\# TODO : Set values as per your requirements

\# Project and Storage Constants
PROJECT\_ID \= "<your project id>"
REGION \= "us-central1"
GCS\_BUCKET\_NAME \= "<your bucket name>"
GCS\_BUCKET\_URI \= f"gs://{GCS\_BUCKET\_NAME}"

\# TODO : Set values as per your requirements # Project and Storage Constants PROJECT\_ID = "" REGION = "us-central1" GCS\_BUCKET\_NAME = "" GCS\_BUCKET\_URI = f"gs://{GCS\_BUCKET\_NAME}"

In \[ \]:

Copied!

from google.cloud import aiplatform

aiplatform.init(project\=PROJECT\_ID, location\=REGION)

from google.cloud import aiplatform aiplatform.init(project=PROJECT\_ID, location=REGION)

### Download Sample Documents for Testing[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_with_llamaindex_and_vertexai_managed_index/#download-sample-documents-for-testing)

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

### Enable async for the notebook[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_with_llamaindex_and_vertexai_managed_index/#enable-async-for-the-notebook)

In \[ \]:

Copied!

import nest\_asyncio

nest\_asyncio.apply()

import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

from llama\_index.indices.managed.vertexai import VertexAIIndex

\# TODO(developer): Replace these values with your project information
project\_id \= PROJECT\_ID
location \= "us-central1"

from llama\_index.indices.managed.vertexai import VertexAIIndex # TODO(developer): Replace these values with your project information project\_id = PROJECT\_ID location = "us-central1"

In \[ \]:

Copied!

\# configure embedding model
embed\_model \= VertexTextEmbedding(
    model\_name\="text-embedding-004",
    project\=PROJECT\_ID,
    location\=REGION,
)

vertex\_gemini \= Vertex(
    model\="gemini-1.5-pro-preview-0514", temperature\=0, additional\_kwargs\={}
)

\# setup the index/query process, ie the embedding model (and completion if used)
Settings.embed\_model \= embed\_model
Settings.llm \= vertex\_gemini

\# configure embedding model embed\_model = VertexTextEmbedding( model\_name="text-embedding-004", project=PROJECT\_ID, location=REGION, ) vertex\_gemini = Vertex( model="gemini-1.5-pro-preview-0514", temperature=0, additional\_kwargs={} ) # setup the index/query process, ie the embedding model (and completion if used) Settings.embed\_model = embed\_model Settings.llm = vertex\_gemini

In \[ \]:

Copied!

\# Optional: If creating a new corpus
corpus\_display\_name \= "my-corpus"
corpus\_description \= "Vertex AI Corpus for LlamaIndex"

\# Create a corpus or provide an existing corpus ID
index \= VertexAIIndex(
    project\_id,
    location,
    corpus\_display\_name\=corpus\_display\_name,
    corpus\_description\=corpus\_description,
)
print(f"Newly created corpus name is {index.corpus\_name}.")

\# Upload local file
file\_name \= index.insert\_file(
    file\_path\="longlora.pdf",
    metadata\={
        "display\_name": "long\_lora",
        "description": "Long Lora paper",
    },
)

\# Optional: If creating a new corpus corpus\_display\_name = "my-corpus" corpus\_description = "Vertex AI Corpus for LlamaIndex" # Create a corpus or provide an existing corpus ID index = VertexAIIndex( project\_id, location, corpus\_display\_name=corpus\_display\_name, corpus\_description=corpus\_description, ) print(f"Newly created corpus name is {index.corpus\_name}.") # Upload local file file\_name = index.insert\_file( file\_path="longlora.pdf", metadata={ "display\_name": "long\_lora", "description": "Long Lora paper", }, )

In \[ \]:

Copied!

index.list\_files()

index.list\_files()

### Create Llamaindex query engine and retriever[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_with_llamaindex_and_vertexai_managed_index/#create-llamaindex-query-engine-and-retriever)

In \[ \]:

Copied!

\# Querying
query\_engine \= index.as\_query\_engine()

\# Retrieving
retriever \= index.as\_retriever()

\# Querying query\_engine = index.as\_query\_engine() # Retrieving retriever = index.as\_retriever()

In \[ \]:

Copied!

response \= query\_engine.query("What is long lora?")
print(response)

response = query\_engine.query("What is long lora?") print(response)

In \[ \]:

Copied!

nodes \= retriever.retrieve("What is long lora?")
for n in nodes:
    print(n.text)

nodes = retriever.retrieve("What is long lora?") for n in nodes: print(n.text)

### Task 1: Router query engine[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_with_llamaindex_and_vertexai_managed_index/#task-1-router-query-engine)

#### Create vector index[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_with_llamaindex_and_vertexai_managed_index/#create-vector-index)

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader(input\_files\=\["metagpt.pdf"\]).load\_data()

\# load documents documents = SimpleDirectoryReader(input\_files=\["metagpt.pdf"\]).load\_data()

In \[ \]:

Copied!

\# define index from vector store
index.insert\_file(
    file\_path\="metagpt.pdf",
    metadata\={
        "display\_name": "metagpt",
        "description": "metagpt",
    },
)

\# define index from vector store index.insert\_file( file\_path="metagpt.pdf", metadata={ "display\_name": "metagpt", "description": "metagpt", }, )

In \[ \]:

Copied!

splitter \= SentenceSplitter(chunk\_size\=1024)
nodes \= splitter.get\_nodes\_from\_documents(documents)

splitter = SentenceSplitter(chunk\_size=1024) nodes = splitter.get\_nodes\_from\_documents(documents)

#### Create summary index[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_with_llamaindex_and_vertexai_managed_index/#create-summary-index)

In \[ \]:

Copied!

summary\_index \= SummaryIndex(nodes)

summary\_index = SummaryIndex(nodes)

#### Create query engine from vector store[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_with_llamaindex_and_vertexai_managed_index/#create-query-engine-from-vector-store)

In \[ \]:

Copied!

summary\_query\_engine \= summary\_index.as\_query\_engine(
    response\_mode\="tree\_summarize",
    use\_async\=True,
)
vector\_query\_engine \= index.as\_query\_engine()

summary\_query\_engine = summary\_index.as\_query\_engine( response\_mode="tree\_summarize", use\_async=True, ) vector\_query\_engine = index.as\_query\_engine()

In \[ \]:

Copied!

summary\_query\_engine.query("what's the summary of the document?")

summary\_query\_engine.query("what's the summary of the document?")

#### Create tools from query engines[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_with_llamaindex_and_vertexai_managed_index/#create-tools-from-query-engines)

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

### Task 2: Tool calling[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_with_llamaindex_and_vertexai_managed_index/#task-2-tool-calling)

#### Create auto-retrieval tools with parameters[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_with_llamaindex_and_vertexai_managed_index/#create-auto-retrieval-tools-with-parameters)

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(
    similarity\_top\_k\=2,
    filters\=MetadataFilters.from\_dicts(\[{"key": "page\_label", "value": "2"}\]),
)

response \= query\_engine.query(
    "What are some high-level results of MetaGPT?",
)

query\_engine = index.as\_query\_engine( similarity\_top\_k=2, filters=MetadataFilters.from\_dicts(\[{"key": "page\_label", "value": "2"}\]), ) response = query\_engine.query( "What are some high-level results of MetaGPT?", )

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

#### Define auto-retrieval tools for function calling[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_with_llamaindex_and_vertexai_managed_index/#define-auto-retrieval-tools-for-function-calling)

In \[ \]:

Copied!

def vector\_query(query: str, page\_numbers: List\[str\]) \-> str:
    """Perform a vector search over an index.

    query (str): the string query to be embedded.
    page\_numbers (List\[str\]): Filter by set of pages. Leave BLANK if we want to perform a vector search
        over all pages. Otherwise, filter by the set of specified pages.

    """

    metadata\_dicts \= \[{"key": "page\_label", "value": p} for p in page\_numbers\]

    query\_engine \= index.as\_query\_engine(
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

def vector\_query(query: str, page\_numbers: List\[str\]) -> str: """Perform a vector search over an index. query (str): the string query to be embedded. page\_numbers (List\[str\]): Filter by set of pages. Leave BLANK if we want to perform a vector search over all pages. Otherwise, filter by the set of specified pages. """ metadata\_dicts = \[{"key": "page\_label", "value": p} for p in page\_numbers\] query\_engine = index.as\_query\_engine( similarity\_top\_k=2, filters=MetadataFilters.from\_dicts( metadata\_dicts, condition=FilterCondition.OR ), ) response = query\_engine.query(query) return response vector\_query\_tool = FunctionTool.from\_defaults( fn=vector\_query, # name='vector\_query' )

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

response \= vertex\_gemini.predict\_and\_call(
    \[summary\_tool, vector\_query\_tool\],
    "What is a summary of the paper?",
    verbose\=True,
)

response = vertex\_gemini.predict\_and\_call( \[summary\_tool, vector\_query\_tool\], "What is a summary of the paper?", verbose=True, )

### Task 3: Building an Agent Reasoning Loop[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_with_llamaindex_and_vertexai_managed_index/#task-3-building-an-agent-reasoning-loop)

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
    vector\_index \= index
    vector\_index.insert\_file(
        file\_path\=file\_path,
        metadata\={
            "display\_name": f"vector\_index\_{name}",
            "description": f"vector\_index\_{name}",
        },
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

\# TODO: abstract all of this into a function that takes in a PDF file name def get\_doc\_tools( file\_path: str, name: str, ) -> str: """Get vector query and summary query tools from a document.""" # load documents documents = SimpleDirectoryReader(input\_files=\[file\_path\]).load\_data() splitter = SentenceSplitter(chunk\_size=1024) nodes = splitter.get\_nodes\_from\_documents(documents) vector\_index = index vector\_index.insert\_file( file\_path=file\_path, metadata={ "display\_name": f"vector\_index\_{name}", "description": f"vector\_index\_{name}", }, ) summary\_index = SummaryIndex(nodes) def vector\_query( query: str, page\_numbers: Optional\[List\[str\]\] = None ) -> str: """Use to answer questions over the MetaGPT paper. Useful if you have specific questions over the MetaGPT paper. Always leave page\_numbers as None UNLESS there is a specific page you want to search for. Args: query (str): the string query to be embedded. page\_numbers (Optional\[List\[str\]\]): Filter by set of pages. Leave as NONE if we want to perform a vector search over all pages. Otherwise, filter by the set of specified pages. """ page\_numbers = page\_numbers or \[\] metadata\_dicts = \[ {"key": "page\_label", "value": p} for p in page\_numbers \] query\_engine = vector\_index.as\_query\_engine( similarity\_top\_k=2, filters=MetadataFilters.from\_dicts( metadata\_dicts, condition=FilterCondition.OR ), ) response = query\_engine.query(query) return response vector\_query\_tool = FunctionTool.from\_defaults( name=f"vector\_tool\_{name}", fn=vector\_query ) def summary\_query( query: str, ) -> str: """Perform a summary of document query (str): the string query to be embedded. """ summary\_engine = summary\_index.as\_query\_engine( response\_mode="tree\_summarize", use\_async=True, ) response = summary\_engine.query(query) return response summary\_tool = FunctionTool.from\_defaults( fn=summary\_query, name=f"summary\_tool\_{name}" ) return vector\_query\_tool, summary\_tool

In \[ \]:

Copied!

vector\_query\_tool, summary\_tool \= get\_doc\_tools("metagpt.pdf", "metagpt")

vector\_query\_tool, summary\_tool = get\_doc\_tools("metagpt.pdf", "metagpt")

In \[ \]:

Copied!

\# Create Vertex AI client
vertex\_gemini \= Vertex(model\="gemini-1.5-flash-preview-0514")

\# Create Vertex AI client vertex\_gemini = Vertex(model="gemini-1.5-flash-preview-0514")

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

### Task 4: Multi-document agent[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_with_llamaindex_and_vertexai_managed_index/#task-4-multi-document-agent)

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
    "knowledge\_card.pdf",
    "metra.pdf",
\]

papers = \[ "metagpt.pdf", "longlora.pdf", "loftq.pdf", "swebench.pdf", "selfrag.pdf", "zipformer.pdf", "values.pdf", "knowledge\_card.pdf", "metra.pdf", \]

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
    "Compare and contrast the LoRA papers (LongLoRA, LoftQ) "
    "Analyze the approach in each paper first."
)

response = agent.query( "Compare and contrast the LoRA papers (LongLoRA, LoftQ) " "Analyze the approach in each paper first." )

Back to top

[Previous Agentic rag using vertex ai](https://docs.llamaindex.ai/en/stable/examples/agent/agentic_rag_using_vertex_ai/)[Next Function Calling Anthropic Agent](https://docs.llamaindex.ai/en/stable/examples/agent/anthropic_agent/)

🦙
