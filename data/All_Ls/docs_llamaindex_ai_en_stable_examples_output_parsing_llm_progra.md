Title: LLM Pydantic Program - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/output_parsing/llm_program/

Markdown Content:
LLM Pydantic Program - LlamaIndex


This guide shows you how to generate structured data with our `LLMTextCompletionProgram`. Given an LLM as well as an output Pydantic class, generate a structured Pydantic object.

In terms of the target object, you can choose to directly specify `output_cls`, or specify a `PydanticOutputParser` or any other BaseOutputParser that generates a Pydantic object.

in the examples below, we show you different ways of extracting into the `Album` object (which can contain a list of Song objects)

Extract into `Album` class[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/llm_program/#extract-into-album-class)
---------------------------------------------------------------------------------------------------------------------------------

This is a simple example of parsing an output into an `Album` schema, which can contain multiple songs.

Just pass `Album` into the `output_cls` property on initialization of the `LLMTextCompletionProgram`.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

from pydantic import BaseModel
from typing import List

from llama\_index.core.program import LLMTextCompletionProgram

from pydantic import BaseModel from typing import List from llama\_index.core.program import LLMTextCompletionProgram

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

Define LLM pydantic program

In \[ \]:

Copied!

from llama\_index.core.program import LLMTextCompletionProgram

from llama\_index.core.program import LLMTextCompletionProgram

In \[ \]:

Copied!

prompt\_template\_str \= """\\
Generate an example album, with an artist and a list of songs. \\
Using the movie {movie\_name} as inspiration.\\
"""
program \= LLMTextCompletionProgram.from\_defaults(
    output\_cls\=Album,
    prompt\_template\_str\=prompt\_template\_str,
    verbose\=True,
)

prompt\_template\_str = """\\ Generate an example album, with an artist and a list of songs. \\ Using the movie {movie\_name} as inspiration.\\ """ program = LLMTextCompletionProgram.from\_defaults( output\_cls=Album, prompt\_template\_str=prompt\_template\_str, verbose=True, )

Run program to get structured output.

In \[ \]:

Copied!

output \= program(movie\_name\="The Shining")

output = program(movie\_name="The Shining")

The output is a valid Pydantic object that we can then use to call functions/APIs.

In \[ \]:

Copied!

output

output

Out\[ \]:

Album(name='The Overlook', artist='Jack Torrance', songs=\[Song(title='Redrum', length\_seconds=240), Song(title="Here's Johnny", length\_seconds=180), Song(title='Room 237', length\_seconds=300), Song(title='All Work and No Play', length\_seconds=210), Song(title='The Maze', length\_seconds=270)\])

### Initialize with Pydantic Output Parser[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/llm_program/#initialize-with-pydantic-output-parser)

The above is equivalent to defining a Pydantic output parser and passing that in instead of the `output_cls` directly.

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

Define a Custom Output Parser[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/llm_program/#define-a-custom-output-parser)
-----------------------------------------------------------------------------------------------------------------------------------------

Sometimes you may want to parse an output your own way into a JSON object.

In \[ \]:

Copied!

from llama\_index.core.output\_parsers import ChainableOutputParser

class CustomAlbumOutputParser(ChainableOutputParser):
    """Custom Album output parser.

    Assume first line is name and artist.

    Assume each subsequent line is the song.

    """

    def \_\_init\_\_(self, verbose: bool \= False):
        self.verbose \= verbose

    def parse(self, output: str) \-> Album:
        """Parse output."""
        if self.verbose:
            print(f"> Raw output: {output}")
        lines \= output.split("\\n")
        name, artist \= lines\[0\].split(",")
        songs \= \[\]
        for i in range(1, len(lines)):
            title, length\_seconds \= lines\[i\].split(",")
            songs.append(Song(title\=title, length\_seconds\=length\_seconds))

        return Album(name\=name, artist\=artist, songs\=songs)

from llama\_index.core.output\_parsers import ChainableOutputParser class CustomAlbumOutputParser(ChainableOutputParser): """Custom Album output parser. Assume first line is name and artist. Assume each subsequent line is the song. """ def \_\_init\_\_(self, verbose: bool = False): self.verbose = verbose def parse(self, output: str) -> Album: """Parse output.""" if self.verbose: print(f"> Raw output: {output}") lines = output.split("\\n") name, artist = lines\[0\].split(",") songs = \[\] for i in range(1, len(lines)): title, length\_seconds = lines\[i\].split(",") songs.append(Song(title=title, length\_seconds=length\_seconds)) return Album(name=name, artist=artist, songs=songs)

In \[ \]:

Copied!

prompt\_template\_str \= """\\
Generate an example album, with an artist and a list of songs. \\
Using the movie {movie\_name} as inspiration.\\

Return answer in following format.
The first line is:
<album\_name>, <album\_artist>
Every subsequent line is a song with format:
<song\_title>, <song\_length\_seconds>

"""
program \= LLMTextCompletionProgram.from\_defaults(
    output\_parser\=CustomAlbumOutputParser(verbose\=True),
    output\_cls\=Album,
    prompt\_template\_str\=prompt\_template\_str,
    verbose\=True,
)

prompt\_template\_str = """\\ Generate an example album, with an artist and a list of songs. \\ Using the movie {movie\_name} as inspiration.\\ Return answer in following format. The first line is: , Every subsequent line is a song with format: , """ program = LLMTextCompletionProgram.from\_defaults( output\_parser=CustomAlbumOutputParser(verbose=True), output\_cls=Album, prompt\_template\_str=prompt\_template\_str, verbose=True, )

In \[ \]:

Copied!

output \= program(movie\_name\="The Dark Knight")

output = program(movie\_name="The Dark Knight")

\> Raw output: Gotham's Reckoning, The Dark Knight
A Dark Knight Rises, 240
The Joker's Symphony, 180
Harvey Dent's Lament, 210
Gotham's Guardian, 195
The Batmobile Chase, 225
The Dark Knight's Theme, 150
The Joker's Mind Games, 180
Rachel's Tragedy, 210
Gotham's Last Stand, 240
The Dark Knight's Triumph, 180

In \[ \]:

Copied!

output

output

Out\[ \]:

Album(name="Gotham's Reckoning", artist=' The Dark Knight', songs=\[Song(title='A Dark Knight Rises', length\_seconds=240), Song(title="The Joker's Symphony", length\_seconds=180), Song(title="Harvey Dent's Lament", length\_seconds=210), Song(title="Gotham's Guardian", length\_seconds=195), Song(title='The Batmobile Chase', length\_seconds=225), Song(title="The Dark Knight's Theme", length\_seconds=150), Song(title="The Joker's Mind Games", length\_seconds=180), Song(title="Rachel's Tragedy", length\_seconds=210), Song(title="Gotham's Last Stand", length\_seconds=240), Song(title="The Dark Knight's Triumph", length\_seconds=180)\])

Back to top

[Previous Guidance for Sub-Question Query Engine](https://docs.llamaindex.ai/en/stable/examples/output_parsing/guidance_sub_question/)[Next LM Format Enforcer Pydantic Program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/lmformatenforcer_pydantic_program/)

Hi, how can I help you?

🦙
