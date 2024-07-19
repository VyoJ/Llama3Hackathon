Title: Metadata replacement - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/metadata_replacement/

Markdown Content:
Metadata replacement - LlamaIndex


Node PostProcessor module.

MetadataReplacementPostProcessor [#](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/metadata_replacement/#llama_index.core.postprocessor.MetadataReplacementPostProcessor "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseNodePostprocessor](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/#llama_index.core.postprocessor.types.BaseNodePostprocessor "llama_index.core.postprocessor.types.BaseNodePostprocessor")`

Source code in `llama-index-core/llama_index/core/postprocessor/metadata_replacement.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 8</span>
<span class="normal"> 9</span>
<span class="normal">10</span>
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
<span class="normal">33</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">MetadataReplacementPostProcessor</span><span class="p">(</span><span class="n">BaseNodePostprocessor</span><span class="p">):</span>
    <span class="n">target_metadata_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span>
        <span class="n">description</span><span class="o">=</span><span class="s2">"Target metadata key to replace node content with."</span>
    <span class="p">)</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">target_metadata_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">target_metadata_key</span><span class="o">=</span><span class="n">target_metadata_key</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"MetadataReplacementPostProcessor"</span>

    <span class="k">def</span> <span class="nf">_postprocess_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">QueryBundle</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">n</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">set_content</span><span class="p">(</span>
                <span class="n">n</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">target_metadata_key</span><span class="p">,</span>
                    <span class="n">n</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">),</span>
                <span class="p">)</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="n">nodes</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Longllmlingua](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/longllmlingua/)[Next Mixedbreadai rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/mixedbreadai_rerank/)
