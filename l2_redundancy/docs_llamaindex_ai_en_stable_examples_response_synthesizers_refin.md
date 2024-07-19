Title: Refine - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/refine/

Markdown Content:
Refine - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai

%pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

### Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/refine/#download-data)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/refine/#load-data)
---------------------------------------------------------------------------------------------------

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

Summarize[¶](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/refine/#summarize)
---------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI

llm \= OpenAI(model\="gpt-3.5-turbo")

from llama\_index.llms.openai import OpenAI llm = OpenAI(model="gpt-3.5-turbo")

In \[ \]:

Copied!

from llama\_index.core.response\_synthesizers import Refine

summarizer \= Refine(llm\=llm, verbose\=True)

from llama\_index.core.response\_synthesizers import Refine summarizer = Refine(llm=llm, verbose=True)

In \[ \]:

Copied!

response \= summarizer.get\_response("who is Paul Graham?", \[text\])

response = summarizer.get\_response("who is Paul Graham?", \[text\])

\> Refine context: making fakes for a local antique dealer. She'd ...
> Refine context: look legit, and the key to looking legit is hig...
> Refine context: me 8 years to realize it. Even then it took me ...
> Refine context: was one thing rarer than Rtm offering advice, i...

In \[ \]:

Copied!

print(response)

print(response)

Paul Graham is an individual who has played a crucial role in shaping the internet infrastructure and has also pursued a career as a writer. At one point, he received advice from a friend that urged him not to let Y Combinator be his final noteworthy achievement. This advice prompted him to reflect on his future with Y Combinator and ultimately led him to pass on the responsibility to others. He approached Jessica and Sam Altman to assume leadership positions in Y Combinator, aiming to secure its continued success.

Back to top

[Previous Pydantic Tree Summarize](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/pydantic_tree_summarize/)[Next Refine with Structured Answer Filtering](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/structured_refine/)
