Title: OpenAI Agent + Query Engine Experimental Cookbook

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_query_cookbook/

Markdown Content:
OpenAI Agent + Query Engine Experimental Cookbook - LlamaIndex


In this notebook, we try out the OpenAIAgent across a variety of query engine tools and datasets. We explore how OpenAIAgent can compare/replace existing workflows solved by our retrievers/query engines.

*   Auto retrieval
*   Joint SQL and vector search

**NOTE:** Any Text-to-SQL application should be aware that executing arbitrary SQL queries can be a security risk. It is recommended to take precautions as needed, such as using restricted roles, read-only databases, sandboxing, etc.

AutoRetrieval from a Vector Database[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_query_cookbook/#autoretrieval-from-a-vector-database)
--------------------------------------------------------------------------------------------------------------------------------------------------------------

Our existing "auto-retrieval" capabilities (in `VectorIndexAutoRetriever`) allow an LLM to infer the right query parameters for a vector database - including both the query string and metadata filter.

Since the OpenAI Function API can infer function parameters, we explore its capabilities in performing auto-retrieval here.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-agent\-openai
%pip install llama\-index\-llms\-openai
%pip install llama\-index\-readers\-wikipedia
%pip install llama\-index\-vector\-stores\-pinecone

%pip install llama-index-agent-openai %pip install llama-index-llms-openai %pip install llama-index-readers-wikipedia %pip install llama-index-vector-stores-pinecone

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import pinecone
import os

api\_key \= os.environ\["PINECONE\_API\_KEY"\]
pinecone.init(api\_key\=api\_key, environment\="us-west4-gcp-free")

import pinecone import os api\_key = os.environ\["PINECONE\_API\_KEY"\] pinecone.init(api\_key=api\_key, environment="us-west4-gcp-free")

In \[ \]:

Copied!

import os
import getpass

\# os.environ\["OPENAI\_API\_KEY"\] = getpass.getpass("OpenAI API Key:")
import openai

openai.api\_key \= "sk-<your-key>"

import os import getpass # os.environ\["OPENAI\_API\_KEY"\] = getpass.getpass("OpenAI API Key:") import openai openai.api\_key = "sk-"

In \[ \]:

Copied!

\# dimensions are for text-embedding-ada-002
try:
    pinecone.create\_index(
        "quickstart-index", dimension\=1536, metric\="euclidean", pod\_type\="p1"
    )
except Exception:
    \# most likely index already exists
    pass

\# dimensions are for text-embedding-ada-002 try: pinecone.create\_index( "quickstart-index", dimension=1536, metric="euclidean", pod\_type="p1" ) except Exception: # most likely index already exists pass

In \[ \]:

Copied!

pinecone\_index \= pinecone.Index("quickstart-index")

pinecone\_index = pinecone.Index("quickstart-index")

In \[ \]:

Copied!

\# Optional: delete data in your pinecone index
pinecone\_index.delete(deleteAll\=True, namespace\="test")

\# Optional: delete data in your pinecone index pinecone\_index.delete(deleteAll=True, namespace="test")

Out\[ \]:

{}

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, StorageContext
from llama\_index.vector\_stores.pinecone import PineconeVectorStore

from llama\_index.core import VectorStoreIndex, StorageContext from llama\_index.vector\_stores.pinecone import PineconeVectorStore

In \[ \]:

Copied!

from llama\_index.core.schema import TextNode

nodes \= \[
    TextNode(
        text\=(
            "Michael Jordan is a retired professional basketball player,"
            " widely regarded as one of the greatest basketball players of all"
            " time."
        ),
        metadata\={
            "category": "Sports",
            "country": "United States",
            "gender": "male",
            "born": 1963,
        },
    ),
    TextNode(
        text\=(
            "Angelina Jolie is an American actress, filmmaker, and"
            " humanitarian. She has received numerous awards for her acting"
            " and is known for her philanthropic work."
        ),
        metadata\={
            "category": "Entertainment",
            "country": "United States",
            "gender": "female",
            "born": 1975,
        },
    ),
    TextNode(
        text\=(
            "Elon Musk is a business magnate, industrial designer, and"
            " engineer. He is the founder, CEO, and lead designer of SpaceX,"
            " Tesla, Inc., Neuralink, and The Boring Company."
        ),
        metadata\={
            "category": "Business",
            "country": "United States",
            "gender": "male",
            "born": 1971,
        },
    ),
    TextNode(
        text\=(
            "Rihanna is a Barbadian singer, actress, and businesswoman. She"
            " has achieved significant success in the music industry and is"
            " known for her versatile musical style."
        ),
        metadata\={
            "category": "Music",
            "country": "Barbados",
            "gender": "female",
            "born": 1988,
        },
    ),
    TextNode(
        text\=(
            "Cristiano Ronaldo is a Portuguese professional footballer who is"
            " considered one of the greatest football players of all time. He"
            " has won numerous awards and set multiple records during his"
            " career."
        ),
        metadata\={
            "category": "Sports",
            "country": "Portugal",
            "gender": "male",
            "born": 1985,
        },
    ),
\]

from llama\_index.core.schema import TextNode nodes = \[ TextNode( text=( "Michael Jordan is a retired professional basketball player," " widely regarded as one of the greatest basketball players of all" " time." ), metadata={ "category": "Sports", "country": "United States", "gender": "male", "born": 1963, }, ), TextNode( text=( "Angelina Jolie is an American actress, filmmaker, and" " humanitarian. She has received numerous awards for her acting" " and is known for her philanthropic work." ), metadata={ "category": "Entertainment", "country": "United States", "gender": "female", "born": 1975, }, ), TextNode( text=( "Elon Musk is a business magnate, industrial designer, and" " engineer. He is the founder, CEO, and lead designer of SpaceX," " Tesla, Inc., Neuralink, and The Boring Company." ), metadata={ "category": "Business", "country": "United States", "gender": "male", "born": 1971, }, ), TextNode( text=( "Rihanna is a Barbadian singer, actress, and businesswoman. She" " has achieved significant success in the music industry and is" " known for her versatile musical style." ), metadata={ "category": "Music", "country": "Barbados", "gender": "female", "born": 1988, }, ), TextNode( text=( "Cristiano Ronaldo is a Portuguese professional footballer who is" " considered one of the greatest football players of all time. He" " has won numerous awards and set multiple records during his" " career." ), metadata={ "category": "Sports", "country": "Portugal", "gender": "male", "born": 1985, }, ), \]

In \[ \]:

Copied!

vector\_store \= PineconeVectorStore(
    pinecone\_index\=pinecone\_index, namespace\="test"
)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

vector\_store = PineconeVectorStore( pinecone\_index=pinecone\_index, namespace="test" ) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store)

