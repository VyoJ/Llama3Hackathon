Title: Guardrails Output Parsing - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/output_parsing/GuardrailsDemo/

Markdown Content:
Guardrails Output Parsing - LlamaIndex


First, set your openai api keys

In \[ \]:

Copied!

\# import os

\# os.environ\["OPENAI\_API\_KEY"\] = "sk-..."

\# import os # os.environ\["OPENAI\_API\_KEY"\] = "sk-..."

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai
%pip install llama\-index\-output\-parsers\-guardrails

%pip install llama-index-llms-openai %pip install llama-index-output-parsers-guardrails

Requirement already satisfied: llama-index-llms-openai in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (0.1.14)
Requirement already satisfied: llama-index-core<0.11.0,>=0.10.24 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from llama-index-llms-openai) (0.10.27)
Requirement already satisfied: PyYAML>=6.0.1 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (6.0.1)
Requirement already satisfied: SQLAlchemy\[asyncio\]>=1.4.49 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (2.0.29)
Requirement already satisfied: aiohttp<4.0.0,>=3.8.6 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (3.9.3)
Requirement already satisfied: dataclasses-json in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (0.6.4)
Requirement already satisfied: deprecated>=1.2.9.3 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (1.2.14)
Requirement already satisfied: dirtyjson<2.0.0,>=1.0.8 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (1.0.8)
Requirement already satisfied: fsspec>=2023.5.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (2024.3.1)
Requirement already satisfied: httpx in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (0.27.0)
Requirement already satisfied: llamaindex-py-client<0.2.0,>=0.1.16 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (0.1.16)
Requirement already satisfied: nest-asyncio<2.0.0,>=1.5.8 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (1.6.0)
Requirement already satisfied: networkx>=3.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (3.3)
Requirement already satisfied: nltk<4.0.0,>=3.8.1 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (3.8.1)
Requirement already satisfied: numpy in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (1.26.4)
Requirement already satisfied: openai>=1.1.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (1.16.2)
Requirement already satisfied: pandas in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (2.2.1)
Requirement already satisfied: pillow>=9.0.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (10.3.0)
Requirement already satisfied: requests>=2.31.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (2.31.0)
Requirement already satisfied: tenacity<9.0.0,>=8.2.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (8.2.3)
Requirement already satisfied: tiktoken>=0.3.3 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (0.5.2)
Requirement already satisfied: tqdm<5.0.0,>=4.66.1 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (4.66.2)
Requirement already satisfied: typing-extensions>=4.5.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (4.11.0)
Requirement already satisfied: typing-inspect>=0.8.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (0.9.0)
Requirement already satisfied: wrapt in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (1.16.0)
Requirement already satisfied: aiosignal>=1.1.2 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.6->llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (1.3.1)
Requirement already satisfied: attrs>=17.3.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.6->llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (23.2.0)
Requirement already satisfied: frozenlist>=1.1.1 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.6->llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (1.4.1)
Requirement already satisfied: multidict<7.0,>=4.5 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.6->llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (6.0.5)
Requirement already satisfied: yarl<2.0,>=1.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.6->llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (1.9.4)
Requirement already satisfied: pydantic>=1.10 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from llamaindex-py-client<0.2.0,>=0.1.16->llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (2.4.2)
Requirement already satisfied: anyio in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from httpx->llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (4.3.0)
Requirement already satisfied: certifi in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from httpx->llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (2024.2.2)
Requirement already satisfied: httpcore1.\*->httpx->llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (0.14.0)
Requirement already satisfied: click in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from nltk<4.0.0,>=3.8.1->llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (8.1.7)
Requirement already satisfied: joblib in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from nltk<4.0.0,>=3.8.1->llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (1.4.0)
Requirement already satisfied: regex>=2021.8.3 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from nltk<4.0.0,>=3.8.1->llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (2023.12.25)
Requirement already satisfied: distro<2,>=1.7.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from openai>=1.1.0->llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (1.9.0)
Requirement already satisfied: charset-normalizer<4,>=2 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from requests>=2.31.0->llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (3.3.2)
Requirement already satisfied: urllib3<3,>=1.21.1 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from requests>=2.31.0->llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (2.2.1)
Requirement already satisfied: greenlet!=0.4.17 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from SQLAlchemy\[asyncio\]>=1.4.49->llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (3.0.3)
Requirement already satisfied: mypy-extensions>=0.3.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from typing-inspect>=0.8.0->llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (1.0.0)
Requirement already satisfied: marshmallow<4.0.0,>=3.18.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from dataclasses-json->llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (3.21.1)
Requirement already satisfied: python-dateutil>=2.8.2 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from pandas->llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from pandas->llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (2024.1)
Requirement already satisfied: tzdata>=2022.7 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from pandas->llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (2024.1)
Requirement already satisfied: packaging>=17.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from marshmallow<4.0.0,>=3.18.0->dataclasses-json->llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (23.2)
Requirement already satisfied: annotated-types>=0.4.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from pydantic>=1.10->llamaindex-py-client<0.2.0,>=0.1.16->llama-index-core<0.11.0,>=0.10.24->llama-index-llms-openai) (0.6.0)
Requirement already satisfied: pydantic-core1.\* in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from httpx->llama-index-core<0.11.0,>=0.10.1->llama-index-output-parsers-guardrails) (1.0.5)
Requirement already satisfied: idna in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from httpx->llama-index-core<0.11.0,>=0.10.1->llama-index-output-parsers-guardrails) (3.6)
Requirement already satisfied: sniffio in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from httpx->llama-index-core<0.11.0,>=0.10.1->llama-index-output-parsers-guardrails) (1.3.1)
Requirement already satisfied: h11<0.15,>=0.13 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from httpcore2.10.1 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from pydantic<2.5,>=1.10.9->guardrails-ai<0.4.0,>=0.3.2->llama-index-output-parsers-guardrails) (2.10.1)
Requirement already satisfied: charset-normalizer<4,>=2 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from requests>=2.31.0->llama-index-core<0.11.0,>=0.10.1->llama-index-output-parsers-guardrails) (3.3.2)
Requirement already satisfied: urllib3<3,>=1.21.1 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from requests>=2.31.0->llama-index-core<0.11.0,>=0.10.1->llama-index-output-parsers-guardrails) (2.2.1)
Requirement already satisfied: markdown-it-py>=2.2.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from rich<14.0.0,>=13.6.0->guardrails-ai<0.4.0,>=0.3.2->llama-index-output-parsers-guardrails) (3.0.0)
Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from rich<14.0.0,>=13.6.0->guardrails-ai<0.4.0,>=0.3.2->llama-index-output-parsers-guardrails) (2.17.2)
Requirement already satisfied: greenlet!=0.4.17 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from SQLAlchemy\[asyncio\]>=1.4.49->llama-index-core<0.11.0,>=0.10.1->llama-index-output-parsers-guardrails) (3.0.3)
Requirement already satisfied: mypy-extensions>=0.3.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from typing-inspect>=0.8.0->llama-index-core<0.11.0,>=0.10.1->llama-index-output-parsers-guardrails) (1.0.0)
Requirement already satisfied: marshmallow<4.0.0,>=3.18.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from dataclasses-json->llama-index-core<0.11.0,>=0.10.1->llama-index-output-parsers-guardrails) (3.21.1)
Requirement already satisfied: pytz>=2020.1 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from pandas->llama-index-core<0.11.0,>=0.10.1->llama-index-output-parsers-guardrails) (2024.1)
Requirement already satisfied: tzdata>=2022.7 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from pandas->llama-index-core<0.11.0,>=0.10.1->llama-index-output-parsers-guardrails) (2024.1)
Requirement already satisfied: mdurl~=0.1 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from markdown-it-py>=2.2.0->rich<14.0.0,>=13.6.0->guardrails-ai<0.4.0,>=0.3.2->llama-index-output-parsers-guardrails) (0.1.2)
Requirement already satisfied: packaging>=17.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from marshmallow<4.0.0,>=3.18.0->dataclasses-json->llama-index-core<0.11.0,>=0.10.1->llama-index-output-parsers-guardrails) (23.2)
Requirement already satisfied: setuptools in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from zope.interface->eliot<2.0.0,>=1.15.0->guardrails-ai<0.4.0,>=0.3.2->llama-index-output-parsers-guardrails) (65.5.0)
Using cached guardrails\_ai-0.3.3-py3-none-any.whl (148 kB)
Installing collected packages: guardrails-ai
  Attempting uninstall: guardrails-ai
    Found existing installation: guardrails-ai 0.4.2
    Uninstalling guardrails-ai-0.4.2:
      Successfully uninstalled guardrails-ai-0.4.2
