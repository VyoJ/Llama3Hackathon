Title: Cohere init8 and binary Embeddings Retrieval Evaluation

URL Source: https://docs.llamaindex.ai/en/stable/examples/cookbooks/cohere_retriever_eval/

Markdown Content:
Cohere init8 and binary Embeddings Retrieval Evaluation - LlamaIndex


Cohere Embed is the first embedding model that natively supports float, int8, binary and ubinary embeddings. Refer to their [main blog post](https://txt.cohere.com/int8-binary-embeddings/) for more details on Cohere int8 & binary Embeddings.

This notebook helps you to evaluate these different embedding types and pick one for your RAG pipeline. It uses our `RetrieverEvaluator` to evaluate the quality of the embeddings using the Retriever module LlamaIndex.

Observed Metrics:

1.  Hit-Rate
2.  MRR (Mean-Reciprocal-Rank)

For any given question, these will compare the quality of retrieved results from the ground-truth context. The eval dataset is created using our synthetic dataset generation module. We will use GPT-4 for dataset generation to avoid bias.

Note: The results shown at the end of the notebook are very specific to dataset, and various other parameters considered. We recommend you to use the notebook as reference to experiment on your dataset and evaluate the usage of different embedding types in your RAG pipeline.[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/cohere_retriever_eval/#note-the-results-shown-at-the-end-of-the-notebook-are-very-specific-to-dataset-and-various-other-parameters-considered-we-recommend-you-to-use-the-notebook-as-reference-to-experiment-on-your-dataset-and-evaluate-the-usage-of-different-embedding-types-in-your-rag-pipeline)
>\]  73.28K  --.-KB/s    in 0.03s   

2024-03-27 20:26:34 (2.18 MB/s) - ‘data/paul\_graham/paul\_graham\_essay.txt’ saved \[75042/75042\]

Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/cohere_retriever_eval/#load-data)
------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data()

Create Nodes[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/cohere_retriever_eval/#create-nodes)
------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

node\_parser \= SentenceSplitter(chunk\_size\=512)
nodes \= node\_parser.get\_nodes\_from\_documents(documents)

node\_parser = SentenceSplitter(chunk\_size=512) nodes = node\_parser.get\_nodes\_from\_documents(documents)

In \[ \]:

Copied!

\# by default, the node ids are set to random uuids. To ensure same id's per run, we manually set them.
for idx, node in enumerate(nodes):
    node.id\_ \= f"node\_{idx}"

\# by default, the node ids are set to random uuids. To ensure same id's per run, we manually set them. for idx, node in enumerate(nodes): node.id\_ = f"node\_{idx}"

Create retrievers for different embedding types[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/cohere_retriever_eval/#create-retrievers-for-different-embedding-types)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

\# llm for question generation
\# Take any other llm other than from cohereAI to avoid bias.
llm \= OpenAI(model\="gpt-4")

\# Function to return embedding model
def cohere\_embedding(
    model\_name: str, input\_type: str, embedding\_type: str
) \-> CohereEmbedding:
    return CohereEmbedding(
        api\_key\=os.environ\["COHERE\_API\_KEY"\],
        model\_name\=model\_name,
        input\_type\=input\_type,
        embedding\_type\=embedding\_type,
    )

\# Function to return retriver for different embedding type embedding model
def retriver(nodes, embedding\_type\="float", model\_name\="embed-english-v3.0"):
    vector\_index \= VectorStoreIndex(
        nodes,
        embed\_model\=cohere\_embedding(
            model\_name, "search\_document", embedding\_type
        ),
    )
    retriever \= vector\_index.as\_retriever(
        similarity\_top\_k\=2,
        embed\_model\=cohere\_embedding(
            model\_name, "search\_query", embedding\_type
        ),
    )
    return retriever

\# llm for question generation # Take any other llm other than from cohereAI to avoid bias. llm = OpenAI(model="gpt-4") # Function to return embedding model def cohere\_embedding( model\_name: str, input\_type: str, embedding\_type: str ) -> CohereEmbedding: return CohereEmbedding( api\_key=os.environ\["COHERE\_API\_KEY"\], model\_name=model\_name, input\_type=input\_type, embedding\_type=embedding\_type, ) # Function to return retriver for different embedding type embedding model def retriver(nodes, embedding\_type="float", model\_name="embed-english-v3.0"): vector\_index = VectorStoreIndex( nodes, embed\_model=cohere\_embedding( model\_name, "search\_document", embedding\_type ), ) retriever = vector\_index.as\_retriever( similarity\_top\_k=2, embed\_model=cohere\_embedding( model\_name, "search\_query", embedding\_type ), ) return retriever

In \[ \]:

Copied!

\# Build retriever for float embedding type
retriver\_float \= retriver(nodes)

\# Build retriever for int8 embedding type
retriver\_int8 \= retriver(nodes, "int8")

\# Build retriever for binary embedding type
retriver\_binary \= retriver(nodes, "binary")

\# Build retriever for ubinary embedding type
retriver\_ubinary \= retriver(nodes, "ubinary")

\# Build retriever for float embedding type retriver\_float = retriver(nodes) # Build retriever for int8 embedding type retriver\_int8 = retriver(nodes, "int8") # Build retriever for binary embedding type retriver\_binary = retriver(nodes, "binary") # Build retriever for ubinary embedding type retriver\_ubinary = retriver(nodes, "ubinary")

### Try out Retrieval[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/cohere_retriever_eval/#try-out-retrieval)

We'll try out retrieval over a sample query with `float` retriever.

In \[ \]:

Copied!

retrieved\_nodes \= retriver\_float.retrieve("What did the author do growing up?")

retrieved\_nodes = retriver\_float.retrieve("What did the author do growing up?")

In \[ \]:

Copied!

from llama\_index.core.response.notebook\_utils import display\_source\_node

for node in retrieved\_nodes:
    display\_source\_node(node, source\_length\=1000)

from llama\_index.core.response.notebook\_utils import display\_source\_node for node in retrieved\_nodes: display\_source\_node(node, source\_length=1000)

**Node ID:** node\_2  
**Similarity:** 0.3641554823852197  
**Text:** I remember vividly how impressed and envious I felt watching him sitting in front of it, typing programs right into the computer.

Computers were expensive in those days and it took me years of nagging before I convinced my father to buy one, a TRS-80, in about 1980. The gold standard then was the Apple II, but a TRS-80 was good enough. This was when I really started programming. I wrote simple games, a program to predict how high my model rockets would fly, and a word processor that my father used to write at least one book. There was only room in memory for about 2 pages of text, so he'd write 2 pages at a time and then print them out, but it was a lot better than a typewriter.

Though I liked programming, I didn't plan to study it in college. In college I was going to study philosophy, which sounded much more powerful. It seemed, to my naive high school self, to be the study of the ultimate truths, compared to which the things studied in other fields would be mere domain knowledg...

**Node ID:** node\_0  
**Similarity:** 0.36283154406791923  
**Text:** What I Worked On

February 2021

Before college the two main things I worked on, outside of school, were writing and programming. I didn't write essays. I wrote what beginning writers were supposed to write then, and probably still are: short stories. My stories were awful. They had hardly any plot, just characters with strong feelings, which I imagined made them deep.

The first programs I tried writing were on the IBM 1401 that our school district used for what was then called "data processing." This was in 9th grade, so I was 13 or 14. The school district's 1401 happened to be in the basement of our junior high school, and my friend Rich Draves and I got permission to use it. It was like a mini Bond villain's lair down there, with all these alien-looking machines — CPU, disk drives, printer, card reader — sitting up on a raised floor under bright fluorescent lights.

The language we used was an early version of Fortran. You had to type programs on punch cards, then stack them in ...

Evaluation dataset - Synthetic Dataset Generation of (query, context) pairs[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/cohere_retriever_eval/#evaluation-dataset-synthetic-dataset-generation-of-query-context-pairs)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Here we build a simple evaluation dataset over the existing text corpus.

We use our `generate_question_context_pairs` to generate a set of (question, context) pairs over a given unstructured text corpus. This uses the LLM to auto-generate questions from each context chunk.

We get back a `EmbeddingQAFinetuneDataset` object. At a high-level this contains a set of ids mapping to queries and relevant doc chunks, as well as the corpus itself.

In \[ \]:

Copied!

from llama\_index.core.evaluation import (
    generate\_question\_context\_pairs,
    EmbeddingQAFinetuneDataset,
)

from llama\_index.core.evaluation import ( generate\_question\_context\_pairs, EmbeddingQAFinetuneDataset, )

In \[ \]:

Copied!

qa\_dataset \= generate\_question\_context\_pairs(
    nodes, llm\=llm, num\_questions\_per\_chunk\=2
)

qa\_dataset = generate\_question\_context\_pairs( nodes, llm=llm, num\_questions\_per\_chunk=2 )

100%|██████████| 59/59 \[04:10<00:00,  4.24s/it\]

In \[ \]:

Copied!

queries \= qa\_dataset.queries.values()
print(list(queries)\[0\])

queries = qa\_dataset.queries.values() print(list(queries)\[0\])

"Describe the author's initial experiences with programming on the IBM 1401. What were some of the challenges he faced and how did these experiences shape his understanding of programming?"

In \[ \]:

Copied!

\# \[optional\] save
qa\_dataset.save\_json("pg\_eval\_dataset.json")

\# \[optional\] save qa\_dataset.save\_json("pg\_eval\_dataset.json")

In \[ \]:

Copied!

\# \[optional\] load
qa\_dataset \= EmbeddingQAFinetuneDataset.from\_json("pg\_eval\_dataset.json")

\# \[optional\] load qa\_dataset = EmbeddingQAFinetuneDataset.from\_json("pg\_eval\_dataset.json")

Use `RetrieverEvaluator` for Retrieval Evaluation[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/cohere_retriever_eval/#use-retrieverevaluator-for-retrieval-evaluation)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We're now ready to run our retrieval evals. We'll run our `RetrieverEvaluator` over the eval dataset that we generated.

### Define `RetrieverEvaluator` for different embedding\_types[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/cohere_retriever_eval/#define-retrieverevaluator-for-different-embedding_types)

In \[ \]:

Copied!

from llama\_index.core.evaluation import RetrieverEvaluator

metrics \= \["mrr", "hit\_rate"\]

\# Retrieval evaluator for float embedding type
retriever\_evaluator\_float \= RetrieverEvaluator.from\_metric\_names(
    metrics, retriever\=retriver\_float
)

\# Retrieval evaluator for int8 embedding type
retriever\_evaluator\_int8 \= RetrieverEvaluator.from\_metric\_names(
    metrics, retriever\=retriver\_int8
)

\# Retrieval evaluator for binary embedding type
retriever\_evaluator\_binary \= RetrieverEvaluator.from\_metric\_names(
    metrics, retriever\=retriver\_binary
)

\# Retrieval evaluator for ubinary embedding type
retriever\_evaluator\_ubinary \= RetrieverEvaluator.from\_metric\_names(
    metrics, retriever\=retriver\_ubinary
)

from llama\_index.core.evaluation import RetrieverEvaluator metrics = \["mrr", "hit\_rate"\] # Retrieval evaluator for float embedding type retriever\_evaluator\_float = RetrieverEvaluator.from\_metric\_names( metrics, retriever=retriver\_float ) # Retrieval evaluator for int8 embedding type retriever\_evaluator\_int8 = RetrieverEvaluator.from\_metric\_names( metrics, retriever=retriver\_int8 ) # Retrieval evaluator for binary embedding type retriever\_evaluator\_binary = RetrieverEvaluator.from\_metric\_names( metrics, retriever=retriver\_binary ) # Retrieval evaluator for ubinary embedding type retriever\_evaluator\_ubinary = RetrieverEvaluator.from\_metric\_names( metrics, retriever=retriver\_ubinary )

In \[ \]:

Copied!

\# try it out on a sample query
sample\_id, sample\_query \= list(qa\_dataset.queries.items())\[0\]
sample\_expected \= qa\_dataset.relevant\_docs\[sample\_id\]

eval\_result \= retriever\_evaluator\_float.evaluate(sample\_query, sample\_expected)
print(eval\_result)

\# try it out on a sample query sample\_id, sample\_query = list(qa\_dataset.queries.items())\[0\] sample\_expected = qa\_dataset.relevant\_docs\[sample\_id\] eval\_result = retriever\_evaluator\_float.evaluate(sample\_query, sample\_expected) print(eval\_result)

Query: "Describe the author's initial experiences with programming on the IBM 1401. What were some of the challenges he faced and how did these experiences shape his understanding of programming?"
Metrics: {'mrr': 0.5, 'hit\_rate': 1.0}

In \[ \]:

Copied!

\# Evaluation on the entire dataset

\# float embedding type
eval\_results\_float \= await retriever\_evaluator\_float.aevaluate\_dataset(
    qa\_dataset
)

\# int8 embedding type
eval\_results\_int8 \= await retriever\_evaluator\_int8.aevaluate\_dataset(
    qa\_dataset
)

\# binary embedding type
eval\_results\_binary \= await retriever\_evaluator\_binary.aevaluate\_dataset(
    qa\_dataset
)

\# ubinary embedding type
eval\_results\_ubinary \= await retriever\_evaluator\_ubinary.aevaluate\_dataset(
    qa\_dataset
)

\# Evaluation on the entire dataset # float embedding type eval\_results\_float = await retriever\_evaluator\_float.aevaluate\_dataset( qa\_dataset ) # int8 embedding type eval\_results\_int8 = await retriever\_evaluator\_int8.aevaluate\_dataset( qa\_dataset ) # binary embedding type eval\_results\_binary = await retriever\_evaluator\_binary.aevaluate\_dataset( qa\_dataset ) # ubinary embedding type eval\_results\_ubinary = await retriever\_evaluator\_ubinary.aevaluate\_dataset( qa\_dataset )

#### Define `display_results` to get the display the results in dataframe with each retriever.[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/cohere_retriever_eval/#define-display_results-to-get-the-display-the-results-in-dataframe-with-each-retriever)

In \[ \]:

Copied!

import pandas as pd

def display\_results(name, eval\_results):
    """Display results from evaluate."""

    metric\_dicts \= \[\]
    for eval\_result in eval\_results:
        metric\_dict \= eval\_result.metric\_vals\_dict
        metric\_dicts.append(metric\_dict)

    full\_df \= pd.DataFrame(metric\_dicts)

    hit\_rate \= full\_df\["hit\_rate"\].mean()
    mrr \= full\_df\["mrr"\].mean()
    columns \= {"Embedding Type": \[name\], "hit\_rate": \[hit\_rate\], "mrr": \[mrr\]}

    metric\_df \= pd.DataFrame(columns)

    return metric\_df

import pandas as pd def display\_results(name, eval\_results): """Display results from evaluate.""" metric\_dicts = \[\] for eval\_result in eval\_results: metric\_dict = eval\_result.metric\_vals\_dict metric\_dicts.append(metric\_dict) full\_df = pd.DataFrame(metric\_dicts) hit\_rate = full\_df\["hit\_rate"\].mean() mrr = full\_df\["mrr"\].mean() columns = {"Embedding Type": \[name\], "hit\_rate": \[hit\_rate\], "mrr": \[mrr\]} metric\_df = pd.DataFrame(columns) return metric\_df

Evaluation Results[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/cohere_retriever_eval/#evaluation-results)
------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

\# metrics for float embedding type
metrics\_float \= display\_results("float", eval\_results\_float)

\# metrics for int8 embedding type
metrics\_int8 \= display\_results("int8", eval\_results\_int8)

\# metrics for binary embedding type
metrics\_binary \= display\_results("binary", eval\_results\_binary)

\# metrics for ubinary embedding type
metrics\_ubinary \= display\_results("ubinary", eval\_results\_ubinary)

\# metrics for float embedding type metrics\_float = display\_results("float", eval\_results\_float) # metrics for int8 embedding type metrics\_int8 = display\_results("int8", eval\_results\_int8) # metrics for binary embedding type metrics\_binary = display\_results("binary", eval\_results\_binary) # metrics for ubinary embedding type metrics\_ubinary = display\_results("ubinary", eval\_results\_ubinary)

In \[ \]:

Copied!

combined\_metrics \= pd.concat(
    \[metrics\_float, metrics\_int8, metrics\_binary, metrics\_ubinary\]
)
combined\_metrics.set\_index(\["Embedding Type"\], append\=True, inplace\=True)

combined\_metrics = pd.concat( \[metrics\_float, metrics\_int8, metrics\_binary, metrics\_ubinary\] ) combined\_metrics.set\_index(\["Embedding Type"\], append=True, inplace=True)

In \[ \]:

Copied!

combined\_metrics

combined\_metrics

Out\[ \]:

|  |  | hit\_rate | mrr |
| --- | --- | --- | --- |
|  | Embedding Type |  |  |
| --- | --- | --- | --- |
| 0 | float | 0.805085 | 0.665254 |
| int8 | 0.813559 | 0.673729 |
| binary | 0.491525 | 0.394068 |
| ubinary | 0.449153 | 0.377119 |

Note: The results shown above are very specific to dataset, and various other parameters considered. We recommend you to use the notebook as reference to experiment on your dataset and evaluate the usage of different embedding types in your RAG pipeline.[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/cohere_retriever_eval/#note-the-results-shown-above-are-very-specific-to-dataset-and-various-other-parameters-considered-we-recommend-you-to-use-the-notebook-as-reference-to-experiment-on-your-dataset-and-evaluate-the-usage-of-different-embedding-types-in-your-rag-pipeline)


Back to top

[Previous Codestral from MistralAI Cookbook](https://docs.llamaindex.ai/en/stable/examples/cookbooks/codestral/)[Next CrewAI + LlamaIndex Cookbook](https://docs.llamaindex.ai/en/stable/examples/cookbooks/crewai_llamaindex/)
