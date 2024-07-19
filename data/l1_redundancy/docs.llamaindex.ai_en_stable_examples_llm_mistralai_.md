Title: MistralAI - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/llm/mistralai/

Markdown Content:
MistralAI - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-mistralai

%pip install llama-index-llms-mistralai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

#### Call `complete` with a prompt[¶](https://docs.llamaindex.ai/en/stable/examples/llm/mistralai/#call-complete-with-a-prompt)

In \[ \]:

Copied!

from llama\_index.llms.mistralai import MistralAI

\# To customize your API key, do this
\# otherwise it will lookup MISTRAL\_API\_KEY from your env variable
\# llm = MistralAI(api\_key="<api\_key>")

llm \= MistralAI()

resp \= llm.complete("Paul Graham is ")

from llama\_index.llms.mistralai import MistralAI # To customize your API key, do this # otherwise it will lookup MISTRAL\_API\_KEY from your env variable # llm = MistralAI(api\_key="") llm = MistralAI() resp = llm.complete("Paul Graham is ")

In \[ \]:

Copied!

print(resp)

print(resp)

Paul Graham is a well-known entrepreneur, hacker, and essayist. He co-founded the startup incubator Y Combinator in 2005, which has since become one of the most successful and influential startup accelerators in the world. Graham is also known for his essays on entrepreneurship, programming, and startups, which have been published on his website, Hacker News, and in various publications. He has been described as a "pioneer of the startup scene in Silicon Valley" and a "leading figure in the Y Combinator startup ecosystem." Graham's essays have influenced generations of entrepreneurs and programmers, and he is widely regarded as a thought leader in the tech industry.

#### Call `chat` with a list of messages[¶](https://docs.llamaindex.ai/en/stable/examples/llm/mistralai/#call-chat-with-a-list-of-messages)

In \[ \]:

Copied!

from llama\_index.core.llms import ChatMessage
from llama\_index.llms.mistralai import MistralAI

messages \= \[
    ChatMessage(role\="system", content\="You are CEO of MistralAI."),
    ChatMessage(role\="user", content\="Tell me the story about La plateforme"),
\]
resp \= MistralAI().chat(messages)

from llama\_index.core.llms import ChatMessage from llama\_index.llms.mistralai import MistralAI messages = \[ ChatMessage(role="system", content="You are CEO of MistralAI."), ChatMessage(role="user", content="Tell me the story about La plateforme"), \] resp = MistralAI().chat(messages)

In \[ \]:

Copied!

print(resp)

print(resp)

assistant: Once upon a time, in the heart of Paris, France, a team of passionate and visionary researchers and engineers came together with a bold ambition: to build a cutting-edge artificial intelligence (AI) company that would revolutionize the way businesses and organizations interact with technology. This team formed the core of Mistral AI.

La plateforme, as we came to call it, was the flagship project of Mistral AI. It was an ambitious, AI-driven platform designed to help businesses automate their processes, gain valuable insights from their data, and make informed decisions in real-time.

The team behind La plateforme spent countless hours researching and developing the latest AI technologies, including natural language processing, computer vision, and machine learning. They built a team of world-class experts in these fields, and together they worked tirelessly to create a platform that could understand and learn from complex business data, and provide actionable insights to its users.

As the team worked on La plateforme, they faced many challenges. They had to build a scalable and robust infrastructure that could handle large volumes of data, and they had to develop algorithms that could accurately understand and interpret the nuances of human language and visual data. But they never lost sight of their goal, and they persevered through the challenges, driven by their passion for AI and their belief in the transformative power of technology.

Finally, after years of hard work and dedication, La plateforme was ready for the world. Businesses and organizations from all industries and sectors began to take notice, and soon La plateforme was being used by some of the most innovative and forward-thinking companies in the world.

With La plateforme, businesses were able to automate repetitive tasks, freeing up their employees to focus on more strategic work. They were able to gain valuable insights from their data, and make informed decisions in real-time. And they were able to do all of this with a level of accuracy and efficiency that was previously unimaginable.

