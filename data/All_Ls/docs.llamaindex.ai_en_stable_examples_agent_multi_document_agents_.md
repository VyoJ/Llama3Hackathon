Title: Multi-Document Agents - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/multi_document_agents/

Markdown Content:
Multi-Document Agents - LlamaIndex


In this guide, you learn towards setting up an agent that can effectively answer different types of questions over a larger set of documents.

These questions include the following

*   QA over a specific doc
*   QA comparing different docs
*   Summaries over a specific doc
*   Comparing summaries between different docs

We do this with the following architecture:

*   setup a "document agent" over each Document: each doc agent can do QA/summarization within its doc
*   setup a top-level agent over this set of document agents. Do tool retrieval and then do CoT over the set of tools to answer a question.

Setup and Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/agent/multi_document_agents/#setup-and-download-data)
------------------------------------------------------------------------------------------------------------------------------

In this section, we'll define imports and then download Wikipedia articles about different cities. Each article is stored separately.

We load in 18 cities - this is not quite at the level of "hundreds" of documents but its still large enough to warrant some top-level document retrieval!

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-agent\-openai
%pip install llama\-index\-embeddings\-openai
%pip install llama\-index\-llms\-openai

%pip install llama-index-agent-openai %pip install llama-index-embeddings-openai %pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

from llama\_index.core import (
    VectorStoreIndex,
    SimpleKeywordTableIndex,
    SimpleDirectoryReader,
)
from llama\_index.core import SummaryIndex
from llama\_index.core.schema import IndexNode
from llama\_index.core.tools import QueryEngineTool, ToolMetadata
from llama\_index.llms.openai import OpenAI
from llama\_index.core.callbacks import CallbackManager

from llama\_index.core import ( VectorStoreIndex, SimpleKeywordTableIndex, SimpleDirectoryReader, ) from llama\_index.core import SummaryIndex from llama\_index.core.schema import IndexNode from llama\_index.core.tools import QueryEngineTool, ToolMetadata from llama\_index.llms.openai import OpenAI from llama\_index.core.callbacks import CallbackManager

In \[ \]:

Copied!

wiki\_titles \= \[
    "Toronto",
    "Seattle",
    "Chicago",
    "Boston",
    "Houston",
    "Tokyo",
    "Berlin",
    "Lisbon",
    "Paris",
    "London",
    "Atlanta",
    "Munich",
    "Shanghai",
    "Beijing",
    "Copenhagen",
    "Moscow",
    "Cairo",
    "Karachi",
\]

wiki\_titles = \[ "Toronto", "Seattle", "Chicago", "Boston", "Houston", "Tokyo", "Berlin", "Lisbon", "Paris", "London", "Atlanta", "Munich", "Shanghai", "Beijing", "Copenhagen", "Moscow", "Cairo", "Karachi", \]

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

Define Global LLM and Embeddings

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..."

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI
from llama\_index.embeddings.openai import OpenAIEmbedding
from llama\_index.core import Settings

Settings.llm \= OpenAI(temperature\=0, model\="gpt-3.5-turbo")
Settings.embed\_model \= OpenAIEmbedding(model\="text-embedding-ada-002")

from llama\_index.llms.openai import OpenAI from llama\_index.embeddings.openai import OpenAIEmbedding from llama\_index.core import Settings Settings.llm = OpenAI(temperature=0, model="gpt-3.5-turbo") Settings.embed\_model = OpenAIEmbedding(model="text-embedding-ada-002")

