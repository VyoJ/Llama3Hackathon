Title: Couchbase - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/couchbase/

Markdown Content:
Couchbase - LlamaIndex


CouchbaseVectorStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/couchbase/#llama_index.vector_stores.couchbase.CouchbaseVectorStore "Permanent link")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")`

Couchbase Vector Store.

To use, you should have the `couchbase` python package installed.

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-couchbase/llama_index/vector_stores/couchbase/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">115</span>
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
<span class="normal">474</span>
<span class="normal">475</span>
<span class="normal">476</span>
<span class="normal">477</span>
<span class="normal">478</span>
<span class="normal">479</span>
<span class="normal">480</span>
<span class="normal">481</span>
<span class="normal">482</span>
<span class="normal">483</span>
<span class="normal">484</span>
<span class="normal">485</span>
<span class="normal">486</span>
<span class="normal">487</span>
<span class="normal">488</span>
<span class="normal">489</span>
<span class="normal">490</span>
<span class="normal">491</span>
<span class="normal">492</span>
<span class="normal">493</span>
<span class="normal">494</span>
<span class="normal">495</span>
<span class="normal">496</span>
<span class="normal">497</span>
<span class="normal">498</span>
<span class="normal">499</span>
<span class="normal">500</span>
<span class="normal">501</span>
<span class="normal">502</span>
<span class="normal">503</span>
<span class="normal">504</span>
<span class="normal">505</span>
<span class="normal">506</span>
<span class="normal">507</span>
<span class="normal">508</span>
<span class="normal">509</span>
<span class="normal">510</span>
<span class="normal">511</span>
<span class="normal">512</span>
<span class="normal">513</span>
<span class="normal">514</span>
<span class="normal">515</span>
<span class="normal">516</span>
<span class="normal">517</span>
<span class="normal">518</span>
<span class="normal">519</span>
<span class="normal">520</span>
<span class="normal">521</span>
<span class="normal">522</span>
<span class="normal">523</span>
<span class="normal">524</span>
<span class="normal">525</span>
<span class="normal">526</span>
<span class="normal">527</span>
<span class="normal">528</span>
<span class="normal">529</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">CouchbaseVectorStore</span><span class="p">(</span><span class="n">BasePydanticVectorStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Couchbase Vector Store.</span>

<span class="sd">    To use, you should have the ``couchbase`` python package installed.</span>

