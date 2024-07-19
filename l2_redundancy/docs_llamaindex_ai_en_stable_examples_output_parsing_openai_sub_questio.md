Title: OpenAI function calling for Sub-Question Query Engine

URL Source: https://docs.llamaindex.ai/en/stable/examples/output_parsing/openai_sub_question/

Markdown Content:
OpenAI function calling for Sub-Question Query Engine - LlamaIndex


In this notebook, we showcase how to use OpenAI function calling to improve the robustness of our sub-question query engine.

The sub-question query engine is designed to accept swappable question generators that implement the `BaseQuestionGenerator` interface.  
To leverage the power of openai function calling API, we implemented a new `OpenAIQuestionGenerator` (powered by our `OpenAIPydanticProgram`)

OpenAI Question Generator[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/openai_sub_question/#openai-question-generator)
-----------------------------------------------------------------------------------------------------------------------------------------

Unlike the default `LLMQuestionGenerator` that supports generic LLMs via the completion API, `OpenAIQuestionGenerator` only works with the latest OpenAI models that supports the function calling API.

The benefit is that these models are fine-tuned to output JSON objects, so we can worry less about output parsing issues.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-question\-gen\-openai

%pip install llama-index-question-gen-openai

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

from llama\_index.question\_gen.openai import OpenAIQuestionGenerator

from llama\_index.question\_gen.openai import OpenAIQuestionGenerator

In \[ \]:

Copied!

question\_gen \= OpenAIQuestionGenerator.from\_defaults()

question\_gen = OpenAIQuestionGenerator.from\_defaults()

Let's test it out!

In \[ \]:

Copied!

from llama\_index.core.tools import ToolMetadata
from llama\_index.core import QueryBundle

from llama\_index.core.tools import ToolMetadata from llama\_index.core import QueryBundle

In \[ \]:

Copied!

tools \= \[
    ToolMetadata(
        name\="march\_22",
        description\=(
            "Provides information about Uber quarterly financials ending March"
            " 2022"
        ),
    ),
    ToolMetadata(
        name\="june\_22",
        description\=(
            "Provides information about Uber quarterly financials ending June"
            " 2022"
        ),
    ),
    ToolMetadata(
        name\="sept\_22",
        description\=(
            "Provides information about Uber quarterly financials ending"
            " September 2022"
        ),
    ),
    ToolMetadata(
        name\="sept\_21",
        description\=(
            "Provides information about Uber quarterly financials ending"
            " September 2022"
        ),
    ),
    ToolMetadata(
        name\="june\_21",
        description\=(
            "Provides information about Uber quarterly financials ending June"
            " 2022"
        ),
    ),
    ToolMetadata(
        name\="march\_21",
        description\=(
            "Provides information about Uber quarterly financials ending March"
            " 2022"
        ),
    ),
\]

tools = \[ ToolMetadata( name="march\_22", description=( "Provides information about Uber quarterly financials ending March" " 2022" ), ), ToolMetadata( name="june\_22", description=( "Provides information about Uber quarterly financials ending June" " 2022" ), ), ToolMetadata( name="sept\_22", description=( "Provides information about Uber quarterly financials ending" " September 2022" ), ), ToolMetadata( name="sept\_21", description=( "Provides information about Uber quarterly financials ending" " September 2022" ), ), ToolMetadata( name="june\_21", description=( "Provides information about Uber quarterly financials ending June" " 2022" ), ), ToolMetadata( name="march\_21", description=( "Provides information about Uber quarterly financials ending March" " 2022" ), ), \]

In \[ \]:

Copied!

sub\_questions \= question\_gen.generate(
    tools\=tools,
    query\=QueryBundle(
        "Compare the fastest growing sectors for Uber in the first two"
        " quarters of 2022"
    ),
)

sub\_questions = question\_gen.generate( tools=tools, query=QueryBundle( "Compare the fastest growing sectors for Uber in the first two" " quarters of 2022" ), )

In \[ \]:

Copied!

sub\_questions

sub\_questions

Out\[ \]:

\[SubQuestion(sub\_question='What were the fastest growing sectors for Uber in March 2022?', tool\_name='march\_22'),
 SubQuestion(sub\_question='What were the fastest growing sectors for Uber in June 2022?', tool\_name='june\_22')\]

Back to top

[Previous OpenAI Pydantic Program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/openai_pydantic_program/)[Next \[WIP\] Hyperparameter Optimization for RAG](https://docs.llamaindex.ai/en/stable/examples/param_optimizer/param_optimizer/)

Hi, how can I help you?

🦙