Successfully installed guardrails-ai-0.3.3

\[notice\] A new release of pip is available: 23.2.1 -> 24.0
\[notice\] To update, run: pip install --upgrade pip
Note: you may need to restart the kernel to use updated packages.

In \[ \]:

Copied!

%pip install guardrails\-ai

%pip install guardrails-ai

Requirement already satisfied: guardrails-ai in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (0.3.3)
Requirement already satisfied: eliot<2.0.0,>=1.15.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from guardrails-ai) (1.15.0)
Requirement already satisfied: eliot-tree<22.0.0,>=21.0.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from guardrails-ai) (21.0.0)
Requirement already satisfied: griffe<0.37.0,>=0.36.9 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from guardrails-ai) (0.36.9)
Requirement already satisfied: lxml<5.0.0,>=4.9.3 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from guardrails-ai) (4.9.4)
Requirement already satisfied: openai<2 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from guardrails-ai) (1.16.2)
Requirement already satisfied: pydantic<2.5,>=1.10.9 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from guardrails-ai) (2.4.2)
Requirement already satisfied: pydash<8.0.0,>=7.0.6 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from guardrails-ai) (7.0.7)
Requirement already satisfied: python-dateutil<3.0.0,>=2.8.2 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from guardrails-ai) (2.9.0.post0)
Requirement already satisfied: regex<2024.0.0,>=2023.10.3 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from guardrails-ai) (2023.12.25)
Requirement already satisfied: rich<14.0.0,>=13.6.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from guardrails-ai) (13.7.1)
Requirement already satisfied: rstr<4.0.0,>=3.2.2 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from guardrails-ai) (3.2.2)
Requirement already satisfied: tenacity>=8.1.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from guardrails-ai) (8.2.3)
Requirement already satisfied: tiktoken<0.6.0,>=0.5.1 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from guardrails-ai) (0.5.2)
Requirement already satisfied: typer<0.10.0,>=0.9.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from guardrails-ai) (0.9.4)
Requirement already satisfied: typing-extensions<5.0.0,>=4.8.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from guardrails-ai) (4.11.0)
Requirement already satisfied: six in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from eliot<2.0.0,>=1.15.0->guardrails-ai) (1.16.0)
Requirement already satisfied: zope.interface in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from eliot<2.0.0,>=1.15.0->guardrails-ai) (6.2)
Requirement already satisfied: pyrsistent>=0.11.8 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from eliot<2.0.0,>=1.15.0->guardrails-ai) (0.20.0)
Requirement already satisfied: boltons>=19.0.1 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from eliot<2.0.0,>=1.15.0->guardrails-ai) (24.0.0)
Requirement already satisfied: orjson in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from eliot<2.0.0,>=1.15.0->guardrails-ai) (3.10.0)
Requirement already satisfied: jmespath>=0.7.1 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from eliot-tree<22.0.0,>=21.0.0->guardrails-ai) (1.0.1)
Requirement already satisfied: iso8601>=0.1.10 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from eliot-tree<22.0.0,>=21.0.0->guardrails-ai) (2.1.0)
Requirement already satisfied: colored>=1.4.2 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from eliot-tree<22.0.0,>=21.0.0->guardrails-ai) (2.2.4)
Requirement already satisfied: toolz>=0.8.2 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from eliot-tree<22.0.0,>=21.0.0->guardrails-ai) (0.12.1)
Requirement already satisfied: colorama>=0.4 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from griffe<0.37.0,>=0.36.9->guardrails-ai) (0.4.6)
Requirement already satisfied: anyio<5,>=3.5.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from openai<2->guardrails-ai) (4.3.0)
Requirement already satisfied: distro<2,>=1.7.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from openai<2->guardrails-ai) (1.9.0)
Requirement already satisfied: httpx<1,>=0.23.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from openai<2->guardrails-ai) (0.27.0)
Requirement already satisfied: sniffio in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from openai<2->guardrails-ai) (1.3.1)
Requirement already satisfied: tqdm>4 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from openai<2->guardrails-ai) (4.66.2)
Requirement already satisfied: annotated-types>=0.4.0 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from pydantic<2.5,>=1.10.9->guardrails-ai) (0.6.0)
Requirement already satisfied: pydantic-core1.\* in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from httpx<1,>=0.23.0->openai<2->guardrails-ai) (1.0.5)
Requirement already satisfied: h11<0.15,>=0.13 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from httpcore==1.\*->httpx<1,>=0.23.0->openai<2->guardrails-ai) (0.14.0)
Requirement already satisfied: mdurl~=0.1 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from markdown-it-py>=2.2.0->rich<14.0.0,>=13.6.0->guardrails-ai) (0.1.2)
Requirement already satisfied: charset-normalizer<4,>=2 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from requests>=2.26.0->tiktoken<0.6.0,>=0.5.1->guardrails-ai) (3.3.2)
Requirement already satisfied: urllib3<3,>=1.21.1 in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from requests>=2.26.0->tiktoken<0.6.0,>=0.5.1->guardrails-ai) (2.2.1)
Requirement already satisfied: setuptools in /Users/zaydsimjee/workspace/zayd\_forks/llama\_index/.venv/lib/python3.11/site-packages (from zope.interface->eliot<2.0.0,>=1.15.0->guardrails-ai) (65.5.0)

