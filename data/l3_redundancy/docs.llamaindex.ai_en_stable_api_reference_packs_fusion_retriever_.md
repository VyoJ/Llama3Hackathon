Title: Fusion retriever - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/fusion_retriever/

Markdown Content:
Fusion retriever - LlamaIndex


HybridFusionRetrieverPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/fusion_retriever/#llama_index.packs.fusion_retriever.HybridFusionRetrieverPack "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Hybrid fusion retriever pack.

Ensembles vector and bm25 retrievers using fusion.

Source code in `llama-index-packs/llama-index-packs-fusion-retriever/llama_index/packs/fusion_retriever/hybrid_fusion/base.py`

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
<span class="normal">88</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">HybridFusionRetrieverPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Hybrid fusion retriever pack.</span>

<span class="sd">    Ensembles vector and bm25 retrievers using fusion.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">TextNode</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">chunk_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">256</span><span class="p">,</span>
        <span class="n">mode</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"reciprocal_rerank"</span><span class="p">,</span>
        <span class="n">vector_similarity_top_k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span>
        <span class="n">bm25_similarity_top_k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span>
        <span class="n">fusion_similarity_top_k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span>
        <span class="n">num_queries</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">4</span><span class="p">,</span>
        <span class="n">documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">cache_dir</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="n">service_context</span> <span class="o">=</span> <span class="n">ServiceContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span><span class="n">chunk_size</span><span class="o">=</span><span class="n">chunk_size</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">cache_dir</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">cache_dir</span><span class="p">):</span>
            <span class="c1"># Load from cache</span>
            <span class="kn">from</span> <span class="nn">llama_index</span> <span class="kn">import</span> <span class="n">StorageContext</span><span class="p">,</span> <span class="n">load_index_from_storage</span>

            <span class="c1"># rebuild storage context</span>
            <span class="n">storage_context</span> <span class="o">=</span> <span class="n">StorageContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span><span class="n">persist_dir</span><span class="o">=</span><span class="n">cache_dir</span><span class="p">)</span>
            <span class="c1"># load index</span>
            <span class="n">index</span> <span class="o">=</span> <span class="n">load_index_from_storage</span><span class="p">(</span><span class="n">storage_context</span><span class="p">)</span>
        <span class="k">elif</span> <span class="n">documents</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="o">.</span><span class="n">from_documents</span><span class="p">(</span>
                <span class="n">documents</span><span class="o">=</span><span class="n">documents</span><span class="p">,</span> <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">cache_dir</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">cache_dir</span><span class="p">):</span>
            <span class="n">index</span><span class="o">.</span><span class="n">storage_context</span><span class="o">.</span><span class="n">persist</span><span class="p">(</span><span class="n">persist_dir</span><span class="o">=</span><span class="n">cache_dir</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">vector_retriever</span> <span class="o">=</span> <span class="n">index</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span>
            <span class="n">similarity_top_k</span><span class="o">=</span><span class="n">vector_similarity_top_k</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">bm25_retriever</span> <span class="o">=</span> <span class="n">BM25Retriever</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
            <span class="n">docstore</span><span class="o">=</span><span class="n">index</span><span class="o">.</span><span class="n">docstore</span><span class="p">,</span> <span class="n">similarity_top_k</span><span class="o">=</span><span class="n">bm25_similarity_top_k</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">fusion_retriever</span> <span class="o">=</span> <span class="n">QueryFusionRetriever</span><span class="p">(</span>
            <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">vector_retriever</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">bm25_retriever</span><span class="p">],</span>
            <span class="n">similarity_top_k</span><span class="o">=</span><span class="n">fusion_similarity_top_k</span><span class="p">,</span>
            <span class="n">num_queries</span><span class="o">=</span><span class="n">num_queries</span><span class="p">,</span>  <span class="c1"># set this to 1 to disable query generation</span>
            <span class="n">mode</span><span class="o">=</span><span class="n">mode</span><span class="p">,</span>
            <span class="n">use_async</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="c1"># query_gen_prompt="...",  # we could override the query generation prompt here</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span> <span class="o">=</span> <span class="n">RetrieverQueryEngine</span><span class="o">.</span><span class="n">from_args</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">fusion_retriever</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"vector_retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_retriever</span><span class="p">,</span>
            <span class="s2">"bm25_retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">bm25_retriever</span><span class="p">,</span>
            <span class="s2">"fusion_retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">fusion_retriever</span><span class="p">,</span>
            <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">retrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Retrieve."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">fusion_retriever</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/fusion_retriever/#llama_index.packs.fusion_retriever.HybridFusionRetrieverPack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-fusion-retriever/llama_index/packs/fusion_retriever/hybrid_fusion/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"vector_retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_retriever</span><span class="p">,</span>
        <span class="s2">"bm25_retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">bm25_retriever</span><span class="p">,</span>
        <span class="s2">"fusion_retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">fusion_retriever</span><span class="p">,</span>
        <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### retrieve [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/fusion_retriever/#llama_index.packs.fusion_retriever.HybridFusionRetrieverPack.retrieve "Permanent link")

