Title: The ObjectIndex Class - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/objects/object_index/

Markdown Content:
The ObjectIndex Class - LlamaIndex


The `ObjectIndex` class is one that allows for the indexing of arbitrary Python objects. As such, it is quite flexible and applicable to a wide-range of use cases. As examples:

*   [Use an `ObjectIndex` to index Tool objects to then be used by an agent.](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_retrieval.html#building-an-object-index)
*   [Use an `ObjectIndex` to index a SQLTableSchema objects](https://docs.llamaindex.ai/en/stable/examples/index_structs/struct_indices/SQLIndexDemo.html#part-2-query-time-retrieval-of-tables-for-text-to-sql)

To construct an `ObjectIndex`, we require an index as well as another abstraction, namely `ObjectNodeMapping`. This mapping, as its name suggests, provides the means to go between node and the associated object, and vice versa. Alternatively, there exists a `from_objects()` class method, that can conveniently construct an `ObjectIndex` from a set of objects.

In this notebook, we'll quickly cover how you can build an `ObjectIndex` using a `SimpleObjectNodeMapping`.

In \[ \]:

Copied!

from llama\_index.core import Settings

Settings.embed\_model \= "local"

from llama\_index.core import Settings Settings.embed\_model = "local"

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex
from llama\_index.core.objects import ObjectIndex, SimpleObjectNodeMapping

\# some really arbitrary objects
obj1 \= {"input": "Hey, how's it going"}
obj2 \= \["a", "b", "c", "d"\]
obj3 \= "llamaindex is an awesome library!"
arbitrary\_objects \= \[obj1, obj2, obj3\]

\# (optional) object-node mapping
obj\_node\_mapping \= SimpleObjectNodeMapping.from\_objects(arbitrary\_objects)
nodes \= obj\_node\_mapping.to\_nodes(arbitrary\_objects)

\# object index
object\_index \= ObjectIndex(
    index\=VectorStoreIndex(nodes\=nodes),
    object\_node\_mapping\=obj\_node\_mapping,
)

\# object index from\_objects (default index\_cls=VectorStoreIndex)
object\_index \= ObjectIndex.from\_objects(
    arbitrary\_objects, index\_cls\=VectorStoreIndex
)

from llama\_index.core import VectorStoreIndex from llama\_index.core.objects import ObjectIndex, SimpleObjectNodeMapping # some really arbitrary objects obj1 = {"input": "Hey, how's it going"} obj2 = \["a", "b", "c", "d"\] obj3 = "llamaindex is an awesome library!" arbitrary\_objects = \[obj1, obj2, obj3\] # (optional) object-node mapping obj\_node\_mapping = SimpleObjectNodeMapping.from\_objects(arbitrary\_objects) nodes = obj\_node\_mapping.to\_nodes(arbitrary\_objects) # object index object\_index = ObjectIndex( index=VectorStoreIndex(nodes=nodes), object\_node\_mapping=obj\_node\_mapping, ) # object index from\_objects (default index\_cls=VectorStoreIndex) object\_index = ObjectIndex.from\_objects( arbitrary\_objects, index\_cls=VectorStoreIndex )

### As a retriever[¶](https://docs.llamaindex.ai/en/stable/examples/objects/object_index/#as-a-retriever)

With the `object_index` in hand, we can use it as a retriever, to retrieve against the index objects.

In \[ \]:

Copied!

object\_retriever \= object\_index.as\_retriever(similarity\_top\_k\=1)
object\_retriever.retrieve("llamaindex")

object\_retriever = object\_index.as\_retriever(similarity\_top\_k=1) object\_retriever.retrieve("llamaindex")

Out\[ \]:

\['llamaindex is an awesome library!'\]

We can also add node-postprocessors to an object index retriever, for easy convience to things like rerankers and more.

In \[ \]:

Copied!

%pip install llama\-index\-postprocessor\-colbert\-rerank

%pip install llama-index-postprocessor-colbert-rerank

In \[ \]:

Copied!

from llama\_index.postprocessor.colbert\_rerank import ColbertRerank

retriever \= object\_index.as\_retriever(
    similarity\_top\_k\=2, node\_postprocessors\=\[ColbertRerank(top\_n\=1)\]
)
retriever.retrieve("a random list object")

from llama\_index.postprocessor.colbert\_rerank import ColbertRerank retriever = object\_index.as\_retriever( similarity\_top\_k=2, node\_postprocessors=\[ColbertRerank(top\_n=1)\] ) retriever.retrieve("a random list object")

Out\[ \]:

\['llamaindex is an awesome library!'\]

Using a Storage Integration (i.e. Chroma)[¶](https://docs.llamaindex.ai/en/stable/examples/objects/object_index/#using-a-storage-integration-ie-chroma)
-------------------------------------------------------------------------------------------------------------------------------------------------------

The object index supports integrations with any existing storage backend in LlamaIndex.

The following section walks through how to set that up using `Chroma` as an example.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-chroma

%pip install llama-index-vector-stores-chroma

In \[ \]:

Copied!

from llama\_index.core import StorageContext, VectorStoreIndex
from llama\_index.vector\_stores.chroma import ChromaVectorStore
import chromadb

db \= chromadb.PersistentClient(path\="./chroma\_db")
chroma\_collection \= db.get\_or\_create\_collection("quickstart2")
vector\_store \= ChromaVectorStore(chroma\_collection\=chroma\_collection)
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)

object\_index \= ObjectIndex.from\_objects(
    arbitrary\_objects,
    index\_cls\=VectorStoreIndex,
    storage\_context\=storage\_context,
)

from llama\_index.core import StorageContext, VectorStoreIndex from llama\_index.vector\_stores.chroma import ChromaVectorStore import chromadb db = chromadb.PersistentClient(path="./chroma\_db") chroma\_collection = db.get\_or\_create\_collection("quickstart2") vector\_store = ChromaVectorStore(chroma\_collection=chroma\_collection) storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) object\_index = ObjectIndex.from\_objects( arbitrary\_objects, index\_cls=VectorStoreIndex, storage\_context=storage\_context, )

\---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
Cell In\[31\], line 5
      2 from llama\_index.vector\_stores.chroma import ChromaVectorStore
      3 import chromadb
\----> 5 db = chromadb.PersistentClient(path="./chroma\_db2")
      6 chroma\_collection = db.get\_or\_create\_collection("quickstart2")
      7 vector\_store = ChromaVectorStore(chroma\_collection=chroma\_collection)

File ~/giant\_change/llama\_index/venv/lib/python3.10/site-packages/chromadb/\_\_init\_\_.py:146, in PersistentClient(path, settings, tenant, database)
    143 tenant = str(tenant)
    144 database = str(database)
\--> 146 return ClientCreator(tenant=tenant, database=database, settings=settings)

File ~/giant\_change/llama\_index/venv/lib/python3.10/site-packages/chromadb/api/client.py:139, in Client.\_\_init\_\_(self, tenant, database, settings)
    133 def \_\_init\_\_(
    134     self,
    135     tenant: str = DEFAULT\_TENANT,
    136     database: str = DEFAULT\_DATABASE,
    137     settings: Settings = Settings(),
    138 ) -> None:
\--> 139     super().\_\_init\_\_(settings=settings)
    140     self.tenant = tenant
    141     self.database = database

File ~/giant\_change/llama\_index/venv/lib/python3.10/site-packages/chromadb/api/client.py:43, in SharedSystemClient.\_\_init\_\_(self, settings)
     38 def \_\_init\_\_(
     39     self,
     40     settings: Settings = Settings(),
     41 ) -> None:
     42     self.\_identifier = SharedSystemClient.\_get\_identifier\_from\_settings(settings)
\---> 43     SharedSystemClient.\_create\_system\_if\_not\_exists(self.\_identifier, settings)

File ~/giant\_change/llama\_index/venv/lib/python3.10/site-packages/chromadb/api/client.py:54, in SharedSystemClient.\_create\_system\_if\_not\_exists(cls, identifier, settings)
     51     cls.\_identifer\_to\_system\[identifier\] = new\_system
     53     new\_system.instance(ProductTelemetryClient)
\---> 54     new\_system.instance(ServerAPI)
     56     new\_system.start()
     57 else:

File ~/giant\_change/llama\_index/venv/lib/python3.10/site-packages/chromadb/config.py:382, in System.instance(self, type)
    379     type = get\_class(fqn, type)
    381 if type not in self.\_instances:
\--> 382     impl = type(self)
    383     self.\_instances\[type\] = impl
    384     if self.\_running:

File ~/giant\_change/llama\_index/venv/lib/python3.10/site-packages/chromadb/api/segment.py:102, in SegmentAPI.\_\_init\_\_(self, system)
    100 super().\_\_init\_\_(system)
    101 self.\_settings = system.settings
\--> 102 self.\_sysdb = self.require(SysDB)
    103 self.\_manager = self.require(SegmentManager)
    104 self.\_quota = self.require(QuotaEnforcer)

File ~/giant\_change/llama\_index/venv/lib/python3.10/site-packages/chromadb/config.py:281, in Component.require(self, type)
    278 def require(self, type: Type\[T\]) -> T:
    279     """Get a Component instance of the given type, and register as a dependency of
    280     that instance."""
\--> 281     inst = self.\_system.instance(type)
    282     self.\_dependencies.add(inst)
    283     return inst

File ~/giant\_change/llama\_index/venv/lib/python3.10/site-packages/chromadb/config.py:382, in System.instance(self, type)
    379     type = get\_class(fqn, type)
    381 if type not in self.\_instances:
\--> 382     impl = type(self)
    383     self.\_instances\[type\] = impl
    384     if self.\_running:

File ~/giant\_change/llama\_index/venv/lib/python3.10/site-packages/chromadb/db/impl/sqlite.py:88, in SqliteDB.\_\_init\_\_(self, system)
     84     self.\_db\_file = (
     85         self.\_settings.require("persist\_directory") + "/chroma.sqlite3"
     86     )
     87     if not os.path.exists(self.\_db\_file):
\---> 88         os.makedirs(os.path.dirname(self.\_db\_file), exist\_ok=True)
     89     self.\_conn\_pool = PerThreadPool(self.\_db\_file)
     90 self.\_tx\_stack = local()

File ~/miniforge3/lib/python3.10/os.py:225, in makedirs(name, mode, exist\_ok)
    223         return
    224 try:
\--> 225     mkdir(name, mode)
    226 except OSError:
    227     # Cannot rely on checking for EEXIST, since the operating system
    228     # could give priority to other errors like EACCES or EROFS
    229     if not exist\_ok or not path.isdir(name):

FileNotFoundError: \[Errno 2\] No such file or directory: './chroma\_db2'

In \[ \]:

Copied!

object\_retriever \= object\_index.as\_retriever(similarity\_top\_k\=1)
object\_retriever.retrieve("llamaindex")

object\_retriever = object\_index.as\_retriever(similarity\_top\_k=1) object\_retriever.retrieve("llamaindex")

Out\[ \]:

\['llamaindex is an awesome library!'\]

Now, lets "reload" the index

In \[ \]:

Copied!

db \= chromadb.PersistentClient(path\="./chroma\_db")
chroma\_collection \= db.get\_or\_create\_collection("quickstart")
vector\_store \= ChromaVectorStore(chroma\_collection\=chroma\_collection)

index \= VectorStoreIndex.from\_vector\_store(vector\_store\=vector\_store)

object\_index \= ObjectIndex.from\_objects\_and\_index(arbitrary\_objects, index)

db = chromadb.PersistentClient(path="./chroma\_db") chroma\_collection = db.get\_or\_create\_collection("quickstart") vector\_store = ChromaVectorStore(chroma\_collection=chroma\_collection) index = VectorStoreIndex.from\_vector\_store(vector\_store=vector\_store) object\_index = ObjectIndex.from\_objects\_and\_index(arbitrary\_objects, index)

In \[ \]:

Copied!

object\_retriever \= object\_index.as\_retriever(similarity\_top\_k\=1)
object\_retriever.retrieve("llamaindex")

object\_retriever = object\_index.as\_retriever(similarity\_top\_k=1) object\_retriever.retrieve("llamaindex")

Out\[ \]:

\['llamaindex is an awesome library!'\]

Note that when we reload the index, we still have to pass the objects, since those are not saved in the actual index/vector db.

\[Advanced\] Customizing the Mapping[¶](https://docs.llamaindex.ai/en/stable/examples/objects/object_index/#advanced-customizing-the-mapping)
---------------------------------------------------------------------------------------------------------------------------------------------

For specialized cases where you want full control over how objects are mapped to nodes, you can also provide a `to_node_fn()` and `from_node_fn()` hook.

This is useful for when you are converting specialized objects, or want to dynamically create objects at runtime rather than keeping them in memory.

A small example is shown below.

In \[ \]:

Copied!

from llama\_index.core.schema import TextNode

my\_objects \= {
    str(hash(str(obj))): obj for i, obj in enumerate(arbitrary\_objects)
}

def from\_node\_fn(node):
    return my\_objects\[node.id\]

def to\_node\_fn(obj):
    return TextNode(id\=str(hash(str(obj))), text\=str(obj))

object\_index \= ObjectIndex.from\_objects(
    arbitrary\_objects,
    index\_cls\=VectorStoreIndex,
    from\_node\_fn\=from\_node\_fn,
    to\_node\_fn\=to\_node\_fn,
)

object\_retriever \= object\_index.as\_retriever(similarity\_top\_k\=1)

object\_retriever.retrieve("llamaindex")

from llama\_index.core.schema import TextNode my\_objects = { str(hash(str(obj))): obj for i, obj in enumerate(arbitrary\_objects) } def from\_node\_fn(node): return my\_objects\[node.id\] def to\_node\_fn(obj): return TextNode(id=str(hash(str(obj))), text=str(obj)) object\_index = ObjectIndex.from\_objects( arbitrary\_objects, index\_cls=VectorStoreIndex, from\_node\_fn=from\_node\_fn, to\_node\_fn=to\_node\_fn, ) object\_retriever = object\_index.as\_retriever(similarity\_top\_k=1) object\_retriever.retrieve("llamaindex")

Out\[ \]:

\['llamaindex is an awesome library!'\]

Persisting `ObjectIndex` to Disk with Objects[¶](https://docs.llamaindex.ai/en/stable/examples/objects/object_index/#persisting-objectindex-to-disk-with-objects)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

When it comes to persisting the `ObjectIndex`, we have to handle both the index as well as the object-node mapping. Persisting the index is straightforward and can be handled by usual means (e.g., see this [guide](https://docs.llamaindex.ai/en/stable/module_guides/storing/save_load.html#persisting-loading-data)). However, it's a bit of a different story when it comes to persisting the `ObjectNodeMapping`. Since we're indexing aribtrary Python objects with the `ObjectIndex`, it may be the case (and perhaps more often than we'd like), that the arbitrary objects are not serializable. In those cases, you can persist the index, but the user would have to maintain a way to re-construct the `ObjectNodeMapping` to be able to re-construct the `ObjectIndex`. For convenience, there are the `persist` and `from_persist_dir` methods on the `ObjectIndex` that will attempt to persist and load a previously saved `ObjectIndex`, respectively.

### Happy example[¶](https://docs.llamaindex.ai/en/stable/examples/objects/object_index/#happy-example)

In \[ \]:

Copied!

\# persist to disk (no path provided will persist to the default path ./storage)
object\_index.persist()

\# persist to disk (no path provided will persist to the default path ./storage) object\_index.persist()

In \[ \]:

Copied!

\# re-loading (no path provided will attempt to load from the default path ./storage)
reloaded\_object\_index \= ObjectIndex.from\_persist\_dir()

\# re-loading (no path provided will attempt to load from the default path ./storage) reloaded\_object\_index = ObjectIndex.from\_persist\_dir()

In \[ \]:

Copied!

reloaded\_object\_index.\_object\_node\_mapping.obj\_node\_mapping

reloaded\_object\_index.\_object\_node\_mapping.obj\_node\_mapping

Out\[ \]:

{7981070310142320670: {'input': "Hey, how's it going"},
 -5984737625581842527: \['a', 'b', 'c', 'd'\],
 -8305186196625446821: 'llamaindex is an awesome library!'}

In \[ \]:

Copied!

object\_index.\_object\_node\_mapping.obj\_node\_mapping

object\_index.\_object\_node\_mapping.obj\_node\_mapping

Out\[ \]:

{7981070310142320670: {'input': "Hey, how's it going"},
 -5984737625581842527: \['a', 'b', 'c', 'd'\],
 -8305186196625446821: 'llamaindex is an awesome library!'}

### Example of when it doesn't work[¶](https://docs.llamaindex.ai/en/stable/examples/objects/object_index/#example-of-when-it-doesnt-work)

In \[ \]:

Copied!

from llama\_index.core.tools import FunctionTool
from llama\_index.core import SummaryIndex
from llama\_index.core.objects import SimpleToolNodeMapping

def add(a: int, b: int) \-> int:
    """Add two integers and returns the result integer"""
    return a + b

def multiply(a: int, b: int) \-> int:
    """Multiple two integers and returns the result integer"""
    return a \* b

multiply\_tool \= FunctionTool.from\_defaults(fn\=multiply)
add\_tool \= FunctionTool.from\_defaults(fn\=add)

object\_mapping \= SimpleToolNodeMapping.from\_objects(\[add\_tool, multiply\_tool\])
object\_index \= ObjectIndex.from\_objects(
    \[add\_tool, multiply\_tool\], object\_mapping
)

from llama\_index.core.tools import FunctionTool from llama\_index.core import SummaryIndex from llama\_index.core.objects import SimpleToolNodeMapping def add(a: int, b: int) -> int: """Add two integers and returns the result integer""" return a + b def multiply(a: int, b: int) -> int: """Multiple two integers and returns the result integer""" return a \* b multiply\_tool = FunctionTool.from\_defaults(fn=multiply) add\_tool = FunctionTool.from\_defaults(fn=add) object\_mapping = SimpleToolNodeMapping.from\_objects(\[add\_tool, multiply\_tool\]) object\_index = ObjectIndex.from\_objects( \[add\_tool, multiply\_tool\], object\_mapping )

In \[ \]:

Copied!

\# trying to persist the object\_mapping directly will raise an error
object\_mapping.persist()

\# trying to persist the object\_mapping directly will raise an error object\_mapping.persist()

\---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
Cell In\[4\], line 2
      1 \# trying to persist the object\_mapping directly will raise an error
\----> 2 object\_mapping.persist()

File ~/Projects/llama\_index/llama\_index/objects/tool\_node\_mapping.py:47, in BaseToolNodeMapping.persist(self, persist\_dir, obj\_node\_mapping\_fname)
     43 def persist(
     44     self, persist\_dir: str \= ..., obj\_node\_mapping\_fname: str \= ...
     45 ) \-\> None:
     46 """Persist objs."""
\---> 47     raise NotImplementedError("Subclasses should implement this!")

NotImplementedError: Subclasses should implement this!

In \[ \]:

Copied!

\# try to persist the object index here will throw a Warning to the user
object\_index.persist()

\# try to persist the object index here will throw a Warning to the user object\_index.persist()

/var/folders/0g/wd11bmkd791fz7hvgy1kqyp00000gn/T/ipykernel\_77363/46708458.py:2: UserWarning: Unable to persist ObjectNodeMapping. You will need to reconstruct the same object node mapping to build this ObjectIndex
  object\_index.persist()

**In this case, only the index has been persisted.** In order to re-construct the `ObjectIndex` as mentioned above, we will need to manually re-construct `ObjectNodeMapping` and supply that to the `ObjectIndex.from_persist_dir` method.

In \[ \]:

Copied!

reloaded\_object\_index \= ObjectIndex.from\_persist\_dir(
    object\_node\_mapping\=object\_mapping  \# without this, an error will be thrown
)

reloaded\_object\_index = ObjectIndex.from\_persist\_dir( object\_node\_mapping=object\_mapping # without this, an error will be thrown )

Back to top

[Previous RankLLM Reranker Demonstration (Van Gogh Wiki)](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/rankLLM/)[Next Guardrails Output Parsing](https://docs.llamaindex.ai/en/stable/examples/output_parsing/GuardrailsDemo/)

Hi, how can I help you?

🦙
