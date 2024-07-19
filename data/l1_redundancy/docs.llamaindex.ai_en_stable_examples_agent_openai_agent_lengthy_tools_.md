Title: OpenAI Agent Workarounds for Lengthy Tool Descriptions

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_lengthy_tools/

Markdown Content:
OpenAI Agent Workarounds for Lengthy Tool Descriptions - LlamaIndex


In this demo, we illustrate a workaround for defining an OpenAI tool whose description exceeds OpenAI's current limit of 1024 characters. For simplicity, we will build upon the `QueryPlanTool` notebook example.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-agent\-openai
%pip install llama\-index\-llms\-openai

%pip install llama-index-agent-openai %pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

%load\_ext autoreload
%autoreload 2

%load\_ext autoreload %autoreload 2

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama\_index.llms.openai import OpenAI

from llama\_index.core import SimpleDirectoryReader, VectorStoreIndex from llama\_index.llms.openai import OpenAI

In \[ \]:

Copied!

llm \= OpenAI(temperature\=0, model\="gpt-4")

llm = OpenAI(temperature=0, model="gpt-4")

Download Data[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_lengthy_tools/#download-data)
---------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

!mkdir \-p 'data/10q/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10q/uber\_10q\_march\_2022.pdf' \-O 'data/10q/uber\_10q\_march\_2022.pdf'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10q/uber\_10q\_june\_2022.pdf' \-O 'data/10q/uber\_10q\_june\_2022.pdf'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10q/uber\_10q\_sept\_2022.pdf' \-O 'data/10q/uber\_10q\_sept\_2022.pdf'

!mkdir -p 'data/10q/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10q/uber\_10q\_march\_2022.pdf' -O 'data/10q/uber\_10q\_march\_2022.pdf' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10q/uber\_10q\_june\_2022.pdf' -O 'data/10q/uber\_10q\_june\_2022.pdf' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10q/uber\_10q\_sept\_2022.pdf' -O 'data/10q/uber\_10q\_sept\_2022.pdf'

\--2024-05-23 13:36:24--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10q/uber\_10q\_march\_2022.pdf
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.110.133, 185.199.109.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1260185 (1.2M) \[application/octet-stream\]
Saving to: ‘data/10q/uber\_10q\_march\_2022.pdf’

data/10q/uber\_10q\_m 100%\[>\]   1.18M  --.-KB/s    in 0.04s   

2024-05-23 13:36:24 (26.4 MB/s) - ‘data/10q/uber\_10q\_june\_2022.pdf’ saved \[1238483/1238483\]

--2024-05-23 13:36:24--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10q/uber\_10q\_sept\_2022.pdf
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.110.133, 185.199.109.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1178622 (1.1M) \[application/octet-stream\]
Saving to: ‘data/10q/uber\_10q\_sept\_2022.pdf’

data/10q/uber\_10q\_s 100%\[ Calling Function 

Out\[ \]:

Response(response="The risk factors for Uber in September 2022 included:\\n\\n1. Failure to meet regulatory requirements related to climate change or to meet stated climate change commitments, which could impact costs, operations, brand, and reputation.\\n2. The ongoing COVID-19 pandemic and responses to it were also a risk, as they had an adverse impact on business and operations, including reducing the demand for Mobility offerings globally and affecting travel behavior and demand.\\n3. Catastrophic events such as disease, weather events, war, or terrorist attacks could also adversely impact the business, financial condition, and results of operation.\\n4. Other risks included errors, bugs, or vulnerabilities in the platform's code or systems, inappropriate or controversial data practices, and the growing use of artificial intelligence.\\n5. Climate change related physical and transition risks, such as market shifts toward electric vehicles and lower carbon business models, and risks related to extreme weather events or natural disasters, were also a concern.", source\_nodes=\[NodeWithScore(node=TextNode(id\_='a92c1e5e-6285-4225-8c87-b9dbd2b07d89', embedding=None, metadata={'page\_label': '74', 'file\_name': 'uber\_10q\_sept\_2022.pdf', 'file\_path': 'data/10q/uber\_10q\_sept\_2022.pdf', 'file\_type': 'application/pdf', 'file\_size': 1178622, 'creation\_date': '2024-05-23', 'last\_modified\_date': '2024-05-23'}, excluded\_embed\_metadata\_keys=\['file\_name', 'file\_type', 'file\_size', 'creation\_date', 'last\_modified\_date', 'last\_accessed\_date'\], excluded\_llm\_metadata\_keys=\['file\_name', 'file\_type', 'file\_size', 'creation\_date', 'last\_modified\_date', 'last\_accessed\_date'\], relationships={<NodeRelationship.SOURCE: '1'>: RelatedNodeInfo(node\_id='b5e99044-59e9-439a-9e53-802a517b287d', node\_type=<ObjectType.DOCUMENT: '4'>, metadata={'page\_label': '74', 'file\_name': 'uber\_10q\_sept\_2022.pdf', 'file\_path': 'data/10q/uber\_10q\_sept\_2022.pdf', 'file\_type': 'application/pdf', 'file\_size': 1178622, 'creation\_date': '2024-05-23', 'last\_modified\_date': '2024-05-23'}, hash='edddd9bda362411ae2e4d36144b5049c8b2ce5ec26047fa7c04003a9265aa87d'), <NodeRelationship.PREVIOUS: '2'>: RelatedNodeInfo(node\_id='04ae9351-0136-491a-8756-41dc2b8071a1', node\_type=<ObjectType.TEXT: '1'>, metadata={'page\_label': '74', 'file\_name': 'uber\_10q\_sept\_2022.pdf', 'file\_path': 'data/10q/uber\_10q\_sept\_2022.pdf', 'file\_type': 'application/pdf', 'file\_size': 1178622, 'creation\_date': '2024-05-23', 'last\_modified\_date': '2024-05-23'}, hash='bdc5ab49a54e18f73a2687096148f9e567a053ea2d3bd3c051956fb359078f5e')}, text='Any failure to\\nmeet regulatory requirements related to climate change, or to meet our stated climate change commitments on the timeframe we committed to, or at all, could have\\nan adverse impact on our costs and ability to operate, as well as harm our brand, reputation, and consequently, our business.\\nGeneral Economic Risks\\nOutbreaks of contagious disease, such as the COVID-19 pandemic and the impact of actions to mitigate the such disease or pandemic, have adversely impacted\\nand could continue to adversely impact our business, financial condition and results of operations.\\nOccurrence of a catastrophic event, including but not limited to disease, a weather event, war, or terrorist attack, could adversely impact our business, financial\\ncondition and results of operation. We also face risks related to health epidemics, outbreaks of contagious disease, and other adverse health developments. For\\nexample, the ongoing COVID-19 pandemic and responses to it have had, and may continue to have, an adverse impact on our business and operations, including,\\nfor example, by reducing the demand for our Mobility offerings globally, and affecting travel behavior and demand. Even as COVID-related restrictions have been\\nlifted and many regions around the world are making progress in their recovery from the pandemic, we have experienced and may continue to experience Driver\\nsupply constraints, and we are observing that consumer demand for Mobility is recovering faster than driver availability, as such supply constraints have been and\\nmay continue to be impacted by concerns regarding the COVID-19 pandemic. Furthermore, to support social distancing, we temporarily suspended our shared\\nrides offering globally, and recently re-launched our shared rides offering in certain regions.\\n73', start\_char\_idx=4469, end\_char\_idx=6258, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.8039095664957979), NodeWithScore(node=TextNode(id\_='04ae9351-0136-491a-8756-41dc2b8071a1', embedding=None, metadata={'page\_label': '74', 'file\_name': 'uber\_10q\_sept\_2022.pdf', 'file\_path': 'data/10q/uber\_10q\_sept\_2022.pdf', 'file\_type': 'application/pdf', 'file\_size': 1178622, 'creation\_date': '2024-05-23', 'last\_modified\_date': '2024-05-23'}, excluded\_embed\_metadata\_keys=\['file\_name', 'file\_type', 'file\_size', 'creation\_date', 'last\_modified\_date', 'last\_accessed\_date'\], excluded\_llm\_metadata\_keys=\['file\_name', 'file\_type', 'file\_size', 'creation\_date', 'last\_modified\_date', 'last\_accessed\_date'\], relationships={<NodeRelationship.SOURCE: '1'>: RelatedNodeInfo(node\_id='b5e99044-59e9-439a-9e53-802a517b287d', node\_type=<ObjectType.DOCUMENT: '4'>, metadata={'page\_label': '74', 'file\_name': 'uber\_10q\_sept\_2022.pdf', 'file\_path': 'data/10q/uber\_10q\_sept\_2022.pdf', 'file\_type': 'application/pdf', 'file\_size': 1178622, 'creation\_date': '2024-05-23', 'last\_modified\_date': '2024-05-23'}, hash='edddd9bda362411ae2e4d36144b5049c8b2ce5ec26047fa7c04003a9265aa87d'), <NodeRelationship.NEXT: '3'>: RelatedNodeInfo(node\_id='a92c1e5e-6285-4225-8c87-b9dbd2b07d89', node\_type=<ObjectType.TEXT: '1'>, metadata={}, hash='4862564636269739d75565c6c9dc166659cf52e29ec337fe9b85802beeb2ce7d')}, text='platform to platform users. In addition, our release of new software in the past has inadvertently caused, and may in the future cause, interruptions in the\\navailability or functionality of our platform. Any errors, bugs, or vulnerabilities discovered in our code or systems after release could result in an interruption in the\\navailability of our platform or a negative experience for Drivers, consumers, merchants, Shippers, and Carriers, and could also result in negative publicity and\\nunfavorable media coverage, damage to our reputation, loss of platform users, loss of revenue or liability for damages, regulatory inquiries, or other proceedings,\\nany of which could adversely affect our business and financial results. In addition, our growing use of artificial intelligence (“AI”) (including machine learning) in\\nour offerings presents additional risks. AI algorithms or automated processing of data may be flawed and datasets may be insufficient or contain biased information.\\nInappropriate or controversial data practices by us or others could impair the acceptance of AI solutions or subject us to lawsuits and regulatory investigations.\\nThese deficiencies could undermine the decisions, predictions or analysis AI applications produce, or lead to unintentional bias and discrimination, subjecting us to\\ncompetitive harm, legal liability, and brand or reputational harm.\\nWe are subject to climate change risks, including physical and transitional risks, and if we are unable to manage such risks, our business may be adversely\\nimpacted.\\nWe face climate change related physical and transition risks, which include the risk of market shifts toward electric vehicles (“EVs”) and lower carbon\\nbusiness models and risks related to extreme weather events or natural disasters. Climate-related events, including the increasing frequency, severity and duration\\nof extreme weather events and their impact on critical infrastructure in the United States and elsewhere, have the potential to disrupt our business, our third-party\\nsuppliers, and the business of merchants, Shippers, Carriers and Drivers using our platform, and may cause us to experience higher losses and additional costs to\\nmaintain or resume operations. Additionally, we are subject to emerging climate policies such as a regulation adopted in California in May 2021 requiring 90% of\\nvehicle miles traveled by rideshare fleets in California to have been in zero emission vehicles by 2030, with interim targets beginning in 2023. In addition, Drivers\\nmay be subject to climate-related policies that indirectly impact our business, such as the Congestion Charge Zone and Ultra Low Emission Zone schemes adopted\\nin London that impose fees on drivers in fossil-fueled vehicles, which may impact our ability to attract and maintain Drivers on our platform, and to the extent we\\nexperience Driver supply constraints in a given market, we may need to increase Driver incentives.\\nWe have made climate related commitments that require us to invest significant effort, resources, and management time and circumstances may arise,\\nincluding those beyond our control, that may require us to revise the contemplated timeframes for implementing these commitments.\\nWe have made climate related commitments, including our commitment to 100% renewable electricity for our U.S. offices by 2025, our commitment to net\\nzero climate emissions from corporate operations by 2030, and our commitment to be a net zero company by 2040. In addition, our Supplier Code of Conduct sets\\nenvironmental standards for our supply chain, and we recognize that there are inherent climate-related risks wherever business is conducted. Progressing towards\\nour climate commitments requires us to invest significant effort, resources, and management time, and circumstances may arise, including those beyond our\\ncontrol, that may require us to revise our timelines and/or climate commitments. For example, the COVID-19 pandemic has negatively impacted our ability to\\ndedicate resources to make the progress on our climate commitments that we initially anticipated. In addition, our ability to meet our climate commitments is\\ndependent on external factors such as rapidly changing regulations, policies and related interpretation, advances in technology such as battery storage, as well the\\navailability, cost and accessibility of EVs to Drivers, and the availability of EV charging infrastructure that can be efficiently accessed by Drivers. Any failure to\\nmeet regulatory requirements related to climate change, or to meet our stated climate change commitments on the timeframe we committed to, or at all, could have\\nan adverse impact on our costs and ability to operate, as well as harm our brand, reputation, and consequently, our business.\\nGeneral Economic Risks\\nOutbreaks of contagious disease, such as the COVID-19 pandemic and the impact of actions to mitigate the such disease or pandemic, have adversely impacted\\nand could continue to adversely impact our business, financial condition and results of operations.\\nOccurrence of a catastrophic event, including but not limited to disease, a weather event, war, or terrorist attack, could adversely impact our business, financial\\ncondition and results of operation.', start\_char\_idx=0, end\_char\_idx=5248, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.7967699969539317), NodeWithScore(node=TextNode(id\_='474572f4-866f-4efa-aa5f-f898d4ba831a', embedding=None, metadata={'page\_label': '13', 'file\_name': 'uber\_10q\_sept\_2022.pdf', 'file\_path': 'data/10q/uber\_10q\_sept\_2022.pdf', 'file\_type': 'application/pdf', 'file\_size': 1178622, 'creation\_date': '2024-05-23', 'last\_modified\_date': '2024-05-23'}, excluded\_embed\_metadata\_keys=\['file\_name', 'file\_type', 'file\_size', 'creation\_date', 'last\_modified\_date', 'last\_accessed\_date'\], excluded\_llm\_metadata\_keys=\['file\_name', 'file\_type', 'file\_size', 'creation\_date', 'last\_modified\_date', 'last\_accessed\_date'\], relationships={<NodeRelationship.SOURCE: '1'>: RelatedNodeInfo(node\_id='2ecd357c-acd3-4398-a0ae-223bf9980f34', node\_type=<ObjectType.DOCUMENT: '4'>, metadata={'page\_label': '13', 'file\_name': 'uber\_10q\_sept\_2022.pdf', 'file\_path': 'data/10q/uber\_10q\_sept\_2022.pdf', 'file\_type': 'application/pdf', 'file\_size': 1178622, 'creation\_date': '2024-05-23', 'last\_modified\_date': '2024-05-23'}, hash='8da53f7e83f88f63304dfcf8186b0ce111a5e161a317d243451266b863e9f2af'), <NodeRelationship.PREVIOUS: '2'>: RelatedNodeInfo(node\_id='e2e88da4-92e0-4185-96c6-010a35d94287', node\_type=<ObjectType.TEXT: '1'>, metadata={'page\_label': '13', 'file\_name': 'uber\_10q\_sept\_2022.pdf', 'file\_path': 'data/10q/uber\_10q\_sept\_2022.pdf', 'file\_type': 'application/pdf', 'file\_size': 1178622, 'creation\_date': '2024-05-23', 'last\_modified\_date': '2024-05-23'}, hash='373d1a92181565c8fb2ae2831069e904f4f4d2a9fdc70486b91f102cdac9d442')}, text='Estimates are based on historical experience, where\\napplicable, and other assumptions which management believes are reasonable under the circumstances. Additionally, we considered the impacts of the coronavirus\\npandemic (“COVID-19”) on the assumptions and inputs (including market data) supporting certain of these estimates, assumptions and judgments. On an ongoing\\nbasis, management evaluates estimates, including, but not limited to: fair values of investments and other financial instruments (including the measurement of\\ncredit or impairment losses); useful lives of amortizable long-lived assets; fair value of acquired intangible assets and related impairment assessments; impairment\\nof goodwill; stock-based compensation; income taxes and non-income tax reserves; certain deferred tax assets and tax liabilities; insurance reserves; and other\\ncontingent liabilities. These estimates are inherently subject to judgment and actual results could differ from those estimates.\\nCertain Significant Risks and Uncertainties - COVID-19\\nCOVID-19 restrictions have had an adverse impact on our business and operations by reducing, in particular, the global demand for Mobility offerings. It is\\nnot possible to predict COVID-19’s cumulative and ultimate impact on our future business operations, results of operations, financial position, liquidity, and cash\\nflows. The extent of the impact of COVID-19 on our business and financial results will depend largely on future developments, including: outbreaks or variants of\\nthe virus, both globally and within the United\\n12', start\_char\_idx=4007, end\_char\_idx=5573, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.7911034852964277)\], metadata=None)

Back to top

[Previous Context-Augmented OpenAI Agent](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_context_retrieval/)[Next Single-Turn Multi-Function Calling OpenAI Agents](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_parallel_function_calling/)

Hi, how can I help you?

🦙
