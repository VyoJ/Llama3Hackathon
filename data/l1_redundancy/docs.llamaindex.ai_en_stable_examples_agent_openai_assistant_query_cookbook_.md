Title: OpenAI Assistant Advanced Retrieval Cookbook

URL Source: https://docs.llamaindex.ai/en/stable/examples/agent/openai_assistant_query_cookbook/

Markdown Content:
OpenAI Assistant Advanced Retrieval Cookbook - LlamaIndex


In this notebook, we try out OpenAI Assistant API for advanced retrieval tasks, by plugging in a variety of query engine tools and datasets. The wrapper abstraction we use is our `OpenAIAssistantAgent` class, which allows us to plug in custom tools. We explore how `OpenAIAssistant` can complement/replace existing workflows solved by our retrievers/query engines through its agent execution + function calling loop.

*   Joint QA + Summarization
*   Auto retrieval
*   Joint SQL and vector search

In \[ \]:

Copied!

%pip install llama\-index\-agent\-openai
%pip install llama\-index\-vector\-stores\-pinecone
%pip install llama\-index\-readers\-wikipedia
%pip install llama\-index\-llms\-openai

%pip install llama-index-agent-openai %pip install llama-index-vector-stores-pinecone %pip install llama-index-readers-wikipedia %pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

import nest\_asyncio

nest\_asyncio.apply()

import nest\_asyncio nest\_asyncio.apply()

Joint QA and Summarization[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_assistant_query_cookbook/#joint-qa-and-summarization)
----------------------------------------------------------------------------------------------------------------------------------------------

In this section we show how we can get the Assistant agent to both answer fact-based questions and summarization questions. This is something that the in-house retrieval tool struggles to accomplish.

### Load Data[¶](https://docs.llamaindex.ai/en/stable/examples/agent/openai_assistant_query_cookbook/#load-data)

In \[ \]:

Copied!

!mkdir \-p 'data/paul\_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' \-O 'data/paul\_graham/paul\_graham\_essay.txt'

!mkdir -p 'data/paul\_graham/' !wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'

\--2023-11-11 09:40:13--  https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/examples/data/paul\_graham/paul\_graham\_essay.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 2606:50c0:8002::154, 2606:50c0:8003::154, 2606:50c0:8000::154, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|2606:50c0:8002::154|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 75042 (73K) \[text/plain\]
Saving to: ‘data/paul\_graham/paul\_graham\_essay.txt’

data/paul\_graham/pa 100%\[ Calling Function 
Paul Graham is an author with eclectic interests and a varied career path. He began with interests in writing and programming, engaged in philosophy and artificial intelligence during college, and authored a book on Lisp programming. With an equally strong passion for art, he studied at the Accademia di Belli Arti in Florence and briefly at the Rhode Island School of Design before immersing himself in the tech industry by starting Viaweb and later founding the influential startup accelerator Y Combinator. He also created Hacker News, a social news website focused on computer science and entrepreneurship. Graham's life reflects a blend of technology, entrepreneurship, and the arts.

In \[ \]:

Copied!

response \= agent.query("What did the author do after RICS?")
print(str(response))

response = agent.query("What did the author do after RICS?") print(str(response))

\
Calling function: vector\_tool with args: {"input":"After RICS"}
Got output: After RICS, the author moved back to Providence to continue at RISD. However, it became clear that art school, specifically the painting department, did not have the same relationship to art as medical school had to medicine. Painting students were expected to express themselves and develop a distinctive signature style.
 Calling Function 

Calling function: celebrity\_bios with args: {"query": "celebrity from United States", "filter\_key\_list": \["country"\], "filter\_value\_list": \["United States"\]}
Got output: \['Angelina Jolie is an American actress, filmmaker, and humanitarian. She has received numerous awards for her acting and is known for her philanthropic work.', 'Michael Jordan is a retired professional basketball player, widely regarded as one of the greatest basketball players of all time.'\]
 Calling Function 

Calling function: vector\_tool with args: {"input":"What are the arts and culture like in Tokyo, Japan?"}
Got output: Tokyo has a vibrant arts and culture scene. The city is home to many museums, including the Tokyo National Museum, which specializes in traditional Japanese art, the National Museum of Western Art, and the Edo-Tokyo Museum. There are also theaters for traditional forms of Japanese drama, such as the National Noh Theatre and the Kabuki-za. Tokyo hosts modern Japanese and international pop and rock music concerts, and the New National Theater Tokyo is a hub for opera, ballet, contemporary dance, and drama. The city also celebrates various festivals throughout the year, including the Sannō, Sanja, and Kanda Festivals. Additionally, Tokyo is known for its youth style, fashion, and cosplay in the Harajuku neighborhood.
 Calling Function 
Berlin, the capital city of Germany, has a rich and complex history that stretches back to its first documentation in the 13th century. Throughout the centuries, Berlin has been at the heart of numerous important historical movements and events.

Initially a small town, Berlin grew in significance as the capital of the Margraviate of Brandenburg. Later on, it ascended in prominence as the capital of the Kingdom of Prussia. With the unification of Germany, Berlin became the imperial capital of the German Empire, a position it retained until the end of World War I.

The interwar period saw Berlin as the capital of the Weimar Republic, and it was during this time that the city became known for its vibrant cultural scene. However, the rise of the Nazi regime in the 1930s led to a dark period in Berlin's history, and the city was heavily damaged during World War II.

Following the war's end, Berlin became a divided city. The division was physical, represented by the Berlin Wall, and ideological, with West Berlin aligning with democratic West Germany while East Berlin became the capital of the socialist East Germany.

The fall of the Berlin Wall in November 1989 was a historic moment, leading to German reunification in 1990. Berlin was once again chosen as the capital of a united Germany. Since reunification, Berlin has undergone massive reconstruction and has become a hub of contemporary culture, politics, media, and science.

Today, Berlin celebrates its diverse heritage, from its grand historical landmarks like the Brandenburg Gate and the Reichstag, to its remembrance of the past with monuments such as the Berlin Wall Memorial and the Holocaust Memorial. It is a city known for its cultural dynamism, thriving arts and music scenes, and a high quality of life. Berlin's history has shaped it into a unique world city that continues to play a significant role on the global stage.

In \[ \]:

Copied!

response \= agent.chat(
    "Can you give me the country corresponding to each city?"
)
print(str(response))

response = agent.chat( "Can you give me the country corresponding to each city?" ) print(str(response))

\
Calling function: sql\_tool with args: {"input":"SELECT name, country FROM city\_stats"}
Got output: The cities in the city\_stats table are Toronto from Canada, Tokyo from Japan, and Berlin from Germany.

Here are the countries corresponding to each city:

- Toronto: Canada
- Tokyo: Japan
- Berlin: Germany

Back to top

[Previous OpenAI Assistant Agent](https://docs.llamaindex.ai/en/stable/examples/agent/openai_assistant_agent/)[Next OpenAI agent: specifying a forced function call](https://docs.llamaindex.ai/en/stable/examples/agent/openai_forced_function_call/)

Hi, how can I help you?

🦙
