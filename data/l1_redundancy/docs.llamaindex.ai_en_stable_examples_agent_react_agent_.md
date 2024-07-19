Title: ReAct Agent - A Simple Intro with Calculator Tools

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/react_agent/

Markdown Content:
ReAct Agent - A Simple Intro with Calculator Tools - LlamaIndex


This is a notebook that showcases the ReAct agent over very simple calculator tools (no fancy RAG pipelines or API calls).

We show how it can reason step-by-step over different tools to achieve the end goal.

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

from llama\_index.core.agent import ReActAgent
from llama\_index.llms.openai import OpenAI
from llama\_index.core.llms import ChatMessage
from llama\_index.core.tools import BaseTool, FunctionTool

from llama\_index.core.agent import ReActAgent from llama\_index.llms.openai import OpenAI from llama\_index.core.llms import ChatMessage from llama\_index.core.tools import BaseTool, FunctionTool

\[nltk\_data\] Downloading package stopwords to /Users/jerryliu/Programmi
\[nltk\_data\]     ng/gpt\_index/.venv/lib/python3.10/site-
\[nltk\_data\]     packages/llama\_index/legacy/\_static/nltk\_cache...
\[nltk\_data\]   Unzipping corpora/stopwords.zip.
\[nltk\_data\] Downloading package punkt to /Users/jerryliu/Programming/g
\[nltk\_data\]     pt\_index/.venv/lib/python3.10/site-
\[nltk\_data\]     packages/llama\_index/legacy/\_static/nltk\_cache...
\[nltk\_data\]   Unzipping tokenizers/punkt.zip.

