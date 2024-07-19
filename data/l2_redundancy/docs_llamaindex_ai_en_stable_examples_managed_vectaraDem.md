Title: Vectara Managed Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/managed/vectaraDemo/

Markdown Content:
Vectara Managed Index - LlamaIndex


In this notebook we are going to show how to use [Vectara](https://vectara.com/) with LlamaIndex.

Vectara provides an end-to-end managed service for Retrieval Augmented Generation or RAG, which includes:

1.  A way to extract text from document files and chunk them into sentences.
2.  The state-of-the-art [Boomerang](https://vectara.com/how-boomerang-takes-retrieval-augmented-generation-to-the-next-level-via-grounded-generation/) embeddings model. Each text chunk is encoded into a vector embedding using Boomerang, and stored in the Vectara internal vector store. Thus, when using Vectara with LlamaIndex you do not need to call a separate embedding model - this happens automatically within the Vectara backend.
3.  A query service that automatically encodes the query into embedding, and retrieves the most relevant text segments (including support for [Hybrid Search](https://docs.vectara.com/docs/api-reference/search-apis/lexical-matching) and [MMR](https://vectara.com/get-diverse-results-and-comprehensive-summaries-with-vectaras-mmr-reranker/))
4.  An option to a create [generative summary](https://docs.vectara.com/docs/learn/grounded-generation/grounded-generation-overview), based on the retrieved documents, including citations.

See the [Vectara API documentation](https://docs.vectara.com/docs/) for more information on how to use the API.

Getting Started[¶](https://docs.llamaindex.ai/en/stable/examples/managed/vectaraDemo/#getting-started)
------------------------------------------------------------------------------------------------------

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

!pip install llama\-index lama\-index\-indices\-managed\-vectara

!pip install llama-index lama-index-indices-managed-vectara

To get started with Vectara, [sign up](https://vectara.com/integrations/llamaindex) (if you haven't already) and follow our [quickstart guide](https://docs.vectara.com/docs/quickstart) to create a corpus and an API key.

Once you have these, you can provide them as environment variables, which will be used by the LlamaIndex code later on.

```
import os
os.environ['VECTARA_API_KEY'] = "<YOUR_VECTARA_API_KEY>"
os.environ['VECTARA_CORPUS_ID'] = "<YOUR_VECTARA_CORPUS_ID>"
os.environ['VECTARA_CUSTOMER_ID'] = "<YOUR_VECTARA_CUSTOMER_ID>"
```

RAG with LlamaIndex and Vectara[¶](https://docs.llamaindex.ai/en/stable/examples/managed/vectaraDemo/#rag-with-llamaindex-and-vectara)
--------------------------------------------------------------------------------------------------------------------------------------

There are a few ways you can index your data into Vectara, including:

1.  With the `from_documents()` or `insert_file()` methods of `VectaraIndex`
2.  Uploading files directly in the [Vectara console](https://console.vectara.com/)
3.  Using Vectara's FILE\_UPLOAD or standard indexing APIs
4.  Using [vectara-ingest](https://github.com/vectara/vectara-ingest), an open source crawler/indexer project
5.  Using one of our ingest integration partners like Airbyte, Unstructured or DataVolo.

For this purpose, we will use a simple set of small documents, so using `VectaraIndex` directly for the ingest is good enough.

Let's ingest the "AI bill of rights" document into our new corpus.

In \[ \]:

Copied!

from llama\_index.indices.managed.vectara import VectaraIndex
import requests

url \= "https://www.whitehouse.gov/wp-content/uploads/2022/10/Blueprint-for-an-AI-Bill-of-Rights.pdf"
response \= requests.get(url)
local\_path \= "ai-bill-of-rights.pdf"
with open(local\_path, "wb") as file:
    file.write(response.content)

index \= VectaraIndex()
index.insert\_file(
    local\_path, metadata\={"name": "AI bill of rights", "year": 2022}
)

from llama\_index.indices.managed.vectara import VectaraIndex import requests url = "https://www.whitehouse.gov/wp-content/uploads/2022/10/Blueprint-for-an-AI-Bill-of-Rights.pdf" response = requests.get(url) local\_path = "ai-bill-of-rights.pdf" with open(local\_path, "wb") as file: file.write(response.content) index = VectaraIndex() index.insert\_file( local\_path, metadata={"name": "AI bill of rights", "year": 2022} )

### Running single queries with Vectara Query Engine[¶](https://docs.llamaindex.ai/en/stable/examples/managed/vectaraDemo/#running-single-queries-with-vectara-query-engine)

Now that we've uploaded the document (or if documents have been uploaded previously) we can go and ask questions directly in LlamaIndex. This activates Vectara's RAG pipeline.

To use Vectara's internal LLM for summarization, make sure you specify `summary_enabled=True` when you generate the Query engine. Here's an example:

In \[ \]:

Copied!

questions \= \[
    "What are the risks of AI?",
    "What should we do to prevent bad actors from using AI?",
    "What are the benefits?",
\]

questions = \[ "What are the risks of AI?", "What should we do to prevent bad actors from using AI?", "What are the benefits?", \]

In \[ \]:

Copied!

qe \= index.as\_query\_engine(summary\_enabled\=True)
qe.query(questions\[0\]).response

qe = index.as\_query\_engine(summary\_enabled=True) qe.query(questions\[0\]).response

Out\[ \]:

"The risks associated with AI include potential biases leading to discriminatory outcomes, lack of transparency in decision-making processes, and challenges in establishing public trust and understanding of algorithmic systems \[1\]. Safety and efficacy concerns arise in the context of complex technologies like AI, necessitating strong regulations and proactive risk mitigation strategies \[2\]. The process of identifying and addressing risks before and during the deployment of automated systems is crucial to prevent harm to individuals' rights, opportunities, and access \[5\]. Furthermore, the impact of AI risks can be most visible at the community level, emphasizing the importance of considering and mitigating harms to various communities \[6\]. Efforts are being made to translate principles into practice through laws, policies, and technical approaches to ensure AI systems are lawful, respectful, accurate, safe, understandable, responsible, and accountable \[7\]."

If you want the response to be returned in streaming mode, simply set `streaming=True`

In \[ \]:

Copied!

qe \= index.as\_query\_engine(summary\_enabled\=True, streaming\=True)
response \= qe.query(questions\[0\])

for chunk in response.response\_gen:
    print(chunk.delta or "", end\="", flush\=True)

qe = index.as\_query\_engine(summary\_enabled=True, streaming=True) response = qe.query(questions\[0\]) for chunk in response.response\_gen: print(chunk.delta or "", end="", flush=True)

The risks of AI include biased data leading to discriminatory outcomes, opaque decision-making processes, and lack of public trust and understanding in algorithmic systems \[1\]. Organizations are implementing innovative solutions like risk assessments, auditing mechanisms, and ongoing monitoring to mitigate safety and efficacy risks of AI systems \[2\]. Stakeholder engagement and a risk management framework by institutions like NIST aim to address risks to individuals, organizations, and society posed by AI technology \[3\]. Risk identification, mitigation, and focusing on safety and effectiveness of AI systems are crucial before and during deployment to protect people’s rights, opportunities, and access \[5\]. The concept of communities is integral in understanding the impact of AI and automated systems, as the potential harm may be most visible at the community level \[6\]. Practical implementation of principles such as lawful, purposeful, accurate, safe, and accountable AI is essential to address risks, with federal agencies adhering to guidelines promoting trustworthy AI \[7\].

### Using Vectara Chat[¶](https://docs.llamaindex.ai/en/stable/examples/managed/vectaraDemo/#using-vectara-chat)

Vectara also supports a simple chat mode. In this mode the chat history is maintained by Vectara and so you don't have to worry about it. To use it simple call `as_chat_engine`.

(Chat mode always uses Vectara's summarization so you don't have to explicitly specify `summary_enabled=True` like before)

In \[ \]:

Copied!

ce \= index.as\_chat\_engine()

ce = index.as\_chat\_engine()

In \[ \]:

Copied!

for q in questions:
    print(f"Question: {q}\\n")
    response \= ce.chat(q).response
    print(f"Response: {response}\\n")

for q in questions: print(f"Question: {q}\\n") response = ce.chat(q).response print(f"Response: {response}\\n")

Question: What are the risks of AI?

Response: The risks of AI involve potential biases, opaque decision-making processes, and lack of public trust due to discriminatory outcomes and biased data \[1\]. To mitigate these risks, industry is implementing innovative solutions like risk assessments and monitoring mechanisms \[2\]. Stakeholder engagement and the development of a risk management framework by organizations like the National Institute of Standards and Technology aim to manage risks posed by AI to individuals, organizations, and society \[3\]. Identification and mitigation of potential risks, impact assessments, and balancing high impact risks with appropriate mitigation are crucial before and during the deployment of AI systems \[5\]. The Blueprint for an AI Bill of Rights emphasizes the protection of individuals from unsafe or ineffective AI systems \[7\].

Question: What should we do to prevent bad actors from using AI?

Response: To prevent the misuse of AI by malicious entities, several key measures can be implemented. Firstly, it is crucial to ensure that automated systems are designed with safety and effectiveness in mind, following principles such as being lawful, purposeful, accurate, secure, and transparent \[2\]. Entities should proactively identify and manage risks associated with sensitive data, conducting regular audits and limiting access to prevent misuse \[3\], \[4\], \[5\]. Additionally, ongoing monitoring of automated systems is essential to detect and address algorithmic discrimination and unforeseen interactions that could lead to misuse \[6\], \[7\]. By incorporating these practices into the design, development, and deployment of AI technologies, the potential for misuse by malicious entities can be significantly reduced.

Question: What are the benefits?

Response: Artificial Intelligence (AI) offers various advantages, such as promoting the use of trustworthy AI systems with principles focusing on legality, performance, safety, transparency, and accountability \[1\]. Organizations are incorporating protections and ethical principles in AI development, aligning with global recommendations for responsible AI stewardship \[2\]. Furthermore, research is ongoing to enhance explainable AI systems for better human understanding and trust in AI outcomes \[5\]. The U.S. government is establishing councils and frameworks to advance AI technologies, ensuring responsible AI implementation across sectors \[4\], . AI can streamline processes, improve decision-making, and enhance efficiency, although challenges like bias, flaws, and accessibility issues need to be addressed to maximize its benefits \[5\].

Of course streaming works as well with Chat:

In \[ \]:

Copied!

ce \= index.as\_chat\_engine(streaming\=True)

ce = index.as\_chat\_engine(streaming=True)

In \[ \]:

Copied!

response \= ce.stream\_chat("Will robots kill us all?")
for chunk in response.chat\_stream:
    print(chunk.delta or "", end\="", flush\=True)

response = ce.stream\_chat("Will robots kill us all?") for chunk in response.chat\_stream: print(chunk.delta or "", end="", flush=True)

The search results indicate a focus on the relationship between humans and robots, emphasizing the need for co-intelligence and the best use of automated systems \[2\]. The discussions revolve around ensuring that automated systems are designed, tested, and protected to prevent potential harmful outcomes \[1\]. While there are concerns about the use of surveillance technology by companies like Amazon and Walmart, the emphasis is on balancing equities and maintaining oversight in law enforcement activities \[5\]. The search results do not directly answer whether robots will kill us all, but they highlight the importance of proactive protections, context-specific guidance, and existing policies to govern the use of automated systems in various settings \[6\].

### Agentic RAG[¶](https://docs.llamaindex.ai/en/stable/examples/managed/vectaraDemo/#agentic-rag)

Let's create a ReAct Agent using LlamaIndex that utilizes Vectara as its RAG tool. For this you would need to use another LLM as the driver of the agent resoning, and we are using OpenAI's GPT4o here as an example. (for this to work, please make sure you have `OPENAI_API_KEY` defined in your environment).

In \[ \]:

Copied!

from llama\_index.core.agent import ReActAgent
from llama\_index.llms.openai import OpenAI
from llama\_index.core.tools import QueryEngineTool, ToolMetadata

llm \= OpenAI(model\="gpt-4o", temperature\=0)
vectara\_tool \= QueryEngineTool(
    query\_engine\=index.as\_query\_engine(
        summary\_enabled\=True,
        summary\_num\_results\=5,
        summary\_response\_lang\="en",
        summary\_prompt\_name\="vectara-summary-ext-24-05-large",
        reranker\="mmr",
        rerank\_k\=50,
        mmr\_diversity\_bias\=0.2,
    ),
    metadata\=ToolMetadata(
        name\="Vectara",
        description\="Vectara Query Engine that is able to answer Questions about AI regulation.",
    ),
)
agent \= ReActAgent.from\_tools(
    tools\=\[vectara\_tool\],
    llm\=llm,
    context\="""
        You are a helpful chatbot that answers any user questions around AI regulations using the Vectara tool.
        You break down complex questions into simpler ones.
        You use the Vectara query engine to help provide answers to simpler questions.
    """,
    verbose\=True,
)

from llama\_index.core.agent import ReActAgent from llama\_index.llms.openai import OpenAI from llama\_index.core.tools import QueryEngineTool, ToolMetadata llm = OpenAI(model="gpt-4o", temperature=0) vectara\_tool = QueryEngineTool( query\_engine=index.as\_query\_engine( summary\_enabled=True, summary\_num\_results=5, summary\_response\_lang="en", summary\_prompt\_name="vectara-summary-ext-24-05-large", reranker="mmr", rerank\_k=50, mmr\_diversity\_bias=0.2, ), metadata=ToolMetadata( name="Vectara", description="Vectara Query Engine that is able to answer Questions about AI regulation.", ), ) agent = ReActAgent.from\_tools( tools=\[vectara\_tool\], llm=llm, context=""" You are a helpful chatbot that answers any user questions around AI regulations using the Vectara tool. You break down complex questions into simpler ones. You use the Vectara query engine to help provide answers to simpler questions. """, verbose=True, )

In \[ \]:

Copied!

question \= """
    What are the risks of AI? What are the benefits?
    Compare and contrast and provide a summary with arguments for and against from experts.
"""

print(agent.chat(question).response)

question = """ What are the risks of AI? What are the benefits? Compare and contrast and provide a summary with arguments for and against from experts. """ print(agent.chat(question).response)

Thought: The current language of the user is: English. I need to use a tool to help me answer the question.
Action: Vectara
Action Input: {'input': 'What are the risks of AI?'}
Observation: The risks of AI include biased data leading to discriminatory outcomes, opaque decision-making processes, and a lack of public trust and understanding in algorithmic systems. Mitigation strategies discussed involve ongoing transparency, participatory design, and engaging with impacted communities to understand potential harms and integrate protections into the design of AI systems \[1\]. Additionally, there's a focus on identifying and mitigating risks before deployment, particularly those impacting people's rights, opportunities, or safety, with a strong emphasis on avoiding systems that inherently violate safety norms \[5\].
Thought: I have obtained information about the risks of AI. Now, I need to gather information about the benefits of AI to provide a comprehensive comparison.
Action: Vectara
Action Input: {'input': 'What are the benefits of AI?'}
Observation: The benefits of AI include its transformative potential to improve people's lives by building better and more innovative infrastructure. It also offers the possibility to enhance community health, safety, and welfare by ensuring better representation of all voices, particularly those traditionally marginalized by technological advances \[1\]. AI can also prevent harms and improve opportunities, rights, and access for Americans, playing a central role in shaping important policies like the Blueprint for an AI Bill of Rights \[2\].
Thought: I have gathered information about both the risks and benefits of AI. Now, I need to compare and contrast these points and provide a summary with arguments for and against from experts.
Answer: ### Comparison of Risks and Benefits of AI

#### Risks of AI:
1. \*\*Biased Data and Discriminatory Outcomes\*\*: AI systems can perpetuate and even exacerbate biases present in the data they are trained on, leading to unfair and discriminatory outcomes.
2. \*\*Opaque Decision-Making\*\*: The decision-making processes of AI systems can be complex and not easily understandable, leading to a lack of transparency.
3. \*\*Lack of Public Trust\*\*: The opacity and potential biases in AI systems can result in a lack of trust and understanding from the public.
4. \*\*Safety and Rights Violations\*\*: There is a risk of AI systems violating safety norms and impacting people's rights, opportunities, or safety.

#### Benefits of AI:
1. \*\*Improved Infrastructure\*\*: AI has the potential to transform and improve infrastructure, making it more innovative and efficient.
2. \*\*Enhanced Community Health and Safety\*\*: AI can play a significant role in improving community health, safety, and welfare by ensuring better representation and inclusivity.
3. \*\*Prevention of Harms\*\*: AI can help prevent harms and improve opportunities, rights, and access, particularly for marginalized communities.
4. \*\*Policy Shaping\*\*: AI is central to shaping important policies, such as the Blueprint for an AI Bill of Rights, which aims to protect and enhance the rights of individuals.

### Summary with Arguments For and Against AI

#### Arguments For AI:
- \*\*Innovation and Efficiency\*\*: AI can drive significant advancements in technology and infrastructure, leading to more efficient and innovative solutions.
- \*\*Inclusivity and Representation\*\*: AI can ensure better representation of marginalized voices, leading to more equitable outcomes.
- \*\*Health and Safety\*\*: AI can enhance community health and safety by providing better tools and systems for monitoring and intervention.
- \*\*Policy and Rights\*\*: AI can play a crucial role in shaping policies that protect and enhance individual rights and opportunities.

#### Arguments Against AI:
- \*\*Bias and Discrimination\*\*: The risk of biased data leading to discriminatory outcomes is a significant concern.
- \*\*Transparency and Trust\*\*: The opaque nature of AI decision-making processes can erode public trust and understanding.
- \*\*Safety Risks\*\*: There is a potential for AI systems to violate safety norms and impact people's rights and safety negatively.
- \*\*Complexity of Mitigation\*\*: Mitigating the risks associated with AI requires ongoing transparency, participatory design, and engagement with impacted communities, which can be complex and resource-intensive.

In conclusion, while AI offers numerous benefits, including innovation, improved infrastructure, and enhanced community welfare, it also poses significant risks related to bias, transparency, and safety. Experts argue that a balanced approach, involving robust mitigation strategies and inclusive design, is essential to harness the benefits of AI while minimizing its risks.
\### Comparison of Risks and Benefits of AI

#### Risks of AI:
1. \*\*Biased Data and Discriminatory Outcomes\*\*: AI systems can perpetuate and even exacerbate biases present in the data they are trained on, leading to unfair and discriminatory outcomes.
2. \*\*Opaque Decision-Making\*\*: The decision-making processes of AI systems can be complex and not easily understandable, leading to a lack of transparency.
3. \*\*Lack of Public Trust\*\*: The opacity and potential biases in AI systems can result in a lack of trust and understanding from the public.
4. \*\*Safety and Rights Violations\*\*: There is a risk of AI systems violating safety norms and impacting people's rights, opportunities, or safety.

#### Benefits of AI:
1. \*\*Improved Infrastructure\*\*: AI has the potential to transform and improve infrastructure, making it more innovative and efficient.
2. \*\*Enhanced Community Health and Safety\*\*: AI can play a significant role in improving community health, safety, and welfare by ensuring better representation and inclusivity.
3. \*\*Prevention of Harms\*\*: AI can help prevent harms and improve opportunities, rights, and access, particularly for marginalized communities.
4. \*\*Policy Shaping\*\*: AI is central to shaping important policies, such as the Blueprint for an AI Bill of Rights, which aims to protect and enhance the rights of individuals.

### Summary with Arguments For and Against AI

#### Arguments For AI:
- \*\*Innovation and Efficiency\*\*: AI can drive significant advancements in technology and infrastructure, leading to more efficient and innovative solutions.
- \*\*Inclusivity and Representation\*\*: AI can ensure better representation of marginalized voices, leading to more equitable outcomes.
- \*\*Health and Safety\*\*: AI can enhance community health and safety by providing better tools and systems for monitoring and intervention.
- \*\*Policy and Rights\*\*: AI can play a crucial role in shaping policies that protect and enhance individual rights and opportunities.

#### Arguments Against AI:
- \*\*Bias and Discrimination\*\*: The risk of biased data leading to discriminatory outcomes is a significant concern.
- \*\*Transparency and Trust\*\*: The opaque nature of AI decision-making processes can erode public trust and understanding.
- \*\*Safety Risks\*\*: There is a potential for AI systems to violate safety norms and impact people's rights and safety negatively.
- \*\*Complexity of Mitigation\*\*: Mitigating the risks associated with AI requires ongoing transparency, participatory design, and engagement with impacted communities, which can be complex and resource-intensive.

In conclusion, while AI offers numerous benefits, including innovation, improved infrastructure, and enhanced community welfare, it also poses significant risks related to bias, transparency, and safety. Experts argue that a balanced approach, involving robust mitigation strategies and inclusive design, is essential to harness the benefits of AI while minimizing its risks.

Back to top

[Previous Semantic Retriever Benchmark](https://docs.llamaindex.ai/en/stable/examples/managed/manage_retrieval_benchmark/)[Next Managed Index with Zilliz Cloud Pipelines](https://docs.llamaindex.ai/en/stable/examples/managed/zcpDemo/)

Hi, how can I help you?

🦙
