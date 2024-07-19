Title: Usage Pattern - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/usage_pattern/

Markdown Content:
Usage Pattern - LlamaIndex


Get Started[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/usage_pattern/#get-started "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------

Each data loader contains a "Usage" section showing how that loader can be used. At the core of using each loader is a `download_loader` function, which downloads the loader file into a module that you can use within your application.

Example usage:

```
from llama_index.core import VectorStoreIndex, download_loader

from llama_index.readers.google import GoogleDocsReader

gdoc_ids = ["1wf-y2pd9C878Oh-FmLH7Q_BQkljdm6TQal-c1pUfrec"]
loader = GoogleDocsReader()
documents = loader.load_data(document_ids=gdoc_ids)
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
query_engine.query("Where did the author go to school?")
```

Back to top

[Previous Data Connectors (LlamaHub)](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/)[Next LlamaParse](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/llama_parse/)
