Title: RunGPT - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/llm/rungpt/

Markdown Content:
RunGPT - LlamaIndex


RunGPT is an open-source cloud-native large-scale multimodal models (LMMs) serving framework. It is designed to simplify the deployment and management of large language models, on a distributed cluster of GPUs. RunGPT aim to make it a one-stop solution for a centralized and accessible place to gather techniques for optimizing large-scale multimodal models and make them easy to use for everyone. In RunGPT, we have supported a number of LLMs such as LLaMA, Pythia, StableLM, Vicuna, MOSS, and Large Multi-modal Model(LMMs) like MiniGPT-4 and OpenFlamingo additionally.

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/llm/rungpt/#setup)


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-rungpt

%pip install llama-index-llms-rungpt

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

You need to install rungpt package in your python environment with `pip install`

In \[ \]:

Copied!

!pip install rungpt

!pip install rungpt

After installing successfully, models supported by RunGPT can be deployed with an one-line command. This option will download target language model from open source platform and deploy it as a service at a localhost port, which can be accessed by http or grpc requests. I suppose you not run this command in jupyter book, but in command line instead.

In \[ \]:

Copied!

!rungpt serve decapoda\-research/llama\-7b\-hf \--precision fp16 \--device\_map balanced

!rungpt serve decapoda-research/llama-7b-hf --precision fp16 --device\_map balanced

Basic Usage[¶](https://docs.llamaindex.ai/en/stable/examples/llm/rungpt/#basic-usage)
-------------------------------------------------------------------------------------

#### Call `complete` with a prompt[¶](https://docs.llamaindex.ai/en/stable/examples/llm/rungpt/#call-complete-with-a-prompt)

In \[ \]:

Copied!

from llama\_index.llms.rungpt import RunGptLLM

llm \= RunGptLLM()
promot \= "What public transportation might be available in a city?"
response \= llm.complete(promot)

from llama\_index.llms.rungpt import RunGptLLM llm = RunGptLLM() promot = "What public transportation might be available in a city?" response = llm.complete(promot)

In \[ \]:

Copied!

print(response)

print(response)

I don't want to go to work, so what should I do?
I have a job interview on Monday. What can I wear that will make me look professional but not too stuffy or boring?

#### Call `chat` with a list of messages[¶](https://docs.llamaindex.ai/en/stable/examples/llm/rungpt/#call-chat-with-a-list-of-messages)

In \[ \]:

Copied!

from llama\_index.core.llms import ChatMessage, MessageRole
from llama\_index.llms.rungpt import RunGptLLM

messages \= \[
    ChatMessage(
        role\=MessageRole.USER,
        content\="Now, I want you to do some math for me.",
    ),
    ChatMessage(
        role\=MessageRole.ASSISTANT, content\="Sure, I would like to help you."
    ),
    ChatMessage(
        role\=MessageRole.USER,
        content\="How many points determine a straight line?",
    ),
\]
llm \= RunGptLLM()
response \= llm.chat(messages\=messages, temperature\=0.8, max\_tokens\=15)

from llama\_index.core.llms import ChatMessage, MessageRole from llama\_index.llms.rungpt import RunGptLLM messages = \[ ChatMessage( role=MessageRole.USER, content="Now, I want you to do some math for me.", ), ChatMessage( role=MessageRole.ASSISTANT, content="Sure, I would like to help you." ), ChatMessage( role=MessageRole.USER, content="How many points determine a straight line?", ), \] llm = RunGptLLM() response = llm.chat(messages=messages, temperature=0.8, max\_tokens=15)

In \[ \]:

Copied!

print(response)

print(response)

Streaming[¶](https://docs.llamaindex.ai/en/stable/examples/llm/rungpt/#streaming)
---------------------------------------------------------------------------------

Using `stream_complete` endpoint

In \[ \]:

Copied!

promot \= "What public transportation might be available in a city?"
response \= RunGptLLM().stream\_complete(promot)
for item in response:
    print(item.text)

promot = "What public transportation might be available in a city?" response = RunGptLLM().stream\_complete(promot) for item in response: print(item.text)

Using `stream_chat` endpoint

In \[ \]:

Copied!

from llama\_index.llms.rungpt import RunGptLLM

messages \= \[
    ChatMessage(
        role\=MessageRole.USER,
        content\="Now, I want you to do some math for me.",
    ),
    ChatMessage(
        role\=MessageRole.ASSISTANT, content\="Sure, I would like to help you."
    ),
    ChatMessage(
        role\=MessageRole.USER,
        content\="How many points determine a straight line?",
    ),
\]
response \= RunGptLLM().stream\_chat(messages\=messages)

from llama\_index.llms.rungpt import RunGptLLM messages = \[ ChatMessage( role=MessageRole.USER, content="Now, I want you to do some math for me.", ), ChatMessage( role=MessageRole.ASSISTANT, content="Sure, I would like to help you." ), ChatMessage( role=MessageRole.USER, content="How many points determine a straight line?", ), \] response = RunGptLLM().stream\_chat(messages=messages)

In \[ \]:

Copied!

for item in response:
    print(item.message)

for item in response: print(item.message)

Back to top

[Previous Client of Baidu Intelligent Cloud's Qianfan LLM Platform](https://docs.llamaindex.ai/en/stable/examples/llm/qianfan/)[Next Interacting with LLM deployed in Amazon SageMaker Endpoint with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/llm/sagemaker_endpoint_llm/)

Hi, how can I help you?

🦙
