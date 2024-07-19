Title: JSON Query Engine - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/query_engine/json_query_engine/

Markdown Content:
JSON Query Engine - LlamaIndex


The JSON query engine is useful for querying JSON documents that conform to a JSON schema.

This JSON schema is then used in the context of a prompt to convert a natural language query into a structured JSON Path query. This JSON Path query is then used to retrieve data to answer the given question.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai

%pip install llama-index-llms-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

\# First, install the jsonpath-ng package which is used by default to parse & execute the JSONPath queries.
!pip install jsonpath\-ng

\# First, install the jsonpath-ng package which is used by default to parse & execute the JSONPath queries. !pip install jsonpath-ng

Requirement already satisfied: jsonpath-ng in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (1.5.3)
Requirement already satisfied: ply in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from jsonpath-ng) (3.11)
Requirement already satisfied: six in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from jsonpath-ng) (1.16.0)
Requirement already satisfied: decorator in /Users/loganmarkewich/llama\_index/llama-index/lib/python3.9/site-packages (from jsonpath-ng) (5.1.1)
WARNING: You are using pip version 21.2.4; however, version 23.2.1 is available.
You should consider upgrading via the '/Users/loganmarkewich/llama\_index/llama-index/bin/python3 -m pip install --upgrade pip' command.

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

In \[ \]:

Copied!

import os
import openai

os.environ\["OPENAI\_API\_KEY"\] \= "YOUR\_KEY\_HERE"

import os import openai os.environ\["OPENAI\_API\_KEY"\] = "YOUR\_KEY\_HERE"

In \[ \]:

Copied!

from IPython.display import Markdown, display

from IPython.display import Markdown, display

### Let's start on a Toy JSON[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/json_query_engine/#lets-start-on-a-toy-json)

Very simple JSON object containing data from a blog post site with user comments.

We will also provide a JSON schema (which we were able to generate by giving ChatGPT a sample of the JSON).

#### Advice[¶](https://docs.llamaindex.ai/en/stable/examples/query_engine/json_query_engine/#advice)

Do make sure that you've provided a helpful `"description"` value for each of the fields in your JSON schema.

As you can see in the given example, the description for the `"username"` field mentions that usernames are lowercased. You'll see that this ends up being helpful for the LLM in producing the correct JSON path query.

In \[ \]:

Copied!

\# Test on some sample data
json\_value \= {
    "blogPosts": \[
        {
            "id": 1,
            "title": "First blog post",
            "content": "This is my first blog post",
        },
        {
            "id": 2,
            "title": "Second blog post",
            "content": "This is my second blog post",
        },
    \],
    "comments": \[
        {
            "id": 1,
            "content": "Nice post!",
            "username": "jerry",
            "blogPostId": 1,
        },
        {
            "id": 2,
            "content": "Interesting thoughts",
            "username": "simon",
            "blogPostId": 2,
        },
        {
            "id": 3,
            "content": "Loved reading this!",
            "username": "simon",
            "blogPostId": 2,
        },
    \],
}

\# JSON Schema object that the above JSON value conforms to
json\_schema \= {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "description": "Schema for a very simple blog post app",
    "type": "object",
    "properties": {
        "blogPosts": {
            "description": "List of blog posts",
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "description": "Unique identifier for the blog post",
                        "type": "integer",
                    },
                    "title": {
                        "description": "Title of the blog post",
                        "type": "string",
                    },
                    "content": {
                        "description": "Content of the blog post",
                        "type": "string",
                    },
                },
                "required": \["id", "title", "content"\],
            },
        },
        "comments": {
            "description": "List of comments on blog posts",
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "description": "Unique identifier for the comment",
                        "type": "integer",
                    },
                    "content": {
                        "description": "Content of the comment",
                        "type": "string",
                    },
                    "username": {
                        "description": (
                            "Username of the commenter (lowercased)"
                        ),
                        "type": "string",
                    },
                    "blogPostId": {
                        "description": (
                            "Identifier for the blog post to which the comment"
                            " belongs"
                        ),
                        "type": "integer",
                    },
                },
                "required": \["id", "content", "username", "blogPostId"\],
            },
        },
    },
    "required": \["blogPosts", "comments"\],
}

