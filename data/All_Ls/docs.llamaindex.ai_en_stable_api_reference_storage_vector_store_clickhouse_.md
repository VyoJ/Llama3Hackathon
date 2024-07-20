Title: Clickhouse - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/clickhouse/

Markdown Content:
Clickhouse - LlamaIndex


ClickHouseVectorStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/clickhouse/#llama_index.vector_stores.clickhouse.ClickHouseVectorStore "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")`

ClickHouse Vector Store. In this vector store, embeddings and docs are stored within an existing ClickHouse cluster. During query time, the index uses ClickHouse to query for the top k most similar nodes.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `clickhouse_client` | `httpclient` | 
clickhouse-connect httpclient of an existing ClickHouse cluster.



 | `None` |
| `table` | `str` | 

The name of the ClickHouse table where data will be stored. Defaults to "llama\_index".



 | `'llama_index'` |
| `database` | `str` | 

The name of the ClickHouse database where data will be stored. Defaults to "default".



 | `'default'` |
| `index_type` | `str` | 

The type of the ClickHouse vector index. Defaults to "NONE", supported are ("NONE", "HNSW", "ANNOY")



 | `'NONE'` |
| `metric` | `str` | 

The metric type of the ClickHouse vector index. Defaults to "cosine".



 | `'cosine'` |
| `batch_size` | `int` | 

the size of documents to insert. Defaults to 1000.



 | `1000` |
| `index_params` | `dict` | 

The index parameters for ClickHouse. Defaults to None.



 | `None` |
| `search_params` | `dict` | 

The search parameters for a ClickHouse query. Defaults to None.



 | `None` |
| `service_context` | `ServiceContext` | 

Vector store service context. Defaults to None



 | `None` |

**Examples:**

`pip install llama-index-vector-stores-clickhouse`

```
from llama_index.vector_stores.clickhouse import ClickHouseVectorStore
import clickhouse_connect

# initialize client
client = clickhouse_connect.get_client(
    host="localhost",
    port=8123,
    username="default",
    password="",
)

vector_store = ClickHouseVectorStore(clickhouse_client=client)
```

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-clickhouse/llama_index/vector_stores/clickhouse/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">116</span>
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
<span class="normal">489</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">ClickHouseVectorStore</span><span class="p">(</span><span class="n">BasePydanticVectorStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""ClickHouse Vector Store.</span>
<span class="sd">    In this vector store, embeddings and docs are stored within an existing</span>
<span class="sd">    ClickHouse cluster.</span>
<span class="sd">    During query time, the index uses ClickHouse to query for the top</span>
<span class="sd">    k most similar nodes.</span>

<span class="sd">    Args:</span>
<span class="sd">        clickhouse_client (httpclient): clickhouse-connect httpclient of</span>
<span class="sd">            an existing ClickHouse cluster.</span>
<span class="sd">        table (str, optional): The name of the ClickHouse table</span>
<span class="sd">            where data will be stored. Defaults to "llama_index".</span>
<span class="sd">        database (str, optional): The name of the ClickHouse database</span>
<span class="sd">            where data will be stored. Defaults to "default".</span>
<span class="sd">        index_type (str, optional): The type of the ClickHouse vector index.</span>
<span class="sd">            Defaults to "NONE", supported are ("NONE", "HNSW", "ANNOY")</span>
<span class="sd">        metric (str, optional): The metric type of the ClickHouse vector index.</span>
<span class="sd">            Defaults to "cosine".</span>
<span class="sd">        batch_size (int, optional): the size of documents to insert. Defaults to 1000.</span>
<span class="sd">        index_params (dict, optional): The index parameters for ClickHouse.</span>
<span class="sd">            Defaults to None.</span>
<span class="sd">        search_params (dict, optional): The search parameters for a ClickHouse query.</span>
<span class="sd">            Defaults to None.</span>
<span class="sd">        service_context (ServiceContext, optional): Vector store service context.</span>
<span class="sd">            Defaults to None</span>

<span class="sd">    Examples:</span>
<span class="sd">        `pip install llama-index-vector-stores-clickhouse`</span>

