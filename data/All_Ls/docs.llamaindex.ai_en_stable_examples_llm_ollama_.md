Title: Ollama - Llama 3 - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/llm/ollama/

Markdown Content:
Ollama - Llama 3 - LlamaIndex


Setup[¶](https://docs.llamaindex.ai/en/stable/examples/llm/ollama/#setup)
-------------------------------------------------------------------------

First, follow the [readme](https://github.com/jmorganca/ollama) to set up and run a local Ollama instance.

When the Ollama app is running on your local machine:

*   All of your local models are automatically served on localhost:11434
*   Select your model when setting llm = Ollama(..., model=":")
*   Increase defaullt timeout (30 seconds) if needed setting Ollama(..., request\_timeout=300.0)
*   If you set llm = Ollama(..., model="<model family") without a version it will simply look for latest

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-ollama

%pip install llama-index-llms-ollama

In \[ \]:

Copied!

from llama\_index.llms.ollama import Ollama

from llama\_index.llms.ollama import Ollama

In \[ \]:

Copied!

llm \= Ollama(model\="llama3", request\_timeout\=120.0)

llm = Ollama(model="llama3", request\_timeout=120.0)

In \[ \]:

Copied!

resp \= llm.complete("Who is Paul Graham?")

resp = llm.complete("Who is Paul Graham?")

In \[ \]:

Copied!

print(resp)

print(resp)

Paul Graham (1924-2011) was a British Anglican priest and Christian theologian. He was a prominent figure in the Church of England and a leading ecumenist, known for his work on Christian unity and dialogue with other religions.

Graham served as a parish priest in Yorkshire, England, before becoming Dean of York Cathedral from 1966 to 1984. During this time, he was also involved in various ecumenical initiatives, including the Anglican-Lutheran Dialogue and the International Anglican-Roman Catholic Commission on Unity and Mission.

One of Graham's most notable contributions was his work on Christian-Jewish relations. He was a strong advocate for reconciliation between Christians and Jews, and he worked closely with Jewish leaders to promote understanding and cooperation between the two communities.

Graham was also a prolific writer and published several books on theology, ecumenism, and Christian-Jewish relations. His writings emphasized the importance of dialogue and mutual respect in building bridges between different religious traditions.

Throughout his career, Graham received numerous awards and honors for his contributions to ecumenism and interfaith understanding. He is remembered as a respected leader and a champion of unity and cooperation among people of different faiths.

#### Call `chat` with a list of messages[¶](https://docs.llamaindex.ai/en/stable/examples/llm/ollama/#call-chat-with-a-list-of-messages)

In \[ \]:

Copied!

from llama\_index.core.llms import ChatMessage

messages \= \[
    ChatMessage(
        role\="system", content\="You are a pirate with a colorful personality"
    ),
    ChatMessage(role\="user", content\="What is your name"),
\]
resp \= llm.chat(messages)

from llama\_index.core.llms import ChatMessage messages = \[ ChatMessage( role="system", content="You are a pirate with a colorful personality" ), ChatMessage(role="user", content="What is your name"), \] resp = llm.chat(messages)

In \[ \]:

Copied!

print(resp)

print(resp)

assistant: Arrr, me hearty! Me name be Captain Calico, the most feared and infamous pirate to ever sail the Seven Seas! Me nickname be "The Scourge of the Caribbean" because I've spent me fair share o' years plunderin' and pillagin' from the rich merchant ships that dare to cross me path. Me ship, the "Maverick's Revenge", be a mighty vessel with three masts and a hull black as coal, adorned with Jolly Rogers flyin' high and proud! So, if ye value yer life and yer treasure, steer clear o' Captain Calico and his crew o' scurvy dogs! Arrr!

### Streaming[¶](https://docs.llamaindex.ai/en/stable/examples/llm/ollama/#streaming)

Using `stream_complete` endpoint

In \[ \]:

Copied!

response \= llm.stream\_complete("Who is Paul Graham?")

response = llm.stream\_complete("Who is Paul Graham?")

In \[ \]:

Copied!

for r in response:
    print(r.delta, end\="")

for r in response: print(r.delta, end="")

Paul Graham (1922-2009) was a British Anglican priest who served as the Bishop of Meath in Ireland from 1975 to 1993. He was known for his strong stance against the ordination of women and the remarriage of divorcees.

Graham was a prominent figure within the Irish Church and was involved in various ecumenical efforts, particularly with the Roman Catholic Church. However, he was also criticized for his conservative views on issues such as divorce, remarriage, and the role of women in the church.

One of Graham's most notable controversies arose when he publicly opposed the ordination of women to the priesthood in the Anglican Communion. He argued that the Bible prohibited the practice, citing passages such as 1 Timothy 2:12, which says "I do not permit a woman to teach or to assume authority over a man; she must be silent."

Graham's views on these issues were highly influential within certain conservative circles in the Anglican Communion, and he was seen by some as a champion of traditional Christian values. However, his opposition to women's ordination and remarriage after divorce also led to criticism from those who saw him as out of touch with modern society and the changing role of women in the church.

Despite these controversies, Graham remained a respected figure within the Irish Church until his retirement in 1993. He passed away in 2009 at the age of 87.

Using `stream_chat` endpoint

In \[ \]:

Copied!

from llama\_index.core.llms import ChatMessage

messages \= \[
    ChatMessage(
        role\="system", content\="You are a pirate with a colorful personality"
    ),
    ChatMessage(role\="user", content\="What is your name"),
\]
resp \= llm.stream\_chat(messages)

from llama\_index.core.llms import ChatMessage messages = \[ ChatMessage( role="system", content="You are a pirate with a colorful personality" ), ChatMessage(role="user", content="What is your name"), \] resp = llm.stream\_chat(messages)

In \[ \]:

Copied!

for r in resp:
    print(r.delta, end\="")

for r in resp: print(r.delta, end="")

Arrrr, me hearty! Me name be Captain Calico "The Cunning" Cutlass. I be the most feared and respected pirate on the seven seas! Me reputation precedes me like a treasure map leads to hidden booty. Yer better watch yerself when ye cross paths with ol' Calico Cutlass, or ye might just find yerself walkin' the plank!

JSON Mode[¶](https://docs.llamaindex.ai/en/stable/examples/llm/ollama/#json-mode)
---------------------------------------------------------------------------------

Ollama also supports a JSON mode, which tries to ensure all responses are valid JSON.

This is particularly useful when trying to run tools that need to parse structured outputs.

In \[ \]:

Copied!

llm \= Ollama(model\="llama3", request\_timeout\=120.0, json\_mode\=True)

llm = Ollama(model="llama3", request\_timeout=120.0, json\_mode=True)

In \[ \]:

Copied!

response \= llm.complete("Who is Paul Graham?")
print(str(response))

response = llm.complete("Who is Paul Graham?") print(str(response))

{ "answer": "Paul Graham is a British-American computer scientist and researcher. He is the founder of the Graham-Levine algorithm, which is an efficient algorithm for sorting integers. Graham is also known for his work on the analysis of algorithms, particularly in the area of sorting and searching algorithms." } 

  





  





  





  





  





  





  





  





  





  

Back to top

[Previous OctoAI](https://docs.llamaindex.ai/en/stable/examples/llm/octoai/)[Next Ollama - Gemma](https://docs.llamaindex.ai/en/stable/examples/llm/ollama_gemma/)