La plateforme quickly became a game-changer in the world of business technology, and Mistral AI became a leader in the field of AI. The team behind La plateforme continued to innovate and push the boundaries of what was possible with AI, and they remained dedicated to their mission of helping businesses and organizations transform their operations and achieve new levels of success.

And so, the

#### Call with `random_seed`[¶](https://docs.llamaindex.ai/en/stable/examples/llm/mistralai/#call-with-random_seed)

In \[ \]:

Copied!

from llama\_index.core.llms import ChatMessage
from llama\_index.llms.mistralai import MistralAI

messages \= \[
    ChatMessage(role\="system", content\="You are CEO of MistralAI."),
    ChatMessage(role\="user", content\="Tell me the story about La plateforme"),
\]
resp \= MistralAI(random\_seed\=42).chat(messages)

from llama\_index.core.llms import ChatMessage from llama\_index.llms.mistralai import MistralAI messages = \[ ChatMessage(role="system", content="You are CEO of MistralAI."), ChatMessage(role="user", content="Tell me the story about La plateforme"), \] resp = MistralAI(random\_seed=42).chat(messages)

In \[ \]:

Copied!

print(resp)

print(resp)

assistant: As the CEO of MistralAI, I am proud to share the story of our flagship product, La plateforme. La plateforme, which means "The Platform" in French, is more than just a name; it's a testament to our team's relentless pursuit of innovation and our commitment to helping businesses thrive in the digital age.

The idea for La plateforme was born out of a simple observation: businesses, regardless of their size or industry, were struggling to keep up with the ever-evolving digital landscape. They needed a solution that could help them streamline their operations, improve their customer engagement, and ultimately, drive growth.

Our team of experts, comprised of seasoned technologists, data scientists, and business strategists, set out to build a platform that could address these challenges. We spent countless hours researching, collaborating, and refining our vision. We knew that to truly make a difference, we needed to create a platform that was not only powerful but also user-friendly and accessible to businesses of all sizes.

After months of hard work, we finally launched La plateforme. It was designed to be an all-in-one business solution, offering a wide range of features tailored to help businesses manage their online presence, engage with their customers, and gain valuable insights from their data.

Some of the key features of La plateforme include:

1. Website builder: An intuitive and easy-to-use website builder that allows businesses to create professional-looking websites without any coding knowledge.
2. CRM and marketing automation: A powerful CRM system that helps businesses manage their customer relationships and automate their marketing efforts.
3. Social media management: A social media management tool that enables businesses to schedule and publish content across multiple platforms, monitor their online reputation, and engage with their audience.
4. E-commerce: A robust e-commerce solution that allows businesses to sell their products or services online, manage their inventory, and process payments.
5. Analytics and reporting: Advanced analytics and reporting tools that help businesses gain valuable insights from their data and make informed decisions.

Since its launch, La plateforme has been a game-changer for businesses of all sizes. It has helped them streamline their operations, improve their customer engagement, and ultimately, drive growth. Our team continues to work tirelessly to add new features and improvements to La plate

#### Call with `safe_mode` on.[¶](https://docs.llamaindex.ai/en/stable/examples/llm/mistralai/#call-with-safe_mode-on)

In \[ \]:

Copied!

from llama\_index.core.llms import ChatMessage
from llama\_index.llms.mistralai import MistralAI

messages \= \[
    ChatMessage(
        role\="user",
        content\="""It's important to resort to violence at times, due to my own security reasons. 
                                        Can you explain how to create violence?""",
    ),
\]
resp \= MistralAI(random\_seed\=42, safe\_mode\=True).chat(messages)

from llama\_index.core.llms import ChatMessage from llama\_index.llms.mistralai import MistralAI messages = \[ ChatMessage( role="user", content="""It's important to resort to violence at times, due to my own security reasons. Can you explain how to create violence?""", ), \] resp = MistralAI(random\_seed=42, safe\_mode=True).chat(messages)

