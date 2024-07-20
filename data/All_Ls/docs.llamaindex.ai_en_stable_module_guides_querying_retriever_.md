Title: Retriever - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/

Markdown Content:
Retriever - LlamaIndex


Concept[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/#concept "Permanent link")
-----------------------------------------------------------------------------------------------------------

Retrievers are responsible for fetching the most relevant context given a user query (or chat message).

It can be built on top of [indexes](https://docs.llamaindex.ai/en/stable/module_guides/indexing/), but can also be defined independently. It is used as a key building block in [query engines](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/) (and [Chat Engines](https://docs.llamaindex.ai/en/stable/module_guides/deploying/chat_engines/)) for retrieving relevant context.

Tip

Confused about where retriever fits in the pipeline? Read about [high-level concepts](https://docs.llamaindex.ai/en/stable/getting_started/concepts/)

Usage Pattern[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/#usage-pattern "Permanent link")
-----------------------------------------------------------------------------------------------------------------------

Get started with:

```
retriever = index.as_retriever()
nodes = retriever.retrieve("Who is Paul Graham?")
```

Get Started[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/#get-started "Permanent link")
-------------------------------------------------------------------------------------------------------------------

Get a retriever from index:

```
retriever = index.as_retriever()
```

Retrieve relevant context for a question:

```
nodes = retriever.retrieve("Who is Paul Graham?")
```

> Note: To learn how to build an index, see [Indexing](https://docs.llamaindex.ai/en/stable/module_guides/indexing/)

High-Level API[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/#high-level-api "Permanent link")
-------------------------------------------------------------------------------------------------------------------------

### Selecting a Retriever[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/#selecting-a-retriever "Permanent link")

You can select the index-specific retriever class via `retriever_mode`. For example, with a `SummaryIndex`:

```
retriever = summary_index.as_retriever(
    retriever_mode="llm",
)
```

This creates a [SummaryIndexLLMRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/summary/) on top of the summary index.

See [**Retriever Modes**](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retriever_modes/) for a full list of (index-specific) retriever modes and the retriever classes they map to.

### Configuring a Retriever[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/#configuring-a-retriever "Permanent link")

In the same way, you can pass kwargs to configure the selected retriever.

> Note: take a look at the API reference for the selected retriever class' constructor parameters for a list of valid kwargs.

For example, if we selected the "llm" retriever mode, we might do the following:

```
retriever = summary_index.as_retriever(
    retriever_mode="llm",
    choice_batch_size=5,
)
```

Low-Level Composition API[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/#low-level-composition-api "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------

You can use the low-level composition API if you need more granular control.

To achieve the same outcome as above, you can directly import and construct the desired retriever class:

```
from llama_index.core.retrievers import SummaryIndexLLMRetriever

retriever = SummaryIndexLLMRetriever(
    index=summary_index,
    choice_batch_size=5,
)
```

Examples[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/#examples "Permanent link")
-------------------------------------------------------------------------------------------------------------

See more examples in the [retrievers guide](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retrievers/).

Back to top

[Previous Module Guides](https://docs.llamaindex.ai/en/stable/module_guides/deploying/chat_engines/modules/)[Next Retriever Modules](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retrievers/)
