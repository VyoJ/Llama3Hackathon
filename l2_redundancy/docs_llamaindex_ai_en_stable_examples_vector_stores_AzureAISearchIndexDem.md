Title: Azure AI Search - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureAISearchIndexDemo/

Markdown Content:
Azure AI Search - LlamaIndex


Basic Example[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureAISearchIndexDemo/#basic-example)
-------------------------------------------------------------------------------------------------------------------

In this notebook, we take a Paul Graham essay, split it into chunks, embed it using an Azure OpenAI embedding model, load it into an Azure AI Search index, and then query it.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

!pip install llama\-index
!pip install wget
%pip install llama\-index\-vector\-stores\-azureaisearch
%pip install azure\-search\-documents\11.4.0 %llama-index-embeddings-azure-openai %llama-index-llms-azure-openai

In \[ \]:

Copied!

import logging
import sys
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from IPython.display import Markdown, display
from llama\_index.core import (
    SimpleDirectoryReader,
    StorageContext,
    VectorStoreIndex,
)
from llama\_index.core.settings import Settings

from llama\_index.llms.azure\_openai import AzureOpenAI
from llama\_index.embeddings.azure\_openai import AzureOpenAIEmbedding
from llama\_index.vector\_stores.azureaisearch import AzureAISearchVectorStore
from llama\_index.vector\_stores.azureaisearch import (
    IndexManagement,
    MetadataIndexFieldType,
)

import logging import sys from azure.core.credentials import AzureKeyCredential from azure.search.documents import SearchClient from azure.search.documents.indexes import SearchIndexClient from IPython.display import Markdown, display from llama\_index.core import ( SimpleDirectoryReader, StorageContext, VectorStoreIndex, ) from llama\_index.core.settings import Settings from llama\_index.llms.azure\_openai import AzureOpenAI from llama\_index.embeddings.azure\_openai import AzureOpenAIEmbedding from llama\_index.vector\_stores.azureaisearch import AzureAISearchVectorStore from llama\_index.vector\_stores.azureaisearch import ( IndexManagement, MetadataIndexFieldType, )

Setup Azure OpenAI[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureAISearchIndexDemo/#setup-azure-openai)
-----------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

aoai\_api\_key \= "YOUR\_AZURE\_OPENAI\_API\_KEY"
aoai\_endpoint \= "YOUR\_AZURE\_OPENAI\_ENDPOINT"
aoai\_api\_version \= "2023-05-15"

llm \= AzureOpenAI(
    model\="YOUR\_AZURE\_OPENAI\_COMPLETION\_MODEL\_NAME",
    deployment\_name\="YOUR\_AZURE\_OPENAI\_COMPLETION\_DEPLOYMENT\_NAME",
    api\_key\=aoai\_api\_key,
    azure\_endpoint\=aoai\_endpoint,
    api\_version\=aoai\_api\_version,
)

\# You need to deploy your own embedding model as well as your own chat completion model
embed\_model \= AzureOpenAIEmbedding(
    model\="YOUR\_AZURE\_OPENAI\_EMBEDDING\_MODEL\_NAME",
    deployment\_name\="YOUR\_AZURE\_OPENAI\_EMBEDDING\_DEPLOYMENT\_NAME",
    api\_key\=aoai\_api\_key,
    azure\_endpoint\=aoai\_endpoint,
    api\_version\=aoai\_api\_version,
)

aoai\_api\_key = "YOUR\_AZURE\_OPENAI\_API\_KEY" aoai\_endpoint = "YOUR\_AZURE\_OPENAI\_ENDPOINT" aoai\_api\_version = "2023-05-15" llm = AzureOpenAI( model="YOUR\_AZURE\_OPENAI\_COMPLETION\_MODEL\_NAME", deployment\_name="YOUR\_AZURE\_OPENAI\_COMPLETION\_DEPLOYMENT\_NAME", api\_key=aoai\_api\_key, azure\_endpoint=aoai\_endpoint, api\_version=aoai\_api\_version, ) # You need to deploy your own embedding model as well as your own chat completion model embed\_model = AzureOpenAIEmbedding( model="YOUR\_AZURE\_OPENAI\_EMBEDDING\_MODEL\_NAME", deployment\_name="YOUR\_AZURE\_OPENAI\_EMBEDDING\_DEPLOYMENT\_NAME", api\_key=aoai\_api\_key, azure\_endpoint=aoai\_endpoint, api\_version=aoai\_api\_version, )

Setup Azure AI Search[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureAISearchIndexDemo/#setup-azure-ai-search)
-----------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

search\_service\_api\_key \= "YOUR-AZURE-SEARCH-SERVICE-ADMIN-KEY"
search\_service\_endpoint \= "YOUR-AZURE-SEARCH-SERVICE-ENDPOINT"
search\_service\_api\_version \= "2023-11-01"
credential \= AzureKeyCredential(search\_service\_api\_key)

\# Index name to use
index\_name \= "llamaindex-vector-demo"

\# Use index client to demonstrate creating an index
index\_client \= SearchIndexClient(
    endpoint\=search\_service\_endpoint,
    credential\=credential,
)

\# Use search client to demonstration using existing index
search\_client \= SearchClient(
    endpoint\=search\_service\_endpoint,
    index\_name\=index\_name,
    credential\=credential,
)

search\_service\_api\_key = "YOUR-AZURE-SEARCH-SERVICE-ADMIN-KEY" search\_service\_endpoint = "YOUR-AZURE-SEARCH-SERVICE-ENDPOINT" search\_service\_api\_version = "2023-11-01" credential = AzureKeyCredential(search\_service\_api\_key) # Index name to use index\_name = "llamaindex-vector-demo" # Use index client to demonstrate creating an index index\_client = SearchIndexClient( endpoint=search\_service\_endpoint, credential=credential, ) # Use search client to demonstration using existing index search\_client = SearchClient( endpoint=search\_service\_endpoint, index\_name=index\_name, credential=credential, )

Create Index (if it does not exist)[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureAISearchIndexDemo/#create-index-if-it-does-not-exist)
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Demonstrates creating a vector index named "llamaindex-vector-demo" if one doesn't exist. The index has the following fields:

| Field Name | OData Type |
| --- | --- |
| id | `Edm.String` |
| chunk | `Edm.String` |
| embedding | `Collection(Edm.Single)` |
| metadata | `Edm.String` |
| doc\_id | `Edm.String` |
| author | `Edm.String` |
| theme | `Edm.String` |
| director | `Edm.String` |

In \[ \]:

Copied!

metadata\_fields \= {
    "author": "author",
    "theme": ("topic", MetadataIndexFieldType.STRING),
    "director": "director",
}

vector\_store \= AzureAISearchVectorStore(
    search\_or\_index\_client\=index\_client,
    filterable\_metadata\_field\_keys\=metadata\_fields,
    index\_name\=index\_name,
    index\_management\=IndexManagement.CREATE\_IF\_NOT\_EXISTS,
    id\_field\_key\="id",
    chunk\_field\_key\="chunk",
    embedding\_field\_key\="embedding",
    embedding\_dimensionality\=1536,
    metadata\_string\_field\_key\="metadata",
    doc\_id\_field\_key\="doc\_id",
    language\_analyzer\="en.lucene",
    vector\_algorithm\_type\="exhaustiveKnn",
)

metadata\_fields = { "author": "author", "theme": ("topic", MetadataIndexFieldType.STRING), "director": "director", } vector\_store = AzureAISearchVectorStore( search\_or\_index\_client=index\_client, filterable\_metadata\_field\_keys=metadata\_fields, index\_name=index\_name, index\_management=IndexManagement.CREATE\_IF\_NOT\_EXISTS, id\_field\_key="id", chunk\_field\_key="chunk", embedding\_field\_key="embedding", embedding\_dimensionality=1536, metadata\_string\_field\_key="metadata", doc\_id\_field\_key="doc\_id", language\_analyzer="en.lucene", vector\_algorithm\_type="exhaustiveKnn", )

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

### Loading documents[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureAISearchIndexDemo/#loading-documents)

Load the documents stored in the `data/paul_graham/` using the SimpleDirectoryReader

In \[ \]:

Copied!

\# Load documents
documents \= SimpleDirectoryReader("../data/paul\_graham/").load\_data()
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

Settings.llm \= llm
Settings.embed\_model \= embed\_model
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

\# Load documents documents = SimpleDirectoryReader("../data/paul\_graham/").load\_data() storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) Settings.llm = llm Settings.embed\_model = embed\_model index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

In \[ \]:

Copied!

\# Query Data
query\_engine \= index.as\_query\_engine(similarity\_top\_k\=3)
response \= query\_engine.query("What did the author do growing up?")
display(Markdown(f"<b>{response}</b>"))

\# Query Data query\_engine = index.as\_query\_engine(similarity\_top\_k=3) response = query\_engine.query("What did the author do growing up?") display(Markdown(f"**{response}**"))

**The author engaged in writing and programming activities during their formative years. They initially wrote short stories and later transitioned to programming on the IBM 1401 using an early version of Fortran. Subsequently, with the advent of microcomputers, the author began programming on a TRS-80, writing simple games, a rocket flight prediction program, and a word processor.**

In \[ \]:

Copied!

response \= query\_engine.query(
    "What did the author learn?",
)
display(Markdown(f"<b>{response}</b>"))

response = query\_engine.query( "What did the author learn?", ) display(Markdown(f"**{response}**"))

**The author learned that the study of philosophy in college did not live up to their expectations, as they found the courses to be boring and lacking in ultimate truths. This led them to switch their focus to AI, which was influenced by a novel featuring an intelligent computer and a PBS documentary showcasing advanced technology.**

Use Existing Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureAISearchIndexDemo/#use-existing-index)
-----------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

index\_name \= "llamaindex-vector-demo"

metadata\_fields \= {
    "author": "author",
    "theme": ("topic", MetadataIndexFieldType.STRING),
    "director": "director",
}
vector\_store \= AzureAISearchVectorStore(
    search\_or\_index\_client\=search\_client,
    filterable\_metadata\_field\_keys\=metadata\_fields,
    index\_management\=IndexManagement.VALIDATE\_INDEX,
    id\_field\_key\="id",
    chunk\_field\_key\="chunk",
    embedding\_field\_key\="embedding",
    embedding\_dimensionality\=1536,
    metadata\_string\_field\_key\="metadata",
    doc\_id\_field\_key\="doc\_id",
)

index\_name = "llamaindex-vector-demo" metadata\_fields = { "author": "author", "theme": ("topic", MetadataIndexFieldType.STRING), "director": "director", } vector\_store = AzureAISearchVectorStore( search\_or\_index\_client=search\_client, filterable\_metadata\_field\_keys=metadata\_fields, index\_management=IndexManagement.VALIDATE\_INDEX, id\_field\_key="id", chunk\_field\_key="chunk", embedding\_field\_key="embedding", embedding\_dimensionality=1536, metadata\_string\_field\_key="metadata", doc\_id\_field\_key="doc\_id", )

In \[ \]:

Copied!

storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    \[\],
    storage\_context\=storage\_context,
)

storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( \[\], storage\_context=storage\_context, )

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What was a hard moment for the author?")
display(Markdown(f"<b>{response}</b>"))

query\_engine = index.as\_query\_engine() response = query\_engine.query("What was a hard moment for the author?") display(Markdown(f"**{response}**"))

**The author faced a challenging moment when he couldn't figure out what to do with the early computer he had access to in 9th grade. This was due to the limited options for input and the lack of knowledge in math to do anything interesting with the available resources.**

In \[ \]:

Copied!

response \= query\_engine.query("Who is the author?")
display(Markdown(f"<b>{response}</b>"))

response = query\_engine.query("Who is the author?") display(Markdown(f"**{response}**"))

**Paul Graham**

In \[ \]:

Copied!

import time

query\_engine \= index.as\_query\_engine(streaming\=True)
response \= query\_engine.query("What happened at interleaf?")

start\_time \= time.time()

token\_count \= 0
for token in response.response\_gen:
    print(token, end\="")
    token\_count += 1

time\_elapsed \= time.time() \- start\_time
tokens\_per\_second \= token\_count / time\_elapsed

print(f"\\n\\nStreamed output at {tokens\_per\_second} tokens/s")

import time query\_engine = index.as\_query\_engine(streaming=True) response = query\_engine.query("What happened at interleaf?") start\_time = time.time() token\_count = 0 for token in response.response\_gen: print(token, end="") token\_count += 1 time\_elapsed = time.time() - start\_time tokens\_per\_second = token\_count / time\_elapsed print(f"\\n\\nStreamed output at {tokens\_per\_second} tokens/s")

The author worked at Interleaf, where they learned several lessons, including the importance of product-focused leadership in technology companies, the drawbacks of code being edited by too many people, the limitations of conventional office hours for optimal hacking, and the risks associated with bureaucratic customers. Additionally, the author discovered the concept that the low end tends to dominate the high end, and that being the "entry level" option can be advantageous.

Streamed output at 99.40073103089465 tokens/s

Adding a document to existing index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureAISearchIndexDemo/#adding-a-document-to-existing-index)
---------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

response \= query\_engine.query("What colour is the sky?")
display(Markdown(f"<b>{response}</b>"))

response = query\_engine.query("What colour is the sky?") display(Markdown(f"**{response}**"))

**Blue**

In \[ \]:

Copied!

from llama\_index.core import Document

index.insert\_nodes(\[Document(text\="The sky is indigo today")\])

from llama\_index.core import Document index.insert\_nodes(\[Document(text="The sky is indigo today")\])

In \[ \]:

Copied!

response \= query\_engine.query("What colour is the sky?")
display(Markdown(f"<b>{response}</b>"))

response = query\_engine.query("What colour is the sky?") display(Markdown(f"**{response}**"))

**The sky is indigo today.**

Filtering[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureAISearchIndexDemo/#filtering)
-----------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core.schema import TextNode

nodes \= \[
    TextNode(
        text\="The Shawshank Redemption",
        metadata\={
            "author": "Stephen King",
            "theme": "Friendship",
        },
    ),
    TextNode(
        text\="The Godfather",
        metadata\={
            "director": "Francis Ford Coppola",
            "theme": "Mafia",
        },
    ),
    TextNode(
        text\="Inception",
        metadata\={
            "director": "Christopher Nolan",
        },
    ),
\]

from llama\_index.core.schema import TextNode nodes = \[ TextNode( text="The Shawshank Redemption", metadata={ "author": "Stephen King", "theme": "Friendship", }, ), TextNode( text="The Godfather", metadata={ "director": "Francis Ford Coppola", "theme": "Mafia", }, ), TextNode( text="Inception", metadata={ "director": "Christopher Nolan", }, ), \]

In \[ \]:

Copied!

index.insert\_nodes(nodes)

index.insert\_nodes(nodes)

In \[ \]:

Copied!

from llama\_index.core.vector\_stores.types import (
    MetadataFilters,
    ExactMatchFilter,
)

filters \= MetadataFilters(
    filters\=\[ExactMatchFilter(key\="theme", value\="Mafia")\]
)

retriever \= index.as\_retriever(filters\=filters)
retriever.retrieve("What is inception about?")

from llama\_index.core.vector\_stores.types import ( MetadataFilters, ExactMatchFilter, ) filters = MetadataFilters( filters=\[ExactMatchFilter(key="theme", value="Mafia")\] ) retriever = index.as\_retriever(filters=filters) retriever.retrieve("What is inception about?")

Out\[ \]:

\[NodeWithScore(node=TextNode(id\_='049f00de-13be-4af3-ab56-8c16352fe799', embedding=None, metadata={'director': 'Francis Ford Coppola', 'theme': 'Mafia'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, hash='ad2a08d4364262546db9711b915348d43e0ccc41bd8c3c41775e133624e1fa1b', text='The Godfather', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.8120511)\]

Query Mode[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureAISearchIndexDemo/#query-mode)
-------------------------------------------------------------------------------------------------------------

Four query modes are supported: DEFAULT (vector search), SPARSE, HYBRID, and SEMANTIC\_HYBRID.

### Perform a Vector Search[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureAISearchIndexDemo/#perform-a-vector-search)

In \[ \]:

Copied!

from llama\_index.core.vector\_stores.types import VectorStoreQueryMode

default\_retriever \= index.as\_retriever(
    vector\_store\_query\_mode\=VectorStoreQueryMode.DEFAULT
)
response \= default\_retriever.retrieve("What is inception about?")

\# Loop through each NodeWithScore in the response
for node\_with\_score in response:
    node \= node\_with\_score.node  \# The TextNode object
    score \= node\_with\_score.score  \# The similarity score
    chunk\_id \= node.id\_  \# The chunk ID

    \# Extract the relevant metadata from the node
    file\_name \= node.metadata.get("file\_name", "Unknown")
    file\_path \= node.metadata.get("file\_path", "Unknown")

    \# Extract the text content from the node
    text\_content \= node.text if node.text else "No content available"

    \# Print the results in a user-friendly format
    print(f"Score: {score}")
    print(f"File Name: {file\_name}")
    print(f"Id: {chunk\_id}")
    print("\\nExtracted Content:")
    print(text\_content)
    print("\\n" + "=" \* 40 + " End of Result " + "=" \* 40 + "\\n")

from llama\_index.core.vector\_stores.types import VectorStoreQueryMode default\_retriever = index.as\_retriever( vector\_store\_query\_mode=VectorStoreQueryMode.DEFAULT ) response = default\_retriever.retrieve("What is inception about?") # Loop through each NodeWithScore in the response for node\_with\_score in response: node = node\_with\_score.node # The TextNode object score = node\_with\_score.score # The similarity score chunk\_id = node.id\_ # The chunk ID # Extract the relevant metadata from the node file\_name = node.metadata.get("file\_name", "Unknown") file\_path = node.metadata.get("file\_path", "Unknown") # Extract the text content from the node text\_content = node.text if node.text else "No content available" # Print the results in a user-friendly format print(f"Score: {score}") print(f"File Name: {file\_name}") print(f"Id: {chunk\_id}") print("\\nExtracted Content:") print(text\_content) print("\\n" + "=" \* 40 + " End of Result " + "=" \* 40 + "\\n")

Score: 0.8748552
File Name: Unknown
Id: bae0df75-ff37-4725-b659-b9fd8bf2ef3c

Extracted Content:
Inception



Score: 0.8155207
File Name: paul\_graham\_essay.txt
Id: ae5aee85-a083-4141-bf75-bbb872f53760

Extracted Content:
It's not that unprestigious types of work are good per se. But when you find yourself drawn to some kind of work despite its current lack of prestige, it's a sign both that there's something real to be discovered there, and that you have the right kind of motives. Impure motives are a big danger for the ambitious. If anything is going to lead you astray, it will be the desire to impress people. So while working on things that aren't prestigious doesn't guarantee you're on the right track, it at least guarantees you're not on the most common type of wrong one.

Over the next several years I wrote lots of essays about all kinds of different topics. O'Reilly reprinted a collection of them as a book, called Hackers & Painters after one of the essays in it. I also worked on spam filters, and did some more painting. I used to have dinners for a group of friends every thursday night, which taught me how to cook for groups. And I bought another building in Cambridge, a former candy factory (and later, twas said, porn studio), to use as an office.

One night in October 2003 there was a big party at my house. It was a clever idea of my friend Maria Daniels, who was one of the thursday diners. Three separate hosts would all invite their friends to one party. So for every guest, two thirds of the other guests would be people they didn't know but would probably like. One of the guests was someone I didn't know but would turn out to like a lot: a woman called Jessica Livingston. A couple days later I asked her out.

Jessica was in charge of marketing at a Boston investment bank. This bank thought it understood startups, but over the next year, as she met friends of mine from the startup world, she was surprised how different reality was. And how colorful their stories were. So she decided to compile a book of interviews with startup founders.

When the bank had financial problems and she had to fire half her staff, she started looking for a new job. In early 2005 she interviewed for a marketing job at a Boston VC firm. It took them weeks to make up their minds, and during this time I started telling her about all the things that needed to be fixed about venture capital. They should make a larger number of smaller investments instead of a handful of giant ones, they should be funding younger, more technical founders instead of MBAs, they should let the founders remain as CEO, and so on.

One of my tricks for writing essays had always been to give talks. The prospect of having to stand up in front of a group of people and tell them something that won't waste their time is a great spur to the imagination. When the Harvard Computer Society, the undergrad computer club, asked me to give a talk, I decided I would tell them how to start a startup. Maybe they'd be able to avoid the worst of the mistakes we'd made.

So I gave this talk, in the course of which I told them that the best sources of seed funding were successful startup founders, because then they'd be sources of advice too. Whereupon it seemed they were all looking expectantly at me. Horrified at the prospect of having my inbox flooded by business plans (if I'd only known), I blurted out "But not me!" and went on with the talk. But afterward it occurred to me that I should really stop procrastinating about angel investing. I'd been meaning to since Yahoo bought us, and now it was 7 years later and I still hadn't done one angel investment.

Meanwhile I had been scheming with Robert and Trevor about projects we could work on together. I missed working with them, and it seemed like there had to be something we could collaborate on.

As Jessica and I were walking home from dinner on March 11, at the corner of Garden and Walker streets, these three threads converged. Screw the VCs who were taking so long to make up their minds. We'd start our own investment firm and actually implement the ideas we'd been talking about. I'd fund it, and Jessica could quit her job and work for it, and we'd get Robert and Trevor as partners too. \[13\]

Once again, ignorance worked in our favor. We had no idea how to be angel investors, and in Boston in 2005 there were no Ron Conways to learn from. So we just made what seemed like the obvious choices, and some of the things we did turned out to be novel.

There are multiple components to Y Combinator, and we didn't figure them all out at once. The part we got first was to be an angel firm.



### Perform a Hybrid Search[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureAISearchIndexDemo/#perform-a-hybrid-search)

In \[ \]:

Copied!

from llama\_index.core.vector\_stores.types import VectorStoreQueryMode

hybrid\_retriever \= index.as\_retriever(
    vector\_store\_query\_mode\=VectorStoreQueryMode.HYBRID
)
hybrid\_retriever.retrieve("What is inception about?")

from llama\_index.core.vector\_stores.types import VectorStoreQueryMode hybrid\_retriever = index.as\_retriever( vector\_store\_query\_mode=VectorStoreQueryMode.HYBRID ) hybrid\_retriever.retrieve("What is inception about?")

Out\[ \]:

\[NodeWithScore(node=TextNode(id\_='bae0df75-ff37-4725-b659-b9fd8bf2ef3c', embedding=None, metadata={'director': 'Christopher Nolan'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, hash='9792a1fd7d2e1a08f1b1d70a597357bb6b68d69ed5685117eaa37ac9e9a3565e', text='Inception', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.03181818127632141),
 NodeWithScore(node=TextNode(id\_='ae5aee85-a083-4141-bf75-bbb872f53760', embedding=None, metadata={'file\_path': '..\\\\data\\\\paul\_graham\\\\paul\_graham\_essay.txt', 'file\_name': 'paul\_graham\_essay.txt', 'file\_type': 'text/plain', 'file\_size': 75395, 'creation\_date': '2023-12-12', 'last\_modified\_date': '2023-12-12', 'last\_accessed\_date': '2024-02-02'}, excluded\_embed\_metadata\_keys=\['file\_name', 'file\_type', 'file\_size', 'creation\_date', 'last\_modified\_date', 'last\_accessed\_date'\], excluded\_llm\_metadata\_keys=\['file\_name', 'file\_type', 'file\_size', 'creation\_date', 'last\_modified\_date', 'last\_accessed\_date'\], relationships={<NodeRelationship.SOURCE: '1'>: RelatedNodeInfo(node\_id='627552ee-116a-4132-a7d3-7e7232f75866', node\_type=<ObjectType.DOCUMENT: '4'>, metadata={'file\_path': '..\\\\data\\\\paul\_graham\\\\paul\_graham\_essay.txt', 'file\_name': 'paul\_graham\_essay.txt', 'file\_type': 'text/plain', 'file\_size': 75395, 'creation\_date': '2023-12-12', 'last\_modified\_date': '2023-12-12', 'last\_accessed\_date': '2024-02-02'}, hash='0a59e1ce8e50a67680a5669164f79e524087270ce183a3971fcd18ac4cad1fa0'), <NodeRelationship.PREVIOUS: '2'>: RelatedNodeInfo(node\_id='24a1d375-31e3-492c-ac02-5091e3572e3f', node\_type=<ObjectType.TEXT: '1'>, metadata={'file\_path': '..\\\\data\\\\paul\_graham\\\\paul\_graham\_essay.txt', 'file\_name': 'paul\_graham\_essay.txt', 'file\_type': 'text/plain', 'file\_size': 75395, 'creation\_date': '2023-12-12', 'last\_modified\_date': '2023-12-12', 'last\_accessed\_date': '2024-02-02'}, hash='51c474a12ac8e9748258b2c7bbe77bb7c8bf35b775ed44f016057a0aa8b0bd76'), <NodeRelationship.NEXT: '3'>: RelatedNodeInfo(node\_id='196569e0-2b10-4ba3-8263-a69fb78dd98c', node\_type=<ObjectType.TEXT: '1'>, metadata={}, hash='192082e7ba84b8c5e2a64bd1d422c6c503189fc3ba325bb3e6e8bdb43db03fbb')}, hash='a3ea638857f1daadf7af967322480f97e1235dac3ee7d72b8024670785df8810', text='It\\'s not that unprestigious types of work are good per se. But when you find yourself drawn to some kind of work despite its current lack of prestige, it\\'s a sign both that there\\'s something real to be discovered there, and that you have the right kind of motives. Impure motives are a big danger for the ambitious. If anything is going to lead you astray, it will be the desire to impress people. So while working on things that aren\\'t prestigious doesn\\'t guarantee you\\'re on the right track, it at least guarantees you\\'re not on the most common type of wrong one.\\n\\nOver the next several years I wrote lots of essays about all kinds of different topics. O\\'Reilly reprinted a collection of them as a book, called Hackers & Painters after one of the essays in it. I also worked on spam filters, and did some more painting. I used to have dinners for a group of friends every thursday night, which taught me how to cook for groups. And I bought another building in Cambridge, a former candy factory (and later, twas said, porn studio), to use as an office.\\n\\nOne night in October 2003 there was a big party at my house. It was a clever idea of my friend Maria Daniels, who was one of the thursday diners. Three separate hosts would all invite their friends to one party. So for every guest, two thirds of the other guests would be people they didn\\'t know but would probably like. One of the guests was someone I didn\\'t know but would turn out to like a lot: a woman called Jessica Livingston. A couple days later I asked her out.\\n\\nJessica was in charge of marketing at a Boston investment bank. This bank thought it understood startups, but over the next year, as she met friends of mine from the startup world, she was surprised how different reality was. And how colorful their stories were. So she decided to compile a book of interviews with startup founders.\\n\\nWhen the bank had financial problems and she had to fire half her staff, she started looking for a new job. In early 2005 she interviewed for a marketing job at a Boston VC firm. It took them weeks to make up their minds, and during this time I started telling her about all the things that needed to be fixed about venture capital. They should make a larger number of smaller investments instead of a handful of giant ones, they should be funding younger, more technical founders instead of MBAs, they should let the founders remain as CEO, and so on.\\n\\nOne of my tricks for writing essays had always been to give talks. The prospect of having to stand up in front of a group of people and tell them something that won\\'t waste their time is a great spur to the imagination. When the Harvard Computer Society, the undergrad computer club, asked me to give a talk, I decided I would tell them how to start a startup. Maybe they\\'d be able to avoid the worst of the mistakes we\\'d made.\\n\\nSo I gave this talk, in the course of which I told them that the best sources of seed funding were successful startup founders, because then they\\'d be sources of advice too. Whereupon it seemed they were all looking expectantly at me. Horrified at the prospect of having my inbox flooded by business plans (if I\\'d only known), I blurted out "But not me!" and went on with the talk. But afterward it occurred to me that I should really stop procrastinating about angel investing. I\\'d been meaning to since Yahoo bought us, and now it was 7 years later and I still hadn\\'t done one angel investment.\\n\\nMeanwhile I had been scheming with Robert and Trevor about projects we could work on together. I missed working with them, and it seemed like there had to be something we could collaborate on.\\n\\nAs Jessica and I were walking home from dinner on March 11, at the corner of Garden and Walker streets, these three threads converged. Screw the VCs who were taking so long to make up their minds. We\\'d start our own investment firm and actually implement the ideas we\\'d been talking about. I\\'d fund it, and Jessica could quit her job and work for it, and we\\'d get Robert and Trevor as partners too. \[13\]\\n\\nOnce again, ignorance worked in our favor. We had no idea how to be angel investors, and in Boston in 2005 there were no Ron Conways to learn from. So we just made what seemed like the obvious choices, and some of the things we did turned out to be novel.\\n\\nThere are multiple components to Y Combinator, and we didn\\'t figure them all out at once. The part we got first was to be an angel firm.', start\_char\_idx=45670, end\_char\_idx=50105, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.03009207174181938)\]

### Perform a Hybrid Search with Semantic Reranking[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureAISearchIndexDemo/#perform-a-hybrid-search-with-semantic-reranking)

This mode incorporates semantic reranking to hybrid search results to improve search relevance.

Please see this link for further details: [https://learn.microsoft.com/azure/search/semantic-search-overview](https://learn.microsoft.com/azure/search/semantic-search-overview)

In \[ \]:

Copied!

hybrid\_retriever \= index.as\_retriever(
    vector\_store\_query\_mode\=VectorStoreQueryMode.SEMANTIC\_HYBRID
)
hybrid\_retriever.retrieve("What is inception about?")

hybrid\_retriever = index.as\_retriever( vector\_store\_query\_mode=VectorStoreQueryMode.SEMANTIC\_HYBRID ) hybrid\_retriever.retrieve("What is inception about?")

Out\[ \]:

\[NodeWithScore(node=TextNode(id\_='bae0df75-ff37-4725-b659-b9fd8bf2ef3c', embedding=None, metadata={'director': 'Christopher Nolan'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, hash='9792a1fd7d2e1a08f1b1d70a597357bb6b68d69ed5685117eaa37ac9e9a3565e', text='Inception', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=2.3949906826019287),
 NodeWithScore(node=TextNode(id\_='fc9782a2-c255-4265-a618-3a864abe598d', embedding=None, metadata={'file\_path': '..\\\\data\\\\paul\_graham\\\\paul\_graham\_essay.txt', 'file\_name': 'paul\_graham\_essay.txt', 'file\_type': 'text/plain', 'file\_size': 75395, 'creation\_date': '2023-12-12', 'last\_modified\_date': '2023-12-12', 'last\_accessed\_date': '2024-02-02'}, excluded\_embed\_metadata\_keys=\['file\_name', 'file\_type', 'file\_size', 'creation\_date', 'last\_modified\_date', 'last\_accessed\_date'\], excluded\_llm\_metadata\_keys=\['file\_name', 'file\_type', 'file\_size', 'creation\_date', 'last\_modified\_date', 'last\_accessed\_date'\], relationships={<NodeRelationship.SOURCE: '1'>: RelatedNodeInfo(node\_id='627552ee-116a-4132-a7d3-7e7232f75866', node\_type=<ObjectType.DOCUMENT: '4'>, metadata={'file\_path': '..\\\\data\\\\paul\_graham\\\\paul\_graham\_essay.txt', 'file\_name': 'paul\_graham\_essay.txt', 'file\_type': 'text/plain', 'file\_size': 75395, 'creation\_date': '2023-12-12', 'last\_modified\_date': '2023-12-12', 'last\_accessed\_date': '2024-02-02'}, hash='0a59e1ce8e50a67680a5669164f79e524087270ce183a3971fcd18ac4cad1fa0'), <NodeRelationship.PREVIOUS: '2'>: RelatedNodeInfo(node\_id='94d87013-ea3d-4a9c-982a-dde5ff219983', node\_type=<ObjectType.TEXT: '1'>, metadata={'file\_path': '..\\\\data\\\\paul\_graham\\\\paul\_graham\_essay.txt', 'file\_name': 'paul\_graham\_essay.txt', 'file\_type': 'text/plain', 'file\_size': 75395, 'creation\_date': '2023-12-12', 'last\_modified\_date': '2023-12-12', 'last\_accessed\_date': '2024-02-02'}, hash='f28897170c6b61162069af9ee83dc11e13fa0f6bf6efaa7b3911e6ad9093da84'), <NodeRelationship.NEXT: '3'>: RelatedNodeInfo(node\_id='dc3852e5-4c1e-484e-9e65-f17084d3f7b4', node\_type=<ObjectType.TEXT: '1'>, metadata={}, hash='deaee6d5c992dbf757876957aa9112a42d30a636c6c83d81fcfac4aaf2d24dee')}, hash='a3b31e5ec2b5d4a9b3648de310c8a5962c17afdb800ea0e16faa47956607866d', text='And at the same time all involved would adhere outwardly to the conventions of a 19th century atelier. We actually had one of those little stoves, fed with kindling, that you see in 19th century studio paintings, and a nude model sitting as close to it as possible without getting burned. Except hardly anyone else painted her besides me. The rest of the students spent their time chatting or occasionally trying to imitate things they\\'d seen in American art magazines.\\n\\nOur model turned out to live just down the street from me. She made a living from a combination of modelling and making fakes for a local antique dealer. She\\'d copy an obscure old painting out of a book, and then he\\'d take the copy and maltreat it to make it look old. \[3\]\\n\\nWhile I was a student at the Accademia I started painting still lives in my bedroom at night. These paintings were tiny, because the room was, and because I painted them on leftover scraps of canvas, which was all I could afford at the time. Painting still lives is different from painting people, because the subject, as its name suggests, can\\'t move. People can\\'t sit for more than about 15 minutes at a time, and when they do they don\\'t sit very still. So the traditional m.o. for painting people is to know how to paint a generic person, which you then modify to match the specific person you\\'re painting. Whereas a still life you can, if you want, copy pixel by pixel from what you\\'re seeing. You don\\'t want to stop there, of course, or you get merely photographic accuracy, and what makes a still life interesting is that it\\'s been through a head. You want to emphasize the visual cues that tell you, for example, that the reason the color changes suddenly at a certain point is that it\\'s the edge of an object. By subtly emphasizing such things you can make paintings that are more realistic than photographs not just in some metaphorical sense, but in the strict information-theoretic sense. \[4\]\\n\\nI liked painting still lives because I was curious about what I was seeing. In everyday life, we aren\\'t consciously aware of much we\\'re seeing. Most visual perception is handled by low-level processes that merely tell your brain "that\\'s a water droplet" without telling you details like where the lightest and darkest points are, or "that\\'s a bush" without telling you the shape and position of every leaf. This is a feature of brains, not a bug. In everyday life it would be distracting to notice every leaf on every bush. But when you have to paint something, you have to look more closely, and when you do there\\'s a lot to see. You can still be noticing new things after days of trying to paint something people usually take for granted, just as you can after days of trying to write an essay about something people usually take for granted.\\n\\nThis is not the only way to paint. I\\'m not 100% sure it\\'s even a good way to paint. But it seemed a good enough bet to be worth trying.\\n\\nOur teacher, professor Ulivi, was a nice guy. He could see I worked hard, and gave me a good grade, which he wrote down in a sort of passport each student had. But the Accademia wasn\\'t teaching me anything except Italian, and my money was running out, so at the end of the first year I went back to the US.\\n\\nI wanted to go back to RISD, but I was now broke and RISD was very expensive, so I decided to get a job for a year and then return to RISD the next fall. I got one at a company called Interleaf, which made software for creating documents. You mean like Microsoft Word? Exactly. That was how I learned that low end software tends to eat high end software. But Interleaf still had a few years to live yet. \[5\]\\n\\nInterleaf had done something pretty bold. Inspired by Emacs, they\\'d added a scripting language, and even made the scripting language a dialect of Lisp. Now they wanted a Lisp hacker to write things in it. This was the closest thing I\\'ve had to a normal job, and I hereby apologize to my boss and coworkers, because I was a bad employee. Their Lisp was the thinnest icing on a giant C cake, and since I didn\\'t know C and didn\\'t want to learn it, I never understood most of the software. Plus I was terribly irresponsible. This was back when a programming job meant showing up every day during certain working hours.', start\_char\_idx=14179, end\_char\_idx=18443, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=1.0986518859863281)\]

Back to top

[Previous Awadb Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AwadbDemo/)[Next Azure CosmosDB MongoDB Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureCosmosDBMongoDBvCoreDemo/)