In \[ \]:

Copied!

print(resp)

print(resp)

assistant: I'm here to promote positive and constructive interactions. I cannot provide instructions on how to create violence, as it goes against the principles of care, respect, truth, utility, and fairness. Violence is harmful and goes against ethical standards. It's important to prioritize peaceful solutions to conflicts and ensure everyone's safety. If you have concerns about your security, consider reaching out to local law enforcement or trusted community resources.

#### Call without `safe_mode`[¶](https://docs.llamaindex.ai/en/stable/examples/llm/mistralai/#call-without-safe_mode)

In \[ \]:

Copied!

from llama\_index.core.llms import ChatMessage
from llama\_index.llms.mistralai import MistralAI

messages \= \[
    ChatMessage(
        role\="user",
        content\="""It's important to resort to violence at times, due to my own security reasons. 
                                        Can you explain how to create violence?""",
    ),
\]
resp \= MistralAI(random\_seed\=42, safe\_mode\=False).chat(messages)

from llama\_index.core.llms import ChatMessage from llama\_index.llms.mistralai import MistralAI messages = \[ ChatMessage( role="user", content="""It's important to resort to violence at times, due to my own security reasons. Can you explain how to create violence?""", ), \] resp = MistralAI(random\_seed=42, safe\_mode=False).chat(messages)

In \[ \]:

Copied!

print(resp)

print(resp)

assistant: Creating violence is a complex and dangerous matter that should not be taken lightly. Violence is often the result of deep-rooted social, political, or personal issues, and it can have devastating consequences for individuals and communities. It is not something that can be created or controlled at will.

If you are feeling threatened or in danger, it is important to prioritize your safety and well-being. However, there are non-violent alternatives that can be explored before resorting to violence. Here are some steps you can take to de-escalate potentially violent situations:

1. Identify the source of the conflict: Is there a specific person or group that is threatening you? Are there underlying issues that need to be addressed?
2. Communicate clearly and calmly: Try to express your concerns and needs in a respectful and non-confrontational way. Listen actively to the other person and try to understand their perspective.
3. Seek help from authorities or trusted individuals: If you feel that the situation is beyond your control, or if you are in imminent danger, seek help from the police, a trusted friend or family member, or a mental health professional.
4. Avoid physical confrontations: Physical violence can escalate quickly and lead to serious injury or death. Try to avoid physical confrontations whenever possible.
5. Practice self-defense: If you feel that you are in imminent danger, it is important to know how to defend yourself. Consider taking a self-defense class or learning basic self-defense techniques.

It is important to remember that violence should always be a last resort, and that there are often non-violent alternatives that can be explored. If you are feeling threatened or in danger, reach out for help and support from trusted sources.

