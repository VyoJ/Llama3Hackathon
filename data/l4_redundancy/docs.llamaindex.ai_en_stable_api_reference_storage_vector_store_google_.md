Title: Google - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/google/

Markdown Content:
Google - LlamaIndex


GoogleVectorStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/google/#llama_index.vector_stores.google.GoogleVectorStore "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")`

Google GenerativeAI Vector Store.

Currently, it computes the embedding vectors on the server side.

**Examples:**

google\_vector\_store = GoogleVectorStore.from\_corpus( corpus\_id="my-corpus-id", include\_metadata=True, metadata\_keys=\['file\_name', 'creation\_date'\] ) index = VectorStoreIndex.from\_vector\_store( vector\_store=google\_vector\_store )

**Attributes:**

| Name | Type | Description |
| --- | --- | --- |
| `[corpus_id](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/google/#llama_index.vector_stores.google.GoogleVectorStore.corpus_id "llama_index.vector_stores.google.GoogleVectorStore.corpus_id")` | `str` | 
The corpus ID that this vector store instance will read and write to.



 |
| `include_metadata` | `bool` | 

Indicates whether to include custom metadata in the query results. Defaults to False.



 |
| `metadata_keys` | `Optional[List[str]]` | 

Specifies which metadata keys to include in the query results if include\_metadata is set to True. If None, all metadata keys are included. Defaults to None.



 |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-google/llama_index/vector_stores/google/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 95</span>
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
<span class="normal">257</span>
<span class="normal">258</span>
<span class="normal">259</span>
<span class="normal">260</span>
<span class="normal">261</span>
<span class="normal">262</span>
<span class="normal">263</span>
<span class="normal">264</span>
<span class="normal">265</span>
<span class="normal">266</span>
<span class="normal">267</span>
<span class="normal">268</span>
<span class="normal">269</span>
<span class="normal">270</span>
<span class="normal">271</span>
<span class="normal">272</span>
<span class="normal">273</span>
<span class="normal">274</span>
<span class="normal">275</span>
<span class="normal">276</span>
<span class="normal">277</span>
<span class="normal">278</span>
<span class="normal">279</span>
<span class="normal">280</span>
<span class="normal">281</span>
<span class="normal">282</span>
<span class="normal">283</span>
<span class="normal">284</span>
<span class="normal">285</span>
<span class="normal">286</span>
<span class="normal">287</span>
<span class="normal">288</span>
<span class="normal">289</span>
<span class="normal">290</span>
<span class="normal">291</span>
<span class="normal">292</span>
<span class="normal">293</span>
<span class="normal">294</span>
<span class="normal">295</span>
<span class="normal">296</span>
<span class="normal">297</span>
<span class="normal">298</span>
<span class="normal">299</span>
<span class="normal">300</span>
<span class="normal">301</span>
<span class="normal">302</span>
<span class="normal">303</span>
<span class="normal">304</span>
<span class="normal">305</span>
<span class="normal">306</span>
<span class="normal">307</span>
<span class="normal">308</span>
<span class="normal">309</span>
<span class="normal">310</span>
<span class="normal">311</span>
<span class="normal">312</span>
<span class="normal">313</span>
<span class="normal">314</span>
<span class="normal">315</span>
<span class="normal">316</span>
<span class="normal">317</span>
<span class="normal">318</span>
<span class="normal">319</span>
<span class="normal">320</span>
<span class="normal">321</span>
<span class="normal">322</span>
<span class="normal">323</span>
<span class="normal">324</span>
<span class="normal">325</span>
<span class="normal">326</span>
<span class="normal">327</span>
<span class="normal">328</span>
<span class="normal">329</span>
<span class="normal">330</span>
<span class="normal">331</span>
<span class="normal">332</span>
<span class="normal">333</span>
<span class="normal">334</span>
<span class="normal">335</span>
<span class="normal">336</span>
<span class="normal">337</span>
<span class="normal">338</span>
<span class="normal">339</span>
<span class="normal">340</span>
<span class="normal">341</span>
<span class="normal">342</span>
<span class="normal">343</span>
<span class="normal">344</span>
<span class="normal">345</span>
<span class="normal">346</span>
<span class="normal">347</span>
<span class="normal">348</span>
<span class="normal">349</span>
<span class="normal">350</span>
<span class="normal">351</span>
<span class="normal">352</span>
<span class="normal">353</span>
<span class="normal">354</span>
<span class="normal">355</span>
<span class="normal">356</span>
<span class="normal">357</span>
<span class="normal">358</span>
<span class="normal">359</span>
<span class="normal">360</span>
<span class="normal">361</span>
<span class="normal">362</span>
<span class="normal">363</span>
<span class="normal">364</span>
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
<span class="normal">394</span>
<span class="normal">395</span>
<span class="normal">396</span>
<span class="normal">397</span>
<span class="normal">398</span>
<span class="normal">399</span>
<span class="normal">400</span>
<span class="normal">401</span>
<span class="normal">402</span>
<span class="normal">403</span>
<span class="normal">404</span>
<span class="normal">405</span>
<span class="normal">406</span>
<span class="normal">407</span>
<span class="normal">408</span>
<span class="normal">409</span>
<span class="normal">410</span>
<span class="normal">411</span>
<span class="normal">412</span>
<span class="normal">413</span>
<span class="normal">414</span>
<span class="normal">415</span>
<span class="normal">416</span>
<span class="normal">417</span>
<span class="normal">418</span>
<span class="normal">419</span>
<span class="normal">420</span>
<span class="normal">421</span>
<span class="normal">422</span>
<span class="normal">423</span>
<span class="normal">424</span>
<span class="normal">425</span>
<span class="normal">426</span>
<span class="normal">427</span>
<span class="normal">428</span>
<span class="normal">429</span>
<span class="normal">430</span>
<span class="normal">431</span>
<span class="normal">432</span>
<span class="normal">433</span>
<span class="normal">434</span>
<span class="normal">435</span>
<span class="normal">436</span>
<span class="normal">437</span>
<span class="normal">438</span>
<span class="normal">439</span>
<span class="normal">440</span>
<span class="normal">441</span>
<span class="normal">442</span>
<span class="normal">443</span>
<span class="normal">444</span>
<span class="normal">445</span>
<span class="normal">446</span>
<span class="normal">447</span>
<span class="normal">448</span>
<span class="normal">449</span>
<span class="normal">450</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">GoogleVectorStore</span><span class="p">(</span><span class="n">BasePydanticVectorStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Google GenerativeAI Vector Store.</span>

<span class="sd">    Currently, it computes the embedding vectors on the server side.</span>

<span class="sd">    Examples:</span>
<span class="sd">        google_vector_store = GoogleVectorStore.from_corpus(</span>
<span class="sd">            corpus_id="my-corpus-id",</span>
<span class="sd">            include_metadata=True,</span>
<span class="sd">            metadata_keys=['file_name', 'creation_date']</span>
<span class="sd">        )</span>
<span class="sd">        index = VectorStoreIndex.from_vector_store(</span>
<span class="sd">            vector_store=google_vector_store</span>
<span class="sd">        )</span>

