Title: Chroma - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/chroma/

Markdown Content:
Chroma - LlamaIndex


ChromaVectorStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/chroma/#llama_index.vector_stores.chroma.ChromaVectorStore "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")`

Chroma vector store.

In this vector store, embeddings are stored within a ChromaDB collection.

During query time, the index uses ChromaDB to query for the top k most similar nodes.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `chroma_collection` | `Collection` | 
ChromaDB collection instance



 | `None` |

**Examples:**

`pip install llama-index-vector-stores-chroma`

```
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore

# Create a Chroma client and collection
chroma_client = chromadb.EphemeralClient()
chroma_collection = chroma_client.create_collection("example_collection")

# Set up the ChromaVectorStore and StorageContext
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
```

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-chroma/llama_index/vector_stores/chroma/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">111</span>
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
<span class="normal">450</span>
<span class="normal">451</span>
<span class="normal">452</span>
<span class="normal">453</span>
<span class="normal">454</span>
<span class="normal">455</span>
<span class="normal">456</span>
<span class="normal">457</span>
<span class="normal">458</span>
<span class="normal">459</span>
<span class="normal">460</span>
<span class="normal">461</span>
<span class="normal">462</span>
<span class="normal">463</span>
<span class="normal">464</span>
<span class="normal">465</span>
<span class="normal">466</span>
<span class="normal">467</span>
<span class="normal">468</span>
<span class="normal">469</span>
<span class="normal">470</span>
<span class="normal">471</span>
<span class="normal">472</span>
<span class="normal">473</span>
<span class="normal">474</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ChromaVectorStore</span><span class="p">(</span><span class="n">BasePydanticVectorStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Chroma vector store.</span>

<span class="sd">    In this vector store, embeddings are stored within a ChromaDB collection.</span>

<span class="sd">    During query time, the index uses ChromaDB to query for the top</span>
<span class="sd">    k most similar nodes.</span>

<span class="sd">    Args:</span>
<span class="sd">        chroma_collection (chromadb.api.models.Collection.Collection):</span>
<span class="sd">            ChromaDB collection instance</span>

<span class="sd">    Examples:</span>
<span class="sd">        `pip install llama-index-vector-stores-chroma`</span>

<span class="sd">        ```python</span>
<span class="sd">        import chromadb</span>
<span class="sd">        from llama_index.vector_stores.chroma import ChromaVectorStore</span>

<span class="sd">        # Create a Chroma client and collection</span>
<span class="sd">        chroma_client = chromadb.EphemeralClient()</span>
<span class="sd">        chroma_collection = chroma_client.create_collection("example_collection")</span>

<span class="sd">        # Set up the ChromaVectorStore and StorageContext</span>
<span class="sd">        vector_store = ChromaVectorStore(chroma_collection=chroma_collection)</span>
<span class="sd">        ```</span>

<span class="sd">    """</span>

    <span class="n">stores_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">flat_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="n">collection_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
    <span class="n">host</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
    <span class="n">port</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
    <span class="n">ssl</span><span class="p">:</span> <span class="nb">bool</span>
    <span class="n">headers</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]</span>
    <span class="n">persist_dir</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
    <span class="n">collection_kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="n">Field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="nb">dict</span><span class="p">)</span>

    <span class="n">_collection</span><span class="p">:</span> <span class="n">Collection</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">chroma_collection</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">collection_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">host</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">port</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">ssl</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">headers</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">persist_dir</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">collection_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Init params."""</span>
        <span class="n">collection_kwargs</span> <span class="o">=</span> <span class="n">collection_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="k">if</span> <span class="n">chroma_collection</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">client</span> <span class="o">=</span> <span class="n">chromadb</span><span class="o">.</span><span class="n">HttpClient</span><span class="p">(</span><span class="n">host</span><span class="o">=</span><span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="o">=</span><span class="n">port</span><span class="p">,</span> <span class="n">ssl</span><span class="o">=</span><span class="n">ssl</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">get_or_create_collection</span><span class="p">(</span>
                <span class="n">name</span><span class="o">=</span><span class="n">collection_name</span><span class="p">,</span> <span class="o">**</span><span class="n">collection_kwargs</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">Collection</span><span class="p">,</span> <span class="n">chroma_collection</span><span class="p">)</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">host</span><span class="o">=</span><span class="n">host</span><span class="p">,</span>
            <span class="n">port</span><span class="o">=</span><span class="n">port</span><span class="p">,</span>
            <span class="n">ssl</span><span class="o">=</span><span class="n">ssl</span><span class="p">,</span>
            <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">,</span>
            <span class="n">collection_name</span><span class="o">=</span><span class="n">collection_name</span><span class="p">,</span>
            <span class="n">persist_dir</span><span class="o">=</span><span class="n">persist_dir</span><span class="p">,</span>
            <span class="n">collection_kwargs</span><span class="o">=</span><span class="n">collection_kwargs</span> <span class="ow">or</span> <span class="p">{},</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_collection</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">collection</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"ChromaVectorStore"</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">chromadb</span> <span class="kn">import</span> <span class="n">Collection</span>
        <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">import_err_msg</span><span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">collection</span><span class="p">,</span> <span class="n">Collection</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s2">"argument is not chromadb collection instance"</span><span class="p">)</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">chroma_collection</span><span class="o">=</span><span class="n">collection</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_params</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">collection_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">host</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">port</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">ssl</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">headers</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">persist_dir</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">collection_kwargs</span><span class="p">:</span> <span class="nb">dict</span> <span class="o">=</span> <span class="p">{},</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"ChromaVectorStore"</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">persist_dir</span><span class="p">:</span>
            <span class="n">client</span> <span class="o">=</span> <span class="n">chromadb</span><span class="o">.</span><span class="n">PersistentClient</span><span class="p">(</span><span class="n">path</span><span class="o">=</span><span class="n">persist_dir</span><span class="p">)</span>
            <span class="n">collection</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">get_or_create_collection</span><span class="p">(</span>
                <span class="n">name</span><span class="o">=</span><span class="n">collection_name</span><span class="p">,</span> <span class="o">**</span><span class="n">collection_kwargs</span>
            <span class="p">)</span>
        <span class="k">elif</span> <span class="n">host</span> <span class="ow">and</span> <span class="n">port</span><span class="p">:</span>
            <span class="n">client</span> <span class="o">=</span> <span class="n">chromadb</span><span class="o">.</span><span class="n">HttpClient</span><span class="p">(</span><span class="n">host</span><span class="o">=</span><span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="o">=</span><span class="n">port</span><span class="p">,</span> <span class="n">ssl</span><span class="o">=</span><span class="n">ssl</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">)</span>
            <span class="n">collection</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">get_or_create_collection</span><span class="p">(</span>
                <span class="n">name</span><span class="o">=</span><span class="n">collection_name</span><span class="p">,</span> <span class="o">**</span><span class="n">collection_kwargs</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Either `persist_dir` or (`host`,`port`) must be specified"</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">chroma_collection</span><span class="o">=</span><span class="n">collection</span><span class="p">,</span>
            <span class="n">host</span><span class="o">=</span><span class="n">host</span><span class="p">,</span>
            <span class="n">port</span><span class="o">=</span><span class="n">port</span><span class="p">,</span>
            <span class="n">ssl</span><span class="o">=</span><span class="n">ssl</span><span class="p">,</span>
            <span class="n">headers</span><span class="o">=</span><span class="n">headers</span><span class="p">,</span>
            <span class="n">persist_dir</span><span class="o">=</span><span class="n">persist_dir</span><span class="p">,</span>
            <span class="n">collection_kwargs</span><span class="o">=</span><span class="n">collection_kwargs</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"ChromaVectorStore"</span>

    <span class="k">def</span> <span class="nf">get_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">node_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]],</span>
        <span class="n">filters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">MetadataFilters</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Get nodes from index.</span>

<span class="sd">        Args:</span>
<span class="sd">            node_ids (List[str]): list of node ids</span>
<span class="sd">            filters (List[MetadataFilters]): list of metadata filters</span>

<span class="sd">        """</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Collection not initialized"</span><span class="p">)</span>

        <span class="n">node_ids</span> <span class="o">=</span> <span class="n">node_ids</span> <span class="ow">or</span> <span class="p">[]</span>

        <span class="k">if</span> <span class="n">filters</span><span class="p">:</span>
            <span class="n">where</span> <span class="o">=</span> <span class="n">_to_chroma_filter</span><span class="p">(</span><span class="n">filters</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">where</span> <span class="o">=</span> <span class="p">{}</span>

        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="n">where</span><span class="o">=</span><span class="n">where</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">node_ids</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">result</span><span class="o">.</span><span class="n">nodes</span>

    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Add nodes to index.</span>

<span class="sd">        Args:</span>
<span class="sd">            nodes: List[BaseNode]: list of nodes with embeddings</span>

<span class="sd">        """</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Collection not initialized"</span><span class="p">)</span>

        <span class="n">max_chunk_size</span> <span class="o">=</span> <span class="n">MAX_CHUNK_SIZE</span>
        <span class="n">node_chunks</span> <span class="o">=</span> <span class="n">chunk_list</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">max_chunk_size</span><span class="p">)</span>

        <span class="n">all_ids</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node_chunk</span> <span class="ow">in</span> <span class="n">node_chunks</span><span class="p">:</span>
            <span class="n">embeddings</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="n">metadatas</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">node_chunk</span><span class="p">:</span>
                <span class="n">embeddings</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">get_embedding</span><span class="p">())</span>
                <span class="n">metadata_dict</span> <span class="o">=</span> <span class="n">node_to_metadata_dict</span><span class="p">(</span>
                    <span class="n">node</span><span class="p">,</span> <span class="n">remove_text</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">flat_metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">flat_metadata</span>
                <span class="p">)</span>
                <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">metadata_dict</span><span class="p">:</span>
                    <span class="k">if</span> <span class="n">metadata_dict</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                        <span class="n">metadata_dict</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="s2">""</span>
                <span class="n">metadatas</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">metadata_dict</span><span class="p">)</span>
                <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span>
                <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">))</span>

            <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">add</span><span class="p">(</span>
                <span class="n">embeddings</span><span class="o">=</span><span class="n">embeddings</span><span class="p">,</span>
                <span class="n">ids</span><span class="o">=</span><span class="n">ids</span><span class="p">,</span>
                <span class="n">metadatas</span><span class="o">=</span><span class="n">metadatas</span><span class="p">,</span>
                <span class="n">documents</span><span class="o">=</span><span class="n">documents</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">all_ids</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">ids</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">all_ids</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Delete nodes using with ref_doc_id.</span>

<span class="sd">        Args:</span>
<span class="sd">            ref_doc_id (str): The doc_id of the document to delete.</span>

<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">where</span><span class="o">=</span><span class="p">{</span><span class="s2">"document_id"</span><span class="p">:</span> <span class="n">ref_doc_id</span><span class="p">})</span>

    <span class="k">def</span> <span class="nf">delete_nodes</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">node_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">filters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">MetadataFilters</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Delete nodes from index.</span>

<span class="sd">        Args:</span>
<span class="sd">            node_ids (List[str]): list of node ids</span>
<span class="sd">            filters (List[MetadataFilters]): list of metadata filters</span>

<span class="sd">        """</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Collection not initialized"</span><span class="p">)</span>

        <span class="n">node_ids</span> <span class="o">=</span> <span class="n">node_ids</span> <span class="ow">or</span> <span class="p">[]</span>

        <span class="k">if</span> <span class="n">filters</span><span class="p">:</span>
            <span class="n">where</span> <span class="o">=</span> <span class="n">_to_chroma_filter</span><span class="p">(</span><span class="n">filters</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">where</span> <span class="o">=</span> <span class="p">{}</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">ids</span><span class="o">=</span><span class="n">node_ids</span><span class="p">,</span> <span class="n">where</span><span class="o">=</span><span class="n">where</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">clear</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Clear the collection."""</span>
        <span class="n">ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">get</span><span class="p">()[</span><span class="s2">"ids"</span><span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">ids</span><span class="o">=</span><span class="n">ids</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return client."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span>

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Query index for top k most similar nodes.</span>

<span class="sd">        Args:</span>
<span class="sd">            query_embedding (List[float]): query embedding</span>
<span class="sd">            similarity_top_k (int): top k most similar nodes</span>

<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">if</span> <span class="s2">"where"</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"Cannot specify metadata filters via both query and kwargs. "</span>
                    <span class="s2">"Use kwargs only for chroma specific items that are "</span>
                    <span class="s2">"not supported via the generic query interface."</span>
                <span class="p">)</span>
            <span class="n">where</span> <span class="o">=</span> <span class="n">_to_chroma_filter</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">where</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"where"</span><span class="p">,</span> <span class="p">{})</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get</span><span class="p">(</span><span class="n">limit</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span> <span class="n">where</span><span class="o">=</span><span class="n">where</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query</span><span class="p">(</span>
            <span class="n">query_embeddings</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">,</span>
            <span class="n">n_results</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
            <span class="n">where</span><span class="o">=</span><span class="n">where</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_query</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query_embeddings</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="s2">"float"</span><span class="p">],</span> <span class="n">n_results</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">where</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
        <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">query</span><span class="p">(</span>
            <span class="n">query_embeddings</span><span class="o">=</span><span class="n">query_embeddings</span><span class="p">,</span>
            <span class="n">n_results</span><span class="o">=</span><span class="n">n_results</span><span class="p">,</span>
            <span class="n">where</span><span class="o">=</span><span class="n">where</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Top </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">results</span><span class="p">[</span><span class="s1">'documents'</span><span class="p">][</span><span class="mi">0</span><span class="p">])</span><span class="si">}</span><span class="s2"> nodes:"</span><span class="p">)</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">similarities</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node_id</span><span class="p">,</span> <span class="n">text</span><span class="p">,</span> <span class="n">metadata</span><span class="p">,</span> <span class="n">distance</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span>
            <span class="n">results</span><span class="p">[</span><span class="s2">"ids"</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span>
            <span class="n">results</span><span class="p">[</span><span class="s2">"documents"</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span>
            <span class="n">results</span><span class="p">[</span><span class="s2">"metadatas"</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span>
            <span class="n">results</span><span class="p">[</span><span class="s2">"distances"</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span>
        <span class="p">):</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">node</span> <span class="o">=</span> <span class="n">metadata_dict_to_node</span><span class="p">(</span><span class="n">metadata</span><span class="p">)</span>
                <span class="n">node</span><span class="o">.</span><span class="n">set_content</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
            <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
                <span class="c1"># NOTE: deprecated legacy logic for backward compatibility</span>
                <span class="n">metadata</span><span class="p">,</span> <span class="n">node_info</span><span class="p">,</span> <span class="n">relationships</span> <span class="o">=</span> <span class="n">legacy_metadata_dict_to_node</span><span class="p">(</span>
                    <span class="n">metadata</span>
                <span class="p">)</span>

                <span class="n">node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
                    <span class="n">id_</span><span class="o">=</span><span class="n">node_id</span><span class="p">,</span>
                    <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
                    <span class="n">start_char_idx</span><span class="o">=</span><span class="n">node_info</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"start"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                    <span class="n">end_char_idx</span><span class="o">=</span><span class="n">node_info</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"end"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                    <span class="n">relationships</span><span class="o">=</span><span class="n">relationships</span><span class="p">,</span>
                <span class="p">)</span>

            <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>

            <span class="n">similarity_score</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">exp</span><span class="p">(</span><span class="o">-</span><span class="n">distance</span><span class="p">)</span>
            <span class="n">similarities</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">similarity_score</span><span class="p">)</span>

            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"&gt; [Node </span><span class="si">{</span><span class="n">node_id</span><span class="si">}</span><span class="s2">] [Similarity score: </span><span class="si">{</span><span class="n">similarity_score</span><span class="si">}</span><span class="s2">] "</span>
                <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">truncate_text</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">text</span><span class="p">),</span><span class="w"> </span><span class="mi">100</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>
            <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node_id</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span><span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span> <span class="n">similarities</span><span class="o">=</span><span class="n">similarities</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">ids</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_get</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">limit</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">],</span> <span class="n">where</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
        <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
            <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span>
            <span class="n">where</span><span class="o">=</span><span class="n">where</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"&gt; Top </span><span class="si">{</span><span class="nb">len</span><span class="p">(</span><span class="n">results</span><span class="p">[</span><span class="s1">'documents'</span><span class="p">])</span><span class="si">}</span><span class="s2"> nodes:"</span><span class="p">)</span>
        <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">results</span><span class="p">[</span><span class="s2">"ids"</span><span class="p">]:</span>
            <span class="n">results</span><span class="p">[</span><span class="s2">"ids"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[[]]</span>

        <span class="k">for</span> <span class="n">node_id</span><span class="p">,</span> <span class="n">text</span><span class="p">,</span> <span class="n">metadata</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span>
            <span class="n">results</span><span class="p">[</span><span class="s2">"ids"</span><span class="p">],</span> <span class="n">results</span><span class="p">[</span><span class="s2">"documents"</span><span class="p">],</span> <span class="n">results</span><span class="p">[</span><span class="s2">"metadatas"</span><span class="p">]</span>
        <span class="p">):</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">node</span> <span class="o">=</span> <span class="n">metadata_dict_to_node</span><span class="p">(</span><span class="n">metadata</span><span class="p">)</span>
                <span class="n">node</span><span class="o">.</span><span class="n">set_content</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
            <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
                <span class="c1"># NOTE: deprecated legacy logic for backward compatibility</span>
                <span class="n">metadata</span><span class="p">,</span> <span class="n">node_info</span><span class="p">,</span> <span class="n">relationships</span> <span class="o">=</span> <span class="n">legacy_metadata_dict_to_node</span><span class="p">(</span>
                    <span class="n">metadata</span>
                <span class="p">)</span>

                <span class="n">node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
                    <span class="n">id_</span><span class="o">=</span><span class="n">node_id</span><span class="p">,</span>
                    <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
                    <span class="n">start_char_idx</span><span class="o">=</span><span class="n">node_info</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"start"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                    <span class="n">end_char_idx</span><span class="o">=</span><span class="n">node_info</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"end"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                    <span class="n">relationships</span><span class="o">=</span><span class="n">relationships</span><span class="p">,</span>
                <span class="p">)</span>

            <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>

            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"&gt; [Node </span><span class="si">{</span><span class="n">node_id</span><span class="si">}</span><span class="s2">] [Similarity score: N/A - using get()] "</span>
                <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">truncate_text</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">text</span><span class="p">),</span><span class="w"> </span><span class="mi">100</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>
            <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node_id</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span><span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">ids</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### client `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/chroma/#llama_index.vector_stores.chroma.ChromaVectorStore.client "Permanent link")