<span class="sd">    """</span>

    <span class="n">stores_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">flat_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="c1"># Default batch size</span>
    <span class="n">DEFAULT_BATCH_SIZE</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">100</span>

    <span class="n">_cluster</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_bucket</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_scope</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_collection</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_bucket_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_scope_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_collection_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_index_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_id_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_text_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_embedding_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_metadata_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_scoped_index</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">cluster</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
        <span class="n">bucket_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">scope_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">collection_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">index_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">text_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"text"</span><span class="p">,</span>
        <span class="n">embedding_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"embedding"</span><span class="p">,</span>
        <span class="n">metadata_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"metadata"</span><span class="p">,</span>
        <span class="n">scoped_index</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Initializes a connection to a Couchbase Vector Store.</span>

<span class="sd">        Args:</span>
<span class="sd">            cluster (Cluster): Couchbase cluster object with active connection.</span>
<span class="sd">            bucket_name (str): Name of bucket to store documents in.</span>
<span class="sd">            scope_name (str): Name of scope in the bucket to store documents in.</span>
<span class="sd">            collection_name (str): Name of collection in the scope to store documents in.</span>
<span class="sd">            index_name (str): Name of the Search index.</span>
<span class="sd">            text_key (Optional[str], optional): The field for the document text.</span>
<span class="sd">                Defaults to "text".</span>
<span class="sd">            embedding_key (Optional[str], optional): The field for the document embedding.</span>
<span class="sd">                Defaults to "embedding".</span>
<span class="sd">            metadata_key (Optional[str], optional): The field for the document metadata.</span>
<span class="sd">                Defaults to "metadata".</span>
<span class="sd">            scoped_index (Optional[bool]): specify whether the index is a scoped index.</span>
<span class="sd">                Set to True by default.</span>

<span class="sd">        Returns:</span>
<span class="sd">            None</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">couchbase.cluster</span> <span class="kn">import</span> <span class="n">Cluster</span>
        <span class="k">except</span> <span class="ne">ImportError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
                <span class="s2">"Could not import couchbase python package. "</span>
                <span class="s2">"Please install couchbase SDK  with `pip install couchbase`."</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">cluster</span><span class="p">,</span> <span class="n">Cluster</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"cluster should be an instance of couchbase.Cluster, "</span>
                <span class="sa">f</span><span class="s2">"got </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">cluster</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_cluster</span> <span class="o">=</span> <span class="n">cluster</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">bucket_name</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"bucket_name must be provided."</span><span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">scope_name</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"scope_name must be provided."</span><span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">collection_name</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"collection_name must be provided."</span><span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">index_name</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"index_name must be provided."</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_bucket_name</span> <span class="o">=</span> <span class="n">bucket_name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_scope_name</span> <span class="o">=</span> <span class="n">scope_name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_collection_name</span> <span class="o">=</span> <span class="n">collection_name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_text_key</span> <span class="o">=</span> <span class="n">text_key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_embedding_key</span> <span class="o">=</span> <span class="n">embedding_key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_index_name</span> <span class="o">=</span> <span class="n">index_name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_metadata_key</span> <span class="o">=</span> <span class="n">metadata_key</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_scoped_index</span> <span class="o">=</span> <span class="n">scoped_index</span>

        <span class="c1"># Check if the bucket exists</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_check_bucket_exists</span><span class="p">():</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Bucket </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_bucket_name</span><span class="si">}</span><span class="s2"> does not exist. "</span>
                <span class="s2">" Please create the bucket before searching."</span>
            <span class="p">)</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_bucket</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cluster</span><span class="o">.</span><span class="n">bucket</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_bucket_name</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_scope</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_bucket</span><span class="o">.</span><span class="n">scope</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_scope_name</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_scope</span><span class="o">.</span><span class="n">collection</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_collection_name</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Error connecting to couchbase. "</span>
                <span class="s2">"Please check the connection and credentials."</span>
            <span class="p">)</span> <span class="kn">from</span> <span class="nn">e</span>

        <span class="c1"># Check if the scope and collection exists. Throws ValueError if they don't</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_check_scope_and_collection_exists</span><span class="p">()</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">raise</span>

        <span class="c1"># Check if the index exists. Throws ValueError if it doesn't</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_check_index_exists</span><span class="p">()</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">raise</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_bucket</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cluster</span><span class="o">.</span><span class="n">bucket</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_bucket_name</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_scope</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_bucket</span><span class="o">.</span><span class="n">scope</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_scope_name</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_scope</span><span class="o">.</span><span class="n">collection</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_collection_name</span><span class="p">)</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Add nodes to the collection and return their document IDs.</span>

<span class="sd">        Args:</span>
<span class="sd">            nodes (List[BaseNode]): List of nodes to add.</span>
<span class="sd">            **kwargs (Any): Additional keyword arguments.</span>
<span class="sd">                batch_size (int): Size of the batch for batch insert.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[str]: List of document IDs for the added nodes.</span>
<span class="sd">        """</span>
        <span class="kn">from</span> <span class="nn">couchbase.exceptions</span> <span class="kn">import</span> <span class="n">DocumentExistsException</span>

        <span class="n">batch_size</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"batch_size"</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">DEFAULT_BATCH_SIZE</span><span class="p">)</span>
        <span class="n">documents_to_insert</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">doc_ids</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">metadata</span> <span class="o">=</span> <span class="n">node_to_metadata_dict</span><span class="p">(</span>
                <span class="n">node</span><span class="p">,</span>
                <span class="n">remove_text</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">text_field</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_text_key</span><span class="p">,</span>
                <span class="n">flat_metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">flat_metadata</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">doc_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">node_id</span>

            <span class="n">doc</span> <span class="o">=</span> <span class="p">{</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_text_key</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">),</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_embedding_key</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">embedding</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_metadata_key</span><span class="p">:</span> <span class="n">metadata</span><span class="p">,</span>
            <span class="p">}</span>

            <span class="n">documents_to_insert</span><span class="o">.</span><span class="n">append</span><span class="p">({</span><span class="n">doc_id</span><span class="p">:</span> <span class="n">doc</span><span class="p">})</span>

        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">documents_to_insert</span><span class="p">),</span> <span class="n">batch_size</span><span class="p">):</span>
            <span class="n">batch</span> <span class="o">=</span> <span class="n">documents_to_insert</span><span class="p">[</span><span class="n">i</span> <span class="p">:</span> <span class="n">i</span> <span class="o">+</span> <span class="n">batch_size</span><span class="p">]</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="c1"># convert the list of dicts to a single dict for batch insert</span>
                <span class="n">insert_batch</span> <span class="o">=</span> <span class="p">{}</span>
                <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">batch</span><span class="p">:</span>
                    <span class="n">insert_batch</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">doc</span><span class="p">)</span>

                <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Inserting batch of documents to Couchbase"</span><span class="p">,</span> <span class="n">insert_batch</span><span class="p">)</span>

                <span class="c1"># upsert the batch of documents into the collection</span>
                <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">upsert_multi</span><span class="p">(</span><span class="n">insert_batch</span><span class="p">)</span>

                <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Insert result: </span><span class="si">{</span><span class="n">result</span><span class="o">.</span><span class="n">all_ok</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
                <span class="k">if</span> <span class="n">result</span><span class="o">.</span><span class="n">all_ok</span><span class="p">:</span>
                    <span class="n">doc_ids</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">insert_batch</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>

            <span class="k">except</span> <span class="n">DocumentExistsException</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Document already exists: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Inserted batch of documents to Couchbase"</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">doc_ids</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Delete a document by its reference document ID.</span>

<span class="sd">        Args:</span>
<span class="sd">            ref_doc_id: The reference document ID to be deleted.</span>

<span class="sd">        Returns:</span>
<span class="sd">            None</span>
<span class="sd">        """</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">document_field</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_metadata_key</span> <span class="o">+</span> <span class="s2">".ref_doc_id"</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_scope</span><span class="o">.</span><span class="n">query</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"DELETE FROM `</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_collection_name</span><span class="si">}</span><span class="s2">` WHERE </span><span class="si">{</span><span class="n">document_field</span><span class="si">}</span><span class="s2"> = '</span><span class="si">{</span><span class="n">ref_doc_id</span><span class="si">}</span><span class="s2">'"</span>
            <span class="p">)</span><span class="o">.</span><span class="n">execute</span><span class="p">()</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Deleted document </span><span class="si">{</span><span class="n">ref_doc_id</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Error deleting document </span><span class="si">{</span><span class="n">ref_doc_id</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">raise</span>

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Executes a query in the vector store and returns the result.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (VectorStoreQuery): The query object containing the search parameters.</span>
<span class="sd">            **kwargs (Any): Additional keyword arguments.</span>
<span class="sd">                cb_search_options (Dict): Search options to pass to Couchbase Search</span>

<span class="sd">        Returns:</span>
<span class="sd">            VectorStoreQueryResult: The result of the query containing the top-k nodes, similarities, and ids.</span>
<span class="sd">        """</span>
        <span class="kn">import</span> <span class="nn">couchbase.search</span> <span class="k">as</span> <span class="nn">search</span>
        <span class="kn">from</span> <span class="nn">couchbase.options</span> <span class="kn">import</span> <span class="n">SearchOptions</span>
        <span class="kn">from</span> <span class="nn">couchbase.vector_search</span> <span class="kn">import</span> <span class="n">VectorQuery</span><span class="p">,</span> <span class="n">VectorSearch</span>

        <span class="n">fields</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">output_fields</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">fields</span><span class="p">:</span>
            <span class="n">fields</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"*"</span><span class="p">]</span>

        <span class="c1"># Document text field needs to be returned from the search</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_text_key</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">fields</span> <span class="ow">and</span> <span class="n">fields</span> <span class="o">!=</span> <span class="p">[</span><span class="s2">"*"</span><span class="p">]:</span>
            <span class="n">fields</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_text_key</span><span class="p">)</span>

        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Output Fields: "</span><span class="p">,</span> <span class="n">fields</span><span class="p">)</span>

        <span class="n">k</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span>

        <span class="c1"># Get the search options</span>
        <span class="n">search_options</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"cb_search_options"</span><span class="p">,</span> <span class="p">{})</span>

        <span class="k">if</span> <span class="n">search_options</span> <span class="ow">and</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Cannot use both filters and cb_search_options"</span><span class="p">)</span>
        <span class="k">elif</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">:</span>
            <span class="n">couchbase_options</span> <span class="o">=</span> <span class="n">_to_couchbase_filter</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">)</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Filters transformed to Couchbase: </span><span class="si">{</span><span class="n">couchbase_options</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="n">search_options</span> <span class="o">=</span> <span class="n">couchbase_options</span>

        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Filters: </span><span class="si">{</span><span class="n">search_options</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="c1"># Create Search Request</span>
        <span class="n">search_req</span> <span class="o">=</span> <span class="n">search</span><span class="o">.</span><span class="n">SearchRequest</span><span class="o">.</span><span class="n">create</span><span class="p">(</span>
            <span class="n">VectorSearch</span><span class="o">.</span><span class="n">from_vector_query</span><span class="p">(</span>
                <span class="n">VectorQuery</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_embedding_key</span><span class="p">,</span>
                    <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">,</span>
                    <span class="n">k</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">)</span>
        <span class="p">)</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Querying Couchbase"</span><span class="p">)</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_scoped_index</span><span class="p">:</span>
                <span class="n">search_iter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_scope</span><span class="o">.</span><span class="n">search</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_index_name</span><span class="p">,</span>
                    <span class="n">search_req</span><span class="p">,</span>
                    <span class="n">SearchOptions</span><span class="p">(</span><span class="n">limit</span><span class="o">=</span><span class="n">k</span><span class="p">,</span> <span class="n">fields</span><span class="o">=</span><span class="n">fields</span><span class="p">,</span> <span class="n">raw</span><span class="o">=</span><span class="n">search_options</span><span class="p">),</span>
                <span class="p">)</span>

            <span class="k">else</span><span class="p">:</span>
                <span class="n">search_iter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cluster</span><span class="o">.</span><span class="n">search</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_index_name</span><span class="p">,</span>
                    <span class="n">search_req</span><span class="p">,</span>
                    <span class="n">SearchOptions</span><span class="p">(</span><span class="n">limit</span><span class="o">=</span><span class="n">k</span><span class="p">,</span> <span class="n">fields</span><span class="o">=</span><span class="n">fields</span><span class="p">,</span> <span class="n">raw</span><span class="o">=</span><span class="n">search_options</span><span class="p">),</span>
                <span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Search failed with error </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Search failed with error: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="n">top_k_nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">top_k_scores</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">top_k_ids</span> <span class="o">=</span> <span class="p">[]</span>

        <span class="c1"># Parse the results</span>
        <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">search_iter</span><span class="o">.</span><span class="n">rows</span><span class="p">():</span>
            <span class="n">text</span> <span class="o">=</span> <span class="n">result</span><span class="o">.</span><span class="n">fields</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_text_key</span><span class="p">,</span> <span class="s2">""</span><span class="p">)</span>

            <span class="n">score</span> <span class="o">=</span> <span class="n">result</span><span class="o">.</span><span class="n">score</span>

            <span class="c1"># Format the metadata into a dictionary</span>
            <span class="n">metadata_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_format_metadata</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">fields</span><span class="p">)</span>

            <span class="nb">id</span> <span class="o">=</span> <span class="n">result</span><span class="o">.</span><span class="n">id</span>

            <span class="k">try</span><span class="p">:</span>
                <span class="n">node</span> <span class="o">=</span> <span class="n">metadata_dict_to_node</span><span class="p">(</span><span class="n">metadata_dict</span><span class="p">,</span> <span class="n">text</span><span class="p">)</span>
            <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
                <span class="c1"># Deprecated legacy logic for backwards compatibility</span>
                <span class="n">node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
                    <span class="n">id_</span><span class="o">=</span><span class="nb">id</span><span class="p">,</span>
                    <span class="n">score</span><span class="o">=</span><span class="n">score</span><span class="p">,</span>
                    <span class="n">metadata</span><span class="o">=</span><span class="n">metadata_dict</span><span class="p">,</span>
                <span class="p">)</span>

            <span class="n">top_k_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
            <span class="n">top_k_scores</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">score</span><span class="p">)</span>
            <span class="n">top_k_ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">id</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span>
            <span class="n">nodes</span><span class="o">=</span><span class="n">top_k_nodes</span><span class="p">,</span> <span class="n">similarities</span><span class="o">=</span><span class="n">top_k_scores</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">top_k_ids</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Property function to access the client attribute.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cluster</span>

    <span class="k">def</span> <span class="nf">_check_bucket_exists</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Check if the bucket exists in the linked Couchbase cluster.</span>

