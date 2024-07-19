Title: Firestore Vector Store - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/FirestoreVectorStore/

Markdown Content:
Firestore Vector Store - LlamaIndex


Google Firestore (Native Mode)[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/FirestoreVectorStore/#google-firestore-native-mode)


### Initialize FirestoreVectorStore[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/FirestoreVectorStore/#initialize-firestorevectorstore)

`FirestoreVectroStore` allows you to load data into Firestore and query it.

In \[ \]:

Copied!

\# @markdown Please specify a source for demo purpose.
COLLECTION\_NAME \= "test\_collection"

\# @markdown Please specify a source for demo purpose. COLLECTION\_NAME = "test\_collection"

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

\# Load documents and build index
documents \= SimpleDirectoryReader(
    "../../examples/data/paul\_graham"
).load\_data()

from llama\_index.core import SimpleDirectoryReader # Load documents and build index documents = SimpleDirectoryReader( "../../examples/data/paul\_graham" ).load\_data()

In \[ \]:

Copied!

from llama\_index.embeddings.huggingface import HuggingFaceEmbedding
from llama\_index.core import Settings

\# Set the embedding model, this is a local model
embed\_model \= HuggingFaceEmbedding(model\_name\="BAAI/bge-small-en-v1.5")

from llama\_index.embeddings.huggingface import HuggingFaceEmbedding from llama\_index.core import Settings # Set the embedding model, this is a local model embed\_model = HuggingFaceEmbedding(model\_name="BAAI/bge-small-en-v1.5")

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex
from llama\_index.core import StorageContext, ServiceContext

from llama\_index.vector\_stores.firestore import FirestoreVectorStore

\# Create a Firestore vector store
store \= FirestoreVectorStore(collection\_name\=COLLECTION\_NAME)

storage\_context \= StorageContext.from\_defaults(vector\_store\=store)
service\_context \= ServiceContext.from\_defaults(
    llm\=None, embed\_model\=embed\_model
)

index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context, service\_context\=service\_context
)

from llama\_index.core import VectorStoreIndex from llama\_index.core import StorageContext, ServiceContext from llama\_index.vector\_stores.firestore import FirestoreVectorStore # Create a Firestore vector store store = FirestoreVectorStore(collection\_name=COLLECTION\_NAME) storage\_context = StorageContext.from\_defaults(vector\_store=store) service\_context = ServiceContext.from\_defaults( llm=None, embed\_model=embed\_model ) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context, service\_context=service\_context )

/var/folders/mh/cqn7wzgs3j79rbg243\_gfcx80000gn/T/ipykernel\_29666/1668628626.py:10: DeprecationWarning: Call to deprecated class method from\_defaults. (ServiceContext is deprecated, please use \`llama\_index.settings.Settings\` instead.) -- Deprecated since version 0.10.0.
  service\_context = ServiceContext.from\_defaults(llm=None, embed\_model=embed\_model)

LLM is explicitly disabled. Using MockLLM.

### Perform search[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/FirestoreVectorStore/#perform-search)

You can use the `FirestoreVectorStore` to perform similarity searches on the vectors you have stored. This is useful for finding similar documents or text.

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()
res \= query\_engine.query("What did the author do growing up?")
print(str(res.source\_nodes\[0\].text))

query\_engine = index.as\_query\_engine() res = query\_engine.query("What did the author do growing up?") print(str(res.source\_nodes\[0\].text))

None
What I Worked On

February 2021

Before college the two main things I worked on, outside of school, were writing and programming. I didn't write essays. I wrote what beginning writers were supposed to write then, and probably still are: short stories. My stories were awful. They had hardly any plot, just characters with strong feelings, which I imagined made them deep.

The first programs I tried writing were on the IBM 1401 that our school district used for what was then called "data processing." This was in 9th grade, so I was 13 or 14. The school district's 1401 happened to be in the basement of our junior high school, and my friend Rich Draves and I got permission to use it. It was like a mini Bond villain's lair down there, with all these alien-looking machines — CPU, disk drives, printer, card reader — sitting up on a raised floor under bright fluorescent lights.

The language we used was an early version of Fortran. You had to type programs on punch cards, then stack them in the card reader and press a button to load the program into memory and run it. The result would ordinarily be to print something on the spectacularly loud printer.

I was puzzled by the 1401. I couldn't figure out what to do with it. And in retrospect there's not much I could have done with it. The only form of input to programs was data stored on punched cards, and I didn't have any data stored on punched cards. The only other option was to do things that didn't rely on any input, like calculate approximations of pi, but I didn't know enough math to do anything interesting of that type. So I'm not surprised I can't remember any programs I wrote, because they can't have done much. My clearest memory is of the moment I learned it was possible for programs not to terminate, when one of mine didn't. On a machine without time-sharing, this was a social as well as a technical error, as the data center manager's expression made clear.

With microcomputers, everything changed. Now you could have a computer sitting right in front of you, on a desk, that could respond to your keystrokes as it was running instead of just churning through a stack of punch cards and then stopping. \[1\]

The first of my friends to get a microcomputer built it himself. It was sold as a kit by Heathkit. I remember vividly how impressed and envious I felt watching him sitting in front of it, typing programs right into the computer.

Computers were expensive in those days and it took me years of nagging before I convinced my father to buy one, a TRS-80, in about 1980. The gold standard then was the Apple II, but a TRS-80 was good enough. This was when I really started programming. I wrote simple games, a program to predict how high my model rockets would fly, and a word processor that my father used to write at least one book. There was only room in memory for about 2 pages of text, so he'd write 2 pages at a time and then print them out, but it was a lot better than a typewriter.

Though I liked programming, I didn't plan to study it in college. In college I was going to study philosophy, which sounded much more powerful. It seemed, to my naive high school self, to be the study of the ultimate truths, compared to which the things studied in other fields would be mere domain knowledge. What I discovered when I got to college was that the other fields took up so much of the space of ideas that there wasn't much left for these supposed ultimate truths. All that seemed left for philosophy were edge cases that people in other fields felt could safely be ignored.

I couldn't have put this into words when I was 18. All I knew at the time was that I kept taking philosophy courses and they kept being boring. So I decided to switch to AI.

AI was in the air in the mid 1980s, but there were two things especially that made me want to work on it: a novel by Heinlein called The Moon is a Harsh Mistress, which featured an intelligent computer called Mike, and a PBS documentary that showed Terry Winograd using SHRDLU. I haven't tried rereading The Moon is a Harsh Mistress, so I don't know how well it has aged, but when I read it I was drawn entirely into its world.

You can apply pre-filtering to the search results by specifying a `filters` argument.

In \[ \]:

Copied!

from llama\_index.core.vector\_stores.types import (
    MetadataFilters,
    ExactMatchFilter,
    MetadataFilter,
)

filters \= MetadataFilters(
    filters\=\[MetadataFilter(key\="author", value\="Paul Graham")\]
)
query\_engine \= index.as\_query\_engine(filters\=filters)
res \= query\_engine.query("What did the author do growing up?")
print(str(res.source\_nodes\[0\].text))

from llama\_index.core.vector\_stores.types import ( MetadataFilters, ExactMatchFilter, MetadataFilter, ) filters = MetadataFilters( filters=\[MetadataFilter(key="author", value="Paul Graham")\] ) query\_engine = index.as\_query\_engine(filters=filters) res = query\_engine.query("What did the author do growing up?") print(str(res.source\_nodes\[0\].text))

Back to top

[Previous Faiss Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/FaissIndexDemo/)[Next Hologres](https://docs.llamaindex.ai/en/stable/examples/vector_stores/HologresDemo/)