\[notice\] A new release of pip is available: 23.2.1 -> 24.0
\[notice\] To update, run: pip install --upgrade pip
Note: you may need to restart the kernel to use updated packages.

#### Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/GuardrailsDemo/#download-data)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!curl 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \> 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !curl 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' > 'data/paul\_graham/paul\_graham\_essay.txt'

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 75042  100 75042    0     0   390k      0 --:--:-- --:--:-- --:--:--  396k

#### Load documents, build the VectorStoreIndex[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/GuardrailsDemo/#load-documents-build-the-vectorstoreindex)

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout)) from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader

In \[ \]:

Copied!

\# load documents
documents \= SimpleDirectoryReader("./data/paul\_graham/").load\_data()

\# load documents documents = SimpleDirectoryReader("./data/paul\_graham/").load\_data()

In \[ \]:

Copied!

index \= VectorStoreIndex.from\_documents(documents, chunk\_size\=512)

index = VectorStoreIndex.from\_documents(documents, chunk\_size=512)

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"

#### Define Query + Guardrails Spec[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/GuardrailsDemo/#define-query-guardrails-spec)

In \[ \]:

Copied!

from llama\_index.output\_parsers.guardrails import GuardrailsOutputParser

from llama\_index.output\_parsers.guardrails import GuardrailsOutputParser

