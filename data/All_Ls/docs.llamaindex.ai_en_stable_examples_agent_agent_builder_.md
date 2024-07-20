Title: GPT Builder Demo - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/agent_builder/

Markdown Content:
GPT Builder Demo - LlamaIndex


[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/docs/examples/agent/agent_builder.ipynb)

Inspired by GPTs interface, presented at OpenAI Dev Day 2023. Construct an agent with natural language.

Here you can build your own agent...with another agent!

In \[ \]:

Copied!

%pip install llama\-index\-agent\-openai
%pip install llama\-index\-embeddings\-openai
%pip install llama\-index\-llms\-openai

%pip install llama-index-agent-openai %pip install llama-index-embeddings-openai %pip install llama-index-llms-openai

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..."

In \[ \]:

Copied!

from llama\_index.embeddings.openai import OpenAIEmbedding
from llama\_index.llms.openai import OpenAI
from llama\_index.core import Settings

llm \= OpenAI(model\="gpt-4")
Settings.llm \= llm
Settings.embed\_model \= OpenAIEmbedding(model\="text-embedding-3-small")

from llama\_index.embeddings.openai import OpenAIEmbedding from llama\_index.llms.openai import OpenAI from llama\_index.core import Settings llm = OpenAI(model="gpt-4") Settings.llm = llm Settings.embed\_model = OpenAIEmbedding(model="text-embedding-3-small")

