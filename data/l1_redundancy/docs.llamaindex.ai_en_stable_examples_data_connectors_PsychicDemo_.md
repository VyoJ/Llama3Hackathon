Title: Psychic Reader - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/data_connectors/PsychicDemo/

Markdown Content:
Psychic Reader - LlamaIndex


Demonstrates the Psychic data connector. Used to query data from many SaaS tools from a single LlamaIndex-compatible API.

Prerequisites[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/PsychicDemo/#prerequisites)
----------------------------------------------------------------------------------------------------------

Connections must first be established from the Psychic dashboard or React hook before documents can be loaded. Refer to [https://docs.psychic.dev/](https://docs.psychic.dev/) for more info.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-readers\-psychic

%pip install llama-index-readers-psychic

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import logging
import sys
import os

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys import os logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

In \[ \]:

Copied!

from llama\_index.core import SummaryIndex
from llama\_index.readers.psychic import PsychicReader
from IPython.display import Markdown, display

from llama\_index.core import SummaryIndex from llama\_index.readers.psychic import PsychicReader from IPython.display import Markdown, display

In \[ \]:

Copied!

\# Get Psychic API key from https://dashboard.psychic.dev/api-keys
psychic\_key \= "PSYCHIC\_API\_KEY"
\# Connector ID and Account ID are typically set programatically based on the application state.
account\_id \= "ACCOUNT\_ID"
connector\_id \= "notion"
documents \= PsychicReader(psychic\_key\=psychic\_key).load\_data(
    connector\_id\=connector\_id, account\_id\=account\_id
)

\# Get Psychic API key from https://dashboard.psychic.dev/api-keys psychic\_key = "PSYCHIC\_API\_KEY" # Connector ID and Account ID are typically set programatically based on the application state. account\_id = "ACCOUNT\_ID" connector\_id = "notion" documents = PsychicReader(psychic\_key=psychic\_key).load\_data( connector\_id=connector\_id, account\_id=account\_id )

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
os.environ\["OPENAI\_API\_KEY"\] \= "OPENAI\_API\_KEY"
index \= SummaryIndex.from\_documents(documents)
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What is Psychic's privacy policy?")
display(Markdown(f"<b>{response}</b>"))

\# set Logging to DEBUG for more detailed outputs os.environ\["OPENAI\_API\_KEY"\] = "OPENAI\_API\_KEY" index = SummaryIndex.from\_documents(documents) query\_engine = index.as\_query\_engine() response = query\_engine.query("What is Psychic's privacy policy?") display(Markdown(f"**{response}**"))

INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
> \[build\_index\_from\_nodes\] Total LLM token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[build\_index\_from\_nodes\] Total embedding token usage: 0 tokens
> \[build\_index\_from\_nodes\] Total embedding token usage: 0 tokens
> \[build\_index\_from\_nodes\] Total embedding token usage: 0 tokens
> \[build\_index\_from\_nodes\] Total embedding token usage: 0 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total LLM token usage: 2383 tokens
> \[get\_response\] Total LLM token usage: 2383 tokens
> \[get\_response\] Total LLM token usage: 2383 tokens
> \[get\_response\] Total LLM token usage: 2383 tokens
INFO:llama\_index.token\_counter.token\_counter:> \[get\_response\] Total embedding token usage: 0 tokens
> \[get\_response\] Total embedding token usage: 0 tokens
> \[get\_response\] Total embedding token usage: 0 tokens
> \[get\_response\] Total embedding token usage: 0 tokens

**Psychic's privacy policy explains how we access, use, store, and share Google user data when you connect your Google Drive or other Google services to our application. By using Psychic, you agree to this Privacy Policy and our Terms of Service. We use the information we collect for the following purposes: to provide you with the Psychic services, including allowing you to access, view, and query files and folders stored in your connected Google Drive; to improve our services, including analyzing usage patterns and troubleshooting issues; and to communicate with you about important updates, promotions, or news related to Psychic. We take the security of your information seriously and implement appropriate security measures to protect it. We may share your information in certain cases, such as with service providers who assist us in providing and maintaining Psychic services, as required by law, or to protect the rights, property, or safety of Psychic, our users, or the public. Psychic provides in-product privacy notifications to inform you about the ways we access, use, store, and share your Google user data. We may update this Privacy Policy from time to time, and your continued use of Psychic after any changes to this Privacy Policy constitutes your acceptance of the updated policy.**

Back to top

[Previous Pinecone Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/PineconeDemo/)[Next Qdrant Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/QdrantDemo/)
