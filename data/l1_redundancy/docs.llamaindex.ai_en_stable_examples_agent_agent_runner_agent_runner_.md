Title: Step-wise, Controllable Agents - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_runner/

Markdown Content:
Step-wise, Controllable Agents - LlamaIndex


This notebook shows you how to use our brand-new lower-level agent API, which supports a host of functionalities beyond simply executing a user query to help you create tasks, iterate through steps, and control the inputs for each step.

### High-Level Agent Architecture[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_runner/#high-level-agent-architecture)

Our "agents" are composed of `AgentRunner` objects that interact with `AgentWorkers`. `AgentRunner`s are orchestrators that store state (including conversational memory), create and maintain tasks, run steps through each task, and offer the user-facing, high-level interface for users to interact with.

`AgentWorker`s **control the step-wise execution of a Task**. Given an input step, an agent worker is responsible for generating the next step. They can be initialized with parameters and act upon state passed down from the Task/TaskStep objects, but do not inherently store state themselves. The outer `AgentRunner` is responsible for calling an `AgentWorker` and collecting/aggregating the results.

If you are building your own agent, you will likely want to create your own `AgentWorker`. See below for an example!

### Notebook Walkthrough[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_runner/#notebook-walkthrough)

This notebook shows you how to run step-wise execution and full-execution with agents.

*   We show you how to do execution with OpenAIAgent (function calling)
*   We show you how to do execution with ReActAgent

In \[ \]:

Copied!

%pip install llama\-index\-agent\-openai
%pip install llama\-index\-llms\-openai

%pip install llama-index-agent-openai %pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import json
from typing import Sequence, List

from llama\_index.llms.openai import OpenAI
from llama\_index.core.llms import ChatMessage
from llama\_index.core.tools import BaseTool, FunctionTool

import nest\_asyncio

nest\_asyncio.apply()

import json from typing import Sequence, List from llama\_index.llms.openai import OpenAI from llama\_index.core.llms import ChatMessage from llama\_index.core.tools import BaseTool, FunctionTool import nest\_asyncio nest\_asyncio.apply()

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

llm \= OpenAI(model\="gpt-3.5-turbo")

llm = OpenAI(model="gpt-3.5-turbo")

