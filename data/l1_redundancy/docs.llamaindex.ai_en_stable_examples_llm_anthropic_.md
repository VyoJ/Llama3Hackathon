Title: Anthropic - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/llm/anthropic/

Markdown Content:
Anthropic - LlamaIndex


Anthropic has recently released its latest models: `Claude 3 Opus`, `Claude 3 Sonnet`, and `Claude 3 Haiku` (which will be available soon). By default, the `claude-2.1 model` is used. This notebook provides guidance on how to utilize these new models.

1.  Claude 3 Opus - claude-3-opus-20240229
2.  Claude 3 Sonnet - claude-3-sonnet-20240229
3.  Claude 3 Haiku - claude-3-haiku-20240307

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-anthropic

%pip install llama-index-llms-anthropic

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

#### Set Tokenizer[¶](https://docs.llamaindex.ai/en/stable/examples/llm/anthropic/#set-tokenizer)

First we want to set the tokenizer, which is slightly different than TikToken.

**NOTE**: The Claude 3 tokenizer has not been updated yet; using the existing Anthropic tokenizer leads to context overflow errors for 200k tokens. We've temporarily set the max tokens for Claude 3 to 180k.

In \[ \]:

Copied!

from llama\_index.llms.anthropic import Anthropic
from llama\_index.core import Settings

tokenizer \= Anthropic().tokenizer
Settings.tokenizer \= tokenizer

from llama\_index.llms.anthropic import Anthropic from llama\_index.core import Settings tokenizer = Anthropic().tokenizer Settings.tokenizer = tokenizer

#### Call `complete` with a prompt[¶](https://docs.llamaindex.ai/en/stable/examples/llm/anthropic/#call-complete-with-a-prompt)

In \[ \]:

Copied!

import os

os.environ\["ANTHROPIC\_API\_KEY"\] \= "YOUR ANTHROPIC API KEY"

import os os.environ\["ANTHROPIC\_API\_KEY"\] = "YOUR ANTHROPIC API KEY"

In \[ \]:

Copied!

from llama\_index.llms.anthropic import Anthropic

\# To customize your API key, do this
\# otherwise it will lookup ANTHROPIC\_API\_KEY from your env variable
\# llm = Anthropic(api\_key="<api\_key>")
llm \= Anthropic(model\="claude-3-opus-20240229")

resp \= llm.complete("Paul Graham is ")

from llama\_index.llms.anthropic import Anthropic # To customize your API key, do this # otherwise it will lookup ANTHROPIC\_API\_KEY from your env variable # llm = Anthropic(api\_key="") llm = Anthropic(model="claude-3-opus-20240229") resp = llm.complete("Paul Graham is ")

In \[ \]:

Copied!

print(resp)

print(resp)

Paul Graham is a well-known entrepreneur, programmer, venture capitalist, and essayist. He is best known for co-founding Viaweb, one of the first web application companies, which was later sold to Yahoo! in 1998 and became Yahoo! Store. Graham is also the co-founder of Y Combinator, a highly successful startup accelerator that has helped launch numerous successful companies, such as Dropbox, Airbnb, and Reddit.

Some key points about Paul Graham:

1. Programming: Graham is a skilled programmer and has written extensively on the subject, including his book "Hackers & Painters: Big Ideas from the Computer Age."

2. Essays: He is a prolific essayist, writing on various topics related to technology, startups, and entrepreneurship. His essays have been influential in the tech startup community.

3. Lisp: Graham is an advocate for the Lisp programming language and has written several essays on its advantages.

4. Y Combinator: As a co-founder of Y Combinator, Graham has played a significant role in shaping the startup ecosystem and has mentored and invested in numerous successful companies.

5. Wealth and inequality: In recent years, Graham has written about income inequality and the concentration of wealth, sparking discussions and debates within the tech community.

Overall, Paul Graham is a significant figure in the technology and startup world, known for his contributions as a programmer, investor, and thought leader.

#### Call `chat` with a list of messages[¶](https://docs.llamaindex.ai/en/stable/examples/llm/anthropic/#call-chat-with-a-list-of-messages)

In \[ \]:

Copied!

from llama\_index.core.llms import ChatMessage
from llama\_index.llms.anthropic import Anthropic

messages \= \[
    ChatMessage(
        role\="system", content\="You are a pirate with a colorful personality"
    ),
    ChatMessage(role\="user", content\="Tell me a story"),
\]
resp \= Anthropic(model\="claude-3-opus-20240229").chat(messages)

