Title: OpenAI Assistant Agent - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/openai_assistant_agent/

Markdown Content:
OpenAI Assistant Agent - LlamaIndex


[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/docs/examples/agent/openai_assistant_agent.ipynb)

This shows you how to use our agent abstractions built on top of the [OpenAI Assistant API](https://platform.openai.com/docs/assistants/overview).

In \[ \]:

Copied!

%pip install llama\-index\-agent\-openai
%pip install llama\-index\-vector\-stores\-supabase

%pip install llama-index-agent-openai %pip install llama-index-vector-stores-supabase

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

Simple Agent (no external tools)[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_assistant_agent/#simple-agent-no-external-tools)
-----------------------------------------------------------------------------------------------------------------------------------------------

Here we show a simple example with the built-in code interpreter.

Let's start by importing some simple building blocks.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

from llama\_index.agent.openai import OpenAIAssistantAgent

from llama\_index.agent.openai import OpenAIAssistantAgent

In \[ \]:

Copied!

agent \= OpenAIAssistantAgent.from\_new(
    name\="Math Tutor",
    instructions\="You are a personal math tutor. Write and run code to answer math questions.",
    openai\_tools\=\[{"type": "code\_interpreter"}\],
    instructions\_prefix\="Please address the user as Jane Doe. The user has a premium account.",
)

agent = OpenAIAssistantAgent.from\_new( name="Math Tutor", instructions="You are a personal math tutor. Write and run code to answer math questions.", openai\_tools=\[{"type": "code\_interpreter"}\], instructions\_prefix="Please address the user as Jane Doe. The user has a premium account.", )

In \[ \]:

Copied!

agent.thread\_id

agent.thread\_id

Out\[ \]:

'thread\_ctzN0ZY3JUWETHhYxI3DiFSo'

In \[ \]:

Copied!

response \= agent.chat(
    "I need to solve the equation \`3x + 11 = 14\`. Can you help me?"
)

response = agent.chat( "I need to solve the equation \`3x + 11 = 14\`. Can you help me?" )

In \[ \]:

Copied!

print(str(response))

print(str(response))

The solution to the equation \\(3x + 11 = 14\\) is \\(x = 1\\).

Assistant with Built-In Retrieval[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_assistant_agent/#assistant-with-built-in-retrieval)
---------------------------------------------------------------------------------------------------------------------------------------------------

Let's test the assistant by having it use the built-in OpenAI Retrieval tool over a user-uploaded file.

Here, we upload and pass in the file during assistant-creation time.

The other option is you can upload/pass the file-id in for a message in a given thread with `upload_files` and `add_message`.

In \[ \]:

Copied!

from llama\_index.agent.openai import OpenAIAssistantAgent

from llama\_index.agent.openai import OpenAIAssistantAgent

In \[ \]:

Copied!

agent \= OpenAIAssistantAgent.from\_new(
    name\="SEC Analyst",
    instructions\="You are a QA assistant designed to analyze sec filings.",
    openai\_tools\=\[{"type": "retrieval"}\],
    instructions\_prefix\="Please address the user as Jerry.",
    files\=\["data/10k/lyft\_2021.pdf"\],
    verbose\=True,
)

agent = OpenAIAssistantAgent.from\_new( name="SEC Analyst", instructions="You are a QA assistant designed to analyze sec filings.", openai\_tools=\[{"type": "retrieval"}\], instructions\_prefix="Please address the user as Jerry.", files=\["data/10k/lyft\_2021.pdf"\], verbose=True, )

In \[ \]:

Copied!

response \= agent.chat("What was Lyft's revenue growth in 2021?")

response = agent.chat("What was Lyft's revenue growth in 2021?")

In \[ \]:

Copied!

print(str(response))

print(str(response))

Lyft's revenue increased by $843.6 million or 36% in 2021 as compared to the previous year【7†source】.

Assistant with Query Engine Tools[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_assistant_agent/#assistant-with-query-engine-tools)
---------------------------------------------------------------------------------------------------------------------------------------------------

Here we showcase the function calling capabilities of the OpenAIAssistantAgent by integrating it with our query engine tools over different documents.

### 1\. Setup: Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_assistant_agent/#1-setup-load-data)

In \[ \]:

Copied!

from llama\_index.agent.openai import OpenAIAssistantAgent
from llama\_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
    load\_index\_from\_storage,
)

from llama\_index.core.tools import QueryEngineTool, ToolMetadata

from llama\_index.agent.openai import OpenAIAssistantAgent from llama\_index.core import ( SimpleDirectoryReader, VectorStoreIndex, StorageContext, load\_index\_from\_storage, ) from llama\_index.core.tools import QueryEngineTool, ToolMetadata

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

In \[ \]:

Copied!

!mkdir \-p 'data/10k/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' \-O 'data/10k/uber\_2021.pdf'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/lyft\_2021.pdf' \-O 'data/10k/lyft\_2021.pdf'

!mkdir -p 'data/10k/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' -O 'data/10k/uber\_2021.pdf' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/lyft\_2021.pdf' -O 'data/10k/lyft\_2021.pdf'

\--2023-11-07 00:20:08--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 2606:50c0:8000::154, 2606:50c0:8001::154, 2606:50c0:8002::154, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|2606:50c0:8000::154|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1880483 (1.8M) \[application/octet-stream\]
Saving to: ‘data/10k/uber\_2021.pdf’

data/10k/uber\_2021. 100%\[>\]   1.37M  --.-KB/s    in 0.06s   

2023-11-07 00:20:09 (22.2 MB/s) - ‘data/10k/lyft\_2021.pdf’ saved \[1440303/1440303\]

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

### 2\. Let's Try it Out[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_assistant_agent/#2-lets-try-it-out)

In \[ \]:

Copied!

agent \= OpenAIAssistantAgent.from\_new(
    name\="SEC Analyst",
    instructions\="You are a QA assistant designed to analyze sec filings.",
    tools\=query\_engine\_tools,
    instructions\_prefix\="Please address the user as Jerry.",
    verbose\=True,
    run\_retrieve\_sleep\_time\=1.0,
)

agent = OpenAIAssistantAgent.from\_new( name="SEC Analyst", instructions="You are a QA assistant designed to analyze sec filings.", tools=query\_engine\_tools, instructions\_prefix="Please address the user as Jerry.", verbose=True, run\_retrieve\_sleep\_time=1.0, )

In \[ \]:

Copied!

response \= agent.chat("What was Lyft's revenue growth in 2021?")

response = agent.chat("What was Lyft's revenue growth in 2021?")

\
Calling function: lyft\_10k with args: {"input":"What was Lyft's revenue growth in 2021?"}
Got output: Lyft's revenue growth in 2021 was 36%.
 Calling Function 

Calling function: lyft\_10k with args: {"input": "How did Lyft respond to COVID-19?"}

/Users/jerryliu/Programming/gpt\_index/.venv/lib/python3.10/site-packages/vecs/collection.py:445: UserWarning: Query does not have a covering index for cosine\_distance. See Collection.create\_index
  warnings.warn(

Got output: Lyft responded to COVID-19 by adopting multiple measures, including establishing new health and safety requirements for ridesharing and updating workplace policies. They also made adjustments to their expenses and cash flow to correlate with declines in revenues, which included headcount reductions in 2020. Additionally, Lyft temporarily reduced pricing for Flexdrive rentals in cities most affected by COVID-19 and waived rental fees for drivers who tested positive for COVID-19 or were requested to quarantine by a medical professional. These measures were implemented to mitigate the negative effects of the pandemic on their business.


In \[ \]:

Copied!

print(str(response))

print(str(response))

Lyft's 2021 10-K filing outlines a multifaceted risk landscape for the company, encapsulating both operational and environmental challenges that could impact its business model:

- \*\*Economic Factors\*\*: Risks include the ramifications of the COVID-19 pandemic, susceptibility to natural disasters, the volatility of economic downturns, and geopolitical tensions.

- \*\*Operational Dynamics\*\*: The company is cognizant of its limited operating history, the uncertainties surrounding its financial performance, the intense competition in the ridesharing sector, the unpredictability in financial results, and the ambiguity tied to the expansion potential of the rideshare market.

- \*\*Human Capital\*\*: A critical concern is the ability of Lyft to attract and maintain a robust network of both drivers and riders, which is essential for the platform's vitality.

- \*\*Insurance and Safety\*\*: Ensuring adequate insurance coverage for stakeholders and addressing autonomous vehicle technology risks are pivotal.

- \*\*Reputation and Brand\*\*: Lyft is attentive to the influence that illegal or unseemly activities on its platform can have on its public image.

- \*\*Pricing Structure\*\*: Changing pricing models pose a risk to Lyft's revenue streams, considering how essential pricing dynamics are to maintaining competitive service offerings.

- \*\*Systemic Integrity\*\*: Lyft also acknowledges risks emanating from potential system failures which could disrupt service continuity.

Furthermore, Lyft is vigilant about regulatory and legal risks that could lead to litigation and is conscious of the broader implications of climate change on its operations.

In terms of its response to COVID-19, Lyft has adopted strategic measures to secure the welfare of both its workforce and customer base:

1. \*\*Health and Safety Protocols\*\*: Lyft has instituted health and safety mandates tailored specifically to the ridesharing experience in view of the pandemic.

2. \*\*Workplace Adjustments\*\*: The company revised its workplace policies to accommodate the shifts in the work environment precipitated by the pandemic.

3. \*\*Financial Adaptations\*\*: To synchronize with the revenue contraction experienced during the pandemic, Lyft executed monetary realignments, which necessitated workforce reductions in 2020.

These initiatives reflect Lyft's calculated approach to navigating the operational and financial hurdles enacted by the COVID-19 pandemic. By prioritizing health and safety, nimbly altering corporate practices, and recalibrating fiscal management, Lyft aimed to buttress its business against the storm of the pandemic while setting a foundation for post-pandemic recovery.

Back to top

[Previous OpenAI Agent with Query Engine Tools](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_with_query_engine/)[Next OpenAI Assistant Advanced Retrieval Cookbook](https://docs.llamaindex.ai/en/stable/examples/agent/openai_assistant_query_cookbook/)

Hi, how can I help you?

🦙
