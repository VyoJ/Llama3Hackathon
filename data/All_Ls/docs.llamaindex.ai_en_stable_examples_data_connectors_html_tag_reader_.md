Title: HTML Tag Reader - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/data_connectors/html_tag_reader/

Markdown Content:
HTML Tag Reader - LlamaIndex


If you're opening this Notebook on colab, you will probably need to install LlamaIndex 🦙.

In \[ \]:

Copied!

%pip install llama\-index\-readers\-file

%pip install llama-index-readers-file

In \[ \]:

Copied!

!pip install llama\-index

!pip install llama-index

### Download HTML file[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/html_tag_reader/#download-html-file)

In \[ \]:

Copied!

%%bash
wget \-e robots\=off \--no\-clobber \--page\-requisites \\
  \--html\-extension \--convert\-links \--restrict\-file\-names\=windows \\
  \--domains docs.ray.io \--no\-parent \--accept\=html \\
  \-P data/ https://docs.ray.io/en/master/ray\-overview/installation.html

%%bash wget -e robots=off --no-clobber --page-requisites \\ --html-extension --convert-links --restrict-file-names=windows \\ --domains docs.ray.io --no-parent --accept=html \\ -P data/ https://docs.ray.io/en/master/ray-overview/installation.html

Both --no-clobber and --convert-links were specified, only --convert-links will be used.
--2023-09-07 16:36:36--  https://docs.ray.io/en/master/ray-overview/installation.html
Resolving docs.ray.io (docs.ray.io)... 104.18.1.163, 104.18.0.163
Connecting to docs.ray.io (docs.ray.io)|104.18.1.163|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: unspecified \[text/html\]
Saving to: ‘data/docs.ray.io/en/master/ray-overview/installation.html’

     0K .......... .......... .......... .......... ..........  125M
    50K .......... .......... .......... .......... .......... 21.4M
   100K .......... .......... .......... ........              1.01M=0.04s

2023-09-07 16:36:37 (3.37 MB/s) - ‘data/docs.ray.io/en/master/ray-overview/installation.html’ saved \[142067\]

FINISHED --2023-09-07 16:36:37--
Total wall clock time: 0.3s
Downloaded: 1 files, 139K in 0.04s (3.37 MB/s)
Converting links in data/docs.ray.io/en/master/ray-overview/installation.html... 116.
48-68
Converted links in 1 files in 0.002 seconds.

In \[ \]:

Copied!

from llama\_index.readers.file import HTMLTagReader

reader \= HTMLTagReader(tag\="section", ignore\_no\_id\=True)
docs \= reader.load\_data(
    "data/docs.ray.io/en/master/ray-overview/installation.html"
)

from llama\_index.readers.file import HTMLTagReader reader = HTMLTagReader(tag="section", ignore\_no\_id=True) docs = reader.load\_data( "data/docs.ray.io/en/master/ray-overview/installation.html" )

In \[ \]:

Copied!

for doc in docs:
    print(doc.metadata)

for doc in docs: print(doc.metadata)

{'tag': 'section', 'tag\_id': 'installing-ray', 'file\_path': 'data/docs.ray.io/en/master/ray-overview/installation.html'}
{'tag': 'section', 'tag\_id': 'official-releases', 'file\_path': 'data/docs.ray.io/en/master/ray-overview/installation.html'}
{'tag': 'section', 'tag\_id': 'from-wheels', 'file\_path': 'data/docs.ray.io/en/master/ray-overview/installation.html'}
{'tag': 'section', 'tag\_id': 'daily-releases-nightlies', 'file\_path': 'data/docs.ray.io/en/master/ray-overview/installation.html'}
{'tag': 'section', 'tag\_id': 'installing-from-a-specific-commit', 'file\_path': 'data/docs.ray.io/en/master/ray-overview/installation.html'}
{'tag': 'section', 'tag\_id': 'install-ray-java-with-maven', 'file\_path': 'data/docs.ray.io/en/master/ray-overview/installation.html'}
{'tag': 'section', 'tag\_id': 'install-ray-c', 'file\_path': 'data/docs.ray.io/en/master/ray-overview/installation.html'}
{'tag': 'section', 'tag\_id': 'm1-mac-apple-silicon-support', 'file\_path': 'data/docs.ray.io/en/master/ray-overview/installation.html'}
{'tag': 'section', 'tag\_id': 'windows-support', 'file\_path': 'data/docs.ray.io/en/master/ray-overview/installation.html'}
{'tag': 'section', 'tag\_id': 'installing-ray-on-arch-linux', 'file\_path': 'data/docs.ray.io/en/master/ray-overview/installation.html'}
{'tag': 'section', 'tag\_id': 'installing-from-conda-forge', 'file\_path': 'data/docs.ray.io/en/master/ray-overview/installation.html'}
{'tag': 'section', 'tag\_id': 'building-ray-from-source', 'file\_path': 'data/docs.ray.io/en/master/ray-overview/installation.html'}
{'tag': 'section', 'tag\_id': 'docker-source-images', 'file\_path': 'data/docs.ray.io/en/master/ray-overview/installation.html'}
{'tag': 'section', 'tag\_id': 'launch-ray-in-docker', 'file\_path': 'data/docs.ray.io/en/master/ray-overview/installation.html'}
{'tag': 'section', 'tag\_id': 'test-if-the-installation-succeeded', 'file\_path': 'data/docs.ray.io/en/master/ray-overview/installation.html'}
{'tag': 'section', 'tag\_id': 'installed-python-dependencies', 'file\_path': 'data/docs.ray.io/en/master/ray-overview/installation.html'}

Back to top

[Previous Deplot Reader Demo](https://docs.llamaindex.ai/en/stable/examples/data_connectors/deplot/DeplotReader/)[Next Simple Directory Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/simple_directory_reader/)