from llama\_index.core.llms import ChatMessage from llama\_index.llms.anthropic import Anthropic messages = \[ ChatMessage( role="system", content="You are a pirate with a colorful personality" ), ChatMessage(role="user", content="Tell me a story"), \] resp = Anthropic(model="claude-3-opus-20240229").chat(messages)

In \[ \]:

Copied!

print(resp)

print(resp)

assistant: \*clears throat and speaks in a pirate accent\* Aye, gather 'round me hearties and I'll spin ye a yarn of adventure on the high seas!

T'was a dark and stormy night when the Black Pearl set sail from Tortuga. The salty sea spray stung me eyes as I stood at the helm, guidin' me beloved ship through the roilin' waves. Me loyal crew scurried about, securin' the riggin' and battening down the hatches. 

Suddenly, the lookout cried "Ship ahoy!" and pointed off the starboard bow. I raised me spyglass and spied a Spanish galleon, her decks heavily laden with treasure. The crew gave a hearty cheer - we'd be feastin' and drinkin' well tonight!

I ordered the crew to ready the cannons as we drew alongside the galleon. "Fire all!" I bellowed and the Pearl shook as the guns unleashed a barrage. The Spaniards returned fire but they were no match for me skilled gunners.

We boarded the galleon, swords flashin' and pistols blazin'. The fight was fast and bloody but in the end, the Pearl was victorious! We claimed the treasure as our own - mountains of gold and jewels glintin' in the moonlight.

As we sailed away, I couldn't help but grin. T'was a fine night of piratin' and I knew many more adventures lay ahead for me and me crew. No matter the danger, the Black Pearl would always prevail! Yo ho ho!

\*laughs heartily\* And that, me friends, is a taste of the pirate's life. May yer sails always be full and yer horizons bright. Fare thee well!

