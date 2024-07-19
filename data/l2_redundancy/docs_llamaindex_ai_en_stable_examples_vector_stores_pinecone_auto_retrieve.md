Title: A Simple to Advanced Guide with Auto-Retrieval (with Pinecone + Arize Phoenix)

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/pinecone_auto_retriever/

Markdown Content:
A Simple to Advanced Guide with Auto-Retrieval (with Pinecone + Arize Phoenix) - LlamaIndex


In this notebook we showcase how to perform **auto-retrieval** against Pinecone, which lets you execute a broad range of semi-structured queries beyond what you can do with standard top-k semantic search.

We show both how to setup basic auto-retrieval, as well as how to extend it (by customizing the prompt and through dynamic metadata retrieval).

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-pinecone

%pip install llama-index-vector-stores-pinecone

In \[ \]:

Copied!

\# !pip install llama-index>=0.9.31 scikit-learn2.4.1 pinecone-client>=3.0.0

\# !pip install llama-index>=0.9.31 scikit-learn2.4.1 pinecone-client>=3.0.0

Part 1: Setup Auto-Retrieval[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/pinecone_auto_retriever/#part-1-setup-auto-retrieval)
-------------------------------------------------------------------------------------------------------------------------------------------------

To setup auto-retrieval, do the following:

1.  We'll do some setup, load data, build a Pinecone vector index.
2.  We'll define our autoretriever and run some sample queries.
3.  We'll use Phoenix to observe each trace and visualize the prompt inputs/outputs.
4.  We'll show you how to customize the auto-retrieval prompt.

### 1.a Setup Pinecone/Phoenix, Load Data, and Build Vector Index[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/pinecone_auto_retriever/#1a-setup-pineconephoenix-load-data-and-build-vector-index)

In this section we setup pinecone and ingest some toy data on books/movies (with text data and metadata).

We also setup Phoenix so that it captures downstream traces.

In \[ \]:

Copied!

\# setup Phoenix
import phoenix as px
import llama\_index.core

px.launch\_app()
llama\_index.core.set\_global\_handler("arize\_phoenix")

\# setup Phoenix import phoenix as px import llama\_index.core px.launch\_app() llama\_index.core.set\_global\_handler("arize\_phoenix")

🌍 To view the Phoenix app in your browser, visit http://127.0.0.1:6006/
📺 To view the Phoenix app in a notebook, run \`px.active\_session().view()\`
📖 For more information on how to use Phoenix, check out https://docs.arize.com/phoenix

In \[ \]:

Copied!

import os

os.environ\[
    "PINECONE\_API\_KEY"
\] \= "<Your Pinecone API key, from app.pinecone.io>"
\# os.environ\["OPENAI\_API\_KEY"\] = "sk-..."

import os os.environ\[ "PINECONE\_API\_KEY" \] = "" # os.environ\["OPENAI\_API\_KEY"\] = "sk-..."

In \[ \]:

Copied!

from pinecone import Pinecone
from pinecone import ServerlessSpec

api\_key \= os.environ\["PINECONE\_API\_KEY"\]
pc \= Pinecone(api\_key\=api\_key)

from pinecone import Pinecone from pinecone import ServerlessSpec api\_key = os.environ\["PINECONE\_API\_KEY"\] pc = Pinecone(api\_key=api\_key)

In \[ \]:

Copied!

\# delete if needed
\# pc.delete\_index("quickstart-index")

\# delete if needed # pc.delete\_index("quickstart-index")

In \[ \]:

Copied!

\# Dimensions are for text-embedding-ada-002
try:
    pc.create\_index(
        "quickstart-index",
        dimension\=1536,
        metric\="euclidean",
        spec\=ServerlessSpec(cloud\="aws", region\="us-west-2"),
    )
except Exception as e:
    \# Most likely index already exists
    print(e)
    pass

\# Dimensions are for text-embedding-ada-002 try: pc.create\_index( "quickstart-index", dimension=1536, metric="euclidean", spec=ServerlessSpec(cloud="aws", region="us-west-2"), ) except Exception as e: # Most likely index already exists print(e) pass

In \[ \]:

Copied!

pinecone\_index \= pc.Index("quickstart-index")

pinecone\_index = pc.Index("quickstart-index")

#### Load documents, build the PineconeVectorStore and VectorStoreIndex[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/pinecone_auto_retriever/#load-documents-build-the-pineconevectorstore-and-vectorstoreindex)

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
        text\="The Shawshank Redemption",
        metadata\={
            "author": "Stephen King",
            "theme": "Friendship",
            "year": 1994,
        },
    ),
    TextNode(
        text\="The Godfather",
        metadata\={
            "director": "Francis Ford Coppola",
            "theme": "Mafia",
            "year": 1972,
        },
    ),
    TextNode(
        text\="Inception",
        metadata\={
            "director": "Christopher Nolan",
            "theme": "Fiction",
            "year": 2010,
        },
    ),
    TextNode(
        text\="To Kill a Mockingbird",
        metadata\={
            "author": "Harper Lee",
            "theme": "Fiction",
            "year": 1960,
        },
    ),
    TextNode(
        text\="1984",
        metadata\={
            "author": "George Orwell",
            "theme": "Totalitarianism",
            "year": 1949,
        },
    ),
    TextNode(
        text\="The Great Gatsby",
        metadata\={
            "author": "F. Scott Fitzgerald",
            "theme": "The American Dream",
            "year": 1925,
        },
    ),
    TextNode(
        text\="Harry Potter and the Sorcerer's Stone",
        metadata\={
            "author": "J.K. Rowling",
            "theme": "Fiction",
            "year": 1997,
        },
    ),
\]

from llama\_index.core.schema import TextNode nodes = \[ TextNode( text="The Shawshank Redemption", metadata={ "author": "Stephen King", "theme": "Friendship", "year": 1994, }, ), TextNode( text="The Godfather", metadata={ "director": "Francis Ford Coppola", "theme": "Mafia", "year": 1972, }, ), TextNode( text="Inception", metadata={ "director": "Christopher Nolan", "theme": "Fiction", "year": 2010, }, ), TextNode( text="To Kill a Mockingbird", metadata={ "author": "Harper Lee", "theme": "Fiction", "year": 1960, }, ), TextNode( text="1984", metadata={ "author": "George Orwell", "theme": "Totalitarianism", "year": 1949, }, ), TextNode( text="The Great Gatsby", metadata={ "author": "F. Scott Fitzgerald", "theme": "The American Dream", "year": 1925, }, ), TextNode( text="Harry Potter and the Sorcerer's Stone", metadata={ "author": "J.K. Rowling", "theme": "Fiction", "year": 1997, }, ), \]

In \[ \]:

Copied!

vector\_store \= PineconeVectorStore(
    pinecone\_index\=pinecone\_index,
    namespace\="test",
)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

vector\_store = PineconeVectorStore( pinecone\_index=pinecone\_index, namespace="test", ) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store)

In \[ \]:

Copied!

index \= VectorStoreIndex(nodes, storage\_context\=storage\_context)

index = VectorStoreIndex(nodes, storage\_context=storage\_context)

Upserted vectors:   0%|          | 0/7 \[00:00<?, ?it/s\]

### 1.b Define Autoretriever, Run Some Sample Queries[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/pinecone_auto_retriever/#1b-define-autoretriever-run-some-sample-queries)

#### Setup the `VectorIndexAutoRetriever`[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/pinecone_auto_retriever/#setup-the-vectorindexautoretriever)

One of the inputs is a `schema` describing what content the vector store collection contains. This is similar to a table schema describing a table in the SQL database. This schema information is then injected into the prompt, which is passed to the LLM to infer what the full query should be (including metadata filters).

In \[ \]:

Copied!

from llama\_index.core.retrievers import VectorIndexAutoRetriever
from llama\_index.core.vector\_stores import MetadataInfo, VectorStoreInfo

vector\_store\_info \= VectorStoreInfo(
    content\_info\="famous books and movies",
    metadata\_info\=\[
        MetadataInfo(
            name\="director",
            type\="str",
            description\=("Name of the director"),
        ),
        MetadataInfo(
            name\="theme",
            type\="str",
            description\=("Theme of the book/movie"),
        ),
        MetadataInfo(
            name\="year",
            type\="int",
            description\=("Year of the book/movie"),
        ),
    \],
)
retriever \= VectorIndexAutoRetriever(
    index,
    vector\_store\_info\=vector\_store\_info,
    empty\_query\_top\_k\=10,
    \# this is a hack to allow for blank queries in pinecone
    default\_empty\_query\_vector\=\[0\] \* 1536,
    verbose\=True,
)

from llama\_index.core.retrievers import VectorIndexAutoRetriever from llama\_index.core.vector\_stores import MetadataInfo, VectorStoreInfo vector\_store\_info = VectorStoreInfo( content\_info="famous books and movies", metadata\_info=\[ MetadataInfo( name="director", type="str", description=("Name of the director"), ), MetadataInfo( name="theme", type="str", description=("Theme of the book/movie"), ), MetadataInfo( name="year", type="int", description=("Year of the book/movie"), ), \], ) retriever = VectorIndexAutoRetriever( index, vector\_store\_info=vector\_store\_info, empty\_query\_top\_k=10, # this is a hack to allow for blank queries in pinecone default\_empty\_query\_vector=\[0\] \* 1536, verbose=True, )

#### Let's run some queries[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/pinecone_auto_retriever/#lets-run-some-queries)

Let's run some sample queries that make use of the structured information.

In \[ \]:

Copied!

nodes \= retriever.retrieve(
    "Tell me about some books/movies after the year 2000"
)

nodes = retriever.retrieve( "Tell me about some books/movies after the year 2000" )

Using query str: 
Using filters: \[('year', '>', 2000)\]

In \[ \]:

Copied!

for node in nodes:
    print(node.text)
    print(node.metadata)

for node in nodes: print(node.text) print(node.metadata)

Inception
{'director': 'Christopher Nolan', 'theme': 'Fiction', 'year': 2010}

In \[ \]:

Copied!

nodes \= retriever.retrieve("Tell me about some books that are Fiction")

nodes = retriever.retrieve("Tell me about some books that are Fiction")

Using query str: Fiction
Using filters: \[('theme', '", "value": 1997}\]
filters \= MetadataFilters.from\_dicts(filter\_dicts)
retriever2 \= VectorIndexAutoRetriever(
    index,
    vector\_store\_info\=vector\_store\_info,
    empty\_query\_top\_k\=10,
    \# this is a hack to allow for blank queries in pinecone
    default\_empty\_query\_vector\=\[0\] \* 1536,
    extra\_filters\=filters,
)

from llama\_index.core.vector\_stores import MetadataFilters filter\_dicts = \[{"key": "year", "operator": "', 'mafia')\]

In \[ \]:

Copied!

for node in nodes:
    print(node.text)
    print(node.metadata)

for node in nodes: print(node.text) print(node.metadata)

### Visualize Traces[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/pinecone_auto_retriever/#visualize-traces)

Let's open up Phoenix to take a look at the traces!

![Image 4: No description has been provided for this image](https://drive.google.com/uc?export=view&id=1PCEwIdv7GcInk3i6ebd2WWjTp9ducG5F)

Let's take a look at the auto-retrieval prompt. We see that the auto-retrieval prompt makes use of two few-shot examples.

Part 2: Extending Auto-Retrieval (with Dynamic Metadata Retrieval)[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/pinecone_auto_retriever/#part-2-extending-auto-retrieval-with-dynamic-metadata-retrieval)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We now extend auto-retrieval by customizing the prompt. In the first part, we explicitly add some rules.

In the second part we implement **dynamic metadata retrieval**, which will do a first-stage retrieval pass of fetching relevant metadata from the vector db, and insert that as few-shot examples to the auto-retrieval prompt. (Of course, the second stage retrieval pass retrieves the actual items from the vector db).

### 2.a Improve the Auto-retrieval Prompt[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/pinecone_auto_retriever/#2a-improve-the-auto-retrieval-prompt)

Our auto-retrieval prompt works, but it can be improved in various ways. Some examples include the fact that it includes 2 hardcoded few-shot examples (how can you include your own?), and also the fact that the auto-retrieval doesn't "always" infer the right metadata filters.

For instance, all the `theme` fields are capitalized. How do we tell the LLM that, so it doesn't erroneously infer a "theme" that's in lower-case?

Let's take a stab at modifying the prompt!

In \[ \]:

Copied!

from llama\_index.core.prompts import display\_prompt\_dict
from llama\_index.core import PromptTemplate

from llama\_index.core.prompts import display\_prompt\_dict from llama\_index.core import PromptTemplate

In \[ \]:

Copied!

prompts\_dict \= retriever.get\_prompts()

prompts\_dict = retriever.get\_prompts()

In \[ \]:

Copied!

display\_prompt\_dict(prompts\_dict)

display\_prompt\_dict(prompts\_dict)

In \[ \]:

Copied!

\# look at required template variables.
prompts\_dict\["prompt"\].template\_vars

\# look at required template variables. prompts\_dict\["prompt"\].template\_vars

Out\[ \]:

\['schema\_str', 'info\_str', 'query\_str'\]

#### Customize the Prompt[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/pinecone_auto_retriever/#customize-the-prompt)

Let's customize the prompt a little bit. We do the following:

*   Take out the first few-shot example to save tokens
*   Add a message to always capitalize a letter if inferring "theme".

Note that the prompt template expects `schema_str`, `info_str`, and `query_str` to be defined.

In \[ \]:

Copied!

\# write prompt template, and modify it.

prompt\_tmpl\_str \= """\\
Your goal is to structure the user's query to match the request schema provided below.

<< Structured Request Schema >>
When responding use a markdown code snippet with a JSON object formatted in the following schema:

{schema\_str}

The query string should contain only text that is expected to match the contents of documents. Any conditions in the filter should not be mentioned in the query as well.

Make sure that filters only refer to attributes that exist in the data source.
Make sure that filters take into account the descriptions of attributes.
Make sure that filters are only used as needed. If there are no filters that should be applied return \[\] for the filter value.
If the user's query explicitly mentions number of documents to retrieve, set top\_k to that number, otherwise do not set top\_k.
Do NOT EVER infer a null value for a filter. This will break the downstream program. Instead, don't include the filter.

<< Example 1. >>
Data Source:
\`\`\`json
{{
    "metadata\_info": \[
        {{
            "name": "author",
            "type": "str",
            "description": "Author name"
        }},
        {{
            "name": "book\_title",
            "type": "str",
            "description": "Book title"
        }},
        {{
            "name": "year",
            "type": "int",
            "description": "Year Published"
        }},
        {{
            "name": "pages",
            "type": "int",
            "description": "Number of pages"
        }},
        {{
            "name": "summary",
            "type": "str",
            "description": "A short summary of the book"
        }}
    \],
    "content\_info": "Classic literature"
}}
\`\`\`

User Query:
What are some books by Jane Austen published after 1813 that explore the theme of marriage for social standing?

Additional Instructions:
None

Structured Request:
\`\`\`json
{{"query": "Books related to theme of marriage for social standing", "filters": \[{{"key": "year", "value": "1813", "operator": ">"}}, {{"key": "author", "value": "Jane Austen", "operator": ""}}\], "top\_k": null}} \`\`\` << Example 2. >> Data Source: \`\`\`json {info\_str} \`\`\` User Query: {query\_str} Additional Instructions: {additional\_instructions} Structured Request: """

In \[ \]:

Copied!

prompt\_tmpl \= PromptTemplate(prompt\_tmpl\_str)

prompt\_tmpl = PromptTemplate(prompt\_tmpl\_str)

You'll notice we added an `additional_instructions` template variable. This allows us to insert vector collection-specific instructions.

We'll use `partial_format` to add the instruction.

In \[ \]:

Copied!

add\_instrs \= """\\
If one of the filters is 'theme', please make sure that the first letter of the inferred value is capitalized. Only words that are capitalized are valid values for "theme". \\
"""
prompt\_tmpl \= prompt\_tmpl.partial\_format(additional\_instructions\=add\_instrs)

add\_instrs = """\\ If one of the filters is 'theme', please make sure that the first letter of the inferred value is capitalized. Only words that are capitalized are valid values for "theme". \\ """ prompt\_tmpl = prompt\_tmpl.partial\_format(additional\_instructions=add\_instrs)

In \[ \]:

Copied!

retriever.update\_prompts({"prompt": prompt\_tmpl})

retriever.update\_prompts({"prompt": prompt\_tmpl})

#### Re-run some queries[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/pinecone_auto_retriever/#re-run-some-queries)

Now let's try rerunning some queries, and we'll see that the value is auto-inferred.

In \[ \]:

Copied!

nodes \= retriever.retrieve(
    "Tell me about some books that are friendship-themed"
)

nodes = retriever.retrieve( "Tell me about some books that are friendship-themed" )

In \[ \]:

Copied!

for node in nodes:
    print(node.text)
    print(node.metadata)

for node in nodes: print(node.text) print(node.metadata)

### 2.b Implement Dynamic Metadata Retrieval[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/pinecone_auto_retriever/#2b-implement-dynamic-metadata-retrieval)

An option besides hardcoding rules in the prompt is to retrieve **relevant few-shot examples of metadata**, to help the LLM better infer the correct metadata filters.

This will better prevent the LLM from making mistakes when inferring "where" clauses, especially around aspects like spelling / correct formatting of the value.

We can do this via vector retrieval. The existing vector db collection stores the raw text + metadata; we could query this collection directly, or separately only index the metadata and retrieve from that. In this section we choose to do the former but in practice you may want to do the latter.

In \[ \]:

Copied!

\# define retriever that fetches the top 2 examples.
metadata\_retriever \= index.as\_retriever(similarity\_top\_k\=2)

\# define retriever that fetches the top 2 examples. metadata\_retriever = index.as\_retriever(similarity\_top\_k=2)

We use the same `prompt_tmpl_str` defined in the previous section.

In \[ \]:

Copied!

from typing import List, Any

def format\_additional\_instrs(\*\*kwargs: Any) \-> str:
    """Format examples into a string."""

    nodes \= metadata\_retriever.retrieve(kwargs\["query\_str"\])
    context\_str \= (
        "Here is the metadata of relevant entries from the database collection. "
        "This should help you infer the right filters: \\n"
    )
    for node in nodes:
        context\_str += str(node.node.metadata) + "\\n"
    return context\_str

ext\_prompt\_tmpl \= PromptTemplate(
    prompt\_tmpl\_str,
    function\_mappings\={"additional\_instructions": format\_additional\_instrs},
)

from typing import List, Any def format\_additional\_instrs(\*\*kwargs: Any) -> str: """Format examples into a string.""" nodes = metadata\_retriever.retrieve(kwargs\["query\_str"\]) context\_str = ( "Here is the metadata of relevant entries from the database collection. " "This should help you infer the right filters: \\n" ) for node in nodes: context\_str += str(node.node.metadata) + "\\n" return context\_str ext\_prompt\_tmpl = PromptTemplate( prompt\_tmpl\_str, function\_mappings={"additional\_instructions": format\_additional\_instrs}, )

In \[ \]:

Copied!

retriever.update\_prompts({"prompt": ext\_prompt\_tmpl})

retriever.update\_prompts({"prompt": ext\_prompt\_tmpl})

#### Re-run some queries[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/pinecone_auto_retriever/#re-run-some-queries)

Now let's try rerunning some queries, and we'll see that the value is auto-inferred.

In \[ \]:

Copied!

nodes \= retriever.retrieve("Tell me about some books that are mafia-themed")
for node in nodes:
    print(node.text)
    print(node.metadata)

nodes = retriever.retrieve("Tell me about some books that are mafia-themed") for node in nodes: print(node.text) print(node.metadata)

Using query str: books
Using filters: \[('theme', '', 'Harper Lee')\]
To Kill a Mockingbird
{'author': 'Harper Lee', 'theme': 'Fiction', 'year': 1960}

Back to top

[Previous Neo4j Vector Store - Metadata Filter](https://docs.llamaindex.ai/en/stable/examples/vector_stores/neo4j_metadata_filter/)[Next Pinecone Vector Store - Metadata Filter](https://docs.llamaindex.ai/en/stable/examples/vector_stores/pinecone_metadata_filter/)
