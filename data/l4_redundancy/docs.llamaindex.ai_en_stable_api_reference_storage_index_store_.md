Title: Index - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/

Markdown Content:
Index - LlamaIndex


BaseIndexStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/#llama_index.core.storage.index_store.types.BaseIndexStore "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `ABC`

Source code in `llama-index-core/llama_index/core/storage/index_store/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">13</span>
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
<span class="normal">37</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseIndexStore</span><span class="p">(</span><span class="n">ABC</span><span class="p">):</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">index_structs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">IndexStruct</span><span class="p">]:</span>
        <span class="k">pass</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">add_index_struct</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index_struct</span><span class="p">:</span> <span class="n">IndexStruct</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">pass</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">delete_index_struct</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">pass</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">get_index_struct</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">struct_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">IndexStruct</span><span class="p">]:</span>
        <span class="k">pass</span>

    <span class="k">def</span> <span class="nf">persist</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">persist_path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_PERSIST_PATH</span><span class="p">,</span>
        <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Persist the index store to disk."""</span>
</code></pre></div></td></tr></tbody></table>

### persist [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/#llama_index.core.storage.index_store.types.BaseIndexStore.persist "Permanent link")

```
persist(persist_path: str = DEFAULT_PERSIST_PATH, fs: Optional[AbstractFileSystem] = None) -> None
```

Persist the index store to disk.

Source code in `llama-index-core/llama_index/core/storage/index_store/types.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">persist</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">persist_path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_PERSIST_PATH</span><span class="p">,</span>
    <span class="n">fs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">fsspec</span><span class="o">.</span><span class="n">AbstractFileSystem</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Persist the index store to disk."""</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Firestore](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/firestore/)[Next Mongodb](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/mongodb/)
