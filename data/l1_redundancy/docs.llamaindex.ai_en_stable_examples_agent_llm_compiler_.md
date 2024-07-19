Title: LLM Compiler Agent Cookbook - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/llm_compiler/

Markdown Content:
LLM Compiler Agent Cookbook - LlamaIndex


[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/docs/examples/agent/llm_compiler.ipynb)

**NOTE**: Full credits to the [source repo for LLMCompiler](https://github.com/SqueezeAILab/LLMCompiler). A lot of our implementation was lifted from this repo (and adapted with LlamaIndex modules).

In this cookbook, we show how to use our LLMCompiler agent implementation for various settings. This includes using some simple function tools to do math, but also to answer multi-part queries for more advanced RAG use cases over multiple documents.

We see that the LLMCompilerAgent is capable of parallel function calling, giving results much more quickly than sequential execution through ReAct.

In \[ \]:

Copied!

%pip install llama\-index\-agent\-llm\-compiler
%pip install llama\-index\-readers\-wikipedia
%pip install llama\-index\-llms\-openai

%pip install llama-index-agent-llm-compiler %pip install llama-index-readers-wikipedia %pip install llama-index-llms-openai

In \[ \]:

Copied!

import nest\_asyncio

nest\_asyncio.apply()

import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

from llama\_index.agent.llm\_compiler import LLMCompilerAgentWorker

from llama\_index.agent.llm\_compiler import LLMCompilerAgentWorker

Test LLMCompiler Agent with Simple Functions[¶](https://docs.llamaindex.ai/en/stable/examples/agent/llm_compiler/#test-llmcompiler-agent-with-simple-functions)
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Here we test the LLMCompilerAgent with simple math functions (add, multiply) to illustrate how it works.

In \[ \]:

Copied!

import json
from typing import Sequence, List

from llama\_index.llms.openai import OpenAI
from llama\_index.core.llms import ChatMessage
from llama\_index.core.tools import BaseTool, FunctionTool

import json from typing import Sequence, List from llama\_index.llms.openai import OpenAI from llama\_index.core.llms import ChatMessage from llama\_index.core.tools import BaseTool, FunctionTool

### Define Functions[¶](https://docs.llamaindex.ai/en/stable/examples/agent/llm_compiler/#define-functions)

In \[ \]:

Copied!

def multiply(a: int, b: int) \-> int:
    """Multiple two integers and returns the result integer"""
    return a \* b

multiply\_tool \= FunctionTool.from\_defaults(fn\=multiply)

def add(a: int, b: int) \-> int:
    """Add two integers and returns the result integer"""
    return a + b

add\_tool \= FunctionTool.from\_defaults(fn\=add)

tools \= \[multiply\_tool, add\_tool\]

def multiply(a: int, b: int) -> int: """Multiple two integers and returns the result integer""" return a \* b multiply\_tool = FunctionTool.from\_defaults(fn=multiply) def add(a: int, b: int) -> int: """Add two integers and returns the result integer""" return a + b add\_tool = FunctionTool.from\_defaults(fn=add) tools = \[multiply\_tool, add\_tool\]

In \[ \]:

Copied!

multiply\_tool.metadata.fn\_schema\_str

multiply\_tool.metadata.fn\_schema\_str

Out\[ \]:

'{"type": "object", "properties": {"a": {"title": "A", "type": "integer"}, "b": {"title": "B", "type": "integer"}}, "required": \["a", "b"\]}'

### Setup LLMCompiler Agent[¶](https://docs.llamaindex.ai/en/stable/examples/agent/llm_compiler/#setup-llmcompiler-agent)

We import the `LLMCompilerAgentWorker` and combine it with the `AgentRunner`.

In \[ \]:

Copied!

from llama\_index.core.agent import AgentRunner

from llama\_index.core.agent import AgentRunner

In \[ \]:

Copied!

llm \= OpenAI(model\="gpt-4")

llm = OpenAI(model="gpt-4")

In \[ \]:

Copied!

callback\_manager \= llm.callback\_manager

callback\_manager = llm.callback\_manager

In \[ \]:

Copied!

agent\_worker \= LLMCompilerAgentWorker.from\_tools(
    tools, llm\=llm, verbose\=True, callback\_manager\=callback\_manager
)
agent \= AgentRunner(agent\_worker, callback\_manager\=callback\_manager)

agent\_worker = LLMCompilerAgentWorker.from\_tools( tools, llm=llm, verbose=True, callback\_manager=callback\_manager ) agent = AgentRunner(agent\_worker, callback\_manager=callback\_manager)

### Test out some Queries[¶](https://docs.llamaindex.ai/en/stable/examples/agent/llm_compiler/#test-out-some-queries)

In \[ \]:

Copied!

response \= agent.chat("What is (121 \* 3) + 42?")

response = agent.chat("What is (121 \* 3) + 42?")

\> Running step 1ecbfd84-5440-4390-b954-a6c83b2dcb9a for task 8ac1971d-e9ee-4bf3-9e42-b6b07ab7c2da.
> Step count: 0
\> Plan: 1. multiply(121, 3)
2. add($1, 42)
Thought: I can answer the question now.
3. join()<END\_OF\_PLAN>
Ran task: multiply. Observation: 363
Ran task: add. Observation: 405
Ran task: join. Observation: None
\> Thought: The result of the operation is 405.
\> Answer: 405

In \[ \]:

Copied!

response

response

Out\[ \]:

AgentChatResponse(response='405', sources=\[\], source\_nodes=\[\], is\_dummy\_stream=False)

In \[ \]:

Copied!

agent.memory.get\_all()

agent.memory.get\_all()

Out\[ \]:

\[ChatMessage(role=<MessageRole.USER: 'user'>, content='What is (121 \* 3) + 42?', additional\_kwargs={}),
 ChatMessage(role=<MessageRole.ASSISTANT: 'assistant'>, content='405', additional\_kwargs={})\]

Try out LLMCompiler for RAG[¶](https://docs.llamaindex.ai/en/stable/examples/agent/llm_compiler/#try-out-llmcompiler-for-rag)
-----------------------------------------------------------------------------------------------------------------------------

Now let's try out the LLMCompiler for RAG use cases. Specifically, we load a dataset of Wikipedia articles about various cities and ask questions over them.

### Setup Data[¶](https://docs.llamaindex.ai/en/stable/examples/agent/llm_compiler/#setup-data)

We use our `WikipediaReader` to load data for various cities.

In \[ \]:

Copied!

%pip install llama\-index\-readers\-wikipedia wikipedia

%pip install llama-index-readers-wikipedia wikipedia

In \[ \]:

Copied!

from llama\_index.readers.wikipedia import WikipediaReader

from llama\_index.readers.wikipedia import WikipediaReader

In \[ \]:

Copied!

wiki\_titles \= \["Toronto", "Seattle", "Chicago", "Boston", "Miami"\]

wiki\_titles = \["Toronto", "Seattle", "Chicago", "Boston", "Miami"\]

In \[ \]:

Copied!

city\_docs \= {}
reader \= WikipediaReader()
for wiki\_title in wiki\_titles:
    docs \= reader.load\_data(pages\=\[wiki\_title\])
    city\_docs\[wiki\_title\] \= docs

city\_docs = {} reader = WikipediaReader() for wiki\_title in wiki\_titles: docs = reader.load\_data(pages=\[wiki\_title\]) city\_docs\[wiki\_title\] = docs

### Setup LLM + Service Context[¶](https://docs.llamaindex.ai/en/stable/examples/agent/llm_compiler/#setup-llm-service-context)

In \[ \]:

Copied!

from llama\_index.core import ServiceContext
from llama\_index.llms.openai import OpenAI
from llama\_index.core.callbacks import CallbackManager

llm \= OpenAI(temperature\=0, model\="gpt-4")
service\_context \= ServiceContext.from\_defaults(llm\=llm)
callback\_manager \= CallbackManager(\[\])

from llama\_index.core import ServiceContext from llama\_index.llms.openai import OpenAI from llama\_index.core.callbacks import CallbackManager llm = OpenAI(temperature=0, model="gpt-4") service\_context = ServiceContext.from\_defaults(llm=llm) callback\_manager = CallbackManager(\[\])

/var/folders/0g/wd11bmkd791fz7hvgy1kqyp00000gn/T/ipykernel\_52010/432572999.py:6: DeprecationWarning: Call to deprecated class method from\_defaults. (ServiceContext is deprecated, please use \`llama\_index.settings.Settings\` instead.) -- Deprecated since version 0.10.0.
  service\_context = ServiceContext.from\_defaults(llm=llm)

### Define Toolset[¶](https://docs.llamaindex.ai/en/stable/examples/agent/llm_compiler/#define-toolset)

In \[ \]:

Copied!

from llama\_index.core import load\_index\_from\_storage, StorageContext
from llama\_index.core.node\_parser import SentenceSplitter
from llama\_index.core.tools import QueryEngineTool, ToolMetadata
from llama\_index.core import VectorStoreIndex
import os

node\_parser \= SentenceSplitter()

\# Build agents dictionary
query\_engine\_tools \= \[\]

for idx, wiki\_title in enumerate(wiki\_titles):
    nodes \= node\_parser.get\_nodes\_from\_documents(city\_docs\[wiki\_title\])

    if not os.path.exists(f"./data/{wiki\_title}"):
        \# build vector index
        vector\_index \= VectorStoreIndex(
            nodes,
            service\_context\=service\_context,
            callback\_manager\=callback\_manager,
        )
        vector\_index.storage\_context.persist(
            persist\_dir\=f"./data/{wiki\_title}"
        )
    else:
        vector\_index \= load\_index\_from\_storage(
            StorageContext.from\_defaults(persist\_dir\=f"./data/{wiki\_title}"),
            service\_context\=service\_context,
            callback\_manager\=callback\_manager,
        )
    \# define query engines
    vector\_query\_engine \= vector\_index.as\_query\_engine()

    \# define tools
    query\_engine\_tools.append(
        QueryEngineTool(
            query\_engine\=vector\_query\_engine,
            metadata\=ToolMetadata(
                name\=f"vector\_tool\_{wiki\_title}",
                description\=(
                    "Useful for questions related to specific aspects of"
                    f" {wiki\_title} (e.g. the history, arts and culture,"
                    " sports, demographics, or more)."
                ),
            ),
        )
    )

from llama\_index.core import load\_index\_from\_storage, StorageContext from llama\_index.core.node\_parser import SentenceSplitter from llama\_index.core.tools import QueryEngineTool, ToolMetadata from llama\_index.core import VectorStoreIndex import os node\_parser = SentenceSplitter() # Build agents dictionary query\_engine\_tools = \[\] for idx, wiki\_title in enumerate(wiki\_titles): nodes = node\_parser.get\_nodes\_from\_documents(city\_docs\[wiki\_title\]) if not os.path.exists(f"./data/{wiki\_title}"): # build vector index vector\_index = VectorStoreIndex( nodes, service\_context=service\_context, callback\_manager=callback\_manager, ) vector\_index.storage\_context.persist( persist\_dir=f"./data/{wiki\_title}" ) else: vector\_index = load\_index\_from\_storage( StorageContext.from\_defaults(persist\_dir=f"./data/{wiki\_title}"), service\_context=service\_context, callback\_manager=callback\_manager, ) # define query engines vector\_query\_engine = vector\_index.as\_query\_engine() # define tools query\_engine\_tools.append( QueryEngineTool( query\_engine=vector\_query\_engine, metadata=ToolMetadata( name=f"vector\_tool\_{wiki\_title}", description=( "Useful for questions related to specific aspects of" f" {wiki\_title} (e.g. the history, arts and culture," " sports, demographics, or more)." ), ), ) )

### Setup LLMCompilerAgent[¶](https://docs.llamaindex.ai/en/stable/examples/agent/llm_compiler/#setup-llmcompileragent)

In \[ \]:

Copied!

from llama\_index.core.agent import AgentRunner
from llama\_index.llms.openai import OpenAI

llm \= OpenAI(model\="gpt-4")
agent\_worker \= LLMCompilerAgentWorker.from\_tools(
    query\_engine\_tools,
    llm\=llm,
    verbose\=True,
    callback\_manager\=callback\_manager,
)
agent \= AgentRunner(agent\_worker, callback\_manager\=callback\_manager)

from llama\_index.core.agent import AgentRunner from llama\_index.llms.openai import OpenAI llm = OpenAI(model="gpt-4") agent\_worker = LLMCompilerAgentWorker.from\_tools( query\_engine\_tools, llm=llm, verbose=True, callback\_manager=callback\_manager, ) agent = AgentRunner(agent\_worker, callback\_manager=callback\_manager)

### Test out Queries[¶](https://docs.llamaindex.ai/en/stable/examples/agent/llm_compiler/#test-out-queries)

In \[ \]:

Copied!

response \= agent.chat(
    "Tell me about the demographics of Miami, and compare that with the demographics of Chicago?"
)
print(str(response))

response = agent.chat( "Tell me about the demographics of Miami, and compare that with the demographics of Chicago?" ) print(str(response))

\> Running step 7010cd56-3e69-4e25-8875-1ae0ab644e7d for task 1ec47644-e7e5-459e-81b4-2cb2f8105912.
> Step count: 0
\> Plan: 1. vector\_tool\_Miami("demographics")
2. vector\_tool\_Chicago("demographics")
3. join()<END\_OF\_PLAN>
Ran task: vector\_tool\_Chicago. Observation: Chicago's demographics are diverse and have changed significantly over time. The city's industrial working class was initially formed by various ethnic groups, with a significant influx of African Americans from the American South in the early 20th century. The city also has a notable Bosnian population that arrived mainly in the 1990s and 2000s. Most of the foreign-born population in Chicago were born in Mexico, Poland, and India. 

As of July 2019, the largest racial or ethnic group in Chicago is non-Hispanic White, making up 32.8% of the population, followed by Blacks at 30.1% and the Hispanic population at 29.0%. The city also has the third-largest LGBT population in the United States, with an estimated 7.5% of the adult population identifying as LGBTQ in 2018. 

In terms of economic demographics, the median income for a household in the city was $47,408, and the median income for a family was $54,188, according to the U.S. Census Bureau's American Community Survey data estimates for 2008–2012. About 18.3% of families and 22.1% of the population lived below the poverty line. 

Religion also plays a significant role in the city's demographics. Christianity is the most practiced religion in Chicago, with Roman Catholicism and Protestantism being the largest branches. The city also has a sizable non-Christian population, including those who are irreligious, Jewish, Muslim, Buddhist, and Hindu.
Ran task: vector\_tool\_Miami. Observation: Miami is the largest city in South Florida and the second-largest in Florida, with a population of 442,241 as of the 2020 census. The city is part of the Miami metropolitan area, which has over 6 million residents. Miami's population is diverse, with a significant Hispanic majority. In 1970, the population was reported as 45.3% Hispanic, 32.9% non-Hispanic white, and 22.7% black. As of 2010, 34.4% of city residents were of Cuban origin, and other significant populations included Central American, South American, and West Indian or Afro-Caribbean American origins. The non-Hispanic white population has been growing in the 21st century, making up 14.0% of the population by 2020. The city also has a small Asian population, accounting for 1.0% of the population in 2010. Christianity is the most practiced religion in Miami, followed by Judaism, Islam, Buddhism, Hinduism, and other religions. As of 2022, there were 3,440 homeless people in Miami-Dade County, with 591 unsheltered homeless people within the city limits of Miami.
Ran task: join. Observation: None
\> Thought: Miami and Chicago are both diverse cities with significant Hispanic populations. Miami has a larger Hispanic majority, with a significant Cuban population. Chicago, on the other hand, has a more evenly distributed demographic, with non-Hispanic Whites being the largest group, followed closely by Blacks and Hispanics. Both cities have a significant Christian population, but Chicago also has a sizable non-Christian population. In terms of economic demographics, Chicago has a higher median income and a higher poverty rate than Miami.
\> Answer: Miami and Chicago are both diverse cities with significant Hispanic populations. Miami has a larger Hispanic majority, with a significant Cuban population. Chicago, on the other hand, has a more evenly distributed demographic, with non-Hispanic Whites being the largest group, followed closely by Blacks and Hispanics. Both cities have a significant Christian population, but Chicago also has a sizable non-Christian population. In terms of economic demographics, Chicago has a higher median income and a higher poverty rate than Miami.
Miami and Chicago are both diverse cities with significant Hispanic populations. Miami has a larger Hispanic majority, with a significant Cuban population. Chicago, on the other hand, has a more evenly distributed demographic, with non-Hispanic Whites being the largest group, followed closely by Blacks and Hispanics. Both cities have a significant Christian population, but Chicago also has a sizable non-Christian population. In terms of economic demographics, Chicago has a higher median income and a higher poverty rate than Miami.

In \[ \]:

Copied!

response \= agent.chat(
    "Is the climate of Chicago or Seattle better during the wintertime?"
)
print(str(response))

response = agent.chat( "Is the climate of Chicago or Seattle better during the wintertime?" ) print(str(response))

\> Running step c5ce4ccc-80a7-453b-8ebc-b3aeedfdb338 for task 16e3d4ca-7cab-4d0c-bbfa-225a09680ccd.
> Step count: 0
\> Plan: 1. vector\_tool\_Chicago("climate during wintertime")
2. vector\_tool\_Seattle("climate during wintertime")
3. join()<END\_OF\_PLAN>
Ran task: vector\_tool\_Seattle. Observation: During wintertime, Seattle experiences cool, wet weather. Extreme cold temperatures, below about 15 °F or -9 °C, are rare due to the moderating influence of the adjacent Puget Sound, the greater Pacific Ocean, and Lake Washington. The city is often cloudy due to frequent storms and lows moving in from the Pacific Ocean, and it has many "rain days". However, the precipitation is often a light drizzle rather than heavy rainfall.
Ran task: vector\_tool\_Chicago. Observation: During wintertime, the city experiences relatively cold and snowy conditions. Blizzards can occur, as they did in winter 2011. The normal winter high from December through March is about 36 °F (2 °C). January and February are the coldest months. A polar vortex in January 2019 nearly broke the city's cold record of −27 °F (−33 °C), which was set on January 20, 1985. Measurable snowfall can continue through the first or second week of April. The city's proximity to Lake Michigan tends to keep the lakefront somewhat cooler in summer and less brutally cold in winter than inland parts of the city and suburbs away from the lake. Northeast winds from wintertime cyclones departing south of the region sometimes bring the city lake-effect snow.
Ran task: join. Observation: None
\> Thought: Comparing the two climates, Seattle seems to have a milder winter climate than Chicago.
\> Answer: Seattle
Seattle

Back to top

[Previous Language Agent Tree Search](https://docs.llamaindex.ai/en/stable/examples/agent/lats_agent/)[Next Simple Composable Memory](https://docs.llamaindex.ai/en/stable/examples/agent/memory/composable_memory/)

Hi, how can I help you?

🦙
