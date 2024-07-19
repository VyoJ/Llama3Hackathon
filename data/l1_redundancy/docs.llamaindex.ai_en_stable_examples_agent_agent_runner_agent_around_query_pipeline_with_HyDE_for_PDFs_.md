Title: Building a Multi-PDF Agent using Query Pipelines and HyDE

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_around_query_pipeline_with_HyDE_for_PDFs/

Markdown Content:
Building a Multi-PDF Agent using Query Pipelines and HyDE - LlamaIndex


[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/docs/examples/agent/agent_runner/agent_around_query_pipeline_with_HyDE_for_PDFs.ipynb)

In this example, we show you how to build a multi-PDF agent that can reason across multiple tools, each one corresponding to a RAG pipeline with HyDE over a document.

Author: [https://github.com/DoganK01](https://github.com/DoganK01)

**Install Dependencies**[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_around_query_pipeline_with_HyDE_for_PDFs/#install-dependencies)
------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai
%pip install llama\-index
%pip install pyvis

%pip install llama-index-llms-openai %pip install llama-index %pip install pyvis

In \[ \]:

Copied!

%pip install arize\-phoenix\[evals\]

%pip install arize-phoenix\[evals\]

In \[ \]:

Copied!

%pip install llama\-index\-callbacks\-arize\-phoenix

%pip install llama-index-callbacks-arize-phoenix

**Download Data and Do Imports**[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_around_query_pipeline_with_HyDE_for_PDFs/#download-data-and-do-imports)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

!mkdir \-p 'data/10k/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' \-O 'data/10k/uber\_2021.pdf'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/lyft\_2021.pdf' \-O 'data/10k/lyft\_2021.pdf'

!mkdir -p 'data/10k/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' -O 'data/10k/uber\_2021.pdf' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/lyft\_2021.pdf' -O 'data/10k/lyft\_2021.pdf'

In \[ \]:

Copied!

import os

import os

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.core.indices.query.query\_transform import HyDEQueryTransform
from llama\_index.core.query\_engine import TransformQueryEngine
from IPython.display import Markdown, display

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout)) from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.core.indices.query.query\_transform import HyDEQueryTransform from llama\_index.core.query\_engine import TransformQueryEngine from IPython.display import Markdown, display

In \[ \]:

Copied!

from llama\_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
    load\_index\_from\_storage,
)

from llama\_index.core.tools import QueryEngineTool, ToolMetadata

\# define global callback setting
from llama\_index.core.settings import Settings
from llama\_index.core.callbacks import CallbackManager

from llama\_index.core import ( SimpleDirectoryReader, VectorStoreIndex, StorageContext, load\_index\_from\_storage, ) from llama\_index.core.tools import QueryEngineTool, ToolMetadata # define global callback setting from llama\_index.core.settings import Settings from llama\_index.core.callbacks import CallbackManager