```
retrieve(query_str: str) -> Any
```

Retrieve.

Source code in `llama-index-packs/llama-index-packs-fusion-retriever/llama_index/packs/fusion_retriever/hybrid_fusion/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">retrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Retrieve."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">fusion_retriever</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/fusion_retriever/#llama_index.packs.fusion_retriever.HybridFusionRetrieverPack.run "Permanent link")

```
run(*args: Any, **kwargs: Any) -> Any
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-fusion-retriever/llama_index/packs/fusion_retriever/hybrid_fusion/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

QueryRewritingRetrieverPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/fusion_retriever/#llama_index.packs.fusion_retriever.QueryRewritingRetrieverPack "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Query rewriting retriever pack.

Given input nodes, build a vector index.

Then rewrite the query into multiple queries and rerank the results.

Source code in `llama-index-packs/llama-index-packs-fusion-retriever/llama_index/packs/fusion_retriever/query_rewrite/base.py`

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
<span class="normal">66</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">QueryRewritingRetrieverPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Query rewriting retriever pack.</span>

<span class="sd">    Given input nodes, build a vector index.</span>

<span class="sd">    Then rewrite the query into multiple queries and</span>
<span class="sd">    rerank the results.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">TextNode</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">chunk_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">256</span><span class="p">,</span>
        <span class="n">mode</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"reciprocal_rerank"</span><span class="p">,</span>
        <span class="n">vector_similarity_top_k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span>
        <span class="n">fusion_similarity_top_k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span>
        <span class="n">num_queries</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">4</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="n">service_context</span> <span class="o">=</span> <span class="n">ServiceContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span><span class="n">chunk_size</span><span class="o">=</span><span class="n">chunk_size</span><span class="p">)</span>
        <span class="n">index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">vector_retriever</span> <span class="o">=</span> <span class="n">index</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span>
            <span class="n">similarity_top_k</span><span class="o">=</span><span class="n">vector_similarity_top_k</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">fusion_retriever</span> <span class="o">=</span> <span class="n">QueryFusionRetriever</span><span class="p">(</span>
            <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">vector_retriever</span><span class="p">],</span>
            <span class="n">similarity_top_k</span><span class="o">=</span><span class="n">fusion_similarity_top_k</span><span class="p">,</span>
            <span class="n">num_queries</span><span class="o">=</span><span class="n">num_queries</span><span class="p">,</span>  <span class="c1"># set this to 1 to disable query generation</span>
            <span class="n">mode</span><span class="o">=</span><span class="n">mode</span><span class="p">,</span>
            <span class="n">use_async</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="c1"># query_gen_prompt="...",  # we could override the query generation prompt here</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span> <span class="o">=</span> <span class="n">RetrieverQueryEngine</span><span class="o">.</span><span class="n">from_args</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">fusion_retriever</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"vector_retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_retriever</span><span class="p">,</span>
            <span class="s2">"fusion_retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">fusion_retriever</span><span class="p">,</span>
            <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">retrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Retrieve."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">fusion_retriever</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/fusion_retriever/#llama_index.packs.fusion_retriever.QueryRewritingRetrieverPack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-fusion-retriever/llama_index/packs/fusion_retriever/query_rewrite/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"vector_retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_retriever</span><span class="p">,</span>
        <span class="s2">"fusion_retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">fusion_retriever</span><span class="p">,</span>
        <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### retrieve [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/fusion_retriever/#llama_index.packs.fusion_retriever.QueryRewritingRetrieverPack.retrieve "Permanent link")

```
retrieve(query_str: str) -> Any
```

Retrieve.

Source code in `llama-index-packs/llama-index-packs-fusion-retriever/llama_index/packs/fusion_retriever/query_rewrite/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">retrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Retrieve."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">fusion_retriever</span><span class="o">.</span><span class="n">retrieve</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/fusion_retriever/#llama_index.packs.fusion_retriever.QueryRewritingRetrieverPack.run "Permanent link")

```
run(*args: Any, **kwargs: Any) -> Any
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-fusion-retriever/llama_index/packs/fusion_retriever/query_rewrite/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Finchat](https://docs.llamaindex.ai/en/stable/api_reference/packs/finchat/)[Next Fuzzy citation](https://docs.llamaindex.ai/en/stable/api_reference/packs/fuzzy_citation/)
