Title: Time-Weighted Rerank - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/TimeWeightedPostprocessorDemo/

Markdown Content:
Time-Weighted Rerank - LlamaIndex


Showcase capabilities of time-weighted node postprocessor

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.core.postprocessor import TimeWeightedPostprocessor
from llama\_index.core.node\_parser import SentenceSplitter
from llama\_index.core.storage.docstore import SimpleDocumentStore
from llama\_index.core.response.notebook\_utils import display\_response
from datetime import datetime, timedelta

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.core.postprocessor import TimeWeightedPostprocessor from llama\_index.core.node\_parser import SentenceSplitter from llama\_index.core.storage.docstore import SimpleDocumentStore from llama\_index.core.response.notebook\_utils import display\_response from datetime import datetime, timedelta

/home/loganm/miniconda3/envs/llama-index/lib/python3.11/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user\_install.html
  from .autonotebook import tqdm as notebook\_tqdm

### Parse Documents into Nodes, add to Docstore[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/TimeWeightedPostprocessorDemo/#parse-documents-into-nodes-add-to-docstore)

In this example, there are 3 different versions of PG's essay. They are largely identical **except** for one specific section, which details the amount of funding they raised for Viaweb.

V1: 50k, V2: 30k, V3: 10K

V1: -1 day, V2: -2 days, V3: -3 days

The idea is to encourage index to fetch the most recent info (which is V3)

In \[ \]:

Copied!

\# load documents
from llama\_index.core import StorageContext

now \= datetime.now()
key \= "\_\_last\_accessed\_\_"

doc1 \= SimpleDirectoryReader(
    input\_files\=\["./test\_versioned\_data/paul\_graham\_essay\_v1.txt"\]
).load\_data()\[0\]

doc2 \= SimpleDirectoryReader(
    input\_files\=\["./test\_versioned\_data/paul\_graham\_essay\_v2.txt"\]
).load\_data()\[0\]

doc3 \= SimpleDirectoryReader(
    input\_files\=\["./test\_versioned\_data/paul\_graham\_essay\_v3.txt"\]
).load\_data()\[0\]

\# define settings
from llama\_index.core import Settings

Settings.text\_splitter \= SentenceSplitter(chunk\_size\=512)

\# use node parser from settings to parse docs into nodes
nodes1 \= Settings.text\_splitter.get\_nodes\_from\_documents(\[doc1\])
nodes2 \= Settings.text\_splitter.get\_nodes\_from\_documents(\[doc2\])
nodes3 \= Settings.text\_splitter.get\_nodes\_from\_documents(\[doc3\])

\# fetch the modified chunk from each document, set metadata
\# also exclude the date from being read by the LLM
nodes1\[14\].metadata\[key\] \= (now \- timedelta(hours\=3)).timestamp()
nodes1\[14\].excluded\_llm\_metadata\_keys \= \[key\]

nodes2\[14\].metadata\[key\] \= (now \- timedelta(hours\=2)).timestamp()
nodes2\[14\].excluded\_llm\_metadata\_keys \= \[key\]

nodes3\[14\].metadata\[key\] \= (now \- timedelta(hours\=1)).timestamp()
nodes2\[14\].excluded\_llm\_metadata\_keys \= \[key\]

\# add to docstore
docstore \= SimpleDocumentStore()
nodes \= \[nodes1\[14\], nodes2\[14\], nodes3\[14\]\]
docstore.add\_documents(nodes)

storage\_context \= StorageContext.from\_defaults(docstore\=docstore)

\# load documents from llama\_index.core import StorageContext now = datetime.now() key = "\_\_last\_accessed\_\_" doc1 = SimpleDirectoryReader( input\_files=\["./test\_versioned\_data/paul\_graham\_essay\_v1.txt"\] ).load\_data()\[0\] doc2 = SimpleDirectoryReader( input\_files=\["./test\_versioned\_data/paul\_graham\_essay\_v2.txt"\] ).load\_data()\[0\] doc3 = SimpleDirectoryReader( input\_files=\["./test\_versioned\_data/paul\_graham\_essay\_v3.txt"\] ).load\_data()\[0\] # define settings from llama\_index.core import Settings Settings.text\_splitter = SentenceSplitter(chunk\_size=512) # use node parser from settings to parse docs into nodes nodes1 = Settings.text\_splitter.get\_nodes\_from\_documents(\[doc1\]) nodes2 = Settings.text\_splitter.get\_nodes\_from\_documents(\[doc2\]) nodes3 = Settings.text\_splitter.get\_nodes\_from\_documents(\[doc3\]) # fetch the modified chunk from each document, set metadata # also exclude the date from being read by the LLM nodes1\[14\].metadata\[key\] = (now - timedelta(hours=3)).timestamp() nodes1\[14\].excluded\_llm\_metadata\_keys = \[key\] nodes2\[14\].metadata\[key\] = (now - timedelta(hours=2)).timestamp() nodes2\[14\].excluded\_llm\_metadata\_keys = \[key\] nodes3\[14\].metadata\[key\] = (now - timedelta(hours=1)).timestamp() nodes2\[14\].excluded\_llm\_metadata\_keys = \[key\] # add to docstore docstore = SimpleDocumentStore() nodes = \[nodes1\[14\], nodes2\[14\], nodes3\[14\]\] docstore.add\_documents(nodes) storage\_context = StorageContext.from\_defaults(docstore=docstore)

