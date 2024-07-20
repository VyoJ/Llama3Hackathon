Title: Extracting Metadata for Better Document Indexing and Understanding

URL Source: https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MetadataExtractionSEC/

Markdown Content:
Extracting Metadata for Better Document Indexing and Understanding - LlamaIndex


In many cases, especially with long documents, a chunk of text may lack the context necessary to disambiguate the chunk from other similar chunks of text. One method of addressing this is manually labelling each chunk in our dataset or knowledge base. However, this can be labour intensive and time consuming for a large number or continually updated set of documents.

To combat this, we use LLMs to extract certain contextual information relevant to the document to better help the retrieval and language models disambiguate similar-looking passages.

We do this through our brand-new `Metadata Extractor` modules.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai
%pip install llama\-index\-extractors\-entity

%pip install llama-index-llms-openai %pip install llama-index-extractors-entity

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import nest\_asyncio

nest\_asyncio.apply()

import os
import openai

os.environ\["OPENAI\_API\_KEY"\] \= "YOUR\_API\_KEY\_HERE"

import nest\_asyncio nest\_asyncio.apply() import os import openai os.environ\["OPENAI\_API\_KEY"\] = "YOUR\_API\_KEY\_HERE"

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI
from llama\_index.core.schema import MetadataMode

from llama\_index.llms.openai import OpenAI from llama\_index.core.schema import MetadataMode

In \[ \]:

Copied!

llm \= OpenAI(temperature\=0.1, model\="gpt-3.5-turbo", max\_tokens\=512)

llm = OpenAI(temperature=0.1, model="gpt-3.5-turbo", max\_tokens=512)

We create a node parser that extracts the document title and hypothetical question embeddings relevant to the document chunk.

We also show how to instantiate the `SummaryExtractor` and `KeywordExtractor`, as well as how to create your own custom extractor based on the `BaseExtractor` base class

In \[ \]:

Copied!

from llama\_index.core.extractors import (
    SummaryExtractor,
    QuestionsAnsweredExtractor,
    TitleExtractor,
    KeywordExtractor,
    BaseExtractor,
)
from llama\_index.extractors.entity import EntityExtractor
from llama\_index.core.node\_parser import TokenTextSplitter

text\_splitter \= TokenTextSplitter(
    separator\=" ", chunk\_size\=512, chunk\_overlap\=128
)

class CustomExtractor(BaseExtractor):
    def extract(self, nodes):
        metadata\_list \= \[
            {
                "custom": (
                    node.metadata\["document\_title"\]
                    + "\\n"
                    + node.metadata\["excerpt\_keywords"\]
                )
            }
            for node in nodes
        \]
        return metadata\_list

extractors \= \[
    TitleExtractor(nodes\=5, llm\=llm),
    QuestionsAnsweredExtractor(questions\=3, llm\=llm),
    \# EntityExtractor(prediction\_threshold=0.5),
    \# SummaryExtractor(summaries=\["prev", "self"\], llm=llm),
    \# KeywordExtractor(keywords=10, llm=llm),
    \# CustomExtractor()
\]

transformations \= \[text\_splitter\] + extractors

