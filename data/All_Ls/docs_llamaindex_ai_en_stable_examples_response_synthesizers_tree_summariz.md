Title: Tree Summarize - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/tree_summarize/

Markdown Content:
Tree Summarize - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/tree_summarize/#download-data)
-------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/tree_summarize/#load-data)
-----------------------------------------------------------------------------------------------------------

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

Summarize[¶](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/tree_summarize/#summarize)
-----------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core.response\_synthesizers import TreeSummarize

from llama\_index.core.response\_synthesizers import TreeSummarize

In \[ \]:

Copied!

summarizer \= TreeSummarize(verbose\=True)

summarizer = TreeSummarize(verbose=True)

In \[ \]:

Copied!

response \= await summarizer.aget\_response("who is Paul Graham?", \[text\])

response = await summarizer.aget\_response("who is Paul Graham?", \[text\])

6 text chunks after repacking
1 text chunks after repacking

In \[ \]:

Copied!

print(response)

print(response)

Paul Graham is a computer scientist, writer, artist, entrepreneur, investor, and essayist. He is best known for his work in artificial intelligence, Lisp programming, and writing the book On Lisp, as well as for co-founding the startup accelerator Y Combinator and for his essays on technology, business, and start-ups. He is also the creator of the programming language Arc and the Lisp dialect Bel.

Back to top

[Previous Refine with Structured Answer Filtering](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/structured_refine/)[Next Auto Merging Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/auto_merging_retriever/)
