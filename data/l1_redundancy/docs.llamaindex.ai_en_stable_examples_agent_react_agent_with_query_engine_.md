Title: ReAct Agent with Query Engine (RAG) Tools

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/react_agent_with_query_engine/

Markdown Content:
ReAct Agent with Query Engine (RAG) Tools - LlamaIndex


In this section, we show how to setup an agent powered by the ReAct loop for financial analysis.

The agent has access to two "tools": one to query the 2021 Lyft 10-K and the other to query the 2021 Uber 10-K.

We try two different LLMs:

*   gpt-3.5-turbo
*   gpt-3.5-turbo-instruct

Note that you can plug in any LLM that exposes a text completion endpoint.

Build Query Engine Tools[¶](https://docs.llamaindex.ai/en/stable/examples/agent/react_agent_with_query_engine/#build-query-engine-tools)
----------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai

%pip install llama-index-llms-openai

In \[ \]:

Copied!

from llama\_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
    load\_index\_from\_storage,
)

from llama\_index.core.tools import QueryEngineTool, ToolMetadata

from llama\_index.core import ( SimpleDirectoryReader, VectorStoreIndex, StorageContext, load\_index\_from\_storage, ) from llama\_index.core.tools import QueryEngineTool, ToolMetadata

In \[ \]:

Copied!

try:
    storage\_context \= StorageContext.from\_defaults(
        persist\_dir\="./storage/lyft"
    )
    lyft\_index \= load\_index\_from\_storage(storage\_context)

    storage\_context \= StorageContext.from\_defaults(
        persist\_dir\="./storage/uber"
    )
    uber\_index \= load\_index\_from\_storage(storage\_context)

    index\_loaded \= True
except:
    index\_loaded \= False

try: storage\_context = StorageContext.from\_defaults( persist\_dir="./storage/lyft" ) lyft\_index = load\_index\_from\_storage(storage\_context) storage\_context = StorageContext.from\_defaults( persist\_dir="./storage/uber" ) uber\_index = load\_index\_from\_storage(storage\_context) index\_loaded = True except: index\_loaded = False

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/10k/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' \-O 'data/10k/uber\_2021.pdf'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/lyft\_2021.pdf' \-O 'data/10k/lyft\_2021.pdf'

!mkdir -p 'data/10k/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' -O 'data/10k/uber\_2021.pdf' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/lyft\_2021.pdf' -O 'data/10k/lyft\_2021.pdf'

In \[ \]:

Copied!

if not index\_loaded:
    \# load data
    lyft\_docs \= SimpleDirectoryReader(
        input\_files\=\["./data/10k/lyft\_2021.pdf"\]
    ).load\_data()
    uber\_docs \= SimpleDirectoryReader(
        input\_files\=\["./data/10k/uber\_2021.pdf"\]
    ).load\_data()

    \# build index
    lyft\_index \= VectorStoreIndex.from\_documents(lyft\_docs)
    uber\_index \= VectorStoreIndex.from\_documents(uber\_docs)

    \# persist index
    lyft\_index.storage\_context.persist(persist\_dir\="./storage/lyft")
    uber\_index.storage\_context.persist(persist\_dir\="./storage/uber")

if not index\_loaded: # load data lyft\_docs = SimpleDirectoryReader( input\_files=\["./data/10k/lyft\_2021.pdf"\] ).load\_data() uber\_docs = SimpleDirectoryReader( input\_files=\["./data/10k/uber\_2021.pdf"\] ).load\_data() # build index lyft\_index = VectorStoreIndex.from\_documents(lyft\_docs) uber\_index = VectorStoreIndex.from\_documents(uber\_docs) # persist index lyft\_index.storage\_context.persist(persist\_dir="./storage/lyft") uber\_index.storage\_context.persist(persist\_dir="./storage/uber")

In \[ \]:

Copied!

lyft\_engine \= lyft\_index.as\_query\_engine(similarity\_top\_k\=3)
uber\_engine \= uber\_index.as\_query\_engine(similarity\_top\_k\=3)

