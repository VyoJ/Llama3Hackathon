Title: Embedding recency - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/embedding_recency/

Markdown Content:
Embedding recency - LlamaIndex


Node PostProcessor module.

EmbeddingRecencyPostprocessor [#](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/embedding_recency/#llama_index.core.postprocessor.EmbeddingRecencyPostprocessor "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseNodePostprocessor](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/#llama_index.core.postprocessor.types.BaseNodePostprocessor "llama_index.core.postprocessor.types.BaseNodePostprocessor")`

Embedding Recency post-processor.

Source code in `llama-index-core/llama_index/core/postprocessor/node_recency.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 86</span>
<span class="normal"> 87</span>
<span class="normal"> 88</span>
<span class="normal"> 89</span>
<span class="normal"> 90</span>
<span class="normal"> 91</span>
<span class="normal"> 92</span>
<span class="normal"> 93</span>
<span class="normal"> 94</span>
<span class="normal"> 95</span>
<span class="normal"> 96</span>
<span class="normal"> 97</span>
<span class="normal"> 98</span>
<span class="normal"> 99</span>
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
<span class="normal">143</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">EmbeddingRecencyPostprocessor</span><span class="p">(</span><span class="n">BaseNodePostprocessor</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Embedding Recency post-processor."""</span>

    <span class="n">embed_model</span><span class="p">:</span> <span class="n">BaseEmbedding</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="k">lambda</span><span class="p">:</span> <span class="n">Settings</span><span class="o">.</span><span class="n">embed_model</span><span class="p">)</span>
    <span class="n">date_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"date"</span>
    <span class="n">similarity_cutoff</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="mf">0.7</span><span class="p">)</span>
    <span class="n">query_embedding_tmpl</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="n">DEFAULT_QUERY_EMBEDDING_TMPL</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"EmbeddingRecencyPostprocessor"</span>

    <span class="k">def</span> <span class="nf">_postprocess_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">],</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">QueryBundle</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Postprocess nodes."""</span>
        <span class="k">if</span> <span class="n">query_bundle</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Missing query bundle in extra info."</span><span class="p">)</span>

        <span class="c1"># sort nodes by date</span>
        <span class="n">node_dates</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">to_datetime</span><span class="p">(</span>
            <span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">metadata</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">date_key</span><span class="p">]</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>
        <span class="p">)</span>
        <span class="n">sorted_node_idxs</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">flip</span><span class="p">(</span><span class="n">node_dates</span><span class="o">.</span><span class="n">argsort</span><span class="p">())</span>
        <span class="n">sorted_nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">nodes</span><span class="p">[</span><span class="n">idx</span><span class="p">]</span> <span class="k">for</span> <span class="n">idx</span> <span class="ow">in</span> <span class="n">sorted_node_idxs</span><span class="p">]</span>

        <span class="c1"># get embeddings for each node</span>
        <span class="n">texts</span> <span class="o">=</span> <span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">EMBED</span><span class="p">)</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>
        <span class="n">text_embeddings</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">embed_model</span><span class="o">.</span><span class="n">get_text_embedding_batch</span><span class="p">(</span><span class="n">texts</span><span class="o">=</span><span class="n">texts</span><span class="p">)</span>

        <span class="n">node_ids_to_skip</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
        <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">node</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">sorted_nodes</span><span class="p">):</span>
            <span class="k">if</span> <span class="n">node</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span> <span class="ow">in</span> <span class="n">node_ids_to_skip</span><span class="p">:</span>
                <span class="k">continue</span>
            <span class="c1"># get query embedding for the "query" node</span>
            <span class="c1"># NOTE: not the same as the text embedding because</span>
            <span class="c1"># we want to optimize for retrieval results</span>

            <span class="n">query_text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_embedding_tmpl</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
                <span class="n">context_str</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">EMBED</span><span class="p">),</span>
            <span class="p">)</span>
            <span class="n">query_embedding</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">embed_model</span><span class="o">.</span><span class="n">get_query_embedding</span><span class="p">(</span><span class="n">query_text</span><span class="p">)</span>

            <span class="k">for</span> <span class="n">idx2</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">idx</span> <span class="o">+</span> <span class="mi">1</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">sorted_nodes</span><span class="p">)):</span>
                <span class="k">if</span> <span class="n">sorted_nodes</span><span class="p">[</span><span class="n">idx2</span><span class="p">]</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span> <span class="ow">in</span> <span class="n">node_ids_to_skip</span><span class="p">:</span>
                    <span class="k">continue</span>
                <span class="n">node2</span> <span class="o">=</span> <span class="n">sorted_nodes</span><span class="p">[</span><span class="n">idx2</span><span class="p">]</span>
                <span class="k">if</span> <span class="p">(</span>
                    <span class="n">np</span><span class="o">.</span><span class="n">dot</span><span class="p">(</span><span class="n">query_embedding</span><span class="p">,</span> <span class="n">text_embeddings</span><span class="p">[</span><span class="n">idx2</span><span class="p">])</span>
                    <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">similarity_cutoff</span>
                <span class="p">):</span>
                    <span class="n">node_ids_to_skip</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">node2</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span>

        <span class="k">return</span> <span class="p">[</span>
            <span class="n">node</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">sorted_nodes</span> <span class="k">if</span> <span class="n">node</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">node_ids_to_skip</span>
        <span class="p">]</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Dashscope rerank](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/dashscope_rerank/)[Next Fixed recency](https://docs.llamaindex.ai/en/stable/api_reference/postprocessor/fixed_recency/)
