Title: Jina Rerank - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/JinaRerank/

Markdown Content:
Jina Rerank - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

!pip install llama\-index\-postprocessor\-jinaai\-rerank
!pip install llama\-index\-embeddings\-jinaai
!pip install llama\-index

!pip install llama-index-postprocessor-jinaai-rerank !pip install llama-index-embeddings-jinaai !pip install llama-index

In \[ \]:

Copied!

import os
from llama\_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
)

import os from llama\_index.core import ( VectorStoreIndex, SimpleDirectoryReader, )

In \[ \]:

Copied!

from llama\_index.embeddings.jinaai import JinaEmbedding

api\_key \= os.environ\["JINA\_API\_KEY"\]
jina\_embeddings \= JinaEmbedding(api\_key\=api\_key)

\# load documents
import requests

url \= "https://niketeam-asset-download.nike.net/catalogs/2024/2024\_Nike%20Kids\_02\_09\_24.pdf?cb=09302022"
response \= requests.get(url)
with open("Nike\_Catalog.pdf", "wb") as f:
    f.write(response.content)
reader \= SimpleDirectoryReader(input\_files\=\["Nike\_Catalog.pdf"\])
documents \= reader.load\_data()

\# build index
index \= VectorStoreIndex.from\_documents(
    documents\=documents, embed\_model\=jina\_embeddings
)

from llama\_index.embeddings.jinaai import JinaEmbedding api\_key = os.environ\["JINA\_API\_KEY"\] jina\_embeddings = JinaEmbedding(api\_key=api\_key) # load documents import requests url = "https://niketeam-asset-download.nike.net/catalogs/2024/2024\_Nike%20Kids\_02\_09\_24.pdf?cb=09302022" response = requests.get(url) with open("Nike\_Catalog.pdf", "wb") as f: f.write(response.content) reader = SimpleDirectoryReader(input\_files=\["Nike\_Catalog.pdf"\]) documents = reader.load\_data() # build index index = VectorStoreIndex.from\_documents( documents=documents, embed\_model=jina\_embeddings )

#### Retrieve top 10 most relevant nodes, without using a reranker[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/JinaRerank/#retrieve-top-10-most-relevant-nodes-without-using-a-reranker)

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(similarity\_top\_k\=10)
response \= query\_engine.query(
    "What is the best jersey by Nike in terms of fabric?",
)

query\_engine = index.as\_query\_engine(similarity\_top\_k=10) response = query\_engine.query( "What is the best jersey by Nike in terms of fabric?", )

In \[ \]:

Copied!

print(response.source\_nodes\[0\].text, response.source\_nodes\[0\].score)
print("\\n")
print(response.source\_nodes\[1\].text, response.source\_nodes\[1\].score)

print(response.source\_nodes\[0\].text, response.source\_nodes\[0\].score) print("\\n") print(response.source\_nodes\[1\].text, response.source\_nodes\[1\].score)

56
Sustainable MaterialsNIKE KIDS  SOCCER – GOALKEEPER
KIDS NIKE DRY LS US PARK IV GK JERSEY 
CJ6073 $42.00
SIZES:  XS, S, M, L, XL
FABRIC:  100% polyester.
OFFER DATE:  04/01/20
END DATE:  12/31/25
Goal keepers jersey with graphic print on sleeves and across upper back panel, mesh back for breathability, 
slim fit with soft hand feel, shoulder seams rolled forward for better graphic visibility, straight seam across 
back, mesh back for breathability – gameday graphic print inspired by retro campos gk design .  
Body width: 16.3", Body length: 22" (size medium).
010 Black/White/(White) 012 Wolf Grey/White/(Black) 702 Volt/White/(Black)
KIDS NIKE DRY PARK III SHORT 
BV6866 $20.00
SIZES:  XS, S, M, L, XL
FABRIC:  100% polyester.
OFFER DATE:  04/01/20
END DATE:  12/31/25
Dri-FIT angled side seam short (slim fit) with soft hand feel updated fit for better mobility/comfort .  
Hip width: 16.9", Inseam length: 7" (size medium).
010 Black/White/(White) 012 Wolf Grey/Black/(Black) 702 Volt/(Black)
NIKE ACADEMY OTC SOCK (UNISEX) 
SX5728 $12.00
Sold in prepacks of 6.
SIZES:  XS, S, M, L, XL
FABRIC:  93% nylon/6% polyester/1% spandex.
OFFER DATE:  01/01/17
END DATE:  12/31/23
Game day sock with fold-over cuff, articulated foot specific footbed for superior fit and contrast Swoosh 
design trademark at ankle. Sold in prepacks of 6.
010 Black/(White) 018 Wolf Grey/(Black) 702 Volt/(Black)
Sustainable Materials 0.8641328028479249


