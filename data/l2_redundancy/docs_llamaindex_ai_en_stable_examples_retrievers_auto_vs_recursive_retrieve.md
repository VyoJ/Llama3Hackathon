Title: Comparing Methods for Structured Retrieval (Auto-Retrieval vs. Recursive Retrieval)

URL Source: https://docs.llamaindex.ai/en/stable/examples/retrievers/auto_vs_recursive_retriever/

Markdown Content:
Comparing Methods for Structured Retrieval (Auto-Retrieval vs. Recursive Retrieval) - LlamaIndex


In a naive RAG system, the set of input documents are then chunked, embedded, and dumped to a vector database collection. Retrieval would just fetch the top-k documents by embedding similarity.

This can fail if the set of documents is large - it can be hard to disambiguate raw chunks, and you're not guaranteed to filter for the set of documents that contain relevant context.

In this guide we explore **structured retrieval** - more advanced query algorithms that take advantage of structure within your documents for higher-precision retrieval. We compare the following two methods:

*   **Metadata Filters + Auto-Retrieval**: Tag each document with the right set of metadata. During query-time, use auto-retrieval to infer metadata filters along with passing through the query string for semantic search.
*   **Store Document Hierarchies (summaries -> raw chunks) + Recursive Retrieval**: Embed document summaries and map that to the set of raw chunks for each document. During query-time, do recursive retrieval to first fetch summaries before fetching documents.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai
%pip install llama\-index\-vector\-stores\-weaviate

%pip install llama-index-llms-openai %pip install llama-index-vector-stores-weaviate

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import nest\_asyncio

nest\_asyncio.apply()

import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

import logging
import sys
from llama\_index.core import SimpleDirectoryReader
from llama\_index.core import SummaryIndex

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys from llama\_index.core import SimpleDirectoryReader from llama\_index.core import SummaryIndex logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

In \[ \]:

Copied!

wiki\_titles \= \["Michael Jordan", "Elon Musk", "Richard Branson", "Rihanna"\]
wiki\_metadatas \= {
    "Michael Jordan": {
        "category": "Sports",
        "country": "United States",
    },
    "Elon Musk": {
        "category": "Business",
        "country": "United States",
    },
    "Richard Branson": {
        "category": "Business",
        "country": "UK",
    },
    "Rihanna": {
        "category": "Music",
        "country": "Barbados",
    },
}

wiki\_titles = \["Michael Jordan", "Elon Musk", "Richard Branson", "Rihanna"\] wiki\_metadatas = { "Michael Jordan": { "category": "Sports", "country": "United States", }, "Elon Musk": { "category": "Business", "country": "United States", }, "Richard Branson": { "category": "Business", "country": "UK", }, "Rihanna": { "category": "Music", "country": "Barbados", }, }

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
docs\_dict \= {}
for wiki\_title in wiki\_titles:
    doc \= SimpleDirectoryReader(
        input\_files\=\[f"data/{wiki\_title}.txt"\]
    ).load\_data()\[0\]

    doc.metadata.update(wiki\_metadatas\[wiki\_title\])
    docs\_dict\[wiki\_title\] \= doc

\# Load all wiki documents docs\_dict = {} for wiki\_title in wiki\_titles: doc = SimpleDirectoryReader( input\_files=\[f"data/{wiki\_title}.txt"\] ).load\_data()\[0\] doc.metadata.update(wiki\_metadatas\[wiki\_title\]) docs\_dict\[wiki\_title\] = doc

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI
from llama\_index.core.callbacks import LlamaDebugHandler, CallbackManager
from llama\_index.core.node\_parser import SentenceSplitter

llm \= OpenAI("gpt-4")
callback\_manager \= CallbackManager(\[LlamaDebugHandler()\])
splitter \= SentenceSplitter(chunk\_size\=256)

from llama\_index.llms.openai import OpenAI from llama\_index.core.callbacks import LlamaDebugHandler, CallbackManager from llama\_index.core.node\_parser import SentenceSplitter llm = OpenAI("gpt-4") callback\_manager = CallbackManager(\[LlamaDebugHandler()\]) splitter = SentenceSplitter(chunk\_size=256)

