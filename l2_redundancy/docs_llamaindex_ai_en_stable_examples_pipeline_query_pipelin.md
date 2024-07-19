Title: An Introduction to LlamaIndex Query Pipelines

URL Source: https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/

Markdown Content:
An Introduction to LlamaIndex Query Pipelines - LlamaIndex


Overview[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#overview)
--------------------------------------------------------------------------------------------

LlamaIndex provides a declarative query API that allows you to chain together different modules in order to orchestrate simple-to-advanced workflows over your data.

This is centered around our `QueryPipeline` abstraction. Load in a variety of modules (from LLMs to prompts to retrievers to other pipelines), connect them all together into a sequential chain or DAG, and run it end2end.

**NOTE**: You can orchestrate all these workflows without the declarative pipeline abstraction (by using the modules imperatively and writing your own functions). So what are the advantages of `QueryPipeline`?

*   Express common workflows with fewer lines of code/boilerplate
*   Greater readability
*   Greater parity / better integration points with common low-code / no-code solutions (e.g. LangFlow)
*   \[In the future\] A declarative interface allows easy serializability of pipeline components, providing portability of pipelines/easier deployment to different systems.

Cookbook[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#cookbook)
--------------------------------------------------------------------------------------------

In this cookbook we give you an introduction to our `QueryPipeline` interface and show you some basic workflows you can tackle.

*   Chain together prompt and LLM
*   Chain together query rewriting (prompt + LLM) with retrieval
*   Chain together a full RAG query pipeline (query rewriting, retrieval, reranking, response synthesis)
*   Setting up a custom query component
*   Executing a pipeline step-by-step

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#setup)
--------------------------------------------------------------------------------------

Here we setup some data + indexes (from PG's essay) that we'll be using in the rest of the cookbook.

In \[ \]:

Copied!

%pip install llama\-index\-embeddings\-openai
%pip install llama\-index\-postprocessor\-cohere\-rerank
%pip install llama\-index\-llms\-openai

%pip install llama-index-embeddings-openai %pip install llama-index-postprocessor-cohere-rerank %pip install llama-index-llms-openai

In \[ \]:

Copied!

\# setup Arize Phoenix for logging/observability
import phoenix as px

px.launch\_app()
import llama\_index.core

llama\_index.core.set\_global\_handler("arize\_phoenix")

\# setup Arize Phoenix for logging/observability import phoenix as px px.launch\_app() import llama\_index.core llama\_index.core.set\_global\_handler("arize\_phoenix")

🌍 To view the Phoenix app in your browser, visit http://127.0.0.1:6006/
📺 To view the Phoenix app in a notebook, run \`px.active\_session().view()\`
📖 For more information on how to use Phoenix, check out https://docs.arize.com/phoenix

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..."

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI
from llama\_index.embeddings.openai import OpenAIEmbedding
from llama\_index.core import Settings

Settings.llm \= OpenAI(model\="gpt-3.5-turbo")
Settings.embed\_model \= OpenAIEmbedding(model\="text-embedding-3-small")

from llama\_index.llms.openai import OpenAI from llama\_index.embeddings.openai import OpenAIEmbedding from llama\_index.core import Settings Settings.llm = OpenAI(model="gpt-3.5-turbo") Settings.embed\_model = OpenAIEmbedding(model="text-embedding-3-small")

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

reader \= SimpleDirectoryReader("../data/paul\_graham")

from llama\_index.core import SimpleDirectoryReader reader = SimpleDirectoryReader("../data/paul\_graham")

In \[ \]:

Copied!

docs \= reader.load\_data()

docs = reader.load\_data()

In \[ \]:

Copied!

import os
from llama\_index.core import (
    StorageContext,
    VectorStoreIndex,
    load\_index\_from\_storage,
)

if not os.path.exists("storage"):
    index \= VectorStoreIndex.from\_documents(docs)
    \# save index to disk
    index.set\_index\_id("vector\_index")
    index.storage\_context.persist("./storage")
else:
    \# rebuild storage context
    storage\_context \= StorageContext.from\_defaults(persist\_dir\="storage")
    \# load index
    index \= load\_index\_from\_storage(storage\_context, index\_id\="vector\_index")

import os from llama\_index.core import ( StorageContext, VectorStoreIndex, load\_index\_from\_storage, ) if not os.path.exists("storage"): index = VectorStoreIndex.from\_documents(docs) # save index to disk index.set\_index\_id("vector\_index") index.storage\_context.persist("./storage") else: # rebuild storage context storage\_context = StorageContext.from\_defaults(persist\_dir="storage") # load index index = load\_index\_from\_storage(storage\_context, index\_id="vector\_index")

1\. Chain Together Prompt and LLM[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#1-chain-together-prompt-and-llm)
--------------------------------------------------------------------------------------------------------------------------------------------

In this section we show a super simple workflow of chaining together a prompt with LLM.

We simply define `chain` on initialization. This is a special case of a query pipeline where the components are purely sequential, and we automatically convert outputs into the right format for the next inputs.

In \[ \]:

Copied!

from llama\_index.core.query\_pipeline import QueryPipeline
from llama\_index.core import PromptTemplate

\# try chaining basic prompts
prompt\_str \= "Please generate related movies to {movie\_name}"
prompt\_tmpl \= PromptTemplate(prompt\_str)
llm \= OpenAI(model\="gpt-3.5-turbo")

p \= QueryPipeline(chain\=\[prompt\_tmpl, llm\], verbose\=True)

from llama\_index.core.query\_pipeline import QueryPipeline from llama\_index.core import PromptTemplate # try chaining basic prompts prompt\_str = "Please generate related movies to {movie\_name}" prompt\_tmpl = PromptTemplate(prompt\_str) llm = OpenAI(model="gpt-3.5-turbo") p = QueryPipeline(chain=\[prompt\_tmpl, llm\], verbose=True)

In \[ \]:

Copied!

output \= p.run(movie\_name\="The Departed")

output = p.run(movie\_name="The Departed")

\> Running module 8dc57d24-9691-4d8d-87d7-151865a7cd1b with input: 
movie\_name: The Departed

\> Running module 7ed9e26c-a704-4b0b-9cfd-991266e754c0 with input: 
messages: Please generate related movies to The Departed

In \[ \]:

Copied!

print(str(output))

print(str(output))

assistant: 1. Infernal Affairs (2002) - The original Hong Kong film that inspired The Departed
2. The Town (2010) - A crime thriller directed by and starring Ben Affleck
3. Mystic River (2003) - A crime drama directed by Clint Eastwood
4. Goodfellas (1990) - A classic mobster film directed by Martin Scorsese
5. The Irishman (2019) - Another crime drama directed by Martin Scorsese, starring Robert De Niro and Al Pacino
6. The Departed (2006) - The Departed is a 2006 American crime film directed by Martin Scorsese and written by William Monahan. It is a remake of the 2002 Hong Kong film Infernal Affairs. The film stars Leonardo DiCaprio, Matt Damon, Jack Nicholson, and Mark Wahlberg, with Martin Sheen, Ray Winstone, Vera Farmiga, and Alec Baldwin in supporting roles.

### View Intermediate Inputs/Outputs[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#view-intermediate-inputsoutputs)

For debugging and other purposes, we can also view the inputs and outputs at each step.

In \[ \]:

Copied!

output, intermediates \= p.run\_with\_intermediates(movie\_name\="The Departed")

output, intermediates = p.run\_with\_intermediates(movie\_name="The Departed")

\> Running module 8dc57d24-9691-4d8d-87d7-151865a7cd1b with input: 
movie\_name: The Departed

\> Running module 7ed9e26c-a704-4b0b-9cfd-991266e754c0 with input: 
messages: Please generate related movies to The Departed

In \[ \]:

Copied!

intermediates\["8dc57d24-9691-4d8d-87d7-151865a7cd1b"\]

intermediates\["8dc57d24-9691-4d8d-87d7-151865a7cd1b"\]

Out\[ \]:

ComponentIntermediates(inputs={'movie\_name': 'The Departed'}, outputs={'prompt': 'Please generate related movies to The Departed'})

In \[ \]:

Copied!

intermediates\["7ed9e26c-a704-4b0b-9cfd-991266e754c0"\]

intermediates\["7ed9e26c-a704-4b0b-9cfd-991266e754c0"\]

Out\[ \]:

ComponentIntermediates(inputs={'messages': 'Please generate related movies to The Departed'}, outputs={'output': ChatResponse(message=ChatMessage(role=<MessageRole.ASSISTANT: 'assistant'>, content='1. Infernal Affairs (2002) - The original Hong Kong film that inspired The Departed\\n2. The Town (2010) - A crime thriller directed by Ben Affleck\\n3. Mystic River (2003) - A crime drama directed by Clint Eastwood\\n4. Goodfellas (1990) - A classic crime film directed by Martin Scorsese\\n5. The Irishman (2019) - Another crime film directed by Martin Scorsese, starring Robert De Niro and Al Pacino\\n6. The Godfather (1972) - A classic crime film directed by Francis Ford Coppola\\n7. Heat (1995) - A crime thriller directed by Michael Mann, starring Al Pacino and Robert De Niro\\n8. The Departed (2006) - A crime thriller directed by Martin Scorsese, starring Leonardo DiCaprio and Matt Damon.', additional\_kwargs={}), raw={'id': 'chatcmpl-9EKf2nZ4latFJvHy0gzOUZbaB8xwY', 'choices': \[Choice(finish\_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='1. Infernal Affairs (2002) - The original Hong Kong film that inspired The Departed\\n2. The Town (2010) - A crime thriller directed by Ben Affleck\\n3. Mystic River (2003) - A crime drama directed by Clint Eastwood\\n4. Goodfellas (1990) - A classic crime film directed by Martin Scorsese\\n5. The Irishman (2019) - Another crime film directed by Martin Scorsese, starring Robert De Niro and Al Pacino\\n6. The Godfather (1972) - A classic crime film directed by Francis Ford Coppola\\n7. Heat (1995) - A crime thriller directed by Michael Mann, starring Al Pacino and Robert De Niro\\n8. The Departed (2006) - A crime thriller directed by Martin Scorsese, starring Leonardo DiCaprio and Matt Damon.', role='assistant', function\_call=None, tool\_calls=None))\], 'created': 1713203040, 'model': 'gpt-3.5-turbo-0125', 'object': 'chat.completion', 'system\_fingerprint': 'fp\_c2295e73ad', 'usage': CompletionUsage(completion\_tokens=184, prompt\_tokens=15, total\_tokens=199)}, delta=None, logprobs=None, additional\_kwargs={})})

### Try Output Parsing[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#try-output-parsing)

Let's parse the outputs into a structured Pydantic object.

In \[ \]:

Copied!

from typing import List
from pydantic import BaseModel, Field
from llama\_index.core.output\_parsers import PydanticOutputParser

class Movie(BaseModel):
    """Object representing a single movie."""

    name: str \= Field(..., description\="Name of the movie.")
    year: int \= Field(..., description\="Year of the movie.")

class Movies(BaseModel):
    """Object representing a list of movies."""

    movies: List\[Movie\] \= Field(..., description\="List of movies.")

llm \= OpenAI(model\="gpt-3.5-turbo")
output\_parser \= PydanticOutputParser(Movies)
json\_prompt\_str \= """\\
Please generate related movies to {movie\_name}. Output with the following JSON format: 
"""
json\_prompt\_str \= output\_parser.format(json\_prompt\_str)

from typing import List from pydantic import BaseModel, Field from llama\_index.core.output\_parsers import PydanticOutputParser class Movie(BaseModel): """Object representing a single movie.""" name: str = Field(..., description="Name of the movie.") year: int = Field(..., description="Year of the movie.") class Movies(BaseModel): """Object representing a list of movies.""" movies: List\[Movie\] = Field(..., description="List of movies.") llm = OpenAI(model="gpt-3.5-turbo") output\_parser = PydanticOutputParser(Movies) json\_prompt\_str = """\\ Please generate related movies to {movie\_name}. Output with the following JSON format: """ json\_prompt\_str = output\_parser.format(json\_prompt\_str)

In \[ \]:

Copied!

\# add JSON spec to prompt template
json\_prompt\_tmpl \= PromptTemplate(json\_prompt\_str)

p \= QueryPipeline(chain\=\[json\_prompt\_tmpl, llm, output\_parser\], verbose\=True)
output \= p.run(movie\_name\="Toy Story")

\# add JSON spec to prompt template json\_prompt\_tmpl = PromptTemplate(json\_prompt\_str) p = QueryPipeline(chain=\[json\_prompt\_tmpl, llm, output\_parser\], verbose=True) output = p.run(movie\_name="Toy Story")

\> Running module 2e4093c5-ae62-420a-be91-9c28c057bada with input: 
movie\_name: Toy Story

\> Running module 3b41f95c-f54b-41d7-8ef0-8e45b5d7eeb0 with input: 
messages: Please generate related movies to Toy Story. Output with the following JSON format: 



Here's a JSON schema to follow:
{"title": "Movies", "description": "Object representing a list of movies.", "typ...

\> Running module 27e79a16-72de-4ce2-8b2e-94932c4069c3 with input: 
input: assistant: {
  "movies": \[
    {
      "name": "Finding Nemo",
      "year": 2003
    },
    {
      "name": "Monsters, Inc.",
      "year": 2001
    },
    {
      "name": "Cars",
      "year": 2006
...

In \[ \]:

Copied!

output

output

Out\[ \]:

Movies(movies=\[Movie(name='Finding Nemo', year=2003), Movie(name='Monsters, Inc.', year=2001), Movie(name='Cars', year=2006), Movie(name='The Incredibles', year=2004), Movie(name='Ratatouille', year=2007)\])

### Streaming Support[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#streaming-support)

The query pipelines have LLM streaming support (simply do `as_query_component(streaming=True)`). Intermediate outputs will get autoconverted, and the final output can be a streaming output. Here's some examples.

**1\. Chain multiple Prompts with Streaming**

In \[ \]:

Copied!

prompt\_str \= "Please generate related movies to {movie\_name}"
prompt\_tmpl \= PromptTemplate(prompt\_str)
\# let's add some subsequent prompts for fun
prompt\_str2 \= """\\
Here's some text:

{text}

Can you rewrite this with a summary of each movie?
"""
prompt\_tmpl2 \= PromptTemplate(prompt\_str2)
llm \= OpenAI(model\="gpt-3.5-turbo")
llm\_c \= llm.as\_query\_component(streaming\=True)

p \= QueryPipeline(
    chain\=\[prompt\_tmpl, llm\_c, prompt\_tmpl2, llm\_c\], verbose\=True
)
\# p = QueryPipeline(chain=\[prompt\_tmpl, llm\_c\], verbose=True)

prompt\_str = "Please generate related movies to {movie\_name}" prompt\_tmpl = PromptTemplate(prompt\_str) # let's add some subsequent prompts for fun prompt\_str2 = """\\ Here's some text: {text} Can you rewrite this with a summary of each movie? """ prompt\_tmpl2 = PromptTemplate(prompt\_str2) llm = OpenAI(model="gpt-3.5-turbo") llm\_c = llm.as\_query\_component(streaming=True) p = QueryPipeline( chain=\[prompt\_tmpl, llm\_c, prompt\_tmpl2, llm\_c\], verbose=True ) # p = QueryPipeline(chain=\[prompt\_tmpl, llm\_c\], verbose=True)

In \[ \]:

Copied!

output \= p.run(movie\_name\="The Dark Knight")
for o in output:
    print(o.delta, end\="")

output = p.run(movie\_name="The Dark Knight") for o in output: print(o.delta, end="")

\> Running module 213af6d4-3450-46af-9087-b80656ae6951 with input: 
movie\_name: The Dark Knight

\> Running module 3ff7e987-f5f3-4b36-a3e1-be5a4821d9d9 with input: 
messages: Please generate related movies to The Dark Knight

\> Running module a2841bd3-c833-4427-9a7e-83b19872b064 with input: 
text: <generator object llm\_chat\_callback.<locals>.wrap.<locals>.wrapped\_llm\_chat.<locals>.wrapped\_gen at 0x298d338b0>

\> Running module c7e0a454-213a-460e-b029-f2d42fd7d938 with input: 
messages: Here's some text:

1. Batman Begins (2005)
2. The Dark Knight Rises (2012)
3. Batman v Superman: Dawn of Justice (2016)
4. Man of Steel (2013)
5. The Avengers (2012)
6. Iron Man (2008)
7. Captain Amer...

1\. Batman Begins (2005): A young Bruce Wayne becomes Batman to fight crime in Gotham City, facing his fears and training under the guidance of Ra's al Ghul.
2. The Dark Knight Rises (2012): Batman returns to protect Gotham City from the ruthless terrorist Bane, who plans to destroy the city and its symbol of hope.
3. Batman v Superman: Dawn of Justice (2016): Batman and Superman clash as their ideologies collide, leading to an epic battle while a new threat emerges that threatens humanity.
4. Man of Steel (2013): The origin story of Superman, as he embraces his powers and faces General Zod, a fellow Kryptonian seeking to destroy Earth.
5. The Avengers (2012): Earth's mightiest heroes, including Iron Man, Captain America, Thor, and Hulk, join forces to stop Loki and his alien army from conquering the world.
6. Iron Man (2008): Billionaire Tony Stark builds a high-tech suit to escape captivity and becomes the superhero Iron Man, using his technology to fight against evil.
7. Captain America: The Winter Soldier (2014): Captain America teams up with Black Widow and Falcon to uncover a conspiracy within S.H.I.E.L.D. while facing a deadly assassin known as the Winter Soldier.
8. The Amazing Spider-Man (2012): Peter Parker, a high school student bitten by a radioactive spider, becomes Spider-Man and battles the Lizard, a monstrous villain threatening New York City.
9. Watchmen (2009): Set in an alternate reality, a group of retired vigilantes investigates the murder of one of their own, uncovering a conspiracy that could have catastrophic consequences.
10. Sin City (2005): A neo-noir anthology film set in the crime-ridden city of Basin City, following various characters as they navigate through corruption, violence, and redemption.
11. V for Vendetta (2005): In a dystopian future, a masked vigilante known as V fights against a totalitarian government, inspiring the people to rise up and reclaim their freedom.
12. Blade Runner 2049 (2017): A young blade runner uncovers a long-buried secret that leads him to seek out former blade runner Rick Deckard, while unraveling the mysteries of a future society.
13. Inception (2010): A skilled thief enters people's dreams to steal information, but is tasked with planting an idea instead, leading to a mind-bending journey through multiple layers of reality.
14. The Matrix (1999): A computer hacker discovers the truth about reality, joining a group of rebels fighting against sentient machines that have enslaved humanity in a simulated world.
15. The Crow (1994): A musician, resurrected by a supernatural crow, seeks vengeance against the gang that murdered him and his fiancée, unleashing a dark and atmospheric tale of revenge.

**2\. Feed streaming output to output parser**

In \[ \]:

Copied!

p \= QueryPipeline(
    chain\=\[
        json\_prompt\_tmpl,
        llm.as\_query\_component(streaming\=True),
        output\_parser,
    \],
    verbose\=True,
)
output \= p.run(movie\_name\="Toy Story")
print(output)

p = QueryPipeline( chain=\[ json\_prompt\_tmpl, llm.as\_query\_component(streaming=True), output\_parser, \], verbose=True, ) output = p.run(movie\_name="Toy Story") print(output)

\> Running module fe1dbf6a-56e0-44bf-97d7-a2a1fe9d9b8c with input: 
movie\_name: Toy Story

\> Running module a8eaaf91-df9d-46c4-bbae-06c15cd15123 with input: 
messages: Please generate related movies to Toy Story. Output with the following JSON format: 



Here's a JSON schema to follow:
{"title": "Movies", "description": "Object representing a list of movies.", "typ...

\> Running module fcbc0b09-0ef5-43e0-b007-c4508fd6742f with input: 
input: <generator object llm\_chat\_callback.<locals>.wrap.<locals>.wrapped\_llm\_chat.<locals>.wrapped\_gen at 0x298d32dc0>

movies=\[Movie(name='Finding Nemo', year=2003), Movie(name='Monsters, Inc.', year=2001), Movie(name='The Incredibles', year=2004), Movie(name='Cars', year=2006), Movie(name='Ratatouille', year=2007)\]

Chain Together Query Rewriting Workflow (prompts + LLM) with Retrieval[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#chain-together-query-rewriting-workflow-prompts-llm-with-retrieval)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Here we try a slightly more complex workflow where we send the input through two prompts before initiating retrieval.

1.  Generate question about given topic.
2.  Hallucinate answer given question, for better retrieval.

Since each prompt only takes in one input, note that the `QueryPipeline` will automatically chain LLM outputs into the prompt and then into the LLM.

You'll see how to define links more explicitly in the next section.

In \[ \]:

Copied!

\# !pip install llama-index-postprocessor-cohere-rerank

\# !pip install llama-index-postprocessor-cohere-rerank

In \[ \]:

Copied!

from llama\_index.postprocessor.cohere\_rerank import CohereRerank

\# generate question regarding topic
prompt\_str1 \= "Please generate a concise question about Paul Graham's life regarding the following topic {topic}"
prompt\_tmpl1 \= PromptTemplate(prompt\_str1)
\# use HyDE to hallucinate answer.
prompt\_str2 \= (
    "Please write a passage to answer the question\\n"
    "Try to include as many key details as possible.\\n"
    "\\n"
    "\\n"
    "{query\_str}\\n"
    "\\n"
    "\\n"
    'Passage:"""\\n'
)
prompt\_tmpl2 \= PromptTemplate(prompt\_str2)

llm \= OpenAI(model\="gpt-3.5-turbo")
retriever \= index.as\_retriever(similarity\_top\_k\=5)
p \= QueryPipeline(
    chain\=\[prompt\_tmpl1, llm, prompt\_tmpl2, llm, retriever\], verbose\=True
)

from llama\_index.postprocessor.cohere\_rerank import CohereRerank # generate question regarding topic prompt\_str1 = "Please generate a concise question about Paul Graham's life regarding the following topic {topic}" prompt\_tmpl1 = PromptTemplate(prompt\_str1) # use HyDE to hallucinate answer. prompt\_str2 = ( "Please write a passage to answer the question\\n" "Try to include as many key details as possible.\\n" "\\n" "\\n" "{query\_str}\\n" "\\n" "\\n" 'Passage:"""\\n' ) prompt\_tmpl2 = PromptTemplate(prompt\_str2) llm = OpenAI(model="gpt-3.5-turbo") retriever = index.as\_retriever(similarity\_top\_k=5) p = QueryPipeline( chain=\[prompt\_tmpl1, llm, prompt\_tmpl2, llm, retriever\], verbose=True )

In \[ \]:

Copied!

nodes \= p.run(topic\="college")
len(nodes)

nodes = p.run(topic="college") len(nodes)

\> Running module f5435516-61b6-49e9-9926-220cfb6443bd with input: 
topic: college

\> Running module 1dcaa097-cedc-4466-81bb-f8fd8768762b with input: 
messages: Please generate a concise question about Paul Graham's life regarding the following topic college

\> Running module 891afa10-5fe0-47ed-bdee-42a59d0e916d with input: 
query\_str: assistant: How did Paul Graham's college experience shape his career and entrepreneurial mindset?

\> Running module 5bcd9964-b972-41a9-960d-96894c57a372 with input: 
messages: Please write a passage to answer the question
Try to include as many key details as possible.


How did Paul Graham's college experience shape his career and entrepreneurial mindset?


Passage:"""

\> Running module 0b81a91a-2c90-4700-8ba1-25ffad5311fd with input: 
input: assistant: Paul Graham's college experience played a pivotal role in shaping his career and entrepreneurial mindset. As a student at Cornell University, Graham immersed himself in the world of compute...

Out\[ \]:

5

Create a Full RAG Pipeline as a DAG[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#create-a-full-rag-pipeline-as-a-dag)
--------------------------------------------------------------------------------------------------------------------------------------------------

Here we chain together a full RAG pipeline consisting of query rewriting, retrieval, reranking, and response synthesis.

Here we can't use `chain` syntax because certain modules depend on multiple inputs (for instance, response synthesis expects both the retrieved nodes and the original question). Instead we'll construct a DAG explicitly, through `add_modules` and then `add_link`.

### 1\. RAG Pipeline with Query Rewriting[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#1-rag-pipeline-with-query-rewriting)

We use an LLM to rewrite the query first before passing it to our downstream modules - retrieval/reranking/synthesis.

In \[ \]:

Copied!

from llama\_index.postprocessor.cohere\_rerank import CohereRerank
from llama\_index.core.response\_synthesizers import TreeSummarize

\# define modules
prompt\_str \= "Please generate a question about Paul Graham's life regarding the following topic {topic}"
prompt\_tmpl \= PromptTemplate(prompt\_str)
llm \= OpenAI(model\="gpt-3.5-turbo")
retriever \= index.as\_retriever(similarity\_top\_k\=3)
reranker \= CohereRerank()
summarizer \= TreeSummarize(llm\=llm)

from llama\_index.postprocessor.cohere\_rerank import CohereRerank from llama\_index.core.response\_synthesizers import TreeSummarize # define modules prompt\_str = "Please generate a question about Paul Graham's life regarding the following topic {topic}" prompt\_tmpl = PromptTemplate(prompt\_str) llm = OpenAI(model="gpt-3.5-turbo") retriever = index.as\_retriever(similarity\_top\_k=3) reranker = CohereRerank() summarizer = TreeSummarize(llm=llm)

In \[ \]:

Copied!

\# define query pipeline
p \= QueryPipeline(verbose\=True)
p.add\_modules(
    {
        "llm": llm,
        "prompt\_tmpl": prompt\_tmpl,
        "retriever": retriever,
        "summarizer": summarizer,
        "reranker": reranker,
    }
)

\# define query pipeline p = QueryPipeline(verbose=True) p.add\_modules( { "llm": llm, "prompt\_tmpl": prompt\_tmpl, "retriever": retriever, "summarizer": summarizer, "reranker": reranker, } )

Next we draw links between modules with `add_link`. `add_link` takes in the source/destination module ids, and optionally the `source_key` and `dest_key`. Specify the `source_key` or `dest_key` if there are multiple outputs/inputs respectively.

You can view the set of input/output keys for each module through `module.as_query_component().input_keys` and `module.as_query_component().output_keys`.

Here we explicitly specify `dest_key` for the `reranker` and `summarizer` modules because they take in two inputs (query\_str and nodes).

In \[ \]:

Copied!

p.add\_link("prompt\_tmpl", "llm")
p.add\_link("llm", "retriever")
p.add\_link("retriever", "reranker", dest\_key\="nodes")
p.add\_link("llm", "reranker", dest\_key\="query\_str")
p.add\_link("reranker", "summarizer", dest\_key\="nodes")
p.add\_link("llm", "summarizer", dest\_key\="query\_str")

\# look at summarizer input keys
print(summarizer.as\_query\_component().input\_keys)

p.add\_link("prompt\_tmpl", "llm") p.add\_link("llm", "retriever") p.add\_link("retriever", "reranker", dest\_key="nodes") p.add\_link("llm", "reranker", dest\_key="query\_str") p.add\_link("reranker", "summarizer", dest\_key="nodes") p.add\_link("llm", "summarizer", dest\_key="query\_str") # look at summarizer input keys print(summarizer.as\_query\_component().input\_keys)

required\_keys={'query\_str', 'nodes'} optional\_keys=set()

We use `networkx` to store the graph representation. This gives us an easy way to view the DAG!

In \[ \]:

Copied!

\## create graph
from pyvis.network import Network

net \= Network(notebook\=True, cdn\_resources\="in\_line", directed\=True)
net.from\_nx(p.dag)
net.show("rag\_dag.html")

\## another option using \`pygraphviz\`
\# from networkx.drawing.nx\_agraph import to\_agraph
\# from IPython.display import Image
\# agraph = to\_agraph(p.dag)
\# agraph.layout(prog="dot")
\# agraph.draw('rag\_dag.png')
\# display(Image('rag\_dag.png'))

\## create graph from pyvis.network import Network net = Network(notebook=True, cdn\_resources="in\_line", directed=True) net.from\_nx(p.dag) net.show("rag\_dag.html") ## another option using \`pygraphviz\` # from networkx.drawing.nx\_agraph import to\_agraph # from IPython.display import Image # agraph = to\_agraph(p.dag) # agraph.layout(prog="dot") # agraph.draw('rag\_dag.png') # display(Image('rag\_dag.png'))

rag\_dag.html

Out\[ \]:

In \[ \]:

Copied!

response \= p.run(topic\="YC")

response = p.run(topic="YC")

\> Running module prompt\_tmpl with input: 
topic: YC

\> Running module llm with input: 
messages: Please generate a question about Paul Graham's life regarding the following topic YC

\> Running module retriever with input: 
input: assistant: What role did Paul Graham play in the founding and development of Y Combinator (YC)?

\> Running module reranker with input: 
query\_str: assistant: What role did Paul Graham play in the founding and development of Y Combinator (YC)?
nodes: \[NodeWithScore(node=TextNode(id\_='ccd39041-5a64-4bd3-aca7-48f804b5a23f', embedding=None, metadata={'file\_path': '../data/paul\_graham/paul\_graham\_essay.txt', 'file\_name': 'paul\_graham\_essay.txt', 'file...

\> Running module summarizer with input: 
query\_str: assistant: What role did Paul Graham play in the founding and development of Y Combinator (YC)?
nodes: \[NodeWithScore(node=TextNode(id\_='120574dd-a5c9-4985-ab3e-37b1070b500a', embedding=None, metadata={'file\_path': '../data/paul\_graham/paul\_graham\_essay.txt', 'file\_name': 'paul\_graham\_essay.txt', 'file...

In \[ \]:

Copied!

print(str(response))

print(str(response))

Paul Graham played a significant role in the founding and development of Y Combinator (YC). He was one of the co-founders of YC and provided the initial funding for the investment firm. Along with his partners, he implemented the ideas they had been discussing and started their own investment firm. Paul Graham also played a key role in shaping the unique batch model of YC, where a group of startups is funded and provided intensive support for a period of three months. He was actively involved in selecting and helping the founders, and he also wrote essays and worked on YC's internal software.

In \[ \]:

Copied!

\# you can do async too
response \= await p.arun(topic\="YC")
print(str(response))

\# you can do async too response = await p.arun(topic="YC") print(str(response))

\> Running modules and inputs in parallel: 
Module key: prompt\_tmpl. Input: 
topic: YC

\> Running modules and inputs in parallel: 
Module key: llm. Input: 
messages: Please generate a question about Paul Graham's life regarding the following topic YC

\> Running modules and inputs in parallel: 
Module key: retriever. Input: 
input: assistant: What role did Paul Graham play in the founding and development of Y Combinator (YC)?

\> Running modules and inputs in parallel: 
Module key: reranker. Input: 
query\_str: assistant: What role did Paul Graham play in the founding and development of Y Combinator (YC)?
nodes: \[NodeWithScore(node=TextNode(id\_='ccd39041-5a64-4bd3-aca7-48f804b5a23f', embedding=None, metadata={'file\_path': '../data/paul\_graham/paul\_graham\_essay.txt', 'file\_name': 'paul\_graham\_essay.txt', 'file...

\> Running modules and inputs in parallel: 
Module key: summarizer. Input: 
query\_str: assistant: What role did Paul Graham play in the founding and development of Y Combinator (YC)?
nodes: \[NodeWithScore(node=TextNode(id\_='120574dd-a5c9-4985-ab3e-37b1070b500a', embedding=None, metadata={'file\_path': '../data/paul\_graham/paul\_graham\_essay.txt', 'file\_name': 'paul\_graham\_essay.txt', 'file...

Paul Graham played a significant role in the founding and development of Y Combinator (YC). He was one of the co-founders of YC and provided the initial funding for the investment firm. Along with his partners, he implemented the ideas they had been discussing and decided to start their own investment firm. Paul Graham also played a key role in shaping the unique batch model of YC, where a group of startups is funded and provided intensive support for a period of three months. He was actively involved in selecting and helping the founders and worked on various projects related to YC, including writing essays and developing internal software.

### 2\. RAG Pipeline without Query Rewriting[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#2-rag-pipeline-without-query-rewriting)

Here we setup a RAG pipeline without the query rewriting step.

Here we need a way to link the input query to both the retriever, reranker, and summarizer. We can do this by defining a special `InputComponent`, allowing us to link the inputs to multiple downstream modules.

In \[ \]:

Copied!

from llama\_index.postprocessor.cohere\_rerank import CohereRerank
from llama\_index.core.response\_synthesizers import TreeSummarize
from llama\_index.core.query\_pipeline import InputComponent

retriever \= index.as\_retriever(similarity\_top\_k\=5)
summarizer \= TreeSummarize(llm\=OpenAI(model\="gpt-3.5-turbo"))
reranker \= CohereRerank()

from llama\_index.postprocessor.cohere\_rerank import CohereRerank from llama\_index.core.response\_synthesizers import TreeSummarize from llama\_index.core.query\_pipeline import InputComponent retriever = index.as\_retriever(similarity\_top\_k=5) summarizer = TreeSummarize(llm=OpenAI(model="gpt-3.5-turbo")) reranker = CohereRerank()

In \[ \]:

Copied!

p \= QueryPipeline(verbose\=True)
p.add\_modules(
    {
        "input": InputComponent(),
        "retriever": retriever,
        "summarizer": summarizer,
    }
)
p.add\_link("input", "retriever")
p.add\_link("input", "summarizer", dest\_key\="query\_str")
p.add\_link("retriever", "summarizer", dest\_key\="nodes")

p = QueryPipeline(verbose=True) p.add\_modules( { "input": InputComponent(), "retriever": retriever, "summarizer": summarizer, } ) p.add\_link("input", "retriever") p.add\_link("input", "summarizer", dest\_key="query\_str") p.add\_link("retriever", "summarizer", dest\_key="nodes")

In \[ \]:

Copied!

output \= p.run(input\="what did the author do in YC")

output = p.run(input="what did the author do in YC")

\> Running module input with input: 
input: what did the author do in YC

\> Running module retriever with input: 
input: what did the author do in YC

\> Running module summarizer with input: 
query\_str: what did the author do in YC
nodes: \[NodeWithScore(node=TextNode(id\_='86dea730-ca35-4bcb-9f9b-4c99e8eadd08', embedding=None, metadata={'file\_path': '../data/paul\_graham/paul\_graham\_essay.txt', 'file\_name': 'paul\_graham\_essay.txt', 'file...

In \[ \]:

Copied!

print(str(output))

print(str(output))

The author worked on various projects at YC, including writing essays and working on YC's internal software. They also played a key role in the creation and operation of YC by funding the program with their own money and organizing a batch model where they would fund a group of startups twice a year. They provided support and guidance to the startups during a three-month intensive program and used their building in Cambridge as the headquarters for YC. Additionally, they hosted weekly dinners where experts on startups would give talks.

Defining a Custom Component in a Query Pipeline[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#defining-a-custom-component-in-a-query-pipeline)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can easily define a custom component. Simply subclass a `QueryComponent`, implement validation/run functions + some helpers, and plug it in.

Let's wrap the related movie generation prompt+LLM chain from the first example into a custom component.

In \[ \]:

Copied!

from llama\_index.core.query\_pipeline import (
    CustomQueryComponent,
    InputKeys,
    OutputKeys,
)
from typing import Dict, Any
from llama\_index.core.llms.llm import LLM
from pydantic import Field

class RelatedMovieComponent(CustomQueryComponent):
    """Related movie component."""

    llm: LLM \= Field(..., description\="OpenAI LLM")

    def \_validate\_component\_inputs(
        self, input: Dict\[str, Any\]
    ) \-> Dict\[str, Any\]:
        """Validate component inputs during run\_component."""
        \# NOTE: this is OPTIONAL but we show you here how to do validation as an example
        return input

    @property
    def \_input\_keys(self) \-> set:
        """Input keys dict."""
        \# NOTE: These are required inputs. If you have optional inputs please override
        \# \`optional\_input\_keys\_dict\`
        return {"movie"}

    @property
    def \_output\_keys(self) \-> set:
        return {"output"}

    def \_run\_component(self, \*\*kwargs) \-> Dict\[str, Any\]:
        """Run the component."""
        \# use QueryPipeline itself here for convenience
        prompt\_str \= "Please generate related movies to {movie\_name}"
        prompt\_tmpl \= PromptTemplate(prompt\_str)
        p \= QueryPipeline(chain\=\[prompt\_tmpl, llm\])
        return {"output": p.run(movie\_name\=kwargs\["movie"\])}

from llama\_index.core.query\_pipeline import ( CustomQueryComponent, InputKeys, OutputKeys, ) from typing import Dict, Any from llama\_index.core.llms.llm import LLM from pydantic import Field class RelatedMovieComponent(CustomQueryComponent): """Related movie component.""" llm: LLM = Field(..., description="OpenAI LLM") def \_validate\_component\_inputs( self, input: Dict\[str, Any\] ) -> Dict\[str, Any\]: """Validate component inputs during run\_component.""" # NOTE: this is OPTIONAL but we show you here how to do validation as an example return input @property def \_input\_keys(self) -> set: """Input keys dict.""" # NOTE: These are required inputs. If you have optional inputs please override # \`optional\_input\_keys\_dict\` return {"movie"} @property def \_output\_keys(self) -> set: return {"output"} def \_run\_component(self, \*\*kwargs) -> Dict\[str, Any\]: """Run the component.""" # use QueryPipeline itself here for convenience prompt\_str = "Please generate related movies to {movie\_name}" prompt\_tmpl = PromptTemplate(prompt\_str) p = QueryPipeline(chain=\[prompt\_tmpl, llm\]) return {"output": p.run(movie\_name=kwargs\["movie"\])}

Let's try the custom component out! We'll also add a step to convert the output to Shakespeare.

In \[ \]:

Copied!

llm \= OpenAI(model\="gpt-3.5-turbo")
component \= RelatedMovieComponent(llm\=llm)

\# let's add some subsequent prompts for fun
prompt\_str \= """\\
Here's some text:

{text}

Can you rewrite this in the voice of Shakespeare?
"""
prompt\_tmpl \= PromptTemplate(prompt\_str)

p \= QueryPipeline(chain\=\[component, prompt\_tmpl, llm\], verbose\=True)

llm = OpenAI(model="gpt-3.5-turbo") component = RelatedMovieComponent(llm=llm) # let's add some subsequent prompts for fun prompt\_str = """\\ Here's some text: {text} Can you rewrite this in the voice of Shakespeare? """ prompt\_tmpl = PromptTemplate(prompt\_str) p = QueryPipeline(chain=\[component, prompt\_tmpl, llm\], verbose=True)

In \[ \]:

Copied!

output \= p.run(movie\="Love Actually")

output = p.run(movie="Love Actually")

\> Running module 31ca224a-f226-4956-882b-73878843d869 with input: 
movie: Love Actually

\> Running module febb41b5-2528-416a-bde7-6accdb0f9c51 with input: 
text: assistant: 1. "Valentine's Day" (2010)
2. "New Year's Eve" (2011)
3. "The Holiday" (2006)
4. "Crazy, Stupid, Love" (2011)
5. "Notting Hill" (1999)
6. "Four Weddings and a Funeral" (1994)
7. "Bridget J...

\> Running module e834ffbe-e97c-4ab0-9726-24f1534745b2 with input: 
messages: Here's some text:

1. "Valentine's Day" (2010)
2. "New Year's Eve" (2011)
3. "The Holiday" (2006)
4. "Crazy, Stupid, Love" (2011)
5. "Notting Hill" (1999)
6. "Four Weddings and a Funeral" (1994)
7. "B...

In \[ \]:

Copied!

print(str(output))

print(str(output))

assistant: 1. "Valentine's Day" (2010) - "A day of love, where hearts entwine, 
   And Cupid's arrow finds its mark divine."

2. "New Year's Eve" (2011) - "When old year fades, and new year dawns,
   We gather 'round, to celebrate the morns."

3. "The Holiday" (2006) - "Two souls, adrift in search of cheer,
   Find solace in a holiday so dear."

4. "Crazy, Stupid, Love" (2011) - "A tale of love, both wild and mad,
   Where hearts are lost, then found, and glad."

5. "Notting Hill" (1999) - "In London town, where love may bloom,
   A humble man finds love, and breaks the gloom."

6. "Four Weddings and a Funeral" (1994) - "Four times the vows, and one time mourn,
   Love's journey, with laughter and tears adorned."

7. "Bridget Jones's Diary" (2001) - "A maiden fair, with wit and charm,
   Records her life, and love's alarm."

8. "About Time" (2013) - "A tale of time, where love transcends,
   And moments cherished, never truly ends."

9. "The Best Exotic Marigold Hotel" (2011) - "In India's land, where dreams unfold,
   A hotel blooms, where hearts find gold."

10. "The Notebook" (2004) - "A love that spans both time and space,
    Where words and memories find their place."

11. "Serendipity" (2001) - "By chance or fate, two souls collide,
    In search of love, they cannot hide."

12. "P.S. I Love You" (2007) - "In letters penned, from love's embrace,
    A departed soul, still finds its trace."

13. "500 Days of Summer" (2009) - "A tale of love, both sweet and sour,
    Where seasons change, and hearts devour."

14. "The Fault in Our Stars" (2014) - "Two hearts, aflame, in starlit skies,
    Love's tragedy, where hope never dies."

15. "La La Land" (2016) - "In dreams and songs, two hearts entwine,
    A city's magic, where love's stars align."

Stepwise Execution of a Pipeline[¶](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/#stepwise-execution-of-a-pipeline)
--------------------------------------------------------------------------------------------------------------------------------------------

Executing a pipeline one step at a time is a great idea if you:

*   want to better debug the order of execution
*   log data in between each step
*   give feedback to a user as to what is being processed
*   and more!

To execute a pipeline, you must create a `run_state`, and then loop through the exection. A basic example is below.

In \[ \]:

Copied!

from llama\_index.core.query\_pipeline import QueryPipeline
from llama\_index.core import PromptTemplate
from llama\_index.llms.openai import OpenAI

\# try chaining basic prompts
prompt\_str \= "Please generate related movies to {movie\_name}"
prompt\_tmpl \= PromptTemplate(prompt\_str)
llm \= OpenAI(model\="gpt-3.5-turbo")

p \= QueryPipeline(chain\=\[prompt\_tmpl, llm\], verbose\=True)

from llama\_index.core.query\_pipeline import QueryPipeline from llama\_index.core import PromptTemplate from llama\_index.llms.openai import OpenAI # try chaining basic prompts prompt\_str = "Please generate related movies to {movie\_name}" prompt\_tmpl = PromptTemplate(prompt\_str) llm = OpenAI(model="gpt-3.5-turbo") p = QueryPipeline(chain=\[prompt\_tmpl, llm\], verbose=True)

In \[ \]:

Copied!

run\_state \= p.get\_run\_state(movie\_name\="The Departed")

next\_module\_keys \= p.get\_next\_module\_keys(run\_state)

while True:
    for module\_key in next\_module\_keys:
        \# get the module and input
        module \= run\_state.module\_dict\[module\_key\]
        module\_input \= run\_state.all\_module\_inputs\[module\_key\]

        \# run the module
        output\_dict \= module.run\_component(\*\*module\_input)

        \# process the output
        p.process\_component\_output(
            output\_dict,
            module\_key,
            run\_state,
        )

    \# get the next module keys
    next\_module\_keys \= p.get\_next\_module\_keys(
        run\_state,
    )

    \# if no more modules to run, break
    if not next\_module\_keys:
        run\_state.result\_outputs\[module\_key\] \= output\_dict
        break

\# the final result is at \`module\_key\`
\# it is a dict of 'output' -> ChatResponse object in this case
print(run\_state.result\_outputs\[module\_key\]\["output"\].message.content)

run\_state = p.get\_run\_state(movie\_name="The Departed") next\_module\_keys = p.get\_next\_module\_keys(run\_state) while True: for module\_key in next\_module\_keys: # get the module and input module = run\_state.module\_dict\[module\_key\] module\_input = run\_state.all\_module\_inputs\[module\_key\] # run the module output\_dict = module.run\_component(\*\*module\_input) # process the output p.process\_component\_output( output\_dict, module\_key, run\_state, ) # get the next module keys next\_module\_keys = p.get\_next\_module\_keys( run\_state, ) # if no more modules to run, break if not next\_module\_keys: run\_state.result\_outputs\[module\_key\] = output\_dict break # the final result is at \`module\_key\` # it is a dict of 'output' -> ChatResponse object in this case print(run\_state.result\_outputs\[module\_key\]\["output"\].message.content)

1\. Infernal Affairs (2002) - The original Hong Kong film that inspired The Departed
2. The Town (2010) - A crime thriller directed by Ben Affleck
3. Mystic River (2003) - A crime drama directed by Clint Eastwood
4. Goodfellas (1990) - A classic mobster film directed by Martin Scorsese
5. The Irishman (2019) - Another crime drama directed by Martin Scorsese, starring Robert De Niro and Al Pacino
6. The Departed (2006) - The Departed is a 2006 American crime film directed by Martin Scorsese and written by William Monahan. It is a remake of the 2002 Hong Kong film Infernal Affairs. The film stars Leonardo DiCaprio, Matt Damon, Jack Nicholson, and Mark Wahlberg, with Martin Sheen, Ray Winstone, Vera Farmiga, and Alec Baldwin in supporting roles.

Back to top

[Previous Sub Question Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/sub_question_query_engine/)[Next Query Pipeline with Async/Parallel Execution](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline_async/)
