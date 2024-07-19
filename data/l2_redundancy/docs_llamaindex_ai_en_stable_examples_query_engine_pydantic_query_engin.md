Title: Query Engine with Pydantic Outputs

URL Source: https://docs.llamaindex.ai/en/stable/examples/query_engine/pydantic_query_engine/

Markdown Content:
Query Engine with Pydantic Outputs - LlamaIndex


Every query engine has support for integrated structured responses using the following `response_mode`s in `RetrieverQueryEngine`:

*   `refine`
*   `compact`
*   `tree_summarize`
*   `accumulate` (beta, requires extra parsing to convert to objects)
*   `compact_accumulate` (beta, requires extra parsing to convert to objects)

In this notebook, we walk through a small example demonstrating the usage.

Under the hood, every LLM response will be a pydantic object. If that response needs to be refined or summarized, it is converted into a JSON string for the next response. Then, the final response is returned as a pydantic object.

**NOTE:** This can technically work with any LLM, but non-openai is support is still in development and considered beta.

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/pydantic_query_engine/#setup)
-------------------------------------------------------------------------------------------------

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

In \[ \]:

Copied!

import os
import openai

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."
openai.api\_key \= os.environ\["OPENAI\_API\_KEY"\]

import os import openai os.environ\["OPENAI\_API\_KEY"\] = "sk-..." openai.api\_key = os.environ\["OPENAI\_API\_KEY"\]

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

documents \= SimpleDirectoryReader("./data/paul\_graham").load\_data()

from llama\_index.core import SimpleDirectoryReader documents = SimpleDirectoryReader("./data/paul\_graham").load\_data()

### Create our Pydanitc Output Object[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/pydantic_query_engine/#create-our-pydanitc-output-object)

In \[ \]:

Copied!

from typing import List
from pydantic import BaseModel

class Biography(BaseModel):
    """Data model for a biography."""

    name: str
    best\_known\_for: List\[str\]
    extra\_info: str

from typing import List from pydantic import BaseModel class Biography(BaseModel): """Data model for a biography.""" name: str best\_known\_for: List\[str\] extra\_info: str