<span class="sd">        Returns:</span>
<span class="sd">            True if the bucket exists</span>
<span class="sd">        """</span>
        <span class="n">bucket_manager</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cluster</span><span class="o">.</span><span class="n">buckets</span><span class="p">()</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">bucket_manager</span><span class="o">.</span><span class="n">get_bucket</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_bucket_name</span><span class="p">)</span>
            <span class="k">return</span> <span class="kc">True</span>
        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Error checking if bucket exists:"</span><span class="p">,</span> <span class="n">e</span><span class="p">)</span>
            <span class="k">return</span> <span class="kc">False</span>

    <span class="k">def</span> <span class="nf">_check_scope_and_collection_exists</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Check if the scope and collection exists in the linked Couchbase bucket</span>
<span class="sd">        Returns:</span>
<span class="sd">            True if the scope and collection exist in the bucket</span>
<span class="sd">            Raises a ValueError if either is not found.</span>
<span class="sd">        """</span>
        <span class="n">scope_collection_map</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>

        <span class="c1"># Get a list of all scopes in the bucket</span>
        <span class="k">for</span> <span class="n">scope</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_bucket</span><span class="o">.</span><span class="n">collections</span><span class="p">()</span><span class="o">.</span><span class="n">get_all_scopes</span><span class="p">():</span>
            <span class="n">scope_collection_map</span><span class="p">[</span><span class="n">scope</span><span class="o">.</span><span class="n">name</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>

            <span class="c1"># Get a list of all the collections in the scope</span>
            <span class="k">for</span> <span class="n">collection</span> <span class="ow">in</span> <span class="n">scope</span><span class="o">.</span><span class="n">collections</span><span class="p">:</span>
                <span class="n">scope_collection_map</span><span class="p">[</span><span class="n">scope</span><span class="o">.</span><span class="n">name</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">collection</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>

        <span class="c1"># Check if the scope exists</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_scope_name</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">scope_collection_map</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Scope </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_scope_name</span><span class="si">}</span><span class="s2"> not found in Couchbase "</span>
                <span class="sa">f</span><span class="s2">"bucket </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_bucket_name</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>

        <span class="c1"># Check if the collection exists in the scope</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection_name</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">scope_collection_map</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_scope_name</span><span class="p">]:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s2">"Collection </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_collection_name</span><span class="si">}</span><span class="s2"> not found in scope "</span>
                <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_scope_name</span><span class="si">}</span><span class="s2"> in Couchbase bucket </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_bucket_name</span><span class="si">}</span><span class="s2">"</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="nf">_check_index_exists</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Check if the Search index exists in the linked Couchbase cluster</span>