In \[ \]:

Copied!

index \= VectorStoreIndex(nodes, storage\_context\=storage\_context)

index = VectorStoreIndex(nodes, storage\_context=storage\_context)

Upserted vectors: 100%|██████████| 5/5 \[00:00<00:00,  5.79it/s\]

#### Define Function Tool[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_query_cookbook/#define-function-tool)

Here we define the function interface, which is passed to OpenAI to perform auto-retrieval.

We were not able to get OpenAI to work with nested pydantic objects or tuples as arguments, so we converted the metadata filter keys and values into lists for the function API to work with.

In \[ \]:

Copied!

\# define function tool
from llama\_index.core.tools import FunctionTool
from llama\_index.core.vector\_stores import (
    VectorStoreInfo,
    MetadataInfo,
    MetadataFilter,
    MetadataFilters,
    FilterCondition,
    FilterOperator,
)
from llama\_index.core.retrievers import VectorIndexRetriever
from llama\_index.core.query\_engine import RetrieverQueryEngine

from typing import List, Tuple, Any
from pydantic import BaseModel, Field

\# hardcode top k for now
top\_k \= 3

\# define vector store info describing schema of vector store
vector\_store\_info \= VectorStoreInfo(
    content\_info\="brief biography of celebrities",
    metadata\_info\=\[
        MetadataInfo(
            name\="category",
            type\="str",
            description\=(
                "Category of the celebrity, one of \[Sports, Entertainment,"
                " Business, Music\]"
            ),
        ),
        MetadataInfo(
            name\="country",
            type\="str",
            description\=(
                "Country of the celebrity, one of \[United States, Barbados,"
                " Portugal\]"
            ),
        ),
        MetadataInfo(
            name\="gender",
            type\="str",
            description\=("Gender of the celebrity, one of \[male, female\]"),
        ),
        MetadataInfo(
            name\="born",
            type\="int",
            description\=("Born year of the celebrity, could be any integer"),
        ),
    \],
)

\# define function tool from llama\_index.core.tools import FunctionTool from llama\_index.core.vector\_stores import ( VectorStoreInfo, MetadataInfo, MetadataFilter, MetadataFilters, FilterCondition, FilterOperator, ) from llama\_index.core.retrievers import VectorIndexRetriever from llama\_index.core.query\_engine import RetrieverQueryEngine from typing import List, Tuple, Any from pydantic import BaseModel, Field # hardcode top k for now top\_k = 3 # define vector store info describing schema of vector store vector\_store\_info = VectorStoreInfo( content\_info="brief biography of celebrities", metadata\_info=\[ MetadataInfo( name="category", type="str", description=( "Category of the celebrity, one of \[Sports, Entertainment," " Business, Music\]" ), ), MetadataInfo( name="country", type="str", description=( "Country of the celebrity, one of \[United States, Barbados," " Portugal\]" ), ), MetadataInfo( name="gender", type="str", description=("Gender of the celebrity, one of \[male, female\]"), ), MetadataInfo( name="born", type="int", description=("Born year of the celebrity, could be any integer"), ), \], )

