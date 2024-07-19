Title: Standalone Usage - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/module_guides/models/llms/usage_standalone/

Markdown Content:
Standalone Usage - LlamaIndex


You can use our LLM modules on their own.

Text Completion Example[#](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/usage_standalone/#text-completion-example "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------

```
from llama_index.llms.openai import OpenAI

# non-streaming
completion = OpenAI().complete("Paul Graham is ")
print(completion)

# using streaming endpoint
from llama_index.llms.openai import OpenAI

llm = OpenAI()
completions = llm.stream_complete("Paul Graham is ")
for completion in completions:
    print(completion.delta, end="")
```

Chat Example[#](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/usage_standalone/#chat-example "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------

```
from llama_index.core.llms import ChatMessage
from llama_index.llms.openai import OpenAI

messages = [
    ChatMessage(
        role="system", content="You are a pirate with a colorful personality"
    ),
    ChatMessage(role="user", content="What is your name"),
]
resp = OpenAI().chat(messages)
print(resp)
```

Check out our [modules section](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/modules/) for usage guides for each LLM.

Back to top

[Previous Using LLMs](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/)[Next Customizing LLMs](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/usage_custom/)
