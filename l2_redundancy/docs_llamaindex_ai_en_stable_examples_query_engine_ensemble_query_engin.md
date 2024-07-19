Title: Ensemble Query Engine Guide - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/query_engine/ensemble_query_engine/

Markdown Content:
Ensemble Query Engine Guide - LlamaIndex


Oftentimes when building a RAG application there are different query pipelines you need to experiment with (e.g. top-k retrieval, keyword search, knowledge graphs).

Thought: what if we could try a bunch of strategies at once, and have the LLM 1) rate the relevance of each query, and 2) synthesize the results?

This guide showcases this over the Great Gatsby. We do ensemble retrieval over different chunk sizes and also different indices.

**NOTE**: Please also see our closely-related [Ensemble Retrieval Guide](https://gpt-index.readthedocs.io/en/stable/examples/retrievers/ensemble_retrieval.html)!

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai

%pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/ensemble_query_engine/#setup)
-------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

\# NOTE: This is ONLY necessary in jupyter notebook.
\# Details: Jupyter runs an event-loop behind the scenes.
\#          This results in nested event-loops when we start an event-loop to make async queries.
\#          This is normally not allowed, we use nest\_asyncio to allow it for convenience.
import nest\_asyncio

nest\_asyncio.apply()

\# NOTE: This is ONLY necessary in jupyter notebook. # Details: Jupyter runs an event-loop behind the scenes. # This results in nested event-loops when we start an event-loop to make async queries. # This is normally not allowed, we use nest\_asyncio to allow it for convenience. import nest\_asyncio nest\_asyncio.apply()

Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/ensemble_query_engine/#download-data)
-----------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

!wget 'https://raw.githubusercontent.com/jerryjliu/llama\_index/main/examples/gatsby/gatsby\_full.txt' \-O 'gatsby\_full.txt'

!wget 'https://raw.githubusercontent.com/jerryjliu/llama\_index/main/examples/gatsby/gatsby\_full.txt' -O 'gatsby\_full.txt'

Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/ensemble_query_engine/#load-data)
---------------------------------------------------------------------------------------------------------

We first show how to convert a Document into a set of Nodes, and insert into a DocumentStore.

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

\# try loading great gatsby

documents \= SimpleDirectoryReader(
    input\_files\=\["./gatsby\_full.txt"\]
).load\_data()

from llama\_index.core import SimpleDirectoryReader # try loading great gatsby documents = SimpleDirectoryReader( input\_files=\["./gatsby\_full.txt"\] ).load\_data()

Define Query Engines[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/ensemble_query_engine/#define-query-engines)
-------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

\# initialize settings (set chunk size)
from llama\_index.llms.openai import OpenAI
from llama\_index.core import Settings

Settings.llm \= OpenAI(model\="gpt-3.5-turbo")
Settings.chunk\_size \= 1024

nodes \= Settings.node\_parser.get\_nodes\_from\_documents(documents)

\# initialize settings (set chunk size) from llama\_index.llms.openai import OpenAI from llama\_index.core import Settings Settings.llm = OpenAI(model="gpt-3.5-turbo") Settings.chunk\_size = 1024 nodes = Settings.node\_parser.get\_nodes\_from\_documents(documents)

In \[ \]:

Copied!

from llama\_index.core import StorageContext

\# initialize storage context (by default it's in-memory)
storage\_context \= StorageContext.from\_defaults()
storage\_context.docstore.add\_documents(nodes)

from llama\_index.core import StorageContext # initialize storage context (by default it's in-memory) storage\_context = StorageContext.from\_defaults() storage\_context.docstore.add\_documents(nodes)

In \[ \]:

Copied!

from llama\_index.core import SimpleKeywordTableIndex, VectorStoreIndex

keyword\_index \= SimpleKeywordTableIndex(
    nodes,
    storage\_context\=storage\_context,
    show\_progress\=True,
)
vector\_index \= VectorStoreIndex(
    nodes,
    storage\_context\=storage\_context,
    show\_progress\=True,
)

from llama\_index.core import SimpleKeywordTableIndex, VectorStoreIndex keyword\_index = SimpleKeywordTableIndex( nodes, storage\_context=storage\_context, show\_progress=True, ) vector\_index = VectorStoreIndex( nodes, storage\_context=storage\_context, show\_progress=True, )

Extracting keywords from nodes:   0%|          | 0/77 \[00:00<?, ?it/s\]

Generating embeddings:   0%|          | 0/77 \[00:00<?, ?it/s\]

In \[ \]:

Copied!

from llama\_index.core import PromptTemplate

QA\_PROMPT\_TMPL \= (
    "Context information is below.\\n"
    "---------------------\\n"
    "{context\_str}\\n"
    "---------------------\\n"
    "Given the context information and not prior knowledge, "
    "answer the question. If the answer is not in the context, inform "
    "the user that you can't answer the question - DO NOT MAKE UP AN ANSWER.\\n"
    "In addition to returning the answer, also return a relevance score as to "
    "how relevant the answer is to the question. "
    "Question: {query\_str}\\n"
    "Answer (including relevance score): "
)
QA\_PROMPT \= PromptTemplate(QA\_PROMPT\_TMPL)

keyword\_query\_engine \= keyword\_index.as\_query\_engine(
    text\_qa\_template\=QA\_PROMPT
)
vector\_query\_engine \= vector\_index.as\_query\_engine(text\_qa\_template\=QA\_PROMPT)

from llama\_index.core import PromptTemplate QA\_PROMPT\_TMPL = ( "Context information is below.\\n" "---------------------\\n" "{context\_str}\\n" "---------------------\\n" "Given the context information and not prior knowledge, " "answer the question. If the answer is not in the context, inform " "the user that you can't answer the question - DO NOT MAKE UP AN ANSWER.\\n" "In addition to returning the answer, also return a relevance score as to " "how relevant the answer is to the question. " "Question: {query\_str}\\n" "Answer (including relevance score): " ) QA\_PROMPT = PromptTemplate(QA\_PROMPT\_TMPL) keyword\_query\_engine = keyword\_index.as\_query\_engine( text\_qa\_template=QA\_PROMPT ) vector\_query\_engine = vector\_index.as\_query\_engine(text\_qa\_template=QA\_PROMPT)

In \[ \]:

Copied!

response \= vector\_query\_engine.query(
    "Describe and summarize the interactions between Gatsby and Daisy"
)

response = vector\_query\_engine.query( "Describe and summarize the interactions between Gatsby and Daisy" )

In \[ \]:

Copied!

print(response)

print(response)

Gatsby and Daisy's interactions are described as intimate and conspiring. They sit opposite each other at a kitchen table, with Gatsby's hand covering Daisy's hand. They communicate through nods and seem to have a natural intimacy. Gatsby waits for Daisy to go to bed and is reluctant to leave until he knows what she will do. They have a conversation in which Gatsby tells the story of his youth with Dan Cody. Daisy's face is smeared with tears, but Gatsby glows with a new well-being. Gatsby invites Daisy to his house and expresses his desire for her to come. They admire Gatsby's house together and discuss the interesting people who visit. The relevance score of this answer is 10/10.

In \[ \]:

Copied!

response \= keyword\_query\_engine.query(
    "Describe and summarize the interactions between Gatsby and Daisy"
)

response = keyword\_query\_engine.query( "Describe and summarize the interactions between Gatsby and Daisy" )

\> Starting query: Describe and summarize the interactions between Gatsby and Daisy
query keywords: \['describe', 'interactions', 'gatsby', 'summarize', 'daisy'\]
> Extracted keywords: \['gatsby', 'daisy'\]

In \[ \]:

Copied!

print(response)

print(response)

The interactions between Gatsby and Daisy are characterized by a sense of tension and longing. Gatsby is visibly disappointed when Daisy expresses her dissatisfaction with their time together and insists that she didn't have a good time. He feels distant from her and struggles to make her understand his emotions. Gatsby dismisses the significance of the dance and instead focuses on his desire for Daisy to confess her love for him and leave Tom. He yearns for a deep connection with Daisy, but feels that she doesn't fully comprehend his feelings. These interactions highlight the complexities of their relationship and the challenges they face in rekindling their romance. The relevance score for these interactions is 8 out of 10.

Define Router Query Engine[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/ensemble_query_engine/#define-router-query-engine)
-------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core.tools import QueryEngineTool

keyword\_tool \= QueryEngineTool.from\_defaults(
    query\_engine\=keyword\_query\_engine,
    description\="Useful for answering questions about this essay",
)

vector\_tool \= QueryEngineTool.from\_defaults(
    query\_engine\=vector\_query\_engine,
    description\="Useful for answering questions about this essay",
)

from llama\_index.core.tools import QueryEngineTool keyword\_tool = QueryEngineTool.from\_defaults( query\_engine=keyword\_query\_engine, description="Useful for answering questions about this essay", ) vector\_tool = QueryEngineTool.from\_defaults( query\_engine=vector\_query\_engine, description="Useful for answering questions about this essay", )

In \[ \]:

Copied!

from llama\_index.core.query\_engine import RouterQueryEngine
from llama\_index.core.selectors import LLMSingleSelector, LLMMultiSelector
from llama\_index.core.selectors import (
    PydanticMultiSelector,
    PydanticSingleSelector,
)
from llama\_index.core.response\_synthesizers import TreeSummarize

TREE\_SUMMARIZE\_PROMPT\_TMPL \= (
    "Context information from multiple sources is below. Each source may or"
    " may not have \\na relevance score attached to"
    " it.\\n\---------------------\\n{context\_str}\\n\---------------------\\nGiven"
    " the information from multiple sources and their associated relevance"
    " scores (if provided) and not prior knowledge, answer the question. If"
    " the answer is not in the context, inform the user that you can't answer"
    " the question.\\nQuestion: {query\_str}\\nAnswer: "
)

tree\_summarize \= TreeSummarize(
    summary\_template\=PromptTemplate(TREE\_SUMMARIZE\_PROMPT\_TMPL)
)

query\_engine \= RouterQueryEngine(
    selector\=LLMMultiSelector.from\_defaults(),
    query\_engine\_tools\=\[
        keyword\_tool,
        vector\_tool,
    \],
    summarizer\=tree\_summarize,
)

from llama\_index.core.query\_engine import RouterQueryEngine from llama\_index.core.selectors import LLMSingleSelector, LLMMultiSelector from llama\_index.core.selectors import ( PydanticMultiSelector, PydanticSingleSelector, ) from llama\_index.core.response\_synthesizers import TreeSummarize TREE\_SUMMARIZE\_PROMPT\_TMPL = ( "Context information from multiple sources is below. Each source may or" " may not have \\na relevance score attached to" " it.\\n---------------------\\n{context\_str}\\n---------------------\\nGiven" " the information from multiple sources and their associated relevance" " scores (if provided) and not prior knowledge, answer the question. If" " the answer is not in the context, inform the user that you can't answer" " the question.\\nQuestion: {query\_str}\\nAnswer: " ) tree\_summarize = TreeSummarize( summary\_template=PromptTemplate(TREE\_SUMMARIZE\_PROMPT\_TMPL) ) query\_engine = RouterQueryEngine( selector=LLMMultiSelector.from\_defaults(), query\_engine\_tools=\[ keyword\_tool, vector\_tool, \], summarizer=tree\_summarize, )

Experiment with Queries[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/ensemble_query_engine/#experiment-with-queries)
-------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

response \= await query\_engine.aquery(
    "Describe and summarize the interactions between Gatsby and Daisy"
)
print(response)

response = await query\_engine.aquery( "Describe and summarize the interactions between Gatsby and Daisy" ) print(response)

message='OpenAI API response' path=https://api.openai.com/v1/chat/completions processing\_ms=1590 request\_id=b049001384d0e2f2d96e308903351ca3 response\_code=200
Selecting query engine 0: Useful for answering questions about this essay.
Selecting query engine 1: Useful for answering questions about this essay.
> Starting query: Describe and summarize the interactions between Gatsby and Daisy
query keywords: \['interactions', 'summarize', 'describe', 'daisy', 'gatsby'\]
> Extracted keywords: \['daisy', 'gatsby'\]
message='OpenAI API response' path=https://api.openai.com/v1/embeddings processing\_ms=75 request\_id=3f76f611bb063605c3c2365437480f87 response\_code=200
message='OpenAI API response' path=https://api.openai.com/v1/chat/completions processing\_ms=4482 request\_id=597221bd776638356f16034c4d8ad2f6 response\_code=200
message='OpenAI API response' path=https://api.openai.com/v1/chat/completions processing\_ms=5773 request\_id=50a6030879054f470a1e45952b4b80b3 response\_code=200
message='OpenAI API response' path=https://api.openai.com/v1/chat/completions processing\_ms=6478 request\_id=9171e42c7ced18baedc77cc89ec7478c response\_code=200
message='OpenAI API response' path=https://api.openai.com/v1/chat/completions processing\_ms=6166 request\_id=f3218012e3f9a12e00daeee0b9b06f67 response\_code=200
message='OpenAI API response' path=https://api.openai.com/v1/chat/completions processing\_ms=4808 request\_id=ab6887cbec9a44c2342d6402e28129d6 response\_code=200
Combining responses from multiple query engines.
message='OpenAI API response' path=https://api.openai.com/v1/chat/completions processing\_ms=4506 request\_id=5fd128dab043f58111521d19e7c4f59a response\_code=200
The interactions between Gatsby and Daisy are portrayed as intense, passionate, and filled with longing and desire. Gatsby is deeply in love with Daisy and throws extravagant parties in the hopes of winning her back. Despite Daisy's marriage to Tom Buchanan, they reconnect and begin an affair. They spend time together at Gatsby's lavish house and even plan to run away together. However, their relationship ends tragically when Daisy accidentally kills Tom's mistress, Myrtle, while driving Gatsby's car. Gatsby takes the blame for the accident and is later killed by Myrtle's husband. Overall, their interactions explore themes of love, wealth, and the pursuit of happiness.

In \[ \]:

Copied!

response.source\_nodes

response.source\_nodes

Out\[ \]:

\[\]

In \[ \]:

Copied!

response \= await query\_engine.aquery(
    "What part of his past is Gatsby trying to recapture?"
)
print(response)

response = await query\_engine.aquery( "What part of his past is Gatsby trying to recapture?" ) print(response)

Selecting query engine 0: Keywords: Gatsby, past, recapture.
> Starting query: What part of his past is Gatsby trying to recapture?
query keywords: \['gatsby', 'past', 'recapture'\]
> Extracted keywords: \['gatsby', 'past'\]

KeyboardInterrupt

Back to top

[Previous Defining a Custom Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/custom_query_engine/)[Next FLARE Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/flare_query_engine/)

Hi, how can I help you?

🦙
