Title: Weaviate Reader - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/data_connectors/WeaviateDemo/

Markdown Content:
Weaviate Reader - LlamaIndex


In \[ \]:

Copied!

%pip install llama\-index\-readers\-weaviate

%pip install llama-index-readers-weaviate

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import weaviate
from llama\_index.readers.weaviate import WeaviateReader

import weaviate from llama\_index.readers.weaviate import WeaviateReader

In \[ \]:

Copied!

\# See https://weaviate.io/developers/weaviate/current/client-libraries/python.html
\# for more details on authentication
resource\_owner\_config \= weaviate.AuthClientPassword(
    username\="<username>",
    password\="<password>",
)

\# initialize reader
reader \= WeaviateReader(
    "https://<cluster-id>.semi.network/",
    auth\_client\_secret\=resource\_owner\_config,
)

\# See https://weaviate.io/developers/weaviate/current/client-libraries/python.html # for more details on authentication resource\_owner\_config = weaviate.AuthClientPassword( username="", password="", ) # initialize reader reader = WeaviateReader( "https://.semi.network/", auth\_client\_secret=resource\_owner\_config, )

You have two options for the Weaviate reader: 1) directly specify the class\_name and properties, or 2) input the raw graphql\_query. Examples are shown below.

In \[ \]:

Copied!

\# 1) load data using class\_name and properties
\# docs = reader.load\_data(
\#    class\_name="Author", properties=\["name", "description"\], separate\_documents=True
\# )

documents \= reader.load\_data(
    class\_name\="<class\_name>",
    properties\=\["property1", "property2", "..."\],
    separate\_documents\=True,
)

\# 1) load data using class\_name and properties # docs = reader.load\_data( # class\_name="Author", properties=\["name", "description"\], separate\_documents=True # ) documents = reader.load\_data( class\_name="", properties=\["property1", "property2", "..."\], separate\_documents=True, )

In \[ \]:

Copied!

\# 2) example GraphQL query
\# query = """
\# {
\#   Get {
\#     Author {
\#       name
\#       description
\#     }
\#   }
\# }
\# """
\# docs = reader.load\_data(graphql\_query=query, separate\_documents=True)

query \= """
{
  Get {
    <class\_name> {
      <property1>
      <property2>
      ...
    }
  }
}
"""

documents \= reader.load\_data(graphql\_query\=query, separate\_documents\=True)

\# 2) example GraphQL query # query = """ # { # Get { # Author { # name # description # } # } # } # """ # docs = reader.load\_data(graphql\_query=query, separate\_documents=True) query = """ { Get { { ... } } } """ documents = reader.load\_data(graphql\_query=query, separate\_documents=True)

### Create index[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WeaviateDemo/#create-index)

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

[Previous Twitter Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/TwitterDemo/)[Next Web Page Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/)
