Title: Chat Engine - Condense Plus Context Mode

URL Source: https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_condense_plus_context/

Markdown Content:
Chat Engine - Condense Plus Context Mode - LlamaIndex


This is a multi-step chat mode built on top of a retriever over your data.

For each chat interaction:

*   First condense a conversation and latest user message to a standalone question
*   Then build a context for the standalone question from a retriever,
*   Then pass the context along with prompt and user message to LLM to generate a response.

This approach is simple, and works for questions directly related to the knowledge base and general interactions.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai

%pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_condense_plus_context/#download-data)
----------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

Get started in 5 lines of code[¶](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_condense_plus_context/#get-started-in-5-lines-of-code)
--------------------------------------------------------------------------------------------------------------------------------------------------------------

Load data and build index

In \[ \]:

Copied!

import openai
import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."
openai.api\_key \= os.environ\["OPENAI\_API\_KEY"\]

import openai import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..." openai.api\_key = os.environ\["OPENAI\_API\_KEY"\]

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.llms.openai import OpenAI

llm \= OpenAI(model\="gpt-3.5-turbo")
data \= SimpleDirectoryReader(input\_dir\="./data/paul\_graham/").load\_data()
index \= VectorStoreIndex.from\_documents(data)

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.llms.openai import OpenAI llm = OpenAI(model="gpt-3.5-turbo") data = SimpleDirectoryReader(input\_dir="./data/paul\_graham/").load\_data() index = VectorStoreIndex.from\_documents(data)

Configure chat engine

Since the context retrieved can take up a large amount of the available LLM context, let's ensure we configure a smaller limit to the chat history!

In \[ \]:

Copied!

from llama\_index.core.memory import ChatMemoryBuffer

memory \= ChatMemoryBuffer.from\_defaults(token\_limit\=3900)

chat\_engine \= index.as\_chat\_engine(
    chat\_mode\="condense\_plus\_context",
    memory\=memory,
    llm\=llm,
    context\_prompt\=(
        "You are a chatbot, able to have normal interactions, as well as talk"
        " about an essay discussing Paul Grahams life."
        "Here are the relevant documents for the context:\\n"
        "{context\_str}"
        "\\nInstruction: Use the previous chat history, or the context above, to interact and help the user."
    ),
    verbose\=False,
)

from llama\_index.core.memory import ChatMemoryBuffer memory = ChatMemoryBuffer.from\_defaults(token\_limit=3900) chat\_engine = index.as\_chat\_engine( chat\_mode="condense\_plus\_context", memory=memory, llm=llm, context\_prompt=( "You are a chatbot, able to have normal interactions, as well as talk" " about an essay discussing Paul Grahams life." "Here are the relevant documents for the context:\\n" "{context\_str}" "\\nInstruction: Use the previous chat history, or the context above, to interact and help the user." ), verbose=False, )

Chat with your data

In \[ \]:

Copied!

response \= chat\_engine.chat("What did Paul Graham do growing up")

response = chat\_engine.chat("What did Paul Graham do growing up")

In \[ \]:

Copied!

print(response)

print(response)

Growing up, Paul Graham had two main interests: writing and programming. He started by writing short stories, although he admits that they were not very good. In terms of programming, he began working with computers in 9th grade when he had access to an IBM 1401 at his school. He used an early version of Fortran to write programs on punch cards for the 1401. However, he found it challenging to figure out what to do with the machine since the only input option was data stored on punched cards. Later, with the advent of microcomputers, he became more involved in programming and got his own TRS-80 computer. He wrote simple games, a program to predict rocket heights, and even a word processor. Despite his interest in programming, he initially planned to study philosophy in college but eventually switched to AI.

Ask a follow up question

In \[ \]:

Copied!

response\_2 \= chat\_engine.chat("Can you tell me more?")

response\_2 = chat\_engine.chat("Can you tell me more?")

In \[ \]:

Copied!

print(response\_2)

print(response\_2)

Certainly! After Paul Graham switched his focus from philosophy to AI in college, he became fascinated with the field. AI, or artificial intelligence, was gaining attention in the mid-1980s, and Graham was particularly inspired by a novel called "The Moon is a Harsh Mistress" by Robert A. Heinlein, which featured an intelligent computer named Mike. He also saw a PBS documentary showcasing Terry Winograd using a program called SHRDLU, which further fueled his interest in AI.

Graham believed that AI was on the verge of significant advancements, and he wanted to be a part of it. He saw the potential for intelligent machines and the impact they could have on society. This passion for AI led him to pursue it as a field of study and work.

Throughout his journey, Graham continued to explore programming and writing. He wrote numerous essays on various topics and even published a collection of them in a book called "Hackers & Painters." He also worked on spam filters and continued his interest in painting.

Graham's experiences with writing, programming, and his fascination with AI eventually led him to co-found Viaweb, an early e-commerce platform, which was later acquired by Yahoo. This venture marked the beginning of his entrepreneurial career and set the stage for his future endeavors, including the founding of Y Combinator, a renowned startup accelerator.

Overall, Graham's upbringing and early interests in writing and programming played a significant role in shaping his path, leading him to become a successful entrepreneur, investor, and influential figure in the tech industry.

Reset conversation state

In \[ \]:

Copied!

chat\_engine.reset()

chat\_engine.reset()

In \[ \]:

Copied!

response \= chat\_engine.chat("Hello! What do you know?")

response = chat\_engine.chat("Hello! What do you know?")

In \[ \]:

Copied!

print(response)

print(response)

Hello! I'm a chatbot here to help you with any questions or topics you'd like to discuss. Is there something specific you'd like to know or talk about?

Streaming Support[¶](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_condense_plus_context/#streaming-support)
------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.llms.openai import OpenAI
from llama\_index.core import Settings

llm \= OpenAI(model\="gpt-3.5-turbo", temperature\=0)
Settings.llm \= llm
data \= SimpleDirectoryReader(input\_dir\="./data/paul\_graham/").load\_data()
index \= VectorStoreIndex.from\_documents(data)

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.llms.openai import OpenAI from llama\_index.core import Settings llm = OpenAI(model="gpt-3.5-turbo", temperature=0) Settings.llm = llm data = SimpleDirectoryReader(input\_dir="./data/paul\_graham/").load\_data() index = VectorStoreIndex.from\_documents(data)

In \[ \]:

Copied!

chat\_engine \= index.as\_chat\_engine(
    chat\_mode\="condense\_plus\_context",
    context\_prompt\=(
        "You are a chatbot, able to have normal interactions, as well as talk"
        " about an essay discussing Paul Grahams life."
        "Here are the relevant documents for the context:\\n"
        "{context\_str}"
        "\\nInstruction: Based on the above documents, provide a detailed answer for the user question below."
    ),
)

chat\_engine = index.as\_chat\_engine( chat\_mode="condense\_plus\_context", context\_prompt=( "You are a chatbot, able to have normal interactions, as well as talk" " about an essay discussing Paul Grahams life." "Here are the relevant documents for the context:\\n" "{context\_str}" "\\nInstruction: Based on the above documents, provide a detailed answer for the user question below." ), )

In \[ \]:

Copied!

response \= chat\_engine.stream\_chat("What did Paul Graham do after YC?")
for token in response.response\_gen:
    print(token, end\="")

response = chat\_engine.stream\_chat("What did Paul Graham do after YC?") for token in response.response\_gen: print(token, end="")

After Y Combinator (YC), Paul Graham made a significant decision to step back from his role in YC and pursue other endeavors. In 2012, his mother had a stroke caused by colon cancer, which led him to reevaluate his priorities. He realized that YC was consuming more of his attention and that he was ready to hand over the reins to someone else.

Paul approached Jessica Livingston, his wife and co-founder of YC, to see if she wanted to become the president of YC, but she declined. They then decided to recruit Sam Altman, who was a successful entrepreneur and had been involved with YC as a founder. They also involved Robert Morris and Trevor Blackwell, who were original partners in YC.

To ensure the long-term success of YC, they decided to reorganize the company. Previously, YC had been controlled by the original LLC formed by the four founders. However, they wanted to ensure that YC would continue to thrive even without their direct control. If Sam accepted the offer, he would be given the opportunity to reorganize YC, with Paul and Robert retiring and Jessica and Trevor becoming ordinary partners.

After persistent persuasion, Sam agreed to become the president of YC in October 2013, and the transition began with the winter 2014 batch. During the rest of 2013, Paul gradually handed over the responsibilities of running YC to Sam, allowing him to learn the job while Paul focused on his mother, who was battling cancer.

It is worth noting that Paul Graham's decision to step back from YC was influenced by the advice of Robert Morris, who suggested that YC should not be the last cool thing Paul does. This advice made Paul realize that he wanted to explore other opportunities and not be solely defined by his work at YC.

Back to top

[Previous Chat Engine - Best Mode](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_best/)[Next Chat Engine - Condense Question Mode](https://docs.llamaindex.ai/en/stable/examples/chat_engine/chat_engine_condense_question/)