Metadata Filters + Auto-Retrieval[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/auto_vs_recursive_retriever/#metadata-filters-auto-retrieval)
-----------------------------------------------------------------------------------------------------------------------------------------------------------

In this approach, we tag each Document with metadata (category, country), and store in a Weaviate vector db.

During retrieval-time, we then perform "auto-retrieval" to infer the relevant set of metadata filters.

In \[ \]:

Copied!

\## Setup Weaviate
import weaviate

\# cloud
auth\_config \= weaviate.AuthApiKey(api\_key\="<api\_key>")
client \= weaviate.Client(
    "https://llama-index-test-v0oggsoz.weaviate.network",
    auth\_client\_secret\=auth\_config,
)

\## Setup Weaviate import weaviate # cloud auth\_config = weaviate.AuthApiKey(api\_key="") client = weaviate.Client( "https://llama-index-test-v0oggsoz.weaviate.network", auth\_client\_secret=auth\_config, )

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.vector\_stores.weaviate import WeaviateVectorStore
from IPython.display import Markdown, display

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.vector\_stores.weaviate import WeaviateVectorStore from IPython.display import Markdown, display

In \[ \]:

Copied!

\# drop items from collection first
client.schema.delete\_class("LlamaIndex")

\# drop items from collection first client.schema.delete\_class("LlamaIndex")

In \[ \]:

Copied!

from llama\_index.core import StorageContext

\# If you want to load the index later, be sure to give it a name!
vector\_store \= WeaviateVectorStore(
    weaviate\_client\=client, index\_name\="LlamaIndex"
)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

\# NOTE: you may also choose to define a index\_name manually.
\# index\_name = "test\_prefix"
\# vector\_store = WeaviateVectorStore(weaviate\_client=client, index\_name=index\_name)

from llama\_index.core import StorageContext # If you want to load the index later, be sure to give it a name! vector\_store = WeaviateVectorStore( weaviate\_client=client, index\_name="LlamaIndex" ) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) # NOTE: you may also choose to define a index\_name manually. # index\_name = "test\_prefix" # vector\_store = WeaviateVectorStore(weaviate\_client=client, index\_name=index\_name)

In \[ \]:

Copied!

\# validate that the schema was created
class\_schema \= client.schema.get("LlamaIndex")
display(class\_schema)

\# validate that the schema was created class\_schema = client.schema.get("LlamaIndex") display(class\_schema)

{'class': 'LlamaIndex',
 'description': 'Class for LlamaIndex',
 'invertedIndexConfig': {'bm25': {'b': 0.75, 'k1': 1.2},
  'cleanupIntervalSeconds': 60,
  'stopwords': {'additions': None, 'preset': 'en', 'removals': None}},
 'multiTenancyConfig': {'enabled': False},
 'properties': \[{'dataType': \['text'\],
   'description': 'Text property',
   'indexFilterable': True,
   'indexSearchable': True,
   'name': 'text',
   'tokenization': 'word'},
  {'dataType': \['text'\],
   'description': 'The ref\_doc\_id of the Node',
   'indexFilterable': True,
   'indexSearchable': True,
   'name': 'ref\_doc\_id',
   'tokenization': 'word'},
  {'dataType': \['text'\],
   'description': 'node\_info (in JSON)',
   'indexFilterable': True,
   'indexSearchable': True,
   'name': 'node\_info',
   'tokenization': 'word'},
  {'dataType': \['text'\],
   'description': 'The relationships of the node (in JSON)',
   'indexFilterable': True,
   'indexSearchable': True,
   'name': 'relationships',
   'tokenization': 'word'}\],
 'replicationConfig': {'factor': 1},
 'shardingConfig': {'virtualPerPhysical': 128,
  'desiredCount': 1,
  'actualCount': 1,
  'desiredVirtualCount': 128,
  'actualVirtualCount': 128,
  'key': '\_id',
  'strategy': 'hash',
  'function': 'murmur3'},
 'vectorIndexConfig': {'skip': False,
  'cleanupIntervalSeconds': 300,
  'maxConnections': 64,
  'efConstruction': 128,
  'ef': -1,
  'dynamicEfMin': 100,
  'dynamicEfMax': 500,
  'dynamicEfFactor': 8,
  'vectorCacheMaxObjects': 1000000000000,
  'flatSearchCutoff': 40000,
  'distance': 'cosine',
  'pq': {'enabled': False,
   'bitCompression': False,
   'segments': 0,
   'centroids': 256,
   'trainingLimit': 100000,
   'encoder': {'type': 'kmeans', 'distribution': 'log-normal'}}},
 'vectorIndexType': 'hnsw',
 'vectorizer': 'none'}

In \[ \]:

Copied!

index \= VectorStoreIndex(
    \[\],
    storage\_context\=storage\_context,
    transformations\=\[splitter\],
    callback\_manager\=callback\_manager,
)

\# add documents to index
for wiki\_title in wiki\_titles:
    index.insert(docs\_dict\[wiki\_title\])

index = VectorStoreIndex( \[\], storage\_context=storage\_context, transformations=\[splitter\], callback\_manager=callback\_manager, ) # add documents to index for wiki\_title in wiki\_titles: index.insert(docs\_dict\[wiki\_title\])

\*\*\*\*\*\*\*\*\*\*
Trace: index\_construction
\*\*\*\*\*\*\*\*\*\*
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
\*\*\*\*\*\*\*\*\*\*
Trace: insert
\*\*\*\*\*\*\*\*\*\*
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
\*\*\*\*\*\*\*\*\*\*
Trace: insert
\*\*\*\*\*\*\*\*\*\*
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
\*\*\*\*\*\*\*\*\*\*
Trace: insert
\*\*\*\*\*\*\*\*\*\*
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
\*\*\*\*\*\*\*\*\*\*
Trace: insert
\*\*\*\*\*\*\*\*\*\*

In \[ \]:

Copied!

from llama\_index.core.retrievers import VectorIndexAutoRetriever
from llama\_index.core.vector\_stores.types import MetadataInfo, VectorStoreInfo

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
    \],
)
retriever \= VectorIndexAutoRetriever(
    index,
    vector\_store\_info\=vector\_store\_info,
    llm\=llm,
    callback\_manager\=callback\_manager,
    max\_top\_k\=10000,
)

