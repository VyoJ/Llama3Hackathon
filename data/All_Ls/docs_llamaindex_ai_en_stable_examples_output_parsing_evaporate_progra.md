Title: Evaporate Demo - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/output_parsing/evaporate_program/

Markdown Content:
Evaporate Demo - LlamaIndex


This demo shows how you can extract DataFrame from raw text using the Evaporate paper (Arora et al.): [https://arxiv.org/abs/2304.09433](https://arxiv.org/abs/2304.09433).

The inspiration is to first "fit" on a set of training text. The fitting process uses the LLM to generate a set of parsing functions from the text. These fitted functions are then applied to text during inference time.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-llms\-openai
%pip install llama\-index\-program\-evaporate

%pip install llama-index-llms-openai %pip install llama-index-program-evaporate

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

%load\_ext autoreload
%autoreload 2

%load\_ext autoreload %autoreload 2

Use `DFEvaporateProgram`[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/evaporate_program/#use-dfevaporateprogram)
-----------------------------------------------------------------------------------------------------------------------------------

The `DFEvaporateProgram` will extract a 2D dataframe from a set of datapoints given a set of fields, and some training data to "fit" some functions on.

### Load data[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/evaporate_program/#load-data)

Here we load a set of cities from Wikipedia.

In \[ \]:

Copied!

wiki\_titles \= \["Toronto", "Seattle", "Chicago", "Boston", "Houston"\]

wiki\_titles = \["Toronto", "Seattle", "Chicago", "Boston", "Houston"\]

In \[ \]:

Copied!

from pathlib import Path

import requests

for title in wiki\_titles:
    response \= requests.get(
        "https://en.wikipedia.org/w/api.php",
        params\={
            "action": "query",
            "format": "json",
            "titles": title,
            "prop": "extracts",
            \# 'exintro': True,
            "explaintext": True,
        },
    ).json()
    page \= next(iter(response\["query"\]\["pages"\].values()))
    wiki\_text \= page\["extract"\]

    data\_path \= Path("data")
    if not data\_path.exists():
        Path.mkdir(data\_path)

    with open(data\_path / f"{title}.txt", "w") as fp:
        fp.write(wiki\_text)

from pathlib import Path import requests for title in wiki\_titles: response = requests.get( "https://en.wikipedia.org/w/api.php", params={ "action": "query", "format": "json", "titles": title, "prop": "extracts", # 'exintro': True, "explaintext": True, }, ).json() page = next(iter(response\["query"\]\["pages"\].values())) wiki\_text = page\["extract"\] data\_path = Path("data") if not data\_path.exists(): Path.mkdir(data\_path) with open(data\_path / f"{title}.txt", "w") as fp: fp.write(wiki\_text)

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

\# Load all wiki documents
city\_docs \= {}
for wiki\_title in wiki\_titles:
    city\_docs\[wiki\_title\] \= SimpleDirectoryReader(
        input\_files\=\[f"data/{wiki\_title}.txt"\]
    ).load\_data()

from llama\_index.core import SimpleDirectoryReader # Load all wiki documents city\_docs = {} for wiki\_title in wiki\_titles: city\_docs\[wiki\_title\] = SimpleDirectoryReader( input\_files=\[f"data/{wiki\_title}.txt"\] ).load\_data()

### Parse Data[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/evaporate_program/#parse-data)

In \[ \]:

Copied!

from llama\_index.llms.openai import OpenAI
from llama\_index.core import Settings

\# setup settings
Settings.llm \= OpenAI(temperature\=0, model\="gpt-3.5-turbo")
Settings.chunk\_size \= 512

from llama\_index.llms.openai import OpenAI from llama\_index.core import Settings # setup settings Settings.llm = OpenAI(temperature=0, model="gpt-3.5-turbo") Settings.chunk\_size = 512

In \[ \]:

Copied!

\# get nodes for each document
city\_nodes \= {}
for wiki\_title in wiki\_titles:
    docs \= city\_docs\[wiki\_title\]
    nodes \= Settings.node\_parser.get\_nodes\_from\_documents(docs)
    city\_nodes\[wiki\_title\] \= nodes

\# get nodes for each document city\_nodes = {} for wiki\_title in wiki\_titles: docs = city\_docs\[wiki\_title\] nodes = Settings.node\_parser.get\_nodes\_from\_documents(docs) city\_nodes\[wiki\_title\] = nodes

### Running the DFEvaporateProgram[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/evaporate_program/#running-the-dfevaporateprogram)

Here we demonstrate how to extract datapoints with our `DFEvaporateProgram`. Given a set of fields, the `DFEvaporateProgram` can first fit functions on a set of training data, and then run extraction over inference data.

In \[ \]:

Copied!

from llama\_index.program.evaporate import DFEvaporateProgram

\# define program
program \= DFEvaporateProgram.from\_defaults(
    fields\_to\_extract\=\["population"\],
)

from llama\_index.program.evaporate import DFEvaporateProgram # define program program = DFEvaporateProgram.from\_defaults( fields\_to\_extract=\["population"\], )

### Fitting Functions[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/evaporate_program/#fitting-functions)

In \[ \]:

Copied!

program.fit\_fields(city\_nodes\["Toronto"\]\[:1\])

program.fit\_fields(city\_nodes\["Toronto"\]\[:1\])

Out\[ \]:

{'population': 'def get\_population\_field(text: str):\\n    """\\n    Function to extract population. \\n    """\\n    \\n    # Use regex to find the population field\\n    pattern = r\\'(?<=population of )(\\\\d+,?\\\\d\*)\\'\\n    population\_field = re.search(pattern, text).group(1)\\n    \\n    # Return the population field as a single value\\n    return int(population\_field.replace(\\',\\', \\'\\'))'}

In \[ \]:

Copied!

\# view extracted function
print(program.get\_function\_str("population"))

\# view extracted function print(program.get\_function\_str("population"))

def get\_population\_field(text: str):
    """
    Function to extract population. 
    """
    
    # Use regex to find the population field
    pattern = r'(?<=population of )(\\d+,?\\d\*)'
    population\_field = re.search(pattern, text).group(1)
    
    # Return the population field as a single value
    return int(population\_field.replace(',', ''))

### Run Inference[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/evaporate_program/#run-inference)

In \[ \]:

Copied!

seattle\_df \= program(nodes\=city\_nodes\["Seattle"\]\[:1\])

seattle\_df = program(nodes=city\_nodes\["Seattle"\]\[:1\])

In \[ \]:

Copied!

seattle\_df

seattle\_df

Out\[ \]:

DataFrameRowsOnly(rows=\[DataFrameRow(row\_values=\[749256\])\])

Use `MultiValueEvaporateProgram`[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/evaporate_program/#use-multivalueevaporateprogram)
---------------------------------------------------------------------------------------------------------------------------------------------------

In contrast to the `DFEvaporateProgram`, which assumes the output obeys a 2D tabular format (one row per node), the `MultiValueEvaporateProgram` returns a list of `DataFrameRow` objects - each object corresponds to a column, and can contain a variable length of values. This can help if we want to extract multiple values for one field from a given piece of text.

In this example, we use this program to parse gold medal counts.

In \[ \]:

Copied!

Settings.llm \= OpenAI(temperature\=0, model\="gpt-4")
Settings.chunk\_size \= 1024
Settings.chunk\_overlap \= 0

Settings.llm = OpenAI(temperature=0, model="gpt-4") Settings.chunk\_size = 1024 Settings.chunk\_overlap = 0

In \[ \]:

Copied!

from llama\_index.core.data\_structs import Node

\# Olympic total medal counts: https://en.wikipedia.org/wiki/All-time\_Olympic\_Games\_medal\_table

train\_text \= """
<table class="wikitable sortable" style="margin-top:0; text-align:center; font-size:90%;">

<tbody><tr>
<th>Team (IOC code)
</th>
<th>No. Summer
</th>
<th>No. Winter
</th>
<th>No. Games
</th></tr>
<tr>
<td align="left"><span id="ALB"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/3/36/Flag\_of\_Albania.svg/22px-Flag\_of\_Albania.svg.png" decoding="async" width="22" height="16" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/3/36/Flag\_of\_Albania.svg/33px-Flag\_of\_Albania.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/3/36/Flag\_of\_Albania.svg/44px-Flag\_of\_Albania.svg.png 2x" data-file-width="980" data-file-height="700" />&#160;<a href="/wiki/Albania\_at\_the\_Olympics" title="Albania at the Olympics">Albania</a>&#160;<span style="font-size:90%;">(ALB)</span></span>
</td>
<td style="background:#f2f2ce;">9</td>
<td style="background:#cedff2;">5</td>
<td>14
</td></tr>
<tr>
<td align="left"><span id="ASA"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/8/87/Flag\_of\_American\_Samoa.svg/22px-Flag\_of\_American\_Samoa.svg.png" decoding="async" width="22" height="11" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/8/87/Flag\_of\_American\_Samoa.svg/33px-Flag\_of\_American\_Samoa.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/8/87/Flag\_of\_American\_Samoa.svg/44px-Flag\_of\_American\_Samoa.svg.png 2x" data-file-width="1000" data-file-height="500" />&#160;<a href="/wiki/American\_Samoa\_at\_the\_Olympics" title="American Samoa at the Olympics">American Samoa</a>&#160;<span style="font-size:90%;">(ASA)</span></span>
</td>
<td style="background:#f2f2ce;">9</td>
<td style="background:#cedff2;">2</td>
<td>11
</td></tr>
<tr>
<td align="left"><span id="AND"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/19/Flag\_of\_Andorra.svg/22px-Flag\_of\_Andorra.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/19/Flag\_of\_Andorra.svg/33px-Flag\_of\_Andorra.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/19/Flag\_of\_Andorra.svg/44px-Flag\_of\_Andorra.svg.png 2x" data-file-width="1000" data-file-height="700" />&#160;<a href="/wiki/Andorra\_at\_the\_Olympics" title="Andorra at the Olympics">Andorra</a>&#160;<span style="font-size:90%;">(AND)</span></span>
</td>
<td style="background:#f2f2ce;">12</td>
<td style="background:#cedff2;">13</td>
<td>25
</td></tr>
<tr>
<td align="left"><span id="ANG"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Flag\_of\_Angola.svg/22px-Flag\_of\_Angola.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Flag\_of\_Angola.svg/33px-Flag\_of\_Angola.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Flag\_of\_Angola.svg/44px-Flag\_of\_Angola.svg.png 2x" data-file-width="900" data-file-height="600" />&#160;<a href="/wiki/Angola\_at\_the\_Olympics" title="Angola at the Olympics">Angola</a>&#160;<span style="font-size:90%;">(ANG)</span></span>
</td>
<td style="background:#f2f2ce;">10</td>
<td style="background:#cedff2;">0</td>
<td>10
</td></tr>
<tr>
<td align="left"><span id="ANT"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/8/89/Flag\_of\_Antigua\_and\_Barbuda.svg/22px-Flag\_of\_Antigua\_and\_Barbuda.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/8/89/Flag\_of\_Antigua\_and\_Barbuda.svg/33px-Flag\_of\_Antigua\_and\_Barbuda.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/8/89/Flag\_of\_Antigua\_and\_Barbuda.svg/44px-Flag\_of\_Antigua\_and\_Barbuda.svg.png 2x" data-file-width="900" data-file-height="600" />&#160;<a href="/wiki/Antigua\_and\_Barbuda\_at\_the\_Olympics" title="Antigua and Barbuda at the Olympics">Antigua and Barbuda</a>&#160;<span style="font-size:90%;">(ANT)</span></span>
</td>
<td style="background:#f2f2ce;">11</td>
<td style="background:#cedff2;">0</td>
<td>11
</td></tr>
<tr>
<td align="left"><span id="ARU"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Flag\_of\_Aruba.svg/22px-Flag\_of\_Aruba.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Flag\_of\_Aruba.svg/33px-Flag\_of\_Aruba.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Flag\_of\_Aruba.svg/44px-Flag\_of\_Aruba.svg.png 2x" data-file-width="900" data-file-height="600" />&#160;<a href="/wiki/Aruba\_at\_the\_Olympics" title="Aruba at the Olympics">Aruba</a>&#160;<span style="font-size:90%;">(ARU)</span></span>
</td>
<td style="background:#f2f2ce;">9</td>
<td style="background:#cedff2;">0</td>
<td>9
</td></tr>
"""
train\_nodes \= \[Node(text\=train\_text)\]

from llama\_index.core.data\_structs import Node # Olympic total medal counts: https://en.wikipedia.org/wiki/All-time\_Olympic\_Games\_medal\_table train\_text = """ """ train\_nodes = \[Node(text=train\_text)\]

| Team (IOC code) | No. Summer | No. Winter | No. Games |
| --- | --- | --- | --- |
|  ![Image 4](https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Flag_of_Albania.svg/22px-Flag_of_Albania.svg.png) [Albania](https://docs.llamaindex.ai/wiki/Albania_at_the_Olympics "Albania at the Olympics") (ALB) | 9 | 5 | 14 |
|  ![Image 5](https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Flag_of_American_Samoa.svg/22px-Flag_of_American_Samoa.svg.png) [American Samoa](https://docs.llamaindex.ai/wiki/American_Samoa_at_the_Olympics "American Samoa at the Olympics") (ASA) | 9 | 2 | 11 |
|  ![Image 6](https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Flag_of_Andorra.svg/22px-Flag_of_Andorra.svg.png) [Andorra](https://docs.llamaindex.ai/wiki/Andorra_at_the_Olympics "Andorra at the Olympics") (AND) | 12 | 13 | 25 |
|  ![Image 7](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Flag_of_Angola.svg/22px-Flag_of_Angola.svg.png) [Angola](https://docs.llamaindex.ai/wiki/Angola_at_the_Olympics "Angola at the Olympics") (ANG) | 10 | 0 | 10 |
|  ![Image 8](https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Flag_of_Antigua_and_Barbuda.svg/22px-Flag_of_Antigua_and_Barbuda.svg.png) [Antigua and Barbuda](https://docs.llamaindex.ai/wiki/Antigua_and_Barbuda_at_the_Olympics "Antigua and Barbuda at the Olympics") (ANT) | 11 | 0 | 11 |
|  ![Image 9](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Flag_of_Aruba.svg/22px-Flag_of_Aruba.svg.png) [Aruba](https://docs.llamaindex.ai/wiki/Aruba_at_the_Olympics "Aruba at the Olympics") (ARU) | 9 | 0 | 9 |

In \[ \]:

Copied!

infer\_text \= """
<td align="left"><span id="BAN"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Flag\_of\_Bangladesh.svg/22px-Flag\_of\_Bangladesh.svg.png" decoding="async" width="22" height="13" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Flag\_of\_Bangladesh.svg/33px-Flag\_of\_Bangladesh.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Flag\_of\_Bangladesh.svg/44px-Flag\_of\_Bangladesh.svg.png 2x" data-file-width="1000" data-file-height="600" />&#160;<a href="/wiki/Bangladesh\_at\_the\_Olympics" title="Bangladesh at the Olympics">Bangladesh</a>&#160;<span style="font-size:90%;">(BAN)</span></span>
</td>
<td style="background:#f2f2ce;">10</td>
<td style="background:#cedff2;">0</td>
<td>10
</td></tr>
<tr>
<td align="left"><span id="BIZ"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Flag\_of\_Belize.svg/22px-Flag\_of\_Belize.svg.png" decoding="async" width="22" height="13" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Flag\_of\_Belize.svg/33px-Flag\_of\_Belize.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Flag\_of\_Belize.svg/44px-Flag\_of\_Belize.svg.png 2x" data-file-width="1000" data-file-height="600" />&#160;<a href="/wiki/Belize\_at\_the\_Olympics" title="Belize at the Olympics">Belize</a>&#160;<span style="font-size:90%;">(BIZ)</span></span> <sup class="reference" id="ref\_BIZBIZ"><a href="#endnote\_BIZBIZ">\[BIZ\]</a></sup>
</td>
<td style="background:#f2f2ce;">13</td>
<td style="background:#cedff2;">0</td>
<td>13
</td></tr>
<tr>
<td align="left"><span id="BEN"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Flag\_of\_Benin.svg/22px-Flag\_of\_Benin.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Flag\_of\_Benin.svg/33px-Flag\_of\_Benin.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Flag\_of\_Benin.svg/44px-Flag\_of\_Benin.svg.png 2x" data-file-width="900" data-file-height="600" />&#160;<a href="/wiki/Benin\_at\_the\_Olympics" title="Benin at the Olympics">Benin</a>&#160;<span style="font-size:90%;">(BEN)</span></span> <sup class="reference" id="ref\_BENBEN"><a href="#endnote\_BENBEN">\[BEN\]</a></sup>
</td>
<td style="background:#f2f2ce;">12</td>
<td style="background:#cedff2;">0</td>
<td>12
</td></tr>
<tr>
<td align="left"><span id="BHU"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/91/Flag\_of\_Bhutan.svg/22px-Flag\_of\_Bhutan.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/91/Flag\_of\_Bhutan.svg/33px-Flag\_of\_Bhutan.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/91/Flag\_of\_Bhutan.svg/44px-Flag\_of\_Bhutan.svg.png 2x" data-file-width="900" data-file-height="600" />&#160;<a href="/wiki/Bhutan\_at\_the\_Olympics" title="Bhutan at the Olympics">Bhutan</a>&#160;<span style="font-size:90%;">(BHU)</span></span>
</td>
<td style="background:#f2f2ce;">10</td>
<td style="background:#cedff2;">0</td>
<td>10
</td></tr>
<tr>
<td align="left"><span id="BOL"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag\_of\_Bolivia.svg/22px-Flag\_of\_Bolivia.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag\_of\_Bolivia.svg/33px-Flag\_of\_Bolivia.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag\_of\_Bolivia.svg/44px-Flag\_of\_Bolivia.svg.png 2x" data-file-width="1100" data-file-height="750" />&#160;<a href="/wiki/Bolivia\_at\_the\_Olympics" title="Bolivia at the Olympics">Bolivia</a>&#160;<span style="font-size:90%;">(BOL)</span></span>
</td>
<td style="background:#f2f2ce;">15</td>
<td style="background:#cedff2;">7</td>
<td>22
</td></tr>
<tr>
<td align="left"><span id="BIH"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Flag\_of\_Bosnia\_and\_Herzegovina.svg/22px-Flag\_of\_Bosnia\_and\_Herzegovina.svg.png" decoding="async" width="22" height="11" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Flag\_of\_Bosnia\_and\_Herzegovina.svg/33px-Flag\_of\_Bosnia\_and\_Herzegovina.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Flag\_of\_Bosnia\_and\_Herzegovina.svg/44px-Flag\_of\_Bosnia\_and\_Herzegovina.svg.png 2x" data-file-width="800" data-file-height="400" />&#160;<a href="/wiki/Bosnia\_and\_Herzegovina\_at\_the\_Olympics" title="Bosnia and Herzegovina at the Olympics">Bosnia and Herzegovina</a>&#160;<span style="font-size:90%;">(BIH)</span></span>
</td>
<td style="background:#f2f2ce;">8</td>
<td style="background:#cedff2;">8</td>
<td>16
</td></tr>
<tr>
<td align="left"><span id="IVB"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/42/Flag\_of\_the\_British\_Virgin\_Islands.svg/22px-Flag\_of\_the\_British\_Virgin\_Islands.svg.png" decoding="async" width="22" height="11" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/42/Flag\_of\_the\_British\_Virgin\_Islands.svg/33px-Flag\_of\_the\_British\_Virgin\_Islands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/42/Flag\_of\_the\_British\_Virgin\_Islands.svg/44px-Flag\_of\_the\_British\_Virgin\_Islands.svg.png 2x" data-file-width="1200" data-file-height="600" />&#160;<a href="/wiki/British\_Virgin\_Islands\_at\_the\_Olympics" title="British Virgin Islands at the Olympics">British Virgin Islands</a>&#160;<span style="font-size:90%;">(IVB)</span></span>
</td>
<td style="background:#f2f2ce;">10</td>
<td style="background:#cedff2;">2</td>
<td>12
</td></tr>
<tr>
<td align="left"><span id="BRU"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Flag\_of\_Brunei.svg/22px-Flag\_of\_Brunei.svg.png" decoding="async" width="22" height="11" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Flag\_of\_Brunei.svg/33px-Flag\_of\_Brunei.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Flag\_of\_Brunei.svg/44px-Flag\_of\_Brunei.svg.png 2x" data-file-width="1440" data-file-height="720" />&#160;<a href="/wiki/Brunei\_at\_the\_Olympics" title="Brunei at the Olympics">Brunei</a>&#160;<span style="font-size:90%;">(BRU)</span></span> <sup class="reference" id="ref\_AA"><a href="#endnote\_AA">\[A\]</a></sup>
</td>
<td style="background:#f2f2ce;">6</td>
<td style="background:#cedff2;">0</td>
<td>6
</td></tr>
<tr>
<td align="left"><span id="CAM"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/8/83/Flag\_of\_Cambodia.svg/22px-Flag\_of\_Cambodia.svg.png" decoding="async" width="22" height="14" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/8/83/Flag\_of\_Cambodia.svg/33px-Flag\_of\_Cambodia.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/8/83/Flag\_of\_Cambodia.svg/44px-Flag\_of\_Cambodia.svg.png 2x" data-file-width="1000" data-file-height="640" />&#160;<a href="/wiki/Cambodia\_at\_the\_Olympics" title="Cambodia at the Olympics">Cambodia</a>&#160;<span style="font-size:90%;">(CAM)</span></span>
</td>
<td style="background:#f2f2ce;">10</td>
<td style="background:#cedff2;">0</td>
<td>10
</td></tr>
<tr>
<td align="left"><span id="CPV"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/3/38/Flag\_of\_Cape\_Verde.svg/22px-Flag\_of\_Cape\_Verde.svg.png" decoding="async" width="22" height="13" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/3/38/Flag\_of\_Cape\_Verde.svg/33px-Flag\_of\_Cape\_Verde.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/3/38/Flag\_of\_Cape\_Verde.svg/44px-Flag\_of\_Cape\_Verde.svg.png 2x" data-file-width="1020" data-file-height="600" />&#160;<a href="/wiki/Cape\_Verde\_at\_the\_Olympics" title="Cape Verde at the Olympics">Cape Verde</a>&#160;<span style="font-size:90%;">(CPV)</span></span>
</td>
<td style="background:#f2f2ce;">7</td>
<td style="background:#cedff2;">0</td>
<td>7
</td></tr>
<tr>
<td align="left"><span id="CAY"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Flag\_of\_the\_Cayman\_Islands.svg/22px-Flag\_of\_the\_Cayman\_Islands.svg.png" decoding="async" width="22" height="11" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Flag\_of\_the\_Cayman\_Islands.svg/33px-Flag\_of\_the\_Cayman\_Islands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Flag\_of\_the\_Cayman\_Islands.svg/44px-Flag\_of\_the\_Cayman\_Islands.svg.png 2x" data-file-width="1200" data-file-height="600" />&#160;<a href="/wiki/Cayman\_Islands\_at\_the\_Olympics" title="Cayman Islands at the Olympics">Cayman Islands</a>&#160;<span style="font-size:90%;">(CAY)</span></span>
</td>
<td style="background:#f2f2ce;">11</td>
<td style="background:#cedff2;">2</td>
<td>13
</td></tr>
<tr>
<td align="left"><span id="CAF"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Flag\_of\_the\_Central\_African\_Republic.svg/22px-Flag\_of\_the\_Central\_African\_Republic.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Flag\_of\_the\_Central\_African\_Republic.svg/33px-Flag\_of\_the\_Central\_African\_Republic.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Flag\_of\_the\_Central\_African\_Republic.svg/44px-Flag\_of\_the\_Central\_African\_Republic.svg.png 2x" data-file-width="900" data-file-height="600" />&#160;<a href="/wiki/Central\_African\_Republic\_at\_the\_Olympics" title="Central African Republic at the Olympics">Central African Republic</a>&#160;<span style="font-size:90%;">(CAF)</span></span>
</td>
<td style="background:#f2f2ce;">11</td>
<td style="background:#cedff2;">0</td>
<td>11
</td></tr>
<tr>
<td align="left"><span id="CHA"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Flag\_of\_Chad.svg/22px-Flag\_of\_Chad.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Flag\_of\_Chad.svg/33px-Flag\_of\_Chad.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Flag\_of\_Chad.svg/44px-Flag\_of\_Chad.svg.png 2x" data-file-width="900" data-file-height="600" />&#160;<a href="/wiki/Chad\_at\_the\_Olympics" title="Chad at the Olympics">Chad</a>&#160;<span style="font-size:90%;">(CHA)</span></span>
</td>
<td style="background:#f2f2ce;">13</td>
<td style="background:#cedff2;">0</td>
<td>13
</td></tr>
<tr>
<td align="left"><span id="COM"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/94/Flag\_of\_the\_Comoros.svg/22px-Flag\_of\_the\_Comoros.svg.png" decoding="async" width="22" height="13" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/94/Flag\_of\_the\_Comoros.svg/33px-Flag\_of\_the\_Comoros.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/94/Flag\_of\_the\_Comoros.svg/44px-Flag\_of\_the\_Comoros.svg.png 2x" data-file-width="1000" data-file-height="600" />&#160;<a href="/wiki/Comoros\_at\_the\_Olympics" title="Comoros at the Olympics">Comoros</a>&#160;<span style="font-size:90%;">(COM)</span></span>
</td>
<td style="background:#f2f2ce;">7</td>
<td style="background:#cedff2;">0</td>
<td>7
</td></tr>
<tr>
<td align="left"><span id="CGO"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag\_of\_the\_Republic\_of\_the\_Congo.svg/22px-Flag\_of\_the\_Republic\_of\_the\_Congo.svg.png" decoding="async" width="22" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag\_of\_the\_Republic\_of\_the\_Congo.svg/33px-Flag\_of\_the\_Republic\_of\_the\_Congo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag\_of\_the\_Republic\_of\_the\_Congo.svg/44px-Flag\_of\_the\_Republic\_of\_the\_Congo.svg.png 2x" data-file-width="900" data-file-height="600" />&#160;<a href="/wiki/Republic\_of\_the\_Congo\_at\_the\_Olympics" title="Republic of the Congo at the Olympics">Republic of the Congo</a>&#160;<span style="font-size:90%;">(CGO)</span></span>
</td>
<td style="background:#f2f2ce;">13</td>
<td style="background:#cedff2;">0</td>
<td>13
</td></tr>
<tr>
<td align="left"><span id="COD"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Flag\_of\_the\_Democratic\_Republic\_of\_the\_Congo.svg/22px-Flag\_of\_the\_Democratic\_Republic\_of\_the\_Congo.svg.png" decoding="async" width="22" height="17" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Flag\_of\_the\_Democratic\_Republic\_of\_the\_Congo.svg/33px-Flag\_of\_the\_Democratic\_Republic\_of\_the\_Congo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Flag\_of\_the\_Democratic\_Republic\_of\_the\_Congo.svg/44px-Flag\_of\_the\_Democratic\_Republic\_of\_the\_Congo.svg.png 2x" data-file-width="800" data-file-height="600" />&#160;<a href="/wiki/Democratic\_Republic\_of\_the\_Congo\_at\_the\_Olympics" title="Democratic Republic of the Congo at the Olympics">Democratic Republic of the Congo</a>&#160;<span style="font-size:90%;">(COD)</span></span> <sup class="reference" id="ref\_CODCOD"><a href="#endnote\_CODCOD">\[COD\]</a></sup>
</td>
<td style="background:#f2f2ce;">11</td>
<td style="background:#cedff2;">0</td>
<td>11
</td></tr>
"""

infer\_nodes \= \[Node(text\=infer\_text)\]

infer\_text = """  ![Image 10](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Flag_of_Bangladesh.svg/22px-Flag_of_Bangladesh.svg.png) [Bangladesh](https://docs.llamaindex.ai/wiki/Bangladesh_at_the_Olympics "Bangladesh at the Olympics") (BAN) 10 0 10  ![Image 11](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Flag_of_Belize.svg/22px-Flag_of_Belize.svg.png) [Belize](https://docs.llamaindex.ai/wiki/Belize_at_the_Olympics "Belize at the Olympics") (BIZ) [\[BIZ\]](https://docs.llamaindex.ai/en/stable/examples/output_parsing/evaporate_program/#endnote_BIZBIZ) 13 0 13  ![Image 12](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Flag_of_Benin.svg/22px-Flag_of_Benin.svg.png) [Benin](https://docs.llamaindex.ai/wiki/Benin_at_the_Olympics "Benin at the Olympics") (BEN) [\[BEN\]](https://docs.llamaindex.ai/en/stable/examples/output_parsing/evaporate_program/#endnote_BENBEN) 12 0 12  ![Image 13](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Flag_of_Bhutan.svg/22px-Flag_of_Bhutan.svg.png) [Bhutan](https://docs.llamaindex.ai/wiki/Bhutan_at_the_Olympics "Bhutan at the Olympics") (BHU) 10 0 10  ![Image 14](https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Bolivia.svg/22px-Flag_of_Bolivia.svg.png) [Bolivia](https://docs.llamaindex.ai/wiki/Bolivia_at_the_Olympics "Bolivia at the Olympics") (BOL) 15 7 22  ![Image 15](https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Flag_of_Bosnia_and_Herzegovina.svg/22px-Flag_of_Bosnia_and_Herzegovina.svg.png) [Bosnia and Herzegovina](https://docs.llamaindex.ai/wiki/Bosnia_and_Herzegovina_at_the_Olympics "Bosnia and Herzegovina at the Olympics") (BIH) 8 8 16  ![Image 16](https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Flag_of_the_British_Virgin_Islands.svg/22px-Flag_of_the_British_Virgin_Islands.svg.png) [British Virgin Islands](https://docs.llamaindex.ai/wiki/British_Virgin_Islands_at_the_Olympics "British Virgin Islands at the Olympics") (IVB) 10 2 12  ![Image 17](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Flag_of_Brunei.svg/22px-Flag_of_Brunei.svg.png) [Brunei](https://docs.llamaindex.ai/wiki/Brunei_at_the_Olympics "Brunei at the Olympics") (BRU) [\[A\]](https://docs.llamaindex.ai/en/stable/examples/output_parsing/evaporate_program/#endnote_AA) 6 0 6  ![Image 18](https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Flag_of_Cambodia.svg/22px-Flag_of_Cambodia.svg.png) [Cambodia](https://docs.llamaindex.ai/wiki/Cambodia_at_the_Olympics "Cambodia at the Olympics") (CAM) 10 0 10  ![Image 19](https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Flag_of_Cape_Verde.svg/22px-Flag_of_Cape_Verde.svg.png) [Cape Verde](https://docs.llamaindex.ai/wiki/Cape_Verde_at_the_Olympics "Cape Verde at the Olympics") (CPV) 7 0 7  ![Image 20](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Flag_of_the_Cayman_Islands.svg/22px-Flag_of_the_Cayman_Islands.svg.png) [Cayman Islands](https://docs.llamaindex.ai/wiki/Cayman_Islands_at_the_Olympics "Cayman Islands at the Olympics") (CAY) 11 2 13  ![Image 21](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Flag_of_the_Central_African_Republic.svg/22px-Flag_of_the_Central_African_Republic.svg.png) [Central African Republic](https://docs.llamaindex.ai/wiki/Central_African_Republic_at_the_Olympics "Central African Republic at the Olympics") (CAF) 11 0 11  ![Image 22](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Flag_of_Chad.svg/22px-Flag_of_Chad.svg.png) [Chad](https://docs.llamaindex.ai/wiki/Chad_at_the_Olympics "Chad at the Olympics") (CHA) 13 0 13  ![Image 23](https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Flag_of_the_Comoros.svg/22px-Flag_of_the_Comoros.svg.png) [Comoros](https://docs.llamaindex.ai/wiki/Comoros_at_the_Olympics "Comoros at the Olympics") (COM) 7 0 7  ![Image 24](https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Flag_of_the_Republic_of_the_Congo.svg/22px-Flag_of_the_Republic_of_the_Congo.svg.png) [Republic of the Congo](https://docs.llamaindex.ai/wiki/Republic_of_the_Congo_at_the_Olympics "Republic of the Congo at the Olympics") (CGO) 13 0 13  ![Image 25](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Flag_of_the_Democratic_Republic_of_the_Congo.svg/22px-Flag_of_the_Democratic_Republic_of_the_Congo.svg.png) [Democratic Republic of the Congo](https://docs.llamaindex.ai/wiki/Democratic_Republic_of_the_Congo_at_the_Olympics "Democratic Republic of the Congo at the Olympics") (COD) [\[COD\]](https://docs.llamaindex.ai/en/stable/examples/output_parsing/evaporate_program/#endnote_CODCOD) 11 0 11 """ infer\_nodes = \[Node(text=infer\_text)\]

In \[ \]:

Copied!

from llama\_index.core.program.predefined import MultiValueEvaporateProgram

program \= MultiValueEvaporateProgram.from\_defaults(
    fields\_to\_extract\=\["countries", "medal\_count"\],
)

from llama\_index.core.program.predefined import MultiValueEvaporateProgram program = MultiValueEvaporateProgram.from\_defaults( fields\_to\_extract=\["countries", "medal\_count"\], )

In \[ \]:

Copied!

program.fit\_fields(train\_nodes\[:1\])

program.fit\_fields(train\_nodes\[:1\])

Out\[ \]:

{'countries': 'def get\_countries\_field(text: str):\\n    """\\n    Function to extract countries. \\n    """\\n    \\n    # Use regex to extract the countries field\\n    countries\_field = re.findall(r\\'<a href=".\*">(.\*)</a>\\', text)\\n    \\n    # Return the result as a list\\n    return countries\_field',
 'medal\_count': 'def get\_medal\_count\_field(text: str):\\n    """\\n    Function to extract medal\_count. \\n    """\\n    \\n    # Use regex to extract the medal count field\\n    medal\_count\_field = re.findall(r\\'<td style="background:#f2f2ce;">(.\*?)</td>\\', text)\\n    \\n    # Return the result as a list\\n    return medal\_count\_field'}

In \[ \]:

Copied!

print(program.get\_function\_str("countries"))

print(program.get\_function\_str("countries"))

def get\_countries\_field(text: str):
    """
    Function to extract countries. 
    """
    
    # Use regex to extract the countries field
    countries\_field = re.findall(r'<a href=".\*">(.\*)</a>', text)
    
    # Return the result as a list
    return countries\_field

In \[ \]:

Copied!

print(program.get\_function\_str("medal\_count"))

print(program.get\_function\_str("medal\_count"))

def get\_medal\_count\_field(text: str):
    """
    Function to extract medal\_count. 
    """
    
    # Use regex to extract the medal count field
    medal\_count\_field = re.findall(r'<td style="background:#f2f2ce;">(.\*?)</td>', text)
    
    # Return the result as a list
    return medal\_count\_field

In \[ \]:

Copied!

result \= program(nodes\=infer\_nodes\[:1\])

result = program(nodes=infer\_nodes\[:1\])

In \[ \]:

Copied!

\# output countries
print(f"Countries: {result.columns\[0\].row\_values}\\n")
\# output medal counts
print(f"Medal Counts: {result.columns\[0\].row\_values}\\n")

\# output countries print(f"Countries: {result.columns\[0\].row\_values}\\n") # output medal counts print(f"Medal Counts: {result.columns\[0\].row\_values}\\n")

Countries: \['Bangladesh', '\[BIZ\]', '\[BEN\]', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'British Virgin Islands', '\[A\]', 'Cambodia', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Comoros', 'Republic of the Congo', '\[COD\]'\]

Medal Counts: \['Bangladesh', '\[BIZ\]', '\[BEN\]', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'British Virgin Islands', '\[A\]', 'Cambodia', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Comoros', 'Republic of the Congo', '\[COD\]'\]

Bonus: Use the underlying `EvaporateExtractor`[¶](https://docs.llamaindex.ai/en/stable/examples/output_parsing/evaporate_program/#bonus-use-the-underlying-evaporateextractor)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The underlying `EvaporateExtractor` offers some additional functionality, e.g. actually helping to identify fields over a set of text.

Here we show how you can use `identify_fields` to determine relevant fields around a general `topic` field.

In \[ \]:

Copied!

\# a list of nodes, one node per city, corresponding to intro paragraph
\# city\_pop\_nodes = \[\]
city\_pop\_nodes \= \[city\_nodes\["Toronto"\]\[0\], city\_nodes\["Seattle"\]\[0\]\]

\# a list of nodes, one node per city, corresponding to intro paragraph # city\_pop\_nodes = \[\] city\_pop\_nodes = \[city\_nodes\["Toronto"\]\[0\], city\_nodes\["Seattle"\]\[0\]\]

In \[ \]:

Copied!

extractor \= program.extractor

extractor = program.extractor

In \[ \]:

Copied!

\# Try with Toronto and Seattle (should extract "population")
existing\_fields \= extractor.identify\_fields(
    city\_pop\_nodes, topic\="population", fields\_top\_k\=4
)

\# Try with Toronto and Seattle (should extract "population") existing\_fields = extractor.identify\_fields( city\_pop\_nodes, topic="population", fields\_top\_k=4 )

In \[ \]:

Copied!

existing\_fields

existing\_fields

Out\[ \]:

\["seattle metropolitan area's population"\]

Back to top

[Previous DataFrame Structured Data Extraction](https://docs.llamaindex.ai/en/stable/examples/output_parsing/df_program/)[Next Function Calling Program for Structured Extraction](https://docs.llamaindex.ai/en/stable/examples/output_parsing/function_program/)

Hi, how can I help you?

🦙
