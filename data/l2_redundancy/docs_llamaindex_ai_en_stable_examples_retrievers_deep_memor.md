Title: Activeloop Deep Memory - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/

Markdown Content:
Activeloop Deep Memory - LlamaIndex


**How do we get +15% RAG hit\_rate improvement for question answering on documentation?**

Retrieval-Augmented Generators (RAGs) have recently gained significant attention. As advanced RAG techniques and agents emerge, they expand the potential of what RAGs can accomplish. However, several challenges may limit the integration of RAGs into production. The primary factors to consider when implementing RAGs in production settings are accuracy (recall), cost, and latency. For basic use cases, OpenAI's Ada model paired with a naive similarity search can produce satisfactory results. Yet, for higher accuracy or recall during searches, one might need to employ advanced retrieval techniques. These methods might involve varying data chunk sizes, rewriting queries multiple times, and more, potentially increasing latency and costs. [Activeloop's](https://activeloop.ai/) [Deep Memory](https://www.activeloop.ai/resources/use-deep-memory-to-boost-rag-apps-accuracy-by-up-to-22/) a feature available to Activeloop Deep Lake users, addresses these issuea by introducing a tiny neural network layer trained to match user queries with relevant data from a corpus. While this addition incurs minimal latency during search, it can boost retrieval accuracy by up to 27 % and remains cost-effective and simple to use, without requiring any additional advanced rag techniques.

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-deeplake
%pip install llama\-index\-llms\-openai

%pip install llama-index-vector-stores-deeplake %pip install llama-index-llms-openai

In \[ \]:

Copied!

import nest\_asyncio
import os
import getpass

nest\_asyncio.apply()

import nest\_asyncio import os import getpass nest\_asyncio.apply()

In \[ \]:

Copied!

!pip install deeplake beautifulsoup4 html2text tiktoken openai llama\-index python\-dotenv

!pip install deeplake beautifulsoup4 html2text tiktoken openai llama-index python-dotenv

For this tutorial we will parse deeplake documentation, and create a RAG system that could answer the question from the docs.

The tutorial can be divided into several parts:

1.  [Dataset creation and uploading](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/#1-dataset-creation-and-ingestion)
2.  [Generating synthetic queries and training deep\_memory](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/#2-training-deep-memory)
3.  [Evaluating deep memory performance](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/#3-deepmemory-evaluation)
4.  [Deep Memory inference](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/#4-deep-memory-inference)

1\. Dataset Creation and ingestion[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/#1-dataset-creation-and-ingestion)
---------------------------------------------------------------------------------------------------------------------------------------------

Let me parse all of the links using BeautifulSoup and convert them into LlamaIndex documents:

In \[ \]:

Copied!

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get\_all\_links(url):
    response \= requests.get(url)
    if response.status\_code != 200:
        print(f"Failed to retrieve the page: {url}")
        return \[\]

    soup \= BeautifulSoup(response.content, "html.parser")

    \# Finding all 'a' tags which typically contain href attribute for links
    links \= \[
        urljoin(url, a\["href"\])
        for a in soup.find\_all("a", href\=True)
        if a\["href"\]
    \]

    return links

import requests from bs4 import BeautifulSoup from urllib.parse import urljoin def get\_all\_links(url): response = requests.get(url) if response.status\_code != 200: print(f"Failed to retrieve the page: {url}") return \[\] soup = BeautifulSoup(response.content, "html.parser") # Finding all 'a' tags which typically contain href attribute for links links = \[ urljoin(url, a\["href"\]) for a in soup.find\_all("a", href=True) if a\["href"\] \] return links

In \[ \]:

Copied!

from langchain.document\_loaders import AsyncHtmlLoader
from langchain.document\_transformers import Html2TextTransformer
from llama\_index.core import Document

def load\_documents(url):
    all\_links \= get\_all\_links(url)
    loader \= AsyncHtmlLoader(all\_links)
    docs \= loader.load()

    html2text \= Html2TextTransformer()
    docs\_transformed \= html2text.transform\_documents(docs)
    docs \= \[Document.from\_langchain\_format(doc) for doc in docs\_transformed\]
    return docs

docs \= load\_documents("https://docs.deeplake.ai/en/latest/")

from langchain.document\_loaders import AsyncHtmlLoader from langchain.document\_transformers import Html2TextTransformer from llama\_index.core import Document def load\_documents(url): all\_links = get\_all\_links(url) loader = AsyncHtmlLoader(all\_links) docs = loader.load() html2text = Html2TextTransformer() docs\_transformed = html2text.transform\_documents(docs) docs = \[Document.from\_langchain\_format(doc) for doc in docs\_transformed\] return docs docs = load\_documents("https://docs.deeplake.ai/en/latest/")

Fetching pages: 100%|##########| 120/120 \[00:13<00:00,  8.70it/s\]

In \[ \]:

Copied!

len(docs)

len(docs)

Out\[ \]:

120

In \[ \]:

Copied!

from llama\_index.core.evaluation import generate\_question\_context\_pairs
from llama\_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
)
from llama\_index.vector\_stores.deeplake import DeepLakeVectorStore
from llama\_index.core.node\_parser import SimpleNodeParser
from llama\_index.llms.openai import OpenAI

os.environ\["OPENAI\_API\_KEY"\] \= getpass.getpass("Enter your OpenAI API token: ")
\# # activeloop token is needed if you are not signed in using CLI: \`activeloop login -u <USERNAME> -p <PASSWORD>\`
os.environ\["ACTIVELOOP\_TOKEN"\] \= getpass.getpass(
    "Enter your ActiveLoop API token: "
)  \# Get your API token from https://app.activeloop.ai, click on your profile picture in the top right corner, and select "API Tokens"

token \= os.getenv("ACTIVELOOP\_TOKEN")

vector\_store \= DeepLakeVectorStore(
    dataset\_path\="hub://activeloop-test/deeplake\_docs\_deepmemory2",
    overwrite\=False,  \# set to True to overwrite the existing dataset
    runtime\={"tensor\_db": True},
    token\=token,
)

from llama\_index.core.evaluation import generate\_question\_context\_pairs from llama\_index.core import ( VectorStoreIndex, SimpleDirectoryReader, StorageContext, ) from llama\_index.vector\_stores.deeplake import DeepLakeVectorStore from llama\_index.core.node\_parser import SimpleNodeParser from llama\_index.llms.openai import OpenAI os.environ\["OPENAI\_API\_KEY"\] = getpass.getpass("Enter your OpenAI API token: ") # # activeloop token is needed if you are not signed in using CLI: \`activeloop login -u \-p \` os.environ\["ACTIVELOOP\_TOKEN"\] = getpass.getpass( "Enter your ActiveLoop API token: " ) # Get your API token from https://app.activeloop.ai, click on your profile picture in the top right corner, and select "API Tokens" token = os.getenv("ACTIVELOOP\_TOKEN") vector\_store = DeepLakeVectorStore( dataset\_path="hub://activeloop-test/deeplake\_docs\_deepmemory2", overwrite=False, # set to True to overwrite the existing dataset runtime={"tensor\_db": True}, token=token, )

Deep Lake Dataset in hub://activeloop-test/deeplake\_docs\_deepmemory2 already exists, loading from the storage

In \[ \]:

Copied!

def create\_modules(vector\_store, docs\=\[\], populate\_vector\_store\=True):
    if populate\_vector\_store:
        node\_parser \= SimpleNodeParser.from\_defaults(chunk\_size\=512)
        nodes \= node\_parser.get\_nodes\_from\_documents(docs)
    else:
        nodes \= \[\]

    \# by default, the node ids are set to random uuids. To ensure same id's per run, we manually set them.
    for idx, node in enumerate(nodes):
        node.id\_ \= f"node\_{idx}"

    llm \= OpenAI(model\="gpt-4")
    storage\_context \= StorageContext.from\_defaults(vector\_store\=vector\_store)
    return storage\_context, nodes, llm

def create\_modules(vector\_store, docs=\[\], populate\_vector\_store=True): if populate\_vector\_store: node\_parser = SimpleNodeParser.from\_defaults(chunk\_size=512) nodes = node\_parser.get\_nodes\_from\_documents(docs) else: nodes = \[\] # by default, the node ids are set to random uuids. To ensure same id's per run, we manually set them. for idx, node in enumerate(nodes): node.id\_ = f"node\_{idx}" llm = OpenAI(model="gpt-4") storage\_context = StorageContext.from\_defaults(vector\_store=vector\_store) return storage\_context, nodes, llm

In \[ \]:

Copied!

(
    storage\_context,
    nodes,
    llm,
) \= create\_modules(
    docs\=docs,
    vector\_store\=vector\_store,
    \# populate\_vector\_store=False, # uncomment this line to skip populating the vector store
)

( storage\_context, nodes, llm, ) = create\_modules( docs=docs, vector\_store=vector\_store, # populate\_vector\_store=False, # uncomment this line to skip populating the vector store )

In \[ \]:

Copied!

vector\_index \= VectorStoreIndex(nodes, storage\_context\=storage\_context)
deep\_memory\_retriever \= vector\_index.as\_retriever(
    similarity\_top\_k\=4, deep\_memory\=True
)

vector\_index = VectorStoreIndex(nodes, storage\_context=storage\_context) deep\_memory\_retriever = vector\_index.as\_retriever( similarity\_top\_k=4, deep\_memory=True )

2\. Training Deep Memory[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/#2-training-deep-memory)
-------------------------------------------------------------------------------------------------------------------------

![Image 3: Image description](blob:https://docs.llamaindex.ai/384a98df00187f57b3e39c94f8fa1019)

Here above, we showed the overall schema of how deep\_memory works. So as you can see, in order to train it, you need relevance, queries together with corpus data (data that we want to query). The corpus data was already populated in the previous section; here, we will be generating questions and relevance.

1.  `questions` - is a text of strings, where each string represents a query.
2.  `relevance` - contains links to the ground truth for each question. There might be several docs that contain an answer to the given question. Because of this, relevance is List\[List\[tuple\[str, float\]\]\], where the outer list represents queries and the inner list relevant documents. The tuple contains a str, float pair where the string represents the id of the source doc (corresponds to the id tensor in the dataset), while the float corresponds to how much the current document is related to the question.

In \[ \]:

Copied!

from llama\_index.core.evaluation import (
    generate\_question\_context\_pairs,
    EmbeddingQAFinetuneDataset,
)
import random

def create\_train\_test\_datasets(
    number\_of\_samples\=600, llm\=None, nodes\=None, save\=False
):
    random\_indices \= random.sample(range(len(nodes)), number\_of\_samples)

    ratio \= int(len(random\_indices) \* 0.8)

    train\_indices \= random\_indices\[:ratio\]
    test\_indices \= random\_indices\[ratio:\]

    train\_nodes \= \[nodes\[i\] for i in train\_indices\]
    test\_nodes \= \[nodes\[i\] for i in test\_indices\]

    train\_qa\_dataset \= generate\_question\_context\_pairs(
        train\_nodes, llm\=llm, num\_questions\_per\_chunk\=1
    )

    test\_qa\_dataset \= generate\_question\_context\_pairs(
        test\_nodes, llm\=llm, num\_questions\_per\_chunk\=1
    )

    \# \[optional\] save
    if save:
        train\_qa\_dataset.save\_json(
            f"deeplake\_docs\_{number\_of\_samples}\_train.json"
        )
        test\_qa\_dataset.save\_json(
            f"deeplake\_docs\_{number\_of\_samples}\_test.json"
        )
    return train\_qa\_dataset, test\_qa\_dataset

from llama\_index.core.evaluation import ( generate\_question\_context\_pairs, EmbeddingQAFinetuneDataset, ) import random def create\_train\_test\_datasets( number\_of\_samples=600, llm=None, nodes=None, save=False ): random\_indices = random.sample(range(len(nodes)), number\_of\_samples) ratio = int(len(random\_indices) \* 0.8) train\_indices = random\_indices\[:ratio\] test\_indices = random\_indices\[ratio:\] train\_nodes = \[nodes\[i\] for i in train\_indices\] test\_nodes = \[nodes\[i\] for i in test\_indices\] train\_qa\_dataset = generate\_question\_context\_pairs( train\_nodes, llm=llm, num\_questions\_per\_chunk=1 ) test\_qa\_dataset = generate\_question\_context\_pairs( test\_nodes, llm=llm, num\_questions\_per\_chunk=1 ) # \[optional\] save if save: train\_qa\_dataset.save\_json( f"deeplake\_docs\_{number\_of\_samples}\_train.json" ) test\_qa\_dataset.save\_json( f"deeplake\_docs\_{number\_of\_samples}\_test.json" ) return train\_qa\_dataset, test\_qa\_dataset

In \[ \]:

Copied!

train\_qa\_dataset, test\_qa\_dataset \= create\_train\_test\_datasets(
    number\_of\_samples\=600, llm\=llm, nodes\=nodes, save\=True
)

train\_qa\_dataset, test\_qa\_dataset = create\_train\_test\_datasets( number\_of\_samples=600, llm=llm, nodes=nodes, save=True )

  4%|▍         | 19/480 \[02:25<1:04:00,  8.33s/it\]

In \[ \]:

Copied!

train\_qa\_dataset \= EmbeddingQAFinetuneDataset.from\_json(
    "deeplake\_docs\_600\_train.json"
)
test\_qa\_dataset \= EmbeddingQAFinetuneDataset.from\_json(
    "deeplake\_docs\_600\_test.json"
)

train\_qa\_dataset = EmbeddingQAFinetuneDataset.from\_json( "deeplake\_docs\_600\_train.json" ) test\_qa\_dataset = EmbeddingQAFinetuneDataset.from\_json( "deeplake\_docs\_600\_test.json" )

In \[ \]:

Copied!

def create\_query\_relevance(qa\_dataset):
    """Function for converting llama-index dataset to correct format for deep memory training"""
    queries \= \[text for \_, text in qa\_dataset.queries.items()\]
    relevant\_docs \= qa\_dataset.relevant\_docs
    relevance \= \[\]
    for doc in relevant\_docs:
        relevance.append(\[(relevant\_docs\[doc\]\[0\], 1)\])
    return queries, relevance

def create\_query\_relevance(qa\_dataset): """Function for converting llama-index dataset to correct format for deep memory training""" queries = \[text for \_, text in qa\_dataset.queries.items()\] relevant\_docs = qa\_dataset.relevant\_docs relevance = \[\] for doc in relevant\_docs: relevance.append(\[(relevant\_docs\[doc\]\[0\], 1)\]) return queries, relevance

In \[ \]:

Copied!

train\_queries, train\_relevance \= create\_query\_relevance(train\_qa\_dataset)
test\_queries, test\_relevance \= create\_query\_relevance(test\_qa\_dataset)

train\_queries, train\_relevance = create\_query\_relevance(train\_qa\_dataset) test\_queries, test\_relevance = create\_query\_relevance(test\_qa\_dataset)

In \[ \]:

Copied!

train\_queries\[:3\]

train\_queries\[:3\]

Out\[ \]:

\['In the context of creating a bounding box tensor in a dataset, explain the significance of the "coords" argument and its keys "type" and "mode". What does the "type" key specify about the bounding box coordinates?',
 'Explain the process of creating an intrinsics tensor and appending intrinsics matrices in the context of computer vision. What are the dimensions of the intrinsics parameters and what do they represent? Also, describe the concept of a Segmentation Mask Htype and its role in image processing.',
 'In the context of querying for images in the MNIST Train Dataset using \`ds.query\`, what does the command "select \* where labels == 0" signify and what is the expected output?'\]

In \[ \]:

Copied!

train\_relevance\[:3\]

train\_relevance\[:3\]

Out\[ \]:

\[\[('node\_788', 1)\], \[('node\_861', 1)\], \[('node\_82', 1)\]\]

In \[ \]:

Copied!

test\_queries\[:3\]

test\_queries\[:3\]

Out\[ \]:

\['What are the steps to update the information of keypoints and connections in a tensor, and what types of data can be appended to keypoints?',
 'What is the command to create a mesh tensor in DeepLake and what are the supported compressions? Also, explain how to append a ply file containing mesh data to this tensor.',
 'What is a Sequence htype in the context of tensors and how does it function as a wrapper for other htypes? Provide examples.'\]

In \[ \]:

Copied!

test\_relevance\[:3\]

test\_relevance\[:3\]

Out\[ \]:

\[\[('node\_933', 1)\], \[('node\_671', 1)\], \[('node\_471', 1)\]\]

In \[ \]:

Copied!

from langchain.embeddings.openai import OpenAIEmbeddings

embeddings \= OpenAIEmbeddings()

job\_id \= vector\_store.vectorstore.deep\_memory.train(
    queries\=train\_queries,
    relevance\=train\_relevance,
    embedding\_function\=embeddings.embed\_documents,
)

from langchain.embeddings.openai import OpenAIEmbeddings embeddings = OpenAIEmbeddings() job\_id = vector\_store.vectorstore.deep\_memory.train( queries=train\_queries, relevance=train\_relevance, embedding\_function=embeddings.embed\_documents, )

Starting DeepMemory training job
Your Deep Lake dataset has been successfully created!

Preparing training data for deepmemory:

Creating 483 embeddings in 1 batches of size 483:: 100%|██████████| 1/1 \[00:03<00:00,  3.67s/it\]

DeepMemory training job started. Job ID: 65421a5003888c9ca36c72e8

In \[ \]:

Copied!

vector\_store.vectorstore.deep\_memory.status(job\_id)

vector\_store.vectorstore.deep\_memory.status(job\_id)

This dataset can be visualized in Jupyter Notebook by ds.visualize() or at https://app.activeloop.ai/adilkhan/deeplake\_docs\_deepmemory2
--------------------------------------------------------------
|                  65421a5003888c9ca36c72e8                  |
--------------------------------------------------------------
| status                     | completed                     |
--------------------------------------------------------------
| progress                   | eta: 12.2 seconds             |
|                            | recall@10: 67.01% (+18.56%)   |
--------------------------------------------------------------
| results                    | recall@10: 67.01% (+18.56%)   |
--------------------------------------------------------------

3\. DeepMemory Evaluation[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/#3-deepmemory-evaluation)
---------------------------------------------------------------------------------------------------------------------------

Fantastic! The training has led to some remarkable improvements! Now, let's assess its performance on a test set.

In \[ \]:

Copied!

recalls \= vector\_store.vectorstore.deep\_memory.evaluate(
    queries\=test\_queries,
    relevance\=test\_relevance,
    embedding\_function\=embeddings.embed\_documents,
)

recalls = vector\_store.vectorstore.deep\_memory.evaluate( queries=test\_queries, relevance=test\_relevance, embedding\_function=embeddings.embed\_documents, )

info Wed Nov  1 09:32:44 2023 GMT         Added distance metric \`deepmemory\_distance\`.
Embedding queries took 0.95 seconds
---- Evaluating without Deep Memory ---- 
Recall@1:	  12.5%
Recall@3:	  23.3%
Recall@5:	  30.8%
Recall@10:	  50.8%
Recall@50:	  94.2%
Recall@100:	  95.8%
---- Evaluating with Deep Memory ---- 
Recall@1:	  11.7%
Recall@3:	  27.5%
Recall@5:	  40.8%
Recall@10:	  65.0%
Recall@50:	  96.7%
Recall@100:	  98.3%

Impressive! We've observed a 15% increase in recall on the test set. Next, let's employ the RetrieverEvaluator to examine the MRR (Mean Reciprocal Rank) and hit rates.

In \[ \]:

Copied!

import pandas as pd

def display\_results(eval\_results):
    """Display results from evaluate."""
    hit\_rates \= \[\]
    mrrs \= \[\]
    names \= \[\]
    for name, eval\_result in eval\_results.items():
        metric\_dicts \= \[\]
        for er in eval\_result:
            metric\_dict \= er.metric\_vals\_dict
            metric\_dicts.append(metric\_dict)

        full\_df \= pd.DataFrame(metric\_dicts)

        hit\_rate \= full\_df\["hit\_rate"\].mean()
        mrr \= full\_df\["mrr"\].mean()

        hit\_rates.append(hit\_rate)
        mrrs.append(mrr)
        names.append(name)

    metric\_df \= pd.DataFrame(
        \[
            {"retrievers": names\[i\], "hit\_rate": hit\_rates\[i\], "mrr": mrrs\[i\]}
            for i in range(2)
        \],
    )

    return metric\_df

import pandas as pd def display\_results(eval\_results): """Display results from evaluate.""" hit\_rates = \[\] mrrs = \[\] names = \[\] for name, eval\_result in eval\_results.items(): metric\_dicts = \[\] for er in eval\_result: metric\_dict = er.metric\_vals\_dict metric\_dicts.append(metric\_dict) full\_df = pd.DataFrame(metric\_dicts) hit\_rate = full\_df\["hit\_rate"\].mean() mrr = full\_df\["mrr"\].mean() hit\_rates.append(hit\_rate) mrrs.append(mrr) names.append(name) metric\_df = pd.DataFrame( \[ {"retrievers": names\[i\], "hit\_rate": hit\_rates\[i\], "mrr": mrrs\[i\]} for i in range(2) \], ) return metric\_df

Evaluating performance of retrieval with deep memory:

In \[ \]:

Copied!

from llama\_index.core.evaluation import RetrieverEvaluator

deep\_memory\_retriever \= vector\_index.as\_retriever(
    similarity\_top\_k\=10, vector\_store\_kwargs\={"deep\_memory": True}
)
dm\_retriever\_evaluator \= RetrieverEvaluator.from\_metric\_names(
    \["mrr", "hit\_rate"\], retriever\=deep\_memory\_retriever
)

dm\_eval\_results \= await dm\_retriever\_evaluator.aevaluate\_dataset(
    test\_qa\_dataset, retriever\=dm\_retriever\_evaluator
)

from llama\_index.core.evaluation import RetrieverEvaluator deep\_memory\_retriever = vector\_index.as\_retriever( similarity\_top\_k=10, vector\_store\_kwargs={"deep\_memory": True} ) dm\_retriever\_evaluator = RetrieverEvaluator.from\_metric\_names( \["mrr", "hit\_rate"\], retriever=deep\_memory\_retriever ) dm\_eval\_results = await dm\_retriever\_evaluator.aevaluate\_dataset( test\_qa\_dataset, retriever=dm\_retriever\_evaluator )

In \[ \]:

Copied!

from llama\_index.core.evaluation import RetrieverEvaluator

naive\_retriever \= vector\_index.as\_retriever(similarity\_top\_k\=10)
naive\_retriever\_evaluator \= RetrieverEvaluator.from\_metric\_names(
    \["mrr", "hit\_rate"\], retriever\=naive\_retriever
)

naive\_eval\_results \= await naive\_retriever\_evaluator.aevaluate\_dataset(
    test\_qa\_dataset, retriever\=naive\_retriever
)

from llama\_index.core.evaluation import RetrieverEvaluator naive\_retriever = vector\_index.as\_retriever(similarity\_top\_k=10) naive\_retriever\_evaluator = RetrieverEvaluator.from\_metric\_names( \["mrr", "hit\_rate"\], retriever=naive\_retriever ) naive\_eval\_results = await naive\_retriever\_evaluator.aevaluate\_dataset( test\_qa\_dataset, retriever=naive\_retriever )

In \[ \]:

Copied!

eval\_results \= {
    f"{mode} with Deep Memory top-10 eval": eval\_result
    for mode, eval\_result in zip(
        \["with", "without"\], \[dm\_eval\_results, naive\_eval\_results\]
    )
}

display\_results(eval\_results)

eval\_results = { f"{mode} with Deep Memory top-10 eval": eval\_result for mode, eval\_result in zip( \["with", "without"\], \[dm\_eval\_results, naive\_eval\_results\] ) } display\_results(eval\_results)

Out\[ \]:

|  | retrievers | hit\_rate | mrr |
| --- | --- | --- | --- |
| 0 | with with Deep Memory top-10 eval | 0.650000 | 0.244775 |
| 1 | without with Deep Memory top-10 eval | 0.508333 | 0.215129 |

Not only hit\_rate has increased but also MRR

4\. Deep Memory Inference[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/#4-deep-memory-inference)
---------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

query\_engine \= vector\_index.as\_query\_engine(
    vector\_store\_kwargs\={"deep\_memory": True}, llm\=llm
)
response \= query\_engine.query(
    "How can you connect your own storage to the deeplake?"
)
print(response)

query\_engine = vector\_index.as\_query\_engine( vector\_store\_kwargs={"deep\_memory": True}, llm=llm ) response = query\_engine.query( "How can you connect your own storage to the deeplake?" ) print(response)

info Wed Nov  1 11:37:33 2023 GMT         Can't find any metric in the dataset.
You can connect your own storage to deeplake by using the \`connect()\` function in the deeplake API.

In \[ \]:

Copied!

query\_engine \= vector\_index.as\_query\_engine(
    vector\_store\_kwargs\={"deep\_memory": False}, llm\=llm
)
response \= query\_engine.query(
    "How can you connect your own storage to the deeplake?"
)
print(response)

query\_engine = vector\_index.as\_query\_engine( vector\_store\_kwargs={"deep\_memory": False}, llm=llm ) response = query\_engine.query( "How can you connect your own storage to the deeplake?" ) print(response)

The context does not provide information on how to connect your own storage to Deep Lake.

From our observations, without "deep memory", our model tends to produce inaccuracies because it retrieves the wrong context.

Back to top

[Previous Composable Objects](https://docs.llamaindex.ai/en/stable/examples/retrievers/composable_retrievers/)[Next Ensemble Retrieval Guide](https://docs.llamaindex.ai/en/stable/examples/retrievers/ensemble_retrieval/)
