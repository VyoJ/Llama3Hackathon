Title: Simple - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/simple/

Markdown Content:
Simple - LlamaIndex


SimpleDocumentStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/simple/#llama_index.core.storage.docstore.SimpleDocumentStore "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `KVDocumentStore`

Simple Document (Node) store.

An in-memory store for Document and Node objects.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `simple_kvstore` | `[SimpleKVStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/simple/#llama_index.core.storage.kvstore.SimpleKVStore "llama_index.core.storage.kvstore.simple_kvstore.SimpleKVStore")` | 
simple key-value store



 | `None` |
| `namespace` | `str` | 

namespace for the docstore



 | `None` |

Source code in `llama-index-core/llama_index/core/storage/docstore/simple_docstore.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SimpleDocumentStore</span><span class="p">(</span><span class="n">KVDocumentStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Simple Document (Node) store.</span>

<span class="sd">    An in-memory store for Document and Node objects.</span>

<span class="sd">    Args:</span>
<span class="sd">        simple_kvstore (SimpleKVStore): simple key-value store</span>
<span class="sd">        namespace (str): namespace for the docstore</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">simple_kvstore</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">SimpleKVStore</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_BATCH_SIZE</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init a SimpleDocumentStore."""</span>
        <span class="n">simple_kvstore</span> <span class="o">=</span> <span class="n">simple_kvstore</span> <span class="ow">or</span> <span class="n">SimpleKVStore</span><span class="p">()</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">simple_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="o">=</span><span class="n">namespace</span><span class="p">,</span> <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_persist_dir</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">persist_dir</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_PERSIST_DIR</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"SimpleDocumentStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create a SimpleDocumentStore from a persist directory.</span>

<span class="sd">        Args:</span>
<span class="sd">            persist_dir (str): directory to persist the store</span>
<span class="sd">            namespace (Optional[str]): namespace for the docstore</span>
<span class="sd">            fs (Optional[fsspec.AbstractFileSystem]): filesystem to use</span>

<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">fs</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">persist_path</span> <span class="o">=</span> <span class="n">concat_dirs</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">DEFAULT_PERSIST_FNAME</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">persist_path</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">DEFAULT_PERSIST_FNAME</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_persist_path</span><span class="p">(</span><span class="n">persist_path</span><span class="p">,</span> <span class="n">namespace</span><span class="o">=</span><span class="n">namespace</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_persist_path</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">persist_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"SimpleDocumentStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create a SimpleDocumentStore from a persist path.</span>

<span class="sd">        Args:</span>
<span class="sd">            persist_path (str): Path to persist the store</span>
<span class="sd">            namespace (Optional[str]): namespace for the docstore</span>
<span class="sd">            fs (Optional[fsspec.AbstractFileSystem]): filesystem to use</span>

<span class="sd">        """</span>
        <span class="n">simple_kvstore</span> <span class="o">=</span> <span class="n">SimpleKVStore</span><span class="o">.</span><span class="n">from_persist_path</span><span class="p">(</span><span class="n">persist_path</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">simple_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">persist</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">persist_path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_PERSIST_PATH</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Persist the store."""</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="p">,</span> <span class="n">BaseInMemoryKVStore</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">persist</span><span class="p">(</span><span class="n">persist_path</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_dict</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span> <span class="n">save_dict</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span> <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"SimpleDocumentStore"</span><span class="p">:</span>
        <span class="n">simple_kvstore</span> <span class="o">=</span> <span class="n">SimpleKVStore</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">save_dict</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">simple_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">to_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="p">,</span> <span class="n">SimpleKVStore</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### from\_persist\_dir `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/simple/#llama_index.core.storage.docstore.SimpleDocumentStore.from_persist_dir "Permanent link")

```
from_persist_dir(persist_dir: str = DEFAULT_PERSIST_DIR, namespace: Optional[str] = None, fs: Optional[AbstractFileSystem] = None) -> [SimpleDocumentStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/simple/#llama_index.core.storage.docstore.SimpleDocumentStore "llama_index.core.storage.docstore.simple_docstore.SimpleDocumentStore")
```

