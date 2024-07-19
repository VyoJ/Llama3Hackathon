Title: Streaming for Chat Engine - Condense Question Mode

URL Source: https://docs.llamaindex.ai/en/stable/examples/customization/streaming/chat_engine_condense_question_stream_response/

Markdown Content:
Streaming for Chat Engine - Condense Question Mode - LlamaIndex


Load documents, build the VectorStoreIndex

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout)) from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

\--2024-02-20 11:00:23--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.111.133, 185.199.110.133, 185.199.109.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.111.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 75042 (73K) \[text/plain\]
Saving to: ‘data/paul\_graham/paul\_graham\_essay.txt’

data/paul\_graham/pa 100%\[>\]  73.28K  --.-KB/s    in 0.05s   

2024-02-20 11:00:23 (1.59 MB/s) - ‘data/paul\_graham/paul\_graham\_essay.txt’ saved \[75042/75042\]

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham").load\_data()

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham").load\_data()

In \[ \]:

Copied!

index \= VectorStoreIndex.from\_documents(documents)

index = VectorStoreIndex.from\_documents(documents)

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"

Chat with your data

In \[ \]:

Copied!

chat\_engine \= index.as\_chat\_engine(
    chat\_mode\="condense\_question", streaming\=True
)
response\_stream \= chat\_engine.stream\_chat("What did Paul Graham do after YC?")

chat\_engine = index.as\_chat\_engine( chat\_mode="condense\_question", streaming=True ) response\_stream = chat\_engine.stream\_chat("What did Paul Graham do after YC?")

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
INFO:llama\_index.core.chat\_engine.condense\_question:Querying with: What did Paul Graham do after his time at Y Combinator?
Querying with: What did Paul Graham do after his time at Y Combinator?
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"

In \[ \]:

Copied!

response\_stream.print\_response\_stream()

response\_stream.print\_response\_stream()

Paul Graham decided to hand over Y Combinator to someone else after his time there. He asked Jessica if she wanted to be president, but she declined. Eventually, they recruited Sam Altman to take over as president. Paul Graham, along with Robert, retired from Y Combinator, while Jessica and Trevor became ordinary partners.

Ask a follow up question

In \[ \]:

Copied!

response\_stream \= chat\_engine.stream\_chat("What about after that?")

response\_stream = chat\_engine.stream\_chat("What about after that?")

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
INFO:llama\_index.core.chat\_engine.condense\_question:Querying with: What did Paul Graham do after handing over Y Combinator to Sam Altman and retiring from the company?
Querying with: What did Paul Graham do after handing over Y Combinator to Sam Altman and retiring from the company?
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"

In \[ \]:

Copied!

response\_stream.print\_response\_stream()

response\_stream.print\_response\_stream()

After handing over Y Combinator to Sam Altman and retiring from the company, Paul Graham started his own investment firm with Jessica.

In \[ \]:

Copied!

response\_stream \= chat\_engine.stream\_chat("Can you tell me more?")

response\_stream = chat\_engine.stream\_chat("Can you tell me more?")

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
INFO:llama\_index.core.chat\_engine.condense\_question:Querying with: Can you tell me more about Paul Graham's investment firm that he started with Jessica after retiring from Y Combinator?
Querying with: Can you tell me more about Paul Graham's investment firm that he started with Jessica after retiring from Y Combinator?
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"

In \[ \]:

Copied!

response\_stream.print\_response\_stream()

response\_stream.print\_response\_stream()

Paul Graham started an investment firm with Jessica after retiring from Y Combinator. They decided to create their own investment firm to implement the ideas they had been discussing. Paul funded the firm, allowing Jessica to quit her job and work for it, while also bringing on Robert and Trevor as partners. The firm was structured as an angel firm, which was a novel concept at the time. They aimed not only to make seed investments but also to provide comprehensive support to startups, similar to the help they had received when starting their own company. The investment firm was not organized as a fund and was funded with their own money. The distinctive aspect of their approach was the batch model, where they funded multiple startups at once and provided intensive support over a three-month period.

Reset conversation state

In \[ \]:

Copied!

chat\_engine.reset()

chat\_engine.reset()

In \[ \]:

Copied!

response\_stream \= chat\_engine.stream\_chat("What about after that?")

response\_stream = chat\_engine.stream\_chat("What about after that?")

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
INFO:llama\_index.core.chat\_engine.condense\_question:Querying with: What will happen after that?
Querying with: What will happen after that?
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"

In \[ \]:

Copied!

response\_stream.print\_response\_stream()

response\_stream.print\_response\_stream()

After that, the individual started working on Lisp again in March 2015. The distinctive aspect of Lisp is that its core is a language defined by writing an interpreter in itself. Initially intended as a formal model of computation, Lisp evolved into a programming language as well. The individual's interest in Lisp stemmed from its power and elegance derived from its origins as a model of computation.

Back to top

[Previous Streaming](https://docs.llamaindex.ai/en/stable/examples/customization/streaming/SimpleIndexDemo-streaming/)[Next Chroma Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/ChromaDemo/)
