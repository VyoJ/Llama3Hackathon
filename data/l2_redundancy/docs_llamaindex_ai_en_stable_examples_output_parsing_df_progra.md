Title: DataFrame Structured Data Extraction - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/output_parsing/df_program/

Markdown Content:
DataFrame Structured Data Extraction - LlamaIndex


This demo shows how you can extract tabular DataFrames from raw text.

This was directly inspired by jxnl's dataframe example here: [https://github.com/jxnl/openai\_function\_call/blob/main/auto\_dataframe.py](https://github.com/jxnl/openai_function_call/blob/main/auto_dataframe.py).

We show this with different levels of complexity, all backed by the OpenAI Function API:

*   (more code) How to build an extractor yourself using our OpenAIPydanticProgram
*   (less code) Using our out-of-the-box `DFFullProgram` and `DFRowsProgram` objects

Build a DF Extractor Yourself (Using OpenAIPydanticProgram)[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/df_program/#build-a-df-extractor-yourself-using-openaipydanticprogram)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Our OpenAIPydanticProgram is a wrapper around an OpenAI LLM that supports function calling - it will return structured outputs in the form of a Pydantic object.

We import our `DataFrame` and `DataFrameRowsOnly` objects.

To create an output extractor, you just need to 1) specify the relevant Pydantic object, and 2) Add the right prompt

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai
%pip install llama\-index\-program\-openai

%pip install llama-index-llms-openai %pip install llama-index-program-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

from llama\_index.program.openai import OpenAIPydanticProgram
from llama\_index.core.program import (
    DFFullProgram,
    DataFrame,
    DataFrameRowsOnly,
)
from llama\_index.llms.openai import OpenAI

from llama\_index.program.openai import OpenAIPydanticProgram from llama\_index.core.program import ( DFFullProgram, DataFrame, DataFrameRowsOnly, ) from llama\_index.llms.openai import OpenAI

In \[ \]:

Copied!

program \= OpenAIPydanticProgram.from\_defaults(
    output\_cls\=DataFrame,
    llm\=OpenAI(temperature\=0, model\="gpt-4-0613"),
    prompt\_template\_str\=(
        "Please extract the following query into a structured data according"
        " to: {input\_str}.Please extract both the set of column names and a"
        " set of rows."
    ),
    verbose\=True,
)

program = OpenAIPydanticProgram.from\_defaults( output\_cls=DataFrame, llm=OpenAI(temperature=0, model="gpt-4-0613"), prompt\_template\_str=( "Please extract the following query into a structured data according" " to: {input\_str}.Please extract both the set of column names and a" " set of rows." ), verbose=True, )

In \[ \]:

Copied!

\# NOTE: the test example is taken from jxnl's repo

response\_obj \= program(
    input\_str\="""My name is John and I am 25 years old. I live in 
        New York and I like to play basketball. His name is 
        Mike and he is 30 years old. He lives in San Francisco 
        and he likes to play baseball. Sarah is 20 years old 
        and she lives in Los Angeles. She likes to play tennis.
        Her name is Mary and she is 35 years old. 
        She lives in Chicago."""
)
response\_obj

\# NOTE: the test example is taken from jxnl's repo response\_obj = program( input\_str="""My name is John and I am 25 years old. I live in New York and I like to play basketball. His name is Mike and he is 30 years old. He lives in San Francisco and he likes to play baseball. Sarah is 20 years old and she lives in Los Angeles. She likes to play tennis. Her name is Mary and she is 35 years old. She lives in Chicago.""" ) response\_obj