lyft\_engine = lyft\_index.as\_query\_engine(similarity\_top\_k=3) uber\_engine = uber\_index.as\_query\_engine(similarity\_top\_k=3)

In \[ \]:

Copied!

query\_engine\_tools \= \[
    QueryEngineTool(
        query\_engine\=lyft\_engine,
        metadata\=ToolMetadata(
            name\="lyft\_10k",
            description\=(
                "Provides information about Lyft financials for year 2021. "
                "Use a detailed plain text question as input to the tool."
            ),
        ),
    ),
    QueryEngineTool(
        query\_engine\=uber\_engine,
        metadata\=ToolMetadata(
            name\="uber\_10k",
            description\=(
                "Provides information about Uber financials for year 2021. "
                "Use a detailed plain text question as input to the tool."
            ),
        ),
    ),
\]

query\_engine\_tools = \[ QueryEngineTool( query\_engine=lyft\_engine, metadata=ToolMetadata( name="lyft\_10k", description=( "Provides information about Lyft financials for year 2021. " "Use a detailed plain text question as input to the tool." ), ), ), QueryEngineTool( query\_engine=uber\_engine, metadata=ToolMetadata( name="uber\_10k", description=( "Provides information about Uber financials for year 2021. " "Use a detailed plain text question as input to the tool." ), ), ), \]

