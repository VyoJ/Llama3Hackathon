Title: Usage Pattern - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/usage_pattern/

Markdown Content:
Usage Pattern - LlamaIndex


Getting Started[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/usage_pattern/#getting-started "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------

An agent is initialized from a set of Tools. Here's an example of instantiating a ReAct agent from a set of Tools.

```
from llama_index.core.tools import FunctionTool
from llama_index.llms.openai import OpenAI
from llama_index.core.agent import ReActAgent

# define sample Tool
def multiply(a: int, b: int) -> int:
"""Multiple two integers and returns the result integer"""
    return a * b

multiply_tool = FunctionTool.from_defaults(fn=multiply)

# initialize llm
llm = OpenAI(model="gpt-3.5-turbo-0613")

# initialize ReAct agent
agent = ReActAgent.from_tools([multiply_tool], llm=llm, verbose=True)
```

An agent supports both `chat` and `query` endpoints, inheriting from our `ChatEngine` and `QueryEngine` respectively.

Example usage:

```
agent.chat("What is 2123 * 215123")
```

To automatically pick the best agent depending on the LLM, you can use the `from_llm` method to generate an agent.

```
from llama_index.core.agent import AgentRunner

agent = AgentRunner.from_llm([multiply_tool], llm=llm, verbose=True)
```

Defining Tools[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/usage_pattern/#defining-tools "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------

### Query Engine Tools[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/usage_pattern/#query-engine-tools "Permanent link")

It is easy to wrap query engines as tools for an agent as well. Simply do the following:

```
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import QueryEngineTool

# NOTE: lyft_index and uber_index are both SimpleVectorIndex instances
lyft_engine = lyft_index.as_query_engine(similarity_top_k=3)
uber_engine = uber_index.as_query_engine(similarity_top_k=3)

query_engine_tools = [
    QueryEngineTool(
        query_engine=lyft_engine,
        metadata=ToolMetadata(
            name="lyft_10k",
            description="Provides information about Lyft financials for year 2021. "
            "Use a detailed plain text question as input to the tool.",
        ),
        return_direct=False,
    ),
    QueryEngineTool(
        query_engine=uber_engine,
        metadata=ToolMetadata(
            name="uber_10k",
            description="Provides information about Uber financials for year 2021. "
            "Use a detailed plain text question as input to the tool.",
        ),
        return_direct=False,
    ),
]

# initialize ReAct agent
agent = ReActAgent.from_tools(query_engine_tools, llm=llm, verbose=True)
```

### Use other agents as Tools[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/usage_pattern/#use-other-agents-as-tools "Permanent link")

A nifty feature of our agents is that since they inherit from `BaseQueryEngine`, you can easily define other agents as tools through our `QueryEngineTool`.

```
from llama_index.core.tools import QueryEngineTool

query_engine_tools = [
    QueryEngineTool(
        query_engine=sql_agent,
        metadata=ToolMetadata(
            name="sql_agent", description="Agent that can execute SQL queries."
        ),
    ),
    QueryEngineTool(
        query_engine=gmail_agent,
        metadata=ToolMetadata(
            name="gmail_agent",
            description="Tool that can send emails on Gmail.",
        ),
    ),
]

outer_agent = ReActAgent.from_tools(query_engine_tools, llm=llm, verbose=True)
```

Agent With Planning[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/usage_pattern/#agent-with-planning "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------

Breaking down an initial task into easier-to-digest sub-tasks is a powerful pattern.

LlamaIndex provides an agent planning module that does just this:

```
from llama_index.agent.openai import OpenAIAgentWorker
from llama_index.core.agent import (
    StructuredPlannerAgent,
    FunctionCallingAgentWorker,
)

worker = FunctionCallingAgentWorker.from_tools(tools, llm=llm)
agent = StructuredPlannerAgent(worker)
```

In general, this agent may take longer to respond compared to the basic `AgentRunner` class, but the outputs will often be more complete. Another tradeoff to consider is that planning often requires a very capable LLM (for context, `gpt-3.5-turbo` is sometimes flakey for planning, while `gpt-4-turbo` does much better.)

See more in the [complete guide](https://docs.llamaindex.ai/en/stable/examples/agent/structured_planner/)

Lower-Level API[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/usage_pattern/#lower-level-api "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------

The OpenAIAgent and ReActAgent are simple wrappers on top of an `AgentRunner` interacting with an `AgentWorker`.

_All_ agents can be defined this manner. For example for the OpenAIAgent:

```
from llama_index.core.agent import AgentRunner
from llama_index.agent.openai import OpenAIAgentWorker

# construct OpenAIAgent from tools
openai_step_engine = OpenAIAgentWorker.from_tools(tools, llm=llm, verbose=True)
agent = AgentRunner(openai_step_engine)
```

This is also the preferred format for custom agents.

Check out the [lower-level agent guide](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/agent_runner/) for more details.

Customizing your Agent[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/usage_pattern/#customizing-your-agent "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------

If you wish to define a custom agent, the easiest way to do so is to just define a stateful function and wrap it with a `FnAgentWorker`.

The `state` variable passed in and out of the function can contain anything you want it to, whether it's tools or arbitrary variables. It also contains task and output objects.

```
## This is an example showing a trivial function that multiplies an input number by 2 each time.
## Pass this into an agent
def multiply_agent_fn(state: dict) -> Tuple[Dict[str, Any], bool]:
"""Mock agent input function."""
    if "max_count" not in state:
        raise ValueError("max_count must be specified.")

    # __output__ is a special key indicating the final output of the agent
    # __task__ is a special key representing the Task object passed by the agent to the function.
    # `task.input` is the input string passed
    if "__output__" not in state:
        state["__output__"] = int(state["__task__"].input)
        state["count"] = 0
    else:
        state["__output__"] = state["__output__"] * 2
        state["count"] += 1

    is_done = state["count"] >= state["max_count"]

    # the output of this function should be a tuple of the state variable and is_done
    return state, is_done

from llama_index.core.agent import FnAgentWorker

agent = FnAgentWorker(
    fn=multiply_agent_fn, initial_state={"max_count": 5}
).as_agent()
agent.query("5")
```

Check out our [Custom Agent Notebook Guide](https://docs.llamaindex.ai/en/stable/examples/agent/custom_agent/) for more details.

Advanced Concepts (for `OpenAIAgent`, in beta)[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/usage_pattern/#advanced-concepts-for-openaiagent-in-beta "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can also use agents in more advanced settings. For instance, being able to retrieve tools from an index during query-time, and being able to perform query planning over an existing set of Tools.

These are largely implemented with our `OpenAIAgent` classes (which depend on the OpenAI Function API). Support for our more general `ReActAgent` is something we're actively investigating.

NOTE: these are largely still in beta. The abstractions may change and become more general over time.

### Function Retrieval Agents[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/usage_pattern/#function-retrieval-agents "Permanent link")

If the set of Tools is very large, you can create an `ObjectIndex` to index the tools, and then pass in an `ObjectRetriever` to the agent during query-time, to first dynamically retrieve the relevant tools before having the agent pick from the candidate tools.

We first build an `ObjectIndex` over an existing set of Tools.

```
# define an "object" index over these tools
from llama_index.core import VectorStoreIndex
from llama_index.core.objects import ObjectIndex

obj_index = ObjectIndex.from_objects(
    all_tools,
    index_cls=VectorStoreIndex,
)
```

We then define our `OpenAIAgent`:

```
from llama_index.agent.openai import OpenAIAgent

agent = OpenAIAgent.from_tools(
    tool_retriever=obj_index.as_retriever(similarity_top_k=2), verbose=True
)
```

You can find more details on the object index in the [full guide](https://docs.llamaindex.ai/en/stable/examples/objects/object_index/).

### Context Retrieval Agents[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/usage_pattern/#context-retrieval-agents "Permanent link")

Our context-augmented OpenAI Agent will always perform retrieval before calling any tools.

This helps to provide additional context that can help the agent better pick Tools, versus just trying to make a decision without any context.

```
from llama_index.core import Document
from llama_index.agent.openai_legacy import ContextRetrieverOpenAIAgent

# toy index - stores a list of Abbreviations
texts = [
    "Abbreviation: X = Revenue",
    "Abbreviation: YZ = Risk Factors",
    "Abbreviation: Z = Costs",
]
docs = [Document(text=t) for t in texts]
context_index = VectorStoreIndex.from_documents(docs)

# add context agent
context_agent = ContextRetrieverOpenAIAgent.from_tools_and_retriever(
    query_engine_tools,
    context_index.as_retriever(similarity_top_k=1),
    verbose=True,
)
response = context_agent.chat("What is the YZ of March 2022?")
```

### Query Planning[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/usage_pattern/#query-planning "Permanent link")

OpenAI Function Agents can be capable of advanced query planning. The trick is to provide the agent with a `QueryPlanTool` - if the agent calls the QueryPlanTool, it is forced to infer a full Pydantic schema representing a query plan over a set of subtools.

```
# define query plan tool
from llama_index.core.tools import QueryPlanTool
from llama_index.core import get_response_synthesizer

response_synthesizer = get_response_synthesizer(
    service_context=service_context
)
query_plan_tool = QueryPlanTool.from_defaults(
    query_engine_tools=[query_tool_sept, query_tool_june, query_tool_march],
    response_synthesizer=response_synthesizer,
)

# initialize agent
agent = OpenAIAgent.from_tools(
    [query_plan_tool],
    max_function_calls=10,
    llm=OpenAI(temperature=0, model="gpt-4-0613"),
    verbose=True,
)

# should output a query plan to call march, june, and september tools
response = agent.query(
    "Analyze Uber revenue growth in March, June, and September"
)
```

Back to top

[Previous Agents](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/)[Next Lower-Level Agent API](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/agent_runner/)