Define Candidate Tools[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agent_builder/#define-candidate-tools)
--------------------------------------------------------------------------------------------------------------------

We also define a tool retriever to retrieve candidate tools.

In this setting we define tools as different Wikipedia pages.

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

from llama\_index.core import SimpleDirectoryReader

In \[ \]:

Copied!

wiki\_titles \= \["Toronto", "Seattle", "Chicago", "Boston", "Houston"\]

wiki\_titles = \["Toronto", "Seattle", "Chicago", "Boston", "Houston"\]

In \[ \]:

Copied!

from pathlib import Path

import requests

for title in wiki\_titles:
    response \= requests.get(
        "https://en.wikipedia.org/w/api.php",
        params\={
            "action": "query",
            "format": "json",
            "titles": title,
            "prop": "extracts",
            \# 'exintro': True,
            "explaintext": True,
        },
    ).json()
    page \= next(iter(response\["query"\]\["pages"\].values()))
    wiki\_text \= page\["extract"\]

    data\_path \= Path("data")
    if not data\_path.exists():
        Path.mkdir(data\_path)

    with open(data\_path / f"{title}.txt", "w") as fp:
        fp.write(wiki\_text)

from pathlib import Path import requests for title in wiki\_titles: response = requests.get( "https://en.wikipedia.org/w/api.php", params={ "action": "query", "format": "json", "titles": title, "prop": "extracts", # 'exintro': True, "explaintext": True, }, ).json() page = next(iter(response\["query"\]\["pages"\].values())) wiki\_text = page\["extract"\] data\_path = Path("data") if not data\_path.exists(): Path.mkdir(data\_path) with open(data\_path / f"{title}.txt", "w") as fp: fp.write(wiki\_text)

In \[ \]:

Copied!

\# Load all wiki documents
city\_docs \= {}
for wiki\_title in wiki\_titles:
    city\_docs\[wiki\_title\] \= SimpleDirectoryReader(
        input\_files\=\[f"data/{wiki\_title}.txt"\]
    ).load\_data()

\# Load all wiki documents city\_docs = {} for wiki\_title in wiki\_titles: city\_docs\[wiki\_title\] = SimpleDirectoryReader( input\_files=\[f"data/{wiki\_title}.txt"\] ).load\_data()

### Build Query Tool for Each Document[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agent_builder/#build-query-tool-for-each-document)

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex
from llama\_index.agent.openai import OpenAIAgent
from llama\_index.core.tools import QueryEngineTool, ToolMetadata
from llama\_index.core import VectorStoreIndex

\# Build tool dictionary
tool\_dict \= {}

for wiki\_title in wiki\_titles:
    \# build vector index
    vector\_index \= VectorStoreIndex.from\_documents(
        city\_docs\[wiki\_title\],
    )
    \# define query engines
    vector\_query\_engine \= vector\_index.as\_query\_engine(llm\=llm)

    \# define tools
    vector\_tool \= QueryEngineTool(
        query\_engine\=vector\_query\_engine,
        metadata\=ToolMetadata(
            name\=wiki\_title,
            description\=("Useful for questions related to" f" {wiki\_title}"),
        ),
    )
    tool\_dict\[wiki\_title\] \= vector\_tool

from llama\_index.core import VectorStoreIndex from llama\_index.agent.openai import OpenAIAgent from llama\_index.core.tools import QueryEngineTool, ToolMetadata from llama\_index.core import VectorStoreIndex # Build tool dictionary tool\_dict = {} for wiki\_title in wiki\_titles: # build vector index vector\_index = VectorStoreIndex.from\_documents( city\_docs\[wiki\_title\], ) # define query engines vector\_query\_engine = vector\_index.as\_query\_engine(llm=llm) # define tools vector\_tool = QueryEngineTool( query\_engine=vector\_query\_engine, metadata=ToolMetadata( name=wiki\_title, description=("Useful for questions related to" f" {wiki\_title}"), ), ) tool\_dict\[wiki\_title\] = vector\_tool

### Define Tool Retriever[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agent_builder/#define-tool-retriever)

In \[ \]:

Copied!

\# define an "object" index and retriever over these tools
from llama\_index.core import VectorStoreIndex
from llama\_index.core.objects import ObjectIndex

tool\_index \= ObjectIndex.from\_objects(
    list(tool\_dict.values()),
    index\_cls\=VectorStoreIndex,
)
tool\_retriever \= tool\_index.as\_retriever(similarity\_top\_k\=1)

\# define an "object" index and retriever over these tools from llama\_index.core import VectorStoreIndex from llama\_index.core.objects import ObjectIndex tool\_index = ObjectIndex.from\_objects( list(tool\_dict.values()), index\_cls=VectorStoreIndex, ) tool\_retriever = tool\_index.as\_retriever(similarity\_top\_k=1)

### Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agent_builder/#load-data)

Here we load wikipedia pages from different cities.

Define Meta-Tools for GPT Builder[¶](https://docs.llamaindex.ai/en/stable/examples/agent/agent_builder/#define-meta-tools-for-gpt-builder)
------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core.llms import ChatMessage
from llama\_index.core import ChatPromptTemplate
from typing import List

GEN\_SYS\_PROMPT\_STR \= """\\
Task information is given below. 

Given the task, please generate a system prompt for an OpenAI-powered bot to solve this task: 
{task} \\
"""

gen\_sys\_prompt\_messages \= \[
    ChatMessage(
        role\="system",
        content\="You are helping to build a system prompt for another bot.",
    ),
    ChatMessage(role\="user", content\=GEN\_SYS\_PROMPT\_STR),
\]

GEN\_SYS\_PROMPT\_TMPL \= ChatPromptTemplate(gen\_sys\_prompt\_messages)

agent\_cache \= {}

def create\_system\_prompt(task: str):
    """Create system prompt for another agent given an input task."""
    llm \= OpenAI(llm\="gpt-4")
    fmt\_messages \= GEN\_SYS\_PROMPT\_TMPL.format\_messages(task\=task)
    response \= llm.chat(fmt\_messages)
    return response.message.content

def get\_tools(task: str):
    """Get the set of relevant tools to use given an input task."""
    subset\_tools \= tool\_retriever.retrieve(task)
    return \[t.metadata.name for t in subset\_tools\]

def create\_agent(system\_prompt: str, tool\_names: List\[str\]):
    """Create an agent given a system prompt and an input set of tools."""
    llm \= OpenAI(model\="gpt-4")
    try:
        \# get the list of tools
        input\_tools \= \[tool\_dict\[tn\] for tn in tool\_names\]

        agent \= OpenAIAgent.from\_tools(input\_tools, llm\=llm, verbose\=True)
        agent\_cache\["agent"\] \= agent
        return\_msg \= "Agent created successfully."
    except Exception as e:
        return\_msg \= f"An error occurred when building an agent. Here is the error: {repr(e)}"
    return return\_msg

from llama\_index.core.llms import ChatMessage from llama\_index.core import ChatPromptTemplate from typing import List GEN\_SYS\_PROMPT\_STR = """\\ Task information is given below. Given the task, please generate a system prompt for an OpenAI-powered bot to solve this task: {task} \\ """ gen\_sys\_prompt\_messages = \[ ChatMessage( role="system", content="You are helping to build a system prompt for another bot.", ), ChatMessage(role="user", content=GEN\_SYS\_PROMPT\_STR), \] GEN\_SYS\_PROMPT\_TMPL = ChatPromptTemplate(gen\_sys\_prompt\_messages) agent\_cache = {} def create\_system\_prompt(task: str): """Create system prompt for another agent given an input task.""" llm = OpenAI(llm="gpt-4") fmt\_messages = GEN\_SYS\_PROMPT\_TMPL.format\_messages(task=task) response = llm.chat(fmt\_messages) return response.message.content def get\_tools(task: str): """Get the set of relevant tools to use given an input task.""" subset\_tools = tool\_retriever.retrieve(task) return \[t.metadata.name for t in subset\_tools\] def create\_agent(system\_prompt: str, tool\_names: List\[str\]): """Create an agent given a system prompt and an input set of tools.""" llm = OpenAI(model="gpt-4") try: # get the list of tools input\_tools = \[tool\_dict\[tn\] for tn in tool\_names\] agent = OpenAIAgent.from\_tools(input\_tools, llm=llm, verbose=True) agent\_cache\["agent"\] = agent return\_msg = "Agent created successfully." except Exception as e: return\_msg = f"An error occurred when building an agent. Here is the error: {repr(e)}" return return\_msg

In \[ \]:

Copied!

from llama\_index.core.tools import FunctionTool

system\_prompt\_tool \= FunctionTool.from\_defaults(fn\=create\_system\_prompt)
get\_tools\_tool \= FunctionTool.from\_defaults(fn\=get\_tools)
create\_agent\_tool \= FunctionTool.from\_defaults(fn\=create\_agent)

from llama\_index.core.tools import FunctionTool system\_prompt\_tool = FunctionTool.from\_defaults(fn=create\_system\_prompt) get\_tools\_tool = FunctionTool.from\_defaults(fn=get\_tools) create\_agent\_tool = FunctionTool.from\_defaults(fn=create\_agent)

In \[ \]:

Copied!

GPT\_BUILDER\_SYS\_STR \= """\\
You are helping to construct an agent given a user-specified task. You should generally use the tools in this order to build the agent.

1) Create system prompt tool: to create the system prompt for the agent.
2) Get tools tool: to fetch the candidate set of tools to use.
3) Create agent tool: to create the final agent.
"""

prefix\_msgs \= \[ChatMessage(role\="system", content\=GPT\_BUILDER\_SYS\_STR)\]

builder\_agent \= OpenAIAgent.from\_tools(
    tools\=\[system\_prompt\_tool, get\_tools\_tool, create\_agent\_tool\],
    prefix\_messages\=prefix\_msgs,
    verbose\=True,
)

GPT\_BUILDER\_SYS\_STR = """\\ You are helping to construct an agent given a user-specified task. You should generally use the tools in this order to build the agent. 1) Create system prompt tool: to create the system prompt for the agent. 2) Get tools tool: to fetch the candidate set of tools to use. 3) Create agent tool: to create the final agent. """ prefix\_msgs = \[ChatMessage(role="system", content=GPT\_BUILDER\_SYS\_STR)\] builder\_agent = OpenAIAgent.from\_tools( tools=\[system\_prompt\_tool, get\_tools\_tool, create\_agent\_tool\], prefix\_messages=prefix\_msgs, verbose=True, )

In \[ \]:

Copied!

builder\_agent.query("Build an agent that can tell me about Toronto.")

builder\_agent.query("Build an agent that can tell me about Toronto.")

Added user message to memory: Build an agent that can tell me about Toronto.

Calling function: create\_system\_prompt with args: {
  "task": "tell me about Toronto"
}
Got output: "Generate a brief summary about Toronto, including its history, culture, landmarks, and notable features."
 Calling Function 


Calling function: create\_agent with args: {
  "system\_prompt": "Generate a brief summary about Toronto, including its history, culture, landmarks, and notable features.",
  "tool\_names": \["Toronto"\]
}
Got output: Agent created successfully.


Out\[ \]:

Response(response='The agent has been successfully created. It can now provide information about Toronto, including its history, culture, landmarks, and notable features.', source\_nodes=\[\], metadata=None)

In \[ \]:

Copied!

city\_agent \= agent\_cache\["agent"\]

city\_agent = agent\_cache\["agent"\]

In \[ \]:

Copied!

response \= city\_agent.query("Tell me about the parks in Toronto")
print(str(response))

response = city\_agent.query("Tell me about the parks in Toronto") print(str(response))

Added user message to memory: Tell me about the parks in Toronto
Toronto is known for its beautiful and diverse parks. Here are a few of the most popular ones:

1. \*\*High Park\*\*: This is Toronto's largest public park featuring many hiking trails, sports facilities, a beautiful lakefront, convenient parking, easy public transit access, a dog park, a zoo, and playgrounds for children. It's also known for its spring cherry blossoms.

2. \*\*Toronto Islands\*\*: A group of small islands located just off the shore of the city's downtown district, offering stunning views of the city skyline. The islands provide a great escape from the city with their car-free environment, picnic spots, swimming beaches, and Centreville Amusement Park.

3. \*\*Trinity Bellwoods Park\*\*: A popular park in the downtown area, it's a great place for picnics, sports, dog-walking, or just relaxing. It also has a community recreation centre with a pool and gym.

4. \*\*Rouge National Urban Park\*\*: Located in the city's east end, this is Canada's first national urban park. It offers hiking, swimming, camping, and a chance to learn about the area's cultural and agricultural heritage.

5. \*\*Riverdale Farm\*\*: This 7.5-acre farm in the heart of Toronto provides an opportunity to experience farm life and interact with a variety of farm animals.

6. \*\*Evergreen Brick Works\*\*: A former industrial site that has been transformed into an eco-friendly community center with a park, farmers market, and cultural events.

7. \*\*Scarborough Bluffs Park\*\*: Offers a unique natural environment with stunning views of Lake Ontario from atop the bluffs.

8. \*\*Edwards Gardens\*\*: A beautiful botanical garden located in North York, perfect for a peaceful walk surrounded by nature.

9. \*\*Sunnybrook Park\*\*: A large public park that offers many recreational activities including horseback riding, sports fields, and picnic areas.

10. \*\*Cherry Beach\*\*: Located on the waterfront, this park offers a sandy beach, picnic areas, and a dog off-leash area. It's a great spot for swimming, sunbathing, and barbecuing.

These parks offer a variety of experiences, from urban amenities to natural beauty, making Toronto a great city for outdoor enthusiasts.

Back to top

[Previous 💬🤖 How to Build a Chatbot](https://docs.llamaindex.ai/en/stable/examples/agent/Chatbot_SEC/)[Next Building a Multi-PDF Agent using Query Pipelines and HyDE](https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_around_query_pipeline_with_HyDE_for_PDFs/)