```
client: Any
```

Return client.

### get\_nodes [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/chroma/#llama_index.vector_stores.chroma.ChromaVectorStore.get_nodes "Permanent link")

```
get_nodes(node_ids: Optional[List[str]], filters: Optional[List[[MetadataFilters](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.MetadataFilters "llama_index.core.vector_stores.types.MetadataFilters")]] = None) -> List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]
```

Get nodes from index.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `node_ids` | `List[str]` | 
list of node ids



 | _required_ |
| `filters` | `List[[MetadataFilters](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.MetadataFilters "llama_index.core.vector_stores.types.MetadataFilters")]` | 

list of metadata filters



 | `None` |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-chroma/llama_index/vector_stores/chroma/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">238</span>
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
<span class="normal">262</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">get_nodes</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">node_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]],</span>
    <span class="n">filters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">MetadataFilters</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get nodes from index.</span>

<span class="sd">    Args:</span>
<span class="sd">        node_ids (List[str]): list of node ids</span>
<span class="sd">        filters (List[MetadataFilters]): list of metadata filters</span>

<span class="sd">    """</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Collection not initialized"</span><span class="p">)</span>

    <span class="n">node_ids</span> <span class="o">=</span> <span class="n">node_ids</span> <span class="ow">or</span> <span class="p">[]</span>

    <span class="k">if</span> <span class="n">filters</span><span class="p">:</span>
        <span class="n">where</span> <span class="o">=</span> <span class="n">_to_chroma_filter</span><span class="p">(</span><span class="n">filters</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">where</span> <span class="o">=</span> <span class="p">{}</span>

    <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="n">where</span><span class="o">=</span><span class="n">where</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">node_ids</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">result</span><span class="o">.</span><span class="n">nodes</span>
</code></pre></div></td></tr></tbody></table>

### add [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/chroma/#llama_index.vector_stores.chroma.ChromaVectorStore.add "Permanent link")

```
add(nodes: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], **add_kwargs: Any) -> List[str]
```

Add nodes to index.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `nodes` | `List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]` | 
List\[BaseNode\]: list of nodes with embeddings



 | _required_ |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-chroma/llama_index/vector_stores/chroma/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">264</span>
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
<span class="normal">303</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Add nodes to index.</span>

<span class="sd">    Args:</span>
<span class="sd">        nodes: List[BaseNode]: list of nodes with embeddings</span>

<span class="sd">    """</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Collection not initialized"</span><span class="p">)</span>

    <span class="n">max_chunk_size</span> <span class="o">=</span> <span class="n">MAX_CHUNK_SIZE</span>
    <span class="n">node_chunks</span> <span class="o">=</span> <span class="n">chunk_list</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="n">max_chunk_size</span><span class="p">)</span>

    <span class="n">all_ids</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">node_chunk</span> <span class="ow">in</span> <span class="n">node_chunks</span><span class="p">:</span>
        <span class="n">embeddings</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">metadatas</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">node_chunk</span><span class="p">:</span>
            <span class="n">embeddings</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">get_embedding</span><span class="p">())</span>
            <span class="n">metadata_dict</span> <span class="o">=</span> <span class="n">node_to_metadata_dict</span><span class="p">(</span>
                <span class="n">node</span><span class="p">,</span> <span class="n">remove_text</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">flat_metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">flat_metadata</span>
            <span class="p">)</span>
            <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">metadata_dict</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">metadata_dict</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                    <span class="n">metadata_dict</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="s2">""</span>
            <span class="n">metadatas</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">metadata_dict</span><span class="p">)</span>
            <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">node_id</span><span class="p">)</span>
            <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">))</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">add</span><span class="p">(</span>
            <span class="n">embeddings</span><span class="o">=</span><span class="n">embeddings</span><span class="p">,</span>
            <span class="n">ids</span><span class="o">=</span><span class="n">ids</span><span class="p">,</span>
            <span class="n">metadatas</span><span class="o">=</span><span class="n">metadatas</span><span class="p">,</span>
            <span class="n">documents</span><span class="o">=</span><span class="n">documents</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">all_ids</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">ids</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">all_ids</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/chroma/#llama_index.vector_stores.chroma.ChromaVectorStore.delete "Permanent link")

```
delete(ref_doc_id: str, **delete_kwargs: Any) -> None
```

Delete nodes using with ref\_doc\_id.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `ref_doc_id` | `str` | 
The doc\_id of the document to delete.



 | _required_ |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-chroma/llama_index/vector_stores/chroma/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">305</span>
<span class="normal">306</span>
<span class="normal">307</span>
<span class="normal">308</span>
<span class="normal">309</span>
<span class="normal">310</span>
<span class="normal">311</span>
<span class="normal">312</span>
<span class="normal">313</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Delete nodes using with ref_doc_id.</span>

<span class="sd">    Args:</span>
<span class="sd">        ref_doc_id (str): The doc_id of the document to delete.</span>

<span class="sd">    """</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">where</span><span class="o">=</span><span class="p">{</span><span class="s2">"document_id"</span><span class="p">:</span> <span class="n">ref_doc_id</span><span class="p">})</span>
</code></pre></div></td></tr></tbody></table>

### delete\_nodes [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/chroma/#llama_index.vector_stores.chroma.ChromaVectorStore.delete_nodes "Permanent link")

```
delete_nodes(node_ids: Optional[List[str]] = None, filters: Optional[List[[MetadataFilters](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.MetadataFilters "llama_index.core.vector_stores.types.MetadataFilters")]] = None) -> None
```

Delete nodes from index.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `node_ids` | `List[str]` | 
list of node ids



 | `None` |
| `filters` | `List[[MetadataFilters](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.MetadataFilters "llama_index.core.vector_stores.types.MetadataFilters")]` | 

list of metadata filters



 | `None` |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-chroma/llama_index/vector_stores/chroma/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">315</span>
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
<span class="normal">337</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete_nodes</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">node_ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">filters</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">MetadataFilters</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Delete nodes from index.</span>

<span class="sd">    Args:</span>
<span class="sd">        node_ids (List[str]): list of node ids</span>
<span class="sd">        filters (List[MetadataFilters]): list of metadata filters</span>

<span class="sd">    """</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Collection not initialized"</span><span class="p">)</span>

    <span class="n">node_ids</span> <span class="o">=</span> <span class="n">node_ids</span> <span class="ow">or</span> <span class="p">[]</span>

    <span class="k">if</span> <span class="n">filters</span><span class="p">:</span>
        <span class="n">where</span> <span class="o">=</span> <span class="n">_to_chroma_filter</span><span class="p">(</span><span class="n">filters</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">where</span> <span class="o">=</span> <span class="p">{}</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">ids</span><span class="o">=</span><span class="n">node_ids</span><span class="p">,</span> <span class="n">where</span><span class="o">=</span><span class="n">where</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### clear [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/chroma/#llama_index.vector_stores.chroma.ChromaVectorStore.clear "Permanent link")

```
clear() -> None
```

Clear the collection.

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-chroma/llama_index/vector_stores/chroma/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">339</span>
<span class="normal">340</span>
<span class="normal">341</span>
<span class="normal">342</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">clear</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Clear the collection."""</span>
    <span class="n">ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">get</span><span class="p">()[</span><span class="s2">"ids"</span><span class="p">]</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">ids</span><span class="o">=</span><span class="n">ids</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### query [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/chroma/#llama_index.vector_stores.chroma.ChromaVectorStore.query "Permanent link")

```
query(query: [VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery"), **kwargs: Any) -> [VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")
```

Query index for top k most similar nodes.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query_embedding` | `List[float]` | 
query embedding



 | _required_ |
| `similarity_top_k` | `int` | 

top k most similar nodes



 | _required_ |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-chroma/llama_index/vector_stores/chroma/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">349</span>
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
<span class="normal">376</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Query index for top k most similar nodes.</span>

<span class="sd">    Args:</span>
<span class="sd">        query_embedding (List[float]): query embedding</span>
<span class="sd">        similarity_top_k (int): top k most similar nodes</span>

<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="s2">"where"</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Cannot specify metadata filters via both query and kwargs. "</span>
                <span class="s2">"Use kwargs only for chroma specific items that are "</span>
                <span class="s2">"not supported via the generic query interface."</span>
            <span class="p">)</span>
        <span class="n">where</span> <span class="o">=</span> <span class="n">_to_chroma_filter</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">where</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"where"</span><span class="p">,</span> <span class="p">{})</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get</span><span class="p">(</span><span class="n">limit</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span> <span class="n">where</span><span class="o">=</span><span class="n">where</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_query</span><span class="p">(</span>
        <span class="n">query_embeddings</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">,</span>
        <span class="n">n_results</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
        <span class="n">where</span><span class="o">=</span><span class="n">where</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Chatgpt plugin](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/chatgpt_plugin/)[Next Clickhouse](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/clickhouse/)
