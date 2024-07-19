Title: Building a Router from Scratch

URL Source: https://docs.llamaindex.ai/en/stable/examples/low_level/router/

Markdown Content:
Building a Router from Scratch - LlamaIndex


In this tutorial, we show you how to build an LLM-powered router module that can route a user query to submodules.

Routers are a simple but effective form of automated decision making that can allow you to perform dynamic retrieval/querying over your data.

In LlamaIndex, this is abstracted away with our [Router Modules](https://gpt-index.readthedocs.io/en/latest/core_modules/query_modules/router/root.html).

To build a router, we'll walk through the following steps:

*   Crafting an initial prompt to select a set of choices
*   Enforcing structured output (for text completion endpoints)
*   Try integrating with a native function calling endpoint.

And then we'll plug this into a RAG pipeline to dynamically make decisions on QA vs. summarization.

1\. Setup a Basic Router Prompt[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/router/#1-setup-a-basic-router-prompt)
---------------------------------------------------------------------------------------------------------------------------------

At its core, a router is a module that takes in a set of choices. Given a user query, it "selects" a relevant choice.

For simplicity, we'll start with the choices as a set of strings.

In \[ \]:

Copied!

%pip install llama\-index\-readers\-file pymupdf
%pip install llama\-index\-program\-openai
%pip install llama\-index\-llms\-openai

%pip install llama-index-readers-file pymupdf %pip install llama-index-program-openai %pip install llama-index-llms-openai

In \[ \]:

Copied!

from llama\_index.core import PromptTemplate

choices \= \[
    "Useful for questions related to apples",
    "Useful for questions related to oranges",
\]

def get\_choice\_str(choices):
    choices\_str \= "\\n\\n".join(
        \[f"{idx+1}. {c}" for idx, c in enumerate(choices)\]
    )
    return choices\_str

choices\_str \= get\_choice\_str(choices)

from llama\_index.core import PromptTemplate choices = \[ "Useful for questions related to apples", "Useful for questions related to oranges", \] def get\_choice\_str(choices): choices\_str = "\\n\\n".join( \[f"{idx+1}. {c}" for idx, c in enumerate(choices)\] ) return choices\_str choices\_str = get\_choice\_str(choices)

In \[ \]:

Copied!

router\_prompt0 \= PromptTemplate(
    "Some choices are given below. It is provided in a numbered list (1 to"
    " {num\_choices}), where each item in the list corresponds to a"
    " summary.\\n\---------------------\\n{context\_list}\\n\---------------------\\nUsing"
    " only the choices above and not prior knowledge, return the top choices"
    " (no more than {max\_outputs}, but only select what is needed) that are"
    " most relevant to the question: '{query\_str}'\\n"
)

router\_prompt0 = PromptTemplate( "Some choices are given below. It is provided in a numbered list (1 to" " {num\_choices}), where each item in the list corresponds to a" " summary.\\n---------------------\\n{context\_list}\\n---------------------\\nUsing" " only the choices above and not prior knowledge, return the top choices" " (no more than {max\_outputs}, but only select what is needed) that are" " most relevant to the question: '{query\_str}'\\n" )

Let's try this prompt on a set of toy questions and see what the output brings.

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI

llm \= OpenAI(model\="gpt-3.5-turbo")

from llama\_index.llms.openai import OpenAI llm = OpenAI(model="gpt-3.5-turbo")

In \[ \]:

Copied!

def get\_formatted\_prompt(query\_str):
    fmt\_prompt \= router\_prompt0.format(
        num\_choices\=len(choices),
        max\_outputs\=2,
        context\_list\=choices\_str,
        query\_str\=query\_str,
    )
    return fmt\_prompt

def get\_formatted\_prompt(query\_str): fmt\_prompt = router\_prompt0.format( num\_choices=len(choices), max\_outputs=2, context\_list=choices\_str, query\_str=query\_str, ) return fmt\_prompt

In \[ \]:

Copied!

query\_str \= "Can you tell me more about the amount of Vitamin C in apples"
fmt\_prompt \= get\_formatted\_prompt(query\_str)
response \= llm.complete(fmt\_prompt)

query\_str = "Can you tell me more about the amount of Vitamin C in apples" fmt\_prompt = get\_formatted\_prompt(query\_str) response = llm.complete(fmt\_prompt)

In \[ \]:

Copied!

print(str(response))

print(str(response))

1\. Useful for questions related to apples

In \[ \]:

Copied!

query\_str \= "What are the health benefits of eating orange peels?"
fmt\_prompt \= get\_formatted\_prompt(query\_str)
response \= llm.complete(fmt\_prompt)

query\_str = "What are the health benefits of eating orange peels?" fmt\_prompt = get\_formatted\_prompt(query\_str) response = llm.complete(fmt\_prompt)

In \[ \]:

Copied!

print(str(response))

print(str(response))

2\. Useful for questions related to oranges

In \[ \]:

Copied!

query\_str \= (
    "Can you tell me more about the amount of Vitamin C in apples and oranges."
)
fmt\_prompt \= get\_formatted\_prompt(query\_str)
response \= llm.complete(fmt\_prompt)

query\_str = ( "Can you tell me more about the amount of Vitamin C in apples and oranges." ) fmt\_prompt = get\_formatted\_prompt(query\_str) response = llm.complete(fmt\_prompt)

In \[ \]:

Copied!

print(str(response))

print(str(response))

1\. Useful for questions related to apples
2. Useful for questions related to oranges

**Observation**: While the response corresponds to the correct choice, it can be hacky to parse into a structured output (e.g. a single integer). We'd need to do some string parsing on the choices to extract out a single number, and make it robust to failure modes.

2\. A Router Prompt that can generate structured outputs[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/router/#2-a-router-prompt-that-can-generate-structured-outputs)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Therefore the next step is to try to prompt the model to output a more structured representation (JSON).

We define an output parser class (`RouterOutputParser`). This output parser will be responsible for both formatting the prompt and also parsing the result into a structured object (an `Answer`).

We then apply the `format` and `parse` methods of the output parser around the LLM call using the router prompt to generate a structured output.

### 2.a Import Answer Class[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/router/#2a-import-answer-class)

We load in the Answer class from our codebase. It's a very simple dataclass with two fields: `choice` and `reason`

In \[ \]:

Copied!

from dataclasses import fields
from pydantic import BaseModel
import json

from dataclasses import fields from pydantic import BaseModel import json

In \[ \]:

Copied!

class Answer(BaseModel):
    choice: int
    reason: str

class Answer(BaseModel): choice: int reason: str

In \[ \]:

Copied!

print(json.dumps(Answer.schema(), indent\=2))

print(json.dumps(Answer.schema(), indent=2))

{
  "title": "Answer",
  "type": "object",
  "properties": {
    "choice": {
      "title": "Choice",
      "type": "integer"
    },
    "reason": {
      "title": "Reason",
      "type": "string"
    }
  },
  "required": \[
    "choice",
    "reason"
  \]
}

### 2.b Define Router Output Parser[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/router/#2b-define-router-output-parser)

In \[ \]:

Copied!

from llama\_index.core.types import BaseOutputParser

from llama\_index.core.types import BaseOutputParser

In \[ \]:

Copied!

FORMAT\_STR \= """The output should be formatted as a JSON instance that conforms to 
the JSON schema below. 

Here is the output schema:
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "choice": {
        "type": "integer"
      },
      "reason": {
        "type": "string"
      }
    },
    "required": \[
      "choice",
      "reason"
    \],
    "additionalProperties": false
  }
}
"""

FORMAT\_STR = """The output should be formatted as a JSON instance that conforms to the JSON schema below. Here is the output schema: { "type": "array", "items": { "type": "object", "properties": { "choice": { "type": "integer" }, "reason": { "type": "string" } }, "required": \[ "choice", "reason" \], "additionalProperties": false } } """

If we want to put `FORMAT_STR` as part of an f-string as part of a prompt template, then we'll need to escape the curly braces so that they don't get treated as template variables.

In \[ \]:

Copied!

def \_escape\_curly\_braces(input\_string: str) \-> str:
    \# Replace '{' with '{{' and '}' with '}}' to escape curly braces
    escaped\_string \= input\_string.replace("{", "{{").replace("}", "}}")
    return escaped\_string

def \_escape\_curly\_braces(input\_string: str) -> str: # Replace '{' with '{{' and '}' with '}}' to escape curly braces escaped\_string = input\_string.replace("{", "{{").replace("}", "}}") return escaped\_string

We now define a simple parsing function to extract out the JSON string from the LLM response (by searching for square brackets)

In \[ \]:

Copied!

def \_marshal\_output\_to\_json(output: str) \-> str:
    output \= output.strip()
    left \= output.find("\[")
    right \= output.find("\]")
    output \= output\[left : right + 1\]
    return output

def \_marshal\_output\_to\_json(output: str) -> str: output = output.strip() left = output.find("\[") right = output.find("\]") output = output\[left : right + 1\] return output

We put these together in our `RouterOutputParser`

In \[ \]:

Copied!

from typing import List

class RouterOutputParser(BaseOutputParser):
    def parse(self, output: str) \-> List\[Answer\]:
        """Parse string."""
        json\_output \= \_marshal\_output\_to\_json(output)
        json\_dicts \= json.loads(json\_output)
        answers \= \[Answer.from\_dict(json\_dict) for json\_dict in json\_dicts\]
        return answers

    def format(self, prompt\_template: str) \-> str:
        return prompt\_template + "\\n\\n" + \_escape\_curly\_braces(FORMAT\_STR)

from typing import List class RouterOutputParser(BaseOutputParser): def parse(self, output: str) -> List\[Answer\]: """Parse string.""" json\_output = \_marshal\_output\_to\_json(output) json\_dicts = json.loads(json\_output) answers = \[Answer.from\_dict(json\_dict) for json\_dict in json\_dicts\] return answers def format(self, prompt\_template: str) -> str: return prompt\_template + "\\n\\n" + \_escape\_curly\_braces(FORMAT\_STR)

### 2.c Give it a Try[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/router/#2c-give-it-a-try)

We create a function called `route_query` that will take in the output parser, llm, and prompt template and output a structured answer.

In \[ \]:

Copied!

output\_parser \= RouterOutputParser()

output\_parser = RouterOutputParser()

In \[ \]:

Copied!

from typing import List

def route\_query(
    query\_str: str, choices: List\[str\], output\_parser: RouterOutputParser
):
    choices\_str

    fmt\_base\_prompt \= router\_prompt0.format(
        num\_choices\=len(choices),
        max\_outputs\=len(choices),
        context\_list\=choices\_str,
        query\_str\=query\_str,
    )
    fmt\_json\_prompt \= output\_parser.format(fmt\_base\_prompt)

    raw\_output \= llm.complete(fmt\_json\_prompt)
    parsed \= output\_parser.parse(str(raw\_output))

    return parsed

from typing import List def route\_query( query\_str: str, choices: List\[str\], output\_parser: RouterOutputParser ): choices\_str fmt\_base\_prompt = router\_prompt0.format( num\_choices=len(choices), max\_outputs=len(choices), context\_list=choices\_str, query\_str=query\_str, ) fmt\_json\_prompt = output\_parser.format(fmt\_base\_prompt) raw\_output = llm.complete(fmt\_json\_prompt) parsed = output\_parser.parse(str(raw\_output)) return parsed

3\. Perform Routing with a Function Calling Endpoint[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/router/#3-perform-routing-with-a-function-calling-endpoint)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In the previous section, we showed how to build a router with a text completion endpoint. This includes formatting the prompt to encourage the model output structured JSON, and a parse function to load in JSON.

This process can feel a bit messy. Function calling endpoints (e.g. OpenAI) abstract away this complexity by allowing the model to natively output structured functions. This obviates the need to manually prompt + parse the outputs.

LlamaIndex offers an abstraction called a `PydanticProgram` that integrates with a function endpoint to produce a structured Pydantic object. We integrate with OpenAI and Guidance.

We redefine our `Answer` class with annotations, as well as an `Answers` class containing a list of answers.

In \[ \]:

Copied!

from pydantic import Field

class Answer(BaseModel):
    "Represents a single choice with a reason."
    choice: int
    reason: str

class Answers(BaseModel):
    """Represents a list of answers."""

    answers: List\[Answer\]

from pydantic import Field class Answer(BaseModel): "Represents a single choice with a reason." choice: int reason: str class Answers(BaseModel): """Represents a list of answers.""" answers: List\[Answer\]

In \[ \]:

Copied!

Answers.schema()

Answers.schema()

Out\[ \]:

{'title': 'Answers',
 'description': 'Represents a list of answers.',
 'type': 'object',
 'properties': {'answers': {'title': 'Answers',
   'type': 'array',
   'items': {'$ref': '#/definitions/Answer'}}},
 'required': \['answers'\],
 'definitions': {'Answer': {'title': 'Answer',
   'description': 'Represents a single choice with a reason.',
   'type': 'object',
   'properties': {'choice': {'title': 'Choice', 'type': 'integer'},
    'reason': {'title': 'Reason', 'type': 'string'}},
   'required': \['choice', 'reason'\]}}}

In \[ \]:

Copied!

from llama\_index.program.openai import OpenAIPydanticProgram

from llama\_index.program.openai import OpenAIPydanticProgram

In \[ \]:

Copied!

router\_prompt1 \= router\_prompt0.partial\_format(
    num\_choices\=len(choices),
    max\_outputs\=len(choices),
)

router\_prompt1 = router\_prompt0.partial\_format( num\_choices=len(choices), max\_outputs=len(choices), )

In \[ \]:

Copied!

program \= OpenAIPydanticProgram.from\_defaults(
    output\_cls\=Answers,
    prompt\=router\_prompt1,
    verbose\=True,
)

program = OpenAIPydanticProgram.from\_defaults( output\_cls=Answers, prompt=router\_prompt1, verbose=True, )

In \[ \]:

Copied!

query\_str \= "What are the health benefits of eating orange peels?"
output \= program(context\_list\=choices\_str, query\_str\=query\_str)

query\_str = "What are the health benefits of eating orange peels?" output = program(context\_list=choices\_str, query\_str=query\_str)

Function call: Answers with args: {
  "answers": \[
    {
      "choice": 2,
      "reason": "Orange peels are related to oranges"
    }
  \]
}

In \[ \]:

Copied!

output

output

Out\[ \]:

Answers(answers=\[Answer(choice=2, reason='Orange peels are related to oranges')\])

4\. Plug Router Module as part of a RAG pipeline[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/router/#4-plug-router-module-as-part-of-a-rag-pipeline)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this section we'll put the router module to use in a RAG pipeline. We'll use it to dynamically decide whether to perform question-answering or summarization. We can easily get a question-answering query engine using top-k retrieval through our vector index, while summarization is performed through our summary index. Each query engine is described as a "choice" to our router, and we compose the whole thing into a single query engine.

### Setup: Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/router/#setup-load-data)

We load the Llama 2 paper as data.

In \[ \]:

Copied!

!mkdir data
!wget \--user\-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" \-O "data/llama2.pdf"

!mkdir data !wget --user-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" -O "data/llama2.pdf"

mkdir: data: File exists
--2023-09-17 23:37:11--  https://arxiv.org/pdf/2307.09288.pdf
Resolving arxiv.org (arxiv.org)... 128.84.21.199
Connecting to arxiv.org (arxiv.org)|128.84.21.199|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 13661300 (13M) \[application/pdf\]
Saving to: ‘data/llama2.pdf’

data/llama2.pdf     100%\[ 1:
            return responses\[0\]
        else:
            \# if multiple choices are picked, we can pick a summarizer
            response\_strs \= \[str(r) for r in responses\]
            result\_response \= self.summarizer.get\_response(
                query\_str, response\_strs
            )
            return result\_response

class RouterQueryEngine(CustomQueryEngine): """Use our Pydantic program to perform routing.""" query\_engines: List\[BaseQueryEngine\] choice\_descriptions: List\[str\] verbose: bool = False router\_prompt: PromptTemplate llm: OpenAI summarizer: TreeSummarize = Field(default\_factory=TreeSummarize) def custom\_query(self, query\_str: str): """Define custom query.""" program = OpenAIPydanticProgram.from\_defaults( output\_cls=Answers, prompt=router\_prompt1, verbose=self.verbose, llm=self.llm, ) choices\_str = get\_choice\_str(self.choice\_descriptions) output = program(context\_list=choices\_str, query\_str=query\_str) # print choice and reason, and query the underlying engine if self.verbose: print(f"Selected choice(s):") for answer in output.answers: print(f"Choice: {answer.choice}, Reason: {answer.reason}") responses = \[\] for answer in output.answers: choice\_idx = answer.choice - 1 query\_engine = self.query\_engines\[choice\_idx\] response = query\_engine.query(query\_str) responses.append(response) # if a single choice is picked, we can just return that response if len(responses) == 1: return responses\[0\] else: # if multiple choices are picked, we can pick a summarizer response\_strs = \[str(r) for r in responses\] result\_response = self.summarizer.get\_response( query\_str, response\_strs ) return result\_response

In \[ \]:

Copied!

choices \= \[
    (
        "Useful for answering questions about specific sections of the Llama 2"
        " paper"
    ),
    "Useful for questions that ask for a summary of the whole paper",
\]

router\_query\_engine \= RouterQueryEngine(
    query\_engines\=\[vector\_query\_engine, summary\_query\_engine\],
    choice\_descriptions\=choices,
    verbose\=True,
    router\_prompt\=router\_prompt1,
    llm\=OpenAI(model\="gpt-4"),
)

choices = \[ ( "Useful for answering questions about specific sections of the Llama 2" " paper" ), "Useful for questions that ask for a summary of the whole paper", \] router\_query\_engine = RouterQueryEngine( query\_engines=\[vector\_query\_engine, summary\_query\_engine\], choice\_descriptions=choices, verbose=True, router\_prompt=router\_prompt1, llm=OpenAI(model="gpt-4"), )

### Try our constructed Router Query Engine[¶](https://docs.llamaindex.ai/en/stable/examples/low_level/router/#try-our-constructed-router-query-engine)

Let's take our self-built router query engine for a spin! We ask a question that routes to the vector query engine, and also another question that routes to the summarization engine.

In \[ \]:

Copied!

response \= router\_query\_engine.query(
    "How does the Llama 2 model compare to GPT-4 in the experimental results?"
)

response = router\_query\_engine.query( "How does the Llama 2 model compare to GPT-4 in the experimental results?" )

Function call: Answers with args: {
  "answers": \[
    {
      "choice": 1,
      "reason": "This question is asking for specific information about the Llama 2 model and its comparison to GPT-4 in the experimental results. Therefore, the summary that is useful for answering questions about specific sections of the paper would be most relevant."
    }
  \]
}
Selected choice(s):
Choice: 1, Reason: This question is asking for specific information about the Llama 2 model and its comparison to GPT-4 in the experimental results. Therefore, the summary that is useful for answering questions about specific sections of the paper would be most relevant.

In \[ \]:

Copied!

print(str(response))

print(str(response))

The Llama 2 model performs better than GPT-4 in the experimental results.

In \[ \]:

Copied!

response \= router\_query\_engine.query("Can you give a summary of this paper?")

response = router\_query\_engine.query("Can you give a summary of this paper?")

Function call: Answers with args: {
  "answers": \[
    {
      "choice": 2,
      "reason": "This choice is directly related to providing a summary of the whole paper, which is what the question asks for."
    }
  \]
}
Selected choice(s):
Choice: 2, Reason: This choice is directly related to providing a summary of the whole paper, which is what the question asks for.

In \[ \]:

Copied!

print(str(response))

print(str(response))

Back to top

[Previous Building Retrieval from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/retrieval/)[Next Building a (Very Simple) Vector Store from Scratch](https://docs.llamaindex.ai/en/stable/examples/low_level/vector_store/)

Hi, how can I help you?

🦙
