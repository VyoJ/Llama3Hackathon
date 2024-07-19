Title: Using a Property Graph Store

URL Source: https://docs.llamaindex.ai/en/stable/examples/property_graph/graph_store/

Markdown Content:
Using a Property Graph Store - LlamaIndex


Normally in LlamaIndex, you'd create a `PropertyGraphStore`, pass it into a `PropertyGraphIndex`, and it would get used automatically for inserting and querying.

However, there are times when you would want to use the graph store directly. Maybe you want to create the graph yourself and hand it to a retriever or index. Maybe you want to write your own code to manage and query a graph store.

This notebook walks through populating and querying a graph store without ever using an index.

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/graph_store/#setup)
-----------------------------------------------------------------------------------------

Here, we will leverage Neo4j for our property graph store.

To launch Neo4j locally, first ensure you have docker installed. Then, you can launch the database with the following docker command

docker run \\
    \-p 7474:7474 \-p 7687:7687 \\
    \-v $PWD/data:/data \-v $PWD/plugins:/plugins \\
    \--name neo4j-apoc \\
    \-e NEO4J\_apoc\_export\_file\_enabled\=true \\
    \-e NEO4J\_apoc\_import\_file\_enabled\=true \\
    \-e NEO4J\_apoc\_import\_file\_use\_\_neo4j\_\_config\=true \\
    \-e NEO4JLABS\_PLUGINS\=\\\[\\"apoc\\"\\\] \\
    neo4j:latest

