Title: Key-Value Stores - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/module_guides/storing/kv_stores/

Markdown Content:
Key-Value Stores - LlamaIndex


Key-Value stores are the underlying storage abstractions that power our [Document Stores](https://docs.llamaindex.ai/en/stable/module_guides/storing/docstores/) and [Index Stores](https://docs.llamaindex.ai/en/stable/module_guides/storing/index_stores/).

We provide the following key-value stores:

*   **Simple Key-Value Store**: An in-memory KV store. The user can choose to call `persist` on this kv store to persist data to disk.
*   **MongoDB Key-Value Store**: A MongoDB KV store.

See the [API Reference](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/) for more details.

Note: At the moment, these storage abstractions are not externally facing.

Back to top

[Previous Chat Stores](https://docs.llamaindex.ai/en/stable/module_guides/storing/chat_stores/)[Next Persisting & Loading Data](https://docs.llamaindex.ai/en/stable/module_guides/storing/save_load/)
