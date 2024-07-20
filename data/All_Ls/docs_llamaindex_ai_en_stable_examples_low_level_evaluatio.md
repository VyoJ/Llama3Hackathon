Title: Building Evaluation from Scratch - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/low_level/evaluation/

Markdown Content:
Building Evaluation from Scratch - LlamaIndex


We show how you can build evaluation modules from scratch. This includes both evaluation of the final generated response (where the output is plain text), as well as the evaluation of retrievers (where the output is a ranked list of items).

We have in-house modules in our [Evaluation](https://gpt-index.readthedocs.io/en/latest/core_modules/supporting_modules/evaluation/root.html) section.

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/evaluation/#setup)
-----------------------------------------------------------------------------------

We load some data and define a very simple RAG query engine that we'll evaluate (uses top-k retrieval).

In \[ \]:

Copied!

%pip install llama\-index\-readers\-file pymupdf
%pip install llama\-index\-llms\-openai

%pip install llama-index-readers-file pymupdf %pip install llama-index-llms-openai

In \[ \]:

Copied!

!mkdir data
!wget \--user\-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" \-O "data/llama2.pdf"

!mkdir data !wget --user-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" -O "data/llama2.pdf"

mkdir: data: File exists
--2023-09-19 00:05:14--  https://arxiv.org/pdf/2307.09288.pdf
Resolving arxiv.org (arxiv.org)... 128.84.21.199
Connecting to arxiv.org (arxiv.org)|128.84.21.199|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 13661300 (13M) \[application/pdf\]
Saving to: ‘data/llama2.pdf’

data/llama2.pdf     100%\[>\]  13.03M  1.56MB/s    in 9.3s    

2023-09-19 00:05:25 (1.40 MB/s) - ‘data/llama2.pdf’ saved \[13661300/13661300\]

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

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex
from llama\_index.core.node\_parser import SentenceSplitter
from llama\_index.llms.openai import OpenAI

from llama\_index.core import VectorStoreIndex from llama\_index.core.node\_parser import SentenceSplitter from llama\_index.llms.openai import OpenAI

In \[ \]:

Copied!

llm \= OpenAI(model\="gpt-4")
node\_parser \= SentenceSplitter(chunk\_size\=1024)

llm = OpenAI(model="gpt-4") node\_parser = SentenceSplitter(chunk\_size=1024)

In \[ \]:

Copied!

nodes \= node\_parser.get\_nodes\_from\_documents(documents)

nodes = node\_parser.get\_nodes\_from\_documents(documents)

In \[ \]:

Copied!

index \= VectorStoreIndex(nodes)

index = VectorStoreIndex(nodes)

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(llm\=llm)

query\_engine = index.as\_query\_engine(llm=llm)

Dataset Generation[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/evaluation/#dataset-generation)
-------------------------------------------------------------------------------------------------------------

We first go through an exercise of generating a synthetic evaluation dataset. We do this by synthetically generating a set of questions from existing context. We then run each question with existing context through a powerful LLM (e.g. GPT-4) to generate a "ground-truth" response.

### Define Functions[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/evaluation/#define-functions)

We define the functions that we will use for dataset generation:

In \[ \]:

Copied!

from llama\_index.core.schema import BaseNode
from llama\_index.llms.openai import OpenAI
from llama\_index.core.llms import ChatMessage, MessageRole
from llama\_index.core import ChatPromptTemplate, PromptTemplate
from typing import Tuple, List
import re

llm \= OpenAI(model\="gpt-4")

from llama\_index.core.schema import BaseNode from llama\_index.llms.openai import OpenAI from llama\_index.core.llms import ChatMessage, MessageRole from llama\_index.core import ChatPromptTemplate, PromptTemplate from typing import Tuple, List import re llm = OpenAI(model="gpt-4")

We define `generate_answers_for_questions` to generate answers from questions given context.

In \[ \]:

Copied!

QA\_PROMPT \= PromptTemplate(
    "Context information is below.\\n"
    "---------------------\\n"
    "{context\_str}\\n"
    "---------------------\\n"
    "Given the context information and not prior knowledge, "
    "answer the query.\\n"
    "Query: {query\_str}\\n"
    "Answer: "
)

def generate\_answers\_for\_questions(
    questions: List\[str\], context: str, llm: OpenAI
) \-> str:
    """Generate answers for questions given context."""
    answers \= \[\]
    for question in questions:
        fmt\_qa\_prompt \= QA\_PROMPT.format(
            context\_str\=context, query\_str\=question
        )
        response\_obj \= llm.complete(fmt\_qa\_prompt)
        answers.append(str(response\_obj))
    return answers

QA\_PROMPT = PromptTemplate( "Context information is below.\\n" "---------------------\\n" "{context\_str}\\n" "---------------------\\n" "Given the context information and not prior knowledge, " "answer the query.\\n" "Query: {query\_str}\\n" "Answer: " ) def generate\_answers\_for\_questions( questions: List\[str\], context: str, llm: OpenAI ) -> str: """Generate answers for questions given context.""" answers = \[\] for question in questions: fmt\_qa\_prompt = QA\_PROMPT.format( context\_str=context, query\_str=question ) response\_obj = llm.complete(fmt\_qa\_prompt) answers.append(str(response\_obj)) return answers

We define `generate_qa_pairs` to generate qa pairs over an entire list of Nodes.

In \[ \]:

Copied!

QUESTION\_GEN\_USER\_TMPL \= (
    "Context information is below.\\n"
    "---------------------\\n"
    "{context\_str}\\n"
    "---------------------\\n"
    "Given the context information and not prior knowledge, "
    "generate the relevant questions. "
)

QUESTION\_GEN\_SYS\_TMPL \= """\\
You are a Teacher/ Professor. Your task is to setup \\
{num\_questions\_per\_chunk} questions for an upcoming \\
quiz/examination. The questions should be diverse in nature \\
across the document. Restrict the questions to the \\
context information provided.\\
"""

question\_gen\_template \= ChatPromptTemplate(
    message\_templates\=\[
        ChatMessage(role\=MessageRole.SYSTEM, content\=QUESTION\_GEN\_SYS\_TMPL),
        ChatMessage(role\=MessageRole.USER, content\=QUESTION\_GEN\_USER\_TMPL),
    \]
)

def generate\_qa\_pairs(
    nodes: List\[BaseNode\], llm: OpenAI, num\_questions\_per\_chunk: int \= 10
) \-> List\[Tuple\[str, str\]\]:
    """Generate questions."""
    qa\_pairs \= \[\]
    for idx, node in enumerate(nodes):
        print(f"Node {idx}/{len(nodes)}")
        context\_str \= node.get\_content(metadata\_mode\="all")
        fmt\_messages \= question\_gen\_template.format\_messages(
            num\_questions\_per\_chunk\=10,
            context\_str\=context\_str,
        )
        chat\_response \= llm.chat(fmt\_messages)
        raw\_output \= chat\_response.message.content
        result\_list \= str(raw\_output).strip().split("\\n")
        cleaned\_questions \= \[
            re.sub(r"^\\d+\[\\).\\s\]", "", question).strip()
            for question in result\_list
        \]
        answers \= generate\_answers\_for\_questions(
            cleaned\_questions, context\_str, llm
        )
        cur\_qa\_pairs \= list(zip(cleaned\_questions, answers))
        qa\_pairs.extend(cur\_qa\_pairs)
    return qa\_pairs

QUESTION\_GEN\_USER\_TMPL = ( "Context information is below.\\n" "---------------------\\n" "{context\_str}\\n" "---------------------\\n" "Given the context information and not prior knowledge, " "generate the relevant questions. " ) QUESTION\_GEN\_SYS\_TMPL = """\\ You are a Teacher/ Professor. Your task is to setup \\ {num\_questions\_per\_chunk} questions for an upcoming \\ quiz/examination. The questions should be diverse in nature \\ across the document. Restrict the questions to the \\ context information provided.\\ """ question\_gen\_template = ChatPromptTemplate( message\_templates=\[ ChatMessage(role=MessageRole.SYSTEM, content=QUESTION\_GEN\_SYS\_TMPL), ChatMessage(role=MessageRole.USER, content=QUESTION\_GEN\_USER\_TMPL), \] ) def generate\_qa\_pairs( nodes: List\[BaseNode\], llm: OpenAI, num\_questions\_per\_chunk: int = 10 ) -> List\[Tuple\[str, str\]\]: """Generate questions.""" qa\_pairs = \[\] for idx, node in enumerate(nodes): print(f"Node {idx}/{len(nodes)}") context\_str = node.get\_content(metadata\_mode="all") fmt\_messages = question\_gen\_template.format\_messages( num\_questions\_per\_chunk=10, context\_str=context\_str, ) chat\_response = llm.chat(fmt\_messages) raw\_output = chat\_response.message.content result\_list = str(raw\_output).strip().split("\\n") cleaned\_questions = \[ re.sub(r"^\\d+\[\\).\\s\]", "", question).strip() for question in result\_list \] answers = generate\_answers\_for\_questions( cleaned\_questions, context\_str, llm ) cur\_qa\_pairs = list(zip(cleaned\_questions, answers)) qa\_pairs.extend(cur\_qa\_pairs) return qa\_pairs

In \[ \]:

Copied!

qa\_pairs

qa\_pairs

Out\[ \]:

\[('What is the main focus of the work described in the document?',
  'The main focus of the work described in the document is the development and release of Llama 2, a collection of pretrained and fine-tuned large language models (LLMs) ranging in scale from 7 billion to 70 billion parameters. The fine-tuned LLMs, called Llama 2-Chat, are optimized for dialogue use cases. The document also provides a detailed description of the approach to fine-tuning and safety improvements of Llama 2-Chat.'),
 ('What is the range of parameters for the large language models (LLMs) developed in this work?',
  'The range of parameters for the large language models (LLMs) developed in this work is from 7 billion to 70 billion.'),
 ('What is the specific name given to the fine-tuned LLMs optimized for dialogue use cases?',
  'The specific name given to the fine-tuned LLMs optimized for dialogue use cases is Llama 2-Chat.'),
 ('How do the models developed in this work compare to open-source chat models based on the benchmarks tested?',
  'The models developed in this work, specifically the fine-tuned LLMs called Llama 2-Chat, outperform open-source chat models on most benchmarks tested.'),
 ('What are the two key areas of human evaluation mentioned in the document for the developed models?',
  'The two key areas of human evaluation mentioned in the document for the developed models are helpfulness and safety.'),
 ('What is the purpose of providing a detailed description of the approach to fine-tuning and safety improvements of Llama 2-Chat?',
  'The purpose of providing a detailed description of the approach to fine-tuning and safety improvements of Llama 2-Chat is to enable the community to build on their work and contribute to the responsible development of Large Language Models (LLMs).'),
 ('What is the intended benefit for the community from this work?',
  'The intended benefit for the community from this work is to enable them to build on the work and contribute to the responsible development of large language models (LLMs). The team provides a detailed description of their approach to fine-tuning and safety improvements of Llama 2-Chat for this purpose.'),
 ('Who are the corresponding authors of this work and how can they be contacted?',
  'The corresponding authors of this work are Thomas Scialom and Hugo Touvron. They can be contacted via email at tscialom@meta.com and htouvron@meta.com respectively.'),
 ('What is the source of the document and how many pages does it contain?',
  'The source of the document is "1" and it contains 77 pages.'),
 ('Where can the contributions of all the authors be found in the document?',
  'The contributions of all the authors can be found in Section A.1 of the document.')\]

### Getting Pairs over Dataset[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/evaluation/#getting-pairs-over-dataset)

**NOTE**: This can take a long time. For the sake of speed try inputting a subset of the nodes.

In \[ \]:

Copied!

qa\_pairs \= generate\_qa\_pairs(
    \# nodes\[:1\],
    nodes,
    llm,
    num\_questions\_per\_chunk\=10,
)

qa\_pairs = generate\_qa\_pairs( # nodes\[:1\], nodes, llm, num\_questions\_per\_chunk=10, )

#### \[Optional\] Define save/load[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/evaluation/#optional-define-saveload)

In \[ \]:

Copied!

\# save
import pickle

pickle.dump(qa\_pairs, open("eval\_dataset.pkl", "wb"))

\# save import pickle pickle.dump(qa\_pairs, open("eval\_dataset.pkl", "wb"))

In \[ \]:

Copied!

\# save
import pickle

qa\_pairs \= pickle.load(open("eval\_dataset.pkl", "rb"))

\# save import pickle qa\_pairs = pickle.load(open("eval\_dataset.pkl", "rb"))

Evaluating Generation[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/evaluation/#evaluating-generation)
-------------------------------------------------------------------------------------------------------------------

In this section we walk through a few methods for evaluating the generated results. At a high-level we use an "evaluation LLM" to measure the quality of the generated results. We do this in both the **with labels** setting and **without labels** setting.

We go through the following evaluation algorithms:

*   **Correctness**: Compares the generated answer against the ground-truth answer.
*   **Faithfulness**: Evaluates whether a response is faithful to the contexts (label-free).

### Building a Correctness Evaluator[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/evaluation/#building-a-correctness-evaluator)

The correctness evaluator compares the generated answer to the reference ground-truth answer, given the query. We output a score between 1 and 5, where 1 is the worst and 5 is the best.

We do this through a system and user prompt with a chat interface.

In \[ \]:

Copied!

from llama\_index.core.llms import ChatMessage, MessageRole
from llama\_index.core import ChatPromptTemplate, PromptTemplate
from typing import Dict

from llama\_index.core.llms import ChatMessage, MessageRole from llama\_index.core import ChatPromptTemplate, PromptTemplate from typing import Dict

In \[ \]:

Copied!

CORRECTNESS\_SYS\_TMPL \= """
You are an expert evaluation system for a question answering chatbot.

You are given the following information:
\- a user query, 
\- a reference answer, and
\- a generated answer.

Your job is to judge the relevance and correctness of the generated answer.
Output a single score that represents a holistic evaluation.
You must return your response in a line with only the score.
Do not return answers in any other format.
On a separate line provide your reasoning for the score as well.

Follow these guidelines for scoring:
\- Your score has to be between 1 and 5, where 1 is the worst and 5 is the best.
\- If the generated answer is not relevant to the user query, \\
you should give a score of 1.
\- If the generated answer is relevant but contains mistakes, \\
you should give a score between 2 and 3.
\- If the generated answer is relevant and fully correct, \\
you should give a score between 4 and 5.
"""

CORRECTNESS\_USER\_TMPL \= """
\## User Query
{query}

\## Reference Answer
{reference\_answer}

\## Generated Answer
{generated\_answer}
"""

CORRECTNESS\_SYS\_TMPL = """ You are an expert evaluation system for a question answering chatbot. You are given the following information: - a user query, - a reference answer, and - a generated answer. Your job is to judge the relevance and correctness of the generated answer. Output a single score that represents a holistic evaluation. You must return your response in a line with only the score. Do not return answers in any other format. On a separate line provide your reasoning for the score as well. Follow these guidelines for scoring: - Your score has to be between 1 and 5, where 1 is the worst and 5 is the best. - If the generated answer is not relevant to the user query, \\ you should give a score of 1. - If the generated answer is relevant but contains mistakes, \\ you should give a score between 2 and 3. - If the generated answer is relevant and fully correct, \\ you should give a score between 4 and 5. """ CORRECTNESS\_USER\_TMPL = """ ## User Query {query} ## Reference Answer {reference\_answer} ## Generated Answer {generated\_answer} """

In \[ \]:

Copied!

eval\_chat\_template \= ChatPromptTemplate(
    message\_templates\=\[
        ChatMessage(role\=MessageRole.SYSTEM, content\=CORRECTNESS\_SYS\_TMPL),
        ChatMessage(role\=MessageRole.USER, content\=CORRECTNESS\_USER\_TMPL),
    \]
)

eval\_chat\_template = ChatPromptTemplate( message\_templates=\[ ChatMessage(role=MessageRole.SYSTEM, content=CORRECTNESS\_SYS\_TMPL), ChatMessage(role=MessageRole.USER, content=CORRECTNESS\_USER\_TMPL), \] )

Now that we've defined the prompts template, let's define an evaluation function that feeds the prompt to the LLM and parses the output into a dict of results.

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI

def run\_correctness\_eval(
    query\_str: str,
    reference\_answer: str,
    generated\_answer: str,
    llm: OpenAI,
    threshold: float \= 4.0,
) \-> Dict:
    """Run correctness eval."""
    fmt\_messages \= eval\_chat\_template.format\_messages(
        llm\=llm,
        query\=query\_str,
        reference\_answer\=reference\_answer,
        generated\_answer\=generated\_answer,
    )
    chat\_response \= llm.chat(fmt\_messages)
    raw\_output \= chat\_response.message.content

    \# Extract from response
    score\_str, reasoning\_str \= raw\_output.split("\\n", 1)
    score \= float(score\_str)
    reasoning \= reasoning\_str.lstrip("\\n")

    return {"passing": score \>= threshold, "score": score, "reason": reasoning}

from llama\_index.llms.openai import OpenAI def run\_correctness\_eval( query\_str: str, reference\_answer: str, generated\_answer: str, llm: OpenAI, threshold: float = 4.0, ) -> Dict: """Run correctness eval.""" fmt\_messages = eval\_chat\_template.format\_messages( llm=llm, query=query\_str, reference\_answer=reference\_answer, generated\_answer=generated\_answer, ) chat\_response = llm.chat(fmt\_messages) raw\_output = chat\_response.message.content # Extract from response score\_str, reasoning\_str = raw\_output.split("\\n", 1) score = float(score\_str) reasoning = reasoning\_str.lstrip("\\n") return {"passing": score >= threshold, "score": score, "reason": reasoning}

Now let's try running this on some sample inputs with a chat model (GPT-4).

In \[ \]:

Copied!

llm \= OpenAI(model\="gpt-4")

llm = OpenAI(model="gpt-4")

In \[ \]:

Copied!

\# query\_str = "What is the range of parameters for the large language models (LLMs) developed in this work?"
\# reference\_answer = "The range of parameters for the large language models (LLMs) developed in this work is from 7 billion to 70 billion."

query\_str \= (
    "What is the specific name given to the fine-tuned LLMs optimized for"
    " dialogue use cases?"
)
reference\_answer \= (
    "The specific name given to the fine-tuned LLMs optimized for dialogue use"
    " cases is Llama 2-Chat."
)

\# query\_str = "What is the range of parameters for the large language models (LLMs) developed in this work?" # reference\_answer = "The range of parameters for the large language models (LLMs) developed in this work is from 7 billion to 70 billion." query\_str = ( "What is the specific name given to the fine-tuned LLMs optimized for" " dialogue use cases?" ) reference\_answer = ( "The specific name given to the fine-tuned LLMs optimized for dialogue use" " cases is Llama 2-Chat." )

In \[ \]:

Copied!

generated\_answer \= str(query\_engine.query(query\_str))

generated\_answer = str(query\_engine.query(query\_str))

In \[ \]:

Copied!

print(str(generated\_answer))

print(str(generated\_answer))

The fine-tuned Large Language Models (LLMs) optimized for dialogue use cases are specifically called Llama 2-Chat.

In \[ \]:

Copied!

eval\_results \= run\_correctness\_eval(
    query\_str, reference\_answer, generated\_answer, llm\=llm, threshold\=4.0
)
display(eval\_results)

eval\_results = run\_correctness\_eval( query\_str, reference\_answer, generated\_answer, llm=llm, threshold=4.0 ) display(eval\_results)

{'passing': True,
 'score': 5.0,
 'reason': 'The generated answer is completely relevant to the user query and matches the reference answer in terms of information. It correctly identifies "Llama 2-Chat" as the specific name given to the fine-tuned LLMs optimized for dialogue use cases.'}

### Building a Faithfulness Evaluator[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/evaluation/#building-a-faithfulness-evaluator)

The faithfulness evaluator evaluates whether the response is faithful to any of the retrieved contexts.

This is a step up in complexity from the correctness evaluator. Since the set of contexts can be quite long, they might overflow the context window. We would need to figure out how to implement a form of **response synthesis** strategy to iterate over contexts in sequence.

We have a corresponding tutorial showing you [how to build response synthesis from scratch](https://gpt-index.readthedocs.io/en/latest/examples/low_level/response_synthesis.html). We also have [out-of-the-box response synthesis modules](https://gpt-index.readthedocs.io/en/latest/core_modules/query_modules/response_synthesizers/root.html). In this guide we'll use the out of the box modules.

In \[ \]:

Copied!

EVAL\_TEMPLATE \= PromptTemplate(
    "Please tell if a given piece of information "
    "is supported by the context.\\n"
    "You need to answer with either YES or NO.\\n"
    "Answer YES if any of the context supports the information, even "
    "if most of the context is unrelated. "
    "Some examples are provided below. \\n\\n"
    "Information: Apple pie is generally double-crusted.\\n"
    "Context: An apple pie is a fruit pie in which the principal filling "
    "ingredient is apples. \\n"
    "Apple pie is often served with whipped cream, ice cream "
    "('apple pie à la mode'), custard or cheddar cheese.\\n"
    "It is generally double-crusted, with pastry both above "
    "and below the filling; the upper crust may be solid or "
    "latticed (woven of crosswise strips).\\n"
    "Answer: YES\\n"
    "Information: Apple pies tastes bad.\\n"
    "Context: An apple pie is a fruit pie in which the principal filling "
    "ingredient is apples. \\n"
    "Apple pie is often served with whipped cream, ice cream "
    "('apple pie à la mode'), custard or cheddar cheese.\\n"
    "It is generally double-crusted, with pastry both above "
    "and below the filling; the upper crust may be solid or "
    "latticed (woven of crosswise strips).\\n"
    "Answer: NO\\n"
    "Information: {query\_str}\\n"
    "Context: {context\_str}\\n"
    "Answer: "
)

EVAL\_REFINE\_TEMPLATE \= PromptTemplate(
    "We want to understand if the following information is present "
    "in the context information: {query\_str}\\n"
    "We have provided an existing YES/NO answer: {existing\_answer}\\n"
    "We have the opportunity to refine the existing answer "
    "(only if needed) with some more context below.\\n"
    "------------\\n"
    "{context\_msg}\\n"
    "------------\\n"
    "If the existing answer was already YES, still answer YES. "
    "If the information is present in the new context, answer YES. "
    "Otherwise answer NO.\\n"
)

EVAL\_TEMPLATE = PromptTemplate( "Please tell if a given piece of information " "is supported by the context.\\n" "You need to answer with either YES or NO.\\n" "Answer YES if any of the context supports the information, even " "if most of the context is unrelated. " "Some examples are provided below. \\n\\n" "Information: Apple pie is generally double-crusted.\\n" "Context: An apple pie is a fruit pie in which the principal filling " "ingredient is apples. \\n" "Apple pie is often served with whipped cream, ice cream " "('apple pie à la mode'), custard or cheddar cheese.\\n" "It is generally double-crusted, with pastry both above " "and below the filling; the upper crust may be solid or " "latticed (woven of crosswise strips).\\n" "Answer: YES\\n" "Information: Apple pies tastes bad.\\n" "Context: An apple pie is a fruit pie in which the principal filling " "ingredient is apples. \\n" "Apple pie is often served with whipped cream, ice cream " "('apple pie à la mode'), custard or cheddar cheese.\\n" "It is generally double-crusted, with pastry both above " "and below the filling; the upper crust may be solid or " "latticed (woven of crosswise strips).\\n" "Answer: NO\\n" "Information: {query\_str}\\n" "Context: {context\_str}\\n" "Answer: " ) EVAL\_REFINE\_TEMPLATE = PromptTemplate( "We want to understand if the following information is present " "in the context information: {query\_str}\\n" "We have provided an existing YES/NO answer: {existing\_answer}\\n" "We have the opportunity to refine the existing answer " "(only if needed) with some more context below.\\n" "------------\\n" "{context\_msg}\\n" "------------\\n" "If the existing answer was already YES, still answer YES. " "If the information is present in the new context, answer YES. " "Otherwise answer NO.\\n" )

**NOTE**: In the current response synthesizer setup we don't separate out a system and user message for chat endpoints, so we just use our standard `llm.complete` for text completion.

We now define our function below. Since we defined both a standard eval template for a given piece of context but also a refine template for subsequent contexts, we implement our "create-and-refine" response synthesis strategy to obtain the answer.

In \[ \]:

Copied!

from llama\_index.core.response\_synthesizers import Refine
from typing import List, Dict

def run\_faithfulness\_eval(
    generated\_answer: str,
    contexts: List\[str\],
    llm: OpenAI,
) \-> Dict:
    """Run faithfulness eval."""

    refine \= Refine(
        llm\=llm,
        text\_qa\_template\=EVAL\_TEMPLATE,
        refine\_template\=EVAL\_REFINE\_TEMPLATE,
    )

    response\_obj \= refine.get\_response(generated\_answer, contexts)
    response\_txt \= str(response\_obj)

    if "yes" in response\_txt.lower():
        passing \= True
    else:
        passing \= False

    return {"passing": passing, "reason": str(response\_txt)}

from llama\_index.core.response\_synthesizers import Refine from typing import List, Dict def run\_faithfulness\_eval( generated\_answer: str, contexts: List\[str\], llm: OpenAI, ) -> Dict: """Run faithfulness eval.""" refine = Refine( llm=llm, text\_qa\_template=EVAL\_TEMPLATE, refine\_template=EVAL\_REFINE\_TEMPLATE, ) response\_obj = refine.get\_response(generated\_answer, contexts) response\_txt = str(response\_obj) if "yes" in response\_txt.lower(): passing = True else: passing = False return {"passing": passing, "reason": str(response\_txt)}

Let's try it out on some data

In \[ \]:

Copied!

\# use the same query\_str, and reference\_answer as above
\# query\_str = "What is the specific name given to the fine-tuned LLMs optimized for dialogue use cases?"
\# reference\_answer = "The specific name given to the fine-tuned LLMs optimized for dialogue use cases is Llama 2-Chat."

response \= query\_engine.query(query\_str)
generated\_answer \= str(response)

\# use the same query\_str, and reference\_answer as above # query\_str = "What is the specific name given to the fine-tuned LLMs optimized for dialogue use cases?" # reference\_answer = "The specific name given to the fine-tuned LLMs optimized for dialogue use cases is Llama 2-Chat." response = query\_engine.query(query\_str) generated\_answer = str(response)

In \[ \]:

Copied!

context\_list \= \[n.get\_content() for n in response.source\_nodes\]
eval\_results \= run\_faithfulness\_eval(
    generated\_answer,
    contexts\=context\_list,
    llm\=llm,
)
display(eval\_results)

context\_list = \[n.get\_content() for n in response.source\_nodes\] eval\_results = run\_faithfulness\_eval( generated\_answer, contexts=context\_list, llm=llm, ) display(eval\_results)

{'passing': True, 'reason': 'YES'}

Running Evaluation over our Eval Dataset[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/evaluation/#running-evaluation-over-our-eval-dataset)
---------------------------------------------------------------------------------------------------------------------------------------------------------

Now let's tie the two above sections together and run our eval modules over our eval dataset!

**NOTE**: For the sake of speed/cost we extract a very limited sample.

In \[ \]:

Copied!

import random

sample\_size \= 5
qa\_pairs\_sample \= random.sample(qa\_pairs, sample\_size)

import random sample\_size = 5 qa\_pairs\_sample = random.sample(qa\_pairs, sample\_size)

In \[ \]:

Copied!

import pandas as pd

def run\_evals(qa\_pairs: List\[Tuple\[str, str\]\], llm: OpenAI, query\_engine):
    results\_list \= \[\]
    for question, reference\_answer in qa\_pairs:
        response \= query\_engine.query(question)
        generated\_answer \= str(response)
        correctness\_results \= run\_correctness\_eval(
            query\_str,
            reference\_answer,
            generated\_answer,
            llm\=llm,
            threshold\=4.0,
        )
        faithfulness\_results \= run\_faithfulness\_eval(
            generated\_answer,
            contexts\=context\_list,
            llm\=llm,
        )
        cur\_result\_dict \= {
            "correctness": correctness\_results\["passing"\],
            "faithfulness": faithfulness\_results\["passing"\],
        }
        results\_list.append(cur\_result\_dict)
    return pd.DataFrame(results\_list)

import pandas as pd def run\_evals(qa\_pairs: List\[Tuple\[str, str\]\], llm: OpenAI, query\_engine): results\_list = \[\] for question, reference\_answer in qa\_pairs: response = query\_engine.query(question) generated\_answer = str(response) correctness\_results = run\_correctness\_eval( query\_str, reference\_answer, generated\_answer, llm=llm, threshold=4.0, ) faithfulness\_results = run\_faithfulness\_eval( generated\_answer, contexts=context\_list, llm=llm, ) cur\_result\_dict = { "correctness": correctness\_results\["passing"\], "faithfulness": faithfulness\_results\["passing"\], } results\_list.append(cur\_result\_dict) return pd.DataFrame(results\_list)

In \[ \]:

Copied!

evals\_df \= run\_evals(qa\_pairs\_sample, llm, query\_engine)

evals\_df = run\_evals(qa\_pairs\_sample, llm, query\_engine)

In \[ \]:

Copied!

evals\_df\["correctness"\].mean()

evals\_df\["correctness"\].mean()

Out\[ \]:

0.4

In \[ \]:

Copied!

evals\_df\["faithfulness"\].mean()

evals\_df\["faithfulness"\].mean()

Out\[ \]:

0.6

Back to top

[Previous Llama Packs Example](https://docs.llamaindex.ai/en/stable/examples/llama_hub/llama_packs_example/)[Next Building an Advanced Fusion Retriever from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/fusion_retriever/)

Hi, how can I help you?

🦙
