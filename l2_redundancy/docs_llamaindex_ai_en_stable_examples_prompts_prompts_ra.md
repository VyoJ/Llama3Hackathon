Title: Prompt Engineering for RAG - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/prompts/prompts_rag/

Markdown Content:
Prompt Engineering for RAG - LlamaIndex


In this notebook we show various prompt techniques you can try to customize your LlamaIndex RAG pipeline.

*   Getting and setting prompts for query engines, etc.
*   Defining template variable mappings (e.g. you have an existing QA prompt)
*   Adding few-shot examples + performing query transformations/rewriting.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai
%pip install llama\-index\-readers\-file pymupdf

%pip install llama-index-llms-openai %pip install llama-index-readers-file pymupdf

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import os
import openai

import os import openai

In \[ \]:

Copied!

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."
openai.api\_key \= os.environ\["OPENAI\_API\_KEY"\]

os.environ\["OPENAI\_API\_KEY"\] = "sk-..." openai.api\_key = os.environ\["OPENAI\_API\_KEY"\]

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/prompts/prompts_rag/#setup)
----------------------------------------------------------------------------------

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

from llama\_index.core import VectorStoreIndex
from llama\_index.core import PromptTemplate
from IPython.display import Markdown, display

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout)) from llama\_index.core import VectorStoreIndex from llama\_index.core import PromptTemplate from IPython.display import Markdown, display

INFO:numexpr.utils:Note: NumExpr detected 12 cores but "NUMEXPR\_MAX\_THREADS" not set, so enforcing safe limit of 8.
Note: NumExpr detected 12 cores but "NUMEXPR\_MAX\_THREADS" not set, so enforcing safe limit of 8.
INFO:numexpr.utils:NumExpr defaulting to 8 threads.
NumExpr defaulting to 8 threads.

#### Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/prompts/prompts_rag/#load-data)

In \[ \]:

Copied!

!mkdir data
!wget \--user\-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" \-O "data/llama2.pdf"

!mkdir data !wget --user-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" -O "data/llama2.pdf"

mkdir: data: File exists
--2023-10-28 23:19:38--  https://arxiv.org/pdf/2307.09288.pdf
Resolving arxiv.org (arxiv.org)... 128.84.21.199
Connecting to arxiv.org (arxiv.org)|128.84.21.199|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 13661300 (13M) \[application/pdf\]
Saving to: ‘data/llama2.pdf’

data/llama2.pdf     100%\[>\]  13.03M  1.50MB/s    in 10s     

2023-10-28 23:19:49 (1.31 MB/s) - ‘data/llama2.pdf’ saved \[13661300/13661300\]

In \[ \]:

Copied!

from pathlib import Path
from llama\_index.readers.file import PyMuPDFReader

from pathlib import Path from llama\_index.readers.file import PyMuPDFReader

In \[ \]:

Copied!

loader \= PyMuPDFReader()
documents \= loader.load(file\_path\="./data/llama2.pdf")

loader = PyMuPDFReader() documents = loader.load(file\_path="./data/llama2.pdf")

#### Load into Vector Store[¶](https://docs.llamaindex.ai/en/stable/examples/prompts/prompts_rag/#load-into-vector-store)

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex
from llama\_index.llms.openai import OpenAI

gpt35\_llm \= OpenAI(model\="gpt-3.5-turbo")
gpt4\_llm \= OpenAI(model\="gpt-4")

index \= VectorStoreIndex.from\_documents(documents)

from llama\_index.core import VectorStoreIndex from llama\_index.llms.openai import OpenAI gpt35\_llm = OpenAI(model="gpt-3.5-turbo") gpt4\_llm = OpenAI(model="gpt-4") index = VectorStoreIndex.from\_documents(documents)

#### Setup Query Engine / Retriever[¶](https://docs.llamaindex.ai/en/stable/examples/prompts/prompts_rag/#setup-query-engine-retriever)

In \[ \]:

Copied!

query\_str \= "What are the potential risks associated with the use of Llama 2 as mentioned in the context?"

query\_str = "What are the potential risks associated with the use of Llama 2 as mentioned in the context?"

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(similarity\_top\_k\=2, llm\=gpt35\_llm)
\# use this for testing
vector\_retriever \= index.as\_retriever(similarity\_top\_k\=2)

query\_engine = index.as\_query\_engine(similarity\_top\_k=2, llm=gpt35\_llm) # use this for testing vector\_retriever = index.as\_retriever(similarity\_top\_k=2)

In \[ \]:

Copied!

response \= query\_engine.query(query\_str)
print(str(response))

