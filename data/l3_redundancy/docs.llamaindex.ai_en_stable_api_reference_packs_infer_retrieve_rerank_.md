Title: Infer retrieve rerank - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/infer_retrieve_rerank/

Markdown Content:
Infer retrieve rerank - LlamaIndex


InferRetrieveRerankPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/infer_retrieve_rerank/#llama_index.packs.infer_retrieve_rerank.InferRetrieveRerankPack "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Infer Retrieve Rerank pack.

Source code in `llama-index-packs/llama-index-packs-infer-retrieve-rerank/llama_index/packs/infer_retrieve_rerank/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 99</span>
<span class="normal">100</span>
<span class="normal">101</span>
<span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span>
<span class="normal">107</span>
<span class="normal">108</span>
<span class="normal">109</span>
<span class="normal">110</span>
<span class="normal">111</span>
<span class="normal">112</span>
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
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">InferRetrieveRerankPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Infer Retrieve Rerank pack."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">labels</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">pred_context</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="n">reranker_top_n</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">3</span><span class="p">,</span>
        <span class="n">infer_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">PromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">rerank_prompt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">PromptTemplate</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="c1"># NOTE: we use 16k model by default to fit longer contexts</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">OpenAI</span><span class="p">(</span><span class="n">model</span><span class="o">=</span><span class="s2">"gpt-3.5-turbo-16k"</span><span class="p">)</span>
        <span class="n">label_nodes</span> <span class="o">=</span> <span class="p">[</span><span class="n">TextNode</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">label</span><span class="p">)</span> <span class="k">for</span> <span class="n">label</span> <span class="ow">in</span> <span class="n">labels</span><span class="p">]</span>
        <span class="n">pipeline</span> <span class="o">=</span> <span class="n">IngestionPipeline</span><span class="p">(</span><span class="n">transformations</span><span class="o">=</span><span class="p">[</span><span class="n">OpenAIEmbedding</span><span class="p">()])</span>
        <span class="n">label_nodes_w_embed</span> <span class="o">=</span> <span class="n">pipeline</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">documents</span><span class="o">=</span><span class="n">label_nodes</span><span class="p">)</span>

        <span class="n">index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="p">(</span><span class="n">label_nodes_w_embed</span><span class="p">,</span> <span class="n">show_progress</span><span class="o">=</span><span class="n">verbose</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">label_retriever</span> <span class="o">=</span> <span class="n">index</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span><span class="n">similarity_top_k</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">pred_context</span> <span class="o">=</span> <span class="n">pred_context</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">reranker_top_n</span> <span class="o">=</span> <span class="n">reranker_top_n</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span> <span class="o">=</span> <span class="n">verbose</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">infer_prompt</span> <span class="o">=</span> <span class="n">infer_prompt</span> <span class="ow">or</span> <span class="n">INFER_PROMPT_TMPL</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">rerank_prompt</span> <span class="o">=</span> <span class="n">rerank_prompt</span> <span class="ow">or</span> <span class="n">RERANK_PROMPT_TMPL</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
            <span class="s2">"label_retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">label_retriever</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="n">inputs</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"inputs"</span><span class="p">,</span> <span class="p">[])</span>
        <span class="n">pred_reactions</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="nb">input</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">inputs</span><span class="p">):</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span><span class="p">:</span>
                <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="se">\n\n</span><span class="s2">&gt; Generating predictions for input </span><span class="si">{</span><span class="n">idx</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="nb">input</span><span class="p">[:</span><span class="mi">300</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="n">cur_pred_reactions</span> <span class="o">=</span> <span class="n">infer_retrieve_rerank</span><span class="p">(</span>
                <span class="nb">input</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">label_retriever</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">pred_context</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">infer_prompt</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">rerank_prompt</span><span class="p">,</span>
                <span class="n">reranker_top_n</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">reranker_top_n</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span><span class="p">:</span>
                <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Generated predictions: </span><span class="si">{</span><span class="n">cur_pred_reactions</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

            <span class="n">pred_reactions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">cur_pred_reactions</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">pred_reactions</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/infer_retrieve_rerank/#llama_index.packs.infer_retrieve_rerank.InferRetrieveRerankPack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-infer-retrieve-rerank/llama_index/packs/infer_retrieve_rerank/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
        <span class="s2">"label_retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">label_retriever</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/infer_retrieve_rerank/#llama_index.packs.infer_retrieve_rerank.InferRetrieveRerankPack.run "Permanent link")

```
run(*args: Any, **kwargs: Any) -> Any
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-infer-retrieve-rerank/llama_index/packs/infer_retrieve_rerank/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="n">inputs</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"inputs"</span><span class="p">,</span> <span class="p">[])</span>
    <span class="n">pred_reactions</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="nb">input</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">inputs</span><span class="p">):</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="se">\n\n</span><span class="s2">&gt; Generating predictions for input </span><span class="si">{</span><span class="n">idx</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="nb">input</span><span class="p">[:</span><span class="mi">300</span><span class="p">]</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">cur_pred_reactions</span> <span class="o">=</span> <span class="n">infer_retrieve_rerank</span><span class="p">(</span>
            <span class="nb">input</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">label_retriever</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">pred_context</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">infer_prompt</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">rerank_prompt</span><span class="p">,</span>
            <span class="n">reranker_top_n</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">reranker_top_n</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">verbose</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Generated predictions: </span><span class="si">{</span><span class="n">cur_pred_reactions</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="n">pred_reactions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">cur_pred_reactions</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">pred_reactions</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Index](https://docs.llamaindex.ai/en/stable/api_reference/packs/)[Next Koda retriever](https://docs.llamaindex.ai/en/stable/api_reference/packs/koda_retriever/)