\# Test on some sample data json\_value = { "blogPosts": \[ { "id": 1, "title": "First blog post", "content": "This is my first blog post", }, { "id": 2, "title": "Second blog post", "content": "This is my second blog post", }, \], "comments": \[ { "id": 1, "content": "Nice post!", "username": "jerry", "blogPostId": 1, }, { "id": 2, "content": "Interesting thoughts", "username": "simon", "blogPostId": 2, }, { "id": 3, "content": "Loved reading this!", "username": "simon", "blogPostId": 2, }, \], } # JSON Schema object that the above JSON value conforms to json\_schema = { "$schema": "http://json-schema.org/draft-07/schema#", "description": "Schema for a very simple blog post app", "type": "object", "properties": { "blogPosts": { "description": "List of blog posts", "type": "array", "items": { "type": "object", "properties": { "id": { "description": "Unique identifier for the blog post", "type": "integer", }, "title": { "description": "Title of the blog post", "type": "string", }, "content": { "description": "Content of the blog post", "type": "string", }, }, "required": \["id", "title", "content"\], }, }, "comments": { "description": "List of comments on blog posts", "type": "array", "items": { "type": "object", "properties": { "id": { "description": "Unique identifier for the comment", "type": "integer", }, "content": { "description": "Content of the comment", "type": "string", }, "username": { "description": ( "Username of the commenter (lowercased)" ), "type": "string", }, "blogPostId": { "description": ( "Identifier for the blog post to which the comment" " belongs" ), "type": "integer", }, }, "required": \["id", "content", "username", "blogPostId"\], }, }, }, "required": \["blogPosts", "comments"\], }

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI
from llama\_index.core.indices.struct\_store import JSONQueryEngine

llm \= OpenAI(model\="gpt-4")

nl\_query\_engine \= JSONQueryEngine(
    json\_value\=json\_value,
    json\_schema\=json\_schema,
    llm\=llm,
)
raw\_query\_engine \= JSONQueryEngine(
    json\_value\=json\_value,
    json\_schema\=json\_schema,
    llm\=llm,
    synthesize\_response\=False,
)

from llama\_index.llms.openai import OpenAI from llama\_index.core.indices.struct\_store import JSONQueryEngine llm = OpenAI(model="gpt-4") nl\_query\_engine = JSONQueryEngine( json\_value=json\_value, json\_schema=json\_schema, llm=llm, ) raw\_query\_engine = JSONQueryEngine( json\_value=json\_value, json\_schema=json\_schema, llm=llm, synthesize\_response=False, )

In \[ \]:

Copied!

nl\_response \= nl\_query\_engine.query(
    "What comments has Jerry been writing?",
)
raw\_response \= raw\_query\_engine.query(
    "What comments has Jerry been writing?",
)

nl\_response = nl\_query\_engine.query( "What comments has Jerry been writing?", ) raw\_response = raw\_query\_engine.query( "What comments has Jerry been writing?", )

In \[ \]:

Copied!

display(
    Markdown(f"<h1>Natural language Response</h1><br><b>{nl\_response}</b>")
)
display(Markdown(f"<h1>Raw JSON Response</h1><br><b>{raw\_response}</b>"))

display( Markdown(f"

Natural language Response


  
**{raw\_response}**"))

Natural language Response


  
**\["Nice post!"\]**

In \[ \]:

Copied!

\# get the json path query string. Same would apply to raw\_response
print(nl\_response.metadata\["json\_path\_response\_str"\])

\# get the json path query string. Same would apply to raw\_response print(nl\_response.metadata\["json\_path\_response\_str"\])

$.comments\[?(@.username=='jerry')\].content

Back to top

[Previous FLARE Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/flare_query_engine/)[Next Knowledge Graph Query Engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/knowledge_graph_query_engine/)

Hi, how can I help you?

🦙