In \[ \]:

Copied!

\# define pydantic model for auto-retrieval function
class AutoRetrieveModel(BaseModel):
    query: str \= Field(..., description\="natural language query string")
    filter\_key\_list: List\[str\] \= Field(
        ..., description\="List of metadata filter field names"
    )
    filter\_value\_list: List\[Any\] \= Field(
        ...,
        description\=(
            "List of metadata filter field values (corresponding to names"
            " specified in filter\_key\_list)"
        ),
    )
    filter\_operator\_list: List\[str\] \= Field(
        ...,
        description\=(
            "Metadata filters conditions (could be one of <, <=, >, >=, , !=)" ), ) filter\_condition: str = Field( ..., description=("Metadata filters condition values (could be AND or OR)"), ) description = f"""\\ Use this tool to look up biographical information about celebrities. The vector database schema is given below: {vector\_store\_info.json()} """

Define AutoRetrieve Functions

In \[ \]:

Copied!

def auto\_retrieve\_fn(
    query: str,
    filter\_key\_list: List\[str\],
    filter\_value\_list: List\[any\],
    filter\_operator\_list: List\[str\],
    filter\_condition: str,
):
    """Auto retrieval function.

    Performs auto-retrieval from a vector database, and then applies a set of filters.

    """
    query \= query or "Query"

    metadata\_filters \= \[
        MetadataFilter(key\=k, value\=v, operator\=op)
        for k, v, op in zip(
            filter\_key\_list, filter\_value\_list, filter\_operator\_list
        )
    \]
    retriever \= VectorIndexRetriever(
        index,
        filters\=MetadataFilters(
            filters\=metadata\_filters, condition\=filter\_condition
        ),
        top\_k\=top\_k,
    )
    query\_engine \= RetrieverQueryEngine.from\_args(retriever)

    response \= query\_engine.query(query)
    return str(response)

auto\_retrieve\_tool \= FunctionTool.from\_defaults(
    fn\=auto\_retrieve\_fn,
    name\="celebrity\_bios",
    description\=description,
    fn\_schema\=AutoRetrieveModel,
)

def auto\_retrieve\_fn( query: str, filter\_key\_list: List\[str\], filter\_value\_list: List\[any\], filter\_operator\_list: List\[str\], filter\_condition: str, ): """Auto retrieval function. Performs auto-retrieval from a vector database, and then applies a set of filters. """ query = query or "Query" metadata\_filters = \[ MetadataFilter(key=k, value=v, operator=op) for k, v, op in zip( filter\_key\_list, filter\_value\_list, filter\_operator\_list ) \] retriever = VectorIndexRetriever( index, filters=MetadataFilters( filters=metadata\_filters, condition=filter\_condition ), top\_k=top\_k, ) query\_engine = RetrieverQueryEngine.from\_args(retriever) response = query\_engine.query(query) return str(response) auto\_retrieve\_tool = FunctionTool.from\_defaults( fn=auto\_retrieve\_fn, name="celebrity\_bios", description=description, fn\_schema=AutoRetrieveModel, )

#### Initialize Agent[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_query_cookbook/#initialize-agent)

In \[ \]:

Copied!

from llama\_index.agent.openai import OpenAIAgent
from llama\_index.llms.openai import OpenAI

agent \= OpenAIAgent.from\_tools(
    \[auto\_retrieve\_tool\],
    llm\=OpenAI(temperature\=0, model\="gpt-4-0613"),
    verbose\=True,
)

from llama\_index.agent.openai import OpenAIAgent from llama\_index.llms.openai import OpenAI agent = OpenAIAgent.from\_tools( \[auto\_retrieve\_tool\], llm=OpenAI(temperature=0, model="gpt-4-0613"), verbose=True, )

In \[ \]:

Copied!

response \= agent.chat("Tell me about two celebrities from the United States. ")
print(str(response))

response = agent.chat("Tell me about two celebrities from the United States. ") print(str(response))

STARTING TURN 1
---------------


