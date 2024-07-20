Title: MistralRS LLM - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/llm/mistral_rs/

Markdown Content:
MistralRS LLM - LlamaIndex


**NOTE:** MistralRS requires a rust package manager called `cargo` to be installed. Visit [https://rustup.rs/](https://rustup.rs/) for installation details.

In \[ \]:

Copied!

%pip install llama\-index\-core
%pip install llama\-index\-readers\-file
%pip install llama\-index\-llms\-mistral\-rs
%pip install llama\-index\-llms\-huggingface

%pip install llama-index-core %pip install llama-index-readers-file %pip install llama-index-llms-mistral-rs %pip install llama-index-llms-huggingface

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama\_index.core.embeddings import resolve\_embed\_model
from llama\_index.llms.mistral\_rs import MistralRS
from mistralrs import Which, Architecture

documents \= SimpleDirectoryReader("data").load\_data()

\# bge embedding model
Settings.embed\_model \= resolve\_embed\_model("local:BAAI/bge-small-en-v1.5")

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings from llama\_index.core.embeddings import resolve\_embed\_model from llama\_index.llms.mistral\_rs import MistralRS from mistralrs import Which, Architecture documents = SimpleDirectoryReader("data").load\_data() # bge embedding model Settings.embed\_model = resolve\_embed\_model("local:BAAI/bge-small-en-v1.5")

MistralRS uses model IDs from huggingface hub.

In \[ \]:

Copied!

\# Full Model
Settings.llm \= MistralRS(
    which\=Which.Plain(
        model\_id\="mistralai/Mistral-7B-Instruct-v0.1",
        arch\=Architecture.Mistral,
        tokenizer\_json\=None,
        repeat\_last\_n\=64,
    ),
    max\_new\_tokens\=4096,
    context\_window\=1024 \* 5,
)

\# GGUF Model, Quantized
Settings.llm \= MistralRS(
    which\=Which.GGUF(
        tok\_model\_id\="mistralai/Mistral-7B-Instruct-v0.1",
        quantized\_model\_id\="TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
        quantized\_filename\="mistral-7b-instruct-v0.1.Q4\_K\_M.gguf",
        tokenizer\_json\=None,
        repeat\_last\_n\=64,
    ),
    max\_new\_tokens\=4096,
    context\_window\=1024 \* 5,
)

\# Full Model Settings.llm = MistralRS( which=Which.Plain( model\_id="mistralai/Mistral-7B-Instruct-v0.1", arch=Architecture.Mistral, tokenizer\_json=None, repeat\_last\_n=64, ), max\_new\_tokens=4096, context\_window=1024 \* 5, ) # GGUF Model, Quantized Settings.llm = MistralRS( which=Which.GGUF( tok\_model\_id="mistralai/Mistral-7B-Instruct-v0.1", quantized\_model\_id="TheBloke/Mistral-7B-Instruct-v0.1-GGUF", quantized\_filename="mistral-7b-instruct-v0.1.Q4\_K\_M.gguf", tokenizer\_json=None, repeat\_last\_n=64, ), max\_new\_tokens=4096, context\_window=1024 \* 5, )

In \[ \]:

Copied!

index \= VectorStoreIndex.from\_documents(
    documents,
)

index = VectorStoreIndex.from\_documents( documents, )

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("How do I pronounce graphene?")
print(response)

query\_engine = index.as\_query\_engine() response = query\_engine.query("How do I pronounce graphene?") print(response)

Back to top

[Previous Maritalk](https://docs.llamaindex.ai/en/stable/examples/llm/maritalk/)[Next MistralAI](https://docs.llamaindex.ai/en/stable/examples/llm/mistralai/)
