Title: Neo4jvector - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/neo4jvector/

Markdown Content:
Neo4jvector - LlamaIndex


Neo4jVectorStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/neo4jvector/#llama_index.vector_stores.neo4jvector.Neo4jVectorStore "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")`

Neo4j Vector Store.

**Examples:**

`pip install llama-index-vector-stores-neo4jvector`

```
from llama_index.vector_stores.neo4jvector import Neo4jVectorStore

username = "neo4j"
password = "pleaseletmein"
url = "bolt://localhost:7687"
embed_dim = 1536

neo4j_vector = Neo4jVectorStore(username, password, url, embed_dim)
```

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-neo4jvector/llama_index/vector_stores/neo4jvector/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">183</span>
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
<span class="normal">529</span>
<span class="normal">530</span>
<span class="normal">531</span>
<span class="normal">532</span>
<span class="normal">533</span>
<span class="normal">534</span>
<span class="normal">535</span>
<span class="normal">536</span>
<span class="normal">537</span>
<span class="normal">538</span>
<span class="normal">539</span>
<span class="normal">540</span>
<span class="normal">541</span>
<span class="normal">542</span>
<span class="normal">543</span>
<span class="normal">544</span>
<span class="normal">545</span>
<span class="normal">546</span>
<span class="normal">547</span>
<span class="normal">548</span>
<span class="normal">549</span>
<span class="normal">550</span>
<span class="normal">551</span>
<span class="normal">552</span>
<span class="normal">553</span>
<span class="normal">554</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">Neo4jVectorStore</span><span class="p">(</span><span class="n">BasePydanticVectorStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Neo4j Vector Store.</span>

<span class="sd">    Examples:</span>
<span class="sd">        `pip install llama-index-vector-stores-neo4jvector`</span>


