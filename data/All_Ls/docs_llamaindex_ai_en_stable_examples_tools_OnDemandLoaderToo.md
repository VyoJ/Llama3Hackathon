Title: OnDemandLoaderTool Tutorial - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/tools/OnDemandLoaderTool/

Markdown Content:
OnDemandLoaderTool Tutorial - LlamaIndex


Our `OnDemandLoaderTool` is a powerful agent tool that allows for "on-demand" data querying from any data source on LlamaHub.

This tool takes in a `BaseReader` data loader, and when called will 1) load data, 2) index data, and 3) query the data.

In this walkthrough, we show how to use the `OnDemandLoaderTool` to convert our Wikipedia data loader into an accessible search tool for a LangChain agent.

If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-readers\-wikipedia

%pip install llama-index-readers-wikipedia

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

In \[ \]:

Copied!

from llama\_index.core.tools.ondemand\_loader\_tool import OnDemandLoaderTool
from llama\_index.readers.wikipedia import WikipediaReader
from typing import List

from pydantic import BaseModel

from llama\_index.core.tools.ondemand\_loader\_tool import OnDemandLoaderTool from llama\_index.readers.wikipedia import WikipediaReader from typing import List from pydantic import BaseModel

### Define Tool[¶](https://docs.llamaindex.ai/en/stable/examples/tools/OnDemandLoaderTool/#define-tool)

We first define the `WikipediaReader`. Note that the `load_data` interface to `WikipediaReader` takes in a list of `pages`. By default, this queries the Wikipedia search endpoint which will autosuggest the relevant pages.

We then wrap it into our `OnDemandLoaderTool`.

By default since we don't specify the `index_cls`, a simple vector store index is initialized.

In \[ \]:

Copied!

reader \= WikipediaReader()

reader = WikipediaReader()

In \[ \]:

Copied!

tool \= OnDemandLoaderTool.from\_defaults(
    reader,
    name\="Wikipedia Tool",
    description\="A tool for loading and querying articles from Wikipedia",
)

tool = OnDemandLoaderTool.from\_defaults( reader, name="Wikipedia Tool", description="A tool for loading and querying articles from Wikipedia", )

#### Testing[¶](https://docs.llamaindex.ai/en/stable/examples/tools/OnDemandLoaderTool/#testing)

We can try running the tool by itself (or as a LangChain tool), just to showcase what the interface is like!

Note that besides the arguments required for the data loader, the tool also takes in a `query_str` which will be the query against the index.

In \[ \]:

Copied!

\# run tool by itself
tool(\["Berlin"\], query\_str\="What's the arts and culture scene in Berlin?")

\# run tool by itself tool(\["Berlin"\], query\_str="What's the arts and culture scene in Berlin?")

Out\[ \]:

"\\nBerlin has a vibrant and diverse arts and culture scene. It is home to 44 theaters and stages, three major opera houses, and numerous art galleries. The cityscape of Berlin displays large quantities of urban street art, and the Berlin Wall has become one of the largest open-air canvasses in the world. Berlin also has a long history of gay culture, and is an important birthplace of the LGBT rights movement. There are many festivals and events throughout the year, such as the Berlin International Film Festival, the Karneval der Kulturen, the Berlin Festival, and the New Year's Eve celebrations. The city is also home to many museums, such as the Museum Island, the Gemäldegalerie, the Neue Nationalgalerie, the Pergamon Museum, the Bode Museum, the Hamburger Bahnhof, the German Museum of Technology, the Jewish Museum, the Museum für Naturkunde, the Kupferstichkabinett Berlin, the Museum Berggruen, and the Beate Uhse Erotic Museum."

In \[ \]:

Copied!

\# run tool as langchain structured tool
lc\_tool \= tool.to\_langchain\_structured\_tool(verbose\=True)

\# run tool as langchain structured tool lc\_tool = tool.to\_langchain\_structured\_tool(verbose=True)

