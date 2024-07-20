Title: Cohere - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/llm/cohere/

Markdown Content:
Cohere - LlamaIndex


Basic Usage[¶](https://docs.llamaindex.ai/en/stable/examples/llm/cohere/#basic-usage)
-------------------------------------------------------------------------------------

#### Call `complete` with a prompt[¶](https://docs.llamaindex.ai/en/stable/examples/llm/cohere/#call-complete-with-a-prompt)

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai
%pip install llama\-index\-llms\-cohere

%pip install llama-index-llms-openai %pip install llama-index-llms-cohere

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

from llama\_index.llms.cohere import Cohere

api\_key \= "Your api key"
resp \= Cohere(api\_key\=api\_key).complete("Paul Graham is ")

from llama\_index.llms.cohere import Cohere api\_key = "Your api key" resp = Cohere(api\_key=api\_key).complete("Paul Graham is ")

Your text contains a trailing whitespace, which has been trimmed to ensure high quality generations.

In \[ \]:

Copied!

print(resp)

print(resp)

an English computer scientist, entrepreneur and investor. He is best known for his work as a co-founder of the seed accelerator Y Combinator. He is also the author of the free startup advice blog "Startups.com". Paul Graham is known for his philanthropic efforts. Has given away hundreds of millions of dollars to good causes.

#### Call `chat` with a list of messages[¶](https://docs.llamaindex.ai/en/stable/examples/llm/cohere/#call-chat-with-a-list-of-messages)

In \[ \]:

Copied!

from llama\_index.core.llms import ChatMessage
from llama\_index.llms.cohere import Cohere

messages \= \[
    ChatMessage(role\="user", content\="hello there"),
    ChatMessage(
        role\="assistant", content\="Arrrr, matey! How can I help ye today?"
    ),
    ChatMessage(role\="user", content\="What is your name"),
\]

resp \= Cohere(api\_key\=api\_key).chat(
    messages, preamble\_override\="You are a pirate with a colorful personality"
)

from llama\_index.core.llms import ChatMessage from llama\_index.llms.cohere import Cohere messages = \[ ChatMessage(role="user", content="hello there"), ChatMessage( role="assistant", content="Arrrr, matey! How can I help ye today?" ), ChatMessage(role="user", content="What is your name"), \] resp = Cohere(api\_key=api\_key).chat( messages, preamble\_override="You are a pirate with a colorful personality" )

In \[ \]:

Copied!

print(resp)

print(resp)

assistant: Traditionally, ye refers to gender-nonconforming people of any gender, and those who are genderless, whereas matey refers to a friend, commonly used to address a fellow pirate. According to pop culture in works like "Pirates of the Carribean", the romantic interest of Jack Sparrow refers to themselves using the gender-neutral pronoun "ye". 

Are you interested in learning more about the pirate culture?

Streaming[¶](https://docs.llamaindex.ai/en/stable/examples/llm/cohere/#streaming)
---------------------------------------------------------------------------------

Using `stream_complete` endpoint

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI

llm \= Cohere(api\_key\=api\_key)
resp \= llm.stream\_complete("Paul Graham is ")

from llama\_index.llms.openai import OpenAI llm = Cohere(api\_key=api\_key) resp = llm.stream\_complete("Paul Graham is ")

In \[ \]:

Copied!

for r in resp:
    print(r.delta, end\="")

for r in resp: print(r.delta, end="")

 an English computer scientist, essayist, and venture capitalist. He is best known for his work as a co-founder of the Y Combinator startup incubator, and his essays, which are widely read and influential in the startup community. 

Using `stream_chat` endpoint

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI

llm \= Cohere(api\_key\=api\_key)
messages \= \[
    ChatMessage(role\="user", content\="hello there"),
    ChatMessage(
        role\="assistant", content\="Arrrr, matey! How can I help ye today?"
    ),
    ChatMessage(role\="user", content\="What is your name"),
\]
resp \= llm.stream\_chat(
    messages, preamble\_override\="You are a pirate with a colorful personality"
)

from llama\_index.llms.openai import OpenAI llm = Cohere(api\_key=api\_key) messages = \[ ChatMessage(role="user", content="hello there"), ChatMessage( role="assistant", content="Arrrr, matey! How can I help ye today?" ), ChatMessage(role="user", content="What is your name"), \] resp = llm.stream\_chat( messages, preamble\_override="You are a pirate with a colorful personality" )

In \[ \]:

Copied!

for r in resp:
    print(r.delta, end\="")

for r in resp: print(r.delta, end="")

Arrrr, matey! According to etiquette, we are suppose to exchange names first! Mine remains a mystery for now.

Configure Model[¶](https://docs.llamaindex.ai/en/stable/examples/llm/cohere/#configure-model)
---------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.llms.cohere import Cohere

llm \= Cohere(model\="command", api\_key\=api\_key)

from llama\_index.llms.cohere import Cohere llm = Cohere(model="command", api\_key=api\_key)

In \[ \]:

Copied!

resp \= llm.complete("Paul Graham is ")

resp = llm.complete("Paul Graham is ")

Your text contains a trailing whitespace, which has been trimmed to ensure high quality generations.

In \[ \]:

Copied!

print(resp)

print(resp)

an English computer scientist, entrepreneur and investor. He is best known for his work as a co-founder of the seed accelerator Y Combinator. He is also the co-founder of the online dating platform Match.com. 

Async[¶](https://docs.llamaindex.ai/en/stable/examples/llm/cohere/#async)
-------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.llms.cohere import Cohere

llm \= Cohere(model\="command", api\_key\=api\_key)

from llama\_index.llms.cohere import Cohere llm = Cohere(model="command", api\_key=api\_key)

In \[ \]:

Copied!

resp \= await llm.acomplete("Paul Graham is ")

resp = await llm.acomplete("Paul Graham is ")

Your text contains a trailing whitespace, which has been trimmed to ensure high quality generations.

In \[ \]:

Copied!

print(resp)

print(resp)

an English computer scientist, entrepreneur and investor. He is best known for his work as a co-founder of the startup incubator and seed fund Y Combinator, and the programming language Lisp. He has also written numerous essays, many of which have become highly influential in the software engineering field. 

In \[ \]:

Copied!

resp \= await llm.astream\_complete("Paul Graham is ")

resp = await llm.astream\_complete("Paul Graham is ")

In \[ \]:

Copied!

async for delta in resp:
    print(delta.delta, end\="")

async for delta in resp: print(delta.delta, end="")

 an English computer scientist, essayist, and businessman. He is best known for his work as a co-founder of the startup accelerator Y Combinator, and his essay "Beating the Averages." 

Set API Key at a per-instance level[¶](https://docs.llamaindex.ai/en/stable/examples/llm/cohere/#set-api-key-at-a-per-instance-level)
-------------------------------------------------------------------------------------------------------------------------------------

If desired, you can have separate LLM instances use separate API keys.

In \[ \]:

Copied!

from llama\_index.llms.cohere import Cohere

llm\_good \= Cohere(api\_key\=api\_key)
llm\_bad \= Cohere(model\="command", api\_key\="BAD\_KEY")

resp \= llm\_good.complete("Paul Graham is ")
print(resp)

resp \= llm\_bad.complete("Paul Graham is ")
print(resp)

from llama\_index.llms.cohere import Cohere llm\_good = Cohere(api\_key=api\_key) llm\_bad = Cohere(model="command", api\_key="BAD\_KEY") resp = llm\_good.complete("Paul Graham is ") print(resp) resp = llm\_bad.complete("Paul Graham is ") print(resp)

Your text contains a trailing whitespace, which has been trimmed to ensure high quality generations.

an English computer scientist, entrepreneur and investor. He is best known for his work as a co-founder of the acceleration program Y Combinator. He has also written extensively on the topics of computer science and entrepreneurship. Where did you come across his name? 

\---------------------------------------------------------------------------
CohereAPIError                            Traceback (most recent call last)
Cell In\[17\], line 9
      6 resp \= llm\_good.complete("Paul Graham is ")
      7 print(resp)
\----> 9 resp \= llm\_bad.complete("Paul Graham is ")
     10 print(resp)

File /workspaces/llama\_index/gllama\_index/llms/base.py:277, in llm\_completion\_callback.<locals>.wrap.<locals>.wrapped\_llm\_predict(\_self, \*args, \*\*kwargs)
    267 with wrapper\_logic(\_self) as callback\_manager:
    268     event\_id \= callback\_manager.on\_event\_start(
    269         CBEventType.LLM,
    270         payload\={
   (...)
    274         },
    275     )
\--> 277     f\_return\_val \= f(\_self, \*args, \*\*kwargs)
    278     if isinstance(f\_return\_val, Generator):
    279         \# intercept the generator and add a callback to the end
    280         def wrapped\_gen() \-\> CompletionResponseGen:

File /workspaces/llama\_index/gllama\_index/llms/cohere.py:139, in Cohere.complete(self, prompt, \*\*kwargs)
    136 @llm\_completion\_callback()
    137 def complete(self, prompt: str, \*\*kwargs: Any) \-\> CompletionResponse:
    138     all\_kwargs \= self.\_get\_all\_kwargs(\*\*kwargs)
\--> 139     response \= completion\_with\_retry(
    140 client\=self.\_client,
    141 max\_retries\=self.max\_retries,
    142 chat\=False,
    143 prompt\=prompt,
    144 \*\*all\_kwargs
    145 )
    147     return CompletionResponse(
    148         text\=response.generations\[0\].text,
    149         raw\=response.\_\_dict\_\_,
    150     )

File /workspaces/llama\_index/gllama\_index/llms/cohere\_utils.py:74, in completion\_with\_retry(client, max\_retries, chat, \*\*kwargs)
     71     else:
     72         return client.generate(\*\*kwargs)
\---> 74 return \_completion\_with\_retry(\*\*kwargs)

File ~/.local/share/projects/oss/llama\_index/.venv/lib/python3.10/site-packages/tenacity/\_\_init\_\_.py:289, in BaseRetrying.wraps.<locals>.wrapped\_f(\*args, \*\*kw)
    287 @functools.wraps(f)
    288 def wrapped\_f(\*args: t.Any, \*\*kw: t.Any) \-\> t.Any:
\--> 289     return self(f, \*args, \*\*kw)

File ~/.local/share/projects/oss/llama\_index/.venv/lib/python3.10/site-packages/tenacity/\_\_init\_\_.py:379, in Retrying.\_\_call\_\_(self, fn, \*args, \*\*kwargs)
    377 retry\_state \= RetryCallState(retry\_object\=self, fn\=fn, args\=args, kwargs\=kwargs)
    378 while True:
\--> 379     do \= self.iter(retry\_state\=retry\_state)
    380     if isinstance(do, DoAttempt):
    381         try:

File ~/.local/share/projects/oss/llama\_index/.venv/lib/python3.10/site-packages/tenacity/\_\_init\_\_.py:314, in BaseRetrying.iter(self, retry\_state)
    312 is\_explicit\_retry \= fut.failed and isinstance(fut.exception(), TryAgain)
    313 if not (is\_explicit\_retry or self.retry(retry\_state)):
\--> 314     return fut.result()
    316 if self.after is not None:
    317     self.after(retry\_state)

File /usr/lib/python3.10/concurrent/futures/\_base.py:449, in Future.result(self, timeout)
    447     raise CancelledError()
    448 elif self.\_state \== FINISHED:
\--> 449     return self.\_\_get\_result()
    451 self.\_condition.wait(timeout)
    453 if self.\_state in \[CANCELLED, CANCELLED\_AND\_NOTIFIED\]:

File /usr/lib/python3.10/concurrent/futures/\_base.py:401, in Future.\_\_get\_result(self)
    399 if self.\_exception:
    400     try:
\--> 401         raise self.\_exception
    402     finally:
    403         \# Break a reference cycle with the exception in self.\_exception
    404         self \= None

File ~/.local/share/projects/oss/llama\_index/.venv/lib/python3.10/site-packages/tenacity/\_\_init\_\_.py:382, in Retrying.\_\_call\_\_(self, fn, \*args, \*\*kwargs)
    380 if isinstance(do, DoAttempt):
    381     try:
\--> 382         result \= fn(\*args, \*\*kwargs)
    383     except BaseException:  \# noqa: B902
    384         retry\_state.set\_exception(sys.exc\_info())  \# type: ignore\[arg-type\]

File /workspaces/llama\_index/gllama\_index/llms/cohere\_utils.py:72, in completion\_with\_retry.<locals>.\_completion\_with\_retry(\*\*kwargs)
     70     return client.chat(\*\*kwargs)
     71 else:
\---> 72     return client.generate(\*\*kwargs)

File ~/.local/share/projects/oss/llama\_index/.venv/lib/python3.10/site-packages/cohere/client.py:221, in Client.generate(self, prompt, prompt\_vars, model, preset, num\_generations, max\_tokens, temperature, k, p, frequency\_penalty, presence\_penalty, end\_sequences, stop\_sequences, return\_likelihoods, truncate, logit\_bias, stream)
    164 """Generate endpoint.
    165 See https://docs.cohere.ai/reference/generate for advanced arguments
    166 
   (...)
    200         >>>     print(token)
    201 """
    202 json\_body \= {
    203     "model": model,
    204     "prompt": prompt,
   (...)
    219     "stream": stream,
    220 }
\--> 221 response \= self.\_request(cohere.GENERATE\_URL, json\=json\_body, stream\=stream)
    222 if stream:
    223     return StreamingGenerations(response)

File ~/.local/share/projects/oss/llama\_index/.venv/lib/python3.10/site-packages/cohere/client.py:927, in Client.\_request(self, endpoint, json, files, method, stream, params)
    924     except jsonlib.decoder.JSONDecodeError:  \# CohereAPIError will capture status
    925         raise CohereAPIError.from\_response(response, message\=f"Failed to decode json body: {response.text}")
\--> 927     self.\_check\_response(json\_response, response.headers, response.status\_code)
    928 return json\_response

File ~/.local/share/projects/oss/llama\_index/.venv/lib/python3.10/site-packages/cohere/client.py:869, in Client.\_check\_response(self, json\_response, headers, status\_code)
    867     logger.warning(headers\["X-API-Warning"\])
    868 if "message" in json\_response:  \# has errors
\--> 869     raise CohereAPIError(
    870         message\=json\_response\["message"\],
    871         http\_status\=status\_code,
    872         headers\=headers,
    873     )
    874 if 400 <\= status\_code < 500:
    875     raise CohereAPIError(
    876         message\=f"Unexpected client error (status {status\_code}): {json\_response}",
    877         http\_status\=status\_code,
    878         headers\=headers,
    879     )

CohereAPIError: invalid api token

Back to top

[Previous Cleanlab Trustworthy Language Model](https://docs.llamaindex.ai/en/stable/examples/llm/cleanlab/)[Next DashScope LLMS](https://docs.llamaindex.ai/en/stable/examples/llm/dashscope/)
