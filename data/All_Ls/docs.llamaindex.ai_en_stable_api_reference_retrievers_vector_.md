Title: Vector - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/retrievers/vector/

Markdown Content:
Vector - LlamaIndex


VectorIndexRetriever [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/vector/#llama_index.core.retrievers.VectorIndexRetriever "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BaseRetriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/#llama_index.core.base.base_retriever.BaseRetriever "llama_index.core.base.base_retriever.BaseRetriever")`

Vector index retriever.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `index` | `[VectorStoreIndex](https://docs.llamaindex.ai/en/stable/api_reference/indices/vector/#llama_index.core.indices.VectorStoreIndex "llama_index.core.indices.vector_store.base.VectorStoreIndex")` | 
vector store index.



 | _required_ |
| `similarity_top_k` | `int` | 

number of top k results to return.



 | `DEFAULT_SIMILARITY_TOP_K` |
| `vector_store_query_mode` | `str` | 

vector store query mode See reference for VectorStoreQueryMode for full list of supported modes.



 | `DEFAULT` |
| `filters` | `Optional[[MetadataFilters](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.MetadataFilters "llama_index.core.vector_stores.types.MetadataFilters")]` | 

metadata filters, defaults to None



 | `None` |
| `alpha` | `float` | 

weight for sparse/dense retrieval, only used for hybrid query mode.



 | `None` |
| `doc_ids` | `Optional[List[str]]` | 

list of documents to constrain search.



 | `None` |
| `vector_store_kwargs` | `dict` | 

Additional vector store specific kwargs to pass through to the vector store at query time.



 | _required_ |

Source code in `llama-index-core/llama_index/core/indices/vector_store/retrievers/retriever.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 24</span>
<span class="normal"> 25</span>
<span class="normal"> 26</span>
<span class="normal"> 27</span>
<span class="normal"> 28</span>
<span class="normal"> 29</span>
<span class="normal"> 30</span>
<span class="normal"> 31</span>
<span class="normal"> 32</span>
<span class="normal"> 33</span>
<span class="normal"> 34</span>
<span class="normal"> 35</span>
<span class="normal"> 36</span>
<span class="normal"> 37</span>
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
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">VectorIndexRetriever</span><span class="p">(</span><span class="n">BaseRetriever</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Vector index retriever.</span>

<span class="sd">    Args:</span>
<span class="sd">        index (VectorStoreIndex): vector store index.</span>
<span class="sd">        similarity_top_k (int): number of top k results to return.</span>
<span class="sd">        vector_store_query_mode (str): vector store query mode</span>
<span class="sd">            See reference for VectorStoreQueryMode for full list of supported modes.</span>
<span class="sd">        filters (Optional[MetadataFilters]): metadata filters, defaults to None</span>
<span class="sd">        alpha (float): weight for sparse/dense retrieval, only used for</span>
<span class="sd">            hybrid query mode.</span>
<span class="sd">        doc_ids (Optional[List[str]]): list of documents to constrain search.</span>
<span class="sd">        vector_store_kwargs (dict): Additional vector store specific kwargs to pass</span>
<span class="sd">            through to the vector store at query time.</span>

<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">index</span><span class="p">:</span> <span class="n">VectorStoreIndex</span><span class="p">,</span>
        <span class="n">similarity_top_k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_SIMILARITY_TOP_K</span><span class="p">,</span>
        <span class="n">vector_store_query_mode</span><span class="p">:</span> <span class="n">VectorStoreQueryMode</span> <span class="o">=</span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">DEFAULT</span><span class="p">,</span>
        <span class="n">filters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">MetadataFilters</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">alpha</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">node_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">doc_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">sparse_top_k</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">object_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">embed_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseEmbedding</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize params."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index</span> <span class="o">=</span> <span class="n">index</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_vector_store</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">vector_store</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span> <span class="o">=</span> <span class="n">embed_model</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">_embed_model</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">docstore</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_similarity_top_k</span> <span class="o">=</span> <span class="n">similarity_top_k</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_vector_store_query_mode</span> <span class="o">=</span> <span class="n">VectorStoreQueryMode</span><span class="p">(</span><span class="n">vector_store_query_mode</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_alpha</span> <span class="o">=</span> <span class="n">alpha</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_node_ids</span> <span class="o">=</span> <span class="n">node_ids</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_doc_ids</span> <span class="o">=</span> <span class="n">doc_ids</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_filters</span> <span class="o">=</span> <span class="n">filters</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_sparse_top_k</span> <span class="o">=</span> <span class="n">sparse_top_k</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"vector_store_kwargs"</span><span class="p">,</span> <span class="p">{})</span>

        <span class="n">callback_manager</span> <span class="o">=</span> <span class="n">callback_manager</span> <span class="ow">or</span> <span class="n">CallbackManager</span><span class="p">()</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">callback_manager</span><span class="o">=</span><span class="n">callback_manager</span><span class="p">,</span>
            <span class="n">object_map</span><span class="o">=</span><span class="n">object_map</span><span class="p">,</span>
            <span class="n">verbose</span><span class="o">=</span><span class="n">verbose</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">similarity_top_k</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return similarity top k."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_similarity_top_k</span>

    <span class="nd">@similarity_top_k</span><span class="o">.</span><span class="n">setter</span>
    <span class="k">def</span> <span class="nf">similarity_top_k</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">similarity_top_k</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Set similarity top k."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_similarity_top_k</span> <span class="o">=</span> <span class="n">similarity_top_k</span>

    <span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
    <span class="k">def</span> <span class="nf">_retrieve</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vector_store</span><span class="o">.</span><span class="n">is_embedding_query</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">embedding</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">embedding_strs</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
                <span class="n">query_bundle</span><span class="o">.</span><span class="n">embedding</span> <span class="o">=</span> <span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span><span class="o">.</span><span class="n">get_agg_embedding_from_queries</span><span class="p">(</span>
                        <span class="n">query_bundle</span><span class="o">.</span><span class="n">embedding_strs</span>
                    <span class="p">)</span>
                <span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_nodes_with_embeddings</span><span class="p">(</span><span class="n">query_bundle</span><span class="p">)</span>

    <span class="nd">@dispatcher</span><span class="o">.</span><span class="n">span</span>
    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aretrieve</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle</span><span class="p">:</span> <span class="n">QueryBundle</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="n">embedding</span> <span class="o">=</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">embedding</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vector_store</span><span class="o">.</span><span class="n">is_embedding_query</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">query_bundle</span><span class="o">.</span><span class="n">embedding</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">embedding_strs</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
                <span class="n">embed_model</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_embed_model</span>
                <span class="n">embedding</span> <span class="o">=</span> <span class="k">await</span> <span class="n">embed_model</span><span class="o">.</span><span class="n">aget_agg_embedding_from_queries</span><span class="p">(</span>
                    <span class="n">query_bundle</span><span class="o">.</span><span class="n">embedding_strs</span>
                <span class="p">)</span>
        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_aget_nodes_with_embeddings</span><span class="p">(</span>
            <span class="n">QueryBundle</span><span class="p">(</span><span class="n">query_str</span><span class="o">=</span><span class="n">query_bundle</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span> <span class="n">embedding</span><span class="o">=</span><span class="n">embedding</span><span class="p">)</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_build_vector_store_query</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle_with_embeddings</span><span class="p">:</span> <span class="n">QueryBundle</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQuery</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">VectorStoreQuery</span><span class="p">(</span>
            <span class="n">query_embedding</span><span class="o">=</span><span class="n">query_bundle_with_embeddings</span><span class="o">.</span><span class="n">embedding</span><span class="p">,</span>
            <span class="n">similarity_top_k</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_similarity_top_k</span><span class="p">,</span>
            <span class="n">node_ids</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_node_ids</span><span class="p">,</span>
            <span class="n">doc_ids</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_doc_ids</span><span class="p">,</span>
            <span class="n">query_str</span><span class="o">=</span><span class="n">query_bundle_with_embeddings</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
            <span class="n">mode</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_vector_store_query_mode</span><span class="p">,</span>
            <span class="n">alpha</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_alpha</span><span class="p">,</span>
            <span class="n">filters</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_filters</span><span class="p">,</span>
            <span class="n">sparse_top_k</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_sparse_top_k</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_build_node_list_from_query_result</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query_result</span><span class="p">:</span> <span class="n">VectorStoreQueryResult</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="k">if</span> <span class="n">query_result</span><span class="o">.</span><span class="n">nodes</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="c1"># NOTE: vector store does not keep text and returns node indices.</span>
            <span class="c1"># Need to recover all nodes from docstore</span>
            <span class="k">if</span> <span class="n">query_result</span><span class="o">.</span><span class="n">ids</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"Vector store query result should return at "</span>
                    <span class="s2">"least one of nodes or ids."</span>
                <span class="p">)</span>
            <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">index_struct</span><span class="p">,</span> <span class="n">IndexDict</span><span class="p">)</span>
            <span class="n">node_ids</span> <span class="o">=</span> <span class="p">[</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">index_struct</span><span class="o">.</span><span class="n">nodes_dict</span><span class="p">[</span><span class="n">idx</span><span class="p">]</span> <span class="k">for</span> <span class="n">idx</span> <span class="ow">in</span> <span class="n">query_result</span><span class="o">.</span><span class="n">ids</span>
            <span class="p">]</span>
            <span class="n">nodes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span><span class="o">.</span><span class="n">get_nodes</span><span class="p">(</span><span class="n">node_ids</span><span class="p">)</span>
            <span class="n">query_result</span><span class="o">.</span><span class="n">nodes</span> <span class="o">=</span> <span class="n">nodes</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># NOTE: vector store keeps text, returns nodes.</span>
            <span class="c1"># Only need to recover image or index nodes from docstore</span>
            <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">query_result</span><span class="o">.</span><span class="n">nodes</span><span class="p">)):</span>
                <span class="n">source_node</span> <span class="o">=</span> <span class="n">query_result</span><span class="o">.</span><span class="n">nodes</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="o">.</span><span class="n">source_node</span>
                <span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vector_store</span><span class="o">.</span><span class="n">stores_text</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span>
                    <span class="n">source_node</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">source_node</span><span class="o">.</span><span class="n">node_type</span> <span class="o">!=</span> <span class="n">ObjectType</span><span class="o">.</span><span class="n">TEXT</span>
                <span class="p">):</span>
                    <span class="n">node_id</span> <span class="o">=</span> <span class="n">query_result</span><span class="o">.</span><span class="n">nodes</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="o">.</span><span class="n">node_id</span>
                    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span><span class="o">.</span><span class="n">document_exists</span><span class="p">(</span><span class="n">node_id</span><span class="p">):</span>
                        <span class="n">query_result</span><span class="o">.</span><span class="n">nodes</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_docstore</span><span class="o">.</span><span class="n">get_node</span><span class="p">(</span>
                            <span class="n">node_id</span>
                        <span class="p">)</span>  <span class="c1"># type: ignore[index]</span>

        <span class="n">log_vector_store_query_result</span><span class="p">(</span><span class="n">query_result</span><span class="p">)</span>

        <span class="n">node_with_scores</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">ind</span><span class="p">,</span> <span class="n">node</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">query_result</span><span class="o">.</span><span class="n">nodes</span><span class="p">):</span>
            <span class="n">score</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
            <span class="k">if</span> <span class="n">query_result</span><span class="o">.</span><span class="n">similarities</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">score</span> <span class="o">=</span> <span class="n">query_result</span><span class="o">.</span><span class="n">similarities</span><span class="p">[</span><span class="n">ind</span><span class="p">]</span>
            <span class="n">node_with_scores</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">NodeWithScore</span><span class="p">(</span><span class="n">node</span><span class="o">=</span><span class="n">node</span><span class="p">,</span> <span class="n">score</span><span class="o">=</span><span class="n">score</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">node_with_scores</span>

    <span class="k">def</span> <span class="nf">_get_nodes_with_embeddings</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle_with_embeddings</span><span class="p">:</span> <span class="n">QueryBundle</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="n">query</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_vector_store_query</span><span class="p">(</span><span class="n">query_bundle_with_embeddings</span><span class="p">)</span>
        <span class="n">query_result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vector_store</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_kwargs</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_node_list_from_query_result</span><span class="p">(</span><span class="n">query_result</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span> <span class="nf">_aget_nodes_with_embeddings</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query_bundle_with_embeddings</span><span class="p">:</span> <span class="n">QueryBundle</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">NodeWithScore</span><span class="p">]:</span>
        <span class="n">query</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_vector_store_query</span><span class="p">(</span><span class="n">query_bundle_with_embeddings</span><span class="p">)</span>
        <span class="n">query_result</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_vector_store</span><span class="o">.</span><span class="n">aquery</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_kwargs</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_node_list_from_query_result</span><span class="p">(</span><span class="n">query_result</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### similarity\_top\_k `property` `writable` [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/vector/#llama_index.core.retrievers.VectorIndexRetriever.similarity_top_k "Permanent link")

```
similarity_top_k: int
```

Return similarity top k.

VectorIndexAutoRetriever [#](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/vector/#llama_index.core.retrievers.VectorIndexAutoRetriever "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `BaseAutoRetriever`

Vector store auto retriever.

A retriever for vector store index that uses an LLM to automatically set vector store query parameters.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `index` | `[VectorStoreIndex](https://docs.llamaindex.ai/en/stable/api_reference/indices/vector/#llama_index.core.indices.VectorStoreIndex "llama_index.core.indices.vector_store.base.VectorStoreIndex")` | 
vector store index



 | _required_ |
| `vector_store_info` | `[VectorStoreInfo](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreInfo "llama_index.core.vector_stores.types.VectorStoreInfo")` | 

additional information about vector store content and supported metadata filters. The natural language description is used by an LLM to automatically set vector store query parameters.



 | _required_ |
| `prompt_template_str` | `Optional[str]` | 

custom prompt template string for LLM. Uses default template string if None.



 | `None` |
| `service_context` | `Optional[ServiceContext]` | 

service context containing reference to an LLM. Uses service context from index be default if None.



 | `None` |
| `similarity_top_k` | `int` | 

number of top k results to return.



 | `DEFAULT_SIMILARITY_TOP_K` |
| `empty_query_top_k` | `Optional[int]` | 

number of top k results to return if the inferred query string is blank (uses metadata filters only). Can be set to None, which would use the similarity\_top\_k instead. By default, set to 10.



 | `10` |
| `max_top_k` | `int` | 

the maximum top\_k allowed. The top\_k set by LLM or similarity\_top\_k will be clamped to this value.



 | `10` |
| `vector_store_query_mode` | `str` | 

vector store query mode See reference for VectorStoreQueryMode for full list of supported modes.



 | `DEFAULT` |
| `default_empty_query_vector` | `Optional[List[float]]` | 

default empty query vector. Defaults to None. If not None, then this vector will be used as the query vector if the query is empty.



 | `None` |
| `callback_manager` | `Optional[[CallbackManager](https://docs.llamaindex.ai/en/stable/api_reference/callbacks/#llama_index.core.callbacks.base.CallbackManager "llama_index.core.callbacks.base.CallbackManager")]` | 

callback manager



 | `None` |
| `verbose` | `bool` | 

verbose mode



 | `False` |

Source code in `llama-index-core/llama_index/core/indices/vector_store/retrievers/auto_retriever/auto_retriever.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 42</span>
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
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
<span class="normal">225</span>
<span class="normal">226</span>
<span class="normal">227</span>
<span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span>
<span class="normal">231</span>
<span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span>
<span class="normal">236</span>
<span class="normal">237</span>
<span class="normal">238</span>
<span class="normal">239</span>
<span class="normal">240</span>
<span class="normal">241</span>
<span class="normal">242</span>
<span class="normal">243</span>
<span class="normal">244</span>
<span class="normal">245</span>
<span class="normal">246</span>
<span class="normal">247</span>
<span class="normal">248</span>
<span class="normal">249</span>
<span class="normal">250</span>
<span class="normal">251</span>
<span class="normal">252</span>
<span class="normal">253</span>
<span class="normal">254</span>
<span class="normal">255</span>
<span class="normal">256</span>
<span class="normal">257</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">VectorIndexAutoRetriever</span><span class="p">(</span><span class="n">BaseAutoRetriever</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Vector store auto retriever.</span>

<span class="sd">    A retriever for vector store index that uses an LLM to automatically set</span>
<span class="sd">    vector store query parameters.</span>

<span class="sd">    Args:</span>
<span class="sd">        index (VectorStoreIndex): vector store index</span>
<span class="sd">        vector_store_info (VectorStoreInfo): additional information about</span>
<span class="sd">            vector store content and supported metadata filters. The natural language</span>
<span class="sd">            description is used by an LLM to automatically set vector store query</span>
<span class="sd">            parameters.</span>
<span class="sd">        prompt_template_str: custom prompt template string for LLM.</span>
<span class="sd">            Uses default template string if None.</span>
<span class="sd">        service_context: service context containing reference to an LLM.</span>
<span class="sd">            Uses service context from index be default if None.</span>
<span class="sd">        similarity_top_k (int): number of top k results to return.</span>
<span class="sd">        empty_query_top_k (Optional[int]): number of top k results to return</span>
<span class="sd">            if the inferred query string is blank (uses metadata filters only).</span>
<span class="sd">            Can be set to None, which would use the similarity_top_k instead.</span>
<span class="sd">            By default, set to 10.</span>
<span class="sd">        max_top_k (int):</span>
<span class="sd">            the maximum top_k allowed. The top_k set by LLM or similarity_top_k will</span>
<span class="sd">            be clamped to this value.</span>
<span class="sd">        vector_store_query_mode (str): vector store query mode</span>
<span class="sd">            See reference for VectorStoreQueryMode for full list of supported modes.</span>
<span class="sd">        default_empty_query_vector (Optional[List[float]]): default empty query vector.</span>
<span class="sd">            Defaults to None. If not None, then this vector will be used as the query</span>
<span class="sd">            vector if the query is empty.</span>
<span class="sd">        callback_manager (Optional[CallbackManager]): callback manager</span>
<span class="sd">        verbose (bool): verbose mode</span>
<span class="sd">    """</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">index</span><span class="p">:</span> <span class="n">VectorStoreIndex</span><span class="p">,</span>
        <span class="n">vector_store_info</span><span class="p">:</span> <span class="n">VectorStoreInfo</span><span class="p">,</span>
        <span class="n">llm</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">LLM</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">prompt_template_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">max_top_k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">similarity_top_k</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_SIMILARITY_TOP_K</span><span class="p">,</span>
        <span class="n">empty_query_top_k</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span>
        <span class="n">vector_store_query_mode</span><span class="p">:</span> <span class="n">VectorStoreQueryMode</span> <span class="o">=</span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">DEFAULT</span><span class="p">,</span>
        <span class="n">default_empty_query_vector</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">callback_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CallbackManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">extra_filters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">MetadataFilters</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">object_map</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">objects</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">IndexNode</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="c1"># deprecated</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index</span> <span class="o">=</span> <span class="n">index</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_vector_store_info</span> <span class="o">=</span> <span class="n">vector_store_info</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_default_empty_query_vector</span> <span class="o">=</span> <span class="n">default_empty_query_vector</span>

        <span class="n">service_context</span> <span class="o">=</span> <span class="n">service_context</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="o">.</span><span class="n">service_context</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_llm</span> <span class="o">=</span> <span class="n">llm</span> <span class="ow">or</span> <span class="n">llm_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
        <span class="n">callback_manager</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">callback_manager</span>
            <span class="ow">or</span> <span class="n">callback_manager_from_settings_or_context</span><span class="p">(</span><span class="n">Settings</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
        <span class="p">)</span>

        <span class="c1"># prompt</span>
        <span class="n">prompt_template_str</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">prompt_template_str</span> <span class="ow">or</span> <span class="n">DEFAULT_VECTOR_STORE_QUERY_PROMPT_TMPL</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_output_parser</span> <span class="o">=</span> <span class="n">VectorStoreQueryOutputParser</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_prompt</span> <span class="o">=</span> <span class="n">PromptTemplate</span><span class="p">(</span><span class="n">template</span><span class="o">=</span><span class="n">prompt_template_str</span><span class="p">)</span>

        <span class="c1"># additional config</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_max_top_k</span> <span class="o">=</span> <span class="n">max_top_k</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_similarity_top_k</span> <span class="o">=</span> <span class="n">similarity_top_k</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_empty_query_top_k</span> <span class="o">=</span> <span class="n">empty_query_top_k</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_vector_store_query_mode</span> <span class="o">=</span> <span class="n">vector_store_query_mode</span>
        <span class="c1"># if extra_filters is OR condition, we don't support that yet</span>
        <span class="k">if</span> <span class="n">extra_filters</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">extra_filters</span><span class="o">.</span><span class="n">condition</span> <span class="o"></span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">filters</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">filters</span> <span class="o">=</span> <span class="n">MetadataFilters</span><span class="p">(</span>
                <span class="n">filters</span><span class="o">=</span><span class="p">[</span><span class="o">*</span><span class="n">spec</span><span class="o">.</span><span class="n">filters</span><span class="p">,</span> <span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">_extra_filters</span><span class="o">.</span><span class="n">filters</span><span class="p">]</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="p">(</span>
            <span class="n">VectorIndexRetriever</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_index</span><span class="p">,</span>
                <span class="n">filters</span><span class="o">=</span><span class="n">filters</span><span class="p">,</span>
                <span class="n">similarity_top_k</span><span class="o">=</span><span class="n">similarity_top_k</span><span class="p">,</span>
                <span class="n">vector_store_query_mode</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_vector_store_query_mode</span><span class="p">,</span>
                <span class="n">object_map</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">object_map</span><span class="p">,</span>
                <span class="n">verbose</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_verbose</span><span class="p">,</span>
                <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">_kwargs</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">new_query_bundle</span><span class="p">,</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Tree](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/tree/)[Next Videodb](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/videodb/)
