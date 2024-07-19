Title: Pydantic Extractor - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/PydanticExtractor/

Markdown Content:
Pydantic Extractor - LlamaIndex


Here we test out the capabilities of our `PydanticProgramExtractor` - being able to extract out an entire Pydantic object using an LLM (either a standard text completion LLM or a function calling LLM).

The advantage of this over using a "single" metadata extractor is that we can extract multiple entities with a single LLM call.

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/PydanticExtractor/#setup)
----------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

%pip install llama\-index\-readers\-web
%pip install llama\-index\-program\-openai

%pip install llama-index-readers-web %pip install llama-index-program-openai

In \[ \]:

Copied!

import nest\_asyncio

nest\_asyncio.apply()

import os
import openai

import nest\_asyncio nest\_asyncio.apply() import os import openai

In \[ \]:

Copied!

os.environ\["OPENAI\_API\_KEY"\] \= "YOUR\_API\_KEY"
openai.api\_key \= os.getenv("OPENAI\_API\_KEY")

os.environ\["OPENAI\_API\_KEY"\] = "YOUR\_API\_KEY" openai.api\_key = os.getenv("OPENAI\_API\_KEY")

### Setup the Pydantic Model[¶](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/PydanticExtractor/#setup-the-pydantic-model)

Here we define a basic structured schema that we want to extract. It contains:

*   entities: unique entities in a text chunk
*   summary: a concise summary of the text chunk
*   contains\_number: whether the chunk contains numbers

This is obviously a toy schema. We'd encourage you to be creative about the type of metadata you'd want to extract!

In \[ \]:

Copied!

from pydantic import BaseModel, Field
from typing import List

from pydantic import BaseModel, Field from typing import List

In \[ \]:

Copied!

class NodeMetadata(BaseModel):
    """Node metadata."""

    entities: List\[str\] \= Field(
        ..., description\="Unique entities in this text chunk."
    )
    summary: str \= Field(
        ..., description\="A concise summary of this text chunk."
    )
    contains\_number: bool \= Field(
        ...,
        description\=(
            "Whether the text chunk contains any numbers (ints, floats, etc.)"
        ),
    )

class NodeMetadata(BaseModel): """Node metadata.""" entities: List\[str\] = Field( ..., description="Unique entities in this text chunk." ) summary: str = Field( ..., description="A concise summary of this text chunk." ) contains\_number: bool = Field( ..., description=( "Whether the text chunk contains any numbers (ints, floats, etc.)" ), )

### Setup the Extractor[¶](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/PydanticExtractor/#setup-the-extractor)

Here we setup the metadata extractor. Note that we provide the prompt template for visibility into what's going on.

In \[ \]:

Copied!

from llama\_index.program.openai import OpenAIPydanticProgram
from llama\_index.core.extractors import PydanticProgramExtractor

EXTRACT\_TEMPLATE\_STR \= """\\
Here is the content of the section:
\----------------
{context\_str}
\----------------
Given the contextual information, extract out a {class\_name} object.\\
"""

openai\_program \= OpenAIPydanticProgram.from\_defaults(
    output\_cls\=NodeMetadata,
    prompt\_template\_str\="{input}",
    \# extract\_template\_str=EXTRACT\_TEMPLATE\_STR
)

program\_extractor \= PydanticProgramExtractor(
    program\=openai\_program, input\_key\="input", show\_progress\=True
)

from llama\_index.program.openai import OpenAIPydanticProgram from llama\_index.core.extractors import PydanticProgramExtractor EXTRACT\_TEMPLATE\_STR = """\\ Here is the content of the section: ---------------- {context\_str} ---------------- Given the contextual information, extract out a {class\_name} object.\\ """ openai\_program = OpenAIPydanticProgram.from\_defaults( output\_cls=NodeMetadata, prompt\_template\_str="{input}", # extract\_template\_str=EXTRACT\_TEMPLATE\_STR ) program\_extractor = PydanticProgramExtractor( program=openai\_program, input\_key="input", show\_progress=True )

### Load in Data[¶](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/PydanticExtractor/#load-in-data)

We load in Eugene's essay ([https://eugeneyan.com/writing/llm-patterns/](https://eugeneyan.com/writing/llm-patterns/)) using our LlamaHub SimpleWebPageReader.

In \[ \]:

Copied!

\# load in blog

from llama\_index.readers.web import SimpleWebPageReader
from llama\_index.core.node\_parser import SentenceSplitter

reader \= SimpleWebPageReader(html\_to\_text\=True)
docs \= reader.load\_data(urls\=\["https://eugeneyan.com/writing/llm-patterns/"\])

\# load in blog from llama\_index.readers.web import SimpleWebPageReader from llama\_index.core.node\_parser import SentenceSplitter reader = SimpleWebPageReader(html\_to\_text=True) docs = reader.load\_data(urls=\["https://eugeneyan.com/writing/llm-patterns/"\])

In \[ \]:

Copied!

from llama\_index.core.ingestion import IngestionPipeline

node\_parser \= SentenceSplitter(chunk\_size\=1024)

pipeline \= IngestionPipeline(transformations\=\[node\_parser, program\_extractor\])

orig\_nodes \= pipeline.run(documents\=docs)

from llama\_index.core.ingestion import IngestionPipeline node\_parser = SentenceSplitter(chunk\_size=1024) pipeline = IngestionPipeline(transformations=\[node\_parser, program\_extractor\]) orig\_nodes = pipeline.run(documents=docs)

In \[ \]:

Copied!

orig\_nodes

orig\_nodes

Extract Metadata[¶](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/PydanticExtractor/#extract-metadata)
--------------------------------------------------------------------------------------------------------------------------

Now that we've setup the metadata extractor and the data, we're ready to extract some metadata!

We see that the pydantic feature extractor is able to extract _all_ metadata from a given chunk in a single LLM call.

In \[ \]:

Copied!

sample\_entry \= program\_extractor.extract(orig\_nodes\[0:1\])\[0\]

sample\_entry = program\_extractor.extract(orig\_nodes\[0:1\])\[0\]

Extracting Pydantic object:   0%|          | 0/1 \[00:00<?, ?it/s\]

In \[ \]:

Copied!

display(sample\_entry)

display(sample\_entry)

{'entities': \['eugeneyan', 'HackerNews', 'Karpathy'\],
 'summary': 'This section discusses practical patterns for integrating large language models (LLMs) into systems & products. It introduces seven key patterns and provides information on evaluations and benchmarks in the field of language modeling.',
 'contains\_number': True}

In \[ \]:

Copied!

new\_nodes \= program\_extractor.process\_nodes(orig\_nodes)

new\_nodes = program\_extractor.process\_nodes(orig\_nodes)

Extracting Pydantic object:   0%|          | 0/29 \[00:00<?, ?it/s\]

In \[ \]:

Copied!

display(new\_nodes\[5:7\])

display(new\_nodes\[5:7\])

Back to top

[Previous Automated Metadata Extraction for Better Retrieval + Synthesis](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MetadataExtraction_LLMSurvey/)[Next Chroma Multi-Modal Demo with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/multi_modal/ChromaMultiModalDemo/)

Hi, how can I help you?

🦙
