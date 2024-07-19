Title: Advanced RAG with temporal filters using LlamaIndex and KDB.AI vector store

URL Source: https://docs.llamaindex.ai/en/stable/examples/vector_stores/KDBAI_Advanced_RAG_Demo/

Markdown Content:
Advanced RAG with temporal filters using LlamaIndex and KDB.AI vector store - LlamaIndex


> [KDB.AI](https://kdb.ai/) is a powerful knowledge-based vector database and search engine that allows you to build scalable, reliable AI applications, using real-time data, by providing advanced search, recommendation and personalization.

This example demonstrates how to use KDB.AI to run semantic search, summarization and analysis of financial regulations around some specific moment in time.

To access your end point and API keys, sign up to KDB.AI here.

To set up your development environment, follow the instructions on the KDB.AI pre-requisites page.

The following examples demonstrate some of the ways you can interact with KDB.AI through LlamaIndex.

Install dependencies with Pip[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/KDBAI_Advanced_RAG_Demo/#install-dependencies-with-pip)
----------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

\# %pip install llama-index llama-index-embeddings-huggingface llama-index-llms-openai llama-index-readers-file llama-index-vector-stores-kdbai
\# %pip install kdbai\_client pandas

\# %pip install llama-index llama-index-embeddings-huggingface llama-index-llms-openai llama-index-readers-file llama-index-vector-stores-kdbai # %pip install kdbai\_client pandas

Import dependencies[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/KDBAI_Advanced_RAG_Demo/#import-dependencies)
--------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from getpass import getpass
import re
import os
import shutil
import time
import urllib

import pandas as pd

from llama\_index.core import (
    Settings,
    SimpleDirectoryReader,
    ServiceContext,
    StorageContext,
    VectorStoreIndex,
)
from llama\_index.core import Settings
from llama\_index.core.node\_parser import SentenceSplitter
from llama\_index.core.retrievers import VectorIndexRetriever
from llama\_index.embeddings.huggingface import HuggingFaceEmbedding
from llama\_index.llms.openai import OpenAI
from llama\_index.vector\_stores.kdbai import KDBAIVectorStore

import pykx as kx
import kdbai\_client as kdbai

OUTDIR \= "pdf"
RESET \= True

\# LLM = 'gpt-3.5-turbo'
LLM \= "gpt-4-turbo-preview"  \# Expensive !!!
EMBEDDING \= "sentence-transformers/all-mpnet-base-v2"

os.environ\["OPENAI\_API\_KEY"\] \= getpass("OpenAI API key: ")

from getpass import getpass import re import os import shutil import time import urllib import pandas as pd from llama\_index.core import ( Settings, SimpleDirectoryReader, ServiceContext, StorageContext, VectorStoreIndex, ) from llama\_index.core import Settings from llama\_index.core.node\_parser import SentenceSplitter from llama\_index.core.retrievers import VectorIndexRetriever from llama\_index.embeddings.huggingface import HuggingFaceEmbedding from llama\_index.llms.openai import OpenAI from llama\_index.vector\_stores.kdbai import KDBAIVectorStore import pykx as kx import kdbai\_client as kdbai OUTDIR = "pdf" RESET = True # LLM = 'gpt-3.5-turbo' LLM = "gpt-4-turbo-preview" # Expensive !!! EMBEDDING = "sentence-transformers/all-mpnet-base-v2" os.environ\["OPENAI\_API\_KEY"\] = getpass("OpenAI API key: ")

Create KDB.AI session and table[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/KDBAI_Advanced_RAG_Demo/#create-kdbai-session-and-table)
-------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

KDBAI\_ENDPOINT \= "http://localhost:8082"
KDBAI\_API\_KEY \= None
KDBAI\_TABLE\_NAME \= "reports"

session \= kdbai.Session(endpoint\=KDBAI\_ENDPOINT, api\_key\=KDBAI\_API\_KEY)

if KDBAI\_TABLE\_NAME in session.list():
    session.table(KDBAI\_TABLE\_NAME).drop()

schema \= dict(
    columns\=\[
        dict(name\="document\_id", pytype\="bytes"),
        dict(name\="text", pytype\="bytes"),
        dict(
            name\="embedding",
            vectorIndex\=dict(type\="flat", metric\="L2", dims\=768),
        ),
        dict(name\="title", pytype\="bytes"),
        dict(name\="publication\_date", pytype\="datetime64\[ns\]"),
    \]
)

table \= session.create\_table(KDBAI\_TABLE\_NAME, schema)

KDBAI\_ENDPOINT = "http://localhost:8082" KDBAI\_API\_KEY = None KDBAI\_TABLE\_NAME = "reports" session = kdbai.Session(endpoint=KDBAI\_ENDPOINT, api\_key=KDBAI\_API\_KEY) if KDBAI\_TABLE\_NAME in session.list(): session.table(KDBAI\_TABLE\_NAME).drop() schema = dict( columns=\[ dict(name="document\_id", pytype="bytes"), dict(name="text", pytype="bytes"), dict( name="embedding", vectorIndex=dict(type="flat", metric="L2", dims=768), ), dict(name="title", pytype="bytes"), dict(name="publication\_date", pytype="datetime64\[ns\]"), \] ) table = session.create\_table(KDBAI\_TABLE\_NAME, schema)

Financial reports urls and metadata[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/KDBAI_Advanced_RAG_Demo/#financial-reports-urls-and-metadata)
----------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

INPUT\_URLS \= \[
    "https://www.govinfo.gov/content/pkg/PLAW-106publ102/pdf/PLAW-106publ102.pdf",
    "https://www.govinfo.gov/content/pkg/PLAW-111publ203/pdf/PLAW-111publ203.pdf",
\]

METADATA \= {
    "pdf/PLAW-106publ102.pdf": {
        "title": "GRAMM–LEACH–BLILEY ACT, 1999",
        "publication\_date": pd.to\_datetime("1999-11-12"),
    },
    "pdf/PLAW-111publ203.pdf": {
        "title": "DODD-FRANK WALL STREET REFORM AND CONSUMER PROTECTION ACT, 2010",
        "publication\_date": pd.to\_datetime("2010-07-21"),
    },
}

INPUT\_URLS = \[ "https://www.govinfo.gov/content/pkg/PLAW-106publ102/pdf/PLAW-106publ102.pdf", "https://www.govinfo.gov/content/pkg/PLAW-111publ203/pdf/PLAW-111publ203.pdf", \] METADATA = { "pdf/PLAW-106publ102.pdf": { "title": "GRAMM–LEACH–BLILEY ACT, 1999", "publication\_date": pd.to\_datetime("1999-11-12"), }, "pdf/PLAW-111publ203.pdf": { "title": "DODD-FRANK WALL STREET REFORM AND CONSUMER PROTECTION ACT, 2010", "publication\_date": pd.to\_datetime("2010-07-21"), }, }

Download PDF files locally[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/KDBAI_Advanced_RAG_Demo/#download-pdf-files-locally)
----------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

%%time

CHUNK\_SIZE \= 512 \* 1024

def download\_file(url):
    print("Downloading %s..." % url)
    out \= os.path.join(OUTDIR, os.path.basename(url))
    try:
        response \= urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        logging.exception("Failed to download %s !" % url)
    else:
        with open(out, "wb") as f:
            while True:
                chunk \= response.read(CHUNK\_SIZE)
                if chunk:
                    f.write(chunk)
                else:
                    break
    return out

if RESET:
    if os.path.exists(OUTDIR):
        shutil.rmtree(OUTDIR)
    os.mkdir(OUTDIR)

    local\_files \= \[download\_file(x) for x in INPUT\_URLS\]
    local\_files\[:10\]

%%time CHUNK\_SIZE = 512 \* 1024 def download\_file(url): print("Downloading %s..." % url) out = os.path.join(OUTDIR, os.path.basename(url)) try: response = urllib.request.urlopen(url) except urllib.error.URLError as e: logging.exception("Failed to download %s !" % url) else: with open(out, "wb") as f: while True: chunk = response.read(CHUNK\_SIZE) if chunk: f.write(chunk) else: break return out if RESET: if os.path.exists(OUTDIR): shutil.rmtree(OUTDIR) os.mkdir(OUTDIR) local\_files = \[download\_file(x) for x in INPUT\_URLS\] local\_files\[:10\]

Downloading https://www.govinfo.gov/content/pkg/PLAW-106publ102/pdf/PLAW-106publ102.pdf...
Downloading https://www.govinfo.gov/content/pkg/PLAW-111publ203/pdf/PLAW-111publ203.pdf...
CPU times: user 64.6 ms, sys: 4.44 ms, total: 69 ms
Wall time: 4.98 s

Load local PDF files with LlamaIndex[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/KDBAI_Advanced_RAG_Demo/#load-local-pdf-files-with-llamaindex)
------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

%%time

def get\_metadata(filepath):
    return METADATA\[filepath\]

documents \= SimpleDirectoryReader(
    input\_files\=local\_files,
    file\_metadata\=get\_metadata,
)

docs \= documents.load\_data()
len(docs)

%%time def get\_metadata(filepath): return METADATA\[filepath\] documents = SimpleDirectoryReader( input\_files=local\_files, file\_metadata=get\_metadata, ) docs = documents.load\_data() len(docs)

CPU times: user 11.1 s, sys: 56 ms, total: 11.1 s
Wall time: 11.2 s

Out\[ \]:

994

Setup LlamaIndex RAG pipeline using KDB.AI vector store[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/KDBAI_Advanced_RAG_Demo/#setup-llamaindex-rag-pipeline-using-kdbai-vector-store)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

%%time

embed\_model \= HuggingFaceEmbedding(model\_name\=EMBEDDING)
llm \= OpenAI(temperature\=0, model\=LLM)
vector\_store \= KDBAIVectorStore(table)
Settings.embed\_model \= embed\_model
Settings.llm \= llm
storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
index \= VectorStoreIndex.from\_documents(
    docs,
    storage\_context\=storage\_context,
    transformations\=\[SentenceSplitter(chunk\_size\=2048, chunk\_overlap\=0)\],
)

%%time embed\_model = HuggingFaceEmbedding(model\_name=EMBEDDING) llm = OpenAI(temperature=0, model=LLM) vector\_store = KDBAIVectorStore(table) Settings.embed\_model = embed\_model Settings.llm = llm storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) index = VectorStoreIndex.from\_documents( docs, storage\_context=storage\_context, transformations=\[SentenceSplitter(chunk\_size=2048, chunk\_overlap=0)\], )

CPU times: user 3min 32s, sys: 3.72 s, total: 3min 35s
Wall time: 4min 41s

Setup the LlamaIndex Query Engine[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/KDBAI_Advanced_RAG_Demo/#setup-the-llamaindex-query-engine)
------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

%%time

\# Using gpt-3.5-turbo, the 16k tokens context size can only fit around 15 pages of document.
\# Using gpt-4-turbo-preview, the 128k tokens context size can take 100 pages.
K \= 100

query\_engine \= index.as\_query\_engine(
    similarity\_top\_k\=K,
    filter\=\[("<", "publication\_date", "2008-09-15")\],
    sort\_by\="publication\_date",
)

%%time # Using gpt-3.5-turbo, the 16k tokens context size can only fit around 15 pages of document. # Using gpt-4-turbo-preview, the 128k tokens context size can take 100 pages. K = 100 query\_engine = index.as\_query\_engine( similarity\_top\_k=K, filter=\[("<", "publication\_date", "2008-09-15")\], sort\_by="publication\_date", )

CPU times: user 60.2 ms, sys: 766 µs, total: 61 ms
Wall time: 79.1 ms

Before the 2008 crisis[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/KDBAI_Advanced_RAG_Demo/#before-the-2008-crisis)
--------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

%%time

result \= query\_engine.query(
    """
What was the main financial regulation in the US before the 2008 financial crisis ?
"""
)
print(result.response)

%%time result = query\_engine.query( """ What was the main financial regulation in the US before the 2008 financial crisis ? """ ) print(result.response)

The main financial regulation in the US before the 2008 financial crisis was the Gramm-Leach-Bliley Act.
CPU times: user 2.28 s, sys: 666 µs, total: 2.28 s
Wall time: 56.9 s

In \[ \]:

Copied!

%%time

result \= query\_engine.query(
    """
Is the Gramm-Leach-Bliley Act of 1999 enough to prevent the 2008 crisis. Search the document and explain its strenghts and weaknesses to regulate the US stock market.
"""
)
print(result.response)

%%time result = query\_engine.query( """ Is the Gramm-Leach-Bliley Act of 1999 enough to prevent the 2008 crisis. Search the document and explain its strenghts and weaknesses to regulate the US stock market. """ ) print(result.response)

The Gramm-Leach-Bliley Act of 1999, also known as the Financial Services Modernization Act, aimed to modernize financial services by removing barriers between banking, securities, and insurance companies, allowing them to offer each other's services. While the Act contributed to financial services integration and competition, its effectiveness in preventing crises like that of 2008 is debatable due to its strengths and weaknesses in regulating the US stock market.

Strengths:
1. Enhanced Competition: By allowing financial institutions to merge and offer a broader range of services, the Act fostered competition, innovation, and efficiency in the financial sector.
2. Functional Regulation: The Act maintained that activities within financial institutions would be regulated by the appropriate functional regulator (e.g., securities activities by the SEC), aiming for expertise-based oversight.

Weaknesses:
1. Increased Systemic Risk: The Act's facilitation of larger, more complex financial institutions may have contributed to systemic risk, as failures of these institutions could have more significant impacts on the financial system.
2. Regulatory Gaps and Oversight Challenges: The integration of different financial services under one roof made it challenging for regulators to oversee and manage the risks of these conglomerates effectively. The Act did not fully address the need for a systemic risk regulator or enhance oversight of the shadow banking system, which played a significant role in the 2008 crisis.
3. Weakened Consumer Privacy Protections: While the Act included provisions for protecting consumers' personal financial information, critics argue that it also allowed for increased sharing of this information among financial entities, potentially undermining consumer privacy.

In summary, while the Gramm-Leach-Bliley Act of 1999 had the potential to foster innovation and efficiency in the financial sector by breaking down barriers between different types of financial services, its weaknesses in addressing systemic risk and regulatory oversight challenges may have limited its effectiveness in preventing financial crises like that of 2008.
CPU times: user 177 ms, sys: 45.6 ms, total: 223 ms
Wall time: 31.6 s

After the 2008 crisis[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/KDBAI_Advanced_RAG_Demo/#after-the-2008-crisis)
------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

%%time

\# Using gpt-3.5-turbo, the 16k tokens context size can only fit around 15 pages of document.
\# Using gpt-4-turbo-preview, the 128k tokens context size can take 100 pages.
K \= 100

query\_engine \= index.as\_query\_engine(
    similarity\_top\_k\=K,
    filter\=\[(">=", "publication\_date", "2008-09-15")\],
    sort\_by\="publication\_date",
)

%%time # Using gpt-3.5-turbo, the 16k tokens context size can only fit around 15 pages of document. # Using gpt-4-turbo-preview, the 128k tokens context size can take 100 pages. K = 100 query\_engine = index.as\_query\_engine( similarity\_top\_k=K, filter=\[(">=", "publication\_date", "2008-09-15")\], sort\_by="publication\_date", )

CPU times: user 217 µs, sys: 99 µs, total: 316 µs
Wall time: 320 µs

In \[ \]:

Copied!

%%time

result \= query\_engine.query(
    """
What happened on the 15th of September 2008 ? Answer from your own knowledge only.
"""
)
print(result.response)

%%time result = query\_engine.query( """ What happened on the 15th of September 2008 ? Answer from your own knowledge only. """ ) print(result.response)

I'm unable to provide an answer based on the given instructions.
CPU times: user 151 ms, sys: 22 ms, total: 173 ms
Wall time: 12.7 s

In \[ \]:

Copied!

%%time

result \= query\_engine.query(
    """
What was the new US financial regulation enacted after the 2008 crisis to increase the market regulation and to improve consumer sentiment ?
"""
)
print(result.response)

%%time result = query\_engine.query( """ What was the new US financial regulation enacted after the 2008 crisis to increase the market regulation and to improve consumer sentiment ? """ ) print(result.response)

The Dodd-Frank Wall Street Reform and Consumer Protection Act, 2010.
CPU times: user 184 ms, sys: 23.1 ms, total: 207 ms
Wall time: 17.1 s

In depth analysis[¶](https://docs.llamaindex.ai/en/stable/examples/vector_stores/KDBAI_Advanced_RAG_Demo/#in-depth-analysis)
----------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

%%time

\# Using gpt-3.5-turbo, the 16k tokens context size can only fit around 15 pages of document.
\# Using gpt-4-turbo-preview, the 128k tokens context size can take 100 pages.
K \= 100

query\_engine \= index.as\_query\_engine(
    similarity\_top\_k\=K, sort\_by\="publication\_date"
)

%%time # Using gpt-3.5-turbo, the 16k tokens context size can only fit around 15 pages of document. # Using gpt-4-turbo-preview, the 128k tokens context size can take 100 pages. K = 100 query\_engine = index.as\_query\_engine( similarity\_top\_k=K, sort\_by="publication\_date" )

CPU times: user 381 µs, sys: 2 µs, total: 383 µs
Wall time: 399 µs

In \[ \]:

Copied!

%%time

result \= query\_engine.query(
    """
Analyse the US financial regulations before and after the 2008 crisis and produce a report of all related arguments to explain what happened, and to ensure that does not happen again.
Use both the provided context and your own knowledge but do mention explicitely which one you use.
"""
)
print(result.response)

%%time result = query\_engine.query( """ Analyse the US financial regulations before and after the 2008 crisis and produce a report of all related arguments to explain what happened, and to ensure that does not happen again. Use both the provided context and your own knowledge but do mention explicitely which one you use. """ ) print(result.response)

Before the 2008 financial crisis, the US financial system was characterized by deregulation and an increase in complex financial products such as mortgage-backed securities and derivatives. The Gramm-Leach-Bliley Act of 1999 repealed the Glass-Steagall Act, allowing banks to engage in investment activities, which led to increased risk-taking. The lack of transparency and understanding of these complex financial products, coupled with inadequate oversight, contributed to the financial crisis.

After the 2008 crisis, the Dodd-Frank Wall Street Reform and Consumer Protection Act was enacted in 2010 to address the regulatory gaps and weaknesses revealed by the crisis. The Act aimed to increase transparency, protect consumers, and prevent the occurrence of a similar crisis. Key provisions included the creation of the Financial Stability Oversight Council to monitor systemic risk, the establishment of the Consumer Financial Protection Bureau to protect consumers from abusive financial practices, and the introduction of the Volcker Rule to limit speculative investments by banks. Additionally, the Act imposed stricter capital requirements and introduced mechanisms for the orderly liquidation of failing financial institutions to prevent bailouts.

To ensure that a similar crisis does not happen again, it is crucial to maintain vigilant regulatory oversight, promote transparency in financial markets, and ensure that financial institutions have robust risk management practices in place. Continuous monitoring of systemic risks and the ability to adapt regulations in response to evolving financial products and practices are also essential.

This analysis is based on the context provided and my own knowledge of the US financial regulations before and after the 2008 crisis.
CPU times: user 1.11 s, sys: 1.99 s, total: 3.1 s
Wall time: 29.8 s

Back to top

[Previous Jaguar Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/JaguarIndexDemo/)[Next LanceDB Vector Store](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanceDBIndexDemo/)