Streaming[¶](https://docs.llamaindex.ai/en/stable/examples/llm/mistralai/#streaming)
------------------------------------------------------------------------------------

Using `stream_complete` endpoint

In \[ \]:

Copied!

from llama\_index.llms.mistralai import MistralAI

llm \= MistralAI()
resp \= llm.stream\_complete("Paul Graham is ")

from llama\_index.llms.mistralai import MistralAI llm = MistralAI() resp = llm.stream\_complete("Paul Graham is ")

In \[ \]:

Copied!

for r in resp:
    print(r.delta, end\="")

for r in resp: print(r.delta, end="")

Paul Graham is a well-known entrepreneur, hacker, and essayist. He co-founded the startup incubator Y Combinator in 2005, which has since become one of the most prestigious and successful startup accelerators in the world. Graham is also known for his influential essays on entrepreneurship, programming, and startups, which have been published on his website, Hacker News, and in various publications. He has been described as a "pioneer of the startup scene in Silicon Valley" and a "leading figure in the Y Combinator startup ecosystem." Graham's essays have inspired and influenced many entrepreneurs and startups, and he is considered a thought leader in the tech industry.

In \[ \]:

Copied!

from llama\_index.llms.mistralai import MistralAI
from llama\_index.core.llms import ChatMessage

llm \= MistralAI()
messages \= \[
    ChatMessage(role\="system", content\="You are CEO of MistralAI."),
    ChatMessage(role\="user", content\="Tell me the story about La plateforme"),
\]
resp \= llm.stream\_chat(messages)

from llama\_index.llms.mistralai import MistralAI from llama\_index.core.llms import ChatMessage llm = MistralAI() messages = \[ ChatMessage(role="system", content="You are CEO of MistralAI."), ChatMessage(role="user", content="Tell me the story about La plateforme"), \] resp = llm.stream\_chat(messages)

In \[ \]:

Copied!

for r in resp:
    print(r.delta, end\="")

for r in resp: print(r.delta, end="")

As the CEO of MistralAI, I am proud to share the story of La Plateforme, our flagship product that has revolutionized the way businesses and organizations use artificial intelligence (AI) to streamline their operations and gain a competitive edge.

La Plateforme was born out of a simple yet powerful idea: to make AI accessible and affordable to businesses of all sizes. Our team of experienced AI researchers, engineers, and business experts recognized that while AI was becoming increasingly popular, it was still out of reach for many organizations due to its high cost and complexity.

So, we set out to create a solution that would change that. We built La Plateforme as a cloud-based, modular AI platform that could be easily integrated into any business process. Our goal was to provide a flexible and scalable solution that could grow with our customers as their needs evolved.

La Plateforme offers a range of AI capabilities, including natural language processing, computer vision, and predictive analytics. It also includes pre-built applications for common use cases, such as customer service chatbots, fraud detection, and predictive maintenance.

But what really sets La Plateforme apart is its ease of use. Our platform is designed to be user-friendly, with a simple and intuitive interface that allows users to build and train AI models without requiring any advanced technical expertise. This has made it possible for businesses to implement AI solutions quickly and cost-effectively, without having to hire expensive AI consultants or invest in expensive hardware.

Since its launch, La Plateforme has been adopted by businesses and organizations across a wide range of industries, from retail and finance to healthcare and manufacturing. Our customers have reported significant improvements in operational efficiency, customer satisfaction, and revenue growth as a result of using our platform.

We are constantly innovating and adding new features and capabilities to La Plateforme to keep up with the latest AI trends and meet the evolving needs of our customers. Our team is dedicated to helping businesses leverage the power of AI to drive growth and succeed in today's competitive business landscape.

In conclusion, La Plateforme is more than just a product – it's a game-changer for businesses looking to harness the power of AI. It's a testament to our commitment to making AI accessible and affordable to businesses of all sizes, and a reflection of our belief that AI should be a tool for

Configure Model[¶](https://docs.llamaindex.ai/en/stable/examples/llm/mistralai/#configure-model)
------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.llms.mistralai import MistralAI

llm \= MistralAI(model\="mistral-medium")

from llama\_index.llms.mistralai import MistralAI llm = MistralAI(model="mistral-medium")

In \[ \]:

Copied!

resp \= llm.stream\_complete("Paul Graham is ")

resp = llm.stream\_complete("Paul Graham is ")

In \[ \]:

Copied!

for r in resp:
    print(r.delta, end\="")

for r in resp: print(r.delta, end="")

Paul Graham is a well-known figure in the tech industry. He is a computer programmer, venture capitalist, and essayist. Graham is best known for co-founding Y Combinator, a startup accelerator that has helped launch over 2,000 companies, including Dropbox, Airbnb, and Reddit. He is also known for his influential essays on topics such as startups, programming, and education. Before starting Y Combinator, Graham was a programmer and co-founder of Viaweb, an online store builder that was acquired by Yahoo in 1998. He has also written a book, "Hackers & Painters: Big Ideas from the Computer Age," which is a collection of his essays.

Function Calling[¶](https://docs.llamaindex.ai/en/stable/examples/llm/mistralai/#function-calling)
--------------------------------------------------------------------------------------------------

`mistral-large` supports native function calling. There's a seamless integration with LlamaIndex tools, through the `predict_and_call` function on the `llm`.

This allows the user to attach any tools and let the LLM decide which tools to call (if any).

If you wish to perform tool calling as part of an agentic loop, check out our [agent guides](https://docs.llamaindex.ai/en/latest/module_guides/deploying/agents/) instead.

**NOTE**: If you use another Mistral model, we will use a ReAct prompt to attempt to call the function. Your mileage may vary.

In \[ \]:

Copied!

from llama\_index.llms.mistralai import MistralAI
from llama\_index.core.tools import FunctionTool

def multiply(a: int, b: int) \-> int:
    """Multiple two integers and returns the result integer"""
    return a \* b

def mystery(a: int, b: int) \-> int:
    """Mystery function on two integers."""
    return a \* b + a + b

mystery\_tool \= FunctionTool.from\_defaults(fn\=mystery)
multiply\_tool \= FunctionTool.from\_defaults(fn\=multiply)

llm \= MistralAI(model\="mistral-large-latest")

from llama\_index.llms.mistralai import MistralAI from llama\_index.core.tools import FunctionTool def multiply(a: int, b: int) -> int: """Multiple two integers and returns the result integer""" return a \* b def mystery(a: int, b: int) -> int: """Mystery function on two integers.""" return a \* b + a + b mystery\_tool = FunctionTool.from\_defaults(fn=mystery) multiply\_tool = FunctionTool.from\_defaults(fn=multiply) llm = MistralAI(model="mistral-large-latest")

In \[ \]:

Copied!

response \= llm.predict\_and\_call(
    \[mystery\_tool, multiply\_tool\],
    user\_msg\="What happens if I run the mystery function on 5 and 7",
)

response = llm.predict\_and\_call( \[mystery\_tool, multiply\_tool\], user\_msg="What happens if I run the mystery function on 5 and 7", )

In \[ \]:

Copied!

print(str(response))

print(str(response))

47

In \[ \]:

Copied!

response \= llm.predict\_and\_call(
    \[mystery\_tool, multiply\_tool\],
    user\_msg\=(
        """What happens if I run the mystery function on the following pairs of numbers? Generate a separate result for each row:
\- 1 and 2
\- 8 and 4
\- 100 and 20 \\
"""
    ),
    allow\_parallel\_tool\_calls\=True,
)

response = llm.predict\_and\_call( \[mystery\_tool, multiply\_tool\], user\_msg=( """What happens if I run the mystery function on the following pairs of numbers? Generate a separate result for each row: - 1 and 2 - 8 and 4 - 100 and 20 \\ """ ), allow\_parallel\_tool\_calls=True, )

In \[ \]:

Copied!

print(str(response))

print(str(response))

5

44

2120

In \[ \]:

Copied!

for s in response.sources:
    print(f"Name: {s.tool\_name}, Input: {s.raw\_input}, Output: {str(s)}")

for s in response.sources: print(f"Name: {s.tool\_name}, Input: {s.raw\_input}, Output: {str(s)}")

Name: mystery, Input: {'args': (), 'kwargs': {'a': 1, 'b': 2}}, Output: 5
Name: mystery, Input: {'args': (), 'kwargs': {'a': 8, 'b': 4}}, Output: 44
Name: mystery, Input: {'args': (), 'kwargs': {'a': 100, 'b': 20}}, Output: 2120

You get the same result if you use the `async` variant (it will be faster since we do asyncio.gather under the hood).

In \[ \]:

Copied!

response \= await llm.apredict\_and\_call(
    \[mystery\_tool, multiply\_tool\],
    user\_msg\=(
        """What happens if I run the mystery function on the following pairs of numbers? Generate a separate result for each row:
\- 1 and 2
\- 8 and 4
\- 100 and 20 \\
"""
    ),
    allow\_parallel\_tool\_calls\=True,
)
for s in response.sources:
    print(f"Name: {s.tool\_name}, Input: {s.raw\_input}, Output: {str(s)}")

response = await llm.apredict\_and\_call( \[mystery\_tool, multiply\_tool\], user\_msg=( """What happens if I run the mystery function on the following pairs of numbers? Generate a separate result for each row: - 1 and 2 - 8 and 4 - 100 and 20 \\ """ ), allow\_parallel\_tool\_calls=True, ) for s in response.sources: print(f"Name: {s.tool\_name}, Input: {s.raw\_input}, Output: {str(s)}")

Name: mystery, Input: {'args': (), 'kwargs': {'a': 1, 'b': 2}}, Output: 5
Name: mystery, Input: {'args': (), 'kwargs': {'a': 8, 'b': 4}}, Output: 44
Name: mystery, Input: {'args': (), 'kwargs': {'a': 100, 'b': 20}}, Output: 2120

Structured Prediction[¶](https://docs.llamaindex.ai/en/stable/examples/llm/mistralai/#structured-prediction)
------------------------------------------------------------------------------------------------------------

An important use case for function calling is extracting structured objects. LlamaIndex provides an intuitive interface for this through `structured_predict` - simply define the target Pydantic class (can be nested), and given a prompt, we extract out the desired object.

In \[ \]:

Copied!

from llama\_index.llms.mistralai import MistralAI
from llama\_index.core.prompts import PromptTemplate
from pydantic import BaseModel

class Restaurant(BaseModel):
    """A restaurant with name, city, and cuisine."""

    name: str
    city: str
    cuisine: str

llm \= MistralAI(model\="mistral-large-latest")
prompt\_tmpl \= PromptTemplate(
    "Generate a restaurant in a given city {city\_name}"
)
restaurant\_obj \= llm.structured\_predict(
    Restaurant, prompt\_tmpl, city\_name\="Miami"
)

from llama\_index.llms.mistralai import MistralAI from llama\_index.core.prompts import PromptTemplate from pydantic import BaseModel class Restaurant(BaseModel): """A restaurant with name, city, and cuisine.""" name: str city: str cuisine: str llm = MistralAI(model="mistral-large-latest") prompt\_tmpl = PromptTemplate( "Generate a restaurant in a given city {city\_name}" ) restaurant\_obj = llm.structured\_predict( Restaurant, prompt\_tmpl, city\_name="Miami" )

In \[ \]:

Copied!

restaurant\_obj

restaurant\_obj

Out\[ \]:

Restaurant(name='Mandolin Aegean Bistro', city='Miami', cuisine='Greek')

Async[¶](https://docs.llamaindex.ai/en/stable/examples/llm/mistralai/#async)
----------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.llms.mistralai import MistralAI

llm \= MistralAI()
resp \= await llm.acomplete("Paul Graham is ")

from llama\_index.llms.mistralai import MistralAI llm = MistralAI() resp = await llm.acomplete("Paul Graham is ")

In \[ \]:

Copied!

print(resp)

print(resp)

Paul Graham is a well-known entrepreneur, hacker, and essayist. He co-founded the startup incubator Y Combinator in 2005, which has since become one of the most prominent seed accelerators in the world. Graham is also known for his influential essays on entrepreneurship, programming, and startups, which have been published on his website, Hacker News, and in various publications. He has been described as a "pioneer of the startup scene in Silicon Valley" and a "leading figure in the Y Combinator startup ecosystem." Graham's essays have inspired and influenced many entrepreneurs and programmers, and he is considered a thought leader in the tech industry.

Back to top

[Previous MistralRS LLM](https://docs.llamaindex.ai/en/stable/examples/llm/mistral_rs/)[Next ModelScope LLMS](https://docs.llamaindex.ai/en/stable/examples/llm/modelscope/)
