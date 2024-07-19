Title: Gradient Base Model - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/llm/gradient_base_model/

Markdown Content:
Gradient Base Model - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-embeddings\-langchain
%pip install llama\-index\-llms\-gradient

%pip install llama-index-embeddings-langchain %pip install llama-index-llms-gradient

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

%pip install llama\-index \--quiet
%pip install gradientai \--quiet

%pip install llama-index --quiet %pip install gradientai --quiet

In \[ \]:

Copied!

import os

os.environ\["GRADIENT\_ACCESS\_TOKEN"\] \= "{GRADIENT\_ACCESS\_TOKEN}"
os.environ\["GRADIENT\_WORKSPACE\_ID"\] \= "{GRADIENT\_WORKSPACE\_ID}"

import os os.environ\["GRADIENT\_ACCESS\_TOKEN"\] = "{GRADIENT\_ACCESS\_TOKEN}" os.environ\["GRADIENT\_WORKSPACE\_ID"\] = "{GRADIENT\_WORKSPACE\_ID}"

Flow 1: Query Gradient LLM directly[¶](https://docs.llamaindex.ai/en/stable/examples/llm/gradient_base_model/#flow-1-query-gradient-llm-directly)
-------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.llms.gradient import GradientBaseModelLLM

llm \= GradientBaseModelLLM(
    base\_model\_slug\="llama2-7b-chat",
    max\_tokens\=400,
)

from llama\_index.llms.gradient import GradientBaseModelLLM llm = GradientBaseModelLLM( base\_model\_slug="llama2-7b-chat", max\_tokens=400, )

In \[ \]:

Copied!

result \= llm.complete("Can you tell me about large language models?")
print(result)

result = llm.complete("Can you tell me about large language models?") print(result)

Flow 2: Retrieval Augmented Generation (RAG) with Gradient LLM[¶](https://docs.llamaindex.ai/en/stable/examples/llm/gradient_base_model/#flow-2-retrieval-augmented-generation-rag-with-gradient-llm)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.embeddings.langchain import LangchainEmbedding
from langchain.embeddings import HuggingFaceEmbeddings
from llama\_index.core.node\_parser import SentenceSplitter

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.embeddings.langchain import LangchainEmbedding from langchain.embeddings import HuggingFaceEmbeddings from llama\_index.core.node\_parser import SentenceSplitter

#### Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/llm/gradient_base_model/#download-data)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

### Load Documents[¶](https://docs.llamaindex.ai/en/stable/examples/llm/gradient_base_model/#load-documents)

In \[ \]:

Copied!

documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data()

### Configure Gradient LLM[¶](https://docs.llamaindex.ai/en/stable/examples/llm/gradient_base_model/#configure-gradient-llm)

In \[ \]:

Copied!

embed\_model \= LangchainEmbedding(HuggingFaceEmbeddings())
splitter \= SentenceSplitter(chunk\_size\=1024)

embed\_model = LangchainEmbedding(HuggingFaceEmbeddings()) splitter = SentenceSplitter(chunk\_size=1024)

### Setup and Query Index[¶](https://docs.llamaindex.ai/en/stable/examples/llm/gradient_base_model/#setup-and-query-index)

In \[ \]:

Copied!

index \= VectorStoreIndex.from\_documents(
    documents, transformations\=\[splitter\], embed\_model\=embed\_model
)
query\_engine \= index.as\_query\_engine(llm\=llm)

index = VectorStoreIndex.from\_documents( documents, transformations=\[splitter\], embed\_model=embed\_model ) query\_engine = index.as\_query\_engine(llm=llm)

In \[ \]:

Copied!

response \= query\_engine.query(
    "What did the author do after his time at Y Combinator?"
)
print(response)

response = query\_engine.query( "What did the author do after his time at Y Combinator?" ) print(response)

Back to top

[Previous Gemini](https://docs.llamaindex.ai/en/stable/examples/llm/gemini/)[Next Gradient Model Adapter](https://docs.llamaindex.ai/en/stable/examples/llm/gradient_model_adapter/)
