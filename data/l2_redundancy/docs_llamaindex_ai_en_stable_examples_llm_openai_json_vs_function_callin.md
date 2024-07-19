Title: OpenAI JSON Mode vs. Function Calling for Data Extraction

URL Source: https://docs.llamaindex.ai/en/stable/examples/llm/openai_json_vs_function_calling/

Markdown Content:
OpenAI JSON Mode vs. Function Calling for Data Extraction - LlamaIndex


OpenAI just released [JSON Mode](https://platform.openai.com/docs/guides/text-generation/json-mode): This new config constrain the LLM to only generate strings that parse into valid JSON (but no guarantee on validation against any schema).

Before this, the best way to extract structured data from text is via [function calling](https://platform.openai.com/docs/guides/function-calling).

In this notebook, we explore the tradeoff between the latest [JSON Mode](https://platform.openai.com/docs/guides/text-generation/json-mode) and function calling feature for structured output & extraction.

_Update_: OpenAI has clarified that JSON mode is always enabled for function calling, it's opt-in for regular messages ([https://community.openai.com/t/json-mode-vs-function-calling/476994/4](https://community.openai.com/t/json-mode-vs-function-calling/476994/4))

### Generate synthetic data[¶](https://docs.llamaindex.ai/en/stable/examples/llm/openai_json_vs_function_calling/#generate-synthetic-data)

We'll start by generating some synthetic data for our data extraction task. Let's ask our LLM for a hypothetical sales transcript.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai
%pip install llama\-index\-program\-openai

%pip install llama-index-llms-openai %pip install llama-index-program-openai

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI

llm \= OpenAI(model\="gpt-3.5-turbo-1106")
response \= llm.complete(
    "Generate a sales call transcript, use real names, talk about a product, discuss some action items"
)

from llama\_index.llms.openai import OpenAI llm = OpenAI(model="gpt-3.5-turbo-1106") response = llm.complete( "Generate a sales call transcript, use real names, talk about a product, discuss some action items" )

In \[ \]:

Copied!

transcript \= response.text
print(transcript)

transcript = response.text print(transcript)

\[Phone rings\]

John: Hello, this is John.

Sarah: Hi John, this is Sarah from XYZ Company. I'm calling to discuss our new product, the XYZ Widget, and see if it might be a good fit for your business.

John: Hi Sarah, thanks for reaching out. I'm definitely interested in learning more about the XYZ Widget. Can you give me a quick overview of what it does?

Sarah: Of course! The XYZ Widget is a cutting-edge tool that helps businesses streamline their workflow and improve productivity. It's designed to automate repetitive tasks and provide real-time data analytics to help you make informed decisions.

John: That sounds really interesting. I can see how that could benefit our team. Do you have any case studies or success stories from other companies who have used the XYZ Widget?

Sarah: Absolutely, we have several case studies that I can share with you. I'll send those over along with some additional information about the product. I'd also love to schedule a demo for you and your team to see the XYZ Widget in action.

John: That would be great. I'll make sure to review the case studies and then we can set up a time for the demo. In the meantime, are there any specific action items or next steps we should take?

Sarah: Yes, I'll send over the information and then follow up with you to schedule the demo. In the meantime, feel free to reach out if you have any questions or need further information.

John: Sounds good, I appreciate your help Sarah. I'm looking forward to learning more about the XYZ Widget and seeing how it can benefit our business.

Sarah: Thank you, John. I'll be in touch soon. Have a great day!

John: You too, bye.

### Setup our desired schema[¶](https://docs.llamaindex.ai/en/stable/examples/llm/openai_json_vs_function_calling/#setup-our-desired-schema)

Let's specify our desired output "shape", as a Pydantic Model.

In \[ \]:

Copied!

from pydantic import BaseModel, Field
from typing import List

class CallSummary(BaseModel):
    """Data model for a call summary."""

    summary: str \= Field(
        description\="High-level summary of the call transcript. Should not exceed 3 sentences."
    )
    products: List\[str\] \= Field(
        description\="List of products discussed in the call"
    )
    rep\_name: str \= Field(description\="Name of the sales rep")
    prospect\_name: str \= Field(description\="Name of the prospect")
    action\_items: List\[str\] \= Field(description\="List of action items")

from pydantic import BaseModel, Field from typing import List class CallSummary(BaseModel): """Data model for a call summary.""" summary: str = Field( description="High-level summary of the call transcript. Should not exceed 3 sentences." ) products: List\[str\] = Field( description="List of products discussed in the call" ) rep\_name: str = Field(description="Name of the sales rep") prospect\_name: str = Field(description="Name of the prospect") action\_items: List\[str\] = Field(description="List of action items")

### Data extraction with function calling[¶](https://docs.llamaindex.ai/en/stable/examples/llm/openai_json_vs_function_calling/#data-extraction-with-function-calling)

We can use the `OpenAIPydanticProgram` module in LlamaIndex to make things super easy, simply define a prompt template, and pass in the LLM and pydantic model we've definied.

In \[ \]:

Copied!

from llama\_index.program.openai import OpenAIPydanticProgram
from llama\_index.core import ChatPromptTemplate
from llama\_index.core.llms import ChatMessage

from llama\_index.program.openai import OpenAIPydanticProgram from llama\_index.core import ChatPromptTemplate from llama\_index.core.llms import ChatMessage

In \[ \]:

Copied!

prompt \= ChatPromptTemplate(
    message\_templates\=\[
        ChatMessage(
            role\="system",
            content\=(
                "You are an expert assitant for summarizing and extracting insights from sales call transcripts."
            ),
        ),
        ChatMessage(
            role\="user",
            content\=(
                "Here is the transcript: \\n"
                "------\\n"
                "{transcript}\\n"
                "------"
            ),
        ),
    \]
)
program \= OpenAIPydanticProgram.from\_defaults(
    output\_cls\=CallSummary,
    llm\=llm,
    prompt\=prompt,
    verbose\=True,
)

prompt = ChatPromptTemplate( message\_templates=\[ ChatMessage( role="system", content=( "You are an expert assitant for summarizing and extracting insights from sales call transcripts." ), ), ChatMessage( role="user", content=( "Here is the transcript: \\n" "------\\n" "{transcript}\\n" "------" ), ), \] ) program = OpenAIPydanticProgram.from\_defaults( output\_cls=CallSummary, llm=llm, prompt=prompt, verbose=True, )

In \[ \]:

Copied!

output \= program(transcript\=transcript)

output = program(transcript=transcript)

Function call: CallSummary with args: {"summary":"Sarah from XYZ Company called to discuss the new product, the XYZ Widget, which John expressed interest in. Sarah offered to share case studies and schedule a demo. They agreed to review the case studies and set up a time for the demo. The next steps include Sarah sending over information and following up to schedule the demo.","products":\["XYZ Widget"\],"rep\_name":"Sarah","prospect\_name":"John","action\_items":\["Review case studies","Schedule demo"\]}

We now have the desired structured data, as a Pydantic Model. Quick inspection shows that the results are as we expected.

In \[ \]:

Copied!

output.dict()

output.dict()

Out\[ \]:

{'summary': 'Sarah from XYZ Company called to discuss the new product, the XYZ Widget, which John expressed interest in. Sarah offered to share case studies and schedule a demo. They agreed to review the case studies and set up a time for the demo. The next steps include Sarah sending over information and following up to schedule the demo.',
 'products': \['XYZ Widget'\],
 'rep\_name': 'Sarah',
 'prospect\_name': 'John',
 'action\_items': \['Review case studies', 'Schedule demo'\]}

### Data extraction with JSON mode[¶](https://docs.llamaindex.ai/en/stable/examples/llm/openai_json_vs_function_calling/#data-extraction-with-json-mode)

Let's try to do the same with JSON mode, instead of function calling

In \[ \]:

Copied!

prompt \= ChatPromptTemplate(
    message\_templates\=\[
        ChatMessage(
            role\="system",
            content\=(
                "You are an expert assitant for summarizing and extracting insights from sales call transcripts.\\n"
                "Generate a valid JSON following the given schema below:\\n"
                "{json\_schema}"
            ),
        ),
        ChatMessage(
            role\="user",
            content\=(
                "Here is the transcript: \\n"
                "------\\n"
                "{transcript}\\n"
                "------"
            ),
        ),
    \]
)

prompt = ChatPromptTemplate( message\_templates=\[ ChatMessage( role="system", content=( "You are an expert assitant for summarizing and extracting insights from sales call transcripts.\\n" "Generate a valid JSON following the given schema below:\\n" "{json\_schema}" ), ), ChatMessage( role="user", content=( "Here is the transcript: \\n" "------\\n" "{transcript}\\n" "------" ), ), \] )

In \[ \]:

Copied!

messages \= prompt.format\_messages(
    json\_schema\=CallSummary.schema\_json(), transcript\=transcript
)

messages = prompt.format\_messages( json\_schema=CallSummary.schema\_json(), transcript=transcript )

In \[ \]:

Copied!

output \= llm.chat(
    messages, response\_format\={"type": "json\_object"}
).message.content

output = llm.chat( messages, response\_format={"type": "json\_object"} ).message.content

We get a vaid JSON, but it's only regurgitating the schema we specified, and not actually doing the extraction.

In \[ \]:

Copied!

print(output)

print(output)

{
  "title": "CallSummary",
  "description": "Data model for a call summary.",
  "type": "object",
  "properties": {
    "summary": {
      "title": "Summary",
      "description": "High-level summary of the call transcript. Should not exceed 3 sentences.",
      "type": "string"
    },
    "products": {
      "title": "Products",
      "description": "List of products discussed in the call",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "rep\_name": {
      "title": "Rep Name",
      "description": "Name of the sales rep",
      "type": "string"
    },
    "prospect\_name": {
      "title": "Prospect Name",
      "description": "Name of the prospect",
      "type": "string"
    },
    "action\_items": {
      "title": "Action Items",
      "description": "List of action items",
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": \["summary", "products", "rep\_name", "prospect\_name", "action\_items"\]
}

Let's try again by just showing the JSON format we want, instead of specifying the schema

In \[ \]:

Copied!

import json

prompt \= ChatPromptTemplate(
    message\_templates\=\[
        ChatMessage(
            role\="system",
            content\=(
                "You are an expert assitant for summarizing and extracting insights from sales call transcripts.\\n"
                "Generate a valid JSON in the following format:\\n"
                "{json\_example}"
            ),
        ),
        ChatMessage(
            role\="user",
            content\=(
                "Here is the transcript: \\n"
                "------\\n"
                "{transcript}\\n"
                "------"
            ),
        ),
    \]
)

dict\_example \= {
    "summary": "High-level summary of the call transcript. Should not exceed 3 sentences.",
    "products": \["product 1", "product 2"\],
    "rep\_name": "Name of the sales rep",
    "prospect\_name": "Name of the prospect",
    "action\_items": \["action item 1", "action item 2"\],
}

json\_example \= json.dumps(dict\_example)

import json prompt = ChatPromptTemplate( message\_templates=\[ ChatMessage( role="system", content=( "You are an expert assitant for summarizing and extracting insights from sales call transcripts.\\n" "Generate a valid JSON in the following format:\\n" "{json\_example}" ), ), ChatMessage( role="user", content=( "Here is the transcript: \\n" "------\\n" "{transcript}\\n" "------" ), ), \] ) dict\_example = { "summary": "High-level summary of the call transcript. Should not exceed 3 sentences.", "products": \["product 1", "product 2"\], "rep\_name": "Name of the sales rep", "prospect\_name": "Name of the prospect", "action\_items": \["action item 1", "action item 2"\], } json\_example = json.dumps(dict\_example)

In \[ \]:

Copied!

messages \= prompt.format\_messages(
    json\_example\=json\_example, transcript\=transcript
)

messages = prompt.format\_messages( json\_example=json\_example, transcript=transcript )

In \[ \]:

Copied!

output \= llm.chat(
    messages, response\_format\={"type": "json\_object"}
).message.content

output = llm.chat( messages, response\_format={"type": "json\_object"} ).message.content

Now we are able to get the extracted structured data as we expected.

In \[ \]:

Copied!

print(output)

print(output)

{
  "summary": "Sarah from XYZ Company called John to discuss the new product, the XYZ Widget, which is designed to streamline workflow and improve productivity. They discussed case studies and scheduling a demo for John and his team. The next steps include Sarah sending over information and following up to schedule the demo.",
  "products": \["XYZ Widget"\],
  "rep\_name": "Sarah",
  "prospect\_name": "John",
  "action\_items": \["Review case studies", "Schedule demo"\]
}

### Quick Takeaways[¶](https://docs.llamaindex.ai/en/stable/examples/llm/openai_json_vs_function_calling/#quick-takeaways)

*   Function calling remains easier to use for structured data extraction (especially if you have already specified your schema as e.g. a pydantic model)
*   While JSON mode enforces the format of the output, it does not help with validation against a specified schema. Directly passing in a schema may not generate expected JSON and may require additional careful formatting and prompting.

Back to top

[Previous OpenAI](https://docs.llamaindex.ai/en/stable/examples/llm/openai/)[Next OpenLLM](https://docs.llamaindex.ai/en/stable/examples/llm/openllm/)

Hi, how can I help you?

🦙
