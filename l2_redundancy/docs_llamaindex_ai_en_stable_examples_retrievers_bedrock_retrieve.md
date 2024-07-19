Title: Bedrock (Knowledge Bases) - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/retrievers/bedrock_retriever/

Markdown Content:
Bedrock (Knowledge Bases) - LlamaIndex


[Knowledge bases for Amazon Bedrock](https://aws.amazon.com/bedrock/knowledge-bases/) is an Amazon Web Services (AWS) offering which lets you quickly build RAG applications by using your private data to customize FM response.

Implementing `RAG` requires organizations to perform several cumbersome steps to convert data into embeddings (vectors), store the embeddings in a specialized vector database, and build custom integrations into the database to search and retrieve text relevant to the user’s query. This can be time-consuming and inefficient.

With `Knowledge Bases for Amazon Bedrock`, simply point to the location of your data in `Amazon S3`, and `Knowledge Bases for Amazon Bedrock` takes care of the entire ingestion workflow into your vector database. If you do not have an existing vector database, Amazon Bedrock creates an Amazon OpenSearch Serverless vector store for you.

Knowledge base can be configured through [AWS Console](https://aws.amazon.com/console/) or by using [AWS SDKs](https://aws.amazon.com/developer/tools/).

In this notebook, we introduce AmazonKnowledgeBasesRetriever - Amazon Bedrock integration in Llama Index via the Retrieve API to retrieve relevant results for a user query from knowledge bases.

Using the Knowledge Base Retriever[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/bedrock_retriever/#using-the-knowledge-base-retriever)
-----------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

%pip install \--upgrade \--quiet  boto3 botocore
%pip install llama\-index
%pip install llama\-index\-retrievers\-bedrock

%pip install --upgrade --quiet boto3 botocore %pip install llama-index %pip install llama-index-retrievers-bedrock

For more information about the supported parameters for `retrieval_config`, please check the boto3 documentation: [link](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/retrieve.html)

To use filters in the `retrieval_config` you will need to set up metadata.json file for your data source. For more info, see: [link](https://aws.amazon.com/blogs/machine-learning/knowledge-bases-for-amazon-bedrock-now-supports-metadata-filtering-to-improve-retrieval-accuracy/)

In \[ \]:

Copied!

from llama\_index.retrievers.bedrock import AmazonKnowledgeBasesRetriever

retriever \= AmazonKnowledgeBasesRetriever(
    knowledge\_base\_id\="<knowledge-base-id>",
    retrieval\_config\={
        "vectorSearchConfiguration": {
            "numberOfResults": 4,
            "overrideSearchType": "HYBRID",
            "filter": {"equals": {"key": "tag", "value": "space"}},
        }
    },
)

from llama\_index.retrievers.bedrock import AmazonKnowledgeBasesRetriever retriever = AmazonKnowledgeBasesRetriever( knowledge\_base\_id="", retrieval\_config={ "vectorSearchConfiguration": { "numberOfResults": 4, "overrideSearchType": "HYBRID", "filter": {"equals": {"key": "tag", "value": "space"}}, } }, )

In \[ \]:

Copied!

query \= "How big is Milky Way as compared to the entire universe?"
retrieved\_results \= retriever.retrieve(query)

\# Prints the first retrieved result
print(retrieved\_results\[0\].get\_content())

query = "How big is Milky Way as compared to the entire universe?" retrieved\_results = retriever.retrieve(query) # Prints the first retrieved result print(retrieved\_results\[0\].get\_content())

Use the retriever to query with Bedrock LLMs[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/bedrock_retriever/#use-the-retriever-to-query-with-bedrock-llms)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

%pip install llama\-index\-llms\-bedrock

%pip install llama-index-llms-bedrock

In \[ \]:

Copied!

from llama\_index.core import get\_response\_synthesizer
from llama\_index.llms.bedrock.base import Bedrock

llm \= Bedrock(model\="anthropic.claude-v2", temperature\=0, max\_tokens\=3000)
response\_synthesizer \= get\_response\_synthesizer(
    response\_mode\="compact", llm\=llm
)
response\_obj \= response\_synthesizer.synthesize(query, retrieved\_results)
print(response\_obj)

from llama\_index.core import get\_response\_synthesizer from llama\_index.llms.bedrock.base import Bedrock llm = Bedrock(model="anthropic.claude-v2", temperature=0, max\_tokens=3000) response\_synthesizer = get\_response\_synthesizer( response\_mode="compact", llm=llm ) response\_obj = response\_synthesizer.synthesize(query, retrieved\_results) print(response\_obj)

Back to top

[Previous Comparing Methods for Structured Retrieval (Auto-Retrieval vs. Recursive Retrieval)](https://docs.llamaindex.ai/en/stable/examples/retrievers/auto_vs_recursive_retriever/)[Next BM25 Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/bm25_retriever/)
