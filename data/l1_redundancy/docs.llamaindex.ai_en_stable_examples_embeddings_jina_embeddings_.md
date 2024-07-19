Title: Jina 8K Context Window Embeddings

URL Source: https://docs.llamaindex.ai/en/stable/examples/embeddings/jina_embeddings/

Markdown Content:
Jina 8K Context Window Embeddings - LlamaIndex


Here we show you how to use `jina-embeddings-v2` which support an 8k context length and is on-par with `text-embedding-ada-002`

[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/docs/examples/embeddings/jina_embeddings.ipynb)

In \[ \]:

Copied!

%pip install llama\-index\-embeddings\-huggingface
%pip install llama\-index\-embeddings\-huggingface\-api
%pip install llama\-index\-embeddings\-openai

%pip install llama-index-embeddings-huggingface %pip install llama-index-embeddings-huggingface-api %pip install llama-index-embeddings-openai

In \[ \]:

Copied!

import nest\_asyncio

nest\_asyncio.apply()

import nest\_asyncio nest\_asyncio.apply()

Setup Embedding Model[¶](https://docs.llamaindex.ai/en/stable/examples/embeddings/jina_embeddings/#setup-embedding-model)
-------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.embeddings.huggingface import (
    HuggingFaceEmbedding,
)
from llama\_index.embeddings.huggingface\_api import (
    HuggingFaceInferenceAPIEmbedding,
)
from llama\_index.embeddings.openai import OpenAIEmbedding
from llama\_index.core import Settings

from llama\_index.embeddings.huggingface import ( HuggingFaceEmbedding, ) from llama\_index.embeddings.huggingface\_api import ( HuggingFaceInferenceAPIEmbedding, ) from llama\_index.embeddings.openai import OpenAIEmbedding from llama\_index.core import Settings

In \[ \]:

Copied!

\# base model
\# model\_name = "jinaai/jina-embeddings-v2-base-en"
\# small model
model\_name \= "jinaai/jina-embeddings-v2-small-en"

\# base model # model\_name = "jinaai/jina-embeddings-v2-base-en" # small model model\_name = "jinaai/jina-embeddings-v2-small-en"

In \[ \]:

Copied!

\# download model locally
\# note: you need enough RAM+compute to run this
embed\_model \= HuggingFaceEmbedding(
    model\_name\=model\_name, trust\_remote\_code\=True
)

\# use inference API on Hugging Face (though you might run into rate limit issues)
\# embed\_model = HuggingFaceInferenceAPIEmbedding(
\#     model\_name="jinaai/jina-embeddings-v2-base-en",
\# )

\# download model locally # note: you need enough RAM+compute to run this embed\_model = HuggingFaceEmbedding( model\_name=model\_name, trust\_remote\_code=True ) # use inference API on Hugging Face (though you might run into rate limit issues) # embed\_model = HuggingFaceInferenceAPIEmbedding( # model\_name="jinaai/jina-embeddings-v2-base-en", # )

In \[ \]:

Copied!

\# we set chunk size to 1024 for now, you can obviuosly set it to much bigger
Settings.embed\_model \= embed\_model
Settings.chunk\_size \= 1024

\# we set chunk size to 1024 for now, you can obviuosly set it to much bigger Settings.embed\_model = embed\_model Settings.chunk\_size = 1024

### Setup OpenAI ada embeddings as comparison[¶](https://docs.llamaindex.ai/en/stable/examples/embeddings/jina_embeddings/#setup-openai-ada-embeddings-as-comparison)

In \[ \]:

Copied!

embed\_model\_base \= OpenAIEmbedding()

embed\_model\_base = OpenAIEmbedding()

Setup Index to test this out[¶](https://docs.llamaindex.ai/en/stable/examples/embeddings/jina_embeddings/#setup-index-to-test-this-out)
---------------------------------------------------------------------------------------------------------------------------------------

We'll use our standard Paul Graham example.

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader

In \[ \]:

Copied!

reader \= SimpleDirectoryReader("../data/paul\_graham")
docs \= reader.load\_data()

reader = SimpleDirectoryReader("../data/paul\_graham") docs = reader.load\_data()

In \[ \]:

Copied!

index\_jina \= VectorStoreIndex.from\_documents(docs, embed\_model\=embed\_model)

index\_jina = VectorStoreIndex.from\_documents(docs, embed\_model=embed\_model)

In \[ \]:

Copied!

index\_base \= VectorStoreIndex.from\_documents(
    docs, embed\_model\=embed\_model\_base
)

index\_base = VectorStoreIndex.from\_documents( docs, embed\_model=embed\_model\_base )

View Results[¶](https://docs.llamaindex.ai/en/stable/examples/embeddings/jina_embeddings/#view-results)
-------------------------------------------------------------------------------------------------------

Look at retrieved results with Jina-8k vs. Replicate

In \[ \]:

Copied!

from llama\_index.core.response.notebook\_utils import display\_source\_node

retriever\_jina \= index\_jina.as\_retriever(similarity\_top\_k\=1)
retriever\_base \= index\_base.as\_retriever(similarity\_top\_k\=1)

from llama\_index.core.response.notebook\_utils import display\_source\_node retriever\_jina = index\_jina.as\_retriever(similarity\_top\_k=1) retriever\_base = index\_base.as\_retriever(similarity\_top\_k=1)

In \[ \]:

Copied!

retrieved\_nodes \= retriever\_jina.retrieve(
    "What did the author do in art school?"
)

retrieved\_nodes = retriever\_jina.retrieve( "What did the author do in art school?" )

In \[ \]:

Copied!

for n in retrieved\_nodes:
    display\_source\_node(n, source\_length\=2000)

for n in retrieved\_nodes: display\_source\_node(n, source\_length=2000)

**Node ID:** 921cc179-312f-4ee2-a760-3cccd27470d9  
**Similarity:** 0.7612087686435924  
**Text:** That's not always why artists have a signature style, but it's usually why buyers pay a lot for such work. \[6\]

There were plenty of earnest students too: kids who "could draw" in high school, and now had come to what was supposed to be the best art school in the country, to learn to draw even better. They tended to be confused and demoralized by what they found at RISD, but they kept going, because painting was what they did. I was not one of the kids who could draw in high school, but at RISD I was definitely closer to their tribe than the tribe of signature style seekers.

I learned a lot in the color class I took at RISD, but otherwise I was basically teaching myself to paint, and I could do that for free. So in 1993 I dropped out. I hung around Providence for a bit, and then my college friend Nancy Parmet did me a big favor. A rent-controlled apartment in a building her mother owned in New York was becoming vacant. Did I want it? It wasn't much more than my current place, and New York was supposed to be where the artists were. So yes, I wanted it! \[7\]

Asterix comics begin by zooming in on a tiny corner of Roman Gaul that turns out not to be controlled by the Romans. You can do something similar on a map of New York City: if you zoom in on the Upper East Side, there's a tiny corner that's not rich, or at least wasn't in 1993. It's called Yorkville, and that was my new home. Now I was a New York artist — in the strictly technical sense of making paintings and living in New York.

I was nervous about money, because I could sense that Interleaf was on the way down. Freelance Lisp hacking work was very rare, and I didn't want to have to program in another language, which in those days would have meant C++ if I was lucky. So with my unerring nose for financial opportunity, I decided to write another book on Lisp. This would be a popular book, the sort of book that could be used as a textbook. I imagined myself living frugally off the royalties and spending all my...

In \[ \]:

Copied!

retrieved\_nodes \= retriever\_base.retrieve("What did the author do in school?")

retrieved\_nodes = retriever\_base.retrieve("What did the author do in school?")

In \[ \]:

Copied!

for n in retrieved\_nodes:
    display\_source\_node(n, source\_length\=2000)

for n in retrieved\_nodes: display\_source\_node(n, source\_length=2000)

**Node ID:** 0abf44f2-94bd-421f-9ebd-5b50f4de37f0  
**Similarity:** 0.8352482505756655  
**Text:** What I Worked On

February 2021

Before college the two main things I worked on, outside of school, were writing and programming. I didn't write essays. I wrote what beginning writers were supposed to write then, and probably still are: short stories. My stories were awful. They had hardly any plot, just characters with strong feelings, which I imagined made them deep.

The first programs I tried writing were on the IBM 1401 that our school district used for what was then called "data processing." This was in 9th grade, so I was 13 or 14. The school district's 1401 happened to be in the basement of our junior high school, and my friend Rich Draves and I got permission to use it. It was like a mini Bond villain's lair down there, with all these alien-looking machines — CPU, disk drives, printer, card reader — sitting up on a raised floor under bright fluorescent lights.

The language we used was an early version of Fortran. You had to type programs on punch cards, then stack them in the card reader and press a button to load the program into memory and run it. The result would ordinarily be to print something on the spectacularly loud printer.

I was puzzled by the 1401. I couldn't figure out what to do with it. And in retrospect there's not much I could have done with it. The only form of input to programs was data stored on punched cards, and I didn't have any data stored on punched cards. The only other option was to do things that didn't rely on any input, like calculate approximations of pi, but I didn't know enough math to do anything interesting of that type. So I'm not surprised I can't remember any programs I wrote, because they can't have done much. My clearest memory is of the moment I learned it was possible for programs not to terminate, when one of mine didn't. On a machine without time-sharing, this was a social as well as a technical error, as the data center manager's expression made clear.

With microcomputers, everything changed. Now you could h...

Back to top

[Previous Optimized BGE Embedding Model using Intel® Extension for Transformers](https://docs.llamaindex.ai/en/stable/examples/embeddings/itrex/)[Next Jina Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/jinaai_embeddings/)
