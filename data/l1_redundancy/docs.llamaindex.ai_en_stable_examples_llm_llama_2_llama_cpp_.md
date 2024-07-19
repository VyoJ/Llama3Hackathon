Title: LlamaCPP - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/llm/llama_2_llama_cpp/

Markdown Content:
LlamaCPP - LlamaIndex


In this short notebook, we show how to use the [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) library with LlamaIndex.

In this notebook, we use the [`llama-2-chat-13b-ggml`](https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML) model, along with the proper prompt formatting.

Note that if you're using a version of `llama-cpp-python` after version `0.1.79`, the model format has changed from `ggmlv3` to `gguf`. Old model files like the used in this notebook can be converted using scripts in the [`llama.cpp`](https://github.com/ggerganov/llama.cpp) repo. Alternatively, you can download the GGUF version of the model above from [huggingface](https://huggingface.co/TheBloke/Llama-2-13B-chat-GGUF).

By default, if model\_path and model\_url are blank, the `LlamaCPP` module will load llama2-chat-13B in either format depending on your version.

Installation[¶](https://docs.llamaindex.ai/en/stable/examples/llm/llama_2_llama_cpp/#installation)
--------------------------------------------------------------------------------------------------

To get the best performance out of `LlamaCPP`, it is recomended to install the package so that it is compilied with GPU support. A full guide for installing this way is [here](https://github.com/abetlen/llama-cpp-python#installation-with-openblas--cublas--clblast--metal).

Full MACOS instructions are also [here](https://llama-cpp-python.readthedocs.io/en/latest/install/macos/).

In general:

*   Use `CuBLAS` if you have CUDA and an NVidia GPU
*   Use `METAL` if you are running on an M1/M2 MacBook
*   Use `CLBLAST` if you are running on an AMD/Intel GPU

In \[ \]:

Copied!

%pip install llama\-index\-embeddings\-huggingface
%pip install llama\-index\-llms\-llama\-cpp

%pip install llama-index-embeddings-huggingface %pip install llama-index-llms-llama-cpp

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama\_index.llms.llama\_cpp import LlamaCPP
from llama\_index.llms.llama\_cpp.llama\_utils import (
    messages\_to\_prompt,
    completion\_to\_prompt,
)

from llama\_index.core import SimpleDirectoryReader, VectorStoreIndex from llama\_index.llms.llama\_cpp import LlamaCPP from llama\_index.llms.llama\_cpp.llama\_utils import ( messages\_to\_prompt, completion\_to\_prompt, )

Setup LLM[¶](https://docs.llamaindex.ai/en/stable/examples/llm/llama_2_llama_cpp/#setup-llm)
--------------------------------------------------------------------------------------------

The LlamaCPP llm is highly configurable. Depending on the model being used, you'll want to pass in `messages_to_prompt` and `completion_to_prompt` functions to help format the model inputs.

Since the default model is llama2-chat, we use the util functions found in [`llama_index.llms.llama_utils`](https://github.com/jerryjliu/llama_index/blob/main/llama_index/llms/llama_utils.py).

For any kwargs that need to be passed in during initialization, set them in `model_kwargs`. A full list of available model kwargs is available in the [LlamaCPP docs](https://llama-cpp-python.readthedocs.io/en/latest/api-reference/#llama_cpp.llama.Llama.__init__).

For any kwargs that need to be passed in during inference, you can set them in `generate_kwargs`. See the full list of [generate kwargs here](https://llama-cpp-python.readthedocs.io/en/latest/api-reference/#llama_cpp.llama.Llama.__call__).

In general, the defaults are a great starting point. The example below shows configuration with all defaults.

As noted above, we're using the [`llama-2-chat-13b-ggml`](https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML) model in this notebook which uses the `ggmlv3` model format. If you are running a version of `llama-cpp-python` greater than `0.1.79`, you can replace the `model_url` below with `"https://huggingface.co/TheBloke/Llama-2-13B-chat-GGUF/resolve/main/llama-2-13b-chat.Q4_0.gguf"`.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

model\_url \= "https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML/resolve/main/llama-2-13b-chat.ggmlv3.q4\_0.bin"

model\_url = "https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML/resolve/main/llama-2-13b-chat.ggmlv3.q4\_0.bin"

In \[ \]:

Copied!

llm \= LlamaCPP(
    \# You can pass in the URL to a GGML model to download it automatically
    model\_url\=model\_url,
    \# optionally, you can set the path to a pre-downloaded model instead of model\_url
    model\_path\=None,
    temperature\=0.1,
    max\_new\_tokens\=256,
    \# llama2 has a context window of 4096 tokens, but we set it lower to allow for some wiggle room
    context\_window\=3900,
    \# kwargs to pass to \_\_call\_\_()
    generate\_kwargs\={},
    \# kwargs to pass to \_\_init\_\_()
    \# set to at least 1 to use GPU
    model\_kwargs\={"n\_gpu\_layers": 1},
    \# transform inputs into Llama2 format
    messages\_to\_prompt\=messages\_to\_prompt,
    completion\_to\_prompt\=completion\_to\_prompt,
    verbose\=True,
)

llm = LlamaCPP( # You can pass in the URL to a GGML model to download it automatically model\_url=model\_url, # optionally, you can set the path to a pre-downloaded model instead of model\_url model\_path=None, temperature=0.1, max\_new\_tokens=256, # llama2 has a context window of 4096 tokens, but we set it lower to allow for some wiggle room context\_window=3900, # kwargs to pass to \_\_call\_\_() generate\_kwargs={}, # kwargs to pass to \_\_init\_\_() # set to at least 1 to use GPU model\_kwargs={"n\_gpu\_layers": 1}, # transform inputs into Llama2 format messages\_to\_prompt=messages\_to\_prompt, completion\_to\_prompt=completion\_to\_prompt, verbose=True, )

llama.cpp: loading model from /Users/rchan/Library/Caches/llama\_index/models/llama-2-13b-chat.ggmlv3.q4\_0.bin
llama\_model\_load\_internal: format     = ggjt v3 (latest)
llama\_model\_load\_internal: n\_vocab    = 32000
llama\_model\_load\_internal: n\_ctx      = 3900
llama\_model\_load\_internal: n\_embd     = 5120
llama\_model\_load\_internal: n\_mult     = 256
llama\_model\_load\_internal: n\_head     = 40
llama\_model\_load\_internal: n\_head\_kv  = 40
llama\_model\_load\_internal: n\_layer    = 40
llama\_model\_load\_internal: n\_rot      = 128
llama\_model\_load\_internal: n\_gqa      = 1
llama\_model\_load\_internal: rnorm\_eps  = 5.0e-06
llama\_model\_load\_internal: n\_ff       = 13824
llama\_model\_load\_internal: freq\_base  = 10000.0
llama\_model\_load\_internal: freq\_scale = 1
llama\_model\_load\_internal: ftype      = 2 (mostly Q4\_0)
llama\_model\_load\_internal: model size = 13B
llama\_model\_load\_internal: ggml ctx size =    0.11 MB
llama\_model\_load\_internal: mem required  = 6983.72 MB (+ 3046.88 MB per state)
llama\_new\_context\_with\_model: kv self size  = 3046.88 MB
ggml\_metal\_init: allocating
ggml\_metal\_init: loading '/Users/rchan/opt/miniconda3/envs/llama-index/lib/python3.10/site-packages/llama\_cpp/ggml-metal.metal'
ggml\_metal\_init: loaded kernel\_add                            0x14ff4f060
ggml\_metal\_init: loaded kernel\_add\_row                        0x14ff4f2c0
ggml\_metal\_init: loaded kernel\_mul                            0x14ff4f520
ggml\_metal\_init: loaded kernel\_mul\_row                        0x14ff4f780
ggml\_metal\_init: loaded kernel\_scale                          0x14ff4f9e0
ggml\_metal\_init: loaded kernel\_silu                           0x14ff4fc40
ggml\_metal\_init: loaded kernel\_relu                           0x14ff4fea0
ggml\_metal\_init: loaded kernel\_gelu                           0x11f7aef50
ggml\_metal\_init: loaded kernel\_soft\_max                       0x11f7af380
ggml\_metal\_init: loaded kernel\_diag\_mask\_inf                  0x11f7af5e0
ggml\_metal\_init: loaded kernel\_get\_rows\_f16                   0x11f7af840
ggml\_metal\_init: loaded kernel\_get\_rows\_q4\_0                  0x11f7afaa0
ggml\_metal\_init: loaded kernel\_get\_rows\_q4\_1                  0x13ffba0c0
ggml\_metal\_init: loaded kernel\_get\_rows\_q2\_K                  0x13ffba320
ggml\_metal\_init: loaded kernel\_get\_rows\_q3\_K                  0x13ffba580
ggml\_metal\_init: loaded kernel\_get\_rows\_q4\_K                  0x13ffbaab0
ggml\_metal\_init: loaded kernel\_get\_rows\_q5\_K                  0x13ffbaea0
ggml\_metal\_init: loaded kernel\_get\_rows\_q6\_K                  0x13ffbb290
ggml\_metal\_init: loaded kernel\_rms\_norm                       0x13ffbb690
ggml\_metal\_init: loaded kernel\_norm                           0x13ffbba80
ggml\_metal\_init: loaded kernel\_mul\_mat\_f16\_f32                0x13ffbc070
ggml\_metal\_init: loaded kernel\_mul\_mat\_q4\_0\_f32               0x13ffbc510
ggml\_metal\_init: loaded kernel\_mul\_mat\_q4\_1\_f32               0x11f7aff40
ggml\_metal\_init: loaded kernel\_mul\_mat\_q2\_K\_f32               0x11f7b03e0
ggml\_metal\_init: loaded kernel\_mul\_mat\_q3\_K\_f32               0x11f7b0880
ggml\_metal\_init: loaded kernel\_mul\_mat\_q4\_K\_f32               0x11f7b0d20
ggml\_metal\_init: loaded kernel\_mul\_mat\_q5\_K\_f32               0x11f7b11c0
ggml\_metal\_init: loaded kernel\_mul\_mat\_q6\_K\_f32               0x11f7b1860
ggml\_metal\_init: loaded kernel\_mul\_mm\_f16\_f32                 0x11f7b1d40
ggml\_metal\_init: loaded kernel\_mul\_mm\_q4\_0\_f32                0x11f7b2220
ggml\_metal\_init: loaded kernel\_mul\_mm\_q4\_1\_f32                0x11f7b2700
ggml\_metal\_init: loaded kernel\_mul\_mm\_q2\_K\_f32                0x11f7b2be0
ggml\_metal\_init: loaded kernel\_mul\_mm\_q3\_K\_f32                0x11f7b30c0
ggml\_metal\_init: loaded kernel\_mul\_mm\_q4\_K\_f32                0x11f7b35a0
ggml\_metal\_init: loaded kernel\_mul\_mm\_q5\_K\_f32                0x11f7b3a80
ggml\_metal\_init: loaded kernel\_mul\_mm\_q6\_K\_f32                0x11f7b3f60
ggml\_metal\_init: loaded kernel\_rope                           0x11f7b41c0
ggml\_metal\_init: loaded kernel\_alibi\_f32                      0x11f7b47c0
ggml\_metal\_init: loaded kernel\_cpy\_f32\_f16                    0x11f7b4d90
ggml\_metal\_init: loaded kernel\_cpy\_f32\_f32                    0x11f7b5360
ggml\_metal\_init: loaded kernel\_cpy\_f16\_f16                    0x11f7b5930
ggml\_metal\_init: recommendedMaxWorkingSetSize = 21845.34 MB
ggml\_metal\_init: hasUnifiedMemory             = true
ggml\_metal\_init: maxTransferRate              = built-in GPU
llama\_new\_context\_with\_model: compute buffer total size =  356.03 MB
llama\_new\_context\_with\_model: max tensor size =    87.89 MB
ggml\_metal\_add\_buffer: allocated 'data            ' buffer, size =  6984.06 MB, ( 6984.50 / 21845.34)
ggml\_metal\_add\_buffer: allocated 'eval            ' buffer, size =     1.36 MB, ( 6985.86 / 21845.34)
ggml\_metal\_add\_buffer: allocated 'kv              ' buffer, size =  3048.88 MB, (10034.73 / 21845.34)
ggml\_metal\_add\_buffer: allocated 'alloc           ' buffer, size =   354.70 MB, (10389.44 / 21845.34)
AVX = 0 | AVX2 = 0 | AVX512 = 0 | AVX512\_VBMI = 0 | AVX512\_VNNI = 0 | FMA = 0 | NEON = 1 | ARM\_FMA = 1 | F16C = 0 | FP16\_VA = 1 | WASM\_SIMD = 0 | BLAS = 1 | SSE3 = 0 | VSX = 0 | 

We can tell that the model is using `metal` due to the logging!

Start using our `LlamaCPP` LLM abstraction![¶](https://docs.llamaindex.ai/en/stable/examples/llm/llama_2_llama_cpp/#start-using-our-llamacpp-llm-abstraction)
-------------------------------------------------------------------------------------------------------------------------------------------------------------

We can simply use the `complete` method of our `LlamaCPP` LLM abstraction to generate completions given a prompt.

In \[ \]:

Copied!

response \= llm.complete("Hello! Can you tell me a poem about cats and dogs?")
print(response.text)

response = llm.complete("Hello! Can you tell me a poem about cats and dogs?") print(response.text)

  Of course, I'd be happy to help! Here's a short poem about cats and dogs:

Cats and dogs, so different yet the same,
Both furry friends, with their own special game.

Cats purr and curl up tight,
Dogs wag their tails with delight.

Cats hunt mice with stealthy grace,
Dogs chase after balls with joyful pace.

But despite their differences, they share,
A love for play and a love so fair.

So here's to our feline and canine friends,
Both equally dear, and both equally grand.

llama\_print\_timings:        load time =  1204.19 ms
llama\_print\_timings:      sample time =   106.79 ms /   146 runs   (    0.73 ms per token,  1367.14 tokens per second)
llama\_print\_timings: prompt eval time =  1204.14 ms /    81 tokens (   14.87 ms per token,    67.27 tokens per second)
llama\_print\_timings:        eval time =  7468.88 ms /   145 runs   (   51.51 ms per token,    19.41 tokens per second)
llama\_print\_timings:       total time =  8993.90 ms

We can use the `stream_complete` endpoint to stream the response as it’s being generated rather than waiting for the entire response to be generated.

In \[ \]:

Copied!

response\_iter \= llm.stream\_complete("Can you write me a poem about fast cars?")
for response in response\_iter:
    print(response.delta, end\="", flush\=True)

response\_iter = llm.stream\_complete("Can you write me a poem about fast cars?") for response in response\_iter: print(response.delta, end="", flush=True)

Llama.generate: prefix-match hit

  Sure! Here's a poem about fast cars:

Fast cars, sleek and strong
Racing down the highway all day long
Their engines purring smooth and sweet
As they speed through the streets

Their wheels grip the road with might
As they take off like a shot in flight
The wind rushes past with a roar
As they leave all else behind

With paint that shines like the sun
And lines that curve like a dream
They're a sight to behold, my son
These fast cars, so sleek and serene

So if you ever see one pass
Don't be afraid to give a cheer
For these machines of speed and grace
Are truly something to admire and revere.

llama\_print\_timings:        load time =  1204.19 ms
llama\_print\_timings:      sample time =   123.72 ms /   169 runs   (    0.73 ms per token,  1365.97 tokens per second)
llama\_print\_timings: prompt eval time =   267.03 ms /    14 tokens (   19.07 ms per token,    52.43 tokens per second)
llama\_print\_timings:        eval time =  8794.21 ms /   168 runs   (   52.35 ms per token,    19.10 tokens per second)
llama\_print\_timings:       total time =  9485.38 ms

Query engine set up with LlamaCPP[¶](https://docs.llamaindex.ai/en/stable/examples/llm/llama_2_llama_cpp/#query-engine-set-up-with-llamacpp)
--------------------------------------------------------------------------------------------------------------------------------------------

We can simply pass in the `LlamaCPP` LLM abstraction to the `LlamaIndex` query engine as usual.

But first, let's change the global tokenizer to match our LLM.

In \[ \]:

Copied!

from llama\_index.core import set\_global\_tokenizer
from transformers import AutoTokenizer

set\_global\_tokenizer(
    AutoTokenizer.from\_pretrained("NousResearch/Llama-2-7b-chat-hf").encode
)

from llama\_index.core import set\_global\_tokenizer from transformers import AutoTokenizer set\_global\_tokenizer( AutoTokenizer.from\_pretrained("NousResearch/Llama-2-7b-chat-hf").encode )

In \[ \]:

Copied!

\# use Huggingface embeddings
from llama\_index.embeddings.huggingface import HuggingFaceEmbedding

embed\_model \= HuggingFaceEmbedding(model\_name\="BAAI/bge-small-en-v1.5")

\# use Huggingface embeddings from llama\_index.embeddings.huggingface import HuggingFaceEmbedding embed\_model = HuggingFaceEmbedding(model\_name="BAAI/bge-small-en-v1.5")

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader(
    "../../../examples/paul\_graham\_essay/data"
).load\_data()

\# load documents documents = SimpleDirectoryReader( "../../../examples/paul\_graham\_essay/data" ).load\_data()

In \[ \]:

Copied!

\# create vector store index
index \= VectorStoreIndex.from\_documents(documents, embed\_model\=embed\_model)

\# create vector store index index = VectorStoreIndex.from\_documents(documents, embed\_model=embed\_model)

In \[ \]:

Copied!

\# set up query engine
query\_engine \= index.as\_query\_engine(llm\=llm)

\# set up query engine query\_engine = index.as\_query\_engine(llm=llm)

In \[ \]:

Copied!

response \= query\_engine.query("What did the author do growing up?")
print(response)

response = query\_engine.query("What did the author do growing up?") print(response)

Llama.generate: prefix-match hit

  Based on the given context information, the author's childhood activities were writing short stories and programming. They wrote programs on punch cards using an early version of Fortran and later used a TRS-80 microcomputer to write simple games, a program to predict the height of model rockets, and a word processor that their father used to write at least one book.

llama\_print\_timings:        load time =  1204.19 ms
llama\_print\_timings:      sample time =    56.13 ms /    80 runs   (    0.70 ms per token,  1425.21 tokens per second)
llama\_print\_timings: prompt eval time = 65280.71 ms /  2272 tokens (   28.73 ms per token,    34.80 tokens per second)
llama\_print\_timings:        eval time =  6877.38 ms /    79 runs   (   87.06 ms per token,    11.49 tokens per second)
llama\_print\_timings:       total time = 72315.85 ms

Back to top

[Previous Replicate - Llama 2 13B](https://docs.llamaindex.ai/en/stable/examples/llm/llama_2/)[Next 🦙 x 🦙 Rap Battle](https://docs.llamaindex.ai/en/stable/examples/llm/llama_2_rap_battle/)
