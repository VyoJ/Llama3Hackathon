Title: Subdoc summary - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/subdoc_summary/

Markdown Content:
Subdoc summary - LlamaIndex


SubDocSummaryPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/subdoc_summary/#llama_index.packs.subdoc_summary.SubDocSummaryPack "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.BaseLlamaPack")`

Pack for injecting sub-doc metadata into each chunk.

Source code in `llama-index-packs/llama-index-packs-subdoc-summary/llama_index/packs/subdoc_summary/base.py`

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
<span class="normal">93</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">SubDocSummaryPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Pack for injecting sub-doc metadata into each chunk."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span>
        <span class="n">parent_chunk_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">8192</span><span class="p">,</span>
        <span class="n">parent_chunk_overlap</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">512</span><span class="p">,</span>
        <span class="n">child_chunk_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">512</span><span class="p">,</span>
        <span class="n">child_chunk_overlap</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">32</span><span class="p">,</span>
        <span class="n">summary_prompt_str</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_SUMMARY_PROMPT_STR</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">embed_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseEmbedding</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">parent_chunk_size</span> <span class="o">=</span> <span class="n">parent_chunk_size</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">child_chunk_size</span> <span class="o">=</span> <span class="n">child_chunk_size</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">parent_splitter</span> <span class="o">=</span> <span class="n">SentenceSplitter</span><span class="p">(</span>
            <span class="n">chunk_size</span><span class="o">=</span><span class="n">parent_chunk_size</span><span class="p">,</span> <span class="n">chunk_overlap</span><span class="o">=</span><span class="n">parent_chunk_overlap</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">child_splitter</span> <span class="o">=</span> <span class="n">SentenceSplitter</span><span class="p">(</span>
            <span class="n">chunk_size</span><span class="o">=</span><span class="n">child_chunk_size</span><span class="p">,</span> <span class="n">chunk_overlap</span><span class="o">=</span><span class="n">child_chunk_overlap</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">summary_prompt_str</span> <span class="o">=</span> <span class="n">summary_prompt_str</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">embed_model</span> <span class="o">=</span> <span class="n">embed_model</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span>

        <span class="n">parent_nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">parent_splitter</span><span class="o">.</span><span class="n">get_nodes_from_documents</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span>
        <span class="n">all_child_nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="c1"># For each parent node, extract the child nodes and print the text</span>
        <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">parent_node</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">parent_nodes</span><span class="p">):</span>
            <span class="k">if</span> <span class="n">verbose</span><span class="p">:</span>
                <span class="n">print_text</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"&gt; Processing parent chunk </span><span class="si">{</span><span class="n">idx</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mi">1</span><span class="si">}</span><span class="s2"> of </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">parent_nodes</span><span class="p">)</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span>
                    <span class="n">color</span><span class="o">=</span><span class="s2">"blue"</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="c1"># get summary</span>
            <span class="n">summary_index</span> <span class="o">=</span> <span class="n">SummaryIndex</span><span class="p">([</span><span class="n">parent_node</span><span class="p">])</span>
            <span class="n">summary_query_engine</span> <span class="o">=</span> <span class="n">summary_index</span><span class="o">.</span><span class="n">as_query_engine</span><span class="p">(</span>
                <span class="n">response_mode</span><span class="o">=</span><span class="s2">"tree_summarize"</span>
            <span class="p">)</span>
            <span class="n">parent_summary</span> <span class="o">=</span> <span class="n">summary_query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">DEFAULT_SUMMARY_PROMPT_STR</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">verbose</span><span class="p">:</span>
                <span class="n">print_text</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Extracted summary: </span><span class="si">{</span><span class="n">parent_summary</span><span class="si">}</span><span class="se">\n</span><span class="s2">"</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">"pink"</span><span class="p">)</span>

            <span class="c1"># attach summary to all child nodes</span>
            <span class="n">child_nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">child_splitter</span><span class="o">.</span><span class="n">get_nodes_from_documents</span><span class="p">([</span><span class="n">parent_node</span><span class="p">])</span>
            <span class="k">for</span> <span class="n">child_node</span> <span class="ow">in</span> <span class="n">child_nodes</span><span class="p">:</span>
                <span class="n">child_node</span><span class="o">.</span><span class="n">metadata</span><span class="p">[</span><span class="s2">"context_summary"</span><span class="p">]</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">parent_summary</span><span class="p">)</span>

            <span class="n">all_child_nodes</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">child_nodes</span><span class="p">)</span>

        <span class="c1"># build vector index for child nodes</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">vector_index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="p">(</span>
            <span class="n">all_child_nodes</span><span class="p">,</span> <span class="n">embed_model</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">embed_model</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">vector_retriever</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_index</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">vector_query_engine</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_index</span><span class="o">.</span><span class="n">as_query_engine</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="n">llm</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span> <span class="o">=</span> <span class="n">verbose</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"vector_index"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_index</span><span class="p">,</span>
            <span class="s2">"vector_retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_retriever</span><span class="p">,</span>
            <span class="s2">"vector_query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_query_engine</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/subdoc_summary/#llama_index.packs.subdoc_summary.SubDocSummaryPack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-subdoc-summary/llama_index/packs/subdoc_summary/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"vector_index"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_index</span><span class="p">,</span>
        <span class="s2">"vector_retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_retriever</span><span class="p">,</span>
        <span class="s2">"vector_query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_query_engine</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/subdoc_summary/#llama_index.packs.subdoc_summary.SubDocSummaryPack.run "Permanent link")

```
run(*args: Any, **kwargs: Any) -> Any
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-subdoc-summary/llama_index/packs/subdoc_summary/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Sub question weaviate](https://docs.llamaindex.ai/en/stable/api_reference/packs/sub_question_weaviate/)[Next Tables](https://docs.llamaindex.ai/en/stable/api_reference/packs/tables/)