from llama\_index.core.retrievers import VectorIndexAutoRetriever from llama\_index.core.vector\_stores.types import MetadataInfo, VectorStoreInfo vector\_store\_info = VectorStoreInfo( content\_info="brief biography of celebrities", metadata\_info=\[ MetadataInfo( name="category", type="str", description=( "Category of the celebrity, one of \[Sports, Entertainment," " Business, Music\]" ), ), MetadataInfo( name="country", type="str", description=( "Country of the celebrity, one of \[United States, Barbados," " Portugal\]" ), ), \], ) retriever = VectorIndexAutoRetriever( index, vector\_store\_info=vector\_store\_info, llm=llm, callback\_manager=callback\_manager, max\_top\_k=10000, )

In \[ \]:

Copied!

\# NOTE: the "set top-k to 10000" is a hack to return all data.
\# Right now auto-retrieval will always return a fixed top-k, there's a TODO to allow it to be None
\# to fetch all data.
\# So it's theoretically possible to have the LLM infer a None top-k value.
nodes \= retriever.retrieve(
    "Tell me about a celebrity from the United States, set top k to 10000"
)

\# NOTE: the "set top-k to 10000" is a hack to return all data. # Right now auto-retrieval will always return a fixed top-k, there's a TODO to allow it to be None # to fetch all data. # So it's theoretically possible to have the LLM infer a None top-k value. nodes = retriever.retrieve( "Tell me about a celebrity from the United States, set top k to 10000" )

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
INFO:llama\_index.indices.vector\_store.retrievers.auto\_retriever.auto\_retriever:Using query str: Tell me about a celebrity
Using query str: Tell me about a celebrity
INFO:llama\_index.indices.vector\_store.retrievers.auto\_retriever.auto\_retriever:Using filters: \[('country', '', 'United States')\]
INFO:llama\_index.indices.vector\_store.retrievers.auto\_retriever.auto\_retriever:Using top\_k: 2
Using top\_k: 2
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
\*\*\*\*\*\*\*\*\*\*
Trace: query
    |\_retrieve ->  4.232108 seconds
\*\*\*\*\*\*\*\*\*\*

In \[ \]:

Copied!

print(f"Number of nodes: {len(nodes)}")
for node in nodes\[:10\]:
    print(node.node.get\_content())

print(f"Number of nodes: {len(nodes)}") for node in nodes\[:10\]: print(node.node.get\_content())

Number of nodes: 2
In December 2023, Judge Laurel Beeler ruled that Musk must testify again for the SEC.  




Though his ventures were influential within their own industries in the 2000s, Musk only became a public figure in the early 2010s. He has been described as an eccentric who makes spontaneous and controversial statements, contrary to other billionaires who prefer reclusiveness to protect their businesses. Vance described people's opinions of Musk as polarized due to his "part philosopher, part troll" role on Twitter.Musk was a partial inspiration for the characterization of Tony Stark in the Marvel film Iron Man (2008). Musk also had a cameo appearance in the film's 2010 sequel, Iron Man 2. Musk has made cameos and appearances in other films such as Machete Kills (2013), Why Him? (2016), and Men in Black: International (2019). Television series in which he has appeared include The Simpsons ("The Musk Who Fell to Earth", 2015), The Big Bang Theory ("The Platonic Permutation", 2015), South Park ("Members Only", 2016), Young Sheldon ("A Patch, a Modem, and a Zantac®", 2017), Rick and Morty ("One Crew over the Crewcoo's Morty", 2019), and Saturday Night Live (2021).
Musk also had a cameo appearance in the film's 2010 sequel, Iron Man 2. Musk has made cameos and appearances in other films such as Machete Kills (2013), Why Him? (2016), and Men in Black: International (2019). Television series in which he has appeared include The Simpsons ("The Musk Who Fell to Earth", 2015), The Big Bang Theory ("The Platonic Permutation", 2015), South Park ("Members Only", 2016), Young Sheldon ("A Patch, a Modem, and a Zantac®", 2017), Rick and Morty ("One Crew over the Crewcoo's Morty", 2019), and Saturday Night Live (2021). He contributed interviews to the documentaries Racing Extinction (2015) and the Werner Herzog-directed Lo and Behold (2016).Musk was elected a Fellow of the Royal Society (FRS) in 2018. In 2015, he received an honorary doctorate in engineering and technology from Yale University and IEEE Honorary Membership.

In \[ \]:

Copied!

nodes \= retriever.retrieve(
    "Tell me about the childhood of a popular sports celebrity in the United"
    " States"
)
for node in nodes:
    print(node.node.get\_content())

