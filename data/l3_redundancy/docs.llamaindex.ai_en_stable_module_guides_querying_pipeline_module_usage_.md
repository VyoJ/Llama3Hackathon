Title: Module Usage - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/module_usage/

Markdown Content:
Module Usage - LlamaIndex


Currently the following LlamaIndex modules are supported within a QueryPipeline. Remember, you can define your own!

### LLMs (both completion and chat)[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/module_usage/#llms-both-completion-and-chat "Permanent link")

*   Base class: `LLM`
*   [Module Guide](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/)
*   If chat model:
*   Input: `messages`. Takes in any `List[ChatMessage]` or any stringable input.
*   Output: `output`. Outputs `ChatResponse` (stringable)
*   If completion model:
*   Input: `prompt`. Takes in any stringable input.
*   Output: `output`. Outputs `CompletionResponse` (stringable)

### Prompts[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/module_usage/#prompts "Permanent link")

*   Base class: `PromptTemplate`
*   [Module Guide](https://docs.llamaindex.ai/en/stable/module_guides/models/prompts/)
*   Input: Prompt template variables. Each variable can be a stringable input.
*   Output: `output`. Outputs formatted prompt string (stringable)

### Query Engines[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/module_usage/#query-engines "Permanent link")

*   Base class: `BaseQueryEngine`
*   [Module Guide](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/)
*   Input: `input`. Takes in any stringable input.
*   Output: `output`. Outputs `Response` (stringable)

### Query Transforms[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/module_usage/#query-transforms "Permanent link")

*   Base class: `BaseQueryTransform`
*   [Module Guide](https://docs.llamaindex.ai/en/stable/optimizing/advanced_retrieval/query_transformations/)
*   Input: `query_str`, `metadata` (optional). `query_str` is any stringable input.
*   Output: `query_str`. Outputs string.

### Retrievers[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/module_usage/#retrievers "Permanent link")

*   Base class: `BaseRetriever`
*   [Module Guide](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/)
*   Input: `input`. Takes in any stringable input.
*   Output: `output`. Outputs list of nodes `List[BaseNode]`.

### Output Parsers[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/module_usage/#output-parsers "Permanent link")

*   Base class: `BaseOutputParser`
*   [Module Guide](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/output_parser/)
*   Input: `input`. Takes in any stringable input.
*   Output: `output`. Outputs whatever type output parser is supposed to parse out.

### Postprocessors/Rerankers[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/module_usage/#postprocessorsrerankers "Permanent link")

*   Base class: `BaseNodePostprocessor`
*   [Module Guide](https://docs.llamaindex.ai/en/stable/module_guides/querying/node_postprocessors/)
*   Input: `nodes`, `query_str` (optional). `nodes` is `List[BaseNode]`, `query_str` is any stringable input.
*   Output: `nodes`. Outputs list of nodes `List[BaseNode]`.

### Response Synthesizers[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/module_usage/#response-synthesizers "Permanent link")

*   Base class: `BaseSynthesizer`
*   Module Guide
*   Input: `nodes`, `query_str`. `nodes` is `List[BaseNode]`, `query_str` is any stringable input.
*   Output: `output`. Outputs `Response` object (stringable).

### Other QueryPipeline objects[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/module_usage/#other-querypipeline-objects "Permanent link")

You can define a `QueryPipeline` as a module within another query pipeline. This makes it easy for you to string together complex workflows.

### Custom Components[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/module_usage/#custom-components "Permanent link")

See our [custom components guide](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/usage_pattern/#defining-a-custom-query-component) for more details.

Back to top

[Previous Module Guides](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/modules/)[Next Structured Outputs](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/)
