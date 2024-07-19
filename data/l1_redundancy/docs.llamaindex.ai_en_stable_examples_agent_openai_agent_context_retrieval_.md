Title: Context-Augmented OpenAI Agent - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_context_retrieval/

Markdown Content:
Context-Augmented OpenAI Agent - LlamaIndex


In this tutorial, we show you how to use our `ContextRetrieverOpenAIAgent` implementation to build an agent on top of OpenAI's function API and store/index an arbitrary number of tools. Our indexing/retrieval modules help to remove the complexity of having too many functions to fit in the prompt.

Initial Setup[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_context_retrieval/#initial-setup)
-------------------------------------------------------------------------------------------------------------------

Here we setup a ContextRetrieverOpenAIAgent. This agent will perform retrieval first before calling any tools. This can help ground the agent's tool picking and answering capabilities in context.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-agent\-openai\-legacy

%pip install llama-index-agent-openai-legacy

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import json
from typing import Sequence

from llama\_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
    load\_index\_from\_storage,
)
from llama\_index.core.tools import QueryEngineTool, ToolMetadata

import json from typing import Sequence from llama\_index.core import ( SimpleDirectoryReader, VectorStoreIndex, StorageContext, load\_index\_from\_storage, ) from llama\_index.core.tools import QueryEngineTool, ToolMetadata

In \[ \]:

Copied!

try:
    storage\_context \= StorageContext.from\_defaults(
        persist\_dir\="./storage/march"
    )
    march\_index \= load\_index\_from\_storage(storage\_context)

    storage\_context \= StorageContext.from\_defaults(
        persist\_dir\="./storage/june"
    )
    june\_index \= load\_index\_from\_storage(storage\_context)

    storage\_context \= StorageContext.from\_defaults(
        persist\_dir\="./storage/sept"
    )
    sept\_index \= load\_index\_from\_storage(storage\_context)

    index\_loaded \= True
except:
    index\_loaded \= False

try: storage\_context = StorageContext.from\_defaults( persist\_dir="./storage/march" ) march\_index = load\_index\_from\_storage(storage\_context) storage\_context = StorageContext.from\_defaults( persist\_dir="./storage/june" ) june\_index = load\_index\_from\_storage(storage\_context) storage\_context = StorageContext.from\_defaults( persist\_dir="./storage/sept" ) sept\_index = load\_index\_from\_storage(storage\_context) index\_loaded = True except: index\_loaded = False

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/10q/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10q/uber\_10q\_march\_2022.pdf' \-O 'data/10q/uber\_10q\_march\_2022.pdf'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10q/uber\_10q\_june\_2022.pdf' \-O 'data/10q/uber\_10q\_june\_2022.pdf'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10q/uber\_10q\_sept\_2022.pdf' \-O 'data/10q/uber\_10q\_sept\_2022.pdf'

!mkdir -p 'data/10q/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10q/uber\_10q\_march\_2022.pdf' -O 'data/10q/uber\_10q\_march\_2022.pdf' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10q/uber\_10q\_june\_2022.pdf' -O 'data/10q/uber\_10q\_june\_2022.pdf' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10q/uber\_10q\_sept\_2022.pdf' -O 'data/10q/uber\_10q\_sept\_2022.pdf'

In \[ \]:

Copied!

\# build indexes across the three data sources

if not index\_loaded:
    \# load data
    march\_docs \= SimpleDirectoryReader(
        input\_files\=\["./data/10q/uber\_10q\_march\_2022.pdf"\]
    ).load\_data()
    june\_docs \= SimpleDirectoryReader(
        input\_files\=\["./data/10q/uber\_10q\_june\_2022.pdf"\]
    ).load\_data()
    sept\_docs \= SimpleDirectoryReader(
        input\_files\=\["./data/10q/uber\_10q\_sept\_2022.pdf"\]
    ).load\_data()

    \# build index
    march\_index \= VectorStoreIndex.from\_documents(march\_docs)
    june\_index \= VectorStoreIndex.from\_documents(june\_docs)
    sept\_index \= VectorStoreIndex.from\_documents(sept\_docs)

    \# persist index
    march\_index.storage\_context.persist(persist\_dir\="./storage/march")
    june\_index.storage\_context.persist(persist\_dir\="./storage/june")
    sept\_index.storage\_context.persist(persist\_dir\="./storage/sept")

