Title: Google Cloud LlamaIndex on Vertex AI for RAG

URL Source: https://docs.llamaindex.ai/en/stable/examples/managed/VertexAIDemo/

Markdown Content:
Google Cloud LlamaIndex on Vertex AI for RAG - LlamaIndex


In this notebook, we will show you how to get started with the [Vertex AI RAG API](https://cloud.google.com/vertex-ai/generative-ai/docs/llamaindex-on-vertexai).

Installation[¶](https://docs.llamaindex.ai/en/stable/examples/managed/VertexAIDemo/#installation)
-------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

%pip install llama\-index\-llms\-gemini
%pip install llama\-index\-indices\-managed\-vertexai

%pip install llama-index-llms-gemini %pip install llama-index-indices-managed-vertexai

In \[ \]:

Copied!

%pip install llama\-index
%pip install google\-cloud\-aiplatform\1.53.0

### Setup[¶](https://docs.llamaindex.ai/en/stable/examples/managed/VertexAIDemo/#setup)

Follow the steps in this documentation to create a Google Cloud project and enable the Vertex AI API.

[https://cloud.google.com/vertex-ai/docs/start/cloud-environment](https://cloud.google.com/vertex-ai/docs/start/cloud-environment)

### Authenticating your notebook environment[¶](https://docs.llamaindex.ai/en/stable/examples/managed/VertexAIDemo/#authenticating-your-notebook-environment)

*   If you are using **Colab** to run this notebook, run the cell below and continue.
*   If you are using **Vertex AI Workbench**, check out the setup instructions [here](https://github.com/GoogleCloudPlatform/generative-ai/tree/main/setup-env).

In \[ \]:

Copied!

import sys

\# Additional authentication is required for Google Colab
if "google.colab" in sys.modules:
    \# Authenticate user to Google Cloud
    from google.colab import auth

    auth.authenticate\_user()

    ! gcloud config set project {PROJECT\_ID}
    ! gcloud auth application\-default login \-q

import sys # Additional authentication is required for Google Colab if "google.colab" in sys.modules: # Authenticate user to Google Cloud from google.colab import auth auth.authenticate\_user() ! gcloud config set project {PROJECT\_ID} ! gcloud auth application-default login -q

Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/managed/VertexAIDemo/#download-data)
---------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

Basic Usage[¶](https://docs.llamaindex.ai/en/stable/examples/managed/VertexAIDemo/#basic-usage)
-----------------------------------------------------------------------------------------------

A `corpus` is a collection of `document`s. A `document` is a body of text that is broken into `chunk`s.

#### Set up LLM for RAG[¶](https://docs.llamaindex.ai/en/stable/examples/managed/VertexAIDemo/#set-up-llm-for-rag)

In \[ \]:

Copied!

from llama\_index.core import Settings
from llama\_index.llms.vertex import Vertex

vertex\_gemini \= Vertex(
    model\="gemini-1.5-pro-preview-0514", temperature\=0, additional\_kwargs\={}
)

Settings.llm \= vertex\_gemini

from llama\_index.core import Settings from llama\_index.llms.vertex import Vertex vertex\_gemini = Vertex( model="gemini-1.5-pro-preview-0514", temperature=0, additional\_kwargs={} ) Settings.llm = vertex\_gemini

In \[ \]:

Copied!

from llama\_index.indices.managed.vertexai import VertexAIIndex

\# TODO(developer): Replace these values with your project information
project\_id \= "YOUR\_PROJECT\_ID"
location \= "us-central1"

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
    file\_path\="data/paul\_graham/paul\_graham\_essay.txt",
    metadata\={
        "display\_name": "paul\_graham\_essay",
        "description": "Paul Graham essay",
    },
)

from llama\_index.indices.managed.vertexai import VertexAIIndex # TODO(developer): Replace these values with your project information project\_id = "YOUR\_PROJECT\_ID" location = "us-central1" # Optional: If creating a new corpus corpus\_display\_name = "my-corpus" corpus\_description = "Vertex AI Corpus for LlamaIndex" # Create a corpus or provide an existing corpus ID index = VertexAIIndex( project\_id, location, corpus\_display\_name=corpus\_display\_name, corpus\_description=corpus\_description, ) print(f"Newly created corpus name is {index.corpus\_name}.") # Upload local file file\_name = index.insert\_file( file\_path="data/paul\_graham/paul\_graham\_essay.txt", metadata={ "display\_name": "paul\_graham\_essay", "description": "Paul Graham essay", }, )

Let's check that what we've ingested.

In \[ \]:

Copied!

print(index.list\_files())

print(index.list\_files())

Let's ask the index a question.

In \[ \]:

Copied!

\# Querying.
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did Paul Graham do growing up?")

\# Show response.
print(f"Response is {response.response}")

\# Show cited passages that were used to construct the response.
for cited\_text in \[node.text for node in response.source\_nodes\]:
    print(f"Cited text: {cited\_text}")

\# Show answerability. 0 means not answerable from the passages.
\# 1 means the model is certain the answer can be provided from the passages.
if response.metadata:
    print(
        f"Answerability: {response.metadata.get('answerable\_probability', 0)}"
    )

\# Querying. query\_engine = index.as\_query\_engine() response = query\_engine.query("What did Paul Graham do growing up?") # Show response. print(f"Response is {response.response}") # Show cited passages that were used to construct the response. for cited\_text in \[node.text for node in response.source\_nodes\]: print(f"Cited text: {cited\_text}") # Show answerability. 0 means not answerable from the passages. # 1 means the model is certain the answer can be provided from the passages. if response.metadata: print( f"Answerability: {response.metadata.get('answerable\_probability', 0)}" )

Back to top

[Previous PostgresML Managed Index](https://docs.llamaindex.ai/en/stable/examples/managed/PostgresMLDemo/)[Next Semantic Retriever Benchmark](https://docs.llamaindex.ai/en/stable/examples/managed/manage_retrieval_benchmark/)

Hi, how can I help you?

🦙