**Setup Observability**[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_around_query_pipeline_with_HyDE_for_PDFs/#setup-observability)
----------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

callback\_manager \= CallbackManager()
Settings.callback\_manager \= callback\_manager

callback\_manager = CallbackManager() Settings.callback\_manager = callback\_manager

In \[ \]:

Copied!

\# setup Arize Phoenix for logging/observability
import phoenix as px
import llama\_index.core

px.launch\_app()
llama\_index.core.set\_global\_handler("arize\_phoenix")

\# setup Arize Phoenix for logging/observability import phoenix as px import llama\_index.core px.launch\_app() llama\_index.core.set\_global\_handler("arize\_phoenix")

In \[ \]:

Copied!

os.environ\["OPENAI\_API\_KEY"\] \= "sk-"

os.environ\["OPENAI\_API\_KEY"\] = "sk-"

**Setup Multi Doc HyDE Query Engine / Tool**[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_around_query_pipeline_with_HyDE_for_PDFs/#setup-multi-doc-hyde-query-engine-tool)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We setup HyDE Query engines and their tools for our multi doc system.

HyDE, short for Hypothetical Document Embeddings, is an innovative retrieval technique aimed at bolstering the efficiency of document retrieval processes. This method operates by crafting a hypothetical document tailored to an incoming query, which is subsequently embedded. The resulting embedding is leveraged to efficiently retrieve real documents exhibiting similarities to the hypothetical counterpart.

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

try: storage\_context = StorageContext.from\_defaults( persist\_dir="./storage/lyft" ) lyft\_index = load\_index\_from\_storage(storage\_context) storage\_context = StorageContext.from\_defaults( persist\_dir="./storage/uber" ) uber\_index = load\_index\_from\_storage(storage\_context) index\_loaded = True except: index\_loaded = False if not index\_loaded: # load data lyft\_docs = SimpleDirectoryReader( input\_files=\["./data/10k/lyft\_2021.pdf"\] ).load\_data() uber\_docs = SimpleDirectoryReader( input\_files=\["./data/10k/uber\_2021.pdf"\] ).load\_data() # build index lyft\_index = VectorStoreIndex.from\_documents(lyft\_docs) uber\_index = VectorStoreIndex.from\_documents(uber\_docs) # persist index lyft\_index.storage\_context.persist(persist\_dir="./storage/lyft") uber\_index.storage\_context.persist(persist\_dir="./storage/uber")

In \[ \]:

Copied!

lyft\_engine \= lyft\_index.as\_query\_engine(similarity\_top\_k\=3)
uber\_engine \= uber\_index.as\_query\_engine(similarity\_top\_k\=3)

hyde \= HyDEQueryTransform(include\_original\=True)
lyft\_hyde\_query\_engine \= TransformQueryEngine(lyft\_engine, hyde)
uber\_hyde\_query\_engine \= TransformQueryEngine(uber\_engine, hyde)

lyft\_engine = lyft\_index.as\_query\_engine(similarity\_top\_k=3) uber\_engine = uber\_index.as\_query\_engine(similarity\_top\_k=3) hyde = HyDEQueryTransform(include\_original=True) lyft\_hyde\_query\_engine = TransformQueryEngine(lyft\_engine, hyde) uber\_hyde\_query\_engine = TransformQueryEngine(uber\_engine, hyde)

In \[ \]:

Copied!

query\_engine\_tools \= \[
    QueryEngineTool(
        query\_engine\=lyft\_hyde\_query\_engine,
        metadata\=ToolMetadata(
            name\="lyft\_10k",
            description\=(
                "Provides information about Lyft financials for year 2021. "
                "Use a detailed plain text question as input to the tool."
            ),
        ),
    ),
    QueryEngineTool(
        query\_engine\=uber\_hyde\_query\_engine,
        metadata\=ToolMetadata(
            name\="uber\_10k",
            description\=(
                "Provides information about Uber financials for year 2021. "
                "Use a detailed plain text question as input to the tool."
            ),
        ),
    ),
\]

query\_engine\_tools = \[ QueryEngineTool( query\_engine=lyft\_hyde\_query\_engine, metadata=ToolMetadata( name="lyft\_10k", description=( "Provides information about Lyft financials for year 2021. " "Use a detailed plain text question as input to the tool." ), ), ), QueryEngineTool( query\_engine=uber\_hyde\_query\_engine, metadata=ToolMetadata( name="uber\_10k", description=( "Provides information about Uber financials for year 2021. " "Use a detailed plain text question as input to the tool." ), ), ), \]

**Setup ReAct Agent Pipeline**[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_around_query_pipeline_with_HyDE_for_PDFs/#setup-react-agent-pipeline)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### What is ReAct Agent[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_around_query_pipeline_with_HyDE_for_PDFs/#what-is-react-agent)

*   ReAct is a technique that enables LLMs to reason and perform task-specific actions. It combines chain-of-thought reasoning with action planning. It enables LLMs to create reasoning tracks and task-specific actions, strengthening the synergy between them using memory.
    
*   _The ReACT agent model refers to a framework that integrates the reasoning capabilities of LLMs with the ability to take actionable steps, creating a more sophisticated system that can understand and process information, evaluate situations, take appropriate actions, communicate responses, and track ongoing situations._
    

![Image 4: image.png](blob:https://docs.llamaindex.ai/ba60f7ee4665703c158d1f99193cad8f)

**Reasoning Loop** : The reasoning loop allows data agents to select and interact with tools in response to an input task.

**Memory**: LLMs, with access to memory, can store and retrieve data, ideal for apps tracking state or accessing multiple sources. Memory retains past interactions, enabling seamless reference to earlier conversation points. This integration involves allocating memory slots for relevant information and leveraging retrieval mechanisms during conversations. By recalling stored data, LLMs enhance contextual responses and integrate external sources, enriching user experiences.

Steps of the ReAct agent we will create[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_around_query_pipeline_with_HyDE_for_PDFs/#steps-of-the-react-agent-we-will-create)


Here we define the agent component that generates a ReAct prompt, and after the output is generated from the LLM, parses into a structured object.

After the input is received, LLM is called with the ReAct agent prompt.

`ReActChatFormatter` basically generates a fully formatted react prompt using ReAct Prompting (Chain-Of-Thought + Acting) method

In \[ \]:

Copied!

from llama\_index.core.agent import ReActChatFormatter
from llama\_index.core.query\_pipeline import InputComponent, Link
from llama\_index.core.llms import ChatMessage
from llama\_index.core.tools import BaseTool

\## define prompt function
def react\_prompt\_fn(
    task: Task, state: Dict\[str, Any\], input: str, tools: List\[BaseTool\]
) \-> List\[ChatMessage\]:
    \# Add input to reasoning
    chat\_formatter \= ReActChatFormatter()
    return chat\_formatter.format(
        tools,
        chat\_history\=task.memory.get() + state\["memory"\].get\_all(),
        current\_reasoning\=state\["current\_reasoning"\],
    )

react\_prompt\_component \= AgentFnComponent(
    fn\=react\_prompt\_fn, partial\_dict\={"tools": query\_engine\_tools}
)

from llama\_index.core.agent import ReActChatFormatter from llama\_index.core.query\_pipeline import InputComponent, Link from llama\_index.core.llms import ChatMessage from llama\_index.core.tools import BaseTool ## define prompt function def react\_prompt\_fn( task: Task, state: Dict\[str, Any\], input: str, tools: List\[BaseTool\] ) -> List\[ChatMessage\]: # Add input to reasoning chat\_formatter = ReActChatFormatter() return chat\_formatter.format( tools, chat\_history=task.memory.get() + state\["memory"\].get\_all(), current\_reasoning=state\["current\_reasoning"\], ) react\_prompt\_component = AgentFnComponent( fn=react\_prompt\_fn, partial\_dict={"tools": query\_engine\_tools} )

You can see the ReAct prompt here:

[https://github.com/run-llama/llama\_index/blob/6cd92affa5835aa21f823ff985a81f006c496bbd/llama-index-core/llama\_index/core/agent/react/prompts.py#L6](https://github.com/run-llama/llama_index/blob/6cd92affa5835aa21f823ff985a81f006c496bbd/llama-index-core/llama_index/core/agent/react/prompts.py#L6)

**Define Agent Output Parser + Tool Pipeline**[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_around_query_pipeline_with_HyDE_for_PDFs/#define-agent-output-parser-tool-pipeline)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Once the LLM gives an output, we have a decision tree:

1.  If an answer is given, then we’re done. Process the output
    
2.  If an action is given, we need to execute the specified tool with the specified args, and then process the output.
    

Tool calling can be done via the `ToolRunnerComponent` module. This is a simple wrapper module that takes in a list of tools, and can be “executed” with the specified tool name (every tool has a name) and tool action.

We implement this overall module `OutputAgentComponent` that subclasses `CustomAgentComponent`.

`perse_react_output_fn` function simply parses the ReAct prompt got from `react_prompt_fn` into the reasoning step.

In this case, the ReAct Agent choose whatever go with a tool or done with tools and simply gets the output that will be fit in chat response for agents (`AgentChatResponse`).

The `run_tool_fn` function simply runs a tool if it is selected.

Finally, the incoming output is edited in accordance with the Agent output format by applying the `process_agent_response_fn` function.

In \[ \]:

Copied!

from typing import Set, Optional
from llama\_index.core.agent.react.output\_parser import ReActOutputParser
from llama\_index.core.llms import ChatResponse
from llama\_index.core.agent.types import Task

def parse\_react\_output\_fn(
    task: Task, state: Dict\[str, Any\], chat\_response: ChatResponse
):
    """Parse ReAct output into a reasoning step."""
    output\_parser \= ReActOutputParser()
    reasoning\_step \= output\_parser.parse(chat\_response.message.content)
    return {"done": reasoning\_step.is\_done, "reasoning\_step": reasoning\_step}

parse\_react\_output \= AgentFnComponent(fn\=parse\_react\_output\_fn)

def run\_tool\_fn(
    task: Task, state: Dict\[str, Any\], reasoning\_step: ActionReasoningStep
):
    """Run tool and process tool output."""
    tool\_runner\_component \= ToolRunnerComponent(
        query\_engine\_tools, callback\_manager\=task.callback\_manager
    )
    tool\_output \= tool\_runner\_component.run\_component(
        tool\_name\=reasoning\_step.action,
        tool\_input\=reasoning\_step.action\_input,
    )
    observation\_step \= ObservationReasoningStep(
        observation\=str(tool\_output\["output"\])
    )
    state\["current\_reasoning"\].append(observation\_step)
    \# TODO: get output

    return {"response\_str": observation\_step.get\_content(), "is\_done": False}

run\_tool \= AgentFnComponent(fn\=run\_tool\_fn)

def process\_response\_fn(
    task: Task, state: Dict\[str, Any\], response\_step: ResponseReasoningStep
):
    """Process response."""
    state\["current\_reasoning"\].append(response\_step)
    response\_str \= response\_step.response
    \# Now that we're done with this step, put into memory
    state\["memory"\].put(ChatMessage(content\=task.input, role\=MessageRole.USER))
    state\["memory"\].put(
        ChatMessage(content\=response\_str, role\=MessageRole.ASSISTANT)
    )

    return {"response\_str": response\_str, "is\_done": True}

process\_response \= AgentFnComponent(fn\=process\_response\_fn)

def process\_agent\_response\_fn(
    task: Task, state: Dict\[str, Any\], response\_dict: dict
):
    """Process agent response."""
    return (
        AgentChatResponse(response\_dict\["response\_str"\]),
        response\_dict\["is\_done"\],
    )

process\_agent\_response \= AgentFnComponent(fn\=process\_agent\_response\_fn)

from typing import Set, Optional from llama\_index.core.agent.react.output\_parser import ReActOutputParser from llama\_index.core.llms import ChatResponse from llama\_index.core.agent.types import Task def parse\_react\_output\_fn( task: Task, state: Dict\[str, Any\], chat\_response: ChatResponse ): """Parse ReAct output into a reasoning step.""" output\_parser = ReActOutputParser() reasoning\_step = output\_parser.parse(chat\_response.message.content) return {"done": reasoning\_step.is\_done, "reasoning\_step": reasoning\_step} parse\_react\_output = AgentFnComponent(fn=parse\_react\_output\_fn) def run\_tool\_fn( task: Task, state: Dict\[str, Any\], reasoning\_step: ActionReasoningStep ): """Run tool and process tool output.""" tool\_runner\_component = ToolRunnerComponent( query\_engine\_tools, callback\_manager=task.callback\_manager ) tool\_output = tool\_runner\_component.run\_component( tool\_name=reasoning\_step.action, tool\_input=reasoning\_step.action\_input, ) observation\_step = ObservationReasoningStep( observation=str(tool\_output\["output"\]) ) state\["current\_reasoning"\].append(observation\_step) # TODO: get output return {"response\_str": observation\_step.get\_content(), "is\_done": False} run\_tool = AgentFnComponent(fn=run\_tool\_fn) def process\_response\_fn( task: Task, state: Dict\[str, Any\], response\_step: ResponseReasoningStep ): """Process response.""" state\["current\_reasoning"\].append(response\_step) response\_str = response\_step.response # Now that we're done with this step, put into memory state\["memory"\].put(ChatMessage(content=task.input, role=MessageRole.USER)) state\["memory"\].put( ChatMessage(content=response\_str, role=MessageRole.ASSISTANT) ) return {"response\_str": response\_str, "is\_done": True} process\_response = AgentFnComponent(fn=process\_response\_fn) def process\_agent\_response\_fn( task: Task, state: Dict\[str, Any\], response\_dict: dict ): """Process agent response.""" return ( AgentChatResponse(response\_dict\["response\_str"\]), response\_dict\["is\_done"\], ) process\_agent\_response = AgentFnComponent(fn=process\_agent\_response\_fn)

**Stitch together Agent Query Pipeline**[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_around_query_pipeline_with_HyDE_for_PDFs/#stitch-together-agent-query-pipeline)


We can now stitch together the top-level agent pipeline: agent\_input -> react\_prompt -> llm -> react\_output.

The last component is the if-else component that calls sub-components.

In \[ \]:

Copied!

from llama\_index.core.query\_pipeline import QueryPipeline as QP

qp \= QP(verbose\=True)

from llama\_index.core.query\_pipeline import QueryPipeline as QP qp = QP(verbose=True)

In \[ \]:

Copied!

from llama\_index.core.query\_pipeline import QueryPipeline as QP
from llama\_index.llms.openai import OpenAI

qp.add\_modules(
    {
        "agent\_input": agent\_input\_component,
        "react\_prompt": react\_prompt\_component,
        "llm": OpenAI(model\="gpt-4-1106-preview"),
        "react\_output\_parser": parse\_react\_output,
        "run\_tool": run\_tool,
        "process\_response": process\_response,
        "process\_agent\_response": process\_agent\_response,
    }
)

from llama\_index.core.query\_pipeline import QueryPipeline as QP from llama\_index.llms.openai import OpenAI qp.add\_modules( { "agent\_input": agent\_input\_component, "react\_prompt": react\_prompt\_component, "llm": OpenAI(model="gpt-4-1106-preview"), "react\_output\_parser": parse\_react\_output, "run\_tool": run\_tool, "process\_response": process\_response, "process\_agent\_response": process\_agent\_response, } )

In \[ \]:

Copied!

\# link input to react prompt to parsed out response (either tool action/input or observation)
qp.add\_chain(\["agent\_input", "react\_prompt", "llm", "react\_output\_parser"\])

\# add conditional link from react output to tool call (if not done)
qp.add\_link(
    "react\_output\_parser",
    "run\_tool",
    condition\_fn\=lambda x: not x\["done"\],
    input\_fn\=lambda x: x\["reasoning\_step"\],
)
\# add conditional link from react output to final response processing (if done)
qp.add\_link(
    "react\_output\_parser",
    "process\_response",
    condition\_fn\=lambda x: x\["done"\],
    input\_fn\=lambda x: x\["reasoning\_step"\],
)

\# whether response processing or tool output processing, add link to final agent response
qp.add\_link("process\_response", "process\_agent\_response")
qp.add\_link("run\_tool", "process\_agent\_response")

\# link input to react prompt to parsed out response (either tool action/input or observation) qp.add\_chain(\["agent\_input", "react\_prompt", "llm", "react\_output\_parser"\]) # add conditional link from react output to tool call (if not done) qp.add\_link( "react\_output\_parser", "run\_tool", condition\_fn=lambda x: not x\["done"\], input\_fn=lambda x: x\["reasoning\_step"\], ) # add conditional link from react output to final response processing (if done) qp.add\_link( "react\_output\_parser", "process\_response", condition\_fn=lambda x: x\["done"\], input\_fn=lambda x: x\["reasoning\_step"\], ) # whether response processing or tool output processing, add link to final agent response qp.add\_link("process\_response", "process\_agent\_response") qp.add\_link("run\_tool", "process\_agent\_response")

**Visualize Query Pipeline**[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_around_query_pipeline_with_HyDE_for_PDFs/#visualize-query-pipeline)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from pyvis.network import Network

net \= Network(notebook\=True, cdn\_resources\="in\_line", directed\=True)
net.from\_nx(qp.clean\_dag)
print(net)

from pyvis.network import Network net = Network(notebook=True, cdn\_resources="in\_line", directed=True) net.from\_nx(qp.clean\_dag) print(net)

{
    "Nodes": \[
        "agent\_input",
        "react\_prompt",
        "llm",
        "react\_output\_parser",
        "run\_tool",
        "process\_response",
        "process\_agent\_response"
    \],
    "Edges": \[
        {
            "src\_key": null,
            "dest\_key": null,
            "condition\_fn": null,
            "input\_fn": null,
            "width": 1,
            "from": "agent\_input",
            "to": "react\_prompt",
            "arrows": "to"
        },
        {
            "src\_key": null,
            "dest\_key": null,
            "condition\_fn": null,
            "input\_fn": null,
            "width": 1,
            "from": "react\_prompt",
            "to": "llm",
            "arrows": "to"
        },
        {
            "src\_key": null,
            "dest\_key": null,
            "condition\_fn": null,
            "input\_fn": null,
            "width": 1,
            "from": "llm",
            "to": "react\_output\_parser",
            "arrows": "to"
        },
        {
            "src\_key": null,
            "dest\_key": null,
            "width": 1,
            "from": "react\_output\_parser",
            "to": "run\_tool",
            "arrows": "to"
        },
        {
            "src\_key": null,
            "dest\_key": null,
            "width": 1,
            "from": "react\_output\_parser",
            "to": "process\_response",
            "arrows": "to"
        },
        {
            "src\_key": null,
            "dest\_key": null,
            "condition\_fn": null,
            "input\_fn": null,
            "width": 1,
            "from": "run\_tool",
            "to": "process\_agent\_response",
            "arrows": "to"
        },
        {
            "src\_key": null,
            "dest\_key": null,
            "condition\_fn": null,
            "input\_fn": null,
            "width": 1,
            "from": "process\_response",
            "to": "process\_agent\_response",
            "arrows": "to"
        }
    \],
    "Height": "600px",
    "Width": "100%",
    "Heading": ""
}

In \[ \]:

Copied!

\# Save the network as "agent\_dat.html"
net.write\_html("agent\_dag.html")

\# Save the network as "agent\_dat.html" net.write\_html("agent\_dag.html")

In \[ \]:

Copied!

from IPython.display import display, HTML

\# Read the contents of the HTML file
with open("agent\_dag.html", "r") as file:
    html\_content \= file.read()

\# Display the HTML content
display(HTML(html\_content))

from IPython.display import display, HTML # Read the contents of the HTML file with open("agent\_dag.html", "r") as file: html\_content = file.read() # Display the HTML content display(HTML(html\_content))

**Setup Agent Worker around our Query Engines**[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_around_query_pipeline_with_HyDE_for_PDFs/#setup-agent-worker-around-our-query-engines)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core.agent import QueryPipelineAgentWorker
from llama\_index.core.callbacks import CallbackManager

agent\_worker \= QueryPipelineAgentWorker(qp)
agent \= agent\_worker.as\_agent(
    callback\_manager\=CallbackManager(\[\]), verbose\=True
)

from llama\_index.core.agent import QueryPipelineAgentWorker from llama\_index.core.callbacks import CallbackManager agent\_worker = QueryPipelineAgentWorker(qp) agent = agent\_worker.as\_agent( callback\_manager=CallbackManager(\[\]), verbose=True )

**Run the Agent**[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_around_query_pipeline_with_HyDE_for_PDFs/#run-the-agent)
----------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

\# start task
task \= agent.create\_task(
    "What was Uber's Management's Report on Internal Control over Financial Reporting?"
)

\# start task task = agent.create\_task( "What was Uber's Management's Report on Internal Control over Financial Reporting?" )

In \[ \]:

Copied!

step\_output \= agent.run\_step(task.task\_id)

step\_output = agent.run\_step(task.task\_id)

\> Running step 26c623b9-0864-45d9-9f91-f893a4696727. Step input: What was Uber's Management's Report on Internal Control over Financial Reporting?
\> Running module agent\_input with input: 
state: {'sources': \[\], 'memory': ChatMemoryBuffer(token\_limit=3000, tokenizer\_fn=functools.partial(<bound method Encoding.encode of <Encoding 'cl100k\_base'>>, allowed\_special='all'), chat\_store=SimpleChatSto...
task: task\_id='aa7707d1-a35a-4d96-b2cc-ded765a3a3e2' input="What was Uber's Management's Report on Internal Control over Financial Reporting?" memory=ChatMemoryBuffer(token\_limit=3000, tokenizer\_fn=functool...

\> Running module react\_prompt with input: 
input: What was Uber's Management's Report on Internal Control over Financial Reporting?

\> Running module llm with input: 
messages: \[ChatMessage(role=<MessageRole.SYSTEM: 'system'>, content='\\nYou are designed to help with a variety of tasks, from answering questions     to providing summaries to other types of analyses.\\n\\n## Too...

\> Running module react\_output\_parser with input: 
chat\_response: assistant: Thought: I need to use the uber\_10k tool to find the specific section about Uber's Management's Report on Internal Control over Financial Reporting for the year 2021.
Action: uber\_10k
Actio...

\> Running module run\_tool with input: 
reasoning\_step: thought="I need to use the uber\_10k tool to find the specific section about Uber's Management's Report on Internal Control over Financial Reporting for the year 2021." action='uber\_10k' action\_input={...

\> Running module process\_agent\_response with input: 
response\_dict: {'response\_str': 'Observation: {\\'output\\': ToolOutput(content="Uber\\'s Management\\'s Report on Internal Control over Financial Reporting stated that they excluded The Drizly Group, Inc. and TupeloPar...

In \[ \]:

Copied!

print(step\_output)

print(step\_output)

Observation: {'output': ToolOutput(content="Uber's Management's Report on Internal Control over Financial Reporting stated that they excluded The Drizly Group, Inc. and TupeloParent, Inc. from their assessment of internal control over financial reporting as of December 31, 2021 due to their acquisition by the company during 2021. The report also mentioned that Drizly and TupeloParent were excluded from the audit of internal control over financial reporting.", tool\_name='uber\_10k', raw\_input={'input': "What was Uber's Management's Report on Internal Control over Financial Reporting?"}, raw\_output=Response(response="Uber's Management's Report on Internal Control over Financial Reporting stated that they excluded The Drizly Group, Inc. and TupeloParent, Inc. from their assessment of internal control over financial reporting as of December 31, 2021 due to their acquisition by the company during 2021. The report also mentioned that Drizly and TupeloParent were excluded from the audit of internal control over financial reporting.", source\_nodes=\[NodeWithScore(node=TextNode(id\_='931833d8-5d9e-4f37-bd0b-1ffeb58f0256', embedding=None, metadata={'page\_label': '73', 'file\_name': 'uber\_2021.pdf', 'file\_path': 'data/10k/uber\_2021.pdf', 'file\_type': 'application/pdf', 'file\_size': 1880483, 'creation\_date': '2024-03-12', 'last\_modified\_date': '2024-03-12'}, excluded\_embed\_metadata\_keys=\['file\_name', 'file\_type', 'file\_size', 'creation\_date', 'last\_modified\_date', 'last\_accessed\_date'\], excluded\_llm\_metadata\_keys=\['file\_name', 'file\_type', 'file\_size', 'creation\_date', 'last\_modified\_date', 'last\_accessed\_date'\], relationships={<NodeRelationship.SOURCE: '1'>: RelatedNodeInfo(node\_id='239d870b-d23e-4805-8761-5e83f826f10a', node\_type=<ObjectType.DOCUMENT: '4'>, metadata={'page\_label': '73', 'file\_name': 'uber\_2021.pdf', 'file\_path': 'data/10k/uber\_2021.pdf', 'file\_type': 'application/pdf', 'file\_size': 1880483, 'creation\_date': '2024-03-12', 'last\_modified\_date': '2024-03-12'}, hash='0037c6d1cdc56230c931100529a1d35ea0d556331ddae62b0b342c2403104e69'), <NodeRelationship.PREVIOUS: '2'>: RelatedNodeInfo(node\_id='733e2fd3-fded-4e9d-8698-a16782d23a57', node\_type=<ObjectType.TEXT: '1'>, metadata={'page\_label': '73', 'file\_name': 'uber\_2021.pdf', 'file\_path': 'data/10k/uber\_2021.pdf', 'file\_type': 'application/pdf', 'file\_size': 1880483, 'creation\_date': '2024-03-12', 'last\_modified\_date': '2024-03-12'}, hash='3c2f360445d5ff1069578c4a7ba2867bd32389a5ab93ecd5ee1c8998a7c1f5fa'), <NodeRelationship.NEXT: '3'>: RelatedNodeInfo(node\_id='4876454e-2f82-4460-937a-fe7398fb5974', node\_type=<ObjectType.TEXT: '1'>, metadata={}, hash='bb5f14b14770778aa72510551a86642ba81040186ee787609ae76877639d2590')}, text='Our audits also included evaluating the accounting principles used and significantestimates\\n made by management, as well as evaluating the overall presentation of the consolidated financial statements. Our audit of internal control over financialreporting\\n included  obtaining  an  understanding  of  internal  control  over  financial  reporting,  assessing  the  risk  that  a  material  weakness  exists,  and  testing  andevaluating\\n the design and operating effectiveness of internal control based on the assessed risk. Our audits also included performing such other procedures as weconsidered necessary in th\\ne circumstances. We believe that our audits provide a reasonable basis for our opinions.As\\n described in Management’s Report on Internal Control over Financial Reporting, management has excluded The Drizly Group, Inc. (“Drizly”) and TupeloParent, Inc. (“Transplace”) from its assessment of internal control over financial reporting as of December 3\\n1, 2021 because they were acquired by the Company inpurchase\\n business combinations during 2021. We have also excluded Drizly and Transplace from our audit of internal control over financial reporting. Drizly andTransplace\\n are wholly-owned subsidiaries whose total assets and total revenues excluded from management’s assessment and our audit of internal control overfinancial\\n reporting collectively represent approximately 3% and 4%, respectively, of the related consolidated financial statement amounts as of and for the yearended December 31, 2021.\\nDefinition and Limitations of Internal Control over Financial Repor\\ntingA\\n company’s internal control over financial reporting is a process designed to provide reasonable assurance regarding the reliability of financial reporting and thepreparation\\n of financial statements for external purposes in accordance with generally accepted accounting principles. A company’s internal control over financialreporting includes those policies and procedures that (i) pertain to the maintenance of records that, in reasonable detail, accurately an\\nd fairly reflect the transactionsand\\n dispositions  of  the  assets  of  the  company;  (ii)  provide  reasonable  assurance  that  transactions  are  recorded  as  necessary  to  permit  preparation  of  financialstatements in accordance with\\n generally accepted accounting principles, and that receipts and expenditures of the company are being made only in accordance withauthorizations of management\\n and directors of the company; and (iii) provide reasonable assurance regarding71', start\_char\_idx=3733, end\_char\_idx=6274, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.9047882048131767), NodeWithScore(node=TextNode(id\_='733e2fd3-fded-4e9d-8698-a16782d23a57', embedding=None, metadata={'page\_label': '73', 'file\_name': 'uber\_2021.pdf', 'file\_path': 'data/10k/uber\_2021.pdf', 'file\_type': 'application/pdf', 'file\_size': 1880483, 'creation\_date': '2024-03-12', 'last\_modified\_date': '2024-03-12'}, excluded\_embed\_metadata\_keys=\['file\_name', 'file\_type', 'file\_size', 'creation\_date', 'last\_modified\_date', 'last\_accessed\_date'\], excluded\_llm\_metadata\_keys=\['file\_name', 'file\_type', 'file\_size', 'creation\_date', 'last\_modified\_date', 'last\_accessed\_date'\], relationships={<NodeRelationship.SOURCE: '1'>: RelatedNodeInfo(node\_id='239d870b-d23e-4805-8761-5e83f826f10a', node\_type=<ObjectType.DOCUMENT: '4'>, metadata={'page\_label': '73', 'file\_name': 'uber\_2021.pdf', 'file\_path': 'data/10k/uber\_2021.pdf', 'file\_type': 'application/pdf', 'file\_size': 1880483, 'creation\_date': '2024-03-12', 'last\_modified\_date': '2024-03-12'}, hash='0037c6d1cdc56230c931100529a1d35ea0d556331ddae62b0b342c2403104e69'), <NodeRelationship.PREVIOUS: '2'>: RelatedNodeInfo(node\_id='5c1073c7-33f4-4f95-bb85-515619f4135a', node\_type=<ObjectType.TEXT: '1'>, metadata={'page\_label': '72', 'file\_name': 'uber\_2021.pdf', 'file\_path': 'data/10k/uber\_2021.pdf', 'file\_type': 'application/pdf', 'file\_size': 1880483, 'creation\_date': '2024-03-12', 'last\_modified\_date': '2024-03-12'}, hash='5e414926a8e5d3a1ad31529426a96d04ce0fd55f12624297c511c6fa00845bb3'), <NodeRelationship.NEXT: '3'>: RelatedNodeInfo(node\_id='931833d8-5d9e-4f37-bd0b-1ffeb58f0256', node\_type=<ObjectType.TEXT: '1'>, metadata={}, hash='87fae4857bb55d49c262875bb681de6578c8bf807af889f1cfdd6edc819c7ab2')}, text="Report of Independent Registered Public Accounting FirmTo the Board of Directors and Stockhold\\ners of Uber Technologies, Inc.Opinions on the Financial Statements and Internal Control over Financial Reporting\\nWe\\n have audited the accompanying consolidated balance sheets of Uber Technologies, Inc. and its subsidiaries (the “Company”) as of December 31, 2021 and2020,\\n and the related consolidated statements of operations, of comprehensive loss, of redeemable non-controlling interests and equity and of cash flows for eachof\\n the  three  years  in  the  period  ended  December  31,  2021,  including  the  related  notes  and  financial  statement  schedule  listed  in  the  accompanying  index(collectively\\n referred to as the “consolidated financial statements”). We also have audited the Company's internal control over financial reporting as of December31,\\n 2021, based on criteria established in Internal  Control - Integrated Framework (2013)  issued by the Committee of Sponsoring Organizations of the TreadwayCommission (COSO).\\nIn our\\n opinion, the consolidated financial statements referred to above present fairly, in all material respects, the financial position of the Company as of December31,\\n 2021 and 2020, and the results of its operations and its cash flows for each of the three years in the period ended December 31, 2021 in conformity withaccounting\\n principles generally accepted in the United States of America. Also in our opinion, the Company maintained, in all material respects, effective internalcontrol over financia\\nl reporting as of December 31, 2021, based on criteria established in Internal Control - Integrated Framework (2013) issued by the COSO.Changes in Accounting Principles\\nAs discussed in\\n Note 1 to the consolidated financial statements, the Company changed the manner in which it accounts for convertible instruments and contracts inan entity’s own equity in 2021 and the \\nmanner in which it accounts for leases in 2019.Basis for Opinions\\nThe\\n Company's management is responsible for these consolidated financial statements, for maintaining effective internal control over financial reporting, and forits\\n assessment of the effectiveness  of internal control over financial  reporting,  included in Management’s Report on Internal Control over Financial  Reportingappearing under Item\\n 9A. Our responsibility is to express opinions on the Company’s consolidated financial statements and on the Company's internal control overfinancial\\n reporting  based  on  our  audits.  We  are  a  public  accounting  firm  registered  with  the  Public  Company  Accounting  Oversight  Board  (United  States)(PCAOB)\\n and  are  required  to  be  independent  with  respect  to  the  Company  in  accordance  with  the  U.S.  federal  securities  laws  and  the  applicable  rules  andregulations of the Securi\\nties and Exchange Commission and the PCAOB.We\\n conducted  our  audits  in  accordance  with  the  standards  of  the  PCAOB.  Those  standards  require  that  we  plan  and  perform  the  audits  to  obtain  reasonableassurance\\n about  whether  the  consolidated  financial  statements  are  free  of  material  misstatement,  whether  due  to  error  or  fraud,  and  whether  effective  internalcontrol over financial reporti\\nng was maintained in all material respects.Our\\n audits  of  the  consolidated  financial  statements  included  performing  procedures  to  assess  the  risks  of  material  misstatement  of  the  consolidated  financialstatements,\\n whether due to error or fraud, and performing procedures that respond to those risks. Such procedures included examining, on a test basis, evidenceregarding\\n the amounts and disclosures in the consolidated financial statements. Our audits also included evaluating the accounting principles used and significantestimates\\n made by management, as well as evaluating the overall presentation of the consolidated financial statements. Our audit of internal control over financialreporting\\n included  obtaining  an  understanding  of  internal  control  over  financial  reporting,  assessing  the  risk  that  a  material  weakness  exists,  and  testing  andevaluating\\n the design and operating effectiveness of internal control based on the assessed risk. Our audits also included performing such other procedures as weconsidered necessary in th\\ne circumstances. We believe that our audits provide a reasonable basis for our opinions.As\\n described in Management’s Report on Internal Control over Financial Reporting, management has excluded The Drizly Group, Inc. (“Drizly”) and TupeloParent, Inc.", start\_char\_idx=0, end\_char\_idx=4599, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.8978082427817372), NodeWithScore(node=TextNode(id\_='8bd26e38-840b-46ee-88d3-7bfe8f4285da', embedding=None, metadata={'page\_label': '306', 'file\_name': 'uber\_2021.pdf', 'file\_path': 'data/10k/uber\_2021.pdf', 'file\_type': 'application/pdf', 'file\_size': 1880483, 'creation\_date': '2024-03-12', 'last\_modified\_date': '2024-03-12'}, excluded\_embed\_metadata\_keys=\['file\_name', 'file\_type', 'file\_size', 'creation\_date', 'last\_modified\_date', 'last\_accessed\_date'\], excluded\_llm\_metadata\_keys=\['file\_name', 'file\_type', 'file\_size', 'creation\_date', 'last\_modified\_date', 'last\_accessed\_date'\], relationships={<NodeRelationship.SOURCE: '1'>: RelatedNodeInfo(node\_id='64b95267-2f6a-4c1f-8d8f-9de7fe76f4c8', node\_type=<ObjectType.DOCUMENT: '4'>, metadata={'page\_label': '306', 'file\_name': 'uber\_2021.pdf', 'file\_path': 'data/10k/uber\_2021.pdf', 'file\_type': 'application/pdf', 'file\_size': 1880483, 'creation\_date': '2024-03-12', 'last\_modified\_date': '2024-03-12'}, hash='df98f8c54de64315e8021891795f855846ef72199e1261097b125f88c8178f86'), <NodeRelationship.PREVIOUS: '2'>: RelatedNodeInfo(node\_id='75ed4d3d-893c-4466-8dc7-687f1934419b', node\_type=<ObjectType.TEXT: '1'>, metadata={'page\_label': '305', 'file\_name': 'uber\_2021.pdf', 'file\_path': 'data/10k/uber\_2021.pdf', 'file\_type': 'application/pdf', 'file\_size': 1880483, 'creation\_date': '2024-03-12', 'last\_modified\_date': '2024-03-12'}, hash='2137604806ace0fa5b98cfb9734001992adc7b29e39ae0c0a7825cb9f6d5602e'), <NodeRelationship.NEXT: '3'>: RelatedNodeInfo(node\_id='cd51a0cc-80a7-421b-ae34-c7b914f997e6', node\_type=<ObjectType.TEXT: '1'>, metadata={}, hash='3249f19608f14fd995c4e7168eeaecbb6a5663275b96522764a0d0521c921ae7')}, text='Exhibit 31.2CERTIFICATION OF PR\\nINCIPAL FINANCIAL OFFICERPURSUANT TO EXCHANGE A\\nCT RULES 13a-14(a) AND 15d-14(a)AS ADOPTED PURSUANT TO SECTI\\nON 302 OF THE SARBANES-OXLEY ACT OF 2002I, Nelson Chai, certify that:\\n1.\\nI have reviewed this Annual Report on For m 10-K of Uber Technologies, Inc.;2.\\nBased on my knowledge, this report does not contain any untrue statement of a material fact or omit to state a material fact necessary to make thestatements made, in l\\night of the circumstances under which such statements were made, not misleading with respect to the period covered by this report;3.\\nBased on my knowledge, the financia l statements, and other financial information included in this report, fairly present in all material respects thefinancial condition, r\\nesults of operations and cash flows of the registrant as of, and for, the periods presented in this report;4.\\nThe registrant’s other certifying officer and I are responsible for establishing and maintaining disclosure controls and procedures (as defined in ExchangeAct Rules 13a-15(e) and 15d-15(e)\\n) and internal control over financial reporting (as defined in Exchange Act Rules 13a-15(f) and 15d-15(f)) for theregistrant and have:\\n(a)\\nDesigned such disclosure controls and procedures, or caused such disclosure controls and procedures to be designed under our supervision, toensure that materi\\nal information relating to the registrant, including its consolidated subsidiaries, is made known to us by others within thoseentities, particul\\narly during the period in which this report is being prepared;(b)\\nDesigned such internal contro l over financial reporting, or caused such internal control over financial reporting to be designed under oursupervision, to provide reasonab\\nle assurance regarding the reliability of financial reporting and the preparation of financial statements forexternal purposes in acc\\nordance with generally accepted accounting principles;(c)\\nEvaluated the effec tiveness of the registrant’s disclosure controls and procedures and presented in this report our conclusions about theeffectiveness of the d\\nisclosure controls and procedures, as of the end of the period covered by this report based on such evaluation; and(d)\\nDisclosed in this report any ch ange in the registrant’s internal control over financial reporting that occurred during the registrant’s most recentfiscal quarter (the registrant’s f\\nourth fiscal quarter in the case of an annual report) that has materially affected, or is reasonably likely tomaterially affect, the registrant’s inter\\nnal control over financial reporting; and5.\\nThe registrant’s other certifying officer and I have disclosed, based on our most recent evaluation of internal control over financial reporting, to theregistrant’s auditors and\\n the audit committee of the registrant’s board of directors (or persons performing the equivalent functions):(a)\\nAll significant defic iencies and material weaknesses in the design or operation of internal control over financial reporting which are reasonablylikely to adversely affect the\\n registrant’s ability to record, process, summarize and report financial information; and(b)\\nAny fraud, whether or not mater ial, that involves management or other employees who have a significant role in the registrant’s internal controlover financial reporting.\\nDate:\\nFebruary 24, 2022 By: /s/ Nelson Chai Nelson Chai\\nChief Financial Officer\\n(Principal Financial Offic\\ner)', start\_char\_idx=0, end\_char\_idx=3440, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.876161937500491)\], metadata={'931833d8-5d9e-4f37-bd0b-1ffeb58f0256': {'page\_label': '73', 'file\_name': 'uber\_2021.pdf', 'file\_path': 'data/10k/uber\_2021.pdf', 'file\_type': 'application/pdf', 'file\_size': 1880483, 'creation\_date': '2024-03-12', 'last\_modified\_date': '2024-03-12'}, '733e2fd3-fded-4e9d-8698-a16782d23a57': {'page\_label': '73', 'file\_name': 'uber\_2021.pdf', 'file\_path': 'data/10k/uber\_2021.pdf', 'file\_type': 'application/pdf', 'file\_size': 1880483, 'creation\_date': '2024-03-12', 'last\_modified\_date': '2024-03-12'}, '8bd26e38-840b-46ee-88d3-7bfe8f4285da': {'page\_label': '306', 'file\_name': 'uber\_2021.pdf', 'file\_path': 'data/10k/uber\_2021.pdf', 'file\_type': 'application/pdf', 'file\_size': 1880483, 'creation\_date': '2024-03-12', 'last\_modified\_date': '2024-03-12'}}))}

In \[ \]:

Copied!

\# start task
task \= agent.create\_task("What was Lyft's revenue growth in 2021?")

\# start task task = agent.create\_task("What was Lyft's revenue growth in 2021?")

In \[ \]:

Copied!

step\_output \= agent.run\_step(task.task\_id)

step\_output = agent.run\_step(task.task\_id)

\> Running step ee9eff5f-a4be-4b76-bae6-d05d2af41ecd. Step input: What was Lyft's revenue growth in 2021?
\> Running module agent\_input with input: 
state: {'sources': \[\], 'memory': ChatMemoryBuffer(token\_limit=3000, tokenizer\_fn=functools.partial(<bound method Encoding.encode of <Encoding 'cl100k\_base'>>, allowed\_special='all'), chat\_store=SimpleChatSto...
task: task\_id='7a038afc-3ead-4b0c-a924-41cd4f465270' input="What was Lyft's revenue growth in 2021?" memory=ChatMemoryBuffer(token\_limit=3000, tokenizer\_fn=functools.partial(<bound method Encoding.encode of...

\> Running module react\_prompt with input: 
input: What was Lyft's revenue growth in 2021?

\> Running module llm with input: 
messages: \[ChatMessage(role=<MessageRole.SYSTEM: 'system'>, content='\\nYou are designed to help with a variety of tasks, from answering questions     to providing summaries to other types of analyses.\\n\\n## Too...

\> Running module react\_output\_parser with input: 
chat\_response: assistant: Thought: I need to use the lyft\_10k tool to find out the revenue growth for Lyft in 2021.
Action: lyft\_10k
Action Input: {"input": "What was Lyft's revenue growth in 2021?"}

\> Running module run\_tool with input: 
reasoning\_step: thought='I need to use the lyft\_10k tool to find out the revenue growth for Lyft in 2021.' action='lyft\_10k' action\_input={'input': "What was Lyft's revenue growth in 2021?"}

\> Running module process\_agent\_response with input: 
response\_dict: {'response\_str': 'Observation: {\\'output\\': ToolOutput(content="Lyft\\'s revenue increased by 36% in 2021 compared to the prior year.", tool\_name=\\'lyft\_10k\\', raw\_input={\\'input\\': "What was Lyft\\'s r...

In \[ \]:

Copied!

step\_output \= agent.run\_step(task.task\_id)

step\_output = agent.run\_step(task.task\_id)

\> Running step 279c7a46-ce9d-4202-bec4-01d5c1ed50bd. Step input: None
\> Running module agent\_input with input: 
state: {'sources': \[\], 'memory': ChatMemoryBuffer(token\_limit=3000, tokenizer\_fn=functools.partial(<bound method Encoding.encode of <Encoding 'cl100k\_base'>>, allowed\_special='all'), chat\_store=SimpleChatSto...
task: task\_id='7a038afc-3ead-4b0c-a924-41cd4f465270' input="What was Lyft's revenue growth in 2021?" memory=ChatMemoryBuffer(token\_limit=3000, tokenizer\_fn=functools.partial(<bound method Encoding.encode of...

\> Running module react\_prompt with input: 
input: What was Lyft's revenue growth in 2021?

\> Running module llm with input: 
messages: \[ChatMessage(role=<MessageRole.SYSTEM: 'system'>, content='\\nYou are designed to help with a variety of tasks, from answering questions     to providing summaries to other types of analyses.\\n\\n## Too...

\> Running module react\_output\_parser with input: 
chat\_response: assistant: Thought: The user has repeated the question, but the tool has already provided the answer.

Answer: Lyft's revenue increased by 36% in 2021 compared to the prior year.

\> Running module process\_response with input: 
response\_step: thought='The user has repeated the question, but the tool has already provided the answer.' response="Lyft's revenue increased by 36% in 2021 compared to the prior year." is\_streaming=False

\> Running module process\_agent\_response with input: 
response\_dict: {'response\_str': "Lyft's revenue increased by 36% in 2021 compared to the prior year.", 'is\_done': True}

In \[ \]:

Copied!

step\_output.is\_last

step\_output.is\_last

Out\[ \]:

True

In \[ \]:

Copied!

print(step\_output)

print(step\_output)

Uber's Management's Report on Internal Control over Financial Reporting for the year ended December 31, 2021, stated that management excluded The Drizly Group, Inc. ("Drizly") and TupeloParent, Inc. ("Transplace") from its assessment of internal control over financial reporting. This exclusion was due to their acquisition by the company during 2021. Drizly and Transplace were wholly-owned subsidiaries whose total assets and total revenues collectively represented approximately 3% and 4%, respectively, of the related consolidated financial statement amounts for the year.

In \[ \]:

Copied!

response \= agent.finalize\_response(task.task\_id)

response = agent.finalize\_response(task.task\_id)

In \[ \]:

Copied!

print(str(response))

print(str(response))

Uber's Management's Report on Internal Control over Financial Reporting for the year ended December 31, 2021, stated that management excluded The Drizly Group, Inc. ("Drizly") and TupeloParent, Inc. ("Transplace") from its assessment of internal control over financial reporting. This exclusion was due to their acquisition by the company during 2021. Drizly and Transplace were wholly-owned subsidiaries whose total assets and total revenues collectively represented approximately 3% and 4%, respectively, of the related consolidated financial statement amounts for the year.

Back to top

[Previous GPT Builder Demo](https://docs.llamaindex.ai/en/stable/examples/agent/agent_builder/)[Next Step-wise, Controllable Agents](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_runner/)

Hi, how can I help you?

🦙
