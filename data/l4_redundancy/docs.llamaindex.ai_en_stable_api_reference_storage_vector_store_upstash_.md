Title: Upstash - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/upstash/

Markdown Content:
Upstash - LlamaIndex


UpstashVectorStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/upstash/#llama_index.vector_stores.upstash.UpstashVectorStore "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")`

Upstash Vector Store.

**Examples:**

`pip install llama-index-vector-stores-upstash`

```
from llama_index.vector_stores.upstash import UpstashVectorStore

# Create Upstash vector store
upstash_vector_store = UpstashVectorStore(
    url="your_upstash_vector_url",
    token="your_upstash_vector_token",
)
```

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-upstash/llama_index/vector_stores/upstash/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 91</span>
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
<span class="normal">220</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">UpstashVectorStore</span><span class="p">(</span><span class="n">BasePydanticVectorStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Upstash Vector Store.</span>

<span class="sd">    Examples:</span>
<span class="sd">        `pip install llama-index-vector-stores-upstash`</span>

<span class="sd">        ```python</span>
<span class="sd">        from llama_index.vector_stores.upstash import UpstashVectorStore</span>

<span class="sd">        # Create Upstash vector store</span>
<span class="sd">        upstash_vector_store = UpstashVectorStore(</span>
<span class="sd">            url="your_upstash_vector_url",</span>
<span class="sd">            token="your_upstash_vector_token",</span>
<span class="sd">        )</span>
<span class="sd">        ```</span>
<span class="sd">    """</span>

    <span class="n">stores_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">flat_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>

    <span class="n">namespace</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span>

    <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">_index</span><span class="p">:</span> <span class="n">Index</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"UpstashVectorStore"</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return the Upstash client."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">token</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_BATCH_SIZE</span><span class="p">,</span>
        <span class="c1"># Upstash uses ("") as the default namespace, if not provided</span>
        <span class="n">namespace</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Create a UpstashVectorStore. The index can be created using the Upstash console.</span>

<span class="sd">        Args:</span>
<span class="sd">            url (String): URL of the Upstash Vector instance, found in the Upstash console.</span>
<span class="sd">            token (String): Token for the Upstash Vector Index, found in the Upstash console.</span>
<span class="sd">            batch_size (Optional[int]): Batch size for adding nodes to the vector store.</span>

<span class="sd">        Raises:</span>
<span class="sd">            ImportError: If the upstash-vector python package is not installed.</span>
<span class="sd">        """</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span> <span class="n">namespace</span><span class="o">=</span><span class="n">namespace</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index</span> <span class="o">=</span> <span class="n">Index</span><span class="p">(</span><span class="n">url</span><span class="o">=</span><span class="n">url</span><span class="p">,</span> <span class="n">token</span><span class="o">=</span><span class="n">token</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Add nodes to the vector store.</span>

<span class="sd">        Args:</span>
<span class="sd">            nodes: List of nodes to add to the vector store.</span>
<span class="sd">            add_kwargs: Additional arguments to pass to the add method.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List of ids of the added nodes.</span>
<span class="sd">        """</span>
        <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">vectors</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node_batch</span> <span class="ow">in</span> <span class="n">iter_batch</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">batch_size</span><span class="p">):</span>
            <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">node_batch</span><span class="p">:</span>
                <span class="n">metadata_dict</span> <span class="o">=</span> <span class="n">node_to_metadata_dict</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
                <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span>
                <span class="n">vectors</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">,</span> <span class="n">node</span><span class="o">.</span><span class="n">embedding</span><span class="p">,</span> <span class="n">metadata_dict</span><span class="p">))</span>

            <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">upsert</span><span class="p">(</span><span class="n">vectors</span><span class="o">=</span><span class="n">vectors</span><span class="p">,</span> <span class="n">namespace</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">namespace</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">ids</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Delete node from the vector store.</span>

<span class="sd">        Args:</span>
<span class="sd">            ref_doc_id: Reference doc id of the node to delete.</span>
<span class="sd">            delete_kwargs: Additional arguments to pass to the delete method.</span>
<span class="sd">        """</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span>
            <span class="s2">"Delete is not currently supported, but will be in the future."</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Query the vector store.</span>

<span class="sd">        Args:</span>
<span class="sd">            query: Query to run against the vector store.</span>
<span class="sd">            kwargs: Additional arguments to pass to the query method.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Query result.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="o">!=</span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">DEFAULT</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Query mode </span><span class="si">{</span><span class="n">query</span><span class="o">.</span><span class="n">mode</span><span class="si">}</span><span class="s2"> not supported"</span><span class="p">)</span>

        <span class="c1"># if query.filters:</span>
        <span class="c1">#     raise ValueError("Metadata filtering not supported")</span>

        <span class="n">res</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">query</span><span class="p">(</span>
            <span class="n">vector</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">,</span>
            <span class="n">top_k</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
            <span class="n">include_vectors</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">include_metadata</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="nb">filter</span><span class="o">=</span><span class="n">_to_upstash_filters</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">),</span>
            <span class="n">namespace</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">namespace</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">top_k_nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">top_k_ids</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">top_k_scores</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">vector</span> <span class="ow">in</span> <span class="n">res</span><span class="p">:</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">metadata_dict_to_node</span><span class="p">(</span><span class="n">vector</span><span class="o">.</span><span class="n">metadata</span><span class="p">)</span>
            <span class="n">node</span><span class="o">.</span><span class="n">embedding</span> <span class="o">=</span> <span class="n">vector</span><span class="o">.</span><span class="n">vector</span>
            <span class="n">top_k_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
            <span class="n">top_k_ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">vector</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
            <span class="n">top_k_scores</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">vector</span><span class="o">.</span><span class="n">score</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span>
            <span class="n">nodes</span><span class="o">=</span><span class="n">top_k_nodes</span><span class="p">,</span> <span class="n">similarities</span><span class="o">=</span><span class="n">top_k_scores</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">top_k_ids</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### client `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/upstash/#llama_index.vector_stores.upstash.UpstashVectorStore.client "Permanent link")