<span class="sd">        ```python</span>
<span class="sd">        from llama_index.vector_stores.clickhouse import ClickHouseVectorStore</span>
<span class="sd">        import clickhouse_connect</span>

<span class="sd">        # initialize client</span>
<span class="sd">        client = clickhouse_connect.get_client(</span>
<span class="sd">            host="localhost",</span>
<span class="sd">            port=8123,</span>
<span class="sd">            username="default",</span>
<span class="sd">            password="",</span>
<span class="sd">        )</span>

<span class="sd">        vector_store = ClickHouseVectorStore(clickhouse_client=client)</span>
<span class="sd">        ```</span>
<span class="sd">    """</span>

    <span class="n">stores_text</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">flat_metadata</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="n">_table_existed</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">_client</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_config</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_dim</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_column_config</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_column_names</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_column_type_names</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">metadata_column</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"metadata"</span>
    <span class="n">AMPLIFY_RATIO_LE5</span> <span class="o">=</span> <span class="mi">100</span>
    <span class="n">AMPLIFY_RATIO_GT5</span> <span class="o">=</span> <span class="mi">20</span>
    <span class="n">AMPLIFY_RATIO_GT50</span> <span class="o">=</span> <span class="mi">10</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">clickhouse_client</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">table</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"llama_index"</span><span class="p">,</span>
        <span class="n">database</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"default"</span><span class="p">,</span>
        <span class="n">engine</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"MergeTree"</span><span class="p">,</span>
        <span class="n">index_type</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"NONE"</span><span class="p">,</span>
        <span class="n">metric</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"cosine"</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1000</span><span class="p">,</span>
        <span class="n">index_params</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">search_params</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">service_context</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ServiceContext</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize params."""</span>
        <span class="n">import_err_msg</span> <span class="o">=</span> <span class="s2">"""</span>
<span class="s2">            `clickhouse_connect` package not found,</span>
<span class="s2">            please run `pip install clickhouse-connect`</span>
<span class="s2">        """</span>
        <span class="n">clickhouse_connect_spec</span> <span class="o">=</span> <span class="n">importlib</span><span class="o">.</span><span class="n">util</span><span class="o">.</span><span class="n">find_spec</span><span class="p">(</span>
            <span class="s2">"clickhouse_connect.driver.httpclient"</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="n">clickhouse_connect_spec</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="n">import_err_msg</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">clickhouse_client</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Missing ClickHouse client!"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">clickhouse_client</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_config</span> <span class="o">=</span> <span class="n">ClickHouseSettings</span><span class="p">(</span>
            <span class="n">table</span><span class="o">=</span><span class="n">table</span><span class="p">,</span>
            <span class="n">database</span><span class="o">=</span><span class="n">database</span><span class="p">,</span>
            <span class="n">engine</span><span class="o">=</span><span class="n">engine</span><span class="p">,</span>
            <span class="n">index_type</span><span class="o">=</span><span class="n">index_type</span><span class="p">,</span>
            <span class="n">metric</span><span class="o">=</span><span class="n">metric</span><span class="p">,</span>
            <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span>
            <span class="n">index_params</span><span class="o">=</span><span class="n">index_params</span><span class="p">,</span>
            <span class="n">search_params</span><span class="o">=</span><span class="n">search_params</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="c1"># schema column name, type, and construct format method</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_column_config</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"id"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"type"</span><span class="p">:</span> <span class="s2">"String"</span><span class="p">,</span> <span class="s2">"extract_func"</span><span class="p">:</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="o">.</span><span class="n">node_id</span><span class="p">},</span>
            <span class="s2">"doc_id"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"type"</span><span class="p">:</span> <span class="s2">"String"</span><span class="p">,</span> <span class="s2">"extract_func"</span><span class="p">:</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="o">.</span><span class="n">ref_doc_id</span><span class="p">},</span>
            <span class="s2">"text"</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">"type"</span><span class="p">:</span> <span class="s2">"String"</span><span class="p">,</span>
                <span class="s2">"extract_func"</span><span class="p">:</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">escape_str</span><span class="p">(</span>
                    <span class="n">x</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">NONE</span><span class="p">)</span> <span class="ow">or</span> <span class="s2">""</span>
                <span class="p">),</span>
            <span class="p">},</span>
            <span class="s2">"vector"</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">"type"</span><span class="p">:</span> <span class="s2">"Array(Float32)"</span><span class="p">,</span>
                <span class="s2">"extract_func"</span><span class="p">:</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="o">.</span><span class="n">get_embedding</span><span class="p">(),</span>
            <span class="p">},</span>
            <span class="s2">"node_info"</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">"type"</span><span class="p">:</span> <span class="s2">"Tuple(start Nullable(UInt64), end Nullable(UInt64))"</span><span class="p">,</span>
                <span class="s2">"extract_func"</span><span class="p">:</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="o">.</span><span class="n">get_node_info</span><span class="p">(),</span>
            <span class="p">},</span>
            <span class="s2">"metadata"</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">"type"</span><span class="p">:</span> <span class="s2">"String"</span><span class="p">,</span>
                <span class="s2">"extract_func"</span><span class="p">:</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">x</span><span class="o">.</span><span class="n">metadata</span><span class="p">),</span>
            <span class="p">},</span>
        <span class="p">}</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_column_names</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_column_config</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_column_type_names</span> <span class="o">=</span> <span class="p">[</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_column_config</span><span class="p">[</span><span class="n">column_name</span><span class="p">][</span><span class="s2">"type"</span><span class="p">]</span>
            <span class="k">for</span> <span class="n">column_name</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_column_names</span>
        <span class="p">]</span>

        <span class="k">if</span> <span class="n">service_context</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">service_context</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">ServiceContext</span><span class="p">,</span> <span class="n">service_context</span><span class="p">)</span>
            <span class="n">dimension</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span>
                <span class="n">service_context</span><span class="o">.</span><span class="n">embed_model</span><span class="o">.</span><span class="n">get_query_embedding</span><span class="p">(</span><span class="s2">"try this out"</span><span class="p">)</span>
            <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">create_table</span><span class="p">(</span><span class="n">dimension</span><span class="p">)</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">clickhouse_client</span><span class="o">=</span><span class="n">clickhouse_client</span><span class="p">,</span>
            <span class="n">table</span><span class="o">=</span><span class="n">table</span><span class="p">,</span>
            <span class="n">database</span><span class="o">=</span><span class="n">database</span><span class="p">,</span>
            <span class="n">engine</span><span class="o">=</span><span class="n">engine</span><span class="p">,</span>
            <span class="n">index_type</span><span class="o">=</span><span class="n">index_type</span><span class="p">,</span>
            <span class="n">metric</span><span class="o">=</span><span class="n">metric</span><span class="p">,</span>
            <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span>
            <span class="n">index_params</span><span class="o">=</span><span class="n">index_params</span><span class="p">,</span>
            <span class="n">search_params</span><span class="o">=</span><span class="n">search_params</span><span class="p">,</span>
            <span class="n">service_context</span><span class="o">=</span><span class="n">service_context</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get client."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span>

    <span class="k">def</span> <span class="nf">create_table</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dimension</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">index</span> <span class="o">=</span> <span class="s2">""</span>
        <span class="n">settings</span> <span class="o">=</span> <span class="p">{</span><span class="s2">"allow_experimental_object_type"</span><span class="p">:</span> <span class="s2">"1"</span><span class="p">}</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_config</span><span class="o">.</span><span class="n">index_type</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span> <span class="o"></span> <span class="s2">"annoy"</span><span class="p">:</span>
            <span class="n">numTrees</span> <span class="o">=</span> <span class="mi">100</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_config</span><span class="o">.</span><span class="n">index_params</span> <span class="ow">and</span> <span class="s2">"NumTrees"</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_config</span><span class="o">.</span><span class="n">index_params</span><span class="p">:</span>
                <span class="n">numTrees</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_config</span><span class="o">.</span><span class="n">index_params</span><span class="p">[</span><span class="s2">"NumTrees"</span><span class="p">]</span>
            <span class="n">index</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"INDEX annoy_indx vector TYPE annoy('</span><span class="si">{</span><span class="n">DISTANCE_MAPPING</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_config</span><span class="o">.</span><span class="n">metric</span><span class="p">]</span><span class="si">}</span><span class="s2">', </span><span class="si">{</span><span class="n">numTrees</span><span class="si">}</span><span class="s2">)"</span>
            <span class="n">settings</span><span class="p">[</span><span class="s2">"allow_experimental_annoy_index"</span><span class="p">]</span> <span class="o">=</span> <span class="s2">"1"</span>
        <span class="n">schema_</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"""</span>
<span class="s2">            CREATE TABLE IF NOT EXISTS </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_config</span><span class="o">.</span><span class="n">database</span><span class="si">}</span><span class="s2">.</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_config</span><span class="o">.</span><span class="n">table</span><span class="si">}</span><span class="s2">(</span>
<span class="s2">                </span><span class="si">{</span><span class="s2">","</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="n">k</span><span class="si">}</span><span class="s1"> </span><span class="si">{</span><span class="n">v</span><span class="p">[</span><span class="s2">"type"</span><span class="p">]</span><span class="si">}</span><span class="s1">'</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">k</span><span class="p">,</span><span class="w"> </span><span class="n">v</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="bp">self</span><span class="o">.</span><span class="n">_column_config</span><span class="o">.</span><span class="n">items</span><span class="p">()])</span><span class="si">}</span><span class="s2">,</span>
<span class="s2">                CONSTRAINT vector_length CHECK length(vector) = </span><span class="si">{</span><span class="n">dimension</span><span class="si">}</span><span class="s2">,</span>
<span class="s2">                </span><span class="si">{</span><span class="n">index</span><span class="si">}</span>
<span class="s2">            ) ENGINE = MergeTree ORDER BY id</span>
<span class="s2">            """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_dim</span> <span class="o">=</span> <span class="n">dimension</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">command</span><span class="p">(</span><span class="n">schema_</span><span class="p">,</span> <span class="n">settings</span><span class="o">=</span><span class="n">settings</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_table_existed</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="k">def</span> <span class="nf">_upload_batch</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">batch</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">_data</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="c1"># we assume all rows have all columns</span>
        <span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">item</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">batch</span><span class="p">):</span>
            <span class="n">_row</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">column_name</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_column_names</span><span class="p">:</span>
                <span class="n">_row</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_column_config</span><span class="p">[</span><span class="n">column_name</span><span class="p">][</span><span class="s2">"extract_func"</span><span class="p">](</span><span class="n">item</span><span class="p">))</span>
            <span class="n">_data</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">_row</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_config</span><span class="o">.</span><span class="n">database</span><span class="si">}</span><span class="s2">.</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_config</span><span class="o">.</span><span class="n">table</span><span class="si">}</span><span class="s2">"</span><span class="p">,</span>
            <span class="n">data</span><span class="o">=</span><span class="n">_data</span><span class="p">,</span>
            <span class="n">column_names</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_column_names</span><span class="p">,</span>
            <span class="n">column_type_names</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_column_type_names</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_build_text_search_statement</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">similarity_top_k</span><span class="p">:</span> <span class="nb">int</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="c1"># TODO: We could make this overridable</span>
        <span class="n">tokens</span> <span class="o">=</span> <span class="n">_default_tokenizer</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
        <span class="n">terms_pattern</span> <span class="o">=</span> <span class="p">[</span><span class="sa">f</span><span class="s2">"</span><span class="se">\\</span><span class="s2">b(?i)</span><span class="si">{</span><span class="n">x</span><span class="si">}</span><span class="se">\\</span><span class="s2">b"</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">tokens</span><span class="p">]</span>
        <span class="n">column_keys</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_column_config</span><span class="o">.</span><span class="n">keys</span><span class="p">()</span>
        <span class="k">return</span> <span class="p">(</span>
            <span class="sa">f</span><span class="s2">"SELECT </span><span class="si">{</span><span class="s1">','</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="nb">filter</span><span class="p">(</span><span class="k">lambda</span><span class="w"> </span><span class="n">k</span><span class="p">:</span><span class="w"> </span><span class="n">k</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="s1">'vector'</span><span class="p">,</span><span class="w"> </span><span class="n">column_keys</span><span class="p">))</span><span class="si">}</span><span class="s2">, "</span>
            <span class="sa">f</span><span class="s2">"score FROM </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_config</span><span class="o">.</span><span class="n">database</span><span class="si">}</span><span class="s2">.</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_config</span><span class="o">.</span><span class="n">table</span><span class="si">}</span><span class="s2"> WHERE score &gt; 0 "</span>
            <span class="sa">f</span><span class="s2">"ORDER BY length(multiMatchAllIndices(text, </span><span class="si">{</span><span class="n">terms_pattern</span><span class="si">}</span><span class="s2">)) "</span>
            <span class="sa">f</span><span class="s2">"AS score DESC, "</span>
            <span class="sa">f</span><span class="s2">"log(1 + countMatches(text, '</span><span class="se">\\</span><span class="s2">b(?i)(</span><span class="si">{</span><span class="s1">'|'</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">tokens</span><span class="p">)</span><span class="si">}</span><span class="s2">)</span><span class="se">\\</span><span class="s2">b')) "</span>
            <span class="sa">f</span><span class="s2">"AS d2 DESC limit </span><span class="si">{</span><span class="n">similarity_top_k</span><span class="si">}</span><span class="s2">"</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_build_hybrid_search_statement</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">stage_one_sql</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">query_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">similarity_top_k</span><span class="p">:</span> <span class="nb">int</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="c1"># TODO: We could make this overridable</span>
        <span class="n">tokens</span> <span class="o">=</span> <span class="n">_default_tokenizer</span><span class="p">(</span><span class="n">query_str</span><span class="p">)</span>
        <span class="n">terms_pattern</span> <span class="o">=</span> <span class="p">[</span><span class="sa">f</span><span class="s2">"</span><span class="se">\\</span><span class="s2">b(?i)</span><span class="si">{</span><span class="n">x</span><span class="si">}</span><span class="se">\\</span><span class="s2">b"</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">tokens</span><span class="p">]</span>
        <span class="n">column_keys</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_column_config</span><span class="o">.</span><span class="n">keys</span><span class="p">()</span>
        <span class="k">return</span> <span class="p">(</span>
            <span class="sa">f</span><span class="s2">"SELECT </span><span class="si">{</span><span class="s1">','</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="nb">filter</span><span class="p">(</span><span class="k">lambda</span><span class="w"> </span><span class="n">k</span><span class="p">:</span><span class="w"> </span><span class="n">k</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="s1">'vector'</span><span class="p">,</span><span class="w"> </span><span class="n">column_keys</span><span class="p">))</span><span class="si">}</span><span class="s2">, "</span>
            <span class="sa">f</span><span class="s2">"score FROM (</span><span class="si">{</span><span class="n">stage_one_sql</span><span class="si">}</span><span class="s2">) tempt "</span>
            <span class="sa">f</span><span class="s2">"ORDER BY length(multiMatchAllIndices(text, </span><span class="si">{</span><span class="n">terms_pattern</span><span class="si">}</span><span class="s2">)) "</span>
            <span class="sa">f</span><span class="s2">"AS d1 DESC, "</span>
            <span class="sa">f</span><span class="s2">"log(1 + countMatches(text, '</span><span class="se">\\\\</span><span class="s2">b(?i)(</span><span class="si">{</span><span class="s1">'|'</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">tokens</span><span class="p">)</span><span class="si">}</span><span class="s2">)</span><span class="se">\\\\</span><span class="s2">b')) "</span>
            <span class="sa">f</span><span class="s2">"AS d2 DESC limit </span><span class="si">{</span><span class="n">similarity_top_k</span><span class="si">}</span><span class="s2">"</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">_append_meta_filter_condition</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">where_str</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">exact_match_filter</span><span class="p">:</span> <span class="nb">list</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">filter_str</span> <span class="o">=</span> <span class="s2">" AND "</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"JSONExtractString("</span>
            <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">metadata_column</span><span class="si">}</span><span class="s2">, '</span><span class="si">{</span><span class="n">filter_item</span><span class="o">.</span><span class="n">key</span><span class="si">}</span><span class="s2">') "</span>
            <span class="sa">f</span><span class="s2">"= '</span><span class="si">{</span><span class="n">filter_item</span><span class="o">.</span><span class="n">value</span><span class="si">}</span><span class="s2">'"</span>
            <span class="k">for</span> <span class="n">filter_item</span> <span class="ow">in</span> <span class="n">exact_match_filter</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="n">where_str</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">where_str</span> <span class="o">=</span> <span class="n">filter_str</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">where_str</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">where_str</span><span class="si">}</span><span class="s2"> AND "</span> <span class="o">+</span> <span class="n">filter_str</span>
        <span class="k">return</span> <span class="n">where_str</span>

    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Add nodes to index.</span>