NIKE KIDS  SOCCER – STOCK42
Sustainable Materials
KIDS NIKE DRI-FIT US SS 
CHALLENGE IV JERSEY
DH8368 $42.00
SIZES:  XS, S, M, L, XL
FABRIC:  100% polyester.
OFFER DATE:  01/01/22
END DATE:  12/31/23
The Nike Dri-FIT Challenge IV Jersey brings subtle style and modern performance to the field. Sweat-
wicking fabric helps keep you dry and comfortable from the first whistle to the last minute.
010 Black/Black/White/(White) 012 Wolf Grey/Wolf Grey/Black/(Black)
100 White/White/White/(Black) 341 Gorge Green/Gorge Green/White/(White)
419 College Navy/College Navy/White/(White) 448 Valor Blue/Valor Blue/White/(White)
480 Game Royal/Game Royal/White/(White) 657 University Red/University Red/White/(White)
692 Team Maroon/Team Maroon/White/(White) 702 Volt/Volt/Black/(Black)
891 Team Orange/Team Orange/Black/(Black)
NEW
KIDS NIKE DRI-FIT CHALLENGE V JERSEY  
SS US
FD7427 $47.00
SIZES:  XS, S, M, L, XL
FABRIC:  100% polyester.
OFFER DATE:  01/01/24
END DATE:  12/31/25
The Nike Dri-FIT Challenge Jersey V is designed to keep your players cool and comfortable through 90 
minutes and beyond. Mesh on the back and side panels offer breathability where athletes need it most. 
Body and sleeves are a Nike Dri-FIT knit fabric that moves sweat away to help keep players dry. This top 
is made with 100% recycled material. Side panel construction uses a more efficient pattern to help reduce 
material waste. Slim fit for a tailored look and feel.
010 Black/White/(White) 012 Wolf Grey/Black/(Black) 100 White/Black/(Black)
341 Gorge Green/White/(White) 419 College Navy/White/(White) 448 Valor Blue/White/(White)
480 Game Royal/White/(White) 657 University Red/White/(White) 692 Team Maroon/White/(White)
702 Volt/Black/(Black) 891 Team Orange/Black/(Black)
BACK VIEW 0.863721033128725

#### Retrieve top 10 most relevant nodes, but then rerank using Jina Reranker[¶](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/JinaRerank/#retrieve-top-10-most-relevant-nodes-but-then-rerank-using-jina-reranker)

By employing a reranker model, the prompt can be given more relevant context. This will lead to a more accurate response by the LLM.

In \[ \]:

Copied!

import os
from llama\_index.postprocessor.jinaai\_rerank import JinaRerank

jina\_rerank \= JinaRerank(api\_key\=api\_key, top\_n\=2)

import os from llama\_index.postprocessor.jinaai\_rerank import JinaRerank jina\_rerank = JinaRerank(api\_key=api\_key, top\_n=2)

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(
    similarity\_top\_k\=10, node\_postprocessors\=\[jina\_rerank\]
)
response \= query\_engine.query(
    "What is the best jersey by Nike in terms of fabric?",
)

query\_engine = index.as\_query\_engine( similarity\_top\_k=10, node\_postprocessors=\[jina\_rerank\] ) response = query\_engine.query( "What is the best jersey by Nike in terms of fabric?", )

In \[ \]:

Copied!

print(response.source\_nodes\[0\].text, response.source\_nodes\[0\].score)
print("\\n")
print(response.source\_nodes\[1\].text, response.source\_nodes\[1\].score)

