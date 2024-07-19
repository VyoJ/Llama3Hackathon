Title: Custom Embeddings - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/embeddings/custom_embeddings/

Markdown Content:
Custom Embeddings - LlamaIndex


LlamaIndex supports embeddings from OpenAI, Azure, and Langchain. But if this isn't enough, you can also implement any embeddings model!

The example below uses Instructor Embeddings ([install/setup details here](https://huggingface.co/hkunlp/instructor-large)), and implements a custom embeddings class. Instructor embeddings work by providing text, as well as "instructions" on the domain of the text to embed. This is helpful when embedding text from a very specific and specialized topic.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

\# Install dependencies
\# !pip install InstructorEmbedding torch transformers sentence-transformers

\# Install dependencies # !pip install InstructorEmbedding torch transformers sentence-transformers

In \[ \]:

Copied!

import openai
import os

os.environ\["OPENAI\_API\_KEY"\] \= "YOUR\_API\_KEY"
openai.api\_key \= os.environ\["OPENAI\_API\_KEY"\]

import openai import os os.environ\["OPENAI\_API\_KEY"\] = "YOUR\_API\_KEY" openai.api\_key = os.environ\["OPENAI\_API\_KEY"\]

Custom Embeddings Implementation[¶](https://docs.llamaindex.ai/en/stable/examples/embeddings/custom_embeddings/#custom-embeddings-implementation)
-------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from typing import Any, List
from InstructorEmbedding import INSTRUCTOR

from llama\_index.core.bridge.pydantic import PrivateAttr
from llama\_index.core.embeddings import BaseEmbedding

class InstructorEmbeddings(BaseEmbedding):
    \_model: INSTRUCTOR \= PrivateAttr()
    \_instruction: str \= PrivateAttr()

    def \_\_init\_\_(
        self,
        instructor\_model\_name: str \= "hkunlp/instructor-large",
        instruction: str \= "Represent a document for semantic search:",
        \*\*kwargs: Any,
    ) \-> None:
        self.\_model \= INSTRUCTOR(instructor\_model\_name)
        self.\_instruction \= instruction
        super().\_\_init\_\_(\*\*kwargs)

    @classmethod
    def class\_name(cls) \-> str:
        return "instructor"

    async def \_aget\_query\_embedding(self, query: str) \-> List\[float\]:
        return self.\_get\_query\_embedding(query)

    async def \_aget\_text\_embedding(self, text: str) \-> List\[float\]:
        return self.\_get\_text\_embedding(text)

    def \_get\_query\_embedding(self, query: str) \-> List\[float\]:
        embeddings \= self.\_model.encode(\[\[self.\_instruction, query\]\])
        return embeddings\[0\]

    def \_get\_text\_embedding(self, text: str) \-> List\[float\]:
        embeddings \= self.\_model.encode(\[\[self.\_instruction, text\]\])
        return embeddings\[0\]

    def \_get\_text\_embeddings(self, texts: List\[str\]) \-> List\[List\[float\]\]:
        embeddings \= self.\_model.encode(
            \[\[self.\_instruction, text\] for text in texts\]
        )
        return embeddings

from typing import Any, List from InstructorEmbedding import INSTRUCTOR from llama\_index.core.bridge.pydantic import PrivateAttr from llama\_index.core.embeddings import BaseEmbedding class InstructorEmbeddings(BaseEmbedding): \_model: INSTRUCTOR = PrivateAttr() \_instruction: str = PrivateAttr() def \_\_init\_\_( self, instructor\_model\_name: str = "hkunlp/instructor-large", instruction: str = "Represent a document for semantic search:", \*\*kwargs: Any, ) -> None: self.\_model = INSTRUCTOR(instructor\_model\_name) self.\_instruction = instruction super().\_\_init\_\_(\*\*kwargs) @classmethod def class\_name(cls) -> str: return "instructor" async def \_aget\_query\_embedding(self, query: str) -> List\[float\]: return self.\_get\_query\_embedding(query) async def \_aget\_text\_embedding(self, text: str) -> List\[float\]: return self.\_get\_text\_embedding(text) def \_get\_query\_embedding(self, query: str) -> List\[float\]: embeddings = self.\_model.encode(\[\[self.\_instruction, query\]\]) return embeddings\[0\] def \_get\_text\_embedding(self, text: str) -> List\[float\]: embeddings = self.\_model.encode(\[\[self.\_instruction, text\]\]) return embeddings\[0\] def \_get\_text\_embeddings(self, texts: List\[str\]) -> List\[List\[float\]\]: embeddings = self.\_model.encode( \[\[self.\_instruction, text\] for text in texts\] ) return embeddings

Usage Example[¶](https://docs.llamaindex.ai/en/stable/examples/embeddings/custom_embeddings/#usage-example)
-----------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama\_index.core import Settings

from llama\_index.core import SimpleDirectoryReader, VectorStoreIndex from llama\_index.core import Settings

#### Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/embeddings/custom_embeddings/#download-data)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

#### Load Documents[¶](https://docs.llamaindex.ai/en/stable/examples/embeddings/custom_embeddings/#load-documents)

In \[ \]:

Copied!

documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data()

In \[ \]:

Copied!

embed\_model \= InstructorEmbeddings(embed\_batch\_size\=2)

Settings.embed\_model \= embed\_model
Settings.chunk\_size \= 512

\# if running for the first time, will download model weights first!
index \= VectorStoreIndex.from\_documents(documents)

embed\_model = InstructorEmbeddings(embed\_batch\_size=2) Settings.embed\_model = embed\_model Settings.chunk\_size = 512 # if running for the first time, will download model weights first! index = VectorStoreIndex.from\_documents(documents)

load INSTRUCTOR\_Transformer
max\_seq\_length  512

In \[ \]:

Copied!

response \= index.as\_query\_engine().query("What did the author do growing up?")
print(response)

response = index.as\_query\_engine().query("What did the author do growing up?") print(response)

The author wrote short stories and also worked on programming, specifically on an IBM 1401 computer in 9th grade. They used an early version of Fortran and had to type programs on punch cards. Later on, they got a microcomputer, a TRS-80, and started programming more extensively, writing simple games and a word processor. They initially planned to study philosophy in college but eventually switched to AI.

Back to top

[Previous CohereAI Embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/cohereai/)[Next Dashscope embeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/dashscope_embeddings/)