<span class="sd">    Attributes:</span>
<span class="sd">        corpus_id: The corpus ID that this vector store instance will read and</span>
<span class="sd">            write to.</span>
<span class="sd">        include_metadata (bool): Indicates whether to include custom metadata in the query</span>
<span class="sd">            results. Defaults to False.</span>
<span class="sd">        metadata_keys (Optional[List[str]]): Specifies which metadata keys to include in the</span>
<span class="sd">            query results if include_metadata is set to True. If None, all metadata keys</span>
<span class="sd">            are included. Defaults to None.</span>
<span class="sd">    """</span>

    <span class="c1"># Semantic Retriever stores the document node's text as string and embeds</span>
    <span class="c1"># the vectors on the server automatically.</span>
    <span class="n">stores_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">is_embedding_query</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>

    <span class="c1"># This is not the Google's corpus name but an ID generated in the LlamaIndex</span>
    <span class="c1"># world.</span>
    <span class="n">corpus_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">frozen</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="w">    </span><span class="sd">"""Corpus ID that this instance of the vector store is using."""</span>

    <span class="c1"># Configuration options for handling metadata in query results</span>
    <span class="n">include_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="n">metadata_keys</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span>

    <span class="n">_client</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">client</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">):</span>
<span class="w">        </span><span class="sd">"""Raw constructor.</span>

<span class="sd">        Use the class method `from_corpus` or `create_corpus` instead.</span>

<span class="sd">        Args:</span>
<span class="sd">            client: The low-level retriever class from google.ai.generativelanguage.</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">google.ai.generativelanguage</span> <span class="k">as</span> <span class="nn">genai</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">_import_err_msg</span><span class="p">)</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">client</span><span class="p">,</span> <span class="n">genai</span><span class="o">.</span><span class="n">RetrieverServiceClient</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">client</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_corpus</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">corpus_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">include_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">metadata_keys</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"GoogleVectorStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create an instance that points to an existing corpus.</span>

<span class="sd">        Args:</span>
<span class="sd">            corpus_id (str): ID of an existing corpus on Google's server.</span>
<span class="sd">            include_metadata (bool, optional): Specifies whether to include custom metadata in the</span>
<span class="sd">                query results. Defaults to False, meaning metadata will not be included.</span>
<span class="sd">            metadata_keys (Optional[List[str]], optional): Specifies which metadata keys to include</span>
<span class="sd">                in the query results if include_metadata is set to True. If None, all metadata keys</span>
<span class="sd">                are included. Defaults to None.</span>

<span class="sd">        Returns:</span>
<span class="sd">            An instance of the vector store that points to the specified corpus.</span>

<span class="sd">        Raises:</span>
<span class="sd">            NoSuchCorpusException if no such corpus is found.</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">llama_index.vector_stores.google.genai_extension</span> <span class="k">as</span> <span class="nn">genaix</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">_import_err_msg</span><span class="p">)</span>

        <span class="n">_logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="se">\n\n</span><span class="s2">GoogleVectorStore.from_corpus(corpus_id=</span><span class="si">{</span><span class="n">corpus_id</span><span class="si">}</span><span class="s2">)"</span><span class="p">)</span>
        <span class="n">client</span> <span class="o">=</span> <span class="n">genaix</span><span class="o">.</span><span class="n">build_semantic_retriever</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">genaix</span><span class="o">.</span><span class="n">get_corpus</span><span class="p">(</span><span class="n">corpus_id</span><span class="o">=</span><span class="n">corpus_id</span><span class="p">,</span> <span class="n">client</span><span class="o">=</span><span class="n">client</span><span class="p">)</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">NoSuchCorpusException</span><span class="p">(</span><span class="n">corpus_id</span><span class="o">=</span><span class="n">corpus_id</span><span class="p">)</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">corpus_id</span><span class="o">=</span><span class="n">corpus_id</span><span class="p">,</span>
            <span class="n">client</span><span class="o">=</span><span class="n">client</span><span class="p">,</span>
            <span class="n">include_metadata</span><span class="o">=</span><span class="n">include_metadata</span><span class="p">,</span>
            <span class="n">metadata_keys</span><span class="o">=</span><span class="n">metadata_keys</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">create_corpus</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">corpus_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">display_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"GoogleVectorStore"</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create an instance that points to a newly created corpus.</span>