nodes = retriever.retrieve( "Tell me about the childhood of a popular sports celebrity in the United" " States" ) for node in nodes: print(node.node.get\_content())

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
INFO:llama\_index.indices.vector\_store.retrievers.auto\_retriever.auto\_retriever:Using query str: childhood of a popular sports celebrity
Using query str: childhood of a popular sports celebrity
INFO:llama\_index.indices.vector\_store.retrievers.auto\_retriever.auto\_retriever:Using filters: \[('category', '', 'United States')\]
Using filters: \[('category', '', 'United States')\]
INFO:llama\_index.indices.vector\_store.retrievers.auto\_retriever.auto\_retriever:Using top\_k: 2
Using top\_k: 2
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
\*\*\*\*\*\*\*\*\*\*
Trace: query
    |\_retrieve ->  3.546065 seconds
\*\*\*\*\*\*\*\*\*\*
It was announced on November 30, 2013, that the two were expecting their first child together. On February 11, 2014, Prieto gave birth to identical twin daughters named Victoria and Ysabel. In 2019, Jordan became a grandfather when his daughter Jasmine gave birth to a son, whose father is professional basketball player Rakeem Christmas.






Jordan is one of the most marketed sports figures in history. He has been a major spokesman for such brands as Nike, Coca-Cola, Chevrolet, Gatorade, McDonald's, Ball Park Franks, Rayovac, Wheaties, Hanes, and MCI. Jordan has had a long relationship with Gatorade, appearing in over 20 commercials for the company since 1991, including the "Be Like Mike" commercials in which a song was sung by children wishing to be like Jordan.Nike created a signature shoe for Jordan, called the Air Jordan, in 1984. One of Jordan's more popular commercials for the shoe involved Spike Lee playing the part of Mars Blackmon.
In 2019, Jordan became a grandfather when his daughter Jasmine gave birth to a son, whose father is professional basketball player Rakeem Christmas.






Jordan is one of the most marketed sports figures in history. He has been a major spokesman for such brands as Nike, Coca-Cola, Chevrolet, Gatorade, McDonald's, Ball Park Franks, Rayovac, Wheaties, Hanes, and MCI. Jordan has had a long relationship with Gatorade, appearing in over 20 commercials for the company since 1991, including the "Be Like Mike" commercials in which a song was sung by children wishing to be like Jordan.Nike created a signature shoe for Jordan, called the Air Jordan, in 1984. One of Jordan's more popular commercials for the shoe involved Spike Lee playing the part of Mars Blackmon. In the commercials, Lee, as Blackmon, attempted to find the source of Jordan's abilities and became convinced that "it's gotta be the shoes".

In \[ \]:

Copied!

nodes \= retriever.retrieve(
    "Tell me about the college life of a billionaire who started at company at"
    " the age of 16"
)
for node in nodes:
    print(node.node.get\_content())

nodes = retriever.retrieve( "Tell me about the college life of a billionaire who started at company at" " the age of 16" ) for node in nodes: print(node.node.get\_content())

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
INFO:llama\_index.indices.vector\_store.retrievers.auto\_retriever.auto\_retriever:Using query str: college life of a billionaire who started at company at the age of 16
Using query str: college life of a billionaire who started at company at the age of 16
INFO:llama\_index.indices.vector\_store.retrievers.auto\_retriever.auto\_retriever:Using filters: \[\]
Using filters: \[\]
INFO:llama\_index.indices.vector\_store.retrievers.auto\_retriever.auto\_retriever:Using top\_k: 2
Using top\_k: 2
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
\*\*\*\*\*\*\*\*\*\*
Trace: query
    |\_retrieve ->  2.60008 seconds
\*\*\*\*\*\*\*\*\*\*
After his parents divorced in 1980, Musk chose to live primarily with his father. Musk later regretted his decision and became estranged from his father. He has a paternal half-sister and a half-brother.In one incident, after having called a boy whose father had committed suicide "stupid", Musk was severely beaten and thrown down concrete steps. His father derided Elon for his behavior and showed no sympathy for him despite his injuries. He was also an enthusiastic reader of books, later attributing his success in part to having read Benjamin Franklin: An American Life, Lord of the Flies, the Foundation series, and The Hitchhiker's Guide to the Galaxy. At age ten, he developed an interest in computing and video games, teaching himself how to program from the VIC-20 user manual. At age twelve, Musk sold his BASIC-based game Blastar to PC and Office Technology magazine for approximately $500.



Musk attended Waterkloof House Preparatory School, Bryanston High School, and then Pretoria Boys High School, where he graduated.
He has a paternal half-sister and a half-brother.In one incident, after having called a boy whose father had committed suicide "stupid", Musk was severely beaten and thrown down concrete steps. His father derided Elon for his behavior and showed no sympathy for him despite his injuries. He was also an enthusiastic reader of books, later attributing his success in part to having read Benjamin Franklin: An American Life, Lord of the Flies, the Foundation series, and The Hitchhiker's Guide to the Galaxy. At age ten, he developed an interest in computing and video games, teaching himself how to program from the VIC-20 user manual. At age twelve, Musk sold his BASIC-based game Blastar to PC and Office Technology magazine for approximately $500.



