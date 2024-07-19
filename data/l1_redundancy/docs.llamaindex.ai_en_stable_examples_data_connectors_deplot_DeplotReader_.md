Title: Deplot Reader Demo - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/data_connectors/deplot/DeplotReader/

Markdown Content:
Deplot Reader Demo - LlamaIndex


In this notebook we showcase the capabilities of our ImageTabularChartReader, which is powered by the DePlot model [https://arxiv.org/abs/2212.10505](https://arxiv.org/abs/2212.10505).

In \[ \]:

Copied!

%pip install llama\-index\-readers\-file

%pip install llama-index-readers-file

In \[ \]:

Copied!

from llama\_index.readers.file import ImageTabularChartReader
from llama\_index.core import SummaryIndex
from llama\_index.core.response.notebook\_utils import display\_response
from pathlib import Path

from llama\_index.readers.file import ImageTabularChartReader from llama\_index.core import SummaryIndex from llama\_index.core.response.notebook\_utils import display\_response from pathlib import Path

In \[ \]:

Copied!

loader \= ImageTabularChartReader(keep\_image\=True)

loader = ImageTabularChartReader(keep\_image=True)

Load Protected Waters Chart[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/deplot/DeplotReader/#load-protected-waters-chart)
----------------------------------------------------------------------------------------------------------------------------------------------

This chart shows the percentage of marine territorial waters that are protected for each country.

In \[ \]:

Copied!

documents \= loader.load\_data(file\=Path("./marine\_chart.png"))

documents = loader.load\_data(file=Path("./marine\_chart.png"))

In \[ \]:

Copied!

print(documents\[0\].text)

print(documents\[0\].text)

Figure or chart with tabular data: Country | Share of marine territorial waters that are protected, 2016 <0x0A> Greenland | 4.52 <0x0A> Mauritania | 4.15 <0x0A> Indonesia | 2.88 <0x0A> Ireland | 2.33

In \[ \]:

Copied!

summary\_index \= SummaryIndex.from\_documents(documents)
response \= summary\_index.as\_query\_engine().query(
    "What is the difference between the shares of Greenland and the share of"
    " Mauritania?"
)

summary\_index = SummaryIndex.from\_documents(documents) response = summary\_index.as\_query\_engine().query( "What is the difference between the shares of Greenland and the share of" " Mauritania?" )

Retrying langchain.llms.openai.completion\_with\_retry.<locals>.\_completion\_with\_retry in 4.0 seconds as it raised APIConnectionError: Error communicating with OpenAI: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response')).

In \[ \]:

Copied!

display\_response(response, show\_source\=True)

display\_response(response, show\_source=True)

Load Pew Research Chart[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/deplot/DeplotReader/#load-pew-research-chart)
--------------------------------------------------------------------------------------------------------------------------------------

Here we load in a Pew Research chart showing international views of the US/Biden.

Source: [https://www.pewresearch.org/global/2023/06/27/international-views-of-biden-and-u-s-largely-positive/](https://www.pewresearch.org/global/2023/06/27/international-views-of-biden-and-u-s-largely-positive/)

In \[ \]:

Copied!

documents \= loader.load\_data(file\=Path("./pew1.png"))

documents = loader.load\_data(file=Path("./pew1.png"))

In \[ \]:

Copied!

print(documents\[0\].text)

print(documents\[0\].text)

Figure or chart with tabular data: Entity | Values <0x0A> Does not | 50.0 <0x0A> % who say the U.S take into account the interests of countries like theirs | 49.0 <0x0A> Does not | 38.0 <0x0A> % who say the U.S contribute to peace and stability around the world | 61.0 <0x0A> Does not | 15.0 <0x0A> % who say the U.S interfere in the affairs of other countries | 15.0 <0x0A>% who have confidence | 54.0 <0x0A> Views of President Biden | 30.0 <0x0A> Favorable | 59.0 <0x0A> Views of the U.S. | 9.0

In \[ \]:

Copied!

summary\_index \= SummaryIndex.from\_documents(documents)
response \= summary\_index.as\_query\_engine().query(
    "What percentage says that the US contributes to peace and stability?"
)

summary\_index = SummaryIndex.from\_documents(documents) response = summary\_index.as\_query\_engine().query( "What percentage says that the US contributes to peace and stability?" )

In \[ \]:

Copied!

display\_response(response, show\_source\=True)

display\_response(response, show\_source=True)

Back to top

[Previous Web Page Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/WebPageDemo/)[Next HTML Tag Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/html_tag_reader/)
