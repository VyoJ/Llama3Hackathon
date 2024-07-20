Title: Web Page Reader - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/

Markdown Content:
Web Page Reader - LlamaIndex


Demonstrates our web page reader.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index llama\-index\-readers\-web

%pip install llama-index llama-index-readers-web

In \[ \]:

Copied!

import logging
import sys

logging.basicConfig(stream\=sys.stdout, level\=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream\=sys.stdout))

import logging import sys logging.basicConfig(stream=sys.stdout, level=logging.INFO) logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

#### Using SimpleWebPageReader[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/#using-simplewebpagereader)

In \[ \]:

Copied!

from llama\_index.core import SummaryIndex
from llama\_index.readers.web import SimpleWebPageReader
from IPython.display import Markdown, display
import os

from llama\_index.core import SummaryIndex from llama\_index.readers.web import SimpleWebPageReader from IPython.display import Markdown, display import os

In \[ \]:

Copied!

\# NOTE: the html\_to\_text=True option requires html2text to be installed

\# NOTE: the html\_to\_text=True option requires html2text to be installed

In \[ \]:

Copied!

documents \= SimpleWebPageReader(html\_to\_text\=True).load\_data(
    \["http://paulgraham.com/worked.html"\]
)

documents = SimpleWebPageReader(html\_to\_text=True).load\_data( \["http://paulgraham.com/worked.html"\] )

In \[ \]:

Copied!

documents\[0\]

documents\[0\]

In \[ \]:

Copied!

index \= SummaryIndex.from\_documents(documents)

index = SummaryIndex.from\_documents(documents)

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did the author do growing up?")

\# set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine() response = query\_engine.query("What did the author do growing up?")

In \[ \]:

Copied!

display(Markdown(f"<b>{response}</b>"))

display(Markdown(f"**{response}**"))

