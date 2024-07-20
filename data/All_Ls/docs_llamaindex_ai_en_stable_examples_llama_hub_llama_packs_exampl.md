Title: Llama Packs Example - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/llama_hub/llama_packs_example/

Markdown Content:
Llama Packs Example - LlamaIndex


[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jerryjliu/llama_index/blob/main/docs/docs/examples/llama_hub/llama_packs_example.ipynb)

This example shows you how to use a simple Llama Pack with VoyageAI. We show the following:

*   How to download a Llama Pack
*   How to inspect its modules
*   How to run it out of the box
*   How to customize it.

You can find all packs on [https://llamahub.ai](https://llamahub.ai/)

### Setup Data[¶](https://docs.llamaindex.ai/en/stable/examples/llama_hub/llama_packs_example/#setup-data)

In \[ \]:

Copied!

!wget "https://www.dropbox.com/s/f6bmb19xdg0xedm/paul\_graham\_essay.txt?dl=1" \-O paul\_graham\_essay.txt

!wget "https://www.dropbox.com/s/f6bmb19xdg0xedm/paul\_graham\_essay.txt?dl=1" -O paul\_graham\_essay.txt

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

\# load in some sample data
reader \= SimpleDirectoryReader(input\_files\=\["paul\_graham\_essay.txt"\])
documents \= reader.load\_data()

from llama\_index.core import SimpleDirectoryReader # load in some sample data reader = SimpleDirectoryReader(input\_files=\["paul\_graham\_essay.txt"\]) documents = reader.load\_data()

### Download and Initialize Pack[¶](https://docs.llamaindex.ai/en/stable/examples/llama_hub/llama_packs_example/#download-and-initialize-pack)

We use `download_llama_pack` to download the pack class, and then we initialize it with documents.

Every pack will have different initialization parameters. You can find more about the initialization parameters for each pack through its [README](https://github.com/logan-markewich/llama-hub/tree/main/llama_hub/llama_packs/voyage_query_engine) (also on LlamaHub).

**NOTE**: You must also specify an output directory. In this case the pack is downloaded to `voyage_pack`. This allows you to customize and make changes to the file, and import it later!

In \[ \]:

Copied!

from llama\_index.core.llama\_pack import download\_llama\_pack

VoyageQueryEnginePack \= download\_llama\_pack(
    "VoyageQueryEnginePack", "./voyage\_pack"
)

from llama\_index.core.llama\_pack import download\_llama\_pack VoyageQueryEnginePack = download\_llama\_pack( "VoyageQueryEnginePack", "./voyage\_pack" )

In \[ \]:

Copied!

voyage\_pack \= VoyageQueryEnginePack(documents)

voyage\_pack = VoyageQueryEnginePack(documents)

### Inspect Modules[¶](https://docs.llamaindex.ai/en/stable/examples/llama_hub/llama_packs_example/#inspect-modules)

In \[ \]:

Copied!

modules \= voyage\_pack.get\_modules()
display(modules)

modules = voyage\_pack.get\_modules() display(modules)

{'llm': OpenAI(callback\_manager=<llama\_index.callbacks.base.CallbackManager object at 0x11fdaae90>, model='gpt-4', temperature=0.1, max\_tokens=None, additional\_kwargs={}, max\_retries=3, timeout=60.0, api\_key='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', api\_base='https://api.openai.com/v1', api\_version=''),
 'index': <llama\_index.indices.vector\_store.base.VectorStoreIndex at 0x2bccb3b50>}

In \[ \]:

Copied!

llm \= modules\["llm"\]
vector\_index \= modules\["index"\]

llm = modules\["llm"\] vector\_index = modules\["index"\]

In \[ \]:

Copied!

\# try out LLM
response \= llm.complete("hello world")
print(str(response))

\# try out LLM response = llm.complete("hello world") print(str(response))

In \[ \]:

Copied!

\# try out retriever
retriever \= vector\_index.as\_retriever()
results \= retriever.retrieve("What did the author do growing up?")
print(str(results\[0\].get\_content()))

\# try out retriever retriever = vector\_index.as\_retriever() results = retriever.retrieve("What did the author do growing up?") print(str(results\[0\].get\_content()))

### Run Pack[¶](https://docs.llamaindex.ai/en/stable/examples/llama_hub/llama_packs_example/#run-pack)

Every pack has a `run` function that will accomplish a certain task out of the box. Here we will go through the full RAG pipeline with VoyageAI embeddings.

In \[ \]:

Copied!

\# this will run the full pack
response \= voyage\_pack.run(
    "What did the author do growing up?", similarity\_top\_k\=2
)

\# this will run the full pack response = voyage\_pack.run( "What did the author do growing up?", similarity\_top\_k=2 )

In \[ \]:

Copied!

print(str(response))

print(str(response))

The author spent his time outside of school mainly writing and programming. He wrote short stories and attempted to write programs on an IBM 1401. Later, he started programming on a TRS-80, creating simple games and a word processor. He also painted still lives while studying at the Accademia.

### Try Customizing Pack[¶](https://docs.llamaindex.ai/en/stable/examples/llama_hub/llama_packs_example/#try-customizing-pack)

A major feature of LlamaPacks is that you can and should inspect and modify the code templates!

In this example we'll show how to customize the template with a different LLM, while keeping Voyage embeddings, and then re-use it. We'll use Anthropic instead.

Let's go into `voyage_pack` and create a copy.

1.  For demo purposes we'll copy `voyage_pack` into `voyage_pack_copy`.
2.  Go into `voyage_pack_copy/base.py` and look at the `VoyageQueryEnginePack` class definition. This is where all the core logic lives. As you can see the pack class itself is a very light base abstraction. You're free to copy/paste the code as you wish.
3.  Go into the line in the `__init__` where it do `llm = OpenAI(model="gpt-4")` and instead change it to `llm = Anthropic()` (which defaults to claude-2).
4.  Do `from llama_index.llms import Anthropic` and ensure that `ANTHROPIC_API_KEY` is set in your env variable.
5.  Now you can use!

In the below sections we'll directly re-import the modified `VoyageQueryEnginePack` and use it.

In \[ \]:

Copied!

from voyage\_pack\_copy.base import VoyageQueryEnginePack

voyage\_pack \= VoyageQueryEnginePack(documents)

from voyage\_pack\_copy.base import VoyageQueryEnginePack voyage\_pack = VoyageQueryEnginePack(documents)

In \[ \]:

Copied!

response \= voyage\_pack.run("What did the author do during his time in RISD?")
print(str(response))

response = voyage\_pack.run("What did the author do during his time in RISD?") print(str(response))

 Unfortunately I do not have enough context in the provided information to definitively state what the author did during his time at RISD. The passage mentions that he learned a lot in a color class he took there, that he was basically teaching himself to paint, and that in 1993 he dropped out. But there are no specific details provided about his activities or course of study during his time enrolled at RISD. I apologize that I cannot provide a more complete response.

Back to top

[Previous Llama Pack - Resume Screener 📄](https://docs.llamaindex.ai/en/stable/examples/llama_hub/llama_pack_resume/)[Next Building Evaluation from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/evaluation/)

Hi, how can I help you?

🦙
