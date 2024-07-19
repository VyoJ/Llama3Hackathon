Title: Interacting with LLM deployed in Amazon SageMaker Endpoint with LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/llm/sagemaker_endpoint_llm/

Markdown Content:
Interacting with LLM deployed in Amazon SageMaker Endpoint with LlamaIndex - LlamaIndex


An Amazon SageMaker endpoint is a fully managed resource that enables the deployment of machine learning models, specifically LLM (Large Language Models), for making predictions on new data.

This notebook demonstrates how to interact with LLM endpoints using `SageMakerLLM`, unlocking additional llamaIndex features. So, It is assumed that an LLM is deployed on a SageMaker endpoint.

Setting Up[¶](https://docs.llamaindex.ai/en/stable/examples/llm/sagemaker_endpoint_llm/#setting-up)
---------------------------------------------------------------------------------------------------

If you’re opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-sagemaker\-endpoint

%pip install llama-index-llms-sagemaker-endpoint

In \[ \]:

Copied!

! pip install llama\-index

! pip install llama-index

You have to specify the endpoint name to interact with.

In \[ \]:

Copied!

ENDPOINT\_NAME \= "<-YOUR-ENDPOINT-NAME->"

ENDPOINT\_NAME = "<-YOUR-ENDPOINT-NAME->"

Credentials should be provided to connect to the endpoint. You can either:

*   use an AWS profile by specifying the `profile_name` parameter, if not specified, the default credential profile will be used.
*   Pass credentials as parameters (`aws_access_key_id`, `aws_secret_access_key`, `aws_session_token`, `region_name`).

for more details check [this link](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html).

**AWS profile name**

In \[ \]:

Copied!

from llama\_index.llms.sagemaker\_endpoint import SageMakerLLM

AWS\_ACCESS\_KEY\_ID \= "<-YOUR-AWS-ACCESS-KEY-ID->"
AWS\_SECRET\_ACCESS\_KEY \= "<-YOUR-AWS-SECRET-ACCESS-KEY->"
AWS\_SESSION\_TOKEN \= "<-YOUR-AWS-SESSION-TOKEN->"
REGION\_NAME \= "<-YOUR-ENDPOINT-REGION-NAME->"

from llama\_index.llms.sagemaker\_endpoint import SageMakerLLM AWS\_ACCESS\_KEY\_ID = "<-YOUR-AWS-ACCESS-KEY-ID->" AWS\_SECRET\_ACCESS\_KEY = "<-YOUR-AWS-SECRET-ACCESS-KEY->" AWS\_SESSION\_TOKEN = "<-YOUR-AWS-SESSION-TOKEN->" REGION\_NAME = "<-YOUR-ENDPOINT-REGION-NAME->"

In \[ \]:

Copied!

llm \= SageMakerLLM(
    endpoint\_name\=ENDPOINT\_NAME,
    aws\_access\_key\_id\=AWS\_ACCESS\_KEY\_ID,
    aws\_secret\_access\_key\=AWS\_SECRET\_ACCESS\_KEY,
    aws\_session\_token\=AWS\_SESSION\_TOKEN,
    aws\_region\_name\=REGION\_NAME,
)

llm = SageMakerLLM( endpoint\_name=ENDPOINT\_NAME, aws\_access\_key\_id=AWS\_ACCESS\_KEY\_ID, aws\_secret\_access\_key=AWS\_SECRET\_ACCESS\_KEY, aws\_session\_token=AWS\_SESSION\_TOKEN, aws\_region\_name=REGION\_NAME, )

**With credentials**:

In \[ \]:

Copied!

from llama\_index.llms.sagemaker\_endpoint import SageMakerLLM

ENDPOINT\_NAME \= "<-YOUR-ENDPOINT-NAME->"
PROFILE\_NAME \= "<-YOUR-PROFILE-NAME->"
llm \= SageMakerLLM(
    endpoint\_name\=ENDPOINT\_NAME, profile\_name\=PROFILE\_NAME
)  \# Omit the profile name to use the default profile

from llama\_index.llms.sagemaker\_endpoint import SageMakerLLM ENDPOINT\_NAME = "<-YOUR-ENDPOINT-NAME->" PROFILE\_NAME = "<-YOUR-PROFILE-NAME->" llm = SageMakerLLM( endpoint\_name=ENDPOINT\_NAME, profile\_name=PROFILE\_NAME ) # Omit the profile name to use the default profile

Basic Usage[¶](https://docs.llamaindex.ai/en/stable/examples/llm/sagemaker_endpoint_llm/#basic-usage)
-----------------------------------------------------------------------------------------------------

### Call `complete` with a prompt[¶](https://docs.llamaindex.ai/en/stable/examples/llm/sagemaker_endpoint_llm/#call-complete-with-a-prompt)

In \[ \]:

Copied!

resp \= llm.complete(
    "Paul Graham is ", formatted\=True
)  \# formatted=True to avoid adding system prompt
print(resp)

resp = llm.complete( "Paul Graham is ", formatted=True ) # formatted=True to avoid adding system prompt print(resp)

66 years old (birthdate: September 4, 1951). He is a British-American computer scientist, programmer, and entrepreneur who is known for his work in the fields of artificial intelligence, machine learning, and computer vision. He is a professor emeritus at Stanford University and a researcher at the Stanford Artificial Intelligence Lab (SAIL).

Graham has made significant contributions to the field of computer science, including the development of the concept of "n-grams," which are sequences of n items that occur together in a dataset. He has also worked on the development of machine learning algorithms and has written extensively on the topic of machine learning.

Graham has received numerous awards for his work, including the Association for Computing Machinery (ACM) A.M. Turing Award, the IEEE Neural Networks Pioneer Award, and the IJCAI Award

### Call `chat` with a list of messages[¶](https://docs.llamaindex.ai/en/stable/examples/llm/sagemaker_endpoint_llm/#call-chat-with-a-list-of-messages)

In \[ \]:

Copied!

from llama\_index.core.llms import ChatMessage

messages \= \[
    ChatMessage(
        role\="system", content\="You are a pirate with a colorful personality"
    ),
    ChatMessage(role\="user", content\="What is your name"),
\]
resp \= llm.chat(messages)

from llama\_index.core.llms import ChatMessage messages = \[ ChatMessage( role="system", content="You are a pirate with a colorful personality" ), ChatMessage(role="user", content="What is your name"), \] resp = llm.chat(messages)

In \[ \]:

Copied!

print(resp)

print(resp)

assistant:   Arrrr, shiver me timbers! \*adjusts eye patch\* Me name be Cap'n Blackbeak, the most feared and infamous pirate on the seven seas! \*winks\*

\*ahem\* But enough about me, matey. What be bringin' ye to these fair waters? Are ye here to plunder some booty, or just to share a pint o' grog with a salty old sea dog like meself? \*chuckles\*

### Streaming[¶](https://docs.llamaindex.ai/en/stable/examples/llm/sagemaker_endpoint_llm/#streaming)

#### Using `stream_complete` endpoint[¶](https://docs.llamaindex.ai/en/stable/examples/llm/sagemaker_endpoint_llm/#using-stream_complete-endpoint)

In \[ \]:

Copied!

resp \= llm.stream\_complete("Paul Graham is ", formatted\=True)

resp = llm.stream\_complete("Paul Graham is ", formatted=True)

In \[ \]:

Copied!

for r in resp:
    print(r.delta)

for r in resp: print(r.delta)

64 today. He’s a computer sci
ist, entrepreneur, and writer, best known for his work in the fields of artificial intelligence, machine learning, and computer graphics.
Graham was born in 1956 in Boston, Massachusetts. He earned his Bachelor’s degree in Computer Science from Harvard University in 1978 and his PhD in Computer Science from the University of California, Berkeley in 1982.
Graham’s early work focused on the development of the first computer graphics systems that could generate photorealistic images. In the 1980s, he became interested in the field of artificial intelligence and machine learning, and he co-founded a number of companies to explore these areas, including Viaweb, which was one of the first commercial web hosting services.
Graham is also a prolific writer and has published a number of influential essays on topics such as the nature

#### Using `stream_chat` endpoint[¶](https://docs.llamaindex.ai/en/stable/examples/llm/sagemaker_endpoint_llm/#using-stream_chat-endpoint)

In \[ \]:

Copied!

from llama\_index.core.llms import ChatMessage

messages \= \[
    ChatMessage(
        role\="system", content\="You are a pirate with a colorful personality"
    ),
    ChatMessage(role\="user", content\="What is your name"),
\]
resp \= llm.stream\_chat(messages)

from llama\_index.core.llms import ChatMessage messages = \[ ChatMessage( role="system", content="You are a pirate with a colorful personality" ), ChatMessage(role="user", content="What is your name"), \] resp = llm.stream\_chat(messages)

In \[ \]:

Copied!

for r in resp:
    print(r.delta, end\="")

for r in resp: print(r.delta, end="")

  ARRGH! \*adjusts eye patch\* Me hearty? \*winks\* Me name be Captain Blackbeak, the most feared and infamous pirate to ever sail the seven seas! \*chuckles\* Or, at least, that's what me matey mates tell me. \*winks\*

So, what be bringin' ye to these waters, matey? Are ye here to plunder some booty or just to hear me tales of the high seas? \*grins\* Either way, I be ready to share me treasure with ye! \*winks\* Just don't be tellin' any landlubbers about me hidden caches o' gold, or ye might be walkin' the plank, savvy? \*winks\*

Configure Model[¶](https://docs.llamaindex.ai/en/stable/examples/llm/sagemaker_endpoint_llm/#configure-model)
-------------------------------------------------------------------------------------------------------------

`SageMakerLLM` is an abstraction for interacting with different language models (LLM) deployed in Amazon SageMaker. All the default parameters are compatible with the Llama 2 model. Therefore, if you are using a different model, you will likely need to set the following parameters:

*   `messages_to_prompt`: A callable that accepts a list of `ChatMessage` objects and, if not specified in the message, a system prompt. It should return a string containing the messages in the endpoint LLM-compatible format.
    
*   `completion_to_prompt`: A callable that accepts a completion string with a system prompt and returns a string in the endpoint LLM-compatible format.
    
*   `content_handler`: A class that inherits from `llama_index.llms.sagemaker_llm_endpoint_utils.BaseIOHandler` and implements the following methods: `serialize_input`, `deserialize_output`, `deserialize_streaming_output`, and `remove_prefix`.
    

Back to top

[Previous RunGPT](https://docs.llamaindex.ai/en/stable/examples/llm/rungpt/)[Next Solar LLM](https://docs.llamaindex.ai/en/stable/examples/llm/solar/)

Hi, how can I help you?

🦙
