Title: 💬🤖 How to Build a Chatbot

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/Chatbot_SEC/

Markdown Content:
💬🤖 How to Build a Chatbot - LlamaIndex


LlamaIndex serves as a bridge between your data and Language Learning Models (LLMs), providing a toolkit that enables you to establish a query interface around your data for a variety of tasks, such as question-answering and summarization.

In this tutorial, we'll walk you through building a context-augmented chatbot using a [Data Agent](https://gpt-index.readthedocs.io/en/stable/core_modules/agent_modules/agents/root.html). This agent, powered by LLMs, is capable of intelligently executing tasks over your data. The end result is a chatbot agent equipped with a robust set of data interface tools provided by LlamaIndex to answer queries about your data.

**Note**: This tutorial builds upon initial work on creating a query interface over SEC 10-K filings - [check it out here](https://medium.com/@jerryjliu98/how-unstructured-and-llamaindex-can-help-bring-the-power-of-llms-to-your-own-data-3657d063e30d).

### Context[¶](https://docs.llamaindex.ai/en/stable/examples/agent/Chatbot_SEC/#context)

In this guide, we’ll build a "10-K Chatbot" that uses raw UBER 10-K HTML filings from Dropbox. Users can interact with the chatbot to ask questions related to the 10-K filings.

### Preparation[¶](https://docs.llamaindex.ai/en/stable/examples/agent/Chatbot_SEC/#preparation)

In \[ \]:

Copied!

%pip install llama\-index\-readers\-file
%pip install llama\-index\-embeddings\-openai
%pip install llama\-index\-agent\-openai
%pip install llama\-index\-llms\-openai

%pip install llama-index-readers-file %pip install llama-index-embeddings-openai %pip install llama-index-agent-openai %pip install llama-index-llms-openai

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import nest\_asyncio

nest\_asyncio.apply()

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..." import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

\# set text wrapping
from IPython.display import HTML, display

def set\_css():
    display(
        HTML(
            """
  <style>
    pre {
        white-space: pre-wrap;
    }
  </style>
  """
        )
    )

get\_ipython().events.register("pre\_run\_cell", set\_css)

\# set text wrapping from IPython.display import HTML, display def set\_css(): display( HTML( """  """ ) ) get\_ipython().events.register("pre\_run\_cell", set\_css)

### Ingest Data[¶](https://docs.llamaindex.ai/en/stable/examples/agent/Chatbot_SEC/#ingest-data)

Let's first download the raw 10-k files, from 2019-2022.

In \[ \]:

Copied!

\# NOTE: the code examples assume you're operating within a Jupyter notebook.
\# download files
!mkdir data
!wget "https://www.dropbox.com/s/948jr9cfs7fgj99/UBER.zip?dl=1" \-O data/UBER.zip
!unzip data/UBER.zip \-d data

\# NOTE: the code examples assume you're operating within a Jupyter notebook. # download files !mkdir data !wget "https://www.dropbox.com/s/948jr9cfs7fgj99/UBER.zip?dl=1" -O data/UBER.zip !unzip data/UBER.zip -d data

To parse the HTML files into formatted text, we use the [Unstructured](https://github.com/Unstructured-IO/unstructured) library. Thanks to [LlamaHub](https://llamahub.ai/), we can directly integrate with Unstructured, allowing conversion of any text into a Document format that LlamaIndex can ingest.

First we install the necessary packages:

Then we can use the `UnstructuredReader` to parse the HTML files into a list of `Document` objects.

In \[ \]:

Copied!

from llama\_index.readers.file import UnstructuredReader
from pathlib import Path

years \= \[2022, 2021, 2020, 2019\]

loader \= UnstructuredReader()
doc\_set \= {}
all\_docs \= \[\]
for year in years:
    year\_docs \= loader.load\_data(
        file\=Path(f"./data/UBER/UBER\_{year}.html"), split\_documents\=False
    )
    \# insert year metadata into each year
    for d in year\_docs:
        d.metadata \= {"year": year}
    doc\_set\[year\] \= year\_docs
    all\_docs.extend(year\_docs)

from llama\_index.readers.file import UnstructuredReader from pathlib import Path years = \[2022, 2021, 2020, 2019\] loader = UnstructuredReader() doc\_set = {} all\_docs = \[\] for year in years: year\_docs = loader.load\_data( file=Path(f"./data/UBER/UBER\_{year}.html"), split\_documents=False ) # insert year metadata into each year for d in year\_docs: d.metadata = {"year": year} doc\_set\[year\] = year\_docs all\_docs.extend(year\_docs)

### Setting up Vector Indices for each year[¶](https://docs.llamaindex.ai/en/stable/examples/agent/Chatbot_SEC/#setting-up-vector-indices-for-each-year)

We first setup a vector index for each year. Each vector index allows us to ask questions about the 10-K filing of a given year.

We build each index and save it to disk.

In \[ \]:

Copied!

\# initialize simple vector indices
\# NOTE: don't run this cell if the indices are already loaded!
from llama\_index.core import VectorStoreIndex, StorageContext
from llama\_index.embeddings.openai import OpenAIEmbedding
from llama\_index.llms.openai import OpenAI
from llama\_index.core import Settings

Settings.chunk\_size \= 512
Settings.chunk\_overlap \= 64
Settings.llm \= OpenAI(model\="gpt-3.5-turbo")
Settings.embed\_model \= OpenAIEmbedding(model\="text-embedding-3-small")

index\_set \= {}
for year in years:
    storage\_context \= StorageContext.from\_defaults()
    cur\_index \= VectorStoreIndex.from\_documents(
        doc\_set\[year\],
        storage\_context\=storage\_context,
    )
    index\_set\[year\] \= cur\_index
    storage\_context.persist(persist\_dir\=f"./storage/{year}")

\# initialize simple vector indices # NOTE: don't run this cell if the indices are already loaded! from llama\_index.core import VectorStoreIndex, StorageContext from llama\_index.embeddings.openai import OpenAIEmbedding from llama\_index.llms.openai import OpenAI from llama\_index.core import Settings Settings.chunk\_size = 512 Settings.chunk\_overlap = 64 Settings.llm = OpenAI(model="gpt-3.5-turbo") Settings.embed\_model = OpenAIEmbedding(model="text-embedding-3-small") index\_set = {} for year in years: storage\_context = StorageContext.from\_defaults() cur\_index = VectorStoreIndex.from\_documents( doc\_set\[year\], storage\_context=storage\_context, ) index\_set\[year\] = cur\_index storage\_context.persist(persist\_dir=f"./storage/{year}")

To load an index from disk, do the following

In \[ \]:

Copied!

\# Load indices from disk
from llama\_index.core import load\_index\_from\_storage

index\_set \= {}
for year in years:
    storage\_context \= StorageContext.from\_defaults(
        persist\_dir\=f"./storage/{year}"
    )
    cur\_index \= load\_index\_from\_storage(
        storage\_context,
    )
    index\_set\[year\] \= cur\_index

\# Load indices from disk from llama\_index.core import load\_index\_from\_storage index\_set = {} for year in years: storage\_context = StorageContext.from\_defaults( persist\_dir=f"./storage/{year}" ) cur\_index = load\_index\_from\_storage( storage\_context, ) index\_set\[year\] = cur\_index

### Setting up a Sub Question Query Engine to Synthesize Answers Across 10-K Filings[¶](https://docs.llamaindex.ai/en/stable/examples/agent/Chatbot_SEC/#setting-up-a-sub-question-query-engine-to-synthesize-answers-across-10-k-filings)

Since we have access to documents of 4 years, we may not only want to ask questions regarding the 10-K document of a given year, but ask questions that require analysis over all 10-K filings.

To address this, we can use a [Sub Question Query Engine](https://gpt-index.readthedocs.io/en/stable/examples/query_engine/sub_question_query_engine.html). It decomposes a query into subqueries, each answered by an individual vector index, and synthesizes the results to answer the overall query.

LlamaIndex provides some wrappers around indices (and query engines) so that they can be used by query engines and agents. First we define a `QueryEngineTool` for each vector index. Each tool has a name and a description; these are what the LLM agent sees to decide which tool to choose.

In \[ \]:

Copied!

from llama\_index.core.tools import QueryEngineTool, ToolMetadata

individual\_query\_engine\_tools \= \[
    QueryEngineTool(
        query\_engine\=index\_set\[year\].as\_query\_engine(),
        metadata\=ToolMetadata(
            name\=f"vector\_index\_{year}",
            description\=(
                "useful for when you want to answer queries about the"
                f" {year} SEC 10-K for Uber"
            ),
        ),
    )
    for year in years
\]

from llama\_index.core.tools import QueryEngineTool, ToolMetadata individual\_query\_engine\_tools = \[ QueryEngineTool( query\_engine=index\_set\[year\].as\_query\_engine(), metadata=ToolMetadata( name=f"vector\_index\_{year}", description=( "useful for when you want to answer queries about the" f" {year} SEC 10-K for Uber" ), ), ) for year in years \]

Now we can create the Sub Question Query Engine, which will allow us to synthesize answers across the 10-K filings. We pass in the `individual_query_engine_tools` we defined above.

In \[ \]:

Copied!

from llama\_index.core.query\_engine import SubQuestionQueryEngine

query\_engine \= SubQuestionQueryEngine.from\_defaults(
    query\_engine\_tools\=individual\_query\_engine\_tools,
)

from llama\_index.core.query\_engine import SubQuestionQueryEngine query\_engine = SubQuestionQueryEngine.from\_defaults( query\_engine\_tools=individual\_query\_engine\_tools, )

### Setting up the Chatbot Agent[¶](https://docs.llamaindex.ai/en/stable/examples/agent/Chatbot_SEC/#setting-up-the-chatbot-agent)

We use a LlamaIndex Data Agent to setup the outer chatbot agent, which has access to a set of Tools. Specifically, we will use an OpenAIAgent, that takes advantage of OpenAI API function calling. We want to use the separate Tools we defined previously for each index (corresponding to a given year), as well as a tool for the sub question query engine we defined above.

First we define a `QueryEngineTool` for the sub question query engine:

In \[ \]:

Copied!

query\_engine\_tool \= QueryEngineTool(
    query\_engine\=query\_engine,
    metadata\=ToolMetadata(
        name\="sub\_question\_query\_engine",
        description\=(
            "useful for when you want to answer queries that require analyzing"
            " multiple SEC 10-K documents for Uber"
        ),
    ),
)

query\_engine\_tool = QueryEngineTool( query\_engine=query\_engine, metadata=ToolMetadata( name="sub\_question\_query\_engine", description=( "useful for when you want to answer queries that require analyzing" " multiple SEC 10-K documents for Uber" ), ), )

Then, we combine the Tools we defined above into a single list of tools for the agent:

In \[ \]:

Copied!

tools \= individual\_query\_engine\_tools + \[query\_engine\_tool\]

tools = individual\_query\_engine\_tools + \[query\_engine\_tool\]

Finally, we call `OpenAIAgent.from_tools` to create the agent, passing in the list of tools we defined above.

In \[ \]:

Copied!

from llama\_index.agent.openai import OpenAIAgent

agent \= OpenAIAgent.from\_tools(tools, verbose\=True)

from llama\_index.agent.openai import OpenAIAgent agent = OpenAIAgent.from\_tools(tools, verbose=True)

### Testing the Agent[¶](https://docs.llamaindex.ai/en/stable/examples/agent/Chatbot_SEC/#testing-the-agent)

We can now test the agent with various queries.

If we test it with a simple "hello" query, the agent does not use any Tools.

In \[ \]:

Copied!

response \= agent.chat("hi, i am bob")
print(str(response))

response = agent.chat("hi, i am bob") print(str(response))

Added user message to memory: hi, i am bob
Hello Bob! How can I assist you today?

If we test it with a query regarding the 10-k of a given year, the agent will use the relevant vector index Tool.

In \[ \]:

Copied!

response \= agent.chat(
    "What were some of the biggest risk factors in 2020 for Uber?"
)
print(str(response))

response = agent.chat( "What were some of the biggest risk factors in 2020 for Uber?" ) print(str(response))

Added user message to memory: What were some of the biggest risk factors in 2020 for Uber?

Calling function: vector\_index\_2020 with args: {
  "input": "biggest risk factors"
}
Got output: The biggest risk factors mentioned in the context are:

1. The adverse impact of the COVID-19 pandemic and actions taken to mitigate it on the business.
2. The potential reclassification of drivers as employees, workers, or quasi-employees instead of independent contractors.
3. Intense competition in the mobility, delivery, and logistics industries.
4. The need to lower fares or service fees and offer driver incentives and consumer discounts to remain competitive.
5. Significant losses incurred and the uncertainty of achieving profitability.
6. Difficulty in attracting and maintaining a critical mass of platform users.
7. Operational, compliance, and cultural challenges.
8. Negative media coverage and reputation issues.
9. Inability to optimize organizational structure or manage growth effectively.
10. Safety incidents that harm the ability to attract and retain platform users.
11. Risks associated with substantial investments in new offerings and technologies.
12. Potential fines or enforcement measures due to challenges faced.
13. Uncertainty and potential long-term financial impact of the COVID-19 pandemic, including changes in user behavior and demand for mobility services.
14. Potential adverse impact from business partners and third-party vendors affected by the pandemic.
15. Volatility in financial markets and its effect on stock price and access to capital markets.

These are the biggest risk factors mentioned in the given context.
 Calling Function 


Calling function: vector\_index\_2022 with args: {
  "input": "risk factors"
}
Got output: Some of the risk factors mentioned in the context include the potential failure to meet regulatory requirements related to climate change, the impact of contagious diseases and pandemics on the business, the occurrence of catastrophic events, the uncertainty surrounding future pandemics or disease outbreaks, and the competitive nature of the mobility, delivery, and logistics industries. Additionally, the classification of drivers as employees instead of independent contractors, the need to lower fares or service fees to remain competitive, and the company's history of significant losses and anticipated increase in operating expenses are also mentioned as risk factors.
 Calling Function 


Calling function: vector\_index\_2020 with args: {
  "input": "risk factors"
}
Got output: The risk factors mentioned in the context include the adverse impact of the COVID-19 pandemic, potential reclassification of drivers as employees, intense competition in the mobility, delivery, and logistics industries, the need to lower fares and offer incentives to remain competitive, significant losses and increased operating expenses, the importance of attracting and maintaining platform users, operational and cultural challenges, negative media coverage affecting brand reputation, difficulties in managing growth and organizational structure, safety incidents, risks associated with new ventures and investments, legal uncertainties, challenges in international operations, currency fluctuations, tax consequences, financial reporting burdens, political and economic instability, public health concerns, and limited influence over minority-owned affiliates. These risk factors could have an adverse effect on the business, financial condition, operating results, and prospects of the company.
 Calling Function 

Here is a comparison of the risk factors described in the Uber 10-K across years:

2022:
- Potential failure to meet regulatory requirements related to climate change
- Impact of contagious diseases and pandemics on the business
- Occurrence of catastrophic events
- Uncertainty surrounding future pandemics or disease outbreaks
- Competitive nature of the mobility, delivery, and logistics industries
- Classification of drivers as employees instead of independent contractors
- Need to lower fares or service fees to remain competitive
- History of significant losses and anticipated increase in operating expenses

2021:
- Adverse impact of the COVID-19 pandemic and actions to mitigate it
- Potential reclassification of drivers as employees instead of independent contractors
- Intense competition in the mobility, delivery, and logistics industries
- Need to lower fares or service fees and offer driver incentives and consumer discounts
- Significant losses incurred and uncertainty of achieving profitability
- Difficulty in attracting and maintaining a critical mass of platform users
- Operational, compliance, and cultural challenges
- Negative media coverage and reputation issues
- Inability to optimize organizational structure or manage growth effectively
- Safety incidents that harm the ability to attract and retain platform users
- Risks associated with substantial investments in new offerings and technologies

2020:
- Adverse impact of the COVID-19 pandemic and actions taken to mitigate it
- Potential reclassification of drivers as employees, workers, or quasi-employees instead of independent contractors
- Intense competition in the mobility, delivery, and logistics industries
- Need to lower fares or service fees and offer driver incentives and consumer discounts
- Significant losses incurred and uncertainty of achieving profitability
- Difficulty in attracting and maintaining a critical mass of platform users
- Operational, compliance, and cultural challenges
- Negative media coverage and reputation issues
- Inability to optimize organizational structure or manage growth effectively
- Safety incidents that harm the ability to attract and retain platform users
- Risks associated with substantial investments in new offerings and technologies
- Potential fines or enforcement measures due to challenges faced
- Uncertainty and potential long-term financial impact of the COVID-19 pandemic
- Potential adverse impact from business partners and third-party vendors affected by the pandemic
- Volatility in financial markets and its effect on stock price and access to capital markets

2019:
- Highly competitive personal mobility, meal delivery, and logistics industries
- Potential inability to compete effectively in these industries

These bullet points highlight the similarities and differences in the risk factors described in the Uber 10-K across years.

### Setting up the Chatbot Loop[¶](https://docs.llamaindex.ai/en/stable/examples/agent/Chatbot_SEC/#setting-up-the-chatbot-loop)

Now that we have the chatbot setup, it only takes a few more steps to setup a basic interactive loop to chat with our SEC-augmented chatbot!

In \[ \]:

Copied!

agent \= OpenAIAgent.from\_tools(tools)  \# verbose=False by default

while True:
    text\_input \= input("User: ")
    if text\_input \ "exit": break response = agent.chat(text\_input) print(f"Agent: {response}") # User: What were some of the legal proceedings against Uber in 2022?

Agent: In 2022, Uber is facing several legal proceedings. Here are some of them:

1. California: The state Attorney General and city attorneys filed a complaint against Uber and Lyft, alleging that drivers are misclassified as independent contractors. A preliminary injunction was issued but stayed pending appeal. The Court of Appeal affirmed the lower court's ruling, and Uber filed a petition for review with the California Supreme Court. However, the Supreme Court declined the petition for review. The lawsuit is ongoing, focusing on claims by the California Attorney General for periods prior to the enactment of Proposition 22.

2. Massachusetts: The Attorney General of Massachusetts filed a complaint against Uber, alleging that drivers are employees entitled to wage and labor law protections. Uber's motion to dismiss the complaint was denied, and a summary judgment motion is pending.

3. New York: Uber is facing allegations of misclassification and employment violations by the state Attorney General. The resolution of this matter is uncertain.

4. Switzerland: Several administrative bodies in Switzerland have issued rulings classifying Uber drivers as employees for social security or labor purposes. Uber is challenging these rulings before the Social Security and Administrative Tribunals.

These are some of the legal proceedings against Uber in 2022. The outcomes and potential losses in these cases are uncertain.

Back to top

[Previous Examples](https://docs.llamaindex.ai/en/stable/examples/)[Next GPT Builder Demo](https://docs.llamaindex.ai/en/stable/examples/agent/agent_builder/)

Hi, how can I help you?

🦙
