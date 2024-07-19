Title: LlamaHub Demostration - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/llama_hub/llama_hub/

Markdown Content:
LlamaHub Demostration - LlamaIndex


Here we give a simple overview of how to use data loaders and tools (for agents) within [LlamaHub](https://docs.llamaindex.ai/en/stable/examples/llama_hub/llama_hub/llamahub.ai).

**NOTES**:

*   You can learn how to use everything in LlamaHub by clicking into each module and looking at the code snippet.
*   Also, you can find a [full list of agent tools here](https://llamahub.ai/?tab=tools).
*   In this guide we'll show how to use `download_loader` and `download_tool`. You can also install `llama-hub` [as a package](https://github.com/run-llama/llama-hub#usage-use-llama-hub-as-pypi-package).

Using a Data Loader[¶](https://docs.llamaindex.ai/en/stable/examples/llama_hub/llama_hub/#using-a-data-loader)
--------------------------------------------------------------------------------------------------------------

In this example we show how to use `SimpleWebPageReader`.

**NOTE**: for any module on LlamaHub, to use with `download_` functions, note down the class name.

In \[ \]:

Copied!

%pip install llama\-index\-agent\-openai
%pip install llama\-index\-readers\-web
%pip install llama\-index\-tools\-google

%pip install llama-index-agent-openai %pip install llama-index-readers-web %pip install llama-index-tools-google

In \[ \]:

Copied!

from llama\_index.readers.web import SimpleWebPageReader

from llama\_index.readers.web import SimpleWebPageReader

In \[ \]:

Copied!

reader \= SimpleWebPageReader(html\_to\_text\=True)

reader = SimpleWebPageReader(html\_to\_text=True)

In \[ \]:

Copied!

docs \= reader.load\_data(urls\=\["https://eugeneyan.com/writing/llm-patterns/"\])

docs = reader.load\_data(urls=\["https://eugeneyan.com/writing/llm-patterns/"\])

In \[ \]:

Copied!

print(docs\[0\].get\_content()\[:400\])

print(docs\[0\].get\_content()\[:400\])

\# \[eugeneyan\](/)

  \* \[Start Here\](/start-here/ "Start Here")
  \* \[Writing\](/writing/ "Writing")
  \* \[Speaking\](/speaking/ "Speaking")
  \* \[Prototyping\](/prototyping/ "Prototyping")
  \* \[About\](/about/ "About")

# Patterns for Building LLM-based Systems & Products

\[ \[llm\](/tag/llm/) \[engineering\](/tag/engineering/)
\[production\](/tag/production/) \]  · 66 min read

> Discussions on \[HackerNews\](htt

Now you can plug these docs into your downstream LlamaIndex pipeline.

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex

index \= VectorStoreIndex.from\_documents(docs)
query\_engine \= index.as\_query\_engine()

from llama\_index.core import VectorStoreIndex index = VectorStoreIndex.from\_documents(docs) query\_engine = index.as\_query\_engine()

In \[ \]:

Copied!

response \= query\_engine.query("What are ways to evaluate LLMs?")
print(str(response))

response = query\_engine.query("What are ways to evaluate LLMs?") print(str(response))

Using an Agent Tool Spec[¶](https://docs.llamaindex.ai/en/stable/examples/llama_hub/llama_hub/#using-an-agent-tool-spec)
------------------------------------------------------------------------------------------------------------------------

In this example we show how to load an agent tool.

In \[ \]:

Copied!

from llama\_index.tools.google import GmailToolSpec

from llama\_index.tools.google import GmailToolSpec

In \[ \]:

Copied!

tool\_spec \= GmailToolSpec()

tool\_spec = GmailToolSpec()

In \[ \]:

Copied!

\# plug into your agent
from llama\_index.agent.openai import OpenAIAgent

\# plug into your agent from llama\_index.agent.openai import OpenAIAgent

In \[ \]:

Copied!

agent \= OpenAIAgent.from\_tools(tool\_spec.to\_tool\_list())

agent = OpenAIAgent.from\_tools(tool\_spec.to\_tool\_list())

In \[ \]:

Copied!

agent.chat("What is my most recent email")

agent.chat("What is my most recent email")

Back to top

[Previous Contributing a LlamaDataset To LlamaHub](https://docs.llamaindex.ai/en/stable/examples/llama_dataset/uploading_llama_dataset/)[Next Ollama Llama Pack Example](https://docs.llamaindex.ai/en/stable/examples/llama_hub/llama_pack_ollama/)

Hi, how can I help you?

🦙