Create the Index + Query Engine (OpenAI)[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/pydantic_query_engine/#create-the-index-query-engine-openai)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

When using OpenAI, the function calling API will be leveraged for reliable structured outputs.

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex
from llama\_index.llms.openai import OpenAI

llm \= OpenAI(model\="gpt-3.5-turbo", temperature\=0.1)

index \= VectorStoreIndex.from\_documents(
    documents,
)

from llama\_index.core import VectorStoreIndex from llama\_index.llms.openai import OpenAI llm = OpenAI(model="gpt-3.5-turbo", temperature=0.1) index = VectorStoreIndex.from\_documents( documents, )

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(
    output\_cls\=Biography, response\_mode\="compact", llm\=llm
)

query\_engine = index.as\_query\_engine( output\_cls=Biography, response\_mode="compact", llm=llm )

In \[ \]:

Copied!

response \= query\_engine.query("Who is Paul Graham?")

response = query\_engine.query("Who is Paul Graham?")

In \[ \]:

Copied!

print(response.name)
print(response.best\_known\_for)
print(response.extra\_info)

print(response.name) print(response.best\_known\_for) print(response.extra\_info)

Paul Graham
\['working on Bel', 'co-founding Viaweb', 'creating the programming language Arc'\]
Paul Graham is a computer scientist, entrepreneur, and writer. He is best known for his work on Bel, a programming language, and for co-founding Viaweb, an early web application company that was later acquired by Yahoo. Graham also created the programming language Arc. He has written numerous essays on topics such as startups, programming, and life.

In \[ \]:

Copied!

\# get the full pydanitc object
print(type(response.response))

\# get the full pydanitc object print(type(response.response))

<class '\_\_main\_\_.Biography'>

Create the Index + Query Engine (Non-OpenAI, Beta)[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/pydantic_query_engine/#create-the-index-query-engine-non-openai-beta)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When using an LLM that does not support function calling, we rely on the LLM to write the JSON itself, and we parse the JSON into the proper pydantic object.

In \[ \]:

Copied!

import os

os.environ\["ANTHROPIC\_API\_KEY"\] \= "sk-..."

import os os.environ\["ANTHROPIC\_API\_KEY"\] = "sk-..."

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex
from llama\_index.llms.anthropic import Anthropic

llm \= Anthropic(model\="claude-instant-1.2", temperature\=0.1)

index \= VectorStoreIndex.from\_documents(
    documents,
)

from llama\_index.core import VectorStoreIndex from llama\_index.llms.anthropic import Anthropic llm = Anthropic(model="claude-instant-1.2", temperature=0.1) index = VectorStoreIndex.from\_documents( documents, )

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(
    output\_cls\=Biography, response\_mode\="tree\_summarize", llm\=llm
)

query\_engine = index.as\_query\_engine( output\_cls=Biography, response\_mode="tree\_summarize", llm=llm )

In \[ \]:

Copied!

response \= query\_engine.query("Who is Paul Graham?")

response = query\_engine.query("Who is Paul Graham?")

In \[ \]:

Copied!

print(response.name)
print(response.best\_known\_for)
print(response.extra\_info)

print(response.name) print(response.best\_known\_for) print(response.extra\_info)

Paul Graham
\['Co-founder of Y Combinator', 'Essayist and programmer'\]
He is known for creating Viaweb, one of the first web application builders, and for founding Y Combinator, one of the world's top startup accelerators. Graham has also written extensively about technology, investing, and philosophy.

In \[ \]:

Copied!

\# get the full pydanitc object
print(type(response.response))

\# get the full pydanitc object print(type(response.response))

<class '\_\_main\_\_.Biography'>

Accumulate Examples (Beta)[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/pydantic_query_engine/#accumulate-examples-beta)
-----------------------------------------------------------------------------------------------------------------------------------------

Accumulate with pydantic objects requires some extra parsing. This is still a beta feature, but it's still possible to get accumulate pydantic objects.

In \[ \]:

Copied!

from typing import List
from pydantic import BaseModel

class Company(BaseModel):
    """Data model for a companies mentioned."""

    company\_name: str
    context\_info: str

from typing import List from pydantic import BaseModel class Company(BaseModel): """Data model for a companies mentioned.""" company\_name: str context\_info: str

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex,
from llama\_index.llms.openai import OpenAI

llm \= OpenAI(model\="gpt-3.5-turbo", temperature\=0.1)

index \= VectorStoreIndex.from\_documents(
    documents,
)

from llama\_index.core import VectorStoreIndex, from llama\_index.llms.openai import OpenAI llm = OpenAI(model="gpt-3.5-turbo", temperature=0.1) index = VectorStoreIndex.from\_documents( documents, )

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(
    output\_cls\=Company, response\_mode\="accumulate", llm\=llm
)

query\_engine = index.as\_query\_engine( output\_cls=Company, response\_mode="accumulate", llm=llm )

In \[ \]:

Copied!

response \= query\_engine.query("What companies are mentioned in the text?")

response = query\_engine.query("What companies are mentioned in the text?")

In accumulate, responses are separated by a default separator, and prepended with a prefix.

In \[ \]:

Copied!

companies \= \[\]

\# split by the default separator
for response\_str in str(response).split("\\n\---------------------\\n"):
    \# remove the prefix --  every response starts like \`Response 1: {...}\`
    \# so, we find the first bracket and remove everything before it
    response\_str \= response\_str\[response\_str.find("{") :\]
    companies.append(Company.parse\_raw(response\_str))

companies = \[\] # split by the default separator for response\_str in str(response).split("\\n---------------------\\n"): # remove the prefix -- every response starts like \`Response 1: {...}\` # so, we find the first bracket and remove everything before it response\_str = response\_str\[response\_str.find("{") :\] companies.append(Company.parse\_raw(response\_str))

In \[ \]:

Copied!

print(companies)

print(companies)

\[Company(company\_name='Yahoo', context\_info='Yahoo bought us'), Company(company\_name='Yahoo', context\_info="I'd been meaning to since Yahoo bought us")\]

Back to top

[Previous \[Beta\] Text-to-SQL with PGVector](https://docs.llamaindex.ai/en/stable/examples/query_engine/pgvector_sql_query_engine/)[Next Recursive Retriever + Document Agents](https://docs.llamaindex.ai/en/stable/examples/query_engine/recursive_retriever_agents/)