### Build Index[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/TimeWeightedPostprocessorDemo/#build-index)

In \[ \]:

Copied!

\# build index
index \= VectorStoreIndex(nodes, storage\_context\=storage\_context)

\# build index index = VectorStoreIndex(nodes, storage\_context=storage\_context)

### Define Recency Postprocessors[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/TimeWeightedPostprocessorDemo/#define-recency-postprocessors)

In \[ \]:

Copied!

node\_postprocessor \= TimeWeightedPostprocessor(
    time\_decay\=0.5, time\_access\_refresh\=False, top\_k\=1
)

node\_postprocessor = TimeWeightedPostprocessor( time\_decay=0.5, time\_access\_refresh=False, top\_k=1 )

### Query Index[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/TimeWeightedPostprocessorDemo/#query-index)

In \[ \]:

Copied!

\# naive query
query\_engine \= index.as\_query\_engine(
    similarity\_top\_k\=3,
)
response \= query\_engine.query(
    "How much did the author raise in seed funding from Idelle's husband"
    " (Julian) for Viaweb?",
)

\# naive query query\_engine = index.as\_query\_engine( similarity\_top\_k=3, ) response = query\_engine.query( "How much did the author raise in seed funding from Idelle's husband" " (Julian) for Viaweb?", )

In \[ \]:

Copied!

display\_response(response)

display\_response(response)

**`Final Response:`** $50,000

In \[ \]:

Copied!

\# query using time weighted node postprocessor

query\_engine \= index.as\_query\_engine(
    similarity\_top\_k\=3, node\_postprocessors\=\[node\_postprocessor\]
)
response \= query\_engine.query(
    "How much did the author raise in seed funding from Idelle's husband"
    " (Julian) for Viaweb?",
)

\# query using time weighted node postprocessor query\_engine = index.as\_query\_engine( similarity\_top\_k=3, node\_postprocessors=\[node\_postprocessor\] ) response = query\_engine.query( "How much did the author raise in seed funding from Idelle's husband" " (Julian) for Viaweb?", )

In \[ \]:

Copied!

display\_response(response)

display\_response(response)

**`Final Response:`** The author raised $10,000 in seed funding from Idelle's husband (Julian) for Viaweb.

### Query Index (Lower-Level Usage)[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/TimeWeightedPostprocessorDemo/#query-index-lower-level-usage)

In this example we first get the full set of nodes from a query call, and then send to node postprocessor, and then finally synthesize response through a summary index.

In \[ \]:

Copied!

from llama\_index.core import SummaryIndex

from llama\_index.core import SummaryIndex

In \[ \]:

Copied!

query\_str \= (
    "How much did the author raise in seed funding from Idelle's husband"
    " (Julian) for Viaweb?"
)

query\_str = ( "How much did the author raise in seed funding from Idelle's husband" " (Julian) for Viaweb?" )

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(
    similarity\_top\_k\=3, response\_mode\="no\_text"
)
init\_response \= query\_engine.query(
    query\_str,
)
resp\_nodes \= \[n for n in init\_response.source\_nodes\]

query\_engine = index.as\_query\_engine( similarity\_top\_k=3, response\_mode="no\_text" ) init\_response = query\_engine.query( query\_str, ) resp\_nodes = \[n for n in init\_response.source\_nodes\]

In \[ \]:

Copied!

\# get the post-processed nodes -- which should be the top-1 sorted by date
new\_resp\_nodes \= node\_postprocessor.postprocess\_nodes(resp\_nodes)

summary\_index \= SummaryIndex(\[n.node for n in new\_resp\_nodes\])
query\_engine \= summary\_index.as\_query\_engine()
response \= query\_engine.query(query\_str)

\# get the post-processed nodes -- which should be the top-1 sorted by date new\_resp\_nodes = node\_postprocessor.postprocess\_nodes(resp\_nodes) summary\_index = SummaryIndex(\[n.node for n in new\_resp\_nodes\]) query\_engine = summary\_index.as\_query\_engine() response = query\_engine.query(query\_str)

In \[ \]:

Copied!

display\_response(response)

display\_response(response)

**`Final Response:`** The author raised $10,000 in seed funding from Idelle's husband (Julian) for Viaweb.

Back to top

[Previous SentenceTransformerRerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/SentenceTransformerRerank/)[Next VoyageAI Rerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/VoyageAIRerank/)

Hi, how can I help you?

🦙
