Title: Defining a Custom Query Engine

URL Source: https://docs.llamaindex.ai/en/stable/examples/query_engine/custom_query_engine/

Markdown Content:
Defining a Custom Query Engine - LlamaIndex


You can (and should) define your custom query engines in order to plug into your downstream LlamaIndex workflows, whether you're building RAG, agents, or other applications.

We provide a `CustomQueryEngine` that makes it easy to define your own queries.

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/custom_query_engine/#setup)
-----------------------------------------------------------------------------------------------

We first load some sample data and index it.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai

%pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data//paul\_graham/").load\_data()

\# load documents documents = SimpleDirectoryReader("./data//paul\_graham/").load\_data()

In \[ \]:

Copied!

index \= VectorStoreIndex.from\_documents(documents)
retriever \= index.as\_retriever()

index = VectorStoreIndex.from\_documents(documents) retriever = index.as\_retriever()

Building a Custom Query Engine[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/custom_query_engine/#building-a-custom-query-engine)
-------------------------------------------------------------------------------------------------------------------------------------------------

We build a custom query engine that simulates a RAG pipeline. First perform retrieval, and then synthesis.

To define a `CustomQueryEngine`, you just have to define some initialization parameters as attributes and implement the `custom_query` function.

By default, the `custom_query` can return a `Response` object (which the response synthesizer returns), but it can also just return a string. These are options 1 and 2 respectively.

In \[ \]:

Copied!

from llama\_index.core.query\_engine import CustomQueryEngine
from llama\_index.core.retrievers import BaseRetriever
from llama\_index.core import get\_response\_synthesizer
from llama\_index.core.response\_synthesizers import BaseSynthesizer

from llama\_index.core.query\_engine import CustomQueryEngine from llama\_index.core.retrievers import BaseRetriever from llama\_index.core import get\_response\_synthesizer from llama\_index.core.response\_synthesizers import BaseSynthesizer

### Option 1 (`RAGQueryEngine`)[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/custom_query_engine/#option-1-ragqueryengine)

In \[ \]:

Copied!

class RAGQueryEngine(CustomQueryEngine):
    """RAG Query Engine."""

    retriever: BaseRetriever
    response\_synthesizer: BaseSynthesizer

    def custom\_query(self, query\_str: str):
        nodes \= self.retriever.retrieve(query\_str)
        response\_obj \= self.response\_synthesizer.synthesize(query\_str, nodes)
        return response\_obj

class RAGQueryEngine(CustomQueryEngine): """RAG Query Engine.""" retriever: BaseRetriever response\_synthesizer: BaseSynthesizer def custom\_query(self, query\_str: str): nodes = self.retriever.retrieve(query\_str) response\_obj = self.response\_synthesizer.synthesize(query\_str, nodes) return response\_obj

### Option 2 (`RAGStringQueryEngine`)[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/custom_query_engine/#option-2-ragstringqueryengine)

In \[ \]:

Copied!

\# Option 2: return a string (we use a raw LLM call for illustration)

from llama\_index.llms.openai import OpenAI
from llama\_index.core import PromptTemplate

qa\_prompt \= PromptTemplate(
    "Context information is below.\\n"
    "---------------------\\n"
    "{context\_str}\\n"
    "---------------------\\n"
    "Given the context information and not prior knowledge, "
    "answer the query.\\n"
    "Query: {query\_str}\\n"
    "Answer: "
)

class RAGStringQueryEngine(CustomQueryEngine):
    """RAG String Query Engine."""

    retriever: BaseRetriever
    response\_synthesizer: BaseSynthesizer
    llm: OpenAI
    qa\_prompt: PromptTemplate

    def custom\_query(self, query\_str: str):
        nodes \= self.retriever.retrieve(query\_str)

        context\_str \= "\\n\\n".join(\[n.node.get\_content() for n in nodes\])
        response \= self.llm.complete(
            qa\_prompt.format(context\_str\=context\_str, query\_str\=query\_str)
        )

        return str(response)

\# Option 2: return a string (we use a raw LLM call for illustration) from llama\_index.llms.openai import OpenAI from llama\_index.core import PromptTemplate qa\_prompt = PromptTemplate( "Context information is below.\\n" "---------------------\\n" "{context\_str}\\n" "---------------------\\n" "Given the context information and not prior knowledge, " "answer the query.\\n" "Query: {query\_str}\\n" "Answer: " ) class RAGStringQueryEngine(CustomQueryEngine): """RAG String Query Engine.""" retriever: BaseRetriever response\_synthesizer: BaseSynthesizer llm: OpenAI qa\_prompt: PromptTemplate def custom\_query(self, query\_str: str): nodes = self.retriever.retrieve(query\_str) context\_str = "\\n\\n".join(\[n.node.get\_content() for n in nodes\]) response = self.llm.complete( qa\_prompt.format(context\_str=context\_str, query\_str=query\_str) ) return str(response)

Trying it out[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/custom_query_engine/#trying-it-out)
---------------------------------------------------------------------------------------------------------------

We now try it out on our sample data.

### Trying Option 1 (`RAGQueryEngine`)[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/custom_query_engine/#trying-option-1-ragqueryengine)

In \[ \]:

Copied!

synthesizer \= get\_response\_synthesizer(response\_mode\="compact")
query\_engine \= RAGQueryEngine(
    retriever\=retriever, response\_synthesizer\=synthesizer
)

synthesizer = get\_response\_synthesizer(response\_mode="compact") query\_engine = RAGQueryEngine( retriever=retriever, response\_synthesizer=synthesizer )

In \[ \]:

Copied!

response \= query\_engine.query("What did the author do growing up?")

response = query\_engine.query("What did the author do growing up?")

In \[ \]:

Copied!

print(str(response))

print(str(response))

The author worked on writing and programming outside of school before college. They wrote short stories and tried writing programs on an IBM 1401 computer using an early version of Fortran. They also mentioned getting a microcomputer, building it themselves, and writing simple games and programs on it.

In \[ \]:

Copied!

print(response.source\_nodes\[0\].get\_content())

print(response.source\_nodes\[0\].get\_content())

### Trying Option 2 (`RAGStringQueryEngine`)[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/custom_query_engine/#trying-option-2-ragstringqueryengine)

In \[ \]:

Copied!

llm \= OpenAI(model\="gpt-3.5-turbo")

query\_engine \= RAGStringQueryEngine(
    retriever\=retriever,
    response\_synthesizer\=synthesizer,
    llm\=llm,
    qa\_prompt\=qa\_prompt,
)

llm = OpenAI(model="gpt-3.5-turbo") query\_engine = RAGStringQueryEngine( retriever=retriever, response\_synthesizer=synthesizer, llm=llm, qa\_prompt=qa\_prompt, )

In \[ \]:

Copied!

response \= query\_engine.query("What did the author do growing up?")

response = query\_engine.query("What did the author do growing up?")

In \[ \]:

Copied!

print(str(response))

print(str(response))

The author worked on writing and programming before college. They wrote short stories and started programming on the IBM 1401 computer in 9th grade. They later got a microcomputer and continued programming, writing simple games and a word processor.

Back to top

[Previous Cogniswitch query engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/cogniswitch_query_engine/)[Next Ensemble Query Engine Guide](https://docs.llamaindex.ai/en/stable/examples/query_engine/ensemble_query_engine/)

Hi, how can I help you?

🦙
