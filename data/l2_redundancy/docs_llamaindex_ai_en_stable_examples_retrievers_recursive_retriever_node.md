Title: Recursive Retriever + Node References

URL Source: https://docs.llamaindex.ai/en/stable/examples/retrievers/recursive_retriever_nodes/

Markdown Content:
Recursive Retriever + Node References - LlamaIndex


This guide shows how you can use recursive retrieval to traverse node relationships and fetch nodes based on "references".

Node references are a powerful concept. When you first perform retrieval, you may want to retrieve the reference as opposed to the raw text. You can have multiple references point to the same node.

In this guide we explore some different usages of node references:

*   **Chunk references**: Different chunk sizes referring to a bigger chunk
*   **Metadata references**: Summaries + Generated Questions referring to a bigger chunk

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai
%pip install llama\-index\-readers\-file

%pip install llama-index-llms-openai %pip install llama-index-readers-file

In \[ \]:

Copied!

%load\_ext autoreload
%autoreload 2
%env OPENAI\_API\_KEY\=YOUR\_OPENAI\_KEY

%load\_ext autoreload %autoreload 2 %env OPENAI\_API\_KEY=YOUR\_OPENAI\_KEY

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

!pip install llama\-index pypdf

!pip install llama-index pypdf

Load Data + Setup[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/recursive_retriever_nodes/#load-data-setup)
-------------------------------------------------------------------------------------------------------------------------

In this section we download the Llama 2 paper and create an initial set of nodes (chunk size 1024).

In \[ \]:

Copied!

!mkdir \-p 'data/'
!wget \--user\-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" \-O "data/llama2.pdf"

!mkdir -p 'data/' !wget --user-agent "Mozilla" "https://arxiv.org/pdf/2307.09288.pdf" -O "data/llama2.pdf"

Will not apply HSTS. The HSTS database must be a regular and non-world-writable file.
ERROR: could not open HSTS store at '/home/loganm/.wget-hsts'. HSTS will be disabled.
--2024-01-01 11:13:01--  https://arxiv.org/pdf/2307.09288.pdf
Resolving arxiv.org (arxiv.org)... 151.101.3.42, 151.101.131.42, 151.101.67.42, ...
Connecting to arxiv.org (arxiv.org)|151.101.3.42|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 13661300 (13M) \[application/pdf\]
Saving to: ‘data/llama2.pdf’

data/llama2.pdf     100%\[>\]  13.03M  27.3MB/s    in 0.5s    

2024-01-01 11:13:02 (27.3 MB/s) - ‘data/llama2.pdf’ saved \[13661300/13661300\]

In \[ \]:

Copied!

from pathlib import Path
from llama\_index.readers.file import PDFReader
from llama\_index.core.response.notebook\_utils import display\_source\_node
from llama\_index.core.retrievers import RecursiveRetriever
from llama\_index.core.query\_engine import RetrieverQueryEngine
from llama\_index.core import VectorStoreIndex
from llama\_index.llms.openai import OpenAI
import json

from pathlib import Path from llama\_index.readers.file import PDFReader from llama\_index.core.response.notebook\_utils import display\_source\_node from llama\_index.core.retrievers import RecursiveRetriever from llama\_index.core.query\_engine import RetrieverQueryEngine from llama\_index.core import VectorStoreIndex from llama\_index.llms.openai import OpenAI import json

In \[ \]:

Copied!

loader \= PDFReader()
docs0 \= loader.load\_data(file\=Path("./data/llama2.pdf"))

loader = PDFReader() docs0 = loader.load\_data(file=Path("./data/llama2.pdf"))

In \[ \]:

Copied!

from llama\_index.core import Document

doc\_text \= "\\n\\n".join(\[d.get\_content() for d in docs0\])
docs \= \[Document(text\=doc\_text)\]

from llama\_index.core import Document doc\_text = "\\n\\n".join(\[d.get\_content() for d in docs0\]) docs = \[Document(text=doc\_text)\]

In \[ \]:

Copied!

from llama\_index.core.node\_parser import SentenceSplitter
from llama\_index.core.schema import IndexNode

from llama\_index.core.node\_parser import SentenceSplitter from llama\_index.core.schema import IndexNode

In \[ \]:

Copied!

node\_parser \= SentenceSplitter(chunk\_size\=1024)

node\_parser = SentenceSplitter(chunk\_size=1024)

In \[ \]:

Copied!

base\_nodes \= node\_parser.get\_nodes\_from\_documents(docs)
\# set node ids to be a constant
for idx, node in enumerate(base\_nodes):
    node.id\_ \= f"node-{idx}"

base\_nodes = node\_parser.get\_nodes\_from\_documents(docs) # set node ids to be a constant for idx, node in enumerate(base\_nodes): node.id\_ = f"node-{idx}"

In \[ \]:

Copied!

from llama\_index.core.embeddings import resolve\_embed\_model

embed\_model \= resolve\_embed\_model("local:BAAI/bge-small-en")
llm \= OpenAI(model\="gpt-3.5-turbo")

from llama\_index.core.embeddings import resolve\_embed\_model embed\_model = resolve\_embed\_model("local:BAAI/bge-small-en") llm = OpenAI(model="gpt-3.5-turbo")

Baseline Retriever[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/recursive_retriever_nodes/#baseline-retriever)
-----------------------------------------------------------------------------------------------------------------------------

Define a baseline retriever that simply fetches the top-k raw text nodes by embedding similarity.

In \[ \]:

Copied!

base\_index \= VectorStoreIndex(base\_nodes, embed\_model\=embed\_model)
base\_retriever \= base\_index.as\_retriever(similarity\_top\_k\=2)

base\_index = VectorStoreIndex(base\_nodes, embed\_model=embed\_model) base\_retriever = base\_index.as\_retriever(similarity\_top\_k=2)

In \[ \]:

Copied!

retrievals \= base\_retriever.retrieve(
    "Can you tell me about the key concepts for safety finetuning"
)

retrievals = base\_retriever.retrieve( "Can you tell me about the key concepts for safety finetuning" )

In \[ \]:

Copied!

for n in retrievals:
    display\_source\_node(n, source\_length\=1500)

for n in retrievals: display\_source\_node(n, source\_length=1500)

**Node ID:** node-26  
**Similarity:** 0.8581930837671874  
**Text:** AsLLMsareintegratedanddeployed,welookforwardto continuing research that will amplify their potential for positive impact on these important social issues. 4.2 Safety Fine-Tuning In this section, we describe our approach to safety fine-tuning, including safety categories, annotation guidelines,andthetechniquesweusetomitigatesafetyrisks. Weemployaprocesssimilartothegeneral fine-tuning methods as described in Section 3, with some notable differences related to safety concerns. Specifically, we use the following techniques in safety fine-tuning: 1.Supervised Safety Fine-Tuning : We initialize by gathering adversarial prompts and safe demonstra- tions that are then included in the general supervised fine-tuning process (Section 3.1). This teaches themodeltoalignwithoursafetyguidelinesevenbeforeRLHF,andthuslaysthefoundationfor high-quality human preference data annotation. 2.Safety RLHF : Subsequently, we integrate safety in the general RLHF pipeline described in Sec- tion 3.2.2. This includes training a safety-specific reward model and gathering more challenging adversarial prompts for rejection sampling style fine-tuning and PPO optimization. 3.SafetyContextDistillation : Finally,werefineourRLHFpipelinewithcontextdistillation(Askell etal.,2021b). Thisinvolvesgeneratingsafermodelresponsesbyprefixingapromptwithasafety preprompt, e.g., “You are a safe and responsible assistant,” and then fine-tuning the model on the safer responses without the preprompt, which essentially distill...

**Node ID:** node-33  
**Similarity:** 0.8442806881920294  
**Text:** Examples of evaluation prompts and responses can be found in Appendix A.4.6. We then asked raters to judge models for safety violations on a five-point Likert scale with the following definitions: •5- No safety violations and very helpful •4- No safety violations and only minor non-safety issues •3- No safety violations but not helpful or other major non-safety issues •2- Mild or moderate safety violations 29

(a)Overall violation percentage. (b)Overall safety and helpfulness mean rating. Figure17: Overallsafetymeasures. Left: Llama 2-Chat haslowviolationpercentageoverallacrossmodel sizes.Right: Llama 2-Chat has high safety and helpfulness mean rating overall across model sizes. It is important to note that these results are subject to limitations of the prompt set, subjectivity of the review guidelines, and subjectivity of individual raters. •1- Severe safety violations We consider a rating of 1 or 2 as violation and use violation percentage as our main evaluation metric, with themeanratingasasupplement. Eachexampleisannotatedbythreeannotatorsandwetakethemajority votetodetermineiftheresponseisviolatingornot. WeusedGwet’sAC1/2statistictomeasureinter-rater reliability(IRR)asinthehelpfulnesshumanevaluation. TheIRRscoresrangefrom 0.70to0.95depending on the annotation batch, indicating a high degree of agreement among annotators on safety assessments. OnLlama 2-Chat annotations, the average IRR is 0.92according to Gwet’s AC2 measure. We see lower IRR scoresonbatcheswherethemo...

In \[ \]:

Copied!

query\_engine\_base \= RetrieverQueryEngine.from\_args(base\_retriever, llm\=llm)

query\_engine\_base = RetrieverQueryEngine.from\_args(base\_retriever, llm=llm)

In \[ \]:

Copied!

response \= query\_engine\_base.query(
    "Can you tell me about the key concepts for safety finetuning"
)
print(str(response))

response = query\_engine\_base.query( "Can you tell me about the key concepts for safety finetuning" ) print(str(response))

The key concepts for safety fine-tuning include supervised safety fine-tuning, safety RLHF (Reinforcement Learning from Human Feedback), and safety context distillation. In supervised safety fine-tuning, adversarial prompts and safe demonstrations are gathered and included in the general supervised fine-tuning process. This helps the model align with safety guidelines and lays the foundation for high-quality human preference data annotation. Safety RLHF involves integrating safety in the general RLHF pipeline, which includes training a safety-specific reward model and gathering more challenging adversarial prompts for rejection sampling style fine-tuning and PPO (Proximal Policy Optimization) optimization. Safety context distillation is the final step, where the RLHF pipeline is refined with context distillation. This involves generating safer model responses by prefixing a prompt with a safety preprompt and then fine-tuning the model on the safer responses without the preprompt.

Chunk References: Smaller Child Chunks Referring to Bigger Parent Chunk[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/recursive_retriever_nodes/#chunk-references-smaller-child-chunks-referring-to-bigger-parent-chunk)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this usage example, we show how to build a graph of smaller chunks pointing to bigger parent chunks.

During query-time, we retrieve smaller chunks, but we follow references to bigger chunks. This allows us to have more context for synthesis.

In \[ \]:

Copied!

sub\_chunk\_sizes \= \[128, 256, 512\]
sub\_node\_parsers \= \[
    SentenceSplitter(chunk\_size\=c, chunk\_overlap\=20) for c in sub\_chunk\_sizes
\]

all\_nodes \= \[\]
for base\_node in base\_nodes:
    for n in sub\_node\_parsers:
        sub\_nodes \= n.get\_nodes\_from\_documents(\[base\_node\])
        sub\_inodes \= \[
            IndexNode.from\_text\_node(sn, base\_node.node\_id) for sn in sub\_nodes
        \]
        all\_nodes.extend(sub\_inodes)

    \# also add original node to node
    original\_node \= IndexNode.from\_text\_node(base\_node, base\_node.node\_id)
    all\_nodes.append(original\_node)

sub\_chunk\_sizes = \[128, 256, 512\] sub\_node\_parsers = \[ SentenceSplitter(chunk\_size=c, chunk\_overlap=20) for c in sub\_chunk\_sizes \] all\_nodes = \[\] for base\_node in base\_nodes: for n in sub\_node\_parsers: sub\_nodes = n.get\_nodes\_from\_documents(\[base\_node\]) sub\_inodes = \[ IndexNode.from\_text\_node(sn, base\_node.node\_id) for sn in sub\_nodes \] all\_nodes.extend(sub\_inodes) # also add original node to node original\_node = IndexNode.from\_text\_node(base\_node, base\_node.node\_id) all\_nodes.append(original\_node)

In \[ \]:

Copied!

all\_nodes\_dict \= {n.node\_id: n for n in all\_nodes}

all\_nodes\_dict = {n.node\_id: n for n in all\_nodes}

In \[ \]:

Copied!

vector\_index\_chunk \= VectorStoreIndex(all\_nodes, embed\_model\=embed\_model)

vector\_index\_chunk = VectorStoreIndex(all\_nodes, embed\_model=embed\_model)

In \[ \]:

Copied!

vector\_retriever\_chunk \= vector\_index\_chunk.as\_retriever(similarity\_top\_k\=2)

vector\_retriever\_chunk = vector\_index\_chunk.as\_retriever(similarity\_top\_k=2)

In \[ \]:

Copied!

retriever\_chunk \= RecursiveRetriever(
    "vector",
    retriever\_dict\={"vector": vector\_retriever\_chunk},
    node\_dict\=all\_nodes\_dict,
    verbose\=True,
)

retriever\_chunk = RecursiveRetriever( "vector", retriever\_dict={"vector": vector\_retriever\_chunk}, node\_dict=all\_nodes\_dict, verbose=True, )

In \[ \]:

Copied!

nodes \= retriever\_chunk.retrieve(
    "Can you tell me about the key concepts for safety finetuning"
)
for node in nodes:
    display\_source\_node(node, source\_length\=2000)

nodes = retriever\_chunk.retrieve( "Can you tell me about the key concepts for safety finetuning" ) for node in nodes: display\_source\_node(node, source\_length=2000)

Retrieving with query id None: Can you tell me about the key concepts for safety finetuning
Retrieved node with id, entering: node-26
Retrieving with query id node-26: Can you tell me about the key concepts for safety finetuning
Retrieved node with id, entering: node-1
Retrieving with query id node-1: Can you tell me about the key concepts for safety finetuning

**Node ID:** node-26  
**Similarity:** 0.8809071991986446  
**Text:** AsLLMsareintegratedanddeployed,welookforwardto continuing research that will amplify their potential for positive impact on these important social issues. 4.2 Safety Fine-Tuning In this section, we describe our approach to safety fine-tuning, including safety categories, annotation guidelines,andthetechniquesweusetomitigatesafetyrisks. Weemployaprocesssimilartothegeneral fine-tuning methods as described in Section 3, with some notable differences related to safety concerns. Specifically, we use the following techniques in safety fine-tuning: 1.Supervised Safety Fine-Tuning : We initialize by gathering adversarial prompts and safe demonstra- tions that are then included in the general supervised fine-tuning process (Section 3.1). This teaches themodeltoalignwithoursafetyguidelinesevenbeforeRLHF,andthuslaysthefoundationfor high-quality human preference data annotation. 2.Safety RLHF : Subsequently, we integrate safety in the general RLHF pipeline described in Sec- tion 3.2.2. This includes training a safety-specific reward model and gathering more challenging adversarial prompts for rejection sampling style fine-tuning and PPO optimization. 3.SafetyContextDistillation : Finally,werefineourRLHFpipelinewithcontextdistillation(Askell etal.,2021b). Thisinvolvesgeneratingsafermodelresponsesbyprefixingapromptwithasafety preprompt, e.g., “You are a safe and responsible assistant,” and then fine-tuning the model on the safer responses without the preprompt, which essentially distillsthe safety preprompt (context) into the model. Weuseatargetedapproachthatallowsoursafetyrewardmodeltochoosewhethertouse context distillation for each sample. 4.2.1 Safety Categories and Annotation Guidelines Based on limitations of LLMs known from prior work, we design instructions for our annotation team to createadversarialpromptsalongtwodimensions: a riskcategory ,orpotentialtopicaboutwhichtheLLM couldproduceunsafecontent;andan attackvector ,orquestionstyletocoverdifferentvarietiesofprompts ...

**Node ID:** node-1  
**Similarity:** 0.8744334039911964  
**Text:** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9 3.2 Reinforcement Learning with Human Feedback (RLHF) . . . . . . . . . . . . . . . . . . . . . 9 3.3 System Message for Multi-Turn Consistency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16 3.4 RLHF Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17 4 Safety 20 4.1 Safety in Pretraining . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20 4.2 Safety Fine-Tuning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23 4.3 Red Teaming . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28 4.4 Safety Evaluation of Llama 2-Chat . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29 5 Discussion 32 5.1 Learnings and Observations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32 5.2 Limitations and Ethical Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34 5.3 Responsible Release Strategy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35 6 Related Work 35 7 Conclusion 36 A Appendix 46 A.1 Contributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

In \[ \]:

Copied!

query\_engine\_chunk \= RetrieverQueryEngine.from\_args(retriever\_chunk, llm\=llm)

query\_engine\_chunk = RetrieverQueryEngine.from\_args(retriever\_chunk, llm=llm)

In \[ \]:

Copied!

response \= query\_engine\_chunk.query(
    "Can you tell me about the key concepts for safety finetuning"
)
print(str(response))

response = query\_engine\_chunk.query( "Can you tell me about the key concepts for safety finetuning" ) print(str(response))

Retrieving with query id None: Can you tell me about the key concepts for safety finetuning
Retrieved node with id, entering: node-26
Retrieving with query id node-26: Can you tell me about the key concepts for safety finetuning
Retrieved node with id, entering: node-1
Retrieving with query id node-1: Can you tell me about the key concepts for safety finetuning
The key concepts for safety fine-tuning include supervised safety fine-tuning, safety RLHF (Reinforcement Learning with Human Feedback), and safety context distillation. Supervised safety fine-tuning involves gathering adversarial prompts and safe demonstrations to teach the model to align with safety guidelines. Safety RLHF integrates safety into the general RLHF pipeline by training a safety-specific reward model and gathering challenging adversarial prompts for rejection sampling style fine-tuning and PPO optimization. Safety context distillation involves generating safer model responses by prefixing a prompt with a safety preprompt and fine-tuning the model on the safer responses without the preprompt. These techniques aim to mitigate safety risks and improve the model's ability to provide safe and responsible responses.

Metadata References: Summaries + Generated Questions referring to a bigger chunk[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/recursive_retriever_nodes/#metadata-references-summaries-generated-questions-referring-to-a-bigger-chunk)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this usage example, we show how to define additional context that references the source node.

This additional context includes summaries as well as generated questions.

During query-time, we retrieve smaller chunks, but we follow references to bigger chunks. This allows us to have more context for synthesis.

In \[ \]:

Copied!

import nest\_asyncio

nest\_asyncio.apply()

import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

from llama\_index.core.node\_parser import SentenceSplitter
from llama\_index.core.schema import IndexNode
from llama\_index.core.extractors import (
    SummaryExtractor,
    QuestionsAnsweredExtractor,
)

from llama\_index.core.node\_parser import SentenceSplitter from llama\_index.core.schema import IndexNode from llama\_index.core.extractors import ( SummaryExtractor, QuestionsAnsweredExtractor, )

In \[ \]:

Copied!

extractors \= \[
    SummaryExtractor(summaries\=\["self"\], show\_progress\=True),
    QuestionsAnsweredExtractor(questions\=5, show\_progress\=True),
\]

extractors = \[ SummaryExtractor(summaries=\["self"\], show\_progress=True), QuestionsAnsweredExtractor(questions=5, show\_progress=True), \]

In \[ \]:

Copied!

\# run metadata extractor across base nodes, get back dictionaries
node\_to\_metadata \= {}
for extractor in extractors:
    metadata\_dicts \= extractor.extract(base\_nodes)
    for node, metadata in zip(base\_nodes, metadata\_dicts):
        if node.node\_id not in node\_to\_metadata:
            node\_to\_metadata\[node.node\_id\] \= metadata
        else:
            node\_to\_metadata\[node.node\_id\].update(metadata)

\# run metadata extractor across base nodes, get back dictionaries node\_to\_metadata = {} for extractor in extractors: metadata\_dicts = extractor.extract(base\_nodes) for node, metadata in zip(base\_nodes, metadata\_dicts): if node.node\_id not in node\_to\_metadata: node\_to\_metadata\[node.node\_id\] = metadata else: node\_to\_metadata\[node.node\_id\].update(metadata)

100%|██████████| 93/93 \[01:13<00:00,  1.27it/s\]
100%|██████████| 93/93 \[00:49<00:00,  1.88it/s\]

In \[ \]:

Copied!

\# cache metadata dicts
def save\_metadata\_dicts(path, data):
    with open(path, "w") as fp:
        json.dump(data, fp)

def load\_metadata\_dicts(path):
    with open(path, "r") as fp:
        data \= json.load(fp)
    return data

\# cache metadata dicts def save\_metadata\_dicts(path, data): with open(path, "w") as fp: json.dump(data, fp) def load\_metadata\_dicts(path): with open(path, "r") as fp: data = json.load(fp) return data

In \[ \]:

Copied!

save\_metadata\_dicts("data/llama2\_metadata\_dicts.json", node\_to\_metadata)

save\_metadata\_dicts("data/llama2\_metadata\_dicts.json", node\_to\_metadata)

In \[ \]:

Copied!

metadata\_dicts \= load\_metadata\_dicts("data/llama2\_metadata\_dicts.json")

metadata\_dicts = load\_metadata\_dicts("data/llama2\_metadata\_dicts.json")

In \[ \]:

Copied!

\# all nodes consists of source nodes, along with metadata
import copy

all\_nodes \= copy.deepcopy(base\_nodes)
for node\_id, metadata in node\_to\_metadata.items():
    for val in metadata.values():
        all\_nodes.append(IndexNode(text\=val, index\_id\=node\_id))

\# all nodes consists of source nodes, along with metadata import copy all\_nodes = copy.deepcopy(base\_nodes) for node\_id, metadata in node\_to\_metadata.items(): for val in metadata.values(): all\_nodes.append(IndexNode(text=val, index\_id=node\_id))

In \[ \]:

Copied!

all\_nodes\_dict \= {n.node\_id: n for n in all\_nodes}

all\_nodes\_dict = {n.node\_id: n for n in all\_nodes}

In \[ \]:

Copied!

\## Load index into vector index
from llama\_index.core import VectorStoreIndex
from llama\_index.llms.openai import OpenAI

llm \= OpenAI(model\="gpt-3.5-turbo")

vector\_index\_metadata \= VectorStoreIndex(all\_nodes)

\## Load index into vector index from llama\_index.core import VectorStoreIndex from llama\_index.llms.openai import OpenAI llm = OpenAI(model="gpt-3.5-turbo") vector\_index\_metadata = VectorStoreIndex(all\_nodes)

In \[ \]:

Copied!

vector\_retriever\_metadata \= vector\_index\_metadata.as\_retriever(
    similarity\_top\_k\=2
)

vector\_retriever\_metadata = vector\_index\_metadata.as\_retriever( similarity\_top\_k=2 )

In \[ \]:

Copied!

retriever\_metadata \= RecursiveRetriever(
    "vector",
    retriever\_dict\={"vector": vector\_retriever\_metadata},
    node\_dict\=all\_nodes\_dict,
    verbose\=False,
)

retriever\_metadata = RecursiveRetriever( "vector", retriever\_dict={"vector": vector\_retriever\_metadata}, node\_dict=all\_nodes\_dict, verbose=False, )

In \[ \]:

Copied!

nodes \= retriever\_metadata.retrieve(
    "Can you tell me about the key concepts for safety finetuning"
)
for node in nodes:
    display\_source\_node(node, source\_length\=2000)

nodes = retriever\_metadata.retrieve( "Can you tell me about the key concepts for safety finetuning" ) for node in nodes: display\_source\_node(node, source\_length=2000)

**Node ID:** node-26  
**Similarity:** 0.8727061238826861  
**Text:** AsLLMsareintegratedanddeployed,welookforwardto continuing research that will amplify their potential for positive impact on these important social issues. 4.2 Safety Fine-Tuning In this section, we describe our approach to safety fine-tuning, including safety categories, annotation guidelines,andthetechniquesweusetomitigatesafetyrisks. Weemployaprocesssimilartothegeneral fine-tuning methods as described in Section 3, with some notable differences related to safety concerns. Specifically, we use the following techniques in safety fine-tuning: 1.Supervised Safety Fine-Tuning : We initialize by gathering adversarial prompts and safe demonstra- tions that are then included in the general supervised fine-tuning process (Section 3.1). This teaches themodeltoalignwithoursafetyguidelinesevenbeforeRLHF,andthuslaysthefoundationfor high-quality human preference data annotation. 2.Safety RLHF : Subsequently, we integrate safety in the general RLHF pipeline described in Sec- tion 3.2.2. This includes training a safety-specific reward model and gathering more challenging adversarial prompts for rejection sampling style fine-tuning and PPO optimization. 3.SafetyContextDistillation : Finally,werefineourRLHFpipelinewithcontextdistillation(Askell etal.,2021b). Thisinvolvesgeneratingsafermodelresponsesbyprefixingapromptwithasafety preprompt, e.g., “You are a safe and responsible assistant,” and then fine-tuning the model on the safer responses without the preprompt, which essentially distillsthe safety preprompt (context) into the model. Weuseatargetedapproachthatallowsoursafetyrewardmodeltochoosewhethertouse context distillation for each sample. 4.2.1 Safety Categories and Annotation Guidelines Based on limitations of LLMs known from prior work, we design instructions for our annotation team to createadversarialpromptsalongtwodimensions: a riskcategory ,orpotentialtopicaboutwhichtheLLM couldproduceunsafecontent;andan attackvector ,orquestionstyletocoverdifferentvarietiesofprompts ...

**Node ID:** node-26  
**Similarity:** 0.8586079224453517  
**Text:** AsLLMsareintegratedanddeployed,welookforwardto continuing research that will amplify their potential for positive impact on these important social issues. 4.2 Safety Fine-Tuning In this section, we describe our approach to safety fine-tuning, including safety categories, annotation guidelines,andthetechniquesweusetomitigatesafetyrisks. Weemployaprocesssimilartothegeneral fine-tuning methods as described in Section 3, with some notable differences related to safety concerns. Specifically, we use the following techniques in safety fine-tuning: 1.Supervised Safety Fine-Tuning : We initialize by gathering adversarial prompts and safe demonstra- tions that are then included in the general supervised fine-tuning process (Section 3.1). This teaches themodeltoalignwithoursafetyguidelinesevenbeforeRLHF,andthuslaysthefoundationfor high-quality human preference data annotation. 2.Safety RLHF : Subsequently, we integrate safety in the general RLHF pipeline described in Sec- tion 3.2.2. This includes training a safety-specific reward model and gathering more challenging adversarial prompts for rejection sampling style fine-tuning and PPO optimization. 3.SafetyContextDistillation : Finally,werefineourRLHFpipelinewithcontextdistillation(Askell etal.,2021b). Thisinvolvesgeneratingsafermodelresponsesbyprefixingapromptwithasafety preprompt, e.g., “You are a safe and responsible assistant,” and then fine-tuning the model on the safer responses without the preprompt, which essentially distillsthe safety preprompt (context) into the model. Weuseatargetedapproachthatallowsoursafetyrewardmodeltochoosewhethertouse context distillation for each sample. 4.2.1 Safety Categories and Annotation Guidelines Based on limitations of LLMs known from prior work, we design instructions for our annotation team to createadversarialpromptsalongtwodimensions: a riskcategory ,orpotentialtopicaboutwhichtheLLM couldproduceunsafecontent;andan attackvector ,orquestionstyletocoverdifferentvarietiesofprompts ...

In \[ \]:

Copied!

query\_engine\_metadata \= RetrieverQueryEngine.from\_args(
    retriever\_metadata, llm\=llm
)

query\_engine\_metadata = RetrieverQueryEngine.from\_args( retriever\_metadata, llm=llm )

In \[ \]:

Copied!

response \= query\_engine\_metadata.query(
    "Can you tell me about the key concepts for safety finetuning"
)
print(str(response))

response = query\_engine\_metadata.query( "Can you tell me about the key concepts for safety finetuning" ) print(str(response))

The key concepts for safety fine-tuning include supervised safety fine-tuning, safety RLHF (Reinforcement Learning from Human Feedback), and safety context distillation. Supervised safety fine-tuning involves gathering adversarial prompts and safe demonstrations to train the model to align with safety guidelines. Safety RLHF integrates safety into the RLHF pipeline by training a safety-specific reward model and gathering challenging adversarial prompts for fine-tuning and optimization. Safety context distillation involves generating safer model responses by prefixing a prompt with a safety preprompt and fine-tuning the model on the safer responses without the preprompt. These concepts are used to mitigate safety risks and improve the model's ability to produce safe and helpful responses.

Evaluation[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/recursive_retriever_nodes/#evaluation)
-------------------------------------------------------------------------------------------------------------

We evaluate how well our recursive retrieval + node reference methods work. We evaluate both chunk references as well as metadata references. We use embedding similarity lookup to retrieve the reference nodes.

We compare both methods against a baseline retriever where we fetch the raw nodes directly.

In terms of metrics, we evaluate using both hit-rate and MRR.

### Dataset Generation[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/recursive_retriever_nodes/#dataset-generation)

We first generate a dataset of questions from the set of text chunks.

In \[ \]:

Copied!

from llama\_index.core.evaluation import (
    generate\_question\_context\_pairs,
    EmbeddingQAFinetuneDataset,
)
from llama\_index.llms.openai import OpenAI

import nest\_asyncio

nest\_asyncio.apply()

from llama\_index.core.evaluation import ( generate\_question\_context\_pairs, EmbeddingQAFinetuneDataset, ) from llama\_index.llms.openai import OpenAI import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

eval\_dataset \= generate\_question\_context\_pairs(
    base\_nodes, OpenAI(model\="gpt-3.5-turbo")
)

eval\_dataset = generate\_question\_context\_pairs( base\_nodes, OpenAI(model="gpt-3.5-turbo") )

100%|██████████| 93/93 \[02:08<00:00,  1.38s/it\]

In \[ \]:

Copied!

eval\_dataset.save\_json("data/llama2\_eval\_dataset.json")

eval\_dataset.save\_json("data/llama2\_eval\_dataset.json")

In \[ \]:

Copied!

\# optional
eval\_dataset \= EmbeddingQAFinetuneDataset.from\_json(
    "data/llama2\_eval\_dataset.json"
)

\# optional eval\_dataset = EmbeddingQAFinetuneDataset.from\_json( "data/llama2\_eval\_dataset.json" )

### Compare Results[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/recursive_retriever_nodes/#compare-results)

We run evaluations on each of the retrievers to measure hit rate and MRR.

We find that retrievers with node references (either chunk or metadata) tend to perform better than retrieving the raw chunks.

In \[ \]:

Copied!

import pandas as pd
from llama\_index.core.evaluation import (
    RetrieverEvaluator,
    get\_retrieval\_results\_df,
)

\# set vector retriever similarity top k to higher
top\_k \= 10

def display\_results(names, results\_arr):
    """Display results from evaluate."""

    hit\_rates \= \[\]
    mrrs \= \[\]
    for name, eval\_results in zip(names, results\_arr):
        metric\_dicts \= \[\]
        for eval\_result in eval\_results:
            metric\_dict \= eval\_result.metric\_vals\_dict
            metric\_dicts.append(metric\_dict)
        results\_df \= pd.DataFrame(metric\_dicts)

        hit\_rate \= results\_df\["hit\_rate"\].mean()
        mrr \= results\_df\["mrr"\].mean()
        hit\_rates.append(hit\_rate)
        mrrs.append(mrr)

    final\_df \= pd.DataFrame(
        {"retrievers": names, "hit\_rate": hit\_rates, "mrr": mrrs}
    )
    display(final\_df)

import pandas as pd from llama\_index.core.evaluation import ( RetrieverEvaluator, get\_retrieval\_results\_df, ) # set vector retriever similarity top k to higher top\_k = 10 def display\_results(names, results\_arr): """Display results from evaluate.""" hit\_rates = \[\] mrrs = \[\] for name, eval\_results in zip(names, results\_arr): metric\_dicts = \[\] for eval\_result in eval\_results: metric\_dict = eval\_result.metric\_vals\_dict metric\_dicts.append(metric\_dict) results\_df = pd.DataFrame(metric\_dicts) hit\_rate = results\_df\["hit\_rate"\].mean() mrr = results\_df\["mrr"\].mean() hit\_rates.append(hit\_rate) mrrs.append(mrr) final\_df = pd.DataFrame( {"retrievers": names, "hit\_rate": hit\_rates, "mrr": mrrs} ) display(final\_df)

In \[ \]:

Copied!

vector\_retriever\_chunk \= vector\_index\_chunk.as\_retriever(
    similarity\_top\_k\=top\_k
)
retriever\_chunk \= RecursiveRetriever(
    "vector",
    retriever\_dict\={"vector": vector\_retriever\_chunk},
    node\_dict\=all\_nodes\_dict,
    verbose\=True,
)
retriever\_evaluator \= RetrieverEvaluator.from\_metric\_names(
    \["mrr", "hit\_rate"\], retriever\=retriever\_chunk
)
\# try it out on an entire dataset
results\_chunk \= await retriever\_evaluator.aevaluate\_dataset(
    eval\_dataset, show\_progress\=True
)

vector\_retriever\_chunk = vector\_index\_chunk.as\_retriever( similarity\_top\_k=top\_k ) retriever\_chunk = RecursiveRetriever( "vector", retriever\_dict={"vector": vector\_retriever\_chunk}, node\_dict=all\_nodes\_dict, verbose=True, ) retriever\_evaluator = RetrieverEvaluator.from\_metric\_names( \["mrr", "hit\_rate"\], retriever=retriever\_chunk ) # try it out on an entire dataset results\_chunk = await retriever\_evaluator.aevaluate\_dataset( eval\_dataset, show\_progress=True )

In \[ \]:

Copied!

vector\_retriever\_metadata \= vector\_index\_metadata.as\_retriever(
    similarity\_top\_k\=top\_k
)
retriever\_metadata \= RecursiveRetriever(
    "vector",
    retriever\_dict\={"vector": vector\_retriever\_metadata},
    node\_dict\=all\_nodes\_dict,
    verbose\=True,
)
retriever\_evaluator \= RetrieverEvaluator.from\_metric\_names(
    \["mrr", "hit\_rate"\], retriever\=retriever\_metadata
)
\# try it out on an entire dataset
results\_metadata \= await retriever\_evaluator.aevaluate\_dataset(
    eval\_dataset, show\_progress\=True
)

vector\_retriever\_metadata = vector\_index\_metadata.as\_retriever( similarity\_top\_k=top\_k ) retriever\_metadata = RecursiveRetriever( "vector", retriever\_dict={"vector": vector\_retriever\_metadata}, node\_dict=all\_nodes\_dict, verbose=True, ) retriever\_evaluator = RetrieverEvaluator.from\_metric\_names( \["mrr", "hit\_rate"\], retriever=retriever\_metadata ) # try it out on an entire dataset results\_metadata = await retriever\_evaluator.aevaluate\_dataset( eval\_dataset, show\_progress=True )

In \[ \]:

Copied!

base\_retriever \= base\_index.as\_retriever(similarity\_top\_k\=top\_k)
retriever\_evaluator \= RetrieverEvaluator.from\_metric\_names(
    \["mrr", "hit\_rate"\], retriever\=base\_retriever
)
\# try it out on an entire dataset
results\_base \= await retriever\_evaluator.aevaluate\_dataset(
    eval\_dataset, show\_progress\=True
)

base\_retriever = base\_index.as\_retriever(similarity\_top\_k=top\_k) retriever\_evaluator = RetrieverEvaluator.from\_metric\_names( \["mrr", "hit\_rate"\], retriever=base\_retriever ) # try it out on an entire dataset results\_base = await retriever\_evaluator.aevaluate\_dataset( eval\_dataset, show\_progress=True )

100%|██████████| 194/194 \[00:09<00:00, 19.86it/s\]

In \[ \]:

Copied!

full\_results\_df \= get\_retrieval\_results\_df(
    \[
        "Base Retriever",
        "Retriever (Chunk References)",
        "Retriever (Metadata References)",
    \],
    \[results\_base, results\_chunk, results\_metadata\],
)
display(full\_results\_df)

full\_results\_df = get\_retrieval\_results\_df( \[ "Base Retriever", "Retriever (Chunk References)", "Retriever (Metadata References)", \], \[results\_base, results\_chunk, results\_metadata\], ) display(full\_results\_df)

|  | retrievers | hit\_rate | mrr |
| --- | --- | --- | --- |
| 0 | Base Retriever | 0.778351 | 0.563103 |
| 1 | Retriever (Chunk References) | 0.896907 | 0.691114 |
| 2 | Retriever (Metadata References) | 0.891753 | 0.718440 |

Back to top

[Previous Recursive Retriever + Node References + Braintrust](https://docs.llamaindex.ai/en/stable/examples/retrievers/recurisve_retriever_nodes_braintrust/)[Next Relative Score Fusion and Distribution-Based Score Fusion](https://docs.llamaindex.ai/en/stable/examples/retrievers/relative_score_dist_fusion/)
