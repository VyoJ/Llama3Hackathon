Title: Codestral from MistralAI Cookbook - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/cookbooks/codestral/

Markdown Content:
Codestral from MistralAI Cookbook - LlamaIndex


MistralAI released [codestral-latest](https://mistral.ai/news/codestral/) - a code model.

Codestral is a new code model from mistralai tailored for code generation, fluent in over 80 programming languages. It simplifies coding tasks by completing functions, writing tests, and filling in code snippets, enhancing developer efficiency and reducing errors. Codestral operates through a unified API endpoint, making it a versatile tool for software development.

This cookbook showcases how to use the `codestral-latest` model with llama-index. It guides you through using the Codestral fill-in-the-middle and instruct endpoints.

### Setup LLM[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/codestral/#setup-llm)

In \[ \]:

Copied!

import os

os.environ\["MISTRAL\_API\_KEY"\] \= "<YOUR MISTRAL API KEY>"

from llama\_index.llms.mistralai import MistralAI

llm \= MistralAI(model\="codestral-latest", temperature\=0.1)

import os os.environ\["MISTRAL\_API\_KEY"\] = "" from llama\_index.llms.mistralai import MistralAI llm = MistralAI(model="codestral-latest", temperature=0.1)

### Instruct mode usage[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/codestral/#instruct-mode-usage)

#### Write a function for fibonacci[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/codestral/#write-a-function-for-fibonacci)

In \[ \]:

Copied!

from llama\_index.core.llms import ChatMessage

messages \= \[ChatMessage(role\="user", content\="Write a function for fibonacci")\]

response \= llm.chat(messages)

print(response)

from llama\_index.core.llms import ChatMessage messages = \[ChatMessage(role="user", content="Write a function for fibonacci")\] response = llm.chat(messages) print(response)

assistant: Sure, here is a simple Python function that calculates the nth number in the Fibonacci sequence:

\`\`\`python
def fibonacci(n):
    if n <= 0:
        print("Input should be positive integer.")
    elif n  2:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n):
            a, b = b, a + b
        return b
\`\`\`

You can use this function to find the nth number in the Fibonacci sequence by calling \`fibonacci(n)\`, where \`n\` is the position of the number you want to find. For example, \`fibonacci(10)\` will return the 10th number in the Fibonacci sequence.

#### Write a function to build RAG pipeline using LlamaIndex.[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/codestral/#write-a-function-to-build-rag-pipeline-using-llamaindex)

Note: The output is mostly accurate, but it is based on an older LlamaIndex package.

In \[ \]:

Copied!

messages \= \[
    ChatMessage(
        role\="user",
        content\="Write a function to build RAG pipeline using LlamaIndex.",
    )
\]

response \= llm.chat(messages)

print(response)

messages = \[ ChatMessage( role="user", content="Write a function to build RAG pipeline using LlamaIndex.", ) \] response = llm.chat(messages) print(response)

assistant: Sure, I can help you with that. Here's a basic example of how you can build a Retrieval Augmented Generation (RAG) pipeline using LlamaIndex. This example assumes that you have a list of documents.

\`\`\`python
from llama\_index import VectorStoreIndex, SimpleDirectoryReader

def build\_rag\_pipeline(documents\_path):
    # Load documents
    documents = SimpleDirectoryReader(documents\_path).load\_data()

    # Create index
    index = VectorStoreIndex.from\_documents(documents)

    # Create query engine
    query\_engine = index.as\_query\_engine()

    return query\_engine

# Usage
query\_engine = build\_rag\_pipeline("path\_to\_your\_documents")
response = query\_engine.query("Your query here")
print(response)
\`\`\`

In this code:

1. We first import the necessary classes from LlamaIndex.
2. We define a function \`build\_rag\_pipeline\` that takes a path to a directory of documents as input.
3. We load the documents using \`SimpleDirectoryReader\`.
4. We create an index from the documents using \`VectorStoreIndex.from\_documents\`.
5. We create a query engine from the index using \`index.as\_query\_engine\`.
6. Finally, we return the query engine.

You can use the query engine to ask questions about the documents. The query engine will use the index to retrieve relevant documents and then generate a response based on those documents.

### Fill-in-the-middle[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/codestral/#fill-in-the-middle)

This feature allows users to set a starting point with a prompt and an optional ending with a suffix and stop. The Codestral model then generates the intervening code, perfect for tasks requiring specific code generation.

#### Fill the code with start and end of the code.[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/codestral/#fill-the-code-with-start-and-end-of-the-code)

In \[ \]:

Copied!

prompt \= "def multiply("
suffix \= "return a\*b"

response \= llm.fill\_in\_middle(prompt, suffix)

print(
    f"""
{prompt}
{response.text}
{suffix}
"""
)

prompt = "def multiply(" suffix = "return a\*b" response = llm.fill\_in\_middle(prompt, suffix) print( f""" {prompt} {response.text} {suffix} """ )

def multiply(
a, b):
  """
  This function multiplies two numbers
  """
  
return a\*b

#### Fill the code with start, end of the code and stop tokens.[¶](https://docs.llamaindex.ai/en/stable/examples/cookbooks/codestral/#fill-the-code-with-start-end-of-the-code-and-stop-tokens)

In \[ \]:

Copied!

prompt \= "def multiply(a,"
suffix \= ""
stop \= \["\\n\\n\\n"\]

response \= llm.fill\_in\_middle(prompt, suffix, stop)

print(
    f"""
{prompt}
{response.text}
{suffix}
"""
)

prompt = "def multiply(a," suffix = "" stop = \["\\n\\n\\n"\] response = llm.fill\_in\_middle(prompt, suffix, stop) print( f""" {prompt} {response.text} {suffix} """ )

def multiply(a,
 b):

    return a \* b

# test the function
print(multiply(2, 3))  # should print 6
print(multiply(-1, 5))  # should print -5
print(multiply(0, 99))  # should print 0

# we can also test the function with large numbers
print(multiply(123456789, 987654321))  # should print 121932631132635269

# the function should also work with floating point numbers
print(multiply(3.14, 2.71))  # should print approximately 8.5392

# the function should also work with negative floating point numbers
print(multiply(-3.14, 2.71))  # should print approximately -8.5392

# the function should also work with mixed types (integer and floating point)
print(multiply(2, 3.14))  # should print approximately 6.28

Back to top

[Previous Anthropic Haiku Cookbook](https://docs.llamaindex.ai/en/stable/examples/cookbooks/anthropic_haiku/)[Next Cohere init8 and binary Embeddings Retrieval Evaluation](https://docs.llamaindex.ai/en/stable/examples/cookbooks/cohere_retriever_eval/)
