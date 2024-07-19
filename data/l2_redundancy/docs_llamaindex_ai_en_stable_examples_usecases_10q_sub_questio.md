Title: 10Q Analysis - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/usecases/10q_sub_question/

Markdown Content:
10Q Analysis - LlamaIndex


In this demo, we explore answering complex queries by decomposing them into simpler sub-queries.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai

%pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import nest\_asyncio

nest\_asyncio.apply()

import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama\_index.core.response.pprint\_utils import pprint\_response
from llama\_index.llms.openai import OpenAI

from llama\_index.core.tools import QueryEngineTool, ToolMetadata
from llama\_index.core.query\_engine import SubQuestionQueryEngine

from llama\_index.core import SimpleDirectoryReader, VectorStoreIndex from llama\_index.core.response.pprint\_utils import pprint\_response from llama\_index.llms.openai import OpenAI from llama\_index.core.tools import QueryEngineTool, ToolMetadata from llama\_index.core.query\_engine import SubQuestionQueryEngine

Configure LLM service[¶](https://docs.llamaindex.ai/en/stable/examples/usecases/10q_sub_question/#configure-llm-service)
------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "OPENAI\_API\_KEY"

import os os.environ\["OPENAI\_API\_KEY"\] = "OPENAI\_API\_KEY"

In \[ \]:

Copied!

from llama\_index.core import Settings

Settings.llm \= OpenAI(temperature\=0.2, model\="gpt-3.5-turbo")

from llama\_index.core import Settings Settings.llm = OpenAI(temperature=0.2, model="gpt-3.5-turbo")

Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/usecases/10q_sub_question/#download-data)
--------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

!mkdir \-p 'data/10q/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10q/uber\_10q\_march\_2022.pdf' \-O 'data/10q/uber\_10q\_march\_2022.pdf'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10q/uber\_10q\_june\_2022.pdf' \-O 'data/10q/uber\_10q\_june\_2022.pdf'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10q/uber\_10q\_sept\_2022.pdf' \-O 'data/10q/uber\_10q\_sept\_2022.pdf'

!mkdir -p 'data/10q/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10q/uber\_10q\_march\_2022.pdf' -O 'data/10q/uber\_10q\_march\_2022.pdf' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10q/uber\_10q\_june\_2022.pdf' -O 'data/10q/uber\_10q\_june\_2022.pdf' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10q/uber\_10q\_sept\_2022.pdf' -O 'data/10q/uber\_10q\_sept\_2022.pdf'

Load data[¶](https://docs.llamaindex.ai/en/stable/examples/usecases/10q_sub_question/#load-data)
------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

march\_2022 \= SimpleDirectoryReader(
    input\_files\=\["./data/10q/uber\_10q\_march\_2022.pdf"\]
).load\_data()
june\_2022 \= SimpleDirectoryReader(
    input\_files\=\["./data/10q/uber\_10q\_june\_2022.pdf"\]
).load\_data()
sept\_2022 \= SimpleDirectoryReader(
    input\_files\=\["./data/10q/uber\_10q\_sept\_2022.pdf"\]
).load\_data()

march\_2022 = SimpleDirectoryReader( input\_files=\["./data/10q/uber\_10q\_march\_2022.pdf"\] ).load\_data() june\_2022 = SimpleDirectoryReader( input\_files=\["./data/10q/uber\_10q\_june\_2022.pdf"\] ).load\_data() sept\_2022 = SimpleDirectoryReader( input\_files=\["./data/10q/uber\_10q\_sept\_2022.pdf"\] ).load\_data()

Build indices[¶](https://docs.llamaindex.ai/en/stable/examples/usecases/10q_sub_question/#build-indices)


In \[ \]:

Copied!

march\_index \= VectorStoreIndex.from\_documents(march\_2022)
june\_index \= VectorStoreIndex.from\_documents(june\_2022)
sept\_index \= VectorStoreIndex.from\_documents(sept\_2022)

march\_index = VectorStoreIndex.from\_documents(march\_2022) june\_index = VectorStoreIndex.from\_documents(june\_2022) sept\_index = VectorStoreIndex.from\_documents(sept\_2022)

Build query engines[¶](https://docs.llamaindex.ai/en/stable/examples/usecases/10q_sub_question/#build-query-engines)
--------------------------------------------------------------------------------------------------------------------

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
        query\_engine\=sept\_engine,
        metadata\=ToolMetadata(
            name\="sept\_22",
            description\=(
                "Provides information about Uber quarterly financials ending"
                " September 2022"
            ),
        ),
    ),
    QueryEngineTool(
        query\_engine\=june\_engine,
        metadata\=ToolMetadata(
            name\="june\_22",
            description\=(
                "Provides information about Uber quarterly financials ending"
                " June 2022"
            ),
        ),
    ),
    QueryEngineTool(
        query\_engine\=march\_engine,
        metadata\=ToolMetadata(
            name\="march\_22",
            description\=(
                "Provides information about Uber quarterly financials ending"
                " March 2022"
            ),
        ),
    ),
\]

query\_engine\_tools = \[ QueryEngineTool( query\_engine=sept\_engine, metadata=ToolMetadata( name="sept\_22", description=( "Provides information about Uber quarterly financials ending" " September 2022" ), ), ), QueryEngineTool( query\_engine=june\_engine, metadata=ToolMetadata( name="june\_22", description=( "Provides information about Uber quarterly financials ending" " June 2022" ), ), ), QueryEngineTool( query\_engine=march\_engine, metadata=ToolMetadata( name="march\_22", description=( "Provides information about Uber quarterly financials ending" " March 2022" ), ), ), \]

In \[ \]:

Copied!

s\_engine \= SubQuestionQueryEngine.from\_defaults(
    query\_engine\_tools\=query\_engine\_tools
)

s\_engine = SubQuestionQueryEngine.from\_defaults( query\_engine\_tools=query\_engine\_tools )

Run queries[¶](https://docs.llamaindex.ai/en/stable/examples/usecases/10q_sub_question/#run-queries)
----------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

response \= s\_engine.query(
    "Analyze Uber revenue growth over the latest two quarter filings"
)

response = s\_engine.query( "Analyze Uber revenue growth over the latest two quarter filings" )

Generated 2 sub questions.
\[sept\_22\] Q: What is the revenue growth of Uber for the quarter ending September 2022
\[sept\_22\] A: compared to the same period in 2021?

The revenue growth of Uber for the quarter ending September 2022 compared to the same period in 2021 is 72%.
\[june\_22\] Q: What is the revenue growth of Uber for the quarter ending June 2022
\[june\_22\] A: compared to the same period in 2021?

The revenue growth of Uber for the quarter ending June 2022 compared to the same period in 2021 is 105%.

In \[ \]:

Copied!

print(response)

print(response)

Uber's revenue growth over the latest two quarter filings has been strong, with a 72% increase for the quarter ending September 2022 compared to the same period in 2021, and a 105% increase for the quarter ending June 2022 compared to the same period in 2021.

In \[ \]:

Copied!

response \= s\_engine.query(
    "Analyze change in macro environment over the 3 quarters"
)

response = s\_engine.query( "Analyze change in macro environment over the 3 quarters" )

Generated 3 sub questions.
\[sept\_22\] Q: What is the macro environment in September 2022
\[sept\_22\] A: 
The macro environment in September 2022 is one of recovery from the impacts of the COVID-19 pandemic, with increases in Mobility Trip volumes, a $1.3 billion increase in Freight Gross Bookings resulting from the acquisition of Transplace, a $1.1 billion increase in Mobility revenue due to business model changes in the UK, and a $164 million increase in Delivery revenue due to an increase in certain Courier payments and incentives. Additionally, there was a $2.2 billion net increase in Mobility revenue due to business model changes in the UK and an accrual made for the resolution of historical claims in the UK relating to the classification of drivers, and a $751 million increase in Delivery revenue due to an increase in certain Courier payments and incentives.
\[june\_22\] Q: What is the macro environment in June 2022
\[june\_22\] A: 
In June 2022, the macro environment is characterized by the continued impact of COVID-19 restrictions on global demand, the adoption of new accounting standards, and the potential for shifts in consumer travel patterns due to health concerns.
\[march\_22\] Q: What is the macro environment in March 2022
\[march\_22\] A: 
The macro environment in March 2022 is uncertain, as the effects of the COVID-19 pandemic and the actions taken to mitigate it are still being felt. Travel restrictions, business restrictions, school closures, and limitations on social or public gatherings may still be in place in some regions, and the demand for services may still be affected.

In \[ \]:

Copied!

print(response)

print(response)

The macro environment has seen a significant change over the three quarters from March 2022 to September 2022. In March 2022, the macro environment was uncertain due to the effects of the COVID-19 pandemic and the actions taken to mitigate it. By June 2022, the macro environment was characterized by the continued impact of COVID-19 restrictions on global demand, the adoption of new accounting standards, and the potential for shifts in consumer travel patterns due to health concerns. By September 2022, the macro environment had shifted to one of recovery from the impacts of the COVID-19 pandemic, with increases in Mobility Trip volumes, a $1.3 billion increase in Freight Gross Bookings resulting from the acquisition of Transplace, a $1.1 billion increase in Mobility revenue due to business model changes in the UK, and a $164 million increase in Delivery revenue due to an increase in certain Courier payments and incentives. Additionally, there was a $2.2 billion net increase in Mobility revenue due to business model changes in the UK and an accrual made for the resolution of historical claims in the UK relating to the classification of drivers, and a $751 million increase in Delivery revenue due to an increase in certain Courier payments and incentives.

In \[ \]:

Copied!

response \= s\_engine.query("How much cash did Uber have in sept 2022")

response = s\_engine.query("How much cash did Uber have in sept 2022")

Generated 1 sub questions.
\[sept\_22\] Q: How much cash did Uber have in September 2022
\[sept\_22\] A: 
Uber had $4,865 million in cash in September 2022.

In \[ \]:

Copied!

print(response)

print(response)

Uber had $4,865 million in cash in September 2022.

Back to top

[Previous 10K Analysis](https://docs.llamaindex.ai/en/stable/examples/usecases/10k_sub_question/)[Next Email Data Extraction](https://docs.llamaindex.ai/en/stable/examples/usecases/email_data_extraction/)