**Define custom QA and Refine Prompts**

**Define Guardrails Spec**

In \[ \]:

Copied!

\# You can either define a RailSpec and initialise a Guard object from\_rail\_string()
\# OR define Pydantic classes and initialise a Guard object from\_pydantic()
\# For more info: https://docs.guardrailsai.com/defining\_guards/pydantic/
\# Guardrails recommends Pydantic

from pydantic import BaseModel, Field
from typing import List
import guardrails as gd

class BulletPoints(BaseModel):
    \# In all the fields below, you can define validators as well
    \# Left out for brevity
    explanation: str \= Field()
    explanation2: str \= Field()
    explanation3: str \= Field()

class Explanation(BaseModel):
    points: BulletPoints \= Field(
        description\="Bullet points regarding events in the author's life."
    )

\# Define the prompt
prompt \= """
Query string here.

${gr.xml\_prefix\_prompt}

${output\_schema}

${gr.json\_suffix\_prompt\_v2\_wo\_none}
"""

\# You can either define a RailSpec and initialise a Guard object from\_rail\_string() # OR define Pydantic classes and initialise a Guard object from\_pydantic() # For more info: https://docs.guardrailsai.com/defining\_guards/pydantic/ # Guardrails recommends Pydantic from pydantic import BaseModel, Field from typing import List import guardrails as gd class BulletPoints(BaseModel): # In all the fields below, you can define validators as well # Left out for brevity explanation: str = Field() explanation2: str = Field() explanation3: str = Field() class Explanation(BaseModel): points: BulletPoints = Field( description="Bullet points regarding events in the author's life." ) # Define the prompt prompt = """ Query string here. gr.xmlprefixpromptgr.xmlprefixprompt {output\_schema} ${gr.json\_suffix\_prompt\_v2\_wo\_none} """

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI

\# Create a guard object
guard \= gd.Guard.from\_pydantic(output\_class\=Explanation, prompt\=prompt)

\# Create output parse object
output\_parser \= GuardrailsOutputParser(guard)

\# attach to an llm object
llm \= OpenAI(output\_parser\=output\_parser)

