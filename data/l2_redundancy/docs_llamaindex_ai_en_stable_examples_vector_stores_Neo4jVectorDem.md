Title: Neo4j vector store - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/Neo4jVectorDemo/

Markdown Content:
Neo4j vector store - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-neo4jvector

%pip install llama-index-vector-stores-neo4jvector

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import os
import openai

os.environ\["OPENAI\_API\_KEY"\] \= "OPENAI\_API\_KEY"
openai.api\_key \= os.environ\["OPENAI\_API\_KEY"\]

import os import openai os.environ\["OPENAI\_API\_KEY"\] = "OPENAI\_API\_KEY" openai.api\_key = os.environ\["OPENAI\_API\_KEY"\]

Initiate Neo4j vector wrapper[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Neo4jVectorDemo/#initiate-neo4j-vector-wrapper)
--------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.vector\_stores.neo4jvector import Neo4jVectorStore

username \= "neo4j"
password \= "pleaseletmein"
url \= "bolt://localhost:7687"
embed\_dim \= 1536

neo4j\_vector \= Neo4jVectorStore(username, password, url, embed\_dim)

from llama\_index.vector\_stores.neo4jvector import Neo4jVectorStore username = "neo4j" password = "pleaseletmein" url = "bolt://localhost:7687" embed\_dim = 1536 neo4j\_vector = Neo4jVectorStore(username, password, url, embed\_dim)

Load documents, build the VectorStoreIndex[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Neo4jVectorDemo/#load-documents-build-the-vectorstoreindex)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from IPython.display import Markdown, display

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from IPython.display import Markdown, display

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

\--2023-12-14 18:44:00--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.111.133, 185.199.109.133, 185.199.110.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.111.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 75042 (73K) \[text/plain\]
Saving to: ‘data/paul\_graham/paul\_graham\_essay.txt’

data/paul\_graham/pa 100%\[>\]  73,28K  --.-KB/s    in 0,03s   

2023-12-14 18:44:00 (2,16 MB/s) - ‘data/paul\_graham/paul\_graham\_essay.txt’ saved \[75042/75042\]

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham").load\_data()

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham").load\_data()

In \[ \]:

Copied!

from llama\_index.core import StorageContext

storage\_context \= StorageContext.from\_defaults(vector\_store\=neo4j\_vector)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

from llama\_index.core import StorageContext storage\_context = StorageContext.from\_defaults(vector\_store=neo4j\_vector) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What happened at interleaf?")
display(Markdown(f"<b>{response}</b>"))

query\_engine = index.as\_query\_engine() response = query\_engine.query("What happened at interleaf?") display(Markdown(f"**{response}**"))

**At Interleaf, they added a scripting language inspired by Emacs and made it a dialect of Lisp. They were looking for a Lisp hacker to write things in this scripting language. The author of the text worked at Interleaf and mentioned that their Lisp was the thinnest icing on a giant C cake. The author also mentioned that they didn't know C and didn't want to learn it, so they never understood most of the software at Interleaf. Additionally, the author admitted to being a bad employee and spending much of their time working on a separate project called On Lisp.**

Hybrid search[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Neo4jVectorDemo/#hybrid-search)
------------------------------------------------------------------------------------------------------------

Hybrid search uses a combination of keyword and vector search In order to use hybrid search, you need to set the `hybrid_search` to `True`

In \[ \]:

Copied!

neo4j\_vector\_hybrid \= Neo4jVectorStore(
    username, password, url, embed\_dim, hybrid\_search\=True
)

neo4j\_vector\_hybrid = Neo4jVectorStore( username, password, url, embed\_dim, hybrid\_search=True )

In \[ \]:

Copied!

storage\_context \= StorageContext.from\_defaults(
    vector\_store\=neo4j\_vector\_hybrid
)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What happened at interleaf?")
display(Markdown(f"<b>{response}</b>"))

storage\_context = StorageContext.from\_defaults( vector\_store=neo4j\_vector\_hybrid ) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context ) query\_engine = index.as\_query\_engine() response = query\_engine.query("What happened at interleaf?") display(Markdown(f"**{response}**"))

**At Interleaf, they added a scripting language inspired by Emacs and made it a dialect of Lisp. They were looking for a Lisp hacker to write things in this scripting language. The author of the essay worked at Interleaf but didn't understand most of the software because he didn't know C and didn't want to learn it. He also mentioned that their Lisp was the thinnest icing on a giant C cake. The author admits to being a bad employee and spending much of his time working on a contract to publish On Lisp.**

Load existing vector index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Neo4jVectorDemo/#load-existing-vector-index)
--------------------------------------------------------------------------------------------------------------------------------------

In order to connect to an existing vector index, you need to define the `index_name` and `text_node_property` parameters:

*   index\_name: name of the existing vector index (default is `vector`)
*   text\_node\_property: name of the property that containt the text value (default is `text`)

In \[ \]:

Copied!

index\_name \= "existing\_index"
text\_node\_property \= "text"
existing\_vector \= Neo4jVectorStore(
    username,
    password,
    url,
    embed\_dim,
    index\_name\=index\_name,
    text\_node\_property\=text\_node\_property,
)

loaded\_index \= VectorStoreIndex.from\_vector\_store(existing\_vector)

index\_name = "existing\_index" text\_node\_property = "text" existing\_vector = Neo4jVectorStore( username, password, url, embed\_dim, index\_name=index\_name, text\_node\_property=text\_node\_property, ) loaded\_index = VectorStoreIndex.from\_vector\_store(existing\_vector)

Customizing responses[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Neo4jVectorDemo/#customizing-responses)
----------------------------------------------------------------------------------------------------------------------------

You can customize the retrieved information from the knowledge graph using the `retrieval_query` parameter.

The retrieval query must return the following four columns:

*   text:str - The text of the returned document
*   score:str - similarity score
*   id:str - node id
*   metadata: Dict - dictionary with additional metadata (must contain `_node_type` and `_node_content` keys)

In \[ \]:

Copied!

retrieval\_query \= (
    "RETURN 'Interleaf hired Tomaz' AS text, score, node.id AS id, "
    "{author: 'Tomaz', \_node\_type:node.\_node\_type, \_node\_content:node.\_node\_content} AS metadata"
)
neo4j\_vector\_retrieval \= Neo4jVectorStore(
    username, password, url, embed\_dim, retrieval\_query\=retrieval\_query
)

retrieval\_query = ( "RETURN 'Interleaf hired Tomaz' AS text, score, node.id AS id, " "{author: 'Tomaz', \_node\_type:node.\_node\_type, \_node\_content:node.\_node\_content} AS metadata" ) neo4j\_vector\_retrieval = Neo4jVectorStore( username, password, url, embed\_dim, retrieval\_query=retrieval\_query )

In \[ \]:

Copied!

loaded\_index \= VectorStoreIndex.from\_vector\_store(
    neo4j\_vector\_retrieval
).as\_query\_engine()
response \= loaded\_index.query("What happened at interleaf?")
display(Markdown(f"<b>{response}</b>"))

loaded\_index = VectorStoreIndex.from\_vector\_store( neo4j\_vector\_retrieval ).as\_query\_engine() response = loaded\_index.query("What happened at interleaf?") display(Markdown(f"**{response}**"))

**Interleaf hired Tomaz.**

Back to top

[Previous MyScale Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MyScaleIndexDemo/)[Next Opensearch Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/OpensearchDemo/)
