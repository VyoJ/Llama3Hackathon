Title: Multimodal Structured Outputs: GPT-4o vs. Other GPT-4 Variants

URL Source: https://docs.llamaindex.ai/en/stable/examples/multi_modal/gpt4o_mm_structured_outputs/

Markdown Content:
Multimodal Structured Outputs: GPT-4o vs. Other GPT-4 Variants - LlamaIndex


In this notebook, we use the `MultiModalLLMCompletionProgram` class to perform structured data extraction with images. We'll make comparisons across the the GPT-4 vision-capable models.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai \-q
%pip install llama\-index\-multi\-modal\-llms\-openai \-q
%pip install llama\-index\-readers\-file \-q
%pip install \-U llama\-index\-core \-q

%pip install llama-index-llms-openai -q %pip install llama-index-multi-modal-llms-openai -q %pip install llama-index-readers-file -q %pip install -U llama-index-core -q

In \[ \]:

Copied!

from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd

from PIL import Image import matplotlib.pyplot as plt import pandas as pd

The Image Dataset: PaperCards[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gpt4o_mm_structured_outputs/#the-image-dataset-papercards)
-----------------------------------------------------------------------------------------------------------------------------------------------------

For this data extraction task, we'll be using the multimodal LLMs to extract information from so-called PaperCards. These are visualizations containing summaries of research papers. The dataset can be downloaded from our dropbox account by executing the command below.

### Download the images[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gpt4o_mm_structured_outputs/#download-the-images)

In \[ \]:

Copied!

!mkdir data
!wget "https://www.dropbox.com/scl/fo/jlxavjjzddcv6owvr9e6y/AJoNd0T2pUSeynOTtM\_f60c?rlkey=4mvwc1r6lowmy7zqpnm1ikd24&st=1cs1gs9c&dl=1" \-O data/paper\_cards.zip
!unzip data/paper\_cards.zip \-d data
!rm data/paper\_cards.zip

!mkdir data !wget "https://www.dropbox.com/scl/fo/jlxavjjzddcv6owvr9e6y/AJoNd0T2pUSeynOTtM\_f60c?rlkey=4mvwc1r6lowmy7zqpnm1ikd24&st=1cs1gs9c&dl=1" -O data/paper\_cards.zip !unzip data/paper\_cards.zip -d data !rm data/paper\_cards.zip

### Load PaperCards as ImageDocuments[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gpt4o_mm_structured_outputs/#load-papercards-as-imagedocuments)

In \[ \]:

Copied!

\## import json
from llama\_index.core.multi\_modal\_llms.generic\_utils import load\_image\_urls
from llama\_index.core import SimpleDirectoryReader, Document

\# context images
image\_path \= "./data"
image\_documents \= SimpleDirectoryReader(image\_path).load\_data()

\## import json from llama\_index.core.multi\_modal\_llms.generic\_utils import load\_image\_urls from llama\_index.core import SimpleDirectoryReader, Document # context images image\_path = "./data" image\_documents = SimpleDirectoryReader(image\_path).load\_data()

In \[ \]:

Copied!

\# let's see one
img\_doc \= image\_documents\[0\]
image \= Image.open(img\_doc.image\_path).convert("RGB")
plt.figure(figsize\=(8, 8))
plt.axis("off")
plt.imshow(image)
plt.show()

\# let's see one img\_doc = image\_documents\[0\] image = Image.open(img\_doc.image\_path).convert("RGB") plt.figure(figsize=(8, 8)) plt.axis("off") plt.imshow(image) plt.show()

![Image 4: No description has been provided for this image](blob:https://docs.llamaindex.ai/817783acefe3aaa6553589cc80261230)

Build Our MultiModalLLMCompletionProgram (Multimodal Structured Outputs)[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gpt4o_mm_structured_outputs/#build-our-multimodalllmcompletionprogram-multimodal-structured-outputs)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Desired Structured Output[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gpt4o_mm_structured_outputs/#desired-structured-output)

Here we will define our data class (i.e., Pydantic BaseModel) that will hold the data that we extract from a given image or PaperCard.

In \[ \]:

Copied!

from llama\_index.core.program import MultiModalLLMCompletionProgram
from llama\_index.multi\_modal\_llms.openai import OpenAIMultiModal
from llama\_index.core.bridge.pydantic import BaseModel, Field
from typing import List, Optional

\# Desired output structure
class PaperCard(BaseModel):
    """Data class for storing text attributes of a PaperCard."""

    title: str \= Field(description\="Title of paper.")
    year: str \= Field(description\="Year of publication of paper.")
    authors: str \= Field(description\="Authors of paper.")
    arxiv\_id: str \= Field(description\="Arxiv paper id.")
    main\_contribution: str \= Field(
        description\="Main contribution of the paper."
    )
    insights: str \= Field(
        description\="Main insight or motivation for the paper."
    )
    main\_results: List\[str\] \= Field(
        description\="The main results of the paper."
    )
    tech\_bits: Optional\[str\] \= Field(
        description\="Describe what's being displayed in the technical bits section of the image."
    )

from llama\_index.core.program import MultiModalLLMCompletionProgram from llama\_index.multi\_modal\_llms.openai import OpenAIMultiModal from llama\_index.core.bridge.pydantic import BaseModel, Field from typing import List, Optional # Desired output structure class PaperCard(BaseModel): """Data class for storing text attributes of a PaperCard.""" title: str = Field(description="Title of paper.") year: str = Field(description="Year of publication of paper.") authors: str = Field(description="Authors of paper.") arxiv\_id: str = Field(description="Arxiv paper id.") main\_contribution: str = Field( description="Main contribution of the paper." ) insights: str = Field( description="Main insight or motivation for the paper." ) main\_results: List\[str\] = Field( description="The main results of the paper." ) tech\_bits: Optional\[str\] = Field( description="Describe what's being displayed in the technical bits section of the image." )

Next, we define our `MultiModalLLMCompletionProgram`. Here we actually will define three separate programs, one for each of the vision-capable GPT-4 models, namely: GPT-4o, GPT-4v, and GPT-4Turbo.

In \[ \]:

Copied!

paper\_card\_extraction\_prompt \= """
Use the attached PaperCard image to extract data from it and store into the
provided data class.
"""

gpt\_4o \= OpenAIMultiModal(model\="gpt-4o", max\_new\_tokens\=4096)

gpt\_4v \= OpenAIMultiModal(model\="gpt-4-vision-preview", max\_new\_tokens\=4096)

gpt\_4turbo \= OpenAIMultiModal(
    model\="gpt-4-turbo-2024-04-09", max\_new\_tokens\=4096
)

multimodal\_llms \= {
    "gpt\_4o": gpt\_4o,
    "gpt\_4v": gpt\_4v,
    "gpt\_4turbo": gpt\_4turbo,
}

programs \= {
    mdl\_name: MultiModalLLMCompletionProgram.from\_defaults(
        output\_cls\=PaperCard,
        prompt\_template\_str\=paper\_card\_extraction\_prompt,
        multi\_modal\_llm\=mdl,
    )
    for mdl\_name, mdl in multimodal\_llms.items()
}

paper\_card\_extraction\_prompt = """ Use the attached PaperCard image to extract data from it and store into the provided data class. """ gpt\_4o = OpenAIMultiModal(model="gpt-4o", max\_new\_tokens=4096) gpt\_4v = OpenAIMultiModal(model="gpt-4-vision-preview", max\_new\_tokens=4096) gpt\_4turbo = OpenAIMultiModal( model="gpt-4-turbo-2024-04-09", max\_new\_tokens=4096 ) multimodal\_llms = { "gpt\_4o": gpt\_4o, "gpt\_4v": gpt\_4v, "gpt\_4turbo": gpt\_4turbo, } programs = { mdl\_name: MultiModalLLMCompletionProgram.from\_defaults( output\_cls=PaperCard, prompt\_template\_str=paper\_card\_extraction\_prompt, multi\_modal\_llm=mdl, ) for mdl\_name, mdl in multimodal\_llms.items() }

### Let's give it a test run[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gpt4o_mm_structured_outputs/#lets-give-it-a-test-run)

In \[ \]:

Copied!

\# Please ensure you're using llama-index-core v0.10.37
papercard \= programs\["gpt\_4o"\](image\_documents\=\[image\_documents\[0\]\])

\# Please ensure you're using llama-index-core v0.10.37 papercard = programs\["gpt\_4o"\](image\_documents=\[image\_documents\[0\]\])

In \[ \]:

Copied!

papercard

papercard

Out\[ \]:

PaperCard(title='CRITIC: LLMs Can Self-Correct With Tool-Interactive Critiquing', year='2023', authors='Gao, Zhibin et al.', arxiv\_id='arXiv:2305.11738', main\_contribution='A framework for verifying and then correcting hallucinations by large language models (LLMs) with external tools (e.g., text-to-text APIs).', insights='LLMs can hallucinate and produce false information. By using external tools, these hallucinations can be identified and corrected.', main\_results=\['CRITIC leads to marked improvements over baselines on QA, math, and toxicity reduction tasks.', 'Feedback from external tools is crucial for an LLM to self-correct.', 'CRITIC significantly outperforms baselines on QA, math, and toxicity reduction tasks.'\], tech\_bits='The technical bits section describes the CRITIC prompt, which includes an initial output, critique, and revision steps. It also highlights the tools used for critiquing, such as a calculator for math tasks and a toxicity classifier for toxicity reduction tasks.')

Run The Data Extraction Task[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gpt4o_mm_structured_outputs/#run-the-data-extraction-task)
----------------------------------------------------------------------------------------------------------------------------------------------------

Now that we've tested our program, we're ready to apply the programs to the data extraction task over the PaperCards!

In \[ \]:

Copied!

import time
import tqdm

import time import tqdm

In \[ \]:

Copied!

results \= {}

for mdl\_name, program in programs.items():
    print(f"Model: {mdl\_name}")
    results\[mdl\_name\] \= {
        "papercards": \[\],
        "failures": \[\],
        "execution\_times": \[\],
        "image\_paths": \[\],
    }
    total\_time \= 0
    for img in tqdm.tqdm(image\_documents):
        results\[mdl\_name\]\["image\_paths"\].append(img.image\_path)
        start\_time \= time.time()
        try:
            structured\_output \= program(image\_documents\=\[img\])
            end\_time \= time.time() \- start\_time
            results\[mdl\_name\]\["papercards"\].append(structured\_output)
            results\[mdl\_name\]\["execution\_times"\].append(end\_time)
            results\[mdl\_name\]\["failures"\].append(None)
        except Exception as e:
            results\[mdl\_name\]\["papercards"\].append(None)
            results\[mdl\_name\]\["execution\_times"\].append(None)
            results\[mdl\_name\]\["failures"\].append(e)
    print()

results = {} for mdl\_name, program in programs.items(): print(f"Model: {mdl\_name}") results\[mdl\_name\] = { "papercards": \[\], "failures": \[\], "execution\_times": \[\], "image\_paths": \[\], } total\_time = 0 for img in tqdm.tqdm(image\_documents): results\[mdl\_name\]\["image\_paths"\].append(img.image\_path) start\_time = time.time() try: structured\_output = program(image\_documents=\[img\]) end\_time = time.time() - start\_time results\[mdl\_name\]\["papercards"\].append(structured\_output) results\[mdl\_name\]\["execution\_times"\].append(end\_time) results\[mdl\_name\]\["failures"\].append(None) except Exception as e: results\[mdl\_name\]\["papercards"\].append(None) results\[mdl\_name\]\["execution\_times"\].append(None) results\[mdl\_name\]\["failures"\].append(e) print()

Model: gpt\_4o

100%|█████████████████████████████████████████████████████████████████████████████████████| 35/35 \[09:01<00:00, 15.46s/it\]

Model: gpt\_4v

100%|█████████████████████████████████████████████████████████████████████████████████████| 35/35 \[17:29<00:00, 29.99s/it\]

Model: gpt\_4turbo

100%|█████████████████████████████████████████████████████████████████████████████████████| 35/35 \[14:50<00:00, 25.44s/it\]

Quantitative Analysis[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gpt4o_mm_structured_outputs/#quantitative-analysis)
--------------------------------------------------------------------------------------------------------------------------------------

Here, we'll perform a quick quantitative analysis of the various programs. Specifically, we compare the total number of failures, total execution time of successful data extraction jobs, and the average execution time.

In \[ \]:

Copied!

import numpy as np
import pandas as pd

import numpy as np import pandas as pd

In \[ \]:

Copied!

metrics \= {
    "gpt\_4o": {},
    "gpt\_4v": {},
    "gpt\_4turbo": {},
}

\# error count
for mdl\_name, mdl\_results in results.items():
    metrics\[mdl\_name\]\["error\_count"\] \= sum(
        el is not None for el in mdl\_results\["failures"\]
    )
    metrics\[mdl\_name\]\["total\_execution\_time"\] \= sum(
        el for el in mdl\_results\["execution\_times"\] if el is not None
    )
    metrics\[mdl\_name\]\["average\_execution\_time"\] \= metrics\[mdl\_name\]\[
        "total\_execution\_time"
    \] / (len(image\_documents) \- metrics\[mdl\_name\]\["error\_count"\])
    metrics\[mdl\_name\]\["median\_execution\_time"\] \= np.percentile(
        \[el for el in mdl\_results\["execution\_times"\] if el is not None\], q\=0.5
    )

metrics = { "gpt\_4o": {}, "gpt\_4v": {}, "gpt\_4turbo": {}, } # error count for mdl\_name, mdl\_results in results.items(): metrics\[mdl\_name\]\["error\_count"\] = sum( el is not None for el in mdl\_results\["failures"\] ) metrics\[mdl\_name\]\["total\_execution\_time"\] = sum( el for el in mdl\_results\["execution\_times"\] if el is not None ) metrics\[mdl\_name\]\["average\_execution\_time"\] = metrics\[mdl\_name\]\[ "total\_execution\_time" \] / (len(image\_documents) - metrics\[mdl\_name\]\["error\_count"\]) metrics\[mdl\_name\]\["median\_execution\_time"\] = np.percentile( \[el for el in mdl\_results\["execution\_times"\] if el is not None\], q=0.5 )

In \[ \]:

Copied!

pd.DataFrame(metrics)

pd.DataFrame(metrics)

Out\[ \]:

|  | gpt\_4o | gpt\_4v | gpt\_4turbo |
| --- | --- | --- | --- |
| error\_count | 0.000000 | 14.000000 | 1.000000 |
| total\_execution\_time | 541.128802 | 586.500559 | 762.130032 |
| average\_execution\_time | 15.460823 | 27.928598 | 22.415589 |
| median\_execution\_time | 5.377015 | 11.879649 | 7.177287 |

### GPT-4o is indeed faster![¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gpt4o_mm_structured_outputs/#gpt-4o-is-indeed-faster)

*   GPT-4o is clearly faster in both total execution time (of successful programs, failed extractions are not counted here) as well as mean and median execution times
*   Not only is GPT-4o faster, it was able to yield an extraction for all PaperCards. In contrast, GPT-4v failed 14 times, and GPT-4turbo failed 1 time.

Qualitative Analysis[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gpt4o_mm_structured_outputs/#qualitative-analysis)
------------------------------------------------------------------------------------------------------------------------------------

In this final section, we'll conduct a qualitative analysis over the extraction results. Ultimately, we'll end up with a "labelled" dataset of human evaluations on the data extraction task. The utilities provided next will allow you to perform a manual evaluation on the results of the three programs (or models) per PaperCard data extraction. Your job as a labeller is to rank the program's result from 0 to 5 with 5 being a perfect data extraction.

In \[ \]:

Copied!

from IPython.display import clear\_output

from IPython.display import clear\_output

In \[ \]:

Copied!

def display\_results\_and\_papercard(ix: int):
    \# image
    image\_path \= results\["gpt\_4o"\]\["image\_paths"\]\[ix\]

    \# outputs
    gpt\_4o\_output \= results\["gpt\_4o"\]\["papercards"\]\[ix\]
    gpt\_4v\_output \= results\["gpt\_4v"\]\["papercards"\]\[ix\]
    gpt\_4turbo\_output \= results\["gpt\_4turbo"\]\["papercards"\]\[ix\]

    image \= Image.open(image\_path).convert("RGB")
    plt.figure(figsize\=(10, 10))
    plt.axis("off")
    plt.imshow(image)
    plt.show()

    print("GPT-4o\\n")
    if gpt\_4o\_output is not None:
        print(json.dumps(gpt\_4o\_output.dict(), indent\=4))
    else:
        print("Failed to extract data")
    print()
    print("\\n")

    print("GPT-4turbo\\n")
    if gpt\_4turbo\_output is not None:
        print(json.dumps(gpt\_4turbo\_output.dict(), indent\=4))
    else:
        print("Failed to extract data")
    print()
    print("\\n") print("GPT-4v\\n") if gpt\_4v\_output is not None: print(json.dumps(gpt\_4v\_output.dict(), indent=4)) else: print("Failed to extract data") print() print("\\n")

In \[ \]:

Copied!

GRADES \= {
    "gpt\_4o": \[0\] \* len(image\_documents),
    "gpt\_4v": \[0\] \* len(image\_documents),
    "gpt\_4turbo": \[0\] \* len(image\_documents),
}

def manual\_evaluation\_single(img\_ix: int):
    """Update the GRADES dictionary for a single PaperCard
    data extraction task.
    """
    display\_results\_and\_papercard(img\_ix)

    gpt\_4o\_grade \= input(
        "Provide a rating from 0 to 5, with 5 being the highest for GPT-4o."
    )
    gpt\_4v\_grade \= input(
        "Provide a rating from 0 to 5, with 5 being the highest for GPT-4v."
    )
    gpt\_4turbo\_grade \= input(
        "Provide a rating from 0 to 5, with 5 being the highest for GPT-4turbo."
    )

    GRADES\["gpt\_4o"\]\[img\_ix\] \= gpt\_4o\_grade
    GRADES\["gpt\_4v"\]\[img\_ix\] \= gpt\_4v\_grade
    GRADES\["gpt\_4turbo"\]\[img\_ix\] \= gpt\_4turbo\_grade

def manual\_evaluations(img\_ix: Optional\[int\] \= None):
    """An interactive program for manually grading gpt-4 variants on the
    task of PaperCard data extraction.
    """
    if img\_ix is None:
        \# mark all results
        for ix in range(len(image\_documents)):
            print(f"You are marking {ix + 1} out of {len(image\_documents)}")
            print()
            manual\_evaluation\_single(ix)
            clear\_output(wait\=True)
    else:
        manual\_evaluation\_single(img\_ix)

GRADES = { "gpt\_4o": \[0\] \* len(image\_documents), "gpt\_4v": \[0\] \* len(image\_documents), "gpt\_4turbo": \[0\] \* len(image\_documents), } def manual\_evaluation\_single(img\_ix: int): """Update the GRADES dictionary for a single PaperCard data extraction task. """ display\_results\_and\_papercard(img\_ix) gpt\_4o\_grade = input( "Provide a rating from 0 to 5, with 5 being the highest for GPT-4o." ) gpt\_4v\_grade = input( "Provide a rating from 0 to 5, with 5 being the highest for GPT-4v." ) gpt\_4turbo\_grade = input( "Provide a rating from 0 to 5, with 5 being the highest for GPT-4turbo." ) GRADES\["gpt\_4o"\]\[img\_ix\] = gpt\_4o\_grade GRADES\["gpt\_4v"\]\[img\_ix\] = gpt\_4v\_grade GRADES\["gpt\_4turbo"\]\[img\_ix\] = gpt\_4turbo\_grade def manual\_evaluations(img\_ix: Optional\[int\] = None): """An interactive program for manually grading gpt-4 variants on the task of PaperCard data extraction. """ if img\_ix is None: # mark all results for ix in range(len(image\_documents)): print(f"You are marking {ix + 1} out of {len(image\_documents)}") print() manual\_evaluation\_single(ix) clear\_output(wait=True) else: manual\_evaluation\_single(img\_ix)

In \[ \]:

Copied!

manual\_evaluations()

manual\_evaluations()

You are marking 35 out of 35

![Image 5: No description has been provided for this image](blob:https://docs.llamaindex.ai/f7b793ca29117dedcf4650f345efa21d)

GPT-4o

{
    "title": "Prometheus: Inducing Fine-Grained Evaluation Capability In Language Models",
    "year": "2023",
    "authors": "Kim, Seungone et al.",
    "arxiv\_id": "arxiv:2310.08441",
    "main\_contribution": "An open-source LLM (LLMav2) evaluation specializing in fine-grained evaluations using human-like rubrics.",
    "insights": "While large LLMs like GPT-4 have shown impressive performance, they still lack fine-grained evaluation capabilities. Prometheus aims to address this by providing a dataset and evaluation framework that can assess models on a more detailed level.",
    "main\_results": \[
        "Prometheus matches or outperforms GPT-4.",
        "Prometheus can function as a reward model.",
        "Reference answers are crucial for fine-grained evaluation."
    \],
    "tech\_bits": "Score Rubric, Feedback Collection, Generated Instructions, Generated Responses, Generated Rubrics, Evaluations, Answers & Explanations"
}



GPT-4turbo

{
    "title": "Prometheus: Evaluating Capability In Language Models",
    "year": "2023",
    "authors": "Kim, George, et al.",
    "arxiv\_id": "arXiv:2310.05941",
    "main\_contribution": "Prometheus uses a custom feedback collection system designed for fine-tuning language models.",
    "insights": "The main insight is that fine-tuning language models on specific tasks can improve their overall performance, especially when using a custom feedback collection system.",
    "main\_results": \[
        "Prometheus LM outperforms GPT-4 on targeted feedback tasks.",
        "Prometheus LM's custom feedback function was 2% more effective than Prometheus 3.",
        "Feedback quality was better as reported by human judges."
    \],
    "tech\_bits": "The technical bits section includes a Rubric Score, Seed, Fine-Grained Annotations, and Models. It also shows a feedback collection process with a visual representation of the feedback loop involving seed, generated annotations, and models."
}



Provide a rating from 0 to 5, with 5 being the highest for GPT-4o. 3
Provide a rating from 0 to 5, with 5 being the highest for GPT-4v. 1.5
Provide a rating from 0 to 5, with 5 being the highest for GPT-4turbo. 1.5

In \[ \]:

Copied!

grades\_df \= pd.DataFrame(GRADES, dtype\=float)
grades\_df.mean()

grades\_df = pd.DataFrame(GRADES, dtype=float) grades\_df.mean()

Out\[ \]:

gpt\_4o        3.585714
gpt\_4v        1.300000
gpt\_4turbo    2.128571
dtype: float64

### Table Of Observations[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gpt4o_mm_structured_outputs/#table-of-observations)

In the table below, we list our general observations per component that we wished to extract from the PaperCard. GPT-4v and and GPT-4Turbo performed similarly with a slight edge to GPT-4Turbo. Generally speaking, GPT-4o demonstrated significantly better performance in this data extraction task than the other models. Finally, all models seemed to struggle on describing the Tech Bits section of the PaperCard, and at times, all of the models would generate a summary instead of an exact extraction; however, GPT-4o did this less than the other models.

| Extracted component | GPT-4o | GPT-4v & GPT-4Turbo |
| --- | --- | --- |
| Title, Year, Authors | very good, probably 100% | probably 80%, hallucinated on few examples |
| Arxiv ID | good, around 95% accurate | 70% accurate |
| Main Contribution | good (~80%) but couldn't extract multiple contributions listed | not so great, 60% accurate, some halluciations |
| Insights | not so good (~65%) did more summarization then extraction | did more summarization then extraction |
| Main Results | very good at extracting summary statements of main results | hallucinated a lot here |
| Tech Bits | unable to generate detailed descriptions of diagrams here | unable to generate detailed descriptions of diagrams here |

Summary[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gpt4o_mm_structured_outputs/#summary)
----------------------------------------------------------------------------------------------------------

*   GPT-4o is faster and fails less (0 times!) than GPT-4v and GPT-4turbo
*   GPT-4o yields better data extraction results than GPT-4v and GPT-4turbo
*   GPT-4o was very good at extracting facts from the PaperCard: Title, Author, Year, and headline statements of the Main Results section
*   GPT-4v and GPT-4turbo often hallucinated the main results and sometimes the authors
*   Results with GPT-4o can probably be improved using better prompting especially for extracting data from Insights section, but also for describing Tech Bits

Back to top

[Previous Multi-Modal LLM using Google's Gemini model for image understanding and build Retrieval Augmented Generation with LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gemini/)[Next GPT4-V Experiments with General, Specific questions and Chain Of Thought (COT) Prompting Technique.](https://docs.llamaindex.ai/en/stable/examples/multi_modal/gpt4v_experiments_cot/)

Hi, how can I help you?

🦙