Test OpenAI Agent[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_runner/#test-openai-agent)
----------------------------------------------------------------------------------------------------------------------

There's two main ways to initialize the agent.

*   **Option 1**: Initialize `OpenAIAgent`. This is a simple subclass of `AgentRunner` that bundles the `OpenAIAgentWorker` under the hood.
*   **Option 2**: Initialize `AgentRunner` with `OpenAIAgentWorker`. Here you import the modules and compose your own agent.

**NOTE**: The old OpenAIAgent can still be imported via `from llama_index.agent import OldOpenAIAgent`.

In \[ \]:

Copied!

from llama\_index.core.agent import AgentRunner
from llama\_index.agent.openai import OpenAIAgentWorker, OpenAIAgent

\# Option 1: Initialize OpenAIAgent
agent \= OpenAIAgent.from\_tools(tools, llm\=llm, verbose\=True)

\# # Option 2: Initialize AgentRunner with OpenAIAgentWorker
\# openai\_step\_engine = OpenAIAgentWorker.from\_tools(tools, llm=llm, verbose=True)
\# agent = AgentRunner(openai\_step\_engine)

from llama\_index.core.agent import AgentRunner from llama\_index.agent.openai import OpenAIAgentWorker, OpenAIAgent # Option 1: Initialize OpenAIAgent agent = OpenAIAgent.from\_tools(tools, llm=llm, verbose=True) # # Option 2: Initialize AgentRunner with OpenAIAgentWorker # openai\_step\_engine = OpenAIAgentWorker.from\_tools(tools, llm=llm, verbose=True) # agent = AgentRunner(openai\_step\_engine)

### Test E2E Chat[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_runner/#test-e2e-chat)

Here we re-demonstrate the end-to-end execution of a user task through the `chat()` function.

This will iterate step-wise until the agent is done with the current task.

In \[ \]:

Copied!

agent.chat("Hi")

agent.chat("Hi")

Out\[ \]:

AgentChatResponse(response='Hello! How can I assist you today?', sources=\[\], source\_nodes=\[\])

In \[ \]:

Copied!

response \= agent.chat("What is (121 \* 3) + 42?")

response = agent.chat("What is (121 \* 3) + 42?")

\
Calling function: multiply with args: {
  "a": 121,
  "b": 3
}
Got output: 363
 Calling Function 

In \[ \]:

Copied!

response

response

Out\[ \]:

AgentChatResponse(response='The result of (121 \* 3) + 42 is 405.', sources=\[ToolOutput(content='363', tool\_name='multiply', raw\_input={'args': (), 'kwargs': {'a': 121, 'b': 3}}, raw\_output=363), ToolOutput(content='405', tool\_name='add', raw\_input={'args': (), 'kwargs': {'a': 363, 'b': 42}}, raw\_output=405)\], source\_nodes=\[\])

### Test Step-Wise Execution[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_runner/#test-step-wise-execution)

Now let's show the lower-level API in action. We do the same thing, but break this down into steps.

In \[ \]:

Copied!

\# start task
task \= agent.create\_task("What is (121 \* 3) + 42?")

\# start task task = agent.create\_task("What is (121 \* 3) + 42?")

In \[ \]:

Copied!

step\_output \= agent.run\_step(task.task\_id)

step\_output = agent.run\_step(task.task\_id)

\
Calling function: multiply with args: {
  "a": 121,
  "b": 3
}
Got output: 363
 Calling Function 

In \[ \]:

Copied!

step\_output \= agent.run\_step(task.task\_id)

step\_output = agent.run\_step(task.task\_id)

In \[ \]:

Copied!

\# display final response
print(step\_output.is\_last)

\# display final response print(step\_output.is\_last)

True

In \[ \]:

Copied!

\# now that the step execution is done, we can finalize response
response \= agent.finalize\_response(task.task\_id)
print(str(response))

\# now that the step execution is done, we can finalize response response = agent.finalize\_response(task.task\_id) print(str(response))

The result of (121 \* 3) + 42 is 405.

Test ReAct Agent[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_runner/#test-react-agent)
--------------------------------------------------------------------------------------------------------------------

We do the same experiments, but with ReAct.

In \[ \]:

Copied!

llm \= OpenAI(model\="gpt-4-1106-preview")

llm = OpenAI(model="gpt-4-1106-preview")

In \[ \]:

Copied!

from llama\_index.core.agent import AgentRunner, ReActAgentWorker, ReActAgent

from llama\_index.core.agent import AgentRunner, ReActAgentWorker, ReActAgent

In \[ \]:

Copied!

\# Option 1: Initialize OpenAIAgent
agent \= ReActAgent.from\_tools(tools, llm\=llm, verbose\=True)

\# # Option 2: Initialize AgentRunner with ReActAgentWorker
\# react\_step\_engine = ReActAgentWorker.from\_tools(tools, llm=llm, verbose=True)
\# agent = AgentRunner(react\_step\_engine)

\# Option 1: Initialize OpenAIAgent agent = ReActAgent.from\_tools(tools, llm=llm, verbose=True) # # Option 2: Initialize AgentRunner with ReActAgentWorker # react\_step\_engine = ReActAgentWorker.from\_tools(tools, llm=llm, verbose=True) # agent = AgentRunner(react\_step\_engine)

In \[ \]:

Copied!

agent.chat("Hi")

agent.chat("Hi")

Thought: The user has greeted me, and I should respond in kind.
Response: Hello! How can I assist you today?

Out\[ \]:

AgentChatResponse(response='Hello! How can I assist you today?', sources=\[\], source\_nodes=\[\])

In \[ \]:

Copied!

response \= agent.chat("What is (121 \* 3) + 42?")

response = agent.chat("What is (121 \* 3) + 42?")

Thought: I need to use a tool to help me calculate the multiplication part of the question first.
Action: multiply
Action Input: {'a': 121, 'b': 3}
Observation: 363
Thought: Now that I have the result of the multiplication, I need to add 42 to it.
Action: add
Action Input: {'a': 363, 'b': 42}
Observation: 405
Thought: I can answer without using any more tools.
Response: (121 \* 3) + 42 equals 405.

In \[ \]:

Copied!

response

response

Out\[ \]:

AgentChatResponse(response='(121 \* 3) + 42 equals 405.', sources=\[ToolOutput(content='363', tool\_name='multiply', raw\_input={'args': (), 'kwargs': {'a': 121, 'b': 3}}, raw\_output=363), ToolOutput(content='405', tool\_name='add', raw\_input={'args': (), 'kwargs': {'a': 363, 'b': 42}}, raw\_output=405)\], source\_nodes=\[\])

In \[ \]:

Copied!

\# start task
task \= agent.create\_task("What is (121 \* 3) + 42?")

\# start task task = agent.create\_task("What is (121 \* 3) + 42?")

In \[ \]:

Copied!

step\_output \= agent.run\_step(task.task\_id)

step\_output = agent.run\_step(task.task\_id)

Thought: I need to use a tool to help me answer the question.
Action: multiply
Action Input: {'a': 121, 'b': 3}
Observation: 363

In \[ \]:

Copied!

step\_output.output

step\_output.output

Out\[ \]:

AgentChatResponse(response='Observation: 363', sources=\[ToolOutput(content='363', tool\_name='multiply', raw\_input={'args': (), 'kwargs': {'a': 121, 'b': 3}}, raw\_output=363)\], source\_nodes=\[\])

In \[ \]:

Copied!

step\_output \= agent.run\_step(task.task\_id)

step\_output = agent.run\_step(task.task\_id)

Thought: Now that I have the result of the multiplication, I need to add 42 to it.
Action: add
Action Input: {'a': 363, 'b': 42}
Observation: 405

In \[ \]:

Copied!

step\_output.output

step\_output.output

Out\[ \]:

AgentChatResponse(response='Observation: 405', sources=\[ToolOutput(content='363', tool\_name='multiply', raw\_input={'args': (), 'kwargs': {'a': 121, 'b': 3}}, raw\_output=363), ToolOutput(content='405', tool\_name='add', raw\_input={'args': (), 'kwargs': {'a': 363, 'b': 42}}, raw\_output=405)\], source\_nodes=\[\])

In \[ \]:

Copied!

step\_output \= agent.run\_step(task.task\_id)

step\_output = agent.run\_step(task.task\_id)

Thought: I can answer without using any more tools.
Response: (121 \* 3) + 42 equals 405.

In \[ \]:

Copied!

step\_output.output

step\_output.output

Out\[ \]:

AgentChatResponse(response='(121 \* 3) + 42 equals 405.', sources=\[ToolOutput(content='363', tool\_name='multiply', raw\_input={'args': (), 'kwargs': {'a': 121, 'b': 3}}, raw\_output=363), ToolOutput(content='405', tool\_name='add', raw\_input={'args': (), 'kwargs': {'a': 363, 'b': 42}}, raw\_output=405)\], source\_nodes=\[\])

### List Out Tasks[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_runner/#list-out-tasks)

There are 3 tasks, corresponding to the three runs above.

In \[ \]:

Copied!

tasks \= agent.list\_tasks()
print(len(tasks))

tasks = agent.list\_tasks() print(len(tasks))

3

In \[ \]:

Copied!

task\_state \= tasks\[\-1\]
task\_state.task.input

task\_state = tasks\[-1\] task\_state.task.input

Out\[ \]:

'What is (121 \* 3) + 42?'

In \[ \]:

Copied!

\# get completed steps
completed\_steps \= agent.get\_completed\_steps(task\_state.task.task\_id)

\# get completed steps completed\_steps = agent.get\_completed\_steps(task\_state.task.task\_id)

In \[ \]:

Copied!

len(completed\_steps)

len(completed\_steps)

Out\[ \]:

3

In \[ \]:

Copied!

completed\_steps\[0\]

completed\_steps\[0\]

Out\[ \]:

TaskStepOutput(output=AgentChatResponse(response='Observation: 363', sources=\[ToolOutput(content='363', tool\_name='multiply', raw\_input={'args': (), 'kwargs': {'a': 121, 'b': 3}}, raw\_output=363), ToolOutput(content='405', tool\_name='add', raw\_input={'args': (), 'kwargs': {'a': 363, 'b': 42}}, raw\_output=405)\], source\_nodes=\[\]), task\_step=TaskStep(task\_id='1a71f7cb-c854-4baa-ad11-0c97460a6af2', step\_id='72ed54f4-4edd-496b-bb6a-d58f4275f03e', input='What is (121 \* 3) + 42?', step\_state={}, next\_steps={}, prev\_steps={}, is\_ready=True), next\_steps=\[TaskStep(task\_id='1a71f7cb-c854-4baa-ad11-0c97460a6af2', step\_id='6486cc4a-15ea-490a-b761-9dc88881fc24', input=None, step\_state={}, next\_steps={}, prev\_steps={}, is\_ready=True)\], is\_last=False)

In \[ \]:

Copied!

for idx in range(len(completed\_steps)):
    print(f"Step {idx}")
    print(f"Response: {completed\_steps\[idx\].output.response}")
    print(f"Sources: {completed\_steps\[idx\].output.sources}")

for idx in range(len(completed\_steps)): print(f"Step {idx}") print(f"Response: {completed\_steps\[idx\].output.response}") print(f"Sources: {completed\_steps\[idx\].output.sources}")

Step 0
Response: Observation: 363
Sources: \[ToolOutput(content='363', tool\_name='multiply', raw\_input={'args': (), 'kwargs': {'a': 121, 'b': 3}}, raw\_output=363), ToolOutput(content='405', tool\_name='add', raw\_input={'args': (), 'kwargs': {'a': 363, 'b': 42}}, raw\_output=405)\]
Step 1
Response: Observation: 405
Sources: \[ToolOutput(content='363', tool\_name='multiply', raw\_input={'args': (), 'kwargs': {'a': 121, 'b': 3}}, raw\_output=363), ToolOutput(content='405', tool\_name='add', raw\_input={'args': (), 'kwargs': {'a': 363, 'b': 42}}, raw\_output=405)\]
Step 2
Response: (121 \* 3) + 42 equals 405.
Sources: \[ToolOutput(content='363', tool\_name='multiply', raw\_input={'args': (), 'kwargs': {'a': 121, 'b': 3}}, raw\_output=363), ToolOutput(content='405', tool\_name='add', raw\_input={'args': (), 'kwargs': {'a': 363, 'b': 42}}, raw\_output=405)\]

Back to top

[Previous Building a Multi-PDF Agent using Query Pipelines and HyDE](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_around_query_pipeline_with_HyDE_for_PDFs/)[Next Controllable Agents for RAG](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_runner_rag_controllable/)
