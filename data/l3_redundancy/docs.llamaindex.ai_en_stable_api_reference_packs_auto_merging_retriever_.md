Title: Auto merging retriever - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/auto_merging_retriever/

Markdown Content:
Auto merging retriever - LlamaIndex


AutoMergingRetrieverPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/auto_merging_retriever/#llama_index.packs.auto_merging_retriever.AutoMergingRetrieverPack "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Auto-merging Retriever pack.

Build a hierarchical node graph from a set of documents, and run our auto-merging retriever.

Source code in `llama-index-packs/llama-index-packs-auto-merging-retriever/llama_index/packs/auto_merging_retriever/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">19</span>
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
<span class="normal">69</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">AutoMergingRetrieverPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Auto-merging Retriever pack.</span>

<span class="sd">    Build a hierarchical node graph from a set of documents, and</span>
<span class="sd">    run our auto-merging retriever.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">docs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="c1"># create the sentence window node parser w/ default settings</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">node_parser</span> <span class="o">=</span> <span class="n">HierarchicalNodeParser</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">()</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_parser</span><span class="o">.</span><span class="n">get_nodes_from_documents</span><span class="p">(</span><span class="n">docs</span><span class="p">)</span>
        <span class="n">leaf_nodes</span> <span class="o">=</span> <span class="n">get_leaf_nodes</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>
        <span class="n">docstore</span> <span class="o">=</span> <span class="n">SimpleDocumentStore</span><span class="p">()</span>

        <span class="c1"># insert nodes into docstore</span>
        <span class="n">docstore</span><span class="o">.</span><span class="n">add_documents</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>

        <span class="c1"># define storage context (will include vector store by default too)</span>
        <span class="n">storage_context</span> <span class="o">=</span> <span class="n">StorageContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span><span class="n">docstore</span><span class="o">=</span><span class="n">docstore</span><span class="p">)</span>

        <span class="n">service_context</span> <span class="o">=</span> <span class="n">ServiceContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">OpenAI</span><span class="p">(</span><span class="n">model</span><span class="o">=</span><span class="s2">"gpt-3.5-turbo"</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">base_index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="p">(</span>
            <span class="n">leaf_nodes</span><span class="p">,</span>
            <span class="n">storage_context</span><span class="o">=</span><span class="n">storage_context</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">base_retriever</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">base_index</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span><span class="n">similarity_top_k</span><span class="o">=</span><span class="mi">6</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">retriever</span> <span class="o">=</span> <span class="n">AutoMergingRetriever</span><span class="p">(</span>
            <span class="n">base_retriever</span><span class="p">,</span> <span class="n">storage_context</span><span class="p">,</span> <span class="n">verbose</span><span class="o">=</span><span class="kc">True</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span> <span class="o">=</span> <span class="n">RetrieverQueryEngine</span><span class="o">.</span><span class="n">from_args</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">retriever</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"node_parser"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_parser</span><span class="p">,</span>
            <span class="s2">"retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">retriever</span><span class="p">,</span>
            <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/auto_merging_retriever/#llama_index.packs.auto_merging_retriever.AutoMergingRetrieverPack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-auto-merging-retriever/llama_index/packs/auto_merging_retriever/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"node_parser"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_parser</span><span class="p">,</span>
        <span class="s2">"retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">retriever</span><span class="p">,</span>
        <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/auto_merging_retriever/#llama_index.packs.auto_merging_retriever.AutoMergingRetrieverPack.run "Permanent link")

```
run(*args: Any, **kwargs: Any) -> Any
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-auto-merging-retriever/llama_index/packs/auto_merging_retriever/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Arize phoenix query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/arize_phoenix_query_engine/)[Next Chroma autoretrieval](https://docs.llamaindex.ai/en/stable/api_reference/packs/chroma_autoretrieval/)