Define Function Tools[¶](https://docs.llamaindex.ai/en/stable/examples/agent/react_agent/#define-function-tools)
----------------------------------------------------------------------------------------------------------------

We setup some trivial `multiply` and `add` tools. Note that you can define arbitrary functions and pass it to the `FunctionTool` (which will process the docstring and parameter signature).

In \[ \]:

Copied!

def multiply(a: int, b: int) \-> int:
    """Multiply two integers and returns the result integer"""
    return a \* b

multiply\_tool \= FunctionTool.from\_defaults(fn\=multiply)

def multiply(a: int, b: int) -> int: """Multiply two integers and returns the result integer""" return a \* b multiply\_tool = FunctionTool.from\_defaults(fn=multiply)

In \[ \]:

Copied!

def add(a: int, b: int) \-> int:
    """Add two integers and returns the result integer"""
    return a + b

add\_tool \= FunctionTool.from\_defaults(fn\=add)

def add(a: int, b: int) -> int: """Add two integers and returns the result integer""" return a + b add\_tool = FunctionTool.from\_defaults(fn=add)

Run Some Queries[¶](https://docs.llamaindex.ai/en/stable/examples/agent/react_agent/#run-some-queries)
------------------------------------------------------------------------------------------------------

### gpt-3.5-turbo[¶](https://docs.llamaindex.ai/en/stable/examples/agent/react_agent/#gpt-35-turbo)

In \[ \]:

Copied!

llm \= OpenAI(model\="gpt-3.5-turbo-instruct")
agent \= ReActAgent.from\_tools(\[multiply\_tool, add\_tool\], llm\=llm, verbose\=True)

llm = OpenAI(model="gpt-3.5-turbo-instruct") agent = ReActAgent.from\_tools(\[multiply\_tool, add\_tool\], llm=llm, verbose=True)

In \[ \]:

Copied!

response \= agent.chat("What is 20+(2\*4)? Calculate step by step ")

response = agent.chat("What is 20+(2\*4)? Calculate step by step ")

Thought: I need to use a tool to help me answer the question.
Action: multiply
Action Input: {"a": 2, "b": 4}
Observation: 8
Thought: I need to use a tool to help me answer the question.
Action: add
Action Input: {"a": 20, "b": 8}
Observation: 28
Thought: I can answer without using any more tools.
Answer: 28

In \[ \]:

Copied!

response\_gen \= agent.stream\_chat("What is 20+2\*4? Calculate step by step")
response\_gen.print\_response\_stream()

response\_gen = agent.stream\_chat("What is 20+2\*4? Calculate step by step") response\_gen.print\_response\_stream()

28

### gpt-4[¶](https://docs.llamaindex.ai/en/stable/examples/agent/react_agent/#gpt-4)

In \[ \]:

Copied!

llm \= OpenAI(model\="gpt-4")
agent \= ReActAgent.from\_tools(\[multiply\_tool, add\_tool\], llm\=llm, verbose\=True)

llm = OpenAI(model="gpt-4") agent = ReActAgent.from\_tools(\[multiply\_tool, add\_tool\], llm=llm, verbose=True)

In \[ \]:

Copied!

response \= agent.chat("What is 2+2\*4")
print(response)

response = agent.chat("What is 2+2\*4") print(response)

Thought: I need to use the tools to help me answer the question. According to the order of operations in mathematics (BIDMAS/BODMAS), multiplication should be done before addition. So, I will first multiply 2 and 4, and then add the result to 2.
Action: multiply
Action Input: {'a': 2, 'b': 4}
Observation: 8
Thought: Now that I have the result of the multiplication, I need to add this result to 2.
Action: add
Action Input: {'a': 2, 'b': 8}
Observation: 10
Thought: I can answer without using any more tools.
Answer: 10
10

View Prompts[¶](https://docs.llamaindex.ai/en/stable/examples/agent/react_agent/#view-prompts)
----------------------------------------------------------------------------------------------

Let's take a look at the core system prompt powering the ReAct agent!

Within the agent, the current conversation history is dumped below this line.

In \[ \]:

Copied!

llm \= OpenAI(model\="gpt-4")
agent \= ReActAgent.from\_tools(\[multiply\_tool, add\_tool\], llm\=llm, verbose\=True)

llm = OpenAI(model="gpt-4") agent = ReActAgent.from\_tools(\[multiply\_tool, add\_tool\], llm=llm, verbose=True)

In \[ \]:

Copied!

prompt\_dict \= agent.get\_prompts()
for k, v in prompt\_dict.items():
    print(f"Prompt: {k}\\n\\nValue: {v.template}")

prompt\_dict = agent.get\_prompts() for k, v in prompt\_dict.items(): print(f"Prompt: {k}\\n\\nValue: {v.template}")

Prompt: agent\_worker:system\_prompt

Value: 
You are designed to help with a variety of tasks, from answering questions     to providing summaries to other types of analyses.

## Tools
You have access to a wide variety of tools. You are responsible for using
the tools in any sequence you deem appropriate to complete the task at hand.
This may require breaking the task into subtasks and using different tools
to complete each subtask.

You have access to the following tools:
{tool\_desc}

## Output Format
To answer the question, please use the following format.

\`\`\`
Thought: I need to use a tool to help me answer the question.
Action: tool name (one of {tool\_names}) if using a tool.
Action Input: the input to the tool, in a JSON format representing the kwargs (e.g. {{"input": "hello world", "num\_beams": 5}})
\`\`\`

Please ALWAYS start with a Thought.

Please use a valid JSON format for the Action Input. Do NOT do this {{'input': 'hello world', 'num\_beams': 5}}.

If this format is used, the user will respond in the following format:

\`\`\`
Observation: tool response
\`\`\`

You should keep repeating the above format until you have enough information
to answer the question without using any more tools. At that point, you MUST respond
in the one of the following two formats:

\`\`\`
Thought: I can answer without using any more tools.
Answer: \[your answer here\]
\`\`\`

\`\`\`
Thought: I cannot answer the question with the provided tools.
Answer: Sorry, I cannot answer your query.
\`\`\`

## Current Conversation
Below is the current conversation consisting of interleaving human and assistant messages.

### Customizing the Prompt[¶](https://docs.llamaindex.ai/en/stable/examples/agent/react_agent/#customizing-the-prompt)

For fun, let's try instructing the agent to output the answer along with reasoning in bullet points. See "## Additional Rules" section.

In \[ \]:

Copied!

from llama\_index.core import PromptTemplate

react\_system\_header\_str \= """\\

You are designed to help with a variety of tasks, from answering questions \\
    to providing summaries to other types of analyses.

\## Tools
You have access to a wide variety of tools. You are responsible for using
the tools in any sequence you deem appropriate to complete the task at hand.
This may require breaking the task into subtasks and using different tools
to complete each subtask.

You have access to the following tools:
{tool\_desc}

\## Output Format
To answer the question, please use the following format.

\`\`\`
Thought: I need to use a tool to help me answer the question.
Action: tool name (one of {tool\_names}) if using a tool.
Action Input: the input to the tool, in a JSON format representing the kwargs (e.g. {{"input": "hello world", "num\_beams": 5}})
\`\`\`

Please ALWAYS start with a Thought.

Please use a valid JSON format for the Action Input. Do NOT do this {{'input': 'hello world', 'num\_beams': 5}}.

If this format is used, the user will respond in the following format:

\`\`\`
Observation: tool response
\`\`\`

You should keep repeating the above format until you have enough information
to answer the question without using any more tools. At that point, you MUST respond
in the one of the following two formats:

\`\`\`
Thought: I can answer without using any more tools.
Answer: \[your answer here\]
\`\`\`

\`\`\`
Thought: I cannot answer the question with the provided tools.
Answer: Sorry, I cannot answer your query.
\`\`\`

\## Additional Rules
\- The answer MUST contain a sequence of bullet points that explain how you arrived at the answer. This can include aspects of the previous conversation history.
\- You MUST obey the function signature of each tool. Do NOT pass in no arguments if the function expects arguments.

\## Current Conversation
Below is the current conversation consisting of interleaving human and assistant messages.

"""
react\_system\_prompt \= PromptTemplate(react\_system\_header\_str)

from llama\_index.core import PromptTemplate react\_system\_header\_str = """\\ You are designed to help with a variety of tasks, from answering questions \\ to providing summaries to other types of analyses. ## Tools You have access to a wide variety of tools. You are responsible for using the tools in any sequence you deem appropriate to complete the task at hand. This may require breaking the task into subtasks and using different tools to complete each subtask. You have access to the following tools: {tool\_desc} ## Output Format To answer the question, please use the following format. \`\`\` Thought: I need to use a tool to help me answer the question. Action: tool name (one of {tool\_names}) if using a tool. Action Input: the input to the tool, in a JSON format representing the kwargs (e.g. {{"input": "hello world", "num\_beams": 5}}) \`\`\` Please ALWAYS start with a Thought. Please use a valid JSON format for the Action Input. Do NOT do this {{'input': 'hello world', 'num\_beams': 5}}. If this format is used, the user will respond in the following format: \`\`\` Observation: tool response \`\`\` You should keep repeating the above format until you have enough information to answer the question without using any more tools. At that point, you MUST respond in the one of the following two formats: \`\`\` Thought: I can answer without using any more tools. Answer: \[your answer here\] \`\`\` \`\`\` Thought: I cannot answer the question with the provided tools. Answer: Sorry, I cannot answer your query. \`\`\` ## Additional Rules - The answer MUST contain a sequence of bullet points that explain how you arrived at the answer. This can include aspects of the previous conversation history. - You MUST obey the function signature of each tool. Do NOT pass in no arguments if the function expects arguments. ## Current Conversation Below is the current conversation consisting of interleaving human and assistant messages. """ react\_system\_prompt = PromptTemplate(react\_system\_header\_str)

In \[ \]:

Copied!

agent.get\_prompts()

agent.get\_prompts()

Out\[ \]:

{'agent\_worker:system\_prompt': PromptTemplate(metadata={'prompt\_type': <PromptType.CUSTOM: 'custom'>}, template\_vars=\['tool\_desc', 'tool\_names'\], kwargs={}, output\_parser=None, template\_var\_mappings=None, function\_mappings=None, template='\\nYou are designed to help with a variety of tasks, from answering questions     to providing summaries to other types of analyses.\\n\\n## Tools\\nYou have access to a wide variety of tools. You are responsible for using\\nthe tools in any sequence you deem appropriate to complete the task at hand.\\nThis may require breaking the task into subtasks and using different tools\\nto complete each subtask.\\n\\nYou have access to the following tools:\\n{tool\_desc}\\n\\n## Output Format\\nTo answer the question, please use the following format.\\n\\n\`\`\`\\nThought: I need to use a tool to help me answer the question.\\nAction: tool name (one of {tool\_names}) if using a tool.\\nAction Input: the input to the tool, in a JSON format representing the kwargs (e.g. {{"input": "hello world", "num\_beams": 5}})\\n\`\`\`\\n\\nPlease ALWAYS start with a Thought.\\n\\nPlease use a valid JSON format for the Action Input. Do NOT do this {{\\'input\\': \\'hello world\\', \\'num\_beams\\': 5}}.\\n\\nIf this format is used, the user will respond in the following format:\\n\\n\`\`\`\\nObservation: tool response\\n\`\`\`\\n\\nYou should keep repeating the above format until you have enough information\\nto answer the question without using any more tools. At that point, you MUST respond\\nin the one of the following two formats:\\n\\n\`\`\`\\nThought: I can answer without using any more tools.\\nAnswer: \[your answer here\]\\n\`\`\`\\n\\n\`\`\`\\nThought: I cannot answer the question with the provided tools.\\nAnswer: Sorry, I cannot answer your query.\\n\`\`\`\\n\\n## Current Conversation\\nBelow is the current conversation consisting of interleaving human and assistant messages.\\n\\n')}

In \[ \]:

Copied!

agent.update\_prompts({"agent\_worker:system\_prompt": react\_system\_prompt})

agent.update\_prompts({"agent\_worker:system\_prompt": react\_system\_prompt})

In \[ \]:

Copied!

agent.reset()
response \= agent.chat("What is 5+3+2")
print(response)

agent.reset() response = agent.chat("What is 5+3+2") print(response)

Thought: I need to use the add tool to help me answer the question.
Action: add
Action Input: {'a': 5, 'b': 3}
Observation: 8
Thought: Now I need to add the result from the previous operation to 2.
Action: add
Action Input: {'a': 8, 'b': 2}
Observation: 10
Thought: I can answer without using any more tools.
Answer: The result of 5+3+2 is 10.

- I first added 5 and 3 using the add tool, which resulted in 8.
- Then I added the result (8) to 2 using the add tool again, which resulted in 10.
The result of 5+3+2 is 10.

- I first added 5 and 3 using the add tool, which resulted in 8.
- Then I added the result (8) to 2 using the add tool again, which resulted in 10.

Back to top

[Previous Benchmarking OpenAI Retrieval API (through Assistant Agent)](https://docs.llamaindex.ai/en/stable/examples/agent/openai_retrieval_benchmark/)[Next ReAct Agent with Query Engine (RAG) Tools](https://docs.llamaindex.ai/en/stable/examples/agent/react_agent_with_query_engine/)

Hi, how can I help you?

🦙
