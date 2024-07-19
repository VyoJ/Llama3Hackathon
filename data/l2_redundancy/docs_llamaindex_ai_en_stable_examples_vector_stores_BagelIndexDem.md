Title: Bagel Network - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/BagelIndexDemo/

Markdown Content:
Bagel Network - LlamaIndex


> [Bagel](https://docs.bageldb.ai/) is a Open Inference Data for AI. It is built for distributed Machine Learning compute. Cutting AI data infra spend by tenfold.

 [![Image 4: Discord](https://img.shields.io/discord/1073293645303795742)](https://discord.gg/bA7B6r97)  

*   [Website](https://www.bageldb.ai/)
*   [Documentation](https://docs.bageldb.ai/)
*   [Twitter](https://twitter.com/bageldb_ai)
*   [Discord](https://discord.gg/bA7B6r97)

Install Bagel with:

pip install bagelML

Like any other database, you can:

*   `.add`
*   `.get`
*   `.delete`
*   `.update`
*   `.upsert`
*   `.peek`
*   `.modify`
*   and `.find` runs the similarity search.

Basic Example[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BagelIndexDemo/#basic-example)
-----------------------------------------------------------------------------------------------------------

In this basic example, we take the a Paul Graham essay, split it into chunks, embed it using an open-source embedding model, load it into Bagel, and then query it.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-bagel
%pip install llama\-index\-embeddings\-huggingface
%pip install bagelML

%pip install llama-index-vector-stores-bagel %pip install llama-index-embeddings-huggingface %pip install bagelML

In \[ \]:

Copied!

\# import
from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.vector\_stores.bagel import BagelVectorStore
from llama\_index.core import StorageContext
from IPython.display import Markdown, display
import bagel
from bagel import Settings

\# import from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.vector\_stores.bagel import BagelVectorStore from llama\_index.core import StorageContext from IPython.display import Markdown, display import bagel from bagel import Settings

In \[ \]:

Copied!

\# set up OpenAI
import os
import getpass

os.environ\["OPENAI\_API\_KEY"\] \= getpass.getpass("OpenAI API Key:")
import openai

openai.api\_key \= os.environ\["OPENAI\_API\_KEY"\]

\# set up OpenAI import os import getpass os.environ\["OPENAI\_API\_KEY"\] = getpass.getpass("OpenAI API Key:") import openai openai.api\_key = os.environ\["OPENAI\_API\_KEY"\]

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

In \[ \]:

Copied!

\# create server settings
server\_settings \= Settings(
    bagel\_api\_impl\="rest", bagel\_server\_host\="api.bageldb.ai"
)

\# create client
client \= bagel.Client(server\_settings)

\# create collection
collection \= client.get\_or\_create\_cluster(
    "testing\_embeddings", embedding\_model\="custom", dimension\=384
)

\# define embedding function
embed\_model \= "local:BAAI/bge-small-en-v1.5"

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

\# set up BagelVectorStore and load in data
vector\_store \= BagelVectorStore(collection\=collection)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context, embed\_model\=embed\_model
)

query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did the author do growing up?")
print(f"<b>{response}</b>")

\# create server settings server\_settings = Settings( bagel\_api\_impl="rest", bagel\_server\_host="api.bageldb.ai" ) # create client client = bagel.Client(server\_settings) # create collection collection = client.get\_or\_create\_cluster( "testing\_embeddings", embedding\_model="custom", dimension=384 ) # define embedding function embed\_model = "local:BAAI/bge-small-en-v1.5" # load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data() # set up BagelVectorStore and load in data vector\_store = BagelVectorStore(collection=collection) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context, embed\_model=embed\_model ) query\_engine = index.as\_query\_engine() response = query\_engine.query("What did the author do growing up?") print(f"**{response}**")

Create - Add - Get[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BagelIndexDemo/#create-add-get)
-----------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

def create\_add\_get(client):
    """
    Create, add, and get
    """
    name \= "testing"

    \# Get or create a cluster
    cluster \= client.get\_or\_create\_cluster(name)

    \# Add documents to the cluster
    resp \= cluster.add(
        documents\=\[
            "This is document1",
            "This is bidhan",
        \],
        metadatas\=\[{"source": "google"}, {"source": "notion"}\],
        ids\=\[str(uuid.uuid4()), str(uuid.uuid4())\],
    )

    \# Print count
    print("count of docs:", cluster.count())

    \# Get the first item
    first\_item \= cluster.peek(1)
    if first\_item:
        print("get 1st item")

    print(">> create\_add\_get done !\\n")

def create\_add\_get(client): """ Create, add, and get """ name = "testing" # Get or create a cluster cluster = client.get\_or\_create\_cluster(name) # Add documents to the cluster resp = cluster.add( documents=\[ "This is document1", "This is bidhan", \], metadatas=\[{"source": "google"}, {"source": "notion"}\], ids=\[str(uuid.uuid4()), str(uuid.uuid4())\], ) # Print count print("count of docs:", cluster.count()) # Get the first item first\_item = cluster.peek(1) if first\_item: print("get 1st item") print(">> create\_add\_get done !\\n")

Create - Add - Find by Text[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BagelIndexDemo/#create-add-find-by-text)
-----------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

def create\_add\_find(client):
    """
    Create, add, & find

    Parameters
    ----------
    api : \_type\_
        \_description\_
    """
    name \= "testing"

    \# Get or create a cluster
    cluster \= client.get\_or\_create\_cluster(name)

    \# Add documents to the cluster
    cluster.add(
        documents\=\[
            "This is document",
            "This is Towhid",
            "This is text",
        \],
        metadatas\=\[
            {"source": "notion"},
            {"source": "notion"},
            {"source": "google-doc"},
        \],
        ids\=\[str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4())\],
    )

    \# Query the cluster for similar results
    results \= cluster.find(
        query\_texts\=\["This"\],
        n\_results\=5,
        where\={"source": "notion"},
        where\_document\={"$contains": "is"},
    )

    print(results)
    print(">> create\_add\_find done  !\\n")

def create\_add\_find(client): """ Create, add, & find Parameters ---------- api : \_type\_ \_description\_ """ name = "testing" # Get or create a cluster cluster = client.get\_or\_create\_cluster(name) # Add documents to the cluster cluster.add( documents=\[ "This is document", "This is Towhid", "This is text", \], metadatas=\[ {"source": "notion"}, {"source": "notion"}, {"source": "google-doc"}, \], ids=\[str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4())\], ) # Query the cluster for similar results results = cluster.find( query\_texts=\["This"\], n\_results=5, where={"source": "notion"}, where\_document={"$contains": "is"}, ) print(results) print(">> create\_add\_find done !\\n")

Create - Add - Find by Embeddings[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BagelIndexDemo/#create-add-find-by-embeddings)
-----------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

def create\_add\_find\_em(client):
    """Create, add, & find embeddings

    Parameters
    ----------
    api : \_type\_
        \_description\_
    """
    name \= "testing\_embeddings"
    \# Reset the Bagel server
    client.reset()

    \# Get or create a cluster
    cluster \= api.get\_or\_create\_cluster(name)
    \# Add embeddings and other data to the cluster
    cluster.add(
        embeddings\=\[
            \[1.1, 2.3, 3.2\],
            \[4.5, 6.9, 4.4\],
            \[1.1, 2.3, 3.2\],
            \[4.5, 6.9, 4.4\],
            \[1.1, 2.3, 3.2\],
            \[4.5, 6.9, 4.4\],
            \[1.1, 2.3, 3.2\],
            \[4.5, 6.9, 4.4\],
        \],
        metadatas\=\[
            {"uri": "img1.png", "style": "style1"},
            {"uri": "img2.png", "style": "style2"},
            {"uri": "img3.png", "style": "style1"},
            {"uri": "img4.png", "style": "style1"},
            {"uri": "img5.png", "style": "style1"},
            {"uri": "img6.png", "style": "style1"},
            {"uri": "img7.png", "style": "style1"},
            {"uri": "img8.png", "style": "style1"},
        \],
        documents\=\[
            "doc1",
            "doc2",
            "doc3",
            "doc4",
            "doc5",
            "doc6",
            "doc7",
            "doc8",
        \],
        ids\=\["id1", "id2", "id3", "id4", "id5", "id6", "id7", "id8"\],
    )

    \# Query the cluster for results
    results \= cluster.find(query\_embeddings\=\[\[1.1, 2.3, 3.2\]\], n\_results\=5)

    print("find result:", results)
    print(">> create\_add\_find\_em done  !\\n")

def create\_add\_find\_em(client): """Create, add, & find embeddings Parameters ---------- api : \_type\_ \_description\_ """ name = "testing\_embeddings" # Reset the Bagel server client.reset() # Get or create a cluster cluster = api.get\_or\_create\_cluster(name) # Add embeddings and other data to the cluster cluster.add( embeddings=\[ \[1.1, 2.3, 3.2\], \[4.5, 6.9, 4.4\], \[1.1, 2.3, 3.2\], \[4.5, 6.9, 4.4\], \[1.1, 2.3, 3.2\], \[4.5, 6.9, 4.4\], \[1.1, 2.3, 3.2\], \[4.5, 6.9, 4.4\], \], metadatas=\[ {"uri": "img1.png", "style": "style1"}, {"uri": "img2.png", "style": "style2"}, {"uri": "img3.png", "style": "style1"}, {"uri": "img4.png", "style": "style1"}, {"uri": "img5.png", "style": "style1"}, {"uri": "img6.png", "style": "style1"}, {"uri": "img7.png", "style": "style1"}, {"uri": "img8.png", "style": "style1"}, \], documents=\[ "doc1", "doc2", "doc3", "doc4", "doc5", "doc6", "doc7", "doc8", \], ids=\["id1", "id2", "id3", "id4", "id5", "id6", "id7", "id8"\], ) # Query the cluster for results results = cluster.find(query\_embeddings=\[\[1.1, 2.3, 3.2\]\], n\_results=5) print("find result:", results) print(">> create\_add\_find\_em done !\\n")

Create - Add - Modify - Update[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BagelIndexDemo/#create-add-modify-update)
---------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

def create\_add\_modify\_update(client):
    """
    Create, add, modify, and update

    Parameters
    ----------
    api : \_type\_
        \_description\_
    """
    name \= "testing"
    new\_name \= "new\_" + name

    \# Get or create a cluster
    cluster \= client.get\_or\_create\_cluster(name)

    \# Modify the cluster name
    print("Before:", cluster.name)
    cluster.modify(name\=new\_name)
    print("After:", cluster.name)

    \# Add documents to the cluster
    cluster.add(
        documents\=\[
            "This is document1",
            "This is bidhan",
        \],
        metadatas\=\[{"source": "notion"}, {"source": "google"}\],
        ids\=\["id1", "id2"\],
    )

    \# Retrieve document metadata before updating
    print("Before update:")
    print(cluster.get(ids\=\["id1"\]))

    \# Update document metadata
    cluster.update(ids\=\["id1"\], metadatas\=\[{"source": "google"}\])

    \# Retrieve document metadata after updating
    print("After update source:")
    print(cluster.get(ids\=\["id1"\]))

    print(">> create\_add\_modify\_update done !\\n")

def create\_add\_modify\_update(client): """ Create, add, modify, and update Parameters ---------- api : \_type\_ \_description\_ """ name = "testing" new\_name = "new\_" + name # Get or create a cluster cluster = client.get\_or\_create\_cluster(name) # Modify the cluster name print("Before:", cluster.name) cluster.modify(name=new\_name) print("After:", cluster.name) # Add documents to the cluster cluster.add( documents=\[ "This is document1", "This is bidhan", \], metadatas=\[{"source": "notion"}, {"source": "google"}\], ids=\["id1", "id2"\], ) # Retrieve document metadata before updating print("Before update:") print(cluster.get(ids=\["id1"\])) # Update document metadata cluster.update(ids=\["id1"\], metadatas=\[{"source": "google"}\]) # Retrieve document metadata after updating print("After update source:") print(cluster.get(ids=\["id1"\])) print(">> create\_add\_modify\_update done !\\n")

Create - Upsert[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BagelIndexDemo/#create-upsert)
-------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

def create\_upsert(client):
    """
    Create and upsert

    Parameters
    ----------
    api : \_type\_
        \_description\_
    """
    \# Reset the Bagel server
    api.reset()

    name \= "testing"

    \# Get or create a cluster
    cluster \= client.get\_or\_create\_cluster(name)

    \# Add documents to the cluster
    cluster.add(
        documents\=\[
            "This is document1",
            "This is bidhan",
        \],
        metadatas\=\[{"source": "notion"}, {"source": "google"}\],
        ids\=\["id1", "id2"\],
    )

    \# Upsert documents in the cluster
    cluster.upsert(
        documents\=\[
            "This is document",
            "This is google",
        \],
        metadatas\=\[{"source": "notion"}, {"source": "google"}\],
        ids\=\["id1", "id3"\],
    )

    \# Print the count of documents in the cluster
    print("Count of documents:", cluster.count())
    print(">> create\_upsert done !\\n")

def create\_upsert(client): """ Create and upsert Parameters ---------- api : \_type\_ \_description\_ """ # Reset the Bagel server api.reset() name = "testing" # Get or create a cluster cluster = client.get\_or\_create\_cluster(name) # Add documents to the cluster cluster.add( documents=\[ "This is document1", "This is bidhan", \], metadatas=\[{"source": "notion"}, {"source": "google"}\], ids=\["id1", "id2"\], ) # Upsert documents in the cluster cluster.upsert( documents=\[ "This is document", "This is google", \], metadatas=\[{"source": "notion"}, {"source": "google"}\], ids=\["id1", "id3"\], ) # Print the count of documents in the cluster print("Count of documents:", cluster.count()) print(">> create\_upsert done !\\n")

Back to top

[Previous Bagel Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BagelAutoRetriever/)[Next Baidu VectorDB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BaiduVectorDBIndexDemo/)
