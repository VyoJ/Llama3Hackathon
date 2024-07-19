Title: Structured Planning Agent - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/structured_planner/

Markdown Content:
Structured Planning Agent - LlamaIndex


A key pattern in agents is the ability to plan. ReAct for example, uses a structured approach to decompose an input into a set of function calls and thoughts, in order to reason about a final response.

However, breaking down the initial input/task into several sub-tasks can make the ReAct loop (or other reasoning loops) easier to execute.

The `StructuredPlanningAgnet` in LlamaIndex wraps any agent worker (ReAct, Function Calling, Chain-of-Abstraction, etc.) and decomposes an initial input into several sub-tasks. Each sub-task is represented by an input, expected outcome, and any dependendant sub-tasks that should be completed first.

This notebook walks through both the high-level and low-level usage of this agent.

**NOTE:** This agent leverages both structured outputs and agentic reasoning. Because of this, we would recommend a capable LLM (OpenAI, Anthropic, etc.), and open-source LLMs may struggle to plan without prompt engineering or fine-tuning.

Setup[¶](https://docs.llamaindex.ai/en/stable/examples/agent/structured_planner/#setup)
---------------------------------------------------------------------------------------

In order to create plans, we need a set of tools to create plans on top of. Here, we use some classic 10k examples.

In \[ \]:

Copied!

!mkdir \-p 'data/10k/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' \-O 'data/10k/uber\_2021.pdf'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/lyft\_2021.pdf' \-O 'data/10k/lyft\_2021.pdf'

!mkdir -p 'data/10k/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/uber\_2021.pdf' -O 'data/10k/uber\_2021.pdf' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/10k/lyft\_2021.pdf' -O 'data/10k/lyft\_2021.pdf'

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= "sk-..."

import os os.environ\["OPENAI\_API\_KEY"\] = "sk-..."

In \[ \]:

Copied!

from llama\_index.core import Settings
from llama\_index.llms.openai import OpenAI
from llama\_index.embeddings.openai import OpenAIEmbedding

\# Use ollama in JSON mode
Settings.llm \= OpenAI(
    model\="gpt-4-turbo",
    temperature\=0.1,
)
Settings.embed\_model \= OpenAIEmbedding(model\_name\="text-embedding-3-small")

from llama\_index.core import Settings from llama\_index.llms.openai import OpenAI from llama\_index.embeddings.openai import OpenAIEmbedding # Use ollama in JSON mode Settings.llm = OpenAI( model="gpt-4-turbo", temperature=0.1, ) Settings.embed\_model = OpenAIEmbedding(model\_name="text-embedding-3-small")

In \[ \]:

Copied!

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama\_index.core.tools import QueryEngineTool

\# Load documents, create tools
lyft\_documents \= SimpleDirectoryReader(
    input\_files\=\["./data/10k/lyft\_2021.pdf"\]
).load\_data()
uber\_documents \= SimpleDirectoryReader(
    input\_files\=\["./data/10k/uber\_2021.pdf"\]
).load\_data()

lyft\_index \= VectorStoreIndex.from\_documents(lyft\_documents)
uber\_index \= VectorStoreIndex.from\_documents(uber\_documents)

lyft\_tool \= QueryEngineTool.from\_defaults(
    lyft\_index.as\_query\_engine(),
    name\="lyft\_2021",
    description\="Useful for asking questions about Lyft's 2021 10-K filling.",
)

uber\_tool \= QueryEngineTool.from\_defaults(
    uber\_index.as\_query\_engine(),
    name\="uber\_2021",
    description\="Useful for asking questions about Uber's 2021 10-K filling.",
)

from llama\_index.core import VectorStoreIndex, SimpleDirectoryReader from llama\_index.core.tools import QueryEngineTool # Load documents, create tools lyft\_documents = SimpleDirectoryReader( input\_files=\["./data/10k/lyft\_2021.pdf"\] ).load\_data() uber\_documents = SimpleDirectoryReader( input\_files=\["./data/10k/uber\_2021.pdf"\] ).load\_data() lyft\_index = VectorStoreIndex.from\_documents(lyft\_documents) uber\_index = VectorStoreIndex.from\_documents(uber\_documents) lyft\_tool = QueryEngineTool.from\_defaults( lyft\_index.as\_query\_engine(), name="lyft\_2021", description="Useful for asking questions about Lyft's 2021 10-K filling.", ) uber\_tool = QueryEngineTool.from\_defaults( uber\_index.as\_query\_engine(), name="uber\_2021", description="Useful for asking questions about Uber's 2021 10-K filling.", )

High Level API[¶](https://docs.llamaindex.ai/en/stable/examples/agent/structured_planner/#high-level-api)
---------------------------------------------------------------------------------------------------------

In this section, we cover the high-level API for creating with and chatting with a structured planning agent.

### Create the Agent[¶](https://docs.llamaindex.ai/en/stable/examples/agent/structured_planner/#create-the-agent)

In \[ \]:

Copied!

from llama\_index.core.agent import (
    StructuredPlannerAgent,
    FunctionCallingAgentWorker,
    ReActAgentWorker,
)

\# create the function calling worker for reasoning
worker \= FunctionCallingAgentWorker.from\_tools(
    \[lyft\_tool, uber\_tool\], verbose\=True
)

\# wrap the worker in the top-level planner
agent \= StructuredPlannerAgent(
    worker, tools\=\[lyft\_tool, uber\_tool\], verbose\=True
)

from llama\_index.core.agent import ( StructuredPlannerAgent, FunctionCallingAgentWorker, ReActAgentWorker, ) # create the function calling worker for reasoning worker = FunctionCallingAgentWorker.from\_tools( \[lyft\_tool, uber\_tool\], verbose=True ) # wrap the worker in the top-level planner agent = StructuredPlannerAgent( worker, tools=\[lyft\_tool, uber\_tool\], verbose=True )

### Give the agent a complex task[¶](https://docs.llamaindex.ai/en/stable/examples/agent/structured_planner/#give-the-agent-a-complex-task)

In \[ \]:

Copied!

import nest\_asyncio

nest\_asyncio.apply()

import nest\_asyncio nest\_asyncio.apply()

In \[ \]:

Copied!

response \= agent.chat(
    "Summarize the key risk factors for Lyft and Uber in their 2021 10-K filings."
)

response = agent.chat( "Summarize the key risk factors for Lyft and Uber in their 2021 10-K filings." )

\
Extract Lyft Risk Factors:
Summarize the key risk factors from Lyft's 2021 10-K filing. -> A summary of the key risk factors for Lyft as outlined in their 2021 10-K filing.
deps: \[\]


Extract Uber Risk Factors:
Summarize the key risk factors from Uber's 2021 10-K filing. -> A summary of the key risk factors for Uber as outlined in their 2021 10-K filing.
deps: \[\]


Combine Risk Factors Summaries:
Combine the summaries of key risk factors for Lyft and Uber from their 2021 10-K filings into a comprehensive overview. -> A comprehensive summary of the key risk factors for both Lyft and Uber as outlined in their respective 2021 10-K filings.
deps: \['Extract Lyft Risk Factors', 'Extract Uber Risk Factors'\]


> Running step a1428164-9f35-4a0e-9d6d-3328ebe490d4. Step input: Summarize the key risk factors from Lyft's 2021 10-K filing.
Added user message to memory: Summarize the key risk factors from Lyft's 2021 10-K filing.
> Running step 16a0d1f5-03ba-4b47-af0f-ec8758e6dda7. Step input: Summarize the key risk factors from Uber's 2021 10-K filing.
Added user message to memory: Summarize the key risk factors from Uber's 2021 10-K filing.

Calling function: lyft\_2021 with args: {"input": "key risk factors"}

Calling function: uber\_2021 with args: {"input": "What are the key risk factors mentioned in the 2021 10-K filing?"}

The key risk factors mentioned in the 2021 10-K filing include:

1. The potential adverse effects of the COVID-19 pandemic on the business.
2. The risk associated with the classification of drivers as employees or quasi-employees instead of independent contractors.
3. Intense competition in the mobility, delivery, and logistics industries, which feature low barriers to entry, low switching costs, and well-capitalized competitors.
4. The possibility of having to lower fares or service fees and offer significant driver incentives and consumer discounts to remain competitive.
5. Historical financial losses and the expectation of significant increases in operating expenses, which may prevent the company from achieving or maintaining profitability.
6. The necessity of attracting and maintaining a critical mass of drivers, consumers, merchants, shippers, and carriers to keep the platform appealing.
7. The importance of maintaining and enhancing the company's brand and reputation, especially following significant negative publicity in the past.
8. Challenges related to the company's historical workplace culture and the ongoing efforts to address these issues.
9. The need to optimize the organizational structure and effectively manage growth to ensure good financial performance and future prospects.
> Running step 85dc3f14-7c78-4759-88d6-1e9b071c1059. Step input: None

The key risk factors for investing in Lyft's Class A common stock include:

1. General economic factors such as the impact of the COVID-19 pandemic, natural disasters, economic downturns, public health crises, and political crises.
2. Operational factors including Lyft's limited operating history, the unpredictability of financial performance and results of operations, competition in the industry, and uncertainty regarding the growth of the ridesharing market.
3. The company's ability to attract and retain qualified drivers and riders, manage insurance coverage and reserves, and handle claims through third-party insurance providers.
4. Challenges related to autonomous vehicle technology and the development of the autonomous vehicle industry.
5. The company's reputation, brand, and company culture, as well as the potential for illegal or improper activity by users of the platform.
6. The accuracy of background checks on potential or current drivers, changes to pricing practices, and the growth and quality of Lyft's network of Light Vehicles.
7. Security or privacy breaches, system failures, and reliance on third parties such as Amazon Web Services, vehicle rental partners, and payment processors.
8. The ability to operate and manage Lyft's Express Drive and Lyft Rentals programs, delivery service platform, and the effectiveness of matching riders in Shared and Shared Saver Rides offerings.
9. The development of new offerings on the platform and managing the complexities associated with such expansion.
> Running step 8705c8fa-e764-460c-a849-a5f7851e454b. Step input: None

The key risk factors mentioned in Uber's 2021 10-K filing include:

1. \*\*COVID-19 Pandemic Impact:\*\* The ongoing adverse effects of the COVID-19 pandemic on the business.
2. \*\*Driver Classification:\*\* Risks associated with the classification of drivers as employees or quasi-employees instead of independent contractors.
3. \*\*Intense Competition:\*\* The competitive nature of the mobility, delivery, and logistics industries, which have low barriers to entry, low switching costs, and well-capitalized competitors.
4. \*\*Pricing and Incentives:\*\* The need to potentially lower fares or service fees and offer significant driver incentives and consumer discounts to remain competitive.
5. \*\*Financial Losses:\*\* Historical financial losses and expected significant increases in operating expenses, which may prevent the company from achieving or maintaining profitability.
6. \*\*Platform Appeal:\*\* The necessity of attracting and maintaining a critical mass of drivers, consumers, merchants, shippers, and carriers to keep the platform appealing.
7. \*\*Brand and Reputation:\*\* The importance of maintaining and enhancing the company's brand and reputation, particularly in light of significant negative publicity in the past.
8. \*\*Workplace Culture:\*\* Challenges related to the company's historical workplace culture and the ongoing efforts to address these issues.
9. \*\*Organizational Structure:\*\* The need to optimize the organizational structure and effectively manage growth to ensure good financial performance and future prospects.

The key risk factors from Lyft's 2021 10-K filing include:

1. \*\*Economic and Public Health Factors\*\*: Risks related to general economic conditions, the impact of the COVID-19 pandemic, natural disasters, economic downturns, public health crises, and political crises.
2. \*\*Operational Factors\*\*: Lyft's limited operating history, unpredictability of financial performance, competition in the industry, and uncertainty regarding the growth of the ridesharing market.
3. \*\*Driver and Rider Dynamics\*\*: Challenges in attracting and retaining qualified drivers and riders, managing insurance coverage and reserves, and handling claims through third-party insurance providers.
4. \*\*Autonomous Vehicle Technology\*\*: Challenges related to the development of autonomous vehicle technology and the autonomous vehicle industry.
5. \*\*Company Reputation and Culture\*\*: Risks associated with the company's reputation, brand, company culture, and potential illegal or improper activity by platform users.
6. \*\*Background Checks and Pricing Practices\*\*: The accuracy of background checks on potential or current drivers, changes to pricing practices, and the growth and quality of Lyft's network of Light Vehicles.
7. \*\*Security and Privacy\*\*: Security or privacy breaches, system failures, and reliance on third parties such as Amazon Web Services, vehicle rental partners, and payment processors.
8. \*\*Program Management\*\*: The ability to operate and manage Lyft's Express Drive and Lyft Rentals programs, delivery service platform, and the effectiveness of matching riders in Shared and Shared Saver Rides offerings.
9. \*\*Expansion and New Offerings\*\*: The development of new offerings on the platform and managing the complexities associated with such expansion.

Combine Risk Factors Summaries:
Combine the summaries of key risk factors for Lyft and Uber from their 2021 10-K filings into a comprehensive overview. -> A comprehensive summary of the key risk factors for both Lyft and Uber as outlined in their respective 2021 10-K filings.
deps: \['Extract Lyft Risk Factors', 'Extract Uber Risk Factors'\]


Summarize Key Risk Factors:
Summarize the combined risk factors from Lyft and Uber into a concise and comprehensive overview. -> A concise and comprehensive summary of the key risk factors for both Lyft and Uber as outlined in their respective 2021 10-K filings.
deps: \['Combine Risk Factors Summaries'\]


> Running step 874c8c34-3720-4d6f-bde1-7064e18a6433. Step input: Combine the summaries of key risk factors for Lyft and Uber from their 2021 10-K filings into a comprehensive overview.
Added user message to memory: Combine the summaries of key risk factors for Lyft and Uber from their 2021 10-K filings into a comprehensive overview.

The key risk factors from the 2021 10-K filings of Lyft and Uber provide a comprehensive overview of the challenges faced by both companies in the ridesharing and broader mobility industry:

1. \*\*COVID-19 and Economic Conditions\*\*: Both companies highlight the adverse effects of the COVID-19 pandemic and general economic conditions, including economic downturns and public health crises, which impact their operations and market demand.

2. \*\*Regulatory and Classification Issues\*\*: Uber specifically mentions the risk associated with the classification of drivers as employees or quasi-employees instead of independent contractors, which is a significant issue for the industry.

3. \*\*Competition and Market Conditions\*\*: Both companies face intense competition in the mobility, delivery, and logistics industries, characterized by low barriers to entry, low switching costs, and well-capitalized competitors. Lyft also notes the unpredictability of financial performance and the uncertainty regarding the growth of the ridesharing market.

4. \*\*Operational Challenges\*\*: Lyft discusses its limited operating history and the challenges of managing insurance and claims, while Uber emphasizes the need to attract and maintain a critical mass of drivers, consumers, merchants, shippers, and carriers.

5. \*\*Technological Advancements\*\*: Lyft addresses challenges related to autonomous vehicle technology and the development of the autonomous vehicle industry, which are crucial for future growth and competition.

6. \*\*Brand and Reputation\*\*: Both companies stress the importance of maintaining and enhancing their brand and reputation. Uber specifically mentions the need to address historical workplace culture issues, while Lyft highlights the potential for illegal or improper activity by users.

7. \*\*Financial Sustainability\*\*: Uber discusses its historical financial losses and the significant increases in operating expenses that may prevent profitability. Lyft also faces similar financial unpredictability.

8. \*\*Security and Privacy\*\*: Lyft mentions risks related to security or privacy breaches and system failures, emphasizing their reliance on third parties like Amazon Web Services and payment processors.

9. \*\*Service Management and Expansion\*\*: Lyft discusses the management of specific programs like Express Drive and Lyft Rentals, and the development of new offerings. Uber highlights the necessity of optimizing its organizational structure to manage growth effectively.

This combined overview underscores the shared and unique challenges faced by Lyft and Uber as they navigate regulatory landscapes, technological advancements, competitive pressures, and the need for operational efficiency and innovation in a rapidly evolving industry.

Summarize Key Risk Factors:
Summarize the combined risk factors from Lyft and Uber into a concise and comprehensive overview. -> A concise and comprehensive summary of the key risk factors for both Lyft and Uber as outlined in their respective 2021 10-K filings.
deps: \['Combine Risk Factors Summaries'\]


> Running step 8a452cd1-a940-47e8-82a1-277523d689eb. Step input: Summarize the combined risk factors from Lyft and Uber into a concise and comprehensive overview.
Added user message to memory: Summarize the combined risk factors from Lyft and Uber into a concise and comprehensive overview.

The combined key risk factors from the 2021 10-K filings of Lyft and Uber highlight several shared and distinct challenges in the ridesharing and mobility industry:

1. \*\*Pandemic and Economic Impact\*\*: Both companies are significantly affected by the COVID-19 pandemic and broader economic conditions, which influence market demand and operational stability.

2. \*\*Regulatory and Labor Issues\*\*: A major concern is the classification of drivers as independent contractors versus employees, impacting labor costs and operational flexibility.

3. \*\*Intense Competition\*\*: They face fierce competition in the mobility, delivery, and logistics sectors, characterized by low entry barriers and aggressive, well-funded competitors.

4. \*\*Operational and Financial Uncertainty\*\*: Both companies deal with financial unpredictability and operational challenges, including managing insurance, claims, and maintaining profitability amidst high expenses.

5. \*\*Technological and Service Evolution\*\*: Challenges in adopting new technologies like autonomous vehicles and expanding service offerings are crucial for staying competitive and managing growth.

6. \*\*Brand and Reputation Management\*\*: Maintaining a positive brand image and company culture is vital, especially given past issues and the potential for user misconduct.

7. \*\*Security and Privacy Concerns\*\*: Risks related to data breaches, system failures, and dependency on third-party services like cloud providers and payment processors are significant.

This overview encapsulates the multifaceted risks that Lyft and Uber face, emphasizing the need for strategic management and innovation to navigate a complex, rapidly changing industry landscape.

Summarize Key Risk Factors:
Summarize the key risk factors for Lyft and Uber in their 2021 10-K filings. -> The combined key risk factors from the 2021 10-K filings of Lyft and Uber highlight several shared and distinct challenges in the ridesharing and mobility industry:

1. \*\*Pandemic and Economic Impact\*\*: Both companies are significantly affected by the COVID-19 pandemic and broader economic conditions, which influence market demand and operational stability.

2. \*\*Regulatory and Labor Issues\*\*: A major concern is the classification of drivers as independent contractors versus employees, impacting labor costs and operational flexibility.

3. \*\*Intense Competition\*\*: They face fierce competition in the mobility, delivery, and logistics sectors, characterized by low entry barriers and aggressive, well-funded competitors.

4. \*\*Operational and Financial Uncertainty\*\*: Both companies deal with financial unpredictability and operational challenges, including managing insurance, claims, and maintaining profitability amidst high expenses.

5. \*\*Technological and Service Evolution\*\*: Challenges in adopting new technologies like autonomous vehicles and expanding service offerings are crucial for staying competitive and managing growth.

6. \*\*Brand and Reputation Management\*\*: Maintaining a positive brand image and company culture is vital, especially given past issues and the potential for user misconduct.

7. \*\*Security and Privacy Concerns\*\*: Risks related to data breaches, system failures, and dependency on third-party services like cloud providers and payment processors are significant.

This overview encapsulates the multifaceted risks that Lyft and Uber face, emphasizing the need for strategic management and innovation to navigate a complex, rapidly changing industry landscape.
deps: \[\]

In \[ \]:

Copied!

print(str(response))

print(str(response))

assistant: The combined key risk factors from the 2021 10-K filings of Lyft and Uber highlight several shared and distinct challenges in the ridesharing and mobility industry:

1. \*\*Pandemic and Economic Impact\*\*: Both companies are significantly affected by the COVID-19 pandemic and broader economic conditions, which influence market demand and operational stability.

2. \*\*Regulatory and Labor Issues\*\*: A major concern is the classification of drivers as independent contractors versus employees, impacting labor costs and operational flexibility.

3. \*\*Intense Competition\*\*: They face fierce competition in the mobility, delivery, and logistics sectors, characterized by low entry barriers and aggressive, well-funded competitors.

4. \*\*Operational and Financial Uncertainty\*\*: Both companies deal with financial unpredictability and operational challenges, including managing insurance, claims, and maintaining profitability amidst high expenses.

5. \*\*Technological and Service Evolution\*\*: Challenges in adopting new technologies like autonomous vehicles and expanding service offerings are crucial for staying competitive and managing growth.

6. \*\*Brand and Reputation Management\*\*: Maintaining a positive brand image and company culture is vital, especially given past issues and the potential for user misconduct.

7. \*\*Security and Privacy Concerns\*\*: Risks related to data breaches, system failures, and dependency on third-party services like cloud providers and payment processors are significant.

This overview encapsulates the multifaceted risks that Lyft and Uber face, emphasizing the need for strategic management and innovation to navigate a complex, rapidly changing industry landscape.

Changing Prompts[¶](https://docs.llamaindex.ai/en/stable/examples/agent/structured_planner/#changing-prompts)
-------------------------------------------------------------------------------------------------------------

The `StructuredPlanningAgent` has two key prompts:

1.  The initial planning prompt
2.  The plan refinement prompt

Below, we show how to configure these prompts, using the defaults as an example.

In \[ \]:

Copied!

DEFAULT\_INITIAL\_PLAN\_PROMPT \= """\\
Think step-by-step. Given a task and a set of tools, create a comprehesive, end-to-end plan to accomplish the task.
Keep in mind not every task needs to be decomposed into multiple sub-tasks if it is simple enough.
The plan should end with a sub-task that satisfies the overall task.

The tools available are:
{tools\_str}

Overall Task: {task}
"""

DEFAULT\_PLAN\_REFINE\_PROMPT \= """\\
Think step-by-step. Given an overall task, a set of tools, and completed sub-tasks, update (if needed) the remaining sub-tasks so that the overall task can still be completed.
The plan should end with a sub-task that satisfies the overall task.
If the remaining sub-tasks are sufficient, you can skip this step.

The tools available are:
{tools\_str}

Overall Task:
{task}

Completed Sub-Tasks + Outputs:
{completed\_outputs}

Remaining Sub-Tasks:
{remaining\_sub\_tasks}
"""

DEFAULT\_INITIAL\_PLAN\_PROMPT = """\\ Think step-by-step. Given a task and a set of tools, create a comprehesive, end-to-end plan to accomplish the task. Keep in mind not every task needs to be decomposed into multiple sub-tasks if it is simple enough. The plan should end with a sub-task that satisfies the overall task. The tools available are: {tools\_str} Overall Task: {task} """ DEFAULT\_PLAN\_REFINE\_PROMPT = """\\ Think step-by-step. Given an overall task, a set of tools, and completed sub-tasks, update (if needed) the remaining sub-tasks so that the overall task can still be completed. The plan should end with a sub-task that satisfies the overall task. If the remaining sub-tasks are sufficient, you can skip this step. The tools available are: {tools\_str} Overall Task: {task} Completed Sub-Tasks + Outputs: {completed\_outputs} Remaining Sub-Tasks: {remaining\_sub\_tasks} """

In \[ \]:

Copied!

agent \= StructuredPlannerAgent(
    worker,
    tools\=\[lyft\_tool, uber\_tool\],
    initial\_plan\_prompt\=DEFAULT\_INITIAL\_PLAN\_PROMPT,
    plan\_refine\_prompt\=DEFAULT\_PLAN\_REFINE\_PROMPT,
    verbose\=True,
)

agent = StructuredPlannerAgent( worker, tools=\[lyft\_tool, uber\_tool\], initial\_plan\_prompt=DEFAULT\_INITIAL\_PLAN\_PROMPT, plan\_refine\_prompt=DEFAULT\_PLAN\_REFINE\_PROMPT, verbose=True, )

Low-level API \[Advanced\][¶](https://docs.llamaindex.ai/en/stable/examples/agent/structured_planner/#low-level-api-advanced)
-----------------------------------------------------------------------------------------------------------------------------

In this section, we use the same agent, but expose the lower-level steps that are happening under the hood.

This is useful for when you want to expose the underlying plan, tasks, etc. to a human to modify them on the fly, or for debugging and running things step-by-step.

### Create the Agent[¶](https://docs.llamaindex.ai/en/stable/examples/agent/structured_planner/#create-the-agent)

In \[ \]:

Copied!

from llama\_index.core.agent import (
    StructuredPlannerAgent,
    FunctionCallingAgentWorker,
    ReActAgentWorker,
)

\# create the react worker for reasoning
worker \= FunctionCallingAgentWorker.from\_tools(
    \[lyft\_tool, uber\_tool\], verbose\=True
)

\# wrap the worker in the top-level planner
agent \= StructuredPlannerAgent(
    worker, tools\=\[lyft\_tool, uber\_tool\], verbose\=True
)

from llama\_index.core.agent import ( StructuredPlannerAgent, FunctionCallingAgentWorker, ReActAgentWorker, ) # create the react worker for reasoning worker = FunctionCallingAgentWorker.from\_tools( \[lyft\_tool, uber\_tool\], verbose=True ) # wrap the worker in the top-level planner agent = StructuredPlannerAgent( worker, tools=\[lyft\_tool, uber\_tool\], verbose=True )

### Create the initial tasks and plan[¶](https://docs.llamaindex.ai/en/stable/examples/agent/structured_planner/#create-the-initial-tasks-and-plan)

In \[ \]:

Copied!

plan\_id \= agent.create\_plan(
    "Summarize the key risk factors for Lyft and Uber in their 2021 10-K filings."
)

plan\_id = agent.create\_plan( "Summarize the key risk factors for Lyft and Uber in their 2021 10-K filings." )

\
Extract Lyft Risk Factors:
Extract the key risk factors from Lyft's 2021 10-K filing. -> A detailed list of key risk factors for Lyft from its 2021 10-K filing.
deps: \[\]


Extract Uber Risk Factors:
Extract the key risk factors from Uber's 2021 10-K filing. -> A detailed list of key risk factors for Uber from its 2021 10-K filing.
deps: \[\]


Summarize Risk Factors:
Summarize the key risk factors for both Lyft and Uber based on the extracted information from their 2021 10-K filings. -> A comprehensive summary of the key risk factors for Lyft and Uber from their 2021 10-K filings.
deps: \['Extract Lyft Risk Factors', 'Extract Uber Risk Factors'\]

### Inspect the initial tasks and plan[¶](https://docs.llamaindex.ai/en/stable/examples/agent/structured_planner/#inspect-the-initial-tasks-and-plan)

In \[ \]:

Copied!

plan \= agent.state.plan\_dict\[plan\_id\]

for sub\_task in plan.sub\_tasks:
    print(f"")
    print("Expected output: ", sub\_task.expected\_output)
    print("Dependencies: ", sub\_task.dependencies)

plan = agent.state.plan\_dict\[plan\_id\] for sub\_task in plan.sub\_tasks: print(f"") print("Expected output: ", sub\_task.expected\_output) print("Dependencies: ", sub\_task.dependencies)

\
Expected output:  A detailed list of key risk factors for Lyft from its 2021 10-K filing.
Dependencies:  \[\]

Expected output:  A detailed list of key risk factors for Uber from its 2021 10-K filing.
Dependencies:  \[\]

Expected output:  A comprehensive summary of the key risk factors for Lyft and Uber from their 2021 10-K filings.
Dependencies:  \['Extract Lyft Risk Factors', 'Extract Uber Risk Factors'\]

### Execute the first set of tasks[¶](https://docs.llamaindex.ai/en/stable/examples/agent/structured_planner/#execute-the-first-set-of-tasks)

Here, we execute the first set of tasks with their dependencies met.

In \[ \]:

Copied!

next\_tasks \= agent.state.get\_next\_sub\_tasks(plan\_id)

for sub\_task in next\_tasks:
    print(f"")
    print("Expected output: ", sub\_task.expected\_output)
    print("Dependencies: ", sub\_task.dependencies)

for sub\_task in next\_tasks:
    response \= agent.run\_task(sub\_task.name)
    agent.mark\_task\_complete(plan\_id, sub\_task.name)

next\_tasks = agent.state.get\_next\_sub\_tasks(plan\_id) for sub\_task in next\_tasks: print(f"") print("Expected output: ", sub\_task.expected\_output) print("Dependencies: ", sub\_task.dependencies) for sub\_task in next\_tasks: response = agent.run\_task(sub\_task.name) agent.mark\_task\_complete(plan\_id, sub\_task.name)

\
Expected output:  A detailed list of key risk factors for Lyft from its 2021 10-K filing.
Dependencies:  \[\]

Expected output:  A detailed list of key risk factors for Uber from its 2021 10-K filing.
Dependencies:  \[\]
> Running step 4f708bcd-3078-4138-897b-e7f643fc7f35. Step input: Extract the key risk factors from Lyft's 2021 10-K filing.
Added user message to memory: Extract the key risk factors from Lyft's 2021 10-K filing.

Calling function: lyft\_2021 with args: {"input": "key risk factors"}

Key risk factors for Lyft include general economic factors such as the impact of the COVID-19 pandemic, natural disasters, and macroeconomic conditions; operational factors such as limited operating history, competition, unpredictability of results, and the ability to attract and retain drivers and riders; and specific risks related to technology, such as autonomous vehicle development, security breaches, and reliance on third-party service providers. Additionally, risks related to insurance coverage, the adequacy of insurance reserves, and the handling of auto-related insurance claims by third parties are significant. The company also faces risks from potential illegal activities by users, inaccuracies in background checks, and challenges related to managing growth and expanding service offerings.
> Running step 060f219a-0668-47ec-9bef-ce131d0ba887. Step input: None

The key risk factors identified in Lyft's 2021 10-K filing include:

1. \*\*General Economic Factors:\*\*
   - Impact of the COVID-19 pandemic.
   - Natural disasters.
   - Macroeconomic conditions.

2. \*\*Operational Factors:\*\*
   - Limited operating history.
   - Competition.
   - Unpredictability of results.
   - Ability to attract and retain drivers and riders.

3. \*\*Technology-Related Risks:\*\*
   - Autonomous vehicle development.
   - Security breaches.
   - Reliance on third-party service providers.

4. \*\*Insurance-Related Risks:\*\*
   - Insurance coverage adequacy.
   - Insurance reserves adequacy.
   - Handling of auto-related insurance claims by third parties.

5. \*\*Other Risks:\*\*
   - Potential illegal activities by users.
   - Inaccuracies in background checks.
   - Challenges related to managing growth and expanding service offerings.
> Running step 00f6732b-594c-4ecf-82e5-e9f005f8ab71. Step input: Extract the key risk factors from Uber's 2021 10-K filing.
Added user message to memory: Extract the key risk factors from Uber's 2021 10-K filing.

Calling function: uber\_2021 with args: {"input": "key risk factors"}

The key risk factors include market risks such as interest rate risk, investment risk, and foreign currency risk. Interest rate risk is associated with fluctuations in interest rates affecting the company's refinanced term loan facilities and fixed rate notes. Investment risk involves the preservation of capital and meeting liquidity requirements without significantly increasing risk, with exposure to changes in interest rates and the carrying amounts of investments in other companies. Foreign currency risk arises from international transactions in multiple currencies, which could affect revenue and operating results due to fluctuations in exchange rates. Additionally, there are risks related to cyberattacks, which could harm the company's reputation, business, and operating results by compromising data security and the integrity of information technology systems.
> Running step 04e95d17-e7a7-4f35-8519-33e9439e9659. Step input: None

The key risk factors identified in Uber's 2021 10-K filing include:

1. \*\*Market Risks:\*\*
   - \*\*Interest Rate Risk:\*\* Fluctuations in interest rates affecting the company's refinanced term loan facilities and fixed rate notes.
   - \*\*Investment Risk:\*\* Challenges in preserving capital and meeting liquidity requirements without significantly increasing risk, with exposure to changes in interest rates and the carrying amounts of investments in other companies.
   - \*\*Foreign Currency Risk:\*\* Risks from international transactions in multiple currencies, which could affect revenue and operating results due to fluctuations in exchange rates.

2. \*\*Cybersecurity Risks:\*\*
   - Risks related to cyberattacks, which could harm the company's reputation, business, and operating results by compromising data security and the integrity of information technology systems.

If we wanted to, we could even execute each task in a step-wise fashion. It would look something like this:

\# Step-wise execution per task

for sub\_task in next\_tasks:
    \# get the task from the state 
    task \= agent.state.get\_task(sub\_task.name)

    \# run intial resoning step
    step\_output \= agent.run\_step(task.task\_id)

    \# loop until the last step is reached
    while not step\_output.is\_last:
        step\_output \= agent.run\_step(task.task\_id)
    
    \# finalize the response and commit to memory
    agent.finalize\_response(task.task\_id, step\_output\=step\_output)

### Check if we are done[¶](https://docs.llamaindex.ai/en/stable/examples/agent/structured_planner/#check-if-we-are-done)

If there are no remaining tasks, then we can stop. Otherwise, we can refine the current plan and continue

In \[ \]:

Copied!

next\_tasks \= agent.get\_next\_tasks(plan\_id)
print(len(next\_tasks))

next\_tasks = agent.get\_next\_tasks(plan\_id) print(len(next\_tasks))

1

In \[ \]:

Copied!

for sub\_task in next\_tasks:
    print(f"")

for sub\_task in next\_tasks: print(f"")

\

### Refine the plan[¶](https://docs.llamaindex.ai/en/stable/examples/agent/structured_planner/#refine-the-plan)

Since we have tasks remaining, lets refine our plan to make sure we are on track.

In \[ \]:

Copied!

\# refine the plan
agent.refine\_plan(
    "Summarize the key risk factors for Lyft and Uber in their 2021 10-K filings.",
    plan\_id,
)

\# refine the plan agent.refine\_plan( "Summarize the key risk factors for Lyft and Uber in their 2021 10-K filings.", plan\_id, )

\
Summarize Risk Factors:
Summarize the key risk factors for both Lyft and Uber based on the extracted information from their 2021 10-K filings. -> A comprehensive summary of the key risk factors for Lyft and Uber from their 2021 10-K filings.
deps: \['Extract Lyft Risk Factors', 'Extract Uber Risk Factors'\]

In \[ \]:

Copied!

plan \= agent.state.plan\_dict\[plan\_id\]

for sub\_task in plan.sub\_tasks:
    print(f"")
    print("Expected output: ", sub\_task.expected\_output)
    print("Dependencies: ", sub\_task.dependencies)

plan = agent.state.plan\_dict\[plan\_id\] for sub\_task in plan.sub\_tasks: print(f"") print("Expected output: ", sub\_task.expected\_output) print("Dependencies: ", sub\_task.dependencies)

\
Expected output:  A comprehensive summary of the key risk factors for Lyft and Uber from their 2021 10-K filings.
Dependencies:  \['Extract Lyft Risk Factors', 'Extract Uber Risk Factors'\]

### Loop until done[¶](https://docs.llamaindex.ai/en/stable/examples/agent/structured_planner/#loop-until-done)

With our plan refined, we can repeat this process until we have no more tasks to run.

In \[ \]:

Copied!

import asyncio

while True:
    \# are we done?
    next\_tasks \= agent.get\_next\_tasks(plan\_id)
    if len(next\_tasks) \ 0: break # run concurrently for better performance responses = await asyncio.gather( \*\[agent.arun\_task(task\_id) for task\_id in next\_tasks\] ) for task\_id in next\_tasks: agent.mark\_task\_complete(plan\_id, task\_id) # refine the plan await agent.arefine\_plan( "Summarize the key risk factors for Lyft and Uber in their 2021 10-K filings.", plan\_id, )

\> Running step 70356e9a-98ee-49f5-b15f-e5a6b43381d0. Step input: Summarize the key risk factors for both Lyft and Uber based on the extracted information from their 2021 10-K filings.
Added user message to memory: Summarize the key risk factors for both Lyft and Uber based on the extracted information from their 2021 10-K filings.

The key risk factors for Lyft and Uber from their 2021 10-K filings highlight several areas of concern for both companies, with some overlapping and unique challenges:

### Common Risk Factors:
- \*\*Economic and Market Conditions:\*\* Both companies are affected by general economic factors such as macroeconomic conditions and the impact of the COVID-19 pandemic. Additionally, Uber faces specific market risks like interest rate risk, investment risk, and foreign currency risk due to its global operations.

### Lyft-Specific Risk Factors:
- \*\*Operational Challenges:\*\* Lyft faces risks related to its limited operating history, competition, unpredictability of results, and the ability to attract and retain drivers and riders.
- \*\*Technology and Insurance Risks:\*\* Challenges include autonomous vehicle development, security breaches, reliance on third-party service providers, insurance coverage adequacy, and handling of auto-related insurance claims by third parties.
- \*\*Regulatory and Legal Risks:\*\* Potential illegal activities by users, inaccuracies in background checks, and challenges related to managing growth and expanding service offerings.

### Uber-Specific Risk Factors:
- \*\*Cybersecurity Risks:\*\* Uber is particularly concerned with risks related to cyberattacks that could compromise data security and the integrity of its information technology systems.

Both companies operate in dynamic and rapidly evolving environments, facing significant operational and market challenges that could impact their business operations and financial stability.

Extract Lyft Risk Factors:
Extract the key risk factors from Lyft's 2021 10-K filing. -> The key risk factors identified in Lyft's 2021 10-K filing include general economic factors, operational factors, technology-related risks, insurance-related risks, and other risks.
deps: \[\]


Extract Uber Risk Factors:
Extract the key risk factors from Uber's 2021 10-K filing. -> The key risk factors identified in Uber's 2021 10-K filing include market risks, cybersecurity risks, and other specific operational and financial risks.
deps: \[\]


Summarize Risk Factors:
Summarize the key risk factors for Lyft and Uber from their 2021 10-K filings. -> A summary of the key risk factors for Lyft and Uber, highlighting common and unique challenges, including economic, operational, technology, insurance, and cybersecurity risks.
deps: \['Extract Lyft Risk Factors', 'Extract Uber Risk Factors'\]

By the end, we should have a single response, which is our final response

In \[ \]:

Copied!

print(str(responses\[\-1\]))

print(str(responses\[-1\]))

assistant: The key risk factors for Lyft and Uber from their 2021 10-K filings highlight several areas of concern for both companies, with some overlapping and unique challenges:

### Common Risk Factors:
- \*\*Economic and Market Conditions:\*\* Both companies are affected by general economic factors such as macroeconomic conditions and the impact of the COVID-19 pandemic. Additionally, Uber faces specific market risks like interest rate risk, investment risk, and foreign currency risk due to its global operations.

### Lyft-Specific Risk Factors:
- \*\*Operational Challenges:\*\* Lyft faces risks related to its limited operating history, competition, unpredictability of results, and the ability to attract and retain drivers and riders.
- \*\*Technology and Insurance Risks:\*\* Challenges include autonomous vehicle development, security breaches, reliance on third-party service providers, insurance coverage adequacy, and handling of auto-related insurance claims by third parties.
- \*\*Regulatory and Legal Risks:\*\* Potential illegal activities by users, inaccuracies in background checks, and challenges related to managing growth and expanding service offerings.

### Uber-Specific Risk Factors:
- \*\*Cybersecurity Risks:\*\* Uber is particularly concerned with risks related to cyberattacks that could compromise data security and the integrity of its information technology systems.

Both companies operate in dynamic and rapidly evolving environments, facing significant operational and market challenges that could impact their business operations and financial stability.

Back to top

[Previous Controlling Agent Reasoning Loop with Return Direct Tools](https://docs.llamaindex.ai/en/stable/examples/agent/return_direct_agent/)[Next Aim Callback](https://docs.llamaindex.ai/en/stable/examples/callbacks/AimCallback/)

Hi, how can I help you?

🦙