<span class="sd">        Returns:</span>
<span class="sd">            bool: True if the index exists, False otherwise.</span>
<span class="sd">            Raises a ValueError if the index does not exist.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_scoped_index</span><span class="p">:</span>
            <span class="n">all_indexes</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">index</span><span class="o">.</span><span class="n">name</span> <span class="k">for</span> <span class="n">index</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_scope</span><span class="o">.</span><span class="n">search_indexes</span><span class="p">()</span><span class="o">.</span><span class="n">get_all_indexes</span><span class="p">()</span>
            <span class="p">]</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_name</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">all_indexes</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"Index </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_name</span><span class="si">}</span><span class="s2"> does not exist. "</span>
                    <span class="s2">" Please create the index before searching."</span>
                <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">all_indexes</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">index</span><span class="o">.</span><span class="n">name</span> <span class="k">for</span> <span class="n">index</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cluster</span><span class="o">.</span><span class="n">search_indexes</span><span class="p">()</span><span class="o">.</span><span class="n">get_all_indexes</span><span class="p">()</span>
            <span class="p">]</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_index_name</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">all_indexes</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s2">"Index </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_index_name</span><span class="si">}</span><span class="s2"> does not exist. "</span>
                    <span class="s2">" Please create the index before searching."</span>
                <span class="p">)</span>

        <span class="k">return</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="nf">_format_metadata</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">row_fields</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Helper method to format the metadata from the Couchbase Search API.</span>