From here, you can open the db at [http://localhost:7474/](http://localhost:7474/). On this page, you will be asked to sign in. Use the default username/password of `neo4j` and `neo4j`.

Once you login for the first time, you will be asked to change the password.

After this, you are ready to create your first property graph!

In \[ \]:

Copied!

from llama\_index.graph\_stores.neo4j import Neo4jPropertyGraphStore

pg\_store \= Neo4jPropertyGraphStore(
    username\="neo4j",
    password\="llamaindex",
    url\="bolt://localhost:7687",
)

from llama\_index.graph\_stores.neo4j import Neo4jPropertyGraphStore pg\_store = Neo4jPropertyGraphStore( username="neo4j", password="llamaindex", url="bolt://localhost:7687", )

Inserting[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/graph_store/#inserting)
-------------------------------------------------------------------------------------------------

Now that we have the store initialized, we can put some things in it!

Inserting into a property graph store consits of inserting nodes:

*   `EntityNode` - containing some labeled person, place, or thing
*   `ChunkNode` - containing some source text that an entity or relation came from

And inserting `Relation`s (i.e. linking multiple nodes).

In \[ \]:

Copied!

from llama\_index.core.graph\_stores.types import EntityNode, ChunkNode, Relation

\# Create a two entity nodes
entity1 \= EntityNode(label\="PERSON", name\="Logan", properties\={"age": 28})
entity2 \= EntityNode(label\="ORGANIZATION", name\="LlamaIndex")

\# Create a relation
relation \= Relation(
    label\="WORKS\_FOR",
    source\_id\=entity1.id,
    target\_id\=entity2.id,
    properties\={"since": 2023},
)

from llama\_index.core.graph\_stores.types import EntityNode, ChunkNode, Relation # Create a two entity nodes entity1 = EntityNode(label="PERSON", name="Logan", properties={"age": 28}) entity2 = EntityNode(label="ORGANIZATION", name="LlamaIndex") # Create a relation relation = Relation( label="WORKS\_FOR", source\_id=entity1.id, target\_id=entity2.id, properties={"since": 2023}, )

With some entities and relations defined, we can insert them!

In \[ \]:

Copied!

pg\_store.upsert\_nodes(\[entity1, entity2\])
pg\_store.upsert\_relations(\[relation\])

pg\_store.upsert\_nodes(\[entity1, entity2\]) pg\_store.upsert\_relations(\[relation\])

If we wanted, we could also define a text chunk that these came from

In \[ \]:

Copied!

from llama\_index.core.schema import TextNode

source\_node \= TextNode(text\="Logan (age 28), works for LlamaIndex since 2023.")
relations \= \[
    Relation(
        label\="MENTIONS",
        target\_id\=entity1.id,
        source\_id\=source\_node.node\_id,
    ),
    Relation(
        label\="MENTIONS",
        target\_id\=entity2.id,
        source\_id\=source\_node.node\_id,
    ),
\]

pg\_store.upsert\_llama\_nodes(\[source\_node\])
pg\_store.upsert\_relations(relations)

from llama\_index.core.schema import TextNode source\_node = TextNode(text="Logan (age 28), works for LlamaIndex since 2023.") relations = \[ Relation( label="MENTIONS", target\_id=entity1.id, source\_id=source\_node.node\_id, ), Relation( label="MENTIONS", target\_id=entity2.id, source\_id=source\_node.node\_id, ), \] pg\_store.upsert\_llama\_nodes(\[source\_node\]) pg\_store.upsert\_relations(relations)

Now, your graph should have 3 nodes and 3 relations.

![Image 3: low level graph](https://docs.llamaindex.ai/en/stable/examples/property_graph/graph_store/low_level_graph.png)

Retrieving[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/graph_store/#retrieving)
---------------------------------------------------------------------------------------------------

Now that our graph is populated with some nodes and relations, we can access some of the retrieval functions!

In \[ \]:

Copied!

\# get a node
kg\_nodes \= pg\_store.get(ids\=\[entity1.id\])
print(kg\_nodes)

\# get a node kg\_nodes = pg\_store.get(ids=\[entity1.id\]) print(kg\_nodes)

\[EntityNode(label='PERSON', embedding=None, properties={'age': 28, 'name': 'Logan'}, name='Logan')\]

In \[ \]:

Copied!

\# get using properties
kg\_nodes \= pg\_store.get(properties\={"age": 28})
print(kg\_nodes)

\# get using properties kg\_nodes = pg\_store.get(properties={"age": 28}) print(kg\_nodes)

\[EntityNode(label='PERSON', embedding=None, properties={'age': 28, 'name': 'Logan'}, name='Logan')\]

In \[ \]:

Copied!

\# get paths from a node
paths \= pg\_store.get\_rel\_map(kg\_nodes, depth\=1)
for path in paths:
    print(f"{path\[0\].id} -> {path\[1\].id} -> {path\[2\].id}")

\# get paths from a node paths = pg\_store.get\_rel\_map(kg\_nodes, depth=1) for path in paths: print(f"{path\[0\].id} -> {path\[1\].id} -> {path\[2\].id}")

Logan -> WORKS\_FOR -> LlamaIndex

In \[ \]:

Copied!

\# Run a cypher query (this will get all entity nodes)
query \= "match (n:\`\_\_Entity\_\_\`) return n"
result \= pg\_store.structured\_query(query)
print(result)

\# Run a cypher query (this will get all entity nodes) query = "match (n:\`\_\_Entity\_\_\`) return n" result = pg\_store.structured\_query(query) print(result)

\[{'n': {'name': 'Logan', 'id': 'Logan', 'age': 28}}, {'n': {'name': 'LlamaIndex', 'id': 'LlamaIndex'}}\]

In \[ \]:

Copied!

\# get the original text node back
llama\_nodes \= pg\_store.get\_llama\_nodes(\[source\_node.node\_id\])
print(llama\_nodes\[0\].text)

\# get the original text node back llama\_nodes = pg\_store.get\_llama\_nodes(\[source\_node.node\_id\]) print(llama\_nodes\[0\].text)

Logan (age 28), works for LlamaIndex since 2023.

Upserting[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/graph_store/#upserting)
-------------------------------------------------------------------------------------------------

You may have noticed that all the insert operations are actually upserts! As long as the ID of the node is the same, we can avoid duplicating data.

Lets update a node.

In \[ \]:

Copied!

new\_node \= EntityNode(
    label\="PERSON", name\="Logan", properties\={"age": 28, "location": "Canada"}
)
pg\_store.upsert\_nodes(\[new\_node\])

new\_node = EntityNode( label="PERSON", name="Logan", properties={"age": 28, "location": "Canada"} ) pg\_store.upsert\_nodes(\[new\_node\])

In \[ \]:

Copied!

nodes \= pg\_store.get(properties\={"age": 28})
print(nodes)

nodes = pg\_store.get(properties={"age": 28}) print(nodes)

\[EntityNode(label='PERSON', embedding=None, properties={'location': 'Canada', 'age': 28, 'name': 'Logan'}, name='Logan')\]

Deleting[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/graph_store/#deleting)
-----------------------------------------------------------------------------------------------

Deletion works similar to `get()`, with both IDs and properties.

Let's clean-up our graph for a fresh start.

In \[ \]:

Copied!

\# delete our entities
pg\_store.delete(ids\=\[entity1.id, entity2.id\])

\# delete our text nodes
pg\_store.delete(\[source\_node.node\_id\])

\# delete our entities pg\_store.delete(ids=\[entity1.id, entity2.id\]) # delete our text nodes pg\_store.delete(\[source\_node.node\_id\])

In \[ \]:

Copied!

nodes \= pg\_store.get(ids\=\[entity1.id, entity2.id\])
print(nodes)

nodes = pg\_store.get(ids=\[entity1.id, entity2.id\]) print(nodes)

\[\]

Back to top

[Previous Prompt Engineering for RAG](https://docs.llamaindex.ai/en/stable/examples/prompts/prompts_rag/)[Next Property Graph Construction with Predefined Schemas](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_advanced/)

Hi, how can I help you?

🦙