<span class="sd">        Examples:</span>
<span class="sd">            store = GoogleVectorStore.create_corpus()</span>
<span class="sd">            print(f"Created corpus with ID: {store.corpus_id})</span>

<span class="sd">            store = GoogleVectorStore.create_corpus(</span>
<span class="sd">                display_name="My first corpus"</span>
<span class="sd">            )</span>

<span class="sd">            store = GoogleVectorStore.create_corpus(</span>
<span class="sd">                corpus_id="my-corpus-1",</span>
<span class="sd">                display_name="My first corpus"</span>
<span class="sd">            )</span>

<span class="sd">        Args:</span>
<span class="sd">            corpus_id: ID of the new corpus to be created. If not provided,</span>
<span class="sd">                Google server will provide one for you.</span>
<span class="sd">            display_name: Title of the corpus. If not provided, Google server</span>
<span class="sd">                will provide one for you.</span>

<span class="sd">        Returns:</span>
<span class="sd">            An instance of the vector store that points to the specified corpus.</span>

<span class="sd">        Raises:</span>
<span class="sd">            An exception if the corpus already exists or the user hits the</span>
<span class="sd">            quota limit.</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">llama_index.vector_stores.google.genai_extension</span> <span class="k">as</span> <span class="nn">genaix</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">_import_err_msg</span><span class="p">)</span>

        <span class="n">_logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"</span><span class="se">\n\n</span><span class="s2">GoogleVectorStore.create_corpus(new_corpus_id=</span><span class="si">{</span><span class="n">corpus_id</span><span class="si">}</span><span class="s2">, new_display_name=</span><span class="si">{</span><span class="n">display_name</span><span class="si">}</span><span class="s2">)"</span>
        <span class="p">)</span>

        <span class="n">client</span> <span class="o">=</span> <span class="n">genaix</span><span class="o">.</span><span class="n">build_semantic_retriever</span><span class="p">()</span>
        <span class="n">new_corpus_id</span> <span class="o">=</span> <span class="n">corpus_id</span> <span class="ow">or</span> <span class="nb">str</span><span class="p">(</span><span class="n">uuid</span><span class="o">.</span><span class="n">uuid4</span><span class="p">())</span>
        <span class="n">new_corpus</span> <span class="o">=</span> <span class="n">genaix</span><span class="o">.</span><span class="n">create_corpus</span><span class="p">(</span>
            <span class="n">corpus_id</span><span class="o">=</span><span class="n">new_corpus_id</span><span class="p">,</span> <span class="n">display_name</span><span class="o">=</span><span class="n">display_name</span><span class="p">,</span> <span class="n">client</span><span class="o">=</span><span class="n">client</span>
        <span class="p">)</span>
        <span class="n">name</span> <span class="o">=</span> <span class="n">genaix</span><span class="o">.</span><span class="n">EntityName</span><span class="o">.</span><span class="n">from_str</span><span class="p">(</span><span class="n">new_corpus</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">corpus_id</span><span class="o">=</span><span class="n">name</span><span class="o">.</span><span class="n">corpus_id</span><span class="p">,</span> <span class="n">client</span><span class="o">=</span><span class="n">client</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"GoogleVectorStore"</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span>

    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Add nodes with embedding to vector store.</span>

<span class="sd">        If a node has a source node, the source node's ID will be used to create</span>
<span class="sd">        a document. Otherwise, a default document for that corpus will be used</span>
<span class="sd">        to house the node.</span>

<span class="sd">        Furthermore, if the source node has a metadata field "file_name", it</span>
<span class="sd">        will be used as the title of the document. If the source node has no</span>
<span class="sd">        such field, Google server will assign a title to the document.</span>

<span class="sd">        Example:</span>
<span class="sd">            store = GoogleVectorStore.from_corpus(corpus_id="123")</span>
<span class="sd">            store.add([</span>
<span class="sd">                TextNode(</span>
<span class="sd">                    text="Hello, my darling",</span>
<span class="sd">                    relationships={</span>
<span class="sd">                        NodeRelationship.SOURCE: RelatedNodeInfo(</span>
<span class="sd">                            node_id="doc-456",</span>
<span class="sd">                            metadata={"file_name": "Title for doc-456"},</span>
<span class="sd">                        )</span>
<span class="sd">                    },</span>
<span class="sd">                ),</span>
<span class="sd">                TextNode(</span>
<span class="sd">                    text="Goodbye, my baby",</span>
<span class="sd">                    relationships={</span>
<span class="sd">                        NodeRelationship.SOURCE: RelatedNodeInfo(</span>
<span class="sd">                            node_id="doc-456",</span>
<span class="sd">                            metadata={"file_name": "Title for doc-456"},</span>
<span class="sd">                        )</span>
<span class="sd">                    },</span>
<span class="sd">                ),</span>
<span class="sd">            ])</span>

<span class="sd">        The above code will create one document with ID `doc-456` and title</span>
<span class="sd">        `Title for doc-456`. This document will house both nodes.</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">llama_index.vector_stores.google.genai_extension</span> <span class="k">as</span> <span class="nn">genaix</span>

            <span class="kn">import</span> <span class="nn">google.ai.generativelanguage</span> <span class="k">as</span> <span class="nn">genai</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">_import_err_msg</span><span class="p">)</span>

        <span class="n">_logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="se">\n\n</span><span class="s2">GoogleVectorStore.add(nodes=</span><span class="si">{</span><span class="n">nodes</span><span class="si">}</span><span class="s2">)"</span><span class="p">)</span>

        <span class="n">client</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">genai</span><span class="o">.</span><span class="n">RetrieverServiceClient</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="p">)</span>

        <span class="n">created_node_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">nodeGroup</span> <span class="ow">in</span> <span class="n">_group_nodes_by_source</span><span class="p">(</span><span class="n">nodes</span><span class="p">):</span>
            <span class="n">source</span> <span class="o">=</span> <span class="n">nodeGroup</span><span class="o">.</span><span class="n">source_node</span>
            <span class="n">document_id</span> <span class="o">=</span> <span class="n">source</span><span class="o">.</span><span class="n">node_id</span>
            <span class="n">document</span> <span class="o">=</span> <span class="n">genaix</span><span class="o">.</span><span class="n">get_document</span><span class="p">(</span>
                <span class="n">corpus_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">corpus_id</span><span class="p">,</span> <span class="n">document_id</span><span class="o">=</span><span class="n">document_id</span><span class="p">,</span> <span class="n">client</span><span class="o">=</span><span class="n">client</span>
            <span class="p">)</span>

            <span class="k">if</span> <span class="ow">not</span> <span class="n">document</span><span class="p">:</span>
                <span class="n">genaix</span><span class="o">.</span><span class="n">create_document</span><span class="p">(</span>
                    <span class="n">corpus_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">corpus_id</span><span class="p">,</span>
                    <span class="n">display_name</span><span class="o">=</span><span class="n">source</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"file_name"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                    <span class="n">document_id</span><span class="o">=</span><span class="n">document_id</span><span class="p">,</span>
                    <span class="n">metadata</span><span class="o">=</span><span class="n">source</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span>
                    <span class="n">client</span><span class="o">=</span><span class="n">client</span><span class="p">,</span>
                <span class="p">)</span>

            <span class="n">created_chunks</span> <span class="o">=</span> <span class="n">genaix</span><span class="o">.</span><span class="n">batch_create_chunk</span><span class="p">(</span>
                <span class="n">corpus_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">corpus_id</span><span class="p">,</span>
                <span class="n">document_id</span><span class="o">=</span><span class="n">document_id</span><span class="p">,</span>
                <span class="n">texts</span><span class="o">=</span><span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodeGroup</span><span class="o">.</span><span class="n">nodes</span><span class="p">],</span>
                <span class="n">metadatas</span><span class="o">=</span><span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">metadata</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodeGroup</span><span class="o">.</span><span class="n">nodes</span><span class="p">],</span>
                <span class="n">client</span><span class="o">=</span><span class="n">client</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">created_node_ids</span><span class="o">.</span><span class="n">extend</span><span class="p">([</span><span class="n">chunk</span><span class="o">.</span><span class="n">name</span> <span class="k">for</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="n">created_chunks</span><span class="p">])</span>

        <span class="k">return</span> <span class="n">created_node_ids</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete nodes by ref_doc_id.</span>

<span class="sd">        Both the underlying nodes and the document will be deleted from Google</span>
<span class="sd">        server.</span>

<span class="sd">        Args:</span>
<span class="sd">            ref_doc_id: The document ID to be deleted.</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">llama_index.vector_stores.google.genai_extension</span> <span class="k">as</span> <span class="nn">genaix</span>

            <span class="kn">import</span> <span class="nn">google.ai.generativelanguage</span> <span class="k">as</span> <span class="nn">genai</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">_import_err_msg</span><span class="p">)</span>

        <span class="n">_logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="se">\n\n</span><span class="s2">GoogleVectorStore.delete(ref_doc_id=</span><span class="si">{</span><span class="n">ref_doc_id</span><span class="si">}</span><span class="s2">)"</span><span class="p">)</span>

        <span class="n">client</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">genai</span><span class="o">.</span><span class="n">RetrieverServiceClient</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="p">)</span>
        <span class="n">genaix</span><span class="o">.</span><span class="n">delete_document</span><span class="p">(</span>
            <span class="n">corpus_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">corpus_id</span><span class="p">,</span> <span class="n">document_id</span><span class="o">=</span><span class="n">ref_doc_id</span><span class="p">,</span> <span class="n">client</span><span class="o">=</span><span class="n">client</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Query vector store.</span>

<span class="sd">        Example:</span>
<span class="sd">            store = GoogleVectorStore.from_corpus(corpus_id="123")</span>
<span class="sd">            store.query(</span>
<span class="sd">                query=VectorStoreQuery(</span>
<span class="sd">                    query_str="What is the meaning of life?",</span>
<span class="sd">                    # Only nodes with this author.</span>
<span class="sd">                    filters=MetadataFilters(</span>
<span class="sd">                        filters=[</span>
<span class="sd">                            ExactMatchFilter(</span>
<span class="sd">                                key="author",</span>
<span class="sd">                                value="Arthur Schopenhauer",</span>
<span class="sd">                            )</span>
<span class="sd">                        ]</span>
<span class="sd">                    ),</span>
<span class="sd">                    # Only from these docs. If not provided,</span>
<span class="sd">                    # the entire corpus is searched.</span>
<span class="sd">                    doc_ids=["doc-456"],</span>
<span class="sd">                    similarity_top_k=3,</span>
<span class="sd">                )</span>
<span class="sd">            )</span>

<span class="sd">        Args:</span>
<span class="sd">            query: See `llama_index.core.vector_stores.types.VectorStoreQuery`.</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">llama_index.vector_stores.google.genai_extension</span> <span class="k">as</span> <span class="nn">genaix</span>

            <span class="kn">import</span> <span class="nn">google.ai.generativelanguage</span> <span class="k">as</span> <span class="nn">genai</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">_import_err_msg</span><span class="p">)</span>

        <span class="n">_logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="se">\n\n</span><span class="s2">GoogleVectorStore.query(query=</span><span class="si">{</span><span class="n">query</span><span class="si">}</span><span class="s2">)"</span><span class="p">)</span>

        <span class="n">query_str</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">query_str</span>
        <span class="k">if</span> <span class="n">query_str</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"VectorStoreQuery.query_str should not be None."</span><span class="p">)</span>

        <span class="n">client</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">genai</span><span class="o">.</span><span class="n">RetrieverServiceClient</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="p">)</span>

        <span class="n">relevant_chunks</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">genai</span><span class="o">.</span><span class="n">RelevantChunk</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">doc_ids</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="c1"># The chunks from query_corpus should be sorted in reverse order by</span>
            <span class="c1"># relevant score.</span>
            <span class="n">relevant_chunks</span> <span class="o">=</span> <span class="n">genaix</span><span class="o">.</span><span class="n">query_corpus</span><span class="p">(</span>
                <span class="n">corpus_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">corpus_id</span><span class="p">,</span>
                <span class="n">query</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span>
                <span class="nb">filter</span><span class="o">=</span><span class="n">_convert_filter</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">),</span>
                <span class="n">k</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
                <span class="n">client</span><span class="o">=</span><span class="n">client</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">doc_id</span> <span class="ow">in</span> <span class="n">query</span><span class="o">.</span><span class="n">doc_ids</span><span class="p">:</span>
                <span class="n">relevant_chunks</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                    <span class="n">genaix</span><span class="o">.</span><span class="n">query_document</span><span class="p">(</span>
                        <span class="n">corpus_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">corpus_id</span><span class="p">,</span>
                        <span class="n">document_id</span><span class="o">=</span><span class="n">doc_id</span><span class="p">,</span>
                        <span class="n">query</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span>
                        <span class="nb">filter</span><span class="o">=</span><span class="n">_convert_filter</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">),</span>
                        <span class="n">k</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
                        <span class="n">client</span><span class="o">=</span><span class="n">client</span><span class="p">,</span>
                    <span class="p">)</span>
                <span class="p">)</span>
            <span class="c1"># Make sure the chunks are reversed sorted according to relevant</span>
            <span class="c1"># scores even across multiple documents.</span>
            <span class="n">relevant_chunks</span><span class="o">.</span><span class="n">sort</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">c</span><span class="p">:</span> <span class="n">c</span><span class="o">.</span><span class="n">chunk_relevance_score</span><span class="p">,</span> <span class="n">reverse</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

        <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">include_metadata</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">include_metadata</span>
        <span class="n">metadata_keys</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">metadata_keys</span>
        <span class="k">for</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="n">relevant_chunks</span><span class="p">:</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="p">{}</span>
            <span class="k">if</span> <span class="n">include_metadata</span><span class="p">:</span>
                <span class="k">for</span> <span class="n">custom_metadata</span> <span class="ow">in</span> <span class="n">chunk</span><span class="o">.</span><span class="n">chunk</span><span class="o">.</span><span class="n">custom_metadata</span><span class="p">:</span>
                    <span class="c1"># Use getattr to safely extract values</span>
                    <span class="n">value</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">custom_metadata</span><span class="p">,</span> <span class="s2">"string_value"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
                    <span class="k">if</span> <span class="p">(</span>
                        <span class="n">value</span> <span class="ow">is</span> <span class="kc">None</span>
                    <span class="p">):</span>  <span class="c1"># If string_value is not set, check for numeric_value</span>
                        <span class="n">value</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">custom_metadata</span><span class="p">,</span> <span class="s2">"numeric_value"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
                    <span class="c1"># Add to the metadata dictionary only those keys that are present in metadata_keys</span>
                    <span class="k">if</span> <span class="n">value</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="p">(</span>
                        <span class="n">metadata_keys</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">or</span> <span class="n">custom_metadata</span><span class="o">.</span><span class="n">key</span> <span class="ow">in</span> <span class="n">metadata_keys</span>
                    <span class="p">):</span>
                        <span class="n">metadata</span><span class="p">[</span><span class="n">custom_metadata</span><span class="o">.</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">value</span>

            <span class="n">text_node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">chunk</span><span class="o">.</span><span class="n">chunk</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">string_value</span><span class="p">,</span>
                <span class="nb">id</span><span class="o">=</span><span class="n">_extract_chunk_id</span><span class="p">(</span><span class="n">chunk</span><span class="o">.</span><span class="n">chunk</span><span class="o">.</span><span class="n">name</span><span class="p">),</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>  <span class="c1"># Adding metadata to the node</span>
            <span class="p">)</span>
            <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">text_node</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span>
            <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
            <span class="n">ids</span><span class="o">=</span><span class="p">[</span><span class="n">_extract_chunk_id</span><span class="p">(</span><span class="n">chunk</span><span class="o">.</span><span class="n">chunk</span><span class="o">.</span><span class="n">name</span><span class="p">)</span> <span class="k">for</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="n">relevant_chunks</span><span class="p">],</span>
            <span class="n">similarities</span><span class="o">=</span><span class="p">[</span><span class="n">chunk</span><span class="o">.</span><span class="n">chunk_relevance_score</span> <span class="k">for</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="n">relevant_chunks</span><span class="p">],</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### corpus\_id `class-attribute` `instance-attribute` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/google/#llama_index.vector_stores.google.GoogleVectorStore.corpus_id "Permanent link")

```
corpus_id: str = Field(frozen=True)
```

Corpus ID that this instance of the vector store is using.

### from\_corpus `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/google/#llama_index.vector_stores.google.GoogleVectorStore.from_corpus "Permanent link")

```
from_corpus(*, corpus_id: str, include_metadata: bool = False, metadata_keys: Optional[List[str]] = None) -> [GoogleVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/google/#llama_index.vector_stores.google.GoogleVectorStore "llama_index.vector_stores.google.base.GoogleVectorStore")
```

Create an instance that points to an existing corpus.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `corpus_id` | `str` | 
ID of an existing corpus on Google's server.



 | _required_ |
| `include_metadata` | `bool` | 

Specifies whether to include custom metadata in the query results. Defaults to False, meaning metadata will not be included.



 | `False` |
| `metadata_keys` | `Optional[List[str]]` | 

Specifies which metadata keys to include in the query results if include\_metadata is set to True. If None, all metadata keys are included. Defaults to None.



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `[GoogleVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/google/#llama_index.vector_stores.google.GoogleVectorStore "llama_index.vector_stores.google.base.GoogleVectorStore")` | 
An instance of the vector store that points to the specified corpus.



 |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-google/llama_index/vector_stores/google/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">154</span>
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
<span class="normal">193</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">from_corpus</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">corpus_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">include_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">metadata_keys</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"GoogleVectorStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create an instance that points to an existing corpus.</span>

<span class="sd">    Args:</span>
<span class="sd">        corpus_id (str): ID of an existing corpus on Google's server.</span>
<span class="sd">        include_metadata (bool, optional): Specifies whether to include custom metadata in the</span>
<span class="sd">            query results. Defaults to False, meaning metadata will not be included.</span>
<span class="sd">        metadata_keys (Optional[List[str]], optional): Specifies which metadata keys to include</span>
<span class="sd">            in the query results if include_metadata is set to True. If None, all metadata keys</span>
<span class="sd">            are included. Defaults to None.</span>

<span class="sd">    Returns:</span>
<span class="sd">        An instance of the vector store that points to the specified corpus.</span>

<span class="sd">    Raises:</span>
<span class="sd">        NoSuchCorpusException if no such corpus is found.</span>
<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">import</span> <span class="nn">llama_index.vector_stores.google.genai_extension</span> <span class="k">as</span> <span class="nn">genaix</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">_import_err_msg</span><span class="p">)</span>

    <span class="n">_logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="se">\n\n</span><span class="s2">GoogleVectorStore.from_corpus(corpus_id=</span><span class="si">{</span><span class="n">corpus_id</span><span class="si">}</span><span class="s2">)"</span><span class="p">)</span>
    <span class="n">client</span> <span class="o">=</span> <span class="n">genaix</span><span class="o">.</span><span class="n">build_semantic_retriever</span><span class="p">()</span>
    <span class="k">if</span> <span class="n">genaix</span><span class="o">.</span><span class="n">get_corpus</span><span class="p">(</span><span class="n">corpus_id</span><span class="o">=</span><span class="n">corpus_id</span><span class="p">,</span> <span class="n">client</span><span class="o">=</span><span class="n">client</span><span class="p">)</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="n">NoSuchCorpusException</span><span class="p">(</span><span class="n">corpus_id</span><span class="o">=</span><span class="n">corpus_id</span><span class="p">)</span>

    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
        <span class="n">corpus_id</span><span class="o">=</span><span class="n">corpus_id</span><span class="p">,</span>
        <span class="n">client</span><span class="o">=</span><span class="n">client</span><span class="p">,</span>
        <span class="n">include_metadata</span><span class="o">=</span><span class="n">include_metadata</span><span class="p">,</span>
        <span class="n">metadata_keys</span><span class="o">=</span><span class="n">metadata_keys</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### create\_corpus `classmethod` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/google/#llama_index.vector_stores.google.GoogleVectorStore.create_corpus "Permanent link")

