Title: OctoAI - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/llm/octoai/

Markdown Content:
OctoAI - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-octoai
%pip install llama\-index
%pip install octoai\-sdk

%pip install llama-index-llms-octoai %pip install llama-index %pip install octoai-sdk

Include your OctoAI API key below. You can get yours at [OctoAI](https://octo.ai/).

[Here](https://octo.ai/docs/getting-started/how-to-create-an-octoai-access-token) are some instructions in case you need more guidance.

In \[ \]:

Copied!

OCTOAI\_API\_KEY \= ""

OCTOAI\_API\_KEY = ""

#### Initialize the Integration with the default model[¶](https://docs.llamaindex.ai/en/stable/examples/llm/octoai/#initialize-the-integration-with-the-default-model)

In \[ \]:

Copied!

from llama\_index.llms.octoai import OctoAI

octoai \= OctoAI(token\=OCTOAI\_API\_KEY)

from llama\_index.llms.octoai import OctoAI octoai = OctoAI(token=OCTOAI\_API\_KEY)

#### Call `complete` with a prompt[¶](https://docs.llamaindex.ai/en/stable/examples/llm/octoai/#call-complete-with-a-prompt)

In \[ \]:

Copied!

response \= octoai.complete("Paul Graham is ")
print(response)

response = octoai.complete("Paul Graham is ") print(response)

#### Call `chat` with a list of messages[¶](https://docs.llamaindex.ai/en/stable/examples/llm/octoai/#call-chat-with-a-list-of-messages)

In \[ \]:

Copied!

from llama\_index.core.llms import ChatMessage

messages \= \[
    ChatMessage(
        role\="system",
        content\="Below is an instruction that describes a task. Write a response that appropriately completes the request.",
    ),
    ChatMessage(role\="user", content\="Write a blog about Seattle"),
\]
response \= octoai.chat(messages)
print(response)

from llama\_index.core.llms import ChatMessage messages = \[ ChatMessage( role="system", content="Below is an instruction that describes a task. Write a response that appropriately completes the request.", ), ChatMessage(role="user", content="Write a blog about Seattle"), \] response = octoai.chat(messages) print(response)

Streaming[¶](https://docs.llamaindex.ai/en/stable/examples/llm/octoai/#streaming)
---------------------------------------------------------------------------------

Using `stream_complete` endpoint

In \[ \]:

Copied!

response \= octoai.stream\_complete("Paul Graham is ")
for r in response:
    print(r.delta, end\="")

response = octoai.stream\_complete("Paul Graham is ") for r in response: print(r.delta, end="")

Using `stream_chat` with a list of messages

In \[ \]:

Copied!

from llama\_index.core.llms import ChatMessage

messages \= \[
    ChatMessage(
        role\="system",
        content\="Below is an instruction that describes a task. Write a response that appropriately completes the request.",
    ),
    ChatMessage(role\="user", content\="Write a blog about Seattle"),
\]
response \= octoai.stream\_chat(messages)
for r in response:
    print(r.delta, end\="")

from llama\_index.core.llms import ChatMessage messages = \[ ChatMessage( role="system", content="Below is an instruction that describes a task. Write a response that appropriately completes the request.", ), ChatMessage(role="user", content="Write a blog about Seattle"), \] response = octoai.stream\_chat(messages) for r in response: print(r.delta, end="")

Configure Model[¶](https://docs.llamaindex.ai/en/stable/examples/llm/octoai/#configure-model)
---------------------------------------------------------------------------------------------

In \[ \]:

Copied!

\# To customize your API token, do this
\# otherwise it will lookup OCTOAI\_TOKEN from your env variable
octoai \= OctoAI(
    model\="mistral-7b-instruct", max\_tokens\=128, token\=OCTOAI\_API\_KEY
)

response \= octoai.complete("Paul Graham is ")
print(response)

\# To customize your API token, do this # otherwise it will lookup OCTOAI\_TOKEN from your env variable octoai = OctoAI( model="mistral-7b-instruct", max\_tokens=128, token=OCTOAI\_API\_KEY ) response = octoai.complete("Paul Graham is ") print(response)

Back to top

[Previous Oracle Cloud Infrastructure Generative AI](https://docs.llamaindex.ai/en/stable/examples/llm/oci_genai/)[Next Ollama - Llama 3](https://docs.llamaindex.ai/en/stable/examples/llm/ollama/)