print(response.source\_nodes\[0\].text, response.source\_nodes\[0\].score) print("\\n") print(response.source\_nodes\[1\].text, response.source\_nodes\[1\].score)

NIKE KIDS  SOCCER – STOCK41Sustainable Materials
Sustainable Materials
KIDS DRI-FIT ADV VAPOR IV JERSEY US SS
DR0837 $77.00
SIZES:  XS, S, M, L, XL
FABRIC:  100% polyester.
OFFER DATE:  01/01/23
END DATE:  12/31/24
Step on to the field ready for fast-paced play in the Nike Dri-FIT ADV Vapor Jersey. Engineered for 
optimal breathability, its moisture-wicking design helps keep you dry and cool under match-day pressure. 
Lightweight fabric in a relaxed, easy fit combats cling so you can focus on being the first to the ball. Lower 
insets line up perfectly with design details on the Nike Dri-FIT ADV Vapor IV Shorts to create an on-field 
look worthy of pro-level play. 
010  Black/Black/Black/(White) 100  White/White/White/(Black)
419  College Navy/College Navy/Game Royal/(White) 480  Game Royal/Game Royal/College Navy/(White)
657  University Red/University Red/Bright Crimson/(White)
BACK VIEW
GRAPHIC KNIT DETAIL
KIDS NIKE DRI-FIT US SS STRIKE III JERSEY
DR0913  $50.00
SIZES:  XS, S, M, L, XL
FABRIC:  100% polyester.
OFFER DATE:  01/01/23
END DATE:  12/31/24
Take the field in match-ready style in the lightweight Nike Strike Jersey. A relaxed, easy fit ensures that 
nothing comes between you and the ball, and sweat-wicking fabric works with breathable mesh to help 
keep you cool and composed during fast-paced play. Ribbed insets stretch with you to let you move without 
restrictions. Embroidered Swoosh design trademark. 
010  Black/Black/Black/(White) 011  Black/Volt/Volt/(White)
012  Wolf Grey/Black/Black/(White) 100  White/White/White/(Black)
419  College Navy/College Navy/Game Royal/(White) 448  Valor Blue/College Navy/College Navy/(White)
480  Game Royal/College Navy/College Navy/(White) 657  University Red/Bright Crimson/Bright Crimson/(White)
GRAPHIC KNIT DETAIL 0.3603765070438385


NIKE KIDS  SOCCER – STOCK45
Sustainable MaterialsKIDS NIKE DRI-FIT US LS TIEMPO
PREMIER II JERSEY
DH8407 $32.00
SIZES:  XS, S, M, L, XL
FABRIC:  100% polyester.
OFFER DATE:  01/01/22
END DATE:  12/31/26
The Nike Dri-FIT Tiempo Premier II Jersey brings you the cool performance of sweat-wicking fabric and a 
mesh back panel kick in when the game heats up.
010 Black/White/(White) 100 White/White/(Black) 419 College Navy/White/(White)
480 Game Royal/White/(White) 657 University Red/White/(White)
KIDS NIKE DRI-FIT US SS TIEMPO
PREMIER II JERSEY
DH8390 $27.00
SIZES:  XS, S, M, L, XL
FABRIC:  100% polyester.
OFFER DATE:  01/01/22
END DATE:  12/31/26
The Nike Dri-FIT Tiempo Premier II Jersey brings you the cool performance of sweat-wicking fabric and a 
mesh back panel kick in when the game heats up.
010 Black/White/(White) 012 Wolf Grey/Black/(Black) 100 White/White/(Black)
341 Gorge Green/White/(White) 419 College Navy/White/(White) 448 Valor Blue/White/(White)
480 Game Royal/White/(White) 547 Court Purple/White/(White) 616 Vivid Pink/Black/(Black)
657 University Red/White/(White) 692 Team Maroon/White/(White) 702 Volt/Black/(Black)
891 Team Orange/Black/(Black)
Sustainable Materials 0.35767972469329834

Back to top

[Previous FlagEmbeddingReranker](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/FlagEmbeddingReranker/)[Next LLM Reranker Demonstration (Great Gatsby)](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/LLMReranker-Gatsby/)

Hi, how can I help you?

🦙
