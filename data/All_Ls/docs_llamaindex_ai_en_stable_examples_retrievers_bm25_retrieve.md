Title: BM25 Retriever - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/retrievers/bm25_retriever/

Markdown Content:
BM25 Retriever - LlamaIndex


In this guide, we define a bm25 retriever that search documents using the bm25 method. BM25 (Best Matching 25) is a ranking function that extends TF-IDF by considering term frequency saturation and document length. BM25 effectively ranks documents based on query term occurrence and rarity across the corpus.

This notebook is very similar to the RouterQueryEngine notebook.

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/bm25_retriever/#setup)
----------------------------------------------------------------------------------------

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index
%pip install llama\-index\-retrievers\-bm25

%pip install llama-index %pip install llama-index-retrievers-bm25

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-proj-..."

from llama\_index.core import Settings
from llama\_index.llms.openai import OpenAI
from llama\_index.embeddings.openai import OpenAIEmbedding

Settings.llm \= OpenAI(model\="gpt-3.5-turbo")
Settings.embed\_model \= OpenAIEmbedding(model\_name\="text-embedding-3-small")

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-proj-..." from llama\_index.core import Settings from llama\_index.llms.openai import OpenAI from llama\_index.embeddings.openai import OpenAIEmbedding Settings.llm = OpenAI(model="gpt-3.5-turbo") Settings.embed\_model = OpenAIEmbedding(model\_name="text-embedding-3-small")

Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/bm25_retriever/#download-data)
--------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

\--2024-07-05 10:10:09--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.111.133, 185.199.109.133, 185.199.108.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.111.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 75042 (73K) \[text/plain\]
Saving to: ‘data/paul\_graham/paul\_graham\_essay.txt’

data/paul\_graham/pa 100%\[>\]  73.28K  --.-KB/s    in 0.05s   

2024-07-05 10:10:09 (1.36 MB/s) - ‘data/paul\_graham/paul\_graham\_essay.txt’ saved \[75042/75042\]

Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/bm25_retriever/#load-data)
------------------------------------------------------------------------------------------------

We first show how to convert a Document into a set of Nodes, and insert into a DocumentStore.

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham").load\_data()

from llama\_index.core import SimpleDirectoryReader # load documents documents = SimpleDirectoryReader("./data/paul\_graham").load\_data()

In \[ \]:

Copied!

from llama\_index.core.node\_parser import SentenceSplitter

\# initialize node parser
splitter \= SentenceSplitter(chunk\_size\=512)

nodes \= splitter.get\_nodes\_from\_documents(documents)

from llama\_index.core.node\_parser import SentenceSplitter # initialize node parser splitter = SentenceSplitter(chunk\_size=512) nodes = splitter.get\_nodes\_from\_documents(documents)

