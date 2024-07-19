Title: Pydantic Tree Summarize - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/custom_prompt_synthesizer/

Markdown Content:
Pydantic Tree Summarize - LlamaIndex


In this notebook, we demonstrate how to use tree summarize with structured outputs. Specifically, tree summarize is used to output pydantic objects.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import os
import openai

import os import openai

In \[ \]:

Copied!

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."
openai.api\_key \= os.environ\["OPENAI\_API\_KEY"\]

os.environ\["OPENAI\_API\_KEY"\] = "sk-..." openai.api\_key = os.environ\["OPENAI\_API\_KEY"\]

Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/custom_prompt_synthesizer/#download-data)
------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/custom_prompt_synthesizer/#load-data)
----------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

from llama\_index.core import SimpleDirectoryReader

In \[ \]:

Copied!

reader \= SimpleDirectoryReader(
    input\_files\=\["./data/paul\_graham/paul\_graham\_essay.txt"\]
)

reader = SimpleDirectoryReader( input\_files=\["./data/paul\_graham/paul\_graham\_essay.txt"\] )

In \[ \]:

Copied!

docs \= reader.load\_data()

docs = reader.load\_data()

In \[ \]:

Copied!

text \= docs\[0\].text

text = docs\[0\].text

Define Custom Prompt[¶](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/custom_prompt_synthesizer/#define-custom-prompt)
--------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core import PromptTemplate

from llama\_index.core import PromptTemplate

In \[ \]:

Copied!

\# NOTE: we add an extra tone\_name variable here
qa\_prompt\_tmpl \= (
    "Context information is below.\\n"
    "---------------------\\n"
    "{context\_str}\\n"
    "---------------------\\n"
    "Given the context information and not prior knowledge, "
    "answer the query.\\n"
    "Please also write the answer in the style of {tone\_name}.\\n"
    "Query: {query\_str}\\n"
    "Answer: "
)
qa\_prompt \= PromptTemplate(qa\_prompt\_tmpl)

refine\_prompt\_tmpl \= (
    "The original query is as follows: {query\_str}\\n"
    "We have provided an existing answer: {existing\_answer}\\n"
    "We have the opportunity to refine the existing answer "
    "(only if needed) with some more context below.\\n"
    "------------\\n"
    "{context\_msg}\\n"
    "------------\\n"
    "Given the new context, refine the original answer to better "
    "answer the query. "
    "Please also write the answer in the style of {tone\_name}.\\n"
    "If the context isn't useful, return the original answer.\\n"
    "Refined Answer: "
)
refine\_prompt \= PromptTemplate(refine\_prompt\_tmpl)

\# NOTE: we add an extra tone\_name variable here qa\_prompt\_tmpl = ( "Context information is below.\\n" "---------------------\\n" "{context\_str}\\n" "---------------------\\n" "Given the context information and not prior knowledge, " "answer the query.\\n" "Please also write the answer in the style of {tone\_name}.\\n" "Query: {query\_str}\\n" "Answer: " ) qa\_prompt = PromptTemplate(qa\_prompt\_tmpl) refine\_prompt\_tmpl = ( "The original query is as follows: {query\_str}\\n" "We have provided an existing answer: {existing\_answer}\\n" "We have the opportunity to refine the existing answer " "(only if needed) with some more context below.\\n" "------------\\n" "{context\_msg}\\n" "------------\\n" "Given the new context, refine the original answer to better " "answer the query. " "Please also write the answer in the style of {tone\_name}.\\n" "If the context isn't useful, return the original answer.\\n" "Refined Answer: " ) refine\_prompt = PromptTemplate(refine\_prompt\_tmpl)

Try out Response Synthesis with Custom Prompt[¶](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/custom_prompt_synthesizer/#try-out-response-synthesis-with-custom-prompt)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We try out a few different response synthesis strategies with the custom prompt.

In \[ \]:

Copied!

from llama\_index.core.response\_synthesizers import TreeSummarize, Refine
from llama\_index.core.types import BaseModel
from typing import List

from llama\_index.core.response\_synthesizers import TreeSummarize, Refine from llama\_index.core.types import BaseModel from typing import List

In \[ \]:

Copied!

summarizer \= TreeSummarize(verbose\=True, summary\_template\=qa\_prompt)

summarizer = TreeSummarize(verbose=True, summary\_template=qa\_prompt)

In \[ \]:

Copied!

response \= summarizer.get\_response(
    "who is Paul Graham?", \[text\], tone\_name\="a Shakespeare play"
)

response = summarizer.get\_response( "who is Paul Graham?", \[text\], tone\_name="a Shakespeare play" )

5 text chunks after repacking
1 text chunks after repacking

In \[ \]:

Copied!

print(str(response))

print(str(response))

Paul Graham, a noble and esteemed gentleman, is a man of many talents and accomplishments. He hath traversed the realms of art, entrepreneurship, and writing, leaving a lasting impact on each. With his brush, he hath brought life to canvases, capturing the essence of what he saw. In the realm of technology, he hath revolutionized the way we do business, founding Viaweb and bringing the power of the web to entrepreneurs and artists alike. His wisdom and guidance hath shaped the future of technology and entrepreneurship through his co-founding of Y Combinator. But above all, Paul Graham is a visionary, a trailblazer, and a true Renaissance man, whose intellectual curiosity and quest for lasting creation hath inspired generations to come.

In \[ \]:

Copied!

summarizer \= Refine(
    verbose\=True, text\_qa\_template\=qa\_prompt, refine\_template\=refine\_prompt
)

summarizer = Refine( verbose=True, text\_qa\_template=qa\_prompt, refine\_template=refine\_prompt )

In \[ \]:

Copied!

response \= summarizer.get\_response(
    "who is Paul Graham?", \[text\], tone\_name\="a haiku"
)

response = summarizer.get\_response( "who is Paul Graham?", \[text\], tone\_name="a haiku" )

\> Refine context: made a living from a combination of modelling a...
> Refine context: to have studied art, because the main goal of a...
> Refine context: I had been intimately involved with building th...
> Refine context: I didn't understand what he meant, but graduall...

In \[ \]:

Copied!

print(str(response))

print(str(response))

Paul Graham, a web pioneer,
Co-founded Y Combinator,
But stepped down to ensure,
Long-term success and more.

In \[ \]:

Copied!

\# try with pydantic model
class Biography(BaseModel):
    """Data model for a biography."""

    name: str
    best\_known\_for: List\[str\]
    extra\_info: str

\# try with pydantic model class Biography(BaseModel): """Data model for a biography.""" name: str best\_known\_for: List\[str\] extra\_info: str

In \[ \]:

Copied!

summarizer \= TreeSummarize(
    verbose\=True, summary\_template\=qa\_prompt, output\_cls\=Biography
)

summarizer = TreeSummarize( verbose=True, summary\_template=qa\_prompt, output\_cls=Biography )

In \[ \]:

Copied!

response \= summarizer.get\_response(
    "who is Paul Graham?", \[text\], tone\_name\="a business memo"
)

response = summarizer.get\_response( "who is Paul Graham?", \[text\], tone\_name="a business memo" )

5 text chunks after repacking
1 text chunks after repacking

In \[ \]:

Copied!

print(str(response))

print(str(response))

name='Paul Graham' best\_known\_for=\['Co-founder of Y Combinator', 'Writer', 'Investor'\] extra\_info="Paul Graham is a renowned entrepreneur, writer, and investor. He is best known as the co-founder of Y Combinator, a highly successful startup accelerator. Graham has played a significant role in shaping the startup ecosystem and has been instrumental in the success of numerous startups. He is also a prolific writer, known for his insightful essays on a wide range of topics, including technology, startups, and entrepreneurship. Graham's writings have been widely read and have had a profound impact on the tech community. In addition to his work with Y Combinator and his writing, Graham is also an active investor, providing seed funding and mentorship to early-stage startups. His contributions to the startup world have earned him a reputation as one of the most influential figures in the industry."

Back to top

[Previous Query Transform Cookbook](https://docs.llamaindex.ai/en/stable/examples/query_transformations/query_transform_cookbook/)[Next Stress-Testing Long Context LLMs with a Recall Task](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/long_context_test/)
