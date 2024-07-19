Title: Pathway Reader - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/data_connectors/PathwayReaderDemo/

Markdown Content:
Pathway Reader - LlamaIndex


> [Pathway](https://pathway.com/) is an open data processing framework. It allows you to easily develop data transformation pipelines and Machine Learning applications that work with live data sources and changing data.

This notebook demonstrates how to set up a live data indexing pipeline. You can query the results of this pipeline from your LLM application in the same manner as you would a regular reader. However, under the hood, Pathway updates the index on each data change giving you always up-to-date answers.

In this notebook, we will first connect the `llama_index.readers.pathway.PathwayReader` reader to a [public demo document processing pipeline](https://pathway.com/solutions/ai-pipelines#try-it-out) that:

1.  Monitors several cloud data sources for data changes.
2.  Builds a vector index for the data.

To have your own document processing pipeline check the [hosted offering](https://pathway.com/solutions/ai-pipelines) or [build your own](https://pathway.com/developers/user-guide/llm-xpack/vectorstore_pipeline/) by following this notebook.

The basic pipeline described in this document allows to effortlessly build a simple index of files stored in a cloud location. However, Pathway provides everything needed to build realtime data pipelines and apps, including SQL-like able operations such as groupby-reductions and joins between disparate data sources, time-based grouping and windowing of data, and a wide array of connectors.

For more details about Pathway data ingestion pipeline and vector store, visit [vector store pipeline](https://pathway.com/developers/user-guide/llm-xpack/vectorstore_pipeline/).

Prerequisites[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/PathwayReaderDemo/#prerequisites)
----------------------------------------------------------------------------------------------------------------

Install the `llama-index-readers-pathway` integration

In \[ \]:

Copied!

%pip install llama\-index\-readers\-pathway

%pip install llama-index-readers-pathway

Configure logging

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.ERROR)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.ERROR) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

Set up your OpenAI API key.

In \[ \]:

Copied!

import getpass
import os

\# omit if embedder of choice is not OpenAI
if "OPENAI\_API\_KEY" not in os.environ:
    os.environ\["OPENAI\_API\_KEY"\] \= getpass.getpass("OpenAI API Key:")

import getpass import os # omit if embedder of choice is not OpenAI if "OPENAI\_API\_KEY" not in os.environ: os.environ\["OPENAI\_API\_KEY"\] = getpass.getpass("OpenAI API Key:")

Create the reader and connect to a public pipeline[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/PathwayReaderDemo/#create-the-reader-and-connect-to-a-public-pipeline)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To instantiate and configure `PathwayReader` you need to provide either the `url` or the `host` and `port` of your document indexing pipeline. In the code below we use a publicly available [demo pipeline](https://pathway.com/solutions/ai-pipelines#try-it-out), which REST API you can access at `https://demo-document-indexing.pathway.stream`. This demo ingests documents from [Google Drive](https://drive.google.com/drive/u/0/folders/1cULDv2OaViJBmOfG5WB0oWcgayNrGtVs) and [Sharepoint](https://navalgo.sharepoint.com/sites/ConnectorSandbox/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FConnectorSandbox%2FShared%20Documents%2FIndexerSandbox&p=true&ga=1) and maintains an index for retrieving documents.

In \[ \]:

Copied!

from llama\_index.readers.pathway import PathwayReader

reader \= PathwayReader(url\="https://demo-document-indexing.pathway.stream")
\# let us search with some text
reader.load\_data(query\_text\="What is Pathway")

from llama\_index.readers.pathway import PathwayReader reader = PathwayReader(url="https://demo-document-indexing.pathway.stream") # let us search with some text reader.load\_data(query\_text="What is Pathway")

Create a summary index with llama-index[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/PathwayReaderDemo/#create-a-summary-index-with-llama-index)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

docs \= reader.load\_data(query\_text\="What is Pathway", k\=2)
from llama\_index.core import SummaryIndex

index \= SummaryIndex.from\_documents(docs)
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What does Pathway do?")
print(response)

docs = reader.load\_data(query\_text="What is Pathway", k=2) from llama\_index.core import SummaryIndex index = SummaryIndex.from\_documents(docs) query\_engine = index.as\_query\_engine() response = query\_engine.query("What does Pathway do?") print(response)

Building your own data processing pipeline[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/PathwayReaderDemo/#building-your-own-data-processing-pipeline)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Prerequisites[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/PathwayReaderDemo/#prerequisites)

Install `pathway` package. Then download sample data.

In \[ \]:

Copied!

%pip install pathway
%pip install llama\-index\-embeddings\-openai

%pip install pathway %pip install llama-index-embeddings-openai

In \[ \]:

Copied!

!mkdir \-p 'data/'
!wget 'https://gist.githubusercontent.com/janchorowski/dd22a293f3d99d1b726eedc7d46d2fc0/raw/pathway\_readme.md' \-O 'data/pathway\_readme.md'

!mkdir -p 'data/' !wget 'https://gist.githubusercontent.com/janchorowski/dd22a293f3d99d1b726eedc7d46d2fc0/raw/pathway\_readme.md' -O 'data/pathway\_readme.md'

### Define data sources tracked by Pathway[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/PathwayReaderDemo/#define-data-sources-tracked-by-pathway)

Pathway can listen to many sources simultaneously, such as local files, S3 folders, cloud storage and any data stream for data changes.

See [pathway-io](https://pathway.com/developers/api-docs/pathway-io) for more information.

In \[ \]:

Copied!

import pathway as pw

data\_sources \= \[\]
data\_sources.append(
    pw.io.fs.read(
        "./data",
        format\="binary",
        mode\="streaming",
        with\_metadata\=True,
    )  \# This creates a \`pathway\` connector that tracks
    \# all the files in the ./data directory
)

\# This creates a connector that tracks files in Google drive.
\# please follow the instructions at https://pathway.com/developers/tutorials/connectors/gdrive-connector/ to get credentials
\# data\_sources.append(
\#     pw.io.gdrive.read(object\_id="17H4YpBOAKQzEJ93xmC2z170l0bP2npMy", service\_user\_credentials\_file="credentials.json", with\_metadata=True))

import pathway as pw data\_sources = \[\] data\_sources.append( pw.io.fs.read( "./data", format="binary", mode="streaming", with\_metadata=True, ) # This creates a \`pathway\` connector that tracks # all the files in the ./data directory ) # This creates a connector that tracks files in Google drive. # please follow the instructions at https://pathway.com/developers/tutorials/connectors/gdrive-connector/ to get credentials # data\_sources.append( # pw.io.gdrive.read(object\_id="17H4YpBOAKQzEJ93xmC2z170l0bP2npMy", service\_user\_credentials\_file="credentials.json", with\_metadata=True))

### Create the document indexing pipeline[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/PathwayReaderDemo/#create-the-document-indexing-pipeline)

Let us create the document indexing pipeline. The `transformations` should be a list of `TransformComponent`s ending with an `Embedding` transformation.

In this example, let's first split the text first using `TokenTextSplitter`, then embed with `OpenAIEmbedding`.

In \[ \]:

Copied!

from pathway.xpacks.llm.vector\_store import VectorStoreServer
from llama\_index.embeddings.openai import OpenAIEmbedding
from llama\_index.core.node\_parser import TokenTextSplitter

embed\_model \= OpenAIEmbedding(embed\_batch\_size\=10)

transformations\_example \= \[
    TokenTextSplitter(
        chunk\_size\=150,
        chunk\_overlap\=10,
        separator\=" ",
    ),
    embed\_model,
\]

processing\_pipeline \= VectorStoreServer.from\_llamaindex\_components(
    \*data\_sources,
    transformations\=transformations\_example,
)

\# Define the Host and port that Pathway will be on
PATHWAY\_HOST \= "127.0.0.1"
PATHWAY\_PORT \= 8754

\# \`threaded\` runs pathway in detached mode, we have to set it to False when running from terminal or container
\# for more information on \`with\_cache\` check out https://pathway.com/developers/api-docs/persistence-api
processing\_pipeline.run\_server(
    host\=PATHWAY\_HOST, port\=PATHWAY\_PORT, with\_cache\=False, threaded\=True
)

from pathway.xpacks.llm.vector\_store import VectorStoreServer from llama\_index.embeddings.openai import OpenAIEmbedding from llama\_index.core.node\_parser import TokenTextSplitter embed\_model = OpenAIEmbedding(embed\_batch\_size=10) transformations\_example = \[ TokenTextSplitter( chunk\_size=150, chunk\_overlap=10, separator=" ", ), embed\_model, \] processing\_pipeline = VectorStoreServer.from\_llamaindex\_components( \*data\_sources, transformations=transformations\_example, ) # Define the Host and port that Pathway will be on PATHWAY\_HOST = "127.0.0.1" PATHWAY\_PORT = 8754 # \`threaded\` runs pathway in detached mode, we have to set it to False when running from terminal or container # for more information on \`with\_cache\` check out https://pathway.com/developers/api-docs/persistence-api processing\_pipeline.run\_server( host=PATHWAY\_HOST, port=PATHWAY\_PORT, with\_cache=False, threaded=True )

### Connect the reader to the custom pipeline[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/PathwayReaderDemo/#connect-the-reader-to-the-custom-pipeline)

In \[ \]:

Copied!

from llama\_index.readers.pathway import PathwayReader

reader \= PathwayReader(host\=PATHWAY\_HOST, port\=PATHWAY\_PORT)
\# let us search with some text
reader.load\_data(query\_text\="What is Pathway")

from llama\_index.readers.pathway import PathwayReader reader = PathwayReader(host=PATHWAY\_HOST, port=PATHWAY\_PORT) # let us search with some text reader.load\_data(query\_text="What is Pathway")

Back to top

[Previous Obsidian Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/ObsidianReaderDemo/)[Next Pinecone Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/PineconeDemo/)
