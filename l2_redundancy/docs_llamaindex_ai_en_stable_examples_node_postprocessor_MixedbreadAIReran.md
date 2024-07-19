Title: Mixedbread AI Rerank - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/MixedbreadAIRerank/

Markdown Content:
Mixedbread AI Rerank - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index \> /dev/null
%pip install llama\-index\-postprocessor\-mixedbreadai\-rerank \> /dev/null

%pip install llama-index > /dev/null %pip install llama-index-postprocessor-mixedbreadai-rerank > /dev/null

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.core.response.pprint\_utils import pprint\_response

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.core.response.pprint\_utils import pprint\_response

Download Data

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

\--2024-06-17 19:19:32--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.111.133, 185.199.109.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 75042 (73K) \[text/plain\]
Saving to: ‘data/paul\_graham/paul\_graham\_essay.txt’

data/paul\_graham/pa 100%\[>\]  73.28K  --.-KB/s    in 0.03s   

2024-06-17 19:19:32 (2.11 MB/s) - ‘data/paul\_graham/paul\_graham\_essay.txt’ saved \[75042/75042\]

In \[ \]:

Copied!

import os
from llama\_index.embeddings.mixedbreadai import MixedbreadAIEmbedding

\# You can visit https://www.mixedbread.ai/api-reference#quick-start-guide
\# to get an api key
mixedbread\_api\_key \= os.environ.get("MXBAI\_API\_KEY", "your-api-key")
model\_name \= "mixedbread-ai/mxbai-embed-large-v1"

mixbreadai\_embeddings \= MixedbreadAIEmbedding(
    api\_key\=mixedbread\_api\_key, model\_name\=model\_name
)

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

\# build index
index \= VectorStoreIndex.from\_documents(
    documents\=documents, embed\_model\=mixbreadai\_embeddings
)

import os from llama\_index.embeddings.mixedbreadai import MixedbreadAIEmbedding # You can visit https://www.mixedbread.ai/api-reference#quick-start-guide # to get an api key mixedbread\_api\_key = os.environ.get("MXBAI\_API\_KEY", "your-api-key") model\_name = "mixedbread-ai/mxbai-embed-large-v1" mixbreadai\_embeddings = MixedbreadAIEmbedding( api\_key=mixedbread\_api\_key, model\_name=model\_name ) # load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data() # build index index = VectorStoreIndex.from\_documents( documents=documents, embed\_model=mixbreadai\_embeddings )

Retrieve top 10 most relevant nodes, then filter with MixedbreadAI Rerank[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/MixedbreadAIRerank/#retrieve-top-10-most-relevant-nodes-then-filter-with-mixedbreadai-rerank)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.postprocessor.mixedbreadai\_rerank import MixedbreadAIRerank

mixedbreadai\_rerank \= MixedbreadAIRerank(
    api\_key\=mixedbread\_api\_key,
    top\_n\=2,
    model\="mixedbread-ai/mxbai-rerank-large-v1",
)

from llama\_index.postprocessor.mixedbreadai\_rerank import MixedbreadAIRerank mixedbreadai\_rerank = MixedbreadAIRerank( api\_key=mixedbread\_api\_key, top\_n=2, model="mixedbread-ai/mxbai-rerank-large-v1", )

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(
    similarity\_top\_k\=10,
    node\_postprocessors\=\[mixedbreadai\_rerank\],
)
response \= query\_engine.query(
    "What did Sam Altman do in this essay?",
)

query\_engine = index.as\_query\_engine( similarity\_top\_k=10, node\_postprocessors=\[mixedbreadai\_rerank\], ) response = query\_engine.query( "What did Sam Altman do in this essay?", )

In \[ \]:

Copied!

pprint\_response(response, show\_source\=True)

pprint\_response(response, show\_source=True)

Final Response: Sam Altman was asked to become the president of Y
Combinator (YC) after the original founders decided to step back and
reorganize the company to ensure its longevity. Initially hesitant due
to his interest in starting a nuclear reactor startup, Sam eventually
agreed to take over as president starting with the winter 2014 batch.
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Source Node 1/2
Node ID: 9bef8795-4532-44eb-a590-45abf15b11e5
Similarity: 0.109680176
Text: This seemed strange advice, because YC was doing great. But if
there was one thing rarer than Rtm offering advice, it was Rtm being
wrong. So this set me thinking. It was true that on my current
trajectory, YC would be the last thing I did, because it was only
taking up more of my attention. It had already eaten Arc, and was in
the process of ea...
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Source Node 2/2
Node ID: 3060722a-0e57-492e-9071-2148e5eec2be
Similarity: 0.041625977
Text: But after Heroku got bought we had enough money to go back to
being self-funded.  \[15\] I've never liked the term "deal flow,"
because it implies that the number of new startups at any given time
is fixed. This is not only false, but it's the purpose of YC to
falsify it, by causing startups to be founded that would not otherwise
have existed.  \[1...

Directly retrieve top 2 most similar nodes[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/MixedbreadAIRerank/#directly-retrieve-top-2-most-similar-nodes)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(
    similarity\_top\_k\=2,
)
response \= query\_engine.query(
    "What did Sam Altman do in this essay?",
)

query\_engine = index.as\_query\_engine( similarity\_top\_k=2, ) response = query\_engine.query( "What did Sam Altman do in this essay?", )

Retrieved context is irrelevant and response is hallucinated.

In \[ \]:

Copied!

pprint\_response(response, show\_source\=True)

pprint\_response(response, show\_source=True)

Final Response: Sam Altman worked on the application builder, while
Dan worked on network infrastructure, and two undergrads worked on the
first two services (images and phone calls). Later on, Sam realized he
didn't want to run a company and decided to build a subset of the
project as an open source project.
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Source Node 1/2
Node ID: a42ab697-0bd1-40fc-8e23-64148e62fe6d
Similarity: 0.557881093860686
Text: I started working on the application builder, Dan worked on
network infrastructure, and the two undergrads worked on the first two
services (images and phone calls). But about halfway through the
summer I realized I really didn't want to run a company — especially
not a big one, which it was looking like this would have to be. I'd
only started V...
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Source Node 2/2
Node ID: a398b429-fad6-4284-a201-835e5c1fec3c
Similarity: 0.49815489887733433
Text: But alas it was more like the Accademia than not. Better
organized, certainly, and a lot more expensive, but it was now
becoming clear that art school did not bear the same relationship to
art that medical school bore to medicine. At least not the painting
department. The textile department, which my next door neighbor
belonged to, seemed to be ...

Back to top

[Previous Metadata Replacement + Node Sentence Window](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/MetadataReplacementDemo/)[Next NVIDIA NIMs](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/NVIDIARerank/)

Hi, how can I help you?

🦙
