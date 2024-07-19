Title: Github Issue Analysis - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/usecases/github_issue_analysis/

Markdown Content:
Github Issue Analysis - LlamaIndex


Setup[¶](https://docs.llamaindex.ai/en/stable/examples/usecases/github_issue_analysis/#setup)
---------------------------------------------------------------------------------------------

To use the github repo issue loader, you need to set your github token in the environment.

See [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) for how to get a github token.  
See [llama-hub](https://llama-hub-ui.vercel.app/l/github_repo_issues) for more details about the loader.

In \[ \]:

Copied!

%pip install llama\-index\-readers\-github
%pip install llama\-index\-llms\-openai
%pip install llama\-index\-program\-openai

%pip install llama-index-readers-github %pip install llama-index-llms-openai %pip install llama-index-program-openai

In \[ \]:

Copied!

import os

os.environ\["GITHUB\_TOKEN"\] \= "<your github token>"

import os os.environ\["GITHUB\_TOKEN"\] = ""

Load Github Issue tickets[¶](https://docs.llamaindex.ai/en/stable/examples/usecases/github_issue_analysis/#load-github-issue-tickets)
-------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

import os

from llama\_index.readers.github import (
    GitHubRepositoryIssuesReader,
    GitHubIssuesClient,
)

github\_client \= GitHubIssuesClient()
loader \= GitHubRepositoryIssuesReader(
    github\_client,
    owner\="jerryjliu",
    repo\="llama\_index",
    verbose\=True,
)

docs \= loader.load\_data()

import os from llama\_index.readers.github import ( GitHubRepositoryIssuesReader, GitHubIssuesClient, ) github\_client = GitHubIssuesClient() loader = GitHubRepositoryIssuesReader( github\_client, owner="jerryjliu", repo="llama\_index", verbose=True, ) docs = loader.load\_data()

Found 100 issues in the repo page 1
Resulted in 100 documents
Found 100 issues in the repo page 2
Resulted in 200 documents
Found 100 issues in the repo page 3
Resulted in 300 documents
Found 100 issues in the repo page 4
Resulted in 400 documents
Found 4 issues in the repo page 5
Resulted in 404 documents
No more issues found, stopping

Quick inspection

In \[ \]:

Copied!

docs\[10\].text

docs\[10\].text

Out\[ \]:

"feat(context length): QnA Summarization as a relevant information extractor\\n### Feature Description\\r\\n\\r\\nSummarizer can help in cases where the information is evenly distributed in the document i.e. a large amount of context is required but the language is verbose or there are many irrelevant details. Summarization specific to the query can help.\\r\\n\\r\\nEither cheap local model or even LLM are options; the latter for reducing latency due to large context window in RAG. \\r\\n\\r\\nAnother place where it helps is that percentile and top\_k don't account for variable information density. (However, this may be solved with inter-node sub-node reranking). \\r\\n"

In \[ \]:

Copied!

docs\[10\].metadata

docs\[10\].metadata

Out\[ \]:

{'state': 'open',
 'created\_at': '2023-07-13T11:16:30Z',
 'url': 'https://api.github.com/repos/jerryjliu/llama\_index/issues/6889',
 'source': 'https://github.com/jerryjliu/llama\_index/issues/6889'}

Extract themes[¶](https://docs.llamaindex.ai/en/stable/examples/usecases/github_issue_analysis/#extract-themes)
---------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

%load\_ext autoreload
%autoreload 2

%load\_ext autoreload %autoreload 2

The autoreload extension is already loaded. To reload it, use:
  %reload\_ext autoreload

In \[ \]:

Copied!

from pydantic import BaseModel
from typing import List
from tqdm.asyncio import asyncio

from llama\_index.program.openai import OpenAIPydanticProgram
from llama\_index.llms.openai import OpenAI
from llama\_index.core.async\_utils import batch\_gather

from pydantic import BaseModel from typing import List from tqdm.asyncio import asyncio from llama\_index.program.openai import OpenAIPydanticProgram from llama\_index.llms.openai import OpenAI from llama\_index.core.async\_utils import batch\_gather

In \[ \]:

Copied!

prompt\_template\_str \= """\\
Here is a Github Issue ticket.

{ticket}

Please extract central themes and output a list of tags.\\
"""

prompt\_template\_str = """\\ Here is a Github Issue ticket. {ticket} Please extract central themes and output a list of tags.\\ """

In \[ \]:

Copied!

class TagList(BaseModel):
    """A list of tags corresponding to central themes of an issue."""

    tags: List\[str\]

class TagList(BaseModel): """A list of tags corresponding to central themes of an issue.""" tags: List\[str\]

In \[ \]:

Copied!

program \= OpenAIPydanticProgram.from\_defaults(
    prompt\_template\_str\=prompt\_template\_str,
    output\_cls\=TagList,
)

program = OpenAIPydanticProgram.from\_defaults( prompt\_template\_str=prompt\_template\_str, output\_cls=TagList, )

In \[ \]:

Copied!

tasks \= \[program.acall(ticket\=doc) for doc in docs\]

tasks = \[program.acall(ticket=doc) for doc in docs\]

In \[ \]:

Copied!

output \= await batch\_gather(tasks, batch\_size\=10, verbose\=True)

output = await batch\_gather(tasks, batch\_size=10, verbose=True)

\[Optional\] Save/Load Extracted Themes[¶](https://docs.llamaindex.ai/en/stable/examples/usecases/github_issue_analysis/#optional-saveload-extracted-themes)
------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

import pickle

import pickle

In \[ \]:

Copied!

with open("github\_issue\_analysis\_data.pkl", "wb") as f:
    pickle.dump(tag\_lists, f)

with open("github\_issue\_analysis\_data.pkl", "wb") as f: pickle.dump(tag\_lists, f)

In \[ \]:

Copied!

with open("github\_issue\_analysis\_data.pkl", "rb") as f:
    tag\_lists \= pickle.load(f)
    print(f"Loaded tag lists for {len(tag\_lists)} tickets")

with open("github\_issue\_analysis\_data.pkl", "rb") as f: tag\_lists = pickle.load(f) print(f"Loaded tag lists for {len(tag\_lists)} tickets")

Summarize Themes[¶](https://docs.llamaindex.ai/en/stable/examples/usecases/github_issue_analysis/#summarize-themes)
-------------------------------------------------------------------------------------------------------------------

Build prompt

In \[ \]:

Copied!

prompt \= """
Here is a list of central themes (in the form of tags) extracted from a list of Github Issue tickets.
Tags for each ticket is separated by 2 newlines.

{tag\_lists\_str}

Please summarize the key takeaways and what we should prioritize to fix.
"""

tag\_lists\_str \= "\\n\\n".join(\[str(tag\_list) for tag\_list in tag\_lists\])

prompt \= prompt.format(tag\_lists\_str\=tag\_lists\_str)

prompt = """ Here is a list of central themes (in the form of tags) extracted from a list of Github Issue tickets. Tags for each ticket is separated by 2 newlines. {tag\_lists\_str} Please summarize the key takeaways and what we should prioritize to fix. """ tag\_lists\_str = "\\n\\n".join(\[str(tag\_list) for tag\_list in tag\_lists\]) prompt = prompt.format(tag\_lists\_str=tag\_lists\_str)

Summarize with GPT-4

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI

response \= OpenAI(model\="gpt-4").stream\_complete(prompt)

from llama\_index.llms.openai import OpenAI response = OpenAI(model="gpt-4").stream\_complete(prompt)

In \[ \]:

Copied!

for r in response:
    print(r.delta, end\="")

for r in response: print(r.delta, end="")

1\. Bug Fixes: There are numerous bugs reported across different components such as 'Updating/Refreshing documents', 'Supabase Vector Store', 'Parsing', 'Qdrant', 'LLM event', 'Service context', 'Chroma db', 'Markdown Reader', 'Search\_params', 'Index\_params', 'MilvusVectorStore', 'SentenceSplitter', 'Embedding timeouts', 'PGVectorStore', 'NotionPageReader', 'VectorIndexRetriever', 'Knowledge Graph', 'LLM content', and 'Query engine'. These issues need to be prioritized and resolved to ensure smooth functioning of the system.

2. Feature Requests: There are several feature requests like 'QnA Summarization', 'BEIR evaluation', 'Cross-Node Ranking', 'Node content', 'PruningMode', 'RelevanceMode', 'Local-model defaults', 'Dynamically selecting from multiple prompts', 'Human-In-The-Loop Multistep Query', 'Explore Tree-of-Thought', 'Postprocessing', 'Relevant Section Extraction', 'Original Source Reconstruction', 'Varied Latency in Retrieval', and 'MLFlow'. These features can enhance the capabilities of the system and should be considered for future development.

3. Code Refactoring and Testing: There are mentions of code refactoring, testing, and code review. This indicates a need for improving code quality and ensuring robustness through comprehensive testing.

4. Documentation: There are several mentions of documentation updates, indicating a need for better documentation to help users understand and use the system effectively.

5. Integration: There are mentions of integration with other systems like 'BEIR', 'Langflow', 'Hugging Face', 'OpenAI', 'DynamoDB', and 'CometML'. This suggests a need for better interoperability with other systems.

6. Performance and Efficiency: There are mentions of 'Parallelize sync APIs', 'Average query time', 'Efficiency', 'Upgrade', and 'Execution Plan'. This indicates a need for improving the performance and efficiency of the system.

7. User Experience (UX): There are mentions of 'UX', 'Varied Latency in Retrieval', and 'Human-In-The-Loop Multistep Query'. This suggests a need for improving the user experience.

8. Error Handling: There are several mentions of error handling, indicating a need for better error handling mechanisms to ensure system robustness.

9. Authentication: There are mentions of 'authentication' and 'API key', indicating a need for secure access mechanisms.

10. Multilingual Support: There is a mention of 'LLM中文应用交流微信群', indicating a need for multilingual support.

Back to top

[Previous Email Data Extraction](https://docs.llamaindex.ai/en/stable/examples/usecases/email_data_extraction/)[Next AWSDocDBDemo](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AWSDocDBDemo/)
