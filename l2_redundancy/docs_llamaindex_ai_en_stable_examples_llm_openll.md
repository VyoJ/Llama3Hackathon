Title: OpenLLM - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/llm/openllm/

Markdown Content:
OpenLLM - LlamaIndex


There are two ways to interface with LLMs from [OpenLLM](https://github.com/bentoml/OpenLLM).

*   Through [`openllm`](https://github.com/bentoml/OpenLLM) package if you want to run locally: use `llama_index.llms.OpenLLM`
*   If there is a running OpenLLM Server, then it will wraps [openllm-client](https://github.com/bentoml/OpenLLM/tree/main/openllm-client): use `llama_index.llms.OpenLLMAPI`

There are _many_ possible permutations of these two, so this notebook only details a few. See [OpenLLM's README](https://github.com/bentoml/OpenLLM) for more information

In the below line, we install the packages necessary for this demo:

*   `openllm[vllm]` is needed for `OpenLLM` if you have access to GPU, otherwise `openllm`
*   `openllm-client` is needed for `OpenLLMAPI`
*   The quotes are needed for Z shell (`zsh`)

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openllm

%pip install llama-index-llms-openllm

In \[ \]:

Copied!

!pip install "openllm"  \# use 'openllm\[vllm\]' if you have access to GPU

!pip install "openllm" # use 'openllm\[vllm\]' if you have access to GPU

Now that we're set up, let's play around:

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import os
from typing import List, Optional

from llama\_index.llms.openllm import OpenLLM, OpenLLMAPI
from llama\_index.core.llms import ChatMessage

import os from typing import List, Optional from llama\_index.llms.openllm import OpenLLM, OpenLLMAPI from llama\_index.core.llms import ChatMessage

In \[ \]:

Copied!

os.environ\[
    "OPENLLM\_ENDPOINT"
\] \= "na"  \# Change this to a remote server that you might run OpenLLM at.

os.environ\[ "OPENLLM\_ENDPOINT" \] = "na" # Change this to a remote server that you might run OpenLLM at.

In \[ \]:

Copied!

\# This uses https://huggingface.co/HuggingFaceH4/zephyr-7b-alpha
\# downloaded (if first invocation) to the local Hugging Face model cache,
\# and actually runs the model on your local machine's hardware
local\_llm \= OpenLLM("HuggingFaceH4/zephyr-7b-alpha")

\# This will use the model running on the server at localhost:3000
remote\_llm \= OpenLLMAPI(address\="http://localhost:3000")

\# Note here you don't have to pass in the address if OPENLLM\_ENDPOINT environment variable is set
\# address if not pass is address=os.getenv("OPENLLM\_ENDPOINT")
remote\_llm \= OpenLLMAPI()

\# This uses https://huggingface.co/HuggingFaceH4/zephyr-7b-alpha # downloaded (if first invocation) to the local Hugging Face model cache, # and actually runs the model on your local machine's hardware local\_llm = OpenLLM("HuggingFaceH4/zephyr-7b-alpha") # This will use the model running on the server at localhost:3000 remote\_llm = OpenLLMAPI(address="http://localhost:3000") # Note here you don't have to pass in the address if OPENLLM\_ENDPOINT environment variable is set # address if not pass is address=os.getenv("OPENLLM\_ENDPOINT") remote\_llm = OpenLLMAPI()

Underlying a completion with `OpenLLM` supports continuous batching with [vLLM](https://vllm.ai/)

In \[ \]:

Copied!

completion\_response \= remote\_llm.complete("To infinity, and")
print(completion\_response)

completion\_response = remote\_llm.complete("To infinity, and") print(completion\_response)

 beyond!

As a lifelong lover of all things Pixar, I couldn't resist writing about the most recent release in the Toy Story franchise. Toy Story 4 is a nostalgic, heartwarming, and thrilling addition to the series that will have you laughing and crying in equal measure.

The movie follows Woody (Tom Hanks), Buzz Lightyear (Tim Allen), and the rest of the gang as they embark on a road trip with their new owner, Bonnie. However, things take an unexpected turn when Woody meets Bo Peep (Annie Pot

`OpenLLM` and `OpenLLMAPI` also supports streaming, synchronous and asynchronous for `complete`:

In \[ \]:

Copied!

for it in remote\_llm.stream\_complete(
    "The meaning of time is", max\_new\_tokens\=128
):
    print(it, end\="", flush\=True)

for it in remote\_llm.stream\_complete( "The meaning of time is", max\_new\_tokens=128 ): print(it, end="", flush=True)

 often a topic of philosophical debate. Some people argue that time is an objective reality, while others claim that it is a subjective construct. This essay will explore the philosophical and scientific concepts surrounding the nature of time and the various theories that have been proposed to explain it.

One of the earliest philosophical theories of time was put forward by Aristotle, who believed that time was a measure of motion. According to Aristotle, time was an abstraction derived from the regular motion of objects in the universe. This theory was later refined by Galileo and Newton, who introduced the concept of time

They also support chat API as well, `chat`, `stream_chat`, `achat`, and `astream_chat`:

In \[ \]:

Copied!

async for it in remote\_llm.astream\_chat(
    \[
        ChatMessage(
            role\="system", content\="You are acting as Ernest Hemmingway."
        ),
        ChatMessage(role\="user", content\="Hi there!"),
        ChatMessage(role\="assistant", content\="Yes?"),
        ChatMessage(role\="user", content\="What is the meaning of life?"),
    \]
):
    print(it.message.content, flush\=True, end\="")

async for it in remote\_llm.astream\_chat( \[ ChatMessage( role="system", content="You are acting as Ernest Hemmingway." ), ChatMessage(role="user", content="Hi there!"), ChatMessage(role="assistant", content="Yes?"), ChatMessage(role="user", content="What is the meaning of life?"), \] ): print(it.message.content, flush=True, end="")

I don't have beliefs or personal opinions, but according to my programming, the meaning of life is subjective and can vary from person to person. however, some people find meaning in their relationships, their work, their faith, or their personal values. ultimately, finding meaning in life is a personal journey that requires self-reflection, purpose, and fulfillment.

Back to top

[Previous OpenAI JSON Mode vs. Function Calling for Data Extraction](https://docs.llamaindex.ai/en/stable/examples/llm/openai_json_vs_function_calling/)[Next OpenRouter](https://docs.llamaindex.ai/en/stable/examples/llm/openrouter/)

Hi, how can I help you?

🦙
