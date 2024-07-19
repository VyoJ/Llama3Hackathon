Title: VideoDB Retriever - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/retrievers/videodb_retriever/

Markdown Content:
VideoDB Retriever - LlamaIndex


### RAG: Instantly Search and Stream Video Results 📺[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/videodb_retriever/#rag-instantly-search-and-stream-video-results)

> [VideoDB](https://videodb.io/) is a serverless database designed to streamline the storage, search, editing, and streaming of video content. VideoDB offers random access to sequential video data by building indexes and developing interfaces for querying and browsing video content. Learn more at [docs.videodb.io](https://docs.videodb.io/).

Constructing a RAG pipeline for text is relatively straightforward, thanks to the tools developed for parsing, indexing, and retrieving text data. However, adapting RAG models for video content presents a greater challenge. Videos combine visual, auditory, and textual elements, requiring more processing power and sophisticated video pipelines.

While Large Language Models (LLMs) excel with text, they fall short in helping you consume or create video clips. VideoDB provides a sophisticated database abstraction for your MP4 files, enabling the use of LLMs on your video data. With VideoDB, you can not only analyze but also `instantly watch video streams` of your search results.

In this notebook, we introduce `VideoDBRetriever`, a tool specifically designed to simplify the creation of RAG pipelines for video content, without any hassle of dealing with complex video infrastructure.

🛠️️ Setup connection[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/videodb_retriever/#setup-connection)
----------------------------------------------------------------------------------------------------------------------

### Requirements[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/videodb_retriever/#requirements)

To connect to VideoDB, simply get the API key and create a connection. This can be done by setting the `VIDEO_DB_API_KEY` environment variable. You can get it from 👉🏼 [VideoDB Console](https://console.videodb.io/). ( Free for first 50 uploads, **No credit card required!** )

Get your `OPENAI_API_KEY` from OpenAI platform for `llama_index` response synthesizer.

In \[ \]:

Copied!

import os

os.environ\["OPENAI\_API\_KEY"\] \= ""
os.environ\["VIDEO\_DB\_API\_KEY"\] \= ""

import os os.environ\["OPENAI\_API\_KEY"\] = "" os.environ\["VIDEO\_DB\_API\_KEY"\] = ""

### Installing Dependencies[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/videodb_retriever/#installing-dependencies)

To get started, we'll need to install the following packages:

*   `llama-index`
*   `llama-index-retrievers-videodb`
*   `videodb`

In \[ \]:

Copied!

%pip install llama\-index
%pip install videodb

%pip install llama-index %pip install videodb

In \[ \]:

Copied!

%pip install llama\-index\-retrievers\-videodb

%pip install llama-index-retrievers-videodb

### Data Ingestion[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/videodb_retriever/#data-ingestion)

Let's upload a few video files first. You can use any `public url`, `Youtube link` or `local file` on your system. First 50 uploads are free!

In \[ \]:

Copied!

from videodb import connect

\# connect to VideoDB
conn \= connect()

\# upload videos to default collection in VideoDB
print("uploading first video")
video1 \= conn.upload(url\="https://www.youtube.com/watch?v=lsODSDmY4CY")
print("uploading second video")
video2 \= conn.upload(url\="https://www.youtube.com/watch?v=vZ4kOr38JhY")

from videodb import connect # connect to VideoDB conn = connect() # upload videos to default collection in VideoDB print("uploading first video") video1 = conn.upload(url="https://www.youtube.com/watch?v=lsODSDmY4CY") print("uploading second video") video2 = conn.upload(url="https://www.youtube.com/watch?v=vZ4kOr38JhY")

> *   `coll = conn.get_collection()` : Returns default collection object.
> *   `coll.get_videos()` : Returns list of all the videos in a collections.
> *   `coll.get_video(video_id)`: Returns Video object from given`video_id`.

### Indexing[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/videodb_retriever/#indexing)

To search bits inside a video, you have to index the video first. We have two types of indexing possible for a video.

*   `index_spoken_words`: Indexes spoken words in the video.
*   `index_scenes`: Indexes visuals of the video. `(Note: This feature is currently available only for beta users, join our discord for early access)` [https://discord.gg/py9P639jGz](https://discord.gg/py9P639jGz)

In \[ \]:

Copied!

print("Indexing the videos...")
video1.index\_spoken\_words()
video2.index\_spoken\_words()

print("Indexing the videos...") video1.index\_spoken\_words() video2.index\_spoken\_words()

Indexing the videos...

100%|████████████████████████████████████████████████████████████████████████████████████████████████████| 100/100 \[00:39<00:00,  2.56it/s\]                                                
100%|████████████████████████████████████████████████████████████████████████████████████████████████████| 100/100 \[00:39<00:00,  2.51it/s\]                                                

### Querying[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/videodb_retriever/#querying)

Now that the videos are indexed, we can use `VideoDBRetriever` to fetch relevant nodes from VideoDB.

In \[ \]:

Copied!

from llama\_index.retrievers.videodb import VideoDBRetriever
from llama\_index.core import get\_response\_synthesizer
from llama\_index.core.query\_engine import RetrieverQueryEngine

from llama\_index.retrievers.videodb import VideoDBRetriever from llama\_index.core import get\_response\_synthesizer from llama\_index.core.query\_engine import RetrieverQueryEngine

In \[ \]:

Copied!

\# VideoDBRetriever by default uses the default collection in the VideoDB
retriever \= VideoDBRetriever()

\# use your llama\_index response\_synthesizer on search results.
response\_synthesizer \= get\_response\_synthesizer()

query\_engine \= RetrieverQueryEngine(
    retriever\=retriever,
    response\_synthesizer\=response\_synthesizer,
)

\# VideoDBRetriever by default uses the default collection in the VideoDB retriever = VideoDBRetriever() # use your llama\_index response\_synthesizer on search results. response\_synthesizer = get\_response\_synthesizer() query\_engine = RetrieverQueryEngine( retriever=retriever, response\_synthesizer=response\_synthesizer, )

In \[ \]:

Copied!

\# query across all uploaded videos to get the text answer.
response \= query\_engine.query("What is Dopamine?")
print(response)

\# query across all uploaded videos to get the text answer. response = query\_engine.query("What is Dopamine?") print(response)

Dopamine is a neurotransmitter that plays a key role in various brain functions, including motivation, reward, and pleasure. It is involved in regulating mood, movement, and cognitive function.

In \[ \]:

Copied!

response \= query\_engine.query("What's the benefit of morning sunlight?")
print(response)

response = query\_engine.query("What's the benefit of morning sunlight?") print(response)

Morning sunlight can help trigger a cortisol pulse shift, allowing individuals to capture a morning work block by waking up early and exposing themselves to sunlight. This exposure to morning sunlight, along with brief high-intensity exercise, can assist in adjusting the cortisol levels and potentially enhancing productivity during the early hours of the day.

Watch Video Stream of Search Result[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/videodb_retriever/#watch-video-stream-of-search-result)
-------------------------------------------------------------------------------------------------------------------------------------------------------

Although, The `Nodes` returned by Retriever are of type `TextNode`. They also have metadata that can help you `watch the video stream` of results. You can create a compilation of all Nodes using VideoDB's [Programmable video streams](https://docs.videodb.io/version-0-0-3-timeline-and-assets-44). You can even modify it with Audio and Image overlays easily.

![Image 4: Timeline](https://codaio.imgix.net/docs/_s5lUnUCIU/blobs/bl-n4vT_dFztl/e664f43dbd4da89c3a3bfc92e3224c8a188eb19d2d458bebe049e780f72506ca6b19421c7168205f7ad307187e73da60c73cdbb9a0ef3fec77cc711927ad26a29a92cd13691fa9375c231f1c006853bacf28e09b3bf0bbcb5f7b76462b354a180fb437ad?auto=format%2Ccompress&fit=max)

In \[ \]:

Copied!

from videodb import connect, play\_stream
from videodb.timeline import Timeline
from videodb.asset import VideoAsset

from videodb import connect, play\_stream from videodb.timeline import Timeline from videodb.asset import VideoAsset

In \[ \]:

Copied!

\# create video stream of search results
conn \= connect()
timeline \= Timeline(conn)

relevant\_nodes \= retriever.retrieve("What's the benefit of morning sunlight?")

for node\_obj in relevant\_nodes:
    node \= node\_obj.node
    \# create a video asset for each node
    node\_asset \= VideoAsset(
        asset\_id\=node.metadata\["video\_id"\],
        start\=node.metadata\["start"\],
        end\=node.metadata\["end"\],
    )
    \# add the asset to timeline
    timeline.add\_inline(node\_asset)

\# generate stream for the compiled timeline
stream\_url \= timeline.generate\_stream()
play\_stream(stream\_url)

\# create video stream of search results conn = connect() timeline = Timeline(conn) relevant\_nodes = retriever.retrieve("What's the benefit of morning sunlight?") for node\_obj in relevant\_nodes: node = node\_obj.node # create a video asset for each node node\_asset = VideoAsset( asset\_id=node.metadata\["video\_id"\], start=node.metadata\["start"\], end=node.metadata\["end"\], ) # add the asset to timeline timeline.add\_inline(node\_asset) # generate stream for the compiled timeline stream\_url = timeline.generate\_stream() play\_stream(stream\_url)

Out\[ \]:

'https://console.videodb.io/player?url=https://stream.videodb.io/v3/published/manifests/9c39c8a9-62a2-4b5e-b15d-8565cc58c8ae.m3u8'

### Configuring `VideoDBRetriever`[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/videodb_retriever/#configuring-videodbretriever)

**1\. Retriever for only one Video**: You can pass the `id` of the video object to search in only that video.

VideoDBRetriever(video\="my\_video.id")

**2\. Retriever for different type of Indexes**:

\# VideoDBRetriever that uses keyword search - Matches exact occurence of words and sentences. It only supports single video. 
keyword\_retriever \= VideoDBRetriever(search\_type\="keyword", video\="my\_video.id")

\# VideoDBRetriever that uses semantic search - Perfect for question answers type of query.
semantic\_retriever \= VideoDBRetriever(search\_type\="semantic")

\# \[only for beta users of VideoDB\] VideoDBRetriever that uses scene search - Search visual information in the videos.
visual\_retriever \= VideoDBRetriever(search\_type\="scene")

**3\. Configure threshold parameters**:

*   `result_threshold`: is the threshold for number of results returned by retriever; the default value is `5`
*   `score_threshold`: only nodes with score higher than `score_threshold` will be returned by retriever; the default value is `0.2`

custom\_retriever \= VideoDBRetriever(result\_threshold\=2, score\_threshold\=0.5)

### View Specific Node[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/videodb_retriever/#view-specific-node)

To watch stream of each retrieved node, you can directly generate the stream of that part directly from `video` object of VideoDB.

In \[ \]:

Copied!

relevant\_nodes

relevant\_nodes

Out\[ \]:

\[NodeWithScore(node=TextNode(id\_='6ca84002-49df-4091-901d-48248dbe0977', embedding=None, metadata={'collection\_id': 'c-33978c87-33e6-4259-9e27-a9edc79be9ad', 'video\_id': 'm-f201ff7c-88ec-47ca-938b-a4e968676ba0', 'length': '1496.711837', 'title': 'AMA #1: Leveraging Ultradian Cycles, How to Protect Your Brain, Seed Oils Examined and More', 'start': 906.01, 'end': 974.59}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text=" So for somebody that wants to learn an immense amount of material, or who has the opportunity to capture another Altradian cycle, the other time where that tends to occur is also early days. So some people, by waking up early and using stimulants like caffeine and hydration or some brief high intensity city exercise, can trigger that cortisol pulse to shift a little bit earlier so that they can capture a morning work block that occurs somewhere, let's say between six and 07:30 a.m. So let's think about our typical person, at least in my example, that's waking up around 07:00 a.m. And then I said, has their first Altradian work cycle really flip on? Because that bump in cortisol around 930 or 10:00 a.m. If that person were, say, to. Set their alarm clock for 05:30 a.m. Then get up, get some artificial light. If the sun isn't out, turn on bright artificial lights. Or if the sun happens to be up that time of year, get some sunlight in your eyes. But irrespective of sunlight, were to get a little bit of brief, high intensity exercise, maybe ten or 15 minutes of skipping rope or even just jumping jacks or go out for a brief jog.", start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.440981567),
 NodeWithScore(node=TextNode(id\_='2244fd64-121e-4699-ba36-f0f6a110750f', embedding=None, metadata={'collection\_id': 'c-33978c87-33e6-4259-9e27-a9edc79be9ad', 'video\_id': 'm-eae54005-b5ca-44f1-9c31-fcdb2f1db56a', 'length': '1830.498685', 'title': 'AMA #2: Improve Sleep, Reduce Sugar Cravings, Optimal Protein Intake, Stretching Frequency & More', 'start': 899.772, 'end': 977.986}, excluded\_embed\_metadata\_keys=\[\], excluded\_llm\_metadata\_keys=\[\], relationships={}, text=" Because the study, as far as I know, has not been done. Whether or not doing resistance training or some other type of exercise would have led to the same effect. Although I have to imagine that if it's moderately intense to intense resistance training, provided it's done far enough away from going to sleep right prior to 6 hours before sleep, that one ought to see the same effects, although that was not a condition in this study. But it's a very nice study. They looked at everything from changes in core body temperature to caloric expenditure. They didn't see huge changes in core body temperature changes, so that couldn't explain the effect. It really appears that the major effect of improving slow wave sleep was due to something in changing the fine structure of the brainwaves that occur during slow wave sleep. In fact, and this is an important point. The subjects in this study did not report subjectively feeling that much better from their sleep. So you might say, well then, why would I even want to bother? However, it's well known that getting sufficient slow wave sleep is important not just for repair, excuse me, for repair of bodily tissues, but also for repair of brain tissues and repair and washout of debris in the brain. And that debris is known to lead to things like dementia.", start\_char\_idx=None, end\_char\_idx=None, text\_template='{metadata\_str}\\n\\n{content}', metadata\_template='{key}: {value}', metadata\_seperator='\\n'), score=0.282342136)\]

In \[ \]:

Copied!

from videodb import connect

\# retriever = VideoDBRetriever()
\# relevant\_nodes = retriever.retrieve("What is Dopamine?")

video\_node \= relevant\_nodes\[0\].node
conn \= connect()
coll \= conn.get\_collection()

video \= coll.get\_video(video\_node.metadata\["video\_id"\])
start \= video\_node.metadata\["start"\]
end \= video\_node.metadata\["end"\]

stream\_url \= video.generate\_stream(timeline\=\[(start, end)\])
play\_stream(stream\_url)

from videodb import connect # retriever = VideoDBRetriever() # relevant\_nodes = retriever.retrieve("What is Dopamine?") video\_node = relevant\_nodes\[0\].node conn = connect() coll = conn.get\_collection() video = coll.get\_video(video\_node.metadata\["video\_id"\]) start = video\_node.metadata\["start"\] end = video\_node.metadata\["end"\] stream\_url = video.generate\_stream(timeline=\[(start, end)\]) play\_stream(stream\_url)

Out\[ \]:

'https://console.videodb.io/player?url=https://stream.videodb.io/v3/published/manifests/b7201145-7302-4ec5-b87c-d1a4c6592f69.m3u8'

🧹 Cleanup[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/videodb_retriever/#cleanup)
--------------------------------------------------------------------------------------------------

In \[ \]:

Copied!

video1.delete()
video2.delete()

video1.delete() video2.delete()

👨‍👩‍👧‍👦 Support & Community[¶](https://docs.llamaindex.ai/en/stable/examples/retrievers/videodb_retriever/#support-community)
---------------------------------------------------------------------------------------------------------------------------------

Leveraging the capabilities of automation and AI-driven content understanding, the possibilities for creation and repurposing of your content are boundless with VideoDB.

If you have any questions or feedback. Feel free to reach out to us 🙌🏼

*   [Discord](https://discord.gg/py9P639jGz)
*   [GitHub](https://github.com/video-db)
*   [VideoDB](https://videodb.io/)
*   [Email](mailto:ashu@videodb.io)

Back to top

[Previous Auto-Retrieval from a Vectara Index](https://docs.llamaindex.ai/en/stable/examples/retrievers/vectara_auto_retriever/)[Next You.com Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/you_retriever/)
