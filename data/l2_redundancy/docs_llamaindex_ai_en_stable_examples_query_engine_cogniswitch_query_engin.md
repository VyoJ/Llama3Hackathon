Title: Cogniswitch query engine - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/query_engine/cogniswitch_query_engine/

Markdown Content:
Cogniswitch query engine - LlamaIndex


       

CogniswitchQueryEngine[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/cogniswitch_query_engine/#cogniswitchqueryengine)
--------------------------------------------------------------------------------------------------------------------------------------

**Use CogniSwitch to build production ready applications that can consume, organize and retrieve knowledge flawlessly. Using the framework of your choice, in this case LlamaIndex, CogniSwitch helps alleviate the stress of decision making when it comes to choosing the right storage and retrieval formats. It also eradicates reliability issues and hallucinations when it comes to responses that are generated. Start interacting with your knowledge in 3 simple steps!**

Visit [https://www.cogniswitch.ai/developer](https://www.cogniswitch.ai/developer?utm_source=llamaindex&utm_medium=llamaindexbuild&utm_id=dev).

**Registration:**

*   Signup with your email and verify your registration
*   You will get a mail with a platform token and oauth token for using the services.

**Upload Knowledge:**

*   There are two ways to add your knowledge into Cogniswitch.

1.  You can sign-in to Cogniswitch website and upload your document files or submit a url from the Document Upload page.  
    
2.  You can use the CogniswitchToolSpec in llama-hub tools to add document or a url in Cogniswitch.  
    

**CogniswitchQueryEngine:**

*   Instantiate the cogniswitchQueryEngine with the tokens and API keys.
*   Use query\_knowledge function in the Query Engine and input your query.  
    
*   You will get the answer from your knowledge as the response.  
    

### Import Required Libraries[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/cogniswitch_query_engine/#import-required-libraries)

In \[ \]:

Copied!

import warnings

warnings.filterwarnings("ignore")
from llama\_index.core.query\_engine import CogniswitchQueryEngine

import warnings warnings.filterwarnings("ignore") from llama\_index.core.query\_engine import CogniswitchQueryEngine

### Cogniswitch Credentials and OpenAI token[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/cogniswitch_query_engine/#cogniswitch-credentials-and-openai-token)

In \[ \]:

Copied!

\# cs\_token = <your cogniswitch platform token>
\# OAI\_token = <your openai token>
\# oauth\_token = <your cogniswitch apikey>

\# cs\_token = \# OAI\_token = \# oauth\_token =

### Instantiate the Query Engine[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/cogniswitch_query_engine/#instantiate-the-query-engine)

In \[ \]:

Copied!

query\_engine \= CogniswitchQueryEngine(
    cs\_token\=cs\_token, OAI\_token\=OAI\_token, apiKey\=oauth\_token
)

query\_engine = CogniswitchQueryEngine( cs\_token=cs\_token, OAI\_token=OAI\_token, apiKey=oauth\_token )

### Use the query\_engine to chat with your knowledge[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/cogniswitch_query_engine/#use-the-query_engine-to-chat-with-your-knowledge)

In \[ \]:

Copied!

answer\_response \= query\_engine.query\_knowledge("tell me about cogniswitch")
print(answer\_response)

answer\_response = query\_engine.query\_knowledge("tell me about cogniswitch") print(answer\_response)

CogniSwitch is a platform that offers a range of features to users. It helps users organize, explore, and manage data in an intuitive way. The platform visualizes complex ideas, simplifies them, and fine-tunes knowledge. Users can also consume knowledge on-demand through the CogniSwitch API. Furthermore, CogniSwitch provides data storage management capabilities.

Back to top

[Previous CitationQueryEngine](https://docs.llamaindex.ai/en/stable/examples/query_engine/citation_query_engine/)[Next Defining a Custom Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/custom_query_engine/)

Hi, how can I help you?

🦙