```
create_corpus(*, corpus_id: Optional[str] = None, display_name: Optional[str] = None) -> [GoogleVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/google/#llama_index.vector_stores.google.GoogleVectorStore "llama_index.vector_stores.google.base.GoogleVectorStore")
```

Create an instance that points to a newly created corpus.

**Examples:**

store = GoogleVectorStore.create\_corpus() print(f"Created corpus with ID: {store.corpus\_id})

store = GoogleVectorStore.create\_corpus( display\_name="My first corpus" )

store = GoogleVectorStore.create\_corpus( corpus\_id="my-corpus-1", display\_name="My first corpus" )

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `corpus_id` | `Optional[str]` | 
ID of the new corpus to be created. If not provided, Google server will provide one for you.



 | `None` |
| `display_name` | `Optional[str]` | 

Title of the corpus. If not provided, Google server will provide one for you.



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `[GoogleVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/google/#llama_index.vector_stores.google.GoogleVectorStore "llama_index.vector_stores.google.base.GoogleVectorStore")` | 
An instance of the vector store that points to the specified corpus.



 |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-google/llama_index/vector_stores/google/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">195</span>
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
<span class="normal">242</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="nd">@classmethod</span>
<span class="k">def</span> <span class="nf">create_corpus</span><span class="p">(</span>
    <span class="bp">cls</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">corpus_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">display_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"GoogleVectorStore"</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create an instance that points to a newly created corpus.</span>

<span class="sd">    Examples:</span>
<span class="sd">        store = GoogleVectorStore.create_corpus()</span>
<span class="sd">        print(f"Created corpus with ID: {store.corpus_id})</span>

<span class="sd">        store = GoogleVectorStore.create_corpus(</span>
<span class="sd">            display_name="My first corpus"</span>
<span class="sd">        )</span>

<span class="sd">        store = GoogleVectorStore.create_corpus(</span>
<span class="sd">            corpus_id="my-corpus-1",</span>
<span class="sd">            display_name="My first corpus"</span>
<span class="sd">        )</span>

<span class="sd">    Args:</span>
<span class="sd">        corpus_id: ID of the new corpus to be created. If not provided,</span>
<span class="sd">            Google server will provide one for you.</span>
<span class="sd">        display_name: Title of the corpus. If not provided, Google server</span>
<span class="sd">            will provide one for you.</span>

<span class="sd">    Returns:</span>
<span class="sd">        An instance of the vector store that points to the specified corpus.</span>

<span class="sd">    Raises:</span>
<span class="sd">        An exception if the corpus already exists or the user hits the</span>
<span class="sd">        quota limit.</span>
<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">import</span> <span class="nn">llama_index.vector_stores.google.genai_extension</span> <span class="k">as</span> <span class="nn">genaix</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">_import_err_msg</span><span class="p">)</span>

    <span class="n">_logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span>
        <span class="sa">f</span><span class="s2">"</span><span class="se">\n\n</span><span class="s2">GoogleVectorStore.create_corpus(new_corpus_id=</span><span class="si">{</span><span class="n">corpus_id</span><span class="si">}</span><span class="s2">, new_display_name=</span><span class="si">{</span><span class="n">display_name</span><span class="si">}</span><span class="s2">)"</span>
    <span class="p">)</span>

    <span class="n">client</span> <span class="o">=</span> <span class="n">genaix</span><span class="o">.</span><span class="n">build_semantic_retriever</span><span class="p">()</span>
    <span class="n">new_corpus_id</span> <span class="o">=</span> <span class="n">corpus_id</span> <span class="ow">or</span> <span class="nb">str</span><span class="p">(</span><span class="n">uuid</span><span class="o">.</span><span class="n">uuid4</span><span class="p">())</span>
    <span class="n">new_corpus</span> <span class="o">=</span> <span class="n">genaix</span><span class="o">.</span><span class="n">create_corpus</span><span class="p">(</span>
        <span class="n">corpus_id</span><span class="o">=</span><span class="n">new_corpus_id</span><span class="p">,</span> <span class="n">display_name</span><span class="o">=</span><span class="n">display_name</span><span class="p">,</span> <span class="n">client</span><span class="o">=</span><span class="n">client</span>
    <span class="p">)</span>
    <span class="n">name</span> <span class="o">=</span> <span class="n">genaix</span><span class="o">.</span><span class="n">EntityName</span><span class="o">.</span><span class="n">from_str</span><span class="p">(</span><span class="n">new_corpus</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">corpus_id</span><span class="o">=</span><span class="n">name</span><span class="o">.</span><span class="n">corpus_id</span><span class="p">,</span> <span class="n">client</span><span class="o">=</span><span class="n">client</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### add [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/google/#llama_index.vector_stores.google.GoogleVectorStore.add "Permanent link")

```
add(nodes: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], **add_kwargs: Any) -> List[str]
```

Add nodes with embedding to vector store.

If a node has a source node, the source node's ID will be used to create a document. Otherwise, a default document for that corpus will be used to house the node.

Furthermore, if the source node has a metadata field "file\_name", it will be used as the title of the document. If the source node has no such field, Google server will assign a title to the document.

Examplestore = GoogleVectorStore.from\_corpus(corpus\_id="123") store.add(\[ TextNode( text="Hello, my darling", relationships={ NodeRelationship.SOURCE: RelatedNodeInfo( node\_id="doc-456", metadata={"file\_name": "Title for doc-456"}, ) }, ), TextNode( text="Goodbye, my baby", relationships={ NodeRelationship.SOURCE: RelatedNodeInfo( node\_id="doc-456", metadata={"file\_name": "Title for doc-456"}, ) }, ), \])

The above code will create one document with ID `doc-456` and title `Title for doc-456`. This document will house both nodes.

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-google/llama_index/vector_stores/google/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">252</span>
<span class="normal">253</span>
<span class="normal">254</span>
<span class="normal">255</span>
<span class="normal">256</span>
<span class="normal">257</span>
<span class="normal">258</span>
<span class="normal">259</span>
<span class="normal">260</span>
<span class="normal">261</span>
<span class="normal">262</span>
<span class="normal">263</span>
<span class="normal">264</span>
<span class="normal">265</span>
<span class="normal">266</span>
<span class="normal">267</span>
<span class="normal">268</span>
<span class="normal">269</span>
<span class="normal">270</span>
<span class="normal">271</span>
<span class="normal">272</span>
<span class="normal">273</span>
<span class="normal">274</span>
<span class="normal">275</span>
<span class="normal">276</span>
<span class="normal">277</span>
<span class="normal">278</span>
<span class="normal">279</span>
<span class="normal">280</span>
<span class="normal">281</span>
<span class="normal">282</span>
<span class="normal">283</span>
<span class="normal">284</span>
<span class="normal">285</span>
<span class="normal">286</span>
<span class="normal">287</span>
<span class="normal">288</span>
<span class="normal">289</span>
<span class="normal">290</span>
<span class="normal">291</span>
<span class="normal">292</span>
<span class="normal">293</span>
<span class="normal">294</span>
<span class="normal">295</span>
<span class="normal">296</span>
<span class="normal">297</span>
<span class="normal">298</span>
<span class="normal">299</span>
<span class="normal">300</span>
<span class="normal">301</span>
<span class="normal">302</span>
<span class="normal">303</span>
<span class="normal">304</span>
<span class="normal">305</span>
<span class="normal">306</span>
<span class="normal">307</span>
<span class="normal">308</span>
<span class="normal">309</span>
<span class="normal">310</span>
<span class="normal">311</span>
<span class="normal">312</span>
<span class="normal">313</span>
<span class="normal">314</span>
<span class="normal">315</span>
<span class="normal">316</span>
<span class="normal">317</span>
<span class="normal">318</span>
<span class="normal">319</span>
<span class="normal">320</span>
<span class="normal">321</span>
<span class="normal">322</span>
<span class="normal">323</span>
<span class="normal">324</span>
<span class="normal">325</span>
<span class="normal">326</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Add nodes with embedding to vector store.</span>

<span class="sd">    If a node has a source node, the source node's ID will be used to create</span>
<span class="sd">    a document. Otherwise, a default document for that corpus will be used</span>
<span class="sd">    to house the node.</span>

<span class="sd">    Furthermore, if the source node has a metadata field "file_name", it</span>
<span class="sd">    will be used as the title of the document. If the source node has no</span>
<span class="sd">    such field, Google server will assign a title to the document.</span>

<span class="sd">    Example:</span>
<span class="sd">        store = GoogleVectorStore.from_corpus(corpus_id="123")</span>
<span class="sd">        store.add([</span>
<span class="sd">            TextNode(</span>
<span class="sd">                text="Hello, my darling",</span>
<span class="sd">                relationships={</span>
<span class="sd">                    NodeRelationship.SOURCE: RelatedNodeInfo(</span>
<span class="sd">                        node_id="doc-456",</span>
<span class="sd">                        metadata={"file_name": "Title for doc-456"},</span>
<span class="sd">                    )</span>
<span class="sd">                },</span>
<span class="sd">            ),</span>
<span class="sd">            TextNode(</span>
<span class="sd">                text="Goodbye, my baby",</span>
<span class="sd">                relationships={</span>
<span class="sd">                    NodeRelationship.SOURCE: RelatedNodeInfo(</span>
<span class="sd">                        node_id="doc-456",</span>
<span class="sd">                        metadata={"file_name": "Title for doc-456"},</span>
<span class="sd">                    )</span>
<span class="sd">                },</span>
<span class="sd">            ),</span>
<span class="sd">        ])</span>

<span class="sd">    The above code will create one document with ID `doc-456` and title</span>
<span class="sd">    `Title for doc-456`. This document will house both nodes.</span>
<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">import</span> <span class="nn">llama_index.vector_stores.google.genai_extension</span> <span class="k">as</span> <span class="nn">genaix</span>

        <span class="kn">import</span> <span class="nn">google.ai.generativelanguage</span> <span class="k">as</span> <span class="nn">genai</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">_import_err_msg</span><span class="p">)</span>

    <span class="n">_logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="se">\n\n</span><span class="s2">GoogleVectorStore.add(nodes=</span><span class="si">{</span><span class="n">nodes</span><span class="si">}</span><span class="s2">)"</span><span class="p">)</span>

    <span class="n">client</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">genai</span><span class="o">.</span><span class="n">RetrieverServiceClient</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="p">)</span>

    <span class="n">created_node_ids</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">nodeGroup</span> <span class="ow">in</span> <span class="n">_group_nodes_by_source</span><span class="p">(</span><span class="n">nodes</span><span class="p">):</span>
        <span class="n">source</span> <span class="o">=</span> <span class="n">nodeGroup</span><span class="o">.</span><span class="n">source_node</span>
        <span class="n">document_id</span> <span class="o">=</span> <span class="n">source</span><span class="o">.</span><span class="n">node_id</span>
        <span class="n">document</span> <span class="o">=</span> <span class="n">genaix</span><span class="o">.</span><span class="n">get_document</span><span class="p">(</span>
            <span class="n">corpus_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">corpus_id</span><span class="p">,</span> <span class="n">document_id</span><span class="o">=</span><span class="n">document_id</span><span class="p">,</span> <span class="n">client</span><span class="o">=</span><span class="n">client</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">document</span><span class="p">:</span>
            <span class="n">genaix</span><span class="o">.</span><span class="n">create_document</span><span class="p">(</span>
                <span class="n">corpus_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">corpus_id</span><span class="p">,</span>
                <span class="n">display_name</span><span class="o">=</span><span class="n">source</span><span class="o">.</span><span class="n">metadata</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"file_name"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                <span class="n">document_id</span><span class="o">=</span><span class="n">document_id</span><span class="p">,</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">source</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span>
                <span class="n">client</span><span class="o">=</span><span class="n">client</span><span class="p">,</span>
            <span class="p">)</span>

        <span class="n">created_chunks</span> <span class="o">=</span> <span class="n">genaix</span><span class="o">.</span><span class="n">batch_create_chunk</span><span class="p">(</span>
            <span class="n">corpus_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">corpus_id</span><span class="p">,</span>
            <span class="n">document_id</span><span class="o">=</span><span class="n">document_id</span><span class="p">,</span>
            <span class="n">texts</span><span class="o">=</span><span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">()</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodeGroup</span><span class="o">.</span><span class="n">nodes</span><span class="p">],</span>
            <span class="n">metadatas</span><span class="o">=</span><span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">metadata</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodeGroup</span><span class="o">.</span><span class="n">nodes</span><span class="p">],</span>
            <span class="n">client</span><span class="o">=</span><span class="n">client</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">created_node_ids</span><span class="o">.</span><span class="n">extend</span><span class="p">([</span><span class="n">chunk</span><span class="o">.</span><span class="n">name</span> <span class="k">for</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="n">created_chunks</span><span class="p">])</span>

    <span class="k">return</span> <span class="n">created_node_ids</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/google/#llama_index.vector_stores.google.GoogleVectorStore.delete "Permanent link")

```
delete(ref_doc_id: str, **delete_kwargs: Any) -> None
```

Delete nodes by ref\_doc\_id.

Both the underlying nodes and the document will be deleted from Google server.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `ref_doc_id` | `str` | 
The document ID to be deleted.



 | _required_ |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-google/llama_index/vector_stores/google/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">328</span>
<span class="normal">329</span>
<span class="normal">330</span>
<span class="normal">331</span>
<span class="normal">332</span>
<span class="normal">333</span>
<span class="normal">334</span>
<span class="normal">335</span>
<span class="normal">336</span>
<span class="normal">337</span>
<span class="normal">338</span>
<span class="normal">339</span>
<span class="normal">340</span>
<span class="normal">341</span>
<span class="normal">342</span>
<span class="normal">343</span>
<span class="normal">344</span>
<span class="normal">345</span>
<span class="normal">346</span>
<span class="normal">347</span>
<span class="normal">348</span>
<span class="normal">349</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete nodes by ref_doc_id.</span>

<span class="sd">    Both the underlying nodes and the document will be deleted from Google</span>
<span class="sd">    server.</span>

<span class="sd">    Args:</span>
<span class="sd">        ref_doc_id: The document ID to be deleted.</span>
<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">import</span> <span class="nn">llama_index.vector_stores.google.genai_extension</span> <span class="k">as</span> <span class="nn">genaix</span>

        <span class="kn">import</span> <span class="nn">google.ai.generativelanguage</span> <span class="k">as</span> <span class="nn">genai</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">_import_err_msg</span><span class="p">)</span>

    <span class="n">_logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="se">\n\n</span><span class="s2">GoogleVectorStore.delete(ref_doc_id=</span><span class="si">{</span><span class="n">ref_doc_id</span><span class="si">}</span><span class="s2">)"</span><span class="p">)</span>

    <span class="n">client</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">genai</span><span class="o">.</span><span class="n">RetrieverServiceClient</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="p">)</span>
    <span class="n">genaix</span><span class="o">.</span><span class="n">delete_document</span><span class="p">(</span>
        <span class="n">corpus_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">corpus_id</span><span class="p">,</span> <span class="n">document_id</span><span class="o">=</span><span class="n">ref_doc_id</span><span class="p">,</span> <span class="n">client</span><span class="o">=</span><span class="n">client</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### query [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/google/#llama_index.vector_stores.google.GoogleVectorStore.query "Permanent link")

```
query(query: [VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery"), **kwargs: Any) -> [VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")
```

Query vector store.

Examplestore = GoogleVectorStore.from\_corpus(corpus\_id="123") store.query( query=VectorStoreQuery( query\_str="What is the meaning of life?", # Only nodes with this author. filters=MetadataFilters( filters=\[ ExactMatchFilter( key="author", value="Arthur Schopenhauer", ) \] ), # Only from these docs. If not provided, # the entire corpus is searched. doc\_ids=\["doc-456"\], similarity\_top\_k=3, ) )

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `[VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery")` | 
See `llama_index.core.vector_stores.types.VectorStoreQuery`.



 | _required_ |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-google/llama_index/vector_stores/google/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">351</span>
<span class="normal">352</span>
<span class="normal">353</span>
<span class="normal">354</span>
<span class="normal">355</span>
<span class="normal">356</span>
<span class="normal">357</span>
<span class="normal">358</span>
<span class="normal">359</span>
<span class="normal">360</span>
<span class="normal">361</span>
<span class="normal">362</span>
<span class="normal">363</span>
<span class="normal">364</span>
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
<span class="normal">394</span>
<span class="normal">395</span>
<span class="normal">396</span>
<span class="normal">397</span>
<span class="normal">398</span>
<span class="normal">399</span>
<span class="normal">400</span>
<span class="normal">401</span>
<span class="normal">402</span>
<span class="normal">403</span>
<span class="normal">404</span>
<span class="normal">405</span>
<span class="normal">406</span>
<span class="normal">407</span>
<span class="normal">408</span>
<span class="normal">409</span>
<span class="normal">410</span>
<span class="normal">411</span>
<span class="normal">412</span>
<span class="normal">413</span>
<span class="normal">414</span>
<span class="normal">415</span>
<span class="normal">416</span>
<span class="normal">417</span>
<span class="normal">418</span>
<span class="normal">419</span>
<span class="normal">420</span>
<span class="normal">421</span>
<span class="normal">422</span>
<span class="normal">423</span>
<span class="normal">424</span>
<span class="normal">425</span>
<span class="normal">426</span>
<span class="normal">427</span>
<span class="normal">428</span>
<span class="normal">429</span>
<span class="normal">430</span>
<span class="normal">431</span>
<span class="normal">432</span>
<span class="normal">433</span>
<span class="normal">434</span>
<span class="normal">435</span>
<span class="normal">436</span>
<span class="normal">437</span>
<span class="normal">438</span>
<span class="normal">439</span>
<span class="normal">440</span>
<span class="normal">441</span>
<span class="normal">442</span>
<span class="normal">443</span>
<span class="normal">444</span>
<span class="normal">445</span>
<span class="normal">446</span>
<span class="normal">447</span>
<span class="normal">448</span>
<span class="normal">449</span>
<span class="normal">450</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Query vector store.</span>

<span class="sd">    Example:</span>
<span class="sd">        store = GoogleVectorStore.from_corpus(corpus_id="123")</span>
<span class="sd">        store.query(</span>
<span class="sd">            query=VectorStoreQuery(</span>
<span class="sd">                query_str="What is the meaning of life?",</span>
<span class="sd">                # Only nodes with this author.</span>
<span class="sd">                filters=MetadataFilters(</span>
<span class="sd">                    filters=[</span>
<span class="sd">                        ExactMatchFilter(</span>
<span class="sd">                            key="author",</span>
<span class="sd">                            value="Arthur Schopenhauer",</span>
<span class="sd">                        )</span>
<span class="sd">                    ]</span>
<span class="sd">                ),</span>
<span class="sd">                # Only from these docs. If not provided,</span>
<span class="sd">                # the entire corpus is searched.</span>
<span class="sd">                doc_ids=["doc-456"],</span>
<span class="sd">                similarity_top_k=3,</span>
<span class="sd">            )</span>
<span class="sd">        )</span>

<span class="sd">    Args:</span>
<span class="sd">        query: See `llama_index.core.vector_stores.types.VectorStoreQuery`.</span>
<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="kn">import</span> <span class="nn">llama_index.vector_stores.google.genai_extension</span> <span class="k">as</span> <span class="nn">genaix</span>

        <span class="kn">import</span> <span class="nn">google.ai.generativelanguage</span> <span class="k">as</span> <span class="nn">genai</span>
    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">_import_err_msg</span><span class="p">)</span>

    <span class="n">_logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"</span><span class="se">\n\n</span><span class="s2">GoogleVectorStore.query(query=</span><span class="si">{</span><span class="n">query</span><span class="si">}</span><span class="s2">)"</span><span class="p">)</span>

    <span class="n">query_str</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">query_str</span>
    <span class="k">if</span> <span class="n">query_str</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"VectorStoreQuery.query_str should not be None."</span><span class="p">)</span>

    <span class="n">client</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">genai</span><span class="o">.</span><span class="n">RetrieverServiceClient</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="p">)</span>

    <span class="n">relevant_chunks</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">genai</span><span class="o">.</span><span class="n">RelevantChunk</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">doc_ids</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="c1"># The chunks from query_corpus should be sorted in reverse order by</span>
        <span class="c1"># relevant score.</span>
        <span class="n">relevant_chunks</span> <span class="o">=</span> <span class="n">genaix</span><span class="o">.</span><span class="n">query_corpus</span><span class="p">(</span>
            <span class="n">corpus_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">corpus_id</span><span class="p">,</span>
            <span class="n">query</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span>
            <span class="nb">filter</span><span class="o">=</span><span class="n">_convert_filter</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">),</span>
            <span class="n">k</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
            <span class="n">client</span><span class="o">=</span><span class="n">client</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">doc_id</span> <span class="ow">in</span> <span class="n">query</span><span class="o">.</span><span class="n">doc_ids</span><span class="p">:</span>
            <span class="n">relevant_chunks</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span>
                <span class="n">genaix</span><span class="o">.</span><span class="n">query_document</span><span class="p">(</span>
                    <span class="n">corpus_id</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">corpus_id</span><span class="p">,</span>
                    <span class="n">document_id</span><span class="o">=</span><span class="n">doc_id</span><span class="p">,</span>
                    <span class="n">query</span><span class="o">=</span><span class="n">query_str</span><span class="p">,</span>
                    <span class="nb">filter</span><span class="o">=</span><span class="n">_convert_filter</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">),</span>
                    <span class="n">k</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
                    <span class="n">client</span><span class="o">=</span><span class="n">client</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">)</span>
        <span class="c1"># Make sure the chunks are reversed sorted according to relevant</span>
        <span class="c1"># scores even across multiple documents.</span>
        <span class="n">relevant_chunks</span><span class="o">.</span><span class="n">sort</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">c</span><span class="p">:</span> <span class="n">c</span><span class="o">.</span><span class="n">chunk_relevance_score</span><span class="p">,</span> <span class="n">reverse</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

    <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">include_metadata</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">include_metadata</span>
    <span class="n">metadata_keys</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">metadata_keys</span>
    <span class="k">for</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="n">relevant_chunks</span><span class="p">:</span>
        <span class="n">metadata</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">if</span> <span class="n">include_metadata</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">custom_metadata</span> <span class="ow">in</span> <span class="n">chunk</span><span class="o">.</span><span class="n">chunk</span><span class="o">.</span><span class="n">custom_metadata</span><span class="p">:</span>
                <span class="c1"># Use getattr to safely extract values</span>
                <span class="n">value</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">custom_metadata</span><span class="p">,</span> <span class="s2">"string_value"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
                <span class="k">if</span> <span class="p">(</span>
                    <span class="n">value</span> <span class="ow">is</span> <span class="kc">None</span>
                <span class="p">):</span>  <span class="c1"># If string_value is not set, check for numeric_value</span>
                    <span class="n">value</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">custom_metadata</span><span class="p">,</span> <span class="s2">"numeric_value"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
                <span class="c1"># Add to the metadata dictionary only those keys that are present in metadata_keys</span>
                <span class="k">if</span> <span class="n">value</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="p">(</span>
                    <span class="n">metadata_keys</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">or</span> <span class="n">custom_metadata</span><span class="o">.</span><span class="n">key</span> <span class="ow">in</span> <span class="n">metadata_keys</span>
                <span class="p">):</span>
                    <span class="n">metadata</span><span class="p">[</span><span class="n">custom_metadata</span><span class="o">.</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">value</span>

        <span class="n">text_node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span>
            <span class="n">text</span><span class="o">=</span><span class="n">chunk</span><span class="o">.</span><span class="n">chunk</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">string_value</span><span class="p">,</span>
            <span class="nb">id</span><span class="o">=</span><span class="n">_extract_chunk_id</span><span class="p">(</span><span class="n">chunk</span><span class="o">.</span><span class="n">chunk</span><span class="o">.</span><span class="n">name</span><span class="p">),</span>
            <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>  <span class="c1"># Adding metadata to the node</span>
        <span class="p">)</span>
        <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">text_node</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span>
        <span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span>
        <span class="n">ids</span><span class="o">=</span><span class="p">[</span><span class="n">_extract_chunk_id</span><span class="p">(</span><span class="n">chunk</span><span class="o">.</span><span class="n">chunk</span><span class="o">.</span><span class="n">name</span><span class="p">)</span> <span class="k">for</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="n">relevant_chunks</span><span class="p">],</span>
        <span class="n">similarities</span><span class="o">=</span><span class="p">[</span><span class="n">chunk</span><span class="o">.</span><span class="n">chunk_relevance_score</span> <span class="k">for</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="n">relevant_chunks</span><span class="p">],</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Firestore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/firestore/)[Next Hologres](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/hologres/)
