Title: Langchain Output Parsing - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/output_parsing/LangchainOutputParserDemo/

Markdown Content:
Langchain Output Parsing - LlamaIndex


Download Data

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai

%pip install llama-index-llms-openai

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

Will not apply HSTS. The HSTS database must be a regular and non-world-writable file.
ERROR: could not open HSTS store at '/home/loganm/.wget-hsts'. HSTS will be disabled.
--2023-12-11 10:24:04--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.110.133, 185.199.109.133, 185.199.108.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.110.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 75042 (73K) \[text/plain\]
Saving to: ‘data/paul\_graham/paul\_graham\_essay.txt’

data/paul\_graham/pa 100%\[>\]  73.28K  --.-KB/s    in 0.04s   

2023-12-11 10:24:04 (1.74 MB/s) - ‘data/paul\_graham/paul\_graham\_essay.txt’ saved \[75042/75042\]

#### Load documents, build the VectorStoreIndex[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/LangchainOutputParserDemo/#load-documents-build-the-vectorstoreindex)

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from IPython.display import Markdown, display

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout)) from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from IPython.display import Markdown, display import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..."

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data()

In \[ \]:

Copied!

index \= VectorStoreIndex.from\_documents(documents, chunk\_size\=512)

index = VectorStoreIndex.from\_documents(documents, chunk\_size=512)

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"

#### Define Query + Langchain Output Parser[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/LangchainOutputParserDemo/#define-query-langchain-output-parser)

In \[ \]:

Copied!

from llama\_index.core.output\_parsers import LangchainOutputParser
from langchain.output\_parsers import StructuredOutputParser, ResponseSchema

from llama\_index.core.output\_parsers import LangchainOutputParser from langchain.output\_parsers import StructuredOutputParser, ResponseSchema

**Define custom QA and Refine Prompts**

In \[ \]:

Copied!

response\_schemas \= \[
    ResponseSchema(
        name\="Education",
        description\=(
            "Describes the author's educational experience/background."
        ),
    ),
    ResponseSchema(
        name\="Work",
        description\="Describes the author's work experience/background.",
    ),
\]

response\_schemas = \[ ResponseSchema( name="Education", description=( "Describes the author's educational experience/background." ), ), ResponseSchema( name="Work", description="Describes the author's work experience/background.", ), \]

In \[ \]:

Copied!

lc\_output\_parser \= StructuredOutputParser.from\_response\_schemas(
    response\_schemas
)
output\_parser \= LangchainOutputParser(lc\_output\_parser)

lc\_output\_parser = StructuredOutputParser.from\_response\_schemas( response\_schemas ) output\_parser = LangchainOutputParser(lc\_output\_parser)

In \[ \]:

Copied!

from llama\_index.core.prompts.default\_prompts import (
    DEFAULT\_TEXT\_QA\_PROMPT\_TMPL,
)

\# take a look at the new QA template!
fmt\_qa\_tmpl \= output\_parser.format(DEFAULT\_TEXT\_QA\_PROMPT\_TMPL)
print(fmt\_qa\_tmpl)

from llama\_index.core.prompts.default\_prompts import ( DEFAULT\_TEXT\_QA\_PROMPT\_TMPL, ) # take a look at the new QA template! fmt\_qa\_tmpl = output\_parser.format(DEFAULT\_TEXT\_QA\_PROMPT\_TMPL) print(fmt\_qa\_tmpl)

Context information is below.
---------------------
{context\_str}
---------------------
Given the context information and not prior knowledge, answer the query.
Query: {query\_str}
Answer: 

The output should be a markdown code snippet formatted in the following schema, including the leading and trailing "\`\`\`json" and "\`\`\`":

\`\`\`json
{{
	"Education": string  // Describes the author's educational experience/background.
	"Work": string  // Describes the author's work experience/background.
}}
\`\`\`

#### Query Index[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/LangchainOutputParserDemo/#query-index)

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI

llm \= OpenAI(output\_parser\=output\_parser)

query\_engine \= index.as\_query\_engine(
    llm\=llm,
)
response \= query\_engine.query(
    "What are a few things the author did growing up?",
)

from llama\_index.llms.openai import OpenAI llm = OpenAI(output\_parser=output\_parser) query\_engine = index.as\_query\_engine( llm=llm, ) response = query\_engine.query( "What are a few things the author did growing up?", )

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"

In \[ \]:

Copied!

print(response)

print(response)

{'Education': 'The author did not plan to study programming in college, but initially planned to study philosophy.', 'Work': 'Growing up, the author worked on writing short stories and programming. They wrote simple games, a program to predict rocket heights, and a word processor.'}

Back to top

[Previous Guardrails Output Parsing](https://docs.llamaindex.ai/en/stable/examples/output_parsing/GuardrailsDemo/)[Next DataFrame Structured Data Extraction](https://docs.llamaindex.ai/en/stable/examples/output_parsing/df_program/)

Hi, how can I help you?

🦙
