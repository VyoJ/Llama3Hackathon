Title: Building a Custom Agent - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/custom_agent/

Markdown Content:
Building a Custom Agent - LlamaIndex


In this cookbook we show you how to build a custom agent using LlamaIndex.

1.  The easiest way to build a custom agent is to simply define a stateful function and plug it into `FnAgentWorker`.
2.  \[Optional\] Another approach that allows you to peek into our agent abstractions a bit more is to subclass `CustomSimpleAgentWorker` and implement a few required functions. You have complete flexibility in defining the agent step-wise logic.

This lets you add arbitrarily complex reasoning logic on top of your RAG pipeline.

We show you how to build a simple agent that adds a retry layer on top of a RouterQueryEngine, allowing it to retry queries until the task is complete. We build this on top of both a SQL tool and a vector index query tool. Even if the tool makes an error or only answers part of the question, the agent can continue retrying the question until the task is complete.

**NOTE:** Any Text-to-SQL application should be aware that executing arbitrary SQL queries can be a security risk. It is recommended to take precautions as needed, such as using restricted roles, read-only databases, sandboxing, etc.

In \[ \]:

Copied!

%pip install llama\-index\-readers\-wikipedia
%pip install llama\-index\-llms\-openai

%pip install llama-index-readers-wikipedia %pip install llama-index-llms-openai

