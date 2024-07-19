Title: Chain-of-Abstraction LlamaPack - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/coa_agent/

Markdown Content:
Chain-of-Abstraction LlamaPack - LlamaIndex


[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/docs/examples/agent/coa_agent.ipynb)

The chain-of-abstraction (CoA) LlamaPack implements a generalized version of the strategy decsribed in the [original CoA paper](https://arxiv.org/abs/2401.17464).

By prompting the LLM to write function calls in a chain-of-thought format, we can execute both simple and complex combinations of function calls needed to execute a task.

The LLM is prompted to write a response containing function calls, for example, a CoA plan might look like:

```
After buying the apples, Sally has [FUNC add(3, 2) = y1] apples. 
Then, the wizard casts a spell to multiply the number of apples by 3, 
resulting in [FUNC multiply(y1, 3) = y2] apples.
```

From there, the function calls can be parsed into a dependency graph, and executed.

Then, the values in the CoA are replaced with their actual results.

As an extension to the original paper, we also run the LLM a final time, to rewrite the response in a more readable and user-friendly way.

**NOTE:** In the original paper, the authors fine-tuned an LLM specifically for this, and also for specific functions and datasets. As such, only capable LLMs (OpenAI, Anthropic, etc.) will be (hopefully) reliable for this without finetuning.

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/agent/coa_agent/#setup)
------------------------------------------------------------------------------

First, lets install the pack, along with some extra dependencies.

In \[ \]:

Copied!

%pip install llama\-index\-core llama\-index\-llms\-openai llama\-index\-embeddings\-openai
%pip install llama\-index\-agent\-coa llama\-parse

%pip install llama-index-core llama-index-llms-openai llama-index-embeddings-openai %pip install llama-index-agent-coa llama-parse

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import nest\_asyncio

nest\_asyncio.apply()

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..." import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

from llama\_index.core import Settings
from llama\_index.embeddings.openai import OpenAIEmbedding
from llama\_index.llms.openai import OpenAI

Settings.embed\_model \= OpenAIEmbedding(
    model\="text-embedding-3-small", embed\_batch\_size\=256
)
Settings.llm \= OpenAI(model\="gpt-4-turbo", temperature\=0.1)

from llama\_index.core import Settings from llama\_index.embeddings.openai import OpenAIEmbedding from llama\_index.llms.openai import OpenAI Settings.embed\_model = OpenAIEmbedding( model="text-embedding-3-small", embed\_batch\_size=256 ) Settings.llm = OpenAI(model="gpt-4-turbo", temperature=0.1)

Tools setup[¶](https://docs.llamaindex.ai/en/stable/examples/agent/coa_agent/#tools-setup)
------------------------------------------------------------------------------------------

Next, we need some tools for our agent to use.

In this example, we use some classic SEC 10K fillings.

In \[ \]:

Copied!

!mkdir \-p 'data/10k/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' \-O 'data/10k/uber\_2021.pdf'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/lyft\_2021.pdf' \-O 'data/10k/lyft\_2021.pdf'

!mkdir -p 'data/10k/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' -O 'data/10k/uber\_2021.pdf' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/lyft\_2021.pdf' -O 'data/10k/lyft\_2021.pdf'

In \[ \]:

Copied!

from llama\_index.core import StorageContext, load\_index\_from\_storage

try:
    storage\_context \= StorageContext.from\_defaults(
        persist\_dir\="./storage/lyft"
    )
    lyft\_index \= load\_index\_from\_storage(storage\_context)

    storage\_context \= StorageContext.from\_defaults(
        persist\_dir\="./storage/uber"
    )
    uber\_index \= load\_index\_from\_storage(storage\_context)

    index\_loaded \= True
except:
    index\_loaded \= False

from llama\_index.core import StorageContext, load\_index\_from\_storage try: storage\_context = StorageContext.from\_defaults( persist\_dir="./storage/lyft" ) lyft\_index = load\_index\_from\_storage(storage\_context) storage\_context = StorageContext.from\_defaults( persist\_dir="./storage/uber" ) uber\_index = load\_index\_from\_storage(storage\_context) index\_loaded = True except: index\_loaded = False

In \[ \]:

Copied!

from llama\_parse import LlamaParse
from llama\_index.core import SimpleDirectoryReader, VectorStoreIndex

\# (OPTIONAL) -- Use LlamaParse for loading PDF documents
file\_extractor \= {
    ".pdf": LlamaParse(
        result\_type\="markdown",
        api\_key\="llx-...",
    )
}

if not index\_loaded:
    \# load data
    lyft\_docs \= SimpleDirectoryReader(
        input\_files\=\["./data/10k/lyft\_2021.pdf"\],
        file\_extractor\=file\_extractor,
    ).load\_data()
    uber\_docs \= SimpleDirectoryReader(
        input\_files\=\["./data/10k/uber\_2021.pdf"\],
        file\_extractor\=file\_extractor,
    ).load\_data()

    \# build index
    lyft\_index \= VectorStoreIndex.from\_documents(lyft\_docs)
    uber\_index \= VectorStoreIndex.from\_documents(uber\_docs)

    \# persist index
    lyft\_index.storage\_context.persist(persist\_dir\="./storage/lyft")
    uber\_index.storage\_context.persist(persist\_dir\="./storage/uber")

from llama\_parse import LlamaParse from llama\_index.core import SimpleDirectoryReader, VectorStoreIndex # (OPTIONAL) -- Use LlamaParse for loading PDF documents file\_extractor = { ".pdf": LlamaParse( result\_type="markdown", api\_key="llx-...", ) } if not index\_loaded: # load data lyft\_docs = SimpleDirectoryReader( input\_files=\["./data/10k/lyft\_2021.pdf"\], file\_extractor=file\_extractor, ).load\_data() uber\_docs = SimpleDirectoryReader( input\_files=\["./data/10k/uber\_2021.pdf"\], file\_extractor=file\_extractor, ).load\_data() # build index lyft\_index = VectorStoreIndex.from\_documents(lyft\_docs) uber\_index = VectorStoreIndex.from\_documents(uber\_docs) # persist index lyft\_index.storage\_context.persist(persist\_dir="./storage/lyft") uber\_index.storage\_context.persist(persist\_dir="./storage/uber")

In \[ \]:

Copied!

from llama\_index.core.tools import QueryEngineTool

lyft\_engine \= lyft\_index.as\_query\_engine(similarity\_top\_k\=2)
uber\_engine \= uber\_index.as\_query\_engine(similarity\_top\_k\=2)

query\_engine\_tools \= \[
    QueryEngineTool.from\_defaults(
        query\_engine\=lyft\_engine,
        name\="lyft\_10k",
        description\=(
            "Provides information about Lyft financials for year 2021. "
            "Use a detailed plain text question as input to the tool."
        ),
    ),
    QueryEngineTool.from\_defaults(
        query\_engine\=uber\_engine,
        name\="uber\_10k",
        description\=(
            "Provides information about Uber financials for year 2021. "
            "Use a detailed plain text question as input to the tool."
        ),
    ),
\]

from llama\_index.core.tools import QueryEngineTool lyft\_engine = lyft\_index.as\_query\_engine(similarity\_top\_k=2) uber\_engine = uber\_index.as\_query\_engine(similarity\_top\_k=2) query\_engine\_tools = \[ QueryEngineTool.from\_defaults( query\_engine=lyft\_engine, name="lyft\_10k", description=( "Provides information about Lyft financials for year 2021. " "Use a detailed plain text question as input to the tool." ), ), QueryEngineTool.from\_defaults( query\_engine=uber\_engine, name="uber\_10k", description=( "Provides information about Uber financials for year 2021. " "Use a detailed plain text question as input to the tool." ), ), \]

Run the CoAAgentPack[¶](https://docs.llamaindex.ai/en/stable/examples/agent/coa_agent/#run-the-coaagentpack)
------------------------------------------------------------------------------------------------------------

With our tools ready, we can now run the agent pack!

In \[ \]:

Copied!

%pip install llama\-index\-packs\-agents\-coa

%pip install llama-index-packs-agents-coa

In \[ \]:

Copied!

\# needs llama\_index-packs-agents-coa
from llama\_index.packs.agent.coa import CoAAgentPack

pack \= CoAAgentPack(tools\=query\_engine\_tools, llm\=Settings.llm)

\# needs llama\_index-packs-agents-coa from llama\_index.packs.agent.coa import CoAAgentPack pack = CoAAgentPack(tools=query\_engine\_tools, llm=Settings.llm)

In \[ \]:

Copied!

response \= pack.run("How did Ubers revenue growth compare to Lyfts in 2021?")

response = pack.run("How did Ubers revenue growth compare to Lyfts in 2021?")

\
def lyft\_10k(input: string):
   """Provides information about Lyft financials for year 2021. Use a detailed plain text question as input to the tool."""
    ...
def uber\_10k(input: string):
   """Provides information about Uber financials for year 2021. Use a detailed plain text question as input to the tool."""
    ...

To compare Uber's revenue growth to Lyft's in 2021, we need to obtain the revenue growth figures for both companies for that year.

1. Retrieve Uber's revenue growth for 2021 by querying the Uber financial tool with a specific question about revenue growth:
   - \[FUNC uber\_10k("What was Uber's revenue growth in 2021?") = y1\]

2. Retrieve Lyft's revenue growth for 2021 by querying the Lyft financial tool with a similar question about revenue growth:
   - \[FUNC lyft\_10k("What was Lyft's revenue growth in 2021?") = y2\]

3. Compare the revenue growth figures obtained (y1 and y2) to determine which company had higher growth in 2021. This comparison will be done by the reader after the function calls have been executed.



In \[ \]:

Copied!

print(str(response))

print(str(response))

In 2021, Uber's revenue growth was higher than Lyft's. Uber's revenue grew by 57% compared to 2020, while Lyft's revenue increased by 36% compared to the prior year.

Lets recap the logs we just saw

*   The tools get parsed into python-like definitions
*   The agent is prompted to generate a CoA plan
*   The function calls are parsed out of the plan and executed
*   The values in the plan are filled in
*   The agent generates a final response

\[Advanced\] -- Using the CoAAgentWorker[¶](https://docs.llamaindex.ai/en/stable/examples/agent/coa_agent/#advanced-using-the-coaagentworker)
---------------------------------------------------------------------------------------------------------------------------------------------

By installing the CoAAgentPack, you also get access to the underlying agent worker. With this, you can setup the agent manually, as well as customize the prompts and output parsing.

In \[ \]:

Copied!

from llama\_index.agent.coa import CoAAgentWorker

worker \= CoAAgentWorker.from\_tools(
    tools\=query\_engine\_tools,
    llm\=Settings.llm,
    verbose\=True,
)

agent \= worker.as\_agent()

from llama\_index.agent.coa import CoAAgentWorker worker = CoAAgentWorker.from\_tools( tools=query\_engine\_tools, llm=Settings.llm, verbose=True, ) agent = worker.as\_agent()

In \[ \]:

Copied!

agent.chat("How did Ubers revenue growth compare to Lyfts in 2021?")

agent.chat("How did Ubers revenue growth compare to Lyfts in 2021?")

\
def lyft\_10k(input: string):
   """Provides information about Lyft financials for year 2021. Use a detailed plain text question as input to the tool."""
    ...
def uber\_10k(input: string):
   """Provides information about Uber financials for year 2021. Use a detailed plain text question as input to the tool."""
    ...

To compare Uber's revenue growth to Lyft's in 2021, we need to obtain the revenue growth figures for both companies for that year.

1. Retrieve Uber's revenue growth for 2021 by querying the Uber financial tool with a specific question about revenue growth. This can be done using the function call: \[FUNC uber\_10k("What was Uber's revenue growth in 2021?") = y1\].

2. Similarly, retrieve Lyft's revenue growth for 2021 by querying the Lyft financial tool with a specific question about revenue growth. This can be done using the function call: \[FUNC lyft\_10k("What was Lyft's revenue growth in 2021?") = y2\].

3. Once both y1 and y2 are obtained, compare the values to determine which company had higher revenue growth in 2021. This comparison does not require a function call but involves a direct comparison of y1 and y2 to see which is greater.



Out\[ \]:

AgentChatResponse(response="In 2021, Uber's revenue growth was reported as 57%. To compare this with Lyft's revenue growth, we calculate the percentage increase for Lyft based on the provided figures: Lyft's revenue in 2021 was $3,208,323,000 compared to $2,364,681,000 in 2020. The growth in revenue for Lyft can be calculated as:\\n\\n\\\\\[ \\\\text{Growth Percentage} = \\\\left( \\\\frac{\\\\text{Revenue in 2021} - \\\\text{Revenue in 2020}}{\\\\text{Revenue in 2020}} \\\\right) \\\\times 100 \\\\\]\\n\\\\\[ \\\\text{Growth Percentage} = \\\\left( \\\\frac{3,208,323,000 - 2,364,681,000}{2,364,681,000} \\\\right) \\\\times 100 \\\\approx 35.7\\\\% \\\\\]\\n\\nThus, comparing the two, Uber's revenue growth of 57% was higher than Lyft's growth of approximately 35.7% in 2021.", sources=\[\], source\_nodes=\[\], is\_dummy\_stream=False)

\[Advanced\] -- How does this actually work?[¶](https://docs.llamaindex.ai/en/stable/examples/agent/coa_agent/#advanced-how-does-this-actually-work)
----------------------------------------------------------------------------------------------------------------------------------------------------

So, under the hood we are prompting the LLM to first output the CoA, then we parse it and run functions, then we refine all that into a final output.

First, we parse the tools into python-like function defintions by parsing `tool.metadata.fn_schema_str`, along with the tool name and description.

You can find that code in the utils.

What this looks like is we have a prompt like this:

REASONING\_PROMPT\_TEMPALTE \= """Generate an abstract plan of reasoning using placeholders for the specific values and function calls needed.
The placeholders should be labeled y1, y2, etc.
Function calls should be represented as inline strings like \[FUNC {{function\_name}}({{input1}}, {{input2}}, ...) = {{output\_placeholder}}\].
Assume someone will read the plan after the functions have been executed in order to make a final response.
Not every question will require function calls to answer.
If you do invoke a function, only use the available functions, do not make up functions.

Example:
\-----------
Available functions:
\\\`\\\`\\\`python
def add(a: int, b: int) -> int:
    \\"\\"\\"Add two numbers together.\\"\\"\\"
    ...

def multiply(a: int, b: int) -> int:
    \\"\\"\\"Multiply two numbers together.\\"\\"\\"
    ...
\\\`\\\`\\\`

Question:
Sally has 3 apples and buys 2 more. Then magically, a wizard casts a spell that multiplies the number of apples by 3. How many apples does Sally have now?

Abstract plan of reasoning:
After buying the apples, Sally has \[FUNC add(3, 2) = y1\] apples. Then, the wizard casts a spell to multiply the number of apples by 3, resulting in \[FUNC multiply(y1, 3) = y2\] apples.

Your Turn:
\-----------
Available functions:
\\\`\\\`\\\`python
{functions}
\\\`\\\`\\\`

Question:
{question}

Abstract plan of reasoning:
"""

This will generate the chain-of-abstraction reasoning.

Then, the reasoning is parsed using the output parser.

After calling the functions and filling in values, we give the LLM a chance to refine the response, using this prompt:

REFINE\_REASONING\_PROMPT\_TEMPALTE \= """Generate a response to a question by using a previous abstract plan of reasoning. Use the previous reasoning as context to write a response to the question.

Example:
\-----------
Question: 
Sally has 3 apples and buys 2 more. Then magically, a wizard casts a spell that multiplies the number of apples by 3. How many apples does Sally have now?

Previous reasoning:
After buying the apples, Sally has \[FUNC add(3, 2) = 5\] apples. Then, the wizard casts a spell to multiply the number of apples by 3, resulting in \[FUNC multiply(5, 3) = 15\] apples.

Response:
After the wizard casts the spell, Sally has 15 apples.

Your Turn:
\-----------
Question:
{question}

Previous reasoning:
{prev\_reasoning}

Response:
"""

Back to top

[Previous Function Calling AWS Bedrock Converse Agent](https://docs.llamaindex.ai/en/stable/examples/agent/bedrock_converse_agent/)[Next Building a Custom Agent](https://docs.llamaindex.ai/en/stable/examples/agent/custom_agent/)

Hi, how can I help you?

🦙
