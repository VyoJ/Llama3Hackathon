Title: Contributing a LlamaDataset To LlamaHub

URL Source: https://docs.llamaindex.ai/en/stable/examples/llama_dataset/uploading_llama_dataset/

Markdown Content:
Contributing a LlamaDataset To LlamaHub - LlamaIndex


`LlamaDataset`'s storage is managed through a git repository. To contribute a dataset requires making a pull request to `llama_index/llama_datasets` Github (LFS) repository.

To contribute a `LabelledRagDataset` (a subclass of `BaseLlamaDataset`), two sets of files are required:

1.  The `LabelledRagDataset` saved as json named `rag_dataset.json`
2.  Source document files used to create the `LabelledRagDataset`

This brief notebook provides a quick example using the Paul Graham Essay text file.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai

%pip install llama-index-llms-openai

In \[ \]:

Copied!

import nest\_asyncio

nest\_asyncio.apply()

import nest\_asyncio nest\_asyncio.apply()

### Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/llama_dataset/uploading_llama_dataset/#load-data)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

\# Load documents and build index
documents \= SimpleDirectoryReader(
    input\_files\=\["data/paul\_graham/paul\_graham\_essay.txt"\]
).load\_data()

from llama\_index.core import SimpleDirectoryReader # Load documents and build index documents = SimpleDirectoryReader( input\_files=\["data/paul\_graham/paul\_graham\_essay.txt"\] ).load\_data()

In \[ \]:

Copied!

\# generate questions against chunks
from llama\_index.core.llama\_dataset.generator import RagDatasetGenerator
from llama\_index.llms.openai import OpenAI

\# set context for llm provider
llm\_gpt35 \= OpenAI(model\="gpt-4", temperature\=0.3)

\# instantiate a DatasetGenerator
dataset\_generator \= RagDatasetGenerator.from\_documents(
    documents,
    llm\=llm\_gpt35,
    num\_questions\_per\_chunk\=2,  \# set the number of questions per nodes
    show\_progress\=True,
)

rag\_dataset \= dataset\_generator.generate\_dataset\_from\_nodes()

\# generate questions against chunks from llama\_index.core.llama\_dataset.generator import RagDatasetGenerator from llama\_index.llms.openai import OpenAI # set context for llm provider llm\_gpt35 = OpenAI(model="gpt-4", temperature=0.3) # instantiate a DatasetGenerator dataset\_generator = RagDatasetGenerator.from\_documents( documents, llm=llm\_gpt35, num\_questions\_per\_chunk=2, # set the number of questions per nodes show\_progress=True, ) rag\_dataset = dataset\_generator.generate\_dataset\_from\_nodes()

