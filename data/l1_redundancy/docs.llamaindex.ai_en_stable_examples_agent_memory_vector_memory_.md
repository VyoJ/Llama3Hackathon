Title: Vector Memory - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/memory/vector_memory/

Markdown Content:
Vector Memory - LlamaIndex


The vector memory module uses vector search (backed by a vector db) to retrieve relevant conversation items given a user input.

This notebook shows you how to use the `VectorMemory` class. We show you how to use its individual functions. A typical usecase for vector memory is as a long-term memory storage of chat messages. You can

![Image 4: VectorMemoryIllustration](https://d3ddy8balm3goa.cloudfront.net/llamaindex/vector-memory.excalidraw.svg)

### Initialize and Experiment with Memory Module[¶](https://docs.llamaindex.ai/en/stable/examples/agent/memory/vector_memory/#initialize-and-experiment-with-memory-module)

Here we initialize a raw memory module and demonstrate its functions - to put and retrieve from ChatMessage objects.

*   Note that `retriever_kwargs` is the same args you'd specify on the `VectorIndexRetriever` or from `index.as_retriever(..)`.

In \[ \]:

Copied!

from llama\_index.core.memory import VectorMemory
from llama\_index.embeddings.openai import OpenAIEmbedding

vector\_memory \= VectorMemory.from\_defaults(
    vector\_store\=None,  \# leave as None to use default in-memory vector store
    embed\_model\=OpenAIEmbedding(),
    retriever\_kwargs\={"similarity\_top\_k": 1},
)

from llama\_index.core.memory import VectorMemory from llama\_index.embeddings.openai import OpenAIEmbedding vector\_memory = VectorMemory.from\_defaults( vector\_store=None, # leave as None to use default in-memory vector store embed\_model=OpenAIEmbedding(), retriever\_kwargs={"similarity\_top\_k": 1}, )

In \[ \]:

Copied!

from llama\_index.core.llms import ChatMessage

msgs \= \[
    ChatMessage.from\_str("Jerry likes juice.", "user"),
    ChatMessage.from\_str("Bob likes burgers.", "user"),
    ChatMessage.from\_str("Alice likes apples.", "user"),
\]

from llama\_index.core.llms import ChatMessage msgs = \[ ChatMessage.from\_str("Jerry likes juice.", "user"), ChatMessage.from\_str("Bob likes burgers.", "user"), ChatMessage.from\_str("Alice likes apples.", "user"), \]

In \[ \]:

Copied!

\# load into memory
for m in msgs:
    vector\_memory.put(m)

\# load into memory for m in msgs: vector\_memory.put(m)

In \[ \]:

Copied!

\# retrieve from memory
msgs \= vector\_memory.get("What does Jerry like?")
msgs

\# retrieve from memory msgs = vector\_memory.get("What does Jerry like?") msgs

Out\[ \]:

\[ChatMessage(role=<MessageRole.USER: 'user'>, content='Jerry likes juice.', additional\_kwargs={})\]

In \[ \]:

Copied!

vector\_memory.reset()

vector\_memory.reset()

Now let's try resetting and trying again. This time, we'll add an assistant message. Note that user/assistant messages are bundled by default.

In \[ \]:

Copied!

msgs \= \[
    ChatMessage.from\_str("Jerry likes burgers.", "user"),
    ChatMessage.from\_str("Bob likes apples.", "user"),
    ChatMessage.from\_str("Indeed, Bob likes apples.", "assistant"),
    ChatMessage.from\_str("Alice likes juice.", "user"),
\]
vector\_memory.set(msgs)

msgs = \[ ChatMessage.from\_str("Jerry likes burgers.", "user"), ChatMessage.from\_str("Bob likes apples.", "user"), ChatMessage.from\_str("Indeed, Bob likes apples.", "assistant"), ChatMessage.from\_str("Alice likes juice.", "user"), \] vector\_memory.set(msgs)

In \[ \]:

Copied!

msgs \= vector\_memory.get("What does Bob like?")
msgs

msgs = vector\_memory.get("What does Bob like?") msgs

Out\[ \]:

\[ChatMessage(role=<MessageRole.USER: 'user'>, content='Bob likes apples.', additional\_kwargs={}),
 ChatMessage(role=<MessageRole.ASSISTANT: 'assistant'>, content='Indeed, Bob likes apples.', additional\_kwargs={})\]

Back to top

[Previous Simple Composable Memory](https://docs.llamaindex.ai/en/stable/examples/agent/memory/composable_memory/)[Next Function Calling Mistral Agent](https://docs.llamaindex.ai/en/stable/examples/agent/mistral_agent/)

Hi, how can I help you?

🦙