```
client: Any
```

Return the Upstash client.

### add [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/upstash/#llama_index.vector_stores.upstash.UpstashVectorStore.add "Permanent link")

```
add(nodes: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], **add_kwargs: Any) -> List[str]
```

Add nodes to the vector store.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `nodes` | `List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]` | 
List of nodes to add to the vector store.



 | _required_ |
| `add_kwargs` | `Any` | 

Additional arguments to pass to the add method.



 | `{}` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[str]` | 
List of ids of the added nodes.



 |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-upstash/llama_index/vector_stores/upstash/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">147</span>
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
<span class="normal">168</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Add nodes to the vector store.</span>

<span class="sd">    Args:</span>
<span class="sd">        nodes: List of nodes to add to the vector store.</span>
<span class="sd">        add_kwargs: Additional arguments to pass to the add method.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List of ids of the added nodes.</span>
<span class="sd">    """</span>
    <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">vectors</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">node_batch</span> <span class="ow">in</span> <span class="n">iter_batch</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">batch_size</span><span class="p">):</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">node_batch</span><span class="p">:</span>
            <span class="n">metadata_dict</span> <span class="o">=</span> <span class="n">node_to_metadata_dict</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
            <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span>
            <span class="n">vectors</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">,</span> <span class="n">node</span><span class="o">.</span><span class="n">embedding</span><span class="p">,</span> <span class="n">metadata_dict</span><span class="p">))</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">upsert</span><span class="p">(</span><span class="n">vectors</span><span class="o">=</span><span class="n">vectors</span><span class="p">,</span> <span class="n">namespace</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">namespace</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">ids</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/upstash/#llama_index.vector_stores.upstash.UpstashVectorStore.delete "Permanent link")

```
delete(ref_doc_id: str, **delete_kwargs: Any) -> None
```

Delete node from the vector store.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `ref_doc_id` | `str` | 
Reference doc id of the node to delete.



 | _required_ |
| `delete_kwargs` | `Any` | 

Additional arguments to pass to the delete method.



 | `{}` |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-upstash/llama_index/vector_stores/upstash/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Delete node from the vector store.</span>

<span class="sd">    Args:</span>
<span class="sd">        ref_doc_id: Reference doc id of the node to delete.</span>
<span class="sd">        delete_kwargs: Additional arguments to pass to the delete method.</span>
<span class="sd">    """</span>
    <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span>
        <span class="s2">"Delete is not currently supported, but will be in the future."</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### query [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/upstash/#llama_index.vector_stores.upstash.UpstashVectorStore.query "Permanent link")

```
query(query: [VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery"), **kwargs: Any) -> [VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")
```

Query the vector store.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `[VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery")` | 
Query to run against the vector store.



 | _required_ |
| `kwargs` | `Any` | 

Additional arguments to pass to the query method.



 | `{}` |

**Returns:**

| Type | Description |
| --- | --- |
| `[VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")` | 
Query result.



 |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-upstash/llama_index/vector_stores/upstash/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">182</span>
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
<span class="normal">220</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Query the vector store.</span>

<span class="sd">    Args:</span>
<span class="sd">        query: Query to run against the vector store.</span>
<span class="sd">        kwargs: Additional arguments to pass to the query method.</span>

<span class="sd">    Returns:</span>
<span class="sd">        Query result.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="o">!=</span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">DEFAULT</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Query mode </span><span class="si">{</span><span class="n">query</span><span class="o">.</span><span class="n">mode</span><span class="si">}</span><span class="s2"> not supported"</span><span class="p">)</span>

    <span class="c1"># if query.filters:</span>
    <span class="c1">#     raise ValueError("Metadata filtering not supported")</span>

    <span class="n">res</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">query</span><span class="p">(</span>
        <span class="n">vector</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">,</span>
        <span class="n">top_k</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
        <span class="n">include_vectors</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">include_metadata</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="nb">filter</span><span class="o">=</span><span class="n">_to_upstash_filters</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">),</span>
        <span class="n">namespace</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">namespace</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="n">top_k_nodes</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">top_k_ids</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">top_k_scores</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">vector</span> <span class="ow">in</span> <span class="n">res</span><span class="p">:</span>
        <span class="n">node</span> <span class="o">=</span> <span class="n">metadata_dict_to_node</span><span class="p">(</span><span class="n">vector</span><span class="o">.</span><span class="n">metadata</span><span class="p">)</span>
        <span class="n">node</span><span class="o">.</span><span class="n">embedding</span> <span class="o">=</span> <span class="n">vector</span><span class="o">.</span><span class="n">vector</span>
        <span class="n">top_k_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
        <span class="n">top_k_ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">vector</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
        <span class="n">top_k_scores</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">vector</span><span class="o">.</span><span class="n">score</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span>
        <span class="n">nodes</span><span class="o">=</span><span class="n">top_k_nodes</span><span class="p">,</span> <span class="n">similarities</span><span class="o">=</span><span class="n">top_k_scores</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">top_k_ids</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Typesense](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/typesense/)[Next Vearch](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/vearch/)
