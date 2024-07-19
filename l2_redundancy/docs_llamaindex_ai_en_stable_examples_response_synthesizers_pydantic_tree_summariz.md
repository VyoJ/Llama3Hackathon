Title: Pydantic Tree Summarize - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/pydantic_tree_summarize/

Markdown Content:
Pydantic Tree Summarize - LlamaIndex


In this notebook, we demonstrate how to use tree summarize with structured outputs. Specifically, tree summarize is used to output pydantic objects.

In \[ \]:

Copied!

import os
import openai

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."
openai.api\_key \= os.environ\["OPENAI\_API\_KEY"\]

import os import openai os.environ\["OPENAI\_API\_KEY"\] = "sk-..." openai.api\_key = os.environ\["OPENAI\_API\_KEY"\]

Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/pydantic_tree_summarize/#download-data)


In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/pydantic_tree_summarize/#load-data)
--------------------------------------------------------------------------------------------------------------------

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

Summarize[¶](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/pydantic_tree_summarize/#summarize)
--------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core.response\_synthesizers import TreeSummarize
from llama\_index.core.types import BaseModel
from typing import List

from llama\_index.core.response\_synthesizers import TreeSummarize from llama\_index.core.types import BaseModel from typing import List

### Create pydantic model to structure response[¶](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/pydantic_tree_summarize/#create-pydantic-model-to-structure-response)

In \[ \]:

Copied!

class Biography(BaseModel):
    """Data model for a biography."""

    name: str
    best\_known\_for: List\[str\]
    extra\_info: str

class Biography(BaseModel): """Data model for a biography.""" name: str best\_known\_for: List\[str\] extra\_info: str

In \[ \]:

Copied!

summarizer \= TreeSummarize(verbose\=True, output\_cls\=Biography)

summarizer = TreeSummarize(verbose=True, output\_cls=Biography)

In \[ \]:

Copied!

response \= summarizer.get\_response("who is Paul Graham?", \[text\])

response = summarizer.get\_response("who is Paul Graham?", \[text\])

5 text chunks after repacking
1 text chunks after repacking

### Inspect the response[¶](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/pydantic_tree_summarize/#inspect-the-response)

Here, we see the response is in an instance of our `Biography` class.

In \[ \]:

Copied!

print(response)

print(response)

name='Paul Graham' best\_known\_for=\['Writing', 'Programming', 'Art', 'Co-founding Viaweb', 'Co-founding Y Combinator', 'Essayist'\] extra\_info="Paul Graham is a multi-talented individual who has made significant contributions in various fields. He is known for his work in writing, programming, art, co-founding Viaweb, co-founding Y Combinator, and his essays on startups and programming. He started his career by writing short stories and programming on the IBM 1401 computer. He later became interested in artificial intelligence and Lisp programming. He wrote a book called 'On Lisp' and focused on Lisp hacking. Eventually, he decided to pursue art and attended art school. He is known for his paintings, particularly still life paintings. Graham is also a programmer, entrepreneur, and venture capitalist. He co-founded Viaweb, an early e-commerce platform, and Y Combinator, a startup accelerator. He has written influential essays on startups and programming. Additionally, he has made contributions to the field of computer programming and entrepreneurship."

In \[ \]:

Copied!

print(response.name)

print(response.name)

Paul Graham

In \[ \]:

Copied!

print(response.best\_known\_for)

print(response.best\_known\_for)

\['Writing', 'Programming', 'Art', 'Co-founding Viaweb', 'Co-founding Y Combinator', 'Essayist'\]

In \[ \]:

Copied!

print(response.extra\_info)

print(response.extra\_info)

Paul Graham is a multi-talented individual who has made significant contributions in various fields. He is known for his work in writing, programming, art, co-founding Viaweb, co-founding Y Combinator, and his essays on startups and programming. He started his career by writing short stories and programming on the IBM 1401 computer. He later became interested in artificial intelligence and Lisp programming. He wrote a book called 'On Lisp' and focused on Lisp hacking. Eventually, he decided to pursue art and attended art school. He is known for his paintings, particularly still life paintings. Graham is also a programmer, entrepreneur, and venture capitalist. He co-founded Viaweb, an early e-commerce platform, and Y Combinator, a startup accelerator. He has written influential essays on startups and programming. Additionally, he has made contributions to the field of computer programming and entrepreneurship.

Back to top

[Previous Stress-Testing Long Context LLMs with a Recall Task](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/long_context_test/)[Next Refine](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/refine/)
