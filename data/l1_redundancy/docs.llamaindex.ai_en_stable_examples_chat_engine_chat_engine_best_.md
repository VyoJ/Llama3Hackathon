Title: Chat Engine - Best Mode

URL Source: https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_best/

Markdown Content:
Chat Engine - Best Mode - LlamaIndex


The default chat engine mode is "best", which uses the "openai" mode if you are using an OpenAI model that supports the latest function calling API, otherwise uses the "react" mode

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-anthropic
%pip install llama\-index\-llms\-openai

%pip install llama-index-llms-anthropic %pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_best/#download-data)
-----------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

\--2024-01-27 12:15:55--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 2606:50c0:8001::154, 2606:50c0:8002::154, 2606:50c0:8003::154, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|2606:50c0:8001::154|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 75042 (73K) \[text/plain\]
Saving to: ‘data/paul\_graham/paul\_graham\_essay.txt’

data/paul\_graham/pa 100%\[ Calling Function 

In \[ \]:

Copied!

print(response)

print(response)

The first programs Paul Graham tried writing were on the IBM 1401. He used an early version of Fortran for these initial programs.

Back to top

[Previous Wandb Callback Handler](https://docs.llamaindex.ai/en/stable/examples/callbacks/WandbCallbackHandler/)[Next Chat Engine - Condense Plus Context Mode](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_condense_plus_context/)
