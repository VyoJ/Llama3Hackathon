Title: UpTrain Callback Handler - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/callbacks/UpTrainCallback/

Markdown Content:
UpTrain Callback Handler - LlamaIndex


UpTrain ([github](https://github.com/uptrain-ai/uptrain) || [website](https://github.com/uptrain-ai/uptrain/) || [docs](https://docs.uptrain.ai/)) is an open-source platform to evaluate and improve GenAI applications. It provides grades for 20+ preconfigured checks (covering language, code, embedding use cases), performs root cause analysis on failure cases and gives insights on how to resolve them.

This notebook showcases how to use UpTrain Callback Handler to evaluate different components of your RAG pipelines.

1\. **RAG Query Engine Evaluations**:[¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/UpTrainCallback/#1-rag-query-engine-evaluations)
-------------------------------------------------------------------------------------------------------------------------------------------------

The RAG query engine plays a crucial role in retrieving context and generating responses. To ensure its performance and response quality, we conduct the following evaluations:

*   **[Context Relevance](https://docs.uptrain.ai/predefined-evaluations/context-awareness/context-relevance)**: Determines if the retrieved context has sufficient information to answer the user query or not.
*   **[Factual Accuracy](https://docs.uptrain.ai/predefined-evaluations/context-awareness/factual-accuracy)**: Assesses if the LLM's response can be verified via the retrieved context.
*   **[Response Completeness](https://docs.uptrain.ai/predefined-evaluations/response-quality/response-completeness)**: Checks if the response contains all the information required to answer the user query comprehensively.

2\. **Sub-Question Query Generation Evaluation**:[¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/UpTrainCallback/#2-sub-question-query-generation-evaluation)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The SubQuestionQueryGeneration operator decomposes a question into sub-questions, generating responses for each using an RAG query engine. To measure it's accuracy, we use:

*   **[Sub Query Completeness](https://docs.uptrain.ai/predefined-evaluations/query-quality/sub-query-completeness)**: Assures that the sub-questions accurately and comprehensively cover the original query.

3\. **Re-Ranking Evaluations**:[¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/UpTrainCallback/#3-re-ranking-evaluations)
-------------------------------------------------------------------------------------------------------------------------------------

Re-ranking involves reordering nodes based on relevance to the query and choosing the top nodes. Different evaluations are performed based on the number of nodes returned after re-ranking.

a. Same Number of Nodes

*   **[Context Reranking](https://docs.uptrain.ai/predefined-evaluations/context-awareness/context-reranking)**: Checks if the order of re-ranked nodes is more relevant to the query than the original order.

b. Different Number of Nodes:

*   **[Context Conciseness](https://docs.uptrain.ai/predefined-evaluations/context-awareness/context-conciseness)**: Examines whether the reduced number of nodes still provides all the required information.

These evaluations collectively ensure the robustness and effectiveness of the RAG query engine, SubQuestionQueryGeneration operator, and the re-ranking process in the LlamaIndex pipeline.

#### **Note:**[¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/UpTrainCallback/#note)

*   We have performed evaluations using basic RAG query engine, the same evaluations can be performed using the advanced RAG query engine as well.
*   Same is true for Re-Ranking evaluations, we have performed evaluations using SentenceTransformerRerank, the same evaluations can be performed using other re-rankers as well.

Install Dependencies and Import Libraries[¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/UpTrainCallback/#install-dependencies-and-import-libraries)
----------------------------------------------------------------------------------------------------------------------------------------------------------------

Install notebook dependencies.

In \[ \]:

Copied!

%pip install llama\-index\-readers\-web
%pip install llama\-index\-callbacks\-uptrain
%pip install \-q html2text llama\-index pandas tqdm uptrain torch sentence\-transformers

%pip install llama-index-readers-web %pip install llama-index-callbacks-uptrain %pip install -q html2text llama-index pandas tqdm uptrain torch sentence-transformers

Import libraries.

In \[ \]:

Copied!

from getpass import getpass

from llama\_index.core import Settings, VectorStoreIndex
from llama\_index.core.node\_parser import SentenceSplitter
from llama\_index.readers.web import SimpleWebPageReader
from llama\_index.core.callbacks import CallbackManager
from llama\_index.callbacks.uptrain.base import UpTrainCallbackHandler
from llama\_index.core.query\_engine import SubQuestionQueryEngine
from llama\_index.core.tools import QueryEngineTool, ToolMetadata
from llama\_index.core.postprocessor import SentenceTransformerRerank

import os

from getpass import getpass from llama\_index.core import Settings, VectorStoreIndex from llama\_index.core.node\_parser import SentenceSplitter from llama\_index.readers.web import SimpleWebPageReader from llama\_index.core.callbacks import CallbackManager from llama\_index.callbacks.uptrain.base import UpTrainCallbackHandler from llama\_index.core.query\_engine import SubQuestionQueryEngine from llama\_index.core.tools import QueryEngineTool, ToolMetadata from llama\_index.core.postprocessor import SentenceTransformerRerank import os

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/UpTrainCallback/#setup)
----------------------------------------------------------------------------------------

UpTrain provides you with:

1.  Dashboards with advanced drill-down and filtering options
2.  Insights and common topics among failing cases
3.  Observability and real-time monitoring of production data
4.  Regression testing via seamless integration with your CI/CD pipelines

You can choose between the following options for evaluating using UpTrain:

### 1\. **UpTrain's Open-Source Software (OSS)**:[¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/UpTrainCallback/#1-uptrains-open-source-software-oss)

You can use the open-source evaluation service to evaluate your model. In this case, you will need to provide an OpenAI API key. You can get yours [here](https://platform.openai.com/account/api-keys).

In order to view your evaluations in the UpTrain dashboard, you will need to set it up by running the following commands in your terminal:

git clone https://github.com/uptrain-ai/uptrain
cd uptrain
bash run\_uptrain.sh

This will start the UpTrain dashboard on your local machine. You can access it at `http://localhost:3000/dashboard`.

Parameters:

*   key\_type="openai"
*   api\_key="OPENAI\_API\_KEY"
*   project\_name="PROJECT\_NAME"

### 2\. **UpTrain Managed Service and Dashboards**:[¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/UpTrainCallback/#2-uptrain-managed-service-and-dashboards)

Alternatively, you can use UpTrain's managed service to evaluate your model. You can create a free UpTrain account [here](https://uptrain.ai/) and get free trial credits. If you want more trial credits, [book a call with the maintainers of UpTrain here](https://calendly.com/uptrain-sourabh/30min).

The benefits of using the managed service are:

1.  No need to set up the UpTrain dashboard on your local machine.
2.  Access to many LLMs without needing their API keys.

Once you perform the evaluations, you can view them in the UpTrain dashboard at `https://dashboard.uptrain.ai/dashboard`

Parameters:

*   key\_type="uptrain"
*   api\_key="UPTRAIN\_API\_KEY"
*   project\_name="PROJECT\_NAME"

**Note:** The `project_name` will be the project name under which the evaluations performed will be shown in the UpTrain dashboard.

Create the UpTrain Callback Handler[¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/UpTrainCallback/#create-the-uptrain-callback-handler)
----------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

os.environ\["OPENAI\_API\_KEY"\] \= getpass()

callback\_handler \= UpTrainCallbackHandler(
    key\_type\="openai",
    api\_key\=os.environ\["OPENAI\_API\_KEY"\],
    project\_name\="uptrain\_llamaindex",
)

Settings.callback\_manager \= CallbackManager(\[callback\_handler\])

os.environ\["OPENAI\_API\_KEY"\] = getpass() callback\_handler = UpTrainCallbackHandler( key\_type="openai", api\_key=os.environ\["OPENAI\_API\_KEY"\], project\_name="uptrain\_llamaindex", ) Settings.callback\_manager = CallbackManager(\[callback\_handler\])

Load and Parse Documents[¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/UpTrainCallback/#load-and-parse-documents)
------------------------------------------------------------------------------------------------------------------------------

Load documents from Paul Graham's essay "What I Worked On".

In \[ \]:

Copied!

documents \= SimpleWebPageReader().load\_data(
    \[
        "https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt"
    \]
)

documents = SimpleWebPageReader().load\_data( \[ "https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt" \] )

Parse the document into nodes.

In \[ \]:

Copied!

parser \= SentenceSplitter()
nodes \= parser.get\_nodes\_from\_documents(documents)

parser = SentenceSplitter() nodes = parser.get\_nodes\_from\_documents(documents)

1\. RAG Query Engine Evaluation[¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/UpTrainCallback/#1-rag-query-engine-evaluation)


The **sub-question query engine** is used to tackle the problem of answering a complex query using multiple data sources. It first breaks down the complex query into sub-questions for each relevant data source, then gathers all the intermediate responses and synthesizes a final response.

UpTrain callback handler will automatically capture the sub-question and the responses for each of them once generated and will run the following three evaluations _(Graded from 0 to 1)_ on the response:

*   **[Context Relevance](https://docs.uptrain.ai/predefined-evaluations/context-awareness/context-relevance)**: Determines if the retrieved context has sufficient information to answer the user query or not.
*   **[Factual Accuracy](https://docs.uptrain.ai/predefined-evaluations/context-awareness/factual-accuracy)**: Assesses if the LLM's response can be verified via the retrieved context.
*   **[Response Completeness](https://docs.uptrain.ai/predefined-evaluations/response-quality/response-completeness)**: Checks if the response contains all the information required to answer the user query comprehensively.

In addition to the above evaluations, the callback handler will also run the following evaluation:

*   **[Sub Query Completeness](https://docs.uptrain.ai/predefined-evaluations/query-quality/sub-query-completeness)**: Assures that the sub-questions accurately and comprehensively cover the original query.

In \[ \]:

Copied!

\# build index and query engine
vector\_query\_engine \= VectorStoreIndex.from\_documents(
    documents\=documents,
    use\_async\=True,
).as\_query\_engine()

query\_engine\_tools \= \[
    QueryEngineTool(
        query\_engine\=vector\_query\_engine,
        metadata\=ToolMetadata(
            name\="documents",
            description\="Paul Graham essay on What I Worked On",
        ),
    ),
\]

query\_engine \= SubQuestionQueryEngine.from\_defaults(
    query\_engine\_tools\=query\_engine\_tools,
    use\_async\=True,
)

response \= query\_engine.query(
    "How was Paul Grahams life different before, during, and after YC?"
)

\# build index and query engine vector\_query\_engine = VectorStoreIndex.from\_documents( documents=documents, use\_async=True, ).as\_query\_engine() query\_engine\_tools = \[ QueryEngineTool( query\_engine=vector\_query\_engine, metadata=ToolMetadata( name="documents", description="Paul Graham essay on What I Worked On", ), ), \] query\_engine = SubQuestionQueryEngine.from\_defaults( query\_engine\_tools=query\_engine\_tools, use\_async=True, ) response = query\_engine.query( "How was Paul Grahams life different before, during, and after YC?" )

Generated 3 sub questions.
\[documents\] Q: What did Paul Graham work on before YC?
\[documents\] Q: What did Paul Graham work on during YC?
\[documents\] Q: What did Paul Graham work on after YC?
\[documents\] A: After Y Combinator, Paul Graham decided to focus on painting as his next endeavor.
\[documents\] A: Paul Graham worked on writing essays and working on Y Combinator during YC.
\[documents\] A: Before Y Combinator, Paul Graham worked on projects with his colleagues Robert and Trevor.

100%|██████████| 3/3 \[00:02<00:00,  1.47it/s\]
100%|██████████| 3/3 \[00:00<00:00,  3.28it/s\]
100%|██████████| 3/3 \[00:01<00:00,  1.68it/s\]
100%|██████████| 3/3 \[00:01<00:00,  2.28it/s\]

Question: What did Paul Graham work on after YC?
Response: After Y Combinator, Paul Graham decided to focus on painting as his next endeavor.

Context Relevance Score: 0.0
Factual Accuracy Score: 0.0
Response Completeness Score: 0.5


Question: What did Paul Graham work on during YC?
Response: Paul Graham worked on writing essays and working on Y Combinator during YC.

Context Relevance Score: 0.0
Factual Accuracy Score: 1.0
Response Completeness Score: 0.5


Question: What did Paul Graham work on before YC?
Response: Before Y Combinator, Paul Graham worked on projects with his colleagues Robert and Trevor.

Context Relevance Score: 0.0
Factual Accuracy Score: 0.0
Response Completeness Score: 0.5

100%|██████████| 1/1 \[00:01<00:00,  1.24s/it\]

Question: How was Paul Grahams life different before, during, and after YC?
Sub Query Completeness Score: 1.0

3\. Re-ranking[¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/UpTrainCallback/#3-re-ranking)


If the number of nodes returned after re-ranking is the lesser as the original number of nodes, the following evaluation will be performed:

*   **[Context Conciseness](https://docs.uptrain.ai/predefined-evaluations/context-awareness/context-conciseness)**: Examines whether the reduced number of nodes still provides all the required information.

In \[ \]:

Copied!

callback\_handler \= UpTrainCallbackHandler(
    key\_type\="openai",
    api\_key\=os.environ\["OPENAI\_API\_KEY"\],
    project\_name\="uptrain\_llamaindex",
)
Settings.callback\_manager \= CallbackManager(\[callback\_handler\])

rerank\_postprocessor \= SentenceTransformerRerank(
    top\_n\=2,  \# Number of nodes after re-ranking
    keep\_retrieval\_score\=True,
)

index \= VectorStoreIndex.from\_documents(
    documents\=documents,
)
query\_engine \= index.as\_query\_engine(
    similarity\_top\_k\=5,  \# Number of nodes before re-ranking
    node\_postprocessors\=\[rerank\_postprocessor\],
)

\# Use your advanced RAG
response \= query\_engine.query(
    "What did Sam Altman do in this essay?",
)

callback\_handler = UpTrainCallbackHandler( key\_type="openai", api\_key=os.environ\["OPENAI\_API\_KEY"\], project\_name="uptrain\_llamaindex", ) Settings.callback\_manager = CallbackManager(\[callback\_handler\]) rerank\_postprocessor = SentenceTransformerRerank( top\_n=2, # Number of nodes after re-ranking keep\_retrieval\_score=True, ) index = VectorStoreIndex.from\_documents( documents=documents, ) query\_engine = index.as\_query\_engine( similarity\_top\_k=5, # Number of nodes before re-ranking node\_postprocessors=\[rerank\_postprocessor\], ) # Use your advanced RAG response = query\_engine.query( "What did Sam Altman do in this essay?", )

100%|██████████| 1/1 \[00:02<00:00,  2.22s/it\]

Question: What did Sam Altman do in this essay?
Context Conciseness Score: 0.0

100%|██████████| 1/1 \[00:01<00:00,  1.58s/it\]
100%|██████████| 1/1 \[00:00<00:00,  1.19it/s\]
100%|██████████| 1/1 \[00:01<00:00,  1.62s/it\]
100%|██████████| 1/1 \[00:01<00:00,  1.42s/it\]

Question: What did Sam Altman do in this essay?
Response: Sam Altman offered unsolicited advice to the author during a visit to California for interviews.

Context Relevance Score: 0.0
Factual Accuracy Score: 1.0
Response Completeness Score: 0.5

UpTrain's Dashboard and Insights[¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/UpTrainCallback/#uptrains-dashboard-and-insights)


Here's a short video showcasing the dashboard and the insights:

![Image 4: llamaindex_uptrain.gif](https://uptrain-assets.s3.ap-south-1.amazonaws.com/images/llamaindex/llamaindex_uptrain.gif)

Back to top

[Previous Token Counting Handler](https://docs.llamaindex.ai/en/stable/examples/callbacks/TokenCountingHandler/)[Next Wandb Callback Handler](https://docs.llamaindex.ai/en/stable/examples/callbacks/WandbCallbackHandler/)
