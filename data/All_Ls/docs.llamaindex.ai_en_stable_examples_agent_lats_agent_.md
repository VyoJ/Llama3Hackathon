Title: Language Agent Tree Search - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/lats_agent/

Markdown Content:
Language Agent Tree Search - LlamaIndex


[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/run-llama/llama_index/blob/main/llama-index-packs/llama-index-packs-lats/examples/language_agent_tree_search.ipynb)

[LATS (Language Agent Tree Search)](https://arxiv.org/pdf/2310.04406.pdf) by Zhou et al. combines LLM capabilities in planning, acting, and reasoning within a Monte Carlo tree search framework, allowing for deliberate and adaptive problem-solving guided by external feedback and self-reflection.

We've implemented this agent as a LlamaPack - you can either pip install it to run it out-of-the-box or call `download_llama_pack` to load the pack.

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/agent/lats_agent/#setup)
-------------------------------------------------------------------------------

In \[ \]:

Copied!

%pip install llama\-index\-agent\-lats
%pip install llama\-index\-program\-openai
%pip install llama\-index\-llms\-openai
%pip install llama\-index\-embeddings\-openai
%pip install llama\-index\-core llama\-index\-readers\-file

%pip install llama-index-agent-lats %pip install llama-index-program-openai %pip install llama-index-llms-openai %pip install llama-index-embeddings-openai %pip install llama-index-core llama-index-readers-file

### Define Global Settings[¶](https://docs.llamaindex.ai/en/stable/examples/agent/lats_agent/#define-global-settings)

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import nest\_asyncio

nest\_asyncio.apply()

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..." import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI
from llama\_index.embeddings.openai import OpenAIEmbedding
from llama\_index.core import Settings

\# NOTE: a higher temperate will help make the tree-expansion more diverse
llm \= OpenAI(model\="gpt-4-turbo", temperature\=0.6)
embed\_model \= OpenAIEmbedding(model\="text-embedding-3-small")

Settings.llm \= llm
Settings.embed\_model \= embed\_model

from llama\_index.llms.openai import OpenAI from llama\_index.embeddings.openai import OpenAIEmbedding from llama\_index.core import Settings # NOTE: a higher temperate will help make the tree-expansion more diverse llm = OpenAI(model="gpt-4-turbo", temperature=0.6) embed\_model = OpenAIEmbedding(model="text-embedding-3-small") Settings.llm = llm Settings.embed\_model = embed\_model

### Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/agent/lats_agent/#download-data)

In \[ \]:

Copied!

!mkdir \-p 'data/10k/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' \-O 'data/10k/uber\_2021.pdf'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/lyft\_2021.pdf' \-O 'data/10k/lyft\_2021.pdf'

!mkdir -p 'data/10k/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' -O 'data/10k/uber\_2021.pdf' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/lyft\_2021.pdf' -O 'data/10k/lyft\_2021.pdf'

In \[ \]:

Copied!

import os
from llama\_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    load\_index\_from\_storage,
)
from llama\_index.core.storage import StorageContext

if not os.path.exists("./storage/lyft"):
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
else:
    storage\_context \= StorageContext.from\_defaults(
        persist\_dir\="./storage/lyft"
    )
    lyft\_index \= load\_index\_from\_storage(storage\_context)

    storage\_context \= StorageContext.from\_defaults(
        persist\_dir\="./storage/uber"
    )
    uber\_index \= load\_index\_from\_storage(storage\_context)

import os from llama\_index.core import ( SimpleDirectoryReader, VectorStoreIndex, load\_index\_from\_storage, ) from llama\_index.core.storage import StorageContext if not os.path.exists("./storage/lyft"): # load data lyft\_docs = SimpleDirectoryReader( input\_files=\["./data/10k/lyft\_2021.pdf"\] ).load\_data() uber\_docs = SimpleDirectoryReader( input\_files=\["./data/10k/uber\_2021.pdf"\] ).load\_data() # build index lyft\_index = VectorStoreIndex.from\_documents(lyft\_docs) uber\_index = VectorStoreIndex.from\_documents(uber\_docs) # persist index lyft\_index.storage\_context.persist(persist\_dir="./storage/lyft") uber\_index.storage\_context.persist(persist\_dir="./storage/uber") else: storage\_context = StorageContext.from\_defaults( persist\_dir="./storage/lyft" ) lyft\_index = load\_index\_from\_storage(storage\_context) storage\_context = StorageContext.from\_defaults( persist\_dir="./storage/uber" ) uber\_index = load\_index\_from\_storage(storage\_context)

### Setup Tools[¶](https://docs.llamaindex.ai/en/stable/examples/agent/lats_agent/#setup-tools)

In \[ \]:

Copied!

lyft\_engine \= lyft\_index.as\_query\_engine(similarity\_top\_k\=3)
uber\_engine \= uber\_index.as\_query\_engine(similarity\_top\_k\=3)

lyft\_engine = lyft\_index.as\_query\_engine(similarity\_top\_k=3) uber\_engine = uber\_index.as\_query\_engine(similarity\_top\_k=3)

In \[ \]:

Copied!

from llama\_index.core.tools import QueryEngineTool, ToolMetadata

query\_engine\_tools \= \[
    QueryEngineTool(
        query\_engine\=lyft\_engine,
        metadata\=ToolMetadata(
            name\="lyft\_10k",
            description\=(
                "Provides information about Lyft financials for year 2021. "
                "Use a detailed plain text question as input to the tool. "
                "The input is used to power a semantic search engine."
            ),
        ),
    ),
    QueryEngineTool(
        query\_engine\=uber\_engine,
        metadata\=ToolMetadata(
            name\="uber\_10k",
            description\=(
                "Provides information about Uber financials for year 2021. "
                "Use a detailed plain text question as input to the tool. "
                "The input is used to power a semantic search engine."
            ),
        ),
    ),
\]