In \[ \]:

Copied!

lc\_tool.run(
    tool\_input\={
        "pages": \["Berlin"\],
        "query\_str": "What's the arts and culture scene in Berlin?",
    }
)

lc\_tool.run( tool\_input={ "pages": \["Berlin"\], "query\_str": "What's the arts and culture scene in Berlin?", } )

### Initialize LangChain Agent[¶](https://docs.llamaindex.ai/en/stable/examples/tools/OnDemandLoaderTool/#initialize-langchain-agent)

For tutorial purposes, the agent just has access to one tool - the Wikipedia Reader

Note that we need to use Structured Tools from LangChain.

In \[ \]:

Copied!

from langchain.agents import initialize\_agent
from langchain.chat\_models import ChatOpenAI

from langchain.agents import initialize\_agent from langchain.chat\_models import ChatOpenAI

In \[ \]:

Copied!

llm \= ChatOpenAI(temperature\=0, model\_name\="gpt-3.5-turbo", streaming\=True)

llm = ChatOpenAI(temperature=0, model\_name="gpt-3.5-turbo", streaming=True)

In \[ \]:

Copied!

agent \= initialize\_agent(
    \[lc\_tool\],
    llm\=llm,
    agent\="structured-chat-zero-shot-react-description",
    verbose\=True,
)

agent = initialize\_agent( \[lc\_tool\], llm=llm, agent="structured-chat-zero-shot-react-description", verbose=True, )

Now let's run some queries![¶](https://docs.llamaindex.ai/en/stable/examples/tools/OnDemandLoaderTool/#now-lets-run-some-queries)


The OnDemandLoaderTool allows the agent to simultaneously 1) load the data from Wikipedia, 2) query that data.

In \[ \]:

Copied!

agent.run("Tell me about the arts and culture of Berlin")

agent.run("Tell me about the arts and culture of Berlin")

Retrying langchain.chat\_models.openai.ChatOpenAI.completion\_with\_retry.<locals>.\_completion\_with\_retry in 1.0 seconds as it raised APIConnectionError: Error communicating with OpenAI: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response')).

