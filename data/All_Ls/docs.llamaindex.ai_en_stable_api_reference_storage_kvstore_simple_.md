Title: Simple - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/simple/

Markdown Content:
Simple - LlamaIndex


SimpleKVStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/simple/#llama_index.core.storage.kvstore.SimpleKVStore "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseInMemoryKVStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/#llama_index.core.storage.kvstore.types.BaseInMemoryKVStore "llama_index.core.storage.kvstore.types.BaseInMemoryKVStore")`

Simple in-memory Key-Value store.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `data` | `Optional[DATA_TYPE]` | 
data to initialize the store with



 | `None` |

Source code in `llama-index-core/llama_index/core/storage/kvstore/simple_kvstore.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 17</span>
<span class="normal"> 18</span>
<span class="normal"> 19</span>
<span class="normal"> 20</span>
<span class="normal"> 21</span>
<span class="normal"> 22</span>
<span class="normal"> 23</span>
<span class="normal"> 24</span>
<span class="normal"> 25</span>
<span class="normal"> 26</span>
<span class="normal"> 27</span>
<span class="normal"> 28</span>
<span class="normal"> 29</span>
<span class="normal"> 30</span>
<span class="normal"> 31</span>
<span class="normal"> 32</span>
<span class="normal"> 33</span>
<span class="normal"> 34</span>
<span class="normal"> 35</span>
<span class="normal"> 36</span>
<span class="normal"> 37</span>
<span class="normal"> 38</span>
<span class="normal"> 39</span>
<span class="normal"> 40</span>
<span class="normal"> 41</span>
<span class="normal"> 42</span>
<span class="normal"> 43</span>
<span class="normal"> 44</span>
<span class="normal"> 45</span>
<span class="normal"> 46</span>
<span class="normal"> 47</span>
<span class="normal"> 48</span>
<span class="normal"> 49</span>
<span class="normal"> 50</span>
<span class="normal"> 51</span>
<span class="normal"> 52</span>
<span class="normal"> 53</span>
<span class="normal"> 54</span>
<span class="normal"> 55</span>
<span class="normal"> 56</span>
<span class="normal"> 57</span>
<span class="normal"> 58</span>
<span class="normal"> 59</span>
<span class="normal"> 60</span>
<span class="normal"> 61</span>
<span class="normal"> 62</span>
<span class="normal"> 63</span>
<span class="normal"> 64</span>
<span class="normal"> 65</span>
<span class="normal"> 66</span>
<span class="normal"> 67</span>
<span class="normal"> 68</span>
<span class="normal"> 69</span>
<span class="normal"> 70</span>
<span class="normal"> 71</span>
<span class="normal"> 72</span>
<span class="normal"> 73</span>
<span class="normal"> 74</span>
<span class="normal"> 75</span>
<span class="normal"> 76</span>
<span class="normal"> 77</span>
<span class="normal"> 78</span>
<span class="normal"> 79</span>
<span class="normal"> 80</span>
<span class="normal"> 81</span>
<span class="normal"> 82</span>
<span class="normal"> 83</span>
<span class="normal"> 84</span>
<span class="normal"> 85</span>
<span class="normal"> 86</span>
<span class="normal"> 87</span>
<span class="normal"> 88</span>
<span class="normal"> 89</span>
<span class="normal"> 90</span>
<span class="normal"> 91</span>
<span class="normal"> 92</span>
<span class="normal"> 93</span>
<span class="normal"> 94</span>
<span class="normal"> 95</span>
<span class="normal"> 96</span>
<span class="normal"> 97</span>
<span class="normal"> 98</span>
<span class="normal"> 99</span>
<span class="normal">100</span>
<span class="normal">101</span>
<span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span>
<span class="normal">107</span>
<span class="normal">108</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SimpleKVStore</span><span class="p">(</span><span class="n">BaseInMemoryKVStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Simple in-memory Key-Value store.</span>

<span class="sd">    Args:</span>
<span class="sd">        data (Optional[DATA_TYPE]): data to initialize the store with</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">data</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">DATA_TYPE</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init a SimpleKVStore."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_data</span><span class="p">:</span> <span class="n">DATA_TYPE</span> <span class="o">=</span> <span class="n">data</span> <span class="ow">or</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">val</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Put a key-value pair into the store."""</span>
        <span class="k">if</span> <span class="n">collection</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_data</span><span class="p">[</span><span class="n">collection</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_data</span><span class="p">[</span><span class="n">collection</span><span class="p">][</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">val</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aput</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">val</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Put a key-value pair into the store."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">val</span><span class="p">,</span> <span class="n">collection</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get a value from the store."""</span>
        <span class="n">collection_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">collection</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">collection_data</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="n">key</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">collection_data</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>
        <span class="k">return</span> <span class="n">collection_data</span><span class="p">[</span><span class="n">key</span><span class="p">]</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get a value from the store."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">collection</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_all</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get all values from the store."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">collection</span><span class="p">,</span> <span class="p">{})</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_all</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get all values from the store."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_all</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete a value from the store."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_data</span><span class="p">[</span><span class="n">collection</span><span class="p">]</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
            <span class="k">return</span> <span class="kc">True</span>
        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">False</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">adelete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete a value from the store."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">collection</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">persist</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">persist_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Persist the store."""</span>
        <span class="n">fs</span> <span class="o">=</span> <span class="n">fs</span> <span class="ow">or</span> <span class="n">fsspec</span><span class="o">.</span><span class="n">filesystem</span><span class="p">(</span><span class="s2">"file"</span><span class="p">)</span>
        <span class="n">dirpath</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">persist_path</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">fs</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">dirpath</span><span class="p">):</span>
            <span class="n">fs</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="n">dirpath</span><span class="p">)</span>

        <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">persist_path</span><span class="p">,</span> <span class="s2">"w"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_data</span><span class="p">))</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_persist_path</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span> <span class="n">persist_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"SimpleKVStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load a SimpleKVStore from a persist path and filesystem."""</span>
        <span class="n">fs</span> <span class="o">=</span> <span class="n">fs</span> <span class="ow">or</span> <span class="n">fsspec</span><span class="o">.</span><span class="n">filesystem</span><span class="p">(</span><span class="s2">"file"</span><span class="p">)</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Loading </span><span class="si">{</span><span class="vm">__name__</span><span class="si">}</span><span class="s2"> from </span><span class="si">{</span><span class="n">persist_path</span><span class="si">}</span><span class="s2">."</span><span class="p">)</span>
        <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">persist_path</span><span class="p">,</span> <span class="s2">"rb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
            <span class="n">data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">to_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Save the store as dict."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_dict</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">save_dict</span><span class="p">:</span> <span class="nb">dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"SimpleKVStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Load a SimpleKVStore from dict."""</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">save_dict</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### put [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/simple/#llama_index.core.storage.kvstore.SimpleKVStore.put "Permanent link")

```
put(key: str, val: dict, collection: str = DEFAULT_COLLECTION) -> None
```

Put a key-value pair into the store.

Source code in `llama-index-core/llama_index/core/storage/kvstore/simple_kvstore.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">val</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Put a key-value pair into the store."""</span>
    <span class="k">if</span> <span class="n">collection</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_data</span><span class="p">[</span><span class="n">collection</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_data</span><span class="p">[</span><span class="n">collection</span><span class="p">][</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">val</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### aput `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/simple/#llama_index.core.storage.kvstore.SimpleKVStore.aput "Permanent link")

```
aput(key: str, val: dict, collection: str = DEFAULT_COLLECTION) -> None
```

Put a key-value pair into the store.

Source code in `llama-index-core/llama_index/core/storage/kvstore/simple_kvstore.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aput</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">val</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Put a key-value pair into the store."""</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">val</span><span class="p">,</span> <span class="n">collection</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/simple/#llama_index.core.storage.kvstore.SimpleKVStore.get "Permanent link")

```
get(key: str, collection: str = DEFAULT_COLLECTION) -> Optional[dict]
```

Get a value from the store.

Source code in `llama-index-core/llama_index/core/storage/kvstore/simple_kvstore.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get a value from the store."""</span>
    <span class="n">collection_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">collection</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">collection_data</span><span class="p">:</span>
        <span class="k">return</span> <span class="kc">None</span>
    <span class="k">if</span> <span class="n">key</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">collection_data</span><span class="p">:</span>
        <span class="k">return</span> <span class="kc">None</span>
    <span class="k">return</span> <span class="n">collection_data</span><span class="p">[</span><span class="n">key</span><span class="p">]</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### aget `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/simple/#llama_index.core.storage.kvstore.SimpleKVStore.aget "Permanent link")

```
aget(key: str, collection: str = DEFAULT_COLLECTION) -> Optional[dict]
```

Get a value from the store.

Source code in `llama-index-core/llama_index/core/storage/kvstore/simple_kvstore.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aget</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get a value from the store."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">collection</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_all [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/simple/#llama_index.core.storage.kvstore.SimpleKVStore.get_all "Permanent link")

```
get_all(collection: str = DEFAULT_COLLECTION) -> Dict[str, dict]
```

Get all values from the store.

Source code in `llama-index-core/llama_index/core/storage/kvstore/simple_kvstore.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_all</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get all values from the store."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">collection</span><span class="p">,</span> <span class="p">{})</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table>

### aget\_all `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/simple/#llama_index.core.storage.kvstore.SimpleKVStore.aget_all "Permanent link")

```
aget_all(collection: str = DEFAULT_COLLECTION) -> Dict[str, dict]
```

Get all values from the store.

Source code in `llama-index-core/llama_index/core/storage/kvstore/simple_kvstore.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">aget_all</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get all values from the store."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_all</span><span class="p">(</span><span class="n">collection</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/simple/#llama_index.core.storage.kvstore.SimpleKVStore.delete "Permanent link")

```
delete(key: str, collection: str = DEFAULT_COLLECTION) -> bool
```

Delete a value from the store.

Source code in `llama-index-core/llama_index/core/storage/kvstore/simple_kvstore.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete a value from the store."""</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_data</span><span class="p">[</span><span class="n">collection</span><span class="p">]</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
        <span class="k">return</span> <span class="kc">True</span>
    <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
        <span class="k">return</span> <span class="kc">False</span>
</code></pre></div></td></tr></tbody></table>

### adelete `async` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/simple/#llama_index.core.storage.kvstore.SimpleKVStore.adelete "Permanent link")

```
adelete(key: str, collection: str = DEFAULT_COLLECTION) -> bool
```

Delete a value from the store.

Source code in `llama-index-core/llama_index/core/storage/kvstore/simple_kvstore.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">async</span> <span class="k">def</span> <span class="nf">adelete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete a value from the store."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">collection</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### persist [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/simple/#llama_index.core.storage.kvstore.SimpleKVStore.persist "Permanent link")

```
persist(persist_path: str, fs: Optional[AbstractFileSystem] = None) -> None
```

Persist the store.

Source code in `llama-index-core/llama_index/core/storage/kvstore/simple_kvstore.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">persist</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">persist_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Persist the store."""</span>
    <span class="n">fs</span> <span class="o">=</span> <span class="n">fs</span> <span class="ow">or</span> <span class="n">fsspec</span><span class="o">.</span><span class="n">filesystem</span><span class="p">(</span><span class="s2">"file"</span><span class="p">)</span>
    <span class="n">dirpath</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">persist_path</span><span class="p">)</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">fs</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">dirpath</span><span class="p">):</span>
        <span class="n">fs</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="n">dirpath</span><span class="p">)</span>

    <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">persist_path</span><span class="p">,</span> <span class="s2">"w"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
        <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_data</span><span class="p">))</span>
</code></pre></div></td></tr></tbody></table>

### from\_persist\_path `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/simple/#llama_index.core.storage.kvstore.SimpleKVStore.from_persist_path "Permanent link")

```
from_persist_path(persist_path: str, fs: Optional[AbstractFileSystem] = None) -> [SimpleKVStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/simple/#llama_index.core.storage.kvstore.SimpleKVStore "llama_index.core.storage.kvstore.simple_kvstore.SimpleKVStore")
```

Load a SimpleKVStore from a persist path and filesystem.

Source code in `llama-index-core/llama_index/core/storage/kvstore/simple_kvstore.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span>
<span class="normal">97</span>
<span class="normal">98</span>
<span class="normal">99</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_persist_path</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span> <span class="n">persist_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"SimpleKVStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load a SimpleKVStore from a persist path and filesystem."""</span>
    <span class="n">fs</span> <span class="o">=</span> <span class="n">fs</span> <span class="ow">or</span> <span class="n">fsspec</span><span class="o">.</span><span class="n">filesystem</span><span class="p">(</span><span class="s2">"file"</span><span class="p">)</span>
    <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Loading </span><span class="si">{</span><span class="vm">__name__</span><span class="si">}</span><span class="s2"> from </span><span class="si">{</span><span class="n">persist_path</span><span class="si">}</span><span class="s2">."</span><span class="p">)</span>
    <span class="k">with</span> <span class="n">fs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">persist_path</span><span class="p">,</span> <span class="s2">"rb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
        <span class="n">data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### to\_dict [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/simple/#llama_index.core.storage.kvstore.SimpleKVStore.to_dict "Permanent link")

```
to_dict() -> dict
```

Save the store as dict.

Source code in `llama-index-core/llama_index/core/storage/kvstore/simple_kvstore.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">101</span>
<span class="normal">102</span>
<span class="normal">103</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">to_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Save the store as dict."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data</span>
</code></pre></div></td></tr></tbody></table>

### from\_dict `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/simple/#llama_index.core.storage.kvstore.SimpleKVStore.from_dict "Permanent link")

```
from_dict(save_dict: dict) -> [SimpleKVStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/simple/#llama_index.core.storage.kvstore.SimpleKVStore "llama_index.core.storage.kvstore.simple_kvstore.SimpleKVStore")
```

Load a SimpleKVStore from dict.

Source code in `llama-index-core/llama_index/core/storage/kvstore/simple_kvstore.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">105</span>
<span class="normal">106</span>
<span class="normal">107</span>
<span class="normal">108</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_dict</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">save_dict</span><span class="p">:</span> <span class="nb">dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"SimpleKVStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Load a SimpleKVStore from dict."""</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">save_dict</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous S3](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/s3/)[Next Storage context](https://docs.llamaindex.ai/en/stable/api_reference/storage/storage_context/)