\# build indexes across the three data sources if not index\_loaded: # load data march\_docs = SimpleDirectoryReader( input\_files=\["./data/10q/uber\_10q\_march\_2022.pdf"\] ).load\_data() june\_docs = SimpleDirectoryReader( input\_files=\["./data/10q/uber\_10q\_june\_2022.pdf"\] ).load\_data() sept\_docs = SimpleDirectoryReader( input\_files=\["./data/10q/uber\_10q\_sept\_2022.pdf"\] ).load\_data() # build index march\_index = VectorStoreIndex.from\_documents(march\_docs) june\_index = VectorStoreIndex.from\_documents(june\_docs) sept\_index = VectorStoreIndex.from\_documents(sept\_docs) # persist index march\_index.storage\_context.persist(persist\_dir="./storage/march") june\_index.storage\_context.persist(persist\_dir="./storage/june") sept\_index.storage\_context.persist(persist\_dir="./storage/sept")

In \[ \]:

Copied!

march\_engine \= march\_index.as\_query\_engine(similarity\_top\_k\=3)
june\_engine \= june\_index.as\_query\_engine(similarity\_top\_k\=3)
sept\_engine \= sept\_index.as\_query\_engine(similarity\_top\_k\=3)

march\_engine = march\_index.as\_query\_engine(similarity\_top\_k=3) june\_engine = june\_index.as\_query\_engine(similarity\_top\_k=3) sept\_engine = sept\_index.as\_query\_engine(similarity\_top\_k=3)

In \[ \]:

Copied!

query\_engine\_tools \= \[
    QueryEngineTool(
        query\_engine\=march\_engine,
        metadata\=ToolMetadata(
            name\="uber\_march\_10q",
            description\=(
                "Provides information about Uber 10Q filings for March 2022. "
                "Use a detailed plain text question as input to the tool."
            ),
        ),
    ),
    QueryEngineTool(
        query\_engine\=june\_engine,
        metadata\=ToolMetadata(
            name\="uber\_june\_10q",
            description\=(
                "Provides information about Uber financials for June 2021. "
                "Use a detailed plain text question as input to the tool."
            ),
        ),
    ),
    QueryEngineTool(
        query\_engine\=sept\_engine,
        metadata\=ToolMetadata(
            name\="uber\_sept\_10q",
            description\=(
                "Provides information about Uber financials for Sept 2021. "
                "Use a detailed plain text question as input to the tool."
            ),
        ),
    ),
\]

query\_engine\_tools = \[ QueryEngineTool( query\_engine=march\_engine, metadata=ToolMetadata( name="uber\_march\_10q", description=( "Provides information about Uber 10Q filings for March 2022. " "Use a detailed plain text question as input to the tool." ), ), ), QueryEngineTool( query\_engine=june\_engine, metadata=ToolMetadata( name="uber\_june\_10q", description=( "Provides information about Uber financials for June 2021. " "Use a detailed plain text question as input to the tool." ), ), ), QueryEngineTool( query\_engine=sept\_engine, metadata=ToolMetadata( name="uber\_sept\_10q", description=( "Provides information about Uber financials for Sept 2021. " "Use a detailed plain text question as input to the tool." ), ), ), \]

### Try Context-Augmented Agent[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_context_retrieval/#try-context-augmented-agent)

Here we augment our agent with context in different settings:

*   toy context: we define some abbreviations that map to financial terms (e.g. R=Revenue). We supply this as context to the agent

In \[ \]:

Copied!

from llama\_index.core import Document
from llama\_index.agent.openai\_legacy import ContextRetrieverOpenAIAgent

from llama\_index.core import Document from llama\_index.agent.openai\_legacy import ContextRetrieverOpenAIAgent

In \[ \]:

Copied!

\# toy index - stores a list of abbreviations
texts \= \[
    "Abbreviation: X = Revenue",
    "Abbreviation: YZ = Risk Factors",
    "Abbreviation: Z = Costs",
\]
docs \= \[Document(text\=t) for t in texts\]
context\_index \= VectorStoreIndex.from\_documents(docs)

\# toy index - stores a list of abbreviations texts = \[ "Abbreviation: X = Revenue", "Abbreviation: YZ = Risk Factors", "Abbreviation: Z = Costs", \] docs = \[Document(text=t) for t in texts\] context\_index = VectorStoreIndex.from\_documents(docs)

In \[ \]:

Copied!

context\_agent \= ContextRetrieverOpenAIAgent.from\_tools\_and\_retriever(
    query\_engine\_tools,
    context\_index.as\_retriever(similarity\_top\_k\=1),
    verbose\=True,
)

