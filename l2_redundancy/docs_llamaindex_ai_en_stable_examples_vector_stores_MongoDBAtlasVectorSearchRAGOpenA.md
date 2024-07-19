Title: MongoDBAtlasVectorSearchRAGOpenAI - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/MongoDBAtlasVectorSearchRAGOpenAI/

Markdown Content:
MongoDBAtlasVectorSearchRAGOpenAI - LlamaIndex


       

In \[ \]:

Copied!

!pip install llama\-index
!pip install llama\-index\-vector\-stores\-mongodb
!pip install llama\-index\-embeddings\-openai
!pip install pymongo
!pip install datasets
!pip install pandas

!pip install llama-index !pip install llama-index-vector-stores-mongodb !pip install llama-index-embeddings-openai !pip install pymongo !pip install datasets !pip install pandas

In \[ \]:

Copied!

%env OPENAI\_API\_KEY\=OPENAI\_API\_KEY

%env OPENAI\_API\_KEY=OPENAI\_API\_KEY

In \[ \]:

Copied!

from datasets import load\_dataset
import pandas as pd

\# https://huggingface.co/datasets/AIatMongoDB/embedded\_movies
dataset \= load\_dataset("AIatMongoDB/embedded\_movies")

\# Convert the dataset to a pandas dataframe
dataset\_df \= pd.DataFrame(dataset\["train"\])

dataset\_df.head(5)

from datasets import load\_dataset import pandas as pd # https://huggingface.co/datasets/AIatMongoDB/embedded\_movies dataset = load\_dataset("AIatMongoDB/embedded\_movies") # Convert the dataset to a pandas dataframe dataset\_df = pd.DataFrame(dataset\["train"\]) dataset\_df.head(5)

Out\[ \]:

