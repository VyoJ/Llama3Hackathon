Title: Nebulagraph query engine - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/packs/nebulagraph_query_engine/

Markdown Content:
Nebulagraph query engine - LlamaIndex


NebulaGraphQueryEnginePack [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/nebulagraph_query_engine/#llama_index.packs.nebulagraph_query_engine.NebulaGraphQueryEnginePack "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseLlamaPack](https://docs.llamaindex.ai/en/stable/api_reference/packs/#llama_index.core.llama_pack.BaseLlamaPack "llama_index.core.llama_pack.base.BaseLlamaPack")`

NebulaGraph Query Engine pack.

Source code in `llama-index-packs/llama-index-packs-nebulagraph-query-engine/llama_index/packs/nebulagraph_query_engine/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 37</span>
<span class="normal"> 38</span>
<span class="normal"> 39</span>
<span class="normal"> 40</span>
<span class="normal"> 41</span>
<span class="normal"> 42</span>
<span class="normal"> 43</span>
<span class="normal"> 44</span>
<span class="normal"> 45</span>
<span class="normal"> 46</span>
<span class="normal"> 47</span>
<span class="normal"> 48</span>
<span class="normal"> 49</span>
<span class="normal"> 50</span>
<span class="normal"> 51</span>
<span class="normal"> 52</span>
<span class="normal"> 53</span>
<span class="normal"> 54</span>
<span class="normal"> 55</span>
<span class="normal"> 56</span>
<span class="normal"> 57</span>
<span class="normal"> 58</span>
<span class="normal"> 59</span>
<span class="normal"> 60</span>
<span class="normal"> 61</span>
<span class="normal"> 62</span>
<span class="normal"> 63</span>
<span class="normal"> 64</span>
<span class="normal"> 65</span>
<span class="normal"> 66</span>
<span class="normal"> 67</span>
<span class="normal"> 68</span>
<span class="normal"> 69</span>
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
<span class="normal">180</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">NebulaGraphQueryEnginePack</span><span class="p">(</span><span class="n">BaseLlamaPack</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""NebulaGraph Query Engine pack."""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">username</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">password</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">ip_and_port</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">space_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">edge_types</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">rel_prop_names</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">tags</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">max_triplets_per_chunk</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
        <span class="n">docs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Document</span><span class="p">],</span>
        <span class="n">query_engine_type</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">NebulaGraphQueryEngineType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">[</span><span class="s2">"GRAPHD_HOST"</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"127.0.0.1"</span>
        <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">[</span><span class="s2">"NEBULA_USER"</span><span class="p">]</span> <span class="o">=</span> <span class="n">username</span>
        <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">[</span><span class="s2">"NEBULA_PASSWORD"</span><span class="p">]</span> <span class="o">=</span> <span class="n">password</span>
        <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">[</span>
            <span class="s2">"NEBULA_ADDRESS"</span>
        <span class="p">]</span> <span class="o">=</span> <span class="n">ip_and_port</span>  <span class="c1"># such as "127.0.0.1:9669" for local instance</span>

        <span class="n">nebulagraph_graph_store</span> <span class="o">=</span> <span class="n">NebulaGraphStore</span><span class="p">(</span>
            <span class="n">space_name</span><span class="o">=</span><span class="n">space_name</span><span class="p">,</span>
            <span class="n">edge_types</span><span class="o">=</span><span class="n">edge_types</span><span class="p">,</span>
            <span class="n">rel_prop_names</span><span class="o">=</span><span class="n">rel_prop_names</span><span class="p">,</span>
            <span class="n">tags</span><span class="o">=</span><span class="n">tags</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">nebulagraph_storage_context</span> <span class="o">=</span> <span class="n">StorageContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span>
            <span class="n">graph_store</span><span class="o">=</span><span class="n">nebulagraph_graph_store</span>
        <span class="p">)</span>

        <span class="c1"># define LLM</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">llm</span> <span class="o">=</span> <span class="n">OpenAI</span><span class="p">(</span><span class="n">temperature</span><span class="o">=</span><span class="mf">0.1</span><span class="p">,</span> <span class="n">model</span><span class="o">=</span><span class="s2">"gpt-3.5-turbo"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">service_context</span> <span class="o">=</span> <span class="n">ServiceContext</span><span class="o">.</span><span class="n">from_defaults</span><span class="p">(</span><span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">)</span>

        <span class="n">nebulagraph_index</span> <span class="o">=</span> <span class="n">KnowledgeGraphIndex</span><span class="o">.</span><span class="n">from_documents</span><span class="p">(</span>
            <span class="n">documents</span><span class="o">=</span><span class="n">docs</span><span class="p">,</span>
            <span class="n">storage_context</span><span class="o">=</span><span class="n">nebulagraph_storage_context</span><span class="p">,</span>
            <span class="n">max_triplets_per_chunk</span><span class="o">=</span><span class="n">max_triplets_per_chunk</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">service_context</span><span class="p">,</span>
            <span class="n">space_name</span><span class="o">=</span><span class="n">space_name</span><span class="p">,</span>
            <span class="n">edge_types</span><span class="o">=</span><span class="n">edge_types</span><span class="p">,</span>
            <span class="n">rel_prop_names</span><span class="o">=</span><span class="n">rel_prop_names</span><span class="p">,</span>
            <span class="n">tags</span><span class="o">=</span><span class="n">tags</span><span class="p">,</span>
            <span class="n">include_embeddings</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="c1"># create index</span>
        <span class="n">vector_index</span> <span class="o">=</span> <span class="n">VectorStoreIndex</span><span class="o">.</span><span class="n">from_documents</span><span class="p">(</span><span class="n">docs</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">query_engine_type</span> <span class="o"></span> <span class="n">NebulaGraphQueryEngineType</span><span class="o">.</span><span class="n">KG_HYBRID</span><span class="p">:</span>
            <span class="c1"># KG hybrid entity retrieval</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span> <span class="o">=</span> <span class="n">nebulagraph_index</span><span class="o">.</span><span class="n">as_query_engine</span><span class="p">(</span>
                <span class="n">include_text</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">response_mode</span><span class="o">=</span><span class="s2">"tree_summarize"</span><span class="p">,</span>
                <span class="n">embedding_mode</span><span class="o">=</span><span class="s2">"hybrid"</span><span class="p">,</span>
                <span class="n">similarity_top_k</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
                <span class="n">explore_global_knowledge</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="p">)</span>

        <span class="k">elif</span> <span class="n">query_engine_type</span> <span class="o"></span> <span class="n">NebulaGraphQueryEngineType</span><span class="o">.</span><span class="n">RAW_VECTOR_KG_COMBO</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">llama_index.core.query_engine</span> <span class="kn">import</span> <span class="n">RetrieverQueryEngine</span>

            <span class="c1"># create custom retriever</span>
            <span class="n">nebulagraph_vector_retriever</span> <span class="o">=</span> <span class="n">VectorIndexRetriever</span><span class="p">(</span><span class="n">index</span><span class="o">=</span><span class="n">vector_index</span><span class="p">)</span>
            <span class="n">nebulagraph_kg_retriever</span> <span class="o">=</span> <span class="n">KGTableRetriever</span><span class="p">(</span>
                <span class="n">index</span><span class="o">=</span><span class="n">nebulagraph_index</span><span class="p">,</span> <span class="n">retriever_mode</span><span class="o">=</span><span class="s2">"keyword"</span><span class="p">,</span> <span class="n">include_text</span><span class="o">=</span><span class="kc">False</span>
            <span class="p">)</span>
            <span class="n">nebulagraph_custom_retriever</span> <span class="o">=</span> <span class="n">CustomRetriever</span><span class="p">(</span>
                <span class="n">nebulagraph_vector_retriever</span><span class="p">,</span> <span class="n">nebulagraph_kg_retriever</span>
            <span class="p">)</span>

            <span class="c1"># create response synthesizer</span>
            <span class="n">nebulagraph_response_synthesizer</span> <span class="o">=</span> <span class="n">get_response_synthesizer</span><span class="p">(</span>
                <span class="n">service_context</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">service_context</span><span class="p">,</span>
                <span class="n">response_mode</span><span class="o">=</span><span class="s2">"tree_summarize"</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="c1"># Custom combo query engine</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span> <span class="o">=</span> <span class="n">RetrieverQueryEngine</span><span class="p">(</span>
                <span class="n">retriever</span><span class="o">=</span><span class="n">nebulagraph_custom_retriever</span><span class="p">,</span>
                <span class="n">response_synthesizer</span><span class="o">=</span><span class="n">nebulagraph_response_synthesizer</span><span class="p">,</span>
            <span class="p">)</span>

        <span class="k">elif</span> <span class="n">query_engine_type</span> <span class="o"></span> <span class="n">NebulaGraphQueryEngineType</span><span class="o">.</span><span class="n">KG_RAG_RETRIEVER</span><span class="p">:</span>
            <span class="c1"># using KnowledgeGraphRAGRetriever</span>
            <span class="kn">from</span> <span class="nn">llama_index.core.query_engine</span> <span class="kn">import</span> <span class="n">RetrieverQueryEngine</span>
            <span class="kn">from</span> <span class="nn">llama_index.core.retrievers</span> <span class="kn">import</span> <span class="n">KnowledgeGraphRAGRetriever</span>

            <span class="n">nebulagraph_graph_rag_retriever</span> <span class="o">=</span> <span class="n">KnowledgeGraphRAGRetriever</span><span class="p">(</span>
                <span class="n">storage_context</span><span class="o">=</span><span class="n">nebulagraph_storage_context</span><span class="p">,</span>
                <span class="n">service_context</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">service_context</span><span class="p">,</span>
                <span class="n">llm</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
                <span class="n">verbose</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span> <span class="o">=</span> <span class="n">RetrieverQueryEngine</span><span class="o">.</span><span class="n">from_args</span><span class="p">(</span>
                <span class="n">nebulagraph_graph_rag_retriever</span><span class="p">,</span> <span class="n">service_context</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">service_context</span>
            <span class="p">)</span>

        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># KG vector-based entity retrieval</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span> <span class="o">=</span> <span class="n">nebulagraph_index</span><span class="o">.</span><span class="n">as_query_engine</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get modules."""</span>
        <span class="k">return</span> <span class="p">{</span>
            <span class="s2">"llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
            <span class="s2">"service_context"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">service_context</span><span class="p">,</span>
            <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the pipeline."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### get\_modules [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/nebulagraph_query_engine/#llama_index.packs.nebulagraph_query_engine.NebulaGraphQueryEnginePack.get_modules "Permanent link")

```
get_modules() -> Dict[str, Any]
```

Get modules.

Source code in `llama-index-packs/llama-index-packs-nebulagraph-query-engine/llama_index/packs/nebulagraph_query_engine/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_modules</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get modules."""</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s2">"llm"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">llm</span><span class="p">,</span>
        <span class="s2">"service_context"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">service_context</span><span class="p">,</span>
        <span class="s2">"query_engine"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="p">,</span>
    <span class="p">}</span>
</code></pre></div></td></tr></tbody></table>

### run [#](https://docs.llamaindex.ai/en/stable/api_reference/packs/nebulagraph_query_engine/#llama_index.packs.nebulagraph_query_engine.NebulaGraphQueryEnginePack.run "Permanent link")

```
run(*args: Any, **kwargs: Any) -> Any
```

Run the pipeline.

Source code in `llama-index-packs/llama-index-packs-nebulagraph-query-engine/llama_index/packs/nebulagraph_query_engine/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the pipeline."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">query_engine</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Multidoc autoretrieval](https://docs.llamaindex.ai/en/stable/api_reference/packs/multidoc_autoretrieval/)[Next Neo4j query engine](https://docs.llamaindex.ai/en/stable/api_reference/packs/neo4j_query_engine/)