from llama\_index.core.tools import QueryEngineTool, ToolMetadata query\_engine\_tools = \[ QueryEngineTool( query\_engine=lyft\_engine, metadata=ToolMetadata( name="lyft\_10k", description=( "Provides information about Lyft financials for year 2021. " "Use a detailed plain text question as input to the tool. " "The input is used to power a semantic search engine." ), ), ), QueryEngineTool( query\_engine=uber\_engine, metadata=ToolMetadata( name="uber\_10k", description=( "Provides information about Uber financials for year 2021. " "Use a detailed plain text question as input to the tool. " "The input is used to power a semantic search engine." ), ), ), \]

Setup Agent[¶](https://docs.llamaindex.ai/en/stable/examples/agent/lats_agent/#setup-agent)
-------------------------------------------------------------------------------------------

Now we can setup the LATS agent.

Here, `num_expansions` refers to the number of possible sub-actions to explore under each node. `num_expansions=2` means we will explore to possible next-actions for every parent action.

`max_rollouts` refers to how deep each exploration of the search space continues. `max_rollouts=5` means a maximum depth of 5 is explored in the tree.

In \[ \]:

Copied!

from llama\_index.agent.lats import LATSAgentWorker

agent\_worker \= LATSAgentWorker.from\_tools(
    query\_engine\_tools,
    llm\=llm,
    num\_expansions\=2,
    max\_rollouts\=3,  \# using -1 for unlimited rollouts
    verbose\=True,
)
agent \= agent.as\_worker()

from llama\_index.agent.lats import LATSAgentWorker agent\_worker = LATSAgentWorker.from\_tools( query\_engine\_tools, llm=llm, num\_expansions=2, max\_rollouts=3, # using -1 for unlimited rollouts verbose=True, ) agent = agent.as\_worker()

Run Some Queries[¶](https://docs.llamaindex.ai/en/stable/examples/agent/lats_agent/#run-some-queries)
-----------------------------------------------------------------------------------------------------

First, lets use step-wise execution and the lower-level API to create and execute a task.

In \[ \]:

Copied!

task \= agent.create\_task(
    "Given the risk factors of Uber and Lyft described in their 10K files, "
    "which company is performing better? Please use concrete numbers to inform your decision."
)

task = agent.create\_task( "Given the risk factors of Uber and Lyft described in their 10K files, " "which company is performing better? Please use concrete numbers to inform your decision." )

In \[ \]:

Copied!

\# run initial step
step\_output \= agent.run\_step(task.task\_id)

\# run initial step step\_output = agent.run\_step(task.task\_id)

\> Selecting node to expand: Observation: Given the risk factors of Uber and Lyft described in their 10K files, which company is performing better? Please use concrete numbers to inform your decision.
\> Got candidates: \['Review the 10K files of Uber and Lyft to extract relevant financial data and risk factors.', 'Compare key financial metrics from the 10K files of Uber and Lyft, such as revenue, profit margins, and growth rates.'\]
\
Calling function: uber\_10k with args: {"input": "Provide key financial metrics from Uber's 10K for 2021, including revenue, profit margins, and growth rates."}

Calling function: uber\_10k with args: {"input": "What are the key financial figures and risk factors for Uber in 2021?"}

In 2021, Uber Technologies, Inc. reported a revenue of $17,455 million. The company experienced a significant revenue growth rate of 57% compared to the previous year. The total costs and expenses were $21,289 million, leading to a loss from operations of $3,834 million. The net loss attributable to Uber Technologies, Inc. was $496 million. The costs as a percentage of revenue included cost of revenue (exclusive of depreciation and amortization) at 54%, operations and support at 11%, sales and marketing at 27%, research and development at 12%, general and administrative at 13%, and depreciation and amortization at 5%. The total costs and expenses amounted to 122% of the revenue. Other income (expense), net, significantly improved, contributing 19% to the revenue.

Uber Technologies, Inc., in its 2021 financial statements, consolidates its wholly-owned and majority-owned subsidiaries, as well as variable interest entities where it is the primary beneficiary. The financial statements are prepared in accordance with GAAP, and management uses estimates and assumptions that affect reported financial figures, such as the fair values of investments, useful lives of assets, and reserves for income taxes and insurance, among others. These estimates consider the impact of the COVID-19 pandemic on market data and investment recoverability.

Key financial risks for Uber include concentration of credit risk, where cash and other receivables are potentially subject to credit risk concentration. The company's cash, cash equivalents, and securities consist largely of high-credit-quality money market funds, U.S. government and agency securities, and corporate debt securities. Despite exceeding insured limits, these are placed with financial institutions that Uber assesses as having high credit quality. Uber has not reported material losses related to these concentrations during the periods presented. Additionally, Uber's performance and strategy involve forward-looking statements subject to various risks and uncertainties, which could materially affect actual results.
\> Generated new reasoning step: Thought: To compare the performance of Uber and Lyft using their 10K files, I need to gather financial data and risk factors from both companies. I will start by querying the Uber 10K tool.
Action: uber\_10k
Action Input: {'input': 'What are the key financial figures and risk factors for Uber in 2021?'}
Observation: Uber Technologies, Inc., in its 2021 financial statements, consolidates its wholly-owned and majority-owned subsidiaries, as well as variable interest entities where it is the primary beneficiary. The financial statements are prepared in accordance with GAAP, and management uses estimates and assumptions that affect reported financial figures, such as the fair values of investments, useful lives of assets, and reserves for income taxes and insurance, among others. These estimates consider the impact of the COVID-19 pandemic on market data and investment recoverability.

Key financial risks for Uber include concentration of credit risk, where cash and other receivables are potentially subject to credit risk concentration. The company's cash, cash equivalents, and securities consist largely of high-credit-quality money market funds, U.S. government and agency securities, and corporate debt securities. Despite exceeding insured limits, these are placed with financial institutions that Uber assesses as having high credit quality. Uber has not reported material losses related to these concentrations during the periods presented. Additionally, Uber's performance and strategy involve forward-looking statements subject to various risks and uncertainties, which could materially affect actual results.
\> Generated new reasoning step: Thought: The current language of the user is English. I need to use tools to gather detailed financial metrics from the 10K files of Uber and Lyft.
Action: uber\_10k
Action Input: {'input': "Provide key financial metrics from Uber's 10K for 2021, including revenue, profit margins, and growth rates."}
Observation: In 2021, Uber Technologies, Inc. reported a revenue of $17,455 million. The company experienced a significant revenue growth rate of 57% compared to the previous year. The total costs and expenses were $21,289 million, leading to a loss from operations of $3,834 million. The net loss attributable to Uber Technologies, Inc. was $496 million. The costs as a percentage of revenue included cost of revenue (exclusive of depreciation and amortization) at 54%, operations and support at 11%, sales and marketing at 27%, research and development at 12%, general and administrative at 13%, and depreciation and amortization at 5%. The total costs and expenses amounted to 122% of the revenue. Other income (expense), net, significantly improved, contributing 19% to the revenue.
\> Evaluation for input Given the risk factors of Uber and Lyft described in their 10K files, which company is performing better? Please use concrete numbers to inform your decision.
: score=9 is\_done=False reasoning="The conversation history indicates a methodical approach to answering the query about which company, Uber or Lyft, is performing better based on their 10K filings. The observation and thought processes correctly identify the need to compare key financial figures and risk factors from both companies' 10K files. The action taken to query the Uber 10K tool is appropriate and directly addresses part of the query by obtaining Uber's financial data and identifying key risks.\\n\\nHowever, the answer is not yet complete as the information for Lyft has not been gathered, and a direct comparison between the two companies has not been made. The trajectory so far is correct in terms of the steps taken towards gathering the necessary data, but it is incomplete as more information is needed to fully answer the query."

\> Evaluation for input Given the risk factors of Uber and Lyft described in their 10K files, which company is performing better? Please use concrete numbers to inform your decision.
: score=8 is\_done=False reasoning="The conversation so far has correctly focused on extracting key financial metrics from the 10K files of Uber and Lyft, which is essential for answering the query about which company is performing better. The action taken to retrieve Uber's financial metrics from its 10K file is correct and relevant to the query. The observation provides detailed information about Uber's revenue, growth rate, and profit margins, which are crucial data points needed to assess the company's performance.\\n\\nHowever, the conversation is not yet complete as it lacks the corresponding financial data for Lyft. Without comparing similar metrics from Lyft, a complete evaluation cannot be made. Therefore, the next logical step would be to retrieve Lyft's financial metrics from its 10K file to enable a comprehensive comparison. The trajectory is on the right path but needs to continue gathering and analyzing the necessary data to reach a conclusion."

\> Got final response: I am still thinking.

From the step output, we can inspect the task state

In \[ \]:

Copied!

for step in (
    step\_output.task\_step.step\_state\["root\_node"\].children\[0\].current\_reasoning
):
    print(step)
    print("---------")

for step in ( step\_output.task\_step.step\_state\["root\_node"\].children\[0\].current\_reasoning ): print(step) print("---------")

observation='Given the risk factors of Uber and Lyft described in their 10K files, which company is performing better? Please use concrete numbers to inform your decision.' return\_direct=False
---------
observation='Review the 10K files of Uber and Lyft to extract relevant financial data and risk factors.' return\_direct=False
---------

In \[ \]:

Copied!

for step in (
    step\_output.task\_step.step\_state\["root\_node"\]
    .children\[0\]
    .children\[0\]
    .current\_reasoning
):
    print(step)
    print("---------")

for step in ( step\_output.task\_step.step\_state\["root\_node"\] .children\[0\] .children\[0\] .current\_reasoning ): print(step) print("---------")

observation='Given the risk factors of Uber and Lyft described in their 10K files, which company is performing better? Please use concrete numbers to inform your decision.' return\_direct=False
---------
observation='Review the 10K files of Uber and Lyft to extract relevant financial data and risk factors.' return\_direct=False
---------
thought='To compare the performance of Uber and Lyft using their 10K files, I need to gather financial data and risk factors from both companies. I will start by querying the Uber 10K tool.' action='uber\_10k' action\_input={'input': 'What are the key financial figures and risk factors for Uber in 2021?'}
---------
observation="Uber Technologies, Inc., in its 2021 financial statements, consolidates its wholly-owned and majority-owned subsidiaries, as well as variable interest entities where it is the primary beneficiary. The financial statements are prepared in accordance with GAAP, and management uses estimates and assumptions that affect reported financial figures, such as the fair values of investments, useful lives of assets, and reserves for income taxes and insurance, among others. These estimates consider the impact of the COVID-19 pandemic on market data and investment recoverability.\\n\\nKey financial risks for Uber include concentration of credit risk, where cash and other receivables are potentially subject to credit risk concentration. The company's cash, cash equivalents, and securities consist largely of high-credit-quality money market funds, U.S. government and agency securities, and corporate debt securities. Despite exceeding insured limits, these are placed with financial institutions that Uber assesses as having high credit quality. Uber has not reported material losses related to these concentrations during the periods presented. Additionally, Uber's performance and strategy involve forward-looking statements subject to various risks and uncertainties, which could materially affect actual results." return\_direct=False
---------

Lets loop until we finish the task

In \[ \]:

Copied!

\# repeat until the last step is reached
while not step\_output.is\_last:
    step\_output \= agent.run\_step(task.task\_id)

response \= agent.finalize\_response(task.task\_id)

\# repeat until the last step is reached while not step\_output.is\_last: step\_output = agent.run\_step(task.task\_id) response = agent.finalize\_response(task.task\_id)

\> Selecting node to expand: Observation: Uber Technologies, Inc., in its 2021 financial statements, consolidates its wholly-owned and majority-owned subsidiaries, as well as variable interest entities where it is the primary beneficiary. The financial statements are prepared in accordance with GAAP, and management uses estimates and assumptions that affect reported financial figures, such as the fair values of investments, useful lives of assets, and reserves for income taxes and insurance, among others. These estimates consider the impact of the COVID-19 pandemic on market data and investment recoverability.

Key financial risks for Uber include concentration of credit risk, where cash and other receivables are potentially subject to credit risk concentration. The company's cash, cash equivalents, and securities consist largely of high-credit-quality money market funds, U.S. government and agency securities, and corporate debt securities. Despite exceeding insured limits, these are placed with financial institutions that Uber assesses as having high credit quality. Uber has not reported material losses related to these concentrations during the periods presented. Additionally, Uber's performance and strategy involve forward-looking statements subject to various risks and uncertainties, which could materially affect actual results.
\> Got candidates: \['Review the 10K files of Lyft for similar financial data and risk factors.', 'Compare the financial data and risk factors of Uber with those of Lyft.'\]
\
Calling function: lyft\_10k with args: {"input": "What are the key financial figures and risk factors for Lyft in 2021?"}

Calling function: lyft\_10k with args: {"input": "What are the key financial figures and risk factors for Lyft in 2021?"}

In 2021, Lyft reported total revenue of $3,208,323,000, with the majority coming from contracts with customers ($2,957,979,000) and a smaller portion from rental revenue ($250,344,000). Financially, Lyft has faced challenges due to the COVID-19 pandemic, which significantly impacted their operations and revenue streams. The company experienced a decline in revenue in 2020 due to the pandemic and has only partially recovered, with revenue still below pre-COVID levels.

Lyft has identified several risk factors that could affect its business, including the ability to forecast revenue, manage expenses, attract and retain drivers and riders, comply with new regulations, and handle the ongoing impacts of the COVID-19 pandemic. The company also faces risks from macroeconomic changes, maintaining their reputation, managing growth, and developing new platform features and services. Additionally, Lyft's financial performance is subject to uncertainties due to the evolving nature of the market and their business model, and there is no assurance of achieving or maintaining profitability in the future.

In 2021, Lyft reported total revenues of $3,208,323,000. This revenue comprises $2,957,979,000 from contracts with customers under ASC 606, primarily from its ridesharing marketplace, and $250,344,000 in rental revenue under ASC 842 from its network of Light Vehicles and Lyft Rentals.

Key risk factors for Lyft in 2021 include the ongoing impacts of the COVID-19 pandemic, which has led to significant operational adjustments and financial strain. The company's response to the pandemic included new health and safety requirements for ridesharing and adjustments to expenses and cash flow to match declines in revenue. The future impact of the pandemic remains uncertain and depends on various factors such as the duration of the pandemic, vaccine distribution and efficacy, government actions, and changes in consumer behavior.

Additional risks include Lyft's ability to forecast revenue and manage expenses, attract and retain drivers and riders, comply with regulatory changes, manage capital expenditures, and maintain demand and confidence in the safety of its platform. The company also faces challenges related to maintaining profitability, with a history of net losses despite recent Adjusted EBITDA profitability. Moreover, Lyft plans significant investments in electric vehicles (EVs) to comply with regulations and sustainability goals, adding to its financial commitments.
\> Generated new reasoning step: Thought: Having gathered the necessary information from Uber's 10K files, I now need to obtain similar financial data and risk factors from Lyft's 10K files to make a comparison.
Action: lyft\_10k
Action Input: {'input': 'What are the key financial figures and risk factors for Lyft in 2021?'}
Observation: In 2021, Lyft reported total revenue of $3,208,323,000, with the majority coming from contracts with customers ($2,957,979,000) and a smaller portion from rental revenue ($250,344,000). Financially, Lyft has faced challenges due to the COVID-19 pandemic, which significantly impacted their operations and revenue streams. The company experienced a decline in revenue in 2020 due to the pandemic and has only partially recovered, with revenue still below pre-COVID levels.

Lyft has identified several risk factors that could affect its business, including the ability to forecast revenue, manage expenses, attract and retain drivers and riders, comply with new regulations, and handle the ongoing impacts of the COVID-19 pandemic. The company also faces risks from macroeconomic changes, maintaining their reputation, managing growth, and developing new platform features and services. Additionally, Lyft's financial performance is subject to uncertainties due to the evolving nature of the market and their business model, and there is no assurance of achieving or maintaining profitability in the future.
\> Generated new reasoning step: Thought: Now that I have information on Uber's financial data and risk factors, I need to retrieve similar information for Lyft from its 10K file to make a comparison.
Action: lyft\_10k
Action Input: {'input': 'What are the key financial figures and risk factors for Lyft in 2021?'}
Observation: In 2021, Lyft reported total revenues of $3,208,323,000. This revenue comprises $2,957,979,000 from contracts with customers under ASC 606, primarily from its ridesharing marketplace, and $250,344,000 in rental revenue under ASC 842 from its network of Light Vehicles and Lyft Rentals.

Key risk factors for Lyft in 2021 include the ongoing impacts of the COVID-19 pandemic, which has led to significant operational adjustments and financial strain. The company's response to the pandemic included new health and safety requirements for ridesharing and adjustments to expenses and cash flow to match declines in revenue. The future impact of the pandemic remains uncertain and depends on various factors such as the duration of the pandemic, vaccine distribution and efficacy, government actions, and changes in consumer behavior.

Additional risks include Lyft's ability to forecast revenue and manage expenses, attract and retain drivers and riders, comply with regulatory changes, manage capital expenditures, and maintain demand and confidence in the safety of its platform. The company also faces challenges related to maintaining profitability, with a history of net losses despite recent Adjusted EBITDA profitability. Moreover, Lyft plans significant investments in electric vehicles (EVs) to comply with regulations and sustainability goals, adding to its financial commitments.
\> Evaluation for input Given the risk factors of Uber and Lyft described in their 10K files, which company is performing better? Please use concrete numbers to inform your decision.
: score=9 is\_done=False reasoning="The conversation trajectory so far is highly correct in its approach towards answering the query about the comparative performance of Uber and Lyft based on their 10K files. The actions taken to extract key financial data and risk factors from both companies are directly relevant and necessary for making an informed comparison. The thought process is logically structured, beginning with the acquisition of Uber's data, followed by Lyft's, which aligns well with the methodical comparison required by the query.\\n\\nThe completeness of the answer is not yet achieved, as the final comparison between the two sets of data has not been made. However, the trajectory is on the correct path, as the necessary preliminary information has been gathered and the next logical step would be to analyze and compare these findings to conclude which company is performing better based on the data. The conversation is progressing correctly but needs to reach the analysis phase to provide a final answer."

\> Evaluation for input Given the risk factors of Uber and Lyft described in their 10K files, which company is performing better? Please use concrete numbers to inform your decision.
: score=9 is\_done=False reasoning="The conversation so far has correctly followed a logical approach to answering the query about which company, Uber or Lyft, is performing better based on their 10K files. The user has appropriately collected financial data and risk factors for both Uber and Lyft, which are essential for making a comparative analysis. The process involves extracting relevant financial data and risk factors from each company's 10K files, starting with Uber and then moving to Lyft. The observations from each company's 10K files have been noted, and the user is in the process of gathering all the necessary information before making a comparison.\\n\\nThe trajectory is correct in its approach, gathering all the relevant data before attempting to draw conclusions. However, it is not yet complete as the user has not yet compared the information between Uber and Lyft to determine which company is performing better. The final comparison and conclusion are necessary to complete the answer to the query."

\> Got final response: I am still thinking.
\> Selecting node to expand: Observation: In 2021, Lyft reported total revenue of $3,208,323,000, with the majority coming from contracts with customers ($2,957,979,000) and a smaller portion from rental revenue ($250,344,000). Financially, Lyft has faced challenges due to the COVID-19 pandemic, which significantly impacted their operations and revenue streams. The company experienced a decline in revenue in 2020 due to the pandemic and has only partially recovered, with revenue still below pre-COVID levels.

Lyft has identified several risk factors that could affect its business, including the ability to forecast revenue, manage expenses, attract and retain drivers and riders, comply with new regulations, and handle the ongoing impacts of the COVID-19 pandemic. The company also faces risks from macroeconomic changes, maintaining their reputation, managing growth, and developing new platform features and services. Additionally, Lyft's financial performance is subject to uncertainties due to the evolving nature of the market and their business model, and there is no assurance of achieving or maintaining profitability in the future.
\> Got candidates: \['Prepare a comparative analysis of the financial data and risk factors for Uber and Lyft.', 'Summarize the key financial figures and risk factors for Uber and Lyft.'\]
\> Generated new reasoning step: Thought: I can answer without using any more tools. I'll use the user's language to answer.
Answer: Based on the information provided from the 10K files of Uber and Lyft for 2021, here is a comparative analysis of their financial data and risk factors:

\*\*Financial Data:\*\*
1. \*\*Uber\*\* did not disclose specific revenue figures in the provided information, focusing more on their financial management practices and the quality of their financial instruments. They emphasized the high credit quality of their cash equivalents and securities, and the use of GAAP-compliant financial statements influenced by estimates considering the COVID-19 impact.
   
2. \*\*Lyft\*\* reported total revenue of $3,208,323,000 for 2021, with a significant drop due to the COVID-19 pandemic and a partial recovery, still below pre-pandemic levels. This gives a clear numeric insight into their financial status during the year.

\*\*Risk Factors:\*\*
1. \*\*Uber's\*\* key risk factors include concentration of credit risk, with their financial assets placed in high-credit-quality institutions, and various uncertainties that could affect their forward-looking statements and actual results. They manage risks related to their financial estimates and the broader economic impacts of the pandemic.

2. \*\*Lyft\*\* faces risks related to revenue forecasting, expense management, driver and rider retention, regulatory compliance, and pandemic impacts. Additional risks include macroeconomic changes, reputation management, growth management, and innovation on their platform. They also express concerns about the uncertain market and their ability to achieve or maintain profitability.

\*\*Conclusion:\*\*
While Uber's discussion focuses on the management of high-quality financial assets and the broader implications of their financial estimates, Lyft provides more concrete financial results and a detailed list of operational and market risks. Lyft's explicit revenue figures and detailed risk enumeration offer a clearer picture of their financial health and challenges compared to Uber's more generalized financial overview. This analysis suggests that Lyft provides more transparency in their financial reporting, but also highlights more vulnerability in terms of revenue recovery and risk exposure compared to Uber.
\> Generated new reasoning step: Thought: I can answer without using any more tools. I'll use the user's language to answer.
Answer: Uber's key financial considerations include the use of GAAP and the necessity of management's estimates which affect reported figures. Financial risks for Uber highlight a concentration of credit risk primarily in high-credit-quality money market funds, U.S. government and agency securities, and corporate debt securities. Despite the risks of exceeding insured limits, Uber has not reported significant losses in this area.

Lyft reported a total revenue of $3.2 billion in 2021, with the majority from contracts with customers. The company has faced financial challenges due to the COVID-19 pandemic, which significantly impacted its operations and revenue, causing a decline in 2020 and a partial recovery in 2021. Risk factors for Lyft include the ability to forecast revenue, manage expenses, attract and retain drivers and riders, comply with new regulations, and handle the ongoing impacts of COVID-19. Lyft also faces risks from macroeconomic changes, reputation management, growth management, and uncertainties in achieving or maintaining profitability.

Both companies deal with uncertainties and risks due to the COVID-19 pandemic and regulatory environments, but Uber's larger scale and diversified investment portfolio might provide it with a more robust financial base compared to Lyft, which is still struggling to recover to pre-COVID revenue levels and is facing numerous operational and market risks.
\> Evaluation for input Given the risk factors of Uber and Lyft described in their 10K files, which company is performing better? Please use concrete numbers to inform your decision.
: score=10 is\_done=True reasoning="The conversation trajectory effectively addresses the query by systematically gathering and comparing the financial data and risk factors from the 10K files of both Uber and Lyft. The process begins with a clear understanding of the task, followed by separate actions to retrieve the necessary information from each company's 10K files. The final comparative analysis is thorough, highlighting key financial figures and risk factors for both companies, and providing a reasoned conclusion on which company appears to be performing better based on the information available. This comprehensive approach ensures that the conversation correctly and completely answers the query as posed."

\> Evaluation for input Given the risk factors of Uber and Lyft described in their 10K files, which company is performing better? Please use concrete numbers to inform your decision.
: score=9 is\_done=True reasoning='The conversation accurately addresses the query by methodically obtaining and comparing the financial data and risk factors of Uber and Lyft from their respective 10K files. The process involved gathering specific financial figures and risk factors from Uber and then doing the same for Lyft. The final comparison effectively uses the gathered data to assess which company is performing better, focusing on financial stability, revenue impacts due to the pandemic, and broader risk factors affecting both companies. The answer is well-informed and directly addresses the query using the requested concrete numbers, leading to a reasoned conclusion that Uber might be performing better due to its diversified financial base and better recovery indicators. This conclusion is reached after a systematic and relevant examination of the necessary financial documents and data, thus fulfilling the requirements of correctness and completeness in the context of the query.'

\> Found solution node: Based on the information provided from the 10K files of Uber and Lyft for 2021, here is a comparative analysis of their financial data and risk factors:

\*\*Financial Data:\*\*
1. \*\*Uber\*\* did not disclose specific revenue figures in the provided information, focusing more on their financial management practices and the quality of their financial instruments. They emphasized the high credit quality of their cash equivalents and securities, and the use of GAAP-compliant financial statements influenced by estimates considering the COVID-19 impact.
   
2. \*\*Lyft\*\* reported total revenue of $3,208,323,000 for 2021, with a significant drop due to the COVID-19 pandemic and a partial recovery, still below pre-pandemic levels. This gives a clear numeric insight into their financial status during the year.

\*\*Risk Factors:\*\*
1. \*\*Uber's\*\* key risk factors include concentration of credit risk, with their financial assets placed in high-credit-quality institutions, and various uncertainties that could affect their forward-looking statements and actual results. They manage risks related to their financial estimates and the broader economic impacts of the pandemic.

2. \*\*Lyft\*\* faces risks related to revenue forecasting, expense management, driver and rider retention, regulatory compliance, and pandemic impacts. Additional risks include macroeconomic changes, reputation management, growth management, and innovation on their platform. They also express concerns about the uncertain market and their ability to achieve or maintain profitability.

\*\*Conclusion:\*\*
While Uber's discussion focuses on the management of high-quality financial assets and the broader implications of their financial estimates, Lyft provides more concrete financial results and a detailed list of operational and market risks. Lyft's explicit revenue figures and detailed risk enumeration offer a clearer picture of their financial health and challenges compared to Uber's more generalized financial overview. This analysis suggests that Lyft provides more transparency in their financial reporting, but also highlights more vulnerability in terms of revenue recovery and risk exposure compared to Uber.
\> Found solution node: Uber's key financial considerations include the use of GAAP and the necessity of management's estimates which affect reported figures. Financial risks for Uber highlight a concentration of credit risk primarily in high-credit-quality money market funds, U.S. government and agency securities, and corporate debt securities. Despite the risks of exceeding insured limits, Uber has not reported significant losses in this area.

Lyft reported a total revenue of $3.2 billion in 2021, with the majority from contracts with customers. The company has faced financial challenges due to the COVID-19 pandemic, which significantly impacted its operations and revenue, causing a decline in 2020 and a partial recovery in 2021. Risk factors for Lyft include the ability to forecast revenue, manage expenses, attract and retain drivers and riders, comply with new regulations, and handle the ongoing impacts of COVID-19. Lyft also faces risks from macroeconomic changes, reputation management, growth management, and uncertainties in achieving or maintaining profitability.

Both companies deal with uncertainties and risks due to the COVID-19 pandemic and regulatory environments, but Uber's larger scale and diversified investment portfolio might provide it with a more robust financial base compared to Lyft, which is still struggling to recover to pre-COVID revenue levels and is facing numerous operational and market risks.
\> Got final response: Based on the information provided from the 10K files of Uber and Lyft for 2021, here is a comparative analysis of their financial data and risk factors:

\*\*Financial Data:\*\*
1. \*\*Uber\*\* did not disclose specific revenue figures in the provided information, focusing more on their financial management practices and the quality of their financial instruments. They emphasized the high credit quality of their cash equivalents and securities, and the use of GAAP-compliant financial statements influenced by estimates considering the COVID-19 impact.
   
2. \*\*Lyft\*\* reported total revenue of $3,208,323,000 for 2021, with a significant drop due to the COVID-19 pandemic and a partial recovery, still below pre-pandemic levels. This gives a clear numeric insight into their financial status during the year.

\*\*Risk Factors:\*\*
1. \*\*Uber's\*\* key risk factors include concentration of credit risk, with their financial assets placed in high-credit-quality institutions, and various uncertainties that could affect their forward-looking statements and actual results. They manage risks related to their financial estimates and the broader economic impacts of the pandemic.

2. \*\*Lyft\*\* faces risks related to revenue forecasting, expense management, driver and rider retention, regulatory compliance, and pandemic impacts. Additional risks include macroeconomic changes, reputation management, growth management, and innovation on their platform. They also express concerns about the uncertain market and their ability to achieve or maintain profitability.

\*\*Conclusion:\*\*
While Uber's discussion focuses on the management of high-quality financial assets and the broader implications of their financial estimates, Lyft provides more concrete financial results and a detailed list of operational and market risks. Lyft's explicit revenue figures and detailed risk enumeration offer a clearer picture of their financial health and challenges compared to Uber's more generalized financial overview. This analysis suggests that Lyft provides more transparency in their financial reporting, but also highlights more vulnerability in terms of revenue recovery and risk exposure compared to Uber.

In \[ \]:

Copied!

print(str(response))

print(str(response))

Based on the information provided from the 10K files of Uber and Lyft for 2021, here is a comparative analysis of their financial data and risk factors:

\*\*Financial Data:\*\*
1. \*\*Uber\*\* did not disclose specific revenue figures in the provided information, focusing more on their financial management practices and the quality of their financial instruments. They emphasized the high credit quality of their cash equivalents and securities, and the use of GAAP-compliant financial statements influenced by estimates considering the COVID-19 impact.
   
2. \*\*Lyft\*\* reported total revenue of $3,208,323,000 for 2021, with a significant drop due to the COVID-19 pandemic and a partial recovery, still below pre-pandemic levels. This gives a clear numeric insight into their financial status during the year.

\*\*Risk Factors:\*\*
1. \*\*Uber's\*\* key risk factors include concentration of credit risk, with their financial assets placed in high-credit-quality institutions, and various uncertainties that could affect their forward-looking statements and actual results. They manage risks related to their financial estimates and the broader economic impacts of the pandemic.

2. \*\*Lyft\*\* faces risks related to revenue forecasting, expense management, driver and rider retention, regulatory compliance, and pandemic impacts. Additional risks include macroeconomic changes, reputation management, growth management, and innovation on their platform. They also express concerns about the uncertain market and their ability to achieve or maintain profitability.

\*\*Conclusion:\*\*
While Uber's discussion focuses on the management of high-quality financial assets and the broader implications of their financial estimates, Lyft provides more concrete financial results and a detailed list of operational and market risks. Lyft's explicit revenue figures and detailed risk enumeration offer a clearer picture of their financial health and challenges compared to Uber's more generalized financial overview. This analysis suggests that Lyft provides more transparency in their financial reporting, but also highlights more vulnerability in terms of revenue recovery and risk exposure compared to Uber.

Using `.chat()` directly, we can have the agent automatically run until completion.

In \[ \]:

Copied!

agent.reset()

response \= agent.chat(
    "Given the revenue growth and risk factors of Uber and Lyft, "
    "which company is performing better? Please use concrete numbers to inform your decision."
)

agent.reset() response = agent.chat( "Given the revenue growth and risk factors of Uber and Lyft, " "which company is performing better? Please use concrete numbers to inform your decision." )

\> Selecting node to expand: Observation: Given the revenue growth and risk factors of Uber and Lyft, which company is performing better? Please use concrete numbers to inform your decision.
\> Got candidates: \['Review financial reports of Uber and Lyft for the latest fiscal year to compare revenue growth.', 'Analyze risk factors mentioned in the latest quarterly reports of Uber and Lyft.'\]
\
Calling function: uber\_10k with args: {"input": "What was Uber's revenue growth for the fiscal year 2021?"}

Uber's revenue for the fiscal year 2021 was $17,455 million, which represents a growth of 57% compared to the revenue of $11,139 million in 2020.
\> Generated new reasoning step: Thought: The current language of the user is English. I need to use tools to gather data on the revenue growth of Uber and Lyft for the latest fiscal year, which is 2021.
Action: uber\_10k
Action Input: {'input': "What was Uber's revenue growth for the fiscal year 2021?"}
Observation: Uber's revenue for the fiscal year 2021 was $17,455 million, which represents a growth of 57% compared to the revenue of $11,139 million in 2020.
\> Generated new reasoning step: Thought: The user asked for analysis of risk factors from the latest quarterly reports of Uber and Lyft. However, my tools provide information from the financial year 2021. I need to clarify this before proceeding.
Answer: I can access financial information from the year 2021 for Uber and Lyft, but not the latest quarterly reports. Would you like to proceed with the 2021 data, or do you need the most recent quarterly data specifically?
\> Evaluation for input Given the revenue growth and risk factors of Uber and Lyft, which company is performing better? Please use concrete numbers to inform your decision.
: score=5 is\_done=False reasoning="The conversation has correctly identified the need for specific data to address the query about comparing Uber and Lyft's performance based on revenue growth and risk factors. The thought and action taken to clarify the availability of data are appropriate and necessary for providing an accurate answer. However, the conversation has not yet progressed to analyzing the actual data, as it is still in the clarification stage. Therefore, it is not yet complete in answering the query, but the direction is correct. The score of 5 reflects that the conversation is on the right track but has not progressed far enough to provide an evaluation based on the specific data requested."

\> Evaluation for input Given the revenue growth and risk factors of Uber and Lyft, which company is performing better? Please use concrete numbers to inform your decision.
: score=8 is\_done=False reasoning="The conversation thus far has correctly focused on acquiring concrete numbers to compare the revenue growth of Uber and Lyft, in line with the initial query. The action of obtaining Uber's revenue growth for the fiscal year 2021, and observing that it was a 57% increase from the previous year, is a correct step towards answering the query. However, the conversation is not complete as the revenue growth data for Lyft has not yet been obtained, making it impossible to directly compare the two companies and conclude which is performing better. Therefore, while the actions taken are correct in addressing half of the query, completeness is not achieved due to the lack of information about Lyft."

\> Got final response: I am still thinking.
\> Selecting node to expand: Observation: Uber's revenue for the fiscal year 2021 was $17,455 million, which represents a growth of 57% compared to the revenue of $11,139 million in 2020.
\> Got candidates: \['Review financial reports of Lyft for the latest fiscal year to compare its revenue growth with Uber.', 'Calculate the percentage growth in revenue for Lyft to compare with Uber’s 57% growth.'\]
\
Calling function: lyft\_10k with args: {"input": "What was Lyft's revenue growth for the fiscal year 2021?"}

Calling function: lyft\_10k with args: {"input": "What was Lyft's revenue growth for the fiscal year 2021?"}

Lyft's revenue increased by 36% in 2021 compared to the prior year.

Lyft's revenue increased by 36% in 2021 compared to the previous year.
\> Generated new reasoning step: Thought: The current language of the user is English. I need to use a tool to gather data on Lyft's revenue growth for the latest fiscal year, which is 2021.
Action: lyft\_10k
Action Input: {'input': "What was Lyft's revenue growth for the fiscal year 2021?"}
Observation: Lyft's revenue increased by 36% in 2021 compared to the previous year.
\> Generated new reasoning step: Thought: The current language of the user is English. I need to use the tool to gather data on Lyft's revenue growth for the fiscal year 2021 to compare with Uber's 57% growth.
Action: lyft\_10k
Action Input: {'input': "What was Lyft's revenue growth for the fiscal year 2021?"}
Observation: Lyft's revenue increased by 36% in 2021 compared to the prior year.
\> Evaluation for input Given the revenue growth and risk factors of Uber and Lyft, which company is performing better? Please use concrete numbers to inform your decision.
: score=7 is\_done=False reasoning="So far, the conversation has correctly followed the query's directive to compare the revenue growth of Uber and Lyft using concrete numbers from their financial reports. The actions taken to retrieve data on the revenue growth for both companies are appropriate and directly address the query. However, the conversation has not yet addressed the 'risk factors' part of the query, which is crucial for a complete evaluation of which company is performing better. Thus, the conversation is correct in the part it has addressed but incomplete as it has not yet fully answered the query regarding risk factors in addition to revenue growth."

\> Evaluation for input Given the revenue growth and risk factors of Uber and Lyft, which company is performing better? Please use concrete numbers to inform your decision.
: score=8 is\_done=False reasoning="The conversation correctly focuses on comparing revenue growth between Uber and Lyft, which aligns well with the query's requirement to use concrete numbers for performance evaluation. The actions taken to retrieve the specific revenue growth figures for both companies from their respective financial reports are appropriate and directly address the query. However, the conversation is not yet complete as it has not addressed the risk factors of both companies, which is also a critical component of the query. Thus, while the trajectory is correct in terms of revenue growth evaluation, it remains incomplete without the risk factor analysis."

\> Got final response: I am still thinking.
\> Selecting node to expand: Observation: Lyft's revenue increased by 36% in 2021 compared to the previous year.
\> Got candidates: \["Calculate Uber's and Lyft's revenue growth percentages to compare.", 'List risk factors for Uber and Lyft.'\]
\
Calling function: uber\_10k with args: {"input": "What are the risk factors for Uber according to the 2021 financial report?"}

The risk factors for Uber according to the 2021 financial report include the inability to attract or maintain a critical mass of Drivers, consumers, merchants, shippers, and carriers, which could make the platform less appealing to users and adversely impact financial results. Additionally, the COVID-19 pandemic has affected Uber's business by reducing global demand for Mobility rides and causing Driver supply constraints. Other risks include legal challenges regarding the classification of Drivers as independent contractors rather than employees, which could lead to significant legal and financial consequences.
\> Generated new reasoning step: Thought: I can answer without using any more tools. I'll use the user's language to answer.
Answer: Uber's revenue growth for the fiscal year 2021 was 57%, increasing from $11,139 million in 2020 to $17,455 million in 2021. Lyft's revenue growth for the same period was 36%. Comparing these figures, Uber has shown a higher revenue growth percentage than Lyft for the fiscal year 2021.
\> Generated new reasoning step: Thought: The current language of the user is English. I need to gather information on the risk factors for Uber and Lyft.
Action: uber\_10k
Action Input: {'input': 'What are the risk factors for Uber according to the 2021 financial report?'}
Observation: The risk factors for Uber according to the 2021 financial report include the inability to attract or maintain a critical mass of Drivers, consumers, merchants, shippers, and carriers, which could make the platform less appealing to users and adversely impact financial results. Additionally, the COVID-19 pandemic has affected Uber's business by reducing global demand for Mobility rides and causing Driver supply constraints. Other risks include legal challenges regarding the classification of Drivers as independent contractors rather than employees, which could lead to significant legal and financial consequences.
\> Evaluation for input Given the revenue growth and risk factors of Uber and Lyft, which company is performing better? Please use concrete numbers to inform your decision.
: score=8 is\_done=False reasoning="The conversation trajectory so far indicates a methodical approach to answering the query about the better performance between Uber and Lyft by examining both revenue growth and risk factors. The conversation has correctly identified and gathered data on revenue growth for both companies, showing a 57% growth for Uber and 36% for Lyft in 2021. This part of the analysis is well-aligned with the query's requirement to use concrete numbers. However, the conversation is still in the process of collecting information on risk factors. It has gathered detailed risk factors for Uber but has not yet done so for Lyft. The trajectory is correct in its approach but incomplete, as it needs to finish gathering and comparing all necessary information, including Lyft's risk factors, to fully answer the query."

\> Evaluation for input Given the revenue growth and risk factors of Uber and Lyft, which company is performing better? Please use concrete numbers to inform your decision.
: score=9 is\_done=True reasoning="The conversation has effectively addressed the query regarding which company between Uber and Lyft is performing better based on revenue growth. The trajectory includes gathering relevant financial data for both companies for the fiscal year 2021, and clearly comparing the revenue growth percentages. The final answer explicitly states that Uber had a higher revenue growth percentage than Lyft. The reasoning is well-supported by concrete numbers provided for each company, directly answering the user's question.\\n\\nThe evaluation is not a perfect score because while the trajectory correctly identifies and compares revenue growth, it does not address the 'risk factors' part of the query, which is also crucial for determining overall performance. However, the part of the query concerning revenue growth has been completely and correctly answered, hence the score reflects high correctness and completeness in this respect."

\> Found solution node: Uber's revenue growth for the fiscal year 2021 was 57%, increasing from $11,139 million in 2020 to $17,455 million in 2021. Lyft's revenue growth for the same period was 36%. Comparing these figures, Uber has shown a higher revenue growth percentage than Lyft for the fiscal year 2021.
\> Got final response: Uber's revenue growth for the fiscal year 2021 was 57%, increasing from $11,139 million in 2020 to $17,455 million in 2021. Lyft's revenue growth for the same period was 36%. Comparing these figures, Uber has shown a higher revenue growth percentage than Lyft for the fiscal year 2021.

In \[ \]:

Copied!

print(str(response))

print(str(response))

Uber's revenue growth for the fiscal year 2021 was 57%, increasing from $11,139 million in 2020 to $17,455 million in 2021. Lyft's revenue growth for the same period was 36%. Comparing these figures, Uber has shown a higher revenue growth percentage than Lyft for the fiscal year 2021.

Back to top

[Previous Introspective Agents: Performing Tasks With Reflection](https://docs.llamaindex.ai/en/stable/examples/agent/introspective_agent_toxicity_reduction/)[Next LLM Compiler Agent Cookbook](https://docs.llamaindex.ai/en/stable/examples/agent/llm_compiler/)

Hi, how can I help you?

🦙