Setup Data and Tools[¶](https://docs.llamaindex.ai/en/stable/examples/agent/custom_agent/#setup-data-and-tools)
---------------------------------------------------------------------------------------------------------------

We setup both a SQL Tool as well as vector index tools for each city.

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI

llm \= OpenAI(model\="gpt-4o")

from llama\_index.llms.openai import OpenAI llm = OpenAI(model="gpt-4o")

In \[ \]:

Copied!

from llama\_index.core.tools import QueryEngineTool

from llama\_index.core.tools import QueryEngineTool

### Setup SQL DB + Tool[¶](https://docs.llamaindex.ai/en/stable/examples/agent/custom_agent/#setup-sql-db-tool)

In \[ \]:

Copied!

from sqlalchemy import (
    create\_engine,
    MetaData,
    Table,
    Column,
    String,
    Integer,
    select,
    column,
)
from llama\_index.core import SQLDatabase

engine \= create\_engine("sqlite:///:memory:", future\=True)
metadata\_obj \= MetaData()
\# create city SQL table
table\_name \= "city\_stats"
city\_stats\_table \= Table(
    table\_name,
    metadata\_obj,
    Column("city\_name", String(16), primary\_key\=True),
    Column("population", Integer),
    Column("country", String(16), nullable\=False),
)

metadata\_obj.create\_all(engine)

from sqlalchemy import ( create\_engine, MetaData, Table, Column, String, Integer, select, column, ) from llama\_index.core import SQLDatabase engine = create\_engine("sqlite:///:memory:", future=True) metadata\_obj = MetaData() # create city SQL table table\_name = "city\_stats" city\_stats\_table = Table( table\_name, metadata\_obj, Column("city\_name", String(16), primary\_key=True), Column("population", Integer), Column("country", String(16), nullable=False), ) metadata\_obj.create\_all(engine)

In \[ \]:

Copied!

from sqlalchemy import insert

rows \= \[
    {"city\_name": "Toronto", "population": 2930000, "country": "Canada"},
    {"city\_name": "Tokyo", "population": 13960000, "country": "Japan"},
    {"city\_name": "Berlin", "population": 3645000, "country": "Germany"},
\]
for row in rows:
    stmt \= insert(city\_stats\_table).values(\*\*row)
    with engine.begin() as connection:
        cursor \= connection.execute(stmt)

from sqlalchemy import insert rows = \[ {"city\_name": "Toronto", "population": 2930000, "country": "Canada"}, {"city\_name": "Tokyo", "population": 13960000, "country": "Japan"}, {"city\_name": "Berlin", "population": 3645000, "country": "Germany"}, \] for row in rows: stmt = insert(city\_stats\_table).values(\*\*row) with engine.begin() as connection: cursor = connection.execute(stmt)

In \[ \]:

Copied!

from llama\_index.core.query\_engine import NLSQLTableQueryEngine

sql\_database \= SQLDatabase(engine, include\_tables\=\["city\_stats"\])
sql\_query\_engine \= NLSQLTableQueryEngine(
    sql\_database\=sql\_database, tables\=\["city\_stats"\], verbose\=True, llm\=llm
)
sql\_tool \= QueryEngineTool.from\_defaults(
    query\_engine\=sql\_query\_engine,
    description\=(
        "Useful for translating a natural language query into a SQL query over"
        " a table containing: city\_stats, containing the population/country of"
        " each city"
    ),
)

from llama\_index.core.query\_engine import NLSQLTableQueryEngine sql\_database = SQLDatabase(engine, include\_tables=\["city\_stats"\]) sql\_query\_engine = NLSQLTableQueryEngine( sql\_database=sql\_database, tables=\["city\_stats"\], verbose=True, llm=llm ) sql\_tool = QueryEngineTool.from\_defaults( query\_engine=sql\_query\_engine, description=( "Useful for translating a natural language query into a SQL query over" " a table containing: city\_stats, containing the population/country of" " each city" ), )

### Setup Vector Tools[¶](https://docs.llamaindex.ai/en/stable/examples/agent/custom_agent/#setup-vector-tools)

In \[ \]:

Copied!

from llama\_index.readers.wikipedia import WikipediaReader
from llama\_index.core import VectorStoreIndex

from llama\_index.readers.wikipedia import WikipediaReader from llama\_index.core import VectorStoreIndex

In \[ \]:

Copied!

cities \= \["Toronto", "Berlin", "Tokyo"\]
wiki\_docs \= WikipediaReader().load\_data(pages\=cities)

cities = \["Toronto", "Berlin", "Tokyo"\] wiki\_docs = WikipediaReader().load\_data(pages=cities)

In \[ \]:

Copied!

\# build a separate vector index per city
\# You could also choose to define a single vector index across all docs, and annotate each chunk by metadata
vector\_tools \= \[\]
for city, wiki\_doc in zip(cities, wiki\_docs):
    vector\_index \= VectorStoreIndex.from\_documents(\[wiki\_doc\])
    vector\_query\_engine \= vector\_index.as\_query\_engine()
    vector\_tool \= QueryEngineTool.from\_defaults(
        query\_engine\=vector\_query\_engine,
        description\=f"Useful for answering semantic questions about {city}",
    )
    vector\_tools.append(vector\_tool)

\# build a separate vector index per city # You could also choose to define a single vector index across all docs, and annotate each chunk by metadata vector\_tools = \[\] for city, wiki\_doc in zip(cities, wiki\_docs): vector\_index = VectorStoreIndex.from\_documents(\[wiki\_doc\]) vector\_query\_engine = vector\_index.as\_query\_engine() vector\_tool = QueryEngineTool.from\_defaults( query\_engine=vector\_query\_engine, description=f"Useful for answering semantic questions about {city}", ) vector\_tools.append(vector\_tool)

Setup the Custom Agent[¶](https://docs.llamaindex.ai/en/stable/examples/agent/custom_agent/#setup-the-custom-agent)
-------------------------------------------------------------------------------------------------------------------

Here we setup the custom agent. There are two ways to setup a custom agent.

In the first approach, you just define a custom function, whereas in the second approach, you learn a bit more about using some of the low-level agent components that LlamaIndex has to offer, giving you a more structured approach to handle validation, run things step-wise, and modify the output.

### Basic Setup[¶](https://docs.llamaindex.ai/en/stable/examples/agent/custom_agent/#basic-setup)

Here we define some common functions used for both implementations.

In \[ \]:

Copied!

from typing import Dict, Any, List, Tuple, Optional
from llama\_index.core.tools import QueryEngineTool
from llama\_index.core.program import FunctionCallingProgram
from llama\_index.core.query\_engine import RouterQueryEngine
from llama\_index.core import ChatPromptTemplate
from llama\_index.core.selectors import PydanticSingleSelector
from llama\_index.core.bridge.pydantic import Field, BaseModel

from typing import Dict, Any, List, Tuple, Optional from llama\_index.core.tools import QueryEngineTool from llama\_index.core.program import FunctionCallingProgram from llama\_index.core.query\_engine import RouterQueryEngine from llama\_index.core import ChatPromptTemplate from llama\_index.core.selectors import PydanticSingleSelector from llama\_index.core.bridge.pydantic import Field, BaseModel

Here we define some helper variables and methods. E.g. the prompt template to use to detect errors as well as the response format in Pydantic.

In \[ \]:

Copied!

from llama\_index.core.llms import ChatMessage, MessageRole

DEFAULT\_PROMPT\_STR \= """
Given previous question/response pairs, please determine if an error has occurred in the response, and suggest \\
    a modified question that will not trigger the error.

Examples of modified questions:
\- The question itself is modified to elicit a non-erroneous response
\- The question is augmented with context that will help the downstream system better answer the question.
\- The question is augmented with examples of negative responses, or other negative questions.

An error means that either an exception has triggered, or the response is completely irrelevant to the question.

Please return the evaluation of the response in the following JSON format.

"""

def get\_chat\_prompt\_template(
    system\_prompt: str, current\_reasoning: Tuple\[str, str\]
) \-> ChatPromptTemplate:
    system\_msg \= ChatMessage(role\=MessageRole.SYSTEM, content\=system\_prompt)
    messages \= \[system\_msg\]
    for raw\_msg in current\_reasoning:
        if raw\_msg\[0\] \ "user": messages.append( ChatMessage(role=MessageRole.USER, content=raw\_msg\[1\]) ) else: messages.append( ChatMessage(role=MessageRole.ASSISTANT, content=raw\_msg\[1\]) ) return ChatPromptTemplate(message\_templates=messages) class ResponseEval(BaseModel): """Evaluation of whether the response has an error.""" has\_error: bool = Field( ..., description="Whether the response has an error." ) new\_question: str = Field(..., description="The suggested new question.") explanation: str = Field( ..., description=( "The explanation for the error as well as for the new question." "Can include the direct stack trace as well." ), )

### Define Agent State Function[¶](https://docs.llamaindex.ai/en/stable/examples/agent/custom_agent/#define-agent-state-function)

Here we define a simple Python function that modifies the `state` variable and executes a single step. It returns a Tuple of the state dictionary and whether or not the agent has completed execution.

We wrap it with a `FnAgentWorker` that can give us an agent that can run this function multiple steps.

**Notes**:

*   The state dictionary passed to the Python function can access a special `__task__` variable that the `FnAgentWorker` injects during execution, representing the task object maintained by the agent throughout execution.
*   The output of the agent is defined by the `__output__` variable in the state dictionary. When `is_done` is True, make sure `__output__` is defined as well.
*   You can customize the key names of both the input and output variables through customizing `task_input_key` and `output_key` in the `FnAgentWorker`.
*   You can also inject any variables you want during initialization through the `initial_state` parameter in the `FnAgentWorker` initialization.

In \[ \]:

Copied!

from llama\_index.core.bridge.pydantic import PrivateAttr

def retry\_agent\_fn(state: Dict\[str, Any\]) \-> Tuple\[Dict\[str, Any\], bool\]:
    """Retry agent.

    Runs a single step.

    Returns:
        Tuple of (agent\_response, is\_done)

    """
    task, router\_query\_engine \= state\["\_\_task\_\_"\], state\["router\_query\_engine"\]
    llm, prompt\_str \= state\["llm"\], state\["prompt\_str"\]
    verbose \= state.get("verbose", False)

    if "new\_input" not in state:
        new\_input \= task.input
    else:
        new\_input \= state\["new\_input"\]

    \# first run router query engine
    response \= router\_query\_engine.query(new\_input)

    \# append to current reasoning
    state\["current\_reasoning"\].extend(
        \[("user", new\_input), ("assistant", str(response))\]
    )

    \# Then, check for errors
    \# dynamically create pydantic program for structured output extraction based on template
    chat\_prompt\_tmpl \= get\_chat\_prompt\_template(
        prompt\_str, state\["current\_reasoning"\]
    )
    llm\_program \= FunctionCallingProgram.from\_defaults(
        output\_cls\=ResponseEval,
        prompt\=chat\_prompt\_tmpl,
        llm\=llm,
    )
    \# run program, look at the result
    response\_eval \= llm\_program(
        query\_str\=new\_input, response\_str\=str(response)
    )
    if not response\_eval.has\_error:
        is\_done \= True
    else:
        is\_done \= False
    state\["new\_input"\] \= response\_eval.new\_question

    if verbose:
        print(f"> Question: {new\_input}")
        print(f"> Response: {response}")
        print(f"> Response eval: {response\_eval.dict()}")

    \# set output
    state\["\_\_output\_\_"\] \= str(response)

    \# return response
    return state, is\_done

from llama\_index.core.bridge.pydantic import PrivateAttr def retry\_agent\_fn(state: Dict\[str, Any\]) -> Tuple\[Dict\[str, Any\], bool\]: """Retry agent. Runs a single step. Returns: Tuple of (agent\_response, is\_done) """ task, router\_query\_engine = state\["\_\_task\_\_"\], state\["router\_query\_engine"\] llm, prompt\_str = state\["llm"\], state\["prompt\_str"\] verbose = state.get("verbose", False) if "new\_input" not in state: new\_input = task.input else: new\_input = state\["new\_input"\] # first run router query engine response = router\_query\_engine.query(new\_input) # append to current reasoning state\["current\_reasoning"\].extend( \[("user", new\_input), ("assistant", str(response))\] ) # Then, check for errors # dynamically create pydantic program for structured output extraction based on template chat\_prompt\_tmpl = get\_chat\_prompt\_template( prompt\_str, state\["current\_reasoning"\] ) llm\_program = FunctionCallingProgram.from\_defaults( output\_cls=ResponseEval, prompt=chat\_prompt\_tmpl, llm=llm, ) # run program, look at the result response\_eval = llm\_program( query\_str=new\_input, response\_str=str(response) ) if not response\_eval.has\_error: is\_done = True else: is\_done = False state\["new\_input"\] = response\_eval.new\_question if verbose: print(f"> Question: {new\_input}") print(f"> Response: {response}") print(f"> Response eval: {response\_eval.dict()}") # set output state\["\_\_output\_\_"\] = str(response) # return response return state, is\_done

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI
from llama\_index.core.agent import FnAgentWorker

llm \= OpenAI(model\="gpt-4o")
router\_query\_engine \= RouterQueryEngine(
    selector\=PydanticSingleSelector.from\_defaults(llm\=llm),
    query\_engine\_tools\=\[sql\_tool\] + vector\_tools,
    verbose\=True,
)
agent \= FnAgentWorker(
    fn\=retry\_agent\_fn,
    initial\_state\={
        "prompt\_str": DEFAULT\_PROMPT\_STR,
        "llm": llm,
        "router\_query\_engine": router\_query\_engine,
        "current\_reasoning": \[\],
        "verbose": True,
    },
).as\_agent()

from llama\_index.llms.openai import OpenAI from llama\_index.core.agent import FnAgentWorker llm = OpenAI(model="gpt-4o") router\_query\_engine = RouterQueryEngine( selector=PydanticSingleSelector.from\_defaults(llm=llm), query\_engine\_tools=\[sql\_tool\] + vector\_tools, verbose=True, ) agent = FnAgentWorker( fn=retry\_agent\_fn, initial\_state={ "prompt\_str": DEFAULT\_PROMPT\_STR, "llm": llm, "router\_query\_engine": router\_query\_engine, "current\_reasoning": \[\], "verbose": True, }, ).as\_agent()

Try Out Some Queries[¶](https://docs.llamaindex.ai/en/stable/examples/agent/custom_agent/#try-out-some-queries)
---------------------------------------------------------------------------------------------------------------

Now that we've defined the agent, you can try out some queries.

In \[ \]:

Copied!

response \= agent.chat("Which countries are each city from?")
print(str(response))

response = agent.chat("Which countries are each city from?") print(str(response))

Selecting query engine 0: The question asks for the countries of each city, which requires translating a natural language query into a SQL query over a table containing city statistics, including population and country information..
\> Question: Which countries are each city from?
> Response: Here are the countries for each city:

- Toronto is in Canada.
- Tokyo is in Japan.
- Berlin is in Germany.
> Response eval: {'has\_error': True, 'new\_question': 'Can you provide the countries for the following cities: Toronto, Tokyo, and Berlin?', 'explanation': 'The original question is too vague and does not specify which cities need to be identified. The response assumes a set of cities without confirmation. By specifying the cities in the question, the response can be more accurate and relevant.'}
Selecting query engine 0: The question requires translating a natural language query into a SQL query over a table containing city statistics, including the population and country of each city..
\> Question: Can you provide the countries for the following cities: Toronto, Tokyo, and Berlin?
> Response: Sure! Here are the countries for the given cities:

- Toronto is in Canada.
- Tokyo is in Japan.
- Berlin is in Germany.
> Response eval: {'has\_error': False, 'new\_question': 'Can you provide the countries for the following cities: Toronto, Tokyo, and Berlin?', 'explanation': 'The response correctly identifies the countries for the given cities: Toronto (Canada), Tokyo (Japan), and Berlin (Germany). No error is present in the response.'}
Sure! Here are the countries for the given cities:

- Toronto is in Canada.
- Tokyo is in Japan.
- Berlin is in Germany.

In \[ \]:

Copied!

response \= agent.chat(
    "What is the city in Canada, and what are the top modes of transport for that city?"
)
print(str(response))

response = agent.chat( "What is the city in Canada, and what are the top modes of transport for that city?" ) print(str(response))

Selecting query engine 1: The question asks about a city in Canada, and Toronto is a city in Canada. Therefore, the choice that is useful for answering semantic questions about Toronto is the most relevant..
\> Question: What is the city in Canada, and what are the top modes of transport for that city?
> Response: The city in Canada is Toronto. The top modes of transport for Toronto are the Toronto subway system, buses, streetcars, and an extensive network of bicycle lanes and multi-use trails and paths.
> Response eval: {'has\_error': True, 'new\_question': 'What are the top modes of transport in Toronto, Canada?', 'explanation': 'The original question is ambiguous and could refer to any city in Canada. The response incorrectly assumes the city is Toronto without any context. The modified question specifies Toronto directly to avoid ambiguity.'}
Selecting query engine 1: The question is about semantic information specific to Toronto, so the choice that is useful for answering semantic questions about Toronto is the most relevant..
\> Question: What are the top modes of transport in Toronto, Canada?
> Response: The top modes of transport in Toronto, Canada are the public transportation system operated by the Toronto Transit Commission (TTC), which includes the subway system, buses, and streetcars, as well as the regional rail and bus transit system operated by GO Transit. Additionally, Toronto is served by major highways, an extensive network of bicycle lanes, and two airports - Toronto Pearson International Airport and Billy Bishop Toronto City Airport.
> Response eval: {'has\_error': False, 'new\_question': 'What are the top modes of transport in Toronto, Canada?', 'explanation': 'The response correctly identifies the top modes of transport in Toronto, Canada, including the public transportation system operated by the TTC, GO Transit, major highways, bicycle lanes, and airports.'}
The top modes of transport in Toronto, Canada are the public transportation system operated by the Toronto Transit Commission (TTC), which includes the subway system, buses, and streetcars, as well as the regional rail and bus transit system operated by GO Transit. Additionally, Toronto is served by major highways, an extensive network of bicycle lanes, and two airports - Toronto Pearson International Airport and Billy Bishop Toronto City Airport.

In \[ \]:

Copied!

response \= sql\_query\_engine.query(
    "What are the top modes of transporation fo the city with the lowest population?"
)

response = sql\_query\_engine.query( "What are the top modes of transporation fo the city with the lowest population?" )

In \[ \]:

Copied!

print(str(response.metadata\["sql\_query"\]))
print(str(response))

print(str(response.metadata\["sql\_query"\])) print(str(response))

SELECT mode\_of\_transportation, COUNT(\*) as num\_trips
FROM trip\_data
WHERE city\_name = (SELECT city\_name FROM city\_stats ORDER BY population ASC LIMIT 1)
GROUP BY mode\_of\_transportation
ORDER BY num\_trips DESC
LIMIT 3;
It seems there was an error in the SQL query provided. To find the top modes of transportation for the city with the lowest population, you would need to first identify the city with the lowest population from the city\_stats table, and then query the trip\_data table for the mode of transportation used in that city. Once you have the city name, you can then count the number of trips for each mode of transportation in that city to determine the top modes of transportation.

In \[ \]:

Copied!

response \= agent.chat("What are the sports teams of each city in Asia?")
print(str(response))

response = agent.chat("What are the sports teams of each city in Asia?") print(str(response))

Selecting query engine 3: Tokyo is a city in Asia and is likely to have information about sports teams in that region..
\> Question: What are the sports teams of each city in Asia?
> Response: Tokyo is home to two professional baseball clubs, the Yomiuri Giants and Tokyo Yakult Swallows, as well as soccer clubs F.C. Tokyo, Tokyo Verdy 1969, and FC Machida Zelvia. Rugby Union teams in Tokyo include Black Rams Tokyo, Tokyo Sungoliath, and Toshiba Brave Lupus Tokyo. Additionally, basketball clubs in Tokyo include the Hitachi SunRockers, Toyota Alvark Tokyo, and Tokyo Excellence.
> Response eval: {'has\_error': True, 'new\_question': 'What are some sports teams in Tokyo, Japan?', 'explanation': 'The original question was too broad, as there are many cities in Asia with multiple sports teams. The response only provided information about sports teams in Tokyo, Japan. The new question narrows the scope to a specific city in Asia.'}
Selecting query engine 3: The choice (4) is the most relevant as it is useful for answering semantic questions about Tokyo, which includes providing information about sports teams in Tokyo, Japan..
\> Question: What are some sports teams in Tokyo, Japan?
> Response: Some sports teams in Tokyo, Japan include the Yomiuri Giants and Tokyo Yakult Swallows in baseball, F.C. Tokyo and Tokyo Verdy 1969 in soccer, FC Machida Zelvia in soccer, Black Rams Tokyo, Tokyo Sungoliath, and Toshiba Brave Lupus Tokyo in Rugby Union, Hitachi SunRockers, Toyota Alvark Tokyo, and Tokyo Excellence in basketball.
> Response eval: {'has\_error': False, 'new\_question': '', 'explanation': ''}
Some sports teams in Tokyo, Japan include the Yomiuri Giants and Tokyo Yakult Swallows in baseball, F.C. Tokyo and Tokyo Verdy 1969 in soccer, FC Machida Zelvia in soccer, Black Rams Tokyo, Tokyo Sungoliath, and Toshiba Brave Lupus Tokyo in Rugby Union, Hitachi SunRockers, Toyota Alvark Tokyo, and Tokyo Excellence in basketball.

\[Optional\] Build a Custom Agent through Subclassing[¶](https://docs.llamaindex.ai/en/stable/examples/agent/custom_agent/#optional-build-a-custom-agent-through-subclassing)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you'd like, you can also choose to build a custom agent through subclassing the `CustomSimpleAgentWorker`. This is if you want to more heavily customize the mechanisms of our agent interfaces, such as the Task and AgentChatResponse objects and step-wise execution.

**NOTE**: You probably don't need to read this section for most custom agent flows.

### Refresher[¶](https://docs.llamaindex.ai/en/stable/examples/agent/custom_agent/#refresher)

An agent in LlamaIndex consists of both an agent runner + agent worker. An agent runner is an orchestrator that stores state like memory, whereas an agent worker controls the step-wise execution of a Task. Agent runners include sequential, parallel execution. More details can be found in our [lower level API guide](https://docs.llamaindex.ai/en/latest/module_guides/deploying/agents/agent_runner.html).

Most core agent logic (e.g. ReAct, function calling loops), can be executed in the agent worker. Therefore we've made it easy to subclass an agent worker, letting you plug it into any agent runner.

### Creating a Custom Agent Worker Subclass[¶](https://docs.llamaindex.ai/en/stable/examples/agent/custom_agent/#creating-a-custom-agent-worker-subclass)

As mentioned above we subclass `CustomSimpleAgentWorker`. This is a class that already sets up some scaffolding for you. This includes being able to take in tools, callbacks, LLM, and also ensures that the state/steps are properly formatted. In the meantime you mostly have to implement the following functions:

*   `_initialize_state`
*   `_run_step`
*   `_finalize_task`

Some additional notes:

*   You can implement `_arun_step` as well if you want to support async chat in the agent.
*   You can choose to override `__init__` as long as you pass all remaining args, kwargs to `super()`
*   `CustomSimpleAgentWorker` is implemented as a Pydantic `BaseModel` meaning that you can define your own custom properties as well.

Here are the full set of base properties on each `CustomSimpleAgentWorker` (that you need to/can pass in when constructing your custom agent):

*   `tools: Sequence[BaseTool]`
*   `tool_retriever: Optional[ObjectRetriever[BaseTool]]`
*   `llm: LLM`
*   `callback_manager: CallbackManager`
*   `verbose: bool`

Note that `tools` and `tool_retriever` are mutually exclusive, you can only pass in one or the either (e.g. define a static list of tools or define a callable function that returns relevant tools given a user message). You can call `get_tools(message: str)` to return relevant tools given a message.

All of these properties are accessible via `self` when defining your custom agent.

In \[ \]:

Copied!

from llama\_index.core.agent import (
    CustomSimpleAgentWorker,
    Task,
    AgentChatResponse,
)
from typing import Dict, Any, List, Tuple, Optional
from llama\_index.core.tools import BaseTool, QueryEngineTool
from llama\_index.core.program import LLMTextCompletionProgram
from llama\_index.core.output\_parsers import PydanticOutputParser
from llama\_index.core.query\_engine import RouterQueryEngine
from llama\_index.core import ChatPromptTemplate, PromptTemplate
from llama\_index.core.selectors import PydanticSingleSelector
from llama\_index.core.bridge.pydantic import Field, BaseModel

from llama\_index.core.agent import ( CustomSimpleAgentWorker, Task, AgentChatResponse, ) from typing import Dict, Any, List, Tuple, Optional from llama\_index.core.tools import BaseTool, QueryEngineTool from llama\_index.core.program import LLMTextCompletionProgram from llama\_index.core.output\_parsers import PydanticOutputParser from llama\_index.core.query\_engine import RouterQueryEngine from llama\_index.core import ChatPromptTemplate, PromptTemplate from llama\_index.core.selectors import PydanticSingleSelector from llama\_index.core.bridge.pydantic import Field, BaseModel

In \[ \]:

Copied!

from llama\_index.core.bridge.pydantic import PrivateAttr

class RetryAgentWorker(CustomSimpleAgentWorker):
    """Agent worker that adds a retry layer on top of a router.

    Continues iterating until there's no errors / task is done.

    """

    prompt\_str: str \= Field(default\=DEFAULT\_PROMPT\_STR)
    max\_iterations: int \= Field(default\=10)

    \_router\_query\_engine: RouterQueryEngine \= PrivateAttr()

    def \_\_init\_\_(self, tools: List\[BaseTool\], \*\*kwargs: Any) \-> None:
        """Init params."""
        \# validate that all tools are query engine tools
        for tool in tools:
            if not isinstance(tool, QueryEngineTool):
                raise ValueError(
                    f"Tool {tool.metadata.name} is not a query engine tool."
                )
        self.\_router\_query\_engine \= RouterQueryEngine(
            selector\=PydanticSingleSelector.from\_defaults(),
            query\_engine\_tools\=tools,
            verbose\=kwargs.get("verbose", False),
        )
        super().\_\_init\_\_(
            tools\=tools,
            \*\*kwargs,
        )

    def \_initialize\_state(self, task: Task, \*\*kwargs: Any) \-> Dict\[str, Any\]:
        """Initialize state."""
        return {"count": 0, "current\_reasoning": \[\]}

    def \_run\_step(
        self, state: Dict\[str, Any\], task: Task, input: Optional\[str\] \= None
    ) \-> Tuple\[AgentChatResponse, bool\]:
        """Run step.

        Returns:
            Tuple of (agent\_response, is\_done)

        """
        if "new\_input" not in state:
            new\_input \= task.input
        else:
            new\_input \= state\["new\_input"\]

        \# first run router query engine
        response \= self.\_router\_query\_engine.query(new\_input)

        \# append to current reasoning
        state\["current\_reasoning"\].extend(
            \[("user", new\_input), ("assistant", str(response))\]
        )

        \# Then, check for errors
        \# dynamically create pydantic program for structured output extraction based on template
        chat\_prompt\_tmpl \= get\_chat\_prompt\_template(
            self.prompt\_str, state\["current\_reasoning"\]
        )
        llm\_program \= LLMTextCompletionProgram.from\_defaults(
            output\_parser\=PydanticOutputParser(output\_cls\=ResponseEval),
            prompt\=chat\_prompt\_tmpl,
            llm\=self.llm,
        )
        \# run program, look at the result
        response\_eval \= llm\_program(
            query\_str\=new\_input, response\_str\=str(response)
        )
        if not response\_eval.has\_error:
            is\_done \= True
        else:
            is\_done \= False
        state\["new\_input"\] \= response\_eval.new\_question

        if self.verbose:
            print(f"> Question: {new\_input}")
            print(f"> Response: {response}")
            print(f"> Response eval: {response\_eval.dict()}")

        \# return response
        return AgentChatResponse(response\=str(response)), is\_done

    def \_finalize\_task(self, state: Dict\[str, Any\], \*\*kwargs) \-> None:
        """Finalize task."""
        \# nothing to finalize here
        \# this is usually if you want to modify any sort of
        \# internal state beyond what is set in \`\_initialize\_state\`
        pass

from llama\_index.core.bridge.pydantic import PrivateAttr class RetryAgentWorker(CustomSimpleAgentWorker): """Agent worker that adds a retry layer on top of a router. Continues iterating until there's no errors / task is done. """ prompt\_str: str = Field(default=DEFAULT\_PROMPT\_STR) max\_iterations: int = Field(default=10) \_router\_query\_engine: RouterQueryEngine = PrivateAttr() def \_\_init\_\_(self, tools: List\[BaseTool\], \*\*kwargs: Any) -> None: """Init params.""" # validate that all tools are query engine tools for tool in tools: if not isinstance(tool, QueryEngineTool): raise ValueError( f"Tool {tool.metadata.name} is not a query engine tool." ) self.\_router\_query\_engine = RouterQueryEngine( selector=PydanticSingleSelector.from\_defaults(), query\_engine\_tools=tools, verbose=kwargs.get("verbose", False), ) super().\_\_init\_\_( tools=tools, \*\*kwargs, ) def \_initialize\_state(self, task: Task, \*\*kwargs: Any) -> Dict\[str, Any\]: """Initialize state.""" return {"count": 0, "current\_reasoning": \[\]} def \_run\_step( self, state: Dict\[str, Any\], task: Task, input: Optional\[str\] = None ) -> Tuple\[AgentChatResponse, bool\]: """Run step. Returns: Tuple of (agent\_response, is\_done) """ if "new\_input" not in state: new\_input = task.input else: new\_input = state\["new\_input"\] # first run router query engine response = self.\_router\_query\_engine.query(new\_input) # append to current reasoning state\["current\_reasoning"\].extend( \[("user", new\_input), ("assistant", str(response))\] ) # Then, check for errors # dynamically create pydantic program for structured output extraction based on template chat\_prompt\_tmpl = get\_chat\_prompt\_template( self.prompt\_str, state\["current\_reasoning"\] ) llm\_program = LLMTextCompletionProgram.from\_defaults( output\_parser=PydanticOutputParser(output\_cls=ResponseEval), prompt=chat\_prompt\_tmpl, llm=self.llm, ) # run program, look at the result response\_eval = llm\_program( query\_str=new\_input, response\_str=str(response) ) if not response\_eval.has\_error: is\_done = True else: is\_done = False state\["new\_input"\] = response\_eval.new\_question if self.verbose: print(f"> Question: {new\_input}") print(f"> Response: {response}") print(f"> Response eval: {response\_eval.dict()}") # return response return AgentChatResponse(response=str(response)), is\_done def \_finalize\_task(self, state: Dict\[str, Any\], \*\*kwargs) -> None: """Finalize task.""" # nothing to finalize here # this is usually if you want to modify any sort of # internal state beyond what is set in \`\_initialize\_state\` pass

Define Custom Agent[¶](https://docs.llamaindex.ai/en/stable/examples/agent/custom_agent/#define-custom-agent)
-------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI

from llama\_index.llms.openai import OpenAI

In \[ \]:

Copied!

llm \= OpenAI(model\="gpt-4")
callback\_manager \= llm.callback\_manager

query\_engine\_tools \= \[sql\_tool\] + vector\_tools
agent\_worker \= RetryAgentWorker.from\_tools(
    query\_engine\_tools,
    llm\=llm,
    verbose\=True,
    callback\_manager\=callback\_manager,
)
agent \= agent\_worker.as\_agent(callback\_manager\=callback\_manager)

llm = OpenAI(model="gpt-4") callback\_manager = llm.callback\_manager query\_engine\_tools = \[sql\_tool\] + vector\_tools agent\_worker = RetryAgentWorker.from\_tools( query\_engine\_tools, llm=llm, verbose=True, callback\_manager=callback\_manager, ) agent = agent\_worker.as\_agent(callback\_manager=callback\_manager)

Back to top

[Previous Chain-of-Abstraction LlamaPack](https://docs.llamaindex.ai/en/stable/examples/agent/coa_agent/)[Next DashScope Agent Tutorial](https://docs.llamaindex.ai/en/stable/examples/agent/dashscope_agent/)

Hi, how can I help you?

🦙