Function call: DataFrame with args: {
  "columns": \[
    {
      "column\_name": "Name",
      "column\_desc": "Name of the person"
    },
    {
      "column\_name": "Age",
      "column\_desc": "Age of the person"
    },
    {
      "column\_name": "City",
      "column\_desc": "City where the person lives"
    },
    {
      "column\_name": "Hobby",
      "column\_desc": "What the person likes to do"
    }
  \],
  "rows": \[
    {
      "row\_values": \["John", 25, "New York", "play basketball"\]
    },
    {
      "row\_values": \["Mike", 30, "San Francisco", "play baseball"\]
    },
    {
      "row\_values": \["Sarah", 20, "Los Angeles", "play tennis"\]
    },
    {
      "row\_values": \["Mary", 35, "Chicago", "play tennis"\]
    }
  \]
}

Out\[ \]:

DataFrame(description=None, columns=\[DataFrameColumn(column\_name='Name', column\_desc='Name of the person'), DataFrameColumn(column\_name='Age', column\_desc='Age of the person'), DataFrameColumn(column\_name='City', column\_desc='City where the person lives'), DataFrameColumn(column\_name='Hobby', column\_desc='What the person likes to do')\], rows=\[DataFrameRow(row\_values=\['John', 25, 'New York', 'play basketball'\]), DataFrameRow(row\_values=\['Mike', 30, 'San Francisco', 'play baseball'\]), DataFrameRow(row\_values=\['Sarah', 20, 'Los Angeles', 'play tennis'\]), DataFrameRow(row\_values=\['Mary', 35, 'Chicago', 'play tennis'\])\])

In \[ \]:

Copied!

program \= OpenAIPydanticProgram.from\_defaults(
    output\_cls\=DataFrameRowsOnly,
    llm\=OpenAI(temperature\=0, model\="gpt-4-0613"),
    prompt\_template\_str\=(
        "Please extract the following text into a structured data:"
        " {input\_str}. The column names are the following: \['Name', 'Age',"
        " 'City', 'Favorite Sport'\]. Do not specify additional parameters that"
        " are not in the function schema. "
    ),
    verbose\=True,
)

program = OpenAIPydanticProgram.from\_defaults( output\_cls=DataFrameRowsOnly, llm=OpenAI(temperature=0, model="gpt-4-0613"), prompt\_template\_str=( "Please extract the following text into a structured data:" " {input\_str}. The column names are the following: \['Name', 'Age'," " 'City', 'Favorite Sport'\]. Do not specify additional parameters that" " are not in the function schema. " ), verbose=True, )

In \[ \]:

Copied!

program(
    input\_str\="""My name is John and I am 25 years old. I live in 
        New York and I like to play basketball. His name is 
        Mike and he is 30 years old. He lives in San Francisco 
        and he likes to play baseball. Sarah is 20 years old 
        and she lives in Los Angeles. She likes to play tennis.
        Her name is Mary and she is 35 years old. 
        She lives in Chicago."""
)

program( input\_str="""My name is John and I am 25 years old. I live in New York and I like to play basketball. His name is Mike and he is 30 years old. He lives in San Francisco and he likes to play baseball. Sarah is 20 years old and she lives in Los Angeles. She likes to play tennis. Her name is Mary and she is 35 years old. She lives in Chicago.""" )

Function call: DataFrameRowsOnly with args: {
  "rows": \[
    {
      "row\_values": \["John", 25, "New York", "basketball"\]
    },
    {
      "row\_values": \["Mike", 30, "San Francisco", "baseball"\]
    },
    {
      "row\_values": \["Sarah", 20, "Los Angeles", "tennis"\]
    },
    {
      "row\_values": \["Mary", 35, "Chicago", ""\]
    }
  \]
}

Out\[ \]:

DataFrameRowsOnly(rows=\[DataFrameRow(row\_values=\['John', 25, 'New York', 'basketball'\]), DataFrameRow(row\_values=\['Mike', 30, 'San Francisco', 'baseball'\]), DataFrameRow(row\_values=\['Sarah', 20, 'Los Angeles', 'tennis'\]), DataFrameRow(row\_values=\['Mary', 35, 'Chicago', ''\])\])

