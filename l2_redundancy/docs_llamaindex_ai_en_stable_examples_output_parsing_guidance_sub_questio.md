Title: Guidance for Sub-Question Query Engine

URL Source: https://docs.llamaindex.ai/en/stable/examples/output_parsing/guidance_sub_question/

Markdown Content:
Guidance for Sub-Question Query Engine - LlamaIndex


In this notebook, we showcase how to use [**guidance**](https://github.com/microsoft/guidance) to improve the robustness of our sub-question query engine.

The sub-question query engine is designed to accept swappable question generators that implement the `BaseQuestionGenerator` interface.  
To leverage the power of [**guidance**](https://github.com/microsoft/guidance), we implemented a new `GuidanceQuestionGenerator` (powered by our `GuidancePydanticProgram`)

Guidance Question Generator[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/guidance_sub_question/#guidance-question-generator)
-----------------------------------------------------------------------------------------------------------------------------------------------

Unlike the default `LLMQuestionGenerator`, guidance guarantees that we will get the desired structured output, and eliminate output parsing errors.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-question\-gen\-guidance

%pip install llama-index-question-gen-guidance

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

from llama\_index.question\_gen.guidance import GuidanceQuestionGenerator
from guidance.llms import OpenAI as GuidanceOpenAI

from llama\_index.question\_gen.guidance import GuidanceQuestionGenerator from guidance.llms import OpenAI as GuidanceOpenAI

In \[ \]:

Copied!

question\_gen \= GuidanceQuestionGenerator.from\_defaults(
    guidance\_llm\=GuidanceOpenAI("text-davinci-003"), verbose\=False
)

question\_gen = GuidanceQuestionGenerator.from\_defaults( guidance\_llm=GuidanceOpenAI("text-davinci-003"), verbose=False )

Let's test it out!

In \[ \]:

Copied!

from llama\_index.core.tools import ToolMetadata
from llama\_index.core import QueryBundle

from llama\_index.core.tools import ToolMetadata from llama\_index.core import QueryBundle

In \[ \]:

Copied!

tools \= \[
    ToolMetadata(
        name\="lyft\_10k",
        description\="Provides information about Lyft financials for year 2021",
    ),
    ToolMetadata(
        name\="uber\_10k",
        description\="Provides information about Uber financials for year 2021",
    ),
\]

tools = \[ ToolMetadata( name="lyft\_10k", description="Provides information about Lyft financials for year 2021", ), ToolMetadata( name="uber\_10k", description="Provides information about Uber financials for year 2021", ), \]

In \[ \]:

Copied!

sub\_questions \= question\_gen.generate(
    tools\=tools,
    query\=QueryBundle("Compare and contrast Uber and Lyft financial in 2021"),
)

sub\_questions = question\_gen.generate( tools=tools, query=QueryBundle("Compare and contrast Uber and Lyft financial in 2021"), )

In \[ \]:

Copied!

sub\_questions

sub\_questions

Out\[ \]:

\[SubQuestion(sub\_question='What is the revenue of Uber', tool\_name='uber\_10k'),
 SubQuestion(sub\_question='What is the EBITDA of Uber', tool\_name='uber\_10k'),
 SubQuestion(sub\_question='What is the net income of Uber', tool\_name='uber\_10k'),
 SubQuestion(sub\_question='What is the revenue of Lyft', tool\_name='lyft\_10k'),
 SubQuestion(sub\_question='What is the EBITDA of Lyft', tool\_name='lyft\_10k'),
 SubQuestion(sub\_question='What is the net income of Lyft', tool\_name='lyft\_10k')\]

Using Guidance Question Generator with Sub-Question Query Engine[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/guidance_sub_question/#using-guidance-question-generator-with-sub-question-query-engine)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Prepare data and base query engines[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/guidance_sub_question/#prepare-data-and-base-query-engines)

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama\_index.core.response.pprint\_utils import pprint\_response

from llama\_index.core.tools import QueryEngineTool, ToolMetadata
from llama\_index.core.query\_engine import SubQuestionQueryEngine

from llama\_index.core import SimpleDirectoryReader, VectorStoreIndex from llama\_index.core.response.pprint\_utils import pprint\_response from llama\_index.core.tools import QueryEngineTool, ToolMetadata from llama\_index.core.query\_engine import SubQuestionQueryEngine

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/10k/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' \-O 'data/10k/uber\_2021.pdf'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/lyft\_2021.pdf' \-O 'data/10k/lyft\_2021.pdf'

!mkdir -p 'data/10k/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' -O 'data/10k/uber\_2021.pdf' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/lyft\_2021.pdf' -O 'data/10k/lyft\_2021.pdf'

In \[ \]:

Copied!

lyft\_docs \= SimpleDirectoryReader(
    input\_files\=\["./data/10k/lyft\_2021.pdf"\]
).load\_data()
uber\_docs \= SimpleDirectoryReader(
    input\_files\=\["./data/10k/uber\_2021.pdf"\]
).load\_data()

lyft\_docs = SimpleDirectoryReader( input\_files=\["./data/10k/lyft\_2021.pdf"\] ).load\_data() uber\_docs = SimpleDirectoryReader( input\_files=\["./data/10k/uber\_2021.pdf"\] ).load\_data()

In \[ \]:

Copied!

lyft\_index \= VectorStoreIndex.from\_documents(lyft\_docs)
uber\_index \= VectorStoreIndex.from\_documents(uber\_docs)

lyft\_index = VectorStoreIndex.from\_documents(lyft\_docs) uber\_index = VectorStoreIndex.from\_documents(uber\_docs)

In \[ \]:

Copied!

lyft\_engine \= lyft\_index.as\_query\_engine(similarity\_top\_k\=3)
uber\_engine \= uber\_index.as\_query\_engine(similarity\_top\_k\=3)

lyft\_engine = lyft\_index.as\_query\_engine(similarity\_top\_k=3) uber\_engine = uber\_index.as\_query\_engine(similarity\_top\_k=3)

### Construct sub-question query engine and run some queries![¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/guidance_sub_question/#construct-sub-question-query-engine-and-run-some-queries)

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
    question\_gen\=question\_gen,  \# use guidance based question\_gen defined above
    query\_engine\_tools\=query\_engine\_tools,
)

query\_engine\_tools = \[ QueryEngineTool( query\_engine=lyft\_engine, metadata=ToolMetadata( name="lyft\_10k", description=( "Provides information about Lyft financials for year 2021" ), ), ), QueryEngineTool( query\_engine=uber\_engine, metadata=ToolMetadata( name="uber\_10k", description=( "Provides information about Uber financials for year 2021" ), ), ), \] s\_engine = SubQuestionQueryEngine.from\_defaults( question\_gen=question\_gen, # use guidance based question\_gen defined above query\_engine\_tools=query\_engine\_tools, )

In \[ \]:

Copied!

response \= s\_engine.query(
    "Compare and contrast the customer segments and geographies that grew the"
    " fastest"
)

response = s\_engine.query( "Compare and contrast the customer segments and geographies that grew the" " fastest" )

Generated 4 sub questions.
\[uber\_10k\] Q: What customer segments grew the fastest for Uber
\[uber\_10k\] A: in 2021?

The customer segments that grew the fastest for Uber in 2021 were its Mobility Drivers, Couriers, Riders, and Eaters. These segments experienced growth due to the continued stay-at-home order demand related to COVID-19, as well as Uber's membership programs, such as Uber One, Uber Pass, Eats Pass, and Rides Pass. Additionally, Uber's marketplace-centric advertising helped to connect merchants and brands with its platform network, further driving growth.
\[uber\_10k\] Q: What geographies grew the fastest for Uber
\[uber\_10k\] A: 
Based on the context information, it appears that Uber experienced the most growth in large metropolitan areas, such as Chicago, Miami, New York City, Sao Paulo, and London. Additionally, Uber experienced growth in suburban and rural areas, as well as in countries such as Argentina, Germany, Italy, Japan, South Korea, and Spain.
\[lyft\_10k\] Q: What customer segments grew the fastest for Lyft
\[lyft\_10k\] A: 
The customer segments that grew the fastest for Lyft were ridesharing, light vehicles, and public transit. Ridesharing grew as Lyft was able to predict demand and proactively incentivize drivers to be available for rides in the right place at the right time. Light vehicles grew as users were looking for options that were more active, usually lower-priced, and often more efficient for short trips during heavy traffic. Public transit grew as Lyft integrated third-party public transit data into the Lyft App to offer users a robust view of transportation options around them.
\[lyft\_10k\] Q: What geographies grew the fastest for Lyft
\[lyft\_10k\] A: 
It is not possible to answer this question with the given context information.

In \[ \]:

Copied!

print(response)

print(response)

The customer segments that grew the fastest for Uber in 2021 were its Mobility Drivers, Couriers, Riders, and Eaters. These segments experienced growth due to the continued stay-at-home order demand related to COVID-19, as well as Uber's membership programs, such as Uber One, Uber Pass, Eats Pass, and Rides Pass. Additionally, Uber's marketplace-centric advertising helped to connect merchants and brands with its platform network, further driving growth. Uber experienced the most growth in large metropolitan areas, such as Chicago, Miami, New York City, Sao Paulo, and London. Additionally, Uber experienced growth in suburban and rural areas, as well as in countries such as Argentina, Germany, Italy, Japan, South Korea, and Spain.

The customer segments that grew the fastest for Lyft were ridesharing, light vehicles, and public transit. Ridesharing grew as Lyft was able to predict demand and proactively incentivize drivers to be available for rides in the right place at the right time. Light vehicles grew as users were looking for options that were more active, usually lower-priced, and often more efficient for short trips during heavy traffic. Public transit grew as Lyft integrated third-party public transit data into the Lyft App to offer users a robust view of transportation options around them. It is not possible to answer the question of which geographies grew the fastest for Lyft with the given context information.

In summary, Uber and Lyft both experienced growth in customer segments related to their respective services, such as Mobility Drivers, Couriers, Riders, and Eaters for Uber, and ridesharing, light vehicles, and public transit for Lyft. Uber experienced the most growth in large metropolitan areas, as well as in suburban and rural areas, and in countries such as Argentina, Germany, Italy, Japan, South Korea, and Spain. It is not possible to answer the question of which geographies grew the fastest for Lyft with the given context information.

Back to top

[Previous Guidance Pydantic Program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/guidance_pydantic_program/)[Next LLM Pydantic Program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/llm_program/)

Hi, how can I help you?

🦙
