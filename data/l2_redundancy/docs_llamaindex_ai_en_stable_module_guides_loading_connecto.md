Title: Data Connectors (LlamaHub) - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/

Markdown Content:
Data Connectors (LlamaHub) - LlamaIndex


Concept[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/#concept "Permanent link")
----------------------------------------------------------------------------------------------------------

A data connector (aka `Reader`) ingest data from different data sources and data formats into a simple `Document` representation (text and simple metadata).

Tip

Once you've ingested your data, you can build an [Index](https://docs.llamaindex.ai/en/stable/module_guides/indexing/) on top, ask questions using a [Query Engine](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/), and have a conversation using a [Chat Engine](https://docs.llamaindex.ai/en/stable/module_guides/deploying/chat_engines/).

LlamaHub[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/#llamahub "Permanent link")
------------------------------------------------------------------------------------------------------------

Our data connectors are offered through [LlamaHub](https://llamahub.ai/) 🦙. LlamaHub is an open-source repository containing data loaders that you can easily plug and play into any LlamaIndex application.

![Image 3](https://docs.llamaindex.ai/en/stable/_static/data_connectors/llamahub.png)

Usage Pattern[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/#usage-pattern "Permanent link")
----------------------------------------------------------------------------------------------------------------------

Get started with:

```
from llama_index.core import download_loader

from llama_index.readers.google import GoogleDocsReader

loader = GoogleDocsReader()
documents = loader.load_data(document_ids=[...])
```

See the full [usage pattern guide](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/usage_pattern/) for more details.

Modules[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/#modules "Permanent link")
----------------------------------------------------------------------------------------------------------

Some sample data connectors:

*   local file directory (`SimpleDirectoryReader`). Can support parsing a wide range of file types: `.pdf`, `.jpg`, `.png`, `.docx`, etc.
*   [Notion](https://developers.notion.com/) (`NotionPageReader`)
*   [Google Docs](https://developers.google.com/docs/api) (`GoogleDocsReader`)
*   [Slack](https://api.slack.com/) (`SlackReader`)
*   [Discord](https://discord.com/developers/docs/intro) (`DiscordReader`)
*   [Apify Actors](https://llamahub.ai/l/apify-actor) (`ApifyActor`). Can crawl the web, scrape webpages, extract text content, download files including `.pdf`, `.jpg`, `.png`, `.docx`, etc.

See the [modules guide](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/modules/) for more details.

Back to top

[Previous SimpleDirectoryReader](https://docs.llamaindex.ai/en/stable/module_guides/loading/simpledirectoryreader/)[Next Usage Pattern](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/usage_pattern/)
