Title: Recursive retriever - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/recursive_retriever/

Markdown Content:
Recursive retriever - LlamaIndex


EmbeddedTablesUnstructuredRetrieverPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/recursive_retriever/#llama_index.packs.recursive_retriever.EmbeddedTablesUnstructuredRetrieverPack "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Embedded Tables + Unstructured.io Retriever pack.

Use unstructured.io to parse out embedded tables from an HTML document, build a node graph, and then run our recursive retriever against that.

**NOTE**: must take in a single HTML file.

Source code in `llama-index-packs/llama-index-packs-recursive-retriever/llama_index/packs/recursive_retriever/embedded_tables_unstructured/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">16</span>
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
<span class="normal">68</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">EmbeddedTablesUnstructuredRetrieverPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Embedded Tables + Unstructured.io Retriever pack.</span>

<span class="sd">    Use unstructured.io to parse out embedded tables from an HTML document, build</span>
<span class="sd">    a node graph, and then run our recursive retriever against that.</span>

<span class="sd">    **NOTE**: must take in a single HTML file.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">html_path</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">nodes_save_path</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">reader</span> <span class="o">=</span> <span class="n">FlatReader</span><span class="p">()</span>

        <span class="n">docs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">reader</span><span class="o">.</span><span class="n">load_data</span><span class="p">(</span><span class="n">Path</span><span class="p">(</span><span class="n">html_path</span><span class="p">))</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">node_parser</span> <span class="o">=</span> <span class="n">UnstructuredElementNodeParser</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">nodes_save_path</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">or</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">nodes_save_path</span><span class="p">):</span>
            <span class="n">raw_nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_parser</span><span class="o">.</span><span class="n">get_nodes_from_documents</span><span class="p">(</span><span class="n">docs</span><span class="p">)</span>
            <span class="n">pickle</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">raw_nodes</span><span class="p">,</span> <span class="nb">open</span><span class="p">(</span><span class="n">nodes_save_path</span><span class="p">,</span> <span class="s2">"wb"</span><span class="p">))</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">raw_nodes</span> <span class="o">=</span> <span class="n">pickle</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="nb">open</span><span class="p">(</span><span class="n">nodes_save_path</span><span class="p">,</span> <span class="s2">"rb"</span><span class="p">))</span>

        <span class="n">base_nodes</span><span class="p">,</span> <span class="n">node_mappings</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_parser</span><span class="o">.</span><span class="n">get_base_nodes_and_mappings</span><span class="p">(</span>
            <span class="n">raw_nodes</span>
        <span class="p">)</span>
        <span class="c1"># construct top-level vector index + query engine</span>
        <span class="n">vector_index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="p">(</span><span class="n">base_nodes</span><span class="p">)</span>
        <span class="n">vector_retriever</span> <span class="o">=</span> <span class="n">vector_index</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span><span class="n">similarity_top_k</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">recursive_retriever</span> <span class="o">=</span> <span class="n">RecursiveRetriever</span><span class="p">(</span>
            <span class="s2">"vector"</span><span class="p">,</span>
            <span class="n">retriever_dict</span><span class="o">=</span><span class="p">{</span><span class="s2">"vector"</span><span class="p">:</span> <span class="n">vector_retriever</span><span class="p">},</span>
            <span class="n">node_dict</span><span class="o">=</span><span class="n">node_mappings</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span> <span class="o">=</span> <span class="n">RetrieverQueryEngine</span><span class="o">.</span><span class="n">from_args</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">recursive_retriever</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"node_parser"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_parser</span><span class="p">,</span>
            <span class="s2">"recursive_retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">recursive_retriever</span><span class="p">,</span>
            <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/recursive_retriever/#llama_index.packs.recursive_retriever.EmbeddedTablesUnstructuredRetrieverPack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-recursive-retriever/llama_index/packs/recursive_retriever/embedded_tables_unstructured/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"node_parser"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_parser</span><span class="p">,</span>
        <span class="s2">"recursive_retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">recursive_retriever</span><span class="p">,</span>
        <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/recursive_retriever/#llama_index.packs.recursive_retriever.EmbeddedTablesUnstructuredRetrieverPack.run "Permanent link")

```
run(*args: Any, **kwargs: Any) -> Any
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-recursive-retriever/llama_index/packs/recursive_retriever/embedded_tables_unstructured/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

RecursiveRetrieverSmallToBigPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/recursive_retriever/#llama_index.packs.recursive_retriever.RecursiveRetrieverSmallToBigPack "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Small-to-big retrieval (with recursive retriever).

Given input documents, and an initial set of "parent" chunks, subdivide each chunk further into "child" chunks. Link each child chunk to its parent chunk, and index the child chunks.

