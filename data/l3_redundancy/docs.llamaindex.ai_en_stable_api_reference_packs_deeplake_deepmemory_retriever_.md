Title: Deeplake deepmemory retriever - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/deeplake_deepmemory_retriever/

Markdown Content:
Deeplake deepmemory retriever - LlamaIndex


DeepMemoryRetrieverPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/deeplake_deepmemory_retriever/#llama_index.packs.deeplake_deepmemory_retriever.DeepMemoryRetrieverPack "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

DeepMemory retriever pack.

Source code in `llama-index-packs/llama-index-packs-deeplake-deepmemory-retriever/llama_index/packs/deeplake_deepmemory_retriever/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">14</span>
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
<span class="normal">70</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">DeepMemoryRetrieverPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""DeepMemory retriever pack."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">dataset_path</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"llama_index"</span><span class="p">,</span>
        <span class="n">token</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">read_only</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">overwrite</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">TextNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">top_k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">4</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_vector_store</span> <span class="o">=</span> <span class="n">DeepLakeVectorStore</span><span class="p">(</span>
            <span class="n">dataset_path</span><span class="o">=</span><span class="n">dataset_path</span><span class="p">,</span>
            <span class="n">token</span><span class="o">=</span><span class="n">token</span><span class="p">,</span>
            <span class="n">read_only</span><span class="o">=</span><span class="n">read_only</span><span class="p">,</span>
            <span class="n">overwrite</span><span class="o">=</span><span class="n">overwrite</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="n">nodes</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span> <span class="o">=</span> <span class="n">StorageContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
                <span class="n">vector_store</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_vector_store</span>
            <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="p">(</span>
                <span class="n">nodes</span><span class="p">,</span> <span class="n">storage_context</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="o">.</span><span class="n">from_vector_store</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_vector_store</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
            <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">storage_context</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">retriever</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span>
            <span class="n">similarity_top_k</span><span class="o">=</span><span class="n">top_k</span><span class="p">,</span> <span class="n">vector_store_kwargs</span><span class="o">=</span><span class="p">{</span><span class="s2">"deep_memory"</span><span class="p">:</span> <span class="kc">True</span><span class="p">}</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span> <span class="o">=</span> <span class="n">RetrieverQueryEngine</span><span class="o">.</span><span class="n">from_args</span><span class="p">(</span><span class="n">retriever</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">retriever</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"vector_store"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vector_store</span><span class="p">,</span>
            <span class="s2">"storage_context"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span><span class="p">,</span>
            <span class="s2">"index"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="p">,</span>
            <span class="s2">"retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">retriever</span><span class="p">,</span>
            <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">retrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Retrieve."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">retriever</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/deeplake_deepmemory_retriever/#llama_index.packs.deeplake_deepmemory_retriever.DeepMemoryRetrieverPack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-deeplake-deepmemory-retriever/llama_index/packs/deeplake_deepmemory_retriever/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"vector_store"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vector_store</span><span class="p">,</span>
        <span class="s2">"storage_context"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_storage_context</span><span class="p">,</span>
        <span class="s2">"index"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="p">,</span>
        <span class="s2">"retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">retriever</span><span class="p">,</span>
        <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### retrieve [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/deeplake_deepmemory_retriever/#llama_index.packs.deeplake_deepmemory_retriever.DeepMemoryRetrieverPack.retrieve "Permanent link")

```
retrieve(query_str: str) -> Any
```

Retrieve.

Source code in `llama-index-packs/llama-index-packs-deeplake-deepmemory-retriever/llama_index/packs/deeplake_deepmemory_retriever/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">retrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Retrieve."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">retriever</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/deeplake_deepmemory_retriever/#llama_index.packs.deeplake_deepmemory_retriever.DeepMemoryRetrieverPack.run "Permanent link")

```
run(*args: Any, **kwargs: Any) -> Any
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-deeplake-deepmemory-retriever/llama_index/packs/deeplake_deepmemory_retriever/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Corrective rag](https://docs.llamaindex.ai/en/stable/api_reference/packs/corrective_rag/)[Next Deeplake multimodal retrieval](https://docs.llamaindex.ai/en/stable/api_reference/packs/deeplake_multimodal_retrieval/)