Using Spider Reader 🕷[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/#using-spider-reader)
View Demo\* Basic\* StreamingExample requestPythonCopy\`\`\`import requests, osheaders = {    \\'Authorization\\': os.environ\["SPIDER\_API\_KEY"\],    \\'Content-Type\\': \\'application/json\\',}json\_data = {"limit":50,"url":"http://www.example.com"}response = requests.post(\\'https://api.spider.cloud/crawl\\',  headers=headers,  json=json\_data)print(response.json())\`\`\`Example ResponseUnmatched Speed----------### 5secs  ###To crawl 200 pages### 21x  ###Faster than FireCrawl### 150x  ###Faster than Apify Benchmarks displaying performance between Spider Cloud, Firecrawl, and Apify.\[See framework benchmarks \](https://github.com/spider-rs/spider/blob/main/benches/BENCHMARKS.md)Foundations for Crawling Effectively----------### Leading in performance ###Spider is written in Rust and runs in full concurrency to achieve crawling dozens of pages in secs.### Optimal response format ###Get clean and formatted markdown, HTML, or text content for fine-tuning or training AI models.### Caching ###Further boost speed by caching repeated web page crawls.### Smart Mode ###Spider dynamically switches to Headless Chrome when it needs to.Beta### Scrape with AI ###Do custom browser scripting and data extraction using the latest AI models.### Best crawler for LLMs ###Don\\'t let crawling and scraping be the highest latency in your LLM & AI agent stack.### Scrape with no headaches ###\* Proxy rotations\* Agent headers\* Avoid anti-bot detections\* Headless chrome\* Markdown LLM Responses### The Fastest Web Crawler ###\* Powered by \[spider-rs\](https://github.com/spider-rs/spider)\* Do 20,000 pages in seconds\* Full concurrency\* Powerful and simple API\* 5,000 requests per minute### Do more with AI ###\* Custom browser scripting\* Advanced data extraction\* Data pipelines\* Perfect for LLM and AI Agents\* Accurate website labeling\[API\](/docs/api) \[Pricing\](/credits/new) \[Guides\](/guides) \[About\](/about) \[Docs\](https://docs.rs/spider/latest/spider/) \[Privacy\](/privacy) \[Terms\](/eula)© 2024 Spider from A11yWatchTheme Light Dark Toggle Theme \[GitHubGithub\](https://github.com/spider-rs/spider)', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n')\]

Crawl domain following all deeper subpages

In \[ \]:

Copied!

\# Crawl domain with deeper crawling following subpages
from llama\_index.readers.web import SpiderWebReader

spider\_reader \= SpiderWebReader(
    api\_key\="YOUR\_API\_KEY",
    mode\="crawl",
    \# params={} # Optional parameters see more on https://spider.cloud/docs/api
)

documents \= spider\_reader.load\_data(url\="https://spider.cloud")
print(documents)

\# Crawl domain with deeper crawling following subpages from llama\_index.readers.web import SpiderWebReader spider\_reader = SpiderWebReader( api\_key="YOUR\_API\_KEY", mode="crawl", # params={} # Optional parameters see more on https://spider.cloud/docs/api ) documents = spider\_reader.load\_data(url="https://spider.cloud") print(documents)

\[Document(id\_='63f7ccbf-c6c8-4f69-80f7-f6763f761a39', embedding=None, metadata={'description': 'Our privacy policy and how it plays a part in the data collected.', 'domain': 'spider.cloud', 'extracted\_data': None, 'file\_size': 26647, 'keywords': None, 'pathname': '/privacy', 'resource\_type': 'html', 'title': 'Privacy', 'url': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48/spider.cloud/privacy.html', 'user\_id': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text="Privacy\[Spider v1 Logo Spider \](/) \[Credits\](/credits/new)\[GitHubGithub637\](https://github.com/spider-rs/spider)Privacy PolicyLearn how to crawl and scrape websites easily.(4) Total Guides\* \[  Spider v1 Logo  Spider Platform  ----------  How to use the platform to collect data from the internet fast, affordable, and unblockable.  \](/guides/spider)\* \[  Spider v1 Logo  Spider API  ----------  How to use the Spider API to curate data from any source blazing fast. The most advanced crawler that handles all workloads of all sizes.  \](/guides/spider-api)\* \[  Spider v1 Logo  Extract Contacts  ----------  Get contact information from any website in real time with AI. The only way to accurately get dynamic information from websites.  \](/guides/pipelines-extract-contacts)\* \[  Spider v1 Logo  Website Archiving  ----------  The programmable time machine that can store pages and all assets for easy website archiving.  \](/guides/website-archiving)\[API\](/docs/api) \[Pricing\](/credits/new) \[Guides\](/guides) \[About\](/about) \[Docs\](https://docs.rs/spider/latest/spider/) \[Privacy\](/privacy) \[Terms\](/eula)© 2024 Spider from A11yWatchTheme Light Dark Toggle Theme \[GitHubGithub\](https://github.com/spider-rs/spider)', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), Document(id\_='b10c6402-bc35-4fec-b97c-fa30bde54ce8', embedding=None, metadata={'description': 'Complete reference documentation for the Spider API. Includes code snippets and examples for quickly getting started with the system.', 'domain': 'spider.cloud', 'extracted\_data': None, 'file\_size': 195426, 'keywords': None, 'pathname': '/docs/api', 'resource\_type': 'html', 'title': 'Spider API Reference', 'url': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48/spider.cloud/docs\*\_\*api.html', 'user\_id': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='Spider API Reference\[Spider v1 Logo Spider \](/) \[Credits\](/credits/new)\[GitHubGithub637\](https://github.com/spider-rs/spider)API ReferenceStart crawling a website(s) to collect resources.POST https://api.spider.cloud/crawlRequest body\* url\\xa0required\\xa0string  ----------  The URI resource to crawl. This can be a comma split list for multiple urls.  Test Url\* request\\xa0string  ----------  The request type to perform. Possible values are \`http\`, \`chrome\`, and \`smart\`. Use \`smart\` to perform HTTP request by default until JavaScript rendering is needed for the HTML.  HTTP\* limit\\xa0number  ----------  The maximum amount of pages allowed to crawl per website. Remove the value or set it to 0 to crawl all pages.  Crawl Limit\* depth\\xa0number  ----------  The crawl limit for maximum depth. If zero, no limit will be applied.  Crawl DepthSet Example\* cache\\xa0boolean  ----------  Use HTTP caching for the crawl to speed up repeated runs.  Set Example\* budget\\xa0object  ----------  Object that has paths with a counter for limiting the amount of pages example \`{"\*":1}\` for only crawling the root page. The wildcard matches all routes and you can set child paths preventing a depth level, example of limiting \`{ "/docs/colors": 10, "/docs/": 100 }\` which only allows a max of 100 pages if the route matches \`/docs/:pathname\` and only 10 pages if it matches \`/docs/colors/:pathname\`.  Crawl Budget  Set Example\* locale\\xa0string  ----------  The locale to use for request, example \`en-US\`.  Set Example\* cookies\\xa0string  ----------  Add HTTP cookies to use for request.  Set Example\* stealth\\xa0boolean  ----------  Use stealth mode for headless chrome request to help prevent being blocked. The default is enabled on chrome.  Set Example\* headers\\xa0string  ----------  Forward HTTP headers to use for all request. The object is expected to be a map of key value pairs.  Set Example\* metadata\\xa0boolean  ----------  Boolean to store metadata about the pages and content found. This could help improve AI interopt. Defaults to false unless you have the website already stored with the configuration enabled.  Set Example\* viewport\\xa0object  ----------  Configure the viewport for chrome. Defaults to 800x600.  Set Example\* encoding\\xa0string  ----------  The type of encoding to use like \`UTF-8\`, \`SHIFT\_JIS\`, or etc.  Set Example\* subdomains\\xa0boolean  ----------  Allow subdomains to be included.  Set Example\* user\\\\\_agent\\xa0string  ----------  Add a custom HTTP user agent to the request.  Set Example\* store\\\\\_data\\xa0boolean  ----------  Boolean to determine if storage should be used. If set this takes precedence over \`storageless\`. Defaults to false.  Set Example\* gpt\\\\\_config\\xa0object  ----------  Use AI to generate actions to perform during the crawl. You can pass an array for the\`"prompt"\` to chain steps.  Set Example\* fingerprint\\xa0boolean  ----------  Use advanced fingerprint for chrome.  Set Example\* storageless\\xa0boolean  ----------  Boolean to prevent storing any type of data for the request including storage and AI vectors embedding. Defaults to false unless you have the website already stored.  Set Example\* readability\\xa0boolean  ----------  Use \[readability\](https://github.com/mozilla/readability) to pre-process the content for reading. This may drastically improve the content for LLM usage.  Set Example\* return\\\\\_format\\xa0string  ----------  The format to return the data in. Possible values are \`markdown\`, \`raw\`, \`text\`, and \`html2text\`. Use \`raw\` to return the default format of the page like \`HTML\` etc.  Raw\* proxy\\\\\_enabled\\xa0boolean  ----------  Enable high performance premium proxies for the request to prevent being blocked at the network level.  Set Example\* query\\\\\_selector\\xa0string  ----------  The CSS query selector to use when extracting content from the markup.  Test Query Selector\* full\\\\\_resources\\xa0boolean  ----------  Crawl and download all the resources for a website.  Set Example\* request\\\\\_timeout\\xa0number  ----------  The timeout to use for request. Timeouts can be from 5-60. The default is 30 seconds.  Set Example\* run\\\\\_in\\\\\_background\\xa0boolean  ----------  Run the request in the background. Useful if storing data and wanting to trigger crawls to the dashboard. This has no effect if storageless is set.  Set ExampleShow More Properties\* Basic\* StreamingExample requestPythonCopy\`\`\`import requests, osheaders = {    \\'Authorization\\': os.environ\["SPIDER\_API\_KEY"\],    \\'Content-Type\\': \\'application/json\\',}json\_data = {"limit":50,"url":"http://www.example.com"}response = requests.post(\\'https://api.spider.cloud/crawl\\',  headers=headers,  json=json\_data)print(response.json())\`\`\`ResponseCopy\`\`\`\[  {    "content": "<html>...",    "error": null,    "status": 200,    "url": "http://www.example.com"  },  // more content...\]\`\`\`Crawl websites get linksStart taking screenshots of website(s) to collect images to base64 or binary.POST https://api.spider.cloud/screenshotRequest bodyGeneralSpecific\* url\\xa0required\\xa0string  ----------  The URI resource to crawl. This can be a comma split list for multiple urls.  Test Url\* request\\xa0string  ----------  The request type to perform. Possible values are \`http\`, \`chrome\`, and \`smart\`. Use \`smart\` to perform HTTP request by default until JavaScript rendering is needed for the HTML.  HTTP\* limit\\xa0number  ----------  The maximum amount of pages allowed to crawl per website. Remove the value or set it to 0 to crawl all pages.  Crawl Limit\* depth\\xa0number  ----------  The crawl limit for maximum depth. If zero, no limit will be applied.  Crawl DepthSet Example\* cache\\xa0boolean  ----------  Use HTTP caching for the crawl to speed up repeated runs.  Set Example\* budget\\xa0object  ----------  Object that has paths with a counter for limiting the amount of pages example \`{"\*":1}\` for only crawling the root page. The wildcard matches all routes and you can set child paths preventing a depth level, example of limiting \`{ "/docs/colors": 10, "/docs/": 100 }\` which only allows a max of 100 pages if the route matches \`/docs/:pathname\` and only 10 pages if it matches \`/docs/colors/:pathname\`.  Crawl Budget  Set Example\* locale\\xa0string  ----------  The locale to use for request, example \`en-US\`.  Set Example\* cookies\\xa0string  ----------  Add HTTP cookies to use for request.  Set Example\* stealth\\xa0boolean  ----------  Use stealth mode for headless chrome request to help prevent being blocked. The default is enabled on chrome.  Set Example\* headers\\xa0string  ----------  Forward HTTP headers to use for all request. The object is expected to be a map of key value pairs.  Set Example\* metadata\\xa0boolean  ----------  Boolean to store metadata about the pages and content found. This could help improve AI interopt. Defaults to false unless you have the website already stored with the configuration enabled.  Set Example\* viewport\\xa0object  ----------  Configure the viewport for chrome. Defaults to 800x600.  Set Example\* encoding\\xa0string  ----------  The type of encoding to use like \`UTF-8\`, \`SHIFT\_JIS\`, or etc.  Set Example\* subdomains\\xa0boolean  ----------  Allow subdomains to be included.  Set Example\* user\\\\\_agent\\xa0string  ----------  Add a custom HTTP user agent to the request.  Set Example\* store\\\\\_data\\xa0boolean  ----------  Boolean to determine if storage should be used. If set this takes precedence over \`storageless\`. Defaults to false.  Set Example\* gpt\\\\\_config\\xa0object  ----------  Use AI to generate actions to perform during the crawl. You can pass an array for the\`"prompt"\` to chain steps.  Set Example\* fingerprint\\xa0boolean  ----------  Use advanced fingerprint for chrome.  Set Example\* storageless\\xa0boolean  ----------  Boolean to prevent storing any type of data for the request including storage and AI vectors embedding. Defaults to false unless you have the website already stored.  Set Example\* readability\\xa0boolean  ----------  Use \[readability\](https://github.com/mozilla/readability) to pre-process the content for reading. This may drastically improve the content for LLM usage.  Set Example\* return\\\\\_format\\xa0string  ----------  The format to return the data in. Possible values are \`markdown\`, \`raw\`, \`text\`, and \`html2text\`. Use \`raw\` to return the default format of the page like \`HTML\` etc.  Raw\* proxy\\\\\_enabled\\xa0boolean  ----------  Enable high performance premium proxies for the request to prevent being blocked at the network level.  Set Example\* query\\\\\_selector\\xa0string  ----------  The CSS query selector to use when extracting content from the markup.  Test Query Selector\* full\\\\\_resources\\xa0boolean  ----------  Crawl and download all the resources for a website.  Set Example\* request\\\\\_timeout\\xa0number  ----------  The timeout to use for request. Timeouts can be from 5-60. The default is 30 seconds.  Set Example\* run\\\\\_in\\\\\_background\\xa0boolean  ----------  Run the request in the background. Useful if storing data and wanting to trigger crawls to the dashboard. This has no effect if storageless is set.  Set ExampleShow More Properties\* Basic\* StreamingExample requestPythonCopy\`\`\`import requests, osheaders = {    \\'Authorization\\': os.environ\["SPIDER\_API\_KEY"\],    \\'Content-Type\\': \\'application/json\\',}json\_data = {"limit":50,"url":"http://www.example.com"}response = requests.post(\\'https://api.spider.cloud/screenshot\\',  headers=headers,  json=json\_data)print(response.json())\`\`\`ResponseCopy\`\`\`\[  {    "content": "base64...",    "error": null,    "status": 200,    "url": "http://www.example.com"  },  // more content...\]\`\`\`Pipelines----------Create powerful workflows with our pipeline API endpoints. Use AI to extract contacts from any website or filter links with prompts with ease.Crawl websites and extract contactsCrawl a website and accurately categorize it using AI.POST https://api.spider.cloud/pipeline/labelRequest bodyGeneralSpecific\* url\\xa0required\\xa0string  ----------  The URI resource to crawl. This can be a comma split list for multiple urls.  Test Url\* request\\xa0string  ----------  The request type to perform. Possible values are \`http\`, \`chrome\`, and \`smart\`. Use \`smart\` to perform HTTP request by default until JavaScript rendering is needed for the HTML.  HTTP\* limit\\xa0number  ----------  The maximum amount of pages allowed to crawl per website. Remove the value or set it to 0 to crawl all pages.  Crawl Limit\* depth\\xa0number  ----------  The crawl limit for maximum depth. If zero, no limit will be applied.  Crawl DepthSet Example\* cache\\xa0boolean  ----------  Use HTTP caching for the crawl to speed up repeated runs.  Set Example\* budget\\xa0object  ----------  Object that has paths with a counter for limiting the amount of pages example \`{"\*":1}\` for only crawling the root page. The wildcard matches all routes and you can set child paths preventing a depth level, example of limiting \`{ "/docs/colors": 10, "/docs/": 100 }\` which only allows a max of 100 pages if the route matches \`/docs/:pathname\` and only 10 pages if it matches \`/docs/colors/:pathname\`.  Crawl Budget  Set Example\* locale\\xa0string  ----------  The locale to use for request, example \`en-US\`.  Set Example\* cookies\\xa0string  ----------  Add HTTP cookies to use for request.  Set Example\* stealth\\xa0boolean  ----------  Use stealth mode for headless chrome request to help prevent being blocked. The default is enabled on chrome.  Set Example\* headers\\xa0string  ----------  Forward HTTP headers to use for all request. The object is expected to be a map of key value pairs.  Set Example\* metadata\\xa0boolean  ----------  Boolean to store metadata about the pages and content found. This could help improve AI interopt. Defaults to false unless you have the website already stored with the configuration enabled.  Set Example\* viewport\\xa0object  ----------  Configure the viewport for chrome. Defaults to 800x600.  Set Example\* encoding\\xa0string  ----------  The type of encoding to use like \`UTF-8\`, \`SHIFT\_JIS\`, or etc.  Set Example\* subdomains\\xa0boolean  ----------  Allow subdomains to be included.  Set Example\* user\\\\\_agent\\xa0string  ----------  Add a custom HTTP user agent to the request.  Set Example\* store\\\\\_data\\xa0boolean  ----------  Boolean to determine if storage should be used. If set this takes precedence over \`storageless\`. Defaults to false.  Set Example\* gpt\\\\\_config\\xa0object  ----------  Use AI to generate actions to perform during the crawl. You can pass an array for the\`"prompt"\` to chain steps.  Set Example\* fingerprint\\xa0boolean  ----------  Use advanced fingerprint for chrome.  Set Example\* storageless\\xa0boolean  ----------  Boolean to prevent storing any type of data for the request including storage and AI vectors embedding. Defaults to false unless you have the website already stored.  Set Example\* readability\\xa0boolean  ----------  Use \[readability\](https://github.com/mozilla/readability) to pre-process the content for reading. This may drastically improve the content for LLM usage.  Set Example\* return\\\\\_format\\xa0string  ----------  The format to return the data in. Possible values are \`markdown\`, \`raw\`, \`text\`, and \`html2text\`. Use \`raw\` to return the default format of the page like \`HTML\` etc.  Raw\* proxy\\\\\_enabled\\xa0boolean  ----------  Enable high performance premium proxies for the request to prevent being blocked at the network level.  Set Example\* query\\\\\_selector\\xa0string  ----------  The CSS query selector to use when extracting content from the markup.  Test Query Selector\* full\\\\\_resources\\xa0boolean  ----------  Crawl and download all the resources for a website.  Set Example\* request\\\\\_timeout\\xa0number  ----------  The timeout to use for request. Timeouts can be from 5-60. The default is 30 seconds.  Set Example\* run\\\\\_in\\\\\_background\\xa0boolean  ----------  Run the request in the background. Useful if storing data and wanting to trigger crawls to the dashboard. This has no effect if storageless is set.  Set ExampleShow More Properties\* Basic\* StreamingExample requestPythonCopy\`\`\`import requests, osheaders = {    \\'Authorization\\': os.environ\["SPIDER\_API\_KEY"\],    \\'Content-Type\\': \\'application/json\\',}json\_data = {"limit":50,"url":"http://www.example.com"}response = requests.post(\\'https://api.spider.cloud/pipeline/label\\',  headers=headers,  json=json\_data)print(response.json())\`\`\`ResponseCopy\`\`\`\[  {    "content": \["Government"\],    "error": null,    "status": 200,    "url": "http://www.example.com"  },  // more content...\]\`\`\`Crawl StateGet the remaining credits available.GET https://api.spider.cloud/credits\* Basic\* StreamingExample requestPythonCopy\`\`\`import requests, osheaders = {    \\'Authorization\\': os.environ\["SPIDER\_API\_KEY"\],    \\'Content-Type\\': \\'application/json\\',}response = requests.post(\\'https://api.spider.cloud/credits\\',  headers=headers)print(response.json())\`\`\`ResponseCopy\`\`\`{ "credits": 52566 }\`\`\`\[API\](/docs/api) \[Pricing\](/credits/new) \[Guides\](/guides) \[About\](/about) \[Docs\](https://docs.rs/spider/latest/spider/) \[Privacy\](/privacy) \[Terms\](/eula)© 2024 Spider from A11yWatchTheme Light Dark Toggle Theme \[GitHubGithub\](https://github.com/spider-rs/spider)', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), Document(id\_='44b350c3-f907-4767-84ec-a73fe59c190c', embedding=None, metadata={'description': 'End User License Agreement for the Spiderwebai and the spider project.', 'domain': 'spider.cloud', 'extracted\_data': None, 'file\_size': 20123, 'keywords': None, 'pathname': '/eula', 'resource\_type': 'html', 'title': 'EULA', 'url': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48/spider.cloud/eula.html', 'user\_id': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='EULA\[Spider v1 Logo Spider \](/) \[Credits\](/credits/new)\[GitHubGithub637\](https://github.com/spider-rs/spider)End User License AgreementSpider is the fastest web crawler written in Rust. The Cloud version is a hosted version of open-source project. Spider Features----------Our features that facilitate website scraping and provide swift insights in one platform. Deliver astonishing results using our powerful API.### Fast Unblockable Scraping ###When it comes to speed, the Spider project is the fastest web crawler available to the public. Utilize the foundation of open-source tools and make the most of your budget to scrape content effectively.Collecting Data Logo### Gain Website Insights with AI ###Enhance your crawls with AI to obtain relevant information fast from any website.AI Search### Extract Data Using Webhooks ###Set up webhooks across your websites to deliver the desired information anywhere you need.News Logo\[A11yWatch\](https://a11ywatch.com)maintains the project and the hosting for the service.\[API\](/docs/api) \[Pricing\](/credits/new) \[Guides\](/guides) \[About\](/about) \[Docs\](https://docs.rs/spider/latest/spider/) \[Privacy\](/privacy) \[Terms\](/eula)© 2024 Spider from A11yWatchTheme Light Dark Toggle Theme \[GitHubGithub\](https://github.com/spider-rs/spider)', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), Document(id\_='1a2d63a5-0315-4c5b-8fed-8ac460b82cc7', embedding=None, metadata={'description': 'Add the amount of credits you want to purchase for scraping the internet with AI and LLM data curation abilities fast.', 'domain': 'spider.cloud', 'extracted\_data': None, 'file\_size': 23083, 'keywords': None, 'pathname': '/credits/new', 'resource\_type': 'html', 'title': 'Purchase Spider Credits', 'url': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48/spider.cloud/credits\*\_\*new.html', 'user\_id': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='Purchase Spider Credits\[Spider v1 Logo Spider \](/) \[Credits\](/credits/new)\[GitHubGithub637\](https://github.com/spider-rs/spider)Add creditsView Demo\* Basic\* StreamingExample requestPythonCopy\`\`\`import requests, osheaders = {    \\'Authorization\\': os.environ\["SPIDER\_API\_KEY"\],    \\'Content-Type\\': \\'application/json\\',}json\_data = {"limit":50,"url":"http://www.example.com"}response = requests.post(\\'https://api.spider.cloud/crawl\\',  headers=headers,  json=json\_data)print(response.json())\`\`\`Example ResponseUnmatched Speed----------### 5secs  ###To crawl 200 pages### 21x  ###Faster than FireCrawl### 150x  ###Faster than Apify Benchmarks displaying performance between Spider Cloud, Firecrawl, and Apify.\[See framework benchmarks \](https://github.com/spider-rs/spider/blob/main/benches/BENCHMARKS.md)Foundations for Crawling Effectively----------### Leading in performance ###Spider is written in Rust and runs in full concurrency to achieve crawling dozens of pages in secs.### Optimal response format ###Get clean and formatted markdown, HTML, or text content for fine-tuning or training AI models.### Caching ###Further boost speed by caching repeated web page crawls.### Smart Mode ###Spider dynamically switches to Headless Chrome when it needs to.Beta### Scrape with AI ###Do custom browser scripting and data extraction using the latest AI models.### Best crawler for LLMs ###Don\\'t let crawling and scraping be the highest latency in your LLM & AI agent stack.### Scrape with no headaches ###\* Proxy rotations\* Agent headers\* Avoid anti-bot detections\* Headless chrome\* Markdown LLM Responses### The Fastest Web Crawler ###\* Powered by \[spider-rs\](https://github.com/spider-rs/spider)\* Do 20,000 pages in seconds\* Full concurrency\* Powerful and simple API\* 5,000 requests per minute### Do more with AI ###\* Custom browser scripting\* Advanced data extraction\* Data pipelines\* Perfect for LLM and AI Agents\* Accurate website labeling\[API\](/docs/api) \[Pricing\](/credits/new) \[Guides\](/guides) \[About\](/about) \[Docs\](https://docs.rs/spider/latest/spider/) \[Privacy\](/privacy) \[Terms\](/eula)© 2024 Spider from A11yWatchTheme Light Dark Toggle Theme \[GitHubGithub\](https://github.com/spider-rs/spider)', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), Document(id\_='91b98a80-7112-4837-8389-cb78221b254c', embedding=None, metadata={'description': 'Get contact information from any website in real time with AI. The only way to accurately get dynamic information from websites.', 'domain': 'spider.cloud', 'extracted\_data': None, 'file\_size': 25891, 'keywords': None, 'pathname': '/guides/pipelines-extract-contacts', 'resource\_type': 'html', 'title': 'Guides - Extract Contacts', 'url': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48/spider.cloud/guides\*\_\*pipelines-extract-contacts.html', 'user\_id': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='Guides - Extract Contacts\[Spider v1 Logo Spider \](/) \[Credits\](/credits/new)\[GitHubGithub637\](https://github.com/spider-rs/spider)Extract ContactsContents----------\* \[API built to scale\](#api-built-to-scale)\* \[API Usage\](#api-usage)\* \[Crawling One Page\](#crawling-one-page)\* \[Crawling Multiple Pages\](#crawling-multiple-pages)  \* \[Planet Scale Crawling\](#planet-scale-crawling)    \* \[Automatic Configuration\](#automatic-configuration)API built to scale----------Welcome to our cutting-edge web crawler SaaS, renowned for its unparalleled speed.Our platform is designed to effortlessly manage thousands of requests per second, thanks to our elastically scalable system architecture and the Open-Source \[spider\](https://github.com/spider-rs/spider) project. We deliver consistent latency times ensuring swift processing for all responses.For an in-depth understanding of the request parameters supported, we invite you to explore our comprehensive API documentation. At present, we do not provide client-side libraries, as our API has been crafted with simplicity in mind for straightforward usage. However, we are open to expanding our offerings in the future to enhance user convenience.Dive into our \[documentation\]((/docs/api)) to get started and unleash the full potential of our web crawler today.API Usage----------Getting started with the API is simple and straight forward. After you get your \[secret key\](/api-keys)you can access our instance directly. We have one main endpoint \`/crawl\` that handles all things relatedto data curation. The crawler is highly configurable through the params to fit all needs.Crawling One Page----------Most cases you probally just want to crawl one page. Even if you only need one page, our system performs fast enough to lead the race.The most straight forward way to make sure you only crawl a single page is to set the \[budget limit\](./account/settings) with a wild card value or \`\*\` to 1.You can also pass in the param \`limit\` in the JSON body with the limit of pages.Crawling Multiple Pages----------When you crawl multiple pages, the concurrency horsepower of the spider kicks in. You might wonder why and how one request may take (x)ms to come back, and 100 requests take about the same time! That’s because the built-in isolated concurrency allows for crawling thousands to millions of pages in no time. It’s the only current solution that can handle large websites with over 100k pages within a minute or two (sometimes even in a blink or two). By default, we do not add any limits to crawls unless specified.### Planet Scale Crawling ###If you plan on processing crawls that have over 200 pages, we recommend streaming the request from the client instead of parsing the entire payload once finished. We have an example of this with Python on the API docs page, also shown below.\`\`\`import requests, os, jsonheaders = {    \\'Authorization\\': os.environ\["SPIDER\_API\_KEY"\],    \\'Content-Type\\': \\'application/json\\',}json\_data = {"limit":250,"url":"http://www.example.com"}response = requests.post(\\'https://api.spider.cloud/crawl/crawl\\',  headers=headers,  json=json\_data,  stream=True)for line in response.iter\_lines():  if line:      print(json.loads(line))\`\`\`#### Automatic Configuration ####Spider handles automatic concurrency handling and ip rotation to make it simple to curate data.The more credits you have or usage available allows for a higher concurrency limit.Written on:  1/3/2024\[API\](/docs/api) \[Pricing\](/credits/new) \[Guides\](/guides) \[About\](/about) \[Docs\](https://docs.rs/spider/latest/spider/) \[Privacy\](/privacy) \[Terms\](/eula)© 2024 Spider from A11yWatchTheme Light Dark Toggle Theme \[GitHubGithub\](https://github.com/spider-rs/spider)', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), Document(id\_='08e5f1d6-4ae7-4b68-ab96-4b6a3768e88c', embedding=None, metadata={'description': 'The programmable time machine that can store pages and all assets for easy website archiving.', 'domain': 'spider.cloud', 'extracted\_data': None, 'file\_size': 18970, 'keywords': None, 'pathname': '/guides/website-archiving', 'resource\_type': 'html', 'title': 'Guides - Website Archiving', 'url': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48/spider.cloud/guides\*\_\*website-archiving.html', 'user\_id': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='Guides - Website Archiving\[Spider v1 Logo Spider \](/) \[Credits\](/credits/new)\[GitHubGithub637\](https://github.com/spider-rs/spider)Website ArchivingContents----------\* \[Data Curation\](#data-curation)  \* \[Crawling (Website)\](#crawling-website)  \* \[Crawling (API)\](#crawling-api)\* \[Crawl Configuration\](#crawl-configuration)  \* \[Proxies\](#proxies)  \* \[Headless Browser\](#headless-browser)  \* \[Crawl Budget Limits\](#crawl-budget-limits)\* \[Crawling and Scraping Websites\](#crawling-and-scraping-websites)  \* \[Transforming Data\](#transforming-data)    \* \[Leveraging Open Source\](#leveraging-open-source)\* \[Subscription and Spider Credits\](#subscription-and-spider-credits)Data Curation----------Collecting data with Spider can be fast and rewarding if done with some simple preliminary steps.Use the dashboard to collect data seamlessly across the internet with scheduled updates.You have two main ways of collecting data using Spider. The first and simplest is to use the UI available for scraping.The alternative is to use the API to programmatically access the system and perform actions.### Crawling (Website) ###1. Register or login to your account using email or Github.2. Purchase \[credits\](/credits/new) to kickstart crawls with \`pay-as-you-go\` go after credits deplete.3. Configure crawl \[settings\](/account/settings) to fit workflows that you need.4. Navigate to the \[dashboard\](/) and enter a website url or ask a question to get a url that should be crawled.5. Crawl the website and export/download the data as needed.### Crawling (API) ###1. Register or login to your account using email or Github.2. Purchase \[credits\](/credits/new) to kickstart crawls with \`pay-as-you-go\` after credits deplete.3. Configure crawl \[settings\](/account/settings) to fit workflows that you need.4. Navigate to \[API keys\](/api-keys) and create a new secret key.5. Go to the \[API docs\](/docs/api) page to see how the API works and perform crawls with code examples.Crawl Configuration----------Configuration your account for how you would like to crawl can help save costs or effectiveness of the content. Some of the configurations include setting Premium Proxies, Headless Browser Rendering, Webhooks, and Budgeting.### Proxies ###Using proxies with our system is straight forward. Simple check the toggle on if you want all request to use a proxy to increase the success of not being blocked.!\[Proxies example app screenshot.\](/img/app/proxy-setting.png)### Headless Browser ###If you want pages that require JavaScript to be executed the headless browser config is for you. Enabling will run all request through a real Chrome Browser for JavaScript required rendering pages.!\[Headless browser example app screenshot.\](/img/app/headless-browser.png)### Crawl Budget Limits ###One of the key things you may need to do before getting into the crawl is setting up crawl-budgets.Crawl budgets allows you to determine how many pages you are going to crawl for a website.Determining the budget will save you costs when dealing with large websites that you only want certain data points from. The example below shows adding a asterisk (\\\\\*) to determine all routes with a limit of 50 pages maximum. The settings can be overwritten by the website configuration or parameters if using the API.!\[Crawl budget example screenshot\](/img/app/edit-budget.png)Crawling and Scraping Websites----------Collecting data can be done in many ways and for many reasons. Leveraging our state-of-the-art technology allows you to create fast workloads that can process content from multiple locations. At the time of writing, we have started to focus on our data processing API instead of the dashboard. The API has much more flexibility than the UI for performing advanced workloads like batching, formatting, and so on.!\[Dashboard UI for Spider displaying data collecting from www.napster.com, jeffmendez.com, rsseau.rs, and www.drake.com\](/img/app/ui-crawl.png)### Transforming Data ###The API has more features for gathering the content in different formats and transforming the HTML as needed. You can transform the content from HTML to Markdown and feed it to a LLM for better handling the learning aspect. The API is the first class citizen for the application. The UI will have the features provided by the API eventually as the need arises.#### Leveraging Open Source ####One of the reasons Spider is the ultimate data-curation service for scraping is from the power of Open-Source. The core of the engine is completly available on \[Github\](https://github.com/spider-rs/spider) under \[MIT\](https://opensource.org/license/mit/) to show what is in store. We are constantly working on the crawler features including performance with plans to maintain the project for the long run.Subscription and Spider Credits----------The platform allows purchasing credits that gives you the ability to crawl at any time.When you purchase credits a crawl subscription is created that allows you to continue to usethe platform when your credits deplete. The limits provided coralate with the amount of creditspurchased, an example would be if you bought $5 in credits you would have about $40 in spending limit - $10 in credit gives $80 and so on.The highest purchase of credits directly determines how much is allowed on the platform. You can view your usage and credits on the \[usage limits page\](/account/usage).Written on:  1/2/2024\[API\](/docs/api) \[Pricing\](/credits/new) \[Guides\](/guides) \[About\](/about) \[Docs\](https://docs.rs/spider/latest/spider/) \[Privacy\](/privacy) \[Terms\](/eula)© 2024 Spider from A11yWatchTheme Light Dark Toggle Theme \[GitHubGithub\](https://github.com/spider-rs/spider)', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), Document(id\_='44bff527-c7f3-4346-a2f8-1454c52e1b01', embedding=None, metadata={'description': 'Generate API keys that allow access to the system programmatically anywhere. Full management access for your Spider API journey.', 'domain': 'spider.cloud', 'extracted\_data': None, 'file\_size': 28770, 'keywords': None, 'pathname': '/api-keys', 'resource\_type': 'html', 'title': 'API Keys Spider', 'url': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48/spider.cloud/api-keys.html', 'user\_id': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text="API Keys Spider\[Spider v1 Logo Spider \](/) \[Credits\](/credits/new)\[GitHubGithub637\](https://github.com/spider-rs/spider) API KeysBelow you'll find a summary of usage for your account. The data may be delayed up to 5 minutes.Credits----------###  Pay as you go  ######  Approved usage limit  ### The maximum usage Spider allows for your organization each month. Ask for increase.###  Set a monthly budget  ###When your organization reaches this usage threshold each month, subsequent requests will be rejected. Data may be deleted if payments are rejected.\[API\](/docs/api) \[Pricing\](/credits/new) \[Guides\](/guides) \[About\](/about) \[Docs\](https://docs.rs/spider/latest/spider/) \[Privacy\](/privacy) \[Terms\](/eula)© 2024 Spider from A11yWatchTheme Light Dark Toggle Theme \[GitHubGithub\](https://github.com/spider-rs/spider)", start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), Document(id\_='e3eb1e3c-5080-4590-94e8-fd2ef4f6d3c6', embedding=None, metadata={'description': 'Adjust your spider settings to adjust your crawl settings.', 'domain': 'spider.cloud', 'extracted\_data': None, 'file\_size': 18322, 'keywords': None, 'pathname': '/account/settings', 'resource\_type': 'html', 'title': 'Settings - Spider', 'url': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48/spider.cloud/account\*\_\*settings.html', 'user\_id': '48f1bc3c-3fbb-408a-865b-c191a1bb1f48'}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text='Settings - Spider\[Spider v1 Logo Spider \](/) \[Credits\](/credits/new)\[GitHubGithub637\](https://github.com/spider-rs/spider)\[API\](/docs/api) \[Pricing\](/credits/new) \[Guides\](/guides) \[About\](/about) \[Docs\](https://docs.rs/spider/latest/spider/) \[Privacy\](/privacy) \[Terms\](/eula)© 2024 Spider from A11yWatchTheme Light Dark Toggle Theme \[GitHubGithub\](https://github.com/spider-rs/spider)', start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n')\]

For guides and documentation, visit [Spider](https://spider.cloud/docs/api)

Using Browserbase Reader 🅱️[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/#using-browserbase-reader)


[Browserbase](https://browserbase.com/) is a serverless platform for running headless browsers, it offers advanced debugging, session recordings, stealth mode, integrated proxies and captcha solving.

Installation and Setup[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/#installation-and-setup)
----------------------------------------------------------------------------------------------------------------------------

*   Get an API key and Project ID from [browserbase.com](https://browserbase.com/) and set it in environment variables (`BROWSERBASE_API_KEY`, `BROWSERBASE_PROJECT_ID`).
*   Install the [Browserbase SDK](http://github.com/browserbase/python-sdk):

In \[ \]:

Copied!

% pip install browserbase

% pip install browserbase

In \[ \]:

Copied!

from llama\_index.readers.web import BrowserbaseWebReader

from llama\_index.readers.web import BrowserbaseWebReader

In \[ \]:

Copied!

reader \= BrowserbaseWebReader()
docs \= reader.load\_data(
    urls\=\[
        "https://example.com",
    \],
    \# Text mode
    text\_content\=False,
)

reader = BrowserbaseWebReader() docs = reader.load\_data( urls=\[ "https://example.com", \], # Text mode text\_content=False, )

### Using FireCrawl Reader 🔥[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/#using-firecrawl-reader)

Firecrawl is an api that turns entire websites into clean, LLM accessible markdown.

Using Firecrawl to gather an entire website

In \[ \]:

Copied!

from llama\_index.readers.web import FireCrawlWebReader

from llama\_index.readers.web import FireCrawlWebReader

In \[ \]:

Copied!

\# using firecrawl to crawl a website
firecrawl\_reader \= FireCrawlWebReader(
    api\_key\="<your\_api\_key>",  \# Replace with your actual API key from https://www.firecrawl.dev/
    mode\="scrape",  \# Choose between "crawl" and "scrape" for single page scraping
    params\={"additional": "parameters"},  \# Optional additional parameters
)

\# Load documents from a single page URL
documents \= firecrawl\_reader.load\_data(url\="http://paulgraham.com/")

\# using firecrawl to crawl a website firecrawl\_reader = FireCrawlWebReader( api\_key="", # Replace with your actual API key from https://www.firecrawl.dev/ mode="scrape", # Choose between "crawl" and "scrape" for single page scraping params={"additional": "parameters"}, # Optional additional parameters ) # Load documents from a single page URL documents = firecrawl\_reader.load\_data(url="http://paulgraham.com/")

In \[ \]:

Copied!

index \= SummaryIndex.from\_documents(documents)

index = SummaryIndex.from\_documents(documents)

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did the author do growing up?")

\# set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine() response = query\_engine.query("What did the author do growing up?")

In \[ \]:

Copied!

display(Markdown(f"<b>{response}</b>"))

display(Markdown(f"**{response}**"))

Using firecrawl for a single page

In \[ \]:

Copied!

\# Initialize the FireCrawlWebReader with your API key and desired mode
from llama\_index.readers.web.firecrawl\_web.base import FireCrawlWebReader

firecrawl\_reader \= FireCrawlWebReader(
    api\_key\="<your\_api\_key>",  \# Replace with your actual API key from https://www.firecrawl.dev/
    mode\="scrape",  \# Choose between "crawl" and "scrape" for single page scraping
    params\={"additional": "parameters"},  \# Optional additional parameters
)

\# Load documents from a single page URL
documents \= firecrawl\_reader.load\_data(url\="http://paulgraham.com/worked.html")

\# Initialize the FireCrawlWebReader with your API key and desired mode from llama\_index.readers.web.firecrawl\_web.base import FireCrawlWebReader firecrawl\_reader = FireCrawlWebReader( api\_key="", # Replace with your actual API key from https://www.firecrawl.dev/ mode="scrape", # Choose between "crawl" and "scrape" for single page scraping params={"additional": "parameters"}, # Optional additional parameters ) # Load documents from a single page URL documents = firecrawl\_reader.load\_data(url="http://paulgraham.com/worked.html")

Running cells with '/opt/homebrew/bin/python3' requires the ipykernel package.
Run the following command to install 'ipykernel' into the Python environment. 
Command: '/opt/homebrew/bin/python3 -m pip install ipykernel -U --user --force-reinstall'

In \[ \]:

Copied!

index \= SummaryIndex.from\_documents(documents)

index = SummaryIndex.from\_documents(documents)

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did the author do growing up?")

\# set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine() response = query\_engine.query("What did the author do growing up?")

In \[ \]:

Copied!

display(Markdown(f"<b>{response}</b>"))

display(Markdown(f"**{response}**"))

#### Using TrafilaturaWebReader[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/#using-trafilaturawebreader)

In \[ \]:

Copied!

from llama\_index.readers.web import TrafilaturaWebReader

from llama\_index.readers.web import TrafilaturaWebReader

\---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In\[7\], line 1
\----> 1 from llama\_index.readers.web import TrafilaturaWebReader

ModuleNotFoundError: No module named 'llama\_index.readers.web'

In \[ \]:

Copied!

documents \= TrafilaturaWebReader().load\_data(
    \["http://paulgraham.com/worked.html"\]
)

documents = TrafilaturaWebReader().load\_data( \["http://paulgraham.com/worked.html"\] )

In \[ \]:

Copied!

index \= SummaryIndex.from\_documents(documents)

index = SummaryIndex.from\_documents(documents)

In \[ \]:

Copied!

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What did the author do growing up?")

\# set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine() response = query\_engine.query("What did the author do growing up?")

In \[ \]:

Copied!

display(Markdown(f"<b>{response}</b>"))

display(Markdown(f"**{response}**"))

### Using RssReader[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/#using-rssreader)

In \[ \]:

Copied!

from llama\_index.core import SummaryIndex
from llama\_index.readers.web import RssReader

documents \= RssReader().load\_data(
    \["https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"\]
)

index \= SummaryIndex.from\_documents(documents)

\# set Logging to DEBUG for more detailed outputs
query\_engine \= index.as\_query\_engine()
response \= query\_engine.query("What happened in the news today?")

from llama\_index.core import SummaryIndex from llama\_index.readers.web import RssReader documents = RssReader().load\_data( \["https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"\] ) index = SummaryIndex.from\_documents(documents) # set Logging to DEBUG for more detailed outputs query\_engine = index.as\_query\_engine() response = query\_engine.query("What happened in the news today?")

Using ScrapFly[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/#using-scrapfly)
------------------------------------------------------------------------------------------------------------

ScrapFly is a web scraping API with headless browser capabilities, proxies, and anti-bot bypass. It allows for extracting web page data into accessible LLM markdown or text. Install ScrapFly Python SDK using pip:

pip install scrapfly-sdk

Here is a basic usage of ScrapflyReader

In \[ \]:

Copied!

from llama\_index.readers.web import ScrapflyReader

\# Initiate ScrapflyReader with your ScrapFly API key
scrapfly\_reader \= ScrapflyReader(
    api\_key\="Your ScrapFly API key",  \# Get your API key from https://www.scrapfly.io/
    ignore\_scrape\_failures\=True,  \# Ignore unprocessable web pages and log their exceptions
)

\# Load documents from URLs as markdown
documents \= scrapfly\_reader.load\_data(
    urls\=\["https://web-scraping.dev/products"\]
)

from llama\_index.readers.web import ScrapflyReader # Initiate ScrapflyReader with your ScrapFly API key scrapfly\_reader = ScrapflyReader( api\_key="Your ScrapFly API key", # Get your API key from https://www.scrapfly.io/ ignore\_scrape\_failures=True, # Ignore unprocessable web pages and log their exceptions ) # Load documents from URLs as markdown documents = scrapfly\_reader.load\_data( urls=\["https://web-scraping.dev/products"\] )

The ScrapflyReader also allows passigng ScrapeConfig object for customizing the scrape request. See the documentation for the full feature details and their API params: [https://scrapfly.io/docs/scrape-api/getting-started](https://scrapfly.io/docs/scrape-api/getting-started)

In \[ \]:

Copied!

from llama\_index.readers.web import ScrapflyReader

\# Initiate ScrapflyReader with your ScrapFly API key
scrapfly\_reader \= ScrapflyReader(
    api\_key\="Your ScrapFly API key",  \# Get your API key from https://www.scrapfly.io/
    ignore\_scrape\_failures\=True,  \# Ignore unprocessable web pages and log their exceptions
)

scrapfly\_scrape\_config \= {
    "asp": True,  \# Bypass scraping blocking and antibot solutions, like Cloudflare
    "render\_js": True,  \# Enable JavaScript rendering with a cloud headless browser
    "proxy\_pool": "public\_residential\_pool",  \# Select a proxy pool (datacenter or residnetial)
    "country": "us",  \# Select a proxy location
    "auto\_scroll": True,  \# Auto scroll the page
    "js": "",  \# Execute custom JavaScript code by the headless browser
}

\# Load documents from URLs as markdown
documents \= scrapfly\_reader.load\_data(
    urls\=\["https://web-scraping.dev/products"\],
    scrape\_config\=scrapfly\_scrape\_config,  \# Pass the scrape config
    scrape\_format\="markdown",  \# The scrape result format, either \`markdown\`(default) or \`text\`
)

from llama\_index.readers.web import ScrapflyReader # Initiate ScrapflyReader with your ScrapFly API key scrapfly\_reader = ScrapflyReader( api\_key="Your ScrapFly API key", # Get your API key from https://www.scrapfly.io/ ignore\_scrape\_failures=True, # Ignore unprocessable web pages and log their exceptions ) scrapfly\_scrape\_config = { "asp": True, # Bypass scraping blocking and antibot solutions, like Cloudflare "render\_js": True, # Enable JavaScript rendering with a cloud headless browser "proxy\_pool": "public\_residential\_pool", # Select a proxy pool (datacenter or residnetial) "country": "us", # Select a proxy location "auto\_scroll": True, # Auto scroll the page "js": "", # Execute custom JavaScript code by the headless browser } # Load documents from URLs as markdown documents = scrapfly\_reader.load\_data( urls=\["https://web-scraping.dev/products"\], scrape\_config=scrapfly\_scrape\_config, # Pass the scrape config scrape\_format="markdown", # The scrape result format, either \`markdown\`(default) or \`text\` )

Back to top

[Previous Weaviate Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WeaviateDemo/)[Next Deplot Reader Demo](https://docs.llamaindex.ai/en/stable/examples/data_connectors/deplot/DeplotReader/)