Setup ReAct Agent[¶](https://docs.llamaindex.ai/en/stable/examples/agent/react_agent_with_query_engine/#setup-react-agent)
--------------------------------------------------------------------------------------------------------------------------

Here we setup two ReAct agents: one powered by standard gpt-3.5-turbo, and the other powered by gpt-3.5-turbo-instruct.

You can **optionally** specify context which will be added to the core ReAct system prompt.

In \[ \]:

Copied!

from llama\_index.core.agent import ReActAgent
from llama\_index.llms.openai import OpenAI

from llama\_index.core.agent import ReActAgent from llama\_index.llms.openai import OpenAI

In \[ \]:

Copied!

\# \[Optional\] Add Context
\# context = """\\
\# You are a stock market sorcerer who is an expert on the companies Lyft and Uber.\\
\#     You will answer questions about Uber and Lyft as in the persona of a sorcerer \\
\#     and veteran stock market investor.
\# """
llm \= OpenAI(model\="gpt-3.5-turbo-0613")

agent \= ReActAgent.from\_tools(
    query\_engine\_tools,
    llm\=llm,
    verbose\=True,
    \# context=context
)

\# \[Optional\] Add Context # context = """\\ # You are a stock market sorcerer who is an expert on the companies Lyft and Uber.\\ # You will answer questions about Uber and Lyft as in the persona of a sorcerer \\ # and veteran stock market investor. # """ llm = OpenAI(model="gpt-3.5-turbo-0613") agent = ReActAgent.from\_tools( query\_engine\_tools, llm=llm, verbose=True, # context=context )

In \[ \]:

Copied!

response \= agent.chat("What was Lyft's revenue growth in 2021?")
print(str(response))

response = agent.chat("What was Lyft's revenue growth in 2021?") print(str(response))

Thought: I need to use a tool to help me answer the question.
Action: lyft\_10k
Action Input: {'input': "What was Lyft's revenue growth in 2021?"}
Observation: Lyft's revenue growth in 2021 was 36%.
Response: Lyft's revenue growth in 2021 was 36%.
Lyft's revenue growth in 2021 was 36%.

Run Some Example Queries[¶](https://docs.llamaindex.ai/en/stable/examples/agent/react_agent_with_query_engine/#run-some-example-queries)
----------------------------------------------------------------------------------------------------------------------------------------

We run some example queries using the agent, showcasing some of the agent's abilities to do chain-of-thought-reasoning and tool use to synthesize the right answer.

We also show queries.

In \[ \]:

Copied!

response \= agent.chat(
    "Compare and contrast the revenue growth of Uber and Lyft in 2021, then"
    " give an analysis"
)
print(str(response))

response = agent.chat( "Compare and contrast the revenue growth of Uber and Lyft in 2021, then" " give an analysis" ) print(str(response))

Thought: I need to use a tool to help me compare the revenue growth of Uber and Lyft in 2021.
Action: lyft\_10k
Action Input: {'input': "What was Lyft's revenue growth in 2021?"}
Observation: Lyft's revenue growth in 2021 was 36%.
Thought: I need to use a tool to help me compare the revenue growth of Uber and Lyft in 2021.
Action: uber\_10k
Action Input: {'input': "What was Uber's revenue growth in 2021?"}
Observation: Uber's revenue growth in 2021 was 57%.
Response: In 2021, Lyft's revenue growth was 36% while Uber's revenue growth was 57%. This indicates that Uber experienced a higher revenue growth compared to Lyft in 2021.
In 2021, Lyft's revenue growth was 36% while Uber's revenue growth was 57%. This indicates that Uber experienced a higher revenue growth compared to Lyft in 2021.

**Async execution**: Here we try another query with async execution

In \[ \]:

Copied!

\# Try another query with async execution

import nest\_asyncio

nest\_asyncio.apply()

response \= await agent.achat(
    "Compare and contrast the risks of Uber and Lyft in 2021, then give an"
    " analysis"
)
print(str(response))

\# Try another query with async execution import nest\_asyncio nest\_asyncio.apply() response = await agent.achat( "Compare and contrast the risks of Uber and Lyft in 2021, then give an" " analysis" ) print(str(response))

### Compare gpt-3.5-turbo vs. gpt-3.5-turbo-instruct[¶](https://docs.llamaindex.ai/en/stable/examples/agent/react_agent_with_query_engine/#compare-gpt-35-turbo-vs-gpt-35-turbo-instruct)

We compare the performance of the two agents in being able to answer some complex queries.

#### Taking a look at a turbo-instruct agent[¶](https://docs.llamaindex.ai/en/stable/examples/agent/react_agent_with_query_engine/#taking-a-look-at-a-turbo-instruct-agent)

In \[ \]:

Copied!

llm\_instruct \= OpenAI(model\="gpt-3.5-turbo-instruct")
agent\_instruct \= ReActAgent.from\_tools(
    query\_engine\_tools, llm\=llm\_instruct, verbose\=True
)

llm\_instruct = OpenAI(model="gpt-3.5-turbo-instruct") agent\_instruct = ReActAgent.from\_tools( query\_engine\_tools, llm=llm\_instruct, verbose=True )

In \[ \]:

Copied!

response \= agent\_instruct.chat("What was Lyft's revenue growth in 2021?")
print(str(response))

response = agent\_instruct.chat("What was Lyft's revenue growth in 2021?") print(str(response))

Thought: I need to use a tool to help me answer the question.
Action: lyft\_10k
Action Input: {'input': "What was Lyft's revenue growth in 2021?"}
Observation: Lyft's revenue growth in 2021 was 36%.
Response: Lyft's revenue growth in 2021 was 36%.
Lyft's revenue growth in 2021 was 36%.

#### Try more complex queries[¶](https://docs.llamaindex.ai/en/stable/examples/agent/react_agent_with_query_engine/#try-more-complex-queries)

We compare gpt-3.5-turbo with gpt-3.5-turbo-instruct agents on more complex queries.

In \[ \]:

Copied!

response \= agent.chat(
    "Compare and contrast the revenue growth of Uber and Lyft in 2021, then"
    " give an analysis"
)
print(str(response))

response = agent.chat( "Compare and contrast the revenue growth of Uber and Lyft in 2021, then" " give an analysis" ) print(str(response))

Thought: I need to use a tool to help me compare the revenue growth of Uber and Lyft in 2021.
Action: uber\_10k
Action Input: {'input': "Please provide information about Uber's revenue growth in 2021."}
Observation: Uber's revenue grew by 57% in 2021 compared to the previous year. This growth was primarily driven by an increase in Gross Bookings, with Delivery Gross Bookings increasing by 71% and Mobility Gross Bookings growing by 38%. The increase in Delivery Gross Bookings was due to higher demand for food delivery orders and expansion across U.S. and international markets. The growth in Mobility Gross Bookings was a result of increased Trip volumes as the business recovered from the impacts of COVID-19.
Thought: I have information about Uber's revenue growth in 2021. Now I need to use a tool to get information about Lyft's revenue growth in 2021.
Action: lyft\_10k
Action Input: {'input': "Please provide information about Lyft's revenue growth in 2021."}
Observation: Lyft's revenue increased by 36% in 2021 compared to the prior year.
Response: In 2021, Uber experienced a higher revenue growth rate of 57% compared to Lyft's growth rate of 36%. This indicates that Uber had a stronger performance in terms of revenue growth during that period. The growth in Uber's revenue was primarily driven by an increase in Gross Bookings, with both Delivery and Mobility segments contributing to the growth. The increase in Delivery Gross Bookings was due to higher demand for food delivery services, while the growth in Mobility Gross Bookings was a result of increased trip volumes as the business recovered from the impacts of COVID-19.
In 2021, Uber experienced a higher revenue growth rate of 57% compared to Lyft's growth rate of 36%. This indicates that Uber had a stronger performance in terms of revenue growth during that period. The growth in Uber's revenue was primarily driven by an increase in Gross Bookings, with both Delivery and Mobility segments contributing to the growth. The increase in Delivery Gross Bookings was due to higher demand for food delivery services, while the growth in Mobility Gross Bookings was a result of increased trip volumes as the business recovered from the impacts of COVID-19.

In \[ \]:

Copied!

response \= agent\_instruct.chat(
    "Compare and contrast the revenue growth of Uber and Lyft in 2021, then"
    " give an analysis"
)
print(str(response))

response = agent\_instruct.chat( "Compare and contrast the revenue growth of Uber and Lyft in 2021, then" " give an analysis" ) print(str(response))

Response: The revenue growth of Uber was higher than Lyft in 2021, with Uber experiencing a 74% growth compared to Lyft's 48%. This indicates that Uber may have had a stronger financial performance in 2021. However, further analysis is needed to fully understand the factors contributing to this difference.
The revenue growth of Uber was higher than Lyft in 2021, with Uber experiencing a 74% growth compared to Lyft's 48%. This indicates that Uber may have had a stronger financial performance in 2021. However, further analysis is needed to fully understand the factors contributing to this difference.

In \[ \]:

Copied!

response \= agent.chat(
    "Can you tell me about the risk factors of the company with the higher"
    " revenue?"
)
print(str(response))

response = agent.chat( "Can you tell me about the risk factors of the company with the higher" " revenue?" ) print(str(response))

Thought: I need to find out which company has higher revenue before I can provide information about its risk factors.
Action: lyft\_10k
Action Input: {'input': 'What is the revenue of Lyft in 2021?'}
Observation: The revenue of Lyft in 2021 is $3,208,323,000.
Thought: Now that I know Lyft has higher revenue, I can find information about its risk factors.
Action: lyft\_10k
Action Input: {'input': 'What are the risk factors of Lyft?'}
Observation: Lyft faces numerous risk factors that could potentially harm its business, financial condition, and results of operations. These risk factors include general economic factors such as the impact of the COVID-19 pandemic, natural disasters, economic downturns, and political crises. Operational factors such as limited operating history, financial performance, competition, unpredictability of results, uncertainty regarding market growth, ability to attract and retain drivers and riders, insurance coverage, autonomous vehicle technology, reputation and brand, illegal or improper activity on the platform, accuracy of background checks, changes to pricing practices, growth management, security and privacy breaches, reliance on third parties, and ability to operate various programs and services. Additionally, Lyft faces risks related to its evolving business, including forecasting revenue and managing expenses, complying with laws and regulations, managing assets and expenses during the COVID-19 pandemic, capital expenditures, asset development and utilization, macroeconomic changes, reputation and brand management, growth and business operations, geographic expansion, talent acquisition and retention, platform development, and real estate portfolio management. Furthermore, Lyft's financial performance in recent periods may not be indicative of future performance, and achieving or maintaining profitability in the future is not guaranteed. The Express Drive program and Lyft Rentals program also expose Lyft to risks related to vehicle rental partners, residual value of vehicles, and payment processing.
Response: Lyft faces numerous risk factors that could potentially harm its business, financial condition, and results of operations. These risk factors include general economic factors such as the impact of the COVID-19 pandemic, natural disasters, economic downturns, and political crises. Operational factors such as limited operating history, financial performance, competition, unpredictability of results, uncertainty regarding market growth, ability to attract and retain drivers and riders, insurance coverage, autonomous vehicle technology, reputation and brand, illegal or improper activity on the platform, accuracy of background checks, changes to pricing practices, growth management, security and privacy breaches, reliance on third parties, and ability to operate various programs and services. Additionally, Lyft faces risks related to its evolving business, including forecasting revenue and managing expenses, complying with laws and regulations, managing assets and expenses during the COVID-19 pandemic, capital expenditures, asset development and utilization, macroeconomic changes, reputation and brand management, growth and business operations, geographic expansion, talent acquisition and retention, platform development, and real estate portfolio management. Furthermore, Lyft's financial performance in recent periods may not be indicative of future performance, and achieving or maintaining profitability in the future is not guaranteed. The Express Drive program and Lyft Rentals program also expose Lyft to risks related to vehicle rental partners, residual value of vehicles, and payment processing.
Lyft faces numerous risk factors that could potentially harm its business, financial condition, and results of operations. These risk factors include general economic factors such as the impact of the COVID-19 pandemic, natural disasters, economic downturns, and political crises. Operational factors such as limited operating history, financial performance, competition, unpredictability of results, uncertainty regarding market growth, ability to attract and retain drivers and riders, insurance coverage, autonomous vehicle technology, reputation and brand, illegal or improper activity on the platform, accuracy of background checks, changes to pricing practices, growth management, security and privacy breaches, reliance on third parties, and ability to operate various programs and services. Additionally, Lyft faces risks related to its evolving business, including forecasting revenue and managing expenses, complying with laws and regulations, managing assets and expenses during the COVID-19 pandemic, capital expenditures, asset development and utilization, macroeconomic changes, reputation and brand management, growth and business operations, geographic expansion, talent acquisition and retention, platform development, and real estate portfolio management. Furthermore, Lyft's financial performance in recent periods may not be indicative of future performance, and achieving or maintaining profitability in the future is not guaranteed. The Express Drive program and Lyft Rentals program also expose Lyft to risks related to vehicle rental partners, residual value of vehicles, and payment processing.

In \[ \]:

Copied!

response \= agent\_instruct.query(
    "Can you tell me about the risk factors of the company with the higher"
    " revenue?"
)
print(str(response))

response = agent\_instruct.query( "Can you tell me about the risk factors of the company with the higher" " revenue?" ) print(str(response))

Response: The risk factors for the company with the higher revenue include competition, regulatory changes, and dependence on drivers.
The risk factors for the company with the higher revenue include competition, regulatory changes, and dependence on drivers.

**Observation**: The turbo-instruct agent seems to do worse on agent reasoning compared to the regular turbo model. Of course, this is subject to further observation!

Back to top

[Previous ReAct Agent - A Simple Intro with Calculator Tools](https://docs.llamaindex.ai/en/stable/examples/agent/react_agent/)[Next Controlling Agent Reasoning Loop with Return Direct Tools](https://docs.llamaindex.ai/en/stable/examples/agent/return_direct_agent/)

Hi, how can I help you?

🦙