from llama\_index.core.extractors import ( SummaryExtractor, QuestionsAnsweredExtractor, TitleExtractor, KeywordExtractor, BaseExtractor, ) from llama\_index.extractors.entity import EntityExtractor from llama\_index.core.node\_parser import TokenTextSplitter text\_splitter = TokenTextSplitter( separator=" ", chunk\_size=512, chunk\_overlap=128 ) class CustomExtractor(BaseExtractor): def extract(self, nodes): metadata\_list = \[ { "custom": ( node.metadata\["document\_title"\] + "\\n" + node.metadata\["excerpt\_keywords"\] ) } for node in nodes \] return metadata\_list extractors = \[ TitleExtractor(nodes=5, llm=llm), QuestionsAnsweredExtractor(questions=3, llm=llm), # EntityExtractor(prediction\_threshold=0.5), # SummaryExtractor(summaries=\["prev", "self"\], llm=llm), # KeywordExtractor(keywords=10, llm=llm), # CustomExtractor() \] transformations = \[text\_splitter\] + extractors

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

from llama\_index.core import SimpleDirectoryReader

We first load the 10k annual SEC report for Uber and Lyft for the years 2019 and 2020 respectively.

In \[ \]:

Copied!

!mkdir \-p data
!wget \-O "data/10k-132.pdf" "https://www.dropbox.com/scl/fi/6dlqdk6e2k1mjhi8dee5j/uber.pdf?rlkey=2jyoe49bg2vwdlz30l76czq6g&dl=1"
!wget \-O "data/10k-vFinal.pdf" "https://www.dropbox.com/scl/fi/qn7g3vrk5mqb18ko4e5in/lyft.pdf?rlkey=j6jxtjwo8zbstdo4wz3ns8zoj&dl=1"

!mkdir -p data !wget -O "data/10k-132.pdf" "https://www.dropbox.com/scl/fi/6dlqdk6e2k1mjhi8dee5j/uber.pdf?rlkey=2jyoe49bg2vwdlz30l76czq6g&dl=1" !wget -O "data/10k-vFinal.pdf" "https://www.dropbox.com/scl/fi/qn7g3vrk5mqb18ko4e5in/lyft.pdf?rlkey=j6jxtjwo8zbstdo4wz3ns8zoj&dl=1"

In \[ \]:

Copied!

\# Note the uninformative document file name, which may be a common scenario in a production setting
uber\_docs \= SimpleDirectoryReader(input\_files\=\["data/10k-132.pdf"\]).load\_data()
uber\_front\_pages \= uber\_docs\[0:3\]
uber\_content \= uber\_docs\[63:69\]
uber\_docs \= uber\_front\_pages + uber\_content

\# Note the uninformative document file name, which may be a common scenario in a production setting uber\_docs = SimpleDirectoryReader(input\_files=\["data/10k-132.pdf"\]).load\_data() uber\_front\_pages = uber\_docs\[0:3\] uber\_content = uber\_docs\[63:69\] uber\_docs = uber\_front\_pages + uber\_content

In \[ \]:

Copied!

from llama\_index.core.ingestion import IngestionPipeline

pipeline \= IngestionPipeline(transformations\=transformations)

uber\_nodes \= pipeline.run(documents\=uber\_docs)

from llama\_index.core.ingestion import IngestionPipeline pipeline = IngestionPipeline(transformations=transformations) uber\_nodes = pipeline.run(documents=uber\_docs)

In \[ \]:

Copied!

uber\_nodes\[1\].metadata

uber\_nodes\[1\].metadata

Out\[ \]:

{'page\_label': '2',
 'file\_name': '10k-132.pdf',
 'document\_title': 'Exploring the Diverse Landscape of 2019: A Comprehensive Annual Report on Uber Technologies, Inc.',
 'questions\_this\_excerpt\_can\_answer': '1. How many countries does Uber operate in?\\n2. What is the total gross bookings of Uber in 2019?\\n3. How many trips did Uber facilitate in 2019?'}

In \[ \]:

Copied!

\# Note the uninformative document file name, which may be a common scenario in a production setting
lyft\_docs \= SimpleDirectoryReader(
    input\_files\=\["data/10k-vFinal.pdf"\]
).load\_data()
lyft\_front\_pages \= lyft\_docs\[0:3\]
lyft\_content \= lyft\_docs\[68:73\]
lyft\_docs \= lyft\_front\_pages + lyft\_content

\# Note the uninformative document file name, which may be a common scenario in a production setting lyft\_docs = SimpleDirectoryReader( input\_files=\["data/10k-vFinal.pdf"\] ).load\_data() lyft\_front\_pages = lyft\_docs\[0:3\] lyft\_content = lyft\_docs\[68:73\] lyft\_docs = lyft\_front\_pages + lyft\_content

In \[ \]:

Copied!

from llama\_index.core.ingestion import IngestionPipeline

pipeline \= IngestionPipeline(transformations\=transformations)

lyft\_nodes \= pipeline.run(documents\=lyft\_docs)

from llama\_index.core.ingestion import IngestionPipeline pipeline = IngestionPipeline(transformations=transformations) lyft\_nodes = pipeline.run(documents=lyft\_docs)

In \[ \]:

Copied!

lyft\_nodes\[2\].metadata

lyft\_nodes\[2\].metadata

Out\[ \]:

{'page\_label': '2',
 'file\_name': '10k-vFinal.pdf',
 'document\_title': 'Lyft, Inc. Annual Report on Form 10-K for the Fiscal Year Ended December 31, 2020',
 'questions\_this\_excerpt\_can\_answer': "1. Has Lyft, Inc. filed a report on and attestation to its management's assessment of the effectiveness of its internal control over financial reporting under Section 404(b) of the Sarbanes-Oxley Act?\\n2. Is Lyft, Inc. considered a shell company according to Rule 12b-2 of the Exchange Act?\\n3. What was the aggregate market value of Lyft, Inc.'s common stock held by non-affiliates on June 30, 2020?"}

Since we are asking fairly sophisticated questions, we utilize a subquestion query engine for all QnA pipelines below, and prompt it to pay more attention to the relevance of the retrieved sources.

In \[ \]:

Copied!

from llama\_index.core.question\_gen import LLMQuestionGenerator
from llama\_index.core.question\_gen.prompts import (
    DEFAULT\_SUB\_QUESTION\_PROMPT\_TMPL,
)

question\_gen \= LLMQuestionGenerator.from\_defaults(
    llm\=llm,
    prompt\_template\_str\="""
        Follow the example, but instead of giving a question, always prefix the question 
        with: 'By first identifying and quoting the most relevant sources, '. 
        """
    + DEFAULT\_SUB\_QUESTION\_PROMPT\_TMPL,
)

from llama\_index.core.question\_gen import LLMQuestionGenerator from llama\_index.core.question\_gen.prompts import ( DEFAULT\_SUB\_QUESTION\_PROMPT\_TMPL, ) question\_gen = LLMQuestionGenerator.from\_defaults( llm=llm, prompt\_template\_str=""" Follow the example, but instead of giving a question, always prefix the question with: 'By first identifying and quoting the most relevant sources, '. """ + DEFAULT\_SUB\_QUESTION\_PROMPT\_TMPL, )

Querying an Index With No Extra Metadata[¶](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MetadataExtractionSEC/#querying-an-index-with-no-extra-metadata)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from copy import deepcopy

nodes\_no\_metadata \= deepcopy(uber\_nodes) + deepcopy(lyft\_nodes)
for node in nodes\_no\_metadata:
    node.metadata \= {
        k: node.metadata\[k\]
        for k in node.metadata
        if k in \["page\_label", "file\_name"\]
    }
print(
    "LLM sees:\\n",
    (nodes\_no\_metadata)\[9\].get\_content(metadata\_mode\=MetadataMode.LLM),
)

from copy import deepcopy nodes\_no\_metadata = deepcopy(uber\_nodes) + deepcopy(lyft\_nodes) for node in nodes\_no\_metadata: node.metadata = { k: node.metadata\[k\] for k in node.metadata if k in \["page\_label", "file\_name"\] } print( "LLM sees:\\n", (nodes\_no\_metadata)\[9\].get\_content(metadata\_mode=MetadataMode.LLM), )

LLM sees:
 \[Excerpt from document\]
page\_label: 65
file\_name: 10k-132.pdf
Excerpt:
-----
See the section titled “Reconciliations of Non-GAAP Financial Measures” for our definition and a 
reconciliation of net income (loss) attributable to  Uber Technologies, Inc. to Adjusted EBITDA. 
            
  Year Ended December 31,   2017 to 2018   2018 to 2019   
(In millions, exce pt percenta ges)  2017   2018   2019   % Chan ge  % Chan ge  
Adjusted EBITDA ................................  $ (2,642) $ (1,847) $ (2,725)  30%  (48)%
-----

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex
from llama\_index.core.query\_engine import SubQuestionQueryEngine
from llama\_index.core.tools import QueryEngineTool, ToolMetadata

from llama\_index.core import VectorStoreIndex from llama\_index.core.query\_engine import SubQuestionQueryEngine from llama\_index.core.tools import QueryEngineTool, ToolMetadata

In \[ \]:

Copied!

index\_no\_metadata \= VectorStoreIndex(
    nodes\=nodes\_no\_metadata,
)
engine\_no\_metadata \= index\_no\_metadata.as\_query\_engine(
    similarity\_top\_k\=10, llm\=OpenAI(model\="gpt-4")
)

index\_no\_metadata = VectorStoreIndex( nodes=nodes\_no\_metadata, ) engine\_no\_metadata = index\_no\_metadata.as\_query\_engine( similarity\_top\_k=10, llm=OpenAI(model="gpt-4") )

In \[ \]:

Copied!

final\_engine\_no\_metadata \= SubQuestionQueryEngine.from\_defaults(
    query\_engine\_tools\=\[
        QueryEngineTool(
            query\_engine\=engine\_no\_metadata,
            metadata\=ToolMetadata(
                name\="sec\_filing\_documents",
                description\="financial information on companies",
            ),
        )
    \],
    question\_gen\=question\_gen,
    use\_async\=True,
)

final\_engine\_no\_metadata = SubQuestionQueryEngine.from\_defaults( query\_engine\_tools=\[ QueryEngineTool( query\_engine=engine\_no\_metadata, metadata=ToolMetadata( name="sec\_filing\_documents", description="financial information on companies", ), ) \], question\_gen=question\_gen, use\_async=True, )

In \[ \]:

Copied!

response\_no\_metadata \= final\_engine\_no\_metadata.query(
    """
    What was the cost due to research and development v.s. sales and marketing for uber and lyft in 2019 in millions of USD?
    Give your answer as a JSON.
    """
)
print(response\_no\_metadata.response)
\# Correct answer:
\# {"Uber": {"Research and Development": 4836, "Sales and Marketing": 4626},
\#  "Lyft": {"Research and Development": 1505.6, "Sales and Marketing": 814 }}

response\_no\_metadata = final\_engine\_no\_metadata.query( """ What was the cost due to research and development v.s. sales and marketing for uber and lyft in 2019 in millions of USD? Give your answer as a JSON. """ ) print(response\_no\_metadata.response) # Correct answer: # {"Uber": {"Research and Development": 4836, "Sales and Marketing": 4626}, # "Lyft": {"Research and Development": 1505.6, "Sales and Marketing": 814 }}

Generated 4 sub questions.
\[sec\_filing\_documents\] Q: What was the cost due to research and development for Uber in 2019
\[sec\_filing\_documents\] Q: What was the cost due to sales and marketing for Uber in 2019
\[sec\_filing\_documents\] Q: What was the cost due to research and development for Lyft in 2019
\[sec\_filing\_documents\] Q: What was the cost due to sales and marketing for Lyft in 2019
\[sec\_filing\_documents\] A: The cost due to sales and marketing for Uber in 2019 was $814,122 in thousands.
\[sec\_filing\_documents\] A: The cost due to research and development for Uber in 2019 was $1,505,640 in thousands.
\[sec\_filing\_documents\] A: The cost of research and development for Lyft in 2019 was $1,505,640 in thousands.
\[sec\_filing\_documents\] A: The cost due to sales and marketing for Lyft in 2019 was $814,122 in thousands.
{
  "Uber": {
    "Research and Development": 1505.64,
    "Sales and Marketing": 814.122
  },
  "Lyft": {
    "Research and Development": 1505.64,
    "Sales and Marketing": 814.122
  }
}

**RESULT**: As we can see, the QnA agent does not seem to know where to look for the right documents. As a result it gets the Lyft and Uber data completely mixed up.

Querying an Index With Extracted Metadata[¶](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MetadataExtractionSEC/#querying-an-index-with-extracted-metadata)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

print(
    "LLM sees:\\n",
    (uber\_nodes + lyft\_nodes)\[9\].get\_content(metadata\_mode\=MetadataMode.LLM),
)

print( "LLM sees:\\n", (uber\_nodes + lyft\_nodes)\[9\].get\_content(metadata\_mode=MetadataMode.LLM), )

LLM sees:
 \[Excerpt from document\]
page\_label: 65
file\_name: 10k-132.pdf
document\_title: Exploring the Diverse Landscape of 2019: A Comprehensive Annual Report on Uber Technologies, Inc.
Excerpt:
-----
See the section titled “Reconciliations of Non-GAAP Financial Measures” for our definition and a 
reconciliation of net income (loss) attributable to  Uber Technologies, Inc. to Adjusted EBITDA. 
            
  Year Ended December 31,   2017 to 2018   2018 to 2019   
(In millions, exce pt percenta ges)  2017   2018   2019   % Chan ge  % Chan ge  
Adjusted EBITDA ................................  $ (2,642) $ (1,847) $ (2,725)  30%  (48)%
-----

In \[ \]:

Copied!

index \= VectorStoreIndex(
    nodes\=uber\_nodes + lyft\_nodes,
)
engine \= index.as\_query\_engine(similarity\_top\_k\=10, llm\=OpenAI(model\="gpt-4"))

index = VectorStoreIndex( nodes=uber\_nodes + lyft\_nodes, ) engine = index.as\_query\_engine(similarity\_top\_k=10, llm=OpenAI(model="gpt-4"))

In \[ \]:

Copied!

final\_engine \= SubQuestionQueryEngine.from\_defaults(
    query\_engine\_tools\=\[
        QueryEngineTool(
            query\_engine\=engine,
            metadata\=ToolMetadata(
                name\="sec\_filing\_documents",
                description\="financial information on companies.",
            ),
        )
    \],
    question\_gen\=question\_gen,
    use\_async\=True,
)

final\_engine = SubQuestionQueryEngine.from\_defaults( query\_engine\_tools=\[ QueryEngineTool( query\_engine=engine, metadata=ToolMetadata( name="sec\_filing\_documents", description="financial information on companies.", ), ) \], question\_gen=question\_gen, use\_async=True, )

In \[ \]:

Copied!

response \= final\_engine.query(
    """
    What was the cost due to research and development v.s. sales and marketing for uber and lyft in 2019 in millions of USD?
    Give your answer as a JSON.
    """
)
print(response.response)
\# Correct answer:
\# {"Uber": {"Research and Development": 4836, "Sales and Marketing": 4626},
\#  "Lyft": {"Research and Development": 1505.6, "Sales and Marketing": 814 }}

response = final\_engine.query( """ What was the cost due to research and development v.s. sales and marketing for uber and lyft in 2019 in millions of USD? Give your answer as a JSON. """ ) print(response.response) # Correct answer: # {"Uber": {"Research and Development": 4836, "Sales and Marketing": 4626}, # "Lyft": {"Research and Development": 1505.6, "Sales and Marketing": 814 }}

Generated 4 sub questions.
\[sec\_filing\_documents\] Q: What was the cost due to research and development for Uber in 2019
\[sec\_filing\_documents\] Q: What was the cost due to sales and marketing for Uber in 2019
\[sec\_filing\_documents\] Q: What was the cost due to research and development for Lyft in 2019
\[sec\_filing\_documents\] Q: What was the cost due to sales and marketing for Lyft in 2019
\[sec\_filing\_documents\] A: The cost due to sales and marketing for Uber in 2019 was $4,626 million.
\[sec\_filing\_documents\] A: The cost due to research and development for Uber in 2019 was $4,836 million.
\[sec\_filing\_documents\] A: The cost due to sales and marketing for Lyft in 2019 was $814,122 in thousands.
\[sec\_filing\_documents\] A: The cost of research and development for Lyft in 2019 was $1,505,640 in thousands.
{
  "Uber": {
    "Research and Development": 4836,
    "Sales and Marketing": 4626
  },
  "Lyft": {
    "Research and Development": 1505.64,
    "Sales and Marketing": 814.122
  }
}

**RESULT**: As we can see, the LLM answers the questions correctly.

### Challenges Identified in the Problem Domain[¶](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MetadataExtractionSEC/#challenges-identified-in-the-problem-domain)

In this example, we observed that the search quality as provided by vector embeddings was rather poor. This was likely due to highly dense financial documents that were likely not representative of the training set for the model.

In order to improve the search quality, other methods of neural search that employ more keyword-based approaches may help, such as ColBERTv2/PLAID. In particular, this would help in matching on particular keywords to identify high-relevance chunks.

Other valid steps may include utilizing models that are fine-tuned on financial datasets such as Bloomberg GPT.

Finally, we can help to further enrich the metadata by providing more contextual information regarding the surrounding context that the chunk is located in.

### Improvements to this Example[¶](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MetadataExtractionSEC/#improvements-to-this-example)

Generally, this example can be improved further with more rigorous evaluation of both the metadata extraction accuracy, and the accuracy and recall of the QnA pipeline. Further, incorporating a larger set of documents as well as the full length documents, which may provide more confounding passages that are difficult to disambiguate, could further stresss test the system we have built and suggest further improvements.

Back to top

[Previous Metadata Extraction and Augmentation w/ Marvin](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MarvinMetadataExtractorDemo/)[Next Automated Metadata Extraction for Better Retrieval + Synthesis](https://docs.llamaindex.ai/en/stable/examples/metadata_extraction/MetadataExtraction_LLMSurvey/)

Hi, how can I help you?

🦙
