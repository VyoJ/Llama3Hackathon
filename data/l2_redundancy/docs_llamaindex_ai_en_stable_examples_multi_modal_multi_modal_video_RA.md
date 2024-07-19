Title: Multimodal RAG for processing videos using OpenAI GPT4V and LanceDB vectorstore

URL Source: https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_video_RAG/

Markdown Content:
Multimodal RAG for processing videos using OpenAI GPT4V and LanceDB vectorstore - LlamaIndex


In this notebook, we showcase a Multimodal RAG architecture designed for video processing. We utilize OpenAI GPT4V MultiModal LLM class that employs [CLIP](https://github.com/openai/CLIP) to generate multimodal embeddings. Furthermore, we use [LanceDBVectorStore](https://docs.llamaindex.ai/en/latest/examples/vector_stores/LanceDBIndexDemo.html#) for efficient vector storage.

Steps:

1.  Download video from YouTube, process and store it.
    
2.  Build Multi-Modal index and vector store for both texts and images.
    
3.  Retrieve relevant images and context, use both to augment the prompt.
    
4.  Using GPT4V for reasoning the correlations between the input query and augmented data and generating final response.
    

In \[ \]:

Copied!

%pip install llama\-index\-vector\-stores\-lancedb
%pip install llama\-index\-multi\-modal\-llms\-openai

%pip install llama-index-vector-stores-lancedb %pip install llama-index-multi-modal-llms-openai

In \[ \]:

Copied!

%pip install llama\-index\-multi\-modal\-llms\-openai
%pip install llama\-index\-vector\-stores\-lancedb
%pip install llama\-index\-embeddings\-clip

%pip install llama-index-multi-modal-llms-openai %pip install llama-index-vector-stores-lancedb %pip install llama-index-embeddings-clip

In \[ \]:

Copied!

%pip install llama\_index ftfy regex tqdm
%pip install \-U openai\-whisper
%pip install git+https://github.com/openai/CLIP.git
%pip install torch torchvision
%pip install matplotlib scikit\-image
%pip install lancedb
%pip install moviepy
%pip install pytube
%pip install pydub
%pip install SpeechRecognition
%pip install ffmpeg\-python
%pip install soundfile

%pip install llama\_index ftfy regex tqdm %pip install -U openai-whisper %pip install git+https://github.com/openai/CLIP.git %pip install torch torchvision %pip install matplotlib scikit-image %pip install lancedb %pip install moviepy %pip install pytube %pip install pydub %pip install SpeechRecognition %pip install ffmpeg-python %pip install soundfile

In \[ \]:

Copied!

from moviepy.editor import VideoFileClip
from pathlib import Path
import speech\_recognition as sr
from pytube import YouTube
from pprint import pprint

from moviepy.editor import VideoFileClip from pathlib import Path import speech\_recognition as sr from pytube import YouTube from pprint import pprint

In \[ \]:

Copied!

import os

OPENAI\_API\_KEY \= ""
os.environ\["OPENAI\_API\_KEY"\] \= OPENAI\_API\_KEY

import os OPENAI\_API\_KEY = "" os.environ\["OPENAI\_API\_KEY"\] = OPENAI\_API\_KEY

#### Set configuration for input below[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_video_RAG/#set-configuration-for-input-below)

In \[ \]:

Copied!

video\_url \= "https://www.youtube.com/watch?v=d\_qvLDhkg00"
output\_video\_path \= "./video\_data/"
output\_folder \= "./mixed\_data/"
output\_audio\_path \= "./mixed\_data/output\_audio.wav"

filepath \= output\_video\_path + "input\_vid.mp4"
Path(output\_folder).mkdir(parents\=True, exist\_ok\=True)

video\_url = "https://www.youtube.com/watch?v=d\_qvLDhkg00" output\_video\_path = "./video\_data/" output\_folder = "./mixed\_data/" output\_audio\_path = "./mixed\_data/output\_audio.wav" filepath = output\_video\_path + "input\_vid.mp4" Path(output\_folder).mkdir(parents=True, exist\_ok=True)

#### Download and process videos into appropriate format for generating/storing embeddings[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_video_RAG/#download-and-process-videos-into-appropriate-format-for-generatingstoring-embeddings)

In \[ \]:

Copied!

from PIL import Image
import matplotlib.pyplot as plt
import os

def plot\_images(image\_paths):
    images\_shown \= 0
    plt.figure(figsize\=(16, 9))
    for img\_path in image\_paths:
        if os.path.isfile(img\_path):
            image \= Image.open(img\_path)

            plt.subplot(2, 3, images\_shown + 1)
            plt.imshow(image)
            plt.xticks(\[\])
            plt.yticks(\[\])

            images\_shown += 1
            if images\_shown \>= 7:
                break

from PIL import Image import matplotlib.pyplot as plt import os def plot\_images(image\_paths): images\_shown = 0 plt.figure(figsize=(16, 9)) for img\_path in image\_paths: if os.path.isfile(img\_path): image = Image.open(img\_path) plt.subplot(2, 3, images\_shown + 1) plt.imshow(image) plt.xticks(\[\]) plt.yticks(\[\]) images\_shown += 1 if images\_shown >= 7: break

In \[ \]:

Copied!

def download\_video(url, output\_path):
    """
    Download a video from a given url and save it to the output path.

    Parameters:
    url (str): The url of the video to download.
    output\_path (str): The path to save the video to.

    Returns:
    dict: A dictionary containing the metadata of the video.
    """
    yt \= YouTube(url)
    metadata \= {"Author": yt.author, "Title": yt.title, "Views": yt.views}
    yt.streams.get\_highest\_resolution().download(
        output\_path\=output\_path, filename\="input\_vid.mp4"
    )
    return metadata

def video\_to\_images(video\_path, output\_folder):
    """
    Convert a video to a sequence of images and save them to the output folder.

    Parameters:
    video\_path (str): The path to the video file.
    output\_folder (str): The path to the folder to save the images to.

    """
    clip \= VideoFileClip(video\_path)
    clip.write\_images\_sequence(
        os.path.join(output\_folder, "frame%04d.png"), fps\=0.2
    )

def video\_to\_audio(video\_path, output\_audio\_path):
    """
    Convert a video to audio and save it to the output path.

    Parameters:
    video\_path (str): The path to the video file.
    output\_audio\_path (str): The path to save the audio to.

    """
    clip \= VideoFileClip(video\_path)
    audio \= clip.audio
    audio.write\_audiofile(output\_audio\_path)

def audio\_to\_text(audio\_path):
    """
    Convert audio to text using the SpeechRecognition library.

    Parameters:
    audio\_path (str): The path to the audio file.

    Returns:
    test (str): The text recognized from the audio.

    """
    recognizer \= sr.Recognizer()
    audio \= sr.AudioFile(audio\_path)

    with audio as source:
        \# Record the audio data
        audio\_data \= recognizer.record(source)

        try:
            \# Recognize the speech
            text \= recognizer.recognize\_whisper(audio\_data)
        except sr.UnknownValueError:
            print("Speech recognition could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from service; {e}")

    return text

def download\_video(url, output\_path): """ Download a video from a given url and save it to the output path. Parameters: url (str): The url of the video to download. output\_path (str): The path to save the video to. Returns: dict: A dictionary containing the metadata of the video. """ yt = YouTube(url) metadata = {"Author": yt.author, "Title": yt.title, "Views": yt.views} yt.streams.get\_highest\_resolution().download( output\_path=output\_path, filename="input\_vid.mp4" ) return metadata def video\_to\_images(video\_path, output\_folder): """ Convert a video to a sequence of images and save them to the output folder. Parameters: video\_path (str): The path to the video file. output\_folder (str): The path to the folder to save the images to. """ clip = VideoFileClip(video\_path) clip.write\_images\_sequence( os.path.join(output\_folder, "frame%04d.png"), fps=0.2 ) def video\_to\_audio(video\_path, output\_audio\_path): """ Convert a video to audio and save it to the output path. Parameters: video\_path (str): The path to the video file. output\_audio\_path (str): The path to save the audio to. """ clip = VideoFileClip(video\_path) audio = clip.audio audio.write\_audiofile(output\_audio\_path) def audio\_to\_text(audio\_path): """ Convert audio to text using the SpeechRecognition library. Parameters: audio\_path (str): The path to the audio file. Returns: test (str): The text recognized from the audio. """ recognizer = sr.Recognizer() audio = sr.AudioFile(audio\_path) with audio as source: # Record the audio data audio\_data = recognizer.record(source) try: # Recognize the speech text = recognizer.recognize\_whisper(audio\_data) except sr.UnknownValueError: print("Speech recognition could not understand the audio.") except sr.RequestError as e: print(f"Could not request results from service; {e}") return text

In \[ \]:

Copied!

try:
    metadata\_vid \= download\_video(video\_url, output\_video\_path)
    video\_to\_images(filepath, output\_folder)
    video\_to\_audio(filepath, output\_audio\_path)
    text\_data \= audio\_to\_text(output\_audio\_path)

    with open(output\_folder + "output\_text.txt", "w") as file:
        file.write(text\_data)
    print("Text data saved to file")
    file.close()
    os.remove(output\_audio\_path)
    print("Audio file removed")

except Exception as e:
    raise e

try: metadata\_vid = download\_video(video\_url, output\_video\_path) video\_to\_images(filepath, output\_folder) video\_to\_audio(filepath, output\_audio\_path) text\_data = audio\_to\_text(output\_audio\_path) with open(output\_folder + "output\_text.txt", "w") as file: file.write(text\_data) print("Text data saved to file") file.close() os.remove(output\_audio\_path) print("Audio file removed") except Exception as e: raise e

#### Create the multi-modal index[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_video_RAG/#create-the-multi-modal-index)

In \[ \]:

Copied!

from llama\_index.core.indices import MultiModalVectorStoreIndex
from llama\_index.core import SimpleDirectoryReader, StorageContext

from llama\_index.core import SimpleDirectoryReader, StorageContext
from llama\_index.vector\_stores.lancedb import LanceDBVectorStore

from llama\_index.core import SimpleDirectoryReader

text\_store \= LanceDBVectorStore(uri\="lancedb", table\_name\="text\_collection")
image\_store \= LanceDBVectorStore(uri\="lancedb", table\_name\="image\_collection")
storage\_context \= StorageContext.from\_defaults(
    vector\_store\=text\_store, image\_store\=image\_store
)

\# Create the MultiModal index
documents \= SimpleDirectoryReader(output\_folder).load\_data()

index \= MultiModalVectorStoreIndex.from\_documents(
    documents,
    storage\_context\=storage\_context,
)

from llama\_index.core.indices import MultiModalVectorStoreIndex from llama\_index.core import SimpleDirectoryReader, StorageContext from llama\_index.core import SimpleDirectoryReader, StorageContext from llama\_index.vector\_stores.lancedb import LanceDBVectorStore from llama\_index.core import SimpleDirectoryReader text\_store = LanceDBVectorStore(uri="lancedb", table\_name="text\_collection") image\_store = LanceDBVectorStore(uri="lancedb", table\_name="image\_collection") storage\_context = StorageContext.from\_defaults( vector\_store=text\_store, image\_store=image\_store ) # Create the MultiModal index documents = SimpleDirectoryReader(output\_folder).load\_data() index = MultiModalVectorStoreIndex.from\_documents( documents, storage\_context=storage\_context, )

#### Use index as retriever to fetch top k (5 in this example) results from the multimodal vector index[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_video_RAG/#use-index-as-retriever-to-fetch-top-k-5-in-this-example-results-from-the-multimodal-vector-index)

In \[ \]:

Copied!

retriever\_engine \= index.as\_retriever(
    similarity\_top\_k\=5, image\_similarity\_top\_k\=5
)

retriever\_engine = index.as\_retriever( similarity\_top\_k=5, image\_similarity\_top\_k=5 )

#### Set the RAG prompt template[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_video_RAG/#set-the-rag-prompt-template)

In \[ \]:

Copied!

import json

metadata\_str \= json.dumps(metadata\_vid)

qa\_tmpl\_str \= (
    "Given the provided information, including relevant images and retrieved context from the video, \\
 accurately and precisely answer the query without any additional prior knowledge.\\n"
    "Please ensure honesty and responsibility, refraining from any racist or sexist remarks.\\n"
    "---------------------\\n"
    "Context: {context\_str}\\n"
    "Metadata for video: {metadata\_str} \\n"
    "---------------------\\n"
    "Query: {query\_str}\\n"
    "Answer: "
)

import json metadata\_str = json.dumps(metadata\_vid) qa\_tmpl\_str = ( "Given the provided information, including relevant images and retrieved context from the video, \\ accurately and precisely answer the query without any additional prior knowledge.\\n" "Please ensure honesty and responsibility, refraining from any racist or sexist remarks.\\n" "---------------------\\n" "Context: {context\_str}\\n" "Metadata for video: {metadata\_str} \\n" "---------------------\\n" "Query: {query\_str}\\n" "Answer: " )

#### Retrieve most similar text/image embeddings baseed on user query from the DB[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_video_RAG/#retrieve-most-similar-textimage-embeddings-baseed-on-user-query-from-the-db)

In \[ \]:

Copied!

from llama\_index.core.response.notebook\_utils import display\_source\_node
from llama\_index.core.schema import ImageNode

def retrieve(retriever\_engine, query\_str):
    retrieval\_results \= retriever\_engine.retrieve(query\_str)

    retrieved\_image \= \[\]
    retrieved\_text \= \[\]
    for res\_node in retrieval\_results:
        if isinstance(res\_node.node, ImageNode):
            retrieved\_image.append(res\_node.node.metadata\["file\_path"\])
        else:
            display\_source\_node(res\_node, source\_length\=200)
            retrieved\_text.append(res\_node.text)

    return retrieved\_image, retrieved\_text

from llama\_index.core.response.notebook\_utils import display\_source\_node from llama\_index.core.schema import ImageNode def retrieve(retriever\_engine, query\_str): retrieval\_results = retriever\_engine.retrieve(query\_str) retrieved\_image = \[\] retrieved\_text = \[\] for res\_node in retrieval\_results: if isinstance(res\_node.node, ImageNode): retrieved\_image.append(res\_node.node.metadata\["file\_path"\]) else: display\_source\_node(res\_node, source\_length=200) retrieved\_text.append(res\_node.text) return retrieved\_image, retrieved\_text

#### Add query now, fetch relevant details including images and augment the prompt template[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_video_RAG/#add-query-now-fetch-relevant-details-including-images-and-augment-the-prompt-template)

In \[ \]:

Copied!

query\_str \= "Using examples from video, explain all things covered in the video regarding the gaussian function"

img, txt \= retrieve(retriever\_engine\=retriever\_engine, query\_str\=query\_str)
image\_documents \= SimpleDirectoryReader(
    input\_dir\=output\_folder, input\_files\=img
).load\_data()
context\_str \= "".join(txt)
plot\_images(img)

query\_str = "Using examples from video, explain all things covered in the video regarding the gaussian function" img, txt = retrieve(retriever\_engine=retriever\_engine, query\_str=query\_str) image\_documents = SimpleDirectoryReader( input\_dir=output\_folder, input\_files=img ).load\_data() context\_str = "".join(txt) plot\_images(img)

**Node ID:** bda08ef1-137c-4d69-9bcc-b7005a41a13c  
**Similarity:** 0.7431071996688843  
**Text:** The basic function underlying a normal distribution, aka a Gaussian, is e to the negative x squared. But you might wonder why this function? Of all the expressions we could dream up that give you s...

**Node ID:** 7d6d0f32-ce16-461b-be54-883241252e50  
**Similarity:** 0.7335695028305054  
**Text:** This step is actually pretty technical, it goes a little beyond what I want to talk about here. Often use these objects called moment generating functions, that gives you a very abstract argument t...

**Node ID:** 519fb788-3927-4842-ad5c-88be61deaf65  
**Similarity:** 0.7069740295410156  
**Text:** The essence of what we want to compute is what the convolution between two copies of this function looks like. If you remember, in the last video, we had two different ways to visualize convolution...

**Node ID:** f265c3fb-3c9f-4f36-aa2a-fb15efff9783  
**Similarity:** 0.706935465335846  
**Text:** This is the important point. All of the stuff that's involving s is now entirely separate from the integrated variable. This remaining integral is a little bit tricky. I did a whole video on it. It...

![Image 4: No description has been provided for this image](blob:https://docs.llamaindex.ai/0a563b6876f4158b0d16a8beb6548da6)

#### Generate final response using GPT4V[¶](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_video_RAG/#generate-final-response-using-gpt4v)

In \[ \]:

Copied!

from llama\_index.multi\_modal\_llms.openai import OpenAIMultiModal

openai\_mm\_llm \= OpenAIMultiModal(
    model\="gpt-4o", api\_key\=OPENAI\_API\_KEY, max\_new\_tokens\=1500
)

response\_1 \= openai\_mm\_llm.complete(
    prompt\=qa\_tmpl\_str.format(
        context\_str\=context\_str, query\_str\=query\_str, metadata\_str\=metadata\_str
    ),
    image\_documents\=image\_documents,
)

pprint(response\_1.text)

from llama\_index.multi\_modal\_llms.openai import OpenAIMultiModal openai\_mm\_llm = OpenAIMultiModal( model="gpt-4o", api\_key=OPENAI\_API\_KEY, max\_new\_tokens=1500 ) response\_1 = openai\_mm\_llm.complete( prompt=qa\_tmpl\_str.format( context\_str=context\_str, query\_str=query\_str, metadata\_str=metadata\_str ), image\_documents=image\_documents, ) pprint(response\_1.text)

('The video by 3Blue1Brown, titled "A pretty reason why Gaussian + Gaussian = '
 'Gaussian," covers several aspects of the Gaussian function, also known as '
 "the normal distribution. Here's a summary of the key points discussed in the "
 'video:\\n'
 '\\n'
 '1. \*\*Central Limit Theorem\*\*: The video begins by discussing the central '
 'limit theorem, which states that the sum of multiple copies of a random '
 'variable tends to look like a normal distribution. As the number of '
 'variables increases, the approximation to a normal distribution becomes '
 'better.\\n'
 '\\n'
 '2. \*\*Convolution of Random Variables\*\*: The process of adding two random '
 'variables is mathematically represented by a convolution of their respective '
 'distributions. The video explains the concept of convolution and how it is '
 'used to find the distribution of the sum of two random variables.\\n'
 '\\n'
 '3. \*\*Gaussian Function\*\*: The Gaussian function is more complex than just '
 '\\\\( e^{-x^2} \\\\). The full formula includes a scaling factor to ensure the '
 'area under the curve is 1 (making it a valid probability distribution), a '
 'standard deviation parameter \\\\( \\\\sigma \\\\) to describe the spread, and a '
 'mean parameter \\\\( \\\\mu \\\\) to shift the center. However, the video focuses '
 'on centered distributions with \\\\( \\\\mu = 0 \\\\).\\n'
 '\\n'
 '4. \*\*Visualizing Convolution\*\*: The video presents a visual method to '
 'understand the convolution of two Gaussian functions using diagonal slices '
 'on the xy-plane. This method involves looking at the probability density of '
 'landing on a point (x, y) as \\\\( f(x) \\\\times g(y) \\\\), where f and g are '
 'the two distributions being convolved.\\n'
 '\\n'
 '5. \*\*Rotational Symmetry\*\*: A key property of the Gaussian function is its '
 'rotational symmetry, which is unique to bell curves. This symmetry is '
 'exploited in the video to simplify the calculation of the convolution. By '
 'rotating the graph 45 degrees, the computation becomes easier because the '
 'integral only involves one variable.\\n'
 '\\n'
 '6. \*\*Result of Convolution\*\*: The video demonstrates that the convolution of '
 'two Gaussian functions is another Gaussian function. This is a special '
 'property because convolutions typically result in a different kind of '
 'function. The standard deviation of the resulting Gaussian is \\\\( \\\\sqrt{2} '
 '\\\\times \\\\sigma \\\\) if the original Gaussians had the same standard '
 'deviation.\\n'
 '\\n'
 '7. \*\*Proof of Central Limit Theorem\*\*: The video explains that the '
 'convolution of two Gaussians being another Gaussian is a crucial step in '
 'proving the central limit theorem. It shows that the Gaussian function is a '
 'fixed point in the space of distributions, and since all distributions with '
 'finite variance tend towards a single universal shape, that shape must be '
 'the Gaussian.\\n'
 '\\n'
 '8. \*\*Connection to Pi\*\*: The video also touches on the connection between '
 'the Gaussian function and the number Pi, which appears in the formula for '
 'the normal distribution.\\n'
 '\\n'
 'The video aims to provide an intuitive geometric argument for why the sum of '
 'two normally distributed random variables is also normally distributed, and '
 'how this relates to the central limit theorem and the special properties of '
 'the Gaussian function.')

Back to top

[Previous Multi-Modal Retrieval using GPT text embedding and CLIP image embedding for Wikipedia Articles](https://docs.llamaindex.ai/en/stable/examples/multi_modal/multi_modal_retrieval/)[Next Multimodal Ollama Cookbook](https://docs.llamaindex.ai/en/stable/examples/multi_modal/ollama_cookbook/)

Hi, how can I help you?

🦙
