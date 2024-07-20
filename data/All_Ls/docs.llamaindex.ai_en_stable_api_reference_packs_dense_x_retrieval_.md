Title: Dense x retrieval - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/dense_x_retrieval/

Markdown Content:
Dense x retrieval - LlamaIndex


DenseXRetrievalPack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/dense_x_retrieval/#llama_index.packs.dense_x_retrieval.DenseXRetrievalPack "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

Source code in `llama-index-packs/llama-index-packs-dense-x-retrieval/llama_index/packs/dense_x_retrieval/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 69</span>
<span class="normal"> 70</span>
<span class="normal"> 71</span>
<span class="normal"> 72</span>
<span class="normal"> 73</span>
<span class="normal"> 74</span>
<span class="normal"> 75</span>
<span class="normal"> 76</span>
<span class="normal"> 77</span>
<span class="normal"> 78</span>
<span class="normal"> 79</span>
<span class="normal"> 80</span>
<span class="normal"> 81</span>
<span class="normal"> 82</span>
<span class="normal"> 83</span>
<span class="normal"> 84</span>
<span class="normal"> 85</span>
<span class="normal"> 86</span>
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
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span>
<span class="normal">160</span>
<span class="normal">161</span>
<span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span>
<span class="normal">165</span>
<span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">DenseXRetrievalPack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">documents</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span>
        <span class="n">proposition_llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">query_llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">embed_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseEmbedding</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">text_splitter</span><span class="p">:</span> <span class="n">TextSplitter</span> <span class="o">=</span> <span class="n">SentenceSplitter</span><span class="p">(),</span>
        <span class="n">similarity_top_k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">4</span><span class="p">,</span>
        <span class="n">streaming</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_proposition_llm</span> <span class="o">=</span> <span class="n">proposition_llm</span> <span class="ow">or</span> <span class="n">OpenAI</span><span class="p">(</span>
            <span class="n">model</span><span class="o">=</span><span class="s2">"gpt-3.5-turbo"</span><span class="p">,</span>
            <span class="n">temperature</span><span class="o">=</span><span class="mf">0.1</span><span class="p">,</span>
            <span class="n">max_tokens</span><span class="o">=</span><span class="mi">750</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">embed_model</span> <span class="o">=</span> <span class="n">embed_model</span> <span class="ow">or</span> <span class="n">OpenAIEmbedding</span><span class="p">(</span><span class="n">embed_batch_size</span><span class="o">=</span><span class="mi">128</span><span class="p">)</span>

        <span class="n">nodes</span> <span class="o">=</span> <span class="n">text_splitter</span><span class="o">.</span><span class="n">get_nodes_from_documents</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span>
        <span class="n">sub_nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_gen_propositions</span><span class="p">(</span><span class="n">nodes</span><span class="p">)</span>

        <span class="n">all_nodes</span> <span class="o">=</span> <span class="n">nodes</span> <span class="o">+</span> <span class="n">sub_nodes</span>
        <span class="n">all_nodes_dict</span> <span class="o">=</span> <span class="p">{</span><span class="n">n</span><span class="o">.</span><span class="n">node_id</span><span class="p">:</span> <span class="n">n</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">all_nodes</span><span class="p">}</span>

        <span class="n">service_context</span> <span class="o">=</span> <span class="n">ServiceContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
            <span class="n">llm</span><span class="o">=</span><span class="n">query_llm</span> <span class="ow">or</span> <span class="n">OpenAI</span><span class="p">(),</span>
            <span class="n">embed_model</span><span class="o">=</span><span class="n">embed_model</span><span class="p">,</span>
            <span class="n">num_output</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_proposition_llm</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">num_output</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">vector_index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="p">(</span>
            <span class="n">all_nodes</span><span class="p">,</span> <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span> <span class="n">show_progress</span><span class="o">=</span><span class="kc">True</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">retriever</span> <span class="o">=</span> <span class="n">RecursiveRetriever</span><span class="p">(</span>
            <span class="s2">"vector"</span><span class="p">,</span>
            <span class="n">retriever_dict</span><span class="o">=</span><span class="p">{</span>
                <span class="s2">"vector"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">vector_index</span><span class="o">.</span><span class="n">as_retriever</span><span class="p">(</span>
                    <span class="n">similarity_top_k</span><span class="o">=</span><span class="n">similarity_top_k</span>
                <span class="p">)</span>
            <span class="p">},</span>
            <span class="n">node_dict</span><span class="o">=</span><span class="n">all_nodes_dict</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span> <span class="o">=</span> <span class="n">RetrieverQueryEngine</span><span class="o">.</span><span class="n">from_args</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">retriever</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
            <span class="n">streaming</span><span class="o">=</span><span class="n">streaming</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aget_proposition</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">:</span> <span class="n">TextNode</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">TextNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get proposition."""</span>
        <span class="n">inital_output</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_proposition_llm</span><span class="o">.</span><span class="n">apredict</span><span class="p">(</span>
            <span class="n">PROPOSITIONS_PROMPT</span><span class="p">,</span> <span class="n">node_text</span><span class="o">=</span><span class="n">node</span><span class="o">.</span><span class="n">text</span>
        <span class="p">)</span>
        <span class="n">outputs</span> <span class="o">=</span> <span class="n">inital_output</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">"</span><span class="p">)</span>

        <span class="n">all_propositions</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">for</span> <span class="n">output</span> <span class="ow">in</span> <span class="n">outputs</span><span class="p">:</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">output</span><span class="o">.</span><span class="n">strip</span><span class="p">():</span>
                <span class="k">continue</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">output</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s2">"]"</span><span class="p">):</span>
                <span class="k">if</span> <span class="ow">not</span> <span class="n">output</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s1">'"'</span><span class="p">)</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">output</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span>
                    <span class="s2">","</span>
                <span class="p">):</span>
                    <span class="n">output</span> <span class="o">=</span> <span class="n">output</span> <span class="o">+</span> <span class="s1">'"'</span>
                <span class="n">output</span> <span class="o">=</span> <span class="n">output</span> <span class="o">+</span> <span class="s2">" ]"</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">output</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">"["</span><span class="p">):</span>
                <span class="k">if</span> <span class="ow">not</span> <span class="n">output</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s1">'"'</span><span class="p">):</span>
                    <span class="n">output</span> <span class="o">=</span> <span class="s1">'"'</span> <span class="o">+</span> <span class="n">output</span>
                <span class="n">output</span> <span class="o">=</span> <span class="s2">"[ "</span> <span class="o">+</span> <span class="n">output</span>

            <span class="k">try</span><span class="p">:</span>
                <span class="n">propositions</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">output</span><span class="p">)</span>
            <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
                <span class="c1"># fallback to yaml</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="n">propositions</span> <span class="o">=</span> <span class="n">yaml</span><span class="o">.</span><span class="n">safe_load</span><span class="p">(</span><span class="n">output</span><span class="p">)</span>
                <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
                    <span class="c1"># fallback to next output</span>
                    <span class="k">continue</span>

            <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">propositions</span><span class="p">,</span> <span class="nb">list</span><span class="p">):</span>
                <span class="k">continue</span>

            <span class="n">all_propositions</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">propositions</span><span class="p">)</span>

        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">all_propositions</span><span class="p">,</span> <span class="nb">list</span><span class="p">)</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="p">[</span><span class="n">TextNode</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">prop</span><span class="p">)</span> <span class="k">for</span> <span class="n">prop</span> <span class="ow">in</span> <span class="n">all_propositions</span> <span class="k">if</span> <span class="n">prop</span><span class="p">]</span>

        <span class="k">return</span> <span class="p">[</span><span class="n">IndexNode</span><span class="o">.</span><span class="n">from_text_node</span><span class="p">(</span><span class="n">n</span><span class="p">,</span> <span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">_gen_propositions</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">TextNode</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">TextNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get propositions."""</span>
        <span class="n">sub_nodes</span> <span class="o">=</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
            <span class="n">run_jobs</span><span class="p">(</span>
                <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_aget_proposition</span><span class="p">(</span><span class="n">node</span><span class="p">)</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">],</span>
                <span class="n">show_progress</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">workers</span><span class="o">=</span><span class="mi">8</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>

        <span class="c1"># Flatten list</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">node</span> <span class="k">for</span> <span class="n">sub_node</span> <span class="ow">in</span> <span class="n">sub_nodes</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">sub_node</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
            <span class="s2">"retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">retriever</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/dense_x_retrieval/#llama_index.packs.dense_x_retrieval.DenseXRetrievalPack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-dense-x-retrieval/llama_index/packs/dense_x_retrieval/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
        <span class="s2">"retriever"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">retriever</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/dense_x_retrieval/#llama_index.packs.dense_x_retrieval.DenseXRetrievalPack.run "Permanent link")

```
run(query_str: str, **kwargs: Any) -> RESPONSE_TYPE
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-dense-x-retrieval/llama_index/packs/dense_x_retrieval/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RESPONSE_TYPE</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Deeplake multimodal retrieval](https://docs.llamaindex.ai/en/stable/api_reference/packs/deeplake_multimodal_retrieval/)[Next Diff private simple dataset](https://docs.llamaindex.ai/en/stable/api_reference/packs/diff_private_simple_dataset/)