\> Entering new AgentExecutor chain...
Action:
\`\`\`
{
  "action": "Wikipedia Tool",
  "action\_input": {
    "pages": \["Culture in Berlin"\],
    "query\_str": "What is the arts and culture scene like in Berlin?"
  }
}
\`\`\`
Observation: 
The arts and culture scene in Berlin is vibrant and diverse. The city is home to over 600 art galleries, 153 museums, and numerous cultural institutions. It is a world city of culture and creative industries, and is home to many international and regional television and radio stations. Berlin is also home to two major German-language publishing houses, and is an important center of the European and German film industry. The city is also known for its nightlife, with many clubs and festivals, such as the Berlin International Film Festival, the Karneval der Kulturen, and the Christopher Street Day. Berlin is also home to the largest gay fetish festivals in Europe.
Thought:The human may want more specific information about certain aspects of Berlin's arts and culture scene. 

Action:
\`\`\`
{
  "action": "Wikipedia Tool",
  "action\_input": {
    "pages": \["Culture in Berlin"\],
    "query\_str": "What are some notable museums in Berlin?"
  }
}
\`\`\`

Observation: 
Some notable museums in Berlin include the Deutsches Historisches Museum, the Bauhaus Archive, the Jewish Museum, the German Museum of Technology, the Museum für Naturkunde, the Museum of Asian Art, the Ethnological Museum, the Museum of European Cultures, the Allied Museum, the Brücke Museum, the Stasi Museum, the Beate Uhse Erotic Museum, and the Pergamon Museum.
Thought:The human may also be interested in learning about the music scene in Berlin.

Action:
\`\`\`
{
  "action": "Wikipedia Tool",
  "action\_input": {
    "pages": \["Music in Berlin"\],
    "query\_str": "What is the music scene like in Berlin?"
  }
}
\`\`\`

Observation: 
The music scene in Berlin is vibrant and diverse. It is home to many nightclubs, including Kunst Haus Tacheles, Cookies, Tresor, WMF, Ufo, E-Werk, KitKatClub and Berghain, which are known for their long parties. It is also home to many concert music institutions, such as the Berlin Philharmonic Orchestra, the Konzerthausorchester Berlin, the Berlin Radio Symphony Orchestra, the Staatskapelle Berlin, and the SO36 in Kreuzberg. The city is also known for its influence on rock music, with bands like U2 recording at Hansa Studios near the Berlin Wall. Additionally, Berlin is home to many creative industries, such as music, film, advertising, architecture, art, design, fashion, performing arts, publishing, TV, radio, and video games. It is also home to many important musical figures, such as Johann Joachim Quantz, Carl Philipp Emanuel Bach, the Graun brothers, Wilhelm Friedemann Bach, Carl Friedrich Christian Fasch, Johann Friedrich Reichardt, Carl Friedrich Zelter, Friedrich Heinrich Himmel, Vincenzo Righini, Felix Mendelssohn Bartholdy, Spontini, Meyerbeer, Richard Strauss, Arnold Schoenberg, Friedrich Wilhelm Marpurg, Johann Philipp Kirnberger, Reichardt, E. T. A. Hoffmann, Ludwig Rellstab, and A. B. Marx. There are also three major opera houses in Berlin: the Deutsche Oper, the Berlin State Opera, and the Komische Oper.
Thought:The human may want to know more about the theater scene in Berlin.

Action:
\`\`\`
{
  "action": "Wikipedia Tool",
  "action\_input": {
    "pages": \["Theatre in Berlin"\],
    "query\_str": "What is the theater scene like in Berlin?"
  }
}
\`\`\`

Observation: 
The theater scene in Berlin is vibrant and diverse. There are a variety of venues, from traditional theaters to modern cinemas, as well as a range of genres and styles. The Berlin Wintergarten theatre, which opened in 1887 and was destroyed during the Second World War, was the first Bioscop movie theater in history. The theatre was restarted, relocated and the title licensed in 1992, and is now located on Potsdamer Straße just South of Potsdamer Platz in Berlin. There are also many other theaters in the city, including the Berliner Ensemble, the Volksbühne, and the Schaubühne.
Thought:The human may want to know more about the street art scene in Berlin.

Action:
\`\`\`
{
  "action": "Wikipedia Tool",
  "action\_input": {
    "pages": \["Street art in Berlin"\],
    "query\_str": "What is the street art scene like in Berlin?"
  }
}
\`\`\`

Observation: 
The street art scene in Berlin is vibrant and diverse. It has been home to street artists such as Thierry Noir Tavar Zawacki a.k.a. ABOVE and SP 38, and post-communism, cheap rents, and ramshackle buildings have given rise to street art in areas such as Mitte, Prenzlauer Berg, Kreuzberg, and Friedrichshain. In 2016, StreetArtNews initiated an urban artwork in the name of Urban Nation Berlin, in which several famous artists participated. Street art by Bleepsgr, whose work has been categorized as "artivism", can be found in neighborhoods such as Psiri.
Thought:The human may want to know more about the film industry in Berlin.

Action:
\`\`\`
{
  "action": "Wikipedia Tool",
  "action\_input": {
    "pages": \["Cinema of Germany"\],
    "query\_str": "What is the film industry like in Berlin?"
  }
}
\`\`\`

Observation: 
The film industry in Berlin is thriving and has a long history. It is home to the Berlin International Film Festival, the Deutsche Filmakademie, and several film schools. Berlin is also home to many prominent personalities in the film industry, such as Dieter Kosslick, director of the Berlin International Film Festival, and Fritz Lang, a renowned director. The city is also home to several production companies, and is a major hub for the German film industry. Berlin is known for its diverse range of films, from silent films to contemporary works, and is a major center for the production of both feature films and television series.
Thought:The human may want to know more about the literature scene in Berlin.

Action:
\`\`\`
{
  "action": "Wikipedia Tool",
  "action\_input": {
    "pages": \["Literature in Berlin"\],
    "query\_str": "What is the literature scene like in Berlin?"
  }
}
\`\`\`

Observation: 
The literature scene in Berlin is quite diverse and vibrant. There are a variety of literary genres represented in the city, from poetry to prose to children's literature. Berlin is home to a number of literary festivals, book fairs, and other events that celebrate the written word. There are also a number of independent bookstores, libraries, and other literary institutions that promote the reading and writing of literature. Berlin is also home to a number of renowned authors, including Nobel Prize winners Günter Grass and Herta Müller.
Thought:The human may want to know more about the architecture scene in Berlin.

Action:
\`\`\`
{
  "action": "Wikipedia Tool",
  "action\_input": {
    "pages": \["Architecture in Berlin"\],
    "query\_str": "What is the architecture scene like in Berlin?"
  }
}
\`\`\`

Observation: 
Berlin's architecture scene is incredibly diverse and eclectic. The city has been shaped by its history, with each of the governments based in Berlin initiating ambitious construction programs that have left their distinct mark on the city. There are many Plattenbauten in Eastern Berlin, as well as the iconic East Side Gallery, Fernsehturm, Gendarmenmarkt, Museum Island, Unter den Linden, Brandenburg Gate, Potsdamer Platz, Hackescher Markt, Straße des 17. Juni, Kurfürstendamm, Schloss Bellevue, and Funkturm Berlin. These landmarks are a mix of classical, modern, and postmodern architecture, and many of them have been restored after suffering damage during World War II.
Thought:The human may want to know more about the fashion scene in Berlin.

Action:
\`\`\`
{
  "action": "Wikipedia Tool",
  "action\_input": {
    "pages": \["Fashion in Berlin"\],
    "query\_str": "What is the fashion scene like in Berlin?"
  }
}
\`\`\`

Observation: 
The fashion scene in Berlin is vibrant and creative, with many young designers flourishing in the fashion capital. Mercedes-Benz is the main sponsor of the fashion week, which takes place twice a year in January and July. There are a variety of fashion fairs, such as BREAD & BUTTER, Premium Fair, Bright Tradeshow, (capsule), Show&Order, PanoramaBerlin and The Gallery Berlin. The StyleNite by Berlin-based designer Michael Michalsky is a popular event, featuring unusual performances of different art disciplines combined with state-of-the-art fashion. Models of all ages and abilities are featured in the shows, including disabled models and models aged over 60.
Thought:The human may want to know more about the food scene in Berlin.

Action:
\`\`\`
{
  "action": "Wikipedia Tool",
  "action\_input": {
    "pages": \["Cuisine of Berlin"\],
    "query\_str": "What is the food scene like in Berlin?"
  }
}
\`\`\`

Observation: 
The food scene in Berlin is very diverse and international. It is home to a wide variety of cuisines, including German, Turkish, Arab, Vietnamese, Chinese, Thai, Indian, Korean, Japanese, Spanish, Italian, and Greek. There are numerous restaurants, pubs, bakeries, and delicatessen markets, as well as fast-food versions of the doner kebab sandwich. Berlin is also well known for its vegetarian and vegan cuisine, innovative food scene, pop-up street food markets, supper clubs, and food festivals. Additionally, there are seven restaurants that have been awarded two Michelin stars and 14 restaurants that have been awarded one Michelin star.
Thought:The human may want to know more about the dance scene in Berlin.

Action:
\`\`\`
{
  "action": "Wikipedia Tool",
  "action\_input": {
    "pages": \["Dance in Germany"\],
    "query\_str": "What is the dance scene like in Berlin?"
  }
}
\`\`\`

/Users/jerryliu/Programming/gpt\_index/.venv/lib/python3.10/site-packages/wikipedia/wikipedia.py:389: GuessedAtParserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.

The code that caused this warning is on line 389 of the file /Users/jerryliu/Programming/gpt\_index/.venv/lib/python3.10/site-packages/wikipedia/wikipedia.py. To get rid of this warning, pass the additional argument 'features="lxml"' to the BeautifulSoup constructor.

  lis = BeautifulSoup(html).find\_all('li')

\---------------------------------------------------------------------------
DisambiguationError                       Traceback (most recent call last)
Cell In\[12\], line 1
\----> 1 agent.run("Tell me about the arts and culture of Berlin")

File ~/Programming/gpt\_index/.venv/lib/python3.10/site-packages/langchain/chains/base.py:236, in Chain.run(self, callbacks, \*args, \*\*kwargs)
    234     if len(args) != 1:
    235         raise ValueError("\`run\` supports only one positional argument.")
\--> 236     return self(args\[0\], callbacks\=callbacks)\[self.output\_keys\[0\]\]
    238 if kwargs and not args:
    239     return self(kwargs, callbacks\=callbacks)\[self.output\_keys\[0\]\]

File ~/Programming/gpt\_index/.venv/lib/python3.10/site-packages/langchain/chains/base.py:140, in Chain.\_\_call\_\_(self, inputs, return\_only\_outputs, callbacks)
    138 except (KeyboardInterrupt, Exception) as e:
    139     run\_manager.on\_chain\_error(e)
\--> 140     raise e
    141 run\_manager.on\_chain\_end(outputs)
    142 return self.prep\_outputs(inputs, outputs, return\_only\_outputs)

File ~/Programming/gpt\_index/.venv/lib/python3.10/site-packages/langchain/chains/base.py:134, in Chain.\_\_call\_\_(self, inputs, return\_only\_outputs, callbacks)
    128 run\_manager \= callback\_manager.on\_chain\_start(
    129     {"name": self.\_\_class\_\_.\_\_name\_\_},
    130     inputs,
    131 )
    132 try:
    133     outputs \= (
\--> 134         self.\_call(inputs, run\_manager\=run\_manager)
    135         if new\_arg\_supported
    136         else self.\_call(inputs)
    137     )
    138 except (KeyboardInterrupt, Exception) as e:
    139     run\_manager.on\_chain\_error(e)

File ~/Programming/gpt\_index/.venv/lib/python3.10/site-packages/langchain/agents/agent.py:951, in AgentExecutor.\_call(self, inputs, run\_manager)
    949 \# We now enter the agent loop (until it returns something).
    950 while self.\_should\_continue(iterations, time\_elapsed):
\--> 951     next\_step\_output \= self.\_take\_next\_step(
    952 name\_to\_tool\_map,
    953 color\_mapping,
    954 inputs,
    955 intermediate\_steps,
    956 run\_manager\=run\_manager,
    957 )
    958     if isinstance(next\_step\_output, AgentFinish):
    959         return self.\_return(
    960             next\_step\_output, intermediate\_steps, run\_manager\=run\_manager
    961         )

File ~/Programming/gpt\_index/.venv/lib/python3.10/site-packages/langchain/agents/agent.py:818, in AgentExecutor.\_take\_next\_step(self, name\_to\_tool\_map, color\_mapping, inputs, intermediate\_steps, run\_manager)
    816         tool\_run\_kwargs\["llm\_prefix"\] \= ""
    817     \# We then call the tool on the tool input to get an observation
\--> 818     observation \= tool.run(
    819 agent\_action.tool\_input,
    820 verbose\=self.verbose,
    821 color\=color,
    822 callbacks\=run\_manager.get\_child() if run\_manager else None,
    823 \*\*tool\_run\_kwargs,
    824 )
    825 else:
    826     tool\_run\_kwargs \= self.agent.tool\_run\_logging\_kwargs()

File ~/Programming/gpt\_index/.venv/lib/python3.10/site-packages/langchain/tools/base.py:255, in BaseTool.run(self, tool\_input, verbose, start\_color, color, callbacks, \*\*kwargs)
    253 except (Exception, KeyboardInterrupt) as e:
    254     run\_manager.on\_tool\_error(e)
\--> 255     raise e
    256 run\_manager.on\_tool\_end(str(observation), color\=color, name\=self.name, \*\*kwargs)
    257 return observation

File ~/Programming/gpt\_index/.venv/lib/python3.10/site-packages/langchain/tools/base.py:249, in BaseTool.run(self, tool\_input, verbose, start\_color, color, callbacks, \*\*kwargs)
    246 try:
    247     tool\_args, tool\_kwargs \= self.\_to\_args\_and\_kwargs(parsed\_input)
    248     observation \= (
\--> 249         self.\_run(\*tool\_args, run\_manager\=run\_manager, \*\*tool\_kwargs)
    250         if new\_arg\_supported
    251         else self.\_run(\*tool\_args, \*\*tool\_kwargs)
    252     )
    253 except (Exception, KeyboardInterrupt) as e:
    254     run\_manager.on\_tool\_error(e)

File ~/Programming/gpt\_index/.venv/lib/python3.10/site-packages/langchain/tools/base.py:436, in StructuredTool.\_run(self, run\_manager, \*args, \*\*kwargs)
    427 """Use the tool."""
    428 new\_argument\_supported \= signature(self.func).parameters.get("callbacks")
    429 return (
    430     self.func(
    431         \*args,
    432         callbacks\=run\_manager.get\_child() if run\_manager else None,
    433         \*\*kwargs,
    434     )
    435     if new\_argument\_supported
\--> 436     else self.func(\*args, \*\*kwargs)
    437 )

File ~/Programming/gpt\_index/llama\_index/tools/ondemand\_loader\_tool.py:114, in OnDemandLoaderTool.\_\_call\_\_(self, \*args, \*\*kwargs)
    112 else:
    113     query\_str \= kwargs.pop(self.\_query\_str\_kwargs\_key)
\--> 114 docs \= self.\_reader.load\_data(\*args, \*\*kwargs)
    115 index \= self.\_index\_cls.from\_documents(docs, \*\*self.\_index\_kwargs)
    116 \# TODO: add query kwargs

File ~/Programming/gpt\_index/llama\_index/readers/wikipedia.py:35, in WikipediaReader.load\_data(self, pages, \*\*load\_kwargs)
     33 results \= \[\]
     34 for page in pages:
\---> 35     page\_content \= wikipedia.page(page, \*\*load\_kwargs).content
     36     results.append(Document(page\_content))
     37 return results

File ~/Programming/gpt\_index/.venv/lib/python3.10/site-packages/wikipedia/wikipedia.py:276, in page(title, pageid, auto\_suggest, redirect, preload)
    273     except IndexError:
    274       \# if there is no suggestion or search results, the page doesn't exist
    275       raise PageError(title)
\--> 276   return WikipediaPage(title, redirect\=redirect, preload\=preload)
    277 elif pageid is not None:
    278   return WikipediaPage(pageid\=pageid, preload\=preload)

File ~/Programming/gpt\_index/.venv/lib/python3.10/site-packages/wikipedia/wikipedia.py:299, in WikipediaPage.\_\_init\_\_(self, title, pageid, redirect, preload, original\_title)
    296 else:
    297   raise ValueError("Either a title or a pageid must be specified")
\--> 299 self.\_\_load(redirect\=redirect, preload\=preload)
    301 if preload:
    302   for prop in ('content', 'summary', 'images', 'references', 'links', 'sections'):

File ~/Programming/gpt\_index/.venv/lib/python3.10/site-packages/wikipedia/wikipedia.py:393, in WikipediaPage.\_\_load(self, redirect, preload)
    390   filtered\_lis \= \[li for li in lis if not 'tocsection' in ''.join(li.get('class', \[\]))\]
    391   may\_refer\_to \= \[li.a.get\_text() for li in filtered\_lis if li.a\]
\--> 393   raise DisambiguationError(getattr(self, 'title', page\['title'\]), may\_refer\_to)
    395 else:
    396   self.pageid \= pageid

DisambiguationError: "Dance, Dance, Dance" may refer to: 
"Dance, Dance, Dance" (The Beach Boys song)
"Dance, Dance, Dance" (Neil Young song)
"Dance, Dance, Dance" (Yowsah, Yowsah, Yowsah)
"Dance Dance Dance" (James Cottriall song)
"Dance Dance Dance" (E-girls song)
Dance Dance Dance/My Lady
soundtrack
Why Do You Have to Go/Dance, Dance, Dance
Youth Novels
Fly Like an Eagle
Dance Dance Dance (German TV series)
Dance Dance Dance (British TV series)
Dance Dance Dance (novel)
Dance, Dance, Dance: The Best of Chic
Dance, Dance (disambiguation)

In \[ \]:

Copied!

agent.run("Tell me about the critical reception to The Departed")

agent.run("Tell me about the critical reception to The Departed")

\> Entering new AgentExecutor chain...
Action:
\`\`\`
{
  "action": "Wikipedia Tool",
  "action\_input": {
    "pages": \["The Departed"\],
    "query\_str": "critical reception"
  }
}
\`\`\`

Observation: 
The critical reception of The Departed was overwhelmingly positive. On review aggregator Rotten Tomatoes, the film holds a 91% approval rating based on 284 reviews, with an average rating of 8.3/10. The website's critics consensus reads, "Featuring outstanding work from an excellent cast, The Departed is a thoroughly engrossing gangster drama with the gritty authenticity and soupy morality we have come to expect from Martin Scorsese." Metacritic, which uses a weighted average, assigned the film a score of 85 out of 100 based on 39 critics, indicating "universal acclaim". Audiences polled by CinemaScore gave the film an average grade of "A−" on an A+ to F scale. Entertainment Weekly ranked it on its end-of-the-decade "Best of" list, saying: "If they're lucky, directors make one classic film in their career. Martin Scorsese has one per decade (Taxi Driver in the '70s, Raging Bull in the '80s, Goodfellas in the '90s). His 2006 Irish Mafia masterpiece kept the streak alive." Roger Ebert gave the film four stars out of four, praising Scorsese for thematically differentiating his film from the original. Online critic James Berardinelli awarded the film four stars out of four, praising it as "an American epic tragedy." He went on to claim that the film deserves to be ranked alongside Scorsese's past successes, including Taxi Driver, Raging Bull and Goodfellas.
Thought:The critical reception to The Departed was very positive. 
Action:
\`\`\`
{
  "action": "Final Answer",
  "action\_input": "The critical reception to The Departed was overwhelmingly positive, with an approval rating of 91% on Rotten Tomatoes and a score of 85 out of 100 on Metacritic. It was praised for its outstanding cast, gritty authenticity, and soupy morality. Many critics ranked it alongside Scorsese's past successes, including Taxi Driver, Raging Bull, and Goodfellas."
}
\`\`\`

\> Finished chain.

Out\[ \]:

"The critical reception to The Departed was overwhelmingly positive, with an approval rating of 91% on Rotten Tomatoes and a score of 85 out of 100 on Metacritic. It was praised for its outstanding cast, gritty authenticity, and soupy morality. Many critics ranked it alongside Scorsese's past successes, including Taxi Driver, Raging Bull, and Goodfellas."

Back to top

[Previous You.com Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/you_retriever/)[Next Azure Code Interpreter Tool Spec](https://docs.llamaindex.ai/en/stable/examples/tools/azure_code_interpreter/)
