Title: Chat Prompts Customization - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/customization/prompts/chat_prompts/

Markdown Content:
Chat Prompts Customization - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai

%pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

Prompt Setup[¶](https://docs.llamaindex.ai/en/stable/examples/customization/prompts/chat_prompts/#prompt-setup)
---------------------------------------------------------------------------------------------------------------

Below, we take the default prompts and customize them to always answer, even if the context is not helpful.

We show two ways of setting up the prompts:

1.  Explicitly define ChatMessage and MessageRole objects.
2.  Call ChatPromptTemplate.from\_messages

In \[ \]:

Copied!

qa\_prompt\_str \= (
    "Context information is below.\\n"
    "---------------------\\n"
    "{context\_str}\\n"
    "---------------------\\n"
    "Given the context information and not prior knowledge, "
    "answer the question: {query\_str}\\n"
)

refine\_prompt\_str \= (
    "We have the opportunity to refine the original answer "
    "(only if needed) with some more context below.\\n"
    "------------\\n"
    "{context\_msg}\\n"
    "------------\\n"
    "Given the new context, refine the original answer to better "
    "answer the question: {query\_str}. "
    "If the context isn't useful, output the original answer again.\\n"
    "Original Answer: {existing\_answer}"
)

qa\_prompt\_str = ( "Context information is below.\\n" "---------------------\\n" "{context\_str}\\n" "---------------------\\n" "Given the context information and not prior knowledge, " "answer the question: {query\_str}\\n" ) refine\_prompt\_str = ( "We have the opportunity to refine the original answer " "(only if needed) with some more context below.\\n" "------------\\n" "{context\_msg}\\n" "------------\\n" "Given the new context, refine the original answer to better " "answer the question: {query\_str}. " "If the context isn't useful, output the original answer again.\\n" "Original Answer: {existing\_answer}" )

#### 1\. Explicitly Define `ChatMessage` and `MessageRole` objects[¶](https://docs.llamaindex.ai/en/stable/examples/customization/prompts/chat_prompts/#1-explicitly-define-chatmessage-and-messagerole-objects)

In \[ \]:

Copied!

from llama\_index.core.llms import ChatMessage, MessageRole
from llama\_index.core import ChatPromptTemplate

\# Text QA Prompt
chat\_text\_qa\_msgs \= \[
    ChatMessage(
        role\=MessageRole.SYSTEM,
        content\=(
            "Always answer the question, even if the context isn't helpful."
        ),
    ),
    ChatMessage(role\=MessageRole.USER, content\=qa\_prompt\_str),
\]
text\_qa\_template \= ChatPromptTemplate(chat\_text\_qa\_msgs)

\# Refine Prompt
chat\_refine\_msgs \= \[
    ChatMessage(
        role\=MessageRole.SYSTEM,
        content\=(
            "Always answer the question, even if the context isn't helpful."
        ),
    ),
    ChatMessage(role\=MessageRole.USER, content\=refine\_prompt\_str),
\]
refine\_template \= ChatPromptTemplate(chat\_refine\_msgs)

from llama\_index.core.llms import ChatMessage, MessageRole from llama\_index.core import ChatPromptTemplate # Text QA Prompt chat\_text\_qa\_msgs = \[ ChatMessage( role=MessageRole.SYSTEM, content=( "Always answer the question, even if the context isn't helpful." ), ), ChatMessage(role=MessageRole.USER, content=qa\_prompt\_str), \] text\_qa\_template = ChatPromptTemplate(chat\_text\_qa\_msgs) # Refine Prompt chat\_refine\_msgs = \[ ChatMessage( role=MessageRole.SYSTEM, content=( "Always answer the question, even if the context isn't helpful." ), ), ChatMessage(role=MessageRole.USER, content=refine\_prompt\_str), \] refine\_template = ChatPromptTemplate(chat\_refine\_msgs)

#### 2\. Call `ChatPromptTemplate.from_messages`[¶](https://docs.llamaindex.ai/en/stable/examples/customization/prompts/chat_prompts/#2-call-chatprompttemplatefrom_messages)

`from_messages` is syntatic sugar that allows you to define a chat prompt template as a list of tuples, with each tuple corresponding to a chat message ("role", "message").

In \[ \]:

Copied!

from llama\_index.core import ChatPromptTemplate

\# Text QA Prompt
chat\_text\_qa\_msgs \= \[
    (
        "system",
        "Always answer the question, even if the context isn't helpful.",
    ),
    ("user", qa\_prompt\_str),
\]
text\_qa\_template \= ChatPromptTemplate.from\_messages(chat\_text\_qa\_msgs)

\# Refine Prompt
chat\_refine\_msgs \= \[
    (
        "system",
        "Always answer the question, even if the context isn't helpful.",
    ),
    ("user", refine\_prompt\_str),
\]
refine\_template \= ChatPromptTemplate.from\_messages(chat\_refine\_msgs)

from llama\_index.core import ChatPromptTemplate # Text QA Prompt chat\_text\_qa\_msgs = \[ ( "system", "Always answer the question, even if the context isn't helpful.", ), ("user", qa\_prompt\_str), \] text\_qa\_template = ChatPromptTemplate.from\_messages(chat\_text\_qa\_msgs) # Refine Prompt chat\_refine\_msgs = \[ ( "system", "Always answer the question, even if the context isn't helpful.", ), ("user", refine\_prompt\_str), \] refine\_template = ChatPromptTemplate.from\_messages(chat\_refine\_msgs)

Using the Prompts[¶](https://docs.llamaindex.ai/en/stable/examples/customization/prompts/chat_prompts/#using-the-prompts)
-------------------------------------------------------------------------------------------------------------------------

Now, we use the prompts in an index query!

In \[ \]:

Copied!

import openai
import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."
openai.api\_key \= os.environ\["OPENAI\_API\_KEY"\]

import openai import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..." openai.api\_key = os.environ\["OPENAI\_API\_KEY"\]

#### Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/customization/prompts/chat_prompts/#download-data)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.llms.openai import OpenAI

documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

\# Create an index using a chat model, so that we can use the chat prompts!
llm \= OpenAI(model\="gpt-3.5-turbo", temperature\=0.1)

index \= VectorStoreIndex.from\_documents(documents)

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.llms.openai import OpenAI documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data() # Create an index using a chat model, so that we can use the chat prompts! llm = OpenAI(model="gpt-3.5-turbo", temperature=0.1) index = VectorStoreIndex.from\_documents(documents)

### Before Adding Templates[¶](https://docs.llamaindex.ai/en/stable/examples/customization/prompts/chat_prompts/#before-adding-templates)

In \[ \]:

Copied!

print(index.as\_query\_engine(llm\=llm).query("Who is Joe Biden?"))

print(index.as\_query\_engine(llm=llm).query("Who is Joe Biden?"))

I'm unable to provide an answer to that question based on the context information provided.

### After Adding Templates[¶](https://docs.llamaindex.ai/en/stable/examples/customization/prompts/chat_prompts/#after-adding-templates)

In \[ \]:

Copied!

print(
    index.as\_query\_engine(
        text\_qa\_template\=text\_qa\_template,
        refine\_template\=refine\_template,
        llm\=llm,
    ).query("Who is Joe Biden?")
)

print( index.as\_query\_engine( text\_qa\_template=text\_qa\_template, refine\_template=refine\_template, llm=llm, ).query("Who is Joe Biden?") )

Joe Biden is the current President of the United States, having taken office in January 2021. He previously served as Vice President under President Barack Obama from 2009 to 2017.

Back to top

[Previous HuggingFace LLM - StableLM](https://docs.llamaindex.ai/en/stable/examples/customization/llms/SimpleIndexDemo-Huggingface_stablelm/)[Next Completion Prompts Customization](https://docs.llamaindex.ai/en/stable/examples/customization/prompts/completion_prompts/)
