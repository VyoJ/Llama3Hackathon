Title: PaLM - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/llm/palm/

Markdown Content:
PaLM - LlamaIndex


In this short notebook, we show how to use the PaLM LLM from Google in LlamaIndex: [https://ai.google/discover/palm2/](https://ai.google/discover/palm2/).

We use the `text-bison-001` model by default.

### Setup[¶](https://docs.llamaindex.ai/en/stable/examples/llm/palm/#setup)

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-palm

%pip install llama-index-llms-palm

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

!pip install \-q google\-generativeai

!pip install -q google-generativeai

\[notice\] A new release of pip available: 22.3.1 -> 23.1.2
\[notice\] To update, run: pip install --upgrade pip

In \[ \]:

Copied!

import pprint
import google.generativeai as palm

import pprint import google.generativeai as palm

In \[ \]:

Copied!

palm\_api\_key \= ""

palm\_api\_key = ""

In \[ \]:

Copied!

palm.configure(api\_key\=palm\_api\_key)

palm.configure(api\_key=palm\_api\_key)

### Define Model[¶](https://docs.llamaindex.ai/en/stable/examples/llm/palm/#define-model)

In \[ \]:

Copied!

models \= \[
    m
    for m in palm.list\_models()
    if "generateText" in m.supported\_generation\_methods
\]
model \= models\[0\].name
print(model)

models = \[ m for m in palm.list\_models() if "generateText" in m.supported\_generation\_methods \] model = models\[0\].name print(model)

models/text-bison-001

### Start using our `PaLM` LLM abstraction![¶](https://docs.llamaindex.ai/en/stable/examples/llm/palm/#start-using-our-palm-llm-abstraction)

In \[ \]:

Copied!

from llama\_index.llms.palm import PaLM

model \= PaLM(api\_key\=palm\_api\_key)

from llama\_index.llms.palm import PaLM model = PaLM(api\_key=palm\_api\_key)

In \[ \]:

Copied!

model.complete(prompt)

model.complete(prompt)

Out\[ \]:

CompletionResponse(text='1 house has 3 cats \* 4 mittens / cat = 12 mittens.\\n3 houses have 12 mittens / house \* 3 houses = 36 mittens.\\n1 hat needs 4m of yarn. 36 hats need 4m / hat \* 36 hats = 144m of yarn.\\n1 mitten needs 7m of yarn. 36 mittens need 7m / mitten \* 36 mittens = 252m of yarn.\\nIn total 144m of yarn was needed for hats and 252m of yarn was needed for mittens, so 144m + 252m = 396m of yarn was needed.\\n\\nThe answer: 396', additional\_kwargs={}, raw={'output': '1 house has 3 cats \* 4 mittens / cat = 12 mittens.\\n3 houses have 12 mittens / house \* 3 houses = 36 mittens.\\n1 hat needs 4m of yarn. 36 hats need 4m / hat \* 36 hats = 144m of yarn.\\n1 mitten needs 7m of yarn. 36 mittens need 7m / mitten \* 36 mittens = 252m of yarn.\\nIn total 144m of yarn was needed for hats and 252m of yarn was needed for mittens, so 144m + 252m = 396m of yarn was needed.\\n\\nThe answer: 396', 'safety\_ratings': \[{'category': <HarmCategory.HARM\_CATEGORY\_DEROGATORY: 1>, 'probability': <HarmProbability.NEGLIGIBLE: 1>}, {'category': <HarmCategory.HARM\_CATEGORY\_TOXICITY: 2>, 'probability': <HarmProbability.NEGLIGIBLE: 1>}, {'category': <HarmCategory.HARM\_CATEGORY\_VIOLENCE: 3>, 'probability': <HarmProbability.NEGLIGIBLE: 1>}, {'category': <HarmCategory.HARM\_CATEGORY\_SEXUAL: 4>, 'probability': <HarmProbability.NEGLIGIBLE: 1>}, {'category': <HarmCategory.HARM\_CATEGORY\_MEDICAL: 5>, 'probability': <HarmProbability.NEGLIGIBLE: 1>}, {'category': <HarmCategory.HARM\_CATEGORY\_DANGEROUS: 6>, 'probability': <HarmProbability.NEGLIGIBLE: 1>}\]}, delta=None)

Back to top

[Previous Optimum Intel LLMs optimized with IPEX backend](https://docs.llamaindex.ai/en/stable/examples/llm/optimum_intel/)[Next Perplexity](https://docs.llamaindex.ai/en/stable/examples/llm/perplexity/)