Source code in `llama-index-packs/llama-index-packs-recursive-retriever/llama_index/packs/recursive_retriever/small_to_big/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">15</span>
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
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">RecursiveRetrieverSmallToBigPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Small-to-big retrieval (with recursive retriever).</span>

<span class="sd">    Given input documents, and an initial set of "parent" chunks,</span>
<span class="sd">    subdivide each chunk further into "child" chunks.</span>
<span class="sd">    Link each child chunk to its parent chunk, and index the child chunks.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">docs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="c1"># create the sentence window node parser w/ default settings</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">node_parser</span> <span class="o">=</span> <span class="n">SentenceSplitter</span><span class="p">(</span><span class="n">chunk_size</span><span class="o">=</span><span class="mi">1024</span><span class="p">)</span>
        <span class="n">base_nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_parser</span><span class="o">.</span><span class="n">get_nodes_from_documents</span><span class="p">(</span><span class="n">docs</span><span class="p">)</span>
        <span class="c1"># set node ids to be a constant</span>
        <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">node</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">base_nodes</span><span class="p">):</span>
            <span class="n">node</span><span class="o">.</span><span class="n">id_</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"node-</span><span class="si">{</span><span class="n">idx</span><span class="si">}</span><span class="s2">"</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">embed_model</span> <span class="o">=</span> <span class="n">resolve_embed_model</span><span class="p">(</span><span class="s2">"local:BAAI/bge-small-en"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="o">=</span> <span class="n">OpenAI</span><span class="p">(</span><span class="n">model</span><span class="o">=</span><span class="s2">"gpt-3.5-turbo"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">service_context</span> <span class="o">=</span> <span class="n">ServiceContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span> <span class="n">embed_model</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">embed_model</span>
        <span class="p">)</span>
        <span class="c1"># build graph of smaller chunks pointing to bigger parent chunks</span>
        <span class="c1"># make chunk overlap 0</span>
        <span class="n">sub_chunk_sizes</span> <span class="o">=</span> <span class="p">[</span><span class="mi">128</span><span class="p">,</span> <span class="mi">256</span><span class="p">,</span> <span class="mi">512</span><span class="p">]</span>
        <span class="n">sub_node_parsers</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">SentenceSplitter</span><span class="p">(</span><span class="n">chunk_size</span><span class="o">=</span><span class="n">c</span><span class="p">,</span> <span class="n">chunk_overlap</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span> <span class="k">for</span> <span class="n">c</span> <span class="ow">in</span> <span class="n">sub_chunk_sizes</span>
        <span class="p">]</span>

        <span class="n">all_nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">base_node</span> <span class="ow">in</span> <span class="n">base_nodes</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">sub_node_parsers</span><span class="p">:</span>
                <span class="n">sub_nodes</span> <span class="o">=</span> <span class="n">n</span><span class="o">.</span><span class="n">get_nodes_from_documents</span><span class="p">([</span><span class="n">base_node</span><span class="p">])</span>
                <span class="n">sub_inodes</span> <span class="o">=</span> <span class="p">[</span>
                    <span class="n">IndexNode</span><span class="o">.</span><span class="n">from_text_node</span><span class="p">(</span><span class="n">sn</span><span class="p">,</span> <span class="n">base_node</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span> <span class="k">for</span> <span class="n">sn</span> <span class="ow">in</span> <span class="n">sub_nodes</span>
                <span class="p">]</span>
                <span class="n">all_nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">sub_inodes</span><span class="p">)</span>

            <span class="c1"># also add original node to node</span>
            <span class="n">original_node</span> <span class="o">=</span> <span class="n">IndexNode</span><span class="o">.</span><span class="n">from_text_node</span><span class="p">(</span><span class="n">base_node</span><span class="p">,</span> <span class="n">base_node</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span>
            <span class="n">all_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">original_node</span><span class="p">)</span>
        <span class="n">all_nodes_dict</span> <span class="o">=</span> <span class="p">{</span><span class="n">n</span><span class="o">.</span><span class="n">node_id</span><span class="p">:</span> <span class="n">n</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">all_nodes</span><span class="p">}</span>

        <span class="c1"># define recursive retriever</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">vector_index_chunk</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="p">(</span>
            <span class="n">all_nodes</span><span class="p">,</span> <span class="n">service_context</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">service_context</span>
        <span class="p">)</span>
        <span class="n">vector_retriever_chunk</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_index_chunk</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span>
            <span class="n">similarity_top_k</span><span class="o">=</span><span class="mi">2</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">recursive_retriever</span> <span class="o">=</span> <span class="n">RecursiveRetriever</span><span class="p">(</span>
            <span class="s2">"vector"</span><span class="p">,</span>
            <span class="n">retriever_dict</span><span class="o">=</span><span class="p">{</span><span class="s2">"vector"</span><span class="p">:</span> <span class="n">vector_retriever_chunk</span><span class="p">},</span>
            <span class="n">node_dict</span><span class="o">=</span><span class="n">all_nodes_dict</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span> <span class="o">=</span> <span class="n">RetrieverQueryEngine</span><span class="o">.</span><span class="n">from_args</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">recursive_retriever</span><span class="p">,</span> <span class="n">service_context</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">service_context</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
            <span class="s2">"recursive_retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">recursive_retriever</span><span class="p">,</span>
            <span class="s2">"llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
            <span class="s2">"embed_model"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">embed_model</span><span class="p">,</span>
            <span class="s2">"service_context"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">service_context</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/recursive_retriever/#llama_index.packs.recursive_retriever.RecursiveRetrieverSmallToBigPack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-recursive-retriever/llama_index/packs/recursive_retriever/small_to_big/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
        <span class="s2">"recursive_retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">recursive_retriever</span><span class="p">,</span>
        <span class="s2">"llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
        <span class="s2">"embed_model"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">embed_model</span><span class="p">,</span>
        <span class="s2">"service_context"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">service_context</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/recursive_retriever/#llama_index.packs.recursive_retriever.RecursiveRetrieverSmallToBigPack.run "Permanent link")

```
run(*args: Any, **kwargs: Any) -> Any
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-recursive-retriever/llama_index/packs/recursive_retriever/small_to_big/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Raptor](https://docs.llamaindex.ai/en/stable/api_reference/packs/raptor/)[Next Redis ingestion pipeline](https://docs.llamaindex.ai/en/stable/api_reference/packs/redis_ingestion_pipeline/)
