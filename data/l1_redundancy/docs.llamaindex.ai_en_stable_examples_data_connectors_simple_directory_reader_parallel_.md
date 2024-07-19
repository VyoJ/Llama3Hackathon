Title: Parallel Processing SimpleDirectoryReader - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/examples/data_connectors/simple_directory_reader_parallel/

Markdown Content:
Parallel Processing SimpleDirectoryReader - LlamaIndex


In this notebook, we demonstrate how to use parallel processing when loading data with `SimpleDirectoryReader`. Parallel processing can be useful with heavier workloads i.e., loading from a directory consisting of many files. (NOTE: if using Windows, you may see less gains when using parallel processing for loading data. This has to do with the differences between how multiprocess works in linux/mac and windows e.g., see [here](https://pythonforthelab.com/blog/differences-between-multiprocessing-windows-and-linux/) or [here](https://stackoverflow.com/questions/52465237/multiprocessing-slower-than-serial-processing-in-windows-but-not-in-linux))

In \[ \]:

Copied!

import cProfile, pstats
from pstats import SortKey

import cProfile, pstats from pstats import SortKey

In this demo, we'll use the `PatronusAIFinanceBenchDataset` llama-dataset from [llamahub](https://llamahub.ai/). This dataset is based off of a set of 32 PDF files which are included in the download from llamahub.

In \[ \]:

Copied!

!llamaindex\-cli download\-llamadataset PatronusAIFinanceBenchDataset \--download\-dir ./data

!llamaindex-cli download-llamadataset PatronusAIFinanceBenchDataset --download-dir ./data

In \[ \]:

Copied!

from llama\_index.core import SimpleDirectoryReader

\# define our reader with the directory containing the 32 pdf files
reader \= SimpleDirectoryReader(input\_dir\="./data/source\_files")

from llama\_index.core import SimpleDirectoryReader # define our reader with the directory containing the 32 pdf files reader = SimpleDirectoryReader(input\_dir="./data/source\_files")

### Sequential Load[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/simple_directory_reader_parallel/#sequential-load)

Sequential loading is the default behaviour and can be executed via the `load_data()` method.

In \[ \]:

Copied!

documents \= reader.load\_data()
len(documents)

documents = reader.load\_data() len(documents)

Out\[ \]:

4306

In \[ \]:

Copied!

cProfile.run("reader.load\_data()", "oldstats")
p \= pstats.Stats("oldstats")
p.strip\_dirs().sort\_stats(SortKey.CUMULATIVE).print\_stats(15)

cProfile.run("reader.load\_data()", "oldstats") p = pstats.Stats("oldstats") p.strip\_dirs().sort\_stats(SortKey.CUMULATIVE).print\_stats(15)

Wed Jan 10 12:40:50 2024    oldstats

         1857432165 function calls (1853977584 primitive calls) in 391.159 seconds

   Ordered by: cumulative time
   List reduced from 292 to 15 due to restriction <15>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000  391.159  391.159 {built-in method builtins.exec}
        1    0.003    0.003  391.158  391.158 <string>:1(<module>)
        1    0.000    0.000  391.156  391.156 base.py:367(load\_data)
       32    0.000    0.000  391.153   12.224 base.py:256(load\_file)
       32    0.127    0.004  391.149   12.223 docs\_reader.py:24(load\_data)
     4306    1.285    0.000  387.685    0.090 \_page.py:2195(extract\_text)
4444/4306    5.984    0.001  386.399    0.090 \_page.py:1861(\_extract\_text)
     4444    0.006    0.000  270.543    0.061 \_data\_structures.py:1220(operations)
     4444   43.270    0.010  270.536    0.061 \_data\_structures.py:1084(\_parse\_content\_stream)
36489963/33454574   32.688    0.000  167.817    0.000 \_data\_structures.py:1248(read\_object)
 23470599   19.764    0.000  100.843    0.000 \_page.py:1944(process\_operation)
 48258569   37.205    0.000   75.145    0.000 \_utils.py:200(read\_until\_regex)
 25208954   11.215    0.000   64.272    0.000 \_base.py:481(read\_from\_stream)
 18016574   23.488    0.000   49.305    0.000 \_\_init\_\_.py:88(crlf\_space\_check)
  8642699   20.779    0.000   48.224    0.000 \_utils.py:14(read\_hex\_string\_from\_stream)

Out\[ \]:

<pstats.Stats at 0x16bb3d300>

### Parallel Load[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/simple_directory_reader_parallel/#parallel-load)

To load using parallel processes, we set `num_workers` to a positive integer value.

In \[ \]:

Copied!

documents \= reader.load\_data(num\_workers\=10)

documents = reader.load\_data(num\_workers=10)

In \[ \]:

Copied!

len(documents)

len(documents)

Out\[ \]:

4306

In \[ \]:

Copied!

cProfile.run("reader.load\_data(num\_workers=10)", "newstats")
p \= pstats.Stats("newstats")
p.strip\_dirs().sort\_stats(SortKey.CUMULATIVE).print\_stats(15)

cProfile.run("reader.load\_data(num\_workers=10)", "newstats") p = pstats.Stats("newstats") p.strip\_dirs().sort\_stats(SortKey.CUMULATIVE).print\_stats(15)

Wed Jan 10 13:05:13 2024    newstats

         12539 function calls in 31.319 seconds

   Ordered by: cumulative time
   List reduced from 212 to 15 due to restriction <15>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   31.319   31.319 {built-in method builtins.exec}
        1    0.003    0.003   31.319   31.319 <string>:1(<module>)
        1    0.000    0.000   31.316   31.316 base.py:367(load\_data)
       24    0.000    0.000   31.139    1.297 threading.py:589(wait)
       23    0.000    0.000   31.139    1.354 threading.py:288(wait)
      155   31.138    0.201   31.138    0.201 {method 'acquire' of '\_thread.lock' objects}
        1    0.000    0.000   31.133   31.133 pool.py:369(starmap)
        1    0.000    0.000   31.133   31.133 pool.py:767(get)
        1    0.000    0.000   31.133   31.133 pool.py:764(wait)
        1    0.000    0.000    0.155    0.155 context.py:115(Pool)
        1    0.000    0.000    0.155    0.155 pool.py:183(\_\_init\_\_)
        1    0.000    0.000    0.153    0.153 pool.py:305(\_repopulate\_pool)
        1    0.001    0.001    0.153    0.153 pool.py:314(\_repopulate\_pool\_static)
       10    0.001    0.000    0.152    0.015 process.py:110(start)
       10    0.001    0.000    0.150    0.015 context.py:285(\_Popen)

Out\[ \]:

<pstats.Stats at 0x29408ab30>

### In Conclusion[¶](https://docs.llamaindex.ai/en/stable/examples/data_connectors/simple_directory_reader_parallel/#in-conclusion)

In \[ \]:

Copied!

391 / 30

391 / 30

Out\[ \]:

13.033333333333333

As one can observe from the results above, there is a ~13x speed up (or 1200% speed increase) when using parallel processing when loading from a directory with many files.

Back to top

[Previous Simple Directory Reader](https://docs.llamaindex.ai/en/stable/examples/data_connectors/simple_directory_reader/)[Next Simple Directory Reader over a Remote FileSystem](https://docs.llamaindex.ai/en/stable/examples/data_connectors/simple_directory_reader_remote_fs/)