<span class="sd">        ```python</span>
<span class="sd">        from llama_index.vector_stores.neo4jvector import Neo4jVectorStore</span>

<span class="sd">        username = "neo4j"</span>
<span class="sd">        password = "pleaseletmein"</span>
<span class="sd">        url = "bolt://localhost:7687"</span>
<span class="sd">        embed_dim = 1536</span>

<span class="sd">        neo4j_vector = Neo4jVectorStore(username, password, url, embed_dim)</span>
<span class="sd">        ```</span>
<span class="sd">    """</span>

    <span class="n">stores_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">flat_metadata</span> <span class="o">=</span> <span class="kc">True</span>

    <span class="n">distance_strategy</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">index_name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">keyword_index_name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">hybrid_search</span><span class="p">:</span> <span class="nb">bool</span>
    <span class="n">node_label</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">embedding_node_property</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">text_node_property</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">retrieval_query</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">embedding_dimension</span><span class="p">:</span> <span class="nb">int</span>

    <span class="n">_driver</span><span class="p">:</span> <span class="n">neo4j</span><span class="o">.</span><span class="n">GraphDatabase</span><span class="o">.</span><span class="n">driver</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_database</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_support_metadata_filter</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_is_enterprise</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">username</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">password</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span>
        <span class="n">embedding_dimension</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span>
        <span class="n">database</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"neo4j"</span><span class="p">,</span>
        <span class="n">index_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"vector"</span><span class="p">,</span>
        <span class="n">keyword_index_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"keyword"</span><span class="p">,</span>
        <span class="n">node_label</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"Chunk"</span><span class="p">,</span>
        <span class="n">embedding_node_property</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"embedding"</span><span class="p">,</span>
        <span class="n">text_node_property</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"text"</span><span class="p">,</span>
        <span class="n">distance_strategy</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">"cosine"</span><span class="p">,</span>
        <span class="n">hybrid_search</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">retrieval_query</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s2">""</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">distance_strategy</span><span class="o">=</span><span class="n">distance_strategy</span><span class="p">,</span>
            <span class="n">index_name</span><span class="o">=</span><span class="n">index_name</span><span class="p">,</span>
            <span class="n">keyword_index_name</span><span class="o">=</span><span class="n">keyword_index_name</span><span class="p">,</span>
            <span class="n">hybrid_search</span><span class="o">=</span><span class="n">hybrid_search</span><span class="p">,</span>
            <span class="n">node_label</span><span class="o">=</span><span class="n">node_label</span><span class="p">,</span>
            <span class="n">embedding_node_property</span><span class="o">=</span><span class="n">embedding_node_property</span><span class="p">,</span>
            <span class="n">text_node_property</span><span class="o">=</span><span class="n">text_node_property</span><span class="p">,</span>
            <span class="n">retrieval_query</span><span class="o">=</span><span class="n">retrieval_query</span><span class="p">,</span>
            <span class="n">embedding_dimension</span><span class="o">=</span><span class="n">embedding_dimension</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="k">if</span> <span class="n">distance_strategy</span> <span class="ow">not</span> <span class="ow">in</span> <span class="p">[</span><span class="s2">"cosine"</span><span class="p">,</span> <span class="s2">"euclidean"</span><span class="p">]:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"distance_strategy must be either 'euclidean' or 'cosine'"</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span> <span class="o">=</span> <span class="n">neo4j</span><span class="o">.</span><span class="n">GraphDatabase</span><span class="o">.</span><span class="n">driver</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">auth</span><span class="o">=</span><span class="p">(</span><span class="n">username</span><span class="p">,</span> <span class="n">password</span><span class="p">))</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_database</span> <span class="o">=</span> <span class="n">database</span>

        <span class="c1"># Verify connection</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span><span class="o">.</span><span class="n">verify_connectivity</span><span class="p">()</span>
        <span class="k">except</span> <span class="n">neo4j</span><span class="o">.</span><span class="n">exceptions</span><span class="o">.</span><span class="n">ServiceUnavailable</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Could not connect to Neo4j database. "</span>
                <span class="s2">"Please ensure that the url is correct"</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="n">neo4j</span><span class="o">.</span><span class="n">exceptions</span><span class="o">.</span><span class="n">AuthError</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Could not connect to Neo4j database. "</span>
                <span class="s2">"Please ensure that the username and password are correct"</span>
            <span class="p">)</span>

        <span class="c1"># Verify if the version support vector index</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_verify_version</span><span class="p">()</span>

        <span class="c1"># Verify that required values are not null</span>
        <span class="n">check_if_not_null</span><span class="p">(</span>
            <span class="p">[</span>
                <span class="s2">"index_name"</span><span class="p">,</span>
                <span class="s2">"node_label"</span><span class="p">,</span>
                <span class="s2">"embedding_node_property"</span><span class="p">,</span>
                <span class="s2">"text_node_property"</span><span class="p">,</span>
            <span class="p">],</span>
            <span class="p">[</span><span class="n">index_name</span><span class="p">,</span> <span class="n">node_label</span><span class="p">,</span> <span class="n">embedding_node_property</span><span class="p">,</span> <span class="n">text_node_property</span><span class="p">],</span>
        <span class="p">)</span>

        <span class="n">index_already_exists</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">retrieve_existing_index</span><span class="p">()</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">index_already_exists</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">create_new_index</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">hybrid_search</span><span class="p">:</span>
            <span class="n">fts_node_label</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">retrieve_existing_fts_index</span><span class="p">()</span>
            <span class="c1"># If the FTS index doesn't exist yet</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">fts_node_label</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">create_new_keyword_index</span><span class="p">()</span>
            <span class="k">else</span><span class="p">:</span>  <span class="c1"># Validate that FTS and Vector index use the same information</span>
                <span class="k">if</span> <span class="ow">not</span> <span class="n">fts_node_label</span> <span class="o"></span> <span class="s2">"enterprise"</span>

    <span class="k">def</span> <span class="nf">create_new_index</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        This method constructs a Cypher query and executes it</span>
<span class="sd">        to create a new vector index in Neo4j.</span>
<span class="sd">        """</span>
        <span class="n">index_query</span> <span class="o">=</span> <span class="p">(</span>
            <span class="s2">"CALL db.index.vector.createNodeIndex("</span>
            <span class="s2">"$index_name,"</span>
            <span class="s2">"$node_label,"</span>
            <span class="s2">"$embedding_node_property,"</span>
            <span class="s2">"toInteger($embedding_dimension),"</span>
            <span class="s2">"$similarity_metric )"</span>
        <span class="p">)</span>

        <span class="n">parameters</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"index_name"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="p">,</span>
            <span class="s2">"node_label"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">,</span>
            <span class="s2">"embedding_node_property"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">embedding_node_property</span><span class="p">,</span>
            <span class="s2">"embedding_dimension"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">embedding_dimension</span><span class="p">,</span>
            <span class="s2">"similarity_metric"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">distance_strategy</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">database_query</span><span class="p">(</span><span class="n">index_query</span><span class="p">,</span> <span class="n">params</span><span class="o">=</span><span class="n">parameters</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">retrieve_existing_index</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Check if the vector index exists in the Neo4j database</span>
<span class="sd">        and returns its embedding dimension.</span>

<span class="sd">        This method queries the Neo4j database for existing indexes</span>
<span class="sd">        and attempts to retrieve the dimension of the vector index</span>
<span class="sd">        with the specified name. If the index exists, its dimension is returned.</span>
<span class="sd">        If the index doesn't exist, `None` is returned.</span>

<span class="sd">        Returns:</span>
<span class="sd">            int or None: The embedding dimension of the existing index if found.</span>
<span class="sd">        """</span>
        <span class="n">index_information</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">database_query</span><span class="p">(</span>
            <span class="s2">"SHOW INDEXES YIELD name, type, labelsOrTypes, properties, options "</span>
            <span class="s2">"WHERE type = 'VECTOR' AND (name = $index_name "</span>
            <span class="s2">"OR (labelsOrTypes[0] = $node_label AND "</span>
            <span class="s2">"properties[0] = $embedding_node_property)) "</span>
            <span class="s2">"RETURN name, labelsOrTypes, properties, options "</span><span class="p">,</span>
            <span class="n">params</span><span class="o">=</span><span class="p">{</span>
                <span class="s2">"index_name"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="p">,</span>
                <span class="s2">"node_label"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">,</span>
                <span class="s2">"embedding_node_property"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">embedding_node_property</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">)</span>
        <span class="c1"># sort by index_name</span>
        <span class="n">index_information</span> <span class="o">=</span> <span class="n">sort_by_index_name</span><span class="p">(</span><span class="n">index_information</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">index_name</span> <span class="o">=</span> <span class="n">index_information</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">"name"</span><span class="p">]</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">node_label</span> <span class="o">=</span> <span class="n">index_information</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">"labelsOrTypes"</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">embedding_node_property</span> <span class="o">=</span> <span class="n">index_information</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">"properties"</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">embedding_dimension</span> <span class="o">=</span> <span class="n">index_information</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">"options"</span><span class="p">][</span><span class="s2">"indexConfig"</span><span class="p">][</span>
                <span class="s2">"vector.dimensions"</span>
            <span class="p">]</span>

            <span class="k">return</span> <span class="kc">True</span>
        <span class="k">except</span> <span class="ne">IndexError</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">False</span>

    <span class="k">def</span> <span class="nf">retrieve_existing_fts_index</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Check if the fulltext index exists in the Neo4j database.</span>

<span class="sd">        This method queries the Neo4j database for existing fts indexes</span>
<span class="sd">        with the specified name.</span>

<span class="sd">        Returns:</span>
<span class="sd">            (Tuple): keyword index information</span>
<span class="sd">        """</span>
        <span class="n">index_information</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">database_query</span><span class="p">(</span>
            <span class="s2">"SHOW INDEXES YIELD name, type, labelsOrTypes, properties, options "</span>
            <span class="s2">"WHERE type = 'FULLTEXT' AND (name = $keyword_index_name "</span>
            <span class="s2">"OR (labelsOrTypes = [$node_label] AND "</span>
            <span class="s2">"properties = $text_node_property)) "</span>
            <span class="s2">"RETURN name, labelsOrTypes, properties, options "</span><span class="p">,</span>
            <span class="n">params</span><span class="o">=</span><span class="p">{</span>
                <span class="s2">"keyword_index_name"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">keyword_index_name</span><span class="p">,</span>
                <span class="s2">"node_label"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">,</span>
                <span class="s2">"text_node_property"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_node_property</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">)</span>
        <span class="c1"># sort by index_name</span>
        <span class="n">index_information</span> <span class="o">=</span> <span class="n">sort_by_index_name</span><span class="p">(</span><span class="n">index_information</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">keyword_index_name</span> <span class="o">=</span> <span class="n">index_information</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">"name"</span><span class="p">]</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">text_node_property</span> <span class="o">=</span> <span class="n">index_information</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">"properties"</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span>
            <span class="k">return</span> <span class="n">index_information</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">"labelsOrTypes"</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span>
        <span class="k">except</span> <span class="ne">IndexError</span><span class="p">:</span>
            <span class="k">return</span> <span class="kc">None</span>

    <span class="k">def</span> <span class="nf">create_new_keyword_index</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text_node_properties</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">[])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        This method constructs a Cypher query and executes it</span>
<span class="sd">        to create a new full text index in Neo4j.</span>
<span class="sd">        """</span>
        <span class="n">node_props</span> <span class="o">=</span> <span class="n">text_node_properties</span> <span class="ow">or</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">text_node_property</span><span class="p">]</span>
        <span class="n">fts_index_query</span> <span class="o">=</span> <span class="p">(</span>
            <span class="sa">f</span><span class="s2">"CREATE FULLTEXT INDEX </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">keyword_index_name</span><span class="si">}</span><span class="s2"> "</span>
            <span class="sa">f</span><span class="s2">"FOR (n:`</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="si">}</span><span class="s2">`) ON EACH "</span>
            <span class="sa">f</span><span class="s2">"[</span><span class="si">{</span><span class="s1">', '</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="s1">'n.`'</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">el</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="s1">'`'</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">el</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="n">node_props</span><span class="p">])</span><span class="si">}</span><span class="s2">]"</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">database_query</span><span class="p">(</span><span class="n">fts_index_query</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">database_query</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">params</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        This method sends a Cypher query to the connected Neo4j database</span>
<span class="sd">        and returns the results as a list of dictionaries.</span>

<span class="sd">        Args:</span>
<span class="sd">            query (str): The Cypher query to execute.</span>
<span class="sd">            params (dict, optional): Dictionary of query parameters. Defaults to {}.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List[Dict[str, Any]]: List of dictionaries containing the query results.</span>
<span class="sd">        """</span>
        <span class="n">params</span> <span class="o">=</span> <span class="n">params</span> <span class="ow">or</span> <span class="p">{}</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span><span class="o">.</span><span class="n">session</span><span class="p">(</span><span class="n">database</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_database</span><span class="p">)</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">data</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">params</span><span class="p">)</span>
                <span class="k">return</span> <span class="p">[</span><span class="n">r</span><span class="o">.</span><span class="n">data</span><span class="p">()</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">data</span><span class="p">]</span>
            <span class="k">except</span> <span class="n">CypherSyntaxError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Cypher Statement is not valid</span><span class="se">\n</span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span> <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
        <span class="n">ids</span> <span class="o">=</span> <span class="p">[</span><span class="n">r</span><span class="o">.</span><span class="n">node_id</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">]</span>
        <span class="n">import_query</span> <span class="o">=</span> <span class="p">(</span>
            <span class="s2">"UNWIND $data AS row "</span>
            <span class="s2">"CALL { WITH row "</span>
            <span class="sa">f</span><span class="s2">"MERGE (c:`</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="si">}</span><span class="s2">` </span><span class="se">{{</span><span class="s2">id: row.id</span><span class="se">}}</span><span class="s2">) "</span>
            <span class="s2">"WITH c, row "</span>
            <span class="sa">f</span><span class="s2">"CALL db.create.setVectorProperty(c, "</span>
            <span class="sa">f</span><span class="s2">"'</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">embedding_node_property</span><span class="si">}</span><span class="s2">', row.embedding) "</span>
            <span class="s2">"YIELD node "</span>
            <span class="sa">f</span><span class="s2">"SET c.`</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">text_node_property</span><span class="si">}</span><span class="s2">` = row.text "</span>
            <span class="s2">"SET c += row.metadata } IN TRANSACTIONS OF 1000 ROWS"</span>
        <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">database_query</span><span class="p">(</span>
            <span class="n">import_query</span><span class="p">,</span>
            <span class="n">params</span><span class="o">=</span><span class="p">{</span><span class="s2">"data"</span><span class="p">:</span> <span class="n">clean_params</span><span class="p">(</span><span class="n">nodes</span><span class="p">)},</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="n">ids</span>

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">:</span>
            <span class="c1"># Verify that 5.18 or later is used</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_support_metadata_filter</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"Metadata filtering is only supported in "</span>
                    <span class="s2">"Neo4j version 5.18 or greater"</span>
                <span class="p">)</span>
            <span class="c1"># Metadata filtering and hybrid doesn't work</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">hybrid_search</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"Metadata filtering can't be use in combination with "</span>
                    <span class="s2">"a hybrid search approach"</span>
                <span class="p">)</span>
            <span class="n">parallel_query</span> <span class="o">=</span> <span class="p">(</span>
                <span class="s2">"CYPHER runtime = parallel parallelRuntimeSupport=all "</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_enterprise</span>
                <span class="k">else</span> <span class="s2">""</span>
            <span class="p">)</span>
            <span class="n">base_index_query</span> <span class="o">=</span> <span class="n">parallel_query</span> <span class="o">+</span> <span class="p">(</span>
                <span class="sa">f</span><span class="s2">"MATCH (n:`</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="si">}</span><span class="s2">`) WHERE "</span>
                <span class="sa">f</span><span class="s2">"n.`</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">embedding_node_property</span><span class="si">}</span><span class="s2">` IS NOT NULL AND "</span>
                <span class="sa">f</span><span class="s2">"size(n.`</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">embedding_node_property</span><span class="si">}</span><span class="s2">`) = "</span>
                <span class="sa">f</span><span class="s2">"toInteger(</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">embedding_dimension</span><span class="si">}</span><span class="s2">) AND "</span>
            <span class="p">)</span>
            <span class="n">base_cosine_query</span> <span class="o">=</span> <span class="p">(</span>
                <span class="s2">" WITH n as node, vector.similarity.cosine("</span>
                <span class="sa">f</span><span class="s2">"n.`</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">embedding_node_property</span><span class="si">}</span><span class="s2">`, "</span>
                <span class="s2">"$embedding) AS score ORDER BY score DESC LIMIT toInteger($k) "</span>
            <span class="p">)</span>
            <span class="n">filter_snippets</span><span class="p">,</span> <span class="n">filter_params</span> <span class="o">=</span> <span class="n">construct_metadata_filter</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">)</span>
            <span class="n">index_query</span> <span class="o">=</span> <span class="n">base_index_query</span> <span class="o">+</span> <span class="n">filter_snippets</span> <span class="o">+</span> <span class="n">base_cosine_query</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">index_query</span> <span class="o">=</span> <span class="n">_get_search_index_query</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">hybrid_search</span><span class="p">)</span>
            <span class="n">filter_params</span> <span class="o">=</span> <span class="p">{}</span>

        <span class="n">default_retrieval</span> <span class="o">=</span> <span class="p">(</span>
            <span class="sa">f</span><span class="s2">"RETURN node.`</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">text_node_property</span><span class="si">}</span><span class="s2">` AS text, score, "</span>
            <span class="s2">"node.id AS id, "</span>
            <span class="sa">f</span><span class="s2">"node </span><span class="se">{{</span><span class="s2">.*, `</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">text_node_property</span><span class="si">}</span><span class="s2">`: Null, "</span>
            <span class="sa">f</span><span class="s2">"`</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">embedding_node_property</span><span class="si">}</span><span class="s2">`: Null, id: Null </span><span class="se">}}</span><span class="s2"> AS metadata"</span>
        <span class="p">)</span>

        <span class="n">retrieval_query</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">retrieval_query</span> <span class="ow">or</span> <span class="n">default_retrieval</span>
        <span class="n">read_query</span> <span class="o">=</span> <span class="n">index_query</span> <span class="o">+</span> <span class="n">retrieval_query</span>

        <span class="n">parameters</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">"index"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="p">,</span>
            <span class="s2">"k"</span><span class="p">:</span> <span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
            <span class="s2">"embedding"</span><span class="p">:</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">,</span>
            <span class="s2">"keyword_index"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">keyword_index_name</span><span class="p">,</span>
            <span class="s2">"query"</span><span class="p">:</span> <span class="n">remove_lucene_chars</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">query_str</span><span class="p">),</span>
            <span class="o">**</span><span class="n">filter_params</span><span class="p">,</span>
        <span class="p">}</span>

        <span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">database_query</span><span class="p">(</span><span class="n">read_query</span><span class="p">,</span> <span class="n">params</span><span class="o">=</span><span class="n">parameters</span><span class="p">)</span>

        <span class="n">nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">similarities</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">record</span> <span class="ow">in</span> <span class="n">results</span><span class="p">:</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">metadata_dict_to_node</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"metadata"</span><span class="p">])</span>
            <span class="n">node</span><span class="o">.</span><span class="n">set_content</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"text"</span><span class="p">]))</span>
            <span class="n">nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
            <span class="n">similarities</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"score"</span><span class="p">])</span>
            <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">record</span><span class="p">[</span><span class="s2">"id"</span><span class="p">])</span>

        <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span><span class="n">nodes</span><span class="o">=</span><span class="n">nodes</span><span class="p">,</span> <span class="n">similarities</span><span class="o">=</span><span class="n">similarities</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">ids</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">database_query</span><span class="p">(</span>
            <span class="sa">f</span><span class="s2">"MATCH (n:`</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="si">}</span><span class="s2">`) WHERE n.ref_doc_id = $id DETACH DELETE n"</span><span class="p">,</span>
            <span class="n">params</span><span class="o">=</span><span class="p">{</span><span class="s2">"id"</span><span class="p">:</span> <span class="n">ref_doc_id</span><span class="p">},</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### create\_new\_index [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/neo4jvector/#llama_index.vector_stores.neo4jvector.Neo4jVectorStore.create_new_index "Permanent link")

```
create_new_index() -> None
```

This method constructs a Cypher query and executes it to create a new vector index in Neo4j.

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-neo4jvector/llama_index/vector_stores/neo4jvector/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">333</span>
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
<span class="normal">354</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">create_new_index</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    This method constructs a Cypher query and executes it</span>
<span class="sd">    to create a new vector index in Neo4j.</span>
<span class="sd">    """</span>
    <span class="n">index_query</span> <span class="o">=</span> <span class="p">(</span>
        <span class="s2">"CALL db.index.vector.createNodeIndex("</span>
        <span class="s2">"$index_name,"</span>
        <span class="s2">"$node_label,"</span>
        <span class="s2">"$embedding_node_property,"</span>
        <span class="s2">"toInteger($embedding_dimension),"</span>
        <span class="s2">"$similarity_metric )"</span>
    <span class="p">)</span>

    <span class="n">parameters</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"index_name"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="p">,</span>
        <span class="s2">"node_label"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">,</span>
        <span class="s2">"embedding_node_property"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">embedding_node_property</span><span class="p">,</span>
        <span class="s2">"embedding_dimension"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">embedding_dimension</span><span class="p">,</span>
        <span class="s2">"similarity_metric"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">distance_strategy</span><span class="p">,</span>
    <span class="p">}</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">database_query</span><span class="p">(</span><span class="n">index_query</span><span class="p">,</span> <span class="n">params</span><span class="o">=</span><span class="n">parameters</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### retrieve\_existing\_index [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/neo4jvector/#llama_index.vector_stores.neo4jvector.Neo4jVectorStore.retrieve_existing_index "Permanent link")

```
retrieve_existing_index() -> bool
```

Check if the vector index exists in the Neo4j database and returns its embedding dimension.

This method queries the Neo4j database for existing indexes and attempts to retrieve the dimension of the vector index with the specified name. If the index exists, its dimension is returned. If the index doesn't exist, `None` is returned.

**Returns:**

| Type | Description |
| --- | --- |
| `bool` | 
int or None: The embedding dimension of the existing index if found.



 |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-neo4jvector/llama_index/vector_stores/neo4jvector/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">356</span>
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
<span class="normal">393</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">retrieve_existing_index</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Check if the vector index exists in the Neo4j database</span>
<span class="sd">    and returns its embedding dimension.</span>

<span class="sd">    This method queries the Neo4j database for existing indexes</span>
<span class="sd">    and attempts to retrieve the dimension of the vector index</span>
<span class="sd">    with the specified name. If the index exists, its dimension is returned.</span>
<span class="sd">    If the index doesn't exist, `None` is returned.</span>

<span class="sd">    Returns:</span>
<span class="sd">        int or None: The embedding dimension of the existing index if found.</span>
<span class="sd">    """</span>
    <span class="n">index_information</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">database_query</span><span class="p">(</span>
        <span class="s2">"SHOW INDEXES YIELD name, type, labelsOrTypes, properties, options "</span>
        <span class="s2">"WHERE type = 'VECTOR' AND (name = $index_name "</span>
        <span class="s2">"OR (labelsOrTypes[0] = $node_label AND "</span>
        <span class="s2">"properties[0] = $embedding_node_property)) "</span>
        <span class="s2">"RETURN name, labelsOrTypes, properties, options "</span><span class="p">,</span>
        <span class="n">params</span><span class="o">=</span><span class="p">{</span>
            <span class="s2">"index_name"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="p">,</span>
            <span class="s2">"node_label"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">,</span>
            <span class="s2">"embedding_node_property"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">embedding_node_property</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">)</span>
    <span class="c1"># sort by index_name</span>
    <span class="n">index_information</span> <span class="o">=</span> <span class="n">sort_by_index_name</span><span class="p">(</span><span class="n">index_information</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="p">)</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">index_name</span> <span class="o">=</span> <span class="n">index_information</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">"name"</span><span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">node_label</span> <span class="o">=</span> <span class="n">index_information</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">"labelsOrTypes"</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">embedding_node_property</span> <span class="o">=</span> <span class="n">index_information</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">"properties"</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">embedding_dimension</span> <span class="o">=</span> <span class="n">index_information</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">"options"</span><span class="p">][</span><span class="s2">"indexConfig"</span><span class="p">][</span>
            <span class="s2">"vector.dimensions"</span>
        <span class="p">]</span>

        <span class="k">return</span> <span class="kc">True</span>
    <span class="k">except</span> <span class="ne">IndexError</span><span class="p">:</span>
        <span class="k">return</span> <span class="kc">False</span>
</code></pre></div></td></tr></tbody></table>

### retrieve\_existing\_fts\_index [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/neo4jvector/#llama_index.vector_stores.neo4jvector.Neo4jVectorStore.retrieve_existing_fts_index "Permanent link")

```
retrieve_existing_fts_index() -> Optional[str]
```

Check if the fulltext index exists in the Neo4j database.

This method queries the Neo4j database for existing fts indexes with the specified name.

**Returns:**

| Type | Description |
| --- | --- |
| `Tuple` | 
keyword index information



 |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-neo4jvector/llama_index/vector_stores/neo4jvector/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">395</span>
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
<span class="normal">423</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">retrieve_existing_fts_index</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Check if the fulltext index exists in the Neo4j database.</span>

<span class="sd">    This method queries the Neo4j database for existing fts indexes</span>
<span class="sd">    with the specified name.</span>

<span class="sd">    Returns:</span>
<span class="sd">        (Tuple): keyword index information</span>
<span class="sd">    """</span>
    <span class="n">index_information</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">database_query</span><span class="p">(</span>
        <span class="s2">"SHOW INDEXES YIELD name, type, labelsOrTypes, properties, options "</span>
        <span class="s2">"WHERE type = 'FULLTEXT' AND (name = $keyword_index_name "</span>
        <span class="s2">"OR (labelsOrTypes = [$node_label] AND "</span>
        <span class="s2">"properties = $text_node_property)) "</span>
        <span class="s2">"RETURN name, labelsOrTypes, properties, options "</span><span class="p">,</span>
        <span class="n">params</span><span class="o">=</span><span class="p">{</span>
            <span class="s2">"keyword_index_name"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">keyword_index_name</span><span class="p">,</span>
            <span class="s2">"node_label"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="p">,</span>
            <span class="s2">"text_node_property"</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_node_property</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">)</span>
    <span class="c1"># sort by index_name</span>
    <span class="n">index_information</span> <span class="o">=</span> <span class="n">sort_by_index_name</span><span class="p">(</span><span class="n">index_information</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_name</span><span class="p">)</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">keyword_index_name</span> <span class="o">=</span> <span class="n">index_information</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">"name"</span><span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">text_node_property</span> <span class="o">=</span> <span class="n">index_information</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">"properties"</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span>
        <span class="k">return</span> <span class="n">index_information</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">"labelsOrTypes"</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span>
    <span class="k">except</span> <span class="ne">IndexError</span><span class="p">:</span>
        <span class="k">return</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table>

### create\_new\_keyword\_index [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/neo4jvector/#llama_index.vector_stores.neo4jvector.Neo4jVectorStore.create_new_keyword_index "Permanent link")

```
create_new_keyword_index(text_node_properties: List[str] = []) -> None
```

This method constructs a Cypher query and executes it to create a new full text index in Neo4j.

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-neo4jvector/llama_index/vector_stores/neo4jvector/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">425</span>
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
<span class="normal">436</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">create_new_keyword_index</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text_node_properties</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">[])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    This method constructs a Cypher query and executes it</span>
<span class="sd">    to create a new full text index in Neo4j.</span>
<span class="sd">    """</span>
    <span class="n">node_props</span> <span class="o">=</span> <span class="n">text_node_properties</span> <span class="ow">or</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">text_node_property</span><span class="p">]</span>
    <span class="n">fts_index_query</span> <span class="o">=</span> <span class="p">(</span>
        <span class="sa">f</span><span class="s2">"CREATE FULLTEXT INDEX </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">keyword_index_name</span><span class="si">}</span><span class="s2"> "</span>
        <span class="sa">f</span><span class="s2">"FOR (n:`</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">node_label</span><span class="si">}</span><span class="s2">`) ON EACH "</span>
        <span class="sa">f</span><span class="s2">"[</span><span class="si">{</span><span class="s1">', '</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="s1">'n.`'</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">el</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="s1">'`'</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">el</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="n">node_props</span><span class="p">])</span><span class="si">}</span><span class="s2">]"</span>
    <span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">database_query</span><span class="p">(</span><span class="n">fts_index_query</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### database\_query [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/neo4jvector/#llama_index.vector_stores.neo4jvector.Neo4jVectorStore.database_query "Permanent link")

