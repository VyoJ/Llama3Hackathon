Title: Long context reorder - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/long_context_reorder/

Markdown Content:
Long context reorder - LlamaIndex


Node PostProcessor module.

LongContextReorder [#](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/long_context_reorder/#llama_index.core.postprocessor.LongContextReorder "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseNodePostprocessor](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/#llama_index.core.postprocessor.types.BaseNodePostprocessor "llama_index.core.postprocessor.types.BaseNodePostprocessor")`

Models struggle to access significant details found in the center of extended contexts. A study (https://arxiv.org/abs/2307.03172) observed that the best performance typically arises when crucial data is positioned at the start or conclusion of the input context. Additionally, as the input context lengthens, performance drops notably, even in models designed for long contexts.".

Source code in `llama-index-core/llama_index/core/postprocessor/node.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">364</span>
<span class="normal">365</span>
<span class="normal">366</span>
<span class="normal">367</span>
<span class="normal">368</span>
<span class="normal">369</span>
<span class="normal">370</span>
<span class="normal">371</span>
<span class="normal">372</span>
<span class="normal">373</span>
<span class="normal">374</span>
<span class="normal">375</span>
<span class="normal">376</span>
<span class="normal">377</span>
<span class="normal">378</span>
<span class="normal">379</span>
<span class="normal">380</span>
<span class="normal">381</span>
<span class="normal">382</span>
<span class="normal">383</span>
<span class="normal">384</span>
<span class="normal">385</span>
<span class="normal">386</span>
<span class="normal">387</span>
<span class="normal">388</span>
<span class="normal">389</span>
<span class="normal">390</span>
<span class="normal">391</span>
<span class="normal">392</span>
<span class="normal">393</span>
<span class="normal">394</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">LongContextReorder</span><span class="p">(</span><span class="n">BaseNodePostprocessor</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Models struggle to access significant details found</span>
<span class="sd">    in the center of extended contexts. A study</span>
<span class="sd">    (https://arxiv.org/abs/2307.03172) observed that the best</span>
<span class="sd">    performance typically arises when crucial data is positioned</span>
<span class="sd">    at the start or conclusion of the input context. Additionally,</span>
<span class="sd">    as the input context lengthens, performance drops notably, even</span>
<span class="sd">    in models designed for long contexts.".</span>
<span class="sd">    """</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"LongContextReorder"</span>

    <span class="k">def</span> <span class="nf">_postprocess_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">QueryBundle</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Postprocess nodes."""</span>
        <span class="n">reordered_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">ordered_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span>
            <span class="n">nodes</span><span class="p">,</span> <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="o">.</span><span class="n">score</span> <span class="k">if</span> <span class="n">x</span><span class="o">.</span><span class="n">score</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="k">else</span> <span class="mi">0</span>
        <span class="p">)</span>
        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">node</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">ordered_nodes</span><span class="p">):</span>
            <span class="k">if</span> <span class="n">i</span> <span class="o">%</span> <span class="mi">2</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
                <span class="n">reordered_nodes</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">node</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">reordered_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">reordered_nodes</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Llm rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/llm_rerank/)[Next Longllmlingua](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/longllmlingua/)
