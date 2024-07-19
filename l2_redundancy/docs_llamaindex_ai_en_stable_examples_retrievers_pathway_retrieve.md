Title: Pathway Retriever - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/retrievers/pathway_retriever/

Markdown Content:
Pathway Retriever - LlamaIndex


> [Pathway](https://pathway.com/) is an open data processing framework. It allows you to easily develop data transformation pipelines and Machine Learning applications that work with live data sources and changing data.

This notebook demonstrates how to use a live data indexing pipeline with `LlamaIndex`. You can query the results of this pipeline from your LLM application using the provided `PathwayRetriever`. However, under the hood, Pathway updates the index on each data change giving you always up-to-date answers.

In this notebook, we will use a [public demo document processing pipeline](https://pathway.com/solutions/ai-pipelines#try-it-out) that:

1.  Monitors several cloud data sources for data changes.
2.  Builds a vector index for the data.

To have your own document processing pipeline check the [hosted offering](https://pathway.com/solutions/ai-pipelines) or [build your own](https://pathway.com/developers/user-guide/llm-xpack/vectorstore_pipeline/) by following this notebook.

We will connect to the index using `llama_index.retrievers.pathway.PathwayRetriever` retriever, which implements the `retrieve` interface.

The basic pipeline described in this document allows to effortlessly build a simple index of files stored in a cloud location. However, Pathway provides everything needed to build realtime data pipelines and apps, including SQL-like able operations such as groupby-reductions and joins between disparate data sources, time-based grouping and windowing of data, and a wide array of connectors.

For more details about Pathway data ingestion pipeline and vector store, visit [vector store pipeline](https://pathway.com/developers/showcases/vectorstore_pipeline).

Prerequisites[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/pathway_retriever/#prerequisites)
-----------------------------------------------------------------------------------------------------------

To use `PathwayRetrievier` you must install `llama-index-retrievers-pathway` package.

In \[ \]:

Copied!

!pip install llama\-index\-retrievers\-pathway

!pip install llama-index-retrievers-pathway

Create Retriever for llama-index[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/pathway_retriever/#create-retriever-for-llama-index)
-------------------------------------------------------------------------------------------------------------------------------------------------

To instantiate and configure `PathwayRetriever` you need to provide either the `url` or the `host` and `port` of your document indexing pipeline. In the code below we use a publicly available [demo pipeline](https://pathway.com/solutions/ai-pipelines#try-it-out), which REST API you can access at `https://demo-document-indexing.pathway.stream`. This demo ingests documents from [Google Drive](https://drive.google.com/drive/u/0/folders/1cULDv2OaViJBmOfG5WB0oWcgayNrGtVs) and [Sharepoint](https://navalgo.sharepoint.com/sites/ConnectorSandbox/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FConnectorSandbox%2FShared%20Documents%2FIndexerSandbox&p=true&ga=1) and maintains an index for retrieving documents.

In \[ \]:

Copied!

from llama\_index.retrievers.pathway import PathwayRetriever

retriever \= PathwayRetriever(
    url\="https://demo-document-indexing.pathway.stream"
)
retriever.retrieve(str\_or\_query\_bundle\="what is pathway")

from llama\_index.retrievers.pathway import PathwayRetriever retriever = PathwayRetriever( url="https://demo-document-indexing.pathway.stream" ) retriever.retrieve(str\_or\_query\_bundle="what is pathway")

**Your turn!** [Get your pipeline](https://pathway.com/solutions/ai-pipelines) or upload [new documents](https://chat-realtime-sharepoint-gdrive.demo.pathway.com/) to the demo pipeline and retry the query!

Use in Query Engine[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/pathway_retriever/#use-in-query-engine)
-----------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core.query\_engine import RetrieverQueryEngine

query\_engine \= RetrieverQueryEngine.from\_args(
    retriever,
)

from llama\_index.core.query\_engine import RetrieverQueryEngine query\_engine = RetrieverQueryEngine.from\_args( retriever, )

In \[ \]:

Copied!

response \= query\_engine.query("Tell me about Pathway")
print(str(response))

response = query\_engine.query("Tell me about Pathway") print(str(response))

Building your own data processing pipeline[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/pathway_retriever/#building-your-own-data-processing-pipeline)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Prerequisites[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/pathway_retriever/#prerequisites)

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

### Define data sources tracked by Pathway[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/pathway_retriever/#define-data-sources-tracked-by-pathway)

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

### Create the document indexing pipeline[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/pathway_retriever/#create-the-document-indexing-pipeline)

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

### Connect the retriever to the custom pipeline[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/pathway_retriever/#connect-the-retriever-to-the-custom-pipeline)

In \[ \]:

Copied!

from llama\_index.retrievers.pathway import PathwayRetriever

retriever \= PathwayRetriever(host\=PATHWAY\_HOST, port\=PATHWAY\_PORT)
retriever.retrieve(str\_or\_query\_bundle\="what is pathway")

from llama\_index.retrievers.pathway import PathwayRetriever retriever = PathwayRetriever(host=PATHWAY\_HOST, port=PATHWAY\_PORT) retriever.retrieve(str\_or\_query\_bundle="what is pathway")

Back to top

[Previous Chunk + Document Hybrid Retrieval with Long-Context Embeddings (Together.ai)](https://docs.llamaindex.ai/en/stable/examples/retrievers/multi_doc_together_hybrid/)[Next Reciprocal Rerank Fusion Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/reciprocal_rerank_fusion/)
