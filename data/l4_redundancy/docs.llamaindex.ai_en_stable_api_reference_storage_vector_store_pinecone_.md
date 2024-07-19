Title: Pinecone - LlamaIndex

URL Source: https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/pinecone/

Markdown Content:
Pinecone - LlamaIndex


PineconeVectorStore [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/pinecone/#llama_index.vector_stores.pinecone.PineconeVectorStore "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bases: `[BasePydanticVectorStore](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/#llama_index.core.vector_stores.types.BasePydanticVectorStore "llama_index.core.vector_stores.types.BasePydanticVectorStore")`

Pinecone Vector Store.

In this vector store, embeddings and docs are stored within a Pinecone index.

During query time, the index uses Pinecone to query for the top k most similar nodes.

**Parameters:**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `pinecone_index` | `Optional[Union[Index, Index]]` | 
Pinecone index instance,



 | `None` |
| `insert_kwargs` | `Optional[Dict]` | 

insert kwargs during `upsert` call.



 | `None` |
| `add_sparse_vector` | `bool` | 

whether to add sparse vector to index.



 | `False` |
| `tokenizer` | `Optional[Callable]` | 

tokenizer to use to generate sparse



 | `None` |
| `default_empty_query_vector` | `Optional[List[float]]` | 

default empty query vector. Defaults to None. If not None, then this vector will be used as the query vector if the query is empty.



 | `None` |

**Examples:**

`pip install llama-index-vector-stores-pinecone`

```
import os
from llama_index.vector_stores.pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec

# Set up Pinecone API key
os.environ["PINECONE_API_KEY"] = "<Your Pinecone API key, from app.pinecone.io>"
api_key = os.environ["PINECONE_API_KEY"]

# Create Pinecone Vector Store
pc = Pinecone(api_key=api_key)

pc.create_index(
    name="quickstart",
    dimension=1536,
    metric="dotproduct",
    spec=ServerlessSpec(cloud="aws", region="us-west-2"),
)

pinecone_index = pc.Index("quickstart")

vector_store = PineconeVectorStore(
    pinecone_index=pinecone_index,
)
```

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-pinecone/llama_index/vector_stores/pinecone/base.py`

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
<span class="normal">516</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">class</span> <span class="nc">PineconeVectorStore</span><span class="p">(</span><span class="n">BasePydanticVectorStore</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Pinecone Vector Store.</span>

<span class="sd">    In this vector store, embeddings and docs are stored within a</span>
<span class="sd">    Pinecone index.</span>

<span class="sd">    During query time, the index uses Pinecone to query for the top</span>
<span class="sd">    k most similar nodes.</span>

<span class="sd">    Args:</span>
<span class="sd">        pinecone_index (Optional[Union[pinecone.Pinecone.Index, pinecone.Index]]): Pinecone index instance,</span>
<span class="sd">        pinecone.Pinecone.Index for clients &gt;= 3.0.0; pinecone.Index for older clients.</span>
<span class="sd">        insert_kwargs (Optional[Dict]): insert kwargs during `upsert` call.</span>
<span class="sd">        add_sparse_vector (bool): whether to add sparse vector to index.</span>
<span class="sd">        tokenizer (Optional[Callable]): tokenizer to use to generate sparse</span>
<span class="sd">        default_empty_query_vector (Optional[List[float]]): default empty query vector.</span>
<span class="sd">            Defaults to None. If not None, then this vector will be used as the query</span>
<span class="sd">            vector if the query is empty.</span>

<span class="sd">    Examples:</span>
<span class="sd">        `pip install llama-index-vector-stores-pinecone`</span>

<span class="sd">        ```python</span>
<span class="sd">        import os</span>
<span class="sd">        from llama_index.vector_stores.pinecone import PineconeVectorStore</span>
<span class="sd">        from pinecone import Pinecone, ServerlessSpec</span>

<span class="sd">        # Set up Pinecone API key</span>
<span class="sd">        os.environ["PINECONE_API_KEY"] = "&lt;Your Pinecone API key, from app.pinecone.io&gt;"</span>
<span class="sd">        api_key = os.environ["PINECONE_API_KEY"]</span>

<span class="sd">        # Create Pinecone Vector Store</span>
<span class="sd">        pc = Pinecone(api_key=api_key)</span>

<span class="sd">        pc.create_index(</span>
<span class="sd">            name="quickstart",</span>
<span class="sd">            dimension=1536,</span>
<span class="sd">            metric="dotproduct",</span>
<span class="sd">            spec=ServerlessSpec(cloud="aws", region="us-west-2"),</span>
<span class="sd">        )</span>

<span class="sd">        pinecone_index = pc.Index("quickstart")</span>

<span class="sd">        vector_store = PineconeVectorStore(</span>
<span class="sd">            pinecone_index=pinecone_index,</span>
<span class="sd">        )</span>
<span class="sd">        ```</span>
<span class="sd">    """</span>

    <span class="n">stores_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">flat_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>

    <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
    <span class="n">index_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
    <span class="n">environment</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
    <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
    <span class="n">insert_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span>
    <span class="n">add_sparse_vector</span><span class="p">:</span> <span class="nb">bool</span>
    <span class="n">text_key</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">remove_text_from_metadata</span><span class="p">:</span> <span class="nb">bool</span>

    <span class="n">_pinecone_index</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>
    <span class="n">_tokenizer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="n">PrivateAttr</span><span class="p">()</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">pinecone_index</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span>
            <span class="n">Any</span>
        <span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>  <span class="c1"># Dynamic import prevents specific type hinting here</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">index_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">environment</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">insert_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">add_sparse_vector</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">tokenizer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">text_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_TEXT_KEY</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_BATCH_SIZE</span><span class="p">,</span>
        <span class="n">remove_text_from_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">default_empty_query_vector</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">insert_kwargs</span> <span class="o">=</span> <span class="n">insert_kwargs</span> <span class="ow">or</span> <span class="p">{}</span>

        <span class="k">if</span> <span class="n">tokenizer</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">add_sparse_vector</span><span class="p">:</span>
            <span class="n">tokenizer</span> <span class="o">=</span> <span class="n">get_default_tokenizer</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_tokenizer</span> <span class="o">=</span> <span class="n">tokenizer</span>

        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span>
            <span class="n">index_name</span><span class="o">=</span><span class="n">index_name</span><span class="p">,</span>
            <span class="n">environment</span><span class="o">=</span><span class="n">environment</span><span class="p">,</span>
            <span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span>
            <span class="n">namespace</span><span class="o">=</span><span class="n">namespace</span><span class="p">,</span>
            <span class="n">insert_kwargs</span><span class="o">=</span><span class="n">insert_kwargs</span><span class="p">,</span>
            <span class="n">add_sparse_vector</span><span class="o">=</span><span class="n">add_sparse_vector</span><span class="p">,</span>
            <span class="n">text_key</span><span class="o">=</span><span class="n">text_key</span><span class="p">,</span>
            <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span>
            <span class="n">remove_text_from_metadata</span><span class="o">=</span><span class="n">remove_text_from_metadata</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="c1"># TODO: Make following instance check stronger -- check if pinecone_index is not pinecone.Index, else raise</span>
        <span class="c1">#  ValueError</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">pinecone_index</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"`pinecone_index` cannot be of type `str`; should be an instance of pinecone.Index, "</span>
            <span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_pinecone_index</span> <span class="o">=</span> <span class="n">pinecone_index</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_initialize_pinecone_client</span><span class="p">(</span>
            <span class="n">api_key</span><span class="p">,</span> <span class="n">index_name</span><span class="p">,</span> <span class="n">environment</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">_initialize_pinecone_client</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">index_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="n">environment</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Initialize Pinecone client based on version.</span>

<span class="sd">        If client version &lt;3.0.0, use pods-based initialization; else, use serverless initialization.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">index_name</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"`index_name` is required for Pinecone client initialization"</span>
            <span class="p">)</span>

        <span class="n">pinecone</span> <span class="o">=</span> <span class="n">_import_pinecone</span><span class="p">()</span>

        <span class="k">if</span> <span class="p">(</span>
            <span class="ow">not</span> <span class="n">_is_pinecone_v3</span><span class="p">()</span>
        <span class="p">):</span>  <span class="c1"># If old version of Pinecone client (version bifurcation temporary):</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">environment</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"environment is required for Pinecone client &lt; 3.0.0"</span><span class="p">)</span>
            <span class="n">pinecone</span><span class="o">.</span><span class="n">init</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span> <span class="n">environment</span><span class="o">=</span><span class="n">environment</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">pinecone</span><span class="o">.</span><span class="n">Index</span><span class="p">(</span><span class="n">index_name</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>  <span class="c1"># If new version of Pinecone client (serverless):</span>
            <span class="n">pinecone_instance</span> <span class="o">=</span> <span class="n">pinecone</span><span class="o">.</span><span class="n">Pinecone</span><span class="p">(</span>
                <span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span> <span class="n">source_tag</span><span class="o">=</span><span class="s2">"llamaindex"</span>
            <span class="p">)</span>
            <span class="k">return</span> <span class="n">pinecone_instance</span><span class="o">.</span><span class="n">Index</span><span class="p">(</span><span class="n">index_name</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">from_params</span><span class="p">(</span>
        <span class="bp">cls</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">index_name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">environment</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">namespace</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">insert_kwargs</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">add_sparse_vector</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">tokenizer</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">text_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_TEXT_KEY</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">DEFAULT_BATCH_SIZE</span><span class="p">,</span>
        <span class="n">remove_text_from_metadata</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">default_empty_query_vector</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="s2">"PineconeVectorStore"</span><span class="p">:</span>
        <span class="n">pinecone_index</span> <span class="o">=</span> <span class="bp">cls</span><span class="o">.</span><span class="n">_initialize_pinecone_client</span><span class="p">(</span>
            <span class="n">api_key</span><span class="p">,</span> <span class="n">index_name</span><span class="p">,</span> <span class="n">environment</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span>
        <span class="p">)</span>

        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
            <span class="n">pinecone_index</span><span class="o">=</span><span class="n">pinecone_index</span><span class="p">,</span>
            <span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span>
            <span class="n">index_name</span><span class="o">=</span><span class="n">index_name</span><span class="p">,</span>
            <span class="n">environment</span><span class="o">=</span><span class="n">environment</span><span class="p">,</span>
            <span class="n">namespace</span><span class="o">=</span><span class="n">namespace</span><span class="p">,</span>
            <span class="n">insert_kwargs</span><span class="o">=</span><span class="n">insert_kwargs</span><span class="p">,</span>
            <span class="n">add_sparse_vector</span><span class="o">=</span><span class="n">add_sparse_vector</span><span class="p">,</span>
            <span class="n">tokenizer</span><span class="o">=</span><span class="n">tokenizer</span><span class="p">,</span>
            <span class="n">text_key</span><span class="o">=</span><span class="n">text_key</span><span class="p">,</span>
            <span class="n">batch_size</span><span class="o">=</span><span class="n">batch_size</span><span class="p">,</span>
            <span class="n">remove_text_from_metadata</span><span class="o">=</span><span class="n">remove_text_from_metadata</span><span class="p">,</span>
            <span class="n">default_empty_query_vector</span><span class="o">=</span><span class="n">default_empty_query_vector</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">class_name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"PinconeVectorStore"</span>

    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
        <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Add nodes to index.</span>

<span class="sd">        Args:</span>
<span class="sd">            nodes: List[BaseNode]: list of nodes with embeddings</span>

<span class="sd">        """</span>
        <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">entries</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="n">node_id</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">node_id</span>

            <span class="n">metadata</span> <span class="o">=</span> <span class="n">node_to_metadata_dict</span><span class="p">(</span>
                <span class="n">node</span><span class="p">,</span>
                <span class="n">remove_text</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">remove_text_from_metadata</span><span class="p">,</span>
                <span class="n">flat_metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">flat_metadata</span><span class="p">,</span>
            <span class="p">)</span>

            <span class="n">entry</span> <span class="o">=</span> <span class="p">{</span>
                <span class="n">ID_KEY</span><span class="p">:</span> <span class="n">node_id</span><span class="p">,</span>
                <span class="n">VECTOR_KEY</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">get_embedding</span><span class="p">(),</span>
                <span class="n">METADATA_KEY</span><span class="p">:</span> <span class="n">metadata</span><span class="p">,</span>
            <span class="p">}</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">add_sparse_vector</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tokenizer</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">sparse_vector</span> <span class="o">=</span> <span class="n">generate_sparse_vectors</span><span class="p">(</span>
                    <span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">EMBED</span><span class="p">)],</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_tokenizer</span><span class="p">,</span>
                <span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
                <span class="n">entry</span><span class="p">[</span><span class="n">SPARSE_VECTOR_KEY</span><span class="p">]</span> <span class="o">=</span> <span class="n">sparse_vector</span>

            <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node_id</span><span class="p">)</span>
            <span class="n">entries</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">entry</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_pinecone_index</span><span class="o">.</span><span class="n">upsert</span><span class="p">(</span>
            <span class="n">entries</span><span class="p">,</span>
            <span class="n">namespace</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">namespace</span><span class="p">,</span>
            <span class="n">batch_size</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">batch_size</span><span class="p">,</span>
            <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">insert_kwargs</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="n">ids</span>

    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Delete nodes using with ref_doc_id.</span>

<span class="sd">        Args:</span>
<span class="sd">            ref_doc_id (str): The doc_id of the document to delete.</span>

<span class="sd">        """</span>
        <span class="c1"># delete by filtering on the doc_id metadata</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_pinecone_index</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span>
            <span class="nb">filter</span><span class="o">=</span><span class="p">{</span><span class="s2">"doc_id"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"$eq"</span><span class="p">:</span> <span class="n">ref_doc_id</span><span class="p">}},</span>
            <span class="n">namespace</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">namespace</span><span class="p">,</span>
            <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return Pinecone client."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_pinecone_index</span>

    <span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">        Query index for top k most similar nodes.</span>

<span class="sd">        Args:</span>
<span class="sd">            query_embedding (List[float]): query embedding</span>
<span class="sd">            similarity_top_k (int): top k most similar nodes</span>

<span class="sd">        """</span>
        <span class="n">sparse_vector</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="p">(</span>
            <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="ow">in</span> <span class="p">(</span><span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">SPARSE</span><span class="p">,</span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">HYBRID</span><span class="p">)</span>
            <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tokenizer</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
        <span class="p">):</span>
            <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">query_str</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"query_str must be specified if mode is SPARSE or HYBRID."</span>
                <span class="p">)</span>
            <span class="n">sparse_vector</span> <span class="o">=</span> <span class="n">generate_sparse_vectors</span><span class="p">([</span><span class="n">query</span><span class="o">.</span><span class="n">query_str</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tokenizer</span><span class="p">)[</span>
                <span class="mi">0</span>
            <span class="p">]</span>
            <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">alpha</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">sparse_vector</span> <span class="o">=</span> <span class="p">{</span>
                    <span class="s2">"indices"</span><span class="p">:</span> <span class="n">sparse_vector</span><span class="p">[</span><span class="s2">"indices"</span><span class="p">],</span>
                    <span class="s2">"values"</span><span class="p">:</span> <span class="p">[</span><span class="n">v</span> <span class="o">*</span> <span class="p">(</span><span class="mi">1</span> <span class="o">-</span> <span class="n">query</span><span class="o">.</span><span class="n">alpha</span><span class="p">)</span> <span class="k">for</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">sparse_vector</span><span class="p">[</span><span class="s2">"values"</span><span class="p">]],</span>
                <span class="p">}</span>

        <span class="c1"># pinecone requires a query embedding, so default to 0s if not provided</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">dimension</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">dimension</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_pinecone_index</span><span class="o">.</span><span class="n">describe_index_stats</span><span class="p">()[</span><span class="s2">"dimension"</span><span class="p">]</span>
        <span class="n">query_embedding</span> <span class="o">=</span> <span class="p">[</span><span class="mf">0.0</span><span class="p">]</span> <span class="o">*</span> <span class="n">dimension</span>

        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="ow">in</span> <span class="p">(</span><span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">DEFAULT</span><span class="p">,</span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">HYBRID</span><span class="p">):</span>
            <span class="n">query_embedding</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">],</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">alpha</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">query_embedding</span> <span class="o">=</span> <span class="p">[</span><span class="n">v</span> <span class="o">*</span> <span class="n">query</span><span class="o">.</span><span class="n">alpha</span> <span class="k">for</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">query_embedding</span><span class="p">]</span>

        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">if</span> <span class="s2">"filter"</span> <span class="ow">in</span> <span class="n">kwargs</span> <span class="ow">or</span> <span class="s2">"pinecone_query_filters"</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                    <span class="s2">"Cannot specify filter via both query and kwargs. "</span>
                    <span class="s2">"Use kwargs only for pinecone specific items that are "</span>
                    <span class="s2">"not supported via the generic query interface."</span>
                <span class="p">)</span>
            <span class="nb">filter</span> <span class="o">=</span> <span class="n">_to_pinecone_filter</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">)</span>
        <span class="k">elif</span> <span class="s2">"pinecone_query_filters"</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
            <span class="nb">filter</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"pinecone_query_filters"</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="nb">filter</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"filter"</span><span class="p">,</span> <span class="p">{})</span>

        <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_pinecone_index</span><span class="o">.</span><span class="n">query</span><span class="p">(</span>
            <span class="n">vector</span><span class="o">=</span><span class="n">query_embedding</span><span class="p">,</span>
            <span class="n">sparse_vector</span><span class="o">=</span><span class="n">sparse_vector</span><span class="p">,</span>
            <span class="n">top_k</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
            <span class="n">include_values</span><span class="o">=</span><span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"include_values"</span><span class="p">,</span> <span class="kc">True</span><span class="p">),</span>
            <span class="n">include_metadata</span><span class="o">=</span><span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"include_metadata"</span><span class="p">,</span> <span class="kc">True</span><span class="p">),</span>
            <span class="n">namespace</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">namespace</span><span class="p">,</span>
            <span class="nb">filter</span><span class="o">=</span><span class="nb">filter</span><span class="p">,</span>
            <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">top_k_nodes</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">top_k_ids</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">top_k_scores</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">match</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">matches</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">node</span> <span class="o">=</span> <span class="n">metadata_dict_to_node</span><span class="p">(</span><span class="n">match</span><span class="o">.</span><span class="n">metadata</span><span class="p">)</span>
                <span class="n">node</span><span class="o">.</span><span class="n">embedding</span> <span class="o">=</span> <span class="n">match</span><span class="o">.</span><span class="n">values</span>
            <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
                <span class="c1"># NOTE: deprecated legacy logic for backward compatibility</span>
                <span class="n">_logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span>
                    <span class="s2">"Failed to parse Node metadata, fallback to legacy logic."</span>
                <span class="p">)</span>
                <span class="n">metadata</span><span class="p">,</span> <span class="n">node_info</span><span class="p">,</span> <span class="n">relationships</span> <span class="o">=</span> <span class="n">legacy_metadata_dict_to_node</span><span class="p">(</span>
                    <span class="k">match</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span> <span class="n">text_key</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">text_key</span>
                <span class="p">)</span>

                <span class="n">text</span> <span class="o">=</span> <span class="n">match</span><span class="o">.</span><span class="n">metadata</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">text_key</span><span class="p">]</span>
                <span class="nb">id</span> <span class="o">=</span> <span class="n">match</span><span class="o">.</span><span class="n">id</span>
                <span class="n">node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span>
                    <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
                    <span class="n">id_</span><span class="o">=</span><span class="nb">id</span><span class="p">,</span>
                    <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
                    <span class="n">start_char_idx</span><span class="o">=</span><span class="n">node_info</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"start"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                    <span class="n">end_char_idx</span><span class="o">=</span><span class="n">node_info</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"end"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                    <span class="n">relationships</span><span class="o">=</span><span class="n">relationships</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="n">top_k_ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">match</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
            <span class="n">top_k_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
            <span class="n">top_k_scores</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">match</span><span class="o">.</span><span class="n">score</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span>
            <span class="n">nodes</span><span class="o">=</span><span class="n">top_k_nodes</span><span class="p">,</span> <span class="n">similarities</span><span class="o">=</span><span class="n">top_k_scores</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">top_k_ids</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### client `property` [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/pinecone/#llama_index.vector_stores.pinecone.PineconeVectorStore.client "Permanent link")

```
client: Any
```

Return Pinecone client.

### add [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/pinecone/#llama_index.vector_stores.pinecone.PineconeVectorStore.add "Permanent link")

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

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-pinecone/llama_index/vector_stores/pinecone/base.py`

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
<span class="normal">393</span>
<span class="normal">394</span>
<span class="normal">395</span>
<span class="normal">396</span>
<span class="normal">397</span>
<span class="normal">398</span>
<span class="normal">399</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">add</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">nodes</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">],</span>
    <span class="o">**</span><span class="n">add_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Add nodes to index.</span>

<span class="sd">    Args:</span>
<span class="sd">        nodes: List[BaseNode]: list of nodes with embeddings</span>

<span class="sd">    """</span>
    <span class="n">ids</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">entries</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
        <span class="n">node_id</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">node_id</span>

        <span class="n">metadata</span> <span class="o">=</span> <span class="n">node_to_metadata_dict</span><span class="p">(</span>
            <span class="n">node</span><span class="p">,</span>
            <span class="n">remove_text</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">remove_text_from_metadata</span><span class="p">,</span>
            <span class="n">flat_metadata</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">flat_metadata</span><span class="p">,</span>
        <span class="p">)</span>

        <span class="n">entry</span> <span class="o">=</span> <span class="p">{</span>
            <span class="n">ID_KEY</span><span class="p">:</span> <span class="n">node_id</span><span class="p">,</span>
            <span class="n">VECTOR_KEY</span><span class="p">:</span> <span class="n">node</span><span class="o">.</span><span class="n">get_embedding</span><span class="p">(),</span>
            <span class="n">METADATA_KEY</span><span class="p">:</span> <span class="n">metadata</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">add_sparse_vector</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tokenizer</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">sparse_vector</span> <span class="o">=</span> <span class="n">generate_sparse_vectors</span><span class="p">(</span>
                <span class="p">[</span><span class="n">node</span><span class="o">.</span><span class="n">get_content</span><span class="p">(</span><span class="n">metadata_mode</span><span class="o">=</span><span class="n">MetadataMode</span><span class="o">.</span><span class="n">EMBED</span><span class="p">)],</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_tokenizer</span><span class="p">,</span>
            <span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
            <span class="n">entry</span><span class="p">[</span><span class="n">SPARSE_VECTOR_KEY</span><span class="p">]</span> <span class="o">=</span> <span class="n">sparse_vector</span>

        <span class="n">ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node_id</span><span class="p">)</span>
        <span class="n">entries</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">entry</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_pinecone_index</span><span class="o">.</span><span class="n">upsert</span><span class="p">(</span>
        <span class="n">entries</span><span class="p">,</span>
        <span class="n">namespace</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">namespace</span><span class="p">,</span>
        <span class="n">batch_size</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">batch_size</span><span class="p">,</span>
        <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">insert_kwargs</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="n">ids</span>
</code></pre></div></td></tr></tbody></table>

### delete [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/pinecone/#llama_index.vector_stores.pinecone.PineconeVectorStore.delete "Permanent link")

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

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-pinecone/llama_index/vector_stores/pinecone/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">401</span>
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
<span class="normal">414</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ref_doc_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Delete nodes using with ref_doc_id.</span>

<span class="sd">    Args:</span>
<span class="sd">        ref_doc_id (str): The doc_id of the document to delete.</span>

<span class="sd">    """</span>
    <span class="c1"># delete by filtering on the doc_id metadata</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_pinecone_index</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span>
        <span class="nb">filter</span><span class="o">=</span><span class="p">{</span><span class="s2">"doc_id"</span><span class="p">:</span> <span class="p">{</span><span class="s2">"$eq"</span><span class="p">:</span> <span class="n">ref_doc_id</span><span class="p">}},</span>
        <span class="n">namespace</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">namespace</span><span class="p">,</span>
        <span class="o">**</span><span class="n">delete_kwargs</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

### query [#](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/pinecone/#llama_index.vector_stores.pinecone.PineconeVectorStore.query "Permanent link")

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

Source code in `llama-index-integrations/vector_stores/llama-index-vector-stores-pinecone/llama_index/vector_stores/pinecone/base.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">421</span>
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
<span class="normal">516</span></pre></div></td><td class="code"><div><pre><span></span><code><span class="k">def</span> <span class="nf">query</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="n">VectorStoreQuery</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VectorStoreQueryResult</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""</span>
<span class="sd">    Query index for top k most similar nodes.</span>

<span class="sd">    Args:</span>
<span class="sd">        query_embedding (List[float]): query embedding</span>
<span class="sd">        similarity_top_k (int): top k most similar nodes</span>

<span class="sd">    """</span>
    <span class="n">sparse_vector</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="k">if</span> <span class="p">(</span>
        <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="ow">in</span> <span class="p">(</span><span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">SPARSE</span><span class="p">,</span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">HYBRID</span><span class="p">)</span>
        <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tokenizer</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
    <span class="p">):</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">query_str</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"query_str must be specified if mode is SPARSE or HYBRID."</span>
            <span class="p">)</span>
        <span class="n">sparse_vector</span> <span class="o">=</span> <span class="n">generate_sparse_vectors</span><span class="p">([</span><span class="n">query</span><span class="o">.</span><span class="n">query_str</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tokenizer</span><span class="p">)[</span>
            <span class="mi">0</span>
        <span class="p">]</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">alpha</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">sparse_vector</span> <span class="o">=</span> <span class="p">{</span>
                <span class="s2">"indices"</span><span class="p">:</span> <span class="n">sparse_vector</span><span class="p">[</span><span class="s2">"indices"</span><span class="p">],</span>
                <span class="s2">"values"</span><span class="p">:</span> <span class="p">[</span><span class="n">v</span> <span class="o">*</span> <span class="p">(</span><span class="mi">1</span> <span class="o">-</span> <span class="n">query</span><span class="o">.</span><span class="n">alpha</span><span class="p">)</span> <span class="k">for</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">sparse_vector</span><span class="p">[</span><span class="s2">"values"</span><span class="p">]],</span>
            <span class="p">}</span>

    <span class="c1"># pinecone requires a query embedding, so default to 0s if not provided</span>
    <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">dimension</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">dimension</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_pinecone_index</span><span class="o">.</span><span class="n">describe_index_stats</span><span class="p">()[</span><span class="s2">"dimension"</span><span class="p">]</span>
    <span class="n">query_embedding</span> <span class="o">=</span> <span class="p">[</span><span class="mf">0.0</span><span class="p">]</span> <span class="o">*</span> <span class="n">dimension</span>

    <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">mode</span> <span class="ow">in</span> <span class="p">(</span><span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">DEFAULT</span><span class="p">,</span> <span class="n">VectorStoreQueryMode</span><span class="o">.</span><span class="n">HYBRID</span><span class="p">):</span>
        <span class="n">query_embedding</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">],</span> <span class="n">query</span><span class="o">.</span><span class="n">query_embedding</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">alpha</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">query_embedding</span> <span class="o">=</span> <span class="p">[</span><span class="n">v</span> <span class="o">*</span> <span class="n">query</span><span class="o">.</span><span class="n">alpha</span> <span class="k">for</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">query_embedding</span><span class="p">]</span>

    <span class="k">if</span> <span class="n">query</span><span class="o">.</span><span class="n">filters</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="s2">"filter"</span> <span class="ow">in</span> <span class="n">kwargs</span> <span class="ow">or</span> <span class="s2">"pinecone_query_filters"</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
                <span class="s2">"Cannot specify filter via both query and kwargs. "</span>
                <span class="s2">"Use kwargs only for pinecone specific items that are "</span>
                <span class="s2">"not supported via the generic query interface."</span>
            <span class="p">)</span>
        <span class="nb">filter</span> <span class="o">=</span> <span class="n">_to_pinecone_filter</span><span class="p">(</span><span class="n">query</span><span class="o">.</span><span class="n">filters</span><span class="p">)</span>
    <span class="k">elif</span> <span class="s2">"pinecone_query_filters"</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
        <span class="nb">filter</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"pinecone_query_filters"</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="nb">filter</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"filter"</span><span class="p">,</span> <span class="p">{})</span>

    <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_pinecone_index</span><span class="o">.</span><span class="n">query</span><span class="p">(</span>
        <span class="n">vector</span><span class="o">=</span><span class="n">query_embedding</span><span class="p">,</span>
        <span class="n">sparse_vector</span><span class="o">=</span><span class="n">sparse_vector</span><span class="p">,</span>
        <span class="n">top_k</span><span class="o">=</span><span class="n">query</span><span class="o">.</span><span class="n">similarity_top_k</span><span class="p">,</span>
        <span class="n">include_values</span><span class="o">=</span><span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"include_values"</span><span class="p">,</span> <span class="kc">True</span><span class="p">),</span>
        <span class="n">include_metadata</span><span class="o">=</span><span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s2">"include_metadata"</span><span class="p">,</span> <span class="kc">True</span><span class="p">),</span>
        <span class="n">namespace</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">namespace</span><span class="p">,</span>
        <span class="nb">filter</span><span class="o">=</span><span class="nb">filter</span><span class="p">,</span>
        <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span>
    <span class="p">)</span>

    <span class="n">top_k_nodes</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">top_k_ids</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">top_k_scores</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">match</span> <span class="ow">in</span> <span class="n">response</span><span class="o">.</span><span class="n">matches</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">metadata_dict_to_node</span><span class="p">(</span><span class="n">match</span><span class="o">.</span><span class="n">metadata</span><span class="p">)</span>
            <span class="n">node</span><span class="o">.</span><span class="n">embedding</span> <span class="o">=</span> <span class="n">match</span><span class="o">.</span><span class="n">values</span>
        <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
            <span class="c1"># NOTE: deprecated legacy logic for backward compatibility</span>
            <span class="n">_logger</span><span class="o">.</span><span class="n">debug</span><span class="p">(</span>
                <span class="s2">"Failed to parse Node metadata, fallback to legacy logic."</span>
            <span class="p">)</span>
            <span class="n">metadata</span><span class="p">,</span> <span class="n">node_info</span><span class="p">,</span> <span class="n">relationships</span> <span class="o">=</span> <span class="n">legacy_metadata_dict_to_node</span><span class="p">(</span>
                <span class="k">match</span><span class="o">.</span><span class="n">metadata</span><span class="p">,</span> <span class="n">text_key</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">text_key</span>
            <span class="p">)</span>

            <span class="n">text</span> <span class="o">=</span> <span class="n">match</span><span class="o">.</span><span class="n">metadata</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">text_key</span><span class="p">]</span>
            <span class="nb">id</span> <span class="o">=</span> <span class="n">match</span><span class="o">.</span><span class="n">id</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">TextNode</span><span class="p">(</span>
                <span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span>
                <span class="n">id_</span><span class="o">=</span><span class="nb">id</span><span class="p">,</span>
                <span class="n">metadata</span><span class="o">=</span><span class="n">metadata</span><span class="p">,</span>
                <span class="n">start_char_idx</span><span class="o">=</span><span class="n">node_info</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"start"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                <span class="n">end_char_idx</span><span class="o">=</span><span class="n">node_info</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">"end"</span><span class="p">,</span> <span class="kc">None</span><span class="p">),</span>
                <span class="n">relationships</span><span class="o">=</span><span class="n">relationships</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="n">top_k_ids</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">match</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
        <span class="n">top_k_nodes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
        <span class="n">top_k_scores</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">match</span><span class="o">.</span><span class="n">score</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">VectorStoreQueryResult</span><span class="p">(</span>
        <span class="n">nodes</span><span class="o">=</span><span class="n">top_k_nodes</span><span class="p">,</span> <span class="n">similarities</span><span class="o">=</span><span class="n">top_k_scores</span><span class="p">,</span> <span class="n">ids</span><span class="o">=</span><span class="n">top_k_ids</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table>

Back to top

[Previous Pgvecto rs](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/pgvecto_rs/)[Next Postgres](https://docs.llamaindex.ai/en/stable/api_reference/storage/vector_store/postgres/)
