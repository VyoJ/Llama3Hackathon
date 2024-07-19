Title: Function Calling Program for Structured Extraction

URL Source: https://docs.llamaindex.ai/en/stable/examples/output_parsing/function_program/

Markdown Content:
Function Calling Program for Structured Extraction - LlamaIndex


[![Image 3: Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/docs/examples/output_parsing/function_program.ipynb)

This guide shows you how to do structured data extraction with our `FunctionCallingProgram`. Given a function-calling LLM as well as an output Pydantic class, generate a structured Pydantic object. We use three different function calling LLMs:

*   OpenAI
*   Anthropic Claude
*   Mistral

In terms of the target object, you can choose to directly specify `output_cls`, or specify a `PydanticOutputParser` or any other BaseOutputParser that generates a Pydantic object.

in the examples below, we show you different ways of extracting into the `Album` object (which can contain a list of Song objects).

**NOTE**: The `FunctionCallingProgram` only works with LLMs that natively support function calling, by inserting the schema of the Pydantic object as the "tool parameters" for a tool. For all other LLMs, please use our `LLMTextCompletionProgram`, which will directly prompt the model through text to get back a structured output.

Define `Album` class[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/function_program/#define-album-class)
--------------------------------------------------------------------------------------------------------------------------

This is a simple example of parsing an output into an `Album` schema, which can contain multiple songs.

Just pass `Album` into the `output_cls` property on initialization of the `FunctionCallingProgram`.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

from pydantic import BaseModel
from typing import List

from llama\_index.core.program import FunctionCallingProgram

from pydantic import BaseModel from typing import List from llama\_index.core.program import FunctionCallingProgram

Define output schema

In \[ \]:

Copied!

class Song(BaseModel):
    """Data model for a song."""

    title: str
    length\_seconds: int

class Album(BaseModel):
    """Data model for an album."""

    name: str
    artist: str
    songs: List\[Song\]

class Song(BaseModel): """Data model for a song.""" title: str length\_seconds: int class Album(BaseModel): """Data model for an album.""" name: str artist: str songs: List\[Song\]

Define Function Calling Program[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/function_program/#define-function-calling-program)
--------------------------------------------------------------------------------------------------------------------------------------------------

We define a function calling program with three function-calling LLMs:

*   OpenAI
*   Anthropic
*   Mistral

### Function Calling Program with OpenAI[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/function_program/#function-calling-program-with-openai)

Here we use gpt-3.5-turbo.

We demonstrate structured data extraction "single" function calling and also parallel function calling, allowing us to extract out multiple objects.

#### Function Calling (Single Object)[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/function_program/#function-calling-single-object)

In \[ \]:

Copied!

from llama\_index.core.program import FunctionCallingProgram
from llama\_index.llms.openai import OpenAI

from llama\_index.core.program import FunctionCallingProgram from llama\_index.llms.openai import OpenAI

In \[ \]:

Copied!

prompt\_template\_str \= """\\
Generate an example album, with an artist and a list of songs. \\
Using the movie {movie\_name} as inspiration.\\
"""
llm \= OpenAI(model\="gpt-3.5-turbo")

program \= FunctionCallingProgram.from\_defaults(
    output\_cls\=Album,
    prompt\_template\_str\=prompt\_template\_str,
    verbose\=True,
)

prompt\_template\_str = """\\ Generate an example album, with an artist and a list of songs. \\ Using the movie {movie\_name} as inspiration.\\ """ llm = OpenAI(model="gpt-3.5-turbo") program = FunctionCallingProgram.from\_defaults( output\_cls=Album, prompt\_template\_str=prompt\_template\_str, verbose=True, )

Run program to get structured output.

In \[ \]:

Copied!

output \= program(movie\_name\="The Shining")

output = program(movie\_name="The Shining")

\
Calling function: Album with args: {"name": "The Shining Soundtrack", "artist": "Various Artists", "songs": \[{"title": "Main Title", "length\_seconds": 180}, {"title": "Rocky Mountains", "length\_seconds": 240}, {"title": "Lullaby", "length\_seconds": 200}, {"title": "The Overlook Hotel", "length\_seconds": 220}, {"title": "Grady's Story", "length\_seconds": 180}, {"title": "The Maze", "length\_seconds": 210}\]}

name='The Shining Soundtrack' artist='Various Artists' songs=\[Song(title='Main Title', length\_seconds=180), Song(title='Rocky Mountains', length\_seconds=240), Song(title='Lullaby', length\_seconds=200), Song(title='The Overlook Hotel', length\_seconds=220), Song(title="Grady's Story", length\_seconds=180), Song(title='The Maze', length\_seconds=210)\]

The output is a valid Pydantic object that we can then use to call functions/APIs.

In \[ \]:

Copied!

output

output

Out\[ \]:

Album(name='The Shining Soundtrack', artist='Various Artists', songs=\[Song(title='Main Title', length\_seconds=180), Song(title='Rocky Mountains', length\_seconds=240), Song(title='Lullaby', length\_seconds=200), Song(title='The Overlook Hotel', length\_seconds=220), Song(title="Grady's Story", length\_seconds=180), Song(title='The Maze', length\_seconds=210)\])

#### Function Calling (Parallel Function Calling, Multiple Objects)[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/function_program/#function-calling-parallel-function-calling-multiple-objects)

In \[ \]:

Copied!

prompt\_template\_str \= """\\
Generate example albums, with an artist and a list of songs, using each movie below as inspiration. \\

Here are the movies:
{movie\_names}
"""
llm \= OpenAI(model\="gpt-3.5-turbo")

program \= FunctionCallingProgram.from\_defaults(
    output\_cls\=Album,
    prompt\_template\_str\=prompt\_template\_str,
    verbose\=True,
    allow\_parallel\_tool\_calls\=True,
)
output \= program(movie\_names\="The Shining, The Blair Witch Project, Saw")

prompt\_template\_str = """\\ Generate example albums, with an artist and a list of songs, using each movie below as inspiration. \\ Here are the movies: {movie\_names} """ llm = OpenAI(model="gpt-3.5-turbo") program = FunctionCallingProgram.from\_defaults( output\_cls=Album, prompt\_template\_str=prompt\_template\_str, verbose=True, allow\_parallel\_tool\_calls=True, ) output = program(movie\_names="The Shining, The Blair Witch Project, Saw")

\
Calling function: Album with args: {"name": "The Shining", "artist": "Various Artists", "songs": \[{"title": "Main Theme", "length\_seconds": 180}, {"title": "The Overlook Hotel", "length\_seconds": 240}, {"title": "Redrum", "length\_seconds": 200}\]}

name='The Shining' artist='Various Artists' songs=\[Song(title='Main Theme', length\_seconds=180), Song(title='The Overlook Hotel', length\_seconds=240), Song(title='Redrum', length\_seconds=200)\]

Calling function: Album with args: {"name": "The Blair Witch Project", "artist": "Soundtrack Ensemble", "songs": \[{"title": "Into the Woods", "length\_seconds": 210}, {"title": "The Rustling Leaves", "length\_seconds": 180}, {"title": "The Witch's Curse", "length\_seconds": 240}\]}

name='The Blair Witch Project' artist='Soundtrack Ensemble' songs=\[Song(title='Into the Woods', length\_seconds=210), Song(title='The Rustling Leaves', length\_seconds=180), Song(title="The Witch's Curse", length\_seconds=240)\]

Calling function: Album with args: {"name": "Saw", "artist": "Horror Soundscapes", "songs": \[{"title": "The Reverse Bear Trap", "length\_seconds": 220}, {"title": "Jigsaw's Game", "length\_seconds": 260}, {"title": "Bathroom Escape", "length\_seconds": 180}\]}

name='Saw' artist='Horror Soundscapes' songs=\[Song(title='The Reverse Bear Trap', length\_seconds=220), Song(title="Jigsaw's Game", length\_seconds=260), Song(title='Bathroom Escape', length\_seconds=180)\]

In \[ \]:

Copied!

output

output

Out\[ \]:

\[Album(name='The Shining', artist='Various Artists', songs=\[Song(title='Main Theme', length\_seconds=180), Song(title='The Overlook Hotel', length\_seconds=240), Song(title='Redrum', length\_seconds=200)\]),
 Album(name='The Blair Witch Project', artist='Soundtrack Ensemble', songs=\[Song(title='Into the Woods', length\_seconds=210), Song(title='The Rustling Leaves', length\_seconds=180), Song(title="The Witch's Curse", length\_seconds=240)\]),
 Album(name='Saw', artist='Horror Soundscapes', songs=\[Song(title='The Reverse Bear Trap', length\_seconds=220), Song(title="Jigsaw's Game", length\_seconds=260), Song(title='Bathroom Escape', length\_seconds=180)\])\]

### Function Calling Program with Anthropic[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/function_program/#function-calling-program-with-anthropic)

Here we use Claude Sonnet (all three models support function calling).

In \[ \]:

Copied!

from llama\_index.core.program import FunctionCallingProgram
from llama\_index.llms.anthropic import Anthropic

from llama\_index.core.program import FunctionCallingProgram from llama\_index.llms.anthropic import Anthropic

In \[ \]:

Copied!

prompt\_template\_str \= "Generate a song about {topic}."
llm \= Anthropic(model\="claude-3-sonnet-20240229")

program \= FunctionCallingProgram.from\_defaults(
    output\_cls\=Song,
    prompt\_template\_str\=prompt\_template\_str,
    llm\=llm,
    verbose\=True,
)

prompt\_template\_str = "Generate a song about {topic}." llm = Anthropic(model="claude-3-sonnet-20240229") program = FunctionCallingProgram.from\_defaults( output\_cls=Song, prompt\_template\_str=prompt\_template\_str, llm=llm, verbose=True, )

In \[ \]:

Copied!

output \= program(topic\="harry potter")

output = program(topic="harry potter")

\
Calling function: Song with args: {"title": "The Boy Who Lived", "length\_seconds": 180}

title='The Boy Who Lived' length\_seconds=180

In \[ \]:

Copied!

output

output

Out\[ \]:

Song(title='The Boy Who Lived', length\_seconds=180)

### Function Calling Program with Mistral[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/function_program/#function-calling-program-with-mistral)

Here we use mistral-large.

In \[ \]:

Copied!

from llama\_index.core.program import FunctionCallingProgram
from llama\_index.llms.mistralai import MistralAI

from llama\_index.core.program import FunctionCallingProgram from llama\_index.llms.mistralai import MistralAI

In \[ \]:

Copied!

\# prompt\_template\_str = """\\
\# Generate an example album, with an artist and a list of songs. \\
\# Use the broadway show {broadway\_show} as inspiration. \\
\# Make sure to use the tool.
\# """
prompt\_template\_str \= "Generate a song about {topic}."
llm \= MistralAI(model\="mistral-large-latest")
program \= FunctionCallingProgram.from\_defaults(
    output\_cls\=Song,
    prompt\_template\_str\=prompt\_template\_str,
    llm\=llm,
    verbose\=True,
)

\# prompt\_template\_str = """\\ # Generate an example album, with an artist and a list of songs. \\ # Use the broadway show {broadway\_show} as inspiration. \\ # Make sure to use the tool. # """ prompt\_template\_str = "Generate a song about {topic}." llm = MistralAI(model="mistral-large-latest") program = FunctionCallingProgram.from\_defaults( output\_cls=Song, prompt\_template\_str=prompt\_template\_str, llm=llm, verbose=True, )

In \[ \]:

Copied!

output \= program(topic\="the broadway show Wicked")

output = program(topic="the broadway show Wicked")

\
Calling function: Song with args: {"title": "Defying Gravity", "length\_seconds": 240}

title='Defying Gravity' length\_seconds=240

In \[ \]:

Copied!

output

output

Out\[ \]:

Song(title='Defying Gravity', length\_seconds=240)

In \[ \]:

Copied!

from llama\_index.core.output\_parsers import PydanticOutputParser

program \= LLMTextCompletionProgram.from\_defaults(
    output\_parser\=PydanticOutputParser(output\_cls\=Album),
    prompt\_template\_str\=prompt\_template\_str,
    verbose\=True,
)

from llama\_index.core.output\_parsers import PydanticOutputParser program = LLMTextCompletionProgram.from\_defaults( output\_parser=PydanticOutputParser(output\_cls=Album), prompt\_template\_str=prompt\_template\_str, verbose=True, )

In \[ \]:

Copied!

output \= program(movie\_name\="Lord of the Rings")
output

output = program(movie\_name="Lord of the Rings") output

Out\[ \]:

Album(name='The Fellowship of the Ring', artist='Middle-earth Ensemble', songs=\[Song(title='The Shire', length\_seconds=240), Song(title='Concerning Hobbits', length\_seconds=180), Song(title='The Ring Goes South', length\_seconds=300), Song(title='A Knife in the Dark', length\_seconds=270), Song(title='Flight to the Ford', length\_seconds=210), Song(title='Many Meetings', length\_seconds=240), Song(title='The Council of Elrond', length\_seconds=330), Song(title='The Great Eye', length\_seconds=180), Song(title='The Breaking of the Fellowship', length\_seconds=360)\])

Back to top

[Previous Evaporate Demo](https://docs.llamaindex.ai/en/stable/examples/output_parsing/evaporate_program/)[Next Guidance Pydantic Program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/guidance_pydantic_program/)

Hi, how can I help you?

🦙