<span class="sd">        Args:</span>
<span class="sd">            nodes: List[BaseNode]: list of nodes with embeddings</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">[]</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_table_existed</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">create_table</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">nodes</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">get_embedding</span><span class="p">()))</span>

        <span class="k">for</span> <span class="n">batch</span> <span class="ow">in</span> <span class="n">iter_batch</span><span class="p">(</span><span class="n">nodes</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_config</span><span class="o">.</span><span class="n">batch_size</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_upload_batch</span><span class="p">(</span><span class="n">batch</span><span class="o">=</span><span class="n">batch</span><span class="p">)</span>

        <span class="k">return</span> <span class="p">[</span><span class="n">result</span><span class="o">.</span><span class="n">node_id</span> <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Delete nodes using with ref_doc_id.</span>

<span class="sd">        Args:</span>
<span class="sd">            ref_doc_id (str): The doc_id of the document to delete.</span>
<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">command</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"DELETE FROM </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_config</span><span class="o">.</span><span class="n">database</span><span class="si">}</span><span class="s2">.</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_config</span><span class="o">.</span><span class="n">table</span><span class="si">}</span><span class="s2"> WHERE doc_id='</span><span class="si">{</span><span class="n">ref_doc_id</span><span class="si">}</span><span class="s2">'"</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">drop</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Drop ClickHouse table."""</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">command</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"DROP TABLE IF EXISTS </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_config</span><span class="o">.</span><span class="n">database</span><span class="si">}</span><span class="s2">.</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_config</span><span class="o">.</span><span class="n">table</span><span class="si">}</span><span class="s2">"</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="n">where</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Query index for top k most similar nodes.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (VectorStoreQuery): query</span>
<span class="sd">            where (str): additional where filter</span>
<span class="sd">        """</span>
        <span class="n">query_embedding</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">],</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">)</span>
        <span class="n">where_str</span> <span class="o">=</span> <span class="n">where</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">doc_ids</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">where_str</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">where_str</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"</span><span class="si">{</span><span class="n">where_str</span><span class="si">}</span><span class="s2"> AND </span><span class="si">{</span><span class="sa">f</span><span class="s1">'doc_id IN </span><span class="si">{</span><span class="n">format_list_to_string</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">doc_ids</span><span class="p">)</span><span class="si">}</span><span class="s1">'</span><span class="si">}</span><span class="s2">"</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">where_str</span> <span class="o">=</span> <span class="sa">f</span><span class="s2">"doc_id IN </span><span class="si">{</span><span class="n">format_list_to_string</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">doc_ids</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span>

        <span class="c1"># TODO: Support other filter types</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="o">.</span><span class="n">legacy_filters</span><span class="p">())</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">where_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_append_meta_filter_condition</span><span class="p">(</span>
                <span class="n">where_str</span><span class="p">,</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="o">.</span><span class="n">legacy_filters</span><span class="p">()</span>
            <span class="p">)</span>

        <span class="c1"># build query sql</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="o"></span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">HYBRID</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">query_str</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">amplify_ratio</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">AMPLIFY_RATIO_LE5</span>
                <span class="k">if</span> <span class="mi">5</span> <span class="o">&lt;</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span> <span class="o">&lt;</span> <span class="mi">50</span><span class="p">:</span>
                    <span class="n">amplify_ratio</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">AMPLIFY_RATIO_GT5</span>
                <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span> <span class="o">&gt;</span> <span class="mi">50</span><span class="p">:</span>
                    <span class="n">amplify_ratio</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">AMPLIFY_RATIO_GT50</span>
                <span class="n">query_statement</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_hybrid_search_statement</span><span class="p">(</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_config</span><span class="o">.</span><span class="n">build_query_statement</span><span class="p">(</span>
                        <span class="n">query_embed</span><span class="o">=</span><span class="n">query_embedding</span><span class="p">,</span>
                        <span class="n">where_str</span><span class="o">=</span><span class="n">where_str</span><span class="p">,</span>
                        <span class="n">limit</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span> <span class="o">*</span> <span class="n">amplify_ratio</span><span class="p">,</span>
                    <span class="p">),</span>
                    <span class="n">query</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
                    <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
                <span class="p">)</span>
                <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"hybrid query_statement=</span><span class="si">{</span><span class="n">query_statement</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"query_str must be specified for a hybrid query."</span><span class="p">)</span>
        <span class="k">elif</span> <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="o"></span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">DEFAULT</span><span class="p">:</span>
        <span class="n">query_statement</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_config</span><span class="o">.</span><span class="n">build_query_statement</span><span class="p">(</span>
            <span class="n">query_embed</span><span class="o">=</span><span class="n">query_embedding</span><span class="p">,</span>
            <span class="n">where_str</span><span class="o">=</span><span class="n">where_str</span><span class="p">,</span>
            <span class="n">limit</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="k">elif</span> <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="o"></span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">TEXT_SEARCH</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">query_str</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">query_statement</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_build_text_search_statement</span><span class="p">(</span>
                <span class="n">query</span><span class="o">.</span><span class="n">query_str</span><span class="p">,</span>
                <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="n">logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span><span class="sa">f</span><span class="s2">"text query_statement=</span><span class="si">{</span><span class="n">query_statement</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"query_str must be specified for a text query."</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"query mode </span><span class="si">{</span><span class="n">query</span><span class="o">.</span><span class="n">mode</span><span class="si">!s}</span><span class="s2"> not supported"</span><span class="p">)</span>
    <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">similarities</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="n">query_statement</span><span class="p">)</span>
    <span class="n">column_names</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">column_names</span>
    <span class="n">id_idx</span> <span class="o">=</span> <span class="n">column_names</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s2">"id"</span><span class="p">)</span>
    <span class="n">text_idx</span> <span class="o">=</span> <span class="n">column_names</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s2">"text"</span><span class="p">)</span>
    <span class="n">metadata_idx</span> <span class="o">=</span> <span class="n">column_names</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s2">"metadata"</span><span class="p">)</span>
    <span class="n">node_info_idx</span> <span class="o">=</span> <span class="n">column_names</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s2">"node_info"</span><span class="p">)</span>
    <span class="n">score_idx</span> <span class="o">=</span> <span class="n">column_names</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s2">"score"</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">result_rows</span><span class="p">:</span>
        <span class="n">start_char_idx</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="n">end_char_idx</span> <span class="o">=</span> <span class="kc">None</span>

        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">r</span><span class="p">[</span><span class="n">node_info_idx</span><span class="p">],</span> <span class="nb">dict</span><span class="p">):</span>
            <span class="n">start_char_idx</span> <span class="o">=</span> <span class="n">r</span><span class="p">[</span><span class="n">node_info_idx</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"start"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
            <span class="n">end_char_idx</span> <span class="o">=</span> <span class="n">r</span><span class="p">[</span><span class="n">node_info_idx</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"end"</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
        <span class="n">node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span>
            <span class="n">id_</span><span class="o">=</span><span class="n">r</span><span class="p">[</span><span class="n">id_idx</span><span class="p">],</span>
            <span class="n">text</span><span class="o">=</span><span class="n">r</span><span class="p">[</span><span class="n">text_idx</span><span class="p">],</span>
            <span class="n">metadata</span><span class="o">=</span><span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">r</span><span class="p">[</span><span class="n">metadata_idx</span><span class="p">]),</span>
            <span class="n">start_char_idx</span><span class="o">=</span><span class="n">start_char_idx</span><span class="p">,</span>
            <span class="n">end_char_idx</span><span class="o">=</span><span class="n">end_char_idx</span><span class="p">,</span>
            <span class="n">relationships</span><span class="o">=</span><span class="p">{</span>
                <span class="n">NodeRelationship</span><span class="o">.</span><span class="n">SOURCE</span><span class="p">:</span> <span class="n">RelatedNodeInfo</span><span class="p">(</span><span class="n">node_id</span><span class="o">=</span><span class="n">r</span><span class="p">[</span><span class="n">id_idx</span><span class="p">])</span>
            <span class="p">},</span>
        <span class="p">)</span>

        <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
        <span class="n">similarities</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">r</span><span class="p">[</span><span class="n">score_idx</span><span class="p">])</span>
        <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">r</span><span class="p">[</span><span class="n">id_idx</span><span class="p">])</span>
    <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span><span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span> <span class="n">similarities</span><span class="o">=</span><span class="n">similarities</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">ids</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Chroma](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/chroma/)[Next Couchbase](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/couchbase/)