Now that we have our `LabelledRagDataset` generated (btw, it's totally fine to manually create one with human generated queries and reference answers!), we store this into the necessary json file.

In \[ \]:

Copied!

rag\_dataset.save\_json("rag\_dataset.json")

rag\_dataset.save\_json("rag\_dataset.json")

#### Generating Baseline Results[¶](https://docs.llamaindex.ai/en/stable/examples/llama_dataset/uploading_llama_dataset/#generating-baseline-results)

In addition to adding just a `LlamaDataset`, we also encourage adding baseline benchmarks for others to use as sort of measuring stick against their own RAG pipelines.

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex

\# a basic RAG pipeline, uses defaults
index \= VectorStoreIndex.from\_documents(documents\=documents)
query\_engine \= index.as\_query\_engine()

\# manually
prediction\_dataset \= await rag\_dataset.amake\_predictions\_with(
    query\_engine\=query\_engine, show\_progress\=True
)

from llama\_index.core import VectorStoreIndex # a basic RAG pipeline, uses defaults index = VectorStoreIndex.from\_documents(documents=documents) query\_engine = index.as\_query\_engine() # manually prediction\_dataset = await rag\_dataset.amake\_predictions\_with( query\_engine=query\_engine, show\_progress=True )

Submitting The Pull-Requests[¶](https://docs.llamaindex.ai/en/stable/examples/llama_dataset/uploading_llama_dataset/#submitting-the-pull-requests)
--------------------------------------------------------------------------------------------------------------------------------------------------

With the `rag_dataset.json` and source file `paul_graham_essay.txt` (note in this case, there is only one source document, but there can be several), we can perform the two steps for contributing a `LlamaDataset` into `LlamaHub`:

1.  Similar, to how contributions are made for `loader`'s, `agent`'s and `pack`'s, create a pull-request for `llama_hub` repository that adds a new folder for new `LlamaDataset`. This step uploads the information about the new `LlamaDataset` so that it can be presented in the `LlamaHub` UI.
    
2.  Create a pull request into `llama_datasets` repository to actually upload the data files.
    

### Step 0 (Pre-requisites)[¶](https://docs.llamaindex.ai/en/stable/examples/llama_dataset/uploading_llama_dataset/#step-0-pre-requisites)

Fork and then clone (onto your local machine) both, the `llama_hub` Github repository as well as the `llama_datasets` one. You'll be submitting a pull requests into both of these repos from a new branch off of your forked versions.

### Step 1[¶](https://docs.llamaindex.ai/en/stable/examples/llama_dataset/uploading_llama_dataset/#step-1)

Create a new folder in `llama_datasets/` of the `llama_hub` Github repository. For example, in this case we would create a new folder `llama_datasets/paul_graham_essay`.

In that folder, two files are required:

*   `card.json`
*   `README.md`

In particular, on your local machine:

```
cd llama_datasets/
mkdir paul_graham_essay
touch card.json
touch README.md
```

The suggestion here is to look at previously submitted `LlamaDataset`'s and modify their respective files as needed for your new dataset.

In our current example, we need the `card.json` to look as follows

{
    "name": "Paul Graham Essay",
    "description": "A labelled RAG dataset based off an essay by Paul Graham, consisting of queries, reference answers, and reference contexts.",
    "numberObservations": 44,
    "containsExamplesByHumans": false,
    "containsExamplesByAI": true,
    "sourceUrls": \[
        "http://www.paulgraham.com/articles.html"
    \],
    "baselines": \[
        {
            "name": "llamaindex",
            "config": {
                "chunkSize": 1024,
                "llm": "gpt-3.5-turbo",
                "similarityTopK": 2,
                "embedModel": "text-embedding-ada-002"
            },
            "metrics": {
                "contextSimilarity": 0.934,
                "correctness": 4.239,
                "faithfulness": 0.977,
                "relevancy": 0.977
            },
            "codeUrl": "https://github.com/run-llama/llama\_datasets/blob/main/baselines/paul\_graham\_essay/llamaindex\_baseline.py"
        }
    \]
}

And for the `README.md`, these are pretty standard, requiring you to change the name of the dataset argument in the `download_llama_dataset()` function call.

from llama\_index.llama\_datasets import download\_llama\_datasets
from llama\_index.llama\_pack import download\_llama\_pack
from llama\_index import VectorStoreIndex

\# download and install dependencies for rag evaluator pack
RagEvaluatorPack \= download\_llama\_pack(
  "RagEvaluatorPack", "./rag\_evaluator\_pack"
)
rag\_evaluator\_pack \= RagEvaluatorPack()

\# download and install dependencies for benchmark dataset
rag\_dataset, documents \= download\_llama\_datasets(
  "PaulGrahamEssayTruncatedDataset", "./data"
)

\# evaluate
query\_engine \= VectorStoreIndex.as\_query\_engine()  \# previously defined, not shown here
rag\_evaluate\_pack.run(dataset\=paul\_graham\_qa\_data, query\_engine\=query\_engine)

Finally, the last item for Step 1 is to create an entry to `llama_datasets/library.json` file. In this case:

...,
    "PaulGrahamEssayDataset": {
    "id": "llama\_datasets/paul\_graham\_essay",
    "author": "andrei-fajardo",
    "keywords": \["rag"\],
    "extra\_files": \["paul\_graham\_essay.txt"\]
  }

Note: the `extra_files` field is reserved for the source files.

### Step 2 Uploading The Actual Datasets[¶](https://docs.llamaindex.ai/en/stable/examples/llama_dataset/uploading_llama_dataset/#step-2-uploading-the-actual-datasets)

In this step, since we use Github LFS on our `llama_datasets` repo, making a contribution is exactly the same way you would make a contribution with any of our other open Github repos. That is, submit a pull request.

Make a fork of the `llama_datasets` repo, and create a new folder in the `llama_datasets/` directory that matches the `id` field of the entry made in the `library.json` file. So, for this example, we'll create a new folder `llama_datasets/paul_graham_essay/`. It is here where we will add the documents and make the pull request.

To this folder, add `rag_dataset.json` (it must be called this), as well as the rest of the source documents, which in our case is the `paul_graham_essay.txt` file.

llama\_datasets/paul\_graham\_essay/
├── paul\_graham\_essay.txt
└── rag\_dataset.json

Now, simply `git add`, `git commit` and `git push` your branch, and make your PR.

Back to top

[Previous LlamaDataset Submission Template Notebook](https://docs.llamaindex.ai/en/stable/examples/llama_dataset/ragdataset_submission_template/)[Next LlamaHub Demostration](https://docs.llamaindex.ai/en/stable/examples/llama_hub/llama_hub/)

Hi, how can I help you?

🦙