context\_agent = ContextRetrieverOpenAIAgent.from\_tools\_and\_retriever( query\_engine\_tools, context\_index.as\_retriever(similarity\_top\_k=1), verbose=True, )

In \[ \]:

Copied!

response \= context\_agent.chat("What is the YZ of March 2022?")

response = context\_agent.chat("What is the YZ of March 2022?")

Context information is below.
---------------------
Abbreviation: YZ = Risk Factors
---------------------
Given the context information and not prior knowledge, either pick the corresponding tool or answer the function: What is the YZ of March 2022?

\
Calling function: uber\_march\_10q with args: {
  "input": "Risk Factors"
}
Got output: 
•The COVID-19 pandemic and the impact of actions to mitigate the pandemic have adversely affected and may continue to adversely affect parts of our business.
•Our business would be adversely affected if Drivers were classified as employees, workers or quasi-employees instead of independent contractors.
•The mobility, delivery, and logistics industries are highly competitive, with well-established and low-cost alternatives that have been available for decades, low barriers to entry, low switching costs, and well-capitalized competitors in nearly every major geographic region.
•To remain competitive in certain markets, we have in the past lowered, and may continue to lower, fares or service fees, and we have in the past offered, and may continue to offer, significant Driver incentives and consumer discounts and promotions.
•We have incurred significant losses since inception, including in the United States and other major markets. We expect our operating expenses to increase significantly in the foreseeable future, and we may not achieve or maintain profitability.
•If we are unable to attract or maintain a critical mass of Drivers, consumers, merchants, shippers, and carriers, whether as a result of competition or other factors, our platform will become less appealing to platform users.
•Maintaining and enhancing our brand and reputation is critical to our business prospects. We have previously received significant media coverage and negative publicity regarding our brand and reputation, and while we have taken significant steps to rehabilitate our brand and reputation, failure to maintain and enhance our brand and reputation could adversely affect our business.
•The impact of economic conditions, including the resulting effect on discretionary consumer spending, may harm our business and operating results.
•Increases in fuel, food, labor, energy, and other costs due to inflation and other factors could adversely affect our operating results.
•If we experience security or privacy breaches or other unauthorized or improper access to, use of, disclosure of, alteration of or destruction of our proprietary or confidential data, employee data, or platform user data.
•Cyberattacks, including computer malware, ransomware, viruses, spamming, and phishing attacks could harm our reputation, business, and operating results.
•We are subject to climate change risks, including physical and transitional risks, and if we are unable to manage such risks, our business may be adversely impacted.
•We have made climate related commitments that require us to invest significant effort, resources, and management time and circumstances may arise, including those beyond our control, that may require us to revise the contemplated timeframes for implementing these commitments.
•We rely on third parties maintaining open marketplaces to distribute our platform and to provide the software we use in certain of our products and offerings. If such third parties interfere with the distribution of our products or offerings or with our use of such software, our business would be adversely affected.
•We will require additional capital to support the growth of our business, and this capital might not be available on reasonable terms or at all.
•If we are unable to successfully identify, acquire and integrate suitable businesses, our operating results and prospects could be harmed, and any businesses we acquire may not perform as expected or be effectively integrated.
•We may continue to be blocked from or limited in providing or operating our products and offerings in certain jurisdictions, and may be required to modify our business model in those jurisdictions as a result.
•Our business is subject to numerous legal and regulatory risks that could have an adverse impact on our business and future prospects.
•Our business is subject to extensive government regulation and oversight relating to the provision of payment and financial services.
•We face risks related to our collection, use, transfer, disclosure, and other processing of data, which could result in investigations, inquiries, litigation, fines, legislative and regulatory action, and negative press about our privacy and data protection practices.
•If we are unable to protect our intellectual property, or if third parties are successful in claiming that we are misappropriating the intellectual property of others, we may incur significant expense and our business may be adversely affected.
•The market price of our common stock has been, and may continue to be, volatile or may decline steeply or suddenly regardless of our operating performance, and we may not be able to meet investor or analyst expectations. You may not be able to resell your shares at or above the price you paid and may lose all or part of your investment.
 Calling Function 

In \[ \]:

Copied!

print(response)

print(response)

The result of running MAGIC\_FORMULA on Uber's revenue and cost is -1690.

Back to top

[Previous Build your own OpenAI Agent](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent/)[Next OpenAI Agent Workarounds for Lengthy Tool Descriptions](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_lengthy_tools/)

Hi, how can I help you?

🦙
