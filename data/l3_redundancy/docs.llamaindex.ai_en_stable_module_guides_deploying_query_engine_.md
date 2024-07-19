Title: Query Engine - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/

Markdown Content:
Query Engine - LlamaIndex


Concept[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/#concept "Permanent link")
---------------------------------------------------------------------------------------------------------------

Query engine is a generic interface that allows you to ask question over your data.

A query engine takes in a natural language query, and returns a rich response. It is most often (but not always) built on one or many [indexes](https://docs.llamaindex.ai/en/stable/module_guides/indexing/) via [retrievers](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/). You can compose multiple query engines to achieve more advanced capability.

Tip

If you want to have a conversation with your data (multiple back-and-forth instead of a single question & answer), take a look at [Chat Engine](https://docs.llamaindex.ai/en/stable/module_guides/deploying/chat_engines/)

Usage Pattern[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/#usage-pattern "Permanent link")
---------------------------------------------------------------------------------------------------------------------------

Get started with:

```
query_engine = index.as_query_engine()
response = query_engine.query("Who is Paul Graham.")
```

To stream response:

```
query_engine = index.as_query_engine(streaming=True)
streaming_response = query_engine.query("Who is Paul Graham.")
streaming_response.print_response_stream()
```

See the full [usage pattern](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/usage_pattern/) for more details.

Modules[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/#modules "Permanent link")
---------------------------------------------------------------------------------------------------------------

Find all the modules in the [modules guide](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/modules/).

Supporting Modules[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/#supporting-modules "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------

There are also [supporting modules](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/supporting_modules/).

Back to top

[Previous Querying](https://docs.llamaindex.ai/en/stable/module_guides/querying/)[Next Usage Pattern](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/usage_pattern/)
