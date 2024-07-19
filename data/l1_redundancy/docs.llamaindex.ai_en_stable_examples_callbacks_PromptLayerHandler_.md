Title: PromptLayer Handler - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/callbacks/PromptLayerHandler/

Markdown Content:
PromptLayer Handler - LlamaIndex


[PromptLayer](https://promptlayer.com/) is an LLMOps tool to help manage prompts, check out the [features](https://docs.promptlayer.com/introduction). Currently we only support OpenAI for this integration.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙 and PromptLayer.

In \[ \]:

Copied!

!pip install llama\-index
!pip install promptlayer

!pip install llama-index !pip install promptlayer

Configure API keys[¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/PromptLayerHandler/#configure-api-keys)
---------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."
os.environ\["PROMPTLAYER\_API\_KEY"\] \= "pl\_..."

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..." os.environ\["PROMPTLAYER\_API\_KEY"\] = "pl\_..."

Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/PromptLayerHandler/#download-data)
-----------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

Will not apply HSTS. The HSTS database must be a regular and non-world-writable file.
ERROR: could not open HSTS store at '/home/loganm/.wget-hsts'. HSTS will be disabled.
--2023-11-29 21:09:27--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.110.133, 185.199.109.133, 185.199.108.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.110.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 75042 (73K) \[text/plain\]
Saving to: ‘data/paul\_graham/paul\_graham\_essay.txt’

data/paul\_graham/pa 100%\[>\]  73.28K  --.-KB/s    in 0.04s   

2023-11-29 21:09:28 (1.76 MB/s) - ‘data/paul\_graham/paul\_graham\_essay.txt’ saved \[75042/75042\]

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

docs \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

from llama\_index.core import SimpleDirectoryReader docs = SimpleDirectoryReader("./data/paul\_graham/").load\_data()

Callback Manager Setup[¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/PromptLayerHandler/#callback-manager-setup)
-----------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core import set\_global\_handler

\# pl\_tags are optional, to help you organize your prompts and apps
set\_global\_handler("promptlayer", pl\_tags\=\["paul graham", "essay"\])

from llama\_index.core import set\_global\_handler # pl\_tags are optional, to help you organize your prompts and apps set\_global\_handler("promptlayer", pl\_tags=\["paul graham", "essay"\])

Trigger the callback with a query[¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/PromptLayerHandler/#trigger-the-callback-with-a-query)
---------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex

index \= VectorStoreIndex.from\_documents(docs)
query\_engine \= index.as\_query\_engine()

from llama\_index.core import VectorStoreIndex index = VectorStoreIndex.from\_documents(docs) query\_engine = index.as\_query\_engine()

In \[ \]:

Copied!

response \= query\_engine.query("What did the author do growing up?")

response = query\_engine.query("What did the author do growing up?")

Access [promptlayer.com](https://promptlayer.com/) to see stats[¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/PromptLayerHandler/#access-promptlayercom-to-see-stats)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![Image 4: image.png](blob:https://docs.llamaindex.ai/e2fa49ddbd5266e078e3a5bb46923074)

Back to top

[Previous Observability with OpenLLMetry](https://docs.llamaindex.ai/en/stable/examples/callbacks/OpenLLMetry/)[Next Token Counting Handler](https://docs.llamaindex.ai/en/stable/examples/callbacks/TokenCountingHandler/)

Hi, how can I help you?

🦙
