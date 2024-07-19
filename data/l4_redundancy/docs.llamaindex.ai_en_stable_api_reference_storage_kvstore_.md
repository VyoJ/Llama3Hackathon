Title: Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/

Markdown Content:
Index - LlamaIndex


BaseKVStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/#llama_index.core.storage.kvstore.types.BaseKVStore "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `ABC`

Base key-value store.

Source code in `llama-index-core/llama_index/core/storage/kvstore/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">10</span>
<span class="normal">11</span>
<span class="normal">12</span>
<span class="normal">13</span>
<span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
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
<span class="normal">73</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseKVStore</span><span class="p">(</span><span class="n">ABC</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Base key-value store."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">val</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">pass</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">aput</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">val</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">pass</span>

    <span class="k">def</span> <span class="nf">put_all</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">kv_pairs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]],</span>
        <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_BATCH_SIZE</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="c1"># by default, support a batch size of 1</span>
        <span class="k">if</span> <span class="n">batch_size</span> <span class="o">!=</span> <span class="mi">1</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"Batching not supported by this key-value store."</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">val</span> <span class="ow">in</span> <span class="n">kv_pairs</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">val</span><span class="p">,</span> <span class="n">collection</span><span class="o">=</span><span class="n">collection</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">aput_all</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">kv_pairs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]],</span>
        <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_BATCH_SIZE</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="c1"># by default, support a batch size of 1</span>
        <span class="k">if</span> <span class="n">batch_size</span> <span class="o">!=</span> <span class="mi">1</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s2">"Batching not supported by this key-value store."</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">val</span> <span class="ow">in</span> <span class="n">kv_pairs</span><span class="p">:</span>
                <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">aput</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">val</span><span class="p">,</span> <span class="n">collection</span><span class="o">=</span><span class="n">collection</span><span class="p">)</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
        <span class="k">pass</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]:</span>
        <span class="k">pass</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">get_all</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
        <span class="k">pass</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">aget_all</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
        <span class="k">pass</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
        <span class="k">pass</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">adelete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_COLLECTION</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
        <span class="k">pass</span>
</code></pre></div></td></tr></tbody></table>

BaseInMemoryKVStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/#llama_index.core.storage.kvstore.types.BaseInMemoryKVStore "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseKVStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/#llama_index.core.storage.kvstore.types.BaseKVStore "llama_index.core.storage.kvstore.types.BaseKVStore")`

Base in-memory key-value store.

Source code in `llama-index-core/llama_index/core/storage/kvstore/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">76</span>
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
<span class="normal">88</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseInMemoryKVStore</span><span class="p">(</span><span class="n">BaseKVStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Base in-memory key-value store."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">persist</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">persist_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">pass</span>

    <span class="nd">@classmethod</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">from_persist_path</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">persist_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"BaseInMemoryKVStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create a BaseInMemoryKVStore from a persist directory."""</span>
</code></pre></div></td></tr></tbody></table>

### from\_persist\_path `abstractmethod` `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/#llama_index.core.storage.kvstore.types.BaseInMemoryKVStore.from_persist_path "Permanent link")

```
from_persist_path(persist_path: str) -> [BaseInMemoryKVStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/#llama_index.core.storage.kvstore.types.BaseInMemoryKVStore "llama_index.core.storage.kvstore.types.BaseInMemoryKVStore")
```

Create a BaseInMemoryKVStore from a persist directory.

Source code in `llama-index-core/llama_index/core/storage/kvstore/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="nd">@abstractmethod</span>
<span class="k">def</span> <span class="nf">from_persist_path</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">persist_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"BaseInMemoryKVStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create a BaseInMemoryKVStore from a persist directory."""</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Firestore](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/firestore/)[Next Mongodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/mongodb/)
