Title: Usage Pattern - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/usage_pattern/

Markdown Content:
Usage Pattern - LlamaIndex


Get Started[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/usage_pattern/#get-started "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------

Build a query engine from index:

```
query_engine = index.as_query_engine()
```

Tip

To learn how to build an index, see [Indexing](https://docs.llamaindex.ai/en/stable/module_guides/indexing/)

Ask a question over your data

```
response = query_engine.query("Who is Paul Graham?")
```

Configuring a Query Engine[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/usage_pattern/#configuring-a-query-engine "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

### High-Level API[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/usage_pattern/#high-level-api "Permanent link")

You can directly build and configure a query engine from an index in 1 line of code:

```
query_engine = index.as_query_engine(
    response_mode="tree_summarize",
    verbose=True,
)
```

> Note: While the high-level API optimizes for ease-of-use, it does _NOT_ expose full range of configurability.

See [**Response Modes**](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/response_modes/) for a full list of response modes and what they do.

### Low-Level Composition API[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/usage_pattern/#low-level-composition-api "Permanent link")

You can use the low-level composition API if you need more granular control. Concretely speaking, you would explicitly construct a `QueryEngine` object instead of calling `index.as_query_engine(...)`.

> Note: You may need to look at API references or example notebooks.

```
from llama_index.core import VectorStoreIndex, get_response_synthesizer
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine

# build index
index = VectorStoreIndex.from_documents(documents)

# configure retriever
retriever = VectorIndexRetriever(
    index=index,
    similarity_top_k=2,
)

# configure response synthesizer
response_synthesizer = get_response_synthesizer(
    response_mode="tree_summarize",
)

# assemble query engine
query_engine = RetrieverQueryEngine(
    retriever=retriever,
    response_synthesizer=response_synthesizer,
)

# query
response = query_engine.query("What did the author do growing up?")
print(response)
```

### Streaming[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/usage_pattern/#streaming "Permanent link")

To enable streaming, you simply need to pass in a `streaming=True` flag

```
query_engine = index.as_query_engine(
    streaming=True,
)
streaming_response = query_engine.query(
    "What did the author do growing up?",
)
streaming_response.print_response_stream()
```

*   Read the full [streaming guide](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/streaming/)
*   See an [end-to-end example](https://docs.llamaindex.ai/en/stable/examples/customization/streaming/SimpleIndexDemo-streaming/)

Defining a Custom Query Engine[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/usage_pattern/#defining-a-custom-query-engine "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can also define a custom query engine. Simply subclass the `CustomQueryEngine` class, define any attributes you'd want to have (similar to defining a Pydantic class), and implement a `custom_query` function that returns either a `Response` object or a string.

```
from llama_index.core.query_engine import CustomQueryEngine
from llama_index.core.retrievers import BaseRetriever
from llama_index.core import get_response_synthesizer
from llama_index.core.response_synthesizers import BaseSynthesizer

class RAGQueryEngine(CustomQueryEngine):
"""RAG Query Engine."""

    retriever: BaseRetriever
    response_synthesizer: BaseSynthesizer

    def custom_query(self, query_str: str):
        nodes = self.retriever.retrieve(query_str)
        response_obj = self.response_synthesizer.synthesize(query_str, nodes)
        return response_obj
```

See the [Custom Query Engine guide](https://docs.llamaindex.ai/en/stable/examples/query_engine/custom_query_engine/) for more details.

Back to top

[Previous Query Engine](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/)[Next Response Modes](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/response_modes/)
