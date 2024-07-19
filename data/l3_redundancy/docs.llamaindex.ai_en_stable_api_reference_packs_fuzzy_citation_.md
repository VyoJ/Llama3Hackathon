Title: Fuzzy citation - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/fuzzy_citation/

Markdown Content:
Fuzzy citation - LlamaIndex


FuzzyCitationEnginePack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/fuzzy_citation/#llama_index.packs.fuzzy_citation.FuzzyCitationEnginePack "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Source code in `llama-index-packs/llama-index-packs-fuzzy-citation/llama_index/packs/fuzzy_citation/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span>
<span class="normal">119</span>
<span class="normal">120</span>
<span class="normal">121</span>
<span class="normal">122</span>
<span class="normal">123</span>
<span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span>
<span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">FuzzyCitationEnginePack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query_engine</span><span class="p">:</span> <span class="n">BaseQueryEngine</span><span class="p">,</span> <span class="n">threshold</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_THRESHOLD</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">thefuzz</span> <span class="kn">import</span> <span class="n">fuzz</span>  <span class="c1"># noqa: F401</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"Please run `pip install thefuzz` to use the fuzzy citation engine."</span>
            <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span> <span class="o">=</span> <span class="n">FuzzyCitationQueryEngine</span><span class="p">(</span>
            <span class="n">query_engine</span><span class="o">=</span><span class="n">query_engine</span><span class="p">,</span> <span class="n">threshold</span><span class="o">=</span><span class="n">threshold</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
            <span class="s2">"query_engine_cls"</span><span class="p">:</span> <span class="n">FuzzyCitationQueryEngine</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/fuzzy_citation/#llama_index.packs.fuzzy_citation.FuzzyCitationEnginePack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-fuzzy-citation/llama_index/packs/fuzzy_citation/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
        <span class="s2">"query_engine_cls"</span><span class="p">:</span> <span class="n">FuzzyCitationQueryEngine</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/fuzzy_citation/#llama_index.packs.fuzzy_citation.FuzzyCitationEnginePack.run "Permanent link")

```
run(query_str: str, **kwargs: Any) -> RESPONSE_TYPE
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-fuzzy-citation/llama_index/packs/fuzzy_citation/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Fusion retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/fusion_retriever/)[Next Gmail openai agent](https://docs.llamaindex.ai/en/stable/api_reference/packs/gmail_openai_agent/)