Musk attended Waterkloof House Preparatory School, Bryanston High School, and then Pretoria Boys High School, where he graduated. Musk was a good but not exceptional student, earning a 61 in Afrikaans and a B on his senior math certification.

In \[ \]:

Copied!

nodes \= retriever.retrieve("Tell me about the childhood of a UK billionaire")
for node in nodes:
    print(node.node.get\_content())

nodes = retriever.retrieve("Tell me about the childhood of a UK billionaire") for node in nodes: print(node.node.get\_content())

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
INFO:llama\_index.indices.vector\_store.retrievers.auto\_retriever.auto\_retriever:Using query str: childhood of a UK billionaire
Using query str: childhood of a UK billionaire
INFO:llama\_index.indices.vector\_store.retrievers.auto\_retriever.auto\_retriever:Using filters: \[('category', '', 'United Kingdom')\]
Using filters: \[('category', '', 'United Kingdom')\]
INFO:llama\_index.indices.vector\_store.retrievers.auto\_retriever.auto\_retriever:Using top\_k: 2
Using top\_k: 2
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
\*\*\*\*\*\*\*\*\*\*
Trace: query
    |\_retrieve ->  3.565899 seconds
\*\*\*\*\*\*\*\*\*\*

Build Recursive Retriever over Document Summaries[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/auto_vs_recursive_retriever/#build-recursive-retriever-over-document-summaries)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core.schema import IndexNode

from llama\_index.core.schema import IndexNode

In \[ \]:

Copied!

\# define top-level nodes and vector retrievers
nodes \= \[\]
vector\_query\_engines \= {}
vector\_retrievers \= {}

for wiki\_title in wiki\_titles:
    \# build vector index
    vector\_index \= VectorStoreIndex.from\_documents(
        \[docs\_dict\[wiki\_title\]\],
        transformations\=\[splitter\],
        callback\_manager\=callback\_manager,
    )
    \# define query engines
    vector\_query\_engine \= vector\_index.as\_query\_engine(llm\=llm)
    vector\_query\_engines\[wiki\_title\] \= vector\_query\_engine
    vector\_retrievers\[wiki\_title\] \= vector\_index.as\_retriever()

    \# save summaries
    out\_path \= Path("summaries") / f"{wiki\_title}.txt"
    if not out\_path.exists():
        \# use LLM-generated summary
        summary\_index \= SummaryIndex.from\_documents(
            \[docs\_dict\[wiki\_title\]\], callback\_manager\=callback\_manager
        )

        summarizer \= summary\_index.as\_query\_engine(
            response\_mode\="tree\_summarize", llm\=llm
        )
        response \= await summarizer.aquery(
            f"Give me a summary of {wiki\_title}"
        )

        wiki\_summary \= response.response
        Path("summaries").mkdir(exist\_ok\=True)
        with open(out\_path, "w") as fp:
            fp.write(wiki\_summary)
    else:
        with open(out\_path, "r") as fp:
            wiki\_summary \= fp.read()

    print(f"\*\*Summary for {wiki\_title}: {wiki\_summary}")
    node \= IndexNode(text\=wiki\_summary, index\_id\=wiki\_title)
    nodes.append(node)

\# define top-level nodes and vector retrievers nodes = \[\] vector\_query\_engines = {} vector\_retrievers = {} for wiki\_title in wiki\_titles: # build vector index vector\_index = VectorStoreIndex.from\_documents( \[docs\_dict\[wiki\_title\]\], transformations=\[splitter\], callback\_manager=callback\_manager, ) # define query engines vector\_query\_engine = vector\_index.as\_query\_engine(llm=llm) vector\_query\_engines\[wiki\_title\] = vector\_query\_engine vector\_retrievers\[wiki\_title\] = vector\_index.as\_retriever() # save summaries out\_path = Path("summaries") / f"{wiki\_title}.txt" if not out\_path.exists(): # use LLM-generated summary summary\_index = SummaryIndex.from\_documents( \[docs\_dict\[wiki\_title\]\], callback\_manager=callback\_manager ) summarizer = summary\_index.as\_query\_engine( response\_mode="tree\_summarize", llm=llm ) response = await summarizer.aquery( f"Give me a summary of {wiki\_title}" ) wiki\_summary = response.response Path("summaries").mkdir(exist\_ok=True) with open(out\_path, "w") as fp: fp.write(wiki\_summary) else: with open(out\_path, "r") as fp: wiki\_summary = fp.read() print(f"\*\*Summary for {wiki\_title}: {wiki\_summary}") node = IndexNode(text=wiki\_summary, index\_id=wiki\_title) nodes.append(node)

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
\*\*\*\*\*\*\*\*\*\*
Trace: index\_construction
\*\*\*\*\*\*\*\*\*\*
\*\*Summary for Michael Jordan: Michael Jordan, often referred to as MJ, is a retired professional basketball player from the United States who is widely considered one of the greatest players in the history of the sport. He played 15 seasons in the NBA, primarily with the Chicago Bulls, and won six NBA championships. His individual accolades include six NBA Finals MVP awards, ten NBA scoring titles, five NBA MVP awards, and fourteen NBA All-Star Game selections. He also holds the NBA records for career regular season scoring average and career playoff scoring average. Jordan briefly retired to play Minor League Baseball, but returned to lead the Bulls to three more championships. He was twice inducted into the Naismith Memorial Basketball Hall of Fame. 

After retiring, Jordan became a successful businessman, part-owner and head of basketball operations for the Charlotte Hornets, and owner of 23XI Racing in the NASCAR Cup Series. He has also made significant contributions to charitable causes, donating millions to organizations such as the Make-A-Wish Foundation and Habitat for Humanity. In the entertainment industry, he has appeared in productions like "Space Jam" and "The Last Dance", and has authored several books about his life and career. His influence extends beyond sports, making him a significant cultural figure.
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
\*\*\*\*\*\*\*\*\*\*
Trace: index\_construction
\*\*\*\*\*\*\*\*\*\*
\*\*Summary for Elon Musk: Elon Musk is a globally recognized business magnate and investor, who has founded and led numerous high-profile technology companies. He is the founder, CEO, and chief technology officer of SpaceX, an aerospace manufacturer and space transportation company, and the CEO and product architect of Tesla, Inc., a company specializing in electric vehicles and clean energy. Musk also owns and chairs X Corp, and founded the Boring Company, a tunnel construction and infrastructure company. He co-founded Neuralink, a neurotechnology company, and OpenAI, a nonprofit artificial intelligence research company. 

In 2022, Musk acquired Twitter and merged it with X Corp, and also founded xAI, an AI company. Despite his success, he has faced criticism for his controversial statements and management style. Musk was born in South Africa, moved to Canada at 18, and later to the United States to attend Stanford University, but dropped out to start his entrepreneurial journey. He co-founded Zip2 and X.com (later PayPal), which was sold to eBay in 2002. 

Musk envisions a future that includes Mars colonization and the development of a high-speed transportation system known as the Hyperloop. As of August 2023, he is the wealthiest person in the world, with a net worth of over $200 billion. Despite various controversies, Musk has made significant contributions to the tech industry. He has been married multiple times, has several children, and is known for his active presence on social media, particularly Twitter.
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
\*\*\*\*\*\*\*\*\*\*
Trace: index\_construction
\*\*\*\*\*\*\*\*\*\*
\*\*Summary for Richard Branson: Richard Branson, born on 18 July 1950, is a British business magnate, commercial astronaut, and philanthropist. He founded the Virgin Group in the 1970s, which now controls over 400 companies in various fields such as aviation, music, and space travel. His first business venture was a magazine called Student, and he later established a mail-order record business and a chain of record stores known as Virgin Records. The Virgin brand expanded rapidly during the 1980s with the start of Virgin Atlantic airline and the expansion of the Virgin Records music label. In 1997, he founded the Virgin Rail Group, and in 2004, he founded Virgin Galactic. Branson was knighted in 2000 for his services to entrepreneurship. He has a net worth of US$3 billion as of June 2023. Branson has also been involved in numerous philanthropic activities and has launched initiatives like Virgin Startup. Despite his success, he has faced criticism and legal issues, including a brief jail term for tax evasion in 1971. He is married to Joan Templeman, with whom he has two children.
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
\*\*\*\*\*\*\*\*\*\*
Trace: index\_construction
\*\*\*\*\*\*\*\*\*\*
\*\*Summary for Rihanna: Rihanna, whose real name is Robyn Rihanna Fenty, is a renowned Barbadian singer, songwriter, actress, and businesswoman. She rose to fame after signing with Def Jam in 2005 and releasing her first two albums, "Music of the Sun" and "A Girl Like Me". Her third album, "Good Girl Gone Bad", solidified her status as a major music icon. Some of her other successful albums include "Rated R", "Loud", "Talk That Talk", and "Unapologetic", which was her first to reach number one on the Billboard 200. 

Rihanna has sold over 250 million records worldwide, making her one of the best-selling music artists of all time. She has received numerous awards, including nine Grammy Awards, 12 Billboard Music Awards, and 13 American Music Awards. She also holds six Guinness World Records. 

In addition to her music career, Rihanna has ventured into business, founding the cosmetics brand Fenty Beauty and the fashion house Fenty under LVMH. She has also acted in several films, including "Battleship", "Home", "Valerian and the City of a Thousand Planets", and "Ocean's 8". 

Rihanna is also known for her philanthropic work, particularly through her Believe Foundation and the Clara Lionel Foundation. As of 2023, she is the wealthiest female musician, with an estimated net worth of $1.4 billion.

In \[ \]:

Copied!

\# define top-level retriever
top\_vector\_index \= VectorStoreIndex(
    nodes, transformations\=\[splitter\], callback\_manager\=callback\_manager
)
top\_vector\_retriever \= top\_vector\_index.as\_retriever(similarity\_top\_k\=1)

\# define top-level retriever top\_vector\_index = VectorStoreIndex( nodes, transformations=\[splitter\], callback\_manager=callback\_manager ) top\_vector\_retriever = top\_vector\_index.as\_retriever(similarity\_top\_k=1)

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
\*\*\*\*\*\*\*\*\*\*
Trace: index\_construction
\*\*\*\*\*\*\*\*\*\*

In \[ \]:

Copied!

\# define recursive retriever
from llama\_index.core.retrievers import RecursiveRetriever
from llama\_index.core.query\_engine import RetrieverQueryEngine
from llama\_index.core import get\_response\_synthesizer

\# define recursive retriever from llama\_index.core.retrievers import RecursiveRetriever from llama\_index.core.query\_engine import RetrieverQueryEngine from llama\_index.core import get\_response\_synthesizer

In \[ \]:

Copied!

\# note: can pass \`agents\` dict as \`query\_engine\_dict\` since every agent can be used as a query engine
recursive\_retriever \= RecursiveRetriever(
    "vector",
    retriever\_dict\={"vector": top\_vector\_retriever, \*\*vector\_retrievers},
    \# query\_engine\_dict=vector\_query\_engines,
    verbose\=True,
)

\# note: can pass \`agents\` dict as \`query\_engine\_dict\` since every agent can be used as a query engine recursive\_retriever = RecursiveRetriever( "vector", retriever\_dict={"vector": top\_vector\_retriever, \*\*vector\_retrievers}, # query\_engine\_dict=vector\_query\_engines, verbose=True, )

In \[ \]:

Copied!

\# run recursive retriever
nodes \= recursive\_retriever.retrieve(
    "Tell me about a celebrity from the United States"
)
for node in nodes:
    print(node.node.get\_content())

\# run recursive retriever nodes = recursive\_retriever.retrieve( "Tell me about a celebrity from the United States" ) for node in nodes: print(node.node.get\_content())

Retrieving with query id None: Tell me about a celebrity from the United States
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
Retrieved node with id, entering: Michael Jordan
Retrieving with query id Michael Jordan: Tell me about a celebrity from the United States
Retrieving text node: In 1999, an ESPN survey of journalists, athletes and other sports figures ranked Jordan the greatest North American athlete of the 20th century. Jordan placed second to Babe Ruth in the Associated Press' December 1999 list of 20th century athletes. In addition, the Associated Press voted him the greatest basketball player of the 20th century. Jordan has also appeared on the front cover of Sports Illustrated a record 50 times. In the September 1996 issue of Sport, which was the publication's 50th-anniversary issue, Jordan was named the greatest athlete of the past 50 years.Jordan's athletic leaping ability, highlighted in his back-to-back Slam Dunk Contest championships in 1987 and 1988, is credited by many people with having influenced a generation of young players. Several NBA players, including James and Dwyane Wade, have stated that they considered Jordan their role model while they were growing up. In addition, commentators have dubbed a number of next-generation players "the next Michael Jordan" upon their entry to the NBA, including Penny Hardaway, Grant Hill, Allen Iverson, Bryant, Vince Carter, James, and Wade.
Retrieving text node: In 1999, he was named the 20th century's greatest North American athlete by ESPN and was second to Babe Ruth on the Associated Press' list of athletes of the century. Jordan was twice inducted into the Naismith Memorial Basketball Hall of Fame, once in 2009 for his individual career, and again in 2010 as part of the 1992 United States men's Olympic basketball team ("The Dream Team"). He became a member of the United States Olympic Hall of Fame in 2009, a member of the North Carolina Sports Hall of Fame in 2010, and an individual member of the FIBA Hall of Fame in 2015 and a "Dream Team" member in 2017. Jordan was named to the NBA 50th Anniversary Team in 1996 and to the NBA 75th Anniversary Team in 2021.One of the most effectively marketed athletes of his generation, Jordan made many product endorsements. He fueled the success of Nike's Air Jordan sneakers, which were introduced in 1984 and remain popular.
In 1999, an ESPN survey of journalists, athletes and other sports figures ranked Jordan the greatest North American athlete of the 20th century. Jordan placed second to Babe Ruth in the Associated Press' December 1999 list of 20th century athletes. In addition, the Associated Press voted him the greatest basketball player of the 20th century. Jordan has also appeared on the front cover of Sports Illustrated a record 50 times. In the September 1996 issue of Sport, which was the publication's 50th-anniversary issue, Jordan was named the greatest athlete of the past 50 years.Jordan's athletic leaping ability, highlighted in his back-to-back Slam Dunk Contest championships in 1987 and 1988, is credited by many people with having influenced a generation of young players. Several NBA players, including James and Dwyane Wade, have stated that they considered Jordan their role model while they were growing up. In addition, commentators have dubbed a number of next-generation players "the next Michael Jordan" upon their entry to the NBA, including Penny Hardaway, Grant Hill, Allen Iverson, Bryant, Vince Carter, James, and Wade.
In 1999, he was named the 20th century's greatest North American athlete by ESPN and was second to Babe Ruth on the Associated Press' list of athletes of the century. Jordan was twice inducted into the Naismith Memorial Basketball Hall of Fame, once in 2009 for his individual career, and again in 2010 as part of the 1992 United States men's Olympic basketball team ("The Dream Team"). He became a member of the United States Olympic Hall of Fame in 2009, a member of the North Carolina Sports Hall of Fame in 2010, and an individual member of the FIBA Hall of Fame in 2015 and a "Dream Team" member in 2017. Jordan was named to the NBA 50th Anniversary Team in 1996 and to the NBA 75th Anniversary Team in 2021.One of the most effectively marketed athletes of his generation, Jordan made many product endorsements. He fueled the success of Nike's Air Jordan sneakers, which were introduced in 1984 and remain popular.

In \[ \]:

Copied!

nodes \= recursive\_retriever.retrieve(
    "Tell me about the childhood of a billionaire who started at company at"
    " the age of 16"
)
for node in nodes:
    print(node.node.get\_content())

nodes = recursive\_retriever.retrieve( "Tell me about the childhood of a billionaire who started at company at" " the age of 16" ) for node in nodes: print(node.node.get\_content())

Retrieving with query id None: Tell me about the childhood of a billionaire who started at company at the age of 16
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
Retrieved node with id, entering: Richard Branson
Retrieving with query id Richard Branson: Tell me about the childhood of a billionaire who started at company at the age of 16
Retrieving text node: He attended Stowe School, a private school in Buckinghamshire until the age of sixteen.Branson has dyslexia, and had poor academic performance; on his last day at school, his headmaster, Robert Drayson, told him he would either end up in prison or become a millionaire. 
Branson has also talked openly about having ADHD.
Branson's parents were supportive of his endeavours from an early age. His mother was an entrepreneur; one of her most successful ventures was building and selling wooden tissue boxes and wastepaper bins. In London, he started off squatting from 1967 to 1968.Branson is an atheist. He said in a 2011 interview with CNN's Piers Morgan that he believes in evolution and the importance of humanitarian efforts but not in the existence of God. "I would love to believe," he said. "It's very comforting to believe".



After failed attempts to grow and sell both Christmas trees and budgerigars, Branson launched a magazine named Student in 1966 with Nik Powell.
Retrieving text node: Later, he stated that one of his great-great-great-grandmothers was an Indian named Ariya.Branson was educated at Scaitcliffe School, a prep school in Surrey, before briefly attending Cliff View House School in Sussex. He attended Stowe School, a private school in Buckinghamshire until the age of sixteen.Branson has dyslexia, and had poor academic performance; on his last day at school, his headmaster, Robert Drayson, told him he would either end up in prison or become a millionaire. 
Branson has also talked openly about having ADHD.
Branson's parents were supportive of his endeavours from an early age. His mother was an entrepreneur; one of her most successful ventures was building and selling wooden tissue boxes and wastepaper bins. In London, he started off squatting from 1967 to 1968.Branson is an atheist. He said in a 2011 interview with CNN's Piers Morgan that he believes in evolution and the importance of humanitarian efforts but not in the existence of God. "I would love to believe," he said.
He attended Stowe School, a private school in Buckinghamshire until the age of sixteen.Branson has dyslexia, and had poor academic performance; on his last day at school, his headmaster, Robert Drayson, told him he would either end up in prison or become a millionaire. 
Branson has also talked openly about having ADHD.
Branson's parents were supportive of his endeavours from an early age. His mother was an entrepreneur; one of her most successful ventures was building and selling wooden tissue boxes and wastepaper bins. In London, he started off squatting from 1967 to 1968.Branson is an atheist. He said in a 2011 interview with CNN's Piers Morgan that he believes in evolution and the importance of humanitarian efforts but not in the existence of God. "I would love to believe," he said. "It's very comforting to believe".



After failed attempts to grow and sell both Christmas trees and budgerigars, Branson launched a magazine named Student in 1966 with Nik Powell.
Later, he stated that one of his great-great-great-grandmothers was an Indian named Ariya.Branson was educated at Scaitcliffe School, a prep school in Surrey, before briefly attending Cliff View House School in Sussex. He attended Stowe School, a private school in Buckinghamshire until the age of sixteen.Branson has dyslexia, and had poor academic performance; on his last day at school, his headmaster, Robert Drayson, told him he would either end up in prison or become a millionaire. 
Branson has also talked openly about having ADHD.
Branson's parents were supportive of his endeavours from an early age. His mother was an entrepreneur; one of her most successful ventures was building and selling wooden tissue boxes and wastepaper bins. In London, he started off squatting from 1967 to 1968.Branson is an atheist. He said in a 2011 interview with CNN's Piers Morgan that he believes in evolution and the importance of humanitarian efforts but not in the existence of God. "I would love to believe," he said.

Back to top

[Previous Auto Merging Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/auto_merging_retriever/)[Next Bedrock (Knowledge Bases)](https://docs.llamaindex.ai/en/stable/examples/retrievers/bedrock_retriever/)
