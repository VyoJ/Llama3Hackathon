Title: Chat Engine - OpenAI Agent Mode

URL Source: https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_openai/

Markdown Content:
Chat Engine - OpenAI Agent Mode - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai

%pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_openai/#download-data)
-------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

\--2023-11-20 14:52:58--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.110.133, 185.199.108.133, 185.199.109.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.110.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 75042 (73K) \[text/plain\]
Saving to: ‘data/paul\_graham/paul\_graham\_essay.txt’

data/paul\_graham/pa 100%\[ Calling Function 

STARTING TURN 2
---------------

Paul Graham handed over Y Combinator (YC) to Sam Altman.

In \[ \]:

Copied!

response \= chat\_engine.stream\_chat(
    "Use the tool to answer: Who did Paul Graham hand over YC to?"
)
print(response)

response = chat\_engine.stream\_chat( "Use the tool to answer: Who did Paul Graham hand over YC to?" ) print(response)

STARTING TURN 1
---------------


Calling function: query\_engine\_tool with args: {
  "input": "Who did Paul Graham hand over YC to?"
}
Got output: Paul Graham handed over YC to Sam Altman.
 Calling Function 

STARTING TURN 2
---------------

In \[ \]:

Copied!

print(response)

print(response)

Growing up, Paul Graham worked on writing and programming. He wrote short stories and also tried his hand at programming on the IBM 1401 computer that his school district had. He later got a microcomputer, a TRS-80, and started programming more extensively, writing simple games and even a word processor.

Back to top

[Previous Chat Engine - Context Mode](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_context/)[Next Chat Engine with a Personality ✨](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_personality/)
