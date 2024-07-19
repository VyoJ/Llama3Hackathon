Title: Firestore - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/firestore/

Markdown Content:
Firestore - LlamaIndex


FirestoreVectorStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/firestore/#llama_index.vector_stores.firestore.FirestoreVectorStore "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")`

Firestore Vector Store.

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-firestore/llama_index/vector_stores/firestore/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 87</span>
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
<span class="normal">251</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">FirestoreVectorStore</span><span class="p">(</span><span class="n">BasePydanticVectorStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Firestore Vector Store."""</span>

    <span class="n">stores_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">flat_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="n">collection_name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">batch_size</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="n">DEFAULT_BATCH_SIZE</span>
    <span class="n">embedding_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"embedding"</span>
    <span class="n">text_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"text"</span>
    <span class="n">metadata_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"metadata"</span>
    <span class="n">distance_strategy</span><span class="p">:</span> <span class="n">DistanceMeasure</span> <span class="o">=</span> <span class="n">DistanceMeasure</span><span class="o">.</span><span class="n">COSINE</span>

    <span class="n">_client</span><span class="p">:</span> <span class="n">Client</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">client</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Client</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize params."""</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="nb">object</span><span class="o">.</span><span class="fm">__setattr__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="s2">"_client"</span><span class="p">,</span> <span class="n">client_with_user_agent</span><span class="p">(</span><span class="n">client</span><span class="p">))</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"FirestoreVectorStore"</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span>

    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Add nodes to vector store."""</span>
        <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">entries</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">node_id</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">node_id</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="n">node_to_metadata_dict</span><span class="p">(</span>
                <span class="n">node</span><span class="p">,</span>
                <span class="n">remove_text</span><span class="o">=</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">stores_text</span><span class="p">,</span>
                <span class="n">flat_metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">flat_metadata</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">entry</span> <span class="o">=</span> <span class="p">{</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">embedding_key</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">get_embedding</span><span class="p">(),</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">metadata_key</span><span class="p">:</span> <span class="n">metadata</span><span class="p">,</span>
            <span class="p">}</span>
            <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node_id</span><span class="p">)</span>
            <span class="n">entries</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">entry</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_upsert_batch</span><span class="p">(</span><span class="n">entries</span><span class="p">,</span> <span class="n">ids</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">ids</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete nodes using with ref_doc_id."""</span>
        <span class="n">docs</span> <span class="o">=</span> <span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">collection</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">collection_name</span><span class="p">)</span>
            <span class="o">.</span><span class="n">where</span><span class="p">(</span><span class="s2">"metadata.ref_doc_id"</span><span class="p">,</span> <span class="s2">""</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">)</span>
        <span class="o">.</span><span class="n">stream</span><span class="p">()</span>
    <span class="p">)</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">_delete_batch</span><span class="p">([</span><span class="n">doc</span><span class="o">.</span><span class="n">id</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">docs</span><span class="p">])</span>
</code></pre></div></td></tr></tbody></table>

### query [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/firestore/#llama_index.vector_stores.firestore.FirestoreVectorStore.query "Permanent link")

```
query(query: [VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery"), **kwargs: Any) -> [VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")
```

Query vector store.

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-firestore/llama_index/vector_stores/firestore/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">152</span>
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
<span class="normal">196</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Query vector store."""</span>
    <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Query embedding is required."</span><span class="p">)</span>

    <span class="n">filters</span> <span class="o">=</span> <span class="n">_to_firestore_filter</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">)</span> <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span> <span class="k">else</span> <span class="kc">None</span>

    <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_similarity_search</span><span class="p">(</span>
        <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">,</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span> <span class="n">filters</span><span class="o">=</span><span class="n">filters</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
    <span class="p">)</span>

    <span class="n">top_k_ids</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">top_k_nodes</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">top_k_similarities</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="n">LOGGER</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Found </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">results</span><span class="p">)</span><span class="si">}</span><span class="s2"> results."</span><span class="p">)</span>

    <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">results</span><span class="p">:</span>
        <span class="c1"># Convert the Firestore document to dict</span>
        <span class="n">result_dict</span> <span class="o">=</span> <span class="n">result</span><span class="o">.</span><span class="n">to_dict</span><span class="p">()</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="n">metadata</span> <span class="o">=</span> <span class="n">result_dict</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata_key</span><span class="p">)</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="n">fir_vec</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Vector</span><span class="p">]</span> <span class="o">=</span> <span class="n">result_dict</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">embedding_key</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">fir_vec</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Embedding is missing in Firestore document."</span><span class="p">,</span> <span class="n">result</span><span class="o">.</span><span class="n">id</span>
            <span class="p">)</span>
        <span class="n">embedding</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">fir_vec</span><span class="o">.</span><span class="n">to_map_value</span><span class="p">()[</span><span class="s2">"value"</span><span class="p">])</span>

        <span class="c1"># Convert metadata to node, and add text if available</span>
        <span class="n">node</span> <span class="o">=</span> <span class="n">metadata_dict_to_node</span><span class="p">(</span><span class="n">metadata</span><span class="p">,</span> <span class="n">text</span><span class="o">=</span><span class="n">result_dict</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_key</span><span class="p">))</span>

        <span class="c1"># Keep track of the top k ids and nodes</span>
        <span class="n">top_k_ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
        <span class="n">top_k_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
        <span class="n">top_k_similarities</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
            <span class="n">similarity</span><span class="p">(</span>
                <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">,</span>
                <span class="n">embedding</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_distance_to_similarity_mode</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">distance_strategy</span><span class="p">),</span>
            <span class="p">)</span>
        <span class="p">)</span>

    <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span>
        <span class="n">nodes</span><span class="o">=</span><span class="n">top_k_nodes</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">top_k_ids</span><span class="p">,</span> <span class="n">similarities</span><span class="o">=</span><span class="n">top_k_similarities</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Faiss](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/faiss/)[Next Google](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/google/)
