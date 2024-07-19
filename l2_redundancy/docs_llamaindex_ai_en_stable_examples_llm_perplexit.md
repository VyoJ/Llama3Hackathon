Title: Perplexity - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/llm/perplexity/

Markdown Content:
Perplexity - LlamaIndex


Before we get started, make sure you install llama\_index

In \[ \]:

Copied!

%pip install llama\-index\-llms\-perplexity

%pip install llama-index-llms-perplexity

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

Setup LLM[¶](https://docs.llamaindex.ai/en/stable/examples/llm/perplexity/#setup-llm)
-------------------------------------------------------------------------------------

As of Nov 14, 2023 - the following models are supported with the Perplexity LLM class in LLaMa Index:

| Model | Context Length | Model Type |
| --- | --- | --- |
| codellama-34b-instruct | 16384 | Chat Completion |
| llama-2-13b-chat | 4096 | Chat Completion |
| llama-2-70b-chat | 4096 | Chat Completion |
| mistral-7b-instruct | 4096 \[1\] | Chat Completion |
| openhermes-2-mistral-7b | 4096 \[1\] | Chat Completion |
| openhermes-2.5-mistral-7b | 4096 \[1\] | Chat Completion |
| replit-code-v1.5-3b | 4096 | Text Completion |
| pplx-7b-chat-alpha | 4096 | Chat Completion |
| pplx-70b-chat-alpha | 4096 | Chat Completion |

\[1\] Context length of mistral-7b-instruct and openhermes-2-mistral-7b will be increased to 32k tokens (see perplexity roadmap).

You can find the latest supported models here - [https://docs.perplexity.ai/docs/model-cards](https://docs.perplexity.ai/docs/model-cards)  
Rate limits are found here - [https://docs.perplexity.ai/docs/rate-limits](https://docs.perplexity.ai/docs/rate-limits)

In \[ \]:

Copied!

from llama\_index.llms.perplexity import Perplexity

pplx\_api\_key \= "your-perplexity-api-key"

llm \= Perplexity(
    api\_key\=pplx\_api\_key, model\="mistral-7b-instruct", temperature\=0.5
)

from llama\_index.llms.perplexity import Perplexity pplx\_api\_key = "your-perplexity-api-key" llm = Perplexity( api\_key=pplx\_api\_key, model="mistral-7b-instruct", temperature=0.5 )

In \[ \]:

Copied!

from llama\_index.core.llms import ChatMessage

messages\_dict \= \[
    {"role": "system", "content": "Be precise and concise."},
    {"role": "user", "content": "Tell me 5 sentences about Perplexity."},
\]
messages \= \[ChatMessage(\*\*msg) for msg in messages\_dict\]

from llama\_index.core.llms import ChatMessage messages\_dict = \[ {"role": "system", "content": "Be precise and concise."}, {"role": "user", "content": "Tell me 5 sentences about Perplexity."}, \] messages = \[ChatMessage(\*\*msg) for msg in messages\_dict\]

Chat[¶](https://docs.llamaindex.ai/en/stable/examples/llm/perplexity/#chat)
---------------------------------------------------------------------------

In \[ \]:

Copied!

response \= llm.chat(messages)
print(response)

response = llm.chat(messages) print(response)

assistant: 1. Perplexity is the state of being puzzled or confused.
2. It is a measure of how difficult it is to understand something.
3. Perplexity can be caused by a lack of information or a mismatch between the information provided and what is being understood.
4. It can also be caused by the complexity of a problem or the way it is presented.
5. Perplexity can be reduced through further information, clarification, or simplification.

Async Chat[¶](https://docs.llamaindex.ai/en/stable/examples/llm/perplexity/#async-chat)
---------------------------------------------------------------------------------------

In \[ \]:

Copied!

response \= await llm.achat(messages)
print(response)

response = await llm.achat(messages) print(response)

assistant: 1. Perplexity is a measure of how difficult it is to understand or solve a problem or concept.
2. It is often used in fields such as cryptography, linguistics, and artificial intelligence.
3. A high degree of perplexity indicates that a problem or concept is complex and difficult to understand.
4. Perplexity can be calculated using various mathematical formulas, such as the entropy formula.
5. Perplexity is an important concept in many areas of study, as it helps researchers to better understand and solve complex problems.

Stream Chat[¶](https://docs.llamaindex.ai/en/stable/examples/llm/perplexity/#stream-chat)
-----------------------------------------------------------------------------------------

In \[ \]:

Copied!

resp \= llm.stream\_chat(messages)
for r in resp:
    print(r.delta, end\="")

resp = llm.stream\_chat(messages) for r in resp: print(r.delta, end="")

1\. Perplexity refers to the state of being confused or bewildered.
2. It can be caused by a lack of understanding or a mismatch between one's expectations and reality.
3. Perplexity can occur in various areas of life, such as personal relationships, work, or decision-making processes.
4. It can lead to feelings of frustration or anxiety, and can be difficult to resolve.
5. However, perplexity can also be a source of inspiration or creativity, as it can challenge one's assumptions and assumptions.

Async Stream Chat[¶](https://docs.llamaindex.ai/en/stable/examples/llm/perplexity/#async-stream-chat)
-----------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

resp \= await llm.astream\_chat(messages)
async for delta in resp:
    print(delta.delta, end\="")

resp = await llm.astream\_chat(messages) async for delta in resp: print(delta.delta, end="")

1\. Perplexity refers to the state of being puzzled or confused.
2. It is often associated with a lack of understanding or difficulty in comprehending something.
3. Perplexity can be caused by a variety of factors, including complexity, ambiguity, or lack of information.
4. It can manifest in different forms, such as confusion, uncertainty, or disorientation.
5. Perplexity can be overcome through problem-solving, clarification, or seeking additional information.

Back to top

[Previous PaLM](https://docs.llamaindex.ai/en/stable/examples/llm/palm/)[Next Portkey](https://docs.llamaindex.ai/en/stable/examples/llm/portkey/)

Hi, how can I help you?

🦙