Calling function: celebrity\_bios with args: {
"query": "celebrities from the United States",
"filter\_key\_list": \["country"\],
"filter\_value\_list": \["United States"\],
"filter\_operator\_list": \["

STARTING TURN 2
---------------

Here are two celebrities from the United States:

1. \*\*Angelina Jolie\*\*: She is an American actress, filmmaker, and humanitarian. The recipient of numerous accolities, including an Academy Award and three Golden Globe Awards, she has been named Hollywood's highest-paid actress multiple times.

2. \*\*Michael Jordan\*\*: He is a former professional basketball player and the principal owner of the Charlotte Hornets of the National Basketball Association (NBA). He played 15 seasons in the NBA, winning six championships with the Chicago Bulls. He is considered one of the greatest players in the history of the NBA.

In \[ \]:

Copied!

response \= agent.chat("Tell me about two celebrities born after 1980. ")
print(str(response))

response = agent.chat("Tell me about two celebrities born after 1980. ") print(str(response))

STARTING TURN 1
---------------


Calling function: celebrity\_bios with args: {
"query": "celebrities born after 1980",
"filter\_key\_list": \["born"\],
"filter\_value\_list": \[1980\],
"filter\_operator\_list": \[">"\],
"filter\_condition": "and"
}
Got output: Rihanna and Cristiano Ronaldo are both celebrities who were born after 1980.
 Calling Function ", ">"\],
"filter\_condition": "and"
}
Got output: Elon Musk is a notable business celebrity who was born in 1971.
 Calling Function 

Calling function: vector\_tool with args: {
  "input": "Tell me about the arts and culture of Tokyo"
}
Got output: Tokyo has a rich arts and culture scene, with many theaters for performing arts, including national and private theaters for traditional forms of Japanese drama. Noteworthy theaters are the National Noh Theatre for noh and the Kabuki-za for Kabuki. Symphony orchestras and other musical organizations perform modern and traditional music. The New National Theater Tokyo in Shibuya is the national center for the performing arts, including opera, ballet, contemporary dance, and drama. Tokyo also hosts modern Japanese and international pop and rock music at various venues, ranging from intimate clubs to internationally known areas such as the Nippon Budokan.

Many different festivals occur throughout Tokyo, with major events including the Sannō at Hie Shrine, the Sanja at Asakusa Shrine, and the biennial Kanda Festivals. Annually on the last Saturday of July, a massive fireworks display over the Sumida River attracts over a million viewers. Once cherry blossoms bloom in spring, residents gather in Ueno Park, Inokashira Park, and the Shinjuku Gyoen National Garden for picnics under the blossoms. Harajuku, a neighborhood in Shibuya, is known internationally for its youth style, fashion, and cosplay.

Tokyo is also renowned for its fine dining, with Michelin awarding a significant number of stars to the city's restaurants. As of 2017, 227 restaurants in Tokyo have been awarded Michelin stars, surpassing the number awarded in Paris.
 Calling Function 

Out\[ \]:

Response(response='Berlin\\'s history dates back to the 15th century when it was established as the capital of the Margraviate of Brandenburg. The Hohenzollern family ruled Berlin until 1918, first as electors of Brandenburg, then as kings of Prussia, and eventually as German emperors. In 1443, Frederick II Irontooth started the construction of a new royal palace in the twin city Berlin-Cölln.\\n\\nThe Thirty Years\\' War between 1618 and 1648 devastated Berlin, with the city losing half of its population. Frederick William, known as the "Great Elector", initiated a policy of promoting immigration and religious tolerance. In 1701, the dual state of the Margraviate of Brandenburg and the Duchy of Prussia formed the Kingdom of Prussia, with Berlin as its capital. Under the rule of Frederick II, Berlin became a center of the Enlightenment.\\n\\nThe Industrial Revolution in the 19th century transformed Berlin, expanding its economy and population. In 1871, Berlin became the capital of the newly founded German Empire. The early 20th century saw Berlin as a fertile ground for the German Expressionist movement. At the end of the First World War in 1918, a republic was proclaimed, and in 1920, the Greater Berlin Act incorporated dozens of suburban cities, villages, and estates around Berlin.', source\_nodes=\[\], extra\_info=None)

In \[ \]:

Copied!

response \= agent.chat(
    "Can you give me the country corresponding to each city?"
)
print(str(response))

response = agent.chat( "Can you give me the country corresponding to each city?" ) print(str(response))

\
Calling function: sql\_tool with args: {
  "input": "SELECT city, country FROM city\_stats"
}
Got output:  The cities Toronto, Tokyo, and Berlin are located in the countries Canada, Japan, and Germany respectively.


Out\[ \]:

Response(response='Sure, here are the countries corresponding to each city:\\n\\n- Toronto is in Canada\\n- Tokyo is in Japan\\n- Berlin is in Germany', source\_nodes=\[\], extra\_info=None)

Back to top

[Previous Single-Turn Multi-Function Calling OpenAI Agents](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_parallel_function_calling/)[Next OpenAI Agent Query Planning](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_query_plan/)

Hi, how can I help you?

🦙
