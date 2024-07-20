Title: Refine with Structured Answer Filtering

URL Source: https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/structured_refine/

Markdown Content:
Refine with Structured Answer Filtering - LlamaIndex


When using our Refine response synthesizer for response synthesis, it's crucial to filter out non-answers. An issue often encountered is the propagation of a single unhelpful response like "I don't have the answer", which can persist throughout the synthesis process and lead to a final answer of the same nature. This can occur even when there are actual answers present in other, more relevant sections.

These unhelpful responses can be filtered out by setting `structured_answer_filtering` to `True`. It is set to `False` by default since this currently only works best if you are using an OpenAI model that supports function calling.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai

%pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/structured_refine/#load-data)
--------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

texts \= \[
    "The president in the year 2040 is John Cena.",
    "The president in the year 2050 is Florence Pugh.",
    'The president in the year 2060 is Dwayne "The Rock" Johnson.',
\]

texts = \[ "The president in the year 2040 is John Cena.", "The president in the year 2050 is Florence Pugh.", 'The president in the year 2060 is Dwayne "The Rock" Johnson.', \]

Summarize[¶](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/structured_refine/#summarize)
--------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..."

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI

llm \= OpenAI(model\="gpt-3.5-turbo-0613")

from llama\_index.llms.openai import OpenAI llm = OpenAI(model="gpt-3.5-turbo-0613")

In \[ \]:

Copied!

from llama\_index.core import get\_response\_synthesizer

summarizer \= get\_response\_synthesizer(
    response\_mode\="refine", llm\=llm, verbose\=True
)

from llama\_index.core import get\_response\_synthesizer summarizer = get\_response\_synthesizer( response\_mode="refine", llm=llm, verbose=True )

In \[ \]:

Copied!

response \= summarizer.get\_response("who is president in the year 2050?", texts)

response = summarizer.get\_response("who is president in the year 2050?", texts)

\> Refine context: The president in the year 2050 is Florence Pugh.
> Refine context: The president in the year 2060 is Dwayne "The R...

### Failed Result[¶](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/structured_refine/#failed-result)

As you can see, we weren't able to get the correct answer from the input `texts` strings since the initial "I don't know" answer propogated through till the end of the response synthesis.

In \[ \]:

Copied!

print(response)

print(response)

I'm sorry, but I don't have access to information about the future.

Now we'll try again with `structured_answer_filtering=True`

In \[ \]:

Copied!

from llama\_index.core import get\_response\_synthesizer

summarizer \= get\_response\_synthesizer(
    response\_mode\="refine",
    llm\=llm,
    verbose\=True,
    structured\_answer\_filtering\=True,
)

from llama\_index.core import get\_response\_synthesizer summarizer = get\_response\_synthesizer( response\_mode="refine", llm=llm, verbose=True, structured\_answer\_filtering=True, )

In \[ \]:

Copied!

response \= summarizer.get\_response("who is president in the year 2050?", texts)

response = summarizer.get\_response("who is president in the year 2050?", texts)

Function call: StructuredRefineResponse with args: {
  "answer": "It is not possible to determine who the president is in the year 2050 based on the given context information.",
  "query\_satisfied": false
}
> Refine context: The president in the year 2050 is Florence Pugh.
Function call: StructuredRefineResponse with args: {
  "answer": "Florence Pugh",
  "query\_satisfied": true
}
> Refine context: The president in the year 2060 is Dwayne "The R...
Function call: StructuredRefineResponse with args: {
  "answer": "Florence Pugh",
  "query\_satisfied": false
}

### Successful Result[¶](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/structured_refine/#successful-result)

As you can see, we were able to determine the correct answer from the given context by filtering the `texts` strings for the ones that actually contained the answer to our question.

In \[ \]:

Copied!

print(response)

print(response)

Florence Pugh

Non Function-calling LLMs[¶](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/structured_refine/#non-function-calling-llms)
----------------------------------------------------------------------------------------------------------------------------------------------

You may want to make use of this filtering functionality with an LLM that doesn't offer a function calling API.

In that case, the `Refine` module will automatically switch to using a structured output `Program` that doesn't rely on an external function calling API.

In \[ \]:

Copied!

\# we'll stick with OpenAI but use an older model that does not support function calling
instruct\_llm \= OpenAI(model\="gpt-3.5-turbo-instruct")

\# we'll stick with OpenAI but use an older model that does not support function calling instruct\_llm = OpenAI(model="gpt-3.5-turbo-instruct")

In \[ \]:

Copied!

from llama\_index.core import get\_response\_synthesizer

summarizer \= get\_response\_synthesizer(
    response\_mode\="refine",
    llm\=instruct\_llm,
    verbose\=True,
    structured\_answer\_filtering\=True,
)

from llama\_index.core import get\_response\_synthesizer summarizer = get\_response\_synthesizer( response\_mode="refine", llm=instruct\_llm, verbose=True, structured\_answer\_filtering=True, )

In \[ \]:

Copied!

response \= summarizer.get\_response("who is president in the year 2050?", texts)
print(response)

response = summarizer.get\_response("who is president in the year 2050?", texts) print(response)

Florence Pugh

### `CompactAndRefine`[¶](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/structured_refine/#compactandrefine)

Since `CompactAndRefine` is built on top of `Refine`, this response mode also supports structured answer filtering.

In \[ \]:

Copied!

from llama\_index.core import get\_response\_synthesizer

summarizer \= get\_response\_synthesizer(
    response\_mode\="compact",
    llm\=instruct\_llm,
    verbose\=True,
    structured\_answer\_filtering\=True,
)

from llama\_index.core import get\_response\_synthesizer summarizer = get\_response\_synthesizer( response\_mode="compact", llm=instruct\_llm, verbose=True, structured\_answer\_filtering=True, )

In \[ \]:

Copied!

response \= summarizer.get\_response("who is president in the year 2050?", texts)
print(response)

response = summarizer.get\_response("who is president in the year 2050?", texts) print(response)

Florence Pugh

Back to top

[Previous Refine](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/refine/)[Next Tree Summarize](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/tree_summarize/)
