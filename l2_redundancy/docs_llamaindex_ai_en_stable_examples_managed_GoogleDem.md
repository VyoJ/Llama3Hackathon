Title: Google Generative Language Semantic Retriever

URL Source: https://docs.llamaindex.ai/en/stable/examples/managed/GoogleDemo/

Markdown Content:
Google Generative Language Semantic Retriever - LlamaIndex


In this notebook, we will show you how to get started quickly with using Google's Generative Language Semantic Retriever, which offers specialized embedding models for high quality retrieval and a tuned model for producing grounded output with customizable safety settings. We will also show you some advanced examples on how to combine the power of LlamaIndex and this unique offering from Google.

Installation[¶](https://docs.llamaindex.ai/en/stable/examples/managed/GoogleDemo/#installation)
-----------------------------------------------------------------------------------------------

In \[ \]:

Copied!

%pip install llama\-index\-llms\-gemini
%pip install llama\-index\-vector\-stores\-google
%pip install llama\-index\-indices\-managed\-google
%pip install llama\-index\-response\-synthesizers\-google

%pip install llama-index-llms-gemini %pip install llama-index-vector-stores-google %pip install llama-index-indices-managed-google %pip install llama-index-response-synthesizers-google

In \[ \]:

Copied!

%pip install llama\-index
%pip install "google-ai-generativelanguage>=0.4,<=1.0"

%pip install llama-index %pip install "google-ai-generativelanguage>=0.4,<=1.0"

### Google Authentication Overview[¶](https://docs.llamaindex.ai/en/stable/examples/managed/GoogleDemo/#google-authentication-overview)

The Google Semantic Retriever API lets you perform semantic search on your own data. Since it's **your data**, this needs stricter access controls than API keys. Authenticate with OAuth with service accounts or through your user credentials (example in the bottom of the notebook).

This quickstart uses a simplified authentication approach meant for a testing environment, and service account setup are typically easier to start from. Demo recording for authenticating using service accounts: [Demo](https://drive.google.com/file/d/199LzrdhuuiordS15MJAxVrPKAwEJGPOh/view?usp=sharing).

For a production environment, learn about [authentication and authorization](https://developers.google.com/workspace/guides/auth-overview) before choosing the [access credentials](https://developers.google.com/workspace/guides/create-credentials#choose_the_access_credential_that_is_right_for_you) that are appropriate for your app.

**Note**: At this time, the Google Generative AI Semantic Retriever API is [only available in certain regions](https://ai.google.dev/available_regions).

### Setup OAuth using service accounts[¶](https://docs.llamaindex.ai/en/stable/examples/managed/GoogleDemo/#setup-oauth-using-service-accounts)

Follow the steps below to setup OAuth using service accounts:

1.  Enable the [Generative Language API](https://console.cloud.google.com/flows/enableapi?apiid=generativelanguage.googleapis.com).
    
2.  Create the Service Account by following the [documentation](https://developers.google.com/identity/protocols/oauth2/service-account#creatinganaccount).
    

*   After creating the service account, generate a service account key.

3.  Upload your service account file by using the file icon on the left sidebar, then the upload icon, as shown in the screenshot below.

*   Rename the uploaded file to `service_account_key.json` or change the variable `service_account_file_name` in the code below.

![Image 4: No description has been provided for this image](https://developers.generativeai.google/tutorials/images/colab_upload.png)

In \[ \]:

Copied!

%pip install google\-auth\-oauthlib

%pip install google-auth-oauthlib

In \[ \]:

Copied!

from google.oauth2 import service\_account
from llama\_index.vector\_stores.google import set\_google\_config

credentials \= service\_account.Credentials.from\_service\_account\_file(
    "service\_account\_key.json",
    scopes\=\[
        "https://www.googleapis.com/auth/generative-language.retriever",
    \],
)
set\_google\_config(auth\_credentials\=credentials)

from google.oauth2 import service\_account from llama\_index.vector\_stores.google import set\_google\_config credentials = service\_account.Credentials.from\_service\_account\_file( "service\_account\_key.json", scopes=\[ "https://www.googleapis.com/auth/generative-language.retriever", \], ) set\_google\_config(auth\_credentials=credentials)

Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/managed/GoogleDemo/#download-data)
-------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/managed/GoogleDemo/#setup)
---------------------------------------------------------------------------------

First, let's create some helper functions behind the scene.

In \[ \]:

Copied!

import llama\_index.core.vector\_stores.google.generativeai.genai\_extension as genaix
from typing import Iterable
from random import randrange

LLAMA\_INDEX\_COLAB\_CORPUS\_ID\_PREFIX \= f"llama-index-colab"
SESSION\_CORPUS\_ID\_PREFIX \= (
    f"{LLAMA\_INDEX\_COLAB\_CORPUS\_ID\_PREFIX}\-{randrange(1000000)}"
)

def corpus\_id(num\_id: int) \-> str:
    return f"{SESSION\_CORPUS\_ID\_PREFIX}\-{num\_id}"

SESSION\_CORPUS\_ID \= corpus\_id(1)

def list\_corpora() \-> Iterable\[genaix.Corpus\]:
    client \= genaix.build\_semantic\_retriever()
    yield from genaix.list\_corpora(client\=client)

def delete\_corpus(\*, corpus\_id: str) \-> None:
    client \= genaix.build\_semantic\_retriever()
    genaix.delete\_corpus(corpus\_id\=corpus\_id, client\=client)

def cleanup\_colab\_corpora():
    for corpus in list\_corpora():
        if corpus.corpus\_id.startswith(LLAMA\_INDEX\_COLAB\_CORPUS\_ID\_PREFIX):
            try:
                delete\_corpus(corpus\_id\=corpus.corpus\_id)
                print(f"Deleted corpus {corpus.corpus\_id}.")
            except Exception:
                pass

\# Remove any previously leftover corpora from this colab.
cleanup\_colab\_corpora()

import llama\_index.core.vector\_stores.google.generativeai.genai\_extension as genaix from typing import Iterable from random import randrange LLAMA\_INDEX\_COLAB\_CORPUS\_ID\_PREFIX = f"llama-index-colab" SESSION\_CORPUS\_ID\_PREFIX = ( f"{LLAMA\_INDEX\_COLAB\_CORPUS\_ID\_PREFIX}-{randrange(1000000)}" ) def corpus\_id(num\_id: int) -> str: return f"{SESSION\_CORPUS\_ID\_PREFIX}-{num\_id}" SESSION\_CORPUS\_ID = corpus\_id(1) def list\_corpora() -> Iterable\[genaix.Corpus\]: client = genaix.build\_semantic\_retriever() yield from genaix.list\_corpora(client=client) def delete\_corpus(\*, corpus\_id: str) -> None: client = genaix.build\_semantic\_retriever() genaix.delete\_corpus(corpus\_id=corpus\_id, client=client) def cleanup\_colab\_corpora(): for corpus in list\_corpora(): if corpus.corpus\_id.startswith(LLAMA\_INDEX\_COLAB\_CORPUS\_ID\_PREFIX): try: delete\_corpus(corpus\_id=corpus.corpus\_id) print(f"Deleted corpus {corpus.corpus\_id}.") except Exception: pass # Remove any previously leftover corpora from this colab. cleanup\_colab\_corpora()

Basic Usage[¶](https://docs.llamaindex.ai/en/stable/examples/managed/GoogleDemo/#basic-usage)
---------------------------------------------------------------------------------------------

A `corpus` is a collection of `document`s. A `document` is a body of text that is broken into `chunk`s.

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader
from llama\_index.indices.managed.google import GoogleIndex
from llama\_index.core import Response
import time

\# Create a corpus.
index \= GoogleIndex.create\_corpus(
    corpus\_id\=SESSION\_CORPUS\_ID, display\_name\="My first corpus!"
)
print(f"Newly created corpus ID is {index.corpus\_id}.")

\# Ingestion.
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()
index.insert\_documents(documents)

from llama\_index.core import SimpleDirectoryReader from llama\_index.indices.managed.google import GoogleIndex from llama\_index.core import Response import time # Create a corpus. index = GoogleIndex.create\_corpus( corpus\_id=SESSION\_CORPUS\_ID, display\_name="My first corpus!" ) print(f"Newly created corpus ID is {index.corpus\_id}.") # Ingestion. documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data() index.insert\_documents(documents)

Let's check that what we've ingested.

In \[ \]:

Copied!

for corpus in list\_corpora():
    print(corpus)

for corpus in list\_corpora(): print(corpus)

Let's ask the index a question.

In \[ \]:

Copied!

\# Querying.
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did Paul Graham do growing up?")
assert isinstance(response, Response)

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

\# Querying. query\_engine = index.as\_query\_engine() response = query\_engine.query("What did Paul Graham do growing up?") assert isinstance(response, Response) # Show response. print(f"Response is {response.response}") # Show cited passages that were used to construct the response. for cited\_text in \[node.text for node in response.source\_nodes\]: print(f"Cited text: {cited\_text}") # Show answerability. 0 means not answerable from the passages. # 1 means the model is certain the answer can be provided from the passages. if response.metadata: print( f"Answerability: {response.metadata.get('answerable\_probability', 0)}" )

Creating a Corpus[¶](https://docs.llamaindex.ai/en/stable/examples/managed/GoogleDemo/#creating-a-corpus)
---------------------------------------------------------------------------------------------------------

There are various ways to create a corpus.

\# The Google server will provide a corpus ID for you.
index \= GoogleIndex.create\_corpus(display\_name\="My first corpus!")
print(index.corpus\_id)

\# You can also provide your own corpus ID. However, this ID needs to be globally
\# unique. You will get an exception if someone else has this ID already.
index \= GoogleIndex.create\_corpus(
    corpus\_id\="my-first-corpus", display\_name\="My first corpus!"
)

\# If you do not provide any parameter, Google will provide ID and a default
\# display name for you.
index \= GoogleIndex.create\_corpus()

Reusing a Corpus[¶](https://docs.llamaindex.ai/en/stable/examples/managed/GoogleDemo/#reusing-a-corpus)
-------------------------------------------------------------------------------------------------------

Corpora you created persists on the Google servers under your account. You can use its ID to get a handle back. Then, you can query it, add more document to it, etc.

In \[ \]:

Copied!

\# Use a previously created corpus.
index \= GoogleIndex.from\_corpus(corpus\_id\=SESSION\_CORPUS\_ID)

\# Query it again!
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("Which company did Paul Graham build?")
assert isinstance(response, Response)

\# Show response.
print(f"Response is {response.response}")

\# Use a previously created corpus. index = GoogleIndex.from\_corpus(corpus\_id=SESSION\_CORPUS\_ID) # Query it again! query\_engine = index.as\_query\_engine() response = query\_engine.query("Which company did Paul Graham build?") assert isinstance(response, Response) # Show response. print(f"Response is {response.response}")

Listing and Deleting Corpora[¶](https://docs.llamaindex.ai/en/stable/examples/managed/GoogleDemo/#listing-and-deleting-corpora)
-------------------------------------------------------------------------------------------------------------------------------

See the Python library [google-generativeai](https://github.com/google/generative-ai-python) for further documentation.

Loading Documents[¶](https://docs.llamaindex.ai/en/stable/examples/managed/GoogleDemo/#loading-documents)
---------------------------------------------------------------------------------------------------------

Many node parsers and text splitters in LlamaIndex automatically add to each node a _source\_node_ to associate it to a file, e.g.

relationships\={
        NodeRelationship.SOURCE: RelatedNodeInfo(
            node\_id\="abc-123",
            metadata\={"file\_name": "Title for the document"},
        )
    },

Both `GoogleIndex` and `GoogleVectorStore` recognize this source node, and will automatically create documents under your corpus on the Google servers.

In case you are writing your own chunker, you should supply this source node relationship too like below:

In \[ \]:

Copied!

from llama\_index.core.schema import NodeRelationship, RelatedNodeInfo, TextNode

index \= GoogleIndex.from\_corpus(corpus\_id\=SESSION\_CORPUS\_ID)
index.insert\_nodes(
    \[
        TextNode(
            text\="It was the best of times.",
            relationships\={
                NodeRelationship.SOURCE: RelatedNodeInfo(
                    node\_id\="123",
                    metadata\={"file\_name": "Tale of Two Cities"},
                )
            },
        ),
        TextNode(
            text\="It was the worst of times.",
            relationships\={
                NodeRelationship.SOURCE: RelatedNodeInfo(
                    node\_id\="123",
                    metadata\={"file\_name": "Tale of Two Cities"},
                )
            },
        ),
        TextNode(
            text\="Bugs Bunny: Wassup doc?",
            relationships\={
                NodeRelationship.SOURCE: RelatedNodeInfo(
                    node\_id\="456",
                    metadata\={"file\_name": "Bugs Bunny Adventure"},
                )
            },
        ),
    \]
)

from llama\_index.core.schema import NodeRelationship, RelatedNodeInfo, TextNode index = GoogleIndex.from\_corpus(corpus\_id=SESSION\_CORPUS\_ID) index.insert\_nodes( \[ TextNode( text="It was the best of times.", relationships={ NodeRelationship.SOURCE: RelatedNodeInfo( node\_id="123", metadata={"file\_name": "Tale of Two Cities"}, ) }, ), TextNode( text="It was the worst of times.", relationships={ NodeRelationship.SOURCE: RelatedNodeInfo( node\_id="123", metadata={"file\_name": "Tale of Two Cities"}, ) }, ), TextNode( text="Bugs Bunny: Wassup doc?", relationships={ NodeRelationship.SOURCE: RelatedNodeInfo( node\_id="456", metadata={"file\_name": "Bugs Bunny Adventure"}, ) }, ), \] )

If your nodes do not have a source node, then Google server will put your nodes in a default document under your corpus.

Listing and Deleting Documents[¶](https://docs.llamaindex.ai/en/stable/examples/managed/GoogleDemo/#listing-and-deleting-documents)
-----------------------------------------------------------------------------------------------------------------------------------

See the Python library [google-generativeai](https://github.com/google/generative-ai-python) for further documentation.

Querying Corpus[¶](https://docs.llamaindex.ai/en/stable/examples/managed/GoogleDemo/#querying-corpus)
-----------------------------------------------------------------------------------------------------

Google's query engine is backed by a specially tuned LLM that grounds its response based on retrieved passages. For each response, an _answerability probability_ is returned to indicate how confident the LLM was in answering the question from the retrieved passages.

Furthermore, Google's query engine supports _answering styles_, such as `ABSTRACTIVE` (succint but abstract), `EXTRACTIVE` (very brief and extractive) and `VERBOSE` (extra details).

The engine also supports _safety settings_.

In \[ \]:

Copied!

from google.ai.generativelanguage import (
    GenerateAnswerRequest,
    HarmCategory,
    SafetySetting,
)

index \= GoogleIndex.from\_corpus(corpus\_id\=SESSION\_CORPUS\_ID)
query\_engine \= index.as\_query\_engine(
    \# We recommend temperature between 0 and 0.2.
    temperature\=0.2,
    \# See package \`google-generativeai\` for other voice styles.
    answer\_style\=GenerateAnswerRequest.AnswerStyle.ABSTRACTIVE,
    \# See package \`google-generativeai\` for additional safety settings.
    safety\_setting\=\[
        SafetySetting(
            category\=HarmCategory.HARM\_CATEGORY\_SEXUALLY\_EXPLICIT,
            threshold\=SafetySetting.HarmBlockThreshold.BLOCK\_LOW\_AND\_ABOVE,
        ),
        SafetySetting(
            category\=HarmCategory.HARM\_CATEGORY\_VIOLENCE,
            threshold\=SafetySetting.HarmBlockThreshold.BLOCK\_ONLY\_HIGH,
        ),
    \],
)

response \= query\_engine.query("What was Bugs Bunny's favorite saying?")
print(response)

from google.ai.generativelanguage import ( GenerateAnswerRequest, HarmCategory, SafetySetting, ) index = GoogleIndex.from\_corpus(corpus\_id=SESSION\_CORPUS\_ID) query\_engine = index.as\_query\_engine( # We recommend temperature between 0 and 0.2. temperature=0.2, # See package \`google-generativeai\` for other voice styles. answer\_style=GenerateAnswerRequest.AnswerStyle.ABSTRACTIVE, # See package \`google-generativeai\` for additional safety settings. safety\_setting=\[ SafetySetting( category=HarmCategory.HARM\_CATEGORY\_SEXUALLY\_EXPLICIT, threshold=SafetySetting.HarmBlockThreshold.BLOCK\_LOW\_AND\_ABOVE, ), SafetySetting( category=HarmCategory.HARM\_CATEGORY\_VIOLENCE, threshold=SafetySetting.HarmBlockThreshold.BLOCK\_ONLY\_HIGH, ), \], ) response = query\_engine.query("What was Bugs Bunny's favorite saying?") print(response)

See the Python library [google-generativeai](https://github.com/google/generative-ai-python) for further documentation.

Interpreting the Response[¶](https://docs.llamaindex.ai/en/stable/examples/managed/GoogleDemo/#interpreting-the-response)
-------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core import Response

response \= query\_engine.query("What were Paul Graham's achievements?")
assert isinstance(response, Response)

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

from llama\_index.core import Response response = query\_engine.query("What were Paul Graham's achievements?") assert isinstance(response, Response) # Show response. print(f"Response is {response.response}") # Show cited passages that were used to construct the response. for cited\_text in \[node.text for node in response.source\_nodes\]: print(f"Cited text: {cited\_text}") # Show answerability. 0 means not answerable from the passages. # 1 means the model is certain the answer can be provided from the passages. if response.metadata: print( f"Answerability: {response.metadata.get('answerable\_probability', 0)}" )

Advanced RAG[¶](https://docs.llamaindex.ai/en/stable/examples/managed/GoogleDemo/#advanced-rag)
-----------------------------------------------------------------------------------------------

The `GoogleIndex` is built based on `GoogleVectorStore` and `GoogleTextSynthesizer`. These components can be combined with other powerful constructs in LlamaIndex to produce advanced RAG applications.

Below we show a few examples.

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/managed/GoogleDemo/#setup)
---------------------------------------------------------------------------------

First, you need an API key. Get one from [AI Studio](https://makersuite.google.com/app/apikey).

In \[ \]:

Copied!

from llama\_index.llms.gemini import Gemini

GEMINI\_API\_KEY \= ""  \# @param {type:"string"}
gemini \= Gemini(api\_key\=GEMINI\_API\_KEY)

from llama\_index.llms.gemini import Gemini GEMINI\_API\_KEY = "" # @param {type:"string"} gemini = Gemini(api\_key=GEMINI\_API\_KEY)

### Reranker + Google Retriever[¶](https://docs.llamaindex.ai/en/stable/examples/managed/GoogleDemo/#reranker-google-retriever)

Converting content into vectors is a lossy process. LLM-based Reranking remediates this by reranking the retrieved content using LLM, which has higher fidelity because it has access to both the actual query and the passage.

In \[ \]:

Copied!

from llama\_index.response\_synthesizers.google import GoogleTextSynthesizer
from llama\_index.vector\_stores.google import GoogleVectorStore
from llama\_index.core import VectorStoreIndex
from llama\_index.core.postprocessor import LLMRerank
from llama\_index.core.query\_engine import RetrieverQueryEngine
from llama\_index.core.retrievers import VectorIndexRetriever

\# Set up the query engine with a reranker.
store \= GoogleVectorStore.from\_corpus(corpus\_id\=SESSION\_CORPUS\_ID)
index \= VectorStoreIndex.from\_vector\_store(
    vector\_store\=store,
)
response\_synthesizer \= GoogleTextSynthesizer.from\_defaults(
    temperature\=0.2,
    answer\_style\=GenerateAnswerRequest.AnswerStyle.ABSTRACTIVE,
)
reranker \= LLMRerank(
    top\_n\=10,
    llm\=gemini,
)
query\_engine \= RetrieverQueryEngine.from\_args(
    retriever\=VectorIndexRetriever(
        index\=index,
        similarity\_top\_k\=20,
    ),
    node\_postprocessors\=\[reranker\],
    response\_synthesizer\=response\_synthesizer,
)

\# Query.
response \= query\_engine.query("What were Paul Graham's achievements?")
print(response)

from llama\_index.response\_synthesizers.google import GoogleTextSynthesizer from llama\_index.vector\_stores.google import GoogleVectorStore from llama\_index.core import VectorStoreIndex from llama\_index.core.postprocessor import LLMRerank from llama\_index.core.query\_engine import RetrieverQueryEngine from llama\_index.core.retrievers import VectorIndexRetriever # Set up the query engine with a reranker. store = GoogleVectorStore.from\_corpus(corpus\_id=SESSION\_CORPUS\_ID) index = VectorStoreIndex.from\_vector\_store( vector\_store=store, ) response\_synthesizer = GoogleTextSynthesizer.from\_defaults( temperature=0.2, answer\_style=GenerateAnswerRequest.AnswerStyle.ABSTRACTIVE, ) reranker = LLMRerank( top\_n=10, llm=gemini, ) query\_engine = RetrieverQueryEngine.from\_args( retriever=VectorIndexRetriever( index=index, similarity\_top\_k=20, ), node\_postprocessors=\[reranker\], response\_synthesizer=response\_synthesizer, ) # Query. response = query\_engine.query("What were Paul Graham's achievements?") print(response)

### Multi-Query + Google Retriever[¶](https://docs.llamaindex.ai/en/stable/examples/managed/GoogleDemo/#multi-query-google-retriever)

Sometimes, a user's query can be too complex. You may get better retrieval result if you break down the original query into smaller, better focused queries.

In \[ \]:

Copied!

from llama\_index.core.indices.query.query\_transform.base import (
    StepDecomposeQueryTransform,
)
from llama\_index.core.query\_engine import MultiStepQueryEngine

\# Set up the query engine with multi-turn query-rewriter.
store \= GoogleVectorStore.from\_corpus(corpus\_id\=SESSION\_CORPUS\_ID)
index \= VectorStoreIndex.from\_vector\_store(
    vector\_store\=store,
)
response\_synthesizer \= GoogleTextSynthesizer.from\_defaults(
    temperature\=0.2,
    answer\_style\=GenerateAnswerRequest.AnswerStyle.ABSTRACTIVE,
)
single\_step\_query\_engine \= index.as\_query\_engine(
    similarity\_top\_k\=10,
    response\_synthesizer\=response\_synthesizer,
)
step\_decompose\_transform \= StepDecomposeQueryTransform(
    llm\=gemini,
    verbose\=True,
)
query\_engine \= MultiStepQueryEngine(
    query\_engine\=single\_step\_query\_engine,
    query\_transform\=step\_decompose\_transform,
    response\_synthesizer\=response\_synthesizer,
    index\_summary\="Ask me anything.",
    num\_steps\=6,
)

\# Query.
response \= query\_engine.query("What were Paul Graham's achievements?")
print(response)

from llama\_index.core.indices.query.query\_transform.base import ( StepDecomposeQueryTransform, ) from llama\_index.core.query\_engine import MultiStepQueryEngine # Set up the query engine with multi-turn query-rewriter. store = GoogleVectorStore.from\_corpus(corpus\_id=SESSION\_CORPUS\_ID) index = VectorStoreIndex.from\_vector\_store( vector\_store=store, ) response\_synthesizer = GoogleTextSynthesizer.from\_defaults( temperature=0.2, answer\_style=GenerateAnswerRequest.AnswerStyle.ABSTRACTIVE, ) single\_step\_query\_engine = index.as\_query\_engine( similarity\_top\_k=10, response\_synthesizer=response\_synthesizer, ) step\_decompose\_transform = StepDecomposeQueryTransform( llm=gemini, verbose=True, ) query\_engine = MultiStepQueryEngine( query\_engine=single\_step\_query\_engine, query\_transform=step\_decompose\_transform, response\_synthesizer=response\_synthesizer, index\_summary="Ask me anything.", num\_steps=6, ) # Query. response = query\_engine.query("What were Paul Graham's achievements?") print(response)

### HyDE + Google Retriever[¶](https://docs.llamaindex.ai/en/stable/examples/managed/GoogleDemo/#hyde-google-retriever)

When you can write prompt that would produce fake answers that share many traits with the real answer, you can try HyDE!

In \[ \]:

Copied!

from llama\_index.core.indices.query.query\_transform import HyDEQueryTransform
from llama\_index.core.query\_engine import TransformQueryEngine

\# Set up the query engine with multi-turn query-rewriter.
store \= GoogleVectorStore.from\_corpus(corpus\_id\=SESSION\_CORPUS\_ID)
index \= VectorStoreIndex.from\_vector\_store(
    vector\_store\=store,
)
response\_synthesizer \= GoogleTextSynthesizer.from\_defaults(
    temperature\=0.2,
    answer\_style\=GenerateAnswerRequest.AnswerStyle.ABSTRACTIVE,
)
base\_query\_engine \= index.as\_query\_engine(
    similarity\_top\_k\=10,
    response\_synthesizer\=response\_synthesizer,
)
hyde \= HyDEQueryTransform(
    llm\=gemini,
    include\_original\=False,
)
hyde\_query\_engine \= TransformQueryEngine(base\_query\_engine, hyde)

\# Query.
response \= query\_engine.query("What were Paul Graham's achievements?")
print(response)

from llama\_index.core.indices.query.query\_transform import HyDEQueryTransform from llama\_index.core.query\_engine import TransformQueryEngine # Set up the query engine with multi-turn query-rewriter. store = GoogleVectorStore.from\_corpus(corpus\_id=SESSION\_CORPUS\_ID) index = VectorStoreIndex.from\_vector\_store( vector\_store=store, ) response\_synthesizer = GoogleTextSynthesizer.from\_defaults( temperature=0.2, answer\_style=GenerateAnswerRequest.AnswerStyle.ABSTRACTIVE, ) base\_query\_engine = index.as\_query\_engine( similarity\_top\_k=10, response\_synthesizer=response\_synthesizer, ) hyde = HyDEQueryTransform( llm=gemini, include\_original=False, ) hyde\_query\_engine = TransformQueryEngine(base\_query\_engine, hyde) # Query. response = query\_engine.query("What were Paul Graham's achievements?") print(response)

### Multi-Query + Reranker + HyDE + Google Retriever[¶](https://docs.llamaindex.ai/en/stable/examples/managed/GoogleDemo/#multi-query-reranker-hyde-google-retriever)

Or combine them all!

In \[ \]:

Copied!

\# Google's retriever and AQA model setup.
store \= GoogleVectorStore.from\_corpus(corpus\_id\=SESSION\_CORPUS\_ID)
index \= VectorStoreIndex.from\_vector\_store(
    vector\_store\=store,
)
response\_synthesizer \= GoogleTextSynthesizer.from\_defaults(
    temperature\=0.2, answer\_style\=GenerateAnswerRequest.AnswerStyle.ABSTRACTIVE
)

\# Reranker setup.
reranker \= LLMRerank(
    top\_n\=10,
    llm\=gemini,
)
single\_step\_query\_engine \= index.as\_query\_engine(
    similarity\_top\_k\=20,
    node\_postprocessors\=\[reranker\],
    response\_synthesizer\=response\_synthesizer,
)

\# HyDE setup.
hyde \= HyDEQueryTransform(
    llm\=gemini,
    include\_original\=False,
)
hyde\_query\_engine \= TransformQueryEngine(single\_step\_query\_engine, hyde)

\# Multi-query setup.
step\_decompose\_transform \= StepDecomposeQueryTransform(
    llm\=gemini, verbose\=True
)
query\_engine \= MultiStepQueryEngine(
    query\_engine\=hyde\_query\_engine,
    query\_transform\=step\_decompose\_transform,
    response\_synthesizer\=response\_synthesizer,
    index\_summary\="Ask me anything.",
    num\_steps\=6,
)

\# Query.
response \= query\_engine.query("What were Paul Graham's achievements?")
print(response)

\# Google's retriever and AQA model setup. store = GoogleVectorStore.from\_corpus(corpus\_id=SESSION\_CORPUS\_ID) index = VectorStoreIndex.from\_vector\_store( vector\_store=store, ) response\_synthesizer = GoogleTextSynthesizer.from\_defaults( temperature=0.2, answer\_style=GenerateAnswerRequest.AnswerStyle.ABSTRACTIVE ) # Reranker setup. reranker = LLMRerank( top\_n=10, llm=gemini, ) single\_step\_query\_engine = index.as\_query\_engine( similarity\_top\_k=20, node\_postprocessors=\[reranker\], response\_synthesizer=response\_synthesizer, ) # HyDE setup. hyde = HyDEQueryTransform( llm=gemini, include\_original=False, ) hyde\_query\_engine = TransformQueryEngine(single\_step\_query\_engine, hyde) # Multi-query setup. step\_decompose\_transform = StepDecomposeQueryTransform( llm=gemini, verbose=True ) query\_engine = MultiStepQueryEngine( query\_engine=hyde\_query\_engine, query\_transform=step\_decompose\_transform, response\_synthesizer=response\_synthesizer, index\_summary="Ask me anything.", num\_steps=6, ) # Query. response = query\_engine.query("What were Paul Graham's achievements?") print(response)

Cleanup corpora created in the colab[¶](https://docs.llamaindex.ai/en/stable/examples/managed/GoogleDemo/#cleanup-corpora-created-in-the-colab)
-----------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

cleanup\_colab\_corpora()

cleanup\_colab\_corpora()

Appendix: Setup OAuth with user credentials[¶](https://docs.llamaindex.ai/en/stable/examples/managed/GoogleDemo/#appendix-setup-oauth-with-user-credentials)
------------------------------------------------------------------------------------------------------------------------------------------------------------

Please follow [OAuth Quickstart](https://developers.generativeai.google/tutorials/oauth_quickstart) to setup OAuth using user credentials. Below are overview of steps from the documentation that are required.

1.  Enable the `Generative Language API`: [Documentation](https://developers.generativeai.google/tutorials/oauth_quickstart#1_enable_the_api)
    
2.  Configure the OAuth consent screen: [Documentation](https://developers.generativeai.google/tutorials/oauth_quickstart#2_configure_the_oauth_consent_screen)
    
3.  Authorize credentials for a desktop application: [Documentation](https://developers.generativeai.google/tutorials/oauth_quickstart#3_authorize_credentials_for_a_desktop_application)
    

*   If you want to run this notebook in Colab start by uploading your `client_secret*.json` file using the "File > Upload" option.
    
*   Rename the uploaded file to `client_secret.json` or change the variable `client_file_name` in the code below.
    

![Image 5: No description has been provided for this image](https://developers.generativeai.google/tutorials/images/colab_upload.png)

In \[ \]:

Copied!

\# Replace TODO-your-project-name with the project used in the OAuth Quickstart
project\_name \= "TODO-your-project-name"  \#  @param {type:"string"}
\# Replace TODO-your-email@gmail.com with the email added as a test user in the OAuth Quickstart
email \= "TODO-your-email@gmail.com"  \#  @param {type:"string"}
\# Replace client\_secret.json with the client\_secret\_\* file name you uploaded.
client\_file\_name \= "client\_secret.json"

\# IMPORTANT: Follow the instructions from the output - you must copy the command
\# to your terminal and copy the output after authentication back here.
!gcloud config set project $project\_name
!gcloud config set account $email

\# NOTE: The simplified project setup in this tutorial triggers a "Google hasn't verified this app." dialog.
\# This is normal, click "Advanced" -> "Go to \[app name\] (unsafe)"
!gcloud auth application\-default login \--no\-browser \--client\-id\-file\=$client\_file\_name \--scopes\="https://www.googleapis.com/auth/generative-language.retriever,https://www.googleapis.com/auth/cloud-platform"

\# Replace TODO-your-project-name with the project used in the OAuth Quickstart project\_name = "TODO-your-project-name" # @param {type:"string"} # Replace TODO-your-email@gmail.com with the email added as a test user in the OAuth Quickstart email = "TODO-your-email@gmail.com" # @param {type:"string"} # Replace client\_secret.json with the client\_secret\_\* file name you uploaded. client\_file\_name = "client\_secret.json" # IMPORTANT: Follow the instructions from the output - you must copy the command # to your terminal and copy the output after authentication back here. !gcloud config set project projectname!gcloudconfigsetaccountprojectname!gcloudconfigsetaccount email # NOTE: The simplified project setup in this tutorial triggers a "Google hasn't verified this app." dialog. # This is normal, click "Advanced" -> "Go to \[app name\] (unsafe)" !gcloud auth application-default login --no-browser --client-id-file=$client\_file\_name --scopes="https://www.googleapis.com/auth/generative-language.retriever,https://www.googleapis.com/auth/cloud-platform"

This will provide you with a URL, which you should enter into your local browser. Follow the instruction to complete the authentication and authorization.

Back to top

[Previous Building a (Very Simple) Vector Store from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/vector_store/)[Next PostgresML Managed Index](https://docs.llamaindex.ai/en/stable/examples/managed/PostgresMLDemo/)

Hi, how can I help you?

🦙