response = query\_engine.query(query\_str) print(str(response))

The potential risks associated with the use of Llama 2, as mentioned in the context, include the generation of misinformation and the retrieval of information about topics such as bioterrorism or cybercrime. The models have been tuned to avoid these topics and diminish any capabilities they might have offered for those use cases. However, there is a possibility that the safety tuning of the models may go too far, resulting in an overly cautious approach where the model declines certain requests or responds with too many safety details. Users of Llama 2 and Llama 2-Chat need to be cautious and take extra steps in tuning and deployment to ensure responsible use.

Viewing/Customizing Prompts[¶](https://docs.llamaindex.ai/en/stable/examples/prompts/prompts_rag/#viewingcustomizing-prompts)
-----------------------------------------------------------------------------------------------------------------------------

First, let's take a look at the query engine prompts, and see how we can customize it.

### View Prompts[¶](https://docs.llamaindex.ai/en/stable/examples/prompts/prompts_rag/#view-prompts)

In \[ \]:

Copied!

\# define prompt viewing function
def display\_prompt\_dict(prompts\_dict):
    for k, p in prompts\_dict.items():
        text\_md \= f"\*\*Prompt Key\*\*: {k}<br>" f"\*\*Text:\*\* <br>"
        display(Markdown(text\_md))
        print(p.get\_template())
        display(Markdown("<br><br>"))

\# define prompt viewing function def display\_prompt\_dict(prompts\_dict): for k, p in prompts\_dict.items(): text\_md = f"\*\*Prompt Key\*\*: {k}  
" f"\*\*Text:\*\*  
" display(Markdown(text\_md)) print(p.get\_template()) display(Markdown("  
  
"))

In \[ \]:

Copied!

prompts\_dict \= query\_engine.get\_prompts()

prompts\_dict = query\_engine.get\_prompts()

In \[ \]:

Copied!

display\_prompt\_dict(prompts\_dict)

display\_prompt\_dict(prompts\_dict)

**Prompt Key**: response\_synthesizer:text\_qa\_template  
**Text:**

Context information is below.
---------------------
{context\_str}
---------------------
Given the context information and not prior knowledge, answer the query.
Query: {query\_str}
Answer: 

**Prompt Key**: response\_synthesizer:refine\_template  
**Text:**

The original query is as follows: {query\_str}
We have provided an existing answer: {existing\_answer}
We have the opportunity to refine the existing answer (only if needed) with some more context below.
------------
{context\_msg}
------------
Given the new context, refine the original answer to better answer the query. If the context isn't useful, return the original answer.
Refined Answer: 

### Customize Prompts[¶](https://docs.llamaindex.ai/en/stable/examples/prompts/prompts_rag/#customize-prompts)

What if we want to do something different than our standard question-answering prompts?

Let's try out the RAG prompt from [LangchainHub](https://smith.langchain.com/hub/rlm/rag-prompt)

In \[ \]:

Copied!

\# to do this, you need to use the langchain object

from langchain import hub

langchain\_prompt \= hub.pull("rlm/rag-prompt")

\# to do this, you need to use the langchain object from langchain import hub langchain\_prompt = hub.pull("rlm/rag-prompt")

One catch is that the template variables in the prompt are different than what's expected by our synthesizer in the query engine:

*   the prompt uses `context` and `question`,
*   we expect `context_str` and `query_str`

This is not a problem! Let's add our template variable mappings to map variables. We use our `LangchainPromptTemplate` to map to LangChain prompts.

In \[ \]:

Copied!

from llama\_index.core.prompts import LangchainPromptTemplate

lc\_prompt\_tmpl \= LangchainPromptTemplate(
    template\=langchain\_prompt,
    template\_var\_mappings\={"query\_str": "question", "context\_str": "context"},
)

query\_engine.update\_prompts(
    {"response\_synthesizer:text\_qa\_template": lc\_prompt\_tmpl}
)

from llama\_index.core.prompts import LangchainPromptTemplate lc\_prompt\_tmpl = LangchainPromptTemplate( template=langchain\_prompt, template\_var\_mappings={"query\_str": "question", "context\_str": "context"}, ) query\_engine.update\_prompts( {"response\_synthesizer:text\_qa\_template": lc\_prompt\_tmpl} )

In \[ \]:

Copied!

prompts\_dict \= query\_engine.get\_prompts()
display\_prompt\_dict(prompts\_dict)

prompts\_dict = query\_engine.get\_prompts() display\_prompt\_dict(prompts\_dict)

**Prompt Key**: response\_synthesizer:text\_qa\_template  
**Text:**

input\_variables=\['question', 'context'\] messages=\[HumanMessagePromptTemplate(prompt=PromptTemplate(input\_variables=\['question', 'context'\], template="You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.\\nQuestion: {question} \\nContext: {context} \\nAnswer:"))\]

**Prompt Key**: response\_synthesizer:refine\_template  
**Text:**

The original query is as follows: {query\_str}
We have provided an existing answer: {existing\_answer}
We have the opportunity to refine the existing answer (only if needed) with some more context below.
------------
{context\_msg}
------------
Given the new context, refine the original answer to better answer the query. If the context isn't useful, return the original answer.
Refined Answer: 

### Try It Out[¶](https://docs.llamaindex.ai/en/stable/examples/prompts/prompts_rag/#try-it-out)

Let's re-run our query engine again.

In \[ \]:

Copied!

response \= query\_engine.query(query\_str)
print(str(response))

response = query\_engine.query(query\_str) print(str(response))

The potential risks associated with the use of Llama 2 mentioned in the context include the generation of misinformation, retrieval of information about topics like bioterrorism or cybercrime, an overly cautious approach by the model, and the need for users to be cautious and take extra steps in tuning and deployment. However, efforts have been made to tune the models to avoid these topics and diminish any capabilities they might have offered for those use cases.

Adding Few-Shot Examples[¶](https://docs.llamaindex.ai/en/stable/examples/prompts/prompts_rag/#adding-few-shot-examples)
------------------------------------------------------------------------------------------------------------------------

Let's try adding few-shot examples to the prompt, which can be dynamically loaded depending on the query!

We do this by setting the `function_mapping` variable in our prompt template - this allows us to compute functions (e.g. return few-shot examples) during prompt formatting time.

As an example use case, through this we can coerce the model to output results in a structured format, by showing examples of other structured outputs.

Let's parse a pre-generated question/answer file. For the sake of focus we'll skip how the file is generated (tl;dr we used a GPT-4 powered function calling RAG pipeline), but the qa pairs look like this:

```
{"query": "<query>", "response": "<output_json>"}
```

We embed/index these Q/A pairs, and retrieve the top-k.

In \[ \]:

Copied!

from llama\_index.core.schema import TextNode

few\_shot\_nodes \= \[\]
for line in open("../llama2\_qa\_citation\_events.jsonl", "r"):
    few\_shot\_nodes.append(TextNode(text\=line))

few\_shot\_index \= VectorStoreIndex(few\_shot\_nodes)
few\_shot\_retriever \= few\_shot\_index.as\_retriever(similarity\_top\_k\=2)

from llama\_index.core.schema import TextNode few\_shot\_nodes = \[\] for line in open("../llama2\_qa\_citation\_events.jsonl", "r"): few\_shot\_nodes.append(TextNode(text=line)) few\_shot\_index = VectorStoreIndex(few\_shot\_nodes) few\_shot\_retriever = few\_shot\_index.as\_retriever(similarity\_top\_k=2)

In \[ \]:

Copied!

import json

def few\_shot\_examples\_fn(\*\*kwargs):
    query\_str \= kwargs\["query\_str"\]
    retrieved\_nodes \= few\_shot\_retriever.retrieve(query\_str)
    \# go through each node, get json object

    result\_strs \= \[\]
    for n in retrieved\_nodes:
        raw\_dict \= json.loads(n.get\_content())
        query \= raw\_dict\["query"\]
        response\_dict \= json.loads(raw\_dict\["response"\])
        result\_str \= f"""\\
Query: {query}
Response: {response\_dict}"""
        result\_strs.append(result\_str)
    return "\\n\\n".join(result\_strs)

import json def few\_shot\_examples\_fn(\*\*kwargs): query\_str = kwargs\["query\_str"\] retrieved\_nodes = few\_shot\_retriever.retrieve(query\_str) # go through each node, get json object result\_strs = \[\] for n in retrieved\_nodes: raw\_dict = json.loads(n.get\_content()) query = raw\_dict\["query"\] response\_dict = json.loads(raw\_dict\["response"\]) result\_str = f"""\\ Query: {query} Response: {response\_dict}""" result\_strs.append(result\_str) return "\\n\\n".join(result\_strs)

In \[ \]:

Copied!

\# write prompt template with functions
qa\_prompt\_tmpl\_str \= """\\
Context information is below.
\---------------------
{context\_str}
\---------------------
Given the context information and not prior knowledge, \\
answer the query asking about citations over different topics.
Please provide your answer in the form of a structured JSON format containing \\
a list of authors as the citations. Some examples are given below.

{few\_shot\_examples}

Query: {query\_str}
Answer: \\
"""

qa\_prompt\_tmpl \= PromptTemplate(
    qa\_prompt\_tmpl\_str,
    function\_mappings\={"few\_shot\_examples": few\_shot\_examples\_fn},
)

\# write prompt template with functions qa\_prompt\_tmpl\_str = """\\ Context information is below. --------------------- {context\_str} --------------------- Given the context information and not prior knowledge, \\ answer the query asking about citations over different topics. Please provide your answer in the form of a structured JSON format containing \\ a list of authors as the citations. Some examples are given below. {few\_shot\_examples} Query: {query\_str} Answer: \\ """ qa\_prompt\_tmpl = PromptTemplate( qa\_prompt\_tmpl\_str, function\_mappings={"few\_shot\_examples": few\_shot\_examples\_fn}, )

In \[ \]:

Copied!

citation\_query\_str \= (
    "Which citations are mentioned in the section on Safety RLHF?"
)

citation\_query\_str = ( "Which citations are mentioned in the section on Safety RLHF?" )

Let's see what the formatted prompt looks like with the few-shot examples function. (we fill in test context for brevity)

In \[ \]:

Copied!

print(
    qa\_prompt\_tmpl.format(
        query\_str\=citation\_query\_str, context\_str\="test\_context"
    )
)

print( qa\_prompt\_tmpl.format( query\_str=citation\_query\_str, context\_str="test\_context" ) )

Context information is below.
---------------------
test\_context
---------------------
Given the context information and not prior knowledge, answer the query asking about citations over different topics.
Please provide your answer in the form of a structured JSON format containing a list of authors as the citations. Some examples are given below.

Query: Which citation discusses the impact of safety RLHF measured by reward model score distributions?
Response: {'citations': \[{'author': 'Llama 2: Open Foundation and Fine-Tuned Chat Models', 'year': 24, 'desc': 'Impact of safety RLHF measured by reward model score distributions. Left: safety reward model scores of generations on the Meta Safety test set. The clustering of samples in the top left corner suggests the improvements of model safety. Right: helpfulness reward model scores of generations on the Meta Helpfulness test set.'}\]}

Query: Which citations are mentioned in the section on RLHF Results?
Response: {'citations': \[{'author': 'Gilardi et al.', 'year': 2023, 'desc': ''}, {'author': 'Huang et al.', 'year': 2023, 'desc': ''}\]}

Query: Which citations are mentioned in the section on Safety RLHF?
Answer: 

In \[ \]:

Copied!

query\_engine.update\_prompts(
    {"response\_synthesizer:text\_qa\_template": qa\_prompt\_tmpl}
)

query\_engine.update\_prompts( {"response\_synthesizer:text\_qa\_template": qa\_prompt\_tmpl} )

In \[ \]:

Copied!

display\_prompt\_dict(query\_engine.get\_prompts())

display\_prompt\_dict(query\_engine.get\_prompts())

**Prompt Key**: response\_synthesizer:text\_qa\_template  
**Text:**

Context information is below.
---------------------
{context\_str}
---------------------
Given the context information and not prior knowledge, answer the query asking about citations over different topics.
Please provide your answer in the form of a structured JSON format containing a list of authors as the citations. Some examples are given below.

{few\_shot\_examples}

Query: {query\_str}
Answer: 

**Prompt Key**: response\_synthesizer:refine\_template  
**Text:**

The original query is as follows: {query\_str}
We have provided an existing answer: {existing\_answer}
We have the opportunity to refine the existing answer (only if needed) with some more context below.
------------
{context\_msg}
------------
Given the new context, refine the original answer to better answer the query. If the context isn't useful, return the original answer.
Refined Answer: 

In \[ \]:

Copied!

response \= query\_engine.query(citation\_query\_str)
print(str(response))

response = query\_engine.query(citation\_query\_str) print(str(response))

{'citations': \[{'author': 'Llama 2: Open Foundation and Fine-Tuned Chat Models', 'year': 24, 'desc': 'Safety RLHF'}, {'author': 'Bai et al.', 'year': 2022a, 'desc': 'RLHF stage'}, {'author': 'Bai et al.', 'year': 2022a, 'desc': 'adversarial prompts'}, {'author': 'Bai et al.', 'year': 2022a, 'desc': 'safety reward model'}, {'author': 'Bai et al.', 'year': 2022a, 'desc': 'helpfulness reward model'}, {'author': 'Bai et al.', 'year': 2022a, 'desc': 'safety tuning with RLHF'}\]}

In \[ \]:

Copied!

print(response.source\_nodes\[1\].get\_content())

print(response.source\_nodes\[1\].get\_content())

Context Transformations - PII Example[¶](https://docs.llamaindex.ai/en/stable/examples/prompts/prompts_rag/#context-transformations-pii-example)
------------------------------------------------------------------------------------------------------------------------------------------------

We can also dynamically add context transformations as functions in the prompt variable. In this example we show how we can process the `context_str` before feeding to the context window - specifically in masking out PII (a step towards alleviating concerns around data privacy/security).

**NOTE**: You can do these as steps before feeding into the prompt as well, but this gives you flexibility to perform all this on the fly for any QA prompt you define!

In \[ \]:

Copied!

from llama\_index.core.postprocessor import (
    NERPIINodePostprocessor,
    SentenceEmbeddingOptimizer,
)
from llama\_index.core import QueryBundle
from llama\_index.core.schema import NodeWithScore, TextNode

from llama\_index.core.postprocessor import ( NERPIINodePostprocessor, SentenceEmbeddingOptimizer, ) from llama\_index.core import QueryBundle from llama\_index.core.schema import NodeWithScore, TextNode

In \[ \]:

Copied!

pii\_processor \= NERPIINodePostprocessor(llm\=gpt4\_llm)

pii\_processor = NERPIINodePostprocessor(llm=gpt4\_llm)

In \[ \]:

Copied!

def filter\_pii\_fn(\*\*kwargs):
    \# run optimizer
    query\_bundle \= QueryBundle(query\_str\=kwargs\["query\_str"\])

    new\_nodes \= pii\_processor.postprocess\_nodes(
        \[NodeWithScore(node\=TextNode(text\=kwargs\["context\_str"\]))\],
        query\_bundle\=query\_bundle,
    )
    new\_node \= new\_nodes\[0\]
    return new\_node.get\_content()

def filter\_pii\_fn(\*\*kwargs): # run optimizer query\_bundle = QueryBundle(query\_str=kwargs\["query\_str"\]) new\_nodes = pii\_processor.postprocess\_nodes( \[NodeWithScore(node=TextNode(text=kwargs\["context\_str"\]))\], query\_bundle=query\_bundle, ) new\_node = new\_nodes\[0\] return new\_node.get\_content()

In \[ \]:

Copied!

qa\_prompt\_tmpl\_str \= (
    "Context information is below.\\n"
    "---------------------\\n"
    "{context\_str}\\n"
    "---------------------\\n"
    "Given the context information and not prior knowledge, "
    "answer the query.\\n"
    "Query: {query\_str}\\n"
    "Answer: "
)
qa\_prompt\_tmpl \= PromptTemplate(
    qa\_prompt\_tmpl\_str, function\_mappings\={"context\_str": filter\_pii\_fn}
)

qa\_prompt\_tmpl\_str = ( "Context information is below.\\n" "---------------------\\n" "{context\_str}\\n" "---------------------\\n" "Given the context information and not prior knowledge, " "answer the query.\\n" "Query: {query\_str}\\n" "Answer: " ) qa\_prompt\_tmpl = PromptTemplate( qa\_prompt\_tmpl\_str, function\_mappings={"context\_str": filter\_pii\_fn} )

In \[ \]:

Copied!

query\_engine.update\_prompts(
    {"response\_synthesizer:text\_qa\_template": qa\_prompt\_tmpl}
)

query\_engine.update\_prompts( {"response\_synthesizer:text\_qa\_template": qa\_prompt\_tmpl} )

In \[ \]:

Copied!

\# take a look at the prompt
retrieved\_nodes \= vector\_retriever.retrieve(query\_str)
context\_str \= "\\n\\n".join(\[n.get\_content() for n in retrieved\_nodes\])

\# take a look at the prompt retrieved\_nodes = vector\_retriever.retrieve(query\_str) context\_str = "\\n\\n".join(\[n.get\_content() for n in retrieved\_nodes\])

In \[ \]:

Copied!

print(qa\_prompt\_tmpl.format(query\_str\=query\_str, context\_str\=context\_str))

print(qa\_prompt\_tmpl.format(query\_str=query\_str, context\_str=context\_str))

In \[ \]:

Copied!

response \= query\_engine.query(query\_str)
print(str(response))

response = query\_engine.query(query\_str) print(str(response))

Back to top

[Previous "Optimization by Prompting" for RAG](https://docs.llamaindex.ai/en/stable/examples/prompts/prompt_optimization/)[Next Using a Property Graph Store](https://docs.llamaindex.ai/en/stable/examples/property_graph/graph_store/)

Hi, how can I help you?

🦙