Create a SimpleDocumentStore from a persist directory.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `persist_dir` | `str` | 
directory to persist the store



 | `DEFAULT_PERSIST_DIR` |
| `namespace` | `Optional[str]` | 

namespace for the docstore



 | `None` |
| `fs` | `Optional[AbstractFileSystem]` | 

filesystem to use



 | `None` |

Source code in `llama-index-core/llama_index/core/storage/docstore/simple_docstore.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_persist_dir</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">persist_dir</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_PERSIST_DIR</span><span class="p">,</span>
    <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"SimpleDocumentStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create a SimpleDocumentStore from a persist directory.</span>

<span class="sd">    Args:</span>
<span class="sd">        persist_dir (str): directory to persist the store</span>
<span class="sd">        namespace (Optional[str]): namespace for the docstore</span>
<span class="sd">        fs (Optional[fsspec.AbstractFileSystem]): filesystem to use</span>

<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">fs</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">persist_path</span> <span class="o">=</span> <span class="n">concat_dirs</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">DEFAULT_PERSIST_FNAME</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">persist_path</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">persist_dir</span><span class="p">,</span> <span class="n">DEFAULT_PERSIST_FNAME</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_persist_path</span><span class="p">(</span><span class="n">persist_path</span><span class="p">,</span> <span class="n">namespace</span><span class="o">=</span><span class="n">namespace</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### from\_persist\_path `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/simple/#llama_index.core.storage.docstore.SimpleDocumentStore.from_persist_path "Permanent link")

```
from_persist_path(persist_path: str, namespace: Optional[str] = None, fs: Optional[AbstractFileSystem] = None) -> [SimpleDocumentStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/simple/#llama_index.core.storage.docstore.SimpleDocumentStore "llama_index.core.storage.docstore.simple_docstore.SimpleDocumentStore")
```

Create a SimpleDocumentStore from a persist path.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `persist_path` | `str` | 
Path to persist the store



 | _required_ |
| `namespace` | `Optional[str]` | 

namespace for the docstore



 | `None` |
| `fs` | `Optional[AbstractFileSystem]` | 

filesystem to use



 | `None` |

Source code in `llama-index-core/llama_index/core/storage/docstore/simple_docstore.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_persist_path</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="n">persist_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"SimpleDocumentStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create a SimpleDocumentStore from a persist path.</span>

<span class="sd">    Args:</span>
<span class="sd">        persist_path (str): Path to persist the store</span>
<span class="sd">        namespace (Optional[str]): namespace for the docstore</span>
<span class="sd">        fs (Optional[fsspec.AbstractFileSystem]): filesystem to use</span>

<span class="sd">    """</span>
    <span class="n">simple_kvstore</span> <span class="o">=</span> <span class="n">SimpleKVStore</span><span class="o">.</span><span class="n">from_persist_path</span><span class="p">(</span><span class="n">persist_path</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">simple_kvstore</span><span class="p">,</span> <span class="n">namespace</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### persist [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/simple/#llama_index.core.storage.docstore.SimpleDocumentStore.persist "Permanent link")

```
persist(persist_path: str = DEFAULT_PERSIST_PATH, fs: Optional[AbstractFileSystem] = None) -> None
```

Persist the store.

Source code in `llama-index-core/llama_index/core/storage/docstore/simple_docstore.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">persist</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">persist_path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_PERSIST_PATH</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Persist the store."""</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="p">,</span> <span class="n">BaseInMemoryKVStore</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_kvstore</span><span class="o">.</span><span class="n">persist</span><span class="p">(</span><span class="n">persist_path</span><span class="p">,</span> <span class="n">fs</span><span class="o">=</span><span class="n">fs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Redis](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/redis/)[Next Falkordb](https://docs.llamaindex.ai/en/stable/api_reference/storage/graph_stores/falkordb/)
