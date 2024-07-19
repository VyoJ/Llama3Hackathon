Title: Simple Composable Memory - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/memory/composable_memory/

Markdown Content:
Simple Composable Memory - LlamaIndex


In this notebook, we demonstrate how to inject multiple memory sources into an agent. Specifically, we use the `SimpleComposableMemory` which is comprised of a `primary_memory` as well as potentially several secondary memory sources (stored in `secondary_memory_sources`). The main difference is that `primary_memory` will be used as the main chat buffer for the agent, where as any retrieved messages from `secondary_memory_sources` will be injected to the system prompt message only.

Multiple memory sources may be of use for example in situations where you have a longer-term memory such as `VectorMemory` that you want to use in addition to the default `ChatMemoryBuffer`. What you'll see in this notebook is that with a `SimpleComposableMemory` you'll be able to effectively "load" the desired messages from long-term memory into the main memory (i.e. the `ChatMemoryBuffer`).

How `SimpleComposableMemory` Works?[¶](https://docs.llamaindex.ai/en/stable/examples/agent/memory/composable_memory/#how-simplecomposablememory-works)
------------------------------------------------------------------------------------------------------------------------------------------------------

We begin with the basic usage of the `SimpleComposableMemory`. Here we construct a `VectorMemory` as well as a default `ChatMemoryBuffer`. The `VectorMemory` will be our secondary memory source, whereas the `ChatMemoryBuffer` will be the main or primary one. To instantiate a `SimpleComposableMemory` object, we need to supply a `primary_memory` and (optionally) a list of `secondary_memory_sources`.

![Image 4: SimpleComposableMemoryIllustration](https://d3ddy8balm3goa.cloudfront.net/llamaindex/simple-composable-memory.excalidraw.svg)

In \[ \]:

Copied!

from llama\_index.core.memory import (
    VectorMemory,
    SimpleComposableMemory,
    ChatMemoryBuffer,
)
from llama\_index.core.llms import ChatMessage
from llama\_index.embeddings.openai import OpenAIEmbedding

vector\_memory \= VectorMemory.from\_defaults(
    vector\_store\=None,  \# leave as None to use default in-memory vector store
    embed\_model\=OpenAIEmbedding(),
    retriever\_kwargs\={"similarity\_top\_k": 1},
)

\# let's set some initial messages in our secondary vector memory
msgs \= \[
    ChatMessage.from\_str("You are a SOMEWHAT helpful assistant.", "system"),
    ChatMessage.from\_str("Bob likes burgers.", "user"),
    ChatMessage.from\_str("Indeed, Bob likes apples.", "assistant"),
    ChatMessage.from\_str("Alice likes apples.", "user"),
\]
vector\_memory.set(msgs)

chat\_memory\_buffer \= ChatMemoryBuffer.from\_defaults()

composable\_memory \= SimpleComposableMemory.from\_defaults(
    primary\_memory\=chat\_memory\_buffer,
    secondary\_memory\_sources\=\[vector\_memory\],
)

from llama\_index.core.memory import ( VectorMemory, SimpleComposableMemory, ChatMemoryBuffer, ) from llama\_index.core.llms import ChatMessage from llama\_index.embeddings.openai import OpenAIEmbedding vector\_memory = VectorMemory.from\_defaults( vector\_store=None, # leave as None to use default in-memory vector store embed\_model=OpenAIEmbedding(), retriever\_kwargs={"similarity\_top\_k": 1}, ) # let's set some initial messages in our secondary vector memory msgs = \[ ChatMessage.from\_str("You are a SOMEWHAT helpful assistant.", "system"), ChatMessage.from\_str("Bob likes burgers.", "user"), ChatMessage.from\_str("Indeed, Bob likes apples.", "assistant"), ChatMessage.from\_str("Alice likes apples.", "user"), \] vector\_memory.set(msgs) chat\_memory\_buffer = ChatMemoryBuffer.from\_defaults() composable\_memory = SimpleComposableMemory.from\_defaults( primary\_memory=chat\_memory\_buffer, secondary\_memory\_sources=\[vector\_memory\], )

In \[ \]:

Copied!

composable\_memory.primary\_memory

composable\_memory.primary\_memory

Out\[ \]:

ChatMemoryBuffer(chat\_store=SimpleChatStore(store={}), chat\_store\_key='chat\_history', token\_limit=3000, tokenizer\_fn=functools.partial(<bound method Encoding.encode of <Encoding 'cl100k\_base'>>, allowed\_special='all'))

In \[ \]:

Copied!

composable\_memory.secondary\_memory\_sources

composable\_memory.secondary\_memory\_sources

Out\[ \]:

\[VectorMemory(vector\_index=<llama\_index.core.indices.vector\_store.base.VectorStoreIndex object at 0x137b912a0>, retriever\_kwargs={'similarity\_top\_k': 1}, batch\_by\_user\_message=True, cur\_batch\_textnode=TextNode(id\_='288b0ef3-570e-4698-a1ae-b3531df66361', embedding=None, metadata={'sub\_dicts': \[{'role': <MessageRole.USER: 'user'>, 'content': 'Alice likes apples.', 'additional\_kwargs': {}}\]}, excluded\_embed\_metadata\_keys=\['sub\_dicts'\], excluded\_llm\_metadata\_keys=\['sub\_dicts'\], relationships={}, text='Alice likes apples.', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'))\]

### `put()` messages into memory[¶](https://docs.llamaindex.ai/en/stable/examples/agent/memory/composable_memory/#put-messages-into-memory)

Since `SimpleComposableMemory` is itself a subclass of `BaseMemory`, we add messages to it in the same way as we do for other memory modules. Note that for `SimpleComposableMemory`, invoking `.put()` effectively calls `.put()` on all memory sources. In other words, the message gets added to `primary` and `secondary` sources.

In \[ \]:

Copied!

msgs \= \[
    ChatMessage.from\_str("You are a REALLY helpful assistant.", "system"),
    ChatMessage.from\_str("Jerry likes juice.", "user"),
\]

msgs = \[ ChatMessage.from\_str("You are a REALLY helpful assistant.", "system"), ChatMessage.from\_str("Jerry likes juice.", "user"), \]

In \[ \]:

Copied!

\# load into all memory sources modules"
for m in msgs:
    composable\_memory.put(m)

\# load into all memory sources modules" for m in msgs: composable\_memory.put(m)

### `get()` messages from memory[¶](https://docs.llamaindex.ai/en/stable/examples/agent/memory/composable_memory/#get-messages-from-memory)

When `.get()` is invoked, we similarly execute all of the `.get()` methods of `primary` memory as well as all of the `secondary` sources. This leaves us with sequence of lists of messages that we have to must "compose" into a sensible single set of messages (to pass downstream to our agents). Special care must be applied here in general to ensure that the final sequence of messages are both sensible and conform to the chat APIs of the LLM provider.

For `SimpleComposableMemory`, we **inject the messages from the `secondary` sources in the system message of the `primary` memory**. The rest of the message history of the `primary` source is left intact, and this composition is what is ultimately returned.

In \[ \]:

Copied!

msgs \= composable\_memory.get("What does Bob like?")
msgs

msgs = composable\_memory.get("What does Bob like?") msgs

Out\[ \]:

\[ChatMessage(role=<MessageRole.SYSTEM: 'system'>, content='You are a REALLY helpful assistant.\\n\\nBelow are a set of relevant dialogues retrieved from potentially several memory sources:\\n\\n\\n\\n\\tUSER: Bob likes burgers.\\n\\tASSISTANT: Indeed, Bob likes apples.\\n\\n\\n\\nThis is the end of the retrieved message dialogues.', additional\_kwargs={}),
 ChatMessage(role=<MessageRole.USER: 'user'>, content='Jerry likes juice.', additional\_kwargs={})\]

In \[ \]:

Copied!

\# see the memory injected into the system message of the primary memory
print(msgs\[0\])

\# see the memory injected into the system message of the primary memory print(msgs\[0\])

system: You are a REALLY helpful assistant.

Below are a set of relevant dialogues retrieved from potentially several memory sources:



	USER: Bob likes burgers.
	ASSISTANT: Indeed, Bob likes apples.



This is the end of the retrieved message dialogues.

### Successive calls to `get()`[¶](https://docs.llamaindex.ai/en/stable/examples/agent/memory/composable_memory/#successive-calls-to-get)

Successive calls of `get()` will simply replace the loaded `secondary` memory messages in the system prompt.

In \[ \]:

Copied!

msgs \= composable\_memory.get("What does Alice like?")
msgs

msgs = composable\_memory.get("What does Alice like?") msgs

Out\[ \]:

\[ChatMessage(role=<MessageRole.SYSTEM: 'system'>, content='You are a REALLY helpful assistant.\\n\\nBelow are a set of relevant dialogues retrieved from potentially several memory sources:\\n\\n\\n\\n\\tUSER: Alice likes apples.\\n\\n\\n\\nThis is the end of the retrieved message dialogues.', additional\_kwargs={}),
 ChatMessage(role=<MessageRole.USER: 'user'>, content='Jerry likes juice.', additional\_kwargs={})\]

In \[ \]:

Copied!

\# see the memory injected into the system message of the primary memory
print(msgs\[0\])

\# see the memory injected into the system message of the primary memory print(msgs\[0\])

system: You are a REALLY helpful assistant.

Below are a set of relevant dialogues retrieved from potentially several memory sources:



	USER: Alice likes apples.



This is the end of the retrieved message dialogues.

### What if `get()` retrieves `secondary` messages that already exist in `primary` memory?[¶](https://docs.llamaindex.ai/en/stable/examples/agent/memory/composable_memory/#what-if-get-retrieves-secondary-messages-that-already-exist-in-primary-memory)

In the event that messages retrieved from `secondary` memory already exist in `primary` memory, then these rather redundant secondary messages will not get added to the system message. In the below example, the message "Jerry likes juice." was `put` into all memory sources, so the system message is not altered.

In \[ \]:

Copied!

msgs \= composable\_memory.get("What does Jerry like?")
msgs

msgs = composable\_memory.get("What does Jerry like?") msgs

Out\[ \]:

\[ChatMessage(role=<MessageRole.SYSTEM: 'system'>, content='You are a REALLY helpful assistant.', additional\_kwargs={}),
 ChatMessage(role=<MessageRole.USER: 'user'>, content='Jerry likes juice.', additional\_kwargs={})\]

### How to `reset` memory[¶](https://docs.llamaindex.ai/en/stable/examples/agent/memory/composable_memory/#how-to-reset-memory)

Similar to the other methods `put()` and `get()`, calling `reset()` will execute `reset()` on both the `primary` and `secondary` memory sources. If you want to reset only the `primary` then you should call the `reset()` method only from it.

#### `reset()` only primary memory[¶](https://docs.llamaindex.ai/en/stable/examples/agent/memory/composable_memory/#reset-only-primary-memory)

In \[ \]:

Copied!

composable\_memory.primary\_memory.reset()

composable\_memory.primary\_memory.reset()

In \[ \]:

Copied!

composable\_memory.primary\_memory.get()

composable\_memory.primary\_memory.get()

Out\[ \]:

\[\]

In \[ \]:

Copied!

composable\_memory.secondary\_memory\_sources\[0\].get("What does Alice like?")

composable\_memory.secondary\_memory\_sources\[0\].get("What does Alice like?")

Out\[ \]:

\[ChatMessage(role=<MessageRole.USER: 'user'>, content='Alice likes apples.', additional\_kwargs={})\]

#### `reset()` all memory sources[¶](https://docs.llamaindex.ai/en/stable/examples/agent/memory/composable_memory/#reset-all-memory-sources)

In \[ \]:

Copied!

composable\_memory.reset()

composable\_memory.reset()

In \[ \]:

Copied!

composable\_memory.primary\_memory.get()

composable\_memory.primary\_memory.get()

Out\[ \]:

\[\]

In \[ \]:

Copied!

composable\_memory.secondary\_memory\_sources\[0\].get("What does Alice like?")

composable\_memory.secondary\_memory\_sources\[0\].get("What does Alice like?")

Out\[ \]:

\[\]

Use `SimpleComposableMemory` With An Agent[¶](https://docs.llamaindex.ai/en/stable/examples/agent/memory/composable_memory/#use-simplecomposablememory-with-an-agent)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Here we will use a `SimpleComposableMemory` with an agent and demonstrate how a secondary, long-term memory source can be used to use messages from on agent conversation as part of another conversation with another agent session.

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI
from llama\_index.core.tools import FunctionTool
from llama\_index.core.agent import FunctionCallingAgentWorker

import nest\_asyncio

nest\_asyncio.apply()

from llama\_index.llms.openai import OpenAI from llama\_index.core.tools import FunctionTool from llama\_index.core.agent import FunctionCallingAgentWorker import nest\_asyncio nest\_asyncio.apply()

### Define our memory modules[¶](https://docs.llamaindex.ai/en/stable/examples/agent/memory/composable_memory/#define-our-memory-modules)

In \[ \]:

Copied!

vector\_memory \= VectorMemory.from\_defaults(
    vector\_store\=None,  \# leave as None to use default in-memory vector store
    embed\_model\=OpenAIEmbedding(),
    retriever\_kwargs\={"similarity\_top\_k": 2},
)

chat\_memory\_buffer \= ChatMemoryBuffer.from\_defaults()

composable\_memory \= SimpleComposableMemory.from\_defaults(
    primary\_memory\=chat\_memory\_buffer,
    secondary\_memory\_sources\=\[vector\_memory\],
)

vector\_memory = VectorMemory.from\_defaults( vector\_store=None, # leave as None to use default in-memory vector store embed\_model=OpenAIEmbedding(), retriever\_kwargs={"similarity\_top\_k": 2}, ) chat\_memory\_buffer = ChatMemoryBuffer.from\_defaults() composable\_memory = SimpleComposableMemory.from\_defaults( primary\_memory=chat\_memory\_buffer, secondary\_memory\_sources=\[vector\_memory\], )

### Define our Agent[¶](https://docs.llamaindex.ai/en/stable/examples/agent/memory/composable_memory/#define-our-agent)

In \[ \]:

Copied!

def multiply(a: int, b: int) \-> int:
    """Multiply two integers and returns the result integer"""
    return a \* b

def mystery(a: int, b: int) \-> int:
    """Mystery function on two numbers"""
    return a\*\*2 \- b\*\*2

multiply\_tool \= FunctionTool.from\_defaults(fn\=multiply)
mystery\_tool \= FunctionTool.from\_defaults(fn\=mystery)

def multiply(a: int, b: int) -> int: """Multiply two integers and returns the result integer""" return a \* b def mystery(a: int, b: int) -> int: """Mystery function on two numbers""" return a\*\*2 - b\*\*2 multiply\_tool = FunctionTool.from\_defaults(fn=multiply) mystery\_tool = FunctionTool.from\_defaults(fn=mystery)

In \[ \]:

Copied!

llm \= OpenAI(model\="gpt-3.5-turbo-0613")
agent\_worker \= FunctionCallingAgentWorker.from\_tools(
    \[multiply\_tool, mystery\_tool\], llm\=llm, verbose\=True
)
agent \= agent\_worker.as\_agent(memory\=composable\_memory)

llm = OpenAI(model="gpt-3.5-turbo-0613") agent\_worker = FunctionCallingAgentWorker.from\_tools( \[multiply\_tool, mystery\_tool\], llm=llm, verbose=True ) agent = agent\_worker.as\_agent(memory=composable\_memory)

### Execute some function calls[¶](https://docs.llamaindex.ai/en/stable/examples/agent/memory/composable_memory/#execute-some-function-calls)

When `.chat()` is invoked, the messages are put into the composable memory, which we understand from the previous section implies that all the messages are put in both `primary` and `secondary` sources.

In \[ \]:

Copied!

response \= agent.chat("What is the mystery function on 5 and 6?")

response = agent.chat("What is the mystery function on 5 and 6?")

Added user message to memory: What is the mystery function on 5 and 6?

Calling function: mystery with args: {"a": 5, "b": 6}

-11

The mystery function on 5 and 6 returns -11.

In \[ \]:

Copied!

response \= agent.chat("What happens if you multiply 2 and 3?")

response = agent.chat("What happens if you multiply 2 and 3?")

Added user message to memory: What happens if you multiply 2 and 3?

Calling function: multiply with args: {"a": 2, "b": 3}

6

If you multiply 2 and 3, the result is 6.

### New Agent Sessions[¶](https://docs.llamaindex.ai/en/stable/examples/agent/memory/composable_memory/#new-agent-sessions)

Now that we've added the messages to our `vector_memory`, we can see the effect of having this memory be used with a new agent session versus when it is used. Specifically, we ask the new agents to "recall" the outputs of the function calls, rather than re-computing.

#### An Agent without our past memory[¶](https://docs.llamaindex.ai/en/stable/examples/agent/memory/composable_memory/#an-agent-without-our-past-memory)

In \[ \]:

Copied!

llm \= OpenAI(model\="gpt-3.5-turbo-0613")
agent\_worker \= FunctionCallingAgentWorker.from\_tools(
    \[multiply\_tool, mystery\_tool\], llm\=llm, verbose\=True
)
agent\_without\_memory \= agent\_worker.as\_agent()

llm = OpenAI(model="gpt-3.5-turbo-0613") agent\_worker = FunctionCallingAgentWorker.from\_tools( \[multiply\_tool, mystery\_tool\], llm=llm, verbose=True ) agent\_without\_memory = agent\_worker.as\_agent()

In \[ \]:

Copied!

response \= agent\_without\_memory.chat(
    "What was the output of the mystery function on 5 and 6 again? Don't recompute."
)

response = agent\_without\_memory.chat( "What was the output of the mystery function on 5 and 6 again? Don't recompute." )

Added user message to memory: What was the output of the mystery function on 5 and 6 again? Don't recompute.

I'm sorry, but I don't have access to the previous output of the mystery function on 5 and 6.

#### An Agent with our past memory[¶](https://docs.llamaindex.ai/en/stable/examples/agent/memory/composable_memory/#an-agent-with-our-past-memory)

We see that the agent without access to the our past memory cannot complete the task. With this next agent we will indeed pass in our previous long-term memory (i.e., `vector_memory`). Note that we even use a fresh `ChatMemoryBuffer` which means there is no `chat_history` with this agent. Nonetheless, it will be able to retrieve from our long-term memory to get the past dialogue it needs.

In \[ \]:

Copied!

llm \= OpenAI(model\="gpt-3.5-turbo-0613")
agent\_worker \= FunctionCallingAgentWorker.from\_tools(
    \[multiply\_tool, mystery\_tool\], llm\=llm, verbose\=True
)
composable\_memory \= SimpleComposableMemory.from\_defaults(
    primary\_memory\=ChatMemoryBuffer.from\_defaults(),
    secondary\_memory\_sources\=\[
        vector\_memory.copy(
            deep\=True
        )  \# using a copy here for illustration purposes
        \# later will use original vector\_memory again
    \],
)
agent\_with\_memory \= agent\_worker.as\_agent(memory\=composable\_memory)

llm = OpenAI(model="gpt-3.5-turbo-0613") agent\_worker = FunctionCallingAgentWorker.from\_tools( \[multiply\_tool, mystery\_tool\], llm=llm, verbose=True ) composable\_memory = SimpleComposableMemory.from\_defaults( primary\_memory=ChatMemoryBuffer.from\_defaults(), secondary\_memory\_sources=\[ vector\_memory.copy( deep=True ) # using a copy here for illustration purposes # later will use original vector\_memory again \], ) agent\_with\_memory = agent\_worker.as\_agent(memory=composable\_memory)

In \[ \]:

Copied!

agent\_with\_memory.chat\_history  \# an empty chat history

agent\_with\_memory.chat\_history # an empty chat history

Out\[ \]:

\[\]

In \[ \]:

Copied!

response \= agent\_with\_memory.chat(
    "What was the output of the mystery function on 5 and 6 again? Don't recompute."
)

response = agent\_with\_memory.chat( "What was the output of the mystery function on 5 and 6 again? Don't recompute." )

Added user message to memory: What was the output of the mystery function on 5 and 6 again? Don't recompute.

The output of the mystery function on 5 and 6 is -11.

In \[ \]:

Copied!

response \= agent\_with\_memory.chat(
    "What was the output of the multiply function on 2 and 3 again? Don't recompute."
)

response = agent\_with\_memory.chat( "What was the output of the multiply function on 2 and 3 again? Don't recompute." )

Added user message to memory: What was the output of the multiply function on 2 and 3 again? Don't recompute.

The output of the multiply function on 2 and 3 is 6.

In \[ \]:

Copied!

agent\_with\_memory.chat\_history

agent\_with\_memory.chat\_history

Out\[ \]:

\[ChatMessage(role=<MessageRole.USER: 'user'>, content="What was the output of the mystery function on 5 and 6 again? Don't recompute.", additional\_kwargs={}),
 ChatMessage(role=<MessageRole.ASSISTANT: 'assistant'>, content='The output of the mystery function on 5 and 6 is -11.', additional\_kwargs={}),
 ChatMessage(role=<MessageRole.USER: 'user'>, content="What was the output of the multiply function on 2 and 3 again? Don't recompute.", additional\_kwargs={}),
 ChatMessage(role=<MessageRole.ASSISTANT: 'assistant'>, content='The output of the multiply function on 2 and 3 is 6.', additional\_kwargs={})\]

### What happens under the hood with `.chat(user_input)`[¶](https://docs.llamaindex.ai/en/stable/examples/agent/memory/composable_memory/#what-happens-under-the-hood-with-chatuser_input)

Under the hood, `.chat(user_input)` call effectively will call the memory's `.get()` method with `user_input` as the argument. As we learned in the previous section, this will ultimately return a composition of the `primary` and all of the `secondary` memory sources. These composed messages are what is being passed to the LLM's chat API as the chat history.

In \[ \]:

Copied!

composable\_memory \= SimpleComposableMemory.from\_defaults(
    primary\_memory\=ChatMemoryBuffer.from\_defaults(),
    secondary\_memory\_sources\=\[
        vector\_memory.copy(
            deep\=True
        )  \# copy for illustrative purposes to explain what
        \# happened under the hood from previous subsection
    \],
)
agent\_with\_memory \= agent\_worker.as\_agent(memory\=composable\_memory)

composable\_memory = SimpleComposableMemory.from\_defaults( primary\_memory=ChatMemoryBuffer.from\_defaults(), secondary\_memory\_sources=\[ vector\_memory.copy( deep=True ) # copy for illustrative purposes to explain what # happened under the hood from previous subsection \], ) agent\_with\_memory = agent\_worker.as\_agent(memory=composable\_memory)

In \[ \]:

Copied!

agent\_with\_memory.memory.get(
    "What was the output of the mystery function on 5 and 6 again? Don't recompute."
)

agent\_with\_memory.memory.get( "What was the output of the mystery function on 5 and 6 again? Don't recompute." )

Out\[ \]:

\[ChatMessage(role=<MessageRole.SYSTEM: 'system'>, content='You are a helpful assistant.\\n\\nBelow are a set of relevant dialogues retrieved from potentially several memory sources:\\n\\n\\n\\n\\tUSER: What is the mystery function on 5 and 6?\\n\\tASSISTANT: None\\n\\tTOOL: -11\\n\\tASSISTANT: The mystery function on 5 and 6 returns -11.\\n\\n\\n\\nThis is the end of the retrieved message dialogues.', additional\_kwargs={})\]

In \[ \]:

Copied!

print(
    agent\_with\_memory.memory.get(
        "What was the output of the mystery function on 5 and 6 again? Don't recompute."
    )\[0\]
)

print( agent\_with\_memory.memory.get( "What was the output of the mystery function on 5 and 6 again? Don't recompute." )\[0\] )

system: You are a helpful assistant.

Below are a set of relevant dialogues retrieved from potentially several memory sources:



	USER: What is the mystery function on 5 and 6?
	ASSISTANT: None
	TOOL: -11
	ASSISTANT: The mystery function on 5 and 6 returns -11.



This is the end of the retrieved message dialogues.

Back to top

[Previous LLM Compiler Agent Cookbook](https://docs.llamaindex.ai/en/stable/examples/agent/llm_compiler/)[Next Vector Memory](https://docs.llamaindex.ai/en/stable/examples/agent/memory/vector_memory/)

Hi, how can I help you?

🦙
