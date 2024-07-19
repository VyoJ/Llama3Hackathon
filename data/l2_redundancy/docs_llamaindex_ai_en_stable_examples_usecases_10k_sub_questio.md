Title: 10K Analysis - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/usecases/10k_sub_question/

Markdown Content:
10K Analysis - LlamaIndex


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
from llama\_index.llms.openai import OpenAI

from llama\_index.core.tools import QueryEngineTool, ToolMetadata
from llama\_index.core.query\_engine import SubQuestionQueryEngine

from llama\_index.core import SimpleDirectoryReader, VectorStoreIndex from llama\_index.llms.openai import OpenAI from llama\_index.core.tools import QueryEngineTool, ToolMetadata from llama\_index.core.query\_engine import SubQuestionQueryEngine

/Users/suo/miniconda3/envs/llama/lib/python3.9/site-packages/deeplake/util/check\_latest\_version.py:32: UserWarning: A newer version of deeplake (3.6.7) is available. It's recommended that you update to the latest version using \`pip install -U deeplake\`.
  warnings.warn(

Configure LLM service[¶](https://docs.llamaindex.ai/en/stable/examples/usecases/10k_sub_question/#configure-llm-service)
------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "YOUR\_API\_KEY"

import os os.environ\["OPENAI\_API\_KEY"\] = "YOUR\_API\_KEY"

In \[ \]:

Copied!

from llama\_index.core import Settings

Settings.llm \= OpenAI(temperature\=0.2, model\="gpt-3.5-turbo")

from llama\_index.core import Settings Settings.llm = OpenAI(temperature=0.2, model="gpt-3.5-turbo")

Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/usecases/10k_sub_question/#download-data)
--------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

!mkdir \-p 'data/10k/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' \-O 'data/10k/uber\_2021.pdf'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/lyft\_2021.pdf' \-O 'data/10k/lyft\_2021.pdf'

!mkdir -p 'data/10k/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' -O 'data/10k/uber\_2021.pdf' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/lyft\_2021.pdf' -O 'data/10k/lyft\_2021.pdf'

Load data[¶](https://docs.llamaindex.ai/en/stable/examples/usecases/10k_sub_question/#load-data)
------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

lyft\_docs \= SimpleDirectoryReader(
    input\_files\=\["./data/10k/lyft\_2021.pdf"\]
).load\_data()
uber\_docs \= SimpleDirectoryReader(
    input\_files\=\["./data/10k/uber\_2021.pdf"\]
).load\_data()

lyft\_docs = SimpleDirectoryReader( input\_files=\["./data/10k/lyft\_2021.pdf"\] ).load\_data() uber\_docs = SimpleDirectoryReader( input\_files=\["./data/10k/uber\_2021.pdf"\] ).load\_data()

Build indices[¶](https://docs.llamaindex.ai/en/stable/examples/usecases/10k_sub_question/#build-indices)
--------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

lyft\_index \= VectorStoreIndex.from\_documents(lyft\_docs)

lyft\_index = VectorStoreIndex.from\_documents(lyft\_docs)

In \[ \]:

Copied!

uber\_index \= VectorStoreIndex.from\_documents(uber\_docs)

uber\_index = VectorStoreIndex.from\_documents(uber\_docs)

Build query engines[¶](https://docs.llamaindex.ai/en/stable/examples/usecases/10k_sub_question/#build-query-engines)
--------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

lyft\_engine \= lyft\_index.as\_query\_engine(similarity\_top\_k\=3)

lyft\_engine = lyft\_index.as\_query\_engine(similarity\_top\_k=3)

In \[ \]:

Copied!

uber\_engine \= uber\_index.as\_query\_engine(similarity\_top\_k\=3)

uber\_engine = uber\_index.as\_query\_engine(similarity\_top\_k=3)

In \[ \]:

Copied!

query\_engine\_tools \= \[
    QueryEngineTool(
        query\_engine\=lyft\_engine,
        metadata\=ToolMetadata(
            name\="lyft\_10k",
            description\=(
                "Provides information about Lyft financials for year 2021"
            ),
        ),
    ),
    QueryEngineTool(
        query\_engine\=uber\_engine,
        metadata\=ToolMetadata(
            name\="uber\_10k",
            description\=(
                "Provides information about Uber financials for year 2021"
            ),
        ),
    ),
\]

s\_engine \= SubQuestionQueryEngine.from\_defaults(
    query\_engine\_tools\=query\_engine\_tools
)

query\_engine\_tools = \[ QueryEngineTool( query\_engine=lyft\_engine, metadata=ToolMetadata( name="lyft\_10k", description=( "Provides information about Lyft financials for year 2021" ), ), ), QueryEngineTool( query\_engine=uber\_engine, metadata=ToolMetadata( name="uber\_10k", description=( "Provides information about Uber financials for year 2021" ), ), ), \] s\_engine = SubQuestionQueryEngine.from\_defaults( query\_engine\_tools=query\_engine\_tools )

Run queries[¶](https://docs.llamaindex.ai/en/stable/examples/usecases/10k_sub_question/#run-queries)
----------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

response \= s\_engine.query(
    "Compare and contrast the customer segments and geographies that grew the"
    " fastest"
)

response = s\_engine.query( "Compare and contrast the customer segments and geographies that grew the" " fastest" )

Generated 4 sub questions.
\[uber\_10k\] Q: What customer segments grew the fastest for Uber
\[uber\_10k\] Q: What geographies grew the fastest for Uber
\[lyft\_10k\] Q: What customer segments grew the fastest for Lyft
\[lyft\_10k\] Q: What geographies grew the fastest for Lyft
\[uber\_10k\] A: 
Uber experienced the fastest growth in five metropolitan areas—Chicago, Miami, and New York City in the United States, Sao Paulo in Brazil, and London in the United Kingdom. Additionally, Uber experienced growth in suburban and rural areas, though the network is smaller and less liquid in these areas.
\[lyft\_10k\] A: 
Lyft has seen the fastest growth in its ridesharing marketplace, Express Drive, Lyft Rentals, Light Vehicles, Public Transit, and Lyft Autonomous customer segments. These customer segments have seen increased demand due to the convenience and high-quality experience they offer drivers and riders, as well as the investments Lyft has made in its proprietary technology, M&A and strategic partnerships, and brand and marketing efforts.
\[lyft\_10k\] A: 
Lyft has grown rapidly in cities across the United States and in select cities in Canada. The ridesharing market grew rapidly prior to the COVID-19 pandemic, and it is uncertain to what extent market acceptance will continue to grow after the pandemic. The market for Lyft's other offerings, such as its network of Light Vehicles, is also new and unproven, and it is uncertain whether demand for bike and scooter sharing will continue to grow.
\[uber\_10k\] A: in 2021?

The customer segments that grew the fastest for Uber in 2021 were Riders and Eaters, who use the platform for ridesharing services and meal preparation, grocery, and other delivery services, respectively. Additionally, Uber One, Uber Pass, Eats Pass, and Rides Pass membership programs grew significantly in 2021, with over 6 million members.

In \[ \]:

Copied!

print(response)

print(response)

Uber and Lyft both experienced the fastest growth in their respective customer segments and geographies in 2021. 

For Uber, the fastest growing customer segments were Riders and Eaters, who use the platform for ridesharing services and meal preparation, grocery, and other delivery services, respectively. Additionally, Uber One, Uber Pass, Eats Pass, and Rides Pass membership programs grew significantly in 2021, with over 6 million members. Uber experienced the fastest growth in five metropolitan areas—Chicago, Miami, and New York City in the United States, Sao Paulo in Brazil, and London in the United Kingdom. Additionally, Uber experienced growth in suburban and rural areas, though the network is smaller and less liquid in these areas.

For Lyft, the fastest growing customer segments were ridesharing, Express Drive, Lyft Rentals, Light Vehicles, Public Transit, and Lyft Autonomous. Lyft has grown rapidly in cities across the United States and in select cities in Canada. The ridesharing market grew rapidly prior to the COVID-19 pandemic, and it is uncertain to what extent market acceptance will continue to grow after the pandemic. The market for Lyft's other offerings, such as its network of Light Vehicles, is also new and unproven, and it is uncertain whether demand for bike and scooter sharing will continue to grow.

Overall, Uber and Lyft experienced the fastest growth in different customer segments and geographies. Uber experienced the fastest growth in Riders and Eaters, as well as in five metropolitan areas, while Lyft experienced the fastest growth in ridesharing, Express Drive, Lyft Rentals, Light Vehicles, Public Transit, and Lyft Autonomous, as well as in cities across the United States and in select cities in Canada.

In \[ \]:

Copied!

response \= s\_engine.query(
    "Compare revenue growth of Uber and Lyft from 2020 to 2021"
)

response = s\_engine.query( "Compare revenue growth of Uber and Lyft from 2020 to 2021" )

Generated 2 sub questions.
\[uber\_10k\] Q: What is the revenue growth of Uber from 2020 to 2021
\[lyft\_10k\] Q: What is the revenue growth of Lyft from 2020 to 2021
\[lyft\_10k\] A: 
The revenue of Lyft grew by 36% from 2020 to 2021.
\[uber\_10k\] A: 
The revenue growth of Uber from 2020 to 2021 was 57%, or 54% on a constant currency basis.

In \[ \]:

Copied!

print(response)

print(response)

The revenue growth of Uber from 2020 to 2021 was 57%, or 54% on a constant currency basis, while the revenue of Lyft grew by 36% from 2020 to 2021. Therefore, Uber had a higher revenue growth than Lyft from 2020 to 2021.

Back to top

[Previous Transforms Evaluation](https://docs.llamaindex.ai/en/stable/examples/transforms/TransformsEval/)[Next 10Q Analysis](https://docs.llamaindex.ai/en/stable/examples/usecases/10q_sub_question/)
