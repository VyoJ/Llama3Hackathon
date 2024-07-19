Title: Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/llms/

Markdown Content:
Index - LlamaIndex


LLM [#](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM "Permanent link")
----------------------------------------------------------------------------------------------------------------

Bases: `BaseLLM`

The LLM class is the main class for interacting with language models.

**Attributes:**

| Name | Type | Description |
| --- | --- | --- |
| `system_prompt` | `Optional[str]` | 
System prompt for LLM calls.



 |
| `messages_to_prompt` | `Callable` | 

Function to convert a list of messages to an LLM prompt.



 |
| `completion_to_prompt` | `Callable` | 

Function to convert a completion to an LLM prompt.



 |
| `output_parser` | `Optional[[BaseOutputParser](https://docs.llamaindex.ai/en/stable/api_reference/output_parsers/#llama_index.core.types.BaseOutputParser "llama_index.core.types.BaseOutputParser")]` | 

Output parser to parse, validate, and correct errors programmatically.



 |
| `pydantic_program_mode` | `PydanticProgramMode` | 

Pydantic program mode to use for structured prediction.



 |

### metadata `abstractmethod` `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM.metadata "Permanent link")

```
metadata: LLMMetadata
```

LLM metadata.

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `LLMMetadata` | `LLMMetadata` | 
LLM metadata containing various information about the LLM.



 |

### class\_name `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM.class_name "Permanent link")

```
class_name() -> str
```

Get the class name, used as a unique ID in serialization.

This provides a key that makes serialization robust against actual class name changes.

### as\_query\_component [#](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM.as_query_component "Permanent link")

```
as_query_component(partial: Optional[Dict[str, Any]] = None, **kwargs: Any) -> [QueryComponent](https://docs.llamaindex.ai/en/stable/api_reference/query_pipeline/#llama_index.core.base.query_pipeline.query.QueryComponent "llama_index.core.base.query_pipeline.query.QueryComponent")
```

Get query component.

### chat `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM.chat "Permanent link")

```
chat(messages: Sequence[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")], **kwargs: Any) -> ChatResponse
```

Chat endpoint for LLM.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `messages` | `Sequence[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]` | 
Sequence of chat messages.



 | _required_ |
| `kwargs` | `Any` | 

Additional keyword arguments to pass to the LLM.



 | `{}` |

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `ChatResponse` | `ChatResponse` | 
Chat response from the LLM.



 |

**Examples:**

```
from llama_index.core.llms import ChatMessage

response = llm.chat([ChatMessage(role="user", content="Hello")])
print(response.content)
```

### complete `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM.complete "Permanent link")

```
complete(prompt: str, formatted: bool = False, **kwargs: Any) -> CompletionResponse
```

Completion endpoint for LLM.

If the LLM is a chat model, the prompt is transformed into a single `user` message.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `prompt` | `str` | 
Prompt to send to the LLM.



 | _required_ |
| `formatted` | `bool` | 

Whether the prompt is already formatted for the LLM, by default False.



 | `False` |
| `kwargs` | `Any` | 

Additional keyword arguments to pass to the LLM.



 | `{}` |

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `CompletionResponse` | `CompletionResponse` | 
Completion response from the LLM.



 |

**Examples:**

```
response = llm.complete("your prompt")
print(response.text)
```

### stream\_chat `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM.stream_chat "Permanent link")

```
stream_chat(messages: Sequence[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")], **kwargs: Any) -> ChatResponseGen
```

Streaming chat endpoint for LLM.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `messages` | `Sequence[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]` | 
Sequence of chat messages.



 | _required_ |
| `kwargs` | `Any` | 

Additional keyword arguments to pass to the LLM.



 | `{}` |

**Yields:**

| Name | Type | Description |
| --- | --- | --- |
| `ChatResponse` | `ChatResponseGen` | 
A generator of ChatResponse objects, each containing a new token of the response.



 |

**Examples:**

```
from llama_index.core.llms import ChatMessage

gen = llm.stream_chat([ChatMessage(role="user", content="Hello")])
for response in gen:
    print(response.delta, end="", flush=True)
```

### stream\_complete `abstractmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM.stream_complete "Permanent link")

```
stream_complete(prompt: str, formatted: bool = False, **kwargs: Any) -> CompletionResponseGen
```

Streaming completion endpoint for LLM.

If the LLM is a chat model, the prompt is transformed into a single `user` message.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `prompt` | `str` | 
Prompt to send to the LLM.



 | _required_ |
| `formatted` | `bool` | 

Whether the prompt is already formatted for the LLM, by default False.



 | `False` |
| `kwargs` | `Any` | 

Additional keyword arguments to pass to the LLM.



 | `{}` |

**Yields:**

| Name | Type | Description |
| --- | --- | --- |
| `CompletionResponse` | `CompletionResponseGen` | 
A generator of CompletionResponse objects, each containing a new token of the response.



 |

**Examples:**

```
gen = llm.stream_complete("your prompt")
for response in gen:
    print(response.text, end="", flush=True)
```

### achat `abstractmethod` `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM.achat "Permanent link")

```
achat(messages: Sequence[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")], **kwargs: Any) -> ChatResponse
```

Async chat endpoint for LLM.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `messages` | `Sequence[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]` | 
Sequence of chat messages.



 | _required_ |
| `kwargs` | `Any` | 

Additional keyword arguments to pass to the LLM.



 | `{}` |

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `ChatResponse` | `ChatResponse` | 
Chat response from the LLM.



 |

**Examples:**

```
from llama_index.core.llms import ChatMessage

response = await llm.achat([ChatMessage(role="user", content="Hello")])
print(response.content)
```

### acomplete `abstractmethod` `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM.acomplete "Permanent link")

```
acomplete(prompt: str, formatted: bool = False, **kwargs: Any) -> CompletionResponse
```

Async completion endpoint for LLM.

If the LLM is a chat model, the prompt is transformed into a single `user` message.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `prompt` | `str` | 
Prompt to send to the LLM.



 | _required_ |
| `formatted` | `bool` | 

Whether the prompt is already formatted for the LLM, by default False.



 | `False` |
| `kwargs` | `Any` | 

Additional keyword arguments to pass to the LLM.



 | `{}` |

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `CompletionResponse` | `CompletionResponse` | 
Completion response from the LLM.



 |

**Examples:**

```
response = await llm.acomplete("your prompt")
print(response.text)
```

### astream\_chat `abstractmethod` `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM.astream_chat "Permanent link")

```
astream_chat(messages: Sequence[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")], **kwargs: Any) -> ChatResponseAsyncGen
```

Async streaming chat endpoint for LLM.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `messages` | `Sequence[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]` | 
Sequence of chat messages.



 | _required_ |
| `kwargs` | `Any` | 

Additional keyword arguments to pass to the LLM.



 | `{}` |

**Yields:**

| Name | Type | Description |
| --- | --- | --- |
| `ChatResponse` | `ChatResponseAsyncGen` | 
An async generator of ChatResponse objects, each containing a new token of the response.



 |

**Examples:**

```
from llama_index.core.llms import ChatMessage

gen = await llm.astream_chat([ChatMessage(role="user", content="Hello")])
async for response in gen:
    print(response.delta, end="", flush=True)
```

### astream\_complete `abstractmethod` `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM.astream_complete "Permanent link")

```
astream_complete(prompt: str, formatted: bool = False, **kwargs: Any) -> CompletionResponseAsyncGen
```

Async streaming completion endpoint for LLM.

If the LLM is a chat model, the prompt is transformed into a single `user` message.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `prompt` | `str` | 
Prompt to send to the LLM.



 | _required_ |
| `formatted` | `bool` | 

Whether the prompt is already formatted for the LLM, by default False.



 | `False` |
| `kwargs` | `Any` | 

Additional keyword arguments to pass to the LLM.



 | `{}` |

**Yields:**

| Name | Type | Description |
| --- | --- | --- |
| `CompletionResponse` | `CompletionResponseAsyncGen` | 
An async generator of CompletionResponse objects, each containing a new token of the response.



 |

**Examples:**

```
gen = await llm.astream_complete("your prompt")
async for response in gen:
    print(response.text, end="", flush=True)
```

### structured\_predict [#](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM.structured_predict "Permanent link")

```
structured_predict(output_cls: BaseModel, prompt: [PromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.PromptTemplate "llama_index.core.prompts.PromptTemplate"), **prompt_args: Any) -> BaseModel
```

Structured predict.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `output_cls` | `BaseModel` | 
Output class to use for structured prediction.



 | _required_ |
| `prompt` | `[PromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.PromptTemplate "llama_index.core.prompts.PromptTemplate")` | 

Prompt template to use for structured prediction.



 | _required_ |
| `prompt_args` | `Any` | 

Additional arguments to format the prompt with.



 | `{}` |

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `BaseModel` | `BaseModel` | 
The structured prediction output.



 |

**Examples:**

```
from pydantic.v1 import BaseModel

class Test(BaseModel):
    \"\"\"My test class.\"\"\"
    name: str

from llama_index.core.prompts import PromptTemplate

prompt = PromptTemplate("Please predict a Test with a random name related to {topic}.")
output = llm.structured_predict(Test, prompt, topic="cats")
print(output.name)
```

### astructured\_predict `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM.astructured_predict "Permanent link")

```
astructured_predict(output_cls: BaseModel, prompt: [PromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.PromptTemplate "llama_index.core.prompts.PromptTemplate"), **prompt_args: Any) -> BaseModel
```

Async Structured predict.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `output_cls` | `BaseModel` | 
Output class to use for structured prediction.



 | _required_ |
| `prompt` | `[PromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.PromptTemplate "llama_index.core.prompts.PromptTemplate")` | 

Prompt template to use for structured prediction.



 | _required_ |
| `prompt_args` | `Any` | 

Additional arguments to format the prompt with.



 | `{}` |

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `BaseModel` | `BaseModel` | 
The structured prediction output.



 |

**Examples:**

```
from pydantic.v1 import BaseModel

class Test(BaseModel):
    \"\"\"My test class.\"\"\"
    name: str

from llama_index.core.prompts import PromptTemplate

prompt = PromptTemplate("Please predict a Test with a random name related to {topic}.")
output = await llm.astructured_predict(Test, prompt, topic="cats")
print(output.name)
```

### predict [#](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM.predict "Permanent link")

```
predict(prompt: [BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate"), **prompt_args: Any) -> str
```

Predict for a given prompt.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `prompt` | `[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")` | 
The prompt to use for prediction.



 | _required_ |
| `prompt_args` | `Any` | 

Additional arguments to format the prompt with.



 | `{}` |

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `str` | `str` | 
The prediction output.



 |

**Examples:**

```
from llama_index.core.prompts import PromptTemplate

prompt = PromptTemplate("Please write a random name related to {topic}.")
output = llm.predict(prompt, topic="cats")
print(output)
```

### stream [#](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM.stream "Permanent link")

```
stream(prompt: [BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate"), **prompt_args: Any) -> TokenGen
```

Stream predict for a given prompt.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `prompt` | `[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")` | 
The prompt to use for prediction.



 | _required_ |
| `prompt_args` | `Any` | 

Additional arguments to format the prompt with.



 | `{}` |

**Yields:**

| Name | Type | Description |
| --- | --- | --- |
| `str` | `TokenGen` | 
Each streamed token.



 |

**Examples:**

```
from llama_index.core.prompts import PromptTemplate

prompt = PromptTemplate("Please write a random name related to {topic}.")
gen = llm.stream_predict(prompt, topic="cats")
for token in gen:
    print(token, end="", flush=True)
```

### apredict `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM.apredict "Permanent link")

```
apredict(prompt: [BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate"), **prompt_args: Any) -> str
```

Async Predict for a given prompt.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `prompt` | `[BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate")` | 
The prompt to use for prediction.



 | _required_ |
| `prompt_args` | `Any` | 

Additional arguments to format the prompt with.



 | `{}` |

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `str` | `str` | 
The prediction output.



 |

**Examples:**

```
from llama_index.core.prompts import PromptTemplate

prompt = PromptTemplate("Please write a random name related to {topic}.")
output = await llm.apredict(prompt, topic="cats")
print(output)
```

### astream `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM.astream "Permanent link")

```
astream(prompt: [BasePromptTemplate](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.BasePromptTemplate "llama_index.core.prompts.BasePromptTemplate"), **prompt_args: Any) -> TokenAsyncGen
```

Async stream predict for a given prompt.

prompt (BasePromptTemplate): The prompt to use for prediction. prompt\_args (Any): Additional arguments to format the prompt with.

**Yields:**

| Name | Type | Description |
| --- | --- | --- |
| `str` | `TokenAsyncGen` | 
An async generator that yields strings of tokens.



 |

**Examples:**

```
from llama_index.core.prompts import PromptTemplate

prompt = PromptTemplate("Please write a random name related to {topic}.")
gen = await llm.astream_predict(prompt, topic="cats")
async for token in gen:
    print(token, end="", flush=True)
```

### predict\_and\_call [#](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM.predict_and_call "Permanent link")

```
predict_and_call(tools: List[[BaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.BaseTool "llama_index.core.tools.types.BaseTool")], user_msg: Optional[Union[str, [ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]] = None, chat_history: Optional[List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]] = None, verbose: bool = False, **kwargs: Any) -> [AgentChatResponse](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.AgentChatResponse "llama_index.core.chat_engine.types.AgentChatResponse")
```

Predict and call the tool.

By default uses a ReAct agent to do tool calling (through text prompting), but function calling LLMs will implement this differently.

### apredict\_and\_call `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/llms/#llama_index.core.llms.llm.LLM.apredict_and_call "Permanent link")

```
apredict_and_call(tools: List[[BaseTool](https://docs.llamaindex.ai/en/stable/api_reference/tools/#llama_index.core.tools.types.BaseTool "llama_index.core.tools.types.BaseTool")], user_msg: Optional[Union[str, [ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]] = None, chat_history: Optional[List[[ChatMessage](https://docs.llamaindex.ai/en/stable/api_reference/prompts/#llama_index.core.prompts.ChatMessage "llama_index.core.base.llms.types.ChatMessage")]] = None, verbose: bool = False, **kwargs: Any) -> [AgentChatResponse](https://docs.llamaindex.ai/en/stable/api_reference/chat_engines/#llama_index.core.chat_engine.types.AgentChatResponse "llama_index.core.chat_engine.types.AgentChatResponse")
```

Predict and call the tool.

Back to top

[Previous Ibm](https://docs.llamaindex.ai/en/stable/api_reference/llms/ibm/)[Next Ipex llm](https://docs.llamaindex.ai/en/stable/api_reference/llms/ipex_llm/)
