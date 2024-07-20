Title: Pinecone Reader - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/data_connectors/PineconeDemo/

Markdown Content:
Pinecone Reader - LlamaIndex


In \[ \]:

Copied!

%pip install llama\-index\-readers\-pinecone

%pip install llama-index-readers-pinecone

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

In \[ \]:

Copied!

api\_key \= "<api\_key>"

api\_key = ""

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

from llama\_index.readers.pinecone import PineconeReader

from llama\_index.readers.pinecone import PineconeReader

In \[ \]:

Copied!

reader \= PineconeReader(api\_key\=api\_key, environment\="us-west1-gcp")

reader = PineconeReader(api\_key=api\_key, environment="us-west1-gcp")

In \[ \]:

Copied!

\# the id\_to\_text\_map specifies a mapping from the ID specified in Pinecone to your text.
id\_to\_text\_map \= {
    "id1": "text blob 1",
    "id2": "text blob 2",
}

\# the query\_vector is an embedding representation of your query\_vector
\# Example query vector:
\#   query\_vector=\[0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3\]

query\_vector \= \[n1, n2, n3, ...\]

\# the id\_to\_text\_map specifies a mapping from the ID specified in Pinecone to your text. id\_to\_text\_map = { "id1": "text blob 1", "id2": "text blob 2", } # the query\_vector is an embedding representation of your query\_vector # Example query vector: # query\_vector=\[0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3\] query\_vector = \[n1, n2, n3, ...\]

In \[ \]:

Copied!

\# NOTE: Required args are index\_name, id\_to\_text\_map, vector.
\# In addition, we pass-through all kwargs that can be passed into the \`Query\` operation in Pinecone.
\# See the API reference: https://docs.pinecone.io/reference/query
\# and also the Python client: https://github.com/pinecone-io/pinecone-python-client
\# for more details.
documents \= reader.load\_data(
    index\_name\="quickstart",
    id\_to\_text\_map\=id\_to\_text\_map,
    top\_k\=3,
    vector\=query\_vector,
    separate\_documents\=True,
)

\# NOTE: Required args are index\_name, id\_to\_text\_map, vector. # In addition, we pass-through all kwargs that can be passed into the \`Query\` operation in Pinecone. # See the API reference: https://docs.pinecone.io/reference/query # and also the Python client: https://github.com/pinecone-io/pinecone-python-client # for more details. documents = reader.load\_data( index\_name="quickstart", id\_to\_text\_map=id\_to\_text\_map, top\_k=3, vector=query\_vector, separate\_documents=True, )

### Create index[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/PineconeDemo/#create-index)

In \[ \]:

Copied!

index \= SummaryIndex.from\_documents(documents)

index = SummaryIndex.from\_documents(documents)

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("<query\_text>")

\# set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine() response = query\_engine.query("")

In \[ \]:

Copied!

display(Markdown(f"<b>{response}</b>"))

display(Markdown(f"**{response}**"))

Back to top

[Previous Pathway Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/PathwayReaderDemo/)[Next Psychic Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/PsychicDemo/)
