Title: OpenAI Agent Query Planning - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_query_plan/

Markdown Content:
OpenAI Agent Query Planning - LlamaIndex


In this demo, we explore adding a `QueryPlanTool` to an `OpenAIAgent`. This effectively enables the agent to do advanced query planning, all through a single tool!

The `QueryPlanTool` is designed to work well with the OpenAI Function API. The tool takes in a set of other tools as input. The tool function signature contains of a QueryPlan Pydantic object, which can in turn contain a DAG of QueryNode objects defining a compute graph. The agent is responsible for defining this graph through the function signature when calling the tool. The tool itself executes the DAG over any corresponding tools.

In this setting we use a familiar example: Uber 10Q filings in March, June, and September of 2022.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-agent\-openai
%pip install llama\-index\-llms\-openai

%pip install llama-index-agent-openai %pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

\# # uncomment to turn on logging
\# import logging
\# import sys

\# logging.basicConfig(stream=sys.stdout, level=logging.INFO)
\# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

\# # uncomment to turn on logging # import logging # import sys # logging.basicConfig(stream=sys.stdout, level=logging.INFO) # logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

In \[ \]:

Copied!

%load\_ext autoreload
%autoreload 2

%load\_ext autoreload %autoreload 2

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama\_index.core.response.pprint\_utils import pprint\_response
from llama\_index.llms.openai import OpenAI

from llama\_index.core import SimpleDirectoryReader, VectorStoreIndex from llama\_index.core.response.pprint\_utils import pprint\_response from llama\_index.llms.openai import OpenAI

In \[ \]:

Copied!

llm \= OpenAI(temperature\=0, model\="gpt-4")

llm = OpenAI(temperature=0, model="gpt-4")

Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_query_plan/#download-data)
------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

!mkdir \-p 'data/10q/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10q/uber\_10q\_march\_2022.pdf' \-O 'data/10q/uber\_10q\_march\_2022.pdf'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10q/uber\_10q\_june\_2022.pdf' \-O 'data/10q/uber\_10q\_june\_2022.pdf'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10q/uber\_10q\_sept\_2022.pdf' \-O 'data/10q/uber\_10q\_sept\_2022.pdf'

!mkdir -p 'data/10q/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10q/uber\_10q\_march\_2022.pdf' -O 'data/10q/uber\_10q\_march\_2022.pdf' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10q/uber\_10q\_june\_2022.pdf' -O 'data/10q/uber\_10q\_june\_2022.pdf' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10q/uber\_10q\_sept\_2022.pdf' -O 'data/10q/uber\_10q\_sept\_2022.pdf'

\--2024-01-26 20:09:25--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/examples/data/10q/uber\_10q\_march\_2022.pdf
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 2606:50c0:8001::154, 2606:50c0:8003::154, 2606:50c0:8002::154, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|2606:50c0:8001::154|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1260185 (1.2M) \[application/octet-stream\]
Saving to: ‘data/10q/uber\_10q\_march\_2022.pdf’

data/10q/uber\_10q\_m 100%\[>\]   1.18M  --.-KB/s    in 0.09s   

2024-01-26 20:09:26 (12.7 MB/s) - ‘data/10q/uber\_10q\_june\_2022.pdf’ saved \[1238483/1238483\]

--2024-01-26 20:09:26--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/examples/data/10q/uber\_10q\_sept\_2022.pdf
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 2606:50c0:8001::154, 2606:50c0:8003::154, 2606:50c0:8002::154, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|2606:50c0:8001::154|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1178622 (1.1M) \[application/octet-stream\]
Saving to: ‘data/10q/uber\_10q\_sept\_2022.pdf’

data/10q/uber\_10q\_s 100%\[ Calling Function 

In \[ \]:

Copied!

print(str(response))

print(str(response))

Based on the provided context information, we can analyze Uber's revenue growth for the three-month periods ending in March, June, and September.

1. For the three months ended March 31, 2022, Uber's revenue was $6.854 billion.
2. For the three months ended June 30, 2022, Uber's revenue was $8.073 billion.
3. For the three months ended September 30, 2022, Uber's revenue was $8.343 billion.

To analyze the growth, we can compare the revenue figures for each period:

- From March to June, Uber's revenue increased by $1.219 billion ($8.073 billion - $6.854 billion), which represents a growth of approximately 17.8% (($1.219 billion / $6.854 billion) \* 100).
- From June to September, Uber's revenue increased by $0.270 billion ($8.343 billion - $8.073 billion), which represents a growth of approximately 3.3% (($0.270 billion / $8.073 billion) \* 100).

In summary, Uber experienced significant revenue growth of 17.8% between the three-month periods ending in March and June, followed by a smaller growth of 3.3% between the periods ending in June and September.

In \[ \]:

Copied!

response \= agent.query(
    "Analyze changes in risk factors in march, june, and september for Uber"
)

response = agent.query( "Analyze changes in risk factors in march, june, and september for Uber" )

In \[ \]:

Copied!

print(str(response))

print(str(response))

In \[ \]:

Copied!

\# response = agent.query("Analyze both Uber revenue growth and risk factors over march, june, and september")

\# response = agent.query("Analyze both Uber revenue growth and risk factors over march, june, and september")

In \[ \]:

Copied!

print(str(response))

print(str(response))

Based on the provided context information, we can analyze Uber's revenue growth for the three-month periods ending in March, June, and September.

1. For the three months ended March 31, 2022, Uber's revenue was $6.854 billion.
2. For the three months ended June 30, 2022, Uber's revenue was $8.073 billion.
3. For the three months ended September 30, 2022, Uber's revenue was $8.343 billion.

To analyze the growth, we can compare the revenue figures for each period:

- From March to June, Uber's revenue increased by $1.219 billion ($8.073 billion - $6.854 billion), which represents a growth of approximately 17.8% (($1.219 billion / $6.854 billion) \* 100).
- From June to September, Uber's revenue increased by $0.270 billion ($8.343 billion - $8.073 billion), which represents a growth of approximately 3.3% (($0.270 billion / $8.073 billion) \* 100).

In summary, Uber experienced significant revenue growth of 17.8% between the three-month periods ending in March and June, followed by a smaller growth of 3.3% between the periods ending in June and September.

In \[ \]:

Copied!

response \= agent.query(
    "First look at Uber's revenue growth and risk factors in March, "
    + "then revenue growth and risk factors in September, and then compare and"
    " contrast the two documents?"
)

response = agent.query( "First look at Uber's revenue growth and risk factors in March, " + "then revenue growth and risk factors in September, and then compare and" " contrast the two documents?" )

In \[ \]:

Copied!

response

response

Back to top

[Previous OpenAI Agent + Query Engine Experimental Cookbook](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_query_cookbook/)[Next Retrieval-Augmented OpenAI Agent](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_retrieval/)

Hi, how can I help you?

🦙
