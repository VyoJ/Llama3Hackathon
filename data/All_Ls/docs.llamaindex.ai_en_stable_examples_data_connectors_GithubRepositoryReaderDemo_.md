Title: Github Repo Reader - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/data_connectors/GithubRepositoryReaderDemo/

Markdown Content:
Github Repo Reader - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-readers\-github

%pip install llama-index-readers-github

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

\# This is due to the fact that we use asyncio.loop\_until\_complete in
\# the DiscordReader. Since the Jupyter kernel itself runs on
\# an event loop, we need to add some help with nesting
import nest\_asyncio

nest\_asyncio.apply()

\# This is due to the fact that we use asyncio.loop\_until\_complete in # the DiscordReader. Since the Jupyter kernel itself runs on # an event loop, we need to add some help with nesting import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

%env OPENAI\_API\_KEY\=sk\-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
from llama\_index.core import VectorStoreIndex
from llama\_index.readers.github import GithubRepositoryReader, GithubClient
from IPython.display import Markdown, display
import os

%env OPENAI\_API\_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx from llama\_index.core import VectorStoreIndex from llama\_index.readers.github import GithubRepositoryReader, GithubClient from IPython.display import Markdown, display import os

env: OPENAI\_API\_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

In \[ \]:

Copied!

%env GITHUB\_TOKEN\=github\_pat\_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
github\_token \= os.environ.get("GITHUB\_TOKEN")
owner \= "jerryjliu"
repo \= "llama\_index"
branch \= "main"

github\_client \= GithubClient(github\_token\=github\_token, verbose\=True)

documents \= GithubRepositoryReader(
    github\_client\=github\_client,
    owner\=owner,
    repo\=repo,
    use\_parser\=False,
    verbose\=False,
    filter\_directories\=(
        \["docs"\],
        GithubRepositoryReader.FilterType.INCLUDE,
    ),
    filter\_file\_extensions\=(
        \[
            ".png",
            ".jpg",
            ".jpeg",
            ".gif",
            ".svg",
            ".ico",
            "json",
            ".ipynb",
        \],
        GithubRepositoryReader.FilterType.EXCLUDE,
    ),
).load\_data(branch\=branch)

%env GITHUB\_TOKEN=github\_pat\_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx github\_token = os.environ.get("GITHUB\_TOKEN") owner = "jerryjliu" repo = "llama\_index" branch = "main" github\_client = GithubClient(github\_token=github\_token, verbose=True) documents = GithubRepositoryReader( github\_client=github\_client, owner=owner, repo=repo, use\_parser=False, verbose=False, filter\_directories=( \["docs"\], GithubRepositoryReader.FilterType.INCLUDE, ), filter\_file\_extensions=( \[ ".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico", "json", ".ipynb", \], GithubRepositoryReader.FilterType.EXCLUDE, ), ).load\_data(branch=branch)

In \[ \]:

Copied!

index \= VectorStoreIndex.from\_documents(documents)

index = VectorStoreIndex.from\_documents(documents)

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine()
response \= query\_engine.query(
    "What is the difference between VectorStoreIndex and SummaryIndex?",
    verbose\=True,
)

query\_engine = index.as\_query\_engine() response = query\_engine.query( "What is the difference between VectorStoreIndex and SummaryIndex?", verbose=True, )

In \[ \]:

Copied!

display(Markdown(f"<b>{response}</b>"))

display(Markdown(f"**{response}**"))

Back to top

[Previous Faiss Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/FaissDemo/)[Next Google Chat Reader Test](https://docs.llamaindex.ai/en/stable/examples/data_connectors/GoogleChatDemo/)
