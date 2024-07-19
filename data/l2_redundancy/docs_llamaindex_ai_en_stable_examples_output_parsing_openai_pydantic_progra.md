Title: OpenAI Pydantic Program - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/output_parsing/openai_pydantic_program/

Markdown Content:
OpenAI Pydantic Program - LlamaIndex


This guide shows you how to generate structured data with [new OpenAI API](https://openai.com/blog/function-calling-and-other-api-updates) via LlamaIndex. The user just needs to specify a Pydantic object.

We demonstrate two settings:

*   Extraction into an `Album` object (which can contain a list of Song objects)
*   Extraction into a `DirectoryTree` object (which can contain recursive Node objects)

Extraction into `Album`[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/openai_pydantic_program/#extraction-into-album)
---------------------------------------------------------------------------------------------------------------------------------------

This is a simple example of parsing an output into an `Album` schema, which can contain multiple songs.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai
%pip install llama\-index\-program\-openai

%pip install llama-index-llms-openai %pip install llama-index-program-openai

In \[ \]:

Copied!

%pip install llama\-index

%pip install llama-index

In \[ \]:

Copied!

from pydantic import BaseModel
from typing import List

from llama\_index.program.openai import OpenAIPydanticProgram

from pydantic import BaseModel from typing import List from llama\_index.program.openai import OpenAIPydanticProgram

### Without docstring in Model[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/openai_pydantic_program/#without-docstring-in-model)

Define output schema (without docstring)

In \[ \]:

Copied!

class Song(BaseModel):
    title: str
    length\_seconds: int

class Album(BaseModel):
    name: str
    artist: str
    songs: List\[Song\]

class Song(BaseModel): title: str length\_seconds: int class Album(BaseModel): name: str artist: str songs: List\[Song\]

Define openai pydantic program

In \[ \]:

Copied!

prompt\_template\_str \= """\\
Generate an example album, with an artist and a list of songs. \\
Using the movie {movie\_name} as inspiration.\\
"""
program \= OpenAIPydanticProgram.from\_defaults(
    output\_cls\=Album, prompt\_template\_str\=prompt\_template\_str, verbose\=True
)

prompt\_template\_str = """\\ Generate an example album, with an artist and a list of songs. \\ Using the movie {movie\_name} as inspiration.\\ """ program = OpenAIPydanticProgram.from\_defaults( output\_cls=Album, prompt\_template\_str=prompt\_template\_str, verbose=True )

Run program to get structured output.

In \[ \]:

Copied!

output \= program(
    movie\_name\="The Shining", description\="Data model for an album."
)

output = program( movie\_name="The Shining", description="Data model for an album." )

Function call: Album with args: {
  "name": "The Shining",
  "artist": "Various Artists",
  "songs": \[
    {
      "title": "Main Title",
      "length\_seconds": 180
    },
    {
      "title": "Opening Credits",
      "length\_seconds": 120
    },
    {
      "title": "The Overlook Hotel",
      "length\_seconds": 240
    },
    {
      "title": "Redrum",
      "length\_seconds": 150
    },
    {
      "title": "Here's Johnny!",
      "length\_seconds": 200
    }
  \]
}

### With docstring in Model[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/openai_pydantic_program/#with-docstring-in-model)

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

In \[ \]:

Copied!

prompt\_template\_str \= """\\
Generate an example album, with an artist and a list of songs. \\
Using the movie {movie\_name} as inspiration.\\
"""
program \= OpenAIPydanticProgram.from\_defaults(
    output\_cls\=Album, prompt\_template\_str\=prompt\_template\_str, verbose\=True
)

prompt\_template\_str = """\\ Generate an example album, with an artist and a list of songs. \\ Using the movie {movie\_name} as inspiration.\\ """ program = OpenAIPydanticProgram.from\_defaults( output\_cls=Album, prompt\_template\_str=prompt\_template\_str, verbose=True )

Run program to get structured output.

In \[ \]:

Copied!

output \= program(movie\_name\="The Shining")

output = program(movie\_name="The Shining")

Function call: Album with args: {
  "name": "The Shining",
  "artist": "Various Artists",
  "songs": \[
    {
      "title": "Main Title",
      "length\_seconds": 180
    },
    {
      "title": "Opening Credits",
      "length\_seconds": 120
    },
    {
      "title": "The Overlook Hotel",
      "length\_seconds": 240
    },
    {
      "title": "Redrum",
      "length\_seconds": 150
    },
    {
      "title": "Here's Johnny",
      "length\_seconds": 200
    }
  \]
}

The output is a valid Pydantic object that we can then use to call functions/APIs.

In \[ \]:

Copied!

output

output

Out\[ \]:

Album(name='The Shining', artist='Various Artists', songs=\[Song(title='Main Title', length\_seconds=180), Song(title='Opening Credits', length\_seconds=120), Song(title='The Overlook Hotel', length\_seconds=240), Song(title='Redrum', length\_seconds=150), Song(title="Here's Johnny", length\_seconds=200)\])

Stream partial intermediate Pydantic Objects[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/openai_pydantic_program/#stream-partial-intermediate-pydantic-objects)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Instead of waiting for the Function Call to generate the entire JSON, we can use the `stream_partial_objects()` method of the `program` to stream valid intermediate instances of the Pydantic Output class as soon as they're available 🔥

First let's define the Output Pydantic class

In \[ \]:

Copied!

from pydantic import BaseModel, Field

class CharacterInfo(BaseModel):
    """Information about a character."""

    character\_name: str
    name: str \= Field(..., description\="Name of the actor/actress")
    hometown: str

class Characters(BaseModel):
    """List of characters."""

    characters: list\[CharacterInfo\] \= Field(default\_factory\=list)

from pydantic import BaseModel, Field class CharacterInfo(BaseModel): """Information about a character.""" character\_name: str name: str = Field(..., description="Name of the actor/actress") hometown: str class Characters(BaseModel): """List of characters.""" characters: list\[CharacterInfo\] = Field(default\_factory=list)

Now we'll initialilze the program with prompt template

In \[ \]:

Copied!

from llama\_index.program.openai import OpenAIPydanticProgram

prompt\_template\_str \= "Information about 3 characters from the movie: {movie}"

program \= OpenAIPydanticProgram.from\_defaults(
    output\_cls\=Characters, prompt\_template\_str\=prompt\_template\_str
)

from llama\_index.program.openai import OpenAIPydanticProgram prompt\_template\_str = "Information about 3 characters from the movie: {movie}" program = OpenAIPydanticProgram.from\_defaults( output\_cls=Characters, prompt\_template\_str=prompt\_template\_str )

Finally we stream the partial objects using the `stream_partial_objects()` method

In \[ \]:

Copied!

for partial\_object in program.stream\_partial\_objects(movie\="Harry Potter"):
    \# send the partial object to the frontend for better user experience
    print(partial\_object)

for partial\_object in program.stream\_partial\_objects(movie="Harry Potter"): # send the partial object to the frontend for better user experience print(partial\_object)

Extracting List of `Album` (with Parallel Function Calling)[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/openai_pydantic_program/#extracting-list-of-album-with-parallel-function-calling)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

With the latest [parallel function calling](https://platform.openai.com/docs/guides/function-calling/parallel-function-calling) feature from OpenAI, we can simultaneously extract multiple structured data from a single prompt!

To do this, we need to:

1.  pick one of the latest models (e.g. `gpt-3.5-turbo-1106`), and
2.  set `allow_multiple` to True in our `OpenAIPydanticProgram` (if not, it will only return the first object, and raise a warning).

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI

prompt\_template\_str \= """\\
Generate 4 albums about spring, summer, fall, and winter.
"""
program \= OpenAIPydanticProgram.from\_defaults(
    output\_cls\=Album,
    llm\=OpenAI(model\="gpt-3.5-turbo-1106"),
    prompt\_template\_str\=prompt\_template\_str,
    allow\_multiple\=True,
    verbose\=True,
)

from llama\_index.llms.openai import OpenAI prompt\_template\_str = """\\ Generate 4 albums about spring, summer, fall, and winter. """ program = OpenAIPydanticProgram.from\_defaults( output\_cls=Album, llm=OpenAI(model="gpt-3.5-turbo-1106"), prompt\_template\_str=prompt\_template\_str, allow\_multiple=True, verbose=True, )

In \[ \]:

Copied!

output \= program()

output = program()

Function call: Album with args: {"name": "Spring", "artist": "Various Artists", "songs": \[{"title": "Blossom", "length\_seconds": 180}, {"title": "Sunshine", "length\_seconds": 240}, {"title": "Renewal", "length\_seconds": 200}\]}
Function call: Album with args: {"name": "Summer", "artist": "Beach Boys", "songs": \[{"title": "Beach Party", "length\_seconds": 220}, {"title": "Heatwave", "length\_seconds": 260}, {"title": "Vacation", "length\_seconds": 180}\]}
Function call: Album with args: {"name": "Fall", "artist": "Autumn Leaves", "songs": \[{"title": "Golden Days", "length\_seconds": 210}, {"title": "Harvest Moon", "length\_seconds": 240}, {"title": "Crisp Air", "length\_seconds": 190}\]}
Function call: Album with args: {"name": "Winter", "artist": "Snowflakes", "songs": \[{"title": "Frosty Morning", "length\_seconds": 190}, {"title": "Snowfall", "length\_seconds": 220}, {"title": "Cozy Nights", "length\_seconds": 250}\]}

The output is a list of valid Pydantic object.

In \[ \]:

Copied!

output

output

Out\[ \]:

\[Album(name='Spring', artist='Various Artists', songs=\[Song(title='Blossom', length\_seconds=180), Song(title='Sunshine', length\_seconds=240), Song(title='Renewal', length\_seconds=200)\]),
 Album(name='Summer', artist='Beach Boys', songs=\[Song(title='Beach Party', length\_seconds=220), Song(title='Heatwave', length\_seconds=260), Song(title='Vacation', length\_seconds=180)\]),
 Album(name='Fall', artist='Autumn Leaves', songs=\[Song(title='Golden Days', length\_seconds=210), Song(title='Harvest Moon', length\_seconds=240), Song(title='Crisp Air', length\_seconds=190)\]),
 Album(name='Winter', artist='Snowflakes', songs=\[Song(title='Frosty Morning', length\_seconds=190), Song(title='Snowfall', length\_seconds=220), Song(title='Cozy Nights', length\_seconds=250)\])\]

Extraction into `Album` (Streaming)[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/openai_pydantic_program/#extraction-into-album-streaming)
-------------------------------------------------------------------------------------------------------------------------------------------------------------

We also support streaming a list of objects through our `stream_list` function.

Full credits to this idea go to `openai_function_call` repo: [https://github.com/jxnl/openai\_function\_call/tree/main/examples/streaming\_multitask](https://github.com/jxnl/openai_function_call/tree/main/examples/streaming_multitask)

In \[ \]:

Copied!

prompt\_template\_str \= "{input\_str}"
program \= OpenAIPydanticProgram.from\_defaults(
    output\_cls\=Album,
    prompt\_template\_str\=prompt\_template\_str,
    verbose\=False,
)

output \= program.stream\_list(
    input\_str\="make up 5 random albums",
)
for obj in output:
    print(obj.json(indent\=2))

prompt\_template\_str = "{input\_str}" program = OpenAIPydanticProgram.from\_defaults( output\_cls=Album, prompt\_template\_str=prompt\_template\_str, verbose=False, ) output = program.stream\_list( input\_str="make up 5 random albums", ) for obj in output: print(obj.json(indent=2))

Extraction into `DirectoryTree` object[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/openai_pydantic_program/#extraction-into-directorytree-object)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

This is directly inspired by jxnl's awesome repo here: [https://github.com/jxnl/openai\_function\_call](https://github.com/jxnl/openai_function_call).

That repository shows how you can use OpenAI's function API to parse recursive Pydantic objects. The main requirement is that you want to "wrap" a recursive Pydantic object with a non-recursive one.

Here we show an example in a "directory" setting, where a `DirectoryTree` object wraps recursive `Node` objects, to parse a file structure.

In \[ \]:

Copied!

\# NOTE: defining recursive objects in a notebook causes errors
from directory import DirectoryTree, Node

\# NOTE: defining recursive objects in a notebook causes errors from directory import DirectoryTree, Node

In \[ \]:

Copied!

DirectoryTree.schema()

DirectoryTree.schema()

Out\[ \]:

{'title': 'DirectoryTree',
 'description': 'Container class representing a directory tree.\\n\\nArgs:\\n    root (Node): The root node of the tree.',
 'type': 'object',
 'properties': {'root': {'title': 'Root',
   'description': 'Root folder of the directory tree',
   'allOf': \[{'$ref': '#/definitions/Node'}\]}},
 'required': \['root'\],
 'definitions': {'NodeType': {'title': 'NodeType',
   'description': 'Enumeration representing the types of nodes in a filesystem.',
   'enum': \['file', 'folder'\],
   'type': 'string'},
  'Node': {'title': 'Node',
   'description': 'Class representing a single node in a filesystem. Can be either a file or a folder.\\nNote that a file cannot have children, but a folder can.\\n\\nArgs:\\n    name (str): The name of the node.\\n    children (List\[Node\]): The list of child nodes (if any).\\n    node\_type (NodeType): The type of the node, either a file or a folder.',
   'type': 'object',
   'properties': {'name': {'title': 'Name',
     'description': 'Name of the folder',
     'type': 'string'},
    'children': {'title': 'Children',
     'description': 'List of children nodes, only applicable for folders, files cannot have children',
     'type': 'array',
     'items': {'$ref': '#/definitions/Node'}},
    'node\_type': {'description': 'Either a file or folder, use the name to determine which it could be',
     'default': 'file',
     'allOf': \[{'$ref': '#/definitions/NodeType'}\]}},
   'required': \['name'\]}}}

In \[ \]:

Copied!

program \= OpenAIPydanticProgram.from\_defaults(
    output\_cls\=DirectoryTree,
    prompt\_template\_str\="{input\_str}",
    verbose\=True,
)

program = OpenAIPydanticProgram.from\_defaults( output\_cls=DirectoryTree, prompt\_template\_str="{input\_str}", verbose=True, )

In \[ \]:

Copied!

input\_str \= """
root
├── folder1
│   ├── file1.txt
│   └── file2.txt
└── folder2
    ├── file3.txt
    └── subfolder1
        └── file4.txt
"""

output \= program(input\_str\=input\_str)

input\_str = """ root ├── folder1 │ ├── file1.txt │ └── file2.txt └── folder2 ├── file3.txt └── subfolder1 └── file4.txt """ output = program(input\_str=input\_str)

Function call: DirectoryTree with args: {
  "root": {
    "name": "root",
    "children": \[
      {
        "name": "folder1",
        "children": \[
          {
            "name": "file1.txt",
            "children": \[\],
            "node\_type": "file"
          },
          {
            "name": "file2.txt",
            "children": \[\],
            "node\_type": "file"
          }
        \],
        "node\_type": "folder"
      },
      {
        "name": "folder2",
        "children": \[
          {
            "name": "file3.txt",
            "children": \[\],
            "node\_type": "file"
          },
          {
            "name": "subfolder1",
            "children": \[
              {
                "name": "file4.txt",
                "children": \[\],
                "node\_type": "file"
              }
            \],
            "node\_type": "folder"
          }
        \],
        "node\_type": "folder"
      }
    \],
    "node\_type": "folder"
  }
}

The output is a full DirectoryTree structure with recursive `Node` objects.

In \[ \]:

Copied!

output

output

Out\[ \]:

DirectoryTree(root=Node(name='root', children=\[Node(name='folder1', children=\[Node(name='file1.txt', children=\[\], node\_type=<NodeType.FILE: 'file'>), Node(name='file2.txt', children=\[\], node\_type=<NodeType.FILE: 'file'>)\], node\_type=<NodeType.FOLDER: 'folder'>), Node(name='folder2', children=\[Node(name='file3.txt', children=\[\], node\_type=<NodeType.FILE: 'file'>), Node(name='subfolder1', children=\[Node(name='file4.txt', children=\[\], node\_type=<NodeType.FILE: 'file'>)\], node\_type=<NodeType.FOLDER: 'folder'>)\], node\_type=<NodeType.FOLDER: 'folder'>)\], node\_type=<NodeType.FOLDER: 'folder'>))

Back to top

[Previous LM Format Enforcer Regular Expression Generation](https://docs.llamaindex.ai/en/stable/examples/output_parsing/lmformatenforcer_regular_expressions/)[Next OpenAI function calling for Sub-Question Query Engine](https://docs.llamaindex.ai/en/stable/examples/output_parsing/openai_sub_question/)

Hi, how can I help you?

🦙