from llama\_index.llms.openai import OpenAI # Create a guard object guard = gd.Guard.from\_pydantic(output\_class=Explanation, prompt=prompt) # Create output parse object output\_parser = GuardrailsOutputParser(guard) # attach to an llm object llm = OpenAI(output\_parser=output\_parser)

In \[ \]:

Copied!

from llama\_index.core.prompts.default\_prompts import (
    DEFAULT\_TEXT\_QA\_PROMPT\_TMPL,
)

\# take a look at the new QA template!
fmt\_qa\_tmpl \= output\_parser.format(DEFAULT\_TEXT\_QA\_PROMPT\_TMPL)
print(fmt\_qa\_tmpl)

from llama\_index.core.prompts.default\_prompts import ( DEFAULT\_TEXT\_QA\_PROMPT\_TMPL, ) # take a look at the new QA template! fmt\_qa\_tmpl = output\_parser.format(DEFAULT\_TEXT\_QA\_PROMPT\_TMPL) print(fmt\_qa\_tmpl)

Context information is below.
---------------------
{context\_str}
---------------------
Given the context information and not prior knowledge, answer the query.
Query: {query\_str}
Answer: 


Given below is XML that describes the information to extract from this document and the tags to extract it into.


<output>
    <object name="points" description="Bullet points regarding events in the author's life.">
        <string name="explanation"/>
        <string name="explanation2"/>
        <string name="explanation3"/>
    </object>
</output>



ONLY return a valid JSON object (no other text is necessary). The JSON MUST conform to the XML format, including any types and format requests e.g. requests for lists, objects and specific types. Be correct and concise.

#### Query Index[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/GuardrailsDemo/#query-index)

In \[ \]:

Copied!

query\_engine \= index.as\_query\_engine(
    llm\=llm,
)
response \= query\_engine.query(
    "What are the three items the author did growing up?",
)

query\_engine = index.as\_query\_engine( llm=llm, ) response = query\_engine.query( "What are the three items the author did growing up?", )

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/embeddings "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"

In \[ \]:

Copied!

print(response)

print(response)

{'points': {'explanation': 'Writing short stories', 'explanation2': 'Programming on the IBM 1401 in 9th grade', 'explanation3': 'Getting a TRS-80 computer and starting programming in 1980'}}

In \[ \]:

Copied!

\# View a summary of what the guard did
guard.history.last.tree

\# View a summary of what the guard did guard.history.last.tree

Out\[ \]:

Logs
└── ╭────────────────────────────────────────────────── Step 0 ───────────────────────────────────────────────────╮
    │ ╭──────────────────────────────────────────────── Prompt ─────────────────────────────────────────────────╮ │
    │ │ No prompt                                                                                               │ │
    │ ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────╯ │
    │ ╭──────────────────────────────────────────── Message History ────────────────────────────────────────────╮ │
    │ │ No message history.                                                                                     │ │
    │ ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────╯ │
    │ ╭──────────────────────────────────────────── Raw LLM Output ─────────────────────────────────────────────╮ │
    │ │ {                                                                                                       │ │
    │ │     "points": {                                                                                         │ │
    │ │         "explanation": "Writing short stories",                                                         │ │
    │ │         "explanation2": "Programming on the IBM 1401 in 9th grade",                                     │ │
    │ │         "explanation3": "Getting a TRS-80 computer and starting programming in 1980"                    │ │
    │ │     }                                                                                                   │ │
    │ │ }                                                                                                       │ │
    │ ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────╯ │
    │ ╭─────────────────────────────────────────── Validated Output ────────────────────────────────────────────╮ │
    │ │ {                                                                                                       │ │
    │ │     'points': {                                                                                         │ │
    │ │         'explanation': 'Writing short stories',                                                         │ │
    │ │         'explanation2': 'Programming on the IBM 1401 in 9th grade',                                     │ │
    │ │         'explanation3': 'Getting a TRS-80 computer and starting programming in 1980'                    │ │
    │ │     }                                                                                                   │ │
    │ │ }                                                                                                       │ │
    │ ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────╯ │
    ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

Back to top

[Previous The ObjectIndex Class](https://docs.llamaindex.ai/en/stable/examples/objects/object_index/)[Next Langchain Output Parsing](https://docs.llamaindex.ai/en/stable/examples/output_parsing/LangchainOutputParserDemo/)

Hi, how can I help you?

🦙
