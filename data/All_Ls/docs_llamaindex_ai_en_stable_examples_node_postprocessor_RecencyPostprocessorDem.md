Title: Recency Filtering - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/RecencyPostprocessorDemo/

Markdown Content:
Recency Filtering - LlamaIndex


Showcase capabilities of recency-weighted node postprocessor

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..."

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.core.postprocessor import (
    FixedRecencyPostprocessor,
    EmbeddingRecencyPostprocessor,
)
from llama\_index.core.node\_parser import SentenceSplitter
from llama\_index.core.storage.docstore import SimpleDocumentStore
from llama\_index.core.response.notebook\_utils import display\_response

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.core.postprocessor import ( FixedRecencyPostprocessor, EmbeddingRecencyPostprocessor, ) from llama\_index.core.node\_parser import SentenceSplitter from llama\_index.core.storage.docstore import SimpleDocumentStore from llama\_index.core.response.notebook\_utils import display\_response

### Parse Documents into Nodes, add to Docstore[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/RecencyPostprocessorDemo/#parse-documents-into-nodes-add-to-docstore)

In this example, there are 3 different versions of PG's essay. They are largely identical **except** for one specific section, which details the amount of funding they raised for Viaweb.

V1: 50k, V2: 30k, V3: 10K

V1: 2020-01-01, V2: 2020-02-03, V3: 2022-04-12

The idea is to encourage index to fetch the most recent info (which is V3)

In \[ \]:

Copied!

\# load documents
from llama\_index.core import StorageContext

def get\_file\_metadata(file\_name: str):
    """Get file metadata."""
    if "v1" in file\_name:
        return {"date": "2020-01-01"}
    elif "v2" in file\_name:
        return {"date": "2020-02-03"}
    elif "v3" in file\_name:
        return {"date": "2022-04-12"}
    else:
        raise ValueError("invalid file")

documents \= SimpleDirectoryReader(
    input\_files\=\[
        "test\_versioned\_data/paul\_graham\_essay\_v1.txt",
        "test\_versioned\_data/paul\_graham\_essay\_v2.txt",
        "test\_versioned\_data/paul\_graham\_essay\_v3.txt",
    \],
    file\_metadata\=get\_file\_metadata,
).load\_data()

\# define settings
from llama\_index.core import Settings

Settings.text\_splitter \= SentenceSplitter(chunk\_size\=512)

\# use node parser to parse into nodes
nodes \= Settings.text\_splitter.get\_nodes\_from\_documents(documents)

\# add to docstore
docstore \= SimpleDocumentStore()
docstore.add\_documents(nodes)

storage\_context \= StorageContext.from\_defaults(docstore\=docstore)

\# load documents from llama\_index.core import StorageContext def get\_file\_metadata(file\_name: str): """Get file metadata.""" if "v1" in file\_name: return {"date": "2020-01-01"} elif "v2" in file\_name: return {"date": "2020-02-03"} elif "v3" in file\_name: return {"date": "2022-04-12"} else: raise ValueError("invalid file") documents = SimpleDirectoryReader( input\_files=\[ "test\_versioned\_data/paul\_graham\_essay\_v1.txt", "test\_versioned\_data/paul\_graham\_essay\_v2.txt", "test\_versioned\_data/paul\_graham\_essay\_v3.txt", \], file\_metadata=get\_file\_metadata, ).load\_data() # define settings from llama\_index.core import Settings Settings.text\_splitter = SentenceSplitter(chunk\_size=512) # use node parser to parse into nodes nodes = Settings.text\_splitter.get\_nodes\_from\_documents(documents) # add to docstore docstore = SimpleDocumentStore() docstore.add\_documents(nodes) storage\_context = StorageContext.from\_defaults(docstore=docstore)

In \[ \]:

Copied!

print(documents\[2\].get\_text())

print(documents\[2\].get\_text())

### Build Index[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/RecencyPostprocessorDemo/#build-index)

In \[ \]:

Copied!

\# build index
index \= VectorStoreIndex(nodes, storage\_context\=storage\_context)

\# build index index = VectorStoreIndex(nodes, storage\_context=storage\_context)

INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total embedding token usage: 84471 tokens

### Define Recency Postprocessors[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/RecencyPostprocessorDemo/#define-recency-postprocessors)

In \[ \]:

Copied!

node\_postprocessor \= FixedRecencyPostprocessor()

node\_postprocessor = FixedRecencyPostprocessor()

In \[ \]:

Copied!

node\_postprocessor\_emb \= EmbeddingRecencyPostprocessor()

node\_postprocessor\_emb = EmbeddingRecencyPostprocessor()

### Query Index[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/RecencyPostprocessorDemo/#query-index)

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

INFO:llama\_index.token\_counter.token\_counter:> \[query\] Total LLM token usage: 1813 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[query\] Total embedding token usage: 22 tokens

In \[ \]:

Copied!

\# query using fixed recency node postprocessor

query\_engine \= index.as\_query\_engine(
    similarity\_top\_k\=3, node\_postprocessors\=\[node\_postprocessor\]
)
response \= query\_engine.query(
    "How much did the author raise in seed funding from Idelle's husband"
    " (Julian) for Viaweb?",
)

\# query using fixed recency node postprocessor query\_engine = index.as\_query\_engine( similarity\_top\_k=3, node\_postprocessors=\[node\_postprocessor\] ) response = query\_engine.query( "How much did the author raise in seed funding from Idelle's husband" " (Julian) for Viaweb?", )

In \[ \]:

Copied!

\# query using embedding-based node postprocessor

query\_engine \= index.as\_query\_engine(
    similarity\_top\_k\=3, node\_postprocessors\=\[node\_postprocessor\_emb\]
)
response \= query\_engine.query(
    "How much did the author raise in seed funding from Idelle's husband"
    " (Julian) for Viaweb?",
)

\# query using embedding-based node postprocessor query\_engine = index.as\_query\_engine( similarity\_top\_k=3, node\_postprocessors=\[node\_postprocessor\_emb\] ) response = query\_engine.query( "How much did the author raise in seed funding from Idelle's husband" " (Julian) for Viaweb?", )

INFO:llama\_index.token\_counter.token\_counter:> \[query\] Total LLM token usage: 541 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[query\] Total embedding token usage: 22 tokens

### Query Index (Lower-Level Usage)[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/RecencyPostprocessorDemo/#query-index-lower-level-usage)

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
resp\_nodes \= \[n.node for n in init\_response.source\_nodes\]

query\_engine = index.as\_query\_engine( similarity\_top\_k=3, response\_mode="no\_text" ) init\_response = query\_engine.query( query\_str, ) resp\_nodes = \[n.node for n in init\_response.source\_nodes\]

INFO:llama\_index.token\_counter.token\_counter:> \[query\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[query\] Total embedding token usage: 22 tokens

In \[ \]:

Copied!

summary\_index \= SummaryIndex(resp\_nodes)
query\_engine \= summary\_index.as\_query\_engine(
    node\_postprocessors\=\[node\_postprocessor\]
)
response \= query\_engine.query(query\_str)

summary\_index = SummaryIndex(resp\_nodes) query\_engine = summary\_index.as\_query\_engine( node\_postprocessors=\[node\_postprocessor\] ) response = query\_engine.query(query\_str)

INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total embedding token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[query\] Total LLM token usage: 541 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[query\] Total embedding token usage: 0 tokens

Back to top

[Previous Forward/Backward Augmentation](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/PrevNextPostprocessorDemo/)[Next SentenceTransformerRerank](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/SentenceTransformerRerank/)

Hi, how can I help you?

🦙