<span class="sd">        Args:</span>
<span class="sd">            row_fields (Dict[str, Any]): The fields to format.</span>

<span class="sd">        Returns:</span>
<span class="sd">            Dict[str, Any]: The formatted metadata.</span>
<span class="sd">        """</span>
        <span class="n">metadata</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">row_fields</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="c1"># Couchbase Search returns the metadata key with a prefix</span>
            <span class="c1"># `metadata.` We remove it to get the original metadata key</span>
            <span class="k">if</span> <span class="n">key</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_metadata_key</span><span class="p">):</span>
                <span class="n">new_key</span> <span class="o">=</span> <span class="n">key</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_metadata_key</span> <span class="o">+</span> <span class="s2">"."</span><span class="p">)[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
                <span class="n">metadata</span><span class="p">[</span><span class="n">new_key</span><span class="p">]</span> <span class="o">=</span> <span class="n">value</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">metadata</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">value</span>

        <span class="k">return</span> <span class="n">metadata</span>
</code></pre></div></td></tr></tbody></table>

### client `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/couchbase/#llama_index.vector_stores.couchbase.CouchbaseVectorStore.client "Permanent link")

```
client: Any
```

Property function to access the client attribute.

### add [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/couchbase/#llama_index.vector_stores.couchbase.CouchbaseVectorStore.add "Permanent link")

```
add(nodes: List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")], **kwargs: Any) -> List[str]
```

Add nodes to the collection and return their document IDs.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `nodes` | `List[[BaseNode](https://docs.llamaindex.ai/en/stable/api_reference/schema/#llama_index.core.schema.BaseNode "llama_index.core.schema.BaseNode")]` | 
List of nodes to add.



 | _required_ |
| `**kwargs` | `Any` | 

Additional keyword arguments. batch\_size (int): Size of the batch for batch insert.



 | `{}` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[str]` | 
List\[str\]: List of document IDs for the added nodes.



 |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-couchbase/llama_index/vector_stores/couchbase/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">247</span>
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
<span class="normal">303</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Add nodes to the collection and return their document IDs.</span>

<span class="sd">    Args:</span>
<span class="sd">        nodes (List[BaseNode]): List of nodes to add.</span>
<span class="sd">        **kwargs (Any): Additional keyword arguments.</span>
<span class="sd">            batch_size (int): Size of the batch for batch insert.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[str]: List of document IDs for the added nodes.</span>
<span class="sd">    """</span>
    <span class="kn">from</span> <span class="nn">couchbase.exceptions</span> <span class="kn">import</span> <span class="n">DocumentExistsException</span>

    <span class="n">batch_size</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"batch_size"</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">DEFAULT_BATCH_SIZE</span><span class="p">)</span>
    <span class="n">documents_to_insert</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">doc_ids</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
        <span class="n">metadata</span> <span class="o">=</span> <span class="n">node_to_metadata_dict</span><span class="p">(</span>
            <span class="n">node</span><span class="p">,</span>
            <span class="n">remove_text</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">text_field</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_text_key</span><span class="p">,</span>
            <span class="n">flat_metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">flat_metadata</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">doc_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">node_id</span>

        <span class="n">doc</span> <span class="o">=</span> <span class="p">{</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_text_key</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">),</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_embedding_key</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">embedding</span><span class="p">,</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_metadata_key</span><span class="p">:</span> <span class="n">metadata</span><span class="p">,</span>
        <span class="p">}</span>

        <span class="n">documents_to_insert</span><span class="o">.</span><span class="n">append</span><span class="p">({</span><span class="n">doc_id</span><span class="p">:</span> <span class="n">doc</span><span class="p">})</span>

    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">documents_to_insert</span><span class="p">),</span> <span class="n">batch_size</span><span class="p">):</span>
        <span class="n">batch</span> <span class="o">=</span> <span class="n">documents_to_insert</span><span class="p">[</span><span class="n">i</span> <span class="p">:</span> <span class="n">i</span> <span class="o">+</span> <span class="n">batch_size</span><span class="p">]</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="c1"># convert the list of dicts to a single dict for batch insert</span>
            <span class="n">insert_batch</span> <span class="o">=</span> <span class="p">{}</span>
            <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">batch</span><span class="p">:</span>
                <span class="n">insert_batch</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">doc</span><span class="p">)</span>

            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Inserting batch of documents to Couchbase"</span><span class="p">,</span> <span class="n">insert_batch</span><span class="p">)</span>

            <span class="c1"># upsert the batch of documents into the collection</span>
            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_collection</span><span class="o">.</span><span class="n">upsert_multi</span><span class="p">(</span><span class="n">insert_batch</span><span class="p">)</span>

            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Insert result: </span><span class="si">{</span><span class="n">result</span><span class="o">.</span><span class="n">all_ok</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">result</span><span class="o">.</span><span class="n">all_ok</span><span class="p">:</span>
                <span class="n">doc_ids</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">insert_batch</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>

        <span class="k">except</span> <span class="n">DocumentExistsException</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Document already exists: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Inserted batch of documents to Couchbase"</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">doc_ids</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/couchbase/#llama_index.vector_stores.couchbase.CouchbaseVectorStore.delete "Permanent link")

```
delete(ref_doc_id: str, **kwargs: Any) -> None
```

Delete a document by its reference document ID.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `ref_doc_id` | `str` | 
The reference document ID to be deleted.



 | _required_ |

**Returns:**

| Type | Description |
| --- | --- |
| `None` | 
None



 |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-couchbase/llama_index/vector_stores/couchbase/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">305</span>
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
<span class="normal">323</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Delete a document by its reference document ID.</span>

<span class="sd">    Args:</span>
<span class="sd">        ref_doc_id: The reference document ID to be deleted.</span>

<span class="sd">    Returns:</span>
<span class="sd">        None</span>
<span class="sd">    """</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">document_field</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_metadata_key</span> <span class="o">+</span> <span class="s2">".ref_doc_id"</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_scope</span><span class="o">.</span><span class="n">query</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"DELETE FROM `</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_collection_name</span><span class="si">}</span><span class="s2">` WHERE </span><span class="si">{</span><span class="n">document_field</span><span class="si">}</span><span class="s2"> = '</span><span class="si">{</span><span class="n">ref_doc_id</span><span class="si">}</span><span class="s2">'"</span>
        <span class="p">)</span><span class="o">.</span><span class="n">execute</span><span class="p">()</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Deleted document </span><span class="si">{</span><span class="n">ref_doc_id</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
    <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">error</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Error deleting document </span><span class="si">{</span><span class="n">ref_doc_id</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">raise</span>
</code></pre></div></td></tr></tbody></table>

### query [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/couchbase/#llama_index.vector_stores.couchbase.CouchbaseVectorStore.query "Permanent link")

```
query(query: [VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery"), **kwargs: Any) -> [VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")
```

Executes a query in the vector store and returns the result.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `[VectorStoreQuery](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQuery "llama_index.core.vector_stores.types.VectorStoreQuery")` | 
The query object containing the search parameters.



 | _required_ |
| `**kwargs` | `Any` | 

Additional keyword arguments. cb\_search\_options (Dict): Search options to pass to Couchbase Search



 | `{}` |

**Returns:**

| Name | Type | Description |
| --- | --- | --- |
| `VectorStoreQueryResult` | `[VectorStoreQueryResult](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.VectorStoreQueryResult "llama_index.core.vector_stores.types.VectorStoreQueryResult")` | 
The result of the query containing the top-k nodes, similarities, and ids.



 |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-couchbase/llama_index/vector_stores/couchbase/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">325</span>
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
<span class="normal">428</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Executes a query in the vector store and returns the result.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (VectorStoreQuery): The query object containing the search parameters.</span>
<span class="sd">        **kwargs (Any): Additional keyword arguments.</span>
<span class="sd">            cb_search_options (Dict): Search options to pass to Couchbase Search</span>

<span class="sd">    Returns:</span>
<span class="sd">        VectorStoreQueryResult: The result of the query containing the top-k nodes, similarities, and ids.</span>
<span class="sd">    """</span>
    <span class="kn">import</span> <span class="nn">couchbase.search</span> <span class="k">as</span> <span class="nn">search</span>
    <span class="kn">from</span> <span class="nn">couchbase.options</span> <span class="kn">import</span> <span class="n">SearchOptions</span>
    <span class="kn">from</span> <span class="nn">couchbase.vector_search</span> <span class="kn">import</span> <span class="n">VectorQuery</span><span class="p">,</span> <span class="n">VectorSearch</span>

    <span class="n">fields</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">output_fields</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="n">fields</span><span class="p">:</span>
        <span class="n">fields</span> <span class="o">=</span> <span class="p">[</span><span class="s2">"*"</span><span class="p">]</span>

    <span class="c1"># Document text field needs to be returned from the search</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_text_key</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">fields</span> <span class="ow">and</span> <span class="n">fields</span> <span class="o">!=</span> <span class="p">[</span><span class="s2">"*"</span><span class="p">]:</span>
        <span class="n">fields</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_text_key</span><span class="p">)</span>

    <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Output Fields: "</span><span class="p">,</span> <span class="n">fields</span><span class="p">)</span>

    <span class="n">k</span> <span class="o">=</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span>

    <span class="c1"># Get the search options</span>
    <span class="n">search_options</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"cb_search_options"</span><span class="p">,</span> <span class="p">{})</span>

    <span class="k">if</span> <span class="n">search_options</span> <span class="ow">and</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Cannot use both filters and cb_search_options"</span><span class="p">)</span>
    <span class="k">elif</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">:</span>
        <span class="n">couchbase_options</span> <span class="o">=</span> <span class="n">_to_couchbase_filter</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">)</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Filters transformed to Couchbase: </span><span class="si">{</span><span class="n">couchbase_options</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="n">search_options</span> <span class="o">=</span> <span class="n">couchbase_options</span>

    <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Filters: </span><span class="si">{</span><span class="n">search_options</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

    <span class="c1"># Create Search Request</span>
    <span class="n">search_req</span> <span class="o">=</span> <span class="n">search</span><span class="o">.</span><span class="n">SearchRequest</span><span class="o">.</span><span class="n">create</span><span class="p">(</span>
        <span class="n">VectorSearch</span><span class="o">.</span><span class="n">from_vector_query</span><span class="p">(</span>
            <span class="n">VectorQuery</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_embedding_key</span><span class="p">,</span>
                <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">,</span>
                <span class="n">k</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">)</span>
    <span class="p">)</span>

    <span class="k">try</span><span class="p">:</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="s2">"Querying Couchbase"</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_scoped_index</span><span class="p">:</span>
            <span class="n">search_iter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_scope</span><span class="o">.</span><span class="n">search</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_index_name</span><span class="p">,</span>
                <span class="n">search_req</span><span class="p">,</span>
                <span class="n">SearchOptions</span><span class="p">(</span><span class="n">limit</span><span class="o">=</span><span class="n">k</span><span class="p">,</span> <span class="n">fields</span><span class="o">=</span><span class="n">fields</span><span class="p">,</span> <span class="n">raw</span><span class="o">=</span><span class="n">search_options</span><span class="p">),</span>
            <span class="p">)</span>

        <span class="k">else</span><span class="p">:</span>
            <span class="n">search_iter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cluster</span><span class="o">.</span><span class="n">search</span><span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_index_name</span><span class="p">,</span>
                <span class="n">search_req</span><span class="p">,</span>
                <span class="n">SearchOptions</span><span class="p">(</span><span class="n">limit</span><span class="o">=</span><span class="n">k</span><span class="p">,</span> <span class="n">fields</span><span class="o">=</span><span class="n">fields</span><span class="p">,</span> <span class="n">raw</span><span class="o">=</span><span class="n">search_options</span><span class="p">),</span>
            <span class="p">)</span>
    <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Search failed with error </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Search failed with error: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

    <span class="n">top_k_nodes</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">top_k_scores</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">top_k_ids</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="c1"># Parse the results</span>
    <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">search_iter</span><span class="o">.</span><span class="n">rows</span><span class="p">():</span>
        <span class="n">text</span> <span class="o">=</span> <span class="n">result</span><span class="o">.</span><span class="n">fields</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_text_key</span><span class="p">,</span> <span class="s2">""</span><span class="p">)</span>

        <span class="n">score</span> <span class="o">=</span> <span class="n">result</span><span class="o">.</span><span class="n">score</span>

        <span class="c1"># Format the metadata into a dictionary</span>
        <span class="n">metadata_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_format_metadata</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">fields</span><span class="p">)</span>

        <span class="nb">id</span> <span class="o">=</span> <span class="n">result</span><span class="o">.</span><span class="n">id</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">metadata_dict_to_node</span><span class="p">(</span><span class="n">metadata_dict</span><span class="p">,</span> <span class="n">text</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
            <span class="c1"># Deprecated legacy logic for backwards compatibility</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
                <span class="n">id_</span><span class="o">=</span><span class="nb">id</span><span class="p">,</span>
                <span class="n">score</span><span class="o">=</span><span class="n">score</span><span class="p">,</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">metadata_dict</span><span class="p">,</span>
            <span class="p">)</span>

        <span class="n">top_k_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
        <span class="n">top_k_scores</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">score</span><span class="p">)</span>
        <span class="n">top_k_ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">id</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span>
        <span class="n">nodes</span><span class="o">=</span><span class="n">top_k_nodes</span><span class="p">,</span> <span class="n">similarities</span><span class="o">=</span><span class="n">top_k_scores</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">top_k_ids</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Clickhouse](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/clickhouse/)[Next Dashvector](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/dashvector/)