Streaming[¶](https://docs.llamaindex.ai/en/stable/examples/llm/anthropic/#streaming)
------------------------------------------------------------------------------------

Using `stream_complete` endpoint

In \[ \]:

Copied!

from llama\_index.llms.anthropic import Anthropic

llm \= Anthropic(model\="claude-3-opus-20240229", max\_tokens\=100)
resp \= llm.stream\_complete("Paul Graham is ")

from llama\_index.llms.anthropic import Anthropic llm = Anthropic(model="claude-3-opus-20240229", max\_tokens=100) resp = llm.stream\_complete("Paul Graham is ")

In \[ \]:

Copied!

for r in resp:
    print(r.delta, end\="")

for r in resp: print(r.delta, end="")

Paul Graham is a well-known entrepreneur, programmer, venture capitalist, and essayist. He is best known for co-founding Viaweb, one of the first web application companies, which was later sold to Yahoo! in 1998 and became Yahoo! Store. 

After the sale of Viaweb, Graham and his wife Jessica Livingston co-founded Y Combinator in 2005, a highly successful startup accelerator that has helped launch

In \[ \]:

Copied!

from llama\_index.llms.anthropic import Anthropic

llm \= Anthropic(model\="claude-3-opus-20240229")
messages \= \[
    ChatMessage(
        role\="system", content\="You are a pirate with a colorful personality"
    ),
    ChatMessage(role\="user", content\="Tell me a story"),
\]
resp \= llm.stream\_chat(messages)

from llama\_index.llms.anthropic import Anthropic llm = Anthropic(model="claude-3-opus-20240229") messages = \[ ChatMessage( role="system", content="You are a pirate with a colorful personality" ), ChatMessage(role="user", content="Tell me a story"), \] resp = llm.stream\_chat(messages)

In \[ \]:

Copied!

for r in resp:
    print(r.delta, end\="")

for r in resp: print(r.delta, end="")

\*clears throat and speaks in a gruff, piratey voice\* 

Aye, gather 'round me hearties and I'll spin ye a yarn of adventure on the high seas! 

'Twas a dark and stormy night, the kind where the wind howls like a banshee and the waves crash over the deck. Me and me crew were sailin' the Caribbean, searchin' for treasure and glory.

Suddenly, the lookout cried "Ship ahoy!" and sure enough, a Spanish galleon was bearin' down on us, her decks bristlin' with cannons. The scurvy dogs wanted our gold, but I'd sooner walk the plank than surrender!

"All hands to battle stations!" I bellowed. "Ready the cannons and prepare to board!" 

A mighty battle erupted, cannons boomin' and swords clashin'. We swung over on ropes and fought the Spaniards hand-to-hand on the pitchin' and rollin' deck. Me cutlass was a blur as I dueled their captain, a big brute with a wicked scar.

Finally, I drove me blade into that bilge rat's black heart and he fell dead at me feet. His crew surrendered and we took their ship as a prize. In the hold, we found chests overflowing with gold doubloons and jewels - a king's ransom! 

We sailed off into the sunset, our pirate flag snappin' in the breeze, flush with coin and the thrill of victory. And that, me buckos, is a taste of the pirate life! Now who wants some grog?

\*laughs heartily\*

Configure Model[¶](https://docs.llamaindex.ai/en/stable/examples/llm/anthropic/#configure-model)
------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.llms.anthropic import Anthropic

llm \= Anthropic(model\="claude-3-sonnet-20240229")

from llama\_index.llms.anthropic import Anthropic llm = Anthropic(model="claude-3-sonnet-20240229")

In \[ \]:

Copied!

resp \= llm.stream\_complete("Paul Graham is ")

resp = llm.stream\_complete("Paul Graham is ")

In \[ \]:

Copied!

for r in resp:
    print(r.delta, end\="")

for r in resp: print(r.delta, end="")

Paul Graham is a computer scientist, entrepreneur, venture capitalist, and author. He is best known for the following:

1. Co-founding Y Combinator: Y Combinator is a prominent startup accelerator based in Silicon Valley. It has funded and helped launch thousands of startups, including Airbnb, Dropbox, Stripe, and Reddit.

2. Writing essays on startups and technology: Graham has written numerous influential essays on topics related to startups, programming, and entrepreneurship. His essays are widely read and have helped shape the thinking of many entrepreneurs and technologists.

3. Developing the programming language Arc: In the early 2000s, Graham developed a new programming language called Arc, which was designed to be a more powerful and expressive dialect of Lisp.

4. Advocating for the use of Lisp and functional programming: Graham is a strong proponent of the Lisp programming language and functional programming paradigms. He has written extensively about the benefits of these approaches and has influenced many programmers to explore them.

5. Authoring books: Graham has authored several books, including "Hackers & Painters: Big Ideas from the Computer Age" (2004), "On Lisp" (1993), and "ANSI Common Lisp" (1995).

6. Investing in startups: Through Y Combinator and his own investments, Graham has invested in and advised numerous successful startups, helping to shape the technology industry.

Overall, Paul Graham is widely respected in the technology and startup communities for his contributions as a programmer, writer, investor, and advocate for innovative ideas and approaches.

Async[¶](https://docs.llamaindex.ai/en/stable/examples/llm/anthropic/#async)
----------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.llms.anthropic import Anthropic

llm \= Anthropic("claude-3-sonnet-20240229")
resp \= await llm.acomplete("Paul Graham is ")

from llama\_index.llms.anthropic import Anthropic llm = Anthropic("claude-3-sonnet-20240229") resp = await llm.acomplete("Paul Graham is ")

In \[ \]:

Copied!

print(resp)

print(resp)

Paul Graham is a computer scientist, entrepreneur, venture capitalist, and author. He is best known for the following:

1. Co-founding Y Combinator: Y Combinator is a prominent startup accelerator based in Silicon Valley. It has funded and helped launch many successful startups, including Airbnb, Dropbox, Stripe, and Reddit.

2. Writing essays on startups and technology: Graham has written numerous influential essays on topics related to startups, programming, and entrepreneurship. His essays are widely read and have helped shape the thinking of many entrepreneurs and technologists.

3. Developing the programming language Arc: Graham designed and developed the programming language Arc, which was intended to be a more powerful and expressive dialect of Lisp.

4. Authoring books: He has written several books, including "Hackers & Painters: Big Ideas from the Computer Age," "ANSI Common Lisp," and "On Lisp."

5. Founding Viaweb: In the 1990s, Graham co-founded Viaweb, one of the earliest web-based application software companies. Viaweb was later acquired by Yahoo! in 1998.

Graham is widely respected in the technology and startup communities for his insights, writings, and contributions to the field of computer science and entrepreneurship.

Back to top

[Previous Aleph Alpha](https://docs.llamaindex.ai/en/stable/examples/llm/alephalpha/)[Next Anyscale](https://docs.llamaindex.ai/en/stable/examples/llm/anyscale/)
