Title: Upstash Vector Store - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/UpstashVectorDemo/

Markdown Content:
Upstash Vector Store - LlamaIndex


We're going to look at how to use LlamaIndex to interface with Upstash Vector!

In \[ \]:

Copied!

! pip install \-q llama\-index upstash\-vector

! pip install -q llama-index upstash-vector

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.core.vector\_stores import UpstashVectorStore
from llama\_index.core import StorageContext
import textwrap
import openai

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.core.vector\_stores import UpstashVectorStore from llama\_index.core import StorageContext import textwrap import openai

In \[ \]:

Copied!

\# Setup the OpenAI API
openai.api\_key \= "sk-..."

\# Setup the OpenAI API openai.api\_key = "sk-..."

In \[ \]:

Copied!

\# Download data
! mkdir \-p 'data/paul\_graham/'
! wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

\# Download data ! mkdir -p 'data/paul\_graham/' ! wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

\--2024-02-03 20:04:25--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.109.133, 185.199.110.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 75042 (73K) \[text/plain\]
Saving to: ‘data/paul\_graham/paul\_graham\_essay.txt’

data/paul\_graham/pa 100%\[>\]  73.28K  --.-KB/s    in 0.01s   

2024-02-03 20:04:25 (5.96 MB/s) - ‘data/paul\_graham/paul\_graham\_essay.txt’ saved \[75042/75042\]

Now, we can load the documents using the LlamaIndex SimpleDirectoryReader

In \[ \]:

Copied!

documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

print("# Documents:", len(documents))

documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data() print("# Documents:", len(documents))

\# Documents: 1

To create an index on Upstash, visit [https://console.upstash.com/vector](https://console.upstash.com/vector), create an index with 1536 dimensions and `Cosine` distance metric. Copy the URL and token below

In \[ \]:

Copied!

vector\_store \= UpstashVectorStore(url\="https://...", token\="...")

storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    documents, storage\_context\=storage\_context
)

vector\_store = UpstashVectorStore(url="https://...", token="...") storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( documents, storage\_context=storage\_context )

Now we've successfully created an index and populated it with vectors from the essay! The data will take a second to index and then it'll be ready for querying.

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()
res1 \= query\_engine.query("What did the author learn?")
print(textwrap.fill(str(res1), 100))

print("\\n")

res2 \= query\_engine.query("What is the author's opinion on startups?")
print(textwrap.fill(str(res2), 100))

query\_engine = index.as\_query\_engine() res1 = query\_engine.query("What did the author learn?") print(textwrap.fill(str(res1), 100)) print("\\n") res2 = query\_engine.query("What is the author's opinion on startups?") print(textwrap.fill(str(res2), 100))

The author learned that the study of philosophy in college did not live up to their expectations.
They found that other fields took up most of the space of ideas, leaving little room for what they
perceived as the ultimate truths that philosophy was supposed to explore. As a result, they decided
to switch to studying AI.


The author's opinion on startups is that they are in need of help and support, especially in the
beginning stages. The author believes that founders of startups are often helpless and face various
challenges, such as getting incorporated and understanding the intricacies of running a company. The
author's investment firm, Y Combinator, aims to provide seed funding and comprehensive support to
startups, offering them the guidance and resources they need to succeed.

### Metadata Filtering[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/UpstashVectorDemo/#metadata-filtering)

You can pass `MetadataFilters` with your `VectorStoreQuery` to filter the nodes returned from Upstash vector store.

In \[ \]:

Copied!

import os

from llama\_index.vector\_stores.upstash import UpstashVectorStore
from llama\_index.core.vector\_stores.types import (
    MetadataFilter,
    MetadataFilters,
    FilterOperator,
)

vector\_store \= UpstashVectorStore(
    url\=os.environ.get("UPSTASH\_VECTOR\_URL") or "",
    token\=os.environ.get("UPSTASH\_VECTOR\_TOKEN") or "",
)

index \= VectorStoreIndex.from\_vector\_store(vector\_store\=vector\_store)

filters \= MetadataFilters(
    filters\=\[
        MetadataFilter(
            key\="author", value\="Marie Curie", operator\=FilterOperator.EQ
        )
    \],
)

retriever \= index.as\_retriever(filters\=filters)

retriever.retrieve("What is inception about?")

import os from llama\_index.vector\_stores.upstash import UpstashVectorStore from llama\_index.core.vector\_stores.types import ( MetadataFilter, MetadataFilters, FilterOperator, ) vector\_store = UpstashVectorStore( url=os.environ.get("UPSTASH\_VECTOR\_URL") or "", token=os.environ.get("UPSTASH\_VECTOR\_TOKEN") or "", ) index = VectorStoreIndex.from\_vector\_store(vector\_store=vector\_store) filters = MetadataFilters( filters=\[ MetadataFilter( key="author", value="Marie Curie", operator=FilterOperator.EQ ) \], ) retriever = index.as\_retriever(filters=filters) retriever.retrieve("What is inception about?")

We can also combine multiple `MetadataFilters` with `AND` or `OR` condition

In \[ \]:

Copied!

from llama\_index.core.vector\_stores import FilterOperator, FilterCondition

filters \= MetadataFilters(
    filters\=\[
        MetadataFilter(
            key\="theme",
            value\=\["Fiction", "Horror"\],
            operator\=FilterOperator.IN,
        ),
        MetadataFilter(key\="year", value\=1997, operator\=FilterOperator.GT),
    \],
    condition\=FilterCondition.AND,
)

retriever \= index.as\_retriever(filters\=filters)
retriever.retrieve("Harry Potter?")

from llama\_index.core.vector\_stores import FilterOperator, FilterCondition filters = MetadataFilters( filters=\[ MetadataFilter( key="theme", value=\["Fiction", "Horror"\], operator=FilterOperator.IN, ), MetadataFilter(key="year", value=1997, operator=FilterOperator.GT), \], condition=FilterCondition.AND, ) retriever = index.as\_retriever(filters=filters) retriever.retrieve("Harry Potter?")

Back to top

[Previous Typesense Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TypesenseDemo/)[Next VearchDemo](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VearchDemo/)
