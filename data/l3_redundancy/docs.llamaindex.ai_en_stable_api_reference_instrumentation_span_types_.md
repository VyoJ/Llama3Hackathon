Title: Span types - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/span_types/

Markdown Content:
Span types - LlamaIndex


BaseSpan [#](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/span_types/#llama_index.core.instrumentation.span.base.BaseSpan "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseModel`

Base data class representing a span.

Source code in `llama-index-core/llama_index/core/instrumentation/span/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 5</span>
<span class="normal"> 6</span>
<span class="normal"> 7</span>
<span class="normal"> 8</span>
<span class="normal"> 9</span>
<span class="normal">10</span>
<span class="normal">11</span>
<span class="normal">12</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">BaseSpan</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Base data class representing a span."""</span>

    <span class="n">id_</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="nb">str</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Id of span."</span><span class="p">)</span>
    <span class="n">parent_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Id of parent span."</span><span class="p">)</span>

    <span class="k">class</span> <span class="nc">Config</span><span class="p">:</span>
        <span class="n">arbitrary_types_allowed</span> <span class="o">=</span> <span class="kc">True</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Span handlers](https://docs.llamaindex.ai/en/stable/api_reference/instrumentation/span_handlers/)[Next Ai21](https://docs.llamaindex.ai/en/stable/api_reference/llms/ai21/)