```
database_query(query: str, params: Optional[dict] = None) -> List[Dict[str, Any]]
```

This method sends a Cypher query to the connected Neo4j database and returns the results as a list of dictionaries.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `query` | `str` | 
The Cypher query to execute.



 | _required_ |
| `params` | `dict` | 

Dictionary of query parameters. Defaults to {}.



 | `None` |

**Returns:**

| Type | Description |
| --- | --- |
| `List[Dict[str, Any]]` | 
List\[Dict\[str, Any\]\]: List of dictionaries containing the query results.



 |

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-neo4jvector/llama_index/vector_stores/neo4jvector/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">438</span>
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
<span class="normal">458</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">database_query</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">params</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    This method sends a Cypher query to the connected Neo4j database</span>
<span class="sd">    and returns the results as a list of dictionaries.</span>

<span class="sd">    Args:</span>
<span class="sd">        query (str): The Cypher query to execute.</span>
<span class="sd">        params (dict, optional): Dictionary of query parameters. Defaults to {}.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List[Dict[str, Any]]: List of dictionaries containing the query results.</span>
<span class="sd">    """</span>
    <span class="n">params</span> <span class="o">=</span> <span class="n">params</span> <span class="ow">or</span> <span class="p">{}</span>
    <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_driver</span><span class="o">.</span><span class="n">session</span><span class="p">(</span><span class="n">database</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_database</span><span class="p">)</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">data</span> <span class="o">=</span> <span class="n">session</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">params</span><span class="p">)</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">r</span><span class="o">.</span><span class="n">data</span><span class="p">()</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">data</span><span class="p">]</span>
        <span class="k">except</span> <span class="n">CypherSyntaxError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Cypher Statement is not valid</span><span class="se">\n</span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Myscale](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/myscale/)[Next Neptune](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/neptune/)