|  | awards | metacritic | rated | fullplot | title | writers | languages | plot | plot\_embedding | runtime | countries | genres | directors | cast | type | imdb | poster | num\_mflix\_comments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | {'nominations': 0, 'text': '1 win.', 'wins': 1} | NaN | None | Young Pauline is left a lot of money when her ... | The Perils of Pauline | \[Charles W. Goddard (screenplay), Basil Dickey... | \[English\] | Young Pauline is left a lot of money when her ... | \[0.00072939653, -0.026834568, 0.013515796, -0.... | 199.0 | \[USA\] | \[Action\] | \[Louis J. Gasnier, Donald MacKenzie\] | \[Pearl White, Crane Wilbur, Paul Panzer, Edwar... | movie | {'id': 4465, 'rating': 7.6, 'votes': 744} | https://m.media-amazon.com/images/M/MV5BMzgxOD... | 0 |
| 1 | {'nominations': 1, 'text': '1 nomination.', 'w... | NaN | TV-G | As a penniless man worries about how he will m... | From Hand to Mouth | \[H.M. Walker (titles)\] | \[English\] | A penniless young man tries to save an heiress... | \[-0.022837115, -0.022941574, 0.014937485, -0.0... | 22.0 | \[USA\] | \[Comedy, Short, Action\] | \[Alfred J. Goulding, Hal Roach\] | \[Harold Lloyd, Mildred Davis, 'Snub' Pollard, ... | movie | {'id': 10146, 'rating': 7.0, 'votes': 639} | https://m.media-amazon.com/images/M/MV5BNzE1OW... | 0 |
| 2 | {'nominations': 0, 'text': '1 win.', 'wins': 1} | NaN | None | Michael "Beau" Geste leaves England in disgrac... | Beau Geste | \[Herbert Brenon (adaptation), John Russell (ad... | \[English\] | Michael "Beau" Geste leaves England in disgrac... | \[0.00023330493, -0.028511643, 0.014653289, -0.... | 101.0 | \[USA\] | \[Action, Adventure, Drama\] | \[Herbert Brenon\] | \[Ronald Colman, Neil Hamilton, Ralph Forbes, A... | movie | {'id': 16634, 'rating': 6.9, 'votes': 222} | None | 0 |
| 3 | {'nominations': 0, 'text': '1 win.', 'wins': 1} | NaN | None | A nobleman vows to avenge the death of his fat... | The Black Pirate | \[Douglas Fairbanks (story), Jack Cunningham (a... | None | Seeking revenge, an athletic young man joins t... | \[-0.005927917, -0.033394486, 0.0015323418, -0.... | 88.0 | \[USA\] | \[Adventure, Action\] | \[Albert Parker\] | \[Billie Dove, Tempe Pigott, Donald Crisp, Sam ... | movie | {'id': 16654, 'rating': 7.2, 'votes': 1146} | https://m.media-amazon.com/images/M/MV5BMzU0ND... | 1 |
| 4 | {'nominations': 1, 'text': '1 nomination.', 'w... | NaN | PASSED | The Uptown Boy, J. Harold Manners (Lloyd) is a... | For Heaven's Sake | \[Ted Wilde (story), John Grey (story), Clyde B... | \[English\] | An irresponsible young millionaire changes his... | \[-0.0059373598, -0.026604708, -0.0070914757, -... | 58.0 | \[USA\] | \[Action, Comedy, Romance\] | \[Sam Taylor\] | \[Harold Lloyd, Jobyna Ralston, Noah Young, Jim... | movie | {'id': 16895, 'rating': 7.6, 'votes': 918} | https://m.media-amazon.com/images/M/MV5BMTcxMT... | 0 |

 

 

In \[ \]:

Copied!

\# Remove data point where fullplot coloumn is missing
dataset\_df \= dataset\_df.dropna(subset\=\["fullplot"\])
print("\\nNumber of missing values in each column after removal:")
print(dataset\_df.isnull().sum())

\# Remove the plot\_embedding from each data point in the dataset as we are going to create new embeddings with the new OpenAI emebedding Model "text-embedding-3-small"
dataset\_df \= dataset\_df.drop(columns\=\["plot\_embedding"\])

dataset\_df.head(5)

\# Remove data point where fullplot coloumn is missing dataset\_df = dataset\_df.dropna(subset=\["fullplot"\]) print("\\nNumber of missing values in each column after removal:") print(dataset\_df.isnull().sum()) # Remove the plot\_embedding from each data point in the dataset as we are going to create new embeddings with the new OpenAI emebedding Model "text-embedding-3-small" dataset\_df = dataset\_df.drop(columns=\["plot\_embedding"\]) dataset\_df.head(5)

Number of missing values in each column after removal:
awards                  0
metacritic            893
rated                 279
fullplot                0
title                   0
writers                13
languages               1
plot                    0
plot\_embedding          1
runtime                14
countries               0
genres                  0
directors              12
cast                    1
type                    0
imdb                    0
poster                 78
num\_mflix\_comments      0
dtype: int64

Out\[ \]:

|  | awards | metacritic | rated | fullplot | title | writers | languages | plot | runtime | countries | genres | directors | cast | type | imdb | poster | num\_mflix\_comments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | {'nominations': 0, 'text': '1 win.', 'wins': 1} | NaN | None | Young Pauline is left a lot of money when her ... | The Perils of Pauline | \[Charles W. Goddard (screenplay), Basil Dickey... | \[English\] | Young Pauline is left a lot of money when her ... | 199.0 | \[USA\] | \[Action\] | \[Louis J. Gasnier, Donald MacKenzie\] | \[Pearl White, Crane Wilbur, Paul Panzer, Edwar... | movie | {'id': 4465, 'rating': 7.6, 'votes': 744} | https://m.media-amazon.com/images/M/MV5BMzgxOD... | 0 |
| 1 | {'nominations': 1, 'text': '1 nomination.', 'w... | NaN | TV-G | As a penniless man worries about how he will m... | From Hand to Mouth | \[H.M. Walker (titles)\] | \[English\] | A penniless young man tries to save an heiress... | 22.0 | \[USA\] | \[Comedy, Short, Action\] | \[Alfred J. Goulding, Hal Roach\] | \[Harold Lloyd, Mildred Davis, 'Snub' Pollard, ... | movie | {'id': 10146, 'rating': 7.0, 'votes': 639} | https://m.media-amazon.com/images/M/MV5BNzE1OW... | 0 |
| 2 | {'nominations': 0, 'text': '1 win.', 'wins': 1} | NaN | None | Michael "Beau" Geste leaves England in disgrac... | Beau Geste | \[Herbert Brenon (adaptation), John Russell (ad... | \[English\] | Michael "Beau" Geste leaves England in disgrac... | 101.0 | \[USA\] | \[Action, Adventure, Drama\] | \[Herbert Brenon\] | \[Ronald Colman, Neil Hamilton, Ralph Forbes, A... | movie | {'id': 16634, 'rating': 6.9, 'votes': 222} | None | 0 |
| 3 | {'nominations': 0, 'text': '1 win.', 'wins': 1} | NaN | None | A nobleman vows to avenge the death of his fat... | The Black Pirate | \[Douglas Fairbanks (story), Jack Cunningham (a... | None | Seeking revenge, an athletic young man joins t... | 88.0 | \[USA\] | \[Adventure, Action\] | \[Albert Parker\] | \[Billie Dove, Tempe Pigott, Donald Crisp, Sam ... | movie | {'id': 16654, 'rating': 7.2, 'votes': 1146} | https://m.media-amazon.com/images/M/MV5BMzU0ND... | 1 |
| 4 | {'nominations': 1, 'text': '1 nomination.', 'w... | NaN | PASSED | The Uptown Boy, J. Harold Manners (Lloyd) is a... | For Heaven's Sake | \[Ted Wilde (story), John Grey (story), Clyde B... | \[English\] | An irresponsible young millionaire changes his... | 58.0 | \[USA\] | \[Action, Comedy, Romance\] | \[Sam Taylor\] | \[Harold Lloyd, Jobyna Ralston, Noah Young, Jim... | movie | {'id': 16895, 'rating': 7.6, 'votes': 918} | https://m.media-amazon.com/images/M/MV5BMTcxMT... | 0 |

 

 

In \[ \]:

Copied!

from llama\_index.core.settings import Settings
from llama\_index.llms.openai import OpenAI
from llama\_index.embeddings.openai import OpenAIEmbedding

embed\_model \= OpenAIEmbedding(model\="text-embedding-3-small", dimensions\=256)
llm \= OpenAI()

Settings.llm \= llm
Settings.embed\_model \= embed\_model

from llama\_index.core.settings import Settings from llama\_index.llms.openai import OpenAI from llama\_index.embeddings.openai import OpenAIEmbedding embed\_model = OpenAIEmbedding(model="text-embedding-3-small", dimensions=256) llm = OpenAI() Settings.llm = llm Settings.embed\_model = embed\_model

In \[ \]:

Copied!

import json
from llama\_index.core import Document
from llama\_index.core.schema import MetadataMode

\# Convert the DataFrame to a JSON string representation
documents\_json \= dataset\_df.to\_json(orient\="records")
\# Load the JSON string into a Python list of dictionaries
documents\_list \= json.loads(documents\_json)

llama\_documents \= \[\]

for document in documents\_list:
    \# Value for metadata must be one of (str, int, float, None)
    document\["writers"\] \= json.dumps(document\["writers"\])
    document\["languages"\] \= json.dumps(document\["languages"\])
    document\["genres"\] \= json.dumps(document\["genres"\])
    document\["cast"\] \= json.dumps(document\["cast"\])
    document\["directors"\] \= json.dumps(document\["directors"\])
    document\["countries"\] \= json.dumps(document\["countries"\])
    document\["imdb"\] \= json.dumps(document\["imdb"\])
    document\["awards"\] \= json.dumps(document\["awards"\])

    \# Create a Document object with the text and excluded metadata for llm and embedding models
    llama\_document \= Document(
        text\=document\["fullplot"\],
        metadata\=document,
        excluded\_llm\_metadata\_keys\=\["fullplot", "metacritic"\],
        excluded\_embed\_metadata\_keys\=\[
            "fullplot",
            "metacritic",
            "poster",
            "num\_mflix\_comments",
            "runtime",
            "rated",
        \],
        metadata\_template\="{key}\=>{value}",
        text\_template\="Metadata: {metadata\_str}\\n\-----\\nContent: {content}",
    )

    llama\_documents.append(llama\_document)

\# Observing an example of what the LLM and Embedding model receive as input
print(
    "\\nThe LLM sees this: \\n",
    llama\_documents\[0\].get\_content(metadata\_mode\=MetadataMode.LLM),
)
print(
    "\\nThe Embedding model sees this: \\n",
    llama\_documents\[0\].get\_content(metadata\_mode\=MetadataMode.EMBED),
)

import json from llama\_index.core import Document from llama\_index.core.schema import MetadataMode # Convert the DataFrame to a JSON string representation documents\_json = dataset\_df.to\_json(orient="records") # Load the JSON string into a Python list of dictionaries documents\_list = json.loads(documents\_json) llama\_documents = \[\] for document in documents\_list: # Value for metadata must be one of (str, int, float, None) document\["writers"\] = json.dumps(document\["writers"\]) document\["languages"\] = json.dumps(document\["languages"\]) document\["genres"\] = json.dumps(document\["genres"\]) document\["cast"\] = json.dumps(document\["cast"\]) document\["directors"\] = json.dumps(document\["directors"\]) document\["countries"\] = json.dumps(document\["countries"\]) document\["imdb"\] = json.dumps(document\["imdb"\]) document\["awards"\] = json.dumps(document\["awards"\]) # Create a Document object with the text and excluded metadata for llm and embedding models llama\_document = Document( text=document\["fullplot"\], metadata=document, excluded\_llm\_metadata\_keys=\["fullplot", "metacritic"\], excluded\_embed\_metadata\_keys=\[ "fullplot", "metacritic", "poster", "num\_mflix\_comments", "runtime", "rated", \], metadata\_template="{key}=>{value}", text\_template="Metadata: {metadata\_str}\\n-----\\nContent: {content}", ) llama\_documents.append(llama\_document) # Observing an example of what the LLM and Embedding model receive as input print( "\\nThe LLM sees this: \\n", llama\_documents\[0\].get\_content(metadata\_mode=MetadataMode.LLM), ) print( "\\nThe Embedding model sees this: \\n", llama\_documents\[0\].get\_content(metadata\_mode=MetadataMode.EMBED), )

The LLM sees this: 
 Metadata: awards=>{"nominations": 0, "text": "1 win.", "wins": 1}
rated=>None
title=>The Perils of Pauline
writers=>\["Charles W. Goddard (screenplay)", "Basil Dickey (screenplay)", "Charles W. Goddard (novel)", "George B. Seitz", "Bertram Millhauser"\]
languages=>\["English"\]
plot=>Young Pauline is left a lot of money when her wealthy uncle dies. However, her uncle's secretary has been named as her guardian until she marries, at which time she will officially take ...
runtime=>199.0
countries=>\["USA"\]
genres=>\["Action"\]
directors=>\["Louis J. Gasnier", "Donald MacKenzie"\]
cast=>\["Pearl White", "Crane Wilbur", "Paul Panzer", "Edward Jos\\u00e8"\]
type=>movie
imdb=>{"id": 4465, "rating": 7.6, "votes": 744}
poster=>https://m.media-amazon.com/images/M/MV5BMzgxODk1Mzk2Ml5BMl5BanBnXkFtZTgwMDg0NzkwMjE@.\_V1\_SY1000\_SX677\_AL\_.jpg
num\_mflix\_comments=>0
-----
Content: Young Pauline is left a lot of money when her wealthy uncle dies. However, her uncle's secretary has been named as her guardian until she marries, at which time she will officially take possession of her inheritance. Meanwhile, her "guardian" and his confederates constantly come up with schemes to get rid of Pauline so that he can get his hands on the money himself.

The Embedding model sees this: 
 Metadata: awards=>{"nominations": 0, "text": "1 win.", "wins": 1}
title=>The Perils of Pauline
writers=>\["Charles W. Goddard (screenplay)", "Basil Dickey (screenplay)", "Charles W. Goddard (novel)", "George B. Seitz", "Bertram Millhauser"\]
languages=>\["English"\]
plot=>Young Pauline is left a lot of money when her wealthy uncle dies. However, her uncle's secretary has been named as her guardian until she marries, at which time she will officially take ...
countries=>\["USA"\]
genres=>\["Action"\]
directors=>\["Louis J. Gasnier", "Donald MacKenzie"\]
cast=>\["Pearl White", "Crane Wilbur", "Paul Panzer", "Edward Jos\\u00e8"\]
type=>movie
imdb=>{"id": 4465, "rating": 7.6, "votes": 744}
-----
Content: Young Pauline is left a lot of money when her wealthy uncle dies. However, her uncle's secretary has been named as her guardian until she marries, at which time she will officially take possession of her inheritance. Meanwhile, her "guardian" and his confederates constantly come up with schemes to get rid of Pauline so that he can get his hands on the money himself.

In \[ \]:

Copied!

llama\_documents\[0\]

llama\_documents\[0\]

In \[ \]:

Copied!

from llama\_index.core.node\_parser import SentenceSplitter

parser \= SentenceSplitter()
nodes \= parser.get\_nodes\_from\_documents(llama\_documents)

for node in nodes:
    node\_embedding \= embed\_model.get\_text\_embedding(
        node.get\_content(metadata\_mode\="all")
    )
    node.embedding \= node\_embedding

from llama\_index.core.node\_parser import SentenceSplitter parser = SentenceSplitter() nodes = parser.get\_nodes\_from\_documents(llama\_documents) for node in nodes: node\_embedding = embed\_model.get\_text\_embedding( node.get\_content(metadata\_mode="all") ) node.embedding = node\_embedding

Ensure your databse, collection and vector store index is setup on MongoDB Atlas for the collection or the following step won't work appropriately on MongoDB.

*   For assistance with database cluster setup and obtaining the URI, refer to this [guide](https://www.mongodb.com/docs/guides/atlas/cluster/) for setting up a MongoDB cluster, and this [guide](https://www.mongodb.com/docs/guides/atlas/connection-string/) to get your connection string.
    
*   Once you have successfully created a cluster, create the database and collection within the MongoDB Atlas cluster by clicking “+ Create Database”. The database will be named movies, and the collection will be named movies\_records.
    
*   Creating a vector search index within the movies\_records collection is essential for efficient document retrieval from MongoDB into our development environment. To achieve this, refer to the official [guide](https://www.mongodb.com/docs/atlas/atlas-vector-search/create-index/) on vector search index creation.
    

In \[ \]:

Copied!

import pymongo
from google.colab import userdata

def get\_mongo\_client(mongo\_uri):
    """Establish connection to the MongoDB."""
    try:
        client \= pymongo.MongoClient(mongo\_uri)
        print("Connection to MongoDB successful")
        return client
    except pymongo.errors.ConnectionFailure as e:
        print(f"Connection failed: {e}")
        return None

mongo\_uri \= userdata.get("MONGO\_URI")
if not mongo\_uri:
    print("MONGO\_URI not set in environment variables")

mongo\_client \= get\_mongo\_client(mongo\_uri)

DB\_NAME \= "movies"
COLLECTION\_NAME \= "movies\_records"

db \= mongo\_client\[DB\_NAME\]
collection \= db\[COLLECTION\_NAME\]

import pymongo from google.colab import userdata def get\_mongo\_client(mongo\_uri): """Establish connection to the MongoDB.""" try: client = pymongo.MongoClient(mongo\_uri) print("Connection to MongoDB successful") return client except pymongo.errors.ConnectionFailure as e: print(f"Connection failed: {e}") return None mongo\_uri = userdata.get("MONGO\_URI") if not mongo\_uri: print("MONGO\_URI not set in environment variables") mongo\_client = get\_mongo\_client(mongo\_uri) DB\_NAME = "movies" COLLECTION\_NAME = "movies\_records" db = mongo\_client\[DB\_NAME\] collection = db\[COLLECTION\_NAME\]

Connection to MongoDB successful

In \[ \]:

Copied!

\# To ensure we are working with a fresh collection
\# delete any existing records in the collection
collection.delete\_many({})

\# To ensure we are working with a fresh collection # delete any existing records in the collection collection.delete\_many({})

Out\[ \]:

DeleteResult({'n': 0, 'electionId': ObjectId('7fffffff000000000000000a'), 'opTime': {'ts': Timestamp(1708000722, 1), 't': 10}, 'ok': 1.0, '$clusterTime': {'clusterTime': Timestamp(1708000722, 1), 'signature': {'hash': b'\\xd8\\x1a\\xaci\\xf5EN+\\xe2\\xd1\\xb3y8.${u5P\\xf3', 'keyId': 7320226449804230661}}, 'operationTime': Timestamp(1708000722, 1)}, acknowledged=True)

In \[ \]:

Copied!

from llama\_index.vector\_stores.mongodb import MongoDBAtlasVectorSearch

vector\_store \= MongoDBAtlasVectorSearch(
    mongo\_client,
    db\_name\=DB\_NAME,
    collection\_name\=COLLECTION\_NAME,
    index\_name\="vector\_index",
)
vector\_store.add(nodes)

from llama\_index.vector\_stores.mongodb import MongoDBAtlasVectorSearch vector\_store = MongoDBAtlasVectorSearch( mongo\_client, db\_name=DB\_NAME, collection\_name=COLLECTION\_NAME, index\_name="vector\_index", ) vector\_store.add(nodes)

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, StorageContext

index \= VectorStoreIndex.from\_vector\_store(vector\_store)

from llama\_index.core import VectorStoreIndex, StorageContext index = VectorStoreIndex.from\_vector\_store(vector\_store)

In \[ \]:

Copied!

import pprint
from llama\_index.core.response.notebook\_utils import display\_response

query\_engine \= index.as\_query\_engine(similarity\_top\_k\=3)

query \= "Recommend a romantic movie suitable for the christmas season and justify your selecton"

response \= query\_engine.query(query)
display\_response(response)
pprint.pprint(response.source\_nodes)

import pprint from llama\_index.core.response.notebook\_utils import display\_response query\_engine = index.as\_query\_engine(similarity\_top\_k=3) query = "Recommend a romantic movie suitable for the christmas season and justify your selecton" response = query\_engine.query(query) display\_response(response) pprint.pprint(response.source\_nodes)

**`Final Response:`** The movie "Romancing the Stone" would be a suitable romantic movie for the Christmas season. It is a romantic adventure film that follows a romance writer who sets off on a dangerous adventure to rescue her kidnapped sister. The movie has elements of romance, adventure, and comedy, making it an entertaining choice for the holiday season. Additionally, the movie has received positive reviews and has been nominated for awards, indicating its quality.

\[NodeWithScore(node=TextNode(id\_='c6bbc236-e21d-49ab-b43d-db920b4946e6', embedding=None, metadata={'awards': '{"nominations": 2, "text": "Nominated for 1 Oscar. Another 6 wins & 2 nominations.", "wins": 7}', 'metacritic': None, 'rated': 'PG', 'fullplot': "Joan Wilder, a mousy romance novelist, receives a treasure map in the mail from her recently murdered brother-in-law. Meanwhile, her sister Elaine is kidnapped in Colombia and the two criminals responsible demand that she travel to Colombia to exchange the map for her sister. Joan does, and quickly becomes lost in the jungle after being waylayed by Zolo, a vicious and corrupt Colombian cop who will stop at nothing to obtain the map. There, she meets an irreverent soldier-of-fortune named Jack Colton who agrees to bring her back to civilization. Together, they embark upon an adventure that could be straight out of Joan's novels.", 'title': 'Romancing the Stone', 'writers': '\["Diane Thomas"\]', 'languages': '\["English", "Spanish", "French"\]', 'plot': 'A romance writer sets off to Colombia to ransom her kidnapped sister, and soon finds herself in the middle of a dangerous adventure.', 'runtime': 106.0, 'countries': '\["USA", "Mexico"\]', 'genres': '\["Action", "Adventure", "Comedy"\]', 'directors': '\["Robert Zemeckis"\]', 'cast': '\["Michael Douglas", "Kathleen Turner", "Danny DeVito", "Zack Norman"\]', 'type': 'movie', 'imdb': '{"id": 88011, "rating": 6.9, "votes": 59403}', 'poster': 'https://m.media-amazon.com/images/M/MV5BMDAwNjljMzEtMTc3Yy00NDg2LThjNDAtNjc0NGYyYjM2M2I1XkEyXkFqcGdeQXVyNDE5MTU2MDE@.\_V1\_SY1000\_SX677\_AL\_.jpg', 'num\_mflix\_comments': 0}, excluded\_embed\_metadata\_keys=\['fullplot', 'metacritic', 'poster', 'num\_mflix\_comments', 'runtime', 'rated'\], excluded\_llm\_metadata\_keys=\['fullplot', 'metacritic'\], relationships={<NodeRelationship.SOURCE: '1'>: RelatedNodeInfo(node\_id='e50144b0-96ba-4a5a-b90a-3a2419f5b380', node\_type=<ObjectType.DOCUMENT: '4'>, metadata={'awards': '{"nominations": 2, "text": "Nominated for 1 Oscar. Another 6 wins & 2 nominations.", "wins": 7}', 'metacritic': None, 'rated': 'PG', 'fullplot': "Joan Wilder, a mousy romance novelist, receives a treasure map in the mail from her recently murdered brother-in-law. Meanwhile, her sister Elaine is kidnapped in Colombia and the two criminals responsible demand that she travel to Colombia to exchange the map for her sister. Joan does, and quickly becomes lost in the jungle after being waylayed by Zolo, a vicious and corrupt Colombian cop who will stop at nothing to obtain the map. There, she meets an irreverent soldier-of-fortune named Jack Colton who agrees to bring her back to civilization. Together, they embark upon an adventure that could be straight out of Joan's novels.", 'title': 'Romancing the Stone', 'writers': '\["Diane Thomas"\]', 'languages': '\["English", "Spanish", "French"\]', 'plot': 'A romance writer sets off to Colombia to ransom her kidnapped sister, and soon finds herself in the middle of a dangerous adventure.', 'runtime': 106.0, 'countries': '\["USA", "Mexico"\]', 'genres': '\["Action", "Adventure", "Comedy"\]', 'directors': '\["Robert Zemeckis"\]', 'cast': '\["Michael Douglas", "Kathleen Turner", "Danny DeVito", "Zack Norman"\]', 'type': 'movie', 'imdb': '{"id": 88011, "rating": 6.9, "votes": 59403}', 'poster': 'https://m.media-amazon.com/images/M/MV5BMDAwNjljMzEtMTc3Yy00NDg2LThjNDAtNjc0NGYyYjM2M2I1XkEyXkFqcGdeQXVyNDE5MTU2MDE@.\_V1\_SY1000\_SX677\_AL\_.jpg', 'num\_mflix\_comments': 0}, hash='b984e4f203b7b67eae14afa890718adb800a5816661ac2edf412aa96fd7dc10b'), <NodeRelationship.PREVIOUS: '2'>: RelatedNodeInfo(node\_id='f895e43a-038a-4a1c-8a82-0e22868e35d7', node\_type=<ObjectType.TEXT: '1'>, metadata={'awards': '{"nominations": 1, "text": "1 nomination.", "wins": 0}', 'metacritic': None, 'rated': 'R', 'fullplot': "Chicago psychiatrist Judd Stevens (Roger Moore) is suspected of murdering one of his patients when the man turns up stabbed to death in the middle of the city. After repeated attempts to convince cops Rod Steiger and Elliott Gould of his innocence, Dr.Stevens is forced to go after the real villains himself, and he finds himself up against one of the city's most notorious Mafia kingpins.", 'title': 'The Naked Face', 'writers': '\["Bryan Forbes", "Sidney Sheldon (novel)"\]', 'languages': '\["English"\]', 'plot': 'Chicago psychiatrist Judd Stevens (Roger Moore) is suspected of murdering one of his patients when the man turns up stabbed to death in the middle of the city. After repeated attempts to ...', 'runtime': 103.0, 'countries': '\["USA"\]', 'genres': '\["Action", "Mystery", "Thriller"\]', 'directors': '\["Bryan Forbes"\]', 'cast': '\["Roger Moore", "Rod Steiger", "Elliott Gould", "Art Carney"\]', 'type': 'movie', 'imdb': '{"id": 87777, "rating": 5.3, "votes": 654}', 'poster': 'https://m.media-amazon.com/images/M/MV5BMTg0NDM4MTY0NV5BMl5BanBnXkFtZTcwNTcwOTc2NA@@.\_V1\_SY1000\_SX677\_AL\_.jpg', 'num\_mflix\_comments': 1}, hash='066e2b3d12c5fab61175f52dd625ec41fb1fce1fe6fe4c892774227c576fdbbd'), <NodeRelationship.NEXT: '3'>: RelatedNodeInfo(node\_id='e31f1142-c6b6-4183-b14b-1634166b9d1f', node\_type=<ObjectType.TEXT: '1'>, metadata={}, hash='9b9127e21d18792749a7a35321e04d29b8d77f7b454b0133205f9de1090038b4')}, text="Joan Wilder, a mousy romance novelist, receives a treasure map in the mail from her recently murdered brother-in-law. Meanwhile, her sister Elaine is kidnapped in Colombia and the two criminals responsible demand that she travel to Colombia to exchange the map for her sister. Joan does, and quickly becomes lost in the jungle after being waylayed by Zolo, a vicious and corrupt Colombian cop who will stop at nothing to obtain the map. There, she meets an irreverent soldier-of-fortune named Jack Colton who agrees to bring her back to civilization. Together, they embark upon an adventure that could be straight out of Joan's novels.", start\_char\_idx=0, end\_char\_idx=635, text\_template='Metadata: {metadata\_str}\\n-----\\nContent: {content}', metadata\_template='{key}=>{value}', metadata\_seperator='\\n'), score=0.7502920627593994),
 NodeWithScore(node=TextNode(id\_='5c7cef95-79e3-4c96-a009-4154ea125240', embedding=None, metadata={'awards': '{"nominations": 2, "text": "Nominated for 2 Oscars. Another 1 win & 2 nominations.", "wins": 3}', 'metacritic': 64.0, 'rated': 'PG-13', 'fullplot': 'In 1880, four men travel together to the city of Silverado. They come across with many dangers before they finally engage the "bad guys" and bring peace and equality back to the city.', 'title': 'Silverado', 'writers': '\["Lawrence Kasdan", "Mark Kasdan"\]', 'languages': '\["English"\]', 'plot': 'A misfit bunch of friends come together to right the injustices which exist in a small town.', 'runtime': 133.0, 'countries': '\["USA"\]', 'genres': '\["Action", "Crime", "Drama"\]', 'directors': '\["Lawrence Kasdan"\]', 'cast': '\["Kevin Kline", "Scott Glenn", "Kevin Costner", "Danny Glover"\]', 'type': 'movie', 'imdb': '{"id": 90022, "rating": 7.2, "votes": 26415}', 'poster': 'https://m.media-amazon.com/images/M/MV5BYTljNTE5YmUtMGEyZi00ZjI4LWEzYjUtZDY2YWEwNzVmZjRkXkEyXkFqcGdeQXVyNTI4MjkwNjA@.\_V1\_SY1000\_SX677\_AL\_.jpg', 'num\_mflix\_comments': 1}, excluded\_embed\_metadata\_keys=\['fullplot', 'metacritic', 'poster', 'num\_mflix\_comments', 'runtime', 'rated'\], excluded\_llm\_metadata\_keys=\['fullplot', 'metacritic'\], relationships={<NodeRelationship.SOURCE: '1'>: RelatedNodeInfo(node\_id='decbc30c-c17e-4ba4-bd1e-72dce4ce383a', node\_type=<ObjectType.DOCUMENT: '4'>, metadata={'awards': '{"nominations": 2, "text": "Nominated for 2 Oscars. Another 1 win & 2 nominations.", "wins": 3}', 'metacritic': 64.0, 'rated': 'PG-13', 'fullplot': 'In 1880, four men travel together to the city of Silverado. They come across with many dangers before they finally engage the "bad guys" and bring peace and equality back to the city.', 'title': 'Silverado', 'writers': '\["Lawrence Kasdan", "Mark Kasdan"\]', 'languages': '\["English"\]', 'plot': 'A misfit bunch of friends come together to right the injustices which exist in a small town.', 'runtime': 133.0, 'countries': '\["USA"\]', 'genres': '\["Action", "Crime", "Drama"\]', 'directors': '\["Lawrence Kasdan"\]', 'cast': '\["Kevin Kline", "Scott Glenn", "Kevin Costner", "Danny Glover"\]', 'type': 'movie', 'imdb': '{"id": 90022, "rating": 7.2, "votes": 26415}', 'poster': 'https://m.media-amazon.com/images/M/MV5BYTljNTE5YmUtMGEyZi00ZjI4LWEzYjUtZDY2YWEwNzVmZjRkXkEyXkFqcGdeQXVyNTI4MjkwNjA@.\_V1\_SY1000\_SX677\_AL\_.jpg', 'num\_mflix\_comments': 1}, hash='80b77d835c7dfad9d57d300cf69ba388704e6f282f49dc23106489db03b8b441'), <NodeRelationship.PREVIOUS: '2'>: RelatedNodeInfo(node\_id='1c04fb7f-ff8f-4e8c-84f6-74c57251446a', node\_type=<ObjectType.TEXT: '1'>, metadata={'awards': '{"nominations": 5, "text": "Nominated for 3 Oscars. Another 2 wins & 5 nominations.", "wins": 5}', 'metacritic': None, 'rated': 'R', 'fullplot': 'A hardened convict and a younger prisoner escape from a brutal prison in the middle of winter only to find themselves on an out-of-control train with a female railway worker while being pursued by the vengeful head of security.', 'title': 'Runaway Train', 'writers': '\["Djordje Milicevic (screenplay)", "Paul Zindel (screenplay)", "Edward Bunker (screenplay)", "Akira Kurosawa (based on a screenplay by)"\]', 'languages': '\["English"\]', 'plot': 'Two escaped convicts and a female railway worker find themselves trapped on a train with no brakes and nobody driving.', 'runtime': 111.0, 'countries': '\["USA"\]', 'genres': '\["Action", "Adventure", "Drama"\]', 'directors': '\["Andrey Konchalovskiy"\]', 'cast': '\["Jon Voight", "Eric Roberts", "Rebecca De Mornay", "Kyle T. Heffner"\]', 'type': 'movie', 'imdb': '{"id": 89941, "rating": 7.3, "votes": 19652}', 'poster': 'https://m.media-amazon.com/images/M/MV5BODQyYWU1NGUtNjEzYS00YmNhLTk1YWEtZDdlZGQzMTI4MTI1XkEyXkFqcGdeQXVyMTQxNzMzNDI@.\_V1\_SY1000\_SX677\_AL\_.jpg', 'num\_mflix\_comments': 0}, hash='378c16de972df97080db94775cd46e57f6a0dd5a7472b357e0285eed2e3b7775'), <NodeRelationship.NEXT: '3'>: RelatedNodeInfo(node\_id='5df9410b-6597-45f4-95d5-fee1db8737b1', node\_type=<ObjectType.TEXT: '1'>, metadata={}, hash='77e93faace9b0e102635d3ca997ff27bc03dbba66eaa2d830f0634289d16d927')}, text='In 1880, four men travel together to the city of Silverado. They come across with many dangers before they finally engage the "bad guys" and bring peace and equality back to the city.', start\_char\_idx=0, end\_char\_idx=183, text\_template='Metadata: {metadata\_str}\\n-----\\nContent: {content}', metadata\_template='{key}=>{value}', metadata\_seperator='\\n'), score=0.7419796586036682),
 NodeWithScore(node=TextNode(id\_='ff28e815-5db5-4963-a9b8-99c64716eb00', embedding=None, metadata={'awards': '{"nominations": 1, "text": "1 nomination.", "wins": 0}', 'metacritic': None, 'rated': 'PASSED', 'fullplot': "Dick Powell stars as Haven, a government private investigator assigned to investigate the murders of two cavalrymen. Travelling incognito, Haven arrives in a small frontier outpost, where saloon singer Charlie controls all illegal activities. After making short work of Charlie's burly henchman, Haven gets a job at her gambling emporium, biding his time and gathering evidence against the gorgeous crime chieftain Cast as a philosophical bartender, Burl Ives is afforded at least one opportunity to sing.", 'title': 'Station West', 'writers': '\["Frank Fenton (screenplay)", "Winston Miller (screenplay)", "Luke Short (novel)"\]', 'languages': '\["English"\]', 'plot': 'When two US cavalrymen transporting a gold shipment get killed, US Army Intelligence investigator John Haven goes undercover to a mining and logging town to find the killers.', 'runtime': 87.0, 'countries': '\["USA"\]', 'genres': '\["Action", "Mystery", "Romance"\]', 'directors': '\["Sidney Lanfield"\]', 'cast': '\["Dick Powell", "Jane Greer", "Agnes Moorehead", "Burl Ives"\]', 'type': 'movie', 'imdb': '{"id": 40835, "rating": 6.8, "votes": 578}', 'poster': 'https://m.media-amazon.com/images/M/MV5BN2U3YWJjOWItOWY3Yy00NTMxLTkxMGUtOTQ1MzEzODM2MjRjXkEyXkFqcGdeQXVyNTk1MTk0MDI@.\_V1\_SY1000\_SX677\_AL\_.jpg', 'num\_mflix\_comments': 1}, excluded\_embed\_metadata\_keys=\['fullplot', 'metacritic', 'poster', 'num\_mflix\_comments', 'runtime', 'rated'\], excluded\_llm\_metadata\_keys=\['fullplot', 'metacritic'\], relationships={<NodeRelationship.SOURCE: '1'>: RelatedNodeInfo(node\_id='b04254ab-2edb-47c1-9412-646575747ca8', node\_type=<ObjectType.DOCUMENT: '4'>, metadata={'awards': '{"nominations": 1, "text": "1 nomination.", "wins": 0}', 'metacritic': None, 'rated': 'PASSED', 'fullplot': "Dick Powell stars as Haven, a government private investigator assigned to investigate the murders of two cavalrymen. Travelling incognito, Haven arrives in a small frontier outpost, where saloon singer Charlie controls all illegal activities. After making short work of Charlie's burly henchman, Haven gets a job at her gambling emporium, biding his time and gathering evidence against the gorgeous crime chieftain Cast as a philosophical bartender, Burl Ives is afforded at least one opportunity to sing.", 'title': 'Station West', 'writers': '\["Frank Fenton (screenplay)", "Winston Miller (screenplay)", "Luke Short (novel)"\]', 'languages': '\["English"\]', 'plot': 'When two US cavalrymen transporting a gold shipment get killed, US Army Intelligence investigator John Haven goes undercover to a mining and logging town to find the killers.', 'runtime': 87.0, 'countries': '\["USA"\]', 'genres': '\["Action", "Mystery", "Romance"\]', 'directors': '\["Sidney Lanfield"\]', 'cast': '\["Dick Powell", "Jane Greer", "Agnes Moorehead", "Burl Ives"\]', 'type': 'movie', 'imdb': '{"id": 40835, "rating": 6.8, "votes": 578}', 'poster': 'https://m.media-amazon.com/images/M/MV5BN2U3YWJjOWItOWY3Yy00NTMxLTkxMGUtOTQ1MzEzODM2MjRjXkEyXkFqcGdeQXVyNTk1MTk0MDI@.\_V1\_SY1000\_SX677\_AL\_.jpg', 'num\_mflix\_comments': 1}, hash='90f541ac96dcffa4ac639e6ac25da415471164bf8d7930a29b6aed406d631ede'), <NodeRelationship.PREVIOUS: '2'>: RelatedNodeInfo(node\_id='a48d8737-8615-48c1-9d4a-1ee127e34fb9', node\_type=<ObjectType.TEXT: '1'>, metadata={'awards': '{"nominations": 1, "text": "1 nomination.", "wins": 0}', 'metacritic': None, 'rated': 'PASSED', 'fullplot': 'Jefty, owner of a roadhouse in a backwoods town, hires sultry, tough-talking torch singer Lily Stevens against the advice of his manager Pete Morgan. Jefty is smitten with Lily, who in turn exerts her charms on the more resistant Pete. When Pete finally falls for her and she turns down Jefty\\'s marriage proposal, they must face Jefty\\'s murderous jealousy and his twisted plots to "punish" the two.', 'title': 'Road House', 'writers': '\["Edward Chodorov (screen play)", "Margaret Gruen (story)", "Oscar Saul (story)"\]', 'languages': '\["English"\]', 'plot': 'A night club owner becomes infatuated with a torch singer and frames his best friend/manager for embezzlement when the chanteuse falls in love with him.', 'runtime': 95.0, 'countries': '\["USA"\]', 'genres': '\["Action", "Drama", "Film-Noir"\]', 'directors': '\["Jean Negulesco"\]', 'cast': '\["Ida Lupino", "Cornel Wilde", "Celeste Holm", "Richard Widmark"\]', 'type': 'movie', 'imdb': '{"id": 40740, "rating": 7.3, "votes": 1353}', 'poster': 'https://m.media-amazon.com/images/M/MV5BMjc1ZTNkM2UtYzY3Yi00ZWZmLTljYmEtNjYxZDNmYzk2ZjkzXkEyXkFqcGdeQXVyMjUxODE0MDY@.\_V1\_SY1000\_SX677\_AL\_.jpg', 'num\_mflix\_comments': 2}, hash='040b4a77fcc8fbb5347620e99a217d67b85dcdbd370d91bd23877722a499079f'), <NodeRelationship.NEXT: '3'>: RelatedNodeInfo(node\_id='75f37fbc-d75e-4a76-b86f-f15d9260afd1', node\_type=<ObjectType.TEXT: '1'>, metadata={}, hash='9941706d03783561f3fc3200c26527493a62307f8532dcda60b20948c886b330')}, text="Dick Powell stars as Haven, a government private investigator assigned to investigate the murders of two cavalrymen. Travelling incognito, Haven arrives in a small frontier outpost, where saloon singer Charlie controls all illegal activities. After making short work of Charlie's burly henchman, Haven gets a job at her gambling emporium, biding his time and gathering evidence against the gorgeous crime chieftain Cast as a philosophical bartender, Burl Ives is afforded at least one opportunity to sing.", start\_char\_idx=0, end\_char\_idx=505, text\_template='Metadata: {metadata\_str}\\n-----\\nContent: {content}', metadata\_template='{key}=>{value}', metadata\_seperator='\\n'), score=0.7337073087692261)\]

Back to top

[Previous now make sure you create the search index with the right name here](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MongoDBAtlasVectorSearchRAGFireworks/)[Next MyScale Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MyScaleIndexDemo/)
