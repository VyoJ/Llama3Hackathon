Title: Metadata Extraction and Augmentation w/ Marvin

URL Source: https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MarvinMetadataExtractorDemo/

Markdown Content:
Metadata Extraction and Augmentation w/ Marvin - LlamaIndex


This notebook walks through using [`Marvin`](https://github.com/PrefectHQ/marvin) to extract and augment metadata from text. Marvin uses the LLM to identify and extract metadata. Metadata can be anything from additional and enhanced questions and answers to business object identification and elaboration. This notebook will demonstrate pulling out and elaborating on Sports Supplement information in a csv document.

Note: You will need to supply a valid open ai key below to run this notebook.

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MarvinMetadataExtractorDemo/#setup)
--------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai
%pip install llama\-index\-extractors\-marvin

%pip install llama-index-llms-openai %pip install llama-index-extractors-marvin

In \[ \]:

Copied!

\# !pip install marvin

\# !pip install marvin

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader
from llama\_index.llms.openai import OpenAI
from llama\_index.core.node\_parser import TokenTextSplitter
from llama\_index.extractors.marvin import MarvinMetadataExtractor

from llama\_index.core import SimpleDirectoryReader from llama\_index.llms.openai import OpenAI from llama\_index.core.node\_parser import TokenTextSplitter from llama\_index.extractors.marvin import MarvinMetadataExtractor

In \[ \]:

Copied!

import os
import openai

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import os import openai os.environ\["OPENAI\_API\_KEY"\] = "sk-..."

In \[ \]:

Copied!

documents \= SimpleDirectoryReader("data").load\_data()

\# limit document text length
documents\[0\].text \= documents\[0\].text\[:10000\]

documents = SimpleDirectoryReader("data").load\_data() # limit document text length documents\[0\].text = documents\[0\].text\[:10000\]

In \[ \]:

Copied!

import marvin
from marvin import ai\_model

from llama\_index.core.bridge.pydantic import BaseModel, Field

marvin.settings.openai.api\_key \= os.environ\["OPENAI\_API\_KEY"\]

@ai\_model
class SportsSupplement(BaseModel):
    name: str \= Field(..., description\="The name of the sports supplement")
    description: str \= Field(
        ..., description\="A description of the sports supplement"
    )
    pros\_cons: str \= Field(
        ..., description\="The pros and cons of the sports supplement"
    )

import marvin from marvin import ai\_model from llama\_index.core.bridge.pydantic import BaseModel, Field marvin.settings.openai.api\_key = os.environ\["OPENAI\_API\_KEY"\] @ai\_model class SportsSupplement(BaseModel): name: str = Field(..., description="The name of the sports supplement") description: str = Field( ..., description="A description of the sports supplement" ) pros\_cons: str = Field( ..., description="The pros and cons of the sports supplement" )

In \[ \]:

Copied!

llm\_model \= "gpt-3.5-turbo"

\# construct text splitter to split texts into chunks for processing
\# this takes a while to process, you can increase processing time by using larger chunk\_size
\# file size is a factor too of course
node\_parser \= TokenTextSplitter(
    separator\=" ", chunk\_size\=512, chunk\_overlap\=128
)

\# create metadata extractor
metadata\_extractor \= MarvinMetadataExtractor(
    marvin\_model\=SportsSupplement, llm\_model\_string\=llm\_model
)  \# let's extract custom entities for each node.

\# use node\_parser to get nodes from the documents
from llama\_index.core.ingestion import IngestionPipeline

pipeline \= IngestionPipeline(transformations\=\[node\_parser, metadata\_extractor\])

nodes \= pipeline.run(documents\=documents, show\_progress\=True)

llm\_model = "gpt-3.5-turbo" # construct text splitter to split texts into chunks for processing # this takes a while to process, you can increase processing time by using larger chunk\_size # file size is a factor too of course node\_parser = TokenTextSplitter( separator=" ", chunk\_size=512, chunk\_overlap=128 ) # create metadata extractor metadata\_extractor = MarvinMetadataExtractor( marvin\_model=SportsSupplement, llm\_model\_string=llm\_model ) # let's extract custom entities for each node. # use node\_parser to get nodes from the documents from llama\_index.core.ingestion import IngestionPipeline pipeline = IngestionPipeline(transformations=\[node\_parser, metadata\_extractor\]) nodes = pipeline.run(documents=documents, show\_progress=True)

In \[ \]:

Copied!

from pprint import pprint

for i in range(5):
    pprint(nodes\[i\].metadata)

from pprint import pprint for i in range(5): pprint(nodes\[i\].metadata)

{'marvin\_metadata': {'description': 'L-arginine alpha-ketoglutarate',
                     'name': 'AAKG',
                     'pros\_cons': '1.0, peak power output, strength–power, '
                                  'weight training, OTW, 242, 1, 20, nan, A '
                                  '2006 study found AAKG supplementation '
                                  'improved maximum effort 1-repetition bench '
                                  'press and Wingate peak power performance.'}}
{'marvin\_metadata': {'description': 'Gulping down baking soda (sodium '
                                    'bicarbonate) makes the blood more '
                                    'alkaline, improving performance in '
                                    'lactic-acid-fueled events like the 800m '
                                    'sprint.',
                     'name': 'Baking soda',
                     'pros\_cons': 'Downside: a badly upset stomach.'}}
{'marvin\_metadata': {'description': 'Branched-chain amino acids (BCAAs) are a '
                                    'group of essential amino acids that '
                                    'include leucine, isoleucine, and valine. '
                                    'They are commonly used as a sports '
                                    'supplement to improve fatigue resistance '
                                    'and aerobic endurance during activities '
                                    'such as cycling and circuit training.',
                     'name': 'BCAAs',
                     'pros\_cons': 'Pros: BCAAs can improve fatigue resistance '
                                  'and enhance aerobic endurance. Cons: '
                                  'Limited evidence on their effectiveness and '
                                  'potential side effects.'}}
{'marvin\_metadata': {'description': 'Branched-chain amino acids (BCAAs) are a '
                                    'group of three essential amino acids: '
                                    'leucine, isoleucine, and valine. They are '
                                    'commonly used as a sports supplement to '
                                    'improve aerobic performance, endurance, '
                                    'power, and strength. BCAAs can be '
                                    'beneficial for both aerobic-endurance and '
                                    'strength-power activities, such as '
                                    'cycling and circuit training.',
                     'name': 'Branched-chain amino acids',
                     'pros\_cons': 'Pros: BCAAs have been shown to improve '
                                  'aerobic performance, reduce muscle '
                                  'soreness, and enhance muscle protein '
                                  'synthesis. Cons: BCAAs may not be effective '
                                  'for everyone, and excessive intake can lead '
                                  'to an imbalance in amino acids.'}}
{'marvin\_metadata': {'description': 'Branched-chain amino acids (BCAAs) are a '
                                    'group of three essential amino acids: '
                                    'leucine, isoleucine, and valine. They are '
                                    'commonly used as a sports supplement to '
                                    'improve immune defenses in athletes and '
                                    'promote general fitness. BCAAs are often '
                                    'used by runners and athletes in other '
                                    'sports.',
                     'name': 'BCAAs',
                     'pros\_cons': 'Pros: - Can enhance immune defenses in '
                                  'athletes\\n'
                                  '- May improve general fitness\\n'
                                  'Cons: - Limited evidence for their '
                                  'effectiveness\\n'
                                  '- Potential side effects'}}

Back to top

[Previous Entity Metadata Extraction](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/EntityExtractionClimate/)[Next Extracting Metadata for Better Document Indexing and Understanding](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MetadataExtractionSEC/)

Hi, how can I help you?

🦙