Building Multi-Document Agents[¶](https://docs.llamaindex.ai/en/stable/examples/agent/multi_document_agents/#building-multi-document-agents)
--------------------------------------------------------------------------------------------------------------------------------------------

In this section we show you how to construct the multi-document agent. We first build a document agent for each document, and then define the top-level parent agent with an object index.

### Build Document Agent for each Document[¶](https://docs.llamaindex.ai/en/stable/examples/agent/multi_document_agents/#build-document-agent-for-each-document)

In this section we define "document agents" for each document.

We define both a vector index (for semantic search) and summary index (for summarization) for each document. The two query engines are then converted into tools that are passed to an OpenAI function calling agent.

This document agent can dynamically choose to perform semantic search or summarization within a given document.

We create a separate document agent for each city.

In \[ \]:

Copied!

from llama\_index.agent.openai import OpenAIAgent
from llama\_index.core import load\_index\_from\_storage, StorageContext
from llama\_index.core.node\_parser import SentenceSplitter
import os

node\_parser \= SentenceSplitter()

\# Build agents dictionary
agents \= {}
query\_engines \= {}

\# this is for the baseline
all\_nodes \= \[\]

for idx, wiki\_title in enumerate(wiki\_titles):
    nodes \= node\_parser.get\_nodes\_from\_documents(city\_docs\[wiki\_title\])
    all\_nodes.extend(nodes)

    if not os.path.exists(f"./data/{wiki\_title}"):
        \# build vector index
        vector\_index \= VectorStoreIndex(nodes)
        vector\_index.storage\_context.persist(
            persist\_dir\=f"./data/{wiki\_title}"
        )
    else:
        vector\_index \= load\_index\_from\_storage(
            StorageContext.from\_defaults(persist\_dir\=f"./data/{wiki\_title}"),
        )

    \# build summary index
    summary\_index \= SummaryIndex(nodes)
    \# define query engines
    vector\_query\_engine \= vector\_index.as\_query\_engine(llm\=Settings.llm)
    summary\_query\_engine \= summary\_index.as\_query\_engine(llm\=Settings.llm)

    \# define tools
    query\_engine\_tools \= \[
        QueryEngineTool(
            query\_engine\=vector\_query\_engine,
            metadata\=ToolMetadata(
                name\="vector\_tool",
                description\=(
                    "Useful for questions related to specific aspects of"
                    f" {wiki\_title} (e.g. the history, arts and culture,"
                    " sports, demographics, or more)."
                ),
            ),
        ),
        QueryEngineTool(
            query\_engine\=summary\_query\_engine,
            metadata\=ToolMetadata(
                name\="summary\_tool",
                description\=(
                    "Useful for any requests that require a holistic summary"
                    f" of EVERYTHING about {wiki\_title}. For questions about"
                    " more specific sections, please use the vector\_tool."
                ),
            ),
        ),
    \]

    \# build agent
    function\_llm \= OpenAI(model\="gpt-4")
    agent \= OpenAIAgent.from\_tools(
        query\_engine\_tools,
        llm\=function\_llm,
        verbose\=True,
        system\_prompt\=f"""\\
You are a specialized agent designed to answer queries about {wiki\_title}.
You must ALWAYS use at least one of the tools provided when answering a question; do NOT rely on prior knowledge.\\
""",
    )

    agents\[wiki\_title\] \= agent
    query\_engines\[wiki\_title\] \= vector\_index.as\_query\_engine(
        similarity\_top\_k\=2
    )

from llama\_index.agent.openai import OpenAIAgent from llama\_index.core import load\_index\_from\_storage, StorageContext from llama\_index.core.node\_parser import SentenceSplitter import os node\_parser = SentenceSplitter() # Build agents dictionary agents = {} query\_engines = {} # this is for the baseline all\_nodes = \[\] for idx, wiki\_title in enumerate(wiki\_titles): nodes = node\_parser.get\_nodes\_from\_documents(city\_docs\[wiki\_title\]) all\_nodes.extend(nodes) if not os.path.exists(f"./data/{wiki\_title}"): # build vector index vector\_index = VectorStoreIndex(nodes) vector\_index.storage\_context.persist( persist\_dir=f"./data/{wiki\_title}" ) else: vector\_index = load\_index\_from\_storage( StorageContext.from\_defaults(persist\_dir=f"./data/{wiki\_title}"), ) # build summary index summary\_index = SummaryIndex(nodes) # define query engines vector\_query\_engine = vector\_index.as\_query\_engine(llm=Settings.llm) summary\_query\_engine = summary\_index.as\_query\_engine(llm=Settings.llm) # define tools query\_engine\_tools = \[ QueryEngineTool( query\_engine=vector\_query\_engine, metadata=ToolMetadata( name="vector\_tool", description=( "Useful for questions related to specific aspects of" f" {wiki\_title} (e.g. the history, arts and culture," " sports, demographics, or more)." ), ), ), QueryEngineTool( query\_engine=summary\_query\_engine, metadata=ToolMetadata( name="summary\_tool", description=( "Useful for any requests that require a holistic summary" f" of EVERYTHING about {wiki\_title}. For questions about" " more specific sections, please use the vector\_tool." ), ), ), \] # build agent function\_llm = OpenAI(model="gpt-4") agent = OpenAIAgent.from\_tools( query\_engine\_tools, llm=function\_llm, verbose=True, system\_prompt=f"""\\ You are a specialized agent designed to answer queries about {wiki\_title}. You must ALWAYS use at least one of the tools provided when answering a question; do NOT rely on prior knowledge.\\ """, ) agents\[wiki\_title\] = agent query\_engines\[wiki\_title\] = vector\_index.as\_query\_engine( similarity\_top\_k=2 )

### Build Retriever-Enabled OpenAI Agent[¶](https://docs.llamaindex.ai/en/stable/examples/agent/multi_document_agents/#build-retriever-enabled-openai-agent)

We build a top-level agent that can orchestrate across the different document agents to answer any user query.

This agent takes in all document agents as tools. This specific agent `RetrieverOpenAIAgent` performs tool retrieval before tool use (unlike a default agent that tries to put all tools in the prompt).

Here we use a top-k retriever, but we encourage you to customize the tool retriever method!

In \[ \]:

Copied!

\# define tool for each document agent
all\_tools \= \[\]
for wiki\_title in wiki\_titles:
    wiki\_summary \= (
        f"This content contains Wikipedia articles about {wiki\_title}. Use"
        f" this tool if you want to answer any questions about {wiki\_title}.\\n"
    )
    doc\_tool \= QueryEngineTool(
        query\_engine\=agents\[wiki\_title\],
        metadata\=ToolMetadata(
            name\=f"tool\_{wiki\_title}",
            description\=wiki\_summary,
        ),
    )
    all\_tools.append(doc\_tool)

\# define tool for each document agent all\_tools = \[\] for wiki\_title in wiki\_titles: wiki\_summary = ( f"This content contains Wikipedia articles about {wiki\_title}. Use" f" this tool if you want to answer any questions about {wiki\_title}.\\n" ) doc\_tool = QueryEngineTool( query\_engine=agents\[wiki\_title\], metadata=ToolMetadata( name=f"tool\_{wiki\_title}", description=wiki\_summary, ), ) all\_tools.append(doc\_tool)

In \[ \]:

Copied!

\# define an "object" index and retriever over these tools
from llama\_index.core import VectorStoreIndex
from llama\_index.core.objects import ObjectIndex

obj\_index \= ObjectIndex.from\_objects(
    all\_tools,
    index\_cls\=VectorStoreIndex,
)

\# define an "object" index and retriever over these tools from llama\_index.core import VectorStoreIndex from llama\_index.core.objects import ObjectIndex obj\_index = ObjectIndex.from\_objects( all\_tools, index\_cls=VectorStoreIndex, )

In \[ \]:

Copied!

from llama\_index.agent.openai import OpenAIAgent

top\_agent \= OpenAIAgent.from\_tools(
    tool\_retriever\=obj\_index.as\_retriever(similarity\_top\_k\=3),
    system\_prompt\=""" \\
You are an agent designed to answer queries about a set of given cities.
Please always use the tools provided to answer a question. Do not rely on prior knowledge.\\

""",
    verbose\=True,
)

from llama\_index.agent.openai import OpenAIAgent top\_agent = OpenAIAgent.from\_tools( tool\_retriever=obj\_index.as\_retriever(similarity\_top\_k=3), system\_prompt=""" \\ You are an agent designed to answer queries about a set of given cities. Please always use the tools provided to answer a question. Do not rely on prior knowledge.\\ """, verbose=True, )

### Define Baseline Vector Store Index[¶](https://docs.llamaindex.ai/en/stable/examples/agent/multi_document_agents/#define-baseline-vector-store-index)

As a point of comparison, we define a "naive" RAG pipeline which dumps all docs into a single vector index collection.

We set the top\_k = 4

In \[ \]:

Copied!

base\_index \= VectorStoreIndex(all\_nodes)
base\_query\_engine \= base\_index.as\_query\_engine(similarity\_top\_k\=4)

base\_index = VectorStoreIndex(all\_nodes) base\_query\_engine = base\_index.as\_query\_engine(similarity\_top\_k=4)

Running Example Queries[¶](https://docs.llamaindex.ai/en/stable/examples/agent/multi_document_agents/#running-example-queries)
------------------------------------------------------------------------------------------------------------------------------

Let's run some example queries, ranging from QA / summaries over a single document to QA / summarization over multiple documents.

In \[ \]:

Copied!

\# should use Boston agent -> vector tool
response \= top\_agent.query("Tell me about the arts and culture in Boston")

\# should use Boston agent -> vector tool response = top\_agent.query("Tell me about the arts and culture in Boston")

\
Calling function: tool\_Boston with args: {
  "input": "arts and culture"
}

Calling function: vector\_tool with args: {
  "input": "arts and culture"
}
Got output: Boston is known for its vibrant arts and culture scene. The city is home to a number of performing arts organizations, including the Boston Ballet, Boston Lyric Opera Company, Opera Boston, Boston Baroque, and the Handel and Haydn Society. There are also several theaters in or near the Theater District, such as the Cutler Majestic Theatre, Citi Performing Arts Center, the Colonial Theater, and the Orpheum Theatre. Boston is a center for contemporary classical music, with groups like the Boston Modern Orchestra Project and Boston Musica Viva. The city also hosts major annual events, such as First Night, the Boston Early Music Festival, and the Boston Arts Festival. In addition, Boston has several art museums and galleries, including the Museum of Fine Arts, the Isabella Stewart Gardner Museum, and the Institute of Contemporary Art.


In \[ \]:

Copied!

print(response)

print(response)

Boston has a rich arts and culture scene, with a variety of performing arts organizations and venues. The city is home to renowned institutions such as the Boston Ballet, Boston Lyric Opera Company, Opera Boston, Boston Baroque, and the Handel and Haydn Society. The Theater District in Boston is a hub for theatrical performances, with theaters like the Cutler Majestic Theatre, Citi Performing Arts Center, Colonial Theater, and Orpheum Theatre.

In addition to performing arts, Boston also has a thriving contemporary classical music scene, with groups like the Boston Modern Orchestra Project and Boston Musica Viva. The city hosts several annual events that celebrate the arts, including First Night, the Boston Early Music Festival, and the Boston Arts Festival.

Boston is also known for its visual arts scene, with a number of art museums and galleries. The Museum of Fine Arts, the Isabella Stewart Gardner Museum, and the Institute of Contemporary Art are among the notable institutions in the city. These museums offer a diverse range of art collections, spanning from ancient to contemporary art, and attract art enthusiasts from around the world.

In \[ \]:

Copied!

\# baseline
response \= base\_query\_engine.query(
    "Tell me about the arts and culture in Boston"
)
print(str(response))

\# baseline response = base\_query\_engine.query( "Tell me about the arts and culture in Boston" ) print(str(response))

Boston has a rich arts and culture scene. The city is home to a variety of performing arts organizations, such as the Boston Ballet, Boston Lyric Opera Company, Opera Boston, Boston Baroque, and the Handel and Haydn Society. Additionally, there are numerous contemporary classical music groups associated with the city's conservatories and universities, like the Boston Modern Orchestra Project and Boston Musica Viva. The Theater District in Boston is a hub for theater, with notable venues including the Cutler Majestic Theatre, Citi Performing Arts Center, the Colonial Theater, and the Orpheum Theatre. Boston also hosts several significant annual events, including First Night, the Boston Early Music Festival, the Boston Arts Festival, and the Boston gay pride parade and festival. The city is renowned for its historic sites connected to the American Revolution, as well as its art museums and galleries, such as the Museum of Fine Arts, Isabella Stewart Gardner Museum, and the Institute of Contemporary Art.

In \[ \]:

Copied!

\# should use Houston agent -> vector tool
response \= top\_agent.query(
    "Give me a summary of all the positive aspects of Houston"
)

\# should use Houston agent -> vector tool response = top\_agent.query( "Give me a summary of all the positive aspects of Houston" )

\
Calling function: tool\_Houston with args: {
  "input": "positive aspects"
}

Calling function: summary\_tool with args: {
  "input": "positive aspects"
}
Got output: Houston has many positive aspects that make it an attractive place to live and visit. The city's diverse population, with people from different ethnic and religious backgrounds, adds to its cultural richness and inclusiveness. Additionally, Houston is home to the Texas Medical Center, which is the largest concentration of healthcare and research institutions in the world. The presence of NASA's Johnson Space Center also highlights Houston's importance in the fields of medicine and space exploration. The city's strong economy, supported by industries such as energy, manufacturing, aeronautics, and transportation, provides numerous economic opportunities for residents and visitors alike. Furthermore, Houston has a thriving visual and performing arts scene, including a theater district and a variety of museums and galleries. Overall, Houston's diverse community, cultural attractions, and economic prospects make it an exceptionally appealing city.


In \[ \]:

Copied!

print(response)

print(response)

Houston has numerous positive aspects that make it a desirable place to live and visit. Some of these include:

1. Diversity: Houston is known for its diverse population, with people from different ethnic and religious backgrounds. This diversity adds to the city's cultural richness and inclusiveness.

2. Healthcare and Research Institutions: The city is home to the Texas Medical Center, the largest concentration of healthcare and research institutions in the world. This makes Houston a hub for medical innovation and healthcare services.

3. Space Exploration: Houston is also known for NASA's Johnson Space Center, highlighting the city's significant role in space exploration.

4. Strong Economy: Houston's economy is robust and diverse, supported by industries such as energy, manufacturing, aeronautics, and transportation. This provides numerous economic opportunities for its residents.

5. Arts and Culture: The city has a thriving visual and performing arts scene, with a theater district and a variety of museums and galleries. This makes Houston a vibrant place for art lovers and creatives.

Overall, these aspects contribute to making Houston an appealing and dynamic city.

In \[ \]:

Copied!

\# baseline
response \= base\_query\_engine.query(
    "Give me a summary of all the positive aspects of Houston"
)
print(str(response))

\# baseline response = base\_query\_engine.query( "Give me a summary of all the positive aspects of Houston" ) print(str(response))

Houston has several positive aspects that contribute to its reputation as a thriving city. It is home to a diverse and growing international community, with a large number of foreign banks and consular offices representing 92 countries. The city has received numerous accolades, including being ranked as one of the best cities for employment, college graduates, and homebuyers. Houston has a strong economy, with a broad industrial base in sectors such as energy, manufacturing, aeronautics, and healthcare. It is also a major center for the oil and gas industry and has the second-most Fortune 500 headquarters in the United States. The city's cultural scene is vibrant, with a variety of annual events celebrating different cultures, as well as a reputation for diverse and excellent food. Houston is known for its world-class museums and performing arts scene. Additionally, the city has made significant investments in renewable energy sources like wind and solar. Overall, Houston offers a high quality of life, reasonable living costs, and abundant employment opportunities.

In \[ \]:

Copied!

\# baseline: the response doesn't quite match the sources...
response.source\_nodes\[1\].get\_content()

\# baseline: the response doesn't quite match the sources... response.source\_nodes\[1\].get\_content()

In \[ \]:

Copied!

response \= top\_agent.query(
    "Tell the demographics of Houston, and then compare that with the"
    " demographics of Chicago"
)

response = top\_agent.query( "Tell the demographics of Houston, and then compare that with the" " demographics of Chicago" )

\
Calling function: tool\_Houston with args: {
  "input": "demographics"
}

Calling function: vector\_tool with args: {
  "input": "demographics"
}
Got output: Houston is a majority-minority city with a diverse population. According to the U.S. Census Bureau, in 2019, non-Hispanic whites made up 23.3% of the population, Hispanics and Latino Americans 45.8%, Blacks or African Americans 22.4%, and Asian Americans 6.5%. The largest Hispanic or Latino American ethnic group in the city is Mexican Americans, followed by Puerto Ricans and Cuban Americans. Houston is also home to the largest African American community west of the Mississippi River. Additionally, Houston has a growing Muslim population, with Muslims estimated to make up 1.2% of the city's population. The city is known for its LGBT community and is home to one of the largest pride parades in the United States. The Hindu, Sikh, and Buddhist communities are also growing in Houston. Overall, Houston is considered one of the most ethnically and culturally diverse metropolitan areas in the country.


Calling function: tool\_Chicago with args: {
  "input": "demographics"
}

Calling function: vector\_tool with args: {
  "input": "demographics"
}
Got output: Chicago has a diverse demographic makeup. It experienced rapid population growth during its early years, becoming one of the fastest-growing cities in the world. Waves of immigrants from various European countries, as well as African Americans from the American South, contributed to the city's population growth. Over time, Chicago's population has fluctuated, with a decline in the latter half of the 20th century followed by a rise in recent years. As of the latest census estimates, the largest racial or ethnic groups in Chicago are non-Hispanic White, Black, and Hispanic. Additionally, Chicago has a significant LGBT population and is known for its cultural diversity.


In \[ \]:

Copied!

print(response)

print(response)

Houston has a diverse population with a demographic makeup that includes non-Hispanic whites (23.3%), Hispanics and Latino Americans (45.8%), Blacks or African Americans (22.4%), and Asian Americans (6.5%). The largest Hispanic or Latino American ethnic group in Houston is Mexican Americans. Houston is also home to the largest African American community west of the Mississippi River and has a growing Muslim population.

On the other hand, Chicago is also known for its diverse demographics. The city has a significant non-Hispanic White population, along with a substantial Black population and Hispanic population. Chicago is celebrated for its cultural diversity and has a significant LGBT population.

Both Houston and Chicago have diverse populations, with a mix of different racial and ethnic groups contributing to their vibrant communities.

In \[ \]:

Copied!

\# baseline
response \= base\_query\_engine.query(
    "Tell the demographics of Houston, and then compare that with the"
    " demographics of Chicago"
)
print(str(response))

\# baseline response = base\_query\_engine.query( "Tell the demographics of Houston, and then compare that with the" " demographics of Chicago" ) print(str(response))

Houston is the most populous city in Texas and the fourth-most populous city in the United States. It has a population of 2,304,580 as of the 2020 U.S. census. The city is known for its diversity, with a significant proportion of minorities. In 2019, non-Hispanic whites made up 23.3% of the population, Hispanics and Latino Americans 45.8%, Blacks or African Americans 22.4%, and Asian Americans 6.5%. The largest Hispanic or Latino American ethnic group in Houston is Mexican Americans, comprising 31.6% of the population.

In comparison, Chicago is the third-most populous city in the United States. According to the 2020 U.S. census, Chicago has a population of 2,746,388. The demographics of Chicago are different from Houston, with non-Hispanic whites making up 32.7% of the population, Hispanics and Latino Americans 29.9%, Blacks or African Americans 29.8%, and Asian Americans 7.6%. The largest Hispanic or Latino American ethnic group in Chicago is Mexican Americans, comprising 21.6% of the population.

Overall, both Houston and Chicago have diverse populations, but the specific demographic composition differs between the two cities.

In \[ \]:

Copied!

\# baseline: the response tells you nothing about Chicago...
response.source\_nodes\[3\].get\_content()

\# baseline: the response tells you nothing about Chicago... response.source\_nodes\[3\].get\_content()

In \[ \]:

Copied!

response \= top\_agent.query(
    "Tell me the differences between Shanghai and Beijing in terms of history"
    " and current economy"
)

response = top\_agent.query( "Tell me the differences between Shanghai and Beijing in terms of history" " and current economy" )

\
Calling function: tool\_Shanghai with args: {
  "input": "history"
}

Calling function: vector\_tool with args: {
  "input": "history"
}
Got output: Shanghai has a rich history that dates back to ancient times. However, in the context provided, the history of Shanghai is mainly discussed in relation to its modern development. After the war, Shanghai's economy experienced significant growth, with increased agricultural and industrial output. The city's administrative divisions were rearranged, and it became a center for radical leftism during the 1950s and 1960s. The Cultural Revolution had a severe impact on Shanghai's society, but the city maintained economic production with a positive growth rate. Shanghai also played a significant role in China's Third Front campaign and has been a major contributor of tax revenue to the central government. Economic reforms were initiated in Shanghai in 1990, leading to the development of the Pudong district and its classification as an Alpha+ city.


Calling function: tool\_Beijing with args: {
  "input": "history"
}

Calling function: vector\_tool with args: {
  "input": "history"
}
Got output: Beijing has a rich history that spans several dynasties. It was the capital of the Ming dynasty, during which the city took its current shape and many of its major attractions, such as the Forbidden City and the Temple of Heaven, were constructed. The Qing dynasty succeeded the Ming dynasty and made Beijing its sole capital. During this time, the Imperial residence and the general layout of the city remained largely unchanged. However, the city faced challenges during the Second Opium War and the Boxer Rebellion, resulting in the looting and destruction of important structures. In the early 20th century, Beijing saw the signing of a peace agreement between the Eight-Nation Alliance and the Chinese government, which led to the restoration of Qing dynasty rule. However, the dynasty eventually collapsed in 1911.


Calling function: tool\_Shanghai with args: {
  "input": "current economy"
}

Calling function: vector\_tool with args: {
  "input": "current economy"
}
Got output: The current economy of Shanghai is strong and thriving. It is a global center for finance and innovation, and a national center for commerce, trade, and transportation. The city has a diverse economy, with its six largest industries comprising about half of its GDP. Shanghai has experienced rapid development and has been one of the fastest-developing cities in the world. It has recorded double-digit GDP growth in almost every year between 1992 and 2008. As of 2021, Shanghai had a GDP of CN¥4.46 trillion ($1.106 trillion in PPP), making it one of the wealthiest cities in China. It is also the most expensive city in mainland China to live in. Shanghai is a major player in the global financial industry, ranking first in Asia and third globally in the Global Financial Centres Index. It is home to the Shanghai Stock Exchange, the largest stock exchange in China and the fourth-largest in the world. The city has attracted significant foreign investment and has been a hub for the technology industry and startups. Overall, the current economy of Shanghai is robust and continues to grow.


Calling function: tool\_Beijing with args: {
  "input": "current economy"
}

Calling function: vector\_tool with args: {
  "input": "current economy"
}
Got output: The current economy of Beijing is dominated by the tertiary sector, which includes services such as professional services, wholesale and retail, information technology, commercial real estate, scientific research, and residential real estate. This sector generated 83.8% of the city's output in 2022. The secondary sector, which includes manufacturing and construction, accounted for 15.8% of output, while the primary sector, which includes agriculture and mining, contributed only 0.26%. The city has also identified six high-end economic output zones that are driving local economic growth, including Zhongguancun, Beijing Financial Street, Beijing Central Business District (CBD), Beijing Economic and Technological Development Area (Yizhuang), Beijing Airport Economic Zone, and Beijing Olympic Center Zone. These zones are home to various industries and sectors, such as technology companies, financial institutions, office buildings, industrial parks, and entertainment and sports centers.


In \[ \]:

Copied!

print(str(response))

print(str(response))

In terms of history, both Shanghai and Beijing have rich and complex pasts. Shanghai's history dates back to ancient times, but its modern development is particularly noteworthy. It experienced significant economic growth after the war and played a major role in China's economic reforms. Beijing, on the other hand, has a history that spans several dynasties and served as the capital during the Ming and Qing dynasties. It has preserved its historical heritage while evolving into a modern metropolis.

In terms of current economy, Shanghai is a global center for finance and innovation. It has a diverse economy and has experienced rapid development, with a high GDP and significant foreign investment. It is a major player in the global financial industry and is home to the Shanghai Stock Exchange. Beijing's economy is primarily driven by the tertiary sector, with a focus on services such as professional services, information technology, and commercial real estate. It has identified high-end economic output zones that are driving local economic growth.

Overall, both cities have thriving economies, but Shanghai has a stronger focus on finance and global influence, while Beijing has a diverse economy with a focus on services and high-end economic zones.

In \[ \]:

Copied!

\# baseline
response \= base\_query\_engine.query(
    "Tell me the differences between Shanghai and Beijing in terms of history"
    " and current economy"
)
print(str(response))

\# baseline response = base\_query\_engine.query( "Tell me the differences between Shanghai and Beijing in terms of history" " and current economy" ) print(str(response))

Shanghai and Beijing have distinct differences in terms of history and current economy. Historically, Shanghai was the largest and most prosperous city in East Asia during the 1930s, while Beijing served as the capital of the Republic of China and later the People's Republic of China. Shanghai experienced significant growth and redevelopment in the 1990s, while Beijing expanded its urban area and underwent rapid development in the last two decades.

In terms of the current economy, Shanghai is considered the "showpiece" of China's booming economy. It is a global center for finance and innovation, with a strong focus on industries such as retail, finance, IT, real estate, machine manufacturing, and automotive manufacturing. Shanghai is also home to the world's busiest container port, the Port of Shanghai. The city has a high GDP and is classified as an Alpha+ city by the Globalization and World Cities Research Network.

On the other hand, Beijing is a global financial center and ranks third globally in the Global Financial Centres Index. It is also a hub for the Chinese and global technology industry, with a large startup ecosystem. Beijing has a strong presence in industries such as finance, technology, and pharmaceuticals. The city is home to the headquarters of large state banks and insurance companies, as well as the country's financial regulatory agencies.

Overall, while both Shanghai and Beijing are important economic centers in China, Shanghai has a stronger focus on industries such as finance, retail, and manufacturing, while Beijing has a strong presence in finance, technology, and pharmaceuticals.

Back to top

[Previous Multi-Document Agents (V1)](https://docs.llamaindex.ai/en/stable/examples/agent/multi_document_agents-v1/)[Next Build your own OpenAI Agent](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent/)

Hi, how can I help you?

🦙
