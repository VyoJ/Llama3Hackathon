Title: Chat Engine - Condense Question Mode

URL Source: https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_condense_question/

Markdown Content:
Chat Engine - Condense Question Mode - LlamaIndex


Condense question is a simple chat mode built on top of a query engine over your data.

For each chat interaction:

*   first generate a standalone question from conversation context and last message, then
*   query the query engine with the condensed question for a response.

This approach is simple, and works for questions directly related to the knowledge base. Since it _always_ queries the knowledge base, it can have difficulty answering meta questions like "what did I ask you before?"

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai

%pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_condense_question/#download-data)
------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

Get started in 5 lines of code[¶](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_condense_question/#get-started-in-5-lines-of-code)
----------------------------------------------------------------------------------------------------------------------------------------------------------

Load data and build index

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader

data \= SimpleDirectoryReader(input\_dir\="./data/paul\_graham/").load\_data()
index \= VectorStoreIndex.from\_documents(data)

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader data = SimpleDirectoryReader(input\_dir="./data/paul\_graham/").load\_data() index = VectorStoreIndex.from\_documents(data)

Configure chat engine

In \[ \]:

Copied!

chat\_engine \= index.as\_chat\_engine(chat\_mode\="condense\_question", verbose\=True)

chat\_engine = index.as\_chat\_engine(chat\_mode="condense\_question", verbose=True)

Chat with your data

In \[ \]:

Copied!

response \= chat\_engine.chat("What did Paul Graham do after YC?")

response = chat\_engine.chat("What did Paul Graham do after YC?")

Querying with: What was the next step in Paul Graham's career after his involvement with Y Combinator?

In \[ \]:

Copied!

print(response)

print(response)

Paul Graham's next step in his career after his involvement with Y Combinator was to take up painting. He spent most of the rest of 2014 painting and then in March 2015 he started working on Lisp again.

Ask a follow up question

In \[ \]:

Copied!

response \= chat\_engine.chat("What about after that?")

response = chat\_engine.chat("What about after that?")

Querying with: What did Paul Graham do after he started working on Lisp again in March 2015?

In \[ \]:

Copied!

print(response)

print(response)

Paul Graham spent the rest of 2015 writing essays and working on his new dialect of Lisp, which he called Arc. He also looked for an apartment to buy and started planning a second still life painting from the same objects.

In \[ \]:

Copied!

response \= chat\_engine.chat("Can you tell me more?")

response = chat\_engine.chat("Can you tell me more?")

Querying with: What did Paul Graham do after he started working on Lisp again in March 2015?

In \[ \]:

Copied!

print(response)

print(response)

Paul Graham spent the rest of 2015 writing essays and working on his new dialect of Lisp, which he called Arc. He also looked for an apartment to buy and started planning for a second still life painting.

Reset conversation state

In \[ \]:

Copied!

chat\_engine.reset()

chat\_engine.reset()

In \[ \]:

Copied!

response \= chat\_engine.chat("What about after that?")

response = chat\_engine.chat("What about after that?")

Querying with: What happens after the current situation?

In \[ \]:

Copied!

print(response)

print(response)

After the current situation, the narrator resumes painting and experimenting with a new kind of still life. He also resumes his old life in New York, now that he is rich. He is able to take taxis and eat in restaurants, which is exciting for a while. He also starts to make connections with other people who are trying to paint in New York.

Streaming Support[¶](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_condense_question/#streaming-support)
--------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.llms.openai import OpenAI

llm \= OpenAI(model\="gpt-3.5-turbo", temperature\=0)

data \= SimpleDirectoryReader(input\_dir\="../data/paul\_graham/").load\_data()

index \= VectorStoreIndex.from\_documents(data)

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.llms.openai import OpenAI llm = OpenAI(model="gpt-3.5-turbo", temperature=0) data = SimpleDirectoryReader(input\_dir="../data/paul\_graham/").load\_data() index = VectorStoreIndex.from\_documents(data)

In \[ \]:

Copied!

chat\_engine \= index.as\_chat\_engine(
    chat\_mode\="condense\_question", llm\=llm, verbose\=True
)

chat\_engine = index.as\_chat\_engine( chat\_mode="condense\_question", llm=llm, verbose=True )

In \[ \]:

Copied!

response \= chat\_engine.stream\_chat("What did Paul Graham do after YC?")
for token in response.response\_gen:
    print(token, end\="")

response = chat\_engine.stream\_chat("What did Paul Graham do after YC?") for token in response.response\_gen: print(token, end="")

Querying with: What did Paul Graham do after leaving YC?
After leaving YC, Paul Graham started painting and focused on improving his skills in that area. He then started writing essays again and began working on Lisp.

Back to top

[Previous Chat Engine - Condense Plus Context Mode](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_condense_plus_context/)[Next Chat Engine - Context Mode](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_context/)