Use our DataFrame Programs[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/df_program/#use-our-dataframe-programs)
----------------------------------------------------------------------------------------------------------------------------------

We provide convenience wrappers for `DFFullProgram` and `DFRowsProgram`. This allows a simpler object creation interface than specifying all details through the `OpenAIPydanticProgram`.

In \[ \]:

Copied!

from llama\_index.program.openai import OpenAIPydanticProgram
from llama\_index.core.program import DFFullProgram, DFRowsProgram
import pandas as pd

\# initialize empty df
df \= pd.DataFrame(
    {
        "Name": pd.Series(dtype\="str"),
        "Age": pd.Series(dtype\="int"),
        "City": pd.Series(dtype\="str"),
        "Favorite Sport": pd.Series(dtype\="str"),
    }
)

\# initialize program, using existing df as schema
df\_rows\_program \= DFRowsProgram.from\_defaults(
    pydantic\_program\_cls\=OpenAIPydanticProgram, df\=df
)

from llama\_index.program.openai import OpenAIPydanticProgram from llama\_index.core.program import DFFullProgram, DFRowsProgram import pandas as pd # initialize empty df df = pd.DataFrame( { "Name": pd.Series(dtype="str"), "Age": pd.Series(dtype="int"), "City": pd.Series(dtype="str"), "Favorite Sport": pd.Series(dtype="str"), } ) # initialize program, using existing df as schema df\_rows\_program = DFRowsProgram.from\_defaults( pydantic\_program\_cls=OpenAIPydanticProgram, df=df )

In \[ \]:

Copied!

\# parse text, using existing df as schema
result\_obj \= df\_rows\_program(
    input\_str\="""My name is John and I am 25 years old. I live in 
        New York and I like to play basketball. His name is 
        Mike and he is 30 years old. He lives in San Francisco 
        and he likes to play baseball. Sarah is 20 years old 
        and she lives in Los Angeles. She likes to play tennis.
        Her name is Mary and she is 35 years old. 
        She lives in Chicago."""
)

\# parse text, using existing df as schema result\_obj = df\_rows\_program( input\_str="""My name is John and I am 25 years old. I live in New York and I like to play basketball. His name is Mike and he is 30 years old. He lives in San Francisco and he likes to play baseball. Sarah is 20 years old and she lives in Los Angeles. She likes to play tennis. Her name is Mary and she is 35 years old. She lives in Chicago.""" )

In \[ \]:

Copied!

result\_obj.to\_df(existing\_df\=df)

result\_obj.to\_df(existing\_df=df)

/Users/jerryliu/Programming/gpt\_index/llama\_index/program/predefined/df.py:65: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
  return existing\_df.append(new\_df, ignore\_index=True)

Out\[ \]:

|  | Name | Age | City | Favorite Sport |
| --- | --- | --- | --- | --- |
| 0 | John | 25 | New York | Basketball |
| 1 | Mike | 30 | San Francisco | Baseball |
| 2 | Sarah | 20 | Los Angeles | Tennis |
| 3 | Mary | 35 | Chicago |  |

In \[ \]:

Copied!

\# initialize program that can do joint schema extraction and structured data extraction
df\_full\_program \= DFFullProgram.from\_defaults(
    pydantic\_program\_cls\=OpenAIPydanticProgram,
)

\# initialize program that can do joint schema extraction and structured data extraction df\_full\_program = DFFullProgram.from\_defaults( pydantic\_program\_cls=OpenAIPydanticProgram, )

In \[ \]:

Copied!

result\_obj \= df\_full\_program(
    input\_str\="""My name is John and I am 25 years old. I live in 
        New York and I like to play basketball. His name is 
        Mike and he is 30 years old. He lives in San Francisco 
        and he likes to play baseball. Sarah is 20 years old 
        and she lives in Los Angeles. She likes to play tennis.
        Her name is Mary and she is 35 years old. 
        She lives in Chicago."""
)

result\_obj = df\_full\_program( input\_str="""My name is John and I am 25 years old. I live in New York and I like to play basketball. His name is Mike and he is 30 years old. He lives in San Francisco and he likes to play baseball. Sarah is 20 years old and she lives in Los Angeles. She likes to play tennis. Her name is Mary and she is 35 years old. She lives in Chicago.""" )

In \[ \]:

Copied!

result\_obj.to\_df()

result\_obj.to\_df()

Out\[ \]:

|  | Name | Age | Location | Hobby |
| --- | --- | --- | --- | --- |
| 0 | John | 25 | New York | Basketball |
| 1 | Mike | 30 | San Francisco | Baseball |
| 2 | Sarah | 20 | Los Angeles | Tennis |
| 3 | Mary | 35 | Chicago |  |

In \[ \]:

Copied!

\# initialize empty df
df \= pd.DataFrame(
    {
        "City": pd.Series(dtype\="str"),
        "State": pd.Series(dtype\="str"),
        "Population": pd.Series(dtype\="int"),
    }
)

\# initialize program, using existing df as schema
df\_rows\_program \= DFRowsProgram.from\_defaults(
    pydantic\_program\_cls\=OpenAIPydanticProgram, df\=df
)

\# initialize empty df df = pd.DataFrame( { "City": pd.Series(dtype="str"), "State": pd.Series(dtype="str"), "Population": pd.Series(dtype="int"), } ) # initialize program, using existing df as schema df\_rows\_program = DFRowsProgram.from\_defaults( pydantic\_program\_cls=OpenAIPydanticProgram, df=df )

In \[ \]:

Copied!

input\_text \= """San Francisco is in California, has a population of 800,000. 
New York City is the most populous city in the United States. \\
With a 2020 population of 8,804,190 distributed over 300.46 square miles (778.2 km2), \\
New York City is the most densely populated major city in the United States.
New York City is in New York State.
Boston (US: /ˈbɔːstən/),\[8\] officially the City of Boston, is the capital and largest city of the Commonwealth of Massachusetts \\
and the cultural and financial center of the New England region of the Northeastern United States. \\
The city boundaries encompass an area of about 48.4 sq mi (125 km2)\[9\] and a population of 675,647 as of 2020.\[4\]
"""

\# parse text, using existing df as schema
result\_obj \= df\_rows\_program(input\_str\=input\_text)

input\_text = """San Francisco is in California, has a population of 800,000. New York City is the most populous city in the United States. \\ With a 2020 population of 8,804,190 distributed over 300.46 square miles (778.2 km2), \\ New York City is the most densely populated major city in the United States. New York City is in New York State. Boston (US: /ˈbɔːstən/),\[8\] officially the City of Boston, is the capital and largest city of the Commonwealth of Massachusetts \\ and the cultural and financial center of the New England region of the Northeastern United States. \\ The city boundaries encompass an area of about 48.4 sq mi (125 km2)\[9\] and a population of 675,647 as of 2020.\[4\] """ # parse text, using existing df as schema result\_obj = df\_rows\_program(input\_str=input\_text)

In \[ \]:

Copied!

new\_df \= result\_obj.to\_df(existing\_df\=df)
new\_df

new\_df = result\_obj.to\_df(existing\_df=df) new\_df

/Users/jerryliu/Programming/gpt\_index/llama\_index/program/predefined/df.py:65: FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
  return existing\_df.append(new\_df, ignore\_index=True)

Out\[ \]:

|  | City | State | Population |
| --- | --- | --- | --- |
| 0 | San Francisco | California | 800000 |
| 1 | New York City | New York | 8804190 |
| 2 | Boston | Massachusetts | 675647 |

Back to top

[Previous Langchain Output Parsing](https://docs.llamaindex.ai/en/stable/examples/output_parsing/LangchainOutputParserDemo/)[Next Evaporate Demo](https://docs.llamaindex.ai/en/stable/examples/output_parsing/evaporate_program/)

Hi, how can I help you?

🦙
