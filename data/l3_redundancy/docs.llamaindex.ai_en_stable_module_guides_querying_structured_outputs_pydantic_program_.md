Title: Pydantic Program - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/pydantic_program/

Markdown Content:
Pydantic Program - LlamaIndex


A pydantic program is a generic abstraction that takes in an input string and converts it to a structured Pydantic object type.

Because this abstraction is so generic, it encompasses a broad range of LLM workflows. The programs are composable and be for more generic or specific use cases.

There's a few general types of Pydantic Programs:

*   **Text Completion Pydantic Programs**: These convert input text into a user-specified structured object through a text completion API + output parsing.
*   **Function Calling Pydantic Program**: These convert input text into a user-specified structured object through an LLM function calling API.
*   **Prepackaged Pydantic Programs**: These convert input text into prespecified structured objects.

Text Completion Pydantic Programs[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/pydantic_program/#text-completion-pydantic-programs "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

See the example notebook on [LLM Text Completion programs](https://docs.llamaindex.ai/en/stable/examples/output_parsing/llm_program/)

Function Calling Pydantic Programs[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/pydantic_program/#function-calling-pydantic-programs "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   [Function Calling Pydantic Program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/function_program/)
*   [OpenAI Pydantic Program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/openai_pydantic_program/)
*   [Guidance Pydantic Program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/guidance_pydantic_program/)
*   [Guidance Sub-Question Generator](https://docs.llamaindex.ai/en/stable/examples/output_parsing/guidance_sub_question/)

Prepackaged Pydantic Programs[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/pydantic_program/#prepackaged-pydantic-programs "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   [DF Program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/df_program/)
*   [Evaporate Program](https://docs.llamaindex.ai/en/stable/examples/output_parsing/evaporate_program/)

Back to top

[Previous Query Engines + Pydantic Outputs](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/query_engine/)[Next Agents](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/)
