Title: Completion Prompts Customization - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/customization/prompts/completion_prompts/

Markdown Content:
Completion Prompts Customization - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai

%pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

Prompt Setup[¶](https://docs.llamaindex.ai/en/stable/examples/customization/prompts/completion_prompts/#prompt-setup)
---------------------------------------------------------------------------------------------------------------------

Below, we take the default prompts and customize them to always answer, even if the context is not helpful.

In \[ \]:

Copied!

from llama\_index.core import PromptTemplate

text\_qa\_template\_str \= (
    "Context information is"
    " below.\\n\---------------------\\n{context\_str}\\n\---------------------\\nUsing"
    " both the context information and also using your own knowledge, answer"
    " the question: {query\_str}\\nIf the context isn't helpful, you can also"
    " answer the question on your own.\\n"
)
text\_qa\_template \= PromptTemplate(text\_qa\_template\_str)

refine\_template\_str \= (
    "The original question is as follows: {query\_str}\\nWe have provided an"
    " existing answer: {existing\_answer}\\nWe have the opportunity to refine"
    " the existing answer (only if needed) with some more context"
    " below.\\n\------------\\n{context\_msg}\\n\------------\\nUsing both the new"
    " context and your own knowledge, update or repeat the existing answer.\\n"
)
refine\_template \= PromptTemplate(refine\_template\_str)

from llama\_index.core import PromptTemplate text\_qa\_template\_str = ( "Context information is" " below.\\n---------------------\\n{context\_str}\\n---------------------\\nUsing" " both the context information and also using your own knowledge, answer" " the question: {query\_str}\\nIf the context isn't helpful, you can also" " answer the question on your own.\\n" ) text\_qa\_template = PromptTemplate(text\_qa\_template\_str) refine\_template\_str = ( "The original question is as follows: {query\_str}\\nWe have provided an" " existing answer: {existing\_answer}\\nWe have the opportunity to refine" " the existing answer (only if needed) with some more context" " below.\\n------------\\n{context\_msg}\\n------------\\nUsing both the new" " context and your own knowledge, update or repeat the existing answer.\\n" ) refine\_template = PromptTemplate(refine\_template\_str)

Using the Prompts[¶](https://docs.llamaindex.ai/en/stable/examples/customization/prompts/completion_prompts/#using-the-prompts)
-------------------------------------------------------------------------------------------------------------------------------

Now, we use the prompts in an index query!

In \[ \]:

Copied!

import openai
import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."
openai.api\_key \= os.environ\["OPENAI\_API\_KEY"\]

import openai import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..." openai.api\_key = os.environ\["OPENAI\_API\_KEY"\]

#### Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/customization/prompts/completion_prompts/#download-data)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.llms.openai import OpenAI

llm \= OpenAI(model\="gpt-3.5-turbo")

documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

index \= VectorStoreIndex.from\_documents(documents)

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.llms.openai import OpenAI llm = OpenAI(model="gpt-3.5-turbo") documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data() index = VectorStoreIndex.from\_documents(documents)

### Before Adding Templates[¶](https://docs.llamaindex.ai/en/stable/examples/customization/prompts/completion_prompts/#before-adding-templates)

In \[ \]:

Copied!

print(index.as\_query\_engine(llm\=llm).query("Who is Joe Biden?"))

print(index.as\_query\_engine(llm=llm).query("Who is Joe Biden?"))

 Joe Biden is not mentioned in the context information.

### After Adding Templates[¶](https://docs.llamaindex.ai/en/stable/examples/customization/prompts/completion_prompts/#after-adding-templates)

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

Joe Biden is the 46th President of the United States. He was elected in 2020 and is the first Democratic president since Barack Obama. He previously served as Vice President under Obama from 2009 to 2017.

Back to top

[Previous Chat Prompts Customization](https://docs.llamaindex.ai/en/stable/examples/customization/prompts/chat_prompts/)[Next Streaming](https://docs.llamaindex.ai/en/stable/examples/customization/streaming/SimpleIndexDemo-streaming/)