BM25 Retriever + Disk Persistance[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/bm25_retriever/#bm25-retriever-disk-persistance)
----------------------------------------------------------------------------------------------------------------------------------------------

One option is to create the `BM25Retriever` directly from nodes, and save to and from disk.

In \[ \]:

Copied!

from llama\_index.retrievers.bm25 import BM25Retriever
import Stemmer

\# We can pass in the index, doctore, or list of nodes to create the retriever
bm25\_retriever \= BM25Retriever.from\_defaults(
    nodes\=nodes,
    similarity\_top\_k\=2,
    \# Optional: We can pass in the stemmer and set the language for stopwords
    \# This is important for removing stopwords and stemming the query + text
    \# The default is english for both
    stemmer\=Stemmer.Stemmer("english"),
    language\="english",
)

from llama\_index.retrievers.bm25 import BM25Retriever import Stemmer # We can pass in the index, doctore, or list of nodes to create the retriever bm25\_retriever = BM25Retriever.from\_defaults( nodes=nodes, similarity\_top\_k=2, # Optional: We can pass in the stemmer and set the language for stopwords # This is important for removing stopwords and stemming the query + text # The default is english for both stemmer=Stemmer.Stemmer("english"), language="english", )

BM25S Count Tokens:   0%|          | 0/61 \[00:00<?, ?it/s\]

BM25S Compute Scores:   0%|          | 0/61 \[00:00<?, ?it/s\]

In \[ \]:

Copied!

bm25\_retriever.persist("./bm25\_retriever")

loaded\_bm25\_retriever \= BM25Retriever.from\_persist\_dir("./bm25\_retriever")

bm25\_retriever.persist("./bm25\_retriever") loaded\_bm25\_retriever = BM25Retriever.from\_persist\_dir("./bm25\_retriever")

Finding newlines for mmindex:   0%|          | 0.00/292k \[00:00<?, ?B/s\]

BM25 Retriever + Docstore Persistance[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/bm25_retriever/#bm25-retriever-docstore-persistance)
------------------------------------------------------------------------------------------------------------------------------------------------------

Here, we cover using a `BM25Retriever` with a docstore to hold your nodes. The advantage here is that the docstore can be remote (mongodb, redis, etc.)

In \[ \]:

Copied!

\# initialize a docstore to store nodes
\# also available are mongodb, redis, postgres, etc for docstores
from llama\_index.core.storage.docstore import SimpleDocumentStore

docstore \= SimpleDocumentStore()
docstore.add\_documents(nodes)

\# initialize a docstore to store nodes # also available are mongodb, redis, postgres, etc for docstores from llama\_index.core.storage.docstore import SimpleDocumentStore docstore = SimpleDocumentStore() docstore.add\_documents(nodes)

In \[ \]:

Copied!

from llama\_index.retrievers.bm25 import BM25Retriever
import Stemmer

\# We can pass in the index, doctore, or list of nodes to create the retriever
bm25\_retriever \= BM25Retriever.from\_defaults(
    docstore\=docstore,
    similarity\_top\_k\=2,
    \# Optional: We can pass in the stemmer and set the language for stopwords
    \# This is important for removing stopwords and stemming the query + text
    \# The default is english for both
    stemmer\=Stemmer.Stemmer("english"),
    language\="english",
)

from llama\_index.retrievers.bm25 import BM25Retriever import Stemmer # We can pass in the index, doctore, or list of nodes to create the retriever bm25\_retriever = BM25Retriever.from\_defaults( docstore=docstore, similarity\_top\_k=2, # Optional: We can pass in the stemmer and set the language for stopwords # This is important for removing stopwords and stemming the query + text # The default is english for both stemmer=Stemmer.Stemmer("english"), language="english", )

BM25S Count Tokens:   0%|          | 0/61 \[00:00<?, ?it/s\]

BM25S Compute Scores:   0%|          | 0/61 \[00:00<?, ?it/s\]

In \[ \]:

Copied!

from llama\_index.core.response.notebook\_utils import display\_source\_node

\# will retrieve context from specific companies
retrieved\_nodes \= bm25\_retriever.retrieve(
    "What happened at Viaweb and Interleaf?"
)
for node in retrieved\_nodes:
    display\_source\_node(node, source\_length\=5000)

from llama\_index.core.response.notebook\_utils import display\_source\_node # will retrieve context from specific companies retrieved\_nodes = bm25\_retriever.retrieve( "What happened at Viaweb and Interleaf?" ) for node in retrieved\_nodes: display\_source\_node(node, source\_length=5000)

**Node ID:** a1236ec0-7d41-4b52-950f-27199a1e28de  
**Similarity:** 1.8383275270462036  
**Text:** I saw Florence at street level in every possible condition, from empty dark winter evenings to sweltering summer days when the streets were packed with tourists.

\[4\] You can of course paint people like still lives if you want to, and they're willing. That sort of portrait is arguably the apex of still life painting, though the long sitting does tend to produce pained expressions in the sitters.

\[5\] Interleaf was one of many companies that had smart people and built impressive technology, and yet got crushed by Moore's Law. In the 1990s the exponential growth in the power of commodity (i.e. Intel) processors rolled up high-end, special-purpose hardware and software companies like a bulldozer.

\[6\] The signature style seekers at RISD weren't specifically mercenary. In the art world, money and coolness are tightly coupled. Anything expensive comes to be seen as cool, and anything seen as cool will soon become equally expensive.

\[7\] Technically the apartment wasn't rent-controlled but rent-stabilized, but this is a refinement only New Yorkers would know or care about. The point is that it was really cheap, less than half market price.

\[8\] Most software you can launch as soon as it's done. But when the software is an online store builder and you're hosting the stores, if you don't have any users yet, that fact will be painfully obvious. So before we could launch publicly we had to launch privately, in the sense of recruiting an initial set of users and making sure they had decent-looking stores.

\[9\] We'd had a code editor in Viaweb for users to define their own page styles. They didn't know it, but they were editing Lisp expressions underneath. But this wasn't an app editor, because the code ran when the merchants' sites were generated, not when shoppers visited them.

\[10\] This was the first instance of what is now a familiar experience, and so was what happened next, when I read the comments and found they were full of angry people. How could I claim that Lisp was better than other languages? Weren't they all Turing complete?

**Node ID:** 34259d5b-f0ea-436d-8f44-31d790cfbfb7  
**Similarity:** 1.5173875093460083  
**Text:** This name didn't last long before it was replaced by "software as a service," but it was current for long enough that I named this new company after it: it was going to be called Aspra.

I started working on the application builder, Dan worked on network infrastructure, and the two undergrads worked on the first two services (images and phone calls). But about halfway through the summer I realized I really didn't want to run a company — especially not a big one, which it was looking like this would have to be. I'd only started Viaweb because I needed the money. Now that I didn't need money anymore, why was I doing this? If this vision had to be realized as a company, then screw the vision. I'd build a subset that could be done as an open source project.

Much to my surprise, the time I spent working on this stuff was not wasted after all. After we started Y Combinator, I would often encounter startups working on parts of this new architecture, and it was very useful to have spent so much time thinking about it and even trying to write some of it.

The subset I would build as an open source project was the new Lisp, whose parentheses I now wouldn't even have to hide. A lot of Lisp hackers dream of building a new Lisp, partly because one of the distinctive features of the language is that it has dialects, and partly, I think, because we have in our minds a Platonic form of Lisp that all existing dialects fall short of. I certainly did. So at the end of the summer Dan and I switched to working on this new dialect of Lisp, which I called Arc, in a house I bought in Cambridge.

The following spring, lightning struck. I was invited to give a talk at a Lisp conference, so I gave one about how we'd used Lisp at Viaweb. Afterward I put a postscript file of this talk online, on paulgraham.com, which I'd created years before using Viaweb but had never used for anything. In one day it got 30,000 page views. What on earth had happened? The referring urls showed that someone had posted it on Slashdot.

In \[ \]:

Copied!

retrieved\_nodes \= bm25\_retriever.retrieve("What did the author do after RISD?")
for node in retrieved\_nodes:
    display\_source\_node(node, source\_length\=5000)

retrieved\_nodes = bm25\_retriever.retrieve("What did the author do after RISD?") for node in retrieved\_nodes: display\_source\_node(node, source\_length=5000)

**Node ID:** 3aeed631-54d7-4fc9-83cf-804ba393b281  
**Similarity:** 1.9751536846160889  
**Text:** Plus I was terribly irresponsible. This was back when a programming job meant showing up every day during certain working hours. That seemed unnatural to me, and on this point the rest of the world is coming around to my way of thinking, but at the time it caused a lot of friction. Toward the end of the year I spent much of my time surreptitiously working on On Lisp, which I had by this time gotten a contract to publish.

The good part was that I got paid huge amounts of money, especially by art student standards. In Florence, after paying my part of the rent, my budget for everything else had been $7 a day. Now I was getting paid more than 4 times that every hour, even when I was just sitting in a meeting. By living cheaply I not only managed to save enough to go back to RISD, but also paid off my college loans.

I learned some useful things at Interleaf, though they were mostly about what not to do. I learned that it's better for technology companies to be run by product people than sales people (though sales is a real skill and people who are good at it are really good at it), that it leads to bugs when code is edited by too many people, that cheap office space is no bargain if it's depressing, that planned meetings are inferior to corridor conversations, that big, bureaucratic customers are a dangerous source of money, and that there's not much overlap between conventional office hours and the optimal time for hacking, or conventional offices and the optimal place for it.

But the most important thing I learned, and which I used in both Viaweb and Y Combinator, is that the low end eats the high end: that it's good to be the "entry level" option, even though that will be less prestigious, because if you're not, someone else will be, and will squash you against the ceiling. Which in turn means that prestige is a danger sign.

When I left to go back to RISD the next fall, I arranged to do freelance work for the group that did projects for customers, and this was how I survived for the next several years.

**Node ID:** ea6aabac-ef00-418b-a79b-cc714daf6fb9  
**Similarity:** 1.91998291015625  
**Text:** At least not the painting department. The textile department, which my next door neighbor belonged to, seemed to be pretty rigorous. No doubt illustration and architecture were too. But painting was post-rigorous. Painting students were supposed to express themselves, which to the more worldly ones meant to try to cook up some sort of distinctive signature style.

A signature style is the visual equivalent of what in show business is known as a "schtick": something that immediately identifies the work as yours and no one else's. For example, when you see a painting that looks like a certain kind of cartoon, you know it's by Roy Lichtenstein. So if you see a big painting of this type hanging in the apartment of a hedge fund manager, you know he paid millions of dollars for it. That's not always why artists have a signature style, but it's usually why buyers pay a lot for such work. \[6\]

There were plenty of earnest students too: kids who "could draw" in high school, and now had come to what was supposed to be the best art school in the country, to learn to draw even better. They tended to be confused and demoralized by what they found at RISD, but they kept going, because painting was what they did. I was not one of the kids who could draw in high school, but at RISD I was definitely closer to their tribe than the tribe of signature style seekers.

I learned a lot in the color class I took at RISD, but otherwise I was basically teaching myself to paint, and I could do that for free. So in 1993 I dropped out. I hung around Providence for a bit, and then my college friend Nancy Parmet did me a big favor. A rent-controlled apartment in a building her mother owned in New York was becoming vacant. Did I want it? It wasn't much more than my current place, and New York was supposed to be where the artists were. So yes, I wanted it! \[7\]

Asterix comics begin by zooming in on a tiny corner of Roman Gaul that turns out not to be controlled by the Romans.

Hybrid Retriever with BM25 + Chroma[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/bm25_retriever/#hybrid-retriever-with-bm25-chroma)
--------------------------------------------------------------------------------------------------------------------------------------------------

Now we will combine bm25 and chroma for sparse and dense retrieval.

The results are combined using the `QueryFusionRetriever`.

With the retriever, we can make a complete `RetrieverQueryEngine`.

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, StorageContext
from llama\_index.core.storage.docstore import SimpleDocumentStore
from llama\_index.vector\_stores.chroma import ChromaVectorStore
import chromadb

docstore \= SimpleDocumentStore()
docstore.add\_documents(nodes)

db \= chromadb.PersistentClient(path\="./chroma\_db")
chroma\_collection \= db.get\_or\_create\_collection("dense\_vectors")
vector\_store \= ChromaVectorStore(chroma\_collection\=chroma\_collection)

storage\_context \= StorageContext.from\_defaults(
    docstore\=docstore, vector\_store\=vector\_store
)

index \= VectorStoreIndex(nodes\=nodes, storage\_context\=storage\_context)

from llama\_index.core import VectorStoreIndex, StorageContext from llama\_index.core.storage.docstore import SimpleDocumentStore from llama\_index.vector\_stores.chroma import ChromaVectorStore import chromadb docstore = SimpleDocumentStore() docstore.add\_documents(nodes) db = chromadb.PersistentClient(path="./chroma\_db") chroma\_collection = db.get\_or\_create\_collection("dense\_vectors") vector\_store = ChromaVectorStore(chroma\_collection=chroma\_collection) storage\_context = StorageContext.from\_defaults( docstore=docstore, vector\_store=vector\_store ) index = VectorStoreIndex(nodes=nodes, storage\_context=storage\_context)

In \[ \]:

Copied!

import nest\_asyncio

nest\_asyncio.apply()

from llama\_index.core.retrievers import QueryFusionRetriever

retriever \= QueryFusionRetriever(
    \[
        index.as\_retriever(similarity\_top\_k\=2),
        BM25Retriever.from\_defaults(
            docstore\=index.docstore, similarity\_top\_k\=2
        ),
    \],
    num\_queries\=1,
    use\_async\=True,
)

import nest\_asyncio nest\_asyncio.apply() from llama\_index.core.retrievers import QueryFusionRetriever retriever = QueryFusionRetriever( \[ index.as\_retriever(similarity\_top\_k=2), BM25Retriever.from\_defaults( docstore=index.docstore, similarity\_top\_k=2 ), \], num\_queries=1, use\_async=True, )

BM25S Count Tokens:   0%|          | 0/61 \[00:00<?, ?it/s\]

BM25S Compute Scores:   0%|          | 0/61 \[00:00<?, ?it/s\]

In \[ \]:

Copied!

nodes \= retriever.retrieve("What happened at Viaweb and Interleaf?")
for node in nodes:
    display\_source\_node(node, source\_length\=5000)

nodes = retriever.retrieve("What happened at Viaweb and Interleaf?") for node in nodes: display\_source\_node(node, source\_length=5000)

**Node ID:** d4b9b0fe-066a-4a43-b0b9-3d981ce09b63  
**Similarity:** 1.4261349439620972  
**Text:** Then we'd never have to write anything to run on users' computers. We could generate the sites on the same server we'd serve them from. Users wouldn't need anything more than a browser.

This kind of software, known as a web app, is common now, but at the time it wasn't clear that it was even possible. To find out, we decided to try making a version of our store builder that you could control through the browser. A couple days later, on August 12, we had one that worked. The UI was horrible, but it proved you could build a whole store through the browser, without any client software or typing anything into the command line on the server.

Now we felt like we were really onto something. I had visions of a whole new generation of software working this way. You wouldn't need versions, or ports, or any of that crap. At Interleaf there had been a whole group called Release Engineering that seemed to be at least as big as the group that actually wrote the software. Now you could just update the software right on the server.

We started a new company we called Viaweb, after the fact that our software worked via the web, and we got $10,000 in seed funding from Idelle's husband Julian. In return for that and doing the initial legal work and giving us business advice, we gave him 10% of the company. Ten years later this deal became the model for Y Combinator's. We knew founders needed something like this, because we'd needed it ourselves.

At this stage I had a negative net worth, because the thousand dollars or so I had in the bank was more than counterbalanced by what I owed the government in taxes. (Had I diligently set aside the proper proportion of the money I'd made consulting for Interleaf? No, I had not.) So although Robert had his graduate student stipend, I needed that seed funding to live on.

We originally hoped to launch in September, but we got more ambitious about the software as we worked on it.

**Node ID:** 4504224b-1d57-426f-bfb7-d1c1dd6fdae8  
**Similarity:** 1.3261895179748535  
**Text:** But in the long term the growth rate takes care of the absolute number. If we'd been a startup I was advising at Y Combinator, I would have said: Stop being so stressed out, because you're doing fine. You're growing 7x a year. Just don't hire too many more people and you'll soon be profitable, and then you'll control your own destiny.

Alas I hired lots more people, partly because our investors wanted me to, and partly because that's what startups did during the Internet Bubble. A company with just a handful of employees would have seemed amateurish. So we didn't reach breakeven until about when Yahoo bought us in the summer of 1998. Which in turn meant we were at the mercy of investors for the entire life of the company. And since both we and our investors were noobs at startups, the result was a mess even by startup standards.

It was a huge relief when Yahoo bought us. In principle our Viaweb stock was valuable. It was a share in a business that was profitable and growing rapidly. But it didn't feel very valuable to me; I had no idea how to value a business, but I was all too keenly aware of the near-death experiences we seemed to have every few months. Nor had I changed my grad student lifestyle significantly since we started. So when Yahoo bought us it felt like going from rags to riches. Since we were going to California, I bought a car, a yellow 1998 VW GTI. I remember thinking that its leather seats alone were by far the most luxurious thing I owned.

The next year, from the summer of 1998 to the summer of 1999, must have been the least productive of my life. I didn't realize it at the time, but I was worn out from the effort and stress of running Viaweb. For a while after I got to California I tried to continue my usual m.o. of programming till 3 in the morning, but fatigue combined with Yahoo's prematurely aged culture and grim cube farm in Santa Clara gradually dragged me down. After a few months it felt disconcertingly like working at Interleaf.

In \[ \]:

Copied!

from llama\_index.core.query\_engine import RetrieverQueryEngine

query\_engine \= RetrieverQueryEngine(retriever)

from llama\_index.core.query\_engine import RetrieverQueryEngine query\_engine = RetrieverQueryEngine(retriever)

In \[ \]:

Copied!

response \= query\_engine.query("What did the author do after RISD?")
print(response)

response = query\_engine.query("What did the author do after RISD?") print(response)

The author arranged to do freelance work for the group that did projects for customers after leaving RISD.

### Save and Load w/ a Vector Store[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/bm25_retriever/#save-and-load-w-a-vector-store)

With our data in chroma, and our nodes in our docstore, we can save and recreate!

The vector store is already saved automatically by chroma, but we will need to save our docstore.

In \[ \]:

Copied!

storage\_context.docstore.persist("./docstore.json")

\# or, we could ignore the docstore and just persist the bm25 retriever as shown above
\# bm25\_retriever.persist("./bm25\_retriever")

storage\_context.docstore.persist("./docstore.json") # or, we could ignore the docstore and just persist the bm25 retriever as shown above # bm25\_retriever.persist("./bm25\_retriever")

Now, we can reload and re-create our index.

In \[ \]:

Copied!

db \= chromadb.PersistentClient(path\="./chroma\_db")
chroma\_collection \= db.get\_or\_create\_collection("dense\_vectors")
vector\_store \= ChromaVectorStore(chroma\_collection\=chroma\_collection)

docstore \= SimpleDocumentStore.from\_persist\_path("./docstore.json")

storage\_context \= StorageContext.from\_defaults(
    docstore\=docstore, vector\_store\=vector\_store
)

index \= VectorStoreIndex(nodes\=\[\], storage\_context\=storage\_context)

db = chromadb.PersistentClient(path="./chroma\_db") chroma\_collection = db.get\_or\_create\_collection("dense\_vectors") vector\_store = ChromaVectorStore(chroma\_collection=chroma\_collection) docstore = SimpleDocumentStore.from\_persist\_path("./docstore.json") storage\_context = StorageContext.from\_defaults( docstore=docstore, vector\_store=vector\_store ) index = VectorStoreIndex(nodes=\[\], storage\_context=storage\_context)

Back to top

[Previous Bedrock (Knowledge Bases)](https://docs.llamaindex.ai/en/stable/examples/retrievers/bedrock_retriever/)[Next Composable Objects](https://docs.llamaindex.ai/en/stable/examples/retrievers/composable_retrievers/)
