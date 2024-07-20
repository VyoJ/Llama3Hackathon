Title: Observability with OpenLLMetry - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/callbacks/OpenLLMetry/

Markdown Content:
Observability with OpenLLMetry - LlamaIndex


[OpenLLMetry](https://github.com/traceloop/openllmetry) is an open-source project based on OpenTelemetry for tracing and monitoring LLM applications. It connects to [all major observability platforms](https://www.traceloop.com/docs/openllmetry/integrations/introduction) (like Datadog, Dynatrace, Honeycomb, New Relic and others) and installs in minutes.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙 and OpenLLMetry.

In \[ \]:

Copied!

!pip install llama\-index
!pip install traceloop\-sdk

!pip install llama-index !pip install traceloop-sdk

Configure API keys[¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/OpenLLMetry/#configure-api-keys)
--------------------------------------------------------------------------------------------------------------

Sign-up to Traceloop at [app.traceloop.com](https://app.traceloop.com/). Then, go to the [API keys page](https://app.traceloop.com/settings/api-keys) and create a new API key. Copy the key and paste it in the cell below.

If you prefer to use a different observability platform like Datadog, Dynatrace, Honeycomb or others, you can find instructions on how to configure it [here](https://www.traceloop.com/docs/openllmetry/integrations/introduction).

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."
os.environ\["TRACELOOP\_API\_KEY"\] \= "..."

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..." os.environ\["TRACELOOP\_API\_KEY"\] = "..."

Initialize OpenLLMetry[¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/OpenLLMetry/#initialize-openllmetry)
----------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from traceloop.sdk import Traceloop

Traceloop.init()

from traceloop.sdk import Traceloop Traceloop.init()

Traceloop syncing configuration and prompts
Traceloop exporting traces to https://api.traceloop.com authenticating with bearer token

Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/OpenLLMetry/#download-data)
----------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

\--2024-01-12 12:43:16--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.109.133, 185.199.108.133, 185.199.111.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.109.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 75042 (73K) \[text/plain\]
Saving to: ‘data/paul\_graham/paul\_graham\_essay.txt’

data/paul\_graham/pa 100%\[>\]  73.28K  --.-KB/s    in 0.02s   

2024-01-12 12:43:17 (3.68 MB/s) - ‘data/paul\_graham/paul\_graham\_essay.txt’ saved \[75042/75042\]

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

docs \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

from llama\_index.core import SimpleDirectoryReader docs = SimpleDirectoryReader("./data/paul\_graham/").load\_data()

Run a query[¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/OpenLLMetry/#run-a-query)
------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex

index \= VectorStoreIndex.from\_documents(docs)
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did the author do growing up?")
print(response)

from llama\_index.core import VectorStoreIndex index = VectorStoreIndex.from\_documents(docs) query\_engine = index.as\_query\_engine() response = query\_engine.query("What did the author do growing up?") print(response)

The author wrote short stories and also worked on programming, specifically on an IBM 1401 computer in 9th grade. They used an early version of Fortran and typed programs on punch cards. They also mentioned getting a microcomputer, a TRS-80, in about 1980 and started programming on it.

Go to Traceloop or your favorite platform to view the results[¶](https://docs.llamaindex.ai/en/stable/examples/callbacks/OpenLLMetry/#go-to-traceloop-or-your-favorite-platform-to-view-the-results)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![Image 4: Traceloop](https://docs.llamaindex.ai/en/stable/_images/openllmetry.png)

Back to top

[Previous OpenInference Callback Handler + Arize Phoenix](https://docs.llamaindex.ai/en/stable/examples/callbacks/OpenInferenceCallback/)[Next PromptLayer Handler](https://docs.llamaindex.ai/en/stable/examples/callbacks/PromptLayerHandler/)

Hi, how can I help you?

🦙
